import numpy as np, sys, time
exec(open('bigN.py').read().split('def interval_r')[0])
rng=np.random.default_rng(816)
BD4=(4/np.sqrt(6),[1,-9,16,-8]); BD2=(2.0,[1,-2,1])

def causal_matrix(N,fut):
    allJ=np.arange(N); C=np.zeros((N,N),bool)
    for i in range(N): C[i,:]=fut(i,allJ)
    return C.T                                  # C[y,x] = y < x

def BD_ones(C,pref,cs,rho,d):
    Cf=C.astype(np.float32); nb=(Cf@Cf).astype(np.int32)
    tot=-np.ones(C.shape[0],np.float64)
    for i,c in enumerate(cs,start=1):
        tot += c*((C&(nb==i-1)).sum(axis=0))
    deg=C.sum(axis=0)+C.sum(axis=1)
    keep=deg>np.percentile(deg,60)              # interior only
    return float(np.mean(tot[keep]))*pref*rho**(-2.0/d)

print("="*80)
print("DIAGNOSIS of my own failed calibration, then the corrected criterion")
print("="*80)
print("TWO DEFECTS IN MY FIRST DESIGN:")
print(" (a) my d=3 and d=5 coefficients were GUESSES (binomial-shaped), not the published BD sets.")
print("     I labelled them 'candidate, not asserted' and they are NOT validated. Dropped.")
print(" (b) ★ SIXTH CONFOUND: comparing |B_d| ACROSS operators is invalid -- they carry different")
print("     prefactors and layer counts, so different noise floors. B_2 'won' almost everywhere by")
print("     being the QUIETEST operator, not the right one. Magnitude-at-one-N is not a selector.")
print()
print("CORRECTED CRITERION (and it is what the prompt asked for): CONVERGENCE IN N.")
print("  the correct-d operator -> 0 as N grows on a FLAT sprinkling; wrong-d does not.")
print()
print("CONTROL -- flat 4D Minkowski, B_4 (correct) vs B_2 (wrong), growing N:")
print("    N      B_4            B_2")
for N in [400,800,1600,3200]:
    t,fut,pas,sub=make_MINK(N,4); C=causal_matrix(N,fut)
    b4=BD_ones(C,*BD4,rho=N,d=4); b2=BD_ones(C,*BD2,rho=N,d=2)
    print("   %4d   %+12.5f   %+12.5f"%(N,b4,b2)); sys.stdout.flush()
