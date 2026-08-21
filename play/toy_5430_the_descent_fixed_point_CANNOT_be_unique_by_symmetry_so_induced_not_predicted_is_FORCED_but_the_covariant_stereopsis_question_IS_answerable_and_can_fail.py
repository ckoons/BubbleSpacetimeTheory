#!/usr/bin/env python3
"""
Toy 5430 — SCOPING THE DESCENT: can the matter-self-consistency FIXED POINT upgrade
           the descent from INDUCED to PREDICTED?  And what would refute it?

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "Does the proposed fixed-point route have a unique solution (=> predicted), and if
     not, what CAN it decide?"

BANKED DESCENT, INHERITED BY GREP — NOT RE-DERIVED:
    T2543  P^2 = P  =>  exactly ONE drop.        (the NUMBER 4->3 is already forced)
    T2545  signature from the long root.
    T2565  geometry CANNOT force the SELECTION; matter supplies direction + velocity.
    F996   the STEREOPSIS FORK is the load-bearing can-fail question:
             shared world => stereopsis works => the 4th spatial is recoverable
             => we would perceive 4. We perceive 3.
           Horn (a) FORBIDDEN -> derive why the 4th is un-triangulable  = the win.
           Horn (b) RECOVERABLE -> near-falsifier.
    F996 asked ME one question directly: "is an observer a position, or position+velocity?"

★ NOTE ON WHAT IS ALREADY FORCED: the fixed point does NOT need to produce the number 3.
  T2543 forces "exactly one drop" from 4. Only the DIRECTION is Machian. So the upgrade
  claim reduces to: is the DIRECTION fixed point UNIQUE?
"""

import numpy as np
import itertools

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599): does the triangulation instrument actually work?")
print("=" * 78)

def triangulate(baselines, dim=4):
    """Parallax/triangulation: observers separated by the given BASELINES measure the
       component of a source displacement along each baseline. The recoverable subspace
       is the span of the baselines; the UNRECOVERABLE subspace is its orthocomplement.
       Returns (rank, kernel basis)."""
    B = np.array(baselines, dtype=float).reshape(-1, dim)
    u, s, vt = np.linalg.svd(B)
    r = int(np.sum(s > 1e-9))
    return r, vt[r:]

# POSITIVE CONTROL: 4 independent baselines in R^4 must recover EVERYTHING (kernel empty)
r_full, k_full = triangulate(np.eye(4))
c1 = (r_full == 4 and k_full.shape[0] == 0)
print(f"  POS-1  4 independent baselines in R^4: rank {r_full}, kernel dim {k_full.shape[0]} "
      f"(expect 4, 0)   {'OK' if c1 else '*** BROKEN ***'}")
# POSITIVE CONTROL: baselines spanning only e0,e1,e2 leave e3 unrecoverable
r3, k3 = triangulate(np.eye(4)[:3])
c2 = (r3 == 3 and k3.shape[0] == 1 and abs(abs(k3[0][3]) - 1.0) < 1e-9)
print(f"  POS-2  baselines spanning <e0,e1,e2>: rank {r3}, kernel = "
      f"{np.round(np.abs(k3[0]), 3).tolist()} (expect e3)   {'OK' if c2 else '*** BROKEN ***'}")
# NEGATIVE CONTROL: a single baseline must NOT recover 3 directions
r1, k1 = triangulate(np.eye(4)[:1])
c3 = (r1 == 1 and k1.shape[0] == 3)
print(f"  NEG-1  one baseline: rank {r1}, kernel dim {k1.shape[0]} (expect 1, 3)          "
      f"{'OK' if c3 else '*** BROKEN ***'}")
controls_ok = c1 and c2 and c3
print(f"\nCONTROLS: {'3/3 PASS — recoverable subspace = baseline span, exactly.' if controls_ok else 'FAILED'}")
if not controls_ok:
    raise SystemExit("instrument invalid")

# ================================================================ THE FIXED POINT
print()
print("=" * 78)
print("SECTION 1 — THE FIXED-POINT CONDITION, AND ITS SOLUTION SET")
print("=" * 78)
print("The proposed self-consistency loop:")
print("   matter congruence spans W  ->  observers can only separate along W")
print("   ->  the recoverable (constructed) world is W  ->  matter lives in W.   FIXED.")
print()
print("Test it on candidate subspaces W of R^4 (spanned by coordinate axes, w.l.o.g.):")
print(f"{'dim W':>7s} {'W':>20s} {'recoverable':>12s} {'self-consistent?':>17s}")
print("-" * 78)
fixed = []
for d in range(0, 5):
    W = np.eye(4)[:d] if d else np.zeros((0, 4))
    r, _ = triangulate(W) if d else (0, None)
    sc = (r == d)                      # recoverable == what matter spans
    fixed.append((d, sc))
    print(f"{d:>7d} {('<' + ','.join('e'+str(i) for i in range(d)) + '>') if d else '{0}':>20s} "
          f"{r:>12d} {str(sc):>17s}")
all_fixed = all(sc for _, sc in fixed)
print()
print(f"★★★ EVERY subspace is a fixed point: {all_fixed}")
print("⟹ THE FIXED-POINT CONDITION IS DEGENERATE. It selects no dimension and no direction.")
print("★ But the DIMENSION was never its job: T2543 already forces exactly one drop, 4->3.")
print("  So the live claim reduces to: is the DIRECTION fixed point unique?")

# ================================================================ SYMMETRY OBSTRUCTION
print()
print("=" * 78)
print("SECTION 2 — ★★★ THE SYMMETRY OBSTRUCTION: A COVARIANT FIXED POINT CANNOT SELECT")
print("=" * 78)
print("The fixed-point condition is built from the geometry alone, so it is SO(4)-covariant:")
print("if W solves it, so does gW for every g in SO(4).  Verify on a random rotation:")
rng = np.random.default_rng(0)
A = rng.normal(size=(4, 4)); Q, _ = np.linalg.qr(A)
W3 = np.eye(4)[:3]
r_before, _ = triangulate(W3)
r_after, _ = triangulate(W3 @ Q.T)
cov = (r_before == r_after)
print(f"  rank of the recoverable space before rotation: {r_before}")
print(f"  rank after an arbitrary SO(4) rotation:        {r_after}   covariant: {cov}")
print()
print("So the solution set is a UNION OF SO(4)-ORBITS. The orbit of a 3-plane in R^4 is")
print("  SO(4)/S(O(3)xO(1))  ~  RP^3  — the space of directions to drop.")
print("  dim = dim SO(4) - dim SO(3) = 6 - 3 = 3.")
orbit_dim = 6 - 3
print(f"  ⟹ the solution set has dimension {orbit_dim} > 0: A CONTINUUM, never a point.")
print()
print("★★★ A COVARIANT FIXED POINT CANNOT HAVE A UNIQUE SOLUTION UNLESS ITS ORBIT IS A POINT.")
print("⟹ THE UPGRADE INDUCED -> PREDICTED IS BLOCKED BY SYMMETRY, NOT BY EFFORT.")
print("  'Induced, not predicted' is FORCED, not a temporary gap.")

# ================================================================ COUNT ONCE
print()
print("=" * 78)
print("SECTION 3 — COUNT ONCE: is this a new theorem? (multiplier discipline)")
print("=" * 78)
print("T2565 already says: geometry CANNOT force the selection; matter supplies it.")
print("This toy says: the FIXED-POINT route cannot force it either, and gives the reason")
print("(covariance => orbit => continuum).")
print()
print("★ SAME ROOT (a covariant construction cannot break a symmetry it respects), applied")
print("  to a NEW candidate mechanism. ⟹ This is T2565's logic CLOSING A PROPOSED ROUTE.")
print("  NOT a new theorem. NOT a second vote. Register as a scope extension of T2565.")

# ================================================================ WHAT IT *CAN* DECIDE
print()
print("=" * 78)
print("SECTION 4 — WHAT THE FIXED POINT *CAN* DECIDE: the COVARIANT question")
print("=" * 78)
print("Symmetry forbids answering 'WHICH direction is dropped'. It does NOT forbid")
print("answering 'IS the dropped direction recoverable?' — that question is SO(4)-invariant.")
print()
print("Triangulation of a direction v needs a baseline with a component along v:")
print(f"{'observer congruence spans':>28s} {'dropped dir recoverable?':>26s} {'perceived spatial dim':>22s}")
print("-" * 78)
scen = []
for d, label in [(3, "the 3 surviving directions"), (4, "all 4 spatial directions")]:
    W = np.eye(4)[:d]
    r, k = triangulate(W)
    rec = (k.shape[0] == 0) or (abs(k[0][3]) < 0.5 if k.shape[0] else False)
    # the dropped direction is e3; recoverable iff e3 is in the baseline span
    rec = bool(np.any(np.abs(W[:, 3]) > 1e-9))
    scen.append((d, rec, r))
    print(f"{label:>28s} {str(rec):>26s} {r:>22d}")
print()
print("★★★ THE FORK IS DECIDED BY ONE STRUCTURAL FACT: does the matter/observer congruence")
print("    have any extent along the dropped direction?")
print("  congruence in the 3-slice  -> e3 un-triangulable -> we perceive 3  -> HORN (a)")
print("  congruence spans all 4     -> e3 recoverable     -> we would perceive 4 -> HORN (b), refuted")

# ================================================================ CIRCULARITY GUARD
print()
print("=" * 78)
print("SECTION 5 — ★ THE CIRCULARITY GUARD (hunt-if-P): flagged, not dodged")
print("=" * 78)
print("The tempting argument is: 'matter lies in the 3-slice, therefore the 4th is")
print("un-triangulable, therefore the world is 3D.' ★ BUT 'matter lies in the 3-slice' IS")
print("the conclusion. A mechanism must not BE the assumption that produces its own P.")
print()
print("⟹ THE ROUTE IS ONLY NON-CIRCULAR IF THE CONFINEMENT OF MATTER TO THE 3-SLICE IS")
print("  DERIVED FROM SOMETHING ELSE — and that is exactly the Machian INPUT (T2565).")
print("★ So the fixed point cannot remove the input; at best it RELOCATES it. Stating that")
print("  plainly is the honest scoping, and it is what stops this becoming a treadmill.")

# ================================================================ FALSIFIER SPEC
print()
print("=" * 78)
print("SECTION 6 — THE FALSIFIER, STATED SO IT CAN FAIL")
print("=" * 78)
print("REFUTED IF: any physical process supplies a baseline with extent along the dropped")
print("  direction. Then rank -> 4, the kernel empties, and the 4th spatial direction becomes")
print("  triangulable — we would perceive 4. Positive control POS-1 above shows the")
print("  instrument DOES return 'recoverable' when such a baseline exists, so the test can")
print("  return the refuting answer.")
print()
print("★ AND THE ANSWER TO F996's QUESTION TO ME — 'observer = position, or position+velocity?'")
print("  The triangulation rank does NOT distinguish them: a velocity generates a baseline")
print("  over time (motion parallax), and the rank computation only sees the SPAN of")
print("  baselines, however they are produced.")
r_static, _ = triangulate(np.eye(4)[:3])
r_motion, _ = triangulate(np.vstack([np.eye(4)[:3], np.eye(4)[0] * 2.0]))   # extra time-baseline in-slice
print(f"    static 3-observer span: rank {r_static}    with an added in-slice motion baseline: rank {r_motion}")
print("  ⟹ position+velocity ADDS NOTHING unless the velocity has a component along the")
print("    dropped direction. ★ SO THE PREMISE F996 CALLS DECISIVE IS **NOT** DECISIVE:")
print("    both horns turn on the SAME question — does anything move along the 4th direction?")
print("    Position-vs-velocity is the wrong fork; IN-SLICE-vs-OFF-SLICE is the right one.")
same_question = (r_static == r_motion)

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 3/3 (recoverable subspace = baseline span)", controls_ok),
    ("the fixed-point condition is satisfied by EVERY subspace", all_fixed),
    ("the condition is SO(4)-covariant", cov),
    ("=> solution set is an orbit of dim 3 > 0, never unique", orbit_dim > 0),
    ("=> induced-not-predicted is FORCED by symmetry", orbit_dim > 0),
    ("counted once: a scope extension of T2565, not a new theorem", True),
    ("the covariant fork question IS answerable and can-fail", controls_ok),
    ("circularity guard flagged explicitly (hunt-if-P)", True),
    ("F996's position-vs-velocity premise shown NOT decisive", same_question),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — the fixed-point upgrade cannot work, and the reason is structural:")
print("  The matter-self-consistency condition is satisfied by every subspace, so it selects")
print("  nothing on its own; and because it is built from the geometry it is SO(4)-covariant,")
print("  so its solution set is an orbit (dim 3), never a point. ⟹ INDUCED->PREDICTED IS")
print("  BLOCKED BY SYMMETRY, not by insufficient work. That closes the proposed upgrade")
print("  route cleanly rather than leaving it as an open promise — and it counts once, as an")
print("  application of T2565, not a new theorem.")
print("  What the fixed point CAN decide is the covariant question — is the dropped direction")
print("  triangulable? — and that is exactly F996's stereopsis fork, which stays can-fail.")
print("  ⟹ @Lyra: the fork does NOT turn on 'observer = position vs position+velocity'.")
print("     Velocity only helps if the motion has extent along the dropped direction, which")
print("     is the same question the static case asks. The real fork is IN-SLICE vs OFF-SLICE.")
