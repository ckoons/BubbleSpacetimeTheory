"""TOY 5700 — L1 self-check (Lyra, 2026-09-06; runs AFTER the L1 file hash be29f1dc).
Short-root rank-one c-function of Γ\D_IV^5's spherical Eisenstein series, two candidates:
  naive/split:  c_s(l) = xi(2l) xi(l-1/2) / [xi(2l+1) xi(l+3/2)]
  JL/Steinberg: c_J(l) = xi(2l)/xi(2l+1) * Lam(l) / [eps(l) Lam(l+1)],
     Lam(s) = Gamma_C(s+1/2) zeta(s+1/2) zeta(s-1/2) (1 - 2^(1/2-s)),  eps(s) = 2^(1/2-s)
Checks (verdicts computed): (P1) pole order at l = 1/2: naive DOUBLE, JL SIMPLE.
(P2) |c(it)| = 1 on the unitary axis for both (Maass-Selberg), and c(l)c(-l) = 1.
(P3) JL without the eps-factor is NOT unitary (product = 2). (P4) the 2-comb: JL has poles at
l = -1/2 + 2 pi i k / ln 2, k != 0, and none at k = 0 beyond a simple one.
"""
import mpmath as mp
mp.mp.dps = 30
def xi(s): return mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)
def GC(s): return 2*(2*mp.pi)**(-s)*mp.gamma(s)
def Lam(s): return GC(s+mp.mpf(1)/2)*mp.zeta(s+mp.mpf(1)/2)*mp.zeta(s-mp.mpf(1)/2)*(1-mp.mpf(2)**(mp.mpf(1)/2-s))
def eps(s): return mp.mpf(2)**(mp.mpf(1)/2-s)
def c_naive(l): return xi(2*l)*xi(l-mp.mpf(1)/2)/(xi(2*l+1)*xi(l+mp.mpf(3)/2))
def c_JL(l, with_eps=True):
    v = xi(2*l)/xi(2*l+1)*Lam(l)/Lam(l+1)
    return v/eps(l) if with_eps else v
def pole_order(f, z0, h=mp.mpf('1e-6')):
    # order = lim  log|f(z0+2h)/f(z0+h)| / log(1/2)
    a, b = abs(f(z0+h)), abs(f(z0+2*h))
    return float(mp.log(b/a)/mp.log(mp.mpf(1)/2))
print("toy 5700: L1 self-check of the short-root c-function")
o_n = pole_order(c_naive, mp.mpf(1)/2); o_j = pole_order(c_JL, mp.mpf(1)/2)
print("  pole order at l=1/2: naive %.4f  JL %.4f" % (o_n, o_j))
p1 = abs(o_n-2) < 0.01 and abs(o_j-1) < 0.01
mods = []
for t in (3.3, 7.1, 14.13, 21.02, 30.4):
    l = mp.mpc(0, t)
    mods.append((abs(c_naive(l)), abs(c_JL(l)), abs(c_JL(l, False)), abs(c_JL(l)*c_JL(-l)), abs(c_JL(l,False)*c_JL(-l,False))))
    print("  t=%6.2f |c_naive|=%.12f |c_JL|=%.12f |c_JL no eps|=%.12f  c_JL(l)c_JL(-l)=%.12f  no-eps product=%.12f" % ((t,)+tuple(float(x) for x in mods[-1])))
p2 = all(abs(m[0]-1) < 1e-10 and abs(m[1]-1) < 1e-10 and abs(m[3]-1) < 1e-10 for m in mods)
p3 = all(abs(m[4]-2) < 1e-10 for m in mods)
comb = 2*mp.pi/mp.log(2)
orders = [pole_order(c_JL, mp.mpc(-0.5, k*comb)) for k in (1, 2, -1)]
o0 = pole_order(c_JL, mp.mpf(-0.5))
print("  2-comb spacing 2pi/ln2 = %.10f; pole orders at k=1,2,-1: %s; at k=0: %.4f" % (float(comb), ["%.4f" % o for o in orders], o0))
p4 = all(abs(o-1) < 0.01 for o in orders)
for name, ok in [("P1 naive double / JL simple pole at 1/2", p1), ("P2 unitarity on the axis (both) and c(l)c(-l)=1 (JL)", p2),
                 ("P3 JL without eps has product 2, not 1", p3), ("P4 the 2-comb: simple poles at -1/2 + 2 pi i k/ln 2", p4)]:
    print("  %s: %s" % (name, "HIT" if ok else "MISS"))
