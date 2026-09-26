#!/usr/bin/env python3
"""
Toy 5809 — second method for Lyra's toy 5793 (write operator W_x = D(x,e)) (Elie, 2026-09-26, carried item).
Lyra's method: random complex vectors, numerical ranks, closure by SVD. THIS method: exact sympy with GENERIC symbolic x,y,
and a structural characterisation instead of a dimension count: for x ∈ V1 = span(E2,E3,E4), e = (E0+iE1)/√2,
the Jordan triple {x,y,z} = (x·ȳ)z + (z·ȳ)x − (x·z)ȳ gives D(x,e) = x ēᵀ − ē xᵀ (a complex ANTISYMMETRIC matrix),
so the generated algebra sits inside so(5,C); equality by exhibiting all 10 elementary antisymmetric matrices.
DIRECTION (written before the run): every Lyra claim holds: W† = D(e,x); [W_x,W_y] = 0; W_xW_y e = −q(x,y)ē;
W W W = 0; W_x² = 0 iff q(x,x) = 0; generated = so(5,C), compact form so(5), J = i·1 not generated.
KILL: any one of these fails exactly.
"""
import sympy as sp
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
n = 5
E = [sp.Matrix([1 if i == k else 0 for i in range(n)]) for k in range(n)]
e = (E[0] + sp.I*E[1])/sp.sqrt(2); eb = e.conjugate()
xs = sp.symbols('x2:5'); ys = sp.symbols('y2:5'); zs = sp.symbols('z0:5')
xc = sp.symbols('xc2:5')  # conj(x) as independent symbols
x = sum((c*E[k+2] for k, c in enumerate(xs)), sp.zeros(n, 1)); y = sum((c*E[k+2] for k, c in enumerate(ys)), sp.zeros(n, 1))
xbar = sum((c*E[k+2] for k, c in enumerate(xc)), sp.zeros(n, 1))
dot = lambda a, b: (a.T*b)[0]
def trip(a, bconj, c): return dot(a, bconj)*c + dot(c, bconj)*a - dot(a, c)*bconj
def Dm(a, bconj): return sp.Matrix.hstack(*[trip(a, bconj, E[k]) for k in range(n)])
Wx = Dm(x, eb); Wy = Dm(y, eb)
check("D(x,e) = x ēᵀ − ē xᵀ (antisymmetric) for generic x ∈ V1", sp.simplify(Wx - (x*eb.T - eb*x.T)) == sp.zeros(n) and sp.simplify(Wx + Wx.T) == sp.zeros(n))
Wd = Dm(e, xbar)   # D(e,x) with conj(x) = xbar
check("W_x† = D(e,x) (conjugate-transpose with x̄ symbolic)", sp.simplify(Wx.subs(dict(zip(xs, xc))).conjugate().T.subs({sp.conjugate(c): c for c in xc}) - Wd) == sp.zeros(n)
      or sp.simplify((x.subs(dict(zip(xs, xc)))*eb.T - eb*x.subs(dict(zip(xs, xc))).T).conjugate().T.subs({sp.conjugate(s): s for s in xc}) - Wd) == sp.zeros(n))
check("[W_x, W_y] = 0 identically (writes commute)", sp.simplify(Wx*Wy - Wy*Wx) == sp.zeros(n))
q = dot(x, y)
check("W_x W_y e = −q(x,y) ē identically (two writes give symmetric q)", sp.simplify(Wx*Wy*e + q*eb) == sp.zeros(n, 1))
zz = sp.symbols('w2:5'); zv = sum((c*E[k+2] for k, c in enumerate(zz)), sp.zeros(n, 1)); Wz = Dm(zv, eb)
check("W_x W_y W_z = 0 identically (no top product; ε not a product of writes)", sp.simplify(Wx*Wy*Wz) == sp.zeros(n))
W2 = sp.simplify(Wx*Wx)
check("W_x² = −q(x,x)·ē ēᵀ exactly  ⇒  W_x² = 0 iff x isotropic", sp.simplify(W2 + dot(x, x)*eb*eb.T) == sp.zeros(n))
# generated algebra: take W for x = E2,E3,E4 and their adjoints D(e, E_k)
Ws = [Dm(E[k], eb) for k in (2, 3, 4)]; Wds = [Dm(e, E[k]) for k in (2, 3, 4)]
basis = Ws + Wds
def span_rank(L): return sp.Matrix([list(m) for m in L]).rank()
cur = list(basis)
for _ in range(4):
    new = cur + [sp.simplify(a*b - b*a) for a in cur for b in cur]
    # keep an independent subset
    ind = []
    for m in new:
        if span_rank(ind + [m]) > len(ind): ind.append(m)
    cur = ind
elem = [E[i]*E[j].T - E[j]*E[i].T for i in range(n) for j in range(i+1, n)]
inside = all(sp.simplify(m + m.T) == sp.zeros(n) for m in cur)
full = span_rank(cur + elem) == 10 and span_rank(cur) == 10
check("generated complex Lie algebra = so(5,C): all antisymmetric, spans all 10 elementary E_ij − E_ji", inside and full, f"dim {len(cur)}")
check("J = i·1 (centre of K) is NOT generated (1 is not antisymmetric; rank rises when added)", span_rank(cur + [sp.I*sp.eye(n)]) == 11)
# compact real form: real span of anti-Hermitian combinations i(W+W†), (W−W†) closes to so(5) (real dim 10)
G = [sp.I*(a + b) for a, b in zip(Ws, Wds)] + [(a - b) for a, b in zip(Ws, Wds)]
def rvec(m): return [sp.re(v) for v in m] + [sp.im(v) for v in m]
curR = list(G)
for _ in range(4):
    new = curR + [sp.expand(a*b - b*a) for a in curR for b in curR]
    ind = []
    for m in new:
        if sp.Matrix([rvec(t) for t in ind + [m]]).rank() > len(ind): ind.append(m)
    curR = ind
check("compact form: real dim 10, all anti-Hermitian (so(5) of K, not su(3))",
      len(curR) == 10 and all(sp.simplify(m + m.conjugate().T) == sp.zeros(n) for m in curR), f"real dim {len(curR)}")
print(f"\nSCORE: {sum(score)}/{len(score)}")
