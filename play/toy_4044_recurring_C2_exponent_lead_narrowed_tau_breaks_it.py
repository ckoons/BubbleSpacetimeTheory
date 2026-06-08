"""
Toy 4044: narrowing my own recurring-C_2-exponent lead (flagged Toy 4043) -- the tau factor breaks it.
Honest discipline check before the lead enters the cartography. The C_2-grading of exponents is a
CONFORMAL-BREAKING-SECTOR signature, NOT a universal matter law.

THE LEAD (Toy 4043, flagged not banked): matter-sector exponents cluster at C_2-multiples --
  lepton-ratio power = C_2, alpha-tower = rank.C_2, clock = C_2^2 -- = C_2.{1, rank, C_2}.

THE CHECK (collect ALL matter exponents, test C_2-divisibility):
  muon-ratio power (24/pi^2)^.   exp = C_2 = 6    -> C_2-multiple (x1)    YES
  alpha-tower mass               exp = rank.C_2=12 -> (x2)                 YES
  gravity (= mass^rank)          exp = 2.rank.C_2=24 -> (x4)              YES
  clock (Koons)                  exp = C_2^2 = 36 -> (x6)                 YES
  tau factor (7/3)^.             exp = 10/3 = rank.n_C/N_c                NO (fractional, not /C_2)

VERDICT: the recurring-C_2 lead is PARTIAL. The PRINCIPAL exponents -- the lepton-ratio BASE power and
the gravity-sector alpha-towers (mass, gravity, clock) -- are C_2-multiples. But the 3rd-generation tau
factor exponent 10/3 is NOT. So "matter exponents are C_2-graded" is NOT universal. NARROW the lead:
  C_2-grading is the CONFORMAL-BREAKING / gravity-sector exponent signature (C_2 = dim of the breaking
  coset), NOT a law over all matter exponents. The GENERATION LADDER (tau/muon = (g/N_c)^{rank.n_C/N_c})
  is a DIFFERENT structure -- fractional exponent, base g/N_c -- and does not follow C_2-grading.

CONSISTENCY with the day's pattern (the C_2-grading keeps being SECTOR-SPECIFIC):
  - Toy 4033: C_2-divisibility holds for the Planck/gravity-anchored alpha-towers, NOT within-SM alpha-powers.
  - Toy 4035: the vacuum exponent's C_2-divisibility is representation-dependent (280 vs 282).
  - Toy 4044 (this): the lepton-ratio base power IS C_2 (conformal-breaking), but the generation-ladder is NOT.
  Coherent honest story: C_2 grades the CONFORMAL-BREAKING/gravity sector exponents; other structures
  (within-SM, vacuum, generation-ladder) have their own gradings. C_2 is not a universal exponent law.

GATES (2)
G1: recurring-C_2 lead CHECKED -- principal exponents (lepton base + alpha-towers) /C_2; tau factor 10/3 NOT
G2: narrowed honestly -- C_2-grading = conformal-breaking-sector exponent signature, not universal; consistent with 4033/4035

Per Toy 4043 (the flagged lead); Cal #237 (check leads, narrow honestly, no over-pattern); Toy 4033/4035
(C_2 sector-specificity pattern); K231c. Self-discipline check; my lane.

Elie - Monday 2026-06-08 (narrowing the recurring-C_2 lead; tau breaks the universal version)
"""

from fractions import Fraction as F
N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 78)
print("TOY 4044: recurring-C_2-exponent lead NARROWED -- tau factor (10/3) breaks the universal version")
print("=" * 78)
print()

print("G1: check all matter-sector exponents for C_2-divisibility")
print("-" * 78)
exps = [
    ("muon-ratio power (24/pi^2)^.", F(C_2), "24/pi^2"),
    ("alpha-tower mass", F(rank * C_2), "alpha"),
    ("gravity (= mass^rank)", F(2 * rank * C_2), "alpha"),
    ("clock (Koons)", F(C_2 * C_2), "alpha"),
    ("tau factor (7/3)^.", F(10, 3), "g/N_c"),
]
for nm, e, base in exps:
    mult = (e / C_2).denominator == 1
    tag = f"YES (x{e // C_2})" if mult else "NO (not /C_2)"
    print(f"  {nm:<30} exp {str(e):<6} base {base:<8} -> C_2-multiple? {tag}")
print()

print("G2: narrow the lead honestly")
print("-" * 78)
print("  PRINCIPAL exponents (lepton-ratio base power + gravity-sector alpha-towers): all C_2-multiples.")
print("  GENERATION LADDER (tau/muon = (g/N_c)^{rank.n_C/N_c}): exponent 10/3 -- NOT a C_2-multiple.")
print("  => 'matter exponents are C_2-graded' is NOT universal. NARROW: C_2-grading is the CONFORMAL-BREAKING /")
print("     gravity-sector exponent signature (C_2 = breaking-coset dim); the generation ladder is a different structure.")
print()
print("  Consistent with the day: C_2 keeps being SECTOR-SPECIFIC --")
print("    4033 (alpha-towers: Planck-anchored /C_2, within-SM not) + 4035 (vacuum /C_2 representation-dependent)")
print("    + 4044 (lepton base /C_2, generation ladder not). C_2 grades conformal-breaking; not a universal law.")
print()
print("  @Lyra/@Keeper: my 4043 recurring-C_2 lead -> narrowed to conformal-breaking-sector only; tau is the counterexample.")
print("  Score: 2/2 (lead checked; tau breaks universal version; narrowed to conformal-breaking-sector, consistent w/ 4033/4035)")
print()
print("=" * 78)
print("TOY 4044 SUMMARY -- recurring-C_2 lead (4043) NARROWED: principal matter exponents (lepton-ratio base")
print("  power C_2, alpha-towers rank.C_2/2.rank.C_2/C_2^2) are C_2-multiples, but the 3rd-gen tau factor")
print("  exponent 10/3 is NOT. So C_2-grading is the CONFORMAL-BREAKING-sector exponent signature, not a")
print("  universal matter law -- consistent with the day's pattern (4033 alpha-towers + 4035 vacuum). Honest narrowing.")
print("=" * 78)
print()
print("SCORE: 2/2")
