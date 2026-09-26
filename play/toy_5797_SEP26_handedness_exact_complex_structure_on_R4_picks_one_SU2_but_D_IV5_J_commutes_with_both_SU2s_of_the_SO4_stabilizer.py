#!/usr/bin/env python3
"""
Toy 5797 — handedness, exact (Elie, 2026-09-26, round 5 item 2). Prereg f3f09274.
K1926 Section 3 / Lyra Dictionary L3 (05-29): "SU(2)_L = the J-compatible SU(2) of the SO(4) stabilizer".
(a) R^4 fact: orientation-compatible orthogonal complex structures = unit sphere of Λ²+ = su(2)+; each commutes with su(2)-.
(b) D_IV^5: p = R^5 ⊗ R^2, J = 1 ⊗ j (the SO(2) factor of K). Does J commute with both su(2)s of so(4) ⊂ so(5)?
    Does J even preserve the SO(4) stabilizer's R^4 (= e5-perp ⊗ f1)?
(c) J-invariant real 4-planes of the form (plane ⊗ R^2): canonical orientation (even ⊗ even); which factor holds J,
    which holds the plane's own rotation; does reversing the arrow (j -> -j) move J to the other factor?
(d) generic J-invariant 4-plane (complex 2-plane in C^5): only J's own orientation exists -> J self-dual by construction.
Exact integer/rational arithmetic (sympy).
"""
import sympy as sp
import random
random.seed(5797)
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def E(n,i,j):
    M = sp.zeros(n); M[i,j] = -1; M[j,i] = 1; return M   # rotation generator e_i -> e_j
def br(A,B): return A*B - B*A
def span_dim(mats):
    if not mats: return 0
    return sp.Matrix([list(M) for M in mats]).rank()

# ---- (a) R^4 ----
e12,e13,e14,e23,e24,e34 = E(4,0,1),E(4,0,2),E(4,0,3),E(4,1,2),E(4,1,3),E(4,2,3)
Lp = [e12+e34, e13-e24, e14+e23]   # self-dual for orientation 1234 (*e12=e34, *e13=-e24, *e14=e23)
Lm = [e12-e34, e13+e24, e14-e23]
ok_split = all(br(A,B) == sp.zeros(4) for A in Lp for B in Lm)
check("(a) so(4) = Λ+ ⊕ Λ- with [Λ+,Λ-] = 0 (two commuting su(2)s)", ok_split and span_dim(Lp+Lm) == 6)
a,b,c = sp.symbols('a b c', real=True)
Jg = a*Lp[0]+b*Lp[1]+c*Lp[2]
check("(a) every element of Λ+ squares to -(a²+b²+c²)·1: its unit sphere = orthogonal complex structures",
      sp.expand(Jg*Jg + (a**2+b**2+c**2)*sp.eye(4)) == sp.zeros(4))
J0 = Lp[0]
cent = [M for M in (e12,e13,e14,e23,e24,e34)]
xs = sp.symbols('x0:6', real=True)
Xg = sum((x*M for x,M in zip(xs,cent)), sp.zeros(4))
sol = sp.Matrix(list(br(J0,Xg))).jacobian(xs).nullspace()
check("(a) centralizer of J0=e12+e34 in so(4) = su(2)- ⊕ R·J0 (dim 4 = u(2)); J0 commutes with ALL of Λ-, no other Λ+ element",
      len(sol) == 4 and all(br(J0,M) == sp.zeros(4) for M in Lm) and all(br(J0,M) != sp.zeros(4) for M in Lp[1:]))
u = sp.Matrix([1,0,0,0]); w = sp.Matrix([0,0,1,0])
Jc = -J0  # matrices act as x -> M x ; take the complex structure as the matrix itself
for Jt, lab in ((J0,'Λ+'),(Lm[0],'Λ-')):
    d = sp.Matrix.hstack(u, Jt*u, w, Jt*w).det()
    print(f"   complex orientation (u,Ju,w,Jw) of the {lab} structure: det = {d}")
dp = sp.Matrix.hstack(u, J0*u, w, J0*w).det(); dm = sp.Matrix.hstack(u, Lm[0]*u, w, Lm[0]*w).det()
check("(a) a Λ+ structure induces the given orientation, a Λ- structure the opposite (orientation-compatible = Λ+)",
      sp.sign(dp) != sp.sign(dm))

# ---- (b) D_IV^5 : p = R^5 ⊗ R^2, index (a,s) -> 2a+s ----
j = sp.Matrix([[0,-1],[1,0]])
J = sp.kronecker_product(sp.eye(5), j)
so5 = [sp.kronecker_product(E(5,i,k), sp.eye(2)) for i in range(5) for k in range(i+1,5)]
check("(b) J = 1⊗j is a complex structure on p (J² = -1)", J*J == -sp.eye(10))
check("(b) J commutes with ALL of so(5)⊗1 (10/10 generators)", all(br(J,M) == sp.zeros(10) for M in so5))
# so(4) = stabilizer of e5 : generators on indices 0..3 ; its two su(2)s
def lift(M4):
    M5 = sp.zeros(5); M5[:4,:4] = M4; return sp.kronecker_product(M5, sp.eye(2))
Lp10 = [lift(M) for M in Lp]; Lm10 = [lift(M) for M in Lm]
both = all(br(J,M) == sp.zeros(10) for M in Lp10+Lm10)
check("(b) KILL FIRES: J commutes with BOTH su(2)+ and su(2)- of the SO(4) stabilizer — J picks no hand there", both)
# does J preserve the SO(4) stabilizer's R^4 = span(e1..e4 ⊗ f1)?
R4 = sp.Matrix.hstack(*[sp.Matrix([1 if k==2*a_ else 0 for k in range(10)]) for a_ in range(4)])
JR4 = J*R4
inter = sp.Matrix.hstack(R4, JR4).rank()
check("(b) J does not preserve that R^4: J(R^4⊗f1) ∩ (R^4⊗f1) = 0 (R^4 is totally real, rank 8 of the pair)", inter == 8, f"rank {inter}")

# ---- (c) J-invariant plane⊗R^2 : basis x1=e1f1, x2=e1f2, x3=e2f1, x4=e2f2 ----
def tensor_basis(P, F):   # P: 2 plane vectors in R^2 coords, F: 2 vectors in R^2
    return [sp.kronecker_product(p_, f_) for p_ in P for f_ in F]
std = [sp.Matrix([1,0]), sp.Matrix([0,1])]
B0 = sp.Matrix.hstack(*tensor_basis(std, std))
flips_ok = True
for P in ([std[0], std[1]], [std[1], std[0]], [std[0], -std[1]]):
    for F in ([std[0], std[1]], [std[1], std[0]]):
        Bn = sp.Matrix.hstack(*tensor_basis(P, F))
        if sp.sign(Bn.det()) != sp.sign(B0.det()): flips_ok = False
check("(c) plane⊗R² has an orientation independent of either factor's orientation (flips leave it unchanged)", flips_ok)
Bswap = sp.Matrix.hstack(*[sp.kronecker_product(p_, f_) for f_ in std for p_ in std])  # R²-major ordering
check("(c) ...but it DOES depend on the factor ORDER (plane⊗R² vs R²⊗plane flips it): which factor is called Λ+ is a convention",
      sp.sign(Bswap.det()) != sp.sign(B0.det()))
Jt = sp.kronecker_product(sp.eye(2), j)      # arrow
Rt = sp.kronecker_product(j, sp.eye(2))      # the plane's own rotation (from so(5))
# express in the e_ij basis of R^4 with x-ordering above: compare to Lp/Lm
def coords(M): return sp.Matrix([M[1,0],M[2,0],M[3,0],M[2,1],M[3,1],M[3,2]])  # (e12,e13,e14,e23,e24,e34) components
inLp = lambda M: sp.Matrix.hstack(*[coords(X) for X in Lp]).rank() == sp.Matrix.hstack(*[coords(X) for X in Lp]+[coords(M)]).rank()
inLm = lambda M: sp.Matrix.hstack(*[coords(X) for X in Lm]).rank() == sp.Matrix.hstack(*[coords(X) for X in Lm]+[coords(M)]).rank()
print(f"   arrow J=1⊗j: in Λ+ {inLp(Jt)}, in Λ- {inLm(Jt)};  plane rotation j⊗1: in Λ+ {inLp(Rt)}, in Λ- {inLm(Rt)}")
check("(c) on plane⊗R² (canonical orientation) the arrow J and the plane's rotation sit in OPPOSITE su(2) factors",
      inLp(Jt) != inLp(Rt) and inLm(Jt) != inLm(Rt))
check("(c) reversing the arrow (j -> -j) keeps J in the SAME factor: the arrow's sign does not choose the hand",
      inLp(-Jt) == inLp(Jt))

# ---- (d) generic J-invariant 4-plane: complex 2-plane in C^5 ----
def rv(): return sp.Matrix([sp.Rational(random.randint(-4,4)) for _ in range(10)])
u1, u2 = rv(), rv()
Bg = sp.Matrix.hstack(u1, J*u1, u2, J*u2)
check("(d) generic complex 2-plane in C^5: J-invariant, real rank 4; its only intrinsic orientation is J's own (J self-dual by construction — tautology, not a hand)",
      Bg.rank() == 4 and sp.Matrix.hstack(Bg, J*Bg).rank() == 4)

print("\nREADING: an orthogonal complex structure on an R^4 does pick one su(2) (a). But D_IV^5's J is central in K: it commutes")
print("with all of SO(5), so with BOTH SU(2)s of the SO(4) stabilizer (b), and does not even preserve that R^4 (totally real).")
print("On the J-invariant planes plane⊗R^2 the arrow and the spatial rotation sit in opposite factors, canonically, and the")
print("arrow's SIGN does not move J between factors (c). The lead 'the arrow picks the hand' dies as worded; what survives is a")
print("structural split (complex structure in one SU(2), the plane's rotation in the other) with the L/R label still a convention.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
