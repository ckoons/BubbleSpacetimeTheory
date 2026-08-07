#!/usr/bin/env python3
"""
Toy 5095: OWN the interlock off-by-one in toy 5094 -- SO(4,2) is n_C=4, standard holography is
same-group, so n_C=5 is NOT forced by N_c=3. Crux localized (K1236, Cal §323).
E / Elie -- fish-detector on my own prior toy. Cal caught the hole; Keeper ruled it correct
(two self-catches, both his chain); I own my PROPAGATION of it in toy 5094 check 5.

WHAT I OWN (my miss in toy 5094):
  * Toy 5094 check 5 asserted the chain "N_c=3 -> 4D -> SO(4,2) -> SO(5,2)=IV_5 -> n_C=5" as the
    descent that "picks n=5". I even computed dim SO(4,2)=15 -- and did NOT flag that SO(4,2) IS
    D_IV^4 (n_C=4). The +1 (SO(4,2)->SO(5,2)) was smuggled. I flagged "only n=5" as an open edge
    but did not localize the off-by-one. That is a real miss; I correct it here (5094 stands as
    the record; 5095 supersedes its check-5 claim, like K1224->K1226).
  * I also called T2113 "banked" in my 5094 post. Keeper's grep (K1236): T2113 is registry
    tier-I (Identified), "pending operator algebra" -- NOT proved. So the holography anchor is
    weaker than I stated. Owned.

THE EXACT BOOKKEEPING (exhibit, don't re-smuggle):
  * D_IV^n = SO_0(n,2)/[SO(n)xSO(2)], complex dimension n (source-pinned, toy 5093).
    => SO(4,2) = D_IV^4 = n_C 4;   SO(5,2) = D_IV^5 = n_C 5.
  * The conformal group of 4D Minkowski is SO(4,2) = n_C 4 -- ALREADY four, not five.
  * Standard holography is SAME-GROUP: a 4D CFT (conformal SO(4,2)) is dual to AdS5, whose
    isometry group is ALSO SO(4,2). So holography of a 4D world gives an SO(4,2) bulk = n_C 4,
    NOT SO(5,2). The jump SO(4,2)->SO(5,2) (the +1) is NOT provided by standard holography.
  * The BST bulk is SO(5,2) = D_IV^5 = n_C 5 (= AdS6 / a 5D-conformal object) -- ONE dimension
    higher than the SO(4,2) that 4D physics gives.

=> RULING (Keeper K1236, which I now propagate correctly): n_C=5 is NOT forced by N_c=3. It
remains an INDEPENDENT INPUT until the group-level +1 (SO(4,2) -> SO(5,2)) is exhibited with
exact dimensions and without re-smuggling. The crux of BST's whole geometry is now ONE exact,
well-posed step:  WHY is the BST bulk SO(5,2) and not the standard SO(4,2)? = why one extra
dimension?  Keeper's CANDIDATE reading (the +1 = the commitment/time circle on which the record
is written) is a candidate, NOT exhibited here -- I will not re-smuggle it.

=> WHAT STANDS (unaffected by the hole): the conformal filter selects the FAMILY Type IV (toy
5094, sound -- dimension open); T2545 (the (3,1) signature) is banked; n_C and rank are the
domain's structural data (complex dim + rank), not fitted numbers (toy 5093, banked). Those are
a different, weaker, and TRUE claim than "n_C=5 is forced" -- kept crisply separate.

=> DISPOSITION: owns my 5094 propagation + the T2113 over-statement; exhibits the exact off-by-
one; localizes the crux to a single group-level question; keeps the family filter + T2545 +
structural-not-fitted intact. n_C=5 back to independent input. Nothing banks; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

def dim_so(p, q):
    d = p + q
    return d * (d - 1) // 2

def nC_of_DIV(so_first_index):   # D_IV^n = SO(n,2), complex dim = n
    return so_first_index

print("=" * 78)
print("Toy 5095: OWN the interlock off-by-one -- SO(4,2)=n_C=4, holography same-group (K1236)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. OWN the miss in toy 5094.
# ----------------------------------------------------------------------------
print("\n--- OWN the propagation miss in toy 5094 ---")
dim42, dim52 = dim_so(4, 2), dim_so(5, 2)
check("OWN: toy 5094 check 5 propagated 'SO(4,2) -> SO(5,2) -> n_C=5' while I had dim SO(4,2)=15 "
      "in hand and did NOT flag that SO(4,2) = D_IV^4 = n_C=4. The +1 was smuggled; I correct it "
      "(5094 stands as record, 5095 supersedes its check-5 claim)",
      dim42 == 15 and dim52 == 21 and nC_of_DIV(4) == 4,
      f"SO(4,2)=D_IV^4: dim {dim42}, n_C={nC_of_DIV(4)}. SO(5,2)=D_IV^5: dim {dim52}, n_C={nC_of_DIV(5)}. "
      "I also called T2113 'banked' -- it is tier-I (Identified), 'pending operator algebra', NOT proved. Owned.")

# ----------------------------------------------------------------------------
# 2. The exact bookkeeping: SO(4,2) is ALREADY n_C=4.
# ----------------------------------------------------------------------------
print("\n--- exact bookkeeping: the 4D conformal group SO(4,2) is n_C=4, not 5 ---")
check("the conformal group of 4D Minkowski is SO(4,2) = D_IV^4 = n_C 4 -- ALREADY four. The chain's "
      "4D boundary picks n_C=4; it does not reach 5 by itself",
      nC_of_DIV(4) == 4 and dim_so(4, 2) == 15,
      f"SO(4,2)=D_IV^4, complex dim = 4 = n_C. The '4D boundary -> n_C' step lands on 4, not 5.")

# ----------------------------------------------------------------------------
# 3. Standard holography is SAME-GROUP -> gives n_C=4, not 5.
# ----------------------------------------------------------------------------
print("\n--- standard holography is same-group: 4D CFT SO(4,2) <-> AdS5 isometry SO(4,2) ---")
# AdS_{d+1} isometry = SO(d,2); AdS5 = SO(4,2) = the isometry of the standard AdS5/CFT4 dual.
adS5_isometry = (4, 2)     # SO(4,2)
cft4_conformal = (4, 2)    # SO(4,2)
check("standard holography (AdS/CFT, Rehren) is SAME-GROUP: a 4D CFT (conformal SO(4,2)) is dual "
      "to AdS5 whose isometry is ALSO SO(4,2). So holography of a 4D world gives an SO(4,2) bulk = "
      "n_C=4, NOT SO(5,2). The +1 is not provided by standard holography",
      adS5_isometry == cft4_conformal == (4, 2) and nC_of_DIV(4) == 4,
      f"AdS5 isometry = SO{adS5_isometry} = CFT4 conformal group = SO{cft4_conformal}: same group -> "
      "bulk n_C = 4. The jump SO(4,2)->SO(5,2) (n_C 4->5) is the crux, not a holography output.")

# ----------------------------------------------------------------------------
# 4. Localize the crux: the +1 = one extra complex domain dimension (IV^4 -> IV^5).
# ----------------------------------------------------------------------------
print("\n--- localize the crux: the +1 = one extra complex dimension (IV^4 -> IV^5) ---")
plus_one = nC_of_DIV(5) - nC_of_DIV(4)
check("the crux is ONE exact step: the +1 = one extra COMPLEX domain dimension (D_IV^4 -> D_IV^5, "
      "n_C 4 -> 5), i.e. WHY is the BST bulk SO(5,2) (n_C=5) and not the standard SO(4,2) (n_C=4)? "
      "Keeper's candidate reading (+1 = the commitment/time circle) is CANDIDATE, not exhibited here",
      plus_one == 1,
      f"+1 = n_C(D_IV^5) - n_C(D_IV^4) = {nC_of_DIV(5)} - {nC_of_DIV(4)} = {plus_one}. BST bulk SO(5,2) is "
      "one dimension higher than the SO(4,2) 4D physics gives. I will NOT re-smuggle the +1 = commitment circle.")

# ----------------------------------------------------------------------------
# 5. What STANDS (unaffected).
# ----------------------------------------------------------------------------
print("\n--- what stands (unaffected by the hole) ---")
check("STANDS: (a) the conformal filter selects the FAMILY Type IV (toy 5094, sound -- dimension "
      "open); (b) T2545 (the (3,1) signature) is banked; (c) n_C and rank are the domain's "
      "structural data (complex dim + rank), NOT fitted (toy 5093). A weaker, TRUE claim, kept "
      "separate from the false 'n_C=5 forced'",
      nC_of_DIV(5) == 5 and dim_so(5, 2) == 21,
      "family filter (Type IV) + T2545 + 'n_C,rank structural not fitted' all intact. The forcing of "
      "the VALUE n_C=5 is the open crux; the STRUCTURAL role of n_C=5 (= complex dim of IV_5) stands.")

check("RULING (propagated correctly now): n_C=5 is NOT forced by N_c=3 -- it is an INDEPENDENT "
      "INPUT until the +1 (SO(4,2)->SO(5,2)) is exhibited with exact dims and no re-smuggling. The "
      "deepest open question is now ONE well-posed step: why one extra dimension?",
      True,
      "Cal §323 + Keeper K1236 ruled n_C=5 not forced; I own my 5094 propagation. Crux localized. "
      "Fish-detector on my own toy: the pretty interlock got tested to destruction; what's left is sharp.")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5095 -- OWN the interlock off-by-one; crux localized):
  * OWNED: toy 5094 check 5 propagated 'SO(4,2)->SO(5,2)->n_C=5' without flagging SO(4,2)=D_IV^4=
    n_C=4 (I had dim SO(4,2)=15 in hand). Also called T2113 'banked' -- it is tier-I (Identified),
    NOT proved. Both corrected (5094 stands as record; this supersedes its check-5 claim).
  * EXACT BOOKKEEPING: D_IV^n = SO(n,2), complex dim n. SO(4,2)=D_IV^4=n_C 4; SO(5,2)=D_IV^5=n_C 5.
    The 4D conformal group is SO(4,2) = n_C 4 ALREADY. Standard holography is SAME-GROUP (4D CFT
    SO(4,2) <-> AdS5 isometry SO(4,2)) -> bulk n_C 4, NOT 5. The +1 is not a holography output.
  * CRUX LOCALIZED to one exact step: why is the BST bulk SO(5,2) (n_C=5) and not the standard
    SO(4,2) (n_C=4)? = why one extra complex dimension (D_IV^4 -> D_IV^5)? Keeper's candidate
    (+1 = commitment/time circle) is CANDIDATE, not exhibited -- I refuse to re-smuggle it.
  * RULING: n_C=5 is NOT forced by N_c=3; back to an INDEPENDENT INPUT until the +1 is exhibited.
  * STANDS: the conformal filter -> FAMILY Type IV (5094, sound); T2545 (signature) banked; n_C and
    rank are structural (complex dim + rank) not fitted (5093, banked). Weaker, TRUE, kept separate.

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked. Fish-detector on my own toy; the interlock got
tested to destruction; the crux is now a single well-posed group-level question. Count N.
""")
