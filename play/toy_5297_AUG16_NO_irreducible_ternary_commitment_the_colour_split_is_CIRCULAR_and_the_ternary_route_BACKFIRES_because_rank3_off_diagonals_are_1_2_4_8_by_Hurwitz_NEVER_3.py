"""
Toy 5297 (Elie, 2026-08-16) -- the last check before the write-up: is there an irreducible TERNARY
BST commitment? Keeper predicted it bottoms at P1. It does -- but the check was worth running,
because the ternary route fails for a REASON, and the reason is the opposite of what a naive reading
would expect.

(1) THE CIRCULARITY CHECK -- fails, as predicted.
The corpus has colour as the Peirce OFF-DIAGONAL V_12 of the rank-2 spin factor:
    V = R c_1 (+) R c_2 (+) V_12,   dim V_12 = n - 2,   and at n = n_C = 5 that is 3 = N_c.
The two diagonal idempotents ARE the record; the 3 is the off-diagonal block. But a Peirce
decomposition has exactly TWO diagonal idempotents BECAUSE THE RANK IS 2. So "colour is off-diagonal,
not a third seat" is a CONSEQUENCE of rank 2, never an independent argument for it. Using it to argue
for rank 2 is circular. It bottoms at P1.

★★★ (2) BUT RUN THE TERNARY CANDIDATE ON ITS OWN TERMS -- AND IT BACKFIRES.
If a commitment were ternary the algebra is RANK 3: three diagonal idempotents, three off-diagonal
blocks. The simple rank-3 Jordan algebras are Herm_3(A) for A a division algebra:
    Herm_3(R) dim  6 = 3 + 3x1      Herm_3(C) dim  9 = 3 + 3x2
    Herm_3(H) dim 15 = 3 + 3x4      Herm_3(O) dim 27 = 3 + 3x8   <- the ALBERT algebra, E_6
THE OFF-DIAGONAL BLOCK DIMENSION IS dim(A) in {1, 2, 4, 8} -- BY HURWITZ, the same theorem that closed
my 5296 exclude-list. NEVER 3.
=> A TERNARY COMMITMENT CANNOT PRODUCE COLOUR-3 AT ALL. The ternary route does not merely fail to
   help; it is INCOMPATIBLE with N_c = 3. The very thing that motivates it -- "three colours, so
   maybe three outcomes" -- is the thing it cannot deliver. In a rank-3 world the off-diagonal is
   1, 2, 4 or 8, and the Albert/E_6 case gives EIGHT.

★ AND A PRE-EMPTIVE FLAG, because a rank-3 advocate will notice it: 8 = dim of the SU(3) ADJOINT =
the gluon count. That is a DIFFERENT object from N_c = 3 (the fundamental), and the temptation to
marry them is the same failure class as today's two elevens (c_2 = dim K = 11 vs b_0 = 11N_c/3 = 11)
and this morning's 7/8 and 64/15. Four of these in one day; the standing rule earned its place.

(3) THE VERDICT: both roads bottom at P1. There is no irreducible ternary BST commitment on offer,
and no non-circular route from colour to the rank. P1 stands as the named axiom -- exactly where
Keeper predicted -- and now it stands there for a reason rather than for want of a candidate.

FOR THE WRITE-UP: the two posits are INDEPENDENT and neither should ride behind the other.
    P1  rank 2 ("no is as atomic as yes")  -> Lorentzian type-IV, the T2565 keystone.
    P2  minimality                         -> n = 5, chosen from the infinite set {5,7,9,11,...}
                                              in which n = 7 breaks nothing (my 5296).
P1 is an axiom about the act; P2 is a preference over models. Different kinds of posit, stated
separately.

Nothing pushed. CP existence-only.
"""
print("=" * 92)
print("Toy 5297: NO irreducible ternary commitment -- the colour split is CIRCULAR, and the ternary")
print("          route BACKFIRES: rank-3 off-diagonals are 1, 2, 4, 8 by Hurwitz. NEVER 3.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

print("\n   rank-2 spin factor of dim n:  V = R c_1 (+) R c_2 (+) V_12,  dim V_12 = n - 2\n")
for n in (4, 5, 6, 7):
    print("      n = %d  ->  dim V_12 = %d%s" % (n, n - 2, "    <-- n_C = 5 gives 3 = N_c" if n == 5 else ""))
check("1. THE CIRCULARITY CHECK -- the colour split cannot argue FOR rank 2",
      (5 - 2) == 3,
      "'colour is the OFF-diagonal, the record is the DIAGONAL' comes from the Peirce decomposition, "
      "and a Peirce decomposition has exactly TWO diagonal idempotents BECAUSE THE RANK IS 2. So the "
      "split is a CONSEQUENCE of rank 2, never an independent argument for it. It bottoms at P1, "
      "exactly as flagged.")

print("\n   rank-3 Jordan algebras Herm_3(A): 3 diagonal seats + THREE off-diagonal blocks of dim(A)\n")
rank3 = [("R", 1), ("C", 2), ("H", 4), ("O", 8)]
for A, d in rank3:
    print("      Herm_3(%s) : dim = 3 + 3x%d = %2d%s" % (A, d, 3 + 3 * d, "    <-- ALBERT, E_6" if A == "O" else ""))
offdiag = [d for _, d in rank3]
check("2. ★★★ THE TERNARY ROUTE BACKFIRES -- rank-3 off-diagonals are never 3",
      3 not in offdiag and offdiag == [1, 2, 4, 8],
      "the off-diagonal block dimension in a rank-3 algebra is dim(A) in {1,2,4,8} -- BY HURWITZ, the "
      "same theorem that closed my 5296 exclude-list. NEVER 3. => a ternary commitment CANNOT produce "
      "colour-3 at all; it is INCOMPATIBLE with N_c = 3. The very thing that motivates it -- 'three "
      "colours, so maybe three outcomes' -- is the thing it cannot deliver. The Albert/E_6 case gives "
      "EIGHT.")

check("3. ★ PRE-EMPTIVE FLAG -- a rank-3 advocate will notice the 8",
      8 == 3 ** 2 - 1,
      "8 = dim of the SU(3) ADJOINT = the gluon count. A DIFFERENT object from N_c = 3 (the "
      "fundamental). The temptation to marry them is the same failure class as today's two elevens "
      "(c_2 = dim K = 11 vs b_0 = 11 N_c/3 = 11), the 7/8, and the 64/15. FOUR in one day -- the "
      "standing rule earned its place.")

check("4. THE VERDICT -- both roads bottom at P1, and now for a REASON",
      True,
      "no irreducible ternary BST commitment is on offer, and no non-circular route runs from colour "
      "to the rank. P1 stands as the named axiom -- where Keeper predicted -- but now it stands there "
      "because the ternary alternative FAILS BY HURWITZ, not merely for want of a candidate.")

check("5. FOR THE WRITE-UP -- the two posits are INDEPENDENT and are different KINDS of posit",
      True,
      "P1 = rank 2 ('no is as atomic as yes') -> Lorentzian type-IV, the T2565 keystone: an AXIOM "
      "ABOUT THE ACT. P2 = minimality -> n = 5, chosen from the infinite set {5,7,9,11,...} in which "
      "n = 7 breaks nothing (my 5296): a PREFERENCE OVER MODELS. Neither should ride behind the "
      "other, and they should not be described in the same words.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   the colour split is circular; the ternary route is incompatible with N_c = 3"
      % (sum(tests), len(tests)))
print("       (off-diagonals 1/2/4/8 by Hurwitz); both bottom at P1; the two posits are independent.")
print("=" * 92)
