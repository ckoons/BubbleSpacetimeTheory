import numpy as np, sys, time
exec(open('bigN.py').read().split('def interval_r')[0])
rng=np.random.default_rng(815)

# ---- the BD operator: layer-weighted sum. Coefficients are DIMENSION-SPECIFIC. ----
# B[phi](x) = pref_d * ( -phi(x) + sum_i C_i^(d) * sum_{y in L_i(x)} phi(y) )
# L_i(x) = { y < x : exactly i-1 elements strictly between }.
BD = {2: (2.0,      [1, -2, 1]),
      3: (1.0,      [1, -3, 3, -1]),          # candidate; validated below, not asserted
      4: (4/np.sqrt(6), [1, -9, 16, -8]),
      5: (1.0,      [1, -20, 60, -60, 20])}   # candidate; validated below, not asserted

def layers(C, maxlayer=5):
    """C = strict causal matrix (bool). Returns list of bool matrices L_i (i=1..maxlayer)."""
    Ci = C.astype(np.int32)
    nb = Ci @ Ci                    # nb[y,x] = #{z : y<z<x}
    return [ (C & (nb == i-1)) for i in range(1, maxlayer+1) ]

def BD_on_ones(C, d, rho):
    """B applied to phi==1, per element; continuum limit ∝ -R/2  => 0 for FLAT space."""
    pref, cs = BD[d]
    L = layers(C, len(cs))
    tot = -np.ones(C.shape[0], float)
    for c, Li in zip(cs, L):
        tot += c * Li.sum(axis=0)          # sum over y in L_i(x)
    return pref * tot * rho**(-2.0/d)      # discreteness scale l ~ rho^(-1/d)

print("="*80)
print("BD DISCRETE CURVATURE -- CALIBRATION FIRST, with the wrong-d control")
print("="*80)
print("CORPUS CHECK: grep found NO Benincasa-Dowker in notes/ or play/. This is a NEW IMPORT,")
print("not a corpus reconnect. Flagging that up front.")
print()
print("★ THE TRAP (same as toy 5253): BD's coefficients are DIMENSION-SPECIFIC. Running the 4D")
print("  operator and reading 'flat 4D' would be putting 4D in. So: run EVERY d-operator on the")
print("  SAME causal set. Only the correct d should give ~0 on a flat sprinkling.")
print()
print("CALIBRATION on sprinkled FLAT Minkowski (R=0, so the correct-d operator must -> 0):")
print("   true d   N      B_2         B_3         B_4         B_5     -> which is ~0?")
for dtrue in [2,3,4]:
    for N in [600,1200]:
        t,fut,pas,sub=make_MINK(N,dtrue)
        allJ=np.arange(N)
        C=np.zeros((N,N),bool)
        for i in range(N): C[i,:]=fut(i,allJ)
        C=C.T                                   # C[y,x] = y < x
        rho=N/1.0
        vals={}
        for d in [2,3,4,5]:
            b=BD_on_ones(C,d,rho)
            # interior only: drop elements near the boundary of the diamond (few relations)
            deg=C.sum(axis=0)+C.sum(axis=1)
            keep=deg>np.percentile(deg,60)
            vals[d]=np.mean(b[keep])
        best=min(vals,key=lambda k:abs(vals[k]))
        print("   d=%d      %4d  %+10.3g  %+10.3g  %+10.3g  %+10.3g   -> d=%d"%(
            dtrue,N,vals[2],vals[3],vals[4],vals[5],best))
        sys.stdout.flush()
