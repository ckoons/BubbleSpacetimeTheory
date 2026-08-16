import numpy as np, mpmath as mp
mp.mp.dps=30
print("="*90)
print("THE HILBERT-POLYA TEST THAT COMES BEFORE EVERYTHING: THE COUNTING FUNCTION.")
print("="*90)
print("If H is the operator whose eigenvalues are the zero heights t_n, then N_H(T) MUST equal the")
print("Riemann-von Mangoldt count. That is checkable BEFORE any question of self-adjointness or of")
print("why Re = 1/2 -- and it is a hard constraint, not a soft one.\n")
print("(1) CALIBRATE: Riemann-von Mangoldt against the actual zeros.")
zs=[float(mp.im(mp.zetazero(n))) for n in range(1,201)]
def N_rh(T): return (T/(2*np.pi))*np.log(T/(2*np.pi)) - T/(2*np.pi) + 7/8
print("      T        actual zeros below T     RvM formula")
for T in [50,100,200,400]:
    print("    %5d           %4d                  %8.2f"%(T,sum(1 for z in zs if z<T),N_rh(T)))
print("    => RvM is exact to O(log T). Density dN/dT = log(T/2pi)/2pi -- it grows LOGARITHMICALLY.\n")
print("(2) BST's forced self-adjoint operator (T2562 v3 Kostant cubic Dirac). From my toy 5244, the")
print("    ANALYTIC shape at truncation N is exact:  lambda_max = 2N^2 + 9N + 14,  modes = 32*C(N+5,5).")
from math import comb
print("      N    lambda_max = 2N^2+9N+14    modes = 32*C(N+5,5)")
for N in range(2,9):
    print("    %3d          %6d                  %8d"%(N,2*N*N+9*N+14,32*comb(N+5,5)))
print("    => eliminating N:  N ~ sqrt(lambda/2)  and  modes ~ 32 N^5/120")
print("       so  N_BST(lambda) ~ C * lambda^{5/2}  -- A POWER LAW, exponent 2.5.\n")
def N_bst(lam):
    Nn=(-9+np.sqrt(81+8*(lam-14)))/4
    return 32*np.exp(sum(np.log(Nn+k) for k in range(1,6)))/120 if Nn>0 else 0.0
print("(3) THE COMPARISON, on the same variable T:")
print("      T        Riemann zeros    BST v3 Dirac modes      ratio BST/Riemann")
for T in [50,100,400,1600,6400]:
    a=N_rh(T); b=N_bst(T)
    print("    %6d        %8.1f          %12.1f            %10.1f"%(T,a,b,b/a))
print("\n  ⟹ THE BST OPERATOR HAS VASTLY MORE EIGENVALUES, AND THE EXCESS DIVERGES like T^{3/2}/log T.")
print("     The two counting functions are not close and do not become close. THE IDENTIFICATION IS")
print("     NOT MERELY UNPROVEN -- IT IS EXCLUDED BY THE WEYL LAW.")
print()
print("(4) AND THE OBSTRUCTION IS GENERAL, NOT A DETAIL OF THIS OPERATOR:")
print("    a self-adjoint elliptic operator on a COMPACT manifold of dimension d obeys Weyl:")
print("        N(lambda) ~ C lambda^{d/m}   =>  density ~ lambda^{d/m - 1}, ALWAYS A POWER.")
print("    the Riemann density is  log(T/2pi)/2pi  -- slower than every power T^eps, faster than a")
print("    constant. NO compact-manifold Weyl law of ANY dimension produces it.")
print("    density check (Riemann): ")
for T in [1e2,1e4,1e6,1e8]:
    print("       T=%8.0e   dN/dT = %.4f    vs T^0.1 = %8.2f"%(T,np.log(T/(2*np.pi))/(2*np.pi),T**0.1))
print("    ⟹ the Hilbert-Polya operator cannot be a Dirac or Laplace operator on a compact space.")
print("       (This is Berry-Keating's observation; here it is applied to BST's own candidate.)")
