import numpy as np
from scipy.integrate import quad
from math import gamma, pi
print("I USED THE WRONG REGION FOR n=2 AND MY OWN RATIO CAUGHT IT: I got 100.0 for a 10x increase in")
print("Lam -- that is Lam^2, not a log. Cause: I took {uv >= d^2, u+v <= 2Lam}, whose area is dominated")
print("by the BULK. The Berry-Keating region is the BOUNDED one, {u >= lu, v >= lv, uv <= E}.")
print("Region-matching applies to my own comparison. Redone properly, in cone-polar coordinates.\n")
print("="*92)
print("CONE-POLAR: x_0 = rho cosh(chi), |xvec| = rho sinh(chi)  =>  Delta = rho^2, and")
print("   d^n x = rho^{n-1} drho * sinh^{n-2}(chi) dchi * dOmega_{n-2}")
print("Region {Delta <= E, chi <= X}:   V = [E^{n/2}/n] * |S^{n-2}| * INT_0^X sinh^{n-2}(chi) dchi")
print("and the BK cutoffs u >= lu, v >= lv with uv <= E give exactly  X = (1/2) log(E/(lu lv)).")
print("="*92)
def rap_integral(n,X):
    if n==2: return X                       # sinh^0 = 1
    return quad(lambda c: np.sinh(c)**(n-2), 0, X)[0]
print("\n  THE RAPIDITY INTEGRAL is where the log lives or dies:")
print("      X      n=2 (sinh^0)   n=3 (sinh^1)   n=4 (sinh^2)   n=5 (sinh^3)")
for X in [2,4,6,8]:
    print("   %5.1f    %12.3f  %13.3f  %13.3f  %13.3e"%(X,rap_integral(2,X),rap_integral(3,X),rap_integral(4,X),rap_integral(5,X)))
print("\n  ⟹ n=2 is LINEAR in the rapidity X; every n>=3 is EXPONENTIAL in X (the transverse sphere")
print("     grows like e^{(n-2)X}).")
print()
print("  Now substitute X = (1/2) log(E/cell) -- the BK cutoff -- and read the E-dependence:")
cell=2*np.pi
print("        E          n=2: V/E            n=3: V/E^{3/2}     n=4: V/E^2      n=5: V/E^{5/2}")
for E in [1e2,1e4,1e6,1e8]:
    X=0.5*np.log(E/cell)
    row=[]
    for n in [2,3,4,5]:
        S=2.0 if n==2 else 2*pi**((n-1)/2)/gamma((n-1)/2)
        V=(E**(n/2)/n)*S*rap_integral(n,X)
        row.append(V/E**(n/2))
    print("   %9.0e   %14.4f   %16.2f  %14.2f  %14.2f"%(E,row[0],row[1],row[2],row[3]))
print("\n  ⟹ n = 2 : V/E = (1/2)log(E/cell) -- GROWS LOGARITHMICALLY. THIS IS THE RIEMANN COUNT.")
print("     n >= 3 : V/E^{n/2} grows like a POWER of E as well -- the log is destroyed.")
print()
print("  the clean statement:  INT_0^X sinh^{n-2} dchi  is LINEAR in X only when n-2 = 0.")
print("  ⟹ ★ THE LOGARITHM EXISTS ONLY ON A 2-DIMENSIONAL CONE. It is the RAPIDITY EXTENT of the")
print("     region, and only for n=2 is the transverse sphere a point (S^0) so that rapidity-extent")
print("     and volume coincide. For n>=3 the transverse sphere grows like e^{(n-2)X} and eats it.")
print()
print("  BST's Type IV cone is the forward light cone in R^{4,1}: n = 5.  =>  NO LOG.")
