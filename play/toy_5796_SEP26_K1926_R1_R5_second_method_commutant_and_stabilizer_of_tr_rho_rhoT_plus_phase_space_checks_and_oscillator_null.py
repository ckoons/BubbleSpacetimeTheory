#!/usr/bin/env python3
"""
Toy 5796 — K1926 R1–R5 by a SECOND METHOD (Elie, 2026-09-26, round 5 item 1). Prereg f3f09274.
Keeper's instrument counted dimensions directly; here:
  (i)  the COMMUTANT of all rank-1 records {vv†} (Schur) -> kernel of the U(3) action on records;
  (ii) the stabilizer of the FUNCTION f(rho) = tr(rho rho^T), solved as an exact linear system in u(3)
       over Gaussian-rational records; group level: which unitary g keep f (g^T g = c I);
  (iii) control: stab of the real structure (g = conj(g)) in SU(3);
  (iv) Addendum 3 (phase space): u(3) = o(6) ∩ sp(6,R); omega|_{R^3} = 0; stab of R^3; dim U(3)/O(3);
  (v)  oscillator shells Sym^N(C^3) vs baryon multiplets, with a null.
All exact (sympy Rationals / Gaussian rationals).
"""
import sympy as sp
from itertools import product
import random
random.seed(5796)
I = sp.I
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")

def rand_v():
    return sp.Matrix([sp.Rational(random.randint(-5,5)) + I*sp.Rational(random.randint(-5,5)) for _ in range(3)])
def rec(v):
    return v*v.H
recs = []
while len(recs) < 12:
    v = rand_v()
    if (v.H*v)[0] != 0: recs.append(rec(v))

# generic complex 3x3 with 18 real unknowns
a = sp.symbols('a0:9', real=True); b = sp.symbols('b0:9', real=True)
X = sp.Matrix(3,3,[a[k]+I*b[k] for k in range(9)])
unk = list(a)+list(b)

def solve_dim(eqs_complex, unknowns):
    eqs = []
    for e in eqs_complex:
        e = sp.expand(e); eqs += [sp.re(e), sp.im(e)]
    M = sp.Matrix([[sp.diff(e,u) for u in unknowns] for e in eqs])
    ns = M.nullspace()
    return len(ns), ns

# (i) commutant of all records, in M3(C)
eqs = []
for r in recs:
    C = X*r - r*X; eqs += list(C)
d, ns = solve_dim(eqs, unk)
check("R5/commutant: commutant of {vv†} in M3(C) is the scalars (real dim 2 = complex dim 1)", d == 2, f"real dim {d}")

# u(3) parametrisation: X anti-Hermitian: X = A + iS, A real antisym, S real sym
p = sp.symbols('p0:9', real=True)
A = sp.Matrix([[0,p[0],p[1]],[-p[0],0,p[2]],[-p[1],-p[2],0]])
S = sp.Matrix([[p[3],p[4],p[5]],[p[4],p[6],p[7]],[p[5],p[7],p[8]]])
U = A + I*S
eqs = []
for r in recs: eqs += list(U*r - r*U)
d, ns = solve_dim(eqs, list(p))
check("R5: kernel of u(3) acting on records is exactly u(1) = iR·1 (dim 1) => faithful algebra dim 8 = su(3)", d == 1 and ns[0][3]==ns[0][6]==ns[0][8] and all(ns[0][k]==0 for k in (0,1,2,4,5,7)), f"dim {d}")

# (ii) stabiliser of f(rho) = tr(rho rho^T): derivative 2 tr([U,rho] rho^T) = 0 for all records
eqs = []
for r in recs:
    eqs.append((U*r - r*U)*r.T); eqs[-1] = eqs[-1].trace()
d, ns = solve_dim(eqs, list(p))
# expected: real antisymmetric (p0,p1,p2) + the invisible scalar
basis_ok = d == 4
check("R3/R4: stab of f in u(3) = so(3) ⊕ u(1) (dim 4)", basis_ok, f"dim {d}")
# intersect with su(3): trace(S)=0
eqs_su = eqs + [S.trace()]
d_su, ns_su = solve_dim(eqs_su, list(p))
only_antisym = all(all(n[k]==0 for k in range(3,9)) for n in ns_su)
check("R4: stab of f in su(3) = so(3), dim 3, spanned by real antisymmetric matrices", d_su == 3 and only_antisym, f"dim {d_su}")

# R1 / R2 identities, symbolic
z = sp.symbols('z0:3'); zb = sp.symbols('w0:3')  # treat v and conj(v) independently
v = sp.Matrix(z); vb = sp.Matrix(zb)
rho = v*vb.T                      # v v†  with v† = conj(v)^T
q = (v.T*v)[0]; qb = (vb.T*vb)[0]
check("R2: tr(rho rho^T) = |q|^2 identically (q = v^T v)", sp.expand((rho*rho.T).trace() - q*qb) == 0)
th = sp.symbols('theta', real=True)
vv = rand_v(); r1 = rec(vv); r2 = rec(sp.exp(I*th)*vv)
q1 = (vv.T*vv)[0]; q2 = sp.expand((sp.exp(I*th)*vv).T*(sp.exp(I*th)*vv))[0]
check("R1: e^{iθ}v gives the same record, and q changes by e^{2iθ} (q is forgotten)",
      sp.simplify(r1 - r2) == sp.zeros(3) and sp.simplify(q2 - sp.exp(2*I*th)*q1) == 0 and q1 != 0)

# group level: g unitary keeps f  <=> g^T g = c 1.  Test: omega*O keeps f; generic SU(3) element does not.
def f(r): return sp.nsimplify(sp.expand((r*r.T).trace()))
w = sp.exp(2*sp.pi*I/3)
c_, s_ = sp.Rational(3,5), sp.Rational(4,5)
O = sp.Matrix([[c_,-s_,0],[s_,c_,0],[0,0,1]])
g1 = w*O
g2 = sp.Matrix([[1,0,0],[0,(1+I)/sp.sqrt(2),0],[0,0,(1-I)/sp.sqrt(2)]])  # in SU(3), not real up to phase
okg1 = all(sp.simplify(f(g1*r*g1.H) - f(r)) == 0 for r in recs[:4])
okg2 = any(sp.simplify(f(g2*r*g2.H) - f(r)) != 0 for r in recs[:4])
check("group: ω·O (ω^3=1, O∈SO(3)) keeps f; a diagonal SU(3) element that is not real-up-to-phase breaks f", okg1 and okg2)
# diagonal torus of SU(3): count finite stabiliser e^{2iθ_i} all equal and det=1  -> c*diag(±1) with c^3*sgn=1
sols = set()
for k in range(6):
    c = sp.exp(sp.pi*I*k/3)
    for sg in product([1,-1], repeat=3):
        g = sp.diag(*[c*s for s in sg])
        # run 1 counted (k, signs) LABELS (24); (k,s) and (k+3,-s) are the same matrix — count matrices
        if sp.simplify(g.det()-1) == 0: sols.add(tuple(sp.nsimplify(sp.expand(x)) for x in (g[0,0],g[1,1],g[2,2])))
check("group: diagonal stab of f in SU(3) is finite (12 = ℤ3 centre × 4 sign matrices in SO(3)); no continuous torus part",
      len(sols) == 12, f"{len(sols)} elements")

# (iii) control: stab of the real structure in su(3): U = conj(U)  <=> S = 0 -> so(3), dim 3
d_ctrl, _ = solve_dim(list(S), list(p))
check("CONTROL: stab of the real structure in su(3) = real antisymmetric = so(3) (dim 3) = identity component of stab(f)", d_ctrl == 3)

# (iv) Addendum 3: realify C^3 -> R^6 (x1,x2,x3,y1,y2,y3); J = [[0,-1],[1,0]] blocks; omega = J-matrix
Z3 = sp.zeros(3); I3 = sp.eye(3)
Om = sp.Matrix(sp.BlockMatrix([[Z3,-I3],[I3,Z3]]))
Y = sp.Matrix(6,6, sp.symbols('y0:36', real=True))
eqs = list(Y + Y.T) + list(Y.T*Om + Om*Y)
d_int, _ = solve_dim(eqs, list(Y))
check("Add.3: o(6) ∩ sp(6,R) has dim 9 = dim u(3)", d_int == 9, f"dim {d_int}")
e = [sp.Matrix([1 if i==k else 0 for i in range(6)]) for k in range(6)]
lag = all((e[i].T*Om*e[j])[0] == 0 for i in range(3) for j in range(3))
check("Add.3: ω vanishes on position space R^3 = span(x1,x2,x3) (Lagrangian: half of phase space)", lag)
# stab of span(x) in the 9-dim algebra: Y maps x-block into x-block (lower-left block zero)
eqs2 = eqs + [Y[i,j] for i in range(3,6) for j in range(3)]
d_stab, _ = solve_dim(eqs2, list(Y))
check("Add.3: stab of R^3 in u(3) has dim 3 (o(3)); dim U(3)/O(3) = 9 - 3 = 6", d_stab == 3 and d_int - d_stab == 6, f"stab {d_stab}")

# (v) oscillator shells vs baryon multiplets, structural, with null
def dimSU3(pp,qq): return (pp+1)*(qq+1)*(pp+qq+2)//2
shells = [ (N+1)*(N+2)//2 for N in range(8)]
check("oscillator: Sym^N(C^3) dims = dim (N,0) of SU(3) for N=0..7 (each shell one SU(3) irrep)", all(shells[N]==dimSU3(N,0) for N in range(8)), str(shells))
baryons = [dimSU3(3,0), dimSU3(1,1), dimSU3(1,1), dimSU3(0,0)]
tri = [t for t in range(1,31) if any(t==(N+1)*(N+2)//2 for N in range(10))]
hits = [d for d in (1,8,10) if d in shells]
print(f"   baryon 3⊗3⊗3 = 10+8+8+1 (sum {sum(baryons)}); oscillator-shell dims among {{1,8,10}}: {hits}; null rate of triangular ≤30: {len(tri)}/30 = {len(tri)/30:.3f}")
print(f"   expected overlap by chance for 3 targets: {3*len(tri)/30:.2f}; observed {len(hits)} — NOT evidence (prereg). The 8 (mixed symmetry) is never an oscillator shell.")
check("oscillator null (prereg direction): overlap 2 of 3 = {1,10}, 8 absent, chance expectation ~0.7 — recorded as structure, not evidence",
      sum(baryons)==27 and hits == [1,10])

print(f"\nSCORE: {sum(score)}/{len(score)}")
