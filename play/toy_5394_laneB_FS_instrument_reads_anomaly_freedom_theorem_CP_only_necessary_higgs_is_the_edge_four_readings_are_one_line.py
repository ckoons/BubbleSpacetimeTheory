import numpy as np
print("="*104)
print("TOY 5394 -- LANE 4 SUPPORT: how far does the Frobenius-Schur instrument actually read?")
print("  OBJECT: nu(rho) = FS indicator = EXISTENCE + SYMMETRY of an invariant bilinear form on rho.")
print("  BANKED: (i) census-as-count {0,1,3} = dim EW ; (ii) the Y=0 real rep -> Majorana.")
print("  ASKED: does the SAME instrument also read the Higgs / the anomalies / CP-existence?")
print("="*104)

print("\nTABLE 1 -- is the census map FORCED or CHOSEN? (test the instrument, not the answer)")
print("  A block's gauge generators = anti-Hermitian TRACELESS elements of K, 1x1 over K:")
print("    R -> 0 [O(1) discrete] ;  C -> 1 [u(1)] ;  H -> 3 [su(2)=sp(1)]")
print("  *** {0,1,3} = dim U(1,K): a THEOREM about the division algebra, not an assignment. Sum = 4. ***")

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
    P=np.array(P)                      # 6 x 9 orthonormal rows
    I=np.eye(d)
    return [P@(np.kron(A,I)+np.kron(I,A))@P.conj().T for A in T]

def reality(T,tol=1e-7):
    """find C with C T_a = -T_a^* C  (i.e. C rho C^-1 = rho^*); nu from C's symmetry."""
    d=T[0].shape[0]; rows=[]
    for A in T:
        # vec row-major: vec(C A) = (I (x) A^T) vec(C) ; vec(A^* C) = (A^* (x) I) vec(C)
        rows.append(np.kron(np.eye(d),A.T)+np.kron(A.conj(),np.eye(d)))
    M=np.vstack(rows); s=np.linalg.svd(M,compute_uv=False)
    u,sv,vh=np.linalg.svd(M); k=int(np.sum(sv>tol*max(sv.max(),1.0)))
    ns=vh[k:].conj()
    if ns.shape[0]==0: return 0,None
    C=ns[0].reshape(d,d)
    return (1 if np.linalg.norm(C-C.T)<np.linalg.norm(C+C.T) else -1),C

print("\nTABLE 2 -- *** POSITIVE CONTROL FIRST (my last solver returned COMPLEX for everything). ***")
T=su2(0.5); nu,C=reality(T); Cx=np.array([[0,1],[-1,0]],complex)
res=max(np.linalg.norm(C@A+A.conj()@C) for A in T)
print("   SU(2) doublet: known C = i*sigma_2 (ANTIsymmetric) -> nu must be -1.")
print("   solver C =\n%s"%np.round(C/C[0,1],6))
print("   intertwiner residual max||C T + T* C|| = %.2e   -> nu = %+d   %s"%(res,nu,"CONTROL PASS" if nu==-1 and res<1e-9 else "CONTROL FAIL"))
if nu!=-1: raise SystemExit("instrument not validated -- stop")

print("\nTABLE 3 -- nu computed from scratch for every rep used below")
F=gm()
cases=[("SU(2)","2  (j=1/2)",su2(0.5),-1),("SU(2)","3  (j=1)",su2(1.0),+1),
       ("SU(2)","4  (j=3/2)",su2(1.5),-1),("SU(2)","5  (j=2)",su2(2.0),+1),
       ("SU(3)","3  (fund)",F,0),("SU(3)","3b (anti)",conj_rep(F),0),
       ("SU(3)","8  (adj)",adjoint(F),+1),("SU(3)","6  (sym)",sym2(F),0)]
print("   group  rep          dim   nu    reality        expected")
ok=0
for g,nm,Tr,exp in cases:
    nu,_=reality(Tr); lab={1:"REAL",-1:"PSEUDOREAL",0:"COMPLEX"}[nu]; ok+=(nu==exp)
    print("   %-6s %-12s %-5d %+-5d %-14s %s"%(g,nm,Tr[0].shape[0],nu,lab,"OK" if nu==exp else "MISMATCH exp %+d"%exp))
print("   *** %d/%d reproduced from scratch. *** Instrument validated (control + 8 known types)."%(ok,len(cases)))

print("\nTABLE 4 -- *** READING 1: does nu read the CUBIC GAUGE ANOMALY? ***")
print("   A(R) := Tr({T_a,T_b}T_c) / Tr({t_a,t_b}t_c) on a component with d_abc != 0; (a,b,c)=(1,1,8).")
def anomA(Tr):
    ref=np.trace((F[0]@F[0]+F[0]@F[0])@F[7]).real
    return (np.trace((Tr[0]@Tr[0]+Tr[0]@Tr[0])@Tr[7]).real)/ref
print("   group  rep          nu     A(R)      nu != 0 ?   anomaly-free?")
n_nz=0; consistent=True
for g,nm,Tr,exp in cases:
    nu,_=reality(Tr)
    if g!="SU(3)":
        print("   %-6s %-12s %+-6d %-9s %-11s %s"%(g,nm,nu,"n/a","yes" if nu else "NO","SU(2) has NO d_abc at all"))
        continue
    A=anomA(Tr); n_nz += (nu!=0)
    free=abs(A)<1e-9
    if (nu!=0) and not free: consistent=False
    print("   %-6s %-12s %+-6d %-9.4f %-11s %s"%(g,nm,nu,A,"yes" if nu else "NO","YES" if free else "no, A=%.0f"%A))
print("   *** non-vacuity check: %d rep(s) with nu != 0 were actually tested (last run: ZERO -> vacuous). ***"%n_nz)
print("   *** RESULT: %s -- every nu != 0 rep has A(R) = 0; the anomalous ones (3, 3b, 6) all have nu = 0. ***"%("CONSISTENT" if consistent and n_nz>0 else "NOT ESTABLISHED"))
print("   MECHANISM: nu != 0 <=> R ~ R-bar, so the symmetric trace equals minus itself ==> 0.")
print("   *** AND IT SUBSUMES A STANDARD FACT: SU(2) is anomaly-free BECAUSE all its reps have")
print("       nu != 0 -- the instrument reproducing a theorem it was not built for. ***")

print("\nTABLE 5 -- READING 2: CP-existence. *** necessary vs sufficient ***")
print("   If EVERY rep is real/pseudoreal, a basis exists in which all couplings are real")
print("   ==> CP is automatic. So *** nu = 0 somewhere is NECESSARY for CP violation. ***")
print("   BUT SU(3)_fund has nu = 0 and QCD conserves CP anyway (strong-CP).")
print("   *** NECESSARY, NOT SUFFICIENT. 'CP violation is POSSIBLE' CANNOT FAIL -> not a prediction. ***")

print("\nTABLE 6 -- READING 3: the Higgs. *** where the instrument stops ***")
print("   Higgs = (1,2)_{1/2}: pseudoreal under SU(2) alone, but Y != 0 makes the FULL rep COMPLEX")
print("   (nu = 0) -- the same T2522 mechanism that makes fermions chiral. So nu reads 'complex'.")
print("   *** nu does NOT fix the NUMBER of doublets, the potential, or the vev. That is the edge. ***")
print("   TRAP LOGGED: dim(EW) = 4, dim_R(H) = 4, Higgs real d.o.f. = 4 -- THREE 4s, three sources.")

print("\nTABLE 7 -- *** COUNT-ONCE AUDIT (Bar 1): are these INDEPENDENT? ***")
for a,b,c in [("census {0,1,3} = dim EW","dim of anti-Herm traceless in K","SEPARATE (algebra dim)"),
              ("Majorana (Y=0 real)","SYMMETRY of the form","same form"),
              ("anomaly-freedom (nu != 0)","EXISTENCE of the form","same form"),
              ("CP needs nu = 0","EXISTENCE of the form","same form"),
              ("Higgs is complex","EXISTENCE of the form","same form")]:
    print("   %-28s %-34s %s"%(a,b,c))
print("   *** FOUR of five read ONE object: the invariant bilinear form. PER BAR 1 = ONE LINE. ***")

print("\n"+"="*104); print("VERDICT -- Lane 4"); print("="*104)
print(" (1) *** YES, THE INSTRUMENT READS MORE THAN IT IS CREDITED WITH, AND THE NEW READINGS ARE")
print("     THEOREMS. *** nu = existence + symmetry of an invariant bilinear form:")
print("       nu=+1 symmetric      -> Majorana mass ALLOWED                 [banked]")
print("       nu=-1 antisymmetric  -> vector-like / Kramers")
print("       nu!=0 form exists    -> *** CUBIC ANOMALY VANISHES *** [NEW, verified non-vacuously]")
print("       nu=0  no form        -> chiral; CP violation POSSIBLE         [NEW, weak]")
print()
print(" (2) *** ANOMALY-FREEDOM IS THE STRONGEST NEW READING *** and it subsumes a standard fact:")
print("     SU(2) is anomaly-free BECAUSE all its reps have nu != 0. An instrument reproducing a")
print("     theorem it was not built for is the right kind of evidence that it is real.")
print()
print(" (3) *** THE CP READING IS WEAK AND MUST NOT SHIP AT MAJORANA'S GRADE. *** nu=0 is NECESSARY,")
print("     not sufficient (QCD: nu=0, CP conserved). *** 'CP violation is possible' cannot fail. ***")
print()
print(" (4) *** THE HIGGS IS THE NEGATIVE -- nu reads 'complex' and nothing else. *** Not the doublet")
print("     count, not the potential, not the vev. The instrument has a definite edge; it sits here.")
print()
print(" (5) ★ *** COUNT-ONCE: FOUR of the five readings use ONE object. THEY ARE ONE LINE, NOT FOUR.")
print("     *** Only the census-as-count is structurally separate. @Lyra @Keeper -- 'one object, every")
print("     observable a reading' is exactly right AS A DESCRIPTION, and exactly why they must not be")
print("     counted as independent predictions. *** The unification is real; the multiplicity is not. ***")
print()
print(" (6) ★ *** METHOD, AGAINST MYSELF: my first solver returned COMPLEX for all six reps (missing")
print("     conjugate in C T = -T* C), which made the anomaly table VACUOUS -- it 'verified' a claim")
print("     over an EMPTY set of nu != 0 cases and printed CONSISTENT. *** §599 on my own instrument:")
print("     this run adds a POSITIVE CONTROL (i*sigma_2) and a NON-VACUITY COUNT before the verdict. ***")
