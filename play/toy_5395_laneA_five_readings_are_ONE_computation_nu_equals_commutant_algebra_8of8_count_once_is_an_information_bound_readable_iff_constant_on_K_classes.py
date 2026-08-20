import numpy as np, math
rng=np.random.default_rng(7)
print("="*104)
print("TOY 5395 -- LANE A: are the five reality-type readings ONE computation, or five cousins?")
print("  DECIDABLE FORM: is there a SINGLE datum every reading is a function of?")
print("  *** This also RE-EXAMINES MY OWN 5394, which called the census-as-count 'structurally")
print("  separate' from the nu readings. I test that claim rather than carry it forward. ***")
print("="*104)

def su2(j):
    d=int(round(2*j+1)); m=np.array([j-i for i in range(d)])
    Jz=np.diag(m).astype(complex); Jp=np.zeros((d,d),complex)
    for i in range(1,d): Jp[i-1,i]=np.sqrt(j*(j+1)-m[i]*(m[i]+1))
    Jm=Jp.conj().T; return [(Jp+Jm)/2,(Jp-Jm)/(2j),Jz]
def gm():
    l=[np.zeros((3,3),complex) for _ in range(8)]
    l[0][0,1]=l[0][1,0]=1; l[1][0,1]=-1j; l[1][1,0]=1j
    l[2][0,0]=1; l[2][1,1]=-1; l[3][0,2]=l[3][2,0]=1
    l[4][0,2]=-1j; l[4][2,0]=1j; l[5][1,2]=l[5][2,1]=1
    l[6][1,2]=-1j; l[6][2,1]=1j; l[7]=np.diag([1,1,-2]).astype(complex)/np.sqrt(3)
    return [x/2 for x in l]
def conj_rep(T): return [-A.conj() for A in T]
def adjoint(T):
    n=len(T); f=np.zeros((n,n,n))
    for a in range(n):
        for b in range(n):
            cm=T[a]@T[b]-T[b]@T[a]
            for c in range(n): f[a,b,c]=(-2j*np.trace(cm@T[c])).real
    return [(-1j*f[a]).astype(complex) for a in range(n)]
def sym2(T):
    d=T[0].shape[0]; P=[]
    for i in range(d):
        for j in range(i,d):
            v=np.zeros((d,d),complex)
            if i==j: v[i,i]=1
            else: v[i,j]=v[j,i]=1/np.sqrt(2)
            P.append(v.reshape(-1))
    P=np.array(P); I=np.eye(d)
    return [P@(np.kron(A,I)+np.kron(I,A))@P.conj().T for A in T]
def fs(T,tol=1e-7):
    d=T[0].shape[0]
    M=np.vstack([np.kron(np.eye(d),A.T)+np.kron(A.conj(),np.eye(d)) for A in T])
    u,sv,vh=np.linalg.svd(M); k=int(np.sum(sv>tol*max(sv.max(),1.0))); ns=vh[k:].conj()
    if ns.shape[0]==0: return 0
    C=ns[0].reshape(d,d)
    return 1 if np.linalg.norm(C-C.T)<np.linalg.norm(C+C.T) else -1

def realify(M):
    A,B=M.real,M.imag
    return np.block([[A,-B],[B,A]])
def commutant_real(T,tol=1e-7):
    """REAL commutant of the REALIFIED rep. Returns (dim, orthonormal basis as 2d x 2d arrays)."""
    G=[realify(1j*A) for A in T]          # rep is exp(i theta T) -> algebra element i*T
    D=G[0].shape[0]
    M=np.vstack([np.kron(g,np.eye(D))-np.kron(np.eye(D),g.T) for g in G])
    u,sv,vh=np.linalg.svd(M); k=int(np.sum(sv>tol*max(sv.max(),1.0)))
    ns=vh[k:]
    return ns.shape[0],[v.reshape(D,D) for v in ns]
def trace_form_signature(basis):
    """EXACT discriminator. On the TRACELESS part of the algebra, Q(x)=tr(x^2):
       H  -> imaginary quaternions, x^2 = -|x|^2  ==> NEGATIVE DEFINITE
       M_2(R) -> contains diag(1,-1) with x^2=+I  ==> INDEFINITE
       Deterministic; no sampling of a measure-zero set."""
    D=basis[0].shape[0]
    # orthonormalise, then split off the identity direction
    V=np.array([b.reshape(-1) for b in basis]); V,_=np.linalg.qr(V.T); V=V.T
    E=[v.reshape(D,D) for v in V]
    Idir=np.eye(D).reshape(-1)/np.linalg.norm(np.eye(D))
    P=np.eye(len(E))-np.outer(V@Idir,V@Idir)
    w,U=np.linalg.eigh(P); keep=U[:,w>0.5].T            # traceless subspace coords
    E0=[sum(c*e for c,e in zip(row,E)) for row in keep]
    n=len(E0); Q=np.array([[np.trace(E0[i]@E0[j]).real for j in range(n)] for i in range(n)])
    ev=np.linalg.eigvalsh(Q); ev/=max(abs(ev).max(),1e-300)
    return ev

print("\nTABLE 1 -- *** THE PIVOT, DONE CORRECTLY: nu vs the commutant algebra K = End_G. ***")
print("  My previous run computed the COMPLEX commutant -- which is ALWAYS C*I (dim_R = 2) by Schur")
print("  over C, so it could not distinguish R/C/H at all and its own check printed FAILED.")
print("  *** The R/C/H split lives in the REALIFICATION. Correct expectations: ***")
print("    nu = 0  -> realification IRREDUCIBLE, End = C        -> dim_R 2")
print("    nu = -1 -> realification IRREDUCIBLE, End = H        -> dim_R 4, tr-form NEG DEFINITE (0+,3-)")
print("    nu = +1 -> realification = W (+) W,   End = M_2(R)   -> dim_R 4, tr-form INDEFINITE   (2+,1-)")
F=gm()
reps=[("SU(2) 2  (j=1/2)",su2(0.5)),("SU(2) 3  (j=1)",su2(1.0)),("SU(2) 4  (j=3/2)",su2(1.5)),
      ("SU(2) 5  (j=2)",su2(2.0)),("SU(3) 3  (fund)",F),("SU(3) 3b (anti)",conj_rep(F)),
      ("SU(3) 8  (adj)",adjoint(F)),("SU(3) 6  (sym)",sym2(F))]
print("\n   rep                nu   dim_R End   tr-form sig  algebra    predicted   match?")
NAME={1:"R",0:"C",-1:"H"}; ok=0
for nm,T in reps:
    nu=fs(T); d,B=commutant_real(T)
    if d==2: alg="C"; sig="n/a"
    elif d==4:
        ev=trace_form_signature(B); npos=int(np.sum(ev>1e-8)); nneg=int(np.sum(ev<-1e-8))
        sig="(%d+,%d-)"%(npos,nneg)
        alg="H" if npos==0 else "M_2(R)"
    else: alg="dim %d"%d; sig="n/a"
    pred={0:"C",-1:"H",1:"M_2(R)"}[nu]
    good=(alg==pred); ok+=good
    print("   %-18s %+-4d %-11d %-12s %-10s %-11s %s"%(nm,nu,d,sig,alg,pred,"OK" if good else "*** MISMATCH ***"))
print("   *** %d/%d MATCH. *** nu and the commutant algebra are THE SAME 3-VALUED DATUM, now verified"%(ok,len(reps)))
print("       by TWO independent computations (intertwiner symmetry; realified commutant + trace-form signature).")
if ok!=len(reps): raise SystemExit("*** identification NOT established -- stopping before the verdict ***")

print("\n   *** ==> I CORRECT MY 5394. *** I called the census-as-count 'structurally separate' because")
print("       it counts a DIMENSION. It is NOT separate: dim U(1,K) = {0,1,3} is a FUNCTION of K, and")
print("       K IS nu. *** All five readings are ONE instrument, not 4 + 1. ***")

print("\nTABLE 2 -- *** is EVERY reading a function of the ONE datum K? Build the lookup. ***")
print("   K       nu   gauge gens   Majorana mass    cubic anomaly   CP viol.    rep type")
for K,nu,g,maj,an,cp,rt in [("R",+1,0,"ALLOWED (sym)","VANISHES","forbidden","vector-like"),
                            ("C", 0,1,"forbidden","possible","POSSIBLE","chiral"),
                            ("H",-1,3,"forbidden (antisym)","VANISHES","forbidden","vector-like")]:
    print("   %-7s %+-4d %-12d %-16s %-15s %-11s %s"%(K,nu,g,maj,an,cp,rt))
print("   *** EVERY column is a FUNCTION of the first. ONE INPUT, FIVE OUTPUTS -> ONE COMPUTATION. ***")
print("   *** And they are not even five independent functions: anomaly, CP and chirality are the")
print("       SAME PARTITION {C} vs {R,H} -- i.e. the single BIT 'nu = 0?'. ***")

print("\nTABLE 3 -- *** THE INFORMATION CEILING: what makes count-once PROVABLE ***")
print("   one block: log2(3) = %.4f bits.  A_F has THREE blocks  ->  capacity = log2(27) = %.4f BITS."%(math.log2(3),math.log2(27)))
print("     gauge-generator count            needs the full 3-valued datum   -> 1.585 bits/block")
print("     Majorana / anomaly / CP / chirality  need only 'nu = 0?'          -> 1 bit/block")
print("   *** YOU CANNOT EXTRACT FIVE INDEPENDENT PREDICTIONS FROM 4.75 BITS. Count-once here is an")
print("       INFORMATION BOUND, not a stylistic preference. ***")

print("\nTABLE 4 -- *** THE CRITERION (the deliverable): READABLE IFF CONSTANT ON K-CLASSES ***")
print("   observable                        varies at fixed K?              readable?")
for a,b,c in [("gauge-group DIMENSION","no  (= dim U(1,K))","*** YES ***"),
  ("Majorana vs Dirac","no  (= symmetry of the form)","*** YES ***"),
  ("cubic anomaly vanishing","no  (= nu != 0)","*** YES ***"),
  ("CP violation POSSIBLE","no  (= nu = 0)","YES (existence only)"),
  ("CP violation OCCURS","YES (strong-CP: nu=0, no CPV)","*** NO ***"),
  ("number of Higgs doublets","YES","*** NO ***"),
  ("Higgs potential / vev","YES","*** NO ***"),
  ("number of generations","YES (K is per-block)","*** NO ***"),
  ("fermion MASSES","YES","*** NO ***"),
  ("WHICH SU(N) (the 8 gluons)","YES (K=R for any real block)","*** NO ***")]:
    print("   %-33s %-31s %s"%(a,b,c))
print("   *** THE CRITERION EXPLAINS THE BANKED NEGATIVES INSTEAD OF LISTING THEM: no internal color")
print("       group, no spectrum, no n_gen, no vev -- ALL vary at fixed K, so all are outside the")
print("       instrument BY THEOREM. One mechanism covering four separate negatives. ***")

print("\n"+"="*104); print("VERDICT -- Lane A"); print("="*104)
print(" (1) *** ONE COMPUTATION. CONFIRMED %d/%d, by two independent routes. *** The FS indicator and"%(ok,len(reps)))
print("     the commutant algebra K = End_G(rho) are the SAME 3-valued datum; every reading is a")
print("     function of it. @Grace @Cal -- Lane A's promotion test PASSES.")
print()
print(" (2) *** I CORRECT MY OWN 5394: the census-as-count is NOT structurally separate. *** dim U(1,K)")
print("     = {0,1,3} is a function of K, and K IS nu. The unification is STRONGER than I reported")
print("     and the count-once discipline is STRICTER: *** one line, not 4 + 1. ***")
print()
print(" (3) *** COUNT-ONCE IS AN INFORMATION BOUND: log2(27) = 4.75 bits total. *** Three of the five")
print("     readings share ONE BIT. Five independent predictions cannot come out of this.")
print()
print(" (4) ★★ *** THE DELIVERABLE IS A CRITERION, NOT A LIST: an observable is READABLE IFF IT IS")
print("     CONSTANT ON K-CLASSES *** -- decidable, same family as my 5382 locality criterion.")
print()
print(" (5) ★ FOR @Lyra's ASSET, BOTH HALVES: 'the internal SM has a minimal generating set of exactly")
print("     ONE linear-algebra invariant' is SUPPORTED -- with the rider that *** the invariant")
print("     generates STRUCTURE (group size, reality type, allowedness), NEVER SPECTRUM (masses,")
print("     couplings, counts). *** State both halves or the claim over-reads.")
print()
print(" (6) ★ METHOD, AGAINST MYSELF -- SECOND INSTRUMENT FAILURE IN TWO TOYS. 5394: a missing")
print("     conjugate made the anomaly table vacuous. 5395 (first run): I computed the COMPLEX")
print("     commutant, which is ALWAYS dim 2 by Schur, so it could not distinguish R/C/H even in")
print("     principle. *** Both were caught by a printed consistency check that disagreed with the")
print("     prose verdict -- the check earns its keep precisely when I am confident. ***")
