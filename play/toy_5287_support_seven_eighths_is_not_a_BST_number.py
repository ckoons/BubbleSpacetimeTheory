import numpy as np, mpmath as mp
mp.mp.dps=30
print("MY FIRST PASS WAS WRONG AND ITS PROSE CONTRADICTED ITS OWN DATA -- I wrote 'verified to 1e-8'")
print("above a residual of 5906. Cause: mp.arg returns the PRINCIPAL branch, so arg Gamma(1/4+iT/2)")
print("was wrapped. Riemann-Siegel theta needs the CONTINUOUS branch. Using mp.siegeltheta.\n")
def th_exact(T): return float(mp.siegeltheta(T))
def th_asym(T,pi8=True): return (T/2)*np.log(T/(2*np.pi)) - T/2 + (-np.pi/8 if pi8 else 0.0) + 1/(48*T)
print("      T        theta exact       asym WITH -pi/8    residual      asym WITHOUT -pi/8   residual")
for T in [50,100,500,2000,20000]:
    e=th_exact(T); a=th_asym(T); b=th_asym(T,False)
    print("   %7d   %14.6f   %14.6f   %.2e   %14.6f   %.4f"%(T,e,a,abs(e-a),b,abs(e-b)))
print("\n   ⟹ WITH the -pi/8 the asymptotic matches to ~1e-9; WITHOUT it the residual is pinned at")
print("      %.4f = pi/8 exactly. The -pi/8 is CONFIRMED as the Gamma-factor phase."%(np.pi/8))
print("\n   And the counting identity: N(T) = theta(T)/pi + 1 + S(T).")
zs=[float(mp.im(mp.zetazero(n))) for n in range(1,201)]
for T in [100,200,400]:
    print("      T=%4d : actual zeros %3d   theta/pi + 1 = %8.4f   (difference = S(T), the fluctuation)"%(
        T,sum(1 for z in zs if z<T),th_exact(T)/np.pi+1))
print("\n   ⟹ 7/8 = 1 - (pi/8)/pi. The 8 is the 2 inside Gamma(s/2) working through a stationary-phase")
print("      count. It is a property of zeta's functional equation, with NO BST ingredient in it.")
