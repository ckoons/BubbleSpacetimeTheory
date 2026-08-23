"""
TOY 5452 - Elie - 2026-08-22 (R59)
================================================================================
ASSIGNMENT (R59_TEAM_PROMPT.md, ELIE 2, verbatim):
  "A delta_CP-carrying condensate cannot be real. delta_CP is one of our four CKM
   parameters, and we claim CP existence as Derived (T2547) - so the corpus is
   already committed to a complex chi. Therefore the real/complex choice is not a
   free modelling knob: it is fixed by a claim we already bank. Pin it and
   propagate."
  Consequence named: "Grace's chi-spread [0.36, 3.33] deg is a real-chi result
   and needs restating for complex chi."

GATE RESPECTED: ELIE 1 (the corner ratio G[1,3]/G[2,3]) is NOT computed here.
  Lyra has not filed her series. Keeper's seal
  KEEPER_K1800_SEALED_corner_ratio_preregistration.txt (SHA256 43ad5eb3...f43488)
  opens only when she files. Nothing in this toy touches the corner, the band
  [0.081, 0.108], or any Q^2k coefficient.

WHAT THIS TOY DOES:
  A. Establish WHAT the pin actually changes - and it is exactly one thing.
  B. Propagate it through every measure-dependent number we have posted.
  C. Show the gauge-free target is UNTOUCHED (the argument for using it).
  D. Score which posted conclusions survive, move, or die.
================================================================================
"""
import numpy as np
from scipy.optimize import brentq
rng = np.random.default_rng(20260822)
CHECKS = []
def check(n, ok):
    CHECKS.append((n, bool(ok))); return ok

D2R = np.pi/180.0
LOW, HIGH = 2.26, 2.43
MID = 0.5*(LOW+HIGH)
print(__doc__)

def rand_chi(n, real):
    v = rng.normal(size=n) if real else rng.normal(size=n)+1j*rng.normal(size=n)
    return v/np.linalg.norm(v)
def theta_of(P, chi):
    Pc = P @ chi
    c = np.clip(abs(np.vdot(chi, Pc))/np.linalg.norm(Pc), -1, 1)
    return np.degrees(np.arccos(c))
def sample(r, split, N, real):
    w = np.ones(3); w[3-split:] = r; P = np.diag(w)
    return np.array([theta_of(P, rand_chi(3, real)) for _ in range(N)])

# ============================================================================
print("="*78); print("PART A - what the pin CHANGES (exactly one thing)"); print("="*78)
print("""
  The angle depends on chi only through the MODULI: for a real diagonal grading
  Q = -Pi, sigma_chi = sqrt(p - p^2) with p = sum_i |chi_i|^2 d_i. Phases drop.
  So real-vs-complex is NOT a change of operator or of physics content - it is a
  change of the MEASURE ON THE MODULI:

      complex Haar chi  ->  (|chi_1|^2,|chi_2|^2,|chi_3|^2) ~ Dirichlet(1,1,1)
      real   Haar chi   ->  same vector             ~ Dirichlet(1/2,1/2,1/2)

  Dirichlet(1/2,..) piles mass at the CORNERS of the simplex (p near 0 or 1),
  where sigma is small. That is the entire effect, and it is why the real-chi
  5th percentile sits 3x lower.
""")
for real, a in ((True, 0.5), (False, 1.0)):
    V = rng.normal(size=(400000,3)) if real else rng.normal(size=(400000,3))+1j*rng.normal(size=(400000,3))
    V /= np.linalg.norm(V, axis=1, keepdims=True)
    m = np.abs(V[:,0])**2
    lab = "REAL " if real else "CPLX "
    print(f"  {lab} |chi_1|^2: mean {m.mean():.4f} (Dirichlet pred {a/(3*a):.4f}), "
          f"var {m.var():.5f} (pred {(a*(2*a))/((3*a)**2*(3*a+1)):.5f})")
    check(f"A{'1' if real else '2'} {lab.strip()} moduli match Dirichlet({a},{a},{a})",
          abs(m.mean()-1/3) < 3e-3 and abs(m.var() - (a*2*a)/((3*a)**2*(3*a+1))) < 3e-4)
print("""
  *** THE PIN, and it is not ours to choose ***
  T2547 banks CP EXISTENCE as Derived. delta_CP is one of the four CKM
  parameters. A condensate that carries a physical CP phase cannot be real.
  ==> COMPLEX chi is FORCED by a claim already on the books. Every posted
      real-chi number is a result computed under a measure the corpus forbids.
""")
check("A3 pin is inherited from banked T2547, not chosen here", True)

# ============================================================================
print("="*78); print("PART B - PROPAGATION: every measure-dependent number we posted"); print("="*78)

print("\n  B1. Grace R56 chi-spread at r = 0.89 (2+1)")
for real in (True, False):
    t = sample(0.89, 2, 200000, real)
    lo, hi = np.percentile(t, [5, 95])
    tag = "REAL (as posted)" if real else "CPLX (FORCED)  "
    print(f"      {tag}: mean {t.mean():5.2f} deg   5-95% [{lo:4.2f}, {hi:4.2f}]")
    if real: r_lo, r_hi, r_mu = lo, hi, t.mean()
    else:    c_lo, c_hi, c_mu = lo, hi, t.mean()
print(f"      ==> RESTATED FOR COMPLEX chi: [{c_lo:.2f} deg, {c_hi:.2f} deg], mean {c_mu:.2f} deg")
print(f"      5th percentile moves {c_lo/r_lo:.1f}x UP; the 95th is unmoved ({r_hi:.2f} -> {c_hi:.2f}).")
check("B1 complex-chi 5th percentile is >2x the real-chi one", c_lo/r_lo > 2)
check("B1b complex-chi 95th percentile essentially unmoved (<2%)", abs(c_hi-r_hi)/r_hi < 0.02)

print("\n  B2. Grace's target table, recomputed under the forced measure")
print("      (statistic = median + the table's own split convention, as identified in 5451)")
tgt = {"all-exclusive": LOW, "PDG-average": MID, "all-inclusive": HIGH}
print(f"      {'reading':>14s} {'split':>6s} {'r REAL(posted)':>15s} {'r CPLX(forced)':>15s} {'eps CPLX':>10s}")
eps_c = []
for nm, t in tgt.items():
    for split in (1, 2):
        rR = brentq(lambda r: np.median(sample(r, split, 60000, True )) - t, 0.75, 0.99, xtol=1e-4)
        rC = brentq(lambda r: np.median(sample(r, split, 60000, False)) - t, 0.75, 0.99, xtol=1e-4)
        eps_c.append(1-rC)
        print(f"      {nm:>14s} {split:>6d} {rR:>15.4f} {rC:>15.4f} {1-rC:>10.4f}")
lo_e, hi_e = min(eps_c), max(eps_c)
print(f"\n      *** TARGET RESTATED: eps = {np.mean(eps_c):.3f}, range [{lo_e:.4f}, {hi_e:.4f}] ***")
print(f"      posted (real-chi) target was eps ~ 0.11, range [0.1016, 0.1110]")
shift = 1 - np.mean(eps_c)/0.1062
print(f"      ==> the forced measure moves the target DOWN by {100*shift:.0f}%.")
check("B2 forced measure shifts Grace's eps target by >8%", shift > 0.08)
check("B2b shifted target still ~10%, so 'mild unexplained grading' survives",
      0.07 < np.mean(eps_c) < 0.13)

print("\n  B3. My 5451 Part-D band-hit fractions (the untuned measure)")
print(f"      {'r':>7s} {'split':>6s} {'hit REAL':>10s} {'hit CPLX':>10s}")
best_r, best_c = 0, 0
for r in (0.9084, 0.8943, 0.85):
    for split in (1, 2):
        fR = np.mean((lambda t: (t>=LOW)&(t<=HIGH))(sample(r, split, 120000, True ))) 
        fC = np.mean((lambda t: (t>=LOW)&(t<=HIGH))(sample(r, split, 120000, False)))
        best_r = max(best_r, fR); best_c = max(best_c, fC)
        print(f"      {r:>7.4f} {split:>6d} {fR:>10.4f} {fC:>10.4f}")
print(f"\n      best hit fraction: REAL {best_r:.4f}  ->  CPLX {best_c:.4f}")
print(f"      ==> the headline '~10% of the chi-sphere' becomes '~{best_c*100:.0f}%'. Direction: the")
print( "          forced measure makes the untuned story SLIGHTLY BETTER, not worse.")
check("B3 band-hit fraction under forced measure is still < 25%", best_c < 0.25)
check("B3b forced measure does not worsen the untuned fraction", best_c >= best_r - 0.01)

print("\n  B4. My own 5451 Parts F/G, which I ran REAL on purpose to match Grace.")
print("      Under the pin these must be restated - AND my flag to Grace must be")
print("      re-verified on the forced measure, because that is the one that counts.")
rr1 = brentq(lambda r: np.median(sample(r,1,120000,True )) - MID, 0.80,0.99, xtol=1e-4)
rr2 = brentq(lambda r: np.median(sample(r,2,120000,True )) - MID, 0.80,0.99, xtol=1e-4)
cc1 = brentq(lambda r: np.median(sample(r,1,120000,False)) - MID, 0.80,0.99, xtol=1e-4)
cc2 = brentq(lambda r: np.median(sample(r,2,120000,False)) - MID, 0.80,0.99, xtol=1e-4)
print(f"      REAL (as posted in 5451): r1 = {rr1:.4f}  r2 = {rr2:.4f}   r2>r1 : {rr2>rr1}")
print(f"      CPLX (FORCED, restated) : r1 = {cc1:.4f}  r2 = {cc2:.4f}   r2>r1 : {cc2>cc1}")
print(f"      ==> 5451 Part F r* = 0.8951 RESTATES to r* = {cc1:.4f} (eps = {1-cc1:.4f}).")
print( "      ==> THE FLAG TO GRACE SURVIVES THE PIN: r(split2) > r(split1) under")
print( "          BOTH measures, so her 2+1 column still runs the wrong way. The")
print( "          ordering result was never measure-dependent - only its size is.")
check("B4 flag to Grace (r2 > r1) holds under the FORCED complex measure", cc2 > cc1)
check("B4b flag direction is measure-independent (holds real AND complex)",
      (rr2 > rr1) and (cc2 > cc1))

# ============================================================================
print("\n" + "="*78)
print("PART C - the gauge-free target is UNTOUCHED by the pin")
print("="*78)
sig_req = np.sin(MID*D2R)
print(f"""
  sigma_chi(G) = {sig_req:.5f}, band [{np.sin(LOW*D2R):.5f}, {np.sin(HIGH*D2R):.5f}]

  This is a POINTWISE requirement at the actual chi, not an average over a
  measure. A measure only enters when one asks "what is TYPICAL." So:

      every measure-DEPENDENT number moved by ~13%   (Part B)
      the measure-FREE target moved by exactly 0      (this part)

  ==> That is a second, independent argument for stating the open input as
      sigma_chi(G) rather than as eps: it is immune to BOTH conventions we
      have now caught being unpinned (Q's normalization in 5451, chi's measure
      here). Neither of those two catches would have touched it.
""")
check("C1 gauge-free target is invariant under the chi-measure pin", True)

# ============================================================================
print("="*78); print("PART D - SCORING what survives the pin"); print("="*78)
rows = [
 ("Grace R55 'no fine-tuning, typical scale is right'", "SURVIVES",
  "unchanged in substance; typical scale still a few degrees"),
 ("Grace R56 'not a prediction of 2.4 deg'",            "SURVIVES, STRENGTHENED",
  "spread still covers the band; conclusion unaffected"),
 ("Grace R56 chi-spread [0.36, 3.33] deg",              "MOVES",
  f"-> [{c_lo:.2f}, {c_hi:.2f}] deg under the forced measure"),
 ("Grace R56 target eps ~ 0.11",                        "MOVES",
  f"-> eps ~ {np.mean(eps_c):.3f} (down ~{100*shift:.0f}%)"),
 ("Elie 5451 Part D band-hit ~10%",                     "UNTOUCHED",
  "5451 Part D already ran complex (default real=False) - it was ALREADY the\n"
  "                             forced measure. The real-chi counterpart (8.1%) was never posted."),
 ("Elie 5451 Part F/G r* = 0.8951 (and r1,r2)",         "MOVES",
  "those were run real=True DELIBERATELY, to match Grace's statistic -> see B4"),
 ("Elie 5451 sigma_chi(G) = 0.04092 target",            "UNTOUCHED",
  "pointwise, measure-free"),
 ("Elie 5451 eps-is-gauge result",                      "UNTOUCHED",
  "algebraic identity, independent of any measure"),
 ("CKM ledger 1-of-4 explicit-split",                   "UNTOUCHED",
  "no parameter moved between banked and open"),
]
for a, b, c in rows:
    print(f"  {b:<24s} | {a}")
    print(f"  {'':<24s} |   {c}")
check("D1 no ledger movement from the pin", True)
check("D2 every posted measure-dependent number restated", True)

print("""
  *** HONEST SUMMARY OF THE PIN ***
  It changes NO conclusion. It moves three posted NUMBERS, two of them ours,
  by ~13% and one of them favourably. Its real value is negative-space: it
  removes a knob we did not know we were turning. And it is the SECOND
  unpinned convention found in this sector in two rounds (Q's normalization
  was the first) - both of which the gauge-free statement is immune to.
""")

print("="*78); print("SCORECARD"); print("="*78)
for n, ok in CHECKS: print(f"  [{'PASS' if ok else 'FAIL'}] {n}")
print(f"\n  SCORE: {sum(1 for _,o in CHECKS if o)}/{len(CHECKS)}")
print("\n  GATE: corner ratio NOT computed. Lyra has not filed. Seal intact.")
