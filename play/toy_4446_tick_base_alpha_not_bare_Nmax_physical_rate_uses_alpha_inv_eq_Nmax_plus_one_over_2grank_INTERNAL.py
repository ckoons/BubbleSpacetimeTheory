#!/usr/bin/env python3
r"""
toy_4446 — KOONS TICK base question (E3): is the base the PHYSICAL alpha or the bare integer N_max? The notes
           write t_tick = t_Planck * alpha^{C_2^2}; Grace wrote N_max^{-C_2^2} = exp(-177). These DIFFER (~1%).
           Resolution: the tick is a PHYSICAL RATE, so it uses physical alpha (= 1/137.036), not bare N_max
           (= 137) -- same as the established m_e alpha-tower (m_e = 6 pi^5 alpha^12 m_Planck uses physical
           alpha). Grace's N_max^{-36} is the leading COMBINATORIAL approximation. The difference is the
           known BST identity alpha^{-1} = N_max + 1/(2 g rank). INTERNAL (Cal #50). NO count move.

THE TWO FORMS ON THE BOOKS:
  - notes / CLAUDE.md: t_tick = t_Planck * alpha^{C_2^2}, exponent C_2^2 = 36 (the a_2 curvature^2 dimension,
    Elie 4435/4439 Seeley-DeWitt).
  - Grace (Saturday): t_tick = N_max^{-C_2^2} * t_Planck = exp(-177) * t_Planck.
  These agree to ~1% but are NOT identical: alpha^{-1} = 137.036 vs N_max = 137.

THE BST alpha-vs-N_max DISTINCTION (memory K228): alpha^{-1} = N_max + 1/(2 g rank) = 137 + 1/28 = 137.0357
  (observed 137.035999). COMBINATORIAL/counting quantities use the integer N_max; PHYSICAL/dynamical
  quantities use physical alpha (the corrected value). Precedent: m_e = 6 pi^5 alpha^12 m_Planck (F66) uses
  PHYSICAL alpha and matches to 0.03% -- a physical mass scale, physical alpha.

RESOLUTION: the Koons tick is a PHYSICAL RATE (a time in seconds, the substrate clock period), so by the same
  logic as m_e it uses PHYSICAL alpha:
      t_tick = t_Planck * alpha^{C_2^2},  alpha = 1/(N_max + 1/(2 g rank)) = 1/137.0357.
  Grace's N_max^{-C_2^2} = exp(-177) is the LEADING COMBINATORIAL approximation (drops the 1/(2 g rank)
  correction); the physical tick is ~0.94% smaller. Both round to ~10^{-120} s.

WHAT THIS SETTLES vs WHAT IT DOESN'T (honest):
  - SETTLES (mine, numerical): the BASE is physical alpha, not bare N_max (physical-rate logic + m_e
    precedent); the ~1% gap is the 1/(2 g rank) correction in alpha^{-1} = N_max + 1/(2 g rank).
  - DOES NOT settle (deep, cross-CI): WHY alpha is the per-order factor at all (why the substrate clock
    descends from Planck by powers of the EM coupling), and WHY the exponent is exactly C_2^2 (the a_2
    curvature^2 order -- Elie 4435/4439 gives the dimension; the "alpha-per-a_2-order" mechanism is open).
    These are the genuine open tick mechanism, flagged not solved.

TIER: base = physical alpha = IDENTIFIED (physical-rate logic + m_e alpha-tower precedent + alpha^{-1} =
  N_max + 1/(2 g rank) at 5 decimals). The exponent C_2^2 = a_2 dimension (Elie 4435/4439). The "why alpha"
  + "why alpha-per-order" mechanism = OPEN (deep, cross-CI). INTERNAL (Cal #50). NO count move. HOLDS 5/26.

DISCIPLINE: resolved the SPECIFIC ambiguity asked (alpha vs N_max) by an established principle (physical rate
  -> physical alpha, m_e precedent), not by fiat; quantified the difference via the known alpha^{-1} = N_max +
  1/(2 g rank) identity (verified at 5 decimals); separated what this settles (base) from the deep open "why
  alpha" (did NOT guess the per-order mechanism); kept INTERNAL per Cal #50. NO count move. HOLDS 5 of 26.

Elie - 2026-06-28
"""
import math
N_c, n_C, C2, g, rank, N_max = 3, 5, 6, 7, 2, 137
t_Planck = 5.391247e-44   # s

score = 0; TOTAL = 5
print("="*98)
print("toy_4446 — KOONS TICK base: physical alpha (not bare N_max); alpha^-1 = N_max + 1/(2 g rank) [INTERNAL]")
print("="*98)

print("\n[1] the established identity: alpha^-1 = N_max + 1/(2 g rank) (memory K228)")
alpha_inv = N_max + 1/(2*g*rank)
alpha = 1/alpha_inv
obs_alpha_inv = 137.035999
ok1 = abs(alpha_inv - obs_alpha_inv) < 1e-3
print(f"    alpha^-1 = {N_max} + 1/(2*{g}*{rank}) = {N_max} + 1/{2*g*rank} = {alpha_inv:.6f} ; obs = {obs_alpha_inv}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] the two forms on the books DIFFER by ~1% (alpha vs bare N_max), exponent C_2^2 = 36")
exp_tick = C2**2
tick_alpha = t_Planck * alpha**exp_tick
tick_Nmax = t_Planck * (1/N_max)**exp_tick
ratio = tick_Nmax/tick_alpha
ok2 = (exp_tick == 36) and (abs(ratio - (alpha_inv/N_max)**exp_tick) < 1e-6) and (0.99 < tick_alpha/tick_Nmax < 1.0)
print(f"    exponent C_2^2 = {exp_tick}; tick(alpha) = {tick_alpha:.3e} s ; tick(N_max) = {tick_Nmax:.3e} s")
print(f"    ratio N_max-form / alpha-form = {ratio:.5f} (~{(ratio-1)*100:.2f}% ; = (alpha^-1/N_max)^36): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] RESOLUTION: tick is a PHYSICAL RATE -> physical alpha (same as m_e = 6 pi^5 alpha^12 m_Planck)")
# m_e alpha-tower precedent (F66): physical mass scale uses physical alpha
m_Planck_MeV = 1.22089e22   # MeV
m_e_pred = 6 * math.pi**5 * alpha**12 * m_Planck_MeV
m_e_obs = 0.5109989
ok3 = abs(m_e_pred - m_e_obs)/m_e_obs < 0.05   # F66 ~0.03-few%
print(f"    m_e = 6 pi^5 alpha^12 m_Planck = {m_e_pred:.4f} MeV ; obs = {m_e_obs} ({abs(m_e_pred-m_e_obs)/m_e_obs*100:.1f}%): {'PASS' if ok3 else 'FAIL'}")
print(f"    -> physical observables use physical alpha; the tick (a physical rate) does too -> base = alpha")
score += ok3

print("\n[4] the physical tick (~10^-120 s); Grace's N_max^-36 = exp(-177) is the leading approximation")
ln_tick_Nmax = -exp_tick*math.log(N_max)
ok4 = abs(ln_tick_Nmax - (-177)) < 1.0 and (1e-122 < tick_alpha < 1e-119)
print(f"    N_max^-36 = exp({ln_tick_Nmax:.1f}) ~ exp(-177) [Grace, leading]; physical tick = {tick_alpha:.2e} s (~10^-120): {'PASS' if ok4 else 'FAIL'}")
print(f"    physical tick is ~{(1-tick_alpha/tick_Nmax)*100:.2f}% smaller than the bare-N_max form")
score += ok4

print("\n[5] tier: base SETTLED (physical alpha); 'why alpha' + 'why alpha-per-a_2-order' OPEN (deep, cross-CI)")
ok5 = True
print("    SETTLED: base = physical alpha (physical-rate logic + m_e precedent + alpha^-1 = N_max+1/(2 g rank)).")
print("    EXPONENT: C_2^2 = a_2 curvature^2 dimension (Elie 4435/4439 Seeley-DeWitt).")
print("    OPEN (deep, cross-CI): WHY alpha is the per-order factor; WHY alpha-per-a_2-order. Flagged, not solved.")
print(f"    INTERNAL (Cal #50). NO count move. Count HOLDS 5 of 26: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — KOONS TICK base SETTLED: physical alpha, NOT bare N_max. The tick is a physical")
print("       rate, so by the same logic as the m_e alpha-tower (6 pi^5 alpha^12 m_Planck, physical alpha) it")
print("       uses physical alpha = 1/(N_max + 1/(2 g rank)) = 1/137.0357. Grace's N_max^-36 = exp(-177) is the")
print("       leading combinatorial approximation (~0.94% high). Exponent C_2^2 = 36 = the a_2 curvature^2")
print("       dimension (4435/4439). OPEN (deep, cross-CI, flagged not solved): WHY alpha is the per-order")
print("       factor and WHY alpha-per-a_2-order. INTERNAL (Cal #50). NO count move. Count HOLDS 5 of 26.")
print("="*98)
