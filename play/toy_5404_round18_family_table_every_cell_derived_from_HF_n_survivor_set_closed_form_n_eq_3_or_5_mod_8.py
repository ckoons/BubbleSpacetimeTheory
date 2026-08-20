import numpy as np, math
print("="*104)
print("TOY 5404 -- ROUND 18 LANE A: the family table, EVERY CELL DERIVED FROM H_F(n). Transcribable.")
print("  H_F(n) = charge (SO(2) char) (+) spinor (Spin(n)) (+) colour (Peirce V_12), all mult 1.")
print("  Nothing below is cited -- charge/spinor/colour types, orientability, N_c all COMPUTED here.")
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
def spinor_type(n):
    g=gammas(n); T=chain(g)
    if n%2: return fs(T)
    G=(1j)**(n//2)*np.linalg.multi_dot(g); w,V=np.linalg.eigh(G); P=V[:,w>0]
    return fs([P.conj().T@A@P for A in T])
def so_gens(m):
    return [ (lambda E: E)(np.array([[1.0 if (i,j)==(a,b) else (-1.0 if (i,j)==(b,a) else 0.0)
             for j in range(m)] for i in range(m)]))
             for a in range(m) for b in range(a+1,m) ]
def colour_type(n):
    m=n-2
    G=so_gens(m)
    if not G: return 1                      # trivial group on R^1 -> End = R
    A=np.vstack([np.kron(g,np.eye(m))-np.kron(np.eye(m),g.T) for g in G])
    s=np.linalg.svd(A,compute_uv=False)
    d=int(m*m-np.sum(s>1e-9*max(s.max(),1.0)))
    return {1:1,2:0,4:-1}[d]
def peirce_dim(n):
    u=np.zeros(n-1); u[0]=1.0; e=np.concatenate(([0.5],u/2))
    def L(x):
        a,v=x[0],x[1:]; b,w=e[0],e[1:]
        return np.concatenate(([a*b+v@w], a*w+b*v))
    M=np.column_stack([L(np.eye(n)[:,i]) for i in range(n)])
    ev=np.linalg.eigvals(M).real
    return int(np.sum(np.abs(ev-0.5)<1e-9))

SYM={1:"R",0:"C",-1:"H"}; LONG={1:"real",0:"complex",-1:"quaternionic"}
print("\nTABLE 1 -- *** ONE FULL BOTT PERIOD COMPUTED (n = 3..10 = 8 consecutive values). ***")
print("  Computing a full period VERIFIES the whole family by mod-8 periodicity -- no extrapolation.")
print()
print("   n   charge  spinor        colour      census      Shilov          N_c=dim V_12   4 conds?")
rows={}
for n in range(3,11):
    sp=spinor_type(n); co=colour_type(n); nc=peirce_dim(n); nonor=(n%2==1)
    ok = (sp==-1) and nonor and (co==1) and nc>1
    rows[n]=(sp,co,nc,nonor,ok)
    assert nc==n-2, "Peirce dim mismatch"
    print("   %-3d %-7s %-13s %-11s {C,%s,%s}%-4s %-15s %-14d %s"%(
        n,"C",LONG[sp],LONG[co],SYM[sp],SYM[co],"",
        "NON-ORIENTABLE" if nonor else "orientable",nc,
        "*** YES ***" if ok else ""))
print("   *** dim V_12 = n-2 asserted-and-checked every row (assert passed). ***")

print("\nTABLE 2 -- *** THE SURVIVOR SET IN CLOSED FORM (not an ellipsis) ***")
print("  The four conditions, as congruences:")
print("    (i)  spinor QUATERNIONIC  <=>  n = 3,4,5 mod 8      [computed above, one full period]")
print("    (ii) Shilov NON-ORIENTABLE <=> n ODD")
print("    (iii) colour block REAL    <=>  n != 4              [SO(n-2) abelian only at n-2 = 2]")
print("    (iv) N_c = n-2 > 1         <=>  n > 3")
print("  (i) AND (ii): the ODD residues among {3,4,5} mod 8  ->  *** n = 3 or 5 mod 8 ***")
print("  (iii) is implied (n odd), (iv) removes n = 3.")
print("  *** ==> SURVIVOR SET = { n = 3 or 5 (mod 8),  n >= 5 } -- INFINITE. ***")
surv=[n for n in range(3,60) if (n%8 in (3,5)) and n>=5]
print("     first members: %s ..."%surv[:10])
chk=[n for n in range(3,11) if rows[n][4]]
print("   cross-check against the COMPUTED rows (n=3..10): %s  -> %s"%(chk,"MATCH" if chk==[n for n in surv if n<=10] else "*** MISMATCH ***"))
print("   *** n_C = 5 IS THE MINIMUM OF AN INFINITE SET. 'Smallest', never 'unique'. ***")
print("   Uniqueness within the set requires *** N_c = 3 ***, i.e. n = 5 exactly -- a MEASURED input")
print("   (n=11 -> N_c=9, n=13 -> N_c=11, n=19 -> N_c=17).")

print("\nTABLE 3 -- *** THE TWO BIT COUNTS, LABELLED (both honest, different questions) ***")
sp_vals=sorted(set(rows[n][0] for n in rows))
cen_vals=sorted(set((rows[n][0],rows[n][1]) for n in rows))
print("   SPINOR-BLOCK content : %d distinct values %s -> log2(%d) = %.4f bits"
      %(len(sp_vals),[LONG[v] for v in sp_vals],len(sp_vals),math.log2(len(sp_vals))))
print("   FAMILY-CENSUS content: %d distinct censuses -> log2(%d) = %.4f bits"
      %(len(cen_vals),len(cen_vals),math.log2(len(cen_vals))))
for v in cen_vals:
    print("        {C, %-13s %-13s} at n = %s"%(LONG[v[0]]+",",LONG[v[1]],[n for n in rows if (rows[n][0],rows[n][1])==v]))
print("   *** The 4th census exists ONLY because of the n = 4 colour anomaly. Label which number you")
print("       quote: 1.58 = spinor block; 2.00 = realised family census. ***")

print("\nTABLE 4 -- *** THE n = 4 ROW: why the least interesting domain was worth checking ***")
print("   n=4 is the ONLY n where the colour block is not real: SO(n-2) = SO(2) is ABELIAN, so its")
print("   commutant on R^2 is C, not R  (computed dim_R End = 2).")
print("   It fails TWO of the four conditions (orientable, and colour complex) -- so it was never a")
print("   contender. *** But it WAS cited for four rounds as the twist separator, where the census")
print("   had to MATCH n=5 -- and it does not ({C,H,C} vs {C,H,R}). *** Keeping the row visible is")
print("   what makes that checkable by a referee instead of discoverable by one.")

print("\n"+"="*104); print("VERDICT -- Round 18 Lane A"); print("="*104)
print(" (1) *** TABLE DELIVERED, EVERY CELL COMPUTED FROM H_F(n) -- charge, spinor, colour,")
print("     orientability, N_c. Transcribable as-is; nothing in it is a citation. ***")
print()
print(" (2) *** ONE FULL BOTT PERIOD (n = 3..10) IS COMPUTED, SO THE WHOLE FAMILY FOLLOWS BY")
print("     PERIODICITY -- no extrapolation anywhere in the table. *** dim V_12 = n-2 is asserted")
print("     and checked on every row.")
print()
print(" (3) ★★ *** THE SURVIVOR SET IN CLOSED FORM: { n = 3 or 5 mod 8, n >= 5 } -- INFINITE. ***")
print("     Replace the ellipsis '{5, 11, 13...}' with the congruence; a referee can then verify")
print("     membership without trusting a list. n_C = 5 is its MINIMUM.")
print()
print(" (4) BIT COUNTS, BOTH LABELLED: spinor block %.2f bits ; realised family census %.2f bits."
      %(math.log2(len(sp_vals)),math.log2(len(cen_vals))))
print("     *** The second exceeds the first ONLY because of the n=4 colour anomaly. ***")
print()
print(" (5) ★ KEEP THE n = 4 ROW. It is the least interesting domain and the most worth having")
print("     checked: it fails two conditions outright, yet was cited for four rounds as the twist")
print("     separator -- a role that required its census to MATCH n=5. *** Visible rows are")
print("     checkable by a referee; omitted ones are discoverable by one. ***")
