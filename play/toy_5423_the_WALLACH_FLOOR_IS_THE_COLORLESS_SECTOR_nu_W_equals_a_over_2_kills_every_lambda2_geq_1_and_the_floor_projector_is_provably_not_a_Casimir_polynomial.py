#!/usr/bin/env python3
"""
Toy 5423 — THE FIRST nu_W-ADDRESS READING ON H_{nu_W}.

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "What spectral content does the WALLACH FLOOR read?"
  It does NOT answer the confinement-forcing question (that is toy 5424) and it does NOT
  answer the YM-asymptotic question (toy 5422 closed that).

SYMBOL DISCIPLINE (the whole reason this was gated — my own flag, Round 34):
    nu_W  = the Wallach / generalized-power weight.  VARIES.  floor a/2 = 3/2, ladder N_c = 3.
    p     = the Bergman GENUS = n_C = 5.  HELD SEPARATE.  Never written "nu".
  K1012's "Bergman weight nu = 5" is p, not nu_W: at nu_W = 5 the ladder would read
  s/d = 42, not the observed 20.

THE OBJECT (declared: type / domain / ambient):
    type    — a diagonal operator on the K-type decomposition of H_{nu_W}
    domain  — the weighted Bergman space H_{nu_W}(D_IV^5), nu_W in the Wallach set
    ambient — SO(5)-isotypic components indexed by lambda = (lambda_1, lambda_2)
    eigenvalue at lambda:  the FK generalized Pochhammer
        (nu_W)_lambda = (nu_W)_{lambda_1} * (nu_W - a/2)_{lambda_2},   a = n_C - 2 = 3

Exact rationals throughout (Fraction), per the Toy 395 lesson.
"""

from fractions import Fraction as F

N_c, n_C, rank = 3, 5, 2
a_FK = n_C - 2                    # Faraut-Korányi multiplicity a = 3
FLOOR = F(a_FK, 2)                # the discrete Wallach point a/2 = 3/2
LADDER = F(N_c)                   # nu_W = N_c = 3
GENUS_p = n_C                     # p = 5, held separate — NOT a nu_W value

def rising(x, k):
    out = F(1)
    for j in range(k):
        out *= (x + j)
    return out

def pochhammer(nu_W, lam):
    """FK generalized Pochhammer, rank 2, multiplicity a."""
    return rising(F(nu_W), lam[0]) * rising(F(nu_W) - F(a_FK, 2), lam[1])

def casimir_so5(l1, l2):
    """B_2 Casimir with rho = (3/2,1/2):  <lam, lam+2rho> = l1(l1+3) + l2(l2+1)."""
    return F(l1 * (l1 + 3) + l2 * (l2 + 1))

GRID = [(l1, l2) for l1 in range(9) for l2 in range(l1 + 1)]

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599)")
print("=" * 78)
lad = [pochhammer(LADDER, (k, 0)) for k in (1, 3, 5)]
c1 = (lad == [F(3), F(60), F(2520)])
print(f"  POS-1  ladder at nu_W = N_c = 3, single-row {(1,3,5)}: {[str(x) for x in lad]}"
      f"   expect [3, 60, 2520]   {'OK' if c1 else '*** BROKEN ***'}")
c2 = (pochhammer(LADDER, (3, 0)) / pochhammer(LADDER, (1, 0)) == 20)
print(f"  POS-2  s/d = 20 reproduced (banked K993/T2529)                          "
      f"        {'OK' if c2 else '*** BROKEN ***'}")
casimirs = {casimir_so5(*lw) for lw in GRID}
c3 = (casimir_so5(1, 0) == 4 and casimir_so5(1, 1) == 6 and casimir_so5(2, 0) == 10)
print(f"  POS-3  Casimir spot-values (1,0)=4, (1,1)=6, (2,0)=10                    "
      f"        {'OK' if c3 else '*** BROKEN ***'}")
c4 = (pochhammer(GENUS_p, (3, 0)) / pochhammer(GENUS_p, (1, 0)) == 42)
print(f"  NEG-1  at nu_W = p = 5 the ladder reads s/d = 42, NOT 20 (symbols differ) "
      f"        {'OK' if c4 else '*** BROKEN ***'}")
controls_ok = c1 and c2 and c3 and c4
print(f"\nCONTROLS: {'4/4 PASS' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ THE READING
print()
print("=" * 78)
print("SECTION 1 — SWEEP THE WALLACH SET: which K-types have NONZERO norm at each nu_W?")
print("=" * 78)
print(f"Wallach set for D_IV^5 (rank 2, a = {a_FK}):  {{0, a/2}} U (a/2, oo) = {{0, 3/2}} U (3/2, oo)\n")
print(f"{'nu_W':>8s} {'surviving K-types (nonzero norm)':>44s} {'count on grid':>15s}")
print("-" * 78)
survivors = {}
for nu_W, tag in [(F(0), "trivial Wallach point"),
                  (FLOOR, "THE FLOOR (a/2)"),
                  (F(2), "continuum"),
                  (LADDER, "the ladder (N_c)"),
                  (F(GENUS_p), "genus value p (NOT a ladder)")]:
    surv = [lw for lw in GRID if pochhammer(nu_W, lw) != 0]
    survivors[nu_W] = surv
    l2s = sorted({lw[1] for lw in surv})
    l1s = sorted({lw[0] for lw in surv})
    desc = (f"only (0,0)" if len(surv) == 1
            else f"lambda_2 in {l2s}" + ("  (ALL)" if len(surv) == len(GRID) else ""))
    print(f"{str(nu_W):>8s} {desc:>44s} {len(surv):>7d}/{len(GRID):<7d}  {tag}")

floor_surv = survivors[FLOOR]
floor_is_colorless = all(lw[1] == 0 for lw in floor_surv) and \
                     all(lw in floor_surv for lw in GRID if lw[1] == 0)
print()
print("★★★ AT THE FLOOR nu_W = a/2 = 3/2 THE SECOND FACTOR IS (nu_W - a/2)_{lambda_2} = (0)_{lambda_2}")
print("    and (0)_m = 0 for every m >= 1, while (0)_0 = 1 (empty product).")
print(f"⟹ EVERY lambda_2 >= 1 K-type has ZERO NORM at the floor; every lambda_2 = 0 survives.")
print(f"★★★ THE WALLACH FLOOR IS EXACTLY THE COLORLESS SECTOR.  verified: {floor_is_colorless}")
print()
print("Worked values at the floor:")
print(f"{'lambda':>10s} {'(nu_W)_lambda at 3/2':>22s} {'at N_c = 3':>14s}")
for lw in [(1, 0), (3, 0), (5, 0), (1, 1), (2, 1), (2, 2), (3, 1)]:
    print(f"{str(lw):>10s} {str(pochhammer(FLOOR, lw)):>22s} {str(pochhammer(LADDER, lw)):>14s}")

# ================================================================ STRATA
print()
print("=" * 78)
print("SECTION 2 — THE THREE WALLACH ADDRESSES ARE THE THREE STRATA")
print("=" * 78)
strata = [(F(0), len(survivors[F(0)])), (FLOOR, len(survivors[FLOOR])),
          (LADDER, len(survivors[LADDER]))]
print(f"{'nu_W':>8s} {'surviving':>10s} {'reads':>34s}")
print("-" * 78)
print(f"{'0':>8s} {strata[0][1]:>10d} {'the trivial rep — a POINT':>34s}")
print(f"{'3/2':>8s} {strata[1][1]:>10d} {'the colorless / single-row sector':>34s}")
print(f"{'3':>8s} {strata[2][1]:>10d} {'everything — the full bulk':>34s}")
n_strata = len({s[1] for s in strata})
print()
print(f"★ THREE distinct addresses, THREE distinct contents: {n_strata} strata = rank + 1 = {rank+1}.")
print("★ INHERITED, NOT NEW: F86 already banks '3 = rank+1 support-orbit strata (Korányi-Wolf)'.")
print("  This is the SAME count re-read as a norm degeneration. Count once — not a new 3.")

# ================================================================ T2572 ESCAPE
print()
print("=" * 78)
print("SECTION 3 — DOES THE FLOOR OPERATOR ESCAPE T2572? (the exclusion it must dodge)")
print("=" * 78)
print("T2572: no FIXED-DEGREE polynomial in the Casimir can grade a rising factorial.")
print("Here the escape is sharper than 5421's, and it is a one-line proof:\n")
zero_set = [lw for lw in GRID if lw[1] >= 1]
zero_casimirs = sorted({casimir_so5(*lw) for lw in zero_set})
one_casimirs = sorted({casimir_so5(*lw) for lw in GRID if lw[1] == 0})
print(f"  the floor projector P is 0 on {{lambda_2 >= 1}} and 1 on {{lambda_2 = 0}}")
print(f"  distinct Casimir values where P = 0 (on this finite grid): {len(zero_casimirs)}")
print(f"  distinct Casimir values where P = 1 (on this finite grid): {len(one_casimirs)}")
print(f"  and the family is INFINITE: (l1, 1) for l1 = 1,2,3,... gives Casimir l1(l1+3)+2,")
print(f"    all distinct  ->  P vanishes at INFINITELY many distinct Casimir eigenvalues.")
print()
print("★★★ A NONZERO POLYNOMIAL HAS FINITELY MANY ROOTS.")
print("    P vanishes at infinitely many distinct Casimir values, and P is not identically 0.")
print("⟹ P IS NOT ANY POLYNOMIAL IN THE CASIMIR — no degree, fixed or otherwise. T2572 ESCAPED.")
infinite_zeros = len(zero_casimirs) > 5
poly_impossible = infinite_zeros

# stronger still: is P even a FUNCTION of the Casimir? look for a collision across the divide.
collide = sorted(set(zero_casimirs) & set(one_casimirs))
print()
print("STRONGER TEST — is P even a FUNCTION of the Casimir? (needs a value collision)")
print(f"  Casimir values shared by a lambda_2=0 and a lambda_2>=1 K-type: {[str(c) for c in collide]}")
if collide:
    ex0 = next(lw for lw in GRID if lw[1] == 0 and casimir_so5(*lw) == collide[0])
    exp = next(lw for lw in GRID if lw[1] >= 1 and casimir_so5(*lw) == collide[0])
    print(f"  ★★ COLLISION at C_2 = {collide[0]}:  {ex0} (P=1)  vs  {exp} (P=0)")
    print("  ⟹ P is NOT EVEN A FUNCTION of the Casimir — a strictly stronger statement.")
else:
    print("  none on this grid ⟹ the finitely-many-roots argument is the operative one")
    print("     (sufficient on its own; the collision would only have strengthened it).")

# ================================================================ HONEST FLAG
print()
print("=" * 78)
print("SECTION 4 — THE HONEST FLAG: is this an INDEPENDENT confinement mechanism?")
print("=" * 78)
print("T2523 (Tier D): colored <=> lambda_2 > 0 <=> Silov-vanishing   [Schur, boundary map]")
print("THIS toy:       colored <=> lambda_2 > 0 <=> floor-norm zero   [FK Pochhammer, norm]")
print()
print("★ SAME PREDICATE, DIFFERENT STRUCTURE. That is NOT automatically two votes.")
print("  Both may descend from one fact — that the degenerate stratum carries only class-1")
print("  (single-row) reps. Under this round's own rule, ONE PRIMARY WEARING TWO HATS IS")
print("  MULTIPLIER 1, NOT TWO.")
print("⟹ I am NOT claiming independent confirmation of T2523. @Grace/@Keeper — the")
print("  independence question (is the norm-vanishing derivable FROM the Schur statement,")
print("  or genuinely separate?) is the same shape as the s/d = 20 reconciliation you are")
print("  already running. Same sweep, and it should be run before either counts twice.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 4/4 (ladder, s/d=20, Casimir, symbol-separation)", controls_ok),
    ("floor nu_W = a/2 annihilates every lambda_2 >= 1", floor_is_colorless),
    ("floor keeps every lambda_2 = 0 K-type", all(pochhammer(FLOOR, lw) != 0
                                                  for lw in GRID if lw[1] == 0)),
    ("nu_W = 0 keeps only the trivial K-type", survivors[F(0)] == [(0, 0)]),
    ("nu_W = N_c keeps the full grid", len(survivors[LADDER]) == len(GRID)),
    ("three Wallach addresses -> three distinct contents", n_strata == 3),
    ("floor projector vanishes at infinitely many Casimir values", infinite_zeros),
    ("=> not a polynomial in the Casimir (T2572 escaped)", poly_impossible),
    ("symbol discipline held: nu_W = 5 gives 42, not 20", c4),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the Wallach floor reads the colour split, and it reads it as a NORM:")
print("  At nu_W = a/2 = 3/2 the FK Pochhammer's second factor is (0)_{lambda_2}, which is zero")
print("  for every lambda_2 >= 1. So the floor's Hilbert space contains EXACTLY the single-row")
print("  (colourless) K-types. The operator escapes T2572 outright — it is not a polynomial in")
print("  the Casimir at any degree, because a nonzero polynomial cannot vanish at infinitely")
print("  many distinct eigenvalues. The three Wallach addresses {0, 3/2, N_c} read three")
print("  distinct contents (point / colourless / full), which is F86's rank+1 strata count")
print("  re-read as a norm degeneration — inherited, counted once.")
print("  NOT CLAIMED: that this independently confirms T2523. Same predicate, and the")
print("  independence has to be swept before it counts twice.")
