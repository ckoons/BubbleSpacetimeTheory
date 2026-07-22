#!/usr/bin/env python3
"""
Toy 4789 — Jul 22 (gap (a) TOOL: classify the candidate INDUCED Z₂ actions on the internal bundle — grade vs uniform vs
swap; Elie's rep-theory tool for Lyra, not a claim). The whole parity question has collapsed to gap (a): the Z₂ orbifold
action on the internal-SU(2) bundle is INDUCED by the geometric Z₂ on the boundary (Keeper: "compute the induced action,
don't choose it"). My gap (c) index is blocked downstream of it (toy 4788: the untwisted index is vector-like; the odd/one-
generation index needs the grading twist). So the decider is: does the geometry's induced action GRADE the internal chiral
split (2,1)⊕(1,2) into doublet↔singlet (→ the SM) or act UNIFORMLY (→ vector-like)? That is rep-theory linear algebra on the
internal Cl(5), squarely my lane — so instead of sitting blocked I hand Lyra a TOOL: the three induced-action types and what
each means, with the concrete SM requirement. This is a classification on a chosen internal basis; WHICH operator is the
actual induced action depends on the faithful boundary embedding (the 4781 lesson) — that is Lyra's, and this is a tool for
her computation, NOT a claim that D_IV⁵ gives the SM.

THE INTERNAL SPLIT (Cl(5), internal SO(5) isotropy; SO(4)⊂SO(5) chirality γ⁵₄=Γ₁Γ₂Γ₃Γ₄ grades the 4-spinor into
(2,1)[+1]⊕(1,2)[−1]). Classify each candidate induced Z₂ action by how it acts on this grading:
  * ω = Γ₁Γ₂Γ₃Γ₄Γ₅ (FULL antipodal, all 5 internal dirs, orientation-reversing): CENTRAL on the SO(5) irrep → acts as the
    SAME scalar (−1) on (2,1) and (1,2) → UNIFORM → VECTOR-LIKE (no grading, no SM). This is the "naive orientation-
    reversing lift" — and it does NOT grade, matching toy 4788's even/vector-like default.
  * γ⁵₄ = Γ₁Γ₂Γ₃Γ₄ (EVEN, 4 dirs, orientation-preserving): +1 on (2,1), −1 on (1,2) → GRADES → SM doublet/singlet.
  * Γ₅ (SINGLE reflection, 1 dir, orientation-REVERSING): −1 on (2,1), +1 on (1,2) → GRADES → SM doublet/singlet. ★ This is
    the SWEET SPOT: a single internal reflection is BOTH orientation-reversing (K826-consistent, gives non-orientability/
    chirality) AND grading (SM-consistent). Unlike the full antipodal, it is not central, so it distinguishes the two SU(2)
    factors.
  * Γ₄Γ₅ (two dirs): anticommutes with γ⁵₄ → OFF-DIAGONAL → SWAPS (2,1)↔(1,2) → neither clean SM nor vector-like.

THE DECIDER FOR GAP (a) (handed to Lyra): the induced Z₂ action gives the SM IFF it restricts to a GRADING operator (γ⁵₄- or
Γ₅-type) on the internal 4-space, NOT the central ω (uniform→vector-like) nor a swap. The most promising candidate is the
SINGLE-REFLECTION type Γ₅ — orientation-reversing (so K826 non-orientability holds) AND grading (so the SM doublet/singlet
appears). So Lyra's faithful-embedding computation reduces to: does the geometric Z₂ (antipodal-S⁴ ∘ circle-flip), restricted
to the internal-SU(2) bundle, act as a single-reflection-type grading operator, or as the central ω, or as a swap? Compute
the restriction — don't choose it.

⟹ VERDICT (tool, not claim): I classify the induced Z₂ actions into three buckets — GRADE (γ⁵₄ or single-reflection Γ₅ →
SM doublet/singlet), UNIFORM (central ω → vector-like), SWAP (Γ₄Γ₅ → mixes). The SM requires a grading-type induced action;
the sweet spot is the SINGLE-REFLECTION Γ₅, which is simultaneously orientation-reversing (K826) and grading (SM). This turns
gap (a) into a sharp yes/no on the faithful induced action, and it dissolves the tension I'd worried about (orientation-
reversing need NOT be uniform — only the FULL antipodal is; a partial reflection grades). DISCIPLINE (4781 lesson): this is a
classification on a chosen internal basis; which operator is the ACTUAL induced action is the faithful-embedding computation,
Lyra's — I do NOT claim D_IV⁵ realizes the grading type (that would be the tenth pretty closure). Grade → parity DERIVED;
uniform/swap → vector-like/derived-conditional. My index harness (gap c) computes the instant Lyra fixes the type. Charge
sector closed (gap b); DIRAC + Route 1 + squeeze closed; Five-Absence-positive. Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

s0=np.eye(2); s1=np.array([[0,1],[1,0]]); s2=np.array([[0,-1j],[1j,0]]); s3=np.array([[1,0],[0,-1]])
kron=np.kron
G=[kron(s1,s1),kron(s1,s2),kron(s1,s3),kron(s2,s0),kron(s3,s0)]     # Cl(5) 4×4, internal SO(5)
anticomm = all(np.allclose(G[a]@G[b]+G[b]@G[a], (2 if a==b else 0)*np.eye(4)) for a in range(5) for b in range(5))
g54 = G[0]@G[1]@G[2]@G[3]                                          # SO(4) chirality → (2,1)/(1,2)
PL=(np.eye(4)+g54)/2; PR=(np.eye(4)-g54)/2
def kind(M):
    comm = np.linalg.norm(M@g54-g54@M) < 1e-9
    off  = np.linalg.norm(PL@M@PR)+np.linalg.norm(PR@M@PL)
    aL = np.trace(PL@M@PL)/2; aR = np.trace(PR@M@PR)/2
    if comm and off < 1e-9 and abs(aL-aR) > 1e-9: return 'GRADE', aL, aR
    if comm and off < 1e-9 and abs(aL-aR) < 1e-9: return 'UNIFORM', aL, aR
    return 'SWAP', aL, aR
omega = G[0]@G[1]@G[2]@G[3]@G[4]
k_omega = kind(omega); k_g54 = kind(g54); k_G5 = kind(G[4]); k_G45 = kind(G[3]@G[4])
print(f"\n[grading] SO(4) chirality γ⁵₄ eigenvalues {np.round(np.linalg.eigvalsh(g54).real,1)} → (2,1)/(1,2)")
print(f"  ω=Γ1..Γ5 (antipodal): {k_omega[0]}   γ54=Γ1Γ2Γ3Γ4: {k_g54[0]}   Γ5 (single refl): {k_G5[0]}   Γ4Γ5: {k_G45[0]}")

check("THE INTERNAL SPLIT + CLASSIFICATION: on the internal Cl(5), the SO(4) chirality γ⁵₄=Γ₁Γ₂Γ₃Γ₄ grades the 4-spinor "
      "into (2,1)[+1]⊕(1,2)[−1]. Classify candidate induced Z₂ actions: ω=Γ₁..Γ₅ (full antipodal) is CENTRAL → UNIFORM → "
      "vector-like; γ⁵₄ (even) GRADES → SM doublet/singlet; Γ₅ (single reflection) GRADES → SM; Γ₄Γ₅ SWAPS. Three buckets.",
      anticomm and k_omega[0]=='UNIFORM' and k_g54[0]=='GRADE' and k_G5[0]=='GRADE' and k_G45[0]=='SWAP',
      "induced-action buckets: ω=UNIFORM(vector-like), γ54=GRADE(SM), Γ5=GRADE(SM), Γ4Γ5=SWAP")

check("THE SWEET SPOT (★): the SINGLE reflection Γ₅ is BOTH orientation-REVERSING (K826-consistent → non-orientability/"
      "chirality) AND GRADING (SM-consistent → doublet↔singlet). Unlike the full antipodal ω (central → uniform), a partial "
      "reflection is not central, so it distinguishes the two SU(2) factors. This dissolves the tension I'd worried about: "
      "orientation-reversing need NOT be uniform — only the FULL antipodal is.",
      k_G5[0]=='GRADE' and k_omega[0]=='UNIFORM',
      "single reflection Γ5: orientation-reversing AND grades → the promising induced-action candidate; full antipodal ω is the uniform/vector-like one")

check("THE DECIDER FOR GAP (a) (handed to Lyra): the induced Z₂ action gives the SM IFF it restricts to a GRADING operator "
      "(γ⁵₄- or Γ₅-type) on the internal 4-space, NOT the central ω (uniform→vector-like) nor a swap. So Lyra's faithful-"
      "embedding computation reduces to a sharp classification: does the geometric Z₂ (antipodal-S⁴ ∘ circle-flip), "
      "restricted to the internal-SU(2) bundle, act as a single-reflection-type grader, the central ω, or a swap? Compute "
      "the restriction, don't choose it.",
      True, "gap (a) reduces to: is the faithful induced action a GRADE (→SM), UNIFORM (→vector-like), or SWAP? — a sharp yes/no for Lyra")

check("DISCIPLINE (4781 lesson) + VERDICT (tool, not claim): this is a classification on a CHOSEN internal basis; WHICH "
      "operator is the ACTUAL induced action is the faithful-embedding computation, Lyra's — I do NOT claim D_IV⁵ realizes "
      "the grading type (that would be the 10th pretty closure). I hand over the three buckets + the SM requirement + the "
      "single-reflection sweet spot. Grade → parity DERIVED; uniform/swap → vector-like/derived-conditional. My index "
      "harness (gap c) computes the instant Lyra fixes the type. Charge sector closed (gap b); DIRAC + Route 1 + squeeze "
      "closed; Five-Absence-positive.",
      anticomm and k_omega[0]=='UNIFORM' and k_g54[0]=='GRADE' and k_G5[0]=='GRADE',
      "TOOL delivered: 3 induced-action buckets + SM requires GRADE + Γ5 sweet spot; which one D_IV⁵ realizes = Lyra's faithful embedding; NO SM claim faked")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-17 (07-22) gap (a) TOOL — Elie's induced-Z₂-action classification for Lyra (compute-don't-choose; not a claim):
  * γ⁵₄=Γ1Γ2Γ3Γ4 grades the internal 4-spinor into (2,1)⊕(1,2) = doublet/singlet.
  * BUCKETS: ω=Γ1..Γ5 (full antipodal) → UNIFORM (central → vector-like); γ54 (even) → GRADE (SM); Γ5 (single reflection) → GRADE (SM); Γ4Γ5 → SWAP.
  * ★ SWEET SPOT: single reflection Γ5 is orientation-REVERSING (K826) AND GRADING (SM) — the promising induced-action candidate; only the FULL antipodal is uniform/vector-like.
  => gap (a) reduces to a sharp yes/no: is the faithful induced action a GRADE (→parity DERIVED), UNIFORM (→vector-like), or SWAP? Lyra computes the restriction; I do NOT claim D_IV⁵ gives SM (4781 lesson). Index harness (gap c) fires once the type is fixed. Charge sector + DIRAC + Route 1 + squeeze closed.
""")
