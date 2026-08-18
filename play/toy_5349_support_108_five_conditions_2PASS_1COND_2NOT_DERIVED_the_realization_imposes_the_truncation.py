import numpy as np, itertools
print("="*104)
print("TOY 5349 -- #108 THE FIVE-CONDITION TOEPLITZ-CORRECTION TEST")
print("  Tables first, verdict after.  Geometric operators, not bare matrices -- and the")
print("  difference between those two turns out to BE the answer.")
print("="*104)

# quadrupoles on V_12 = R^3, and so(3)
def E(i,j):
    M=np.zeros((3,3)); M[i,j]=1; return M
so3=[E(1,2)-E(2,1),E(2,0)-E(0,2),E(0,1)-E(1,0)]
S=[np.diag([1,-1,0.]), np.diag([1,1,-2.])/np.sqrt(3)]
for i,j in [(0,1),(0,2),(1,2)]:
    M=np.zeros((3,3)); M[i,j]=M[j,i]=1; S.append(M)

print("\nTABLE 1 -- CONDITION 3 (the one that separates SU(3) from SO(3)): the d-symbol")
print("   d_abc = Tr({S_a,S_b} S_c). su(3) has d =/= 0; so(3)=su(2) has d == 0 identically.")
d=np.array([[[np.trace((S[a]@S[b]+S[b]@S[a])@S[c]) for c in range(5)] for b in range(5)] for a in range(5)])
print("   max |d_abc| over the geometric quadrupoles = %.4f"%np.abs(d).max())
print("   number of independent nonzero components   = %d"%int((np.abs(d)>1e-9).sum()))
# so(3) control
dso3=np.array([[[np.trace((so3[a]@so3[b]+so3[b]@so3[a])@so3[c]) for c in range(3)] for b in range(3)] for a in range(3)])
print("   CONTROL -- same computation on so(3) itself: max |d| = %.2e  (must be 0)"%np.abs(dso3).max())
print("   ==> *** CONDITION 3 PASSES: the d-symbol is nonzero on the geometric quadrupoles,")
print("       and the so(3) control returns exactly zero. This is a real discriminator. ***")

print("\nTABLE 2 -- CONDITION 4 (compact/positive sign) -- carried from 5348")
print("   Killing eigenvalues all -12 (strictly negative) -> COMPACT real form -> su(3),")
print("   not sl(3,R), not su(2,1).  *** CONDITION 4 PASSES. ***")

print("\nTABLE 3 -- *** CONDITION 2 (l=3 vanishing) -- THE CRUX ***")
print("   The quadrupoles carry so(3)-spin 2. Decompose the ANTISYMMETRIC square (= the bracket):")
print("      Lambda^2(spin-2) has dimension C(5,2) = 10")
print("      spin-2 (x) spin-2 = spin-0+1+2+3+4;  ANTISYMMETRIC part = spin-1 (+) spin-3")
print("      dims: 3 + 7 = 10   ->  *** THE BRACKET SPACE CONTAINS A SPIN-3 (l=3) PIECE. ***")
print("   So closure into so(3) requires that spin-3 component to VANISH. Test it:")
img=[]
for a in range(5):
    for b in range(a+1,5):
        img.append((S[a]@S[b]-S[b]@S[a]).flatten())
r=np.linalg.matrix_rank(np.array(img))
print("   rank of the span of all [S_a, S_b] (matrix realization) = %d"%r)
print("   dim so(3) = 3 ;  dim Lambda^2 = 10 ;  dim spin-3 = 7")
print("   ==> the matrix bracket's image is %d-dimensional = so(3) ONLY. The spin-3 is ABSENT."%r)

print("\nTABLE 4 -- *** but WHY is it absent? This is the whole finding. ***")
print("   [S_a,S_b] for symmetric 3x3 is ANTISYMMETRIC 3x3, and antisymmetric 3x3 is a")
print("   3-DIMENSIONAL space. There is simply NO ROOM for a 7-dimensional spin-3.")
print("   ==> *** THE 3x3 MATRIX REALIZATION IMPOSES THE TRUNCATION; IT DOES NOT DERIVE IT. ***")
print("       The bracket space Lambda^2 is 10-dimensional, the matrix commutator map lands in a")
print("       3-dimensional image, so 7 dimensions are PROJECTED AWAY by the choice of realization.")
print("   For genuine Toeplitz operators the symbols are FUNCTIONS on the shell, the bracket is the")
print("   Poisson/Hankel bracket, and *** nothing kills the spin-3 for free. ***")

print("\nTABLE 5 -- CONDITIONS 1 and 5, and the circularity")
print("   condition 1 (finite closure)     : holds IFF the spin-3 truncates (Table 3-4)")
print("   condition 5 (on geometric SO(V_12)): the operators must be the 3x3 action on V_12")
print("   ==> conditions 1 and 5 are THE SAME CONDITION. And 'the operators are 3x3 matrices on")
print("       V_12' is exactly 'V_12 carries the fundamental of a 3x3 matrix algebra' --")
print("       *** which PRESUPPOSES the SU(3) we are trying to derive. ***")

print("\n"+"="*104)
print("VERDICT -- five conditions, scored")
print("="*104)
sc=[("1 finite closure","CONDITIONAL","holds only under the matrix realization = condition 5"),
    ("2 l=3 vanishing","*** NOT DERIVED ***","spin-3 is present in Lambda^2 (7 of 10 dims);"),
    ("3 su(3) d-symbol","PASS","nonzero on the quadrupoles; so(3) control = 0 exactly"),
    ("4 compact sign","PASS","Killing eigenvalues all -12"),
    ("5 geometric SO(V_12)","*** ASSUMED ***","it IS the 3x3 realization, i.e. the assumption")]
for n,v,w in sc:
    print("   %-22s %-22s %s"%(n,v,w))
print("\n   SCORE: *** 2 PASS / 1 CONDITIONAL / 2 NOT DERIVED. ***")
print()
print(" (1) *** THE GOOD NEWS IS REAL: condition 3 is a genuine discriminator and it PASSES. *** The")
print("     d-symbol is nonzero on the geometric quadrupoles and the so(3) control returns exactly")
print("     zero -- so whatever this algebra is, it is NOT a disguised SO(3). With condition 4's")
print("     compact sign, the algebra really is su(3) and not a smaller or split group.")
print()
print(" (2) *** BUT CONDITION 2 IS NOT DERIVED, AND IT IS THE ONE THAT MATTERED. *** Lambda^2 of the")
print("     quadrupoles is 10-dimensional and splits as spin-1 (+) spin-3. Closure needs the spin-3")
print("     (7 of the 10 dimensions) to vanish. In the 3x3 matrix realization it does -- but only")
print("     because antisymmetric 3x3 matrices form a 3-dimensional space with no room for it.")
print("     *** THE REALIZATION IMPOSES THE TRUNCATION RATHER THAN DERIVING IT. ***")
print()
print(" (3) *** AND CONDITIONS 1 AND 5 COLLAPSE INTO THE ASSUMPTION. *** 'Finite closure' holds iff")
print("     the operators are the 3x3 action on V_12, which is condition 5, which is the statement")
print("     that V_12 carries a 3x3 matrix algebra -- i.e. the SU(3) we set out to derive.")
print("     This is the hunt-if-P shape: the mechanism that would deliver the result is the same")
print("     assumption that produces it.")
print()
print(" ==> HONEST FLOOR: *** the algebra is genuinely su(3) (conditions 3+4, and 3 is un-fakeable),")
print("     but its GEOMETRIC HOME is not derived -- the truncation is imposed by the realization,")
print("     not by the geometry. *** That is a smaller-group floor in the precise sense @Keeper")
print("     asked for: we have su(3) the ALGEBRA, and we do not have su(3) FROM D_IV^5.")
print("     What would close it: a computation showing the Hankel corrections kill the spin-3 on the")
print("     second shell WITHOUT assuming the 3x3 realization. I did not find one and did not fake one.")
