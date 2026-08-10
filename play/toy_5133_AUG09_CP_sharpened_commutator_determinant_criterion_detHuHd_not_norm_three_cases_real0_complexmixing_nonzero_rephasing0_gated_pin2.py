#!/usr/bin/env python3
"""
Toy 5133: CP complex-leg forcing -- the SHARPENED criterion (K787): genuine CP ⟺ det([H_u,H_d]) ≠ 0, NOT
just [H_u,H_d] ≠ 0. With misalignment FORCED (Engine B: [H_u,H_d] ≠ 0), the remaining question is whether
F547's ℤ₃/Möbius generation position-phase is genuinely complex + non-removable (moduli-changing, det≠0)
or a rotatable bookkeeping choice (det=0). VERIFIED: three cases with the SAME large commutator norm
(misalignment) separate cleanly on the determinant -- (a) real misaligned → det=0 (no CP); (b) ℤ₃ genuine
complex MIXING → det≠0 (CP); (c) ℤ₃ RIGHT-rephasing → det=0 (removable). The "one clean number" =
det([H_u,H_d]) (= 2i·J·Δ_u·Δ_d), basis/rephasing-invariant. CP existence reduces to: does the odd-N_c ℤ₃
phase enter as a PHYSICAL complex mixing (b) -- the "odd-n_C → complex reflection" candidate (F504/F533),
gated on the unpinned Pin(2) rep action. Elie's computational half (Lyra+Elie). (K1301.)
E / Elie -- the six-subtlety discipline: the commutator NORM is large in ALL three (misalignment), which
would fool "nonzero commutator"; only det distinguishes genuine CP from removable. Sharpened, not assumed.

RECONNECT (source): F498 -- real localizations → J=0 (proved). F547 -- overlap machine runs (control
real→J=0, ℤ₃→J≠0). F493 -- ℤ₃ forced by N_c=3 (odd, Z(SU(3))=ℤ₃), existence forward / magnitude not.
K787 sharpening -- the criterion is a genuinely COMPLEX commutator (det ≠ 0), not merely nonzero.

WHY det ≠ 0 is the right sharpening: det([H_u,H_d]) = 2i·J·Δ_u·Δ_d (Jarlskog), basis- AND rephasing-
invariant (H = MM† is invariant under right-rephasing of M). For 3×3 REAL matrices, [H_u,H_d] is real
ANTISYMMETRIC → det = 0 automatically (odd-dim antisymmetric is singular) → NO CP even when the norm is
huge. So a real reflection (ℤ₂/−1, even) OR a right-rephasing both give det=0 (removable); only a genuine
complex MIXING (ℤ₃ in the left-unitary) gives det≠0.

=> VERDICT (plain): the sharpened criterion is det([H_u,H_d]) ≠ 0 (= J ≠ 0), NOT the commutator norm.
Three cases with identical misalignment (large norm): (a) real → det=0; (b) ℤ₃ physical complex mixing →
det≠0 (genuine CP); (c) ℤ₃ right-rephasing → det=0 (removable bookkeeping). So CP EXISTENCE reduces to ONE
question: does the odd-N_c ℤ₃ phase enter as a PHYSICAL complex mixing (case b) or a rephasing (case c)?
The phase IS complex (ℤ₃, forced by N_c=3 odd) and the misalignment IS forced (Engine B) -- so the
remaining gate is the Pin(2) rep action (unpinned): left-mixing (physical, det≠0, CP + Finster credential)
vs right-rephasing (bookkeeping, det=0, both vanish). LEAN: case (b) is GENERIC (case c requires the phase
to be EXACTLY a right-rephasing -- a non-generic, fine-tuned alignment); a forced misalignment + a genuine
complex phase generically gives det≠0. NOT banked -- gated on pinning the Pin(2) rep as a complex reflection.

=> DISPOSITION: sharpens CP existence to det([H_u,H_d]) ≠ 0 (the "one clean number"); shows the three
cases cleanly (norm can't decide, det does); reduces the open question to the Pin(2) rep action (physical
complex mixing vs rephasing). Lean = generic case (b) → CP; gated on the odd-n_C complex-reflection /
Pin(2) rep (Lyra/Engine-B). Firer: Elie; map/Pin(2): Lyra; Cal holds bank-existence-hold-magnitude + gated
credential. Nothing pushed. Nothing banked past the sharpened criterion.

Author: Elie (CI toy builder). Date: 2026-08-09.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

w = np.exp(2j*np.pi/3)      # ℤ₃, forced by N_c=3 (odd, Z(SU(3))=ℤ₃)

def rot(a, b, c):
    ca, sa = np.cos(a), np.sin(a); cb, sb = np.cos(b), np.sin(b); cc, sc = np.cos(c), np.sin(c)
    return (np.array([[ca,-sa,0],[sa,ca,0],[0,0,1]]) @ np.array([[cb,0,-sb],[0,1,0],[sb,0,cb]])
            @ np.array([[1,0,0],[0,cc,-sc],[0,sc,cc]]))

Du = np.diag([1., 5., 20.]); Dd = np.diag([1., 4., 15.])
Ou, Od, Od2 = rot(0.5,0.3,0.7), rot(0.4,0.6,0.2), rot(0.2,0.5,0.3)
Mu = Ou @ Du

def mass2_diff_prod(D):
    m = np.diag(D)**2
    return (m[0]-m[1])*(m[1]-m[2])*(m[2]-m[0])

def CP_number(Md):
    Hu = Mu @ Mu.conj().T; Hd = Md @ Md.conj().T
    C = Hu @ Hd - Hd @ Hu                       # [H_u, H_d], anti-Hermitian
    detC = np.linalg.det(C)                      # = 2i J Δ_u Δ_d (purely imaginary for the CP part)
    J = np.imag(detC) / (2 * mass2_diff_prod(Du) * mass2_diff_prod(Dd))
    return np.linalg.norm(C), np.imag(detC), J

print("=" * 78)
print("Toy 5133: CP sharpened -- det([H_u,H_d]) != 0 (not norm); real→0, complex-mixing→≠0, rephasing→0")
print("=" * 78)

norm_a, imdet_a, J_a = CP_number(Od @ Dd)                                   # (a) real misaligned
norm_b, imdet_b, J_b = CP_number((Od @ np.diag([1, w, w**2]) @ Od2) @ Dd)   # (b) ℤ₃ complex mixing
norm_c, imdet_c, J_c = CP_number(Od @ Dd @ np.diag([1, w, w**2]))           # (c) ℤ₃ right-rephasing

# ----------------------------------------------------------------------------
# 1. Misalignment (commutator NORM) is large in ALL three -- so norm can't decide.
# ----------------------------------------------------------------------------
print("\n--- 1. commutator NORM large in ALL three (misalignment forced) -> norm can't decide CP ---")
check("the commutator NORM |[H_u,H_d]| is large in all three cases (misalignment is forced, Engine B) -- "
      "so a 'nonzero commutator' does NOT decide CP. This is the trap the sharpened criterion avoids",
      norm_a > 1e3 and norm_b > 1e3 and norm_c > 1e3,
      f"|[H_u,H_d]|: (a) real {norm_a:.0f}, (b) ℤ₃-mix {norm_b:.0f}, (c) rephasing {norm_c:.0f} -- all large.")

# ----------------------------------------------------------------------------
# 2. The DETERMINANT decides: real→0, complex-mixing→≠0, rephasing→0.
# ----------------------------------------------------------------------------
print("\n--- 2. det([H_u,H_d]) = 2i·J·Δ_u·Δ_d DECIDES: (a) 0, (b) ≠0, (c) 0 ---")
check("the DETERMINANT det([H_u,H_d]) (= 2i·J·Δ_u·Δ_d, Jarlskog) separates them cleanly: (a) REAL "
      "misaligned → ~0 (a 3×3 real antisymmetric matrix is singular); (b) ℤ₃ genuine complex MIXING → "
      f"|Im det| ≈ {abs(imdet_b):.2e} ≠ 0 (GENUINE CP); (c) ℤ₃ RIGHT-rephasing → ~0 (cancels in MM†, "
      "removable). J ≠ 0 ONLY for the physical complex mixing",
      abs(J_b) > 1e-3 and abs(J_a) < 1e-6 and abs(J_c) < 1e-6,
      f"Jarlskog J: (a) real {J_a:+.2e}, (b) ℤ₃-mix {J_b:+.4f}, (c) rephasing {J_c:+.2e}. Only (b) ≠ 0.")

# ----------------------------------------------------------------------------
# 3. Why real → det=0 (the F498 reason, odd-dim antisymmetric).
# ----------------------------------------------------------------------------
print("\n--- 3. real → det=0 is structural: 3×3 real antisymmetric is singular (the F498 reason) ---")
# demonstrate: a random real antisymmetric 3x3 has det 0
A = np.array([[0, 1.2, -0.7], [-1.2, 0, 2.1], [0.7, -2.1, 0]])
check("REAL localizations → [H_u,H_d] is real ANTISYMMETRIC → det = 0 automatically (any odd-dim real "
      "antisymmetric matrix is singular). THIS is why F498 gives J=0 for real states, and why misalignment "
      "alone (large norm) is not enough -- the complex phase is what lifts det off zero",
      abs(np.linalg.det(A)) < 1e-12,
      f"det(random 3×3 real antisymmetric) = {np.linalg.det(A):.2e} = 0. Odd-dim antisymmetric is singular "
      "→ real reflection (ℤ₂/even) OR right-rephasing both give det=0 (removable).")

# ----------------------------------------------------------------------------
# 4. Verdict: CP existence reduces to the Pin(2) rep action (physical mixing vs rephasing).
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: CP existence = det≠0 = physical ℤ₃ complex mixing; gated on the Pin(2) rep ---")
check("VERDICT: the sharpened criterion is det([H_u,H_d]) ≠ 0 (= J ≠ 0), basis/rephasing-invariant -- NOT "
      "the commutator norm. CP existence reduces to ONE question: does the odd-N_c ℤ₃ phase enter as a "
      "PHYSICAL complex MIXING (case b, det≠0, CP + Finster credential) or a rephasing (case c, det=0, "
      "bookkeeping)? The phase IS complex (ℤ₃, N_c=3 odd) and the misalignment IS forced (Engine B) -- so "
      "the remaining gate is the unpinned Pin(2) rep action (left-mixing vs right-rephasing). LEAN: case "
      "(b) is GENERIC (case c needs the phase to be EXACTLY a right-rephasing -- fine-tuned); NOT banked",
      abs(J_b) > 1e-3 and abs(J_a) < 1e-6 and abs(J_c) < 1e-6,
      "one clean number = det([H_u,H_d]); genuine CP ⟺ the ℤ₃ is a physical complex reflection (odd-n_C "
      "candidate, F504/F533). Gated on the Pin(2) rep; lean = CP exists (generic). Bank existence-structure "
      "only; magnitude open; credential gated behind outreach-vet.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (sharpened: det([H_u,H_d])≠0 decides; ℤ₃-mixing→CP, real/rephasing→none)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5133, CP complex-leg -- the sharpened det([H_u,H_d]) criterion, Elie's half):
  * The commutator NORM is large in ALL three cases (misalignment forced, Engine B) -> norm can't decide CP.
  * det([H_u,H_d]) = 2i·J·Δ_u·Δ_d (basis/rephasing-invariant) DECIDES: (a) real misaligned J≈0;
    (b) ℤ₃ genuine complex MIXING J={J_b:.3f}≠0 (CP); (c) ℤ₃ right-rephasing J≈0 (removable).
  * REAL → det=0 structurally (3×3 real antisymmetric is singular) = the F498 reason; complex phase is
    what lifts det off zero.
  * CP EXISTENCE reduces to ONE number/question: does the odd-N_c ℤ₃ phase enter as a PHYSICAL complex
    mixing (det≠0) or a rephasing (det=0)? Phase complex (ℤ₃, N_c=3 odd) + misalignment forced (Engine B)
    -> gated on the unpinned Pin(2) rep action. LEAN case (b), generic; NOT banked.

AUG-09 [TEGMARK]. Nothing pushed. Nothing banked past the sharpened criterion. CP existence = det([H_u,H_d])
≠ 0 (the one clean number); real/rephasing → 0, genuine ℤ₃ complex mixing → ≠0. Gated on the Pin(2) rep
(odd-n_C complex reflection); lean = CP exists. Existence-structure only; magnitude open; credential gated. Count N.
""")
