import numpy as np, itertools
np.set_printoptions(precision=4,suppress=True)
print("="*104)
print("TOY 5348 -- #108 TOEPLITZ CHECK: do the l=2 quadrupole operators close into so(3)")
print("            with su(3)'s structure constants?  Definite yes/no.")
print("  Reconnected first: shell structure {1,5,14,30} = SO(5) reps (l,0); K-type multiplication.")
print("="*104)

print("\nTABLE 1 -- is the shape even IN the second shell? (branch 14 under SO(3)xSO(2))")
print("   SO(5) shells (l,0):  l=0 -> 1,  l=1 -> 5,  l=2 -> 14,  l=3 -> 30")
print("   embed 5 = V_12 (+) (2-dim) = 3 + 2, so SO(3)xSO(2) c SO(5), SO(3) acting on V_12")
print("   Sym^2(5) = Sym^2(3) (+) (3 (x) 2) (+) Sym^2(2) = 6 + 6 + 3 = 15")
print("   remove the trace -> 14 = the l=2 shell")
print("   and Sym^2(3) = Sym^2_0(3) (+) trace = 5 + 1")
print("   ==> *** THE l=2 SHELL CONTAINS Sym^2_0(V_12), dim 5 -- THE GLUON SHAPE IS THERE. ***")

print("\nTABLE 2 -- now the ALGEBRA test: build so(3) (+) i.Sym^2_0(R^3) explicitly and close it")
# so(3): real antisymmetric 3x3
def E(i,j):
    M=np.zeros((3,3)); M[i,j]=1; return M
so3=[E(1,2)-E(2,1), E(2,0)-E(0,2), E(0,1)-E(1,0)]
# i * (real symmetric traceless 3x3)
S=[]
S.append(np.diag([1,-1,0.0]))
S.append(np.diag([1,1,-2.0])/np.sqrt(3))
for i,j in [(0,1),(0,2),(1,2)]:
    M=np.zeros((3,3)); M[i,j]=M[j,i]=1; S.append(M)
quad=[1j*s for s in S]
basis=so3+quad
print("   so(3) generators (real antisymmetric)      : %d"%len(so3))
print("   quadrupole i.Sym^2_0 (the candidate gluons): %d"%len(quad))
print("   total                                      : %d   (dim su(3) = 8: %s)"%(len(basis),len(basis)==8))
ah=all(np.allclose(B.conj().T,-B) for B in basis)
tr=all(abs(np.trace(B))<1e-12 for B in basis)
print("   all anti-hermitian? %s     all traceless? %s   -> all lie in su(3): %s"%(ah,tr,ah and tr))
M=np.array([B.flatten() for B in basis])
print("   rank of the 8 generators = %d  -> they SPAN su(3): %s"%(np.linalg.matrix_rank(M),
      np.linalg.matrix_rank(M)==8))

print("\nTABLE 3 -- CLOSURE, sector by sector (the actual test)")
def inspan(X,B):
    A=np.array([b.flatten() for b in B]).T
    c,res,rk,_=np.linalg.lstsq(A,X.flatten(),rcond=None)
    return np.linalg.norm(A@c-X.flatten())
def maxres(As,Bs,target):
    return max(inspan(A@B-B@A,target) for A in As for B in Bs)
r1=maxres(so3,so3,so3); r2=maxres(so3,quad,quad); r3=maxres(quad,quad,so3)
print("   bracket              lands in        max residual")
print("   [so(3), so(3)]       so(3)           %.2e"%r1)
print("   [so(3), quadrupole]  quadrupole      %.2e"%r2)
print("   *** [quad, quad]     so(3)           %.2e  <-- THE DECIDING ONE ***"%r3)
closes = max(r1,r2,r3)<1e-10
print("   ==> *** CLOSES EXACTLY: %s ***"%closes)
print("       [iS, iS'] = -[S,S'] and the commutator of two symmetric matrices is ANTISYMMETRIC,")
print("       so the quadrupoles bracket back into so(3). That IS su(3)'s Cartan decomposition.")

print("\nTABLE 4 -- and are the structure constants su(3)'s? (Killing-form signature test)")
def ad(X,B):
    A=np.array([b.flatten() for b in B]).T
    cols=[np.linalg.lstsq(A,(X@b-b@X).flatten(),rcond=None)[0] for b in B]
    return np.array(cols).T
K=np.array([[np.trace(ad(X,basis)@ad(Y,basis)).real for Y in basis] for X in basis])
ev=np.linalg.eigvalsh(K)
print("   Killing form eigenvalues: %s"%np.round(ev,3))
print("   all strictly negative? %s  -> the real form is COMPACT"%bool(np.all(ev<-1e-9)))
print("   ==> compact + dim 8 + rank 2 => *** su(3), not sl(3,R) and not su(2,1). ***")
print("       (sign matters: [Q,Q] = -[S,S'] gives the COMPACT form; the opposite sign would give")
print("        the split form sl(3,R). The check above fixes which.)")

print("\n"+"="*104)
print("VERDICT -- definite, as asked")
print("="*104)
print(" *** YES on the algebra. The l=2 quadrupole operators close into so(3), and the resulting")
print("     8-dimensional algebra is su(3) -- compact real form, verified by the Killing signature. ***")
print("   And the shape IS in the second shell: 14 = Sym^2_0(5) contains Sym^2_0(V_12) = 5 (Table 1).")
print()
print(" *** BUT -- AND THIS IS THE WHOLE HONEST CONTENT -- WHAT I VERIFIED IS AN IDENTITY, NOT A")
print("     DERIVATION. *** so(3) (+) i.Sym^2_0(R^3) = su(3) is a TEXTBOOK Cartan decomposition. It is")
print("     true of ANY real 3-space, with or without BST. So this hands us:")
print("       - a CONTAINER: the second shell has room for the shape, and the shape closes;")
print("       - NOT a MECHANISM: nothing here forces BST's shell operators to BE these generators")
print("         with these brackets.")
print()
print(" *** THE GAP, NAMED PRECISELY: the test I was asked for is a TOEPLITZ check, and Toeplitz")
print("     operators do NOT commute like matrices. *** [T_f, T_g] =/= T_{[f,g]}; the leading term is")
print("     the Poisson bracket and there are corrections. Closure of the SYMBOLS (verified above)")
print("     does not give closure of the OPERATORS. The genuine test is whether the Toeplitz")
print("     corrections vanish or conspire -- and that I did NOT compute.")
print("   ==> so the honest answer is: *** YES at symbol level, OPEN at operator level. *** The shape")
print("       and the algebra are confirmed; the su(3) is not yet earned as a BST result, because a")
print("       shared algebra is not a shared object -- the same discipline that just decided")
print("       SU(3)-vs-SO(3) against us, applied to ourselves this time.")
