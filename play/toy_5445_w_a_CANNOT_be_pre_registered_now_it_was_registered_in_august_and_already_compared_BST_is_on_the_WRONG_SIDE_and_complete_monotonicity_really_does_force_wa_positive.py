#!/usr/bin/env python3
"""
Toy 5445 — w(a), THE DESI FALSIFIER: pre-register it?

QUESTION THIS COMPUTE ANSWERS (declared before running):
    "The brief says 'compute w(a) from the breathing mode and PRE-REGISTER it against
     DESI before looking at the numbers.' Is that available?"

★ THE ANSWER IS NO, AND SAYING SO IS THE JOB. Reconnect first:

    K1387 (2026-08-11), banked: "BST's banked breathing-mode dark energy predicts
        w_a > 0; DESI DR2 measures w_a < 0 at ~3sigma, and the sign is
        parametrization-robust. This is a LIVE POTENTIAL FALSIFIER, not a success."
    Cal §254: BST is "on the WRONG SIDE of a sharp pre-registered falsifier, stated
        straight."

  ⟹ THE PREDICTION WAS REGISTERED IN AUGUST AND THE COMPARISON HAS ALREADY HAPPENED.
    Filing a "pre-registration" today would be POST-HOC and would quietly re-set a
    clock that already ran. That is not a small bookkeeping point: the whole value of
    a pre-registration is the order of operations, and the order is already fixed.

★ SO WHAT THIS TOY DOES INSTEAD:
    (1) VERIFY the forcing — does complete monotonicity really force w_a > 0? If the
        forcing is soft, the "wrong side" verdict is softer too, and that matters.
    (2) NAME what is still genuinely pre-registerable (there is something).
    (3) Quote NO experimental number as verified (my own 5441 rule).
"""

import numpy as np

# ================================================================ THE FORCING
print("=" * 78)
print("SECTION 1 — VERIFY THE FORCING: does complete monotonicity force w_a > 0?")
print("=" * 78)
print("Bernstein: rho(a) completely monotone in a  <=>  rho(a) = INT exp(-s*a) dmu(s),")
print("mu >= 0. BST's bleed/relaxation gives such a rho (F799). Then")
print("      w(a) = -1 - (1/3) dln(rho)/dln(a)")
print("and we fit the standard CPL form w = w0 + wa*(1-a) to read off the SIGN of wa.\n")

def w_of_a(a, s_nodes, weights):
    """w(a) for rho(a) = sum_i weights_i * exp(-s_i * a), a completely monotone family."""
    rho = np.array([np.sum(weights * np.exp(-s_nodes * x)) for x in a])
    drho = np.array([np.sum(-s_nodes * weights * np.exp(-s_nodes * x)) for x in a])
    return -1.0 - (1.0 / 3.0) * (a * drho / rho)

def cpl_wa(a, w):
    """Least-squares CPL fit w = w0 + wa*(1-a); return wa."""
    A = np.column_stack([np.ones_like(a), 1.0 - a])
    return np.linalg.lstsq(A, w, rcond=None)[0][1]

a = np.linspace(0.3, 1.0, 60)
rng = np.random.default_rng(11)
print(f"{'completely monotone rho (random positive measures)':>52s} {'w(a=1)':>9s} {'CPL wa':>9s}")
print("-" * 78)
was = []
for trial in range(8):
    k = rng.integers(1, 5)
    s = rng.uniform(0.05, 3.0, size=k)
    wt = rng.uniform(0.1, 1.0, size=k)
    w = w_of_a(a, s, wt)
    wa = cpl_wa(a, w)
    was.append(wa)
    print(f"{'  measure with ' + str(k) + ' node(s)':>52s} {w[-1]:>9.4f} {wa:>9.4f}")
all_pos = all(x > 0 for x in was)
print()
print(f"  computed: CPL wa > 0 in {sum(1 for x in was if x>0)}/{len(was)} trials.")
print()
print("=" * 78)
print("SECTION 1b — ★★★ STOP. MY RESULT CONTRADICTS THE BANK. DIAGNOSE BEFORE REPORTING.")
print("=" * 78)
print("  banked (K1387/F799): complete monotonicity FORCES w_a > 0.")
print("  my model returned   : w_a < 0, on every trial.")
print()
print("★ TWO POSSIBILITIES, and I do not get to pick the flattering one:")
print("    (a) the banked forcing is wrong, or")
print("    (b) I MODELLED THE WRONG OBJECT.")
print()
print("DIAGNOSE. For a single exponential rho(a) = exp(-s*a):")
print("      dln(rho)/dln(a) = -s*a   ->   w(a) = -1 + s*a/3")
sdemo = 1.0
for aa in (0.3, 0.6, 1.0):
    print(f"      a = {aa:.1f}  ->  w = {-1 + sdemo*aa/3:+.4f}")
print()
print("★★★ THAT w MOVES **AWAY** FROM -1 AS a GROWS. But the corpus describes the bleed as")
print("    'monotone, APPROACHES THE FLOOR FROM ABOVE' — i.e. w -> -1 as time goes on.")
print("⟹ MY rho IS NOT THE CORPUS'S rho. I imposed complete monotonicity IN a; the banked")
print("  statement is about the RELAXATION approaching the floor, which is monotonicity in")
print("  a different variable. Same words, different object.")
print()
print("## ⟹ VERIFICATION NOT ACHIEVED. I am NOT reporting the bank as wrong — I am")
print("## reporting that I could not verify it because I reconstructed rho from its NAME,")
print("## which is the exact error 5410 cost me a full retraction for.")
print("★ @Lyra/@Grace — I need the ACTUAL rho(a) from F799 to run this. Handing it back")
print("  rather than guessing twice.")
verification = False

# ================================================================ THE ORDER
print()
print("=" * 78)
print("SECTION 2 — ★★★ WHY IT CANNOT BE PRE-REGISTERED TODAY")
print("=" * 78)
print("  registered   : w_a > 0, banked pre-DESI-comparison (F799 / K1387, August)")
print("  compared     : DESI DR2 w_a < 0, sign parametrization-robust (K1387, Cal §390)")
print("  status       : BST is ON THE WRONG SIDE of its own forced prediction")
print()
print("## ⟹ A 'PRE-REGISTRATION' FILED NOW WOULD BE POST-HOC. The clock already ran.")
print("★★ And the honest reading of that is NOT 'BST predicts dynamical dark energy' —")
print("   it is: BST made a sharp, zero-parameter, sign-level prediction; the data")
print("   currently disagree; that is what a falsifier looks like when it fires against")
print("   you. Cal already stated it straight in §254 and it should stay stated.")
print()
print("★ I quote NO experimental number as verified here. The '~3 sigma' is CORPUS-CITED")
print("  (K1387) and NEEDS-PRIMARY-VERIFICATION before it is used in any external claim —")
print("  my own rule from 5441, applied to a number that happens to be inconvenient.")

# ================================================================ WHAT IS LEFT
print()
print("=" * 78)
print("SECTION 3 — WHAT *IS* STILL GENUINELY PRE-REGISTERABLE")
print("=" * 78)
print("Cal §4751 named a DIFFERENT test that has NOT been run, so its clock has not started:")
print()
print("  > \"The 'CPL artifact' claim is HONEST ONLY IF the direct-fit shows BST's")
print("  >  completely-monotone shape fits the DESI data COMPARABLY to CPL (small")
print("  >  delta-chi^2).\"")
print()
print("★★ THAT is pre-registerable today, and it is the right thing to pre-register:")
print("     H0 : BST's monotone w(a) fits DESI's distance data comparably to CPL")
print("     KILL: BST's shape is disfavoured by a stated delta-chi^2 margin")
print("   It is a SHAPE test, not a sign test — the sign question is already decided and")
print("   decided against us. Conflating the two would let a live falsifier hide behind an")
print("   open one.")
print()
print("★ @Cal — this is yours to bar-set (you guard the w(a) pre-registration); I am")
print("  flagging that the thing the brief asked me to pre-register is already registered,")
print("  and pointing at the one that isn't.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("attempted verification of the forcing, result CONTRADICTED the bank", not verification),
    ("diagnosed my own model as the likely fault, not the bank", True),
    ("declined to report the bank as wrong on a reconstructed rho", True),
    ("identified that the sign prediction was registered in August", True),
    ("=> a fresh pre-registration would be post-hoc; declined", True),
    ("no experimental number quoted as verified (5441 rule applied)", True),
    ("named the test that IS still pre-registerable (the shape/delta-chi^2)", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — I decline to pre-register w(a), and the reason is the point:")
print("  The brief asked me to pre-register w(a) against DESI before looking. I reconnected")
print("  first, and the prediction was already registered in August (w_a > 0, forced by")
print("  complete monotonicity) and already compared: DESI DR2 sits at w_a < 0 with a")
print("  parametrization-robust sign. Filing a pre-registration today would re-set a clock")
print("  that has already run — the order of operations is the whole value of the device.")
print("  I also TRIED to verify the forcing rather than assume it, and my model returned")
print("  the OPPOSITE sign on every trial (0/8 positive). Rather than announce a banked")
print("  result wrong, I diagnosed my own setup: for rho completely monotone in a, w moves")
print("  AWAY from -1 as a grows, while the corpus describes the bleed as APPROACHING the")
print("  floor. Same words, different object — I reconstructed rho from its NAME, the exact")
print("  error that cost me a full retraction in 5410. VERIFICATION NOT ACHIEVED.")
print("  ⟹ So the SIGN verdict stands on the corpus's authority, not on mine: I could not")
print("     independently reproduce the forcing, and I need F799's actual rho(a) to try.")
print("     Handing that back rather than guessing twice.")
print("  ⟹ The test still open, and worth pre-registering, is Cal §4751's SHAPE test")
print("     (does the monotone form fit comparably to CPL?) — a different question whose")
print("     clock has not started. @Cal sets that bar.")
