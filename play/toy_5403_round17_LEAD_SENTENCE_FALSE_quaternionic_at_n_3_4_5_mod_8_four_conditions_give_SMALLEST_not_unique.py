import numpy as np, math
print("="*104)
print("TOY 5403 -- ROUND 17: sweep the LEAD SENTENCE before it becomes the paper's first line.")
print("  CLAIM: 'the census turns on one trinary question -- is the spinor real, complex, or")
print("  quaternionic? -- and *** n_C = 5 is the UNIQUE value that makes it quaternionic ***.'")
print("  'UNIQUE' is a quantified claim. The round's own new standing rule: name the class and sweep it.")
print("="*104)

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
def so_gens(m):
    G=[]
    for a in range(m):
        for b in range(a+1,m):
            E=np.zeros((m,m)); E[a,b]=1; E[b,a]=-1; G.append(E)
    return G
def color_type(n):
    m=n-2
    if m<=0: return None
    if not so_gens(m): return 1
    A=np.vstack([np.kron(g,np.eye(m))-np.kron(np.eye(m),g.T) for g in so_gens(m)])
    s=np.linalg.svd(A,compute_uv=False)
    d=int(m*m-np.sum(s>1e-9*max(s.max(),1.0)))
    return {1:1,2:0,4:-1}.get(d,None)

print("\nTABLE 1 -- *** SWEEP THE TRINARY QUESTION (computed n = 3..14) ***")
NM={1:"REAL",0:"COMPLEX",-1:"QUATERNIONIC"}
sp={}
print("   n    n mod 8   spinor type      QUATERNIONIC?")
for n in range(3,15):
    s=half_nu(n) if n<=10 else {3:-1,4:-1,5:-1,6:0,7:1,0:1,1:1,2:0}[n%8]
    sp[n]=s
    print("   %-4d %-9d %-16s %s"%(n,n%8,NM[s],"*** YES ***" if s==-1 else ""))
quat=[n for n in sp if sp[n]==-1]
print("   *** QUATERNIONIC AT n = %s  (n = 3,4,5 mod 8) ***"%quat)
print("   *** ==> THE LEAD SENTENCE IS FALSE AS WRITTEN. n_C = 5 IS **NOT** THE UNIQUE VALUE ***")
print("       that makes the spinor quaternionic -- n = 3 and n = 4 do too, and so do 11, 12, 13.")
print("       *** THE TRINARY QUESTION ALONE DOES NOT SELECT 5. It selects a RESIDUE CLASS. ***")

print("\nTABLE 2 -- *** SO WHAT DOES SELECT n = 5? Add the conditions we have ALREADY PROVED. ***")
print("   n    spinor   Shilov            color block   N_c = n-2   survives?")
surv=[]
for n in range(3,15):
    s=sp[n]; nonor=(n%2==1); c=color_type(n) if n<=10 else 1
    ok = (s==-1) and nonor and (c==1) and (n-2)>1
    if ok: surv.append(n)
    print("   %-4d %-8s %-17s %-13s %-11d %s"%(n,NM[s][:4],"NON-ORIENT" if nonor else "orientable",
          NM[c][:4] if c is not None else "-", n-2, "*** SURVIVES ***" if ok else ""))
print("   conditions: (i) spinor QUATERNIONIC -> the weak force ; (ii) Shilov NON-ORIENTABLE -> chirality")
print("               (iii) colour block REAL -> no internal colour ; (iv) N_c = n-2 > 1 -> colour exists")
print("   *** SURVIVORS in 3..14: %s ***"%surv)
print("   *** n = 3 dies on (iv): N_c = 1, a single colour. n = 4 dies on (ii) AND (iii) (the SO(2)")
print("       abelian accident). n = 12 dies on (ii) (even -> orientable). ***")
print("   ★★★ *** BUT n = 11 AND n = 13 SURVIVE ALL FOUR. THE FOUR CONDITIONS DO **NOT** SELECT 5. ***")
print("   *** I caught this against my own table: my first draft of this toy asserted 'unique")
print("       survivor n = 5' in the prose while the table printed [5, 11, 13]. The table was right. ***")
print("   *** WHAT IS TRUE: n_C = 5 is the **SMALLEST** survivor. Uniqueness needs one more input --")
print("       N_c = 3 exactly (n=5 -> 3, n=11 -> 9, n=13 -> 11), which is MEASURED, not derived. ***")

print("\nTABLE 3 -- *** THE HONEST INFORMATION CONTENT (the round asks for 1.58 bits) ***")
cens={}
for n in range(3,11):
    cens[n]=(0,sp[n],color_type(n))
vals=sorted(set(cens.values()))
print("   distinct censuses realised across D_IV^n, n = 3..10:")
for v in vals:
    ns=[n for n in cens if cens[n]==v]
    print("     {C, %-12s %-12s}  at n = %s"%(NM[v[1]]+",",NM[v[2]],ns))
print("   *** %d DISTINCT CENSUS VALUES -> log2(%d) = %.4f BITS. ***"%(len(vals),len(vals),math.log2(len(vals))))
print("   The round quotes 1.58 bits (= log2 3, spinor-only). *** That is right IF the colour block is")
print("   held REAL -- but the n = 4 accident makes colour COMPLEX there, giving a 4th census value")
print("   and log2(4) = 2.00 bits over the full family. ***")
print("   ==> BOTH numbers are defensible; they answer different questions:")
print("       *** 1.58 bits = the SPINOR block's content (what the trinary question carries).")
print("           2.00 bits = the census's ACTUAL realised content across D_IV^n. ***")
print("   Say which one you are quoting. Either is far below my old 4.75-bit CAPACITY, which was an")
print("   upper bound on a channel, not the content of this one -- the round is right to prefer the")
print("   realised number as the headline.")

print("\n"+"="*104); print("VERDICT -- Round 17 lead-sentence check"); print("="*104)
print(" (1) ★★★★ *** THE LEAD SENTENCE IS FALSE AS WRITTEN, AND IT IS THE PAPER'S FIRST LINE. ***")
print("     'n_C = 5 is the unique value that makes the spinor quaternionic' -- *** n = 3 and n = 4")
print("     are quaternionic too *** (Bott: n = 3,4,5 mod 8; also 11,12,13). The trinary question")
print("     selects a RESIDUE CLASS, not a value. @Lyra -- do NOT ship this sentence.")
print()
print(" (2) *** BUT n = 5 IS STILL SELECTED -- by four conditions we have ALREADY PROVED: ***")
print("       (i) spinor QUATERNIONIC (weak force)      -> n = 3,4,5 mod 8")
print("       (ii) Shilov NON-ORIENTABLE (chirality)    -> n odd            -> kills n = 4")
print("       (iii) colour block REAL (no internal SU(3)) -> kills n = 4 again (SO(2) accident)")
print("       (iv) N_c = n - 2 > 1 (colour exists at all)  -> kills n = 3 (single colour)")
print("     *** SURVIVORS IN 3..14: n = 5, 11, 13. So the four conditions give MINIMALITY, not")
print("     uniqueness: n_C = 5 is the SMALLEST. *** Uniqueness needs N_c = 3, a MEASURED input.")
print()
print(" (3) *** SUGGESTED REPLACEMENT (checkable, and it matches what the corpus ALREADY banked): ***")
print("     'Within D_IV, four proved conditions -- a quaternionic spinor (the weak force), a")
print("      non-orientable Shilov boundary (chirality), a real colour block (no internal colour),")
print("      and more than one colour -- are satisfied by n_C = 5 and by no SMALLER value.'")
print("     *** SMALLEST, not UNIQUE. *** n = 11 and 13 also pass all four; only N_c = 3 (a MEASURED")
print("     input) picks 5 out of them. This is exactly the banked 'unique SMALLEST-that-does-physics'")
print("     (Strong-Uniqueness) form -- *** the round's new sentence WEAKENED a correct claim into a")
print("     false one by swapping 'smallest' for 'unique'. Restore the corpus wording. ***")
print()
print(" (4) ON THE BIT COUNT: 1.58 = log2(3) is the SPINOR block's content; 2.00 = log2(4) is the")
print("     census's REALISED content across the family (the n=4 accident adds a 4th value).")
print("     *** Both honest, different questions -- say which. *** And the round is right that my old")
print("     4.75 was a CAPACITY (upper bound), not this channel's content.")
print()
print(" (5) ★★ THIS IS THE 7TH FACE OF THE SAME DEFECT -- an unswept quantifier -- and it landed in")
print("     the LEAD SENTENCE, one round after the rule was made standing. The sweep took one")
print("     function call against data already on disk.")
print("     ★ *** AND IT CAUGHT ME TOO: my own first replacement sentence claimed n=5 ALONE satisfies")
print("     the four conditions, while my own table printed [5, 11, 13]. I wrote a false uniqueness")
print("     claim WHILE correcting a false uniqueness claim. *** The table caught it, not my care --")
print("     which is the argument for printing the table above the verdict, every time.")
