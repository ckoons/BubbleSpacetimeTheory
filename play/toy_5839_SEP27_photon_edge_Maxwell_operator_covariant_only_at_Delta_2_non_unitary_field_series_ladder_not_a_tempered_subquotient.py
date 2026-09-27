#!/usr/bin/env python3
"""
Toy 5839 — round 16 Lane A, the photon edge (Elie, 2026-09-27). Prereg 175b984e (which states the correction to 5837 (B) first).
(1) Where the photon lives: the conformally covariant first-order operators on p-forms in 4D — solve for the unique Δ.
    Maxwell (div and d on 2-forms), with controls □ (scalar) and ∂·J (vector). Euclidean ℝ⁴ (algebraic covariance is signature-blind).
    Conformal action on a rank-p tensor of weight Δ: K_μ = (x²∂_μ − 2x_μ x·∂ − 2Δ x_μ) − 2 x^ν Σ_{μν}, Σ_{μν} acting on every index as
    (Σ_{μν}V)_a = δ_{μa}V_ν − δ_{νa}V_μ. The convention is CHECKED (not assumed) by [K_μ,K_ν] = 0 and [K_μ,P_ν] = 2(δ_{μν}D + M_{μν})
    with M = orbital + the SAME Σ.
(3) Ørsted–Zhang's actual family: spherical minimal-parabolic HC parameters (iν1, iν2, 0) vs the helicity-1 ladder's (0, 2, 1).
(2) is a logical step (Knapp, pin owed) using 5830/5832's computed non-temperedness — printed, not scored.
"""
import sympy as sp, itertools, numpy as np
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
X = sp.symbols('x0:4'); d = 4
Dl = sp.Symbol('Delta')
def idxs(p): return list(itertools.product(range(d), repeat=p))
def eul(f): return sum(x*sp.diff(f, x) for x in X)
x2 = sum(x*x for x in X)
def sigma(mu, nu, F, p):   # (Σ_{μν} F)_{a1..ap} = Σ_slots [δ_{μ a_k} F_{..ν..} − δ_{ν a_k} F_{..μ..}]
    out = {}
    for I in idxs(p):
        s = 0
        for k in range(p):
            if I[k] == mu: s += F[I[:k] + (nu,) + I[k+1:]]
            if I[k] == nu: s -= F[I[:k] + (mu,) + I[k+1:]]
        out[I] = s
    return out
def K(mu, F, p, D):
    S = {I: 0 for I in idxs(p)}
    for nu in range(d):
        sg = sigma(mu, nu, F, p)
        for I in S: S[I] += X[nu]*sg[I]
    return {I: sp.expand(x2*sp.diff(F[I], X[mu]) - 2*X[mu]*eul(F[I]) - 2*D*X[mu]*F[I] - 2*S[I]) for I in F}
def P(mu, F): return {I: sp.diff(F[I], X[mu]) for I in F}
def Dil(F, D): return {I: sp.expand(eul(F[I]) + D*F[I]) for I in F}
def M(mu, nu, F, p):
    sg = sigma(mu, nu, F, p)
    return {I: sp.expand(X[mu]*sp.diff(F[I], X[nu]) - X[nu]*sp.diff(F[I], X[mu]) + sg[I]) for I in F}
def rand_field(p, antisym, deg=2, seed=0):
    rng = np.random.default_rng(seed); mons = [sp.Integer(1)] + list(X) + [a*b for a, b in itertools.combinations_with_replacement(X, 2)]
    F = {}
    for I in idxs(p):
        if antisym and len(set(I)) < p: F[I] = sp.Integer(0); continue
        if antisym and list(I) != sorted(I): continue
        F[I] = sum(int(rng.integers(-3, 4))*m for m in mons[:(1 + 4 + 10) if deg == 2 else 5])
    if antisym:
        for I in idxs(p):
            if len(set(I)) == p and list(I) != sorted(I):
                perm = sorted(range(p), key=lambda k: I[k]); sgn = sp.combinatorics.Permutation(perm).signature()
                F[I] = sgn*F[tuple(sorted(I))]
    return F
def diffF(A, B): return all(sp.expand(A[I] - B[I]) == 0 for I in A)
# convention check on vectors (p = 1) at generic Δ
V = rand_field(1, False, seed=1)
okKK = all(diffF(K(m, K(n, V, 1, Dl), 1, Dl), K(n, K(m, V, 1, Dl), 1, Dl)) for m in range(d) for n in range(m + 1, d))
okKP = all(diffF({I: K(m, P(n, V), 1, Dl)[I] - P(n, K(m, V, 1, Dl))[I] for I in V},
                 {I: sp.expand(2*((1 if m == n else 0)*Dil(V, Dl)[I] + M(m, n, V, 1)[I])) for I in V}) for m in range(d) for n in range(d))
check("convention CHECKED on vector fields: [K_μ,K_ν] = 0 and [K_μ,P_ν] = 2(δ_{μν}D + M_{μν}) with M = orbital + the same Σ", okKK and okKP)
def solve_Delta(src, tgt_of, p_src, p_tgt, op, F):
    """all Δ with op∘K^(Δ) = K^(Δ+shift)∘op on F"""
    eqs = []
    for mu in range(d):
        lhs = op(K(mu, F, p_src, Dl)); rhs = K(mu, op(F), p_tgt, Dl + tgt_of)
        for I in lhs:
            e = sp.expand(lhs[I] - rhs[I])
            if e != 0: eqs += sp.Poly(e, *X).coeffs()
    if not eqs: return 'all'
    sol = sp.solve(eqs, Dl, dict=True)   # run 1 compared sympy's bare-dict return {Delta: v} with [v] (format only; values were right)
    return sorted(s_[Dl] for s_ in sol) if sol else []
# controls
f0 = {(): sp.expand(sum(X)**2*X[0] + X[1]*X[2]**2 + 3*X[3])}
box = lambda F: {(): sum(sp.diff(F[()], x, 2) for x in X)}
s_box = solve_Delta(None, 2, 0, 0, box, f0)
check("CONTROL □: covariant scalar(Δ) → scalar(Δ+2) ONLY at Δ = 1 = (d−2)/2 (the massless scalar)", s_box == [1], str(s_box))
Vc = rand_field(1, False, seed=3)
divV = lambda F: {(): sum(sp.diff(F[(a,)], X[a]) for a in range(d))}
s_J = solve_Delta(None, 1, 1, 0, divV, Vc)
check("CONTROL ∂·J: covariant vector(Δ) → scalar(Δ+1) ONLY at Δ = 3 = d − 1 (the conserved current)", s_J == [3], str(s_J))
Fm = rand_field(2, True, seed=5)
divF = lambda F: {(b,): sum(sp.diff(F[(a, b)], X[a]) for a in range(d)) for b in range(d)}
s_div = solve_Delta(None, 1, 2, 1, divF, Fm)
dF = lambda F: {(a, b, c): sp.expand(sp.diff(F[(b, c)], X[a]) + sp.diff(F[(c, a)], X[b]) + sp.diff(F[(a, b)], X[c])) for (a, b, c) in idxs(3)}
s_d = solve_Delta(None, 1, 2, 3, dF, Fm)
print(f"   solved Δ: □ {s_box}; ∂·J {s_J}; Maxwell div {s_div}; Maxwell d {s_d}")
check("MAXWELL: div F (2-form(Δ) → vector(Δ+1)) is covariant ONLY at Δ = 2", s_div == [2], str(s_div))
check("MAXWELL: dF (2-form(Δ) → 3-form(Δ+1)) is covariant ONLY at Δ = 2 — both Maxwell equations single out Δ = 2", s_d == [2], str(s_d))
# (3) Ørsted–Zhang's family: spherical minimal-parabolic HC (iν1, iν2, 0) vs the ladder's (0, 2, 1) under W(D3)
def W_equal(u, v):
    for pp in itertools.permutations(range(3)):
        for sg in itertools.product((1, -1), repeat=3):
            if np.prod(sg) != 1: continue
            if all(abs(sg[i]*u[pp[i]] - v[i]) < 1e-12 for i in range(3)): return True
    return False
grid = np.linspace(-4, 4, 161)
hit = any(W_equal((1j*a, 1j*b, 0), (0, 2, 1)) for a in grid for b in grid)
check("(3) Ørsted–Zhang's record family (spherical minimal-parabolic, HC (iν1, iν2, 0)) never has the helicity-1 ladder's infinitesimal "
      "character (0, 2, 1) for real ν (grid incl. ν = 0): its real entries 2, 1 cannot be matched", not hit)
print("\n(2) [logical step, not scored; Knapp pin OWED] Unitarily induced from tempered ⇒ finite sum of TEMPERED irreducibles. The helicity-1")
print("    ladder is NOT tempered (5830/5832, computed) ⇒ it is not a subquotient of ANY unitary-axis representation (ν = 0 included).")
print("READING: the photon lives as the kernel of the Maxwell operator, covariant only at Δ = 2, on the NON-unitary degenerate (field) series;")
print("that series is not in the record continuum, whose family (3) cannot even share the photon's infinitesimal character. Keeper's kill")
print("resolves to 'not a subquotient' ⇒ no covariant photon coupling of H² through the records, of any kind (F·O included).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
