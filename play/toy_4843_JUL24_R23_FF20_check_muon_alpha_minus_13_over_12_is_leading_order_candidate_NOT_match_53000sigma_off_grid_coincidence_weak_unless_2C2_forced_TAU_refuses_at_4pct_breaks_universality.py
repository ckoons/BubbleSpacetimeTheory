#!/usr/bin/env python3
"""
Toy 4843 — Jul 24 (FF-20 check on Casey's ranging shot m_μ/m_e = α^(−13/12); Elie's assigned lane, pull 24w). Casey found the
muon ratio as a near-pure power of α with denominator 12 = 2C₂: m_μ/m_e ≈ α^(−13/12), 13 = C₂+g. Keeper (K892) moved the muon
to candidate-derived, gated on Lyra's 1/(2C₂) weight-shift gate. My lane is the fish-detector bound: is α^(−13/12) real
evidence or a grid coincidence? Three honest results.

(1) σ — it is a leading-order FORM, not a precision match: α^(−13/12) = 206.49 vs 206.768 → 0.133% dev. m_μ/m_e is known to
    ~2.5×10⁻⁸, so 0.133% is ~53,000σ off. Per the score-σ-not-dev discipline, that is NOT an agreement — it is a candidate
    leading-order form that REQUIRES a correction term (exactly like m_e = 6π⁵α¹² sits at 0.03%, not exact). Judge it as a
    forced-vs-fit FORM, not as a match.

(2) GRID-COINCIDENCE — weak unless the denominator is FORCED: with the denominator FREE (any q ≤ 24), there are ~500 grid
    points α^(−p/q) and the ~7% chance of landing within 0.13% of one makes a hit unremarkable. With the denominator FORCED
    to q = 2C₂ = 12 (BST-primary, target-innocent), the grid is sparse (spacing 0.41 in ln-mass) and the hit probability is
    ~0.65% — genuine evidence. So the ENTIRE weight of the α^(−13/12) claim rests on whether the 1/(2C₂) is forced (Lyra's
    gate), not on the fraction being pretty. The α^(−1/12) = 1.507 ≈ 3/2 "identity" is itself only a 0.46% coincidence — weak
    on its own.

(3) TAU — refuses the same ladder (the discriminator, and it's a problem): m_τ/m_e = 3477 → E_τ = 1.657, E_τ×12 = 19.89
    (NOT a clean 20). α^(−20/12) = 3642 misses by 4.75%. So the muon fits α^(−13/12) at 0.13% but the tau MISSES α^(−20/12)
    by ~5%. The α-power ladder is NOT universal across the three generations — either it is muon-specific or the tau is a
    different mechanism. A universal-mechanism claim must explain why the tau refuses.

⟹ VERDICT (plain, fish-detector): m_μ/m_e = α^(−13/12) is a CANDIDATE leading-order form, NOT a match to bank. Three
withholds: (1) it is ~53,000σ off → a form needing a correction, judged as forced-vs-fit not as agreement; (2) the
grid-coincidence is ~7% with a free denominator → real evidence ONLY IF Lyra's gate forces the 1/(2C₂) = 1/12; (3) the tau
refuses the same ladder at ~5% → the mechanism is not universal and must explain the tau. Hold at candidate-derived pending
Lyra's 1/(2C₂) gate AND a tau account; do NOT re-bank the muon on the strength of a pretty fraction. Consistent with the FK/θ
picture only if the α-power is a reading of that spectrum — not an independent second derivation. Structure (T2525)
UNAFFECTED; EW banked; Five-Absence-positive. Count ~6.
"""
import numpy as np
from math import log
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

ainv = 137.035999
mmu_e, mtau_e = 206.7682830, 3477.15
sig_exp = 2.5e-8
E_mu = log(mmu_e) / log(ainv); pred_mu = ainv**(13 / 12); dev_mu = abs(pred_mu - mmu_e) / mmu_e
E_tau = log(mtau_e) / log(ainv); pred_tau = ainv**(20 / 12); dev_tau = abs(pred_tau - mtau_e) / mtau_e
spacing = log(ainv) / 12; p_forced = 2 * dev_mu / spacing
identity_32 = abs(ainv**(1 / 12) - 1.5) / 1.5
print(f"\n[FF-20] α^(-13/12)={pred_mu:.2f} vs 206.768 → {dev_mu*100:.3f}% = {dev_mu/sig_exp:.0f}σ (form not match); grid(q=12 forced)={p_forced*100:.2f}%; tau α^(-20/12)={pred_tau:.0f} vs 3477 → {dev_tau*100:.1f}% (refuses)")

check("(1) σ — LEADING-ORDER FORM, not a precision match: α^(−13/12)=206.49 vs 206.768 → 0.133% dev, and m_μ/m_e is known to "
      "~2.5e-8, so it is ~53,000σ off. Per score-σ-not-dev, that is NOT an agreement — it's a candidate form REQUIRING a "
      "correction (like m_e=6π⁵α¹² at 0.03%). Judge it as forced-vs-fit FORM, not as a match.",
      dev_mu / sig_exp > 1000,
      "α^(-13/12) is 53,000σ off → leading-order form needing a correction, NOT a precision match; judge as forced-vs-fit form")

check("(2) GRID-COINCIDENCE — weak unless the denominator is FORCED: free denominator (q≤24) → ~500 grid points, ~7% hit "
      "within 0.13% (unremarkable). Forced q=2C₂=12 → sparse grid (ln-spacing 0.41), hit prob ~0.65% → genuine evidence. So "
      "the α^(−13/12) claim rests ENTIRELY on Lyra's gate forcing the 1/(2C₂), not on the fraction. The α^(−1/12)≈3/2 "
      "'identity' is itself only a 0.46% coincidence.",
      p_forced < 0.01 and identity_32 < 0.01,
      "grid: forced q=12 → ~0.65% (evidence) vs free q → ~7% (weak); claim rests on Lyra's 1/(2C₂) gate; 3/2 identity 0.46% coincidence")

check("(3) TAU refuses the ladder (discriminator, a problem): m_τ/m_e=3477 → E_τ×12=19.89 (not a clean 20); α^(−20/12)=3642 "
      "misses by 4.75%. The muon fits α^(−13/12) at 0.13% but the tau misses α^(−20/12) at ~5%. So the α-power ladder is NOT "
      "universal — muon-specific or tau a different mechanism; a universal claim must explain why the tau refuses.",
      dev_tau > 0.03 and abs(E_tau * 12 - 20) > 0.05,
      "tau: E_τ×12=19.89 not clean; α^(-20/12) misses 4.75% → ladder NOT universal → muon-specific or tau different; must explain the tau")

check("VERDICT (fish-detector): α^(−13/12) is a CANDIDATE leading-order form, NOT a match. Three withholds: 53,000σ off (form "
      "not agreement, needs a correction); grid-coincidence ~7% free / ~0.65% only if 2C₂ forced (Lyra's gate); tau refuses "
      "at ~5% (not universal). Hold at candidate-derived pending Lyra's 1/(2C₂) gate AND a tau account; do NOT re-bank on the "
      "pretty fraction. Consistent with the FK/θ picture only as a reading of that spectrum, not an independent 2nd "
      "derivation.",
      dev_mu / sig_exp > 1000 and p_forced < 0.01 and dev_tau > 0.03,
      "candidate leading-order form not a match; gated on Lyra's 1/(2C₂) gate + a tau account; don't re-bank on the fraction")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-23 (07-24) FF-20 check on Casey's α^(−13/12) muon (Elie's assigned lane, pull 24w):
  * (1) σ: α^(−13/12)=206.49 vs 206.768 → 0.13% = ~53,000σ off → LEADING-ORDER form needing a correction, NOT a precision match (judge as forced-vs-fit form).
  * (2) grid-coincidence: ~7% with free denominator (weak); ~0.65% only if q=2C₂=12 FORCED → the claim rests entirely on Lyra's 1/(2C₂) gate. (3/2 identity = 0.46% coincidence.)
  * (3) TAU refuses: E_τ×12=19.89 (not 20), α^(−20/12) misses 4.75% → the α-ladder is NOT universal → must explain why the tau refuses.
  => HOLD at candidate-derived pending Lyra's gate + a tau account; do NOT re-bank on the pretty fraction. Structure unaffected; EW banked.
""")
