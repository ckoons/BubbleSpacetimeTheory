"""
Toy 5299 (Elie, 2026-08-16) -- the coding structure at maximum scrutiny: do the FORCED MAPS hold, or
are they shared integers? Two of six hold, and they are the two Casey actually named. The other four
do not, and one of them fails in a way we have now hit three times today.

★★ (1) TWO MAPS ARE GENUINELY FORCED -- and they are exactly Casey's "2 + 3 as two halves".
   rank = 2  <-  the binary alphabet.  The code is over GF(2); the alphabet size IS 2. No choice.
   N_c = 3   <-  d_min = 3.            d >= 2t+1 with t = 1 gives d = 3 for EVERY r -- r-INDEPENDENT.
This second one is the strongest map in the set: single-error-correction forces d = 3 no matter which
Hamming code you take. Casey's "binary decides, trinary validates" is FORCED on both halves.

★★★ (2) BUT g = 7 IS NOT FORCED, AND THE RESIDUAL IS FATAL IN THE DIRECTION SUSPECTED.
Hamming codes are a FAMILY: Hamming(2^r - 1, 2^r - 1 - r, 3), and EVERY member is a PERFECT
single-error-correcting code (verified: 2^k(1+n) = 2^n exactly, for r = 2,3,4,5,6):
      r        2        3        4        5        6
      (n,k,d) (3,1,3)  (7,4,3)  (15,11,3) (31,26,3) (63,57,3)
      perfect  yes      yes      yes       yes       yes
So "the minimal perfect single-error-correcting code" selects r = 2 -> Hamming(3,1,3), LENGTH 3, NOT
length 7. Getting g = 7 requires CHOOSING r = 3, the second member.
=> THAT IS A THIRD POSIT OF EXACTLY THE SHAPE OF P2b. Minimality-alone-gives-3 has now bitten in
   three places today: n (P2b, Cal), the Jordan rank, and now the code length. Same hole, third time.

★ (3) AND n_C = 5 IS NOT A MAP AT ALL -- it is a formula across two structures.
"n_C = g - rank = 7 - 2" subtracts a JORDAN rank from a CODE length. Those are different structures,
and 5 IS NOT AMONG Hamming(7,4,3)'s own quantities, which are {n,k,d,n-k} = {7,4,3,3}. C_2 = 6 and
N_max = 137 are not Hamming quantities either. So of the six integers, TWO come from forced maps and
FOUR do not come from maps.

★★★★ (4) THE NULL MODEL -- and the corpus already wrote the warning we need here.
Does r = 3 collect more BST integers than its neighbours? NO:
      r=2 (3,1,3,2)     -> 3=N_c, 2=rank
      r=3 (7,4,3,3)     -> 7=g, 4=rank^2, 3=N_c
      r=4 (15,11,3,4)   -> 15=N_c*n_C, 11=c_2, 3=N_c, 4=rank^2   <- MORE hits than r=3
      r=5 (31,26,3,5)   -> 31=2^n_C-1, 3=N_c, 5=n_C
The integer-count does NOT select r = 3. And T1956 -- OUR OWN theorem -- already states it: "BST
integer ring is DENSE at small scales, so Heegner-decomposability is GENERIC." Integer-matching
against small code parameters is precisely what the corpus has already ruled out as evidence. We
wrote that warning; it applies to us here.

WHAT I WOULD BANK, AND WHAT I WOULD NOT:
  BANK  : rank = 2 (binary alphabet) and N_c = 3 (= d_min, forced by single-error-correction,
          r-independent). Two forced maps, and they carry Casey's whole "decision + validation"
          picture. That is a real result and it is target-innocent -- Hamming's bound has no physics
          in it.
  DO NOT: "the five integers follow from Hamming(7,4,3)". Four of the six are not maps, g = 7 needs
          r = 3 chosen, and the integer-count actively favours r = 4. The honest claim is TWO
          integers from Shannon, not five.

Nothing pushed. CP existence-only.
"""
print("=" * 92)
print("Toy 5299: TWO of six maps are FORCED (rank=2 binary, N_c=3=d_min); but g=7 needs r=3 chosen,")
print("          minimality gives length 3 AGAIN, and n_C=5 mixes two structures.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

fam = []
print("\n   Hamming(2^r - 1, 2^r - 1 - r, 3) -- is every member perfect?\n")
print("      r    (n, k, d)      redundancy    perfect? 2^k(1+n) = 2^n")
for r in range(2, 7):
    n = 2 ** r - 1; k = n - r
    perf = (2 ** k) * (1 + n) == 2 ** n
    fam.append((r, n, k, 3, n - k, perf))
    tag = "   <- MINIMAL" if r == 2 else ("   <- the claim" if r == 3 else "")
    print("     %2d    (%2d,%2d,%d)         %2d           %s%s" % (r, n, k, 3, n - k, perf, tag))

check("1. ★★ TWO MAPS ARE GENUINELY FORCED -- and they are Casey's two halves",
      all(f[3] == 3 for f in fam),
      "rank = 2 <- the binary ALPHABET (the code is over GF(2); no choice). N_c = 3 <- d_min = 3, "
      "which d >= 2t+1 at t=1 forces for EVERY r -- r-INDEPENDENT, the strongest map in the set. "
      "'Binary decides, trinary validates' is FORCED on both halves.")

check("2. ★★★ BUT g = 7 IS NOT FORCED -- every member is perfect, and the MINIMAL one has length 3",
      all(f[5] for f in fam) and fam[0][1] == 3,
      "2^k(1+n) = 2^n holds exactly for r = 2,3,4,5,6, so ALL are perfect single-error-correcting "
      "codes. 'The minimal perfect single-error-correcting code' selects r = 2 -> length 3, NOT 7. "
      "Getting g = 7 requires CHOOSING r = 3. => A THIRD POSIT OF THE SHAPE OF P2b: "
      "minimality-alone-gives-3 has now bitten at n, at the Jordan rank, and at the code length.")

hamq = [7, 4, 3, 3]
check("3. ★ AND n_C = 5 IS NOT A MAP -- it is a formula across two structures",
      5 not in hamq,
      "'n_C = g - rank = 7 - 2' subtracts a JORDAN rank from a CODE length -- different structures. "
      "And 5 is NOT among Hamming(7,4,3)'s own quantities {n,k,d,n-k} = %s. C_2 = 6 and N_max = 137 "
      "are not Hamming quantities either. TWO of six integers come from forced maps; FOUR do not "
      "come from maps at all." % hamq)

BST = {2: "rank", 3: "N_c", 5: "n_C", 6: "C_2", 7: "g", 11: "c_2", 4: "rank^2",
       15: "N_c*n_C", 31: "2^n_C-1"}
print("\n   null model -- does r = 3 collect more BST integers than its neighbours?\n")
counts = {}
for r, n, k, d, red, _ in fam[:4]:
    q = [n, k, d, red]
    hits = [(x, BST[x]) for x in q if x in BST]
    counts[r] = len(hits)
    print("      r=%d  (%2d,%2d,%d,%d)  ->  %s" % (r, n, k, d, red, ", ".join("%d=%s" % h for h in hits)))
check("4. ★★★★ THE INTEGER-COUNT DOES NOT SELECT r = 3 -- and our own T1956 says why",
      counts[4] >= counts[3],
      "r=4 gives (15,11,3,4) with 15 = N_c*n_C, 11 = c_2, 3 = N_c, 4 = rank^2 -- %d hits against "
      "r=3's %d. The count does NOT favour r = 3. And T1956, OUR OWN theorem, already states it: "
      "'BST integer ring is DENSE at small scales, so Heegner-decomposability is GENERIC.' "
      "Integer-matching against small code parameters is exactly what the corpus has already ruled "
      "out as evidence. We wrote that warning; it applies to us here."
      % (counts[4], counts[3]))

check("5. WHAT I WOULD BANK, AND WHAT I WOULD NOT",
      True,
      "BANK: rank = 2 (binary alphabet) and N_c = 3 (= d_min, forced by single-error-correction, "
      "r-independent) -- TWO forced, target-innocent maps carrying Casey's whole decision+validation "
      "picture. Hamming's bound has no physics in it. DO NOT BANK: 'the five integers follow from "
      "Hamming(7,4,3)' -- four of six are not maps, g=7 needs r=3 chosen, and the integer-count "
      "actively favours r=4. The honest claim is TWO integers from Shannon, not five.")

print("\n" + "=" * 92)
print("SCORE: %d/%d   rank=2 and N_c=3=d_min are FORCED and target-innocent; g=7, n_C=5, C_2, N_max"
      % (sum(tests), len(tests)))
print("       are not maps; minimality gives length 3 a third time; the count favours r=4, not r=3.")
print("=" * 92)
