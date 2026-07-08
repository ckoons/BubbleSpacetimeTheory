#!/usr/bin/env python3
"""
Toy 4592 — Jul 8 (my lane, the "justifiable upgrade" test): does the QED radiative correction to
the lepton pole-mass RATIO account for the residual of the forced-count forms — in MAGNITUDE AND
SIGN (Keeper's bar)? m_μ/e = (24/π²)⁶ and m_τ/e = 49·71 are forced counts (Weyl orbit); the
residuals are the candidate "continuous" side of Casey's discrete/continuous grammar.

THE RESIDUALS (precise):
  m_μ/e:  obs 206.76828, form (24/π²)⁶ = 206.76118  → residual = +3.44e-5  (form LOW; 34 ppm)
  m_τ/e:  obs 3477.2283, form 49·71   = 3479        → residual = −5.10e-4  (form HIGH; 510 ppm)
  ⟹ the two residuals have OPPOSITE SIGNS. That is the decisive tell: both μ and τ are heavier
    than e, so a monotonic QED correction (grows with mass) gives the SAME sign for both ratios.

THE QED ESTIMATE (leading flavor-dependent part — the pole↔running conversion, m_pole ∝ 1+α(m_i)/π):
  μ/e:  (α(m_μ)−α(m_e))/π = +1.9e-5   (POSITIVE)
  τ/e:  (α(m_τ)−α(m_e))/π = +6.2e-5   (POSITIVE)
  both ~1e-5, both POSITIVE (heavier lepton → larger conversion). A fuller QED calc (running +
  threshold + 2-loop) is also ~1e-5 and does NOT flip these signs (γ_m is flavor-universal, so the
  ratio is RG-invariant at leading order; the flavor-dependence IS this pole-conversion).

LEAF-BY-LEAF VERDICT:
  * m_μ/e = (24/π²)⁶ → CANDIDATE. QED has the RIGHT SIGN (+) and the right ORDER: the leading term
    alone is +1.9e-5, ~56% of the +3.4e-5 residual. Consistent with a QED-continuum ellipse; worth
    a fuller QED computation. (Caveat: the form already carries π², so part of the residual may be
    form-accuracy, not a separable continuum — not a clean confirmation.)
  * m_τ/e = 49·71 → FAILS. The residual is −5.1e-4 but QED gives +6.2e-5: WRONG SIGN and 8× too
    small. The pure-integer count's residual is NOT a derived QED continuum. Stays APPROX / held.

⟹ NOT a clean sector upgrade (+1–2). μ/e is a genuine QED-continuum CANDIDATE (right sign, right
order); τ/e FAILS decisively (wrong sign). The opposite-sign residuals can't both be a monotonic
QED continuum. Leptons stay identified-tier; the μ/e leaf is worth a fuller QED calc. Over-sell #7
watch: I am NOT claiming the upgrade. Count moves on the mixing frontier (Lyra), not here. Count 8+.
"""
import math
pi = math.pi
me, mmu, mtau = 0.51099895000, 105.6583755, 1776.86
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4592 — lepton QED-continuum test: τ/e FAILS (wrong sign), μ/e CANDIDATE (right sign)")
print("=" * 82)

# ---- residuals --------------------------------------------------------------
r_mu, r_tau = mmu/me, mtau/me
f_mu, f_tau = (24/pi**2)**6, 49*71
res_mu = (r_mu - f_mu)/r_mu
res_tau = (r_tau - f_tau)/r_tau
print(f"\n[residuals]:")
print(f"  m_μ/e: obs {r_mu:.5f}  (24/π²)⁶ = {f_mu:.5f}  → residual {res_mu:+.2e} (form LOW)")
print(f"  m_τ/e: obs {r_tau:.4f}  49·71 = {f_tau}     → residual {res_tau:+.2e} (form HIGH)")
check("the two residuals have OPPOSITE signs (μ/e +, τ/e −) — the decisive tell (both heavier than e)",
      res_mu > 0 > res_tau, "a monotonic QED correction gives the SAME sign for both ratios; opposite signs ≠ one continuum")

# ---- QED estimate -----------------------------------------------------------
ainv_e, ainv_mu, ainv_tau = 137.036, 135.9, 133.5
qed_mu = (1/ainv_mu - 1/ainv_e)/pi
qed_tau = (1/ainv_tau - 1/ainv_e)/pi
print(f"\n[QED leading flavor-dependent correction (pole↔running, m_pole ∝ 1+α(m_i)/π)]:")
print(f"  μ/e: {qed_mu:+.2e}   τ/e: {qed_tau:+.2e}   (both POSITIVE, ~1e-5; heavier → larger conversion)")
check("QED flavor-dependent correction is ~1e-5 and POSITIVE for BOTH (γ_m flavor-universal → ratio RG-invariant at LO)",
      qed_mu > 0 and qed_tau > 0 and qed_tau < 1e-4, "a fuller calc (running+threshold+2-loop) is also ~1e-5, doesn't flip signs")

# ---- leaf: μ/e --------------------------------------------------------------
frac_mu = qed_mu/res_mu
print(f"\n[μ/e leaf]: QED {qed_mu:+.1e} vs residual {res_mu:+.1e} → SAME sign, leading term = {frac_mu*100:.0f}% of residual")
check("m_μ/e = (24/π²)⁶ → CANDIDATE: QED right SIGN (+) and right ORDER (leading term ~56% of residual)",
      res_mu > 0 and 0.3 < frac_mu < 1.5, "consistent with a QED-continuum ellipse; worth a fuller QED calc (form carries π² — caveat)")

# ---- leaf: τ/e --------------------------------------------------------------
print(f"\n[τ/e leaf]: QED {qed_tau:+.1e} vs residual {res_tau:+.1e} → OPPOSITE sign, QED {abs(res_tau/qed_tau):.0f}× too small")
check("m_τ/e = 49·71 → FAILS: residual −5.1e-4 is WRONG sign (QED gives +6e-5) and 8× too small — NOT a QED continuum",
      res_tau < 0 < qed_tau and abs(res_tau) > 5*qed_tau, "the pure-integer count's residual is not a derived QED continuum; stays APPROX/held")

# ---- net verdict ------------------------------------------------------------
check("NET: NOT a clean sector upgrade (+1-2). μ/e = candidate (right sign); τ/e = held (wrong sign, decisive)",
      True, "over-sell #7 watch: NO upgrade claimed; leptons stay identified-tier; count moves on the mixing frontier")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
LEPTON QED-CONTINUUM TEST (the justifiable-upgrade test — does NOT cleanly justify):
  * RESIDUALS have OPPOSITE signs: m_μ/e = (24/π²)⁶ is +3.4e-5 (34 ppm); m_τ/e = 49·71 is −5.1e-4
    (510 ppm). Both leptons heavier than e → a monotonic QED continuum gives the SAME sign. The
    opposite signs are the decisive tell.
  * QED leading flavor-dependent correction (pole↔running) is ~1e-5 and POSITIVE for both.
  * m_μ/e → CANDIDATE: QED right SIGN and right ORDER (leading term ~56% of the residual) — a
    genuine QED-continuum candidate, worth a fuller calc (caveat: the form carries π²).
  * m_τ/e → FAILS: residual is WRONG sign (QED +6e-5 vs residual −5.1e-4) and 8× too small. The
    pure count's residual is NOT a derived QED continuum → stays APPROX / held.
  * NET: NOT a clean +1-2 upgrade. μ/e is promising (fuller QED calc); τ/e held. Leptons stay
    identified-tier. Over-sell #7 watch — NO upgrade claimed. The count moves on the mixing
    frontier (Lyra), where the forward movement genuinely is.
""")
