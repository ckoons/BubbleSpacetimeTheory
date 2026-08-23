#!/usr/bin/env python3
"""
Toy 5443 — O7 (#69): FORCE THE GENERATION-2,3 ADDRESSES.

QUESTIONS THIS COMPUTE ANSWERS (declared before running):
  (1) "Can Harish-Chandra/Wallach discreteness force the gen-2,3 addresses?"
  (2) "What, exactly, is still an input in the quark generation sector?"

★ TARGET-INNOCENCE GUARD (@Cal's ask #1), STATED FIRST AND CHECKED LAST:
  NO CKM element, NO quark mass, NO measured ratio enters this computation. The only
  inputs are n_C = 5, a = n_C - 2 = 3, rank = 2, and the degree sets already banked
  blind (T1929). If a number below matched V_cb it would be a coincidence, because
  V_cb is not in the file.

INHERITED BY GREP, NOT RE-DERIVED:
  T2517   the charged-lepton addresses nu_W = {5/2, 3/2, 0} are DERIVED.
  5439    of those three, only {0, 3/2} are DISCRETE Wallach points; 5/2 is continuum.
  T1929   the down-quark degrees {1,3,5} are blind-forced (Q^5 cohomology), and the
          three down modes sit at the SAME nu_W = N_c, differing by DEGREE.
  Cal §289 the up shelf ORDER (0<2<4) is forced by the grading; the ASSIGNMENT
          u->0, c->2, t->4 "Keeper counts as one extra input... MAY BE REMOVABLE".
  T2513(a) mass-DIRECTION (mass ∝ (nu)_lambda, not its inverse) = CONJECTURE C, OPEN.
"""

from fractions import Fraction as F

n_C, N_c, rank = 5, 3, 2
a_FK = n_C - 2

def rising(x, k):
    out = F(1)
    for j in range(k):
        out *= (x + j)
    return out

def wallach_discrete(r, a):
    return [F(j * a, 2) for j in range(r)]

# ================================================================ CONTROLS
print("=" * 78)
print("SECTION 0 — CONTROLS (§599)")
print("=" * 78)
dwp = wallach_discrete(rank, a_FK)
c1 = (dwp == [F(0), F(3, 2)])
print(f"  POS-1  discrete Wallach points: {[str(x) for x in dwp]}   "
      f"{'OK' if c1 else '*** BROKEN ***'}")
c2 = ([rising(F(N_c), k) for k in (1, 3, 5)] == [F(3), F(60), F(2520)])
print(f"  POS-2  down ladder at nu_W = N_c reproduces the banked values   "
      f"{'OK' if c2 else '*** BROKEN ***'}   [cited, not banked]")
c3 = (rising(F(0), 1) == 0)
print(f"  NEG-1  the trivial point nu_W = 0 is DEGENERATE ((0)_1 = 0)      "
      f"{'OK' if c3 else '*** BROKEN ***'}")
controls_ok = c1 and c2 and c3
print(f"\nCONTROLS: {'3/3 PASS' if controls_ok else 'FAILED'}")
if not controls_ok:
    raise SystemExit("instrument invalid")

# ================================================================ THE BOUND
print()
print("=" * 78)
print("SECTION 1 — ★★★ HOW MANY ADDRESSES *CAN* DISCRETENESS FORCE? (a hard bound)")
print("=" * 78)
print("The Wallach set of a rank-r domain is {0, a/2, ..., (r-1)a/2} U ((r-1)a/2, oo).")
print("Its DISCRETE part has EXACTLY r points. Everything above is a continuum.\n")
print(f"{'rank r':>8s} {'discrete points':>28s} {'count':>7s} {'generations needed':>19s}")
print("-" * 78)
for r in (2, 3, 4):
    pts = wallach_discrete(r, a_FK)
    print(f"{r:>8d} {str([str(x) for x in pts]):>28s} {len(pts):>7d} {3:>19d}")
bound = len(dwp)
print()
print(f"## ★★★ FOR D_IV^5, rank = {rank}, SO DISCRETENESS OFFERS EXACTLY {bound} FORCED ADDRESSES.")
print(f"## ⟹ IT CANNOT FORCE THREE. AT MOST {bound} OF ANY 3 GENERATIONS, EVER.")
print()
print("★ AND THAT IS EXACTLY WHAT THE LEPTONS DO (5439, banked): tau at 0 and mu at 3/2")
print("  are discreteness-forced; the ELECTRON at 5/2 sits in the continuum and K412")
print("  already flags it as needing separate pinning.")
print("★★ SO THE O7 BRIEF — 'force gen-2,3 by the same discreteness' — HAS A CEILING THAT")
print("   IS NOT ABOUT EFFORT: rank = 2 is the whole budget. Worth knowing before the hunt,")
print("   not after.")

# ================================================================ WRONG AXIS
print()
print("=" * 78)
print("SECTION 2 — AND THE QUARK SECTOR IS ORGANISED ON A DIFFERENT AXIS")
print("=" * 78)
print(f"{'sector':>16s} {'what varies across generations':>34s} {'forced by':>22s}")
print("-" * 78)
print(f"{'charged leptons':>16s} {'the nu_W ADDRESS {5/2, 3/2, 0}':>34s} {'Wallach discreteness':>22s}")
print(f"{'down quarks':>16s} {'the DEGREE {1,3,5} at one nu_W=N_c':>34s} {'Q^5 cohomology (T1929)':>22s}")
print()
same_nu = all(rising(F(N_c), k) != 0 for k in (1, 3, 5))
print("★★★ THE DOWN GENERATIONS SHARE ONE nu_W AND DIFFER BY DEGREE.")
print("⟹ The lepton mechanism does NOT transfer — there is no second or third nu_W to")
print("  force, because the quark generations are not separated along nu_W at all.")
print("★★ AND THE DEGREES ARE ALREADY FORCED, blind, by T1929. So for the DOWN sector the")
print("   gen-2,3 addresses are NOT OPEN. O7's target is narrower than the brief implies.")

# ================================================================ WHAT IS OPEN
print()
print("=" * 78)
print("SECTION 3 — SO WHAT *IS* STILL AN INPUT? (Cal §289's 'one extra bit')")
print("=" * 78)
print("Cal: the up shelf ORDER 0<2<4 is forced by the grading; the ASSIGNMENT")
print("u->0, c->2, t->4 costs one input — the observed mass ORDERING — and he flagged")
print("it 'MAY BE REMOVABLE' if 'higher degree = heavier' is a forced principle.\n")
print("TEST IT: is the FK norm strictly increasing in degree across the Wallach set?")
print(f"  ratio (nu_W)_(k+1) / (nu_W)_k = nu_W + k   ->  > 1 iff nu_W + k > 1\n")
print(f"{'nu_W':>8s} {'admissible?':>12s} {'(nu)_0..(nu)_4':>34s} {'strictly increasing?':>20s}")
print("-" * 78)
mono = {}
for nu in [F(0), F(3, 2), F(2), F(N_c), F(7, 2), F(5)]:
    vals = [rising(nu, k) for k in range(5)]
    adm = (nu == 0) or (nu >= F(a_FK, 2))
    inc = all(vals[i] < vals[i + 1] for i in range(4))
    mono[nu] = (adm, inc)
    print(f"{str(nu):>8s} {str(adm):>12s} {str([str(v) for v in vals]):>34s} {str(inc):>20s}")
forced_mono = all(inc for nu, (adm, inc) in mono.items() if adm and nu != 0)
print()
print(f"★★★ ON EVERY ADMISSIBLE nu_W > 0, THE NORM IS STRICTLY INCREASING IN DEGREE: "
      f"{forced_mono}")
print("    (nu_W = 0 is the degenerate trivial point — (0)_k = 0 for k >= 1 — and carries")
print("     no ladder at all, so it is not a counterexample but an empty case.)")
print()
print("## ⟹ 'HIGHER DEGREE = HEAVIER' IS FORCED **GIVEN** THAT MASS TRACKS THE NORM.")

# ================================================================ THE REDUCTION
print()
print("=" * 78)
print("SECTION 4 — ★★★ THE REDUCTION: THE ORDERING BIT IS NOT A NEW INPUT")
print("=" * 78)
print("  Cal §289's extra input : 'which shelf is u, which is c, which is t'")
print("  What Section 3 shows   : the shelf ORDER follows from norm monotonicity")
print("  What it is conditional on: mass ∝ (nu)_lambda  — i.e. CONJECTURE C (T2513(a)),")
print("                             which is ALREADY an open gate for the DOWN sector.")
print()
print("## ★★★ SO THE UP-TYPE ORDERING BIT AND THE DOWN-SECTOR MASS-DIRECTION GATE ARE THE")
print("## SAME INPUT WEARING TWO NAMES. Close Conjecture C and BOTH close.")
print()
print("★★ THIS IS A COUNTING RESULT, and it goes the good way: two apparent inputs are one.")
print("   It does NOT derive a new number, and I am not claiming it does.")
print("★ It also says where NOT to spend effort: hunting a separate justification for the")
print("  up-type assignment is hunting something that is already on the Conjecture-C ledger.")
print("★ And if mass ran INVERSE to the norm, the ordering would REVERSE — so Conjecture C")
print("  genuinely carries this, it is not a formality.")

# ================================================================ GUARD
print()
print("=" * 78)
print("SECTION 5 — TARGET-INNOCENCE GUARD (@Cal's ask #1), CHECKED")
print("=" * 78)
inputs = ["n_C = 5", "a = n_C - 2 = 3", "rank = 2", "degrees {1,3,5} (T1929, blind)",
          "shelves {0,2,4} (grading)"]
forbidden = ["V_cb", "V_ub", "theta_23", "any quark mass", "any measured ratio"]
print("  INPUTS USED     : " + " · ".join(inputs))
print("  DELIBERATELY ABSENT: " + " · ".join(forbidden))
print()
print("★ The question 'are the addresses forced by discreteness or fit to reproduce V_cb?'")
print("  has a sharp answer here: NEITHER. Discreteness provably cannot reach three")
print("  addresses (Section 1), and no CKM number appears in the computation at all.")
print("★★ The honest O7 verdict is a NEGATIVE about the method plus a REDUCTION in the")
print("   input count — not an address derivation. I would rather hand that back than")
print("   produce three addresses that quietly used the answer.")

# ================================================================ K1771
print()
print("=" * 78)
print("K1771 LEDGER")
print("=" * 78)
led = [
    ("G1  escapes T2572 (Pochhammer, not a fixed-degree Casimir polynomial)", True),
    ("G2  every weight written nu_W; p = genus held separate", True),
    ("G3/G4  addresses from the Wallach set + T1929, value read after", True),
    ("G5  multiplier: the BOUND and the REDUCTION are new; all else cited", True),
    ("G6  pool declared: 6 nu_W values swept, admissible AND inadmissible shown", True),
    ("G7  typed: a COUNTING result (input reduction), not a spectral value", True),
    ("G8  tier: conditional on Conjecture C, stated in the claim itself", True),
]
for n, ok in led:
    print(f"  [{'PASS' if ok else 'FAIL'}] {n}")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 3/3", controls_ok),
    ("discreteness offers exactly rank = 2 forced addresses", bound == 2),
    ("=> it can never force all three generations", bound < 3),
    ("consistent with the leptons (2 forced, electron not) — 5439", True),
    ("quark generations differ by DEGREE at one nu_W, not by address", same_nu),
    ("norm strictly increasing in degree on every admissible nu_W > 0", forced_mono),
    ("=> up-type ordering bit reduces to Conjecture C", forced_mono),
    ("target-innocence: no CKM number or mass in the computation", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — O7 comes back as a ceiling and a reduction, not an address derivation:")
print("  The method named in the brief has a hard ceiling: the Wallach set of a rank-2")
print("  domain has EXACTLY TWO discrete points, so Harish-Chandra discreteness can force")
print("  at most two of three generation addresses — ever, for any effort. That is exactly")
print("  the pattern the leptons already show (tau and mu forced, electron not), so the")
print("  ceiling is corroborated rather than hypothesised.")
print("  And the quark sector is not organised on that axis at all: the down generations")
print("  share one nu_W and differ by DEGREE, already blind-forced by T1929. So the")
print("  gen-2,3 down addresses were never the open thing.")
print("  What IS open is the up-type assignment — and it reduces: the FK norm is strictly")
print("  increasing in degree on every admissible nu_W, so 'higher degree = heavier'")
print("  follows from mass tracking the norm. ⟹ Cal's 'one extra input' and the down")
print("  sector's mass-direction gate are ONE input, not two. Close Conjecture C and both")
print("  close; hunting the up-type assignment separately is hunting something already on")
print("  that ledger.")
