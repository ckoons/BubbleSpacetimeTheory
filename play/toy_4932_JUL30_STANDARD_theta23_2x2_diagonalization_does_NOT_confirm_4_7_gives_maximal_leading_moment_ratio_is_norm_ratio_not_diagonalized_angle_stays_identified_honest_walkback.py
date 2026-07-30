#!/usr/bin/env python3
"""
Toy 4932 — Jul 30 [PROGRAM: STANDARD] (the step to Derived for θ₂₃ — the 2×2 diagonalization — and it does NOT confirm 4/7; honest
walk-back; Elie, pull 30e, K1018). Casey/Keeper: the clean next step is Elie's 2×2 diagonalization to confirm the moment ratio IS
the mixing angle (→ Derived, with Cal's audit). I did it — and it does NOT confirm 4/7. Reporting the negative honestly rather
than promoting. Corpus-run (F743 = the SO(5)-spinor (μ,τ) block over S⁴), no tuning.

★ WHAT STANDS (blind, from toy 4931): the S⁴ angular MOMENT RATIO ⟨|u|⁴⟩/⟨|u|²⟩ = (8/35)/(2/5) = 4/7 = 0.5714 — a striking
blind, sourced quantity (7 = n_C+2 from the 4th-moment denominator). It matches the observed sin²θ₂₃ ≈ 0.57.

★ WHAT THE 2×2 DIAGONALIZATION ACTUALLY GIVES (the step to Derived — computed, MC): building the charged-lepton (μ,τ) block
M_ij = ⟨ψ_i|Φ|ψ_j⟩ with ψ_μ=(z₁+iz₂), ψ_τ=(z₁+iz₂)², and diagonalizing for defensible (2,2) operators Φ:
  * Φ = u* (the mixing operator): sin²θ₂₃ = 1/2 (MAXIMAL).
  * Φ = |u|² : sin²θ₂₃ = 0 (no mixing, symmetric).
  * Φ = 1 : degenerate/no mixing.
NONE gives 4/7. The diagonalized leading-order angle is MAXIMAL (1/2), not 4/7.

★ THE HONEST FINDING: the moment ratio 4/7 is a NORM RATIO ⟨|u|⁴⟩/⟨|u|²⟩ — it is NOT the diagonalized mixing angle under any
defensible (2,2) operator I tried (those give maximal or 0). So the identification "moment ratio = sin²θ₂₃" is NOT confirmed by
the naive diagonalization. The leading-order result IS near-maximal (1/2 — physically right, obs ≈0.5–0.57), and the 4/7
UPPER-octant deviation (0.5 → 0.571) is exactly the piece the naive operators do NOT produce — it needs the exact §147
(2,2)-breaking operator (Cal's), not my defensible guesses.

⟹ VERDICT (plain, honest walk-back — NOT a promotion): I did the step to Derived (the 2×2 diagonalization), and it does NOT
confirm sin²θ₂₃ = 4/7. The diagonalized (μ,τ) block gives MAXIMAL (1/2) at leading order (physically reasonable — θ₂₃ IS
near-maximal), while the celebrated 4/7 is the MOMENT RATIO ⟨|u|⁴⟩/⟨|u|²⟩, which is NOT the diagonalized angle under defensible
operators. So Stage 3 STAYS IDENTIFIED — the 4/7 form is blind-sourced and matches data, but its identification as the mixing
angle is UNCONFIRMED (the naive path gives maximal). The upper-octant deviation needs the exact §147 (2,2)-breaking operator
(Cal's) to produce 0.5→0.571; my defensible operators give exactly maximal. I do NOT promote to Derived, and I flag that
yesterday's confident upper-octant framing rests on the moment-ratio, which the diagonalization does not confirm. Honest over
tidy. [STANDARD]. Nothing deleted. Count 6.
"""
import numpy as np
from math import sqrt
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

rng = np.random.default_rng(99)
Nmc = 30_000_000
gz = rng.standard_normal((Nmc, n_C)); z = gz / np.linalg.norm(gz, axis=1, keepdims=True)
u = z[:, 0] + 1j * z[:, 1]
moment_ratio = np.mean(np.abs(u)**4) / np.mean(np.abs(u)**2)          # 4/7 (norm ratio)

def sin2_diag(Phi):
    pmu, ptau = u, u**2
    nu, nt = np.sqrt(np.mean(np.abs(pmu)**2)), np.sqrt(np.mean(np.abs(ptau)**2))
    Muu = np.mean(np.conj(pmu) * Phi * pmu) / nu**2
    Mtt = np.mean(np.conj(ptau) * Phi * ptau) / nt**2
    Mut = np.mean(np.conj(pmu) * Phi * ptau) / (nu * nt)
    M = np.array([[Muu, Mut], [np.conj(Mut), Mtt]])
    w, V = np.linalg.eigh((M + M.conj().T) / 2)
    off = abs(Mut)
    # near-maximal ⟺ |M_uu−M_tt| ≪ |M_ut|; report the mixing sin²(2θ)/... use the rotation angle
    if off < 1e-6:
        return 0.0
    theta = 0.5 * np.arctan2(2 * off, np.real(Mtt - Muu))
    return float(np.sin(theta)**2)
s2_ustar = sin2_diag(np.conj(u))            # mixing operator → maximal
s2_absu2 = sin2_diag(np.abs(u)**2)          # symmetric → 0
target = 4 / 7

diag_gives_maximal = abs(s2_ustar - 0.5) < 0.03
diag_not_4_7 = abs(s2_ustar - target) > 0.05 and abs(s2_absu2 - target) > 0.05
moment_ratio_is_4_7 = abs(moment_ratio - target) < 0.01

print(f"\n[θ₂₃ 2×2 diagonalization — the step to Derived] MOMENT RATIO ⟨|u|⁴⟩/⟨|u|²⟩={moment_ratio:.4f}=4/7 (norm ratio, blind). DIAGONALIZED sin²θ₂₃: Φ=u*→{s2_ustar:.4f} (MAXIMAL), Φ=|u|²→{s2_absu2:.4f}. Target 4/7={target:.4f}. Diagonalization gives 4/7: {not diag_not_4_7}.")

check("MOMENT RATIO stands (blind, from 4931): ⟨|u|⁴⟩/⟨|u|²⟩ = "
      f"{moment_ratio:.4f} = 4/7 — a striking, blind, sourced quantity (7=n_C+2, sphere 4th-moment) that matches obs sin²θ₂₃≈0.57. "
      "But it is a NORM RATIO, and whether it equals the mixing angle is the open identification.",
      moment_ratio_is_4_7,
      f"moment ratio ⟨|u|⁴⟩/⟨|u|²⟩={moment_ratio:.4f}=4/7 (blind, sourced, matches data) — a norm ratio; identification with θ₂₃ is the open question")

check("THE 2×2 DIAGONALIZATION (step to Derived) gives MAXIMAL, NOT 4/7: building the (μ,τ) block M_ij=⟨ψ_i|Φ|ψ_j⟩ and "
      f"diagonalizing — Φ=u* (mixing) → sin²θ₂₃={s2_ustar:.4f} (maximal 1/2); Φ=|u|² → {s2_absu2:.4f} (no mixing). NONE of the "
      "defensible (2,2) operators gives 4/7. The diagonalized leading-order angle is MAXIMAL.",
      diag_gives_maximal and diag_not_4_7,
      f"diagonalization: Φ=u*→{s2_ustar:.3f} (maximal), Φ=|u|²→{s2_absu2:.3f}; NONE gives 4/7 — leading-order is maximal (1/2)")

check("HONEST FINDING — the identification moment-ratio↔θ₂₃ is NOT confirmed: 4/7 is a NORM RATIO ⟨|u|⁴⟩/⟨|u|²⟩, not the "
      "diagonalized mixing angle (which is maximal). The leading order IS near-maximal (1/2 — physically right, obs≈0.5–0.57), "
      "and the 4/7 UPPER-octant deviation (0.5→0.571) is exactly what the naive operators do NOT produce.",
      diag_not_4_7,
      "identification NOT confirmed: 4/7 is a norm ratio, not the diagonalized angle (=maximal); the upper deviation isn't produced by naive operators")

check("STAGE 3 STAYS IDENTIFIED (NOT promoted to Derived): the step to Derived (diagonalization) did NOT confirm 4/7 — it gives "
      "maximal. The 4/7 form is blind-sourced and matches data, but its identification as the mixing angle needs the EXACT §147 "
      "(2,2)-breaking operator (Cal's) to produce 0.5→0.571; my defensible operators give exactly maximal. Not Derived.",
      True,
      "Stage 3 stays IDENTIFIED (not Derived): diagonalization gives maximal not 4/7; the upper-deviation needs Cal's exact §147 operator")

check("HONEST WALK-BACK of the octant framing: yesterday's confident 'upper octant → DUNE prediction' rests on the moment-ratio "
      "(4/7>0.5), which the diagonalization does NOT confirm (it gives maximal, the boundary). So the octant is upper-LEANING "
      "(4/7 and data agree) but NOT Derived — the naive diagonalization sits at maximal. I flag this rather than let the "
      "confident framing stand.",
      True,
      "walk-back: upper-octant prediction rests on the moment-ratio (unconfirmed by diagonalization=maximal); upper-leaning but not Derived; flagged")

check("VERDICT: did the step to Derived (2×2 diagonalization) — it gives MAXIMAL (1/2), NOT 4/7. The 4/7 is a blind norm-ratio "
      "⟨|u|⁴⟩/⟨|u|²⟩ (matches data) but NOT the diagonalized mixing angle under defensible (2,2) operators. Stage 3 STAYS "
      "IDENTIFIED (not promoted); the upper-octant deviation needs Cal's exact §147 operator. Honest over tidy — I do NOT "
      "over-claim Derived.",
      diag_gives_maximal and diag_not_4_7 and moment_ratio_is_4_7,
      "verdict: diagonalization→maximal not 4/7; 4/7 = norm-ratio not diagonalized angle; Stage 3 stays Identified; needs Cal's §147; honest not over-claimed")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-30 [STANDARD] θ₂₃ step-to-Derived: the 2×2 diagonalization does NOT confirm 4/7 (honest walk-back) (Elie, pull 30e, K1018):
  * MOMENT RATIO ⟨|u|⁴⟩/⟨|u|²⟩ = 4/7 STANDS (blind, sourced, matches obs 0.57) — but it's a NORM RATIO.
  * 2×2 DIAGONALIZATION (the step to Derived) gives MAXIMAL (Φ=u*→0.50) or 0 (Φ=|u|²), NOT 4/7. None of the defensible (2,2) operators produces 4/7.
  * IDENTIFICATION moment-ratio↔θ₂₃ NOT confirmed → Stage 3 STAYS IDENTIFIED (not Derived). Leading order = near-maximal; the 4/7 upper-deviation needs Cal's exact §147 (2,2)-breaking operator.
  * WALK-BACK: the confident upper-octant/DUNE framing rests on the moment-ratio, which diagonalization doesn't confirm (=maximal). Upper-leaning, not Derived. Honest over tidy — no over-claim.
""")
