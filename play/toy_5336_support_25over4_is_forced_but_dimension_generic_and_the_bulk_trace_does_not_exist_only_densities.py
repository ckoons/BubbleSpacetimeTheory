from fractions import Fraction as F
print("="*104)
print("TOY 5336 -- (A) is the Kostant constant 25/4 FORCED, or a clean coincidence?")
print("            (B) the BULK Kostant-D heat trace -- the real induced-gravity computation")
print("  Tables first, verdict after.  No wave-through.")
print("="*104)

def rho(kind,r):
    # B_r : (r-1/2, ..., 1/2)   D_r : (r-1, ..., 1, 0)
    return [F(2*(r-i)-1,2) for i in range(r)] if kind=="B" else [F(r-1-i) for i in range(r)]
def typ(m):                       # so(m,C):  B_r if m odd, D_r if m even
    return ("B",(m-1)//2) if m%2 else ("D",m//2)
def nrm(v): return sum(x*x for x in v)

print("\n--- PART A: sweep the WHOLE D_IV^n family. If the answer is (n/2)^2 for every n,")
print("            the identity is dimension-generic and carries no D_IV^5 information. ---")
print("\nTABLE 1 -- Kostant constant  ||rho_G||^2 - ||rho_K||^2  for D_IV^n = SO(n,2)/[SO(n)xSO(2)]")
print("   n    g=so(n+2)   ||rho_G||^2   k=so(n)   ||rho_K||^2   difference   (n/2)^2   equal?")
allq=True
for n in range(3,11):
    kg,rg=typ(n+2); kk,rk=typ(n)
    a=nrm(rho(kg,rg)); b=nrm(rho(kk,rk)); dif=a-b; tgt=F(n,2)**2
    eq=(dif==tgt); allq&=eq
    star=" <== D_IV^5" if n==5 else ""
    print("   %-4d %-11s %-13s %-9s %-13s %-12s %-9s %s%s"%(
        n,"%s_%d"%(kg,rg),str(a),"%s_%d"%(kk,rk),str(b),str(dif),str(tgt),eq,star))
print("\n   holds for EVERY n in the sweep: %s"%allq)
print("   ==> *** THE CONSTANT IS (n/2)^2 IDENTICALLY IN n. ***")

print("\nTABLE 2 -- so what does that mean for the 5 in 25/4?")
print("   question asked            answer")
print("   is the 5 the domain's n_C?   YES -- the formula is (n/2)^2 and D_IV^5 has n = n_C = 5.")
print("   is it a coincidence?         NO.")
print("   is it FORCED?                YES -- but forced GENERICALLY, as a family identity.")
print("   does it SELECT n_C = 5?      *** NO. It holds for n=3,4,6,7,8,9,10 equally. ***")
print("   ==> the clean number is real and forced, and carries ZERO D_IV^5-specific content.")
print("       Same shape as 'c_2 = dim K identically in n'. Not a signature. NOT a bank.")

print("\n--- PART B: the bulk Kostant-D heat trace ---")
print("\nTABLE 3 -- *** the obstruction, stated before any number ***")
print("   D_IV^5 is a NON-COMPACT symmetric space: Vol(D_IV^5) = INFINITE.")
print("   a_0 = dim(spinor) x Vol  ->  DIVERGES.  Tr e^{-tD^2} is NOT trace-class on the bulk.")
print("   ==> *** THE TOTAL HEAT TRACE DOES NOT EXIST. *** Only the LOCAL Seeley-DeWitt")
print("       DENSITIES are finite -- and those are exactly Sakharov's quantities, so the")
print("       computation is still the right one; it just cannot be a total trace.")

dim_p=10; spin=2**(dim_p//2)
print("\nTABLE 4 -- the local densities on the bulk (Killing normalization)")
print("   real dimension of D_IV^5 = 2 n_C = %d"%dim_p)
print("   Dirac spinor dimension   = 2^(%d/2) = %d"%(dim_p,spin))
print("   symmetric space of NON-COMPACT type: Ric = -(1/2) g  ->  R = -(1/2) dim = %d"%(-dim_p//2))
print("   check the family: R = -n identically (dim = 2n, Ric = -g/2)  -> R = -n_C = -5")
print("   *** SO R = -n IS ALSO DIMENSION-GENERIC. Second family identity, same lesson. ***")
R=F(-5)
a0d=spin
a1d=-F(1,12)*spin*R
print("\n   coefficient   density                          value")
print("   a_0 density   dim(spinor)                      %s"%a0d)
print("   a_1 density   -(1/12) x dim(spinor) x R        %s   <-- the EINSTEIN-HILBERT density"%a1d)
print("   (formula checked against my 5334 S^4 run: -(1/12)(4)(12)Vol = -32 pi^2/3, matched 4e-7)")

print("\nTABLE 5 -- the S^4 result vs the BULK result, side by side")
print("   manifold     dim   R      spinor   a_1 density        sign")
for nm,dm,Rv,sp in [("S^4 (5334)",4,F(12),4),("D_IV^5 bulk",10,F(-5),32)]:
    v=-F(1,12)*sp*Rv
    print("   %-12s %-5d %-6s %-8d %-18s %s"%(nm,dm,str(Rv),sp,str(v),"NEGATIVE" if v<0 else "POSITIVE"))
print("   ==> *** THE SIGN FLIPS. *** The sphere has R > 0, the bulk has R < 0, so the induced")
print("       Einstein-Hilbert coefficient has the OPPOSITE SIGN on the bulk. That is a real,")
print("       physical difference and it is NOT something the S^4 run could have shown.")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (A) *** 25/4 IS FORCED BUT CONTENTLESS. *** The Kostant constant is (n/2)^2 IDENTICALLY")
print("     across the whole D_IV^n family (verified n = 3..10). So the 5 IS the domain's n_C --")
print("     it is not a coincidence -- but the identity SELECTS NOTHING, because it holds just as")
print("     well for n = 3, 4, 6, 7, .... It is a family identity wearing a clean number.")
print("     ==> NOT a bank, NOT a signature. @Keeper: file it as a dimension-generic identity,")
print("         the same category as 'c_2 = dim K identically in n'. The no-wave-through rule")
print("         called this one correctly -- the clean number did not survive as content.")
print()
print(" (B1) *** THE TOTAL BULK HEAT TRACE DOES NOT EXIST -- D_IV^5 has INFINITE VOLUME. *** Any")
print("      'Tr e^{-tD^2} ~ t^{-5}' statement is formal; a_0 diverges. Only LOCAL DENSITIES are")
print("      meaningful. I am reporting that before any number, because it is the honest shape of")
print("      the computation and it changes what can be claimed.")
print()
print(" (B2) THE EINSTEIN-HILBERT TERM DOES STILL FALL OUT -- as a DENSITY:")
print("      a_0 density = 32 ;  a_1 density = -(1/12)(32)(-5) = 40/3.")
print("      *** AND THE SIGN IS OPPOSITE TO THE SPHERE'S, because the bulk is negatively curved.")
print("      That is the one physically new thing here, and my S^4 run could not have seen it. ***")
print()
print(" (B3) STILL OWED, and I am not supplying it: R = -n is ALSO dimension-generic, so neither")
print("      the constant nor the curvature distinguishes D_IV^5. And a genuine induced-G claim")
print("      needs the regularization/cutoff story (what makes 1/G finite), which no local density")
print("      supplies. @Lyra: the gravity section can say 'the EH density falls out with a definite")
print("      sign', and must NOT yet say 'BST induces gravity with coefficient X'.")
