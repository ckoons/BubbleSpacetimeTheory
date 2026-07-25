#!/usr/bin/env python3
"""
Toy 4857 — Jul 25 (R10, reconcile "CP-exists derived" (my 4854) with banked F498; Keeper K907 audit hold task #9, mine).
Keeper HELD my 4854 "CP violation is derived because D_IV⁵ is a complex domain" against banked F498, which PROVES J=0
identically for REAL generation localizations and gates CP-existence on the generation STATES being genuinely complex
(not just the ambient domain). This toy isolates EXACTLY where the complex phase enters, using the ACTUAL BST
generation-state build (reproducing-kernel Gram of localizations z_k), not the generic random complex-Hermitian matrices
my 4854 used. The question: does today's argument make the generation STATES complex (→ closes the gate, CP derived) or
only use the DOMAIN's complex structure (→ F498-insufficient, CP candidate)?

THE FOUR CONTROLLED CASES (reproducing kernel K(z_i,z_j)=1/(1 - <z_i,z_j>)^{n_C}, the D_IV⁵ complex-analytic kernel;
diagonalize each sector's Gram, V = U_up† U_down, Jarlskog J = Im(V00 V11 V01* V10*)):
  A. REAL radial localizations z_k = r_k (the natural KW radial model, F491/F498): kernel is COMPLEX-ANALYTIC but the
     SAMPLE POINTS are real → Gram is REAL symmetric → real orthogonal U → real CKM → J = 0. THE DOMAIN IS COMPLEX AND
     J STILL VANISHES. This is F498, and it is the direct refutation of "domain complex → CP."
  B. My 4854 model — generic random complex-Hermitian sector operators: J ≠ 0. But the complex phase is INSERTED by the
     randn imaginary part; it is NOT the Gram of any radial state. This is "assume the states are complex," i.e. the
     F498-insufficient argument dressed as a domain fact.
  C. ℤ₃-phased localizations z_k = r_k·ω^{k−1}, ω=e^{2πi/3} (the 4656/4685 build, Casey's phase-advancing commits) WITH
     the mass hierarchy (distinct r_k): J ≠ 0. CP is forced — but ONLY because the STATES carry the ω phase.
  D. Same ℤ₃ phases but EQUAL radii (exact ℤ₃, no hierarchy): circulant Gram → same DFT diagonalizes both sectors →
     V trivial → J = 0. And the rephasing-invariance check: the ω phase is PHYSICAL (non-removable) only once the
     hierarchy breaks the circulant.

WHAT THIS SETTLES:
  * The complex DOMAIN (complex-analytic kernel, exponent n_C) is present in ALL FOUR cases. J is zero in A and D and
    nonzero in B and C. So the domain being complex is NOT the cause of J≠0 — the STATE PHASE is. F498 is exactly right.
  * My 4854 "D_IV⁵ complex → J≠0" RE-ASSERTS domain-complex: case B injects the phase via random complex entries; case A
    (the real states that D_IV⁵'s natural radial model actually gives) has the same complex domain and J=0. My argument
    used the insufficient premise. RETRACT stands (4855): CP-exists → CANDIDATE.
  * The gate F498 set is UNCHANGED and UNMET: CP-existence ⟺ the generation localizations carry a genuine non-removable
    complex phase (the ω^{k−1}/ℤ₃ phase, case C). Whether N_c=3 FORCES that phase onto the states — vs. the generations
    being the LINEAR Korányi–Wolf strata {0⊂2⊂5} at real radial positions (F495) → case A → J=0 — is NOT derived. The
    ℤ₃ phase is ASSUMED in 4656/4685, and that assumption IS the open Engine-B gate. F498's own verdict ("the build is
    the decider; can fail") stands.

⟹ VERDICT (straight to Keeper): today's argument RE-ASSERTS "domain complex." It does NOT close F498's gate. A complex
domain with the natural REAL radial states gives J=0 (case A, verified) — the same complex domain, no CP. CP-existence
requires the generation STATES genuinely complex (a non-removable phase, case C), which requires a MECHANISM forcing the
ℤ₃/condensate phase onto the localizations; that mechanism is NOT derived (4656/4685 assume it; F495 argues the strata
are a real linear filtration). So: CP-EXISTS stays CANDIDATE (bucket-1 pending, gated on Engine B / condensate CP-phase);
CP-MAGNITUDE stays open/modulus. This CONFIRMS my own 4855 retraction and Keeper K907's hold. A clean "F498 still gates
it." Nothing to bank. Count n/a (audit reconcile).
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
omega = np.exp(2j*np.pi/3)                       # ℤ₃ phase, from N_c=3 (the DISPUTED premise)
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def gram_scalar(zs):
    """D_IV⁵ complex-analytic reproducing kernel on scalar localizations: K_ij = 1/(1 - z_i conj(z_j))^{n_C}."""
    z = np.asarray(zs, dtype=complex)
    K = np.array([[1.0/(1 - zi*np.conj(zj))**n_C for zj in z] for zi in z])
    d = np.sqrt(np.real(np.diag(K)))
    return K/np.outer(d, d)
def U_of(G):
    _, U = np.linalg.eigh(G); return U
def jarlskog(Uu, Ud):
    V = Uu.conj().T @ Ud
    return abs(np.imag(V[0,0]*V[1,1]*np.conj(V[0,1])*np.conj(V[1,0])))
def herm_generic(seed):
    rng = np.random.RandomState(seed)
    A = rng.randn(3,3) + 1j*rng.randn(3,3)
    return (A + A.conj().T)/2

r_up = [0.30, 0.50, 0.82]     # hierarchical up radii  (target-innocent placeholders, F490 spirit)
r_dn = [0.48, 0.64, 0.72]     # hierarchical down radii

# ---- CASE A: REAL radial states on the complex-analytic kernel → J=0 (F498) --------------------
JA = jarlskog(U_of(gram_scalar(r_up)), U_of(gram_scalar(r_dn)))
check("CASE A — REAL radial localizations z_k=r_k (the natural KW radial model): the D_IV⁵ kernel 1/(1-z z*)^{n_C} is "
      "COMPLEX-ANALYTIC, yet real sample points give a REAL symmetric Gram → real orthogonal U → real CKM → J=0. THE "
      "DOMAIN IS COMPLEX AND J STILL VANISHES. This is F498, and the direct refutation of 'domain complex → CP'.",
      JA < 1e-12, f"real states on the complex kernel → J={JA:.1e} (=0); domain complex but J=0 — F498")

# ---- CASE B: my 4854 generic complex-Hermitian operators → J≠0 (phase INSERTED) --------------
JB = np.mean([jarlskog(U_of(herm_generic(s)), U_of(herm_generic(s+100))) for s in range(1,21)])
check("CASE B — my 4854 model (generic random complex-Hermitian sector operators): J≠0 (mean |J|~0.03). But the phase is "
      "INSERTED by the randn imaginary part — this is NOT the Gram of any radial state. It ASSUMES the states are complex; "
      "it does not derive it. This is the F498-insufficient argument dressed as a domain fact.",
      JB > 1e-6, f"generic complex-Hermitian → J={JB:.2e} (≠0), but complexity injected by randn — assumes the conclusion")

# ---- CASE C: ℤ₃-phased states + hierarchy → J≠0 (the 4656/4685 build) -------------------------
zC_up = [r*omega**k for k, r in enumerate(r_up)]
zC_dn = [r*omega**k for k, r in enumerate(r_dn)]
JC = jarlskog(U_of(gram_scalar(zC_up)), U_of(gram_scalar(zC_dn)))
check("CASE C — ℤ₃-phased localizations z_k=r_k·ω^{k−1} WITH the mass hierarchy (distinct r_k): J≠0. CP is forced — but "
      "ONLY because the STATES carry the genuine ω phase (Casey's phase-advancing commits). This is the build that WOULD "
      "close the gate — IF the ω phase is forced onto the states.",
      JC > 1e-8, f"ℤ₃-phased states + hierarchy → J={JC:.2e} (≠0); CP forced by the STATE phase, not the domain")

# ---- CASE D: exact ℤ₃, equal radii → circulant → J=0 (phase alone is not enough) --------------
r_eq = [0.6, 0.6, 0.6]
zD_up = [0.6*omega**k for k in range(3)]
zD_dn = [0.5*omega**k for k in range(3)]
JD = jarlskog(U_of(gram_scalar(zD_up)), U_of(gram_scalar(zD_dn)))
check("CASE D — exact ℤ₃ phases but EQUAL radii (no hierarchy): circulant Gram → same DFT diagonalizes both sectors → V "
      "trivial → J=0. The ω phase is physical (non-removable) ONLY once the hierarchy breaks the circulant (case C). So "
      "even the phase alone is insufficient; you need phase AND hierarchy — both on the STATES.",
      JD < 1e-12, f"exact ℤ₃ equal radii → J={JD:.1e} (=0); phase needs the hierarchy to become physical")

# ---- THE RECONCILE ----------------------------------------------------------------------------
domain_complex_all = True   # the complex-analytic kernel (exponent n_C) is identical in A,B,C,D
check("RECONCILE (the decisive contrast): the complex DOMAIN — the complex-analytic kernel 1/(1-z z*)^{n_C} — is present "
      "in ALL FOUR cases. J is ZERO in A and D, NONZERO in B and C. So the domain being complex is NOT the cause of J≠0; "
      "the STATE PHASE (plus hierarchy) is. F498 is exactly right, and my 4854 'domain complex → CP derived' used the "
      "insufficient premise.",
      JA < 1e-12 and JD < 1e-12 and JB > 1e-6 and JC > 1e-8 and domain_complex_all,
      "same complex domain in all four; J=0 in A,D and J≠0 in B,C → the STATE phase decides, not the domain (F498 right)")

check("THE GATE IS UNMET (not closed): CP-existence ⟺ the generation localizations carry a genuine non-removable complex "
      "phase (case C's ω^{k−1}). Whether N_c=3 FORCES that phase onto the STATES — vs. the generations being the LINEAR "
      "Korányi–Wolf strata {0⊂2⊂5} at real radial positions (F495) → case A → J=0 — is NOT derived. 4656/4685 ASSUME the "
      "ℤ₃ phase; that assumption IS the open Engine-B gate. F498's 'the build is the decider; can fail' stands.",
      True, "gate unmet: the ω/ℤ₃ STATE phase is assumed (4656/4685), not derived; F495 linear-filtration → real → J=0 is the live alternative")

check("VERDICT (straight to Keeper): today's argument RE-ASSERTS 'domain complex' — it does NOT close F498's gate. A "
      "complex domain with the natural REAL radial states gives J=0 (case A, verified). CP-EXISTS stays CANDIDATE "
      "(bucket-1 pending, gated on Engine B / a mechanism forcing the condensate/ℤ₃ phase onto the states); CP-MAGNITUDE "
      "stays open/modulus. Confirms my own 4855 retraction and K907's hold. A clean 'F498 still gates it.' Nothing to bank.",
      JA < 1e-12 and JC > 1e-8,
      "RE-ASSERTS domain-complex; F498 gate UNMET → CP-exists CANDIDATE, CP-magnitude open/modulus; 4855 + K907 confirmed")

# ---- SCORE ------------------------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("=" * 100)
print("Toy 4857 — CP gate reconcile: domain-complex is INSUFFICIENT; the gate is the STATE phase (ℤ₃), not derived")
print("=" * 100)
print(f"[cases] A real states J={JA:.1e} (=0) | B generic-complex J={JB:.2e} (≠0, injected) | "
      f"C ℤ₃+hierarchy J={JC:.2e} (≠0) | D exact-ℤ₃ J={JD:.1e} (=0)")
print(f"[reconcile] same complex domain in all four; J vanishes in A,D and survives in B,C → the STATE phase decides, not the domain\n")
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 100)
print(f"SCORE: {passed}/{total}")
print("=" * 100)
print("""
R10 (07-25) RECONCILE CP-exists (my 4854) with banked F498 — Keeper K907 hold, task #9:
  * CASE A: REAL radial states on the D_IV⁵ complex-analytic kernel → J=0. THE DOMAIN IS COMPLEX AND J VANISHES. (F498.)
  * CASE B: my 4854 generic complex-Hermitian → J≠0, but the phase is INJECTED by randn — assumes the states complex.
  * CASE C: ℤ₃-phased states + hierarchy → J≠0 — CP forced by the STATE phase (4656/4685), IF the ω phase is forced.
  * CASE D: exact ℤ₃ equal radii → circulant → J=0 — even the phase needs the hierarchy; both live on the STATES.
  => the complex DOMAIN is identical in all four; J=0 in A,D and J≠0 in B,C → the STATE PHASE decides, not the domain.
     My 4854 RE-ASSERTS 'domain complex' (F498-insufficient). The gate — is the ℤ₃/condensate phase FORCED onto the
     generation states (vs. the F495 linear KW radial filtration → J=0)? — is NOT derived; 4656/4685 assume it.
  VERDICT: CP-EXISTS stays CANDIDATE (gated on Engine B / condensate CP-phase); CP-MAGNITUDE open/modulus. F498 still
  gates it. Confirms my 4855 retraction + K907. Nothing to bank.
""")
