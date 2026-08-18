import numpy as np, sympy as sp
from math import factorial, exp, sqrt
from scipy.optimize import brentq
print("="*92)
print("GATE A -- FIRING LYRA'S MAP.  rho_nu(r) ∝ r^{2a-1} (1-r^2)^{b(nu)},  r_* = the PEAK.")
print("="*92)
r,b,a=sp.symbols('r b a', positive=True)
L=(2*a-1)*sp.log(r)+b*sp.log(1-r**2)
sol=sp.solve(sp.diff(L,r),r)
rstar2=sp.simplify(sol[0]**2)
print("  d/dr[(2a-1)ln r + b ln(1-r^2)] = 0  =>  r_*^2 = %s"%sp.simplify(rstar2))
print("  a = n_C - 2 = 3 (FK type-IV multiplicity, PINNED F736 two ways) -> 2a-1 = 5")
f=sp.lambdify(b, rstar2.subs(a,3))
print("  ⟹  r_*^2(b) = 5/(2b+5)")
print()
print("  ★ FIRST, A TARGET-INNOCENT INTERNAL CHECK: the corpus puts the TAU at the SHILOV BOUNDARY")
print("    (nu=0, r->1, F666/T2517). Which b(nu) reading satisfies r_*(nu=0) = 1?")
readings=[("b = nu",            lambda nu: nu),
          ("b = g - nu",        lambda nu: 5-nu),
          ("b = g = 7 (const)", lambda nu: 7.0),
          ("b = nu + a/2",      lambda nu: nu+1.5),
          ("b = 2*nu",          lambda nu: 2*nu)]
print("\n      b(nu) reading        r_*^2(5/2)   r_*^2(3/2)   r_*^2(0)    tau at Shilov (r=1)?")
for name,fn in readings:
    v=[float(f(fn(x))) for x in (2.5,1.5,0.0)]
    print("      %-20s %9.4f    %9.4f    %8.4f    %s"%(name,v[0],v[1],v[2],"YES ✓" if abs(v[2]-1)<1e-9 else "no"))
print("\n  ⟹ ONLY b = nu puts the tau at r = 1. The corpus's own Shilov placement SELECTS b(nu) = nu,")
print("     target-innocently -- no mixing data used. That is a genuine internal pin, and I did not")
print("     choose it: it is the only reading that satisfies a constraint banked before this round.")
print()
print("="*92)
print("★★★ SO FIRE IT: b(nu) = nu  =>  r_*^2 = 5/(2 nu + 5)")
print("="*92)
def c(k,p):
    z=sqrt(p) if p>0 else 1e-12
    return exp(-p/2)*z**k/sqrt(factorial(k))
def cab(p): return (c(2,p)+c(4,p))/(c(0,p)+c(2,p))
tgt=0.2243/0.9743; need=brentq(lambda x: cab(x)-tgt,1e-9,3.0)
vals={nu: float(f(nu)) for nu in (2.5,1.5,0.0)}
print("      nu = 5/2 (gen 1) :  r_*^2 = %.6f   r_* = %.6f"%(vals[2.5],sqrt(vals[2.5])))
print("      nu = 3/2 (gen 2) :  r_*^2 = %.6f   r_* = %.6f"%(vals[1.5],sqrt(vals[1.5])))
print("      nu = 0   (gen 3) :  r_*^2 = %.6f   r_* = %.6f   <- Shilov boundary ✓"%(vals[0.0],sqrt(vals[0.0])))
print("\n  BLIND POST of the three radii, per K1002, before comparison. Now the bar:")
print("      required center p_u = %.4f, to within 0.49%%"%need)
for lab,p in [("p = r_*^2 = %.4f"%vals[2.5],vals[2.5]),("p = r_*   = %.4f"%sqrt(vals[2.5]),sqrt(vals[2.5]))]:
    dev=abs(p-need)/need
    print("      %s  ->  V_us/V_ud = %.4f  (obs %.4f)   dev in p = %6.1f%%   %s"%(
        lab,cab(p),tgt,100*dev,"PASSES" if dev<0.0049 else "**FAILS**"))
print()
print("  ⟹ ★★★★ GATE A: **FAIL**, on both readings of the center, by 30-95%% against a 0.49%% bar.")
print()
print("="*92)
print("AND THE PARAMETER COUNT KEEPER MADE BINDING -- what b WOULD be required?")
print("="*92)
for lab,tp in [("p = r_*^2",need),("p = r_*",need**2)]:
    breq=(5/tp-5)/2
    print("      to get %s = %.4f you need b = %.4f"%(lab,need if lab=="p = r_*^2" else need,breq))
print("      available corpus readings give b(5/2) in {2.5 (b=nu), 2.5 (g-nu), 7 (g), 4.0, 5.0}")
print("      ⟹ the required b = 4.233 is NOT any of them; and b = 4 (b = nu + a/2 at nu=5/2) is the")
print("        nearest, off by 5.8%% in b -- which is %.0f%% in p. Still far outside the bar."%(
    100*abs(float(f(4.0))-need)/need))
print()
print("  ★ THE HONEST READ: the map is RIGID (no free knob once b(nu) is chosen), which is the good")
print("    news Keeper wanted -- it CANNOT be tuned. And precisely because it is rigid, it MISSES.")
print("    A rigid map that misses is a real refutation; a tunable one that hits would have been")
print("    nothing. Lyra built the right kind of object and it does not land.")
