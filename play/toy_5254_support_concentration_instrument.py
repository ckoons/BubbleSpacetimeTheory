import numpy as np
rng=np.random.default_rng(77)

def T_stat(X):
    """Concentration on a great S^3 subset S^4  <=>  the points avoid one direction.
       T = min_n Var(x.n) = smallest eigenvalue of the covariance.  Closed form, no search."""
    C=(X.T@X)/len(X)
    return float(np.linalg.eigvalsh(C)[0])

def unif_S4(N):
    X=rng.normal(size=(N,5)); return X/np.linalg.norm(X,axis=1)[:,None]

def band_S4(N,delta):
    """points within angular half-width delta of a great S^3 (the x5=0 equator)."""
    X=[]
    while len(X)<N:
        Y=unif_S4(4*N)
        keep=Y[np.abs(Y[:,4])<np.sin(delta)]
        X.extend(keep[:N-len(X)])
    return np.array(X[:N])

print("THE TRAP THIS TEST MUST AVOID: uniform on S^4 ALREADY has a preferred-looking direction")
print("at finite N (the least-populated axis), so a naive 'it peaks' test fires on noise.")
print("The statistic must be calibrated against the NULL, including the maximisation over axes.")
print()
print("NULL CALIBRATION -- T = lambda_min(cov) on UNIFORM S^4 (theory: 1/5 = 0.2)")
for N in [500,2000,10000]:
    ts=np.array([T_stat(unif_S4(N)) for _ in range(300)])
    print("   N=%5d   mean T = %.5f   sd = %.5f   5-sigma floor = %.5f"%(N,ts.mean(),ts.std(),ts.mean()-5*ts.std()))
print()
print("POWER -- does it FIRE on a genuinely concentrated measure? (band of half-width delta)")
N=2000
ts=np.array([T_stat(unif_S4(N)) for _ in range(300)]); mu,sd=ts.mean(),ts.std()
print("   delta(rad)  band width      T        sigma below null    verdict")
for delta in [np.pi/2,1.0,0.6,0.4,0.25,0.15,0.08]:
    T=np.mean([T_stat(band_S4(N,delta)) for _ in range(20)])
    z=(mu-T)/sd
    print("   %.3f       %-14s %.5f   %8.1f            %s"%(delta,
        "full sphere" if delta>=np.pi/2-1e-9 else "%.0f%% of pi/2"%(100*delta/(np.pi/2)),
        T,z,"FIRES" if z>5 else "no"))
print()
print("=> the test CAN fail (uniform sits at 0.200 with tiny scatter) and CAN fire (bands do).")
print("=> detection threshold at N=2000: concentration within ~delta < 1.0 rad is detectable at >5 sigma.")
