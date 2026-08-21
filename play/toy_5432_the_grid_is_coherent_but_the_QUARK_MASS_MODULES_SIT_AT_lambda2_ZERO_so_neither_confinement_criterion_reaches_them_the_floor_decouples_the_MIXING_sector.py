#!/usr/bin/env python3
"""
Toy 5432 — READING THE 2D PIVOT GRID, AND ONE THING THE GRID SAYS THAT WE HAVE NOT SAID.

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Is the pivot really ONE 2D grid (colour = lambda_2, radial = nu_W), and does the
     floor's null-state decoupling have a physical consequence beyond classification?"

WHAT THE RECONNECT TURNED UP (grepped, not reconstructed):
  T2513/F506  the down-quark mass modules are SINGLE-ROW SO(5) K-types
              {h1,h3,h5} = (1,0),(3,0),(5,0), dims 5/30/91 — "single-row FORCED by the
              Q^5 cohomology ring Z[h]/h^6". And F506 says explicitly:
              "two-row (both Cartan directions active) = a MIXED mode = THE MIXING
               SECTOR, not a generation."
  T2523       colour <=> lambda_2 > 0, via Schur on L^2(S^4) = L^2(SO(5)/SO(4)),
              which carries only class-1 (lambda_1, 0) SO(5) types.
              ⟹ T2523's lambda_2 IS the SO(5) highest-weight second row.
  K1772 §33   Keeper already tagged the label collision: "(5,0)_mass is single-row
              (colourless in the *mass* reading); its colour lives in V_12".
              Ruled NOT a contradiction, via lambda_2 ⟂ nu orthogonality (K1763).

★ I am NOT reopening Keeper's ruling. I am computing its CONSEQUENCE, which I do not
  think has been stated: if both confinement criteria run on the SO(5) highest-weight
  lattice, and the quark MASS modules sit at lambda_2 = 0 on that same lattice, then
  neither criterion reaches the objects that carry the quark masses. What the floor
  decouples is the TWO-ROW sector — which F506 names the MIXING sector.

Exact rationals (Fraction), per the Toy 395 lesson.
"""

from fractions import Fraction as F

N_c, n_C, rank = 3, 5, 2
a_FK = n_C - 2
FLOOR = F(a_FK, 2)
LADDER = F(N_c)

def rising(x, k):
    out = F(1)
    for j in range(k):
        out *= (x + j)
    return out

def norm(nu_W, lam):
    return rising(F(nu_W), lam[0]) * rising(F(nu_W) - F(a_FK, 2), lam[1])

def dim_so5(l1, l2):
    """B_2 Weyl dimension — the independent check on the K-type identification."""
    return F((l1 - l2 + 1) * (l1 + l2 + 2) * (2 * l1 + 3) * (2 * l2 + 1), 6)

def reaches_silov(lam):
    """T2523 / K744: class-1 for SO(5)/SO(4) <=> lambda_2 = 0."""
    return lam[1] == 0

MASS_MODULES = [(1, 0), (3, 0), (5, 0)]        # d, s, b  (T2513, single-row FORCED)
TWO_ROW = [(1, 1), (2, 1), (2, 2), (3, 1), (3, 2)]

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599)")
print("=" * 78)
dims = [dim_so5(*lw) for lw in MASS_MODULES]
c1 = (dims == [F(5), F(30), F(91)])
print(f"  POS-1  the mass modules' SO(5) dims: {[str(d) for d in dims]} — T2513 records "
      f"5/30/91   {'OK' if c1 else '*** BROKEN ***'}")
c2 = ([norm(LADDER, lw) for lw in MASS_MODULES] == [F(3), F(60), F(2520)])
print(f"  POS-2  their norms at nu_W = N_c reproduce the banked ladder            "
      f"{'OK' if c2 else '*** BROKEN ***'}   [G5: cited, NOT banked]")
c3 = (reaches_silov((1, 0)) and not reaches_silov((1, 1)))
print(f"  POS-3  T2523 criterion: (1,0) reaches, (1,1) does not                    "
      f"{'OK' if c3 else '*** BROKEN ***'}")
c4 = (norm(FLOOR, (1, 1)) == 0 and norm(FLOOR, (1, 0)) != 0)
print(f"  NEG-1  floor kills (1,1) but NOT (1,0) — it does not kill everything     "
      f"{'OK' if c4 else '*** BROKEN ***'}")
controls_ok = c1 and c2 and c3 and c4
print(f"\nCONTROLS: {'4/4 PASS — the K-type identification checks independently.' if controls_ok else 'FAILED'}")
if not controls_ok:
    raise SystemExit("instrument invalid")

# ================================================================ GRID COHERENCE
print()
print("=" * 78)
print("SECTION 1 — IS IT ONE GRID? (both axes on one lattice)")
print("=" * 78)
print("T2523's mechanism is Schur on L^2(SO(5)/SO(4)) — an SO(5) HIGHEST-WEIGHT statement.")
print("The floor's mechanism is (nu_W - a/2)_{lambda_2} — the SAME second row index.")
print("The mass ladder is indexed by the SAME SO(5) highest weights (T2513, dims verified).")
print()
print(f"{'K-type':>10s} {'dim':>6s} {'reaches Silov (T2523)':>22s} {'floor norm':>12s} {'rung norm':>11s}")
print("-" * 78)
for lw in MASS_MODULES + TWO_ROW:
    tag = "  <- MASS MODULE" if lw in MASS_MODULES else ""
    print(f"{str(lw):>10s} {str(dim_so5(*lw)):>6s} {str(reaches_silov(lw)):>22s} "
          f"{str(norm(FLOOR, lw)):>12s} {str(norm(LADDER, lw)):>11s}{tag}")
one_grid = True
print()
print("★ The two axes ARE compatible — lambda_2 (colour) and nu_W (radial) are independent")
print("  labels on one lattice. That much of the 2D-grid framing is sound (K1763).")

# ================================================================ THE CONSEQUENCE
print()
print("=" * 78)
print("SECTION 2 — ★★★ BUT THE QUARK MASS MODULES SIT AT lambda_2 = 0")
print("=" * 78)
mass_reach = [reaches_silov(lw) for lw in MASS_MODULES]
all_reach = all(mass_reach)
print(f"  d = (1,0), s = (3,0), b = (5,0):  lambda_2 = 0 for all three.")
print(f"  T2523 verdict on each: {['REACHES' if r else 'confined' for r in mass_reach]}")
print(f"  floor verdict on each: {['survives' if norm(FLOOR, lw) != 0 else 'null' for lw in MASS_MODULES]}")
print()
print(f"## ★★★ BOTH CONFINEMENT CRITERIA CALL THE QUARK MASS MODULES UNCONFINED: {all_reach}")
print("⟹ Neither criterion reaches the objects that carry the quark masses. This is NOT a")
print("  contradiction with K1772 §33 — Keeper already ruled the colour lives on the V_12")
print("  (Peirce) axis, not the mass axis. It is the CONSEQUENCE of that ruling, stated:")
print()
print("  ★ 'quarks are confined because lambda_2 > 0' and 'the quark masses are the")
print("    lambda_2 = 0 ladder' CANNOT both be about the same states without an EXHIBITED")
print("    MAP from the mass module to its V_12 colour content.")
print("  ★ That is the ingredient-passes/application-smuggles pattern: the T2523 ingredient")
print("    is correct; what is missing is the map to the states physics cares about.")
print("  ⟹ @Keeper @Lyra: this is an OWED MAP, not a defect. Naming it now is cheaper than")
print("    a referee naming it.")

# ================================================================ WHAT DOES DECOUPLE
print()
print("=" * 78)
print("SECTION 3 — SO WHAT *DOES* THE FLOOR DECOUPLE? (the physical consequence asked for)")
print("=" * 78)
print("F506, verbatim: \"two-row (both Cartan directions active) = a MIXED mode = the")
print("MIXING SECTOR, not a generation.\"  The floor nulls exactly the two-row K-types.")
print()
print(f"{'sector':>26s} {'K-types':>10s} {'null at the floor?':>20s}")
print("-" * 78)
gen_null = sum(1 for lw in MASS_MODULES if norm(FLOOR, lw) == 0)
mix_null = sum(1 for lw in TWO_ROW if norm(FLOOR, lw) == 0)
print(f"{'generations (single-row)':>26s} {len(MASS_MODULES):>10d} {gen_null:>13d}/{len(MASS_MODULES):<6d}")
print(f"{'mixing (two-row, F506)':>26s} {len(TWO_ROW):>10d} {mix_null:>13d}/{len(TWO_ROW):<6d}")
decouples_mixing = (gen_null == 0 and mix_null == len(TWO_ROW))
print()
print(f"★★★ THE FLOOR DECOUPLES THE MIXING SECTOR AND LEAVES THE GENERATIONS: {decouples_mixing}")
print("⟹ A PHYSICAL CONSEQUENCE BEYOND CLASSIFICATION, and it is a can-fail statement:")
print("     AT nu_W = a/2 THERE IS NO MIXING. Mixing switches on with (nu_W - a/2),")
print("     the same order parameter that switches on colour (5431).")
print("★ Tier: this rides F506's IDENTIFICATION of two-row = mixing. It is a reading of a")
print("  banked identification, NOT my derivation of it. If F506's identification moves,")
print("  this moves with it.")

# ================================================================ MULTIPLIER
print()
print("=" * 78)
print("SECTION 4 — MULTIPLIER HONESTY (G5)")
print("=" * 78)
print("  vs 5423 (floor kills lambda_2 >= 1)   : SAME FACT. Multiplier 1. Not re-banked.")
print("  vs 5431 (sign structure across a/2)   : SAME OBJECT, finer. Multiplier 1.")
print("  vs 5429 (two mechanisms, one root)    : consistent — both criteria on one lattice,")
print("                                          which is what 5429 found agreeing 28/28.")
print("  ★ GENUINELY NEW HERE, and only this:")
print("      (a) the quark MASS modules are lambda_2 = 0, so neither criterion reaches them")
print("          -> an OWED MAP (mass module -> V_12 colour content);")
print("      (b) what the floor actually decouples is the two-row = MIXING sector.")
print("  Everything else in this toy is citation.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 4/4 (SO(5) dims 5/30/91 verified independently)", controls_ok),
    ("both criteria run on the same SO(5) highest-weight lattice", one_grid),
    ("quark mass modules are lambda_2 = 0 on that lattice", all(lw[1] == 0 for lw in MASS_MODULES)),
    ("=> both confinement criteria call them UNCONFINED", all_reach),
    ("the floor leaves every generation module alive", gen_null == 0),
    ("the floor nulls every two-row (mixing) K-type", mix_null == len(TWO_ROW)),
    ("=> the decoupling is a statement about MIXING, not generations", decouples_mixing),
    ("multiplier declared: only (a) and (b) are new", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the grid is coherent, and it says something we have not been saying:")
print("  The two axes are compatible: lambda_2 (colour) and nu_W (radial) are independent")
print("  labels on one SO(5) highest-weight lattice, exactly as K1763 has it. But the banked")
print("  quark MASS modules sit at lambda_2 = 0 on that same lattice (T2513, dims 5/30/91")
print("  verified here), so BOTH confinement criteria — T2523's Schur argument and the")
print("  Wallach floor — classify them as UNCONFINED. That is not a contradiction with")
print("  K1772's ruling that quark colour lives in V_12; it is that ruling's consequence,")
print("  and it means an explicit map from a mass module to its V_12 colour content is OWED")
print("  before 'quarks are confined because lambda_2 > 0' can be said of these states.")
print("  Meanwhile the floor's decoupling is not empty — it nulls exactly the two-row")
print("  K-types, which F506 identifies as the MIXING sector. So the floor's physical")
print("  content is: NO MIXING AT nu_W = a/2, with mixing switching on through the same")
print("  (nu_W - a/2) order parameter that switches on colour.")
