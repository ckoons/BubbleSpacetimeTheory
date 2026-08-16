print("="*92)
print("DO THE FORCED MAPS HOLD?  Test each one separately -- forced map vs shared integer.")
print("="*92)
print("  Hamming codes are a FAMILY parameterised by r:  Hamming(2^r - 1, 2^r - 1 - r, 3).")
print("      r    length n    dim k    d_min    redundancy n-k    perfect?  (2^k(1+n) = 2^n)")
fam=[]
for r in range(2,7):
    n=2**r-1; k=n-r; d=3
    perfect = (2**k)*(1+n)==2**n
    fam.append((r,n,k,d,n-k,perfect))
    print("     %2d      %4d      %4d      %2d          %2d            %s%s"%(
        r,n,k,d,n-k,perfect,"   <-- Hamming(7,4,3), the claim" if r==3 else ("   <-- the MINIMAL one" if r==2 else "")))
print()
print("  ★ EVERY member is a PERFECT single-error-correcting code. So 'minimal perfect")
print("    single-error-correcting code' selects r = 2 -> Hamming(3,1,3), LENGTH 3. NOT length 7.")
print("  ⟹ THE SUB-RESIDUAL IS FATAL IN THE DIRECTION SUSPECTED: minimality gives r=2/length-3.")
print("     Getting g = 7 requires choosing r = 3, the SECOND member -- a THIRD posit of exactly")
print("     the same shape as P2b (minimality-alone-gives-3). The same hole, a third time.")
print()
print("="*92)
print("MAP BY MAP -- which are FORCED and which are formulas?")
print("="*92)
maps=[
 ("rank = 2  <-  binary alphabet","FORCED","the code is over GF(2); the alphabet size IS 2. No choice."),
 ("N_c = 3  <-  d_min = 3","FORCED","d >= 2t+1 with t=1 gives d = 3 for EVERY r. r-INDEPENDENT. This is the strongest map in the set."),
 ("g = 7  <-  code length","NOT FORCED","length = 2^r - 1 varies with r; minimality gives 3, not 7."),
 ("n_C = 5  <-  g - rank = 7 - 2","NOT A MAP","subtracts a JORDAN rank from a CODE length -- two different structures. And 5 is NOT among Hamming(7,4,3)'s own quantities {7,4,3,3}."),
 ("C_2 = 6","NOT A MAP","not a Hamming quantity at all."),
 ("N_max = 137","NOT A MAP","not a Hamming quantity at all."),
]
for a,b,c in maps:
    print("   %-32s %-11s %s"%(a,b,c))
print()
print("  ⟹ TWO OF SIX MAPS ARE FORCED (rank=2 and N_c=d_min=3). Those two are REAL and they are")
print("     exactly Casey's '2 + 3 as two halves of one operation' -- the decision and the parity.")
print("     THE OTHER FOUR ARE NOT MAPS. g=7 needs r=3 chosen; n_C=5 mixes two structures.")
print()
print("="*92)
print("THE NULL MODEL -- does r = 3 actually collect more BST integers than its neighbours?")
print("="*92)
BST={2:"rank",3:"N_c",5:"n_C",6:"C_2",7:"g",11:"c_2",13:"c_3",137:"N_max",
     4:"rank^2",15:"N_c*n_C",21:"N_c*g",10:"rank*n_C",9:"N_c^2",8:"rank^3",31:"2^n_C-1"}
print("      r   code (n,k,d)      code's own quantities   BST-recognisable ones")
for r,n,k,d,red,_ in fam:
    q=[n,k,d,red]
    hits=[(x,BST[x]) for x in q if x in BST]
    print("     %2d   (%2d,%2d,%d)          %-22s %s"%(r,n,k,d,str(q),", ".join("%d=%s"%h for h in hits)))
print()
print("  ⟹ r = 4 gives (15, 11, 3, 4): 15 = N_c*n_C, 11 = c_2, 3 = N_c, 4 = rank^2 -- FOUR hits,")
print("     MORE than r = 3's (7,4,3,3). The integer-count does NOT select r = 3.")
print("  ★★ AND THE CORPUS ITSELF ALREADY SAID WHY: T1956 -- 'BST integer ring is DENSE at small")
print("     scales, so Heegner-decomposability is GENERIC.' Integer-matching against small code")
print("     parameters is precisely the thing the corpus has already ruled out as evidence.")
print("     We wrote that warning ourselves; it applies here.")
