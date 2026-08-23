import numpy as np
# rho_Lambda(tau) = c0 + sum c_k exp(-lam_k tau), lam_k = k(k+5)  [F799/§4751]
K=6
lam = np.array([0.0]+[k*(k+5) for k in range(1,K+1)])   # lam_0 = 0 (zero mode c0)
def stats(c, tau):
    w = c*np.exp(-lam*tau); p = w/w.sum()
    r   = (p*lam).sum()                 # r = <lam> = -dln rho/dtau
    var = (p*lam**2).sum() - r**2
    return r, var, var/r                # B = Var/r  <- the true bar

print("lam_k =", lam.astype(int), "  lam_1 = C2 =", int(lam[1]))
print(f"{'profile':<14}{'tau':>6}{'r':>10}{'Var':>12}{'B=Var/r':>10}{'C2=6':>7}{'B<6?':>7}")
profiles = {
 'equipartition': np.array([1.0]+[1.0]*K),
 'decreasing':    np.array([1.0]+[1.0/k**2 for k in range(1,K+1)]),
 'single-mode':   np.array([1.0]+[1.0]+[0.0]*(K-1)),
 'c0-dominant':   np.array([20.0]+[1.0]*K),
}
for name,c in profiles.items():
    for tau in (0.10,0.20,0.30,1.0,5.0):
        r,var,B = stats(c,tau)
        print(f"{name:<14}{tau:>6.2f}{r:>10.4f}{var:>12.4f}{B:>10.4f}{6:>7}{str(B<6):>7}")
    print()
# no-zero-mode case (c0 = 0): pure decaying mixture
c = np.array([0.0]+[1.0]*K)
print("c0 = 0 (no attractor):")
for tau in (0.10,0.5,2.0,5.0):
    r,var,B = stats(c,tau); print(f"   tau={tau:<5} r={r:8.4f} Var={var:10.4f} B={B:8.4f}")
