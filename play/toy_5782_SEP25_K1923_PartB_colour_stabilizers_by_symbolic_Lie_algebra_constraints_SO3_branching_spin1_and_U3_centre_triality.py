#!/usr/bin/env python3
"""
Toy 5782 — K1923 Part B by another method: symbolic Lie-algebra constraints (Elie, 2026-09-25).
Keeper's script not opened before this ran.

Method: X in gl(3,C) written with 18 REAL symbols (X = A + iB). Each preserved structure is a
LINEAR condition on the Lie algebra; the stabilizer's real dimension = 18 - rank(conditions),
computed exactly by sympy (rationals only).
  eps (volume form)          : tr X = 0
  h   (Hermitian form, H > 0): X^dagger H + H X = 0
  q   (bilinear form, Q)     : X^T Q + Q X = 0
Input made explicit (K1923 leaves it implicit): h and q are COMPATIBLE — q(x,y) = h(conj x, y) under
the real structure of V12 (Q = H = I in one basis). The toy also runs an INCOMPATIBLE pair
(Takagi values of q w.r.t. h distinct) to show what that input carries.

Then (i) branching of SU(3)'s 3 under SO(3) = stab(eps,h,q): Casimir -> spin; (ii) U(3) centre,
the Z3 kernel of SU(3)xU(1) -> U(3), and singlet counts in 3^n (x) 3bar^m (exact Weyl-character
constant terms) vs triality n - m = 3B mod 3.
"""
import sympy as sp
from itertools import product as iprod

checks = []
def check(name, ok, can_fail=True):
    checks.append((name, bool(ok), can_fail))
    print(f"  [{'PASS' if ok else 'FAIL'}]{'' if can_fail else ' (control)'} {name}")

a = sp.symbols('a0:9', real=True); b = sp.symbols('b0:9', real=True)
X = sp.Matrix(3, 3, lambda i, j: a[3*i+j] + sp.I*b[3*i+j])
vars_ = list(a) + list(b)

def conds(M):
    """real linear equations from a complex matrix expression = 0"""
    out = []
    for e in M:
        e = sp.expand(e)
        out += [sp.re(e), sp.im(e)]
    return out

def dim_stab(*cond_lists):
    eqs = [e for cl in cond_lists for e in cl]
    if not eqs:
        return 18
    A = sp.Matrix([[sp.diff(e, v) for v in vars_] for e in eqs])
    return 18 - A.rank()

I3 = sp.eye(3)
EPS = [sp.expand(X.trace())]
Hc = lambda H: conds(X.H*H + H*X)
Qc = lambda Q: conds(X.T*Q + Q*X)
H, Q = I3, I3

table = {
    "none (gl(3,C))": dim_stab(),
    "eps": dim_stab(conds(sp.Matrix(EPS))),
    "h": dim_stab(Hc(H)),
    "eps+h": dim_stab(conds(sp.Matrix(EPS)), Hc(H)),
    "q": dim_stab(Qc(Q)),
    "q+h": dim_stab(Qc(Q), Hc(H)),
    "eps+h+q": dim_stab(conds(sp.Matrix(EPS)), Hc(H), Qc(Q)),
    "eps+q": dim_stab(conds(sp.Matrix(EPS)), Qc(Q)),
}
expect = {"none (gl(3,C))": 18, "eps": 16, "h": 9, "eps+h": 8, "q": 6, "q+h": 3, "eps+h+q": 3, "eps+q": 6}
print("Toy 5782 — stabilizer real dimensions (exact ranks)")
for k_, v in table.items():
    print(f"  {k_:16s}: {v:2d}   (expected {expect[k_]})")
check("gl(3,C) = 18 (instrument sanity)", table["none (gl(3,C))"] == 18, can_fail=False)
for k_ in ["eps", "h", "eps+h", "q", "q+h", "eps+h+q"]:
    check(f"stab({k_}) = {expect[k_]} matches K1923 Part B", table[k_] == expect[k_])
check("eps adds nothing once q is kept (o(3,C) already traceless)", table["eps+q"] == table["q"])

# compatibility input: q with distinct Takagi values relative to h = I
Qbad = sp.diag(1, 2, 3)
d_bad = dim_stab(Qc(Qbad), Hc(H))
print(f"\n  INCOMPATIBLE q (Takagi values 1,2,3 w.r.t. h): dim stab(q,h) = {d_bad}")
check("SO(3) = 3 needs q compatible with h; generic q gives a smaller stabilizer", d_bad < 3)

# explicit su(3) basis check: stab(eps,h) is traceless antihermitian
print("\n(i) Branching of SU(3)'s 3 under SO(3) = stab(eps,h,q)")
L = []
for (i, j, k) in [(1, 2, 0), (2, 0, 1), (0, 1, 2)]:
    M = sp.zeros(3); M[i, j] = 1; M[j, i] = -1   # real antisymmetric generator of rotations about axis k
    L.append(sp.I*M)                              # Hermitian: L_k = i*(E_ij - E_ji)
for Lk in L:
    ok = all(sp.simplify(e) == 0 for e in (sp.I*Lk).T*Q + Q*(sp.I*Lk))
    assert ok
C = sp.simplify(sum((Lk*Lk for Lk in L), sp.zeros(3)))
print(f"  Casimir L^2 on the triplet = {C.tolist()}")
jj = C[0, 0]
jval = sp.solve(sp.Symbol('j')*(sp.Symbol('j')+1) - jj, sp.Symbol('j'))
print(f"  j(j+1) = {jj} -> j = {[s for s in jval if s >= 0]}")
check("the 3 restricted to stab(eps,h,q) is irreducible spin-1 (L^2 = 2*I)", C == 2*I3)
check("so the triplet is NOT spin-1/2 under this SO(3) (Lyra's 2(b) can-fail line is live)", jj != sp.Rational(3, 4))
# contrast: the SU(2) that fixes a vector (isospin-type embedding) gives 2 + 1
Ls = [sp.zeros(3) for _ in range(3)]
pa = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
for n_, s in enumerate(pa):
    Ls[n_][:2, :2] = s/2
C2 = sum((m*m for m in Ls), sp.zeros(3))
print(f"  contrast, SU(2) fixing one axis: Casimir diag = {[C2[i, i] for i in range(3)]}  (2 + 1: j = 1/2, 0)")
check("control: the SU(2)xU(1) embedding does carry j=1/2 — it is NOT stab(q,h)", C2[0, 0] == sp.Rational(3, 4) and C2[2, 2] == 0, can_fail=False)

print("\n(ii) U(3) = (SU(3) x U(1))/Z3")
w = sp.exp(2*sp.pi*sp.I/3)
cen = [sp.simplify(w**k) for k in range(3)]
print(f"  centre of SU(3): w^k I, det = {[sp.simplify(c**3) for c in cen]}")
check("w^k I has det 1 for k=0,1,2 (centre = Z3)", all(sp.simplify(c**3 - 1) == 0 for c in cen))
# kernel of (g, z) -> z g: z g = I with g in SU(3) => g = z^-1 I, det g = z^-3 = 1 => z in Z3
z = sp.symbols('z')
ker = sp.solve(z**3 - 1, z)
check("kernel of SU(3)xU(1) -> U(3) has exactly 3 elements", len(ker) == 3)

# singlet counts: constant term of chi_3^n chi_3bar^m |Delta|^2 / 6 on the torus x1 x2 x3 = 1
x1, x2 = sp.symbols('x1 x2')
x3 = 1/(x1*x2)
xs = [x1, x2, x3]
chi3 = x1 + x2 + x3
chi3b = 1/x1 + 1/x2 + 1/x3
Delta2 = 1
for i in range(3):
    for j in range(3):
        if i != j:
            Delta2 *= (1 - xs[i]/xs[j])
def const_term(expr):
    e = sp.expand(expr*1)
    num, den = sp.fraction(sp.together(e))
    # den is a monomial x1^p x2^r; constant term = coefficient of den's monomial in num
    P = sp.Poly(sp.expand(num), x1, x2)
    dp = sp.Poly(den, x1, x2).monoms()[0]
    coeffs = dict(zip(P.monoms(), P.coeffs()))
    lc = sp.Poly(den, x1, x2).coeffs()[0]
    return coeffs.get(dp, 0)/lc
print("  singlets in 3^n (x) 3bar^m:  (n,m): count, triality (n-m) mod 3")
ok_tri = True; rows = []
for n_, m_ in iprod(range(0, 5), range(0, 4)):
    if n_ + m_ == 0 or n_ + m_ > 6:
        continue
    c = const_term(chi3**n_ * chi3b**m_ * Delta2)/6
    t = (n_ - m_) % 3
    rows.append((n_, m_, c, t))
    if (t != 0 and c != 0) or (t == 0 and c == 0):
        ok_tri = False
for r in rows:
    print(f"    ({r[0]},{r[1]}): {r[2]}, {r[3]}")
check("singlet exists iff triality n-m = 3B = 0 mod 3 (all n+m <= 6)", ok_tri)
check("qqq has exactly one singlet (eps) and q qbar exactly one (delta)",
      any(r[:3] == (3, 0, 1) for r in rows) and any(r[:3] == (1, 1, 1) for r in rows))

n = len(checks); k = sum(ok for _, ok, _ in checks)
cf = [c for c in checks if c[2]]; kcf = sum(ok for _, ok, _ in cf)
print(f"\nSCORE {k}/{n}  (can-fail {kcf}/{len(cf)}; {n-len(cf)} controls)")
