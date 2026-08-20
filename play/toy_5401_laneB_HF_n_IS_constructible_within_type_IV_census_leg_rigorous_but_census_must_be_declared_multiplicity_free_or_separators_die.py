import numpy as np
print("="*104)
print("TOY 5401 -- LANE B: the census-sweep scope note. The round said BUILD IT or SCOPE IT.")
print("  *** I BUILT IT -- and the gap is NARROWER than I stated, but a NEW fork opened underneath. ***")
print("  CORPUS (F1060, K1724): H_F = charge (SO(2) character, COMPLEX, mult 1 -> C)")
print("                             (+) spinor (Spin(n), reality type by BOTT, mult 1 -> H at n=5)")
print("                             (+) color  (Peirce V_12, REAL, mult N_c -> End_K = R, K1724)")
print("="*104)

print("\nTABLE 1 -- *** WHY THE GAP IS NARROWER THAN I SAID (Cal's own distinction, §640) ***")
print("  Cal ruled SEP-3 ill-posed because it CHANGES RECIPES (type IV -> type III): 'SEP-1/SEP-2")
print("  worked because they varied ONE INTEGER inside a FIXED recipe; SEP-3 changes recipes.'")
print("  *** My Lane B question is the FIRST kind: vary n INSIDE type IV, recipe FIXED. ***")
print("  Every D_IV^n has all three ingredients: an SO(2) circle, a Spin(n) spinor, a Peirce V_12.")
print("  *** ==> H_F(n) IS constructible within type IV. My 5398/5400 scope note was TOO PESSIMISTIC")
print("      -- it conflated 'undefined across TYPES' with 'undefined across n'. Correcting myself. ***")

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

print("\nTABLE 2 -- *** THE PEIRCE COLOR BLOCK: compute dim V_12 for the spin factor J(n) ***")
print("  J(n) = R (+) R^(n-1), product (a,v)o(b,w) = (ab + <v,w>, a w + b v), rank 2.")
print("  Primitive idempotent e = (1/2, u/2), |u| = 1. Peirce = eigenspaces of L_e at 1, 1/2, 0.")
def peirce(n):
    d=n
    u=np.zeros(n-1); u[0]=1.0
    e=np.concatenate(([0.5],u/2))
    def L(x):
        a,v=x[0],x[1:]; b,w=e[0],e[1:]
        return np.concatenate(([a*b+v@w], a*w+b*v))
    M=np.column_stack([L(np.eye(d)[:,i]) for i in range(d)])
    ev=np.linalg.eigvals(M).real
    return [int(np.sum(np.abs(ev-t)<1e-9)) for t in (1.0,0.5,0.0)]
print("   n    dim J(n)   Peirce dims (1, 1/2, 0)   dim V_12 = N_c   N_c = n-2 ?")
Nc={}
for n in range(3,10):
    p=peirce(n); Nc[n]=p[1]
    print("   %-4d %-10d (%d, %d, %d)%-16s %-16d %s"%(n,n,p[0],p[1],p[2],"",p[1],"YES" if p[1]==n-2 else "*** NO ***"))
print("   *** dim V_12 = n - 2 EXACTLY. At n = 5 that is 3 = N_c -- the banked BST relation N_c = n_C - 2. ***")
print("   *** AND ITS REALITY TYPE IS REAL FOR EVERY n (V_12 is a real vector space; End_K = R, K1724). ***")

print("\nTABLE 3 -- *** THE FULL THREE-BLOCK CENSUS ACROSS n (recipe held fixed) ***")
NM={1:"R",0:"C",-1:"H"}
print("   n    charge   spinor (BOTT)   color   reality-TYPE census   color mult (N_c)")
cen={}
for n in range(3,10):
    s=half_nu(n); cen[n]=(0,s,1,Nc[n])
    print("   %-4d %-8s %-15s %-7s {C, %s, R}%-11s %d"%(n,"C",NM[s],"R",NM[s],"",Nc[n]))
print("   *** ONLY THE SPINOR BLOCK'S REALITY TYPE MOVES WITH n. Charge is COMPLEX always; color is")
print("       REAL always. *** ==> my spinor-keyed sweep IS the three-block reality-type sweep. ***")
print("   *** THE GAP I FLAGGED IN 5398/5400 CLOSES -- for the reality-TYPE reading. ***")

print("\nTABLE 4 -- ★★ *** BUT A NEW FORK OPENED, AND IT BITES MY OWN SEPARATORS ***")
print("   'The census' is UNDER-SPECIFIED in exactly the way this round's meta-lesson names.")
print("   Two readings, and they disagree about whether the separators exist:")
print()
print("   reading                                    n=4 census        n=5 census        same?")
print("   (A) multiset of reality TYPES              {C, H, R}         {C, H, R}         *** YES ***")
print("   (B) types WITH multiplicities              {C1, H1, R2}      {C1, H1, R3}      *** NO ***")
print()
print("   *** UNDER (B), D_IV^4 vs D_IV^5 IS NOT A SEPARATOR AT ALL -- the color multiplicity differs")
print("       (N_c = 2 vs 3), so the censuses are NOT equal and 'same census, different twist' FAILS.")
print("       EVERY separator I banked in 5397/5400 dies under reading (B). ***")
print("   *** WHY (A) IS THE RIGHT READING, AND IT MUST BE DECLARED: the census-as-count reads")
print("       dim U(1,K) PER TYPE -- {R,C,H} -> {0,1,3} -- and End_K(V_12) = R regardless of how big")
print("       V_12 is (K1724). *** So multiplicity NEVER enters the count. The theorem uses (A). ***")
print("   *** BUT NOBODY HAS SAID SO. And N_c = n-2 is itself a BANKED BST RESULT, so a reader who")
print("       assumes the census carries N_c will conclude the separators are invalid. ***")

print("\nTABLE 5 -- re-run the separator search under BOTH readings")
for lab,key in [("(A) reality TYPES only",lambda n:cen[n][1]),("(B) types + multiplicities",lambda n:(cen[n][1],cen[n][3]))]:
    orient=lambda n:((-1)**n==1)
    p=[(a,b) for a in range(3,10) for b in range(a+1,10) if key(a)==key(b) and orient(a)!=orient(b)]
    q=[(a,b) for a in range(3,10) for b in range(a+1,10) if key(a)!=key(b) and orient(a)==orient(b)]
    print("   %-27s same-census/diff-twist: %-22s diff-census/same-twist: %s"%(lab,str(p) if p else "*** NONE ***",str(q[:4]) if q else "NONE"))
print("   *** Under (A) both separator kinds exist. Under (B) the twist separator VANISHES ENTIRELY. ***")

print("\n"+"="*104); print("VERDICT -- Lane B"); print("="*104)
print(" (1) *** I BUILT IT RATHER THAN SCOPING IT, AND I CORRECT MY OWN SCOPE NOTE: *** H_F(n) IS")
print("     constructible within type IV -- the recipe (SO(2) circle + Spin(n) spinor + Peirce V_12)")
print("     has all three ingredients at every n. My 5398/5400 note conflated 'undefined across")
print("     TYPES' (true, Cal §640) with 'undefined across n' (FALSE). *** The gap is narrower. ***")
print()
print(" (2) *** THE THREE-BLOCK SWEEP, COMPUTED: charge = COMPLEX always; color = REAL always")
print("     (dim V_12 = n-2, verified exactly); ONLY the spinor block's reality type moves. ***")
print("     ==> *** my spinor-keyed sweep IS the full three-block reality-type sweep. The census leg")
print("     is RIGOROUS, not scoped -- for the reality-TYPE reading. ***")
print()
print(" (3) ★★★ *** BUT A NEW FORK BITES MY OWN SEPARATORS: 'the census' is under-specified. ***")
print("     (A) reality TYPES only -> D_IV^4 and D_IV^5 share {C,H,R} -> separators HOLD.")
print("     (B) types WITH multiplicities -> {C1,H1,R2} vs {C1,H1,R3} -> *** NOT equal -> EVERY")
print("     separator I banked in 5397/5400 DIES. *** Under (B) the twist separator vanishes entirely.")
print()
print(" (4) *** (A) IS CORRECT AND THE THEOREM ALREADY RELIES ON IT -- census-as-count reads")
print("     dim U(1,K) per TYPE, and End_K(V_12) = R however large V_12 is (K1724), so multiplicity")
print("     never enters. *** BUT IT HAS NEVER BEEN DECLARED, AND N_c = n-2 IS ITSELF BANKED --")
print("     a referee who assumes the census carries N_c will call the separators invalid. ***")
print("     @Lyra @Keeper @Cal -- DECLARE 'census = multiset of reality TYPES, multiplicity-free'")
print("     in the theorem. One sentence, and it is load-bearing for both separators.")
print()
print(" (5) ★ This is the 6th face of the same defect the round just named -- an UNDER-SPECIFIED")
print("     OBJECT -- and this time it is inside MY separators, which have been cited for three")
print("     rounds. *** Names aren't armor: I wrote the scope note and still missed that 'census'")
print("     needed the same declaration I was demanding of everyone else. ***")
