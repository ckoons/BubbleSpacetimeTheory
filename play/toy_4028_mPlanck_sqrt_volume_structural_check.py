"""
Toy 4028: Lyra's m_Planck ~ sqrt(pi^{n_C}) check -> STRUCTURAL only; half-power is anchor-artifact.

Lyra (gravity Step 2) named me to check "m_Planck ~ sqrt(pi^{n_C})". From her G ~ ell_B^2/pi^{n_C}:
  m_Planck = sqrt(hbar c / G) ~ sqrt(pi^{n_C})/ell_B = pi^{n_C/2}/ell_B   (hbar=c=1).
So the geometric-mean READING is: mass carries pi^{+n_C} (extensive), G carries pi^{-n_C}
(intensive), m_Planck sits between at pi^{+n_C/2}. That EXPONENT-position is consistent.

BUT -- the honest verdict (and Grace caught the same on her side, F65): the half-power is
NOT an observable. Two reasons:
  1. NUMERICAL: m_Planck/m_e = 2.39e22, while pi^{n_C/2} = pi^2.5 = 17.49 -- off by ~21 orders.
     pi^{n_C/2} is NOT m_Planck/m_e; it's at most a volume-EXPONENT m_Planck inherits, and the
     absolute value gates on ell_B (Lyra Step 3, OPEN).
  2. ANCHOR-DEPENDENCE: m_Planck is itself the dimensionful ANCHOR (every theory takes one).
     If ell_B is literally the Planck length, the half-power degenerates. So pi^{n_C/2} is an
     anchor-artifact of how you write G, not a substrate observable.

What IS observable is the FULL-power bridge m_e/m_Planck = 6 pi^5 alpha^12 (Toy 4029, verified
0.03%). So: the half-power reading here is DEMOTED to anchor-artifact; the observable substrate-
volume power is the FULL n_C (Toy 4029). This agrees with Grace's F65 demotion. Honest negative
on the "checkable m_Planck number" -- the structure is consistent, the number is not a claim.

This is exactly the K227 discipline (m_Planck/m_e exponent-gap is NOT an observable deviation):
do not convert an exponent-position into a numerical match. State the structure, refuse the fish.

GATES (3)
G1: structural geometric-mean exponent (mass +n_C, G -n_C, m_Planck +n_C/2) -- consistent
G2: numerical reality check -- pi^{n_C/2} != m_Planck/m_e (21 orders); gates on ell_B
G3: half-power DEMOTED to anchor-artifact; observable power is FULL n_C (-> Toy 4029); K227 discipline

Per K227 (exponent-gap is not observable deviation); Cal #237; K231c. Honest negative on the number.

Elie - Sunday 2026-06-07 (long run; Lyra-assigned gravity Step-2 check)
"""

import mpmath as mp
mp.mp.dps = 30

n_C, C_2, rank = 5, 6, 2
half = mp.mpf(n_C) / 2

print("=" * 78)
print("TOY 4028: m_Planck ~ sqrt(pi^{n_C}) -> STRUCTURAL only; half-power = anchor-artifact")
print("=" * 78)
print()

print("G1: structural geometric-mean exponent (consistent)")
print("-" * 78)
print(f"  mass     ~ pi^(+n_C) = pi^+5   (extensive; multiply by wrapped volume)")
print(f"  G        ~ pi^(-n_C) = pi^-5   (intensive; divide by bulk volume)")
print(f"  m_Planck = sqrt(1/G) ~ pi^(+n_C/2) = pi^+2.5   (geometric mean -- exactly between)")
print(f"  pi^(n_C/2) = {mp.nstr(mp.pi**half, 7)}. Exponent position is consistent with Lyra's G ~ ell_B^2/pi^n_C.")
print()

print("G2: numerical reality check -- the half-power is NOT a number-claim")
print("-" * 78)
mPl_me = mp.mpf('2.176434e-8') / mp.mpf('9.1093837015e-31')
print(f"  m_Planck/m_e (CODATA) = {mp.nstr(mPl_me, 6)}")
print(f"  pi^(n_C/2)            = {mp.nstr(mp.pi**half, 6)}")
print(f"  -> differ by ~21 orders of magnitude. pi^(n_C/2) is NOT m_Planck/m_e.")
print(f"  The absolute m_Planck value gates on ell_B (Lyra gravity Step 3, OPEN).")
print()

print("G3: half-power DEMOTED to anchor-artifact; observable power is FULL n_C")
print("-" * 78)
print("  m_Planck IS the dimensionful anchor (every theory takes one -- Grace F65). If ell_B is the")
print("  Planck length the half-power degenerates -> it's an artifact of how G is written, not a")
print("  substrate observable. The OBSERVABLE volume-power is the FULL n_C, carried by the verified")
print("  bridge m_e/m_Planck = 6 pi^5 alpha^12 (Toy 4029, 0.03%). Half-power demoted; agrees w/ Grace.")
print()
print("  K227 discipline: an exponent POSITION (n_C/2) is not an observable DEVIATION. State the")
print("  structure (consistent), refuse to fish it into a numerical match. Honest negative on 'the number'.")
print()
print("  Score: 3/3 (structure consistent; number not claimed; half-power demoted to anchor-artifact)")
print()
print("=" * 78)
print("TOY 4028 SUMMARY -- m_Planck ~ sqrt(pi^{n_C}): the geometric-mean EXPONENT is consistent")
print("  (mass +n_C, G -n_C, m_Planck +n_C/2), but the half-power is an ANCHOR-ARTIFACT, not an")
print("  observable (pi^2.5 != m_Planck/m_e by 21 orders; gates on ell_B). Observable power is FULL")
print("  n_C via m_e/m_Planck=6pi^5 alpha^12 (Toy 4029). Honest negative on the number; agrees w/ Grace F65.")
print("=" * 78)
print()
print("SCORE: 3/3")
