import sympy as sp
from math import comb
# (1) SO(n)xSO(2)-invariant harmonic polynomials of degree p on R^n + R^2: invariants are polys in s=|u|^2, t=|v|^2.
# Laplacian on f(s,t) with s=|u|^2 (n dims), t=|v|^2 (2 dims): 4 s f_ss + 2n f_s + 4 t f_tt + 4 f_t
def harmonic_invariants(n, p):
    if p % 2: return 0
    k = p//2
    s,t = sp.symbols('s t')
    cs = sp.symbols('c0:%d' % (k+1))
    f = sum(cs[j]*s**j*t**(k-j) for j in range(k+1))
    L = 4*s*sp.diff(f,s,2) + 2*n*sp.diff(f,s) + 4*t*sp.diff(f,t,2) + 4*sp.diff(f,t)
    eqs = sp.Poly(sp.expand(L), s, t).coeffs()
    sol = sp.linsolve(eqs, cs)
    # dimension of solution space = number of free parameters
    (vec,) = sol
    free = set().union(*[e.free_symbols for e in vec])
    return len(free)
for n in (3,4,5,6,7):
    print("n=%d  dim(K-inv harmonics of degree p), p=0..7:" % n, [harmonic_invariants(n,p) for p in range(8)])
# (2) counting constant: dim of (p,0,...,0) of SO(n+2) = harmonic polys degree p on R^{n+2}
def dimH(N,p):  # harmonic polys of degree p in N variables
    return comb(N+p-1,p) - (comb(N+p-3,p-2) if p>=2 else 0)
n=5; N=n+2
for P in (200,400,800):
    lam = P*(P+n)
    all_p = sum(dimH(N,p) for p in range(P+1))
    even  = sum(dimH(N,p) for p in range(0,P+1,2))
    print("n=5 P=%d  lam^3/N_all=%.1f  lam^3/N_even=%.1f" % (P, lam**3/all_p, lam**3/even))
# (3) Funk constant on even zonal harmonics: c_p = int_0^{2pi} C_p^{n/2}(cos th) dth / C_p^{n/2}(1)
th = sp.symbols('th')
for n in (3,5):
    lam_ = sp.Rational(n,2)
    row=[]
    for p in range(0,7):
        C = sp.gegenbauer(p, lam_, sp.cos(th))
        val = sp.integrate(sp.expand(C.rewrite(sp.cos)), (th,0,2*sp.pi)) / sp.gegenbauer(p,lam_,1)
        row.append(sp.nsimplify(val/sp.pi))
    print("n=%d  c_p/pi for p=0..6:" % n, row)
