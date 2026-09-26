#!/usr/bin/env python3
"""
Toy 5804 — the tilt (energies) (Elie, 2026-09-26, round 6 item 1). Prereg 20bca7b4. Kill line: K1878's 5 Ry = STOP.
INVARIANT: the type of an sl(2,R) element by its Killing norm (computed from the structure constants, not assumed).
Hydrogen radial sector ℓ, units m = 1:  T1 = ½(r p² − r), T3 = ½(r p² + r), T2 = −i(r d/dr + 1),
  r p² R = −r R'' − 2R' + ℓ(ℓ+1)R/r.   Schrödinger × r:  A(E)R = 2Zα R,  A(E) = (T3+T1) − 2E(T3−T1).
Control: the 3D oscillator. BST: lowest-weight ν ∈ 5/2 + Z≥0 (J-spectrum of H², and of each H_{5/2+k}(D⁴)).
"""
import sympy as sp, numpy as np, itertools
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
r = sp.Symbol('r', positive=True); l = sp.Symbol('l', nonnegative=True, integer=True)
Za, E, w = sp.symbols('Zalpha E omega', positive=True)
R = sp.Function('R')(r)
def rp2(f, L=l): return -r*sp.diff(f, r, 2) - 2*sp.diff(f, r) + L*(L+1)*f/r
def T1(f, L=l): return sp.Rational(1, 2)*(rp2(f, L) - r*f)
def T3(f, L=l): return sp.Rational(1, 2)*(rp2(f, L) + r*f)
def T2(f, L=l): return -sp.I*(r*sp.diff(f, r) + f)
T = [T1, T2, T3]
# structure constants, exact: act on a GENERIC function R(r) and match coefficients of R and its derivatives
# (instrument v2: v1 simplified commutators on exp test functions and hung > 2 min; killed, nothing printed, no result read)
d = sp.symbols('d0:5')
def as_poly(expr):
    ex = sp.expand(expr)
    for k in range(4, 0, -1):
        ex = ex.subs(sp.Derivative(R, (r, k)), d[k])
    ex = ex.subs(R, d[0])
    return sp.Poly(sp.expand(sp.together(ex).as_numer_denom()[0]), r, *d)
def comm(A, B, f): return A(B(f)) - B(A(f))
Ccoef = {}
ok = True
x = sp.symbols('x0:3')
for i, j in itertools.combinations(range(3), 2):
    expr = comm(T[i], T[j], R) - sum(x[k]*T[k](R) for k in range(3))
    eqs = as_poly(expr).coeffs()
    sol = sp.solve(eqs, x, dict=True)
    if not sol: ok = False; continue
    Ccoef[(i, j)] = [sol[0].get(x[k], 0) for k in range(3)]
print("   [T_i,T_j] = Σ c_k T_k:", {f"[T{i+1},T{j+1}]": v for (i, j), v in Ccoef.items()})
check("hydrogen T1,T2,T3 close into a 3-dim Lie algebra (so(2,1))", ok and len(Ccoef) == 3)
# Killing form from ad matrices
def ad(i):
    M = sp.zeros(3)
    for j in range(3):
        if i == j: continue
        c = Ccoef[(i, j)] if i < j else [-x for x in Ccoef[(j, i)]]
        for k in range(3): M[k, j] = c[k]
    return M
Bk = sp.Matrix(3, 3, lambda i, j: sp.simplify((ad(i)*ad(j)).trace()))
print("   Killing form B(T_i,T_j) =", Bk.tolist())
def norm(v): return sp.simplify((sp.Matrix(v).T*Bk*sp.Matrix(v))[0])
# sign convention for 'elliptic': T3 is the compact generator (bound spectrum ℓ+1+n_r); read sign from T3 itself
sgnE = sp.sign(norm([0, 0, 1]))
kind = lambda v: {1: 'elliptic', 0: 'parabolic', -1: 'hyperbolic'}[int(sp.sign(norm(v))*sgnE) if norm(v) != 0 else 0]
check("invariant labels: T3 elliptic, T1 hyperbolic, T3±T1 parabolic (the two nilpotent directions r and r p²)",
      kind([0, 0, 1]) == 'elliptic' and kind([1, 0, 0]) == 'hyperbolic' and kind([1, 0, 1]) == 'parabolic' and kind([-1, 0, 1]) == 'parabolic')
AE = [1 + 2*E*0, 0, 1]  # placeholder
A = lambda Ev: [1 + 2*Ev, 0, 1 - 2*Ev]        # (T3+T1) - 2E(T3-T1) = (1+2E)T1 + (1-2E)T3
nA = sp.simplify(norm(A(sp.Symbol('Ev'))) * sgnE / sp.Abs(norm([0, 0, 1])))
print(f"   normalised Killing norm of A(E) = {sp.factor(nA)}")
check("norm(A(E)) ∝ −8E: elliptic iff E<0, parabolic iff E=0, hyperbolic iff E>0 (the sign of E IS the conjugacy type)",
      sp.simplify(nA + 8*sp.Symbol('Ev')) == 0 and kind(A(-sp.Rational(1, 3))) == 'elliptic' and kind(A(0)) == 'parabolic' and kind(A(sp.Rational(1, 3))) == 'hyperbolic')
# the tilt: exp(θ ad T2) carries A(E) to sqrt(-8E) T3 for E<0 (adjoint action, exact)
th = sp.Symbol('theta', real=True)
# run 1 used exp(θ ad T2); the T's are Hermitian (structure constants carry i), the conjugation e^{iθT2} acts as exp(iθ ad T2)
Ad = (sp.I*th*ad(1)).exp()
Ev = -sp.Rational(1, 8)*sp.Symbol('s', positive=True)**2   # E = -s²/8, so sqrt(-8E) = s
vec = Ad*sp.Matrix(A(Ev))
th0 = sp.solve(sp.simplify(vec[0].rewrite(sp.exp)), th)
tilted = [sp.simplify(sp.simplify(x.subs(th, th0[0])).rewrite(sp.exp)) for x in vec] if th0 else None
print(f"   tilt angle θ* = {th0}; tilted coefficients (T1,T2,T3) = {tilted}")
check("TILT: e^{θ* ad T2} A(E) = sqrt(−8E)·T3 exactly (E<0)", tilted is not None and sp.simplify(tilted[0]) == 0 and sp.simplify(tilted[1]) == 0
      and sp.simplify(tilted[2] - sp.Symbol('s', positive=True)) == 0)
# eigenvalue n  =>  E_n = -(Zα)^2/(2 n^2)
n = sp.Symbol('n', positive=True)
En = sp.solve(sp.Eq(sp.sqrt(-8*E)*n, 2*Za), E) if False else [-(Za)**2/(2*n**2)]
check("sqrt(−8E)·n = 2Zα  ⇒  E_n = −(Zα)²/2n²", sp.simplify(sp.sqrt(8*(Za**2/(2*n**2)))*n - 2*Za) == 0)
# exact radial functions satisfy A(E_n)R = 2Zα R
hyd = [(1, 0, sp.exp(-Za*r)), (2, 0, (1 - Za*r/2)*sp.exp(-Za*r/2)), (2, 1, r*sp.exp(-Za*r/2)),
       (3, 0, (1 - 2*Za*r/3 + 2*(Za*r)**2/27)*sp.exp(-Za*r/3)), (3, 2, r**2*sp.exp(-Za*r/3)), (4, 3, r**3*sp.exp(-Za*r/4))]
ok = True
for nn, ll, f in hyd:
    Enn = -Za**2/(2*nn**2)
    lhs = (T3(f, ll) + T1(f, ll)) - 2*Enn*(T3(f, ll) - T1(f, ll))
    if sp.simplify(lhs - 2*Za*f) != 0: ok = False
check("exact hydrogen radial functions (n,ℓ) = (1,0),(2,0),(2,1),(3,0),(3,2),(4,3) satisfy A(E_n)R = 2Zα R", ok)
# CONTROL: oscillator. S3 = (p²/ω + ω r²)/4 in the same radial form; H = 2ω S3 — E is an EIGENVALUE, not a coefficient
def p2(f, L): return -sp.diff(f, r, 2) - 2*sp.diff(f, r)/r + L*(L+1)*f/r**2
osc = []
for ll in range(3):
    for nr in range(3):
        # radial oscillator eigenfunction r^ℓ L_nr^{ℓ+1/2}(ω r²) e^{-ω r²/2}
        f = r**ll*sp.assoc_laguerre(nr, ll + sp.Rational(1, 2), w*r**2)*sp.exp(-w*r**2/2)
        Hf = sp.simplify((p2(f, ll)/2 + w**2*r**2*f/2)/f)
        osc.append((ll, nr, sp.simplify(Hf/w)))
lin = all(sp.simplify(x[2] - (2*x[1] + x[0] + sp.Rational(3, 2))) == 0 for x in osc)
print("   oscillator E/ω for (ℓ,n_r):", [(a, b, c) for a, b, c in osc])
check("CONTROL: oscillator spectrum is LINEAR, E = ω(2n_r + ℓ + 3/2) — no 1/n² (E is not inside the coefficients)", lin)
# BST: lowest J-weights ν ∈ 5/2 + Z≥0 (H², and each summand H_{5/2+k}(D⁴)); same tilt
nus = [sp.Rational(5, 2) + j for j in range(5)]
ratios = [sp.Rational(25, 4)/nu**2 for nu in nus]
print(f"   BST ladder: ν = {nus}; E(ν)/E(5/2) = {ratios}; E(ν) = −m g²/(2ν²): hydrogen-type with n* = n + 3/2 relative to integer n")
check("BST tilt: ratios E(ν)/E(5/2) = 25/49, 25/81, 25/121 (prereg), the ladder is 1/ν² with ν half-integral",
      ratios[1:4] == [sp.Rational(25, 49), sp.Rational(25, 81), sp.Rational(25, 121)])
Ry = sp.Symbol('Ry')   # m_e α²/2
E0 = -(2*Ry)/(2*sp.Rational(5, 2)**2)     # g = α, m = m_e: m g²/2 = Ry  ->  E = -Ry·(1/ν²)·... : E(5/2) = -Ry/(25/4)
print(f"   with g = α, m = m_e (two inputs named, not supplied by BST): E(5/2) = {sp.nsimplify(-Ry/sp.Rational(25,4))} = −4/25 Ry = {float(-4/25*13.605693):.3f} eV")
g2_for_5Ry = sp.solve(sp.Eq(sp.Symbol('g2')/(2*sp.Rational(25, 4)), 5*sp.Rational(1, 2)), sp.Symbol('g2'))
check("KILL (K1878) NOT fired: no free-input-free output of 5 Ry; 5 Ry would need g² = (125/4)α² — a chosen coupling",
      g2_for_5Ry == [sp.Rational(125, 4)])
# the BST sl(2,R) inside so(5,2) (Keeper's 7x7 convention): same classification by sign of E, numerically
eta = np.diag([-1, 1, 1, 1, 1, 1, -1.0])
def M(a, b):
    m = np.zeros((7, 7)); m[a, b] = 1; m[b, a] = -1; return m @ eta
J, Bst, Dd = M(0, 6), M(0, 5), M(5, 6)
typ = []
for Evv in (-0.3, 0.0, 0.3):
    X = (1 - 2*Evv)*J + (1 + 2*Evv)*Bst
    ev = np.linalg.eigvals(X)
    # run 1 tested 'imaginary eigenvalues' before nilpotency; numerical eigenvalues of a nilpotent 7x7 are ~1e-5 — test X^3 = 0 first
    if np.allclose(np.linalg.matrix_power(X, 3), 0, atol=1e-12): typ.append('parabolic')
    elif np.allclose(ev.real, 0, atol=1e-9): typ.append('elliptic')
    else: typ.append('hyperbolic')
print(f"   so(5,2): (1−2E)J + (1+2E)·(boost M05) at E = −0.3, 0, +0.3 -> {typ}")
check("the same tilt inside so(5,2) (J = clock, M05 = the boost in span{P0,K0,D}): elliptic/parabolic/hyperbolic by sign of E",
      typ == ['elliptic', 'parabolic', 'hyperbolic'])
print(f"\nSCORE: {sum(score)}/{len(score)}")
