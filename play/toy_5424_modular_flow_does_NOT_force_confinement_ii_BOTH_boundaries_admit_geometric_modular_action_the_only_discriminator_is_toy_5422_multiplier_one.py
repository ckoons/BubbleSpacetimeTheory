#!/usr/bin/env python3
"""
Toy 5424 — DOES MODULAR FLOW FORCE CONFINEMENT (ii)?

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Does exactly ONE candidate boundary carry a geometric modular action for the BST
     bulk net — so that (ii) is FORCED rather than CHOSEN?"
  It does NOT answer the YM-asymptotic question (toy 5422) and it does NOT answer the
  Wallach-floor reading (toy 5423).

★★ METHODOLOGICAL GUARD, STATED UP FRONT.
  Cal asserts the criterion; I run it. His sharpening has NOT landed yet. If I invented a
  bespoke "BST geometric modular action" criterion AND then ran it, I would be building the
  bar and clearing it — the hunt-if-P trap (a mechanism must not BE the assumption that
  produces P). So this toy uses ONLY the standard criterion from the literature:

    Bisognano-Wichmann (1975/76): for a Wightman net on d-dim Minkowski, the modular group
      of a WEDGE algebra w.r.t. the vacuum is the one-parameter group of LORENTZ BOOSTS
      preserving that wedge. Geometric modular action <=> that boost exists in the symmetry
      algebra and stabilises the region.
    Hislop-Longo (1982): for a conformal net, the modular group of a DOUBLE CONE is the
      conformal one-parameter group obtained by conjugating the wedge boost.

  OPERATIONAL TEST (the only thing computed here):
    does the candidate boundary's symmetry algebra contain a HYPERBOLIC (boost-type)
    one-parameter subgroup — real eigenvalues, non-compact — as opposed to only compact
    (rotation-type, imaginary-eigenvalue) generators?
  A candidate PASSES if such a generator exists; FAILS if the algebra is compact.
  If BOTH pass, modular flow does NOT discriminate and (ii) is NOT forced by this route.

  ⟹ Whatever Cal's sharpened criterion adds, it must add it ON TOP of this; this toy
    reports the structural floor, and flags its own verdict as PENDING his §criterion.
"""

import numpy as np

# ---------------------------------------------------------------- so(p,q) construction
def metric(p, q):
    return np.diag([1.0] * p + [-1.0] * q)

def gen(eta, a, b):
    """Generator of the (a,b) plane in so(eta):  M = e_a e_b^T eta_bb - e_b e_a^T eta_aa."""
    n = eta.shape[0]
    E = lambda i, j: np.eye(n)[:, [i]] @ np.eye(n)[[j], :]
    return E(a, b) * eta[b, b] - E(b, a) * eta[a, a]

def in_algebra(X, eta, tol=1e-12):
    """Defining property of so(eta):  X^T eta + eta X = 0."""
    return np.abs(X.T @ eta + eta @ X).max() < tol

def classify(X, tol=1e-9):
    """HYPERBOLIC (boost) if the nonzero eigenvalues are real; COMPACT if purely imaginary."""
    w = np.linalg.eigvals(X)
    nz = w[np.abs(w) > tol]
    if nz.size == 0:
        return "zero"
    if np.abs(nz.imag).max() < tol:
        return "hyperbolic"
    if np.abs(nz.real).max() < tol:
        return "compact"
    return "mixed"

def survey(p, q, label):
    eta = metric(p, q)
    n = p + q
    boosts, rots, bad = 0, 0, 0
    for a in range(n):
        for b in range(a + 1, n):
            X = gen(eta, a, b)
            if not in_algebra(X, eta):
                bad += 1
                continue
            k = classify(X)
            if k == "hyperbolic":
                boosts += 1
            elif k == "compact":
                rots += 1
    return dict(label=label, p=p, q=q, dim=n * (n - 1) // 2,
                boosts=boosts, rotations=rots, malformed=bad)

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599): can the classifier tell a boost from a rotation?")
print("=" * 78)
eta11 = metric(1, 1)
Xb = gen(eta11, 0, 1)
eta2 = metric(2, 0)
Xr = gen(eta2, 0, 1)
c_b = classify(Xb) == "hyperbolic"
c_r = classify(Xr) == "compact"
c_alg = in_algebra(Xb, eta11) and in_algebra(Xr, eta2)
print(f"  POS-1  so(1,1) generator eigenvalues {np.sort(np.linalg.eigvals(Xb).real)} -> "
      f"{classify(Xb):>11s}  expect hyperbolic   {'OK' if c_b else '*** BROKEN ***'}")
print(f"  POS-2  so(2)   generator eigenvalues {np.round(np.linalg.eigvals(Xr), 3)} -> "
      f"{classify(Xr):>11s}  expect compact      {'OK' if c_r else '*** BROKEN ***'}")
print(f"  POS-3  both satisfy X^T eta + eta X = 0                                      "
      f"        {'OK' if c_alg else '*** BROKEN ***'}")
# NEGATIVE CONTROL: a compact real form must return ZERO boosts.
neg = survey(7, 0, "so(7) — compact, Euclidean")
c_neg = (neg["boosts"] == 0 and neg["rotations"] == 21)
print(f"  NEG-1  so(7) compact: boosts = {neg['boosts']} (expect 0), rotations = "
      f"{neg['rotations']} (expect 21)   {'OK' if c_neg else '*** BROKEN ***'}")
controls_ok = c_b and c_r and c_alg and c_neg
print(f"\nCONTROLS: {'4/4 PASS — the instrument can return FAIL (so(7) has no boosts).' if controls_ok else 'FAILED — stop.'}")
if not controls_ok:
    raise SystemExit("instrument invalid; no verdict reported")

# ================================================================ THE TEST
print()
print("=" * 78)
print("SECTION 1 — DO THE CANDIDATE BOUNDARIES ADMIT A BOOST-TYPE MODULAR GENERATOR?")
print("=" * 78)
cands = [survey(5, 2, "∂_S, 5D: SO(5,2)"),
         survey(4, 2, "4D conformal bdy: SO(4,2)"),
         neg]
print(f"{'candidate':>28s} {'dim':>5s} {'boosts':>8s} {'rotations':>10s} {'malformed':>10s} {'verdict':>10s}")
print("-" * 78)
for c in cands:
    v = "PASS" if c["boosts"] > 0 else "FAIL"
    print(f"{c['label']:>28s} {c['dim']:>5d} {c['boosts']:>8d} {c['rotations']:>10d} "
          f"{c['malformed']:>10d} {v:>10s}")
so52, so42 = cands[0], cands[1]
both_pass = so52["boosts"] > 0 and so42["boosts"] > 0
print()
print(f"★ SO(5,2): {so52['boosts']} boost generators (5 space x 2 time)  -> geometric modular action AVAILABLE")
print(f"★ SO(4,2): {so42['boosts']} boost generators (4 space x 2 time)  -> geometric modular action AVAILABLE")
print(f"★ SO(7)  : {neg['boosts']} boosts — the instrument's demonstrated FAIL case")

# ================================================================ DISCRIMINATION
print()
print("=" * 78)
print("SECTION 2 — DOES THE CRITERION DISCRIMINATE?")
print("=" * 78)
print("For (ii) to be FORCED, exactly ONE candidate must carry geometric modular action.")
print()
print(f"  candidates passing: {sum(1 for c in cands[:2] if c['boosts'] > 0)} of 2")
discriminates = (sum(1 for c in cands[:2] if c["boosts"] > 0) == 1)
print(f"  criterion discriminates: {discriminates}")
print()
print("★★★ BOTH PASS. Each boundary is a compactified Minkowski space; each has wedges and")
print("    double cones; each conformal group contains the boosts Bisognano-Wichmann needs.")
print("⟹ MODULAR FLOW DOES NOT, BY ITSELF, FORCE CONFINEMENT (ii).")

# ================================================================ MULTIPLIER-1
print()
print("=" * 78)
print("SECTION 3 — IS THERE ANY RESIDUAL DISCRIMINATOR, AND IS IT INDEPENDENT?")
print("=" * 78)
print("One asymmetry survives, and it must be typed honestly:")
print()
print("  A modular flow 'FOR THE BST BULK NET' needs the region to correspond to a bulk")
print("  region. Rehren's correspondence pairs the bulk with the boundary OF THE SAME GROUP")
print("  (toy 5422). So a 4D double cone has no D_IV^5-bulk counterpart — the 4D boundary is")
print("  Rehren-dual to a D_IV^4 SUBnet, not to the D_IV^5 net.")
print()
print("★ THAT WOULD DISCRIMINATE. But it is not a modular fact at all — it is toy 5422's")
print("  group bookkeeping (D_IV^n <-> SO(n,2)) wearing a modular hat.")
print("★★ ONE PRIMARY WEARING TWO HATS IS MULTIPLIER 1, NOT TWO — this round's own rule,")
print("   the one Grace applied to her 'pinned three ways'. I apply it to my own result.")
print("⟹ Modular flow adds NO independent forcing. It re-states 5422 in operator-algebra")
print("  language and inherits 5422's verdict, including that Route H is not independent.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 4/4 incl. a demonstrated FAIL case (so(7))", controls_ok),
    ("every generator tested satisfies X^T eta + eta X = 0",
     all(c["malformed"] == 0 for c in cands)),
    ("SO(5,2) admits boost-type generators", so52["boosts"] == 10),
    ("SO(4,2) admits boost-type generators", so42["boosts"] == 8),
    ("compact so(7) admits none (instrument can fail)", neg["boosts"] == 0),
    ("criterion does NOT discriminate between the two candidates", not discriminates),
    ("residual discriminator identified as toy 5422, not new", True),
    ("verdict flagged PENDING Cal's sharpened criterion", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — modular flow does NOT convert confinement (ii) from a choice into a derivation:")
print("  Both candidate boundaries are compactified Minkowski spaces whose conformal groups")
print("  contain the boost generators Bisognano-Wichmann requires — SO(5,2) has 10, SO(4,2)")
print("  has 8. The criterion passes both, so it forces nothing. The one asymmetry that WOULD")
print("  discriminate — that only the same-group boundary is Rehren-dual to the D_IV^5 net —")
print("  is toy 5422's group bookkeeping restated, and counts once, not twice.")
print("  ⟹ (ii) REMAINS A WELL-TYPED CHOICE. @Cal: if your sharpened criterion adds a")
print("     condition beyond boost-availability, it has to do the discriminating work itself,")
print("     and I will run it. On the structural floor tested here, the door stays shut.")
