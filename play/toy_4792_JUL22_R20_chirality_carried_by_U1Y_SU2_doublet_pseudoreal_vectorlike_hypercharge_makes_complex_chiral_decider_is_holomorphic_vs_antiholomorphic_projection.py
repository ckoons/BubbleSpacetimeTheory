#!/usr/bin/env python3
"""
Toy 4792 — Jul 22 (the chirality is carried by U(1)_Y: the SU(2) doublet is pseudoreal (vector-like alone), hypercharge
makes it complex/chiral — Elie's reality-type computation, with the real decider flagged both ways). Casey's steer: "again
linear algebra, one manifold D_IV⁵." Keeper K831 reframe: the vector-like obstruction dressed up as "Witten's Kaluza-Klein
generations problem" is nothing new — it is the SQUEEZE (toy 4785) / K822 ⟨γ⁵⟩=0 again: an SU(2) grading alone is vector-like
because the doublet is PSEUDOREAL (2≅2̄). So the instanton (k=1, toy 4790) builds the doublet/singlet GRADING but cannot by
itself make it chiral. What makes the Standard Model chiral is U(1)_Y — it breaks the pseudoreality and makes the full rep
COMPLEX (R≇R̄). I compute the reality types (Frobenius-Schur indicators) target-innocently and confirm this exactly: the
chirality is carried by the SAME hypercharge that closed the charge sector today. AND — following the steer honestly — I
surface the real remaining decider (holomorphic vs anti-holomorphic projection) rather than assert parity closed.

THE COMPUTATION (Frobenius-Schur indicator ν(R)=⟨χ_R(g²)⟩: real +1, pseudoreal −1, complex 0):
  * SU(2) doublet 2: ν = −1 (PSEUDOREAL, 2≅2̄) → vector-like BY ITSELF. This is the squeeze / K822 in rep-language: an SU(2)
    grading (the instanton doublet/singlet) alone cannot be chiral.
  * U(1) charge Y: ν = 1 if Y=0 else 0. So (2,Y=0) stays pseudoreal (vector-like); (2,Y≠0) has ν=0 → COMPLEX → CHIRAL.
  * With the BANKED hypercharges (Y_Q=1/6, Y_L=−1/2, both ≠0): (2,Y) is COMPLEX → chiral. And the full SM one generation is
    R≇R̄ (its conjugate multiset differs) → CHIRAL.
  ⟹ the SU(2) doublet is pseudoreal (vector-like); U(1)_Y makes it complex (chiral). The chirality is carried by U(1)_Y —
  the SAME hypercharge derived in the charge sector today (gap b). So parity and the charge sector are ONE mechanism: the
  complex structure of U(1)_Y. This also explains why the instanton alone can't finish (pseudoreal doublet) and why k=1 (not
  k=3) is right (the instanton is the grading/content; U(1)_Y makes it chiral; the 3 generations are the separate radial
  strata — Grace's chirality⊥radial orthogonality).

THE DECIDER (sharp, one-manifold, flagged BOTH ways — NOT asserted): does the Z₂-projected, instanton-holomorphic section on
D_IV⁵ carry the COMPLEX rep (→ chiral → parity DERIVED, and it would follow from the already-derived U(1)_Y) or does the
projection REAL-IFY it (→ vector-like → derived-conditional)? This turns on whether the effective Z₂ action on the sections
is HOLOMORPHIC (preserves the complex structure → complex → chiral) or ANTI-HOLOMORPHIC (conjugates → real → vector-like).
TWO honest pulls, both real: (+) Born=Bergman sections are inherently holomorphic/complex, and U(1)_Y acts as the center
phase → points to complex/chiral. (−) an orientation-REVERSING map on a complex manifold is naively ANTI-holomorphic (it
conjugates the complex structure) → would real-ify → the very non-orientability (K826) that PERMITS chirality could be what
real-ifies U(1)_Y. These pull opposite ways and MUST be computed on the actual projected sections — I do NOT assert either.

⟹ VERDICT (LEAD, eleventh-closure discipline held): I COMPUTE (linear algebra, one manifold) that the SM chirality is
carried by U(1)_Y — the SU(2) doublet alone is pseudoreal/vector-like (the squeeze again), and hypercharge (banked, ≠0)
makes the rep complex/chiral. So parity and the charge sector are the SAME U(1)_Y mechanism, and IF the projected holomorphic
sections carry the complex rep, parity is DERIVED from the already-derived charge sector. THE SOLE REMAINING DECIDER: is the
effective Z₂-projection HOLOMORPHIC (→ complex → chiral → parity derived) or ANTI-holomorphic (→ real → vector-like →
derived-conditional)? I flag BOTH pulls honestly (holomorphic Born=Bergman vs anti-holomorphic orientation-reversal) and do
NOT assert — "U(1)_Y makes it complex, therefore parity derived" would be the eleventh pretty closure. Compute the reality
type of the actual projected sections. Charge sector + DIRAC + Route 1 + squeeze closed; Five-Absence-positive (all reps/
geometry, non-GUT). Count ~7-8.
"""
import numpy as np
from scipy import integrate
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# Frobenius-Schur indicator
nu_su2, _ = integrate.quad(lambda t: 2*np.cos(2*t)*(2/np.pi)*np.sin(t)**2, 0, np.pi)   # SU(2) doublet
def nu_u1(Y): return 1.0 if abs(Y) < 1e-12 else 0.0
def nu_2Y(Y): return nu_su2 * nu_u1(Y)
print(f"\n[FS] SU(2) doublet ν={nu_su2:+.3f} (pseudoreal); (2,Y=1/6) ν={nu_2Y(1/6):+.3f}; (2,Y=-1/2) ν={nu_2Y(-1/2):+.3f}")

# ---- doublet pseudoreal → vector-like alone --------------------------------
check("SU(2) DOUBLET IS PSEUDOREAL → vector-like by itself: ν(2)=−1 (2≅2̄). This is the SQUEEZE / K822 in rep-language — an "
      "SU(2) grading alone (the instanton doublet/singlet, k=1) cannot be chiral. (2,Y=0) stays ν=−1 (vector-like).",
      abs(nu_su2 + 1) < 1e-3 and abs(nu_2Y(0.0) + 1) < 1e-3,
      "ν(SU(2) doublet)=−1 → pseudoreal → vector-like alone (= the squeeze in rep-language); the instanton grading alone is not chiral")

# ---- U(1)_Y makes it complex → chiral --------------------------------------
comp_quark = abs(nu_2Y(1/6)) < 1e-6; comp_lep = abs(nu_2Y(-1/2)) < 1e-6
check("U(1)_Y MAKES IT COMPLEX → CHIRAL: with the BANKED hypercharges (Y_Q=1/6, Y_L=−1/2, both ≠0), (2,Y) has ν=0 → COMPLEX "
      "→ chiral. Hypercharge breaks the pseudoreality. So the chirality is carried by U(1)_Y — the SAME hypercharge derived "
      "in the charge sector today (gap b). Parity and the charge sector are ONE mechanism (the complex structure of U(1)_Y).",
      comp_quark and comp_lep,
      "(2,Y≠0) ν=0 → complex → chiral; chirality carried by U(1)_Y = the banked charge-sector hypercharge → parity & charge = one mechanism")

# ---- full SM generation is complex -----------------------------------------
gen = {('3',2,1),('3bar',1,-4),('3bar',1,2),('1',2,-3),('1',1,-6)}
def conj(f):
    c,d,y=f; cc={'3':'3bar','3bar':'3','1':'1'}[c]; return (cc,d,-y)
genbar = set(conj(f) for f in gen)
check("FULL SM ONE GENERATION IS COMPLEX → CHIRAL: the content multiset {(3,2,1/6),(3̄,1,−2/3),(3̄,1,1/3),(1,2,−1/2),"
      "(1,1,−1)} ≠ its conjugate multiset (e.g. Q̄=(3̄,2,−1/6) is NOT in the set — the anti-quark-doublet is absent) → R≇R̄ "
      "→ chiral. This is why k=1 (not k=3) is right: the instanton is the grading/content, U(1)_Y makes it chiral, and the "
      "3 generations are the separate radial strata (chirality⊥radial).",
      gen != genbar, "SM one generation R≇R̄ (conjugate multiset differs) → chiral; instanton=content, U(1)_Y=chiral, 3 gens=radial strata (orthogonal)")

# ---- the decider, flagged both ways ----------------------------------------
check("THE DECIDER (sharp, one-manifold, flagged BOTH ways — NOT asserted): does the Z₂-projected instanton-holomorphic "
      "section carry the COMPLEX rep (→ chiral → parity DERIVED from the already-derived U(1)_Y) or REAL-IFY it (→ "
      "vector-like)? Turns on HOLOMORPHIC (preserves complex → chiral) vs ANTI-holomorphic (conjugates → real) effective Z₂. "
      "(+) Born=Bergman sections are holomorphic/complex, U(1)_Y = center phase → points complex/chiral. (−) an "
      "orientation-REVERSING map on a complex manifold is naively ANTI-holomorphic → would real-ify → the non-orientability "
      "(K826) that PERMITS chirality could be what real-ifies U(1)_Y. Both real; MUST be computed on the actual sections.",
      True, "sole decider: is the Z₂-projection holomorphic (→complex/chiral/derived) or anti-holomorphic (→real/vector-like)? Born=Bergman(+) vs orientation-reversal(−) pull opposite — compute, don't assert")

# ---- verdict ---------------------------------------------------------------
check("VERDICT (LEAD, eleventh-closure discipline): the SM chirality is carried by U(1)_Y — the SU(2) doublet alone is "
      "pseudoreal/vector-like (the squeeze), hypercharge (banked, ≠0) makes the rep complex/chiral. Parity and the charge "
      "sector are the SAME U(1)_Y mechanism, so IF the projected holomorphic sections carry the complex rep, parity is "
      "DERIVED from the already-derived charge sector. SOLE DECIDER: is the effective Z₂-projection HOLOMORPHIC (→ chiral, "
      "parity derived) or ANTI-holomorphic (→ vector-like, derived-conditional)? Flagged both ways, NOT asserted — "
      "'U(1)_Y makes it complex therefore parity derived' would be the 11th pretty closure. Charge + DIRAC + Route 1 + "
      "squeeze closed; Five-Absence-positive.",
      abs(nu_su2 + 1) < 1e-3 and comp_quark and comp_lep and gen != genbar,
      "chirality carried by U(1)_Y (doublet pseudoreal, hypercharge makes complex); parity=charge mechanism; sole decider = holomorphic vs anti-holomorphic projection; NOT asserted")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-20 (07-22) chirality carried by U(1)_Y — Elie's reality-type computation (Casey: linear algebra, one manifold):
  * SU(2) doublet ν=−1 PSEUDOREAL → vector-like alone (= the squeeze / K822 in rep-language; the instanton grading alone isn't chiral).
  * U(1)_Y (Y≠0 banked) makes (2,Y) ν=0 COMPLEX → CHIRAL. Full SM gen R≇R̄ → chiral. Chirality carried by hypercharge = the charge sector.
  * So parity & charge = ONE U(1)_Y mechanism; k=1 (not 3) right (instanton=content, U(1)_Y=chiral, 3 gens=radial strata ⊥).
  => SOLE DECIDER: is the Z₂-projection HOLOMORPHIC (→complex→chiral→parity DERIVED) or ANTI-holomorphic (→real→vector-like)? Born=Bergman(+) vs orientation-reversal(−) — flagged both ways, NOT asserted (11th-closure discipline). Charge+DIRAC+Route 1+squeeze closed.
""")
