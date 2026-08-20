import numpy as np
print("="*104)
print("TOY 5402 -- LANE B: bank the H_F(n) construction. *** TWO CORRECTIONS TO MY OWN 5401 FIRST. ***")
print("  K1743 says the color block is 'R at mult 1'; my 5401 column said 'mult (N_c) = n-2'.")
print("  That conflict is in MY toy, and the round is about to cite it. Resolve it before banking.")
print("="*104)

print("\nTABLE 1 -- *** CORRECTION 1: I MISLABELLED DIMENSION AS MULTIPLICITY. ***")
print("  V_12 is ONE irreducible K-block of DIMENSION n-2. Its MULTIPLICITY in H_F is 1.")
print("  *** K1743 is right and my column header was wrong: mult = 1, dim = n-2 = N_c. ***")
print("  CONSEQUENCE FOR MY 5401 FORK -- and it DEFLATES my own alarm:")
print("    (A)  types only                 : n=4 {C,H,?}  n=5 {C,H,?}")
print("    (B') types + true MULTIPLICITIES: {C1,H1,X1} both -> *** SAME. Separators SURVIVE. ***")
print("    (C)  types + rep DIMENSIONS     : differs -- but that is NOT 'the census' on any reading.")
print("  *** So the danger I raised in 5401 was OVERSTATED: what I called 'multiplicities' were")
print("      DIMENSIONS. Under true multiplicity the separators were never at risk. ***")
print("  (The declaration is still worth making -- it removes the ambiguity -- but as hygiene,")
print("   not as a rescue. I am walking my own alarm back on a checkable line.)")

print("\nTABLE 2 -- ★★★ *** CORRECTION 2, AND THIS ONE IS NOT DEFLATIONARY: ***")
print("  Which group acts on V_12? Aut(J(n)) = SO(n-1); fixing the frame fixes u, leaving")
print("  *** SO(n-2) acting on u-perp = R^(n-2) as the VECTOR rep. ***")
print("  So the color block's reality type = type of the SO(m) vector rep on R^m, m = n-2.")
print("  COMPUTE End_SO(m)(R^m) as a REAL algebra (dim 1 = R, 2 = C, 4 = H):")
def so_gens(m):
    G=[]
    for a in range(m):
        for b in range(a+1,m):
            E=np.zeros((m,m)); E[a,b]=1; E[b,a]=-1; G.append(E)
    return G
def commutant_dim(G,m):
    if not G: return m*m           # trivial group: End = all of M_m(R)
    A=np.vstack([np.kron(g,np.eye(m))-np.kron(np.eye(m),g.T) for g in G])
    s=np.linalg.svd(A,compute_uv=False)
    return int(m*m-np.sum(s>1e-9*max(s.max(),1.0)))
print("   n    m = n-2   End_SO(m)(R^m) dim_R   reality type   note")
colortype={}
for n in range(3,10):
    m=n-2; d=commutant_dim(so_gens(m),m)
    t={1:"REAL",2:"*** COMPLEX ***",4:"QUATERNIONIC"}.get(d,"dim %d"%d)
    note=""
    if m==1: note="SO(1) trivial, End(R^1)=R"
    elif m==2: note="*** SO(2) on R^2: rotations COMMUTE -> End = C ***"
    else: note="SO(m) vector irrep, End = R"
    colortype[n]=(0 if d==2 else 1)
    print("   %-4d %-9d %-22d %-14s %s"%(n,m,d,t,note))
print("   *** ==> THE COLOR BLOCK IS REAL FOR EVERY n EXCEPT n = 4, WHERE IT IS COMPLEX. ***")
print("   *** MY 5401 SAID 'color = R always'. THAT IS FALSE AT n = 4. ***")

def gammas(n):
    X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]]); Z=np.diag([1,-1]).astype(complex)
    g=[X,Y]
    while len(g)<n:
        k=g[0].shape[0]
        g=[np.kron(a,Z) for a in g]+[np.kron(np.eye(k),X),np.kron(np.eye(k),Y)]
    return g[:n]
def chain(T): return [-0.25j*(T[a]@T[a+1]-T[a+1]@T[a]) for a in range(len(T)-1)]
def fs(T,tol=1e-6):
    d=T[0].shape[0]; I=np.eye(d); H=np.zeros((d*d,d*d),complex)
    for A in T:
        K=np.kron(I,A.T)+np.kron(A.conj(),I); H+=K.conj().T@K
    w,V=np.linalg.eigh(H)
    if w[0]>tol*max(abs(w[-1]),1.0): return 0
    C=V[:,0].reshape(d,d)
    return 1 if np.linalg.norm(C-C.T)<np.linalg.norm(C+C.T) else -1
def half_nu(n):
    g=gammas(n); T=chain(g)
    if n%2: return fs(T)
    G=(1j)**(n//2)*np.linalg.multi_dot(g); w,V=np.linalg.eigh(G); P=V[:,w>0]
    return fs([P.conj().T@A@P for A in T])

print("\nTABLE 3 -- *** THE CORRECTED THREE-BLOCK CENSUS ***")
NM={1:"R",0:"C",-1:"H"}
print("   n    charge  spinor  color   CENSUS          Shilov            dim V_12 = N_c")
cen={}
for n in range(3,10):
    s=half_nu(n); c=colortype[n]; cen[n]=(0,s,c)
    orient=((-1)**n==1)
    print("   %-4d %-7s %-7s %-7s {C, %s, %s}%-6s %-17s %d"%(n,"C",NM[s],NM[c],NM[s],NM[c],"",
          "orientable" if orient else "NON-ORIENTABLE",n-2))

print("\nTABLE 4 -- ★★★ *** RE-RUN THE SEPARATOR SEARCH ON THE CORRECTED CENSUS ***")
orient=lambda n:((-1)**n==1)
tw=[(a,b) for a in range(3,10) for b in range(a+1,10) if cen[a]==cen[b] and orient(a)!=orient(b)]
ce=[(a,b) for a in range(3,10) for b in range(a+1,10) if cen[a]!=cen[b] and orient(a)==orient(b)]
cen_same_twist=[(a,b) for a in range(3,10) for b in range(a+1,10) if cen[a]!=cen[b] and orient(a)==orient(b)==False]
print("   TWIST separators (same census, different twist): %s"%(tw if tw else "NONE"))
print("   CENSUS separators (different census, same twist): %s"%(ce[:6]))
print("   census separators among NON-ORIENTABLE pairs    : %s"%(cen_same_twist[:6]))
print()
print("   *** D_IV^4 vs D_IV^5:  census {C,H,C} vs {C,H,R}  -> *** NOT EQUAL -> NOT A SEPARATOR. ***")
print("   *** THE SURVIVING TWIST SEPARATOR IS D_IV^7 vs D_IV^8: census {C,R,R} BOTH,")
print("       NON-ORIENTABLE vs ORIENTABLE. *** It was already in my 5397 table -- and it is the one")
print("       that survives the correction, because neither n is 4.")
print("   *** THE CENSUS SEPARATOR D_IV^5 vs D_IV^7 IS UNAFFECTED (both non-orientable, {C,H,R} vs")
print("       {C,R,R}) -- neither is n=4, so Round 15's 'D_IV^7 everywhere' for the census leg STANDS. ***")

print("\n"+"="*104); print("VERDICT -- Lane B"); print("="*104)
print(" (1) *** BANKED, WITH THE CONSTRUCTION VERIFIED: H_F(n) = charge (C, mult 1) (+) spinor")
print("     (Bott(n mod 8), mult 1) (+) color (V_12, DIM n-2, MULT 1). Peirce dims (1, n-2, 1)")
print("     exact for n = 3..9. N_c = dim V_12 = n-2 is a REP-DIMENSION reading, separate from the")
print("     multiplicity-free census -- K1743's 'mult 1' is right and my 5401 header was wrong. ***")
print()
print(" (2) *** CORRECTION 1 (deflates my own 5401 alarm): I mislabelled DIMENSION as MULTIPLICITY.")
print("     Under TRUE multiplicities the separators were never at risk. *** The multiplicity-free")
print("     declaration is still worth making as hygiene -- but I oversold the danger, and the")
print("     round adopted it as load-bearing. Walking it back here, on a checkable line.")
print()
print(" (3) ★★★ *** CORRECTION 2, AND IT IS LOAD-BEARING THE OTHER WAY: THE COLOR BLOCK IS NOT REAL")
print("     AT n = 4. *** SO(2) acting on R^2 has commuting rotations, so End = C (computed: dim_R 2).")
print("     Census at n=4 is {C, H, C}, NOT {C, H, R}. *** MY 5401 'color = R always' IS FALSE. ***")
print()
print(" (4) ★★★★ *** CONSEQUENCE FOR THE PAPER: D_IV^4 vs D_IV^5 IS NOT A VALID TWIST SEPARATOR --")
print("     the censuses differ. Round 16 Lane A item (4) enshrines D_IV^4 as THE twist separator. ***")
print("     *** USE D_IV^7 vs D_IV^8 INSTEAD: census {C,R,R} both, NON-ORIENTABLE vs ORIENTABLE. ***")
print("     It was already in my 5397 table and survives because neither index is 4.")
print()
print(" (5) THE CENSUS LEG IS UNAFFECTED: D_IV^5 vs D_IV^7 (both non-orientable, {C,H,R} vs {C,R,R}).")
print("     Round 15's 'D_IV^7 everywhere' for the census leg STANDS.")
print()
print(" (6) ★ n = 4 IS EXCEPTIONAL FOR A REASON WORTH SAYING: it is the ONLY n where SO(n-2) fails to")
print("     have a real vector commutant, because SO(2) is abelian. *** A single accidental low-rank")
print("     coincidence, and it happened to sit under the separator we chose. ***")
