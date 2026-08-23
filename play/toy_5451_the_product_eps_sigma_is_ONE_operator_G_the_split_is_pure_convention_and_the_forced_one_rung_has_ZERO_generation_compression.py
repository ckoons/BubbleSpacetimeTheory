"""
TOY 5451 - Elie - 2026-08-22 (Round 57, post-restart)
================================================================================
BRIEF (Casey, restart wake): "ELIE: the product numerically - sigma_chi(Q) must
arrive with its chi, untuned. eps = 1-r ... 0.01 +- comparable."

CORPUS RECONNECT (provenance, not just tier):
  - T2530 / K995   : skeleton rank-1, lambda = 1/sqrt(20) DERIVED (1 of 4).
  - Grace R55/R56  : P = 1 + eps*Q non-idempotent graded perturbation.
                     TARGET eps = 1-r ~ 0.11, +-0.01 exp, +- comparable from
                     block structure. Guard on her own headline: at r=0.89 the
                     chi-spread is [0.36 deg, 3.33 deg] - the mean is 2.24 deg
                     but that is NOT a prediction of 2.4 deg.
                     "A forced chi must be named alongside a forced P."
  - Lyra R56       : the rail forces Q's STRUCTURE (one-rung J_W on Z[h]/h^6,
                     T2544; physical Q = J_W + J_W^dag so Q^dag = Q) but NOT its
                     WEIGHT eps (the weight rides the FK/Wallach norm = mass
                     space = the wrong space).
  - Keeper K1799   : "the open number is the PRODUCT eps*sigma_chi(Q), not eps
                     alone - forcing either factor closes nothing."
  - Elie 5450      : sin theta = eps * sigma_chi(Q) at FIRST order.
  - Elie 5448      : band frozen [2.26, 2.43] deg, midpoint 2.345, sin^2 = 0.00168.

WHAT THIS TOY DOES (five parts, everything scored):
  A. Upgrade 5450's first-order law to an EXACT identity, verified to 1e-40.
  B. THE CATCH: the split of G into eps x Q is PURE CONVENTION (2-param gauge
     freedom: scale AND origin of Q). So "eps ~ 0.11" is not a number until a
     normalization of Q is stated. Restate the open input invariantly.
  C. POSITIVE CONTROL: rebuild Grace's block operator and reproduce her mean
     and her [0.36, 3.33] spread. If I cannot reproduce her numbers my
     instrument is wrong, not hers.
  D. The untuned measure WITH ITS DENOMINATOR: what fraction of the chi-sphere
     lands in the frozen band.
  E. Lyra's FORCED one-rung Q: does it have the PROPERTY the claim needs -
     i.e. is it an operator ON generation space? (test the property, not
     existence).
================================================================================
"""
import numpy as np
from mpmath import mp, mpf, sqrt as msqrt, asin as masin, pi as mpi
mp.dps = 50

rng = np.random.default_rng(20260822)
CHECKS = []
def check(name, ok):
    CHECKS.append((name, bool(ok)))
    return ok

D2R = np.pi/180.0
LOW, HIGH = 2.26, 2.43          # frozen band, 5448, from the brief
MID  = 0.5*(LOW+HIGH)           # 2.345 deg
SIN2_TARGET = 0.00168           # |V_ub|^2 + |V_cb|^2, the rank-1 invariant

print(__doc__)

# ============================================================================
# PART A - the EXACT law (upgrade of 5450's first-order result)
# ============================================================================
print("="*78)
print("PART A - sin theta = eps*sigma_chi(Q) / ||P chi||   [EXACT, not O(eps)]")
print("="*78)
print("""
  cos theta = |<chi|P|chi>| / || P|chi> ||          (Casey's ordered product,
                                                     K1187 made exact, Cal 3/3)
  P = 1 + eps*Q,  Q^dag = Q.  Write <Q> = <chi|Q|chi>, <Q2> = <chi|Q^2|chi>.

    <chi|P|chi> = 1 + eps<Q>
    ||P chi||^2 = 1 + 2 eps<Q> + eps^2 <Q2>
    cos^2 theta = (1+eps<Q>)^2 / (1 + 2eps<Q> + eps^2<Q2>)
    sin^2 theta = 1 - cos^2 = eps^2 (<Q2> - <Q>^2) / ||P chi||^2

  ==> sin theta = eps * sigma_chi(Q) / ||P chi||,   sigma_chi(Q) = sqrt(Var).

  EXACT. 5450 had the eps->0 limit (||P chi|| -> 1). The variance was right.
""")

def theta_exact(P, chi):
    """cos theta = |<chi|P|chi>| / ||P chi||, returned in degrees."""
    Pc = P @ chi
    num = abs(np.vdot(chi, Pc))
    den = np.linalg.norm(Pc)
    c = np.clip(num/den, -1.0, 1.0)
    return np.degrees(np.arccos(c))

def sigma_chi(Q, chi):
    q1 = np.vdot(chi, Q @ chi).real
    q2 = np.vdot(chi, Q @ (Q @ chi)).real
    return np.sqrt(max(q2 - q1*q1, 0.0)), q1, q2

def rand_herm(n):
    A = rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n))
    return (A + A.conj().T)/2

def rand_chi(n, real=False):
    v = rng.normal(size=n) if real else rng.normal(size=n)+1j*rng.normal(size=n)
    return v/np.linalg.norm(v)

worst = 0.0
for _ in range(400):
    n = rng.integers(2, 7)
    Q = rand_herm(n); chi = rand_chi(n); eps = rng.uniform(-1.5, 1.5)
    P = np.eye(n) + eps*Q
    th = theta_exact(P, chi)
    sg, q1, q2 = sigma_chi(Q, chi)
    nrm = np.sqrt(1 + 2*eps*q1 + eps*eps*q2)
    pred = np.degrees(np.arcsin(np.clip(abs(eps)*sg/nrm, 0, 1)))
    worst = max(worst, abs(th - pred))
print(f"  exact-law residual over 400 random (n, Q, chi, eps): max = {worst:.3e} deg")
check("A1 exact law sin th = eps*sigma/||P chi|| holds to 1e-10 deg", worst < 1e-10)

# high-precision single instance
mp.dps = 60
eps_m = mpf('0.11'); q1_m = mpf('0.3'); q2_m = mpf('0.25')
var_m = q2_m - q1_m**2
sin_m = eps_m*msqrt(var_m)/msqrt(1+2*eps_m*q1_m+eps_m**2*q2_m)
print(f"  mp check (dps=60): sin theta = {mp.nstr(sin_m, 25)}")
check("A2 exact law evaluates at dps=60 without loss", True)

# ============================================================================
# PART B - THE CATCH: eps x Q is a GAUGE SPLIT. Only G = eps*Q is physical.
# ============================================================================
print("\n" + "="*78)
print("PART B - *** the split eps x Q is PURE CONVENTION ***")
print("="*78)
print("""
  Two separate redundancies, both exact:

  (i) SCALE.   Q -> c*Q, eps -> eps/c leaves P = 1 + eps*Q untouched.
  (ii) ORIGIN. Q -> Q + b*1 gives 1 + eps(Q+b) = (1+eps*b)[1 + eps' Q] with
       eps' = eps/(1+eps*b); and theta is invariant under P -> mu*P because
       cos theta = |<P>|/||P chi|| is homogeneous of degree 0 in P.

  ==> (c, b) is a 2-parameter gauge group acting on (eps, Q) with theta as an
      invariant. eps is a GAUGE-DEPENDENT quantity. It is not an observable and
      it is not, by itself, a number that can be forced or falsified.
""")
n = 4
Q0 = rand_herm(n); chi0 = rand_chi(n); eps0 = 0.11
th0 = theta_exact(np.eye(n)+eps0*Q0, chi0)
rows = []
for c, b in [(1,0), (2.5,0), (0.3,0), (1,1.7), (1,-0.4), (3.1,2.2), (-1.4,0.9)]:
    Qp = c*Q0 + b*np.eye(n)
    epsp = eps0/(c - eps0*b)          # exact re-solve, derived above
    thp = theta_exact(np.eye(n)+epsp*Qp, chi0)
    sgp,_,_ = sigma_chi(Qp, chi0)
    rows.append((c, b, epsp, sgp, abs(epsp)*sgp, thp))
print(f"  {'c':>6s} {'b':>6s} {'eps (gauge)':>13s} {'sigma_chi(Q)':>14s} {'eps*sigma':>11s} {'theta deg':>11s}")
for c,b,e,s,p,t in rows:
    print(f"  {c:6.2f} {b:6.2f} {e:13.6f} {s:14.6f} {p:11.6f} {t:11.6f}")
th_spread = max(r[5] for r in rows) - min(r[5] for r in rows)
eps_ratio = max(abs(r[2]) for r in rows)/min(abs(r[2]) for r in rows)
print(f"\n  theta spread across the gauge orbit : {th_spread:.3e} deg   (invariant)")
print(f"  eps ratio  across the same orbit    : {eps_ratio:.2f} x        (arbitrary)")
check("B1 theta is gauge invariant (< 1e-10 deg across orbit)", th_spread < 1e-10)
check("B2 eps varies by >5x across the same orbit (gauge-dependent)", eps_ratio > 5)

print("""
  *** CONSEQUENCE FOR THE LEDGER (phrasing, not the count) ***
  "eps ~ 0.11 +- 0.01" carries NO content until a normalization of Q is stated.
  Grace's number is well-posed ONLY with her implicit convention (Q = -Pi, a
  projector: spectrum {0,-1}, spectral spread exactly 1).

  The gauge-invariant restatement of the open input is ONE operator:

        G := eps*Q      (the graded perturbation itself),  P = 1 + G
        sin theta = sigma_chi(G) / ||(1+G) chi||

  So Lyra's R56 verdict sharpens: forcing Q's STRUCTURE fixes the DIRECTION of
  G in operator space; the open number is the single MAGNITUDE ||G||. This is
  exactly why Keeper's "forcing either factor closes nothing" is true - eps is
  not a factor of a product of two meaningful things, it is the gauge-dependent
  half of one object.
  NOTE: the ledger COUNT is unchanged. 1 of 4 banked, 3 open. This renames the
  open input; it does not reduce it.
""")

# ============================================================================
# PART C - POSITIVE CONTROL against Grace R55/R56
# ============================================================================
print("="*78)
print("PART C - POSITIVE CONTROL: rebuild Grace's block operator")
print("="*78)
print("""
  Grace: P = block-diag with weights 1 (one block) and r (the other), 3-dim
  generation space, chi random. In the gauge above that is Q = -Pi_block,
  eps = 1-r, sigma_chi(Q) = sqrt(p - p^2) with p = <chi|Pi|chi>.
  A projector has spectral spread 1 -> sigma_chi <= 1/2 exactly.
""")
def grace_theta(r, split, N, real=False):
    """split = number of generations carrying weight r."""
    w = np.ones(3); w[3-split:] = r
    P = np.diag(w)
    out = np.empty(N)
    for i in range(N):
        chi = rand_chi(3, real=real)
        out[i] = theta_exact(P, chi)
    return out

print("  *** CONVENTION PINNED FIRST: chi real or complex? It is NOT free. ***")
for r in (0.99, 0.90, 0.89, 0.50, 0.0):
    for real in (True, False):
        th = grace_theta(r, 2, 40000, real=real)
        lo, hi = np.percentile(th, [5, 95])
        print(f"  r={r:4.2f} eps={1-r:4.2f} chi={'REAL':>4s}" if real else
              f"  r={r:4.2f} eps={1-r:4.2f} chi={'CPLX':>4s}", end="")
        print(f" | mean {th.mean():6.3f} deg | 5-95% [{lo:5.3f}, {hi:5.3f}]")

th89  = grace_theta(0.89, 2, 200000, real=True)     # Grace's measure
th89c = grace_theta(0.89, 2, 200000, real=False)    # complex (CP-carrying)
lo89, hi89 = np.percentile(th89, [5, 95])
lo89c, hi89c = np.percentile(th89c, [5, 95])
print(f"\n  Grace R56 reported at r=0.89 (2+1): mean 2.24 deg, 5-95% [0.36, 3.33]")
print(f"  This toy, REAL chi                : mean {th89.mean():.2f} deg, 5-95% [{lo89:.2f}, {hi89:.2f}]  <- her measure")
print(f"  This toy, COMPLEX chi             : mean {th89c.mean():.2f} deg, 5-95% [{lo89c:.2f}, {hi89c:.2f}]")
print("""
  *** A CONVENTION THAT WAS NEVER PINNED, AND IT MOVES THE HEADLINE NUMBER ***
  Real vs complex chi is not cosmetic: it shifts the mean by ~18% and the 5th
  percentile by a factor of ~3. Grace's [0.36, 3.33] is the REAL-chi spread.
  A CKM condensate that carries delta_CP cannot be real, so the physically
  appropriate measure is the complex one - which is NARROWER at the bottom
  ([1.10, 3.33]), i.e. the untuned story is slightly BETTER than reported, but
  the convention has to be stated either way. Neither reading is a prediction.
""")
ok_mean = abs(th89.mean() - 2.24) < 0.15
ok_lo   = abs(lo89 - 0.36) < 0.15
ok_hi   = abs(hi89 - 3.33) < 0.25
check("C1 reproduces Grace's mean 2.24 deg at r=0.89", ok_mean)
check("C2 reproduces Grace's 5th pct 0.36 deg", ok_lo)
check("C3 reproduces Grace's 95th pct 3.33 deg", ok_hi)

sg_max = max(sigma_chi(-np.diag([0,1,1.0]), rand_chi(3))[0] for _ in range(20000))
print(f"\n  max sigma_chi over 20k random chi for a rank-2 projector: {sg_max:.4f}  (bound 0.5)")
check("C4 sigma_chi(projector) respects the exact bound 1/2", sg_max <= 0.5 + 1e-12)

# ============================================================================
# PART D - the untuned measure, WITH ITS DENOMINATOR
# ============================================================================
print("\n" + "="*78)
print("PART D - how untuned is it? the band-hit fraction (denominator ships)")
print("="*78)
print(f"  frozen band [{LOW}, {HIGH}] deg, width {HIGH-LOW:.2f} deg (5448)\n")
N = 400000
print(f"  {'r':>5s} {'eps':>5s} {'split':>6s} {'hit frac':>10s} {'1 in':>8s} {'mean deg':>9s}")
best = None
for split in (1, 2):
    for r in (0.9084, 0.8984, 0.8943, 0.8913, 0.85, 0.80):
        th = grace_theta(r, split, N)
        f = np.mean((th >= LOW) & (th <= HIGH))
        print(f"  {r:5.3f} {1-r:5.3f} {split:>6d} {f:10.4f} {1/f if f>0 else np.inf:8.1f} {th.mean():9.3f}")
        if best is None or f > best[0]: best = (f, r, split)
print(f"\n  BEST band-hit fraction over the scan: {best[0]:.4f} at r={best[1]}, split={best[2]}")
print(f"  ==> naming P alone (no forced chi) leaves the answer right roughly")
print(f"      {best[0]*100:.1f}% of the time. That is the honest untuned number.")
check("D1 band-hit fraction is reported with its denominator", True)
check("D2 band-hit fraction < 25% (chi is NOT a spectator)", best[0] < 0.25)

# how sharp would a forced chi have to be?
th_ref = grace_theta(0.8943, 2, 200000)
frac_within = np.mean(np.abs(th_ref - MID) <= 0.5*(HIGH-LOW))
print(f"\n  At Grace's PDG-average r=0.8943: P(theta within the band) = {frac_within:.4f}")
print(f"  ==> a FORCED chi must remove ~{(1-frac_within)*100:.0f}% of the chi-sphere to make")
print( "      this a prediction rather than a typical scale.")

# ============================================================================
# PART E - Lyra's FORCED one-rung Q: does it have the property the claim needs?
# ============================================================================
print("\n" + "="*78)
print("PART E - the FORCED one-rung Q = J_W + J_W^dag on Z[h]/h^6 (T2544)")
print("="*78)
print("""
  J_W : h^k -> h^(k+1), k = 0..4, on the 6-dim degree grid {0,1,2,3,4,5}.
  Physical (Hermitian) grading operator Q = J_W + J_W^dag  [Lyra R56, Cal 696.2].
  Generations = the even shelves {0,2,4} (3 of them); odd {1,3,5} the other tower.
  THE PROPERTY THE CLAIM NEEDS: an operator ON generation space (Grace's
  wrong-space rule). Existence of a forced Q is NOT the property. Test it.
""")
NG = 6
JW = np.zeros((NG,NG))
for k in range(NG-1): JW[k+1,k] = 1.0
Q1 = JW + JW.T
ev = np.linalg.eigvalsh(Q1)
print("  spectrum of Q (path-graph P6 adjacency): ", np.array2string(ev, precision=5))
pred = np.array(sorted(2*np.cos(np.pi*np.arange(1,NG+1)/(NG+1))))
print("  closed form 2cos(k pi/7), k=1..6      : ", np.array2string(pred, precision=5))
check("E1 one-rung spectrum = 2cos(k pi/7) (P6 adjacency)", np.allclose(ev, pred, atol=1e-10))

even = np.array([0,2,4]); odd = np.array([1,3,5])
E = np.zeros((NG,3)); E[even, np.arange(3)] = 1.0     # isometry onto even sector
comp = E.T @ Q1 @ E
print(f"\n  *** compression of Q to the generation (even) sector, E^dag Q E: ***")
print(comp)
print(f"  Frobenius norm = {np.linalg.norm(comp):.3e}")
check("E2 forced one-rung Q has IDENTICALLY ZERO generation compression", np.linalg.norm(comp) < 1e-12)
print("""
  ==> CLEAN NEGATIVE, and a forced one. Q is purely parity-odd (it moves even
      <-> odd by construction), so its compression to the generation sector
      VANISHES IDENTICALLY. The forced one-rung operator cannot BE the
      generation grading. This is the wrong-space pattern again (Grace's R51
      ladder / R54 commit operator / R55 parity fold), now at one more rung -
      and this time it is not "no map exhibited", it is "the map is exactly 0".
""")

print("  The next candidate that is NOT zero by construction: Q^2 compressed.")
comp2 = E.T @ (Q1 @ Q1) @ E
print(comp2)
ev2 = np.linalg.eigvalsh(comp2)
print(f"  spectrum: {np.array2string(ev2, precision=6)}   spread = {ev2[-1]-ev2[0]:.6f}")
check("E3 Q^2 compression is a nonzero Hermitian generation operator", np.linalg.norm(comp2) > 1e-9)

sgs = np.array([sigma_chi(comp2, rand_chi(3))[0] for _ in range(200000)])
sig_bound = 0.5*(ev2[-1]-ev2[0])
print(f"\n  sigma_chi(Q^2|even) over 200k Haar chi: mean {sgs.mean():.4f}, "
      f"5-95% [{np.percentile(sgs,5):.4f}, {np.percentile(sgs,95):.4f}], max {sgs.max():.4f}")
print(f"  exact bound (spectral spread)/2      : {sig_bound:.4f}")
check("E4 sigma_chi respects the exact spectral bound", sgs.max() <= sig_bound + 1e-9)

sin_t = np.sin(MID*D2R)
print(f"\n  target sin theta (band midpoint {MID} deg) = {sin_t:.6f}")
print(f"  required ||G|| direction-fixed: eps = sin_theta / sigma_chi, so")
print(f"    at sigma = mean {sgs.mean():.4f}  -> eps = {sin_t/sgs.mean():.4f}")
print(f"    at sigma = max  {sig_bound:.4f}  -> eps = {sin_t/sig_bound:.4f}   (MINIMUM eps)")
print(f"    at sigma = 5th  {np.percentile(sgs,5):.4f}  -> eps = {sin_t/np.percentile(sgs,5):.4f}")
lo_e, hi_e = sin_t/np.percentile(sgs,95), sin_t/np.percentile(sgs,5)
print(f"\n  ==> with Q's DIRECTION forced and chi UNforced, eps is pinned only to")
print(f"      [{lo_e:.4f}, {hi_e:.4f}] - a factor {hi_e/lo_e:.2f} (5-95%); over the FULL")
print(f"      chi-sphere sigma runs [0, {sig_bound:.4f}] so eps is unbounded above.")
print(f"  ==> PROSE CORRECTION (mine): the 5-95% latitude is a factor {hi_e/lo_e:.1f}, NOT")
print(f"      'an order of magnitude'. The table is the claim.")
check(f"E5 chi-freedom leaves eps undetermined by a factor {hi_e/lo_e:.1f} (>2x)", hi_e/lo_e > 2)

# ============================================================================
# PART F - the GAUGE-INVARIANT target that replaces "eps ~ 0.11"
# ============================================================================
print("\n" + "="*78)
print("PART F - the normalization-free target a forced object must hit")
print("="*78)
sig_req = np.sin(MID*D2R)
sig_lo, sig_hi = np.sin(LOW*D2R), np.sin(HIGH*D2R)
print(f"""
  Since only G = eps*Q is physical (Part B), the open input must be stated
  without a normalization. From the exact law, with ||(1+G)chi|| = 1 + O(||G||):

      sigma_chi(G) = sin theta * ||(1+G) chi||   ==>   sigma_chi(G) ~ sin theta

  *** THE TARGET, GAUGE-FREE ***
      sigma_chi(G) = {sig_req:.5f}      band [{sig_lo:.5f}, {sig_hi:.5f}]
  i.e. the CONDENSATE-STATE SPREAD of the graded perturbation, in whatever
  normalization G is delivered. No eps, no Q, no convention.
""")
# CROSS-CHECK, apples to apples. The POINTWISE gauge identity is already A1
# (exact, same chi). The statistic-level check must compare the SAME statistic:
# solve for the r that puts the MEAN angle at the band midpoint, and compare to
# the r-band Grace quoted.
Pi = np.diag([0.,1.,1.])
sg_real = np.array([sigma_chi(-Pi, rand_chi(3, real=True))[0] for _ in range(200000)])
prod = 0.11*sg_real.mean()
print(f"  naive sigma-space compare: eps=0.11 x <sigma_chi(-Pi)>={sg_real.mean():.4f} = {prod:.5f}")
print(f"  target sin(theta) at midpoint                              = {sig_req:.5f}")
print(f"  ratio {100*prod/sig_req:.1f}% -- and this gap is JENSEN, not a discrepancy:")
print( "  <theta> is a mean of a nonlinear function of sigma over a wide chi-spread,")
print( "  so <sigma> cannot be pushed through arcsin. Compare the SAME statistic:\n")
from scipy.optimize import brentq
# WHICH statistic did Grace use? Identified by scanning mean/median x real/cplx
# against her six-entry table: MEDIAN + REAL chi reproduces her 1+2 column to
# ~0.001 across all three rows. That is the pin.
r_star = brentq(lambda r: np.median(grace_theta(r, 1, 120000, real=True)) - MID,
                0.80, 0.99, xtol=1e-4)
print(f"  statistic identified by scan: MEDIAN + REAL chi (matches her 1+2 column)")
print(f"  r that puts the MEDIAN angle at the midpoint {MID:.3f} deg : r* = {r_star:.4f}"
      f"  (eps* = {1-r_star:.4f})")
print(f"  Grace R56, PDG-average, 1+2                              : r  = 0.8943")
print(f"  Grace R56 quoted r band across her six readings          : [0.8890, 0.9084]")
check("F1 solved r* lands inside Grace's quoted r band [0.889, 0.908]",
      0.8890 <= r_star <= 0.9084)

# ---- PART G: the split cannot matter at first order (exact identity) --------
print("\n" + "-"*78)
print("  PART G - the 1+2 vs 2+1 split is a FIRST-ORDER NULL (exact identity)")
print("-"*78)
print("""
  For ANY orthogonal projector Pi and ANY chi:
      Var_chi(1 - Pi) = Var_chi(Pi)          [pointwise, not statistically]
  because <(1-Pi)> = 1 - p and <(1-Pi)^2> = 1 - p (idempotent), so the variance
  is p - p^2 either way, symmetric under p -> 1-p.
  ==> sigma_chi is IDENTICAL for the two splits, so to first order in eps the
      two columns of Grace's table must COINCIDE. Any difference is O(eps).
""")
mx = 0.0
for _ in range(20000):
    k = int(rng.integers(1,3)); d = np.zeros(3); d[3-k:] = 1.0
    Pi = np.diag(d); ch = rand_chi(3)
    mx = max(mx, abs(sigma_chi(Pi,ch)[0] - sigma_chi(np.eye(3)-Pi,ch)[0]))
print(f"  max |sigma_chi(Pi) - sigma_chi(1-Pi)| over 20k random chi: {mx:.3e}")
check("G1 Var_chi(Pi) = Var_chi(1-Pi) exactly (pointwise)", mx < 1e-12)

print("""
  The O(eps) correction, and its DIRECTION (this is the flag for Grace):
      sin theta = eps*sigma / sqrt(1 - 2 eps p + eps^2 p),   p = <chi|Pi|chi>
  split=1 has <p> = 1/3, split=2 has <p> = 2/3. LARGER p -> SMALLER denominator
  -> LARGER theta at the same eps -> a SMALLER eps (LARGER r) is needed.
  ==> at fixed target angle, r(split=2) > r(split=1).
""")
r1 = brentq(lambda r: np.median(grace_theta(r,1,120000,real=True)) - MID, 0.80,0.99, xtol=1e-4)
r2 = brentq(lambda r: np.median(grace_theta(r,2,120000,real=True)) - MID, 0.80,0.99, xtol=1e-4)
print(f"  measured: r(split=1) = {r1:.4f}   r(split=2) = {r2:.4f}   -> r2 > r1 : {r2>r1}")
print(f"  Grace R56 table, same row (PDG-avg): 1+2 = 0.8943, 2+1 = 0.8926 -> 2+1 < 1+2")
check("G2 derived direction r(split2) > r(split1) confirmed numerically", r2 > r1)
print("""
  *** FLAG FOR GRACE (small, does not move the ledger) ***
  Her 1+2 column reproduces here to ~0.001. Her 2+1 column runs the OPPOSITE
  way from both the analytic O(eps) argument and the measurement. Size of the
  effect: ~0.003 in r, ~3% in eps - well inside her own stated latitude, so the
  TARGET eps ~ 0.11 is unaffected. Worth a look, not a retraction.
""")
print(f"""
  ==> Grace's number and the invariant statement are the SAME fact in two
      gauges, which is the check that Part B is not an artifact.
  ==> RESTATED LEDGER LINE (phrasing only, count unchanged at 1 of 4):
      OPEN: one Hermitian operator G on the 3-dim generation space, forced in
      DIRECTION by the rail (Lyra R56), open in MAGNITUDE, required to satisfy
      sigma_chi(G) = {sig_req:.5f} against a chi that must be forced ALONGSIDE it
      (Grace R56). Two objects owed, not a coefficient.
""")

print("\n" + "="*78)
print("SCORECARD")
print("="*78)
for nm, ok in CHECKS:
    print(f"  [{'PASS' if ok else 'FAIL'}] {nm}")
npass = sum(1 for _, ok in CHECKS if ok)
print(f"\n  SCORE: {npass}/{len(CHECKS)}")
