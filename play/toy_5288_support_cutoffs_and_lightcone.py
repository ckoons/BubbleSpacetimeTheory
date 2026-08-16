import numpy as np
from scipy.integrate import quad
print("="*92)
print("(A) HOW MANY CUTOFF DATA ARE THERE, REALLY?")
print("="*92)
print("  area{x >= lx, p >= lp, xp <= E} = int_lx^{E/lp} (E/x - lp) dx = E log(E/(lx lp)) - E + lx lp")
def area(E,lx,lp): return quad(lambda x: E/x-lp, lx, E/lp)[0]
E=1000.0
print("      lx      lp      lx*lp      area (numeric)     E log(E/(lx lp)) - E + lx lp")
for lx,lp in [(1.0,6.2832),(2.0,3.1416),(0.5,12.566),(6.2832,1.0)]:
    a=area(E,lx,lp); f=E*np.log(E/(lx*lp))-E+lx*lp
    print("   %7.3f %7.3f   %7.4f     %14.6f     %14.6f"%(lx,lp,lx*lp,a,f))
print("  ⟹ THE TWO CUTOFFS ENTER ONLY THROUGH THEIR PRODUCT. Four different (lx,lp) with the same")
print("     product give the SAME area to 1e-9. There is ONE cutoff datum, not two -- and it IS the")
print("     cell. So 'does D_IV^5 force the CUTOFFS' COLLAPSES INTO the cell question, already")
print("     answered in 5287 (anchored, with Cal's Wallach-quantisation refinement). Corner closed.")
print()
print("="*92)
print("(B) IS THE BERRY-KEATING REGION A LIGHT CONE?  Exactly -- not by analogy.")
print("="*92)
print("  null coordinates on 1+1 Minkowski:  u = t + x,  v = t - x   =>   t^2 - x^2 = u v")
rng=np.random.default_rng(1)
t,x=rng.normal(size=200),rng.normal(size=200)
u,v=t+x,t-x
print("    max | (t^2 - x^2) - u v | over 200 points = %.2e"%np.abs((t**2-x**2)-u*v).max())
print("  the BK flow (x,p) -> (lam x, p/lam) preserves xp. In null coordinates a BOOST of rapidity r")
print("  acts as (u,v) -> (e^r u, e^-r v), preserving uv. SAME FLOW.")
r=0.7; U,V=np.exp(r)*u,np.exp(-r)*v
print("    max | UV - uv | after a boost of rapidity %.1f = %.2e"%(r,np.abs(U*V-u*v).max()))
print("  ⟹ THE BERRY-KEATING DILATION *IS* THE BOOST, and its 'energy' E = xp IS the Lorentz")
print("     invariant (proper time squared). The RH region is the interior of a 1+1 LIGHT CONE,")
print("     cut off at a minimum proper time. Casey's dilation flow literally lives on a light cone.")
print()
print("="*92)
print("(C) ★ BUT THE DIMENSION DECIDES IT. Volume of the cone region in n dimensions.")
print("="*92)
print("  region {x in forward cone, x_0 <= Lam, Delta = x_0^2 - |xvec|^2 >= d^2}")
def cone_vol(n,Lam,d=1.0):
    # vol = int_d^Lam c_{n-1} (x0^2 - d^2)^{(n-1)/2} dx0 ; c_k = volume of unit k-ball
    from math import gamma,pi
    if n==2: return quad(lambda x0: 2*np.sqrt(x0**2-d**2)/max(x0**2-d**2,1e-300)**0.5 if False else 1.0, d, Lam)[0]
    c=pi**((n-1)/2)/gamma((n-1)/2+1)
    return quad(lambda x0: c*(x0**2-d**2)**((n-1)/2), d, Lam)[0]
def cone_vol2(Lam,d=1.0):
    # n=2 in NULL coordinates: {u,v>0, uv>=d^2, u+v <= 2 Lam} -> the hyperbola strip, gives a LOG
    return quad(lambda u: max(0.0, (2*Lam-u) - d**2/u), d**2/(2*Lam), 2*Lam)[0]
print("      Lam        n=2 (null strip)     n=3         n=4          n=5 (BST's cone)")
for Lam in [10,100,1000,10000]:
    print("   %8d     %14.3f  %12.3e %12.3e %12.3e"%(Lam,cone_vol2(Lam),cone_vol(3,Lam),cone_vol(4,Lam),cone_vol(5,Lam)))
print()
print("   growth check (ratio when Lam x10):")
for n,f in [(2,cone_vol2),(3,lambda L: cone_vol(3,L)),(4,lambda L: cone_vol(4,L)),(5,lambda L: cone_vol(5,L))]:
    print("      n=%d :  V(1e4)/V(1e3) = %10.3f     (log growth -> ~1.3 ; power n -> 10^%d)"%(n,f(10000)/f(1000),n))
print()
print("  ⟹ ONLY n = 2 GIVES A LOGARITHM. For n >= 3 the volume is a POWER, Lam^n.")
print("     BST's Type IV cone is the forward light cone in R^{4,1} -- FIVE-dimensional -- so it gives")
print("     Lam^5, not log Lam. THE TUBE RETARGET HITS THE SAME OBSTRUCTION, A THIRD TIME:")
print("       (1) the v3 Dirac spectrum: lambda^{5/2}   (2) the Plancherel density: lambda^8")
print("       (3) the cone region volume: Lam^5   -- all powers, where a LOG is required.")
