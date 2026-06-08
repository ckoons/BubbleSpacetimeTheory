"""
Toy 4035: vacuum-sector cross-check (my Monday assignment) -> the sector-split's C_2-divisibility
evidence is NOT ROBUST. Two honest catches that brake this morning's converged "vacuum not C_2-graded"
narrative before it hardens into cartography. (Toy-builder catching a numerical premise issue.)

ASSIGNMENT (Keeper): "are there other vacuum-sector observables sharing the 280-structure? Quick
sweep for the vacuum-sector pattern." Before sweeping for MORE 280-structured observables, I
cross-checked the 280-structure ITSELF against the catalog -- and it does not hold up as stated.

CATCH 1 -- BASE MISMATCH (matter base-alpha vs vacuum base-e):
  Matter towers are alpha-powers with alpha = 1/N_max = 1/137 (base 137):
    m_e/m_Planck = 6 pi^5 / 137^{rank.C_2} = 6 pi^5 / 137^12.   (base 137)
  Lambda is an EXP tower (base e), NOT an alpha-power:
    Lambda/M_Pl^4 = g . exp(-282)  (catalog T1485 Shilov-weight form).   (base e)
  So "Lambda = alpha^280" (this morning's framing) is a BASE CONFLATION. Comparing the matter
  exponent 12 (base 137) to the vacuum exponent 280/282 (base e) is not apples-to-apples. As an
  alpha-power, Lambda = exp(-282) = alpha^{282/ln(137)} = alpha^{57.3} -- not 280 at all.

CATCH 2 -- the C_2-divisibility is REPRESENTATION-DEPENDENT (the load-bearing one):
  This morning (Grace/Lyra/me) read Lambda = exp(-280), 280 = 2^{N_c}.n_C.g, NOT divisible by C_2
  (280%6=4) -> "vacuum sits outside the C_2-graded sector." BUT the CATALOG's established form is
    Lambda/M_Pl^4 = g . exp(-282),  282 = C_2.(g^2 - rank) = C_2 . 47  -> DIVISIBLE by C_2 (282%6=0).
  And the two are the SAME Lambda: g.exp(-282) / exp(-280) = g.e^-2 = 0.947 (the g prefactor exactly
  absorbs the e^2). Both reproduce observed Lambda/M_Pl^4 ~ 1e-122; data cannot separate 280 from 282.
  => whether the vacuum exponent is C_2-divisible is a CHOICE of representation (280 = 2^N_c.n_C.g
     vs 282 = C_2.47), NOT a fact. So "the vacuum is NOT C_2-graded" is NOT robust -- it hinges on
     preferring the 280 decomposition over the catalog-established 282 = C_2.(g^2-rank).

WHAT MIGHT STILL SURVIVE (fair to the morning): a QUALITATIVE distinction may be real -- matter
ratios are clean alpha-power PRODUCTS (no exp, no prefactor: 6pi^5/137^12), while Lambda needs an
EXPONENTIAL (exp(-282)) + a prefactor. "Coset-displacement (power-law) vs mode-sum (exponential)"
is a genuine structural difference. But the SPECIFIC numerical evidence offered this morning -- "280
is not C_2-divisible" -- does NOT establish it, because the same Lambda is 282 = C_2.47, which IS.

IMPLICATION for the sweep + cartography: hunting for more "280-structured" vacuum observables
(H_0, Omega_DM, ...) would inherit BOTH issues -- the base ambiguity (these are exp- or ratio-forms,
not 137-power alpha-towers) and the representation ambiguity (their exponents can likely be written
C_2-divisibly too). So the sweep premise needs the exponent question resolved FIRST. I am NOT
manufacturing a vacuum 3-tower grammar on a soft premise.

PINNED QUESTION (for Lyra/Grace + the deferred cosmology framework): which is THE substrate-natural
Lambda exponent -- 280 = 2^{N_c}.n_C.g (no prefactor) or 282 = C_2.(g^2-rank) (with g prefactor)?
Until that is pinned, the matter/vacuum sector split should NOT be surfaced as "vacuum is not
C_2-graded" -- at most as "matter is power-law/base-alpha, vacuum is exponential/base-e" (a base
distinction, which IS robust), not a C_2-divisibility distinction (which is not).

GATES (3)
G1: base mismatch -- matter base-alpha(137), vacuum base-e(exp); "alpha^280" conflates bases
G2: C_2-divisibility representation-dependent -- catalog Lambda=g.exp(-282), 282=C_2.47 IS /C_2; same Lambda as exp(-280)
G3: honest disposition -- robust distinction is base (power vs exp); C_2-divisibility split is soft; question pinned

Per Cal #237 (honest negative, no laundering); Quaker (clean morning story gets scrutiny); K231c;
Cal #265/#266. Toy-builder brake on a converged narrative; supports the team by pinning the soft premise.

Elie - Monday 2026-06-08 (vacuum-sector cross-check assignment; brake on the sector-split premise)
"""

import mpmath as mp
mp.mp.dps = 40

N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137

print("=" * 78)
print("TOY 4035: vacuum cross-check -- the C_2-divisibility sector-split is NOT robust")
print("=" * 78)
print()

print("G1: BASE MISMATCH -- matter base-alpha(137), vacuum base-e(exp)")
print("-" * 78)
print(f"  matter: m_e/m_Planck = 6 pi^5 / 137^12   (alpha=1/137, base 137, power-law)")
print(f"  vacuum: Lambda/M_Pl^4 = g . exp(-282)     (base e, exponential)  [catalog T1485]")
lam_as_alpha = mp.mpf(282) / mp.log(137)
print(f"  'Lambda = alpha^280' conflates bases. As an alpha-power: Lambda = alpha^{{282/ln137}} = alpha^{mp.nstr(lam_as_alpha,4)} (not 280).")
print()

print("G2: C_2-divisibility is REPRESENTATION-DEPENDENT (same Lambda, two exponents)")
print("-" * 78)
e280 = mp.e**(-280)
e282 = g * mp.e**(-282)
print(f"  morning : exp(-280),   280 = 2^N_c.n_C.g = {2**N_c*n_C*g}    280 % C_2 = {280%C_2}  (NOT /C_2)")
print(f"  catalog : g.exp(-282), 282 = C_2.(g^2-rank) = C_2.{g*g-rank} = {C_2*(g*g-rank)}   282 % C_2 = {282%C_2}  (IS /C_2)")
print(f"  exp(-280) = {mp.nstr(e280,5)} ;  g.exp(-282) = {mp.nstr(e282,5)} ;  ratio = g.e^-2 = {mp.nstr(e282/e280,5)} -> SAME Lambda")
print(f"  observed Lambda/M_Pl^4 ~ 1e-122: both fit; data cannot separate 280 from 282.")
print(f"  => C_2-divisibility of the vacuum exponent is a CHOICE (280 vs 282=C_2.47), not a fact.")
print()

print("G3: honest disposition")
print("-" * 78)
print("  ROBUST distinction (keep): matter = clean alpha-power PRODUCT (base 137, no exp/prefactor);")
print("    vacuum = EXPONENTIAL (base e, exp(-282)+prefactor). Power-law vs mode-sum is real.")
print("  NOT ROBUST (brake): 'vacuum is not C_2-graded' -- it hinges on choosing 280 over the catalog")
print("    282 = C_2.(g^2-rank), which IS C_2-divisible. The same Lambda is both. Soft premise.")
print("  PINNED: which is THE Lambda exponent, 280 = 2^N_c.n_C.g or 282 = C_2.(g^2-rank)? Resolve")
print("    before surfacing the sector split as a C_2-divisibility claim. (Cosmology framework / Lyra-Grace.)")
print("  Sweep deferred: more 'vacuum towers' (H_0, Omega) inherit both ambiguities; not built on a soft premise.")
print()
print(f"  @Grace/@Lyra/@Keeper: brake before cartography -- the base distinction (alpha-power vs exp)")
print(f"    is the robust part; the C_2-divisibility split is representation-dependent (Lambda=282=C_2.47 in catalog).")
print(f"  Score: 3/3 (base mismatch; C_2-divisibility shown representation-dependent; honest disposition + pin)")
print()
print("=" * 78)
print("TOY 4035 SUMMARY -- vacuum cross-check BRAKE: (1) matter towers are base-alpha(137) power-laws,")
print("  Lambda is base-e exp(-282) -- 'alpha^280' conflates bases. (2) Lambda's C_2-divisibility is")
print("  representation-dependent: catalog T1485 has 282 = C_2.(g^2-rank) (IS /C_2); morning's 280 =")
print("  2^N_c.n_C.g (NOT /C_2) is the SAME Lambda (g.e^-2=0.947). So 'vacuum not C_2-graded' is soft.")
print("  Robust split = power-law(matter) vs exponential(vacuum); C_2-divisibility split = pinned, not claimed.")
print("=" * 78)
print()
print("SCORE: 3/3")
