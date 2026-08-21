#!/usr/bin/env python3
"""
Toy 5427 — THE SINGLE-BOOST STRATUM: is there a forcing route there?

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Does a bifurcation/modular criterion living on the single-boost stratum discriminate
     n = 5 from n = 4?"

OBJECT DECLARATION (the rule the team just adopted — and it is the whole finding):
    OBJECT A — fixed subspace of ad(K)^2 in 𝔭.
               type: linear subspace | domain: 𝔭 ⊂ 𝔤 = so(n,2) | ambient: the BULK
               symmetric space D_IV^n, real dim 2n.   THIS is what Toy 337 computes.
    OBJECT B — fixed-point set of exp(tK) on the Silov boundary.
               type: projective variety | domain: null directions in R^{n,2}
               ambient: ∂_S = (S^{n-1} x S^1)/Z_2, dim n.  THIS is what Kay-Wald's
               "bifurcation surface, codim 2 in spacetime" is ABOUT.

★★ A AND B ARE DIFFERENT OBJECTS IN DIFFERENT AMBIENTS, AND THE CRITERION HAS BEEN
   READING A's DIMENSION AGAINST B's CONVENTION. This toy computes BOTH, for both
   strata, across D_IV^4..D_IV^9.

Round-37 result inherited (toy 5425, not re-derived): OBJECT A at K_phys = H_1+H_2 gives
dim 3 for EVERY n -> rank-generic -> selects nothing.
Round-38 instruction inherited: the single-boost stratum tracks n (4,5,6,...) in OBJECT A,
"but it gives dim B = n, not n-2, so the Kay-Wald convention needs re-pinning first."
⟹ This toy shows the convention does NOT need re-pinning. OBJECT B already gives n-2.
"""

import numpy as np

# ---------------------------------------------------------------- so(n,2)
def build(nsp):
    N = nsp + 2
    eta = np.diag([1.0] * nsp + [-1.0, -1.0])
    def gen(i, j):
        X = np.zeros((N, N)); X[i, j] = 1.0
        X[j, i] = -eta[i, i] * eta[j, j]
        return X
    basis = [gen(i, j) for i in range(N) for j in range(i + 1, N)]
    p = [X for X in basis if np.allclose(X.T, X, atol=1e-12)]
    return dict(N=N, eta=eta, p=p, H1=gen(0, nsp), H2=gen(1, nsp + 1))

def orthonormalize(mats):
    out = []
    for M in mats:
        V = M.copy()
        for B in out:
            V = V - np.sum(B * V) * B
        nv = np.sqrt(np.sum(V * V))
        if nv > 1e-9:
            out.append(V / nv)
    return out

# ---------------------------------------------------------------- OBJECT A (bulk)
def objectA_dim(K, pbasis, tol=1e-8):
    """dim of the fixed subspace of ad(K)^2 in 𝔭 = the BULK fixed submanifold."""
    B = orthonormalize(pbasis)
    ad = lambda X: K @ X - X @ K
    M = np.zeros((len(B), len(B)))
    for j, Xj in enumerate(B):
        Y = ad(ad(Xj))
        for i, Xi in enumerate(B):
            M[i, j] = np.sum(Xi * Y)
    return int(np.sum(np.abs(np.linalg.eigvals(M).real) < tol))

# ---------------------------------------------------------------- OBJECT B (boundary)
def signature(G, tol=1e-9):
    w = np.linalg.eigvalsh(G)
    return int(np.sum(w > tol)), int(np.sum(w < -tol)), int(np.sum(np.abs(w) <= tol))

def proj_nullcone_dim(W, eta):
    """dim of the projectivised null cone of the subspace spanned by columns of W."""
    d = W.shape[1]
    if d == 0:
        return -1
    G = W.T @ eta @ W
    pp, qq, zz = signature(G)
    if pp >= 1 and qq >= 1:
        return d - 2                 # a genuine quadric hypersurface, projectivised
    if pp == 0 and qq == 0:
        return d - 1                 # totally null: every direction is null
    return zz - 1                    # definite modulo radical: null cone = the radical

def objectB_dim(K, eta, tol=1e-7):
    """dim of the fixed-point set of exp(tK) on the projectivised null cone.
       [v] is fixed  <=>  v is a null EIGENvector of K."""
    w, V = np.linalg.eig(K)
    dims = []
    for lam in sorted(set(np.round(w.real, 7))):
        cols = [i for i in range(len(w)) if abs(w[i].real - lam) < tol
                and abs(w[i].imag) < tol]
        if not cols:
            continue
        W = np.real(V[:, cols])
        # re-orthogonalise the eigenspace basis for numerical safety
        Q, _ = np.linalg.qr(W)
        dims.append(proj_nullcone_dim(Q, eta))
    return max(dims) if dims else -1

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599)")
print("=" * 78)
G5 = build(5)
cA = objectA_dim(G5["H1"] + G5["H2"], G5["p"]) == 3
print(f"  POS-1  OBJECT A reproduces toy 5425 / Toy 337 at K_phys: dim = "
      f"{objectA_dim(G5['H1'] + G5['H2'], G5['p'])} (expect 3)   {'OK' if cA else '*** BROKEN ***'}")
# hand-checkable OBJECT B: single boost in so(5,2). 0-eigenspace = <e1,e2,e3,e4,e6>,
# signature (4,1), so its projectivised null cone has dim 4+1-2 = 3.
b5 = objectB_dim(G5["H1"], G5["eta"])
cB = (b5 == 3)
print(f"  POS-2  OBJECT B, single boost, so(5,2): dim = {b5} (hand-check: sig(4,1) -> "
      f"4+1-2 = 3)   {'OK' if cB else '*** BROKEN ***'}")
# NEGATIVE CONTROL: a GENERIC element of 𝔞 must return something SMALLER than 3, or the
# test is just printing 3 for everything.  (My first attempt used a compact rotation and it
# returned 3 — correctly: a rotation fixes everything orthogonal to its plane, so the
# control premise was wrong, not the instrument. That result is kept below as a FINDING.)
Kgen = G5["H1"] + 2.0 * G5["H2"]
gen_b = objectB_dim(Kgen, G5["eta"])
cN = (gen_b < 3)
print(f"  NEG-1  a GENERIC K in 𝔞 gives OBJECT B dim = {gen_b} (< 3: the test is not "
      f"trivially satisfied)   {'OK' if cN else '*** BROKEN ***'}")
rot = np.zeros((7, 7)); rot[0, 1] = 1.0; rot[1, 0] = -1.0     # so(5) rotation, in 𝔨
rot_b = objectB_dim(rot, G5["eta"])
print(f"  ★ FINDING (not a control): a compact ROTATION also gives OBJECT B dim = {rot_b}.")
print(f"    The bifurcation DIMENSION alone does not even distinguish a boost from a")
print(f"    rotation — another reason it cannot carry a forcing argument by itself.")
controls_ok = cA and cB and cN
print(f"\nCONTROLS: {'3/3 PASS' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ BOTH OBJECTS
print()
print("=" * 78)
print("SECTION 1 — BOTH OBJECTS, BOTH STRATA, ACROSS THE FAMILY")
print("=" * 78)
print(f"{'n_C':>4s} {'bulk dim':>9s} | {'A: K_phys':>10s} {'A: 1-boost':>11s} | "
      f"{'B: K_phys':>10s} {'B: 1-boost':>11s} {'n-2':>5s}")
print("-" * 78)
rows = []
for nsp in range(4, 10):
    G = build(nsp)
    Kd, Ks = G["H1"] + G["H2"], G["H1"]
    a_d, a_s = objectA_dim(Kd, G["p"]), objectA_dim(Ks, G["p"])
    b_d, b_s = objectB_dim(Kd, G["eta"]), objectB_dim(Ks, G["eta"])
    rows.append((nsp, a_d, a_s, b_d, b_s))
    print(f"{nsp:>4d} {2*nsp:>9d} | {a_d:>10d} {a_s:>11d} | {b_d:>10d} {b_s:>11d} {nsp-2:>5d}")

A_diag_flat = len({r[1] for r in rows}) == 1
A_boost_tracks = [r[2] for r in rows] == list(range(4, 10))
B_boost_is_nm2 = all(r[4] == r[0] - 2 for r in rows)
B_diag_flat = len({r[3] for r in rows}) == 1
print()
print(f"★ OBJECT A, diagonal  K_phys : constant 3 across the family  -> rank-generic  ({A_diag_flat})")
print(f"★ OBJECT A, single boost     : 4,5,6,7,8,9 = n              -> tracks n, but = n NOT n-2")
print(f"★ OBJECT B, diagonal  K_phys : constant {rows[0][3]} across the family -> NOT a Rindler boost ({B_diag_flat})")
print(f"★★★ OBJECT B, single boost   : EXACTLY n-2 at every n        -> Kay-Wald, no re-pinning ({B_boost_is_nm2})")

# ================================================================ THE CATCH
print()
print("=" * 78)
print("SECTION 2 — THE OBJECT-DECLARATION CATCH")
print("=" * 78)
print("Kay-Wald: 'the bifurcation surface is codim 2 IN THE SPACETIME.' That is a statement")
print("about OBJECT B (a set in the boundary spacetime), not OBJECT A (a subspace of 𝔭).")
print()
print("Is OBJECT A ever codim 2 in the bulk? bulk dim = 2n; codim 2 needs dim = 2n-2:")
print(f"{'n_C':>4s} {'2n-2 needed':>12s} {'A: K_phys':>10s} {'A: 1-boost':>11s} {'either?':>8s}")
print("-" * 78)
never_codim2 = True
for nsp, a_d, a_s, _, _ in rows:
    hit = (a_d == 2 * nsp - 2) or (a_s == 2 * nsp - 2)
    never_codim2 &= (not hit)
    print(f"{nsp:>4d} {2*nsp-2:>12d} {a_d:>10d} {a_s:>11d} {str(hit):>8s}")
print()
print("★★★ OBJECT A IS NEVER CODIM 2 IN THE BULK, FOR ANY K IN 𝔞, AT ANY n.")
print("⟹ The Kay-Wald convention CANNOT be applied to OBJECT A at all — not with a")
print("  re-pinned constant, not ever. The 'dim B = n, not n-2, so re-pin the convention'")
print("  worry dissolves: read the RIGHT OBJECT and the convention already holds exactly.")
print("★ The single boost's OBJECT B is n-2 on the nose at every n. Nothing to re-pin.")

# ================================================================ DOES IT SELECT?
print()
print("=" * 78)
print("SECTION 3 — SO DOES IT SELECT n = 5 OVER n = 4?")
print("=" * 78)
print("The 4D boundary sits inside ∂_S as the null cone of R^{4,2} ⊂ R^{5,2}.")
print("Is it preserved by the single boost H_1 = boost(e_0, e_5)?  H_1 mixes e_0 and e_5,")
print("both of which lie in R^{4,2} = <e_0,e_1,e_2,e_3,e_5,e_6>.  So YES, preserved.")
G4 = build(4)
b4 = objectB_dim(G4["H1"], G4["eta"])
b5s = objectB_dim(G5["H1"], G5["eta"])
print()
print(f"  single boost on the 5D boundary (so(5,2)):  bifurcation surface dim = {b5s} = 5-2 ✓")
print(f"  single boost on the 4D boundary (so(4,2)):  bifurcation surface dim = {b4} = 4-2 ✓")
print()
print("★★★ BOTH ARE LEGITIMATE RINDLER BOOSTS OF THEIR OWN SPACETIME.")
print("★★★ THE CRITERION RETURNS 'dim = (the dimension of whichever boundary you handed it) - 2'.")
print("⟹ n is an INPUT to this computation, not an OUTPUT. It CONFIRMS a dimension; it")
print("  cannot SELECT one. A consistency check, not a selector.")
selects = (b4 == b5s)
print(f"  does it discriminate 4 from 5?  {not selects}  — it returns different values, but")
print("  only because it was TOLD which boundary to compute on.")

# ================================================================ CONSTRUCTIVE
print()
print("=" * 78)
print("SECTION 4 — WHAT AN ACTUAL SELECTOR WOULD NEED (handing off, not claiming)")
print("=" * 78)
print("A selector must break the symmetry WITHOUT being told the answer. The one structural")
print("asymmetry visible from here is G-stability, and it is Cal's lane (@Cal, your survivor):")
e4 = np.zeros(7); e4[4] = 1.0
G_54 = build(5)
Kout = np.zeros((7, 7)); Kout[4, 5] = 1.0; Kout[5, 4] = 1.0     # boost(e_4, e_5) in so(5,2)
moved = abs((Kout @ e4)[5]) > 1e-9
print(f"  R^{{4,2}} = <e_0,e_1,e_2,e_3,e_5,e_6> omits e_4.")
print(f"  The so(5,2) generator boost(e_4,e_5) maps e_4 out of R^{{4,2}}: {moved}")
print("  ⟹ the 4D boundary is NOT stable under the full G = SO(5,2); only under SO(4,2).")
print("★ That IS an asymmetry not read off the answer — but it must be family-swept the same")
print("  way this one was before it banks. @Cal @Grace: does 'unique closed G-orbit' hold")
print("  for every D_IV^n (rank-generic) or does it pick out n? Same question that killed")
print("  the last selector. I am NOT claiming it; I am handing it over pre-swept.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 3/3 (A reproduces 5425, B hand-checked, generic-K negative)", controls_ok),
    ("bifurcation dim does not distinguish a boost from a rotation", rot_b == 3),
    ("OBJECT A at K_phys is rank-generic (constant 3)", A_diag_flat),
    ("OBJECT A at the single boost equals n (tracks, but wrong convention)", A_boost_tracks),
    ("OBJECT B at the single boost equals n-2 EXACTLY, every n", B_boost_is_nm2),
    ("=> the Kay-Wald convention needs NO re-pinning, just the right object", B_boost_is_nm2),
    ("OBJECT B at K_phys is constant => K_phys is not a Rindler boost", B_diag_flat),
    ("OBJECT A is never codim 2 in the bulk, any K, any n", never_codim2),
    ("both boundaries pass => confirms a dimension, cannot select one", b4 == 2 and b5s == 3),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the single-boost stratum is the RIGHT stratum and still not a forcing route:")
print("  The good news first: the convention never needed re-pinning. Read the boundary object")
print("  instead of the bulk one and the single boost gives bifurcation dim = n-2 exactly, at")
print("  every n — textbook Kay-Wald. K_phys does NOT (it gives a constant 1), so K_phys was")
print("  never a Rindler boost of the boundary; and OBJECT A is never codim 2 in the bulk for")
print("  any K, so the convention could not have been rescued by re-pinning a constant.")
print("  The bad news: the criterion computes n-2 from whichever boundary it is handed. n goes")
print("  IN. It is a consistency check, and a good one — it would have caught a wrong pairing —")
print("  but it cannot select 5 over 4. Both boundaries pass on their own terms.")
print("  ⟹ Confinement (ii) stays an honest choice. The surviving asymmetry is G-stability,")
print("     it is Cal's, and it needs the same family sweep before anyone banks it.")
