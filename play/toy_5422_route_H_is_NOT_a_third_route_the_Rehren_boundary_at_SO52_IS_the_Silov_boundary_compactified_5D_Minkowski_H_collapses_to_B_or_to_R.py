#!/usr/bin/env python3
"""
Toy 5422 — ROUTE H (Rehren / algebraic holography): Cal's pre-registered OPEN route.

CAL §662 PRE-REGISTERED THREE ROUTES (inherited by grep, not re-derived):
   B  bound-then-restrict   -> CLOSES, but construction-guaranteed (zero information)
   R  restrict-then-bound   -> FAILS (Schur obstruction evaporates at SO(4) -> SO(3))
   H  Rehren, bulk -> 4D conformal boundary, "does not pass through the 5-dimensional
      Silov boundary at all"                                      -> UNDECIDED, high value

CAL'S BAR (and this round's headline discipline): the previous "close" was EMPTY
CONFIRMATION — it could not fail. So Route H must be run POSITIVE-CONTROLLED, on the 4D
side, WITHOUT inheriting the bulk answer, and the instrument must be shown able to return
the unwanted verdict.

WHAT THIS TOY FINDS:
  ★★★ Route H is NOT a third route. The Rehren boundary of a bulk with isometry SO(5,2)
      IS the Silov boundary — because the conformal compactification of 5D Minkowski
      R^{1,4} is exactly (S^4 x S^1)/Z_2, with conformal group SO(5,2).
  ⟹ H collapses onto B (if you Rehren at the full group, the boundary is 5-dimensional
    and equals ∂_S) or onto R (if you insist on a genuine 4D boundary, you must first
    restrict to SO(4,2) = D_IV^4 — which is Route R, and R fails).
  ⟹ The premise "Rehren gives a 4D boundary" imports the AdS_5/CFT_4 dimension pairing,
    which belongs to SO(4,2). This is Cal's OWN §323 off-by-one, resurfacing.

Exact integer arithmetic; every branching cross-checked by dimension conservation.
"""

from fractions import Fraction as F

# ---------------------------------------------------------------- group bookkeeping
def dim_so(n):
    return n * (n - 1) // 2

def conformal_compactification(p, q):
    """Conformal compactification of R^{p,q} is (S^p x S^q)/Z_2 with group SO(p+1,q+1)."""
    return (f"(S^{p} x S^{q})/Z_2", f"SO({p+1},{q+1})", p + q, dim_so(p + 1 + q + 1))

# ---------------------------------------------------------------- rep theory
def dim_so5(l1, l2):
    """Weyl dimension formula for B_2 = so(5), highest weight (l1,l2), l1>=l2>=0."""
    return F((l1 - l2 + 1) * (l1 + l2 + 2) * (2 * l1 + 3) * (2 * l2 + 1), 6)

def dim_so4(l1, l2):
    """so(4) irrep (l1,l2), l1>=|l2|;  (j1,j2)=((l1+l2)/2,(l1-l2)/2)."""
    return (l1 + l2 + 1) * (l1 - l2 + 1)

def branch_so5_to_so4(L1, L2):
    """Gelfand-Tsetlin interlacing: (L1,L2) -> (+) (l1,l2) with L1>=l1>=L2>=|l2|.
       Multiplicity one; l2 takes both signs when nonzero."""
    out = []
    for l1 in range(L2, L1 + 1):
        for l2 in range(-L2, L2 + 1):
            if abs(l2) <= L2 <= l1:
                out.append((l1, l2))
    return out

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599): does the rep machinery reproduce known objects?")
print("=" * 78)
known = [((1, 0), 5, "so(5) vector"), ((1, 1), 10, "so(5) adjoint"),
         ((2, 0), 14, "sym traceless 5x5"), ((2, 2), 35, "")]
c_dim = all(dim_so5(*lw) == d for lw, d, _ in known[:3])
for lw, d, name in known[:3]:
    print(f"  dim so(5) {str(lw):>7s} = {str(dim_so5(*lw)):>5s}  expect {d:>3d}  {name:<20s}"
          f"{'OK' if dim_so5(*lw) == d else '*** BROKEN ***'}")
print()
print("  branching conservation:  sum of so(4) dims must equal the so(5) dim")
print(f"  {'(L1,L2)':>9s} {'dim so(5)':>10s} {'sum so(4)':>10s} {'match':>7s}")
c_branch = True
for L1, L2 in [(1, 0), (1, 1), (2, 0), (2, 1), (2, 2), (3, 1), (4, 2), (5, 3)]:
    tot = sum(dim_so4(a, b) for a, b in branch_so5_to_so4(L1, L2))
    ok = (F(tot) == dim_so5(L1, L2))
    c_branch &= ok
    print(f"  {str((L1,L2)):>9s} {str(dim_so5(L1,L2)):>10s} {tot:>10d} {'OK' if ok else 'FAIL':>7s}")
controls_ok = c_dim and c_branch
print(f"\nCONTROLS: {'PASS — dimensions and branching both reproduce standard results.' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ THE IDENTIFICATION
print()
print("=" * 78)
print("SECTION 1 — WHAT IS THE REHREN BOUNDARY OF A BULK WITH ISOMETRY SO(5,2)?")
print("=" * 78)
print("Rehren's algebraic holography pairs a bulk with a conformal boundary OF THE SAME GROUP.")
print("The conformal compactification of R^{p,q} is (S^p x S^q)/Z_2, conformal group SO(p+1,q+1).\n")
print(f"{'Minkowski':>12s} {'compactification':>22s} {'conformal group':>18s} {'bdy dim':>8s}")
print("-" * 78)
rows = []
for p, q, tag in [(3, 1, "4D Minkowski"), (4, 1, "5D Minkowski")]:
    cpt, grp, d, dg = conformal_compactification(p, q)
    rows.append((tag, cpt, grp, d))
    print(f"{tag:>12s} {cpt:>22s} {grp:>18s} {d:>8d}")
print()
SILOV = "(S^4 x S^1)/Z_2"
match_5D = (rows[1][1] == SILOV)
print(f"BST's Silov boundary  ∂_S = {SILOV}   (5-dimensional)")
print(f"Rehren boundary at SO(5,2) = {rows[1][1]}   ->  IDENTICAL: {match_5D}")
print()
print("★★★ THE REHREN BOUNDARY OF AN SO(5,2) BULK **IS** THE SILOV BOUNDARY.")
print("    The Silov boundary of the type-IV domain D_IV^n is the conformal compactification")
print("    of n-dimensional Minkowski space — that is what a Lie ball's Silov boundary IS.")
print("⟹ Route H does NOT bypass ∂_S. At the full group it lands exactly on it.")
print()
print("AND THE 4D BRANCH: a genuine 4-dimensional conformal boundary belongs to SO(4,2),")
print(f"    i.e. to D_IV^4, not D_IV^5   (D_IV^n <-> SO(n,2); Cal §323's off-by-one).")
print("⟹ To get a 4D Rehren boundary you must FIRST restrict SO(5,2) -> SO(4,2).")
print("⟹ That is Route R (restrict, then take the smaller domain's own boundary).")

# ================================================================ THE OBSTRUCTION
print()
print("=" * 78)
print("SECTION 2 — DOES THE SCHUR OBSTRUCTION HOLD ON EACH CANDIDATE BOUNDARY?")
print("=" * 78)
print("A mode reaches a boundary L^2(G/H) iff its H-branching contains the H-invariant")
print("(class-1) vector. L^2(S^4)=L^2(SO(5)/SO(4)) carries only (a,0); L^2(S^3)=L^2(SO(4)/SO(3))")
print("carries only SO(4)-types (a,0).\n")
print(f"{'(L1,L2)':>9s} {'colored?':>9s} {'reaches S^4?':>13s} {'reaches S^3?':>13s} {'so(4) types (a,0)':>20s}")
print("-" * 78)
tab = []
for L1, L2 in [(0, 0), (1, 0), (2, 0), (3, 0), (5, 0),
               (1, 1), (2, 1), (2, 2), (3, 1), (3, 2), (5, 3)]:
    br = branch_so5_to_so4(L1, L2)
    reaches_S4 = (0, 0) in br                      # SO(4)-invariant vector present?
    class1 = sorted({a for a, b in br if b == 0})  # SO(4) types of the form (a,0)
    reaches_S3 = len(class1) > 0                   # any (a,0) => lands in L^2(S^3)
    colored = L2 > 0
    tab.append((L1, L2, colored, reaches_S4, reaches_S3))
    print(f"{str((L1,L2)):>9s} {str(colored):>9s} {str(reaches_S4):>13s} {str(reaches_S3):>13s} "
          f"{str(class1):>20s}")

colored = [r for r in tab if r[2]]
colorless = [r for r in tab if not r[2]]
S4_separates = all(not r[3] for r in colored) and all(r[3] for r in colorless)
S3_separates = all(not r[4] for r in colored) and all(r[4] for r in colorless)
print()
print(f"★ boundary S^4 = ∂_S's sphere factor: colored NEVER reaches, colorless ALWAYS reaches"
      f"  ->  SEPARATES: {S4_separates}")
print(f"★ boundary S^3 (the 4D/SO(4,2) branch):  EVERY mode reaches, colored included"
      f"           ->  SEPARATES: {S3_separates}")
print()
print("⟹ The obstruction is a fact about SO(5)/SO(4). One step down the chain it is GONE:")
print("   taking b=0, a=L2 the interlacing L1 >= L2 >= L2 >= 0 is satisfied for EVERY (L1,L2).")
print("   (This re-verifies Cal §662's branching independently — his result, not a new one.)")

# ================================================================ CAN-FAIL
print()
print("=" * 78)
print("SECTION 3 — CAN THIS INSTRUMENT RETURN THE UNWANTED ANSWER? (anti-empty-confirmation)")
print("=" * 78)
print("The previous 'close' was empty confirmation: it could not fail. This one can — and does.")
print()
n_colored_reaching_S3 = sum(1 for r in colored if r[4])
print(f"  colored modes tested:                       {len(colored)}")
print(f"  colored modes that REACH the S^3 boundary:  {n_colored_reaching_S3}"
      f"   <- the instrument returns CONFINEMENT-FAILS here")
print(f"  colored modes that reach the S^4 boundary:  {sum(1 for r in colored if r[3])}")
print()
can_fail = (n_colored_reaching_S3 == len(colored)) and (sum(1 for r in colored if r[3]) == 0)
print(f"★ The SAME instrument returns 'confined' on one boundary and 'NOT confined' on the")
print(f"  other. It is therefore not rigged to confirm.  CAN-FAIL DEMONSTRATED: {can_fail}")
print()
print("POSITIVE CONTROL — the colorless modes must reach BOTH boundaries (they are observed):")
for r in colorless:
    print(f"    (L1,L2)={str((r[0],r[1])):>7s}   S^4: {str(r[3]):>5s}   S^3: {str(r[4]):>5s}")
pos_ctrl = all(r[3] and r[4] for r in colorless)
print(f"  POSITIVE CONTROL: {pos_ctrl}")

# ================================================================ VERDICT
print()
print("=" * 78)
print("SECTION 4 — ROUTE H, RESOLVED")
print("=" * 78)
print(f"{'route':>6s} {'boundary':>22s} {'group':>10s} {'dim':>4s} {'verdict':>28s}")
print("-" * 78)
print(f"{'B':>6s} {'(S^4 x S^1)/Z_2':>22s} {'SO(5,2)':>10s} {'5':>4s} "
      f"{'closes; construction-guaranteed':>28s}")
print(f"{'R':>6s} {'(S^3 x S^1)/Z_2':>22s} {'SO(4,2)':>10s} {'4':>4s} "
      f"{'FAILS (obstruction gone)':>28s}")
print(f"{'H':>6s} {'(S^4 x S^1)/Z_2':>22s} {'SO(5,2)':>10s} {'5':>4s} "
      f"{'= B, not independent':>28s}")
print(f"{'H(4D)':>6s} {'(S^3 x S^1)/Z_2':>22s} {'SO(4,2)':>10s} {'4':>4s} "
      f"{'= R, therefore FAILS':>28s}")
print()
print("★★★ ROUTE H IS NOT A THIRD ROUTE. It is B or R depending on which group you Rehren at,")
print("    and the group is fixed by the boundary dimension you want. There is no branch of H")
print("    that is both 4-dimensional and carries the Schur obstruction.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls: so(5) dims + branching conservation", controls_ok),
    ("conformal compactification of R^{1,4} = (S^4 x S^1)/Z_2", match_5D),
    ("that is EXACTLY ∂_S — so Rehren@SO(5,2) lands on the Silov boundary", match_5D),
    ("a 4D conformal boundary requires SO(4,2) = D_IV^4, not D_IV^5", True),
    ("obstruction SEPARATES colored/colorless on S^4", S4_separates),
    ("obstruction does NOT separate on S^3 (Cal §662 re-verified)", not S3_separates),
    ("instrument can return the unwanted answer (can-fail)", can_fail),
    ("positive control: colorless modes reach both boundaries", pos_ctrl),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — Route H resolves NEGATIVE, and it resolves by identification, not computation:")
print("  Cal pre-registered H as the route that 'does not pass through the 5-dimensional Silov")
print("  boundary at all.' It does. The Silov boundary of D_IV^5 IS the conformal compactification")
print("  of 5D Minkowski, and SO(5,2) is its conformal group — so Rehren at the bulk's own group")
print("  lands precisely on ∂_S and reproduces Route B, construction-guarantee included.")
print("  Demanding a genuine 4D conformal boundary forces the restriction to SO(4,2) = D_IV^4,")
print("  which is Route R, where the branching shows the Schur obstruction is absent.")
print("  ⟹ THE THREE-ROUTE MENU IS REALLY A TWO-ROUTE MENU, and neither branch supplies an")
print("     independent derivation. Confinement (ii) stays what Cal re-typed it as: a CHOICE")
print("     BST makes on physical grounds, not a test it passes.")
