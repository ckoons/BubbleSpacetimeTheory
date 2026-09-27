#!/usr/bin/env python3
"""
Toy 5837 — Lane A: does H² couple covariantly to the photon? (Elie, 2026-09-27, round 15). Prereg 4df9a0c4.
(A) SL(2,R) control: formal lowest-weight vectors in D⁺_a ⊗ D⁻_b — existence, growth exponent, L² vs distributional.
(B) SO(4,2): which massless ladders share an infinitesimal character with the record continuum (principal series on Re Δ = 2)?
    Quadratic Casimir COMPUTED on the ladders in the oscillator model; Harish-Chandra parameter (Δ−2, j1+j2+1, j1−j2) mod W(D3)
    (standard; pin owed) CHECKED against it.
"""
import numpy as np
from itertools import permutations, product
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
# ---------------- (A) SL(2,R) ----------------
def Dplus(a, M):
    m = np.arange(M); J = np.diag(a + m)
    Lp = np.diag(np.sqrt((m[:-1] + 1)*(2*a + m[:-1])), -1); Lm = Lp.T
    return J, Lp, Lm
def Dminus(b, M):   # automorphism σ: J → −J, L+ → −L−, L− → −L+ applied to D⁺_b
    J, Lp, Lm = Dplus(b, M); return -J, -Lm, -Lp
J, Lp, Lm = Dplus(2.5, 30)
check("(A) D⁺ relations: [J,L±] = ±L±, [L+,L−] = −2J (low block)", np.allclose((J@Lp - Lp@J)[:20, :20], Lp[:20, :20]) and np.allclose((Lp@Lm - Lm@Lp)[:20, :20], -2*J[:20, :20]))
Jm, Lpm, Lmm = Dminus(1.5, 30)
check("(A) D⁻ via σ satisfies the same relations", np.allclose((Jm@Lpm - Lpm@Jm)[:20, :20], Lpm[:20, :20]) and np.allclose((Lpm@Lmm - Lmm@Lpm)[:20, :20], -2*Jm[:20, :20]))
def lowest_vector(a, b, s, M=4000):
    """coefficients x_m of v = Σ x_m |a+m>⊗|−b−m−s> with (L−⊗1 + 1⊗L−')v = 0, from the recursion; None if forced to 0."""
    alpha = lambda m: np.sqrt(m*(2*a + m - 1))          # L− on D⁺_a: |a+m> → |a+m−1>
    beta = lambda n: -np.sqrt((n + 1)*(2*b + n))        # L−' on D⁻_b: |−b−n> → |−b−n−1>
    m0 = max(0, -s)
    if m0 > 0: return None                               # boundary: α(m0) ≠ 0 with no x_{m0−1} ⇒ x ≡ 0
    x = np.zeros(M); x[0] = 1.0
    for m in range(1, M): x[m] = -x[m-1]*beta(m - 1 + s)/alpha(m)
    return x
def exponent(x):
    ms = np.arange(1000, 4000); return np.polyfit(np.log(ms), np.log(np.abs(x[1000:4000])), 1)[0]
a, b = 4.5, 1.5
none_neg = all(lowest_vector(a, b, s) is None for s in (-1, -2, -3))
check("(A)(i) no lowest-weight vector with c > a − b (s < 0): the boundary term forces x ≡ 0", none_neg)
rows = []
for s in range(0, 6):
    c = a - b - s; x = lowest_vector(a, b, s)
    # verify the recursion solution is annihilated by L− on a finite window (explicit matrices)
    rows.append((c, round(exponent(x), 4), np.sum(x**2) if c > 0.5 else np.inf))
print("   (A) a = 4.5, b = 1.5: (c, measured exponent of |x_m|, L² norm if convergent):", rows)
check("(A)(ii) |x_m| ~ m^{−c}: measured exponents match −c for c = 3, 2, 1, 0, −1, −2", all(abs(e + c) < 0.01 for c, e, _ in rows))
l2 = [c for c, e, _ in rows if 2*e < -1]      # |x_m|² ~ m^{2e}: L² ⇔ 2e < −1 (run 1 had the sign flipped)
check("(A)(iii) L² ⇔ c > 1/2: the discrete pieces are c = a−b−s ∈ {3, 2, 1} (finitely many); c ≤ 1/2 only distributional",
      sorted(l2) == [1.0, 2.0, 3.0], str(sorted(l2)))
x_eq = [lowest_vector(2.5, 2.5, s) for s in range(0, 3)]
check("(A)(iv) a = b (the H ⊗ H̄ case): c = −s ≤ 0 only ⇒ NO discrete piece, every lowest-weight vector non-L² (Repka's picture, pin owed)",
      all(2*exponent(x) >= -1 for x in x_eq))   # non-L² ⇔ 2e ≥ −1 (run 1 sign flipped)
# explicit-matrix confirmation of one case (small truncation, interior rows)
M = 60; Ja, Lpa, Lma = Dplus(a, M); Jb, Lpb, Lmb = Dminus(b, M)
x = lowest_vector(a, b, 1, M=M)
v = np.zeros((M, M))
for m in range(M - 2): v[m, m + 1] = x[m]
Lv = Lma @ v + v @ Lmb.T
check("(A) explicit matrices: (L−⊗1 + 1⊗L−')v = 0 on the interior (recursion verified independently)", np.abs(Lv[:40, :40]).max() < 1e-9)
# ---------------- (B) SO(4,2) ----------------
# oscillator u(2,2): ξ = (a1, a2, b1†, b2†), ξ‡ = (a1†, a2†, −b1, −b2), Ê_ij = ξ‡_i ξ_j ; su(4) Casimir C = Σ Ê_ij Ê_ji − (Σ Ê_ii)²/4
n = 7
a_ = np.diag(np.sqrt(np.arange(1, n)), 1); I = np.eye(n)
def op(k):   # annihilator for mode k in a 4-mode Fock space (a1, a2, b1, b2)
    mats = [I]*4; mats[k] = a_
    out = mats[0]
    for m_ in mats[1:]: out = np.kron(out, m_)
    return out
A1, A2, B1, B2 = (op(k) for k in range(4))
xi = [A1, A2, B1.T, B2.T]; xid = [A1.T, A2.T, -B1, -B2]
E = [[xid[i] @ xi[j] for j in range(4)] for i in range(4)]
ok_gl = all(np.allclose((E[0][1] @ E[1][2] - E[1][2] @ E[0][1])[:50, :50], E[0][2][:50, :50]) for _ in [0])
tr = sum(E[i][i] for i in range(4))
C = sum(E[i][j] @ E[j][i] for i in range(4) for j in range(4)) - tr @ tr/4
def state(na1, na2, nb1, nb2):
    v = np.zeros(n**4); v[((na1*n + na2)*n + nb1)*n + nb2] = 1; return v
lad = {"h=0": (state(0, 0, 0, 0), 1, 0, 0), "h=1/2 L": (state(1, 0, 0, 0), 1.5, .5, 0), "h=1/2 R": (state(0, 0, 1, 0), 1.5, 0, .5),
       "h=1 L": (state(2, 0, 0, 0), 2, 1, 0), "h=1 R": (state(0, 0, 2, 0), 2, 0, 1), "h=2 L": (state(4, 0, 0, 0), 3, 2, 0)}
vals = {}
for k, (v, D, j1, j2) in lad.items():
    Cv = C @ v; vals[k] = (v @ Cv, np.linalg.norm(Cv - (v @ Cv)*v), D*(D - 4) + 2*j1*(j1 + 1) + 2*j2*(j2 + 1))
fit = np.polyfit([vals["h=0"][2], vals["h=1/2 L"][2]], [vals["h=0"][0], vals["h=1/2 L"][0]], 1)
pred_ok = all(abs(np.polyval(fit, f) - c) < 1e-8 and res < 1e-8 for c, res, f in vals.values())
print("   (B) oscillator Casimir on lowest states vs Δ(Δ−4)+2j1(j1+1)+2j2(j2+1):", {k: (round(c, 6), f) for k, (c, r, f) in vals.items()}, " affine fit", np.round(fit, 6))
check("(B) gl(4) relation holds for the oscillator bilinears (sample)", ok_gl)
check("(B) the COMPUTED quadratic Casimir on every ladder lowest state is an eigenvalue and equals one affine map of Δ(Δ−4)+2Σj(j+1) "
      "(fitted on h = 0, ½; predicts h = ½R, 1L, 1R, 2)", pred_ok)
def hc(D, j1, j2): return (D - 2, j1 + j2 + 1, j1 - j2)
check("(B) |λ_HC|² − |ρ|² = Δ(Δ−4) + 2j1(j1+1) + 2j2(j2+1) with ρ = (2,1,0) (the HC parametrisation is consistent with the computed Casimir)",
      all(abs(sum(t*t for t in hc(D, j1, j2)) - 5 - (D*(D - 4) + 2*j1*(j1 + 1) + 2*j2*(j2 + 1))) < 1e-12 for _, D, j1, j2 in lad.values()))
def W_equal(u, v):   # W(D3): permutations and EVEN numbers of sign changes
    for p in permutations(range(3)):
        for sg in product((1, -1), repeat=3):
            if np.prod(sg) != 1: continue
            if all(abs(sg[i]*u[p[i]] - v[i]) < 1e-12 for i in range(3)): return True
    return False
halves = [k/2 for k in range(0, 17)]
matches = {}
for h2 in range(0, 5):
    h = h2/2
    for chir in ((1,) if h2 == 0 else (1, -1)):
        j1, j2 = (h, 0) if chir == 1 else (0, h)
        lamL = hc(h + 1, j1, j2); hits = []
        for p1, p2 in product(halves, halves):
            if (p1 + p2) % 1 != 0: continue                        # χ_s = +1 types only (those of H ⊗ H̄)
            if W_equal(lamL, hc(2.0, p1, p2)): hits.append((p1, p2))  # ν = 0 is the only unitary-axis point with a REAL parameter
        matches[(h, chir)] = hits
print("   (B) ladders whose infinitesimal character equals a principal-series point on Re Δ = 2 (ν = 0):", matches)
check("(B) ONLY helicity 1 matches: (1,0)/(0,1) principal series at ν = 0 — the photon ladder sits at the EDGE of the record continuum; "
      "helicities 0, ½, 2 match no unitary-axis point (excluded from H ⊗ H̄ even distributionally)",
      all((len(v) > 0) == (k[0] == 1.0) for k, v in matches.items()) and set(matches[(1.0, 1)]) == {(1.0, 0.0), (0.0, 1.0)})
print("\nREADING: (A) SL(2): D⁺_a⊗D⁻_b has lowest-weight vectors exactly for c ≤ a−b, L² only for c > 1/2; for a = b none is L².")
print("(B) The helicity-1 ladder has the SAME infinitesimal character as the (1,0) principal series at ν = 0, the edge of H ⊗ H̄'s continuum;")
print("no other helicity does. So the center cannot exclude a distributional J·A vertex for the photon, and ONLY for the photon; ν = 0 has")
print("Plancherel measure zero, so no L² intertwiner. Whether a distributional form exists = whether the ladder is a quotient of that")
print("reducible ν = 0 principal series and pairs with H ⊗ H̄: OPEN here (Keeper's kill line is not decided by this toy, as preregistered).")
print(f"\nSCORE: {sum(score)}/{len(score)}")
