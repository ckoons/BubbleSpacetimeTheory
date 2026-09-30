#!/usr/bin/env python3
"""
Toy 5853 — the spinor Wallach set of SO(5,2), computed from the Shapovalov form (Elie, 2026-09-30, round 24). Prereg 6dbbadc4.
g = so(5,2): 7x7 matrices preserving η = diag(1,1,1,1,1,−1,−1); k = so(5)+so(2) (Z = L67); p± by ad Z = ±i.
Lowest-weight module: lowest K-type τ = (so(5) rep) ⊗ (Z acts by a scalar set by λ), p⁻τ = 0; X ∈ g_R acts anti-Hermitian ⇒ X* = −conj(X).
Gram matrices G_k(λ) at levels k = 1,2,3 by moving p⁻ through products of p⁺ (explicit commutators). CONTROL: scalar τ ⇒ {0} ∪ [3/2, ∞).
"""
import numpy as np, itertools
n = 7; eta = np.diag([1., 1, 1, 1, 1, -1, -1])
def L(a, b):
    m = np.zeros((n, n), complex); m[a, b] = 1; m[b, a] = -1; return m @ eta
kso5 = [(a, b) for a in range(5) for b in range(a + 1, 5)]
Kbasis = [L(a, b) for a, b in kso5] + [L(5, 6)]          # 10 so(5) + Z
Z = L(5, 6)
cand = [L(a, 5) + 1j*L(a, 6) for a in range(5)]
def ad(A, B): return A @ B - B @ A
sgn = None
for s in (1, -1):
    X = [L(a, 5) + s*1j*L(a, 6) for a in range(5)]
    if all(np.allclose(ad(Z, x), 1j*x) for x in X): sgn = s; P = X
assert sgn is not None
Y = [-np.conj(x) for x in P]                             # X_a* = −conj(X_a) ∈ p⁻
def coords(M, basis):
    A = np.array([b.ravel() for b in basis]).T
    c, res, *_ = np.linalg.lstsq(A, M.ravel(), rcond=None)
    assert np.allclose(A @ c, M.ravel(), atol=1e-10), "not in span"
    return c
# brackets as structure constants
YX = [[coords(ad(Y[i], P[j]), Kbasis) for j in range(5)] for i in range(5)]      # [Y_i, X_j] ∈ k
KX = [[coords(ad(K, P[j]), P) for j in range(5)] for K in Kbasis]                 # [K, X_j] ∈ p⁺
def taurep(kind, lam, zsign):
    if kind == 'scalar':
        mats = [np.zeros((1, 1), complex) for _ in kso5]; dim = 1
    else:
        s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.diag([1, -1]).astype(complex); I = np.eye(2)
        g = [np.kron(s1, I), np.kron(s2, I), np.kron(s3, s1), np.kron(s3, s2), np.kron(s3, s3)]   # Cl(5), γγ + γγ = 2δ
        mats = [0.25*(g[a] @ g[b] - g[b] @ g[a]) for a, b in kso5]; dim = 4
    return mats + [zsign*1j*lam*np.eye(dim)], dim
# check the spin rep has the same brackets as the matrices (on so(5))
def bracket_check():
    rep, _ = taurep('spinor', 0, 1)
    for i, j in itertools.product(range(10), range(10)):
        c = coords(ad(Kbasis[i], Kbasis[j]), Kbasis)
        lhs = rep[i] @ rep[j] - rep[j] @ rep[i]; rhs = sum(c[k]*rep[k] for k in range(10))
        if not np.allclose(lhs, rhs): return False
    return True
SPIN_OK = bracket_check()
def gram(level, kind, lam, zsign):
    rep, dim = taurep(kind, lam, zsign)
    Kact = rep
    idx = list(itertools.combinations_with_replacement(range(5), level))
    def apply_Y(i, state):   # state: dict tuple(sorted) -> vec(dim)
        out = {}
        def add(key, vec):
            out[key] = out.get(key, 0) + vec
        for key, w in state.items():
            for pos in range(len(key)):
                # Y X_1…X_k w = Σ_pos X_1…X_{pos−1} [Y, X_pos] X_{pos+1}…X_k w : the k-element acts ONLY on the factors to its RIGHT
                # (run 1 let it act on the left factors too — double counting; caught by the scalar control)
                left, right = key[:pos], key[pos + 1:]
                kc = YX[i][key[pos]]
                for m, cm in enumerate(kc):
                    if abs(cm) < 1e-14: continue
                    for q in range(len(right)):
                        for r, cr in enumerate(KX[m][right[q]]):
                            if abs(cr) < 1e-14: continue
                            nk = tuple(sorted(left + right[:q] + (r,) + right[q + 1:])); add(nk, cm*cr*w)
                    add(tuple(sorted(left + right)), cm*(Kact[m] @ w))
        return out
    basis = [(key, a) for key in idx for a in range(dim)]
    G = np.zeros((len(basis), len(basis)), complex)
    for J, (kJ, b) in enumerate(basis):
        st = {kJ: np.eye(dim)[b].astype(complex)}
        for I_, (kI, a) in enumerate(basis):
            s = dict(st)
            for i in reversed(kI):          # (X_{i1}…X_{ik})* = Y_{ik}…Y_{i1}: apply Y_{i1} first? ⟨X_I v, X_J w⟩ = ⟨v, Y_{ik}..Y_{i1} X_J w⟩
                pass
            s = dict(st)
            for i in kI: s = apply_Y(i, s)
            G[I_, J] = s.get((), np.zeros(dim))[a] if () in s else 0
    return G
def min_eig(level, kind, lam, zsign):
    G = gram(level, kind, lam, zsign); G = (G + G.conj().T)/2
    return np.linalg.eigvalsh(G).min()
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
check("setup: p⁺ = eigenvectors of ad Z with eigenvalue +i; p⁺ abelian; the Cl(5) spin rep has the matrices' so(5) brackets",
      all(np.allclose(ad(P[a], P[b]), 0) for a in range(5) for b in range(5)) and SPIN_OK)
# fix the Z sign by the scalar control at level 1 (norm ∝ +λ)
zs = 1 if min_eig(1, 'scalar', 1.0, 1) > 0 else -1
print(f"   Z sign fixed by the scalar control: {zs}")
def uset(kind, levels, grid):
    ok = []
    for lam in grid:
        ok.append(all(min_eig(k, kind, lam, zs) > -1e-9 for k in levels))
    return np.array(ok)
grid = np.round(np.arange(-1.0, 6.01, 0.25), 4)
sc = uset('scalar', (1, 2), grid)
unit_sc = grid[sc]
print(f"   scalar, levels 1–2: unitary at λ ∈ {list(unit_sc[:6])} … (grid 0.25)")
check("CONTROL scalar (levels 1–2): unitary exactly at λ = 0 and λ ≥ 3/2 on the grid (the known Wallach set {0} ∪ [3/2, ∞))",
      set(unit_sc.tolist()) == {0.0} | {x for x in grid.tolist() if x >= 1.5})
sp = uset('spinor', (1, 2), grid)
unit_sp = grid[sp]
print(f"   spinor, levels 1–2: unitary at λ ∈ {list(unit_sp)}")
# refine the spinor endpoint and scan for isolated unitary points (reduction points) with a fine grid
fine = np.round(np.arange(-0.5, 5.001, 0.05), 4)
spf = uset('spinor', (1, 2), fine)
isol = [fine[i] for i in range(len(fine)) if spf[i] and (i == 0 or not spf[i-1]) and (i + 1 < len(fine) and not spf[i + 1])]
endpoint = min(fine[i] for i in range(len(fine)) if all(spf[i:]))
print(f"   spinor (fine grid 0.05, levels 1–2): continuum from λ = {endpoint}; isolated unitary points {isol}")
# level-3 confirmation at a few points
l3 = {lam: min_eig(3, 'spinor', lam, zs) > -1e-9 for lam in (endpoint, 3.5, 4.5)}
print(f"   spinor level-3 PSD at {l3}")
check("spinor unitarity set (levels ≤ 2, confirmed at level 3): the continuum endpoint is λ = 2 (the Di singleton, (n−1)/2)",
      abs(endpoint - 2.0) < 1e-9 and all(l3.values()))
# reduction points (zeros of det G_k) for the spinor family, levels 1–2: sign changes of the smallest eigenvalue of each level
def roots(level):
    xs = np.arange(-1.0, 6.0, 0.02); f = [min_eig(level, 'spinor', x, zs) for x in xs]; rs = []
    for i in range(len(xs) - 1):
        if f[i] == 0 or f[i]*f[i + 1] < 0:
            a, b = xs[i], xs[i + 1]
            for _ in range(40):
                m = (a + b)/2
                if min_eig(level, 'spinor', a, zs)*min_eig(level, 'spinor', m, zs) <= 0: b = m
                else: a = m
            rs.append(round((a + b)/2, 6))
    return rs
r1, r2 = roots(1), roots(2)
print(f"   spinor sign changes of min eigenvalue: level 1 at {r1}; level 2 at {r2}")
# Harish-Chandra holomorphic discrete series threshold (B3; e1 = so(2), e2,e3 = so(5)); calibrate on the scalar value 4
rho = np.array([2.5, 1.5, 0.5]); noncpt = [np.array(v) for v in ([1, 1, 0], [1, -1, 0], [1, 0, 1], [1, 0, -1], [1, 0, 0])]
def hc_threshold(mu):
    # discrete series iff <Λ+ρ, β> < 0 ∀ β ∈ Δn⁺ with Λ = (−λ, μ2, μ3): the binding β gives λ > max_β(ρ·β + μ·β_compact)
    return max(float(rho @ b + mu[0]*b[1] + mu[1]*b[2]) for b in noncpt)
th_s, th_sp = hc_threshold((0, 0)), hc_threshold((0.5, 0.5))
check("CONTROL: the HC holomorphic-discrete-series threshold for the scalar is λ > 4 = p − 1", abs(th_s - 4) < 1e-12)
print(f"   HC holomorphic discrete series threshold: scalar {th_s}, spinor {th_sp}")
nat = {"spinor unitarity endpoint (Di)": endpoint, "spinor HC discrete-series threshold": th_sp}
nat.update({f"reduction pt (level 1) {x}": x for x in r1}); nat.update({f"reduction pt (level 2) {x}": x for x in r2})
hit = [k for k, v in nat.items() if abs(v - 3.5) < 1e-6]
print(f"   natural points of the spinor family: {nat}")
print(f"   points equal to 7/2: {hit}")
print(f"   [reported, not scored] THE QUESTION: is 7/2 a natural point of the spinor family? {'YES: ' + str(hit) if hit else 'NO'} (prereg said NO)")
print(f"\nSCORE: {sum(score)}/{len(score)}")
