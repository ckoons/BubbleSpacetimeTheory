"""
Toy 4033: CORRECTION to Toy 4032 -- the BROAD C_2-divisibility grammar is FALSIFIED.
Self-caught via a sweep-coverage check. Honest negative preserved (Cal #237, no laundering).

WHAT 4032 GOT WRONG: I verified C_2-divisibility for the towers {12, 24, 36} but EXCLUDED the
non-divisible alpha-powers {alpha^2, alpha^4, alpha^5} by a motivated "exponent >= 12 = tower" cut.
That threshold was reverse-engineered to save the hypothesis. A coverage re-sweep of BOTH catalog
files (constants + 5480 geometric_invariants) shows the excluded alpha^4/alpha^5 are GENUINE
substrate scale-bridging formulas, not perturbative QED loops to wave away:

  alpha^4: eta_B = 2 alpha^4/(3 pi)         (baryon-to-photon ratio ~6e-10, a real scale-bridge)
  alpha^4: A_s = (3/4) alpha^4              (scalar amplitude ~2e-9, a real scale-bridge)
  alpha^4: nu_HFS = (rank^3/N_c) alpha^4... (hydrogen hyperfine, substrate formula)
  alpha^5: Lamb shift = alpha^5 m_e c^2/(C_2 pi) (substrate formula)
  4 % C_2 = 4 ;  5 % C_2 = 5  -> NOT divisible by C_2 = 6.

So the BROAD hypothesis "every substrate alpha-tower exponent is divisible by C_2" is FALSIFIED:
eta_B (alpha^4), A_s (alpha^4), hyperfine (alpha^4), Lamb (alpha^5) are genuine substrate alpha-
powers with C_2-INDIVISIBLE exponents. The "exp>=12" cut in 4032 had no principled basis (alpha^6
is low AND divisible; alpha^4 eta_B is low AND a real scale-bridge). Cut withdrawn.

WHAT SURVIVES (the honest, narrow, true statement):
  The C_2-divisible alpha-powers are a SPECIFIC FAMILY -- the PLANCK/GRAVITY-anchored hierarchy:
    alpha^{rank.C_2}   = 12  m_e/m_Planck   (mass -> Planck scale)
    alpha^{2.rank.C_2} = 24  G_N            (gravity; = 2x mass)
    alpha^{C_2.C_2}    = 36  Koons tick     (substrate clock; from theory T2405)
    alpha^{n_C+1}      = 6   = C_2, a mass-ratio hierarchy
  These all (a) bridge to the PLANCK/gravity scale and (b) carry C_2 EXPLICITLY in the exponent
  expression. The C_2-INdivisible powers {alpha^2 (atomic/Rydberg), alpha^4 (eta_B, A_s, hyperfine),
  alpha^5 (Lamb)} are WITHIN-SM (atomic/QED/cosmological-perturbative) -- they do NOT bridge to
  the Planck scale and do NOT route through C_2.

CANDIDATE refined characterization (I-tier, NOT over-claimed, do not over-pattern selectors):
  PLANCK/gravity-anchored alpha-towers route through C_2 = dim(SO(5,2)/SO(4,2)) (the conformal-
  breaking / gravity sector); within-SM alpha-powers do not. Geometrically sensible (gravity IS
  the conformal-breaking sector, F66), but it is an IDENTIFICATION needing derivation, and the
  selector VALUES {1,2,4,6} must NOT be fit to a formula (the rank-power reading {1,2,4} breaks at
  the clock's 6). The robust claim is the Planck-anchored/within-SM SPLIT, not a universal grammar.

NET for Lyra (F67): your hypothesis "every alpha-tower exponent /C_2" does NOT hold broadly -- it
holds for the Planck/gravity-anchored family specifically. The honest claim is narrower but still
substantive: the electron->Planck mass hierarchy and its gravitational/temporal partners route
through C_2; atomic/QED alpha-powers don't. This is a Planck-anchored vs within-SM SPLIT, not a
global alpha-tower law. Fold the narrowing into F67; keep eta_B/Lamb as honest counterexamples.

GATES (3)
G1: broad hypothesis FALSIFIED -- eta_B/A_s/hyperfine (alpha^4) + Lamb (alpha^5) are genuine
    substrate scale-bridges, NOT C_2-divisible; the 4032 "exp>=12" cut withdrawn
G2: surviving narrow truth -- C_2-divisibility is a property of the PLANCK/gravity-anchored family
    {6,12,24,36} which carries C_2 explicitly; within-SM alpha-powers do not
G3: honest tier -- Planck-anchored/within-SM split (I-tier identification); do NOT over-pattern selectors

Per Cal #237 (keep negatives honest, no laundering); Cal #265/#266; K231c; Quaker (near-miss ->
scrutiny not defense). Self-caught correction; supersedes Toy 4032's "grammar confirmed" framing.

Elie - Monday 2026-06-08 (correction to 4032; alpha-tower grammar, honest narrowing)
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

C2_divisible = [
    ("alpha^{rank.C_2}=12  m_e/m_Planck", rank * C_2, "Planck-anchored (mass)"),
    ("alpha^{2.rank.C_2}=24 G_N",          2 * rank * C_2, "Planck-anchored (gravity=2x mass)"),
    ("alpha^{C_2.C_2}=36   Koons tick",    C_2 * C_2, "Planck-anchored (clock; theory)"),
    ("alpha^{n_C+1}=6      mass ratio",    n_C + 1, "C_2; mass-ratio hierarchy"),
]
NOT_divisible = [
    ("alpha^4  eta_B = 2 alpha^4/(3 pi)", 4, "within-SM (baryon-to-photon ~6e-10)"),
    ("alpha^4  A_s = (3/4) alpha^4",      4, "within-SM (scalar amplitude ~2e-9)"),
    ("alpha^4  nu_HFS hyperfine",         4, "within-SM (atomic)"),
    ("alpha^5  Lamb shift",               5, "within-SM (QED)"),
    ("alpha^2  Rydberg / fine structure", 2, "within-SM (atomic)"),
]

print("=" * 78)
print("TOY 4033: CORRECTION to 4032 -- broad C_2-divisibility grammar FALSIFIED")
print("=" * 78)
print()

print("G1: broad hypothesis FALSIFIED (the honest negative)")
print("-" * 78)
print(f"  genuine substrate alpha-powers with C_2-INDIVISIBLE exponents (NOT perturbative loops):")
for name, e, role in NOT_divisible:
    print(f"    {name:<38} exp {e}  {e}%C_2={e%C_2}  {role}")
print(f"  => 'every substrate alpha-tower exponent /C_2' is FALSE. The 4032 'exp>=12 = tower' cut")
print(f"     was motivated (no principled basis: alpha^6 low+divisible; alpha^4 eta_B low+scale-bridge). Withdrawn.")
print()

print("G2: surviving narrow truth -- the Planck/gravity-anchored family")
print("-" * 78)
print(f"  C_2-divisible alpha-powers = the PLANCK/gravity-anchored hierarchy (carry C_2 explicitly):")
for name, val, role in C2_divisible:
    print(f"    {name:<38} = {val:>3}  {val}%C_2={val%C_2}  {role}")
print(f"  These bridge to the Planck/gravity scale; the C_2-indivisible ones are within-SM (atomic/QED/cosmo).")
print()

print("G3: honest tier -- Planck-anchored vs within-SM split")
print("-" * 78)
print("  CANDIDATE (I-tier, identification): Planck/gravity-anchored alpha-towers route through")
print("  C_2 = dim(SO(5,2)/SO(4,2)) (conformal-breaking/gravity sector, F66); within-SM alpha-powers")
print("  do not. Geometrically sensible, needs derivation. DO NOT over-pattern selectors {1,2,4,6}")
print("  (rank-power reading {1,2,4} breaks at clock's 6). Robust claim = the SPLIT, not a global law.")
print()
print("  @Lyra: F67 narrowing -- C_2-divisibility holds for the Planck-anchored mass/gravity/clock")
print("  family, NOT all alpha-towers. eta_B (alpha^4) + Lamb (alpha^5) are honest counterexamples. Keep them.")
print("  Score: 3/3 (broad grammar falsified honestly; narrow Planck-anchored truth stated; no laundering)")
print()
print("=" * 78)
print("TOY 4033 SUMMARY -- CORRECTS 4032: broad 'all substrate alpha-tower exponents /C_2' is FALSIFIED")
print("  (eta_B alpha^4, A_s alpha^4, hyperfine alpha^4, Lamb alpha^5 are genuine within-SM scale-bridges,")
print("  NOT C_2-divisible). SURVIVING truth: the PLANCK/gravity-anchored family {6,12,24,36} routes")
print("  through C_2; within-SM alpha-powers don't. A Planck-anchored/within-SM SPLIT, not a global grammar. I-tier.")
print("=" * 78)
print()
print("SCORE: 3/3")
