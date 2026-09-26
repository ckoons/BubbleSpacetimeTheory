#!/usr/bin/env python3
"""Cal Section 989 instrument (2026-09-26, written 10:44 EDT, hashed before running).

PART A. K1926 R4: "SU(3) on records iff the record forgets V1's real structure."
Position or coordinate?

KILL LINE (written first): R4 is a MENU, not a dichotomy, if
  (a) U(1).SO(3) (the geometry's stabilizer on V1, K1925) has a polynomial invariant on C^3
      beyond |v|^2 and |q|^2 = |v^T v|^2 through bidegree (3,3); or
  (b) su(3) = so(3) + p with p REDUCIBLE under so(3), so that a subalgebra lies strictly between.
Direction: I predict neither. Then the geometry allows exactly two record groups, and the choice
between them is one bit. Whether the bit is forced is a separate question.

PREDICTIONS (written before running):
  QA1  invariant counts in bidegree (k,k), k = 1,2,3:  U(1).SO(3): 1, 2, 2;   U(3): 1, 1, 1.
  QA2  p is irreducible (the so(3) Casimir has one eigenvalue on p, l = 2, multiplicity 5).
  QA3  the centre Z3 (omega I) and the U(1) phase act trivially on records rho = v v^dag/|v|^2.
  QA4  tr(rho rho^T) = tr(rho rho_bar) is the overlap of v's record with the record of its conjugate v_bar.
  QA5  invariants in 3x3 : SO(3) 1, SU(3) 0.   3x3x3 : SO(3) 1, SU(3) 1.   3x3bar : 1, 1.
       => keeping the real structure allows a two-triplet singlet (a "diquark hadron"; B mod 2);
          forgetting it allows only qqq and q qbar singlets (B mod 3, register A12).
  CONTROL  so(3) on 3x3 has exactly the delta invariant (count 1); su(3) acts on records faithfully (dim 8).

PART B. A2 (|V_ud|^2 = 19/20, |V_us/V_ud| = 1/sqrt19): fired or at threshold?
Inputs pinned from Grace's retained sources (data/sources_grace_2026-09-25/):
  vv26.txt (PDG 2026 ch.67): 67.4 Vud(0+) 0.97367(32), Delta_V part (13);  67.8 neutron 0.97413(42), Delta_R part (13);
     67.7 neutron (PDG-average inputs) 0.97441(88);  67.15 |Vus fK|/|Vud fpi| = 0.27679(28)BR(20)corr;
     Table 67.1 |Vus| f+(0) = 0.21656(35);  67.18 Vus = 0.22431(85), S = 2.5.
  pdg2026.txt (ch.12): f+(0) = 0.9698(17).
  flag.txt Eq.76/77: fK/fpi 1.1934(19) [2+1+1], 1.1916(34) [2+1].
  neutron/2501.17916.txt Eq.29: Vud 0.97393(41), Delta_R part (13).
KILL LINE (written first): A2 is FIRED on a route only if that route's value is > 3 sigma from A2 AND
the route is not itself > 3 sigma from another route measuring the same quantity (a prediction is not
killed by one of two mutually inconsistent measurements). Otherwise: at threshold (>= 3 sigma on the
best-determined consistent combination) or live.
PREDICTIONS:
  QB1  fK/fpi predicted 1.2065(15); vs FLAG 2+1+1 at +5.4 sigma.
  QB2  semileptonic ratio Vus(Kl3)/Vud(0+) within 0.5 sigma of 1/sqrt19.
  QB3  leptonic (FLAG) vs semileptonic ratio: the SM's own split, 3 to 4 sigma.
  QB4  PDG's S = 2.5 average Vus vs 1/sqrt20: within 1 sigma.
  QB5  |V_ud| face: superallowed + neutron (67.8), Delta_R-correlated, combined: A2 ABOVE the data by 3.0 to 3.6 sigma.
"""
import itertools
import numpy as np

np.set_printoptions(precision=6, suppress=True)
score = []

# ---------- PART A ----------
def so3_basis():
    L = []
    for (i, j) in [(1, 2), (2, 0), (0, 1)]:
        m = np.zeros((3, 3)); m[i, j] = -1; m[j, i] = 1; L.append(m.astype(complex))
    return L

def su3_basis():
    B = []
    for i in range(3):
        for j in range(i + 1, 3):
            m = np.zeros((3, 3), complex); m[i, j] = 1; m[j, i] = -1; B.append(m)
            m = np.zeros((3, 3), complex); m[i, j] = 1j; m[j, i] = 1j; B.append(m)
    B.append(np.diag([1j, -1j, 0])); B.append(np.diag([1j, 1j, -2j]))
    return B

def u1():
    return [1j * np.eye(3)]

def sym_basis(k, n=3):
    return list(itertools.combinations_with_replacement(range(n), k))

def rep_on_sym(X, k):
    """Action of gl(3) element X on Sym^k(C^3), monomial basis (derivation)."""
    basis = sym_basis(k); idx = {b: i for i, b in enumerate(basis)}
    M = np.zeros((len(basis), len(basis)), complex)
    for c, b in enumerate(basis):
        for pos in range(k):
            for new in range(3):
                coef = X[new, b[pos]]
                if coef == 0: continue
                nb = list(b); nb[pos] = new; nb = tuple(sorted(nb))
                M[idx[nb], c] += coef
    return M

def count_invariant_hermitian_forms(gens, k):
    """Invariant polynomials of bidegree (k,k) in (v, vbar) <-> invariant Hermitian-type
    sesquilinear forms on Sym^k: solve A^dag H + H A = 0 for all generators (anti-Hermitian A)."""
    mats = [rep_on_sym(X, k) for X in gens]
    d = mats[0].shape[0]
    rows = []
    for A in mats:
        # vec(A^H H + H A) = (I kron A^H + A^T kron I) vec(H), column-major vec
        rows.append(np.kron(np.eye(d), A.conj().T) + np.kron(A.T, np.eye(d)))
    Mbig = np.vstack(rows)
    s = np.linalg.svd(Mbig, compute_uv=False)
    return int(np.sum(s < 1e-9 * max(1, s[0]))) + (d * d - len(s) if d * d > len(s) else 0)

qa1 = {}
for k in (1, 2, 3):
    qa1[k] = (count_invariant_hermitian_forms(so3_basis() + u1(), k),
              count_invariant_hermitian_forms(su3_basis() + u1(), k))
print("QA1 invariant (k,k) counts  [U(1).SO(3), U(3)]:", qa1)
ok = qa1 == {1: (1, 1), 2: (2, 1), 3: (2, 1)}
score.append(("QA1", ok))

# QA2: p = i*(real symmetric traceless) inside su(3); so(3) Casimir on p
p_basis = []
for i in range(3):
    for j in range(i + 1, 3):
        m = np.zeros((3, 3), complex); m[i, j] = 1j; m[j, i] = 1j; p_basis.append(m)
p_basis += [np.diag([1j, -1j, 0]), np.diag([1j, 1j, -2j]) / np.sqrt(3)]
P = np.array([m.flatten() for m in p_basis]).T
def ad_on_p(X):
    cols = []
    for m in p_basis:
        c = X @ m - m @ X
        coef, *_ = np.linalg.lstsq(P, c.flatten(), rcond=None)
        assert np.allclose(P @ coef, c.flatten())
        cols.append(coef)
    return np.array(cols).T
C = sum(ad_on_p(X) @ ad_on_p(X) for X in so3_basis())
ev = np.round(np.linalg.eigvals(C).real, 8)
print("QA2 so(3) Casimir on p eigenvalues:", ev)
ok = np.allclose(ev, -6.0)   # -l(l+1), l = 2
score.append(("QA2", ok))

# QA3, QA4 on random states
rng = np.random.default_rng(989)
okA3 = okA4 = True
w = np.exp(2j * np.pi / 3)
for _ in range(200):
    v = rng.normal(size=3) + 1j * rng.normal(size=3)
    rho = np.outer(v, v.conj()) / np.vdot(v, v).real
    okA3 &= np.allclose(np.outer(w * v, (w * v).conj()) / np.vdot(v, v).real, rho)
    okA3 &= np.allclose(np.outer(np.exp(0.7j) * v, (np.exp(0.7j) * v).conj()) / np.vdot(v, v).real, rho)
    q2 = abs(v @ v) ** 2 / np.vdot(v, v).real ** 2
    vb = v.conj(); rhob = np.outer(vb, vb.conj()) / np.vdot(vb, vb).real
    okA4 &= np.isclose(np.trace(rho @ rho.T).real, q2) and np.isclose(np.trace(rho @ rhob).real, q2)
print("QA3 centre and phase trivial on records:", okA3, "  QA4 |q|^2 = overlap(rho, rho_conj):", okA4)
score += [("QA3", okA3), ("QA4", okA4)]

# QA5: invariants in tensor products (Lie algebra kernel)
def tensor_rep(X, factors):
    n = len(factors); d = 3 ** n; M = np.zeros((d, d), complex)
    for i, f in enumerate(factors):
        mats = [np.eye(3)] * n
        mats = list(mats); mats[i] = X if f == 'v' else -X.T   # conjugate rep: -X^T (X anti-Hermitian)
        K = mats[0]
        for m in mats[1:]: K = np.kron(K, m)
        M += K
    return M
def n_inv(gens, factors):
    Mbig = np.vstack([tensor_rep(X, factors) for X in gens])
    s = np.linalg.svd(Mbig, compute_uv=False)
    return int(np.sum(s < 1e-9))
su3_only = su3_basis()
qa5 = {f: (n_inv(so3_basis(), f), n_inv(su3_only, f)) for f in ["vv", "vvv", "vc"]}
print("QA5 invariants [SO(3), SU(3)]  3x3, 3x3x3, 3x3bar:", qa5)
ok = qa5 == {"vv": (1, 0), "vvv": (1, 1), "vc": (1, 1)}
score.append(("QA5", ok))
# control: faithful dim of su(3) on records = dim of {X: [X, rho] spans} -> rank of map X -> [X, rho] over many rho
R = []
for _ in range(10):
    v = rng.normal(size=3) + 1j * rng.normal(size=3)
    rho = np.outer(v, v.conj()); R.append(rho)
rowsC = np.array([np.concatenate([(X @ r - r @ X).flatten() for r in R]) for X in su3_only])
ctrl = (np.linalg.matrix_rank(rowsC, tol=1e-9) == 8) and qa5["vv"][0] == 1
print("CONTROL su(3) faithful on records (rank 8) and so(3) delta invariant:", ctrl)
score.append(("CTRL", ctrl))

# ---------- PART B ----------
s19, s20 = 1 / np.sqrt(19), 1 / np.sqrt(20)
Vud_A2 = np.sqrt(19 / 20)
def sig(x, ex, pred): return (pred - x) / ex

prod, eprod = 0.27679, np.hypot(0.00028, 0.00020)
fk_pred = prod / s19; efk_pred = eprod / s19
print(f"\nQB1 A2 predicts fK/fpi = {fk_pred:.4f}({efk_pred*1e4:.0f})")
for name, f, ef in [("FLAG 2+1+1", 1.1934, 0.0019), ("FLAG 2+1", 1.1916, 0.0034), ("PDG-quoted", 1.1978, 0.0022)]:
    print(f"   vs {name} {f}({ef*1e4:.0f}): {(fk_pred-f)/np.hypot(ef, efk_pred):+.2f} sigma")
qb1 = (fk_pred - 1.1934) / np.hypot(0.0019, efk_pred)
score.append(("QB1", 5.2 < qb1 < 5.6))

Vus_l3 = 0.21656 / 0.9698
eVus_l3 = Vus_l3 * np.hypot(0.00035 / 0.21656, 0.0017 / 0.9698)
Vud0, eVud0 = 0.97367, 0.00032
r_semi = Vus_l3 / Vud0; er_semi = r_semi * np.hypot(eVus_l3 / Vus_l3, eVud0 / Vud0)
r_lep = prod / 1.1934; er_lep = r_lep * np.hypot(eprod / prod, 0.0019 / 1.1934)
print(f"QB2 semileptonic ratio Vus(Kl3)/Vud(0+) = {r_semi:.5f}({er_semi*1e5:.0f}); A2 1/sqrt19 = {s19:.5f}: {sig(r_semi, er_semi, s19):+.2f} sigma")
print(f"    leptonic ratio (FLAG 2+1+1) = {r_lep:.5f}({er_lep*1e5:.0f}); A2: {sig(r_lep, er_lep, s19):+.2f} sigma")
qb3 = (r_lep - r_semi) / np.hypot(er_lep, er_semi)
print(f"QB3 the SM's own leptonic - semileptonic split: {qb3:+.2f} sigma (no correlation; the two share only Vud's absence)")
score.append(("QB2", abs(sig(r_semi, er_semi, s19)) < 0.5))
score.append(("QB3", 3.0 < qb3 < 4.0))
qb4 = sig(0.22431, 0.00085, s20)
print(f"QB4 PDG S=2.5 average Vus 0.22431(85) vs 1/sqrt20 = {s20:.5f}: {qb4:+.2f} sigma")
score.append(("QB4", abs(qb4) < 1.0))

def blue(x1, e1, x2, e2, ecorr):
    Cm = np.array([[e1**2, ecorr**2], [ecorr**2, e2**2]]); Ci = np.linalg.inv(Cm)
    wv = Ci.sum(1) / Ci.sum(); x = wv @ np.array([x1, x2]); ex = np.sqrt(1 / Ci.sum())
    chi = np.array([x1 - x, x2 - x]) @ Ci @ np.array([x1 - x, x2 - x])
    return x, ex, chi
print(f"QB5 |V_ud| face, A2 = sqrt(19/20) = {Vud_A2:.6f}")
res = {}
for name, xn, en in [("PDG 67.8", 0.97413, 0.00042), ("2501.17916 Eq.29", 0.97393, 0.00041), ("PDG 67.7", 0.97441, 0.00088)]:
    for ec, lab in [(0.00013, "DeltaR-correlated"), (0.0, "uncorrelated")]:
        x, ex, chi = blue(Vud0, eVud0, xn, en, ec)
        res[(name, lab)] = (Vud_A2 - x) / ex
        print(f"    superallowed + neutron {name:17s} {lab:18s}: {x:.5f}({ex*1e5:.0f})  chi2 {chi:.2f}  A2 above by {(Vud_A2-x)/ex:+.2f} sigma")
qb5 = res[("PDG 67.8", "DeltaR-correlated")]
score.append(("QB5", 3.0 <= qb5 <= 3.6))

print("\nSCORE", sum(o for _, o in score), "/", len(score), [(n, bool(o)) for n, o in score])
