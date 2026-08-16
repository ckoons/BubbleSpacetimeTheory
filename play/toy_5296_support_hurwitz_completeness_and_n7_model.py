import sympy as sp
print("="*92)
print("(1) IS THE EXCLUDE-LIST COMPLETE?  YES -- AND BY A THEOREM, NOT BY SURVEY.")
print("="*92)
print("  The rank-2 matrix coincidences are exactly Herm_2(A) for A a NORMED DIVISION ALGEBRA,")
print("  and as a spin factor that is n = 2 + dim(A):")
hur=[("R",1),("C",2),("H",4),("O",8)]
for A,d in hur: print("      A = %-1s  dim %d  ->  n = %2d"%(A,d,2+d))
print("  ★ HURWITZ'S THEOREM (1898): there are EXACTLY FOUR normed division algebras over R --")
print("    R, C, H, O, of dimensions 1, 2, 4, 8. No others exist, at any dimension.")
print("  ⟹ THE COINCIDENCE LIST {3,4,6,10} IS CLOSED BY HURWITZ. It cannot be extended, and no")
print("     further n can turn out to be a disguised matrix domain. That is a COMPLETENESS PROOF.")
print()
print("  full accounting of the degeneracies:")
for n,why in [(1,"the disc -- degenerate (type I_1)"),(2,"spin factor dim 2 = R (+) R -- REDUCIBLE"),
              (3,"Herm_2(R) = Sym_2(R) -- Siegel, type III_2"),(4,"Herm_2(C) -- type I_{2,2}"),
              (6,"Herm_2(H) -- SO*(8), type II"),(10,"Herm_2(O) -- octonionic, stays type IV but distinguished")]:
    print("      n = %2d : %s"%(n,why))
print("      n = 5, 7, 8, 9, 11, 12, ... : GENUINELY type IV, no coincidence available")
print("  ⟹ EXCLUDE-LIST COMPLETE: {1,2} degenerate + {3,4,6,10} Hurwitz. Nothing else can appear.")
print()
print("="*92)
print("(2) WHY MINIMALITY IS NOT A DERIVATION -- exhibited, not asserted.")
print("="*92)
print("  A derivation forces a UNIQUE answer from its premises. To show minimality is an EXTRA")
print("  premise, exhibit the other models: does every structure BST uses still exist at n = 7?")
h,n=sp.symbols('h n')
def props(N):
    dimG=(N+2)*(N+1)//2                  # dim SO(N,2)
    dimK=N*(N-1)//2+1
    ser=sp.expand(sp.series((1+h)**(N+2)/(1+2*h),h,0,3).removeO())
    c2=int(sp.Poly(ser,h).coeff_monomial(h**2))
    return dimG,dimK,c2
print("      n     rank   dim SO(n,2)   dim K   c_2   Shilov            spin factor   genus")
for N in [5,7,8,9]:
    dG,dK,c2=props(N)
    print("     %2d       2        %3d       %3d    %3d   (S^%d x S^1)/Z_2      dim %d, (1,%d)     %d%s"%(
        N,dG,dK,c2,N-1,N,N-1,N,"   <-- BST" if N==5 else ""))
print("\n  ⟹ EVERY structural property BST uses is PRESENT at n = 7, 8, 9: rank 2, a Shilov boundary")
print("     of the same shape, a Lorentzian spin factor, the c_2 = dim K identity, an FK genus.")
print("     NOTHING BREAKS. n = 7 is a complete, internally consistent model of the same axioms.")
print("  ⟹ SO MINIMALITY IS SELECTING AMONG GENUINE MODELS. That is an EXTRA AXIOM, not a")
print("     consequence of the axioms already stated. Occam is a preference over models, and a")
print("     preference is not a forcing.")
print()
print("  and to make the cost concrete rather than rhetorical -- what the n=7 world would look like:")
for N in [5,7]:
    _,_,c2=props(N)
    print("      n = %d : c_2 = %2d  ->  the 2-form gap c_2 pi^5 m_e = %7.1f MeV"%(N,c2,c2*(sp.pi**5).evalf()*0.511))
print("     a different universe with the same axioms, not an inconsistency. THAT is the honest")
print("     content of 'minimality is a posit'.")
print()
print("  ★ AND THE SET MINIMALITY CHOOSES FROM IS INFINITE. Even after the strongest non-forbidden")
print("    narrowing (n odd, T2547 quaternionic Spin(n)) the survivors are {5,7,9,11,...} -- still")
print("    infinite. Minimality is not picking 1 of 3; it is picking the least element of an")
print("    unbounded set. The NEAREST alternative is n = 7.")
