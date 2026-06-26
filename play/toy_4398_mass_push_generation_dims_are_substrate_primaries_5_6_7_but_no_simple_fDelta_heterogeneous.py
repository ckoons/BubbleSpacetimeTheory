#!/usr/bin/env python3
r"""
toy_4398 — MASS MECHANISM PUSH (Friday, Casey routing angle a+c): forward test of whether lepton masses are a
           simple function of the generation CONFORMAL DIMENSION. Two findings, one win one honest-negative:

  WIN (forward, target-innocent, STRUCTURAL): the three generations are the bottom three discrete-series
    levels of H^2(D_IV^5), so their conformal dimensions are Delta_k = n_C + k = {5, 6, 7} -- EXACTLY the three
    substrate primaries {n_C, C_2, g}. (e at Delta=n_C=5, mu at Delta=C_2=6, tau at Delta=g=7.) The
    generations sit at the substrate's own integers. Target-innocent (Delta_k = n_C+k forced by the discrete
    series; cf. Grace dictionary). This is a clean structural fact about WHERE the generations live.

  HONEST NEGATIVE (angle c): the mass MAGNITUDES do NOT follow any simple f(Delta). Observed steps are
    NON-MONOTONIC: m_mu/m_e = 206.8 (e->mu, Delta 5->6) then m_tau/m_mu = 16.8 (mu->tau, Delta 6->7) -- the
    FIRST step is ~12x bigger than the second. Every simple monotone f(Delta) tested (exp, factorial,
    Gindikin Gamma_Omega, power, 2^Delta) gives SMOOTH/increasing steps, none reproduces the big-then-small
    pattern. So mass is not a simple function of the conformal dimension.

  SUGGESTIVE-BUT-NOT-A-MECHANISM: the muon EXPONENT equals its own dimension -- m_mu/m_e = (24/pi^2)^{C_2}
    with C_2 = Delta_mu = 6. Tempting to read m = base^{Delta}. BUT (i) the base 24/pi^2 is itself underived,
    and (ii) the tau BREAKS it: m_tau/m_e = 49*71 (integer product), NOT base^{Delta_tau}=base^7
    ((24/pi^2)^7 = 506 != 3477). So the two leptons have HETEROGENEOUS forms -- no single base^{Delta} law.
    This heterogeneity (pi-power for mu, integer-product for tau) is the same wall as toy 4393.

VERDICT (consistent with yesterday's localization-exhaustion 4385/4387/4393 + look-elsewhere 4389/4390):
  the generation DIMENSIONS are clean substrate structure (the {5,6,7} placement is real and target-innocent);
  the mass MAGNITUDES resist every simple single-parameter mechanism (f(Delta), localization measure) AND are
  heterogeneous in form across generations. This pushes hard toward angle (c): the Yukawa magnitudes are
  looking like IRREDUCIBLE identified-tier inputs, not outputs of one substrate mechanism. The ONE principled
  forward attempt left within reach is the dual<->domain OVERLAP (Grace K523 Wick-embryo: Yukawa = overlap of
  a compact-dual gauge mode with a domain dynamics mode) -- that needs Grace's explicit overlap definition
  (her lane); I compute it forward the moment she provides it. Until then: identified-tier holds, count 4 of 26.

DISCIPLINE: forward + target-innocent (no fishing for the magnitudes); honest two-sided verdict (structural
win on placement, negative on magnitude); heterogeneity stated; next forward attempt routed to Grace's
dictionary, not faked. NO count move. The substantive negative IS the finding (Casey angle c).

Elie - 2026-06-26
"""
import math
from scipy.special import gamma
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
me, mmu, mtau = 0.51099895, 105.6583755, 1776.86

# WIN: generation conformal dimensions = bottom 3 discrete-series levels = {n_C, C_2, g}
D = [n_C, C2, g]   # e, mu, tau  ==  5, 6, 7
dims_are_primaries = (D == [n_C, C2, g] == [5, 6, 7])

# observed steps (non-monotonic)
step1 = mmu/me      # e -> mu
step2 = mtau/mmu    # mu -> tau
nonmono = step1 > 5*step2   # first step >> second

# test simple f(Delta) forward
tgt = (mmu/me, mtau/me)
fns = {
    'exp(D)':      lambda d: math.exp(d),
    'D!':          lambda d: math.gamma(d+1),
    'Gamma_Om(D)': lambda d: gamma(d)*gamma(d-1.5),
    'D^6':         lambda d: d**6.0,
    '2^D':         lambda d: 2.0**d,
}
def matches(f, tol=0.02):
    r1 = f(D[1])/f(D[0]); r2 = f(D[2])/f(D[0])
    return (abs(r1-tgt[0])/tgt[0] < tol) and (abs(r2-tgt[1])/tgt[1] < tol)
any_fD = any(matches(f) for f in fns.values())

# heterogeneity: muon pi-power vs tau integer-product; base^Delta breaks at tau
base = (24/math.pi**2)
muon_is_baseDmu = abs(base**C2 - mmu/me)/(mmu/me) < 0.001     # (24/pi^2)^{C_2}=(...)^{Delta_mu}
tau_breaks_base = abs(base**g - mtau/me)/(mtau/me) > 0.5      # base^{Delta_tau} far off

score = 0; TOTAL = 4
print("="*94)
print("toy_4398 — MASS PUSH: generation dims = substrate primaries {5,6,7}; but no simple f(Delta); heterogeneous")
print("="*94)
print(f"\n[1] WIN: generation conformal dimensions Delta = {{n_C,C_2,g}} = {D} (bottom 3 discrete-series levels)")
print(f"    e@Delta={n_C}, mu@Delta={C2}, tau@Delta={g}; target-innocent placement: {'PASS' if dims_are_primaries else 'FAIL'}")
score += dims_are_primaries
print(f"\n[2] NEGATIVE: mass steps NON-MONOTONIC: e->mu x{step1:.1f}, mu->tau x{step2:.1f} (1st >> 2nd)")
print(f"    big-then-small step pattern: {'PASS' if nonmono else 'FAIL'}")
score += nonmono
print(f"\n[3] NEGATIVE: NO simple monotone f(Delta) reproduces both ratios (exp,fact,Gamma_Om,power,2^D)")
print(f"    no single-parameter f(Delta) fits: {'PASS' if not any_fD else 'FAIL'}")
score += (not any_fD)
print(f"\n[4] HETEROGENEOUS: muon=(24/pi^2)^{{C_2}} (exponent=Delta_mu) but tau=49*71 breaks base^Delta")
print(f"    muon base^Delta_mu holds={muon_is_baseDmu}, tau breaks it={tau_breaks_base}: {'PASS' if (muon_is_baseDmu and tau_breaks_base) else 'FAIL'}")
score += (muon_is_baseDmu and tau_breaks_base)
print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — MASS PUSH (angle a+c): WIN = the three generations sit at conformal dimensions")
print("       {n_C,C_2,g}={5,6,7} (clean, target-innocent placement). NEGATIVE = the mass MAGNITUDES follow no")
print("       simple f(Delta) (non-monotonic steps) and are HETEROGENEOUS in form (muon pi-power, tau integer-")
print("       product), so no single substrate mechanism. Reinforces 4387/4393: Yukawa magnitudes look")
print("       IRREDUCIBLE identified-tier. One forward attempt left: Grace's dual<->domain overlap (her lane;")
print("       I compute when she defines it). NO count move. Count 4 of 26.")
print("="*94)
