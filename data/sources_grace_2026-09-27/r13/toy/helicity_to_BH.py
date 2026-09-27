#!/usr/bin/env python3
"""R13: map Mack (d; j1, j2) lowest K-type to a Bai-Hunziker highest weight lambda of su(2,2)
and evaluate BH15 Prop. 3.2 (as restated in arXiv:2409.16555 Prop 3.2, VT-1).
Coordinates: compact Cartan of u(2,2), lambda = (a1,a2 | b1,b2); p+ roots e_i - f_j;
beta = e1 - f2 (highest noncompact root; simply laced, |root|^2 = 2 so coroot = root).
Energy element E = -(1/2)(1,1|-1,-1): the unique element of the centre of k (mod centre of g)
acting by +1 on p- (energy raising by one unit, like P_mu). Lowest K-type: E = d,
(a1-a2) = 2 j1, (b1-b2) = 2 j2.  Constants (Table 1, VT-2): r = 2, c = 1, (rho, beta^vee) = 3.
"""
from fractions import Fraction as F
r, c, rho_beta = 2, 1, 3
z = lambda k: rho_beta - k * c
def lam(d, j1, j2, t=F(0)):
    # choose a1+a2 = -d + t, b1+b2 = d + t (t = central U(1) twist, drops out of su(2,2))
    s_a, s_b = -d + t, d + t
    a1, a2 = (s_a + 2 * j1) / 2, (s_a - 2 * j1) / 2
    b1, b2 = (s_b + 2 * j2) / 2, (s_b - 2 * j2) / 2
    return a1, a2, b1, b2
def E(l): a1, a2, b1, b2 = l; return -(a1 + a2 - b1 - b2) / 2
def pair_beta(l): a1, a2, b1, b2 = l; return a1 - b2
def BH(l):
    k = -pair_beta(l) / c
    if k > r - 1: return k, r * z(r - 1), "O_2 = p+ (dim 4)"
    kk = int(k); return k, kk * z(kk - 1) if kk else 0, f"O_{kk} closure (dim {kk*(4-kk)}), label [2^{kk},1^{4-2*kk}]"
rows = []
print("massless tower (Mack class 5: d = j1+j2+1, j1*j2 = 0):")
for twoh in range(0, 13):
    h = F(twoh, 2)
    for (j1, j2) in [(h, F(0)), (F(0), h)] if h else [(F(0), F(0))]:
        d = j1 + j2 + 1
        l = lam(d, j1, j2)
        assert E(l) == d
        k, gk, av = BH(l)
        print(f"  h={'+' if j1 else ('-' if j2 else ' ')}{h}: d={d} (lambda,beta^v)={pair_beta(l)} k={k} GKdim={gk} AV={av}")
        rows.append((k, gk))
print("controls:")
for (d, j1, j2, lab) in [(F(2), F(0), F(0), "scalar d=2 (Hardy-space point)"), (F(3), F(1,2), F(1,2), "d=j1+j2+2 boundary"),
                          (F(4), F(0), F(0), "scalar d=4 (hol. discrete series, d>3)"), (F(0), F(0), F(0), "trivial")]:
    l = lam(d, j1, j2); k, gk, av = BH(l)
    print(f"  {lab}: (lambda,beta^v)={pair_beta(l)} k={k} GKdim={gk} AV={av}")
ok = all(k == 1 and gk == 3 for k, gk in rows)
print("SCORE: every massless helicity 0..6 has k=1, GKdim=3, AV = closure of O_1:", "PASS" if ok else "FAIL")
