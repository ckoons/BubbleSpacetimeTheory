# Cal: Nyman–Beurling Gram entries WITHOUT Vasyunin's closed form.
# In L²(0,∞) with ρ_a(x) = {1/(a x)}:  <ρ_k, ρ_m> = ∫_0^∞ {1/(kx)}{1/(mx)} dx = ∫_0^∞ {t/k}{t/m} dt/t²   (t = 1/x).
# f(t) = {t/k}{t/m} is periodic with period P = lcm(k,m); Σ_{n≥0} 1/(u+nP)² = ψ'(u/P)/P² (trigamma), so
#   <ρ_k,ρ_m> = ∫_0^P f(u) ψ'(u/P) du / P²,  with f piecewise quadratic between the breakpoints (multiples of k and m).
from mpmath import mp, mpf, quad, polygamma, log, pi, euler, floor
from math import lcm
mp.dps = 30
def gram(k, m):
    P = int(lcm(k, m))
    bps = sorted(set([0] + [i*k for i in range(1, P//k+1)] + [j*m for j in range(1, P//m+1)]))
    tot = mpf(0)
    for a, b in zip(bps[:-1], bps[1:]):
        g = lambda u: (u/k - floor(u/k))*(u/m - floor(u/m))*polygamma(1, u/P)
        tot += quad(g, [a, b])
    return tot / P**2
print("||rho_1||^2 =", gram(1,1), "  memory: log(2π) − γ =", log(2*pi) - euler)
print("<rho_1,rho_2> =", gram(1,2))
print("<rho_2,rho_3> =", gram(2,3))
print("<rho_1,rho_3> =", gram(1,3))
print("conjectured lim d_N^2 log N = 2 + γ − log(4π) =", 2 + euler - log(4*pi), " (Báez-Duarte–Balazard–Landreau–Saias 2000; the board's 0.0462 is RIGHT — Cal's remembered 0.0231 was wrong, corrected by this line)")
