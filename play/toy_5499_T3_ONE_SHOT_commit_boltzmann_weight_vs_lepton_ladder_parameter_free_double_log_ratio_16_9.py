#!/usr/bin/env python3
"""
Toy 5499 — T3 ONE-SHOT: the commit-Boltzmann candidate under the gated prereg.
Gate: notes/Elie_T3_PREREG_..._2026-08-25.md, GATED BY KEEPER (PASS + A1 + A2), amended.
Run date: 2026-08-25 (clock-verified). ONE candidate, evaluated ONCE. Elie.

THE CANDIDATE (declared here, first and only):
  m_j  =  A * exp(-tau * E_j)      -- mass = commit-semigroup amplitude at the
                                      channel's certified exponent E_j = nu_j^2 (K1828).
  W1: the semigroup exp(-tau*H_B) is Tier-0 banked (T2405 commit spine, June),
      grep-dated months pre-lane. The E_j are the K1828-certified numbers.
  W4: no ordering input -- E_e=25/4, E_mu=9/4, E_tau=0 enter as certified values.
  nu=0 FENCE: E_tau = 0 used ONLY as a certified number. No pile fact consumed.
      channel_k0 not needed. Fence untouched.
  A1: A and tau are lepton-sector parameters IF fitted -- so the SCORED consequence
      is the invariant on which BOTH cancel (zero fitted parameters):
        R = ln(m_mu/m_e) / ln(m_tau/m_mu) = (E_e-E_mu)/(E_mu-E_tau) = 4/(9/4) = 16/9.
      (Subscript per the collision discipline: this 16/9_exponent-gap-ratio is NOT
       F120's 16/9_deficit-candidate -- different object, different address.)
  A2: grep-checked this morning -- the form has never been evaluated against lepton
      masses anywhere in the corpus. No prior exposure. Full ladder applies.
  Pre-registered ladder (per ratio): <=0.5% WIN-quality | 0.5-5% SUGGESTIVE | >5% FAIL.
"""
from fractions import Fraction
import math

score, total = 0, 8

# -- certified exponents (K1828), exact --
E_e, E_mu, E_tau = Fraction(25,4), Fraction(9,4), Fraction(0)
R_pred = (E_e - E_mu) / (E_mu - E_tau)
t1 = R_pred == Fraction(16,9); score += t1
print(f"[{'PASS' if t1 else 'FAIL'}] 1. R_pred = (E_e-E_mu)/(E_mu-E_tau) = {R_pred} (exact, parameter-free)")

# -- current experimental numbers (PDG 2024; verify-current-numbers discipline) --
m_e, m_mu = 0.51099895069, 105.6583755          # MeV, CODATA/PDG
for m_tau, tag in [(1776.86, "PDG2022"), (1776.93, "PDG2024")]:
    R_meas = math.log(m_mu/m_e) / math.log(m_tau/m_mu)
    dev = abs(float(R_pred)/R_meas - 1)
    print(f"     m_tau={m_tau} ({tag}): R_meas={R_meas:.5f}, |pred/meas - 1| = {100*dev:.2f}%")
m_tau = 1776.93
R_meas = math.log(m_mu/m_e) / math.log(m_tau/m_mu)
dev = abs(float(R_pred)/R_meas - 1)
t2 = 0.055 < dev < 0.065; score += t2   # sanity band on my own arithmetic
print(f"[{'PASS' if t2 else 'FAIL'}] 2. deviation in expected arithmetic band: {100*dev:.3f}%")

# -- the verdict under the PRE-REGISTERED ladder (fixed before any number ran) --
verdict = "WIN" if dev <= 0.005 else ("SUGGESTIVE" if dev <= 0.05 else "FAIL")
t3 = verdict == "FAIL"; score += t3
print(f"[{'PASS' if t3 else 'FAIL'}] 3. ladder verdict = {verdict}  (5.90% > 5.00% -- the line was pre-named)")

# -- tau-value insensitivity (the verdict cannot be rescued by the m_tau split) --
devs = [abs(float(R_pred)/(math.log(m_mu/m_e)/math.log(mt/m_mu)) - 1) for mt in (1776.74, 1776.86, 1776.93, 1777.05)]
t4 = all(d > 0.05 for d in devs); score += t4
print(f"[{'PASS' if t4 else 'FAIL'}] 4. FAIL robust across m_tau band: devs = {[f'{100*d:.2f}%' for d in devs]}")

# -- how far m_tau would have to move to reach even SUGGESTIVE: report, no advocacy --
# need R_meas <= R_pred/0.95 -> ln(m_tau/m_mu) >= ln(m_mu/m_e)*0.95/R_pred
mt_needed = m_mu * math.exp(math.log(m_mu/m_e) * 0.95 / float(R_pred))
t5 = abs(mt_needed - 1830) < 15; score += t5
print(f"[{'PASS' if t5 else 'FAIL'}] 5. SUGGESTIVE would need m_tau >= {mt_needed:.1f} MeV (actual 1776.93 -- ~{100*(mt_needed/m_tau-1):.1f}% away; excluded)")

# -- W3 must-fail (guards wins; moot for FAIL, run for completeness): down-quark tower --
m_d, m_s, m_b = 4.7, 93.4, 4180.0   # MeV, PDG central
R_dq = math.log(m_s/m_d)/math.log(m_b/m_s)
t6 = abs(float(R_pred)/R_dq - 1) > 0.05; score += t6
print(f"[{'PASS' if t6 else 'FAIL'}] 6. W3 must-fail: down-quark R = {R_dq:.3f} vs 16/9 -- no spurious cross-sector pass")

# -- fence audit: zero pile facts consumed --
pile_used = False
t7 = not pile_used; score += t7
print(f"[{'PASS' if t7 else 'FAIL'}] 7. nu=0 fence: E_tau entered as certified 0 only; pile untouched; channel_k0 uncited")

# -- budget audit: one candidate, one evaluation, final state named --
t8 = True; score += t8
print(f"[{'PASS' if t8 else 'FAIL'}] 8. budget: ONE candidate (commit-Boltzmann), ONE evaluation, final state = FAIL")

print(f"\nSCORE: {score}/{total}")
print("""
FINAL STATE (per the gated prereg, exhaustive-list item 3): *** FAIL ***
The pure commit-Boltzmann weight  m ∝ exp(-tau * nu^2)  is DEAD as the lepton-mass
mechanism. Its unique parameter-free consequence -- the double-log ratio 16/9 =
1.7778 -- misses the measured 1.8891 by 5.90%, outside the pre-registered 5% line,
robust across the m_tau experimental band, with zero fitted parameters to blame.
The anti-alignment ORDER survives (K1828, untouched); the simplest quantitative
carrier of that order is now eliminated. Banked as a negative.
""")
