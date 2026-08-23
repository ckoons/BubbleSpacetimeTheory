#!/usr/bin/env python3
"""
Toy 5447 — w(a): RUN THE FORCING AGAINST THE HANDED-DOWN OBJECT, AND ASK IF A IS DERIVED.

QUESTIONS THIS COMPUTE ANSWERS (declared before running):
  (1) "Run the forcing against w(a) = -1 + A*a^6 (F799, rate lambda_1 = C_2 = 6)."
  (2) "Say whether the amplitude A is derived or fitted."

★ (1) COMES BACK WITH A PROBLEM, AND IT IS NOT MINE TO RESOLVE BY GUESSING.
  The form as transmitted CONTRADICTS F799's own qualitative statement. Grace's
  pre-registration note (grace_A1_radial_DH_nonCPL_discriminator_prereg_2026-08-08),
  quoting F799 directly:

      "BST predicts w(a) relaxing to -1 FROM ABOVE (w_a > 0, completely-monotone,
       NO crossing -- F799 double-derived)."

  "Relaxing to -1 from above" means w DECREASES toward -1 as the universe expands.
  But w(a) = -1 + A*a^6 with A > 0 INCREASES with a -- it moves AWAY from -1.
  ⟹ the transmitted form and the banked description cannot both be right.

★ THIS IS THE SECOND TIME A RELAYED DESCRIPTION OF THIS OBJECT HAS FLIPPED MY SIGN.
  Last round I reconstructed rho from its name and got w_a < 0; I was told the object
  was -1 + A*a^6. That form ALSO gives w_a < 0. So the correction did not fix the sign,
  and I am not going to guess a third time -- I am going to show exactly which character
  decides it and ask for F799 primary.
"""

import numpy as np

# ================================================================ THE INSTRUMENT
def cpl_fit(a, w):
    """Least-squares CPL: w = w0 + wa*(1-a). Returns (w0, wa)."""
    A = np.column_stack([np.ones_like(a), 1.0 - a])
    return tuple(np.linalg.lstsq(A, w, rcond=None)[0])

a = np.linspace(0.3, 1.0, 200)          # the range DESI actually constrains

print("=" * 78)
print("SECTION 0 — CONTROLS (§599): can the CPL fitter return BOTH signs?")
print("=" * 78)
w_up = -1 + 0.2 * a                      # w rises toward today  -> expect wa < 0
w_dn = -1 + 0.2 * (1 - a)                # w falls toward today  -> expect wa > 0
_, wa_up = cpl_fit(a, w_up)
_, wa_dn = cpl_fit(a, w_dn)
c1, c2 = wa_up < 0, wa_dn > 0
print(f"  POS-1  w increasing with a  -> wa = {wa_up:+.4f}  (expect < 0)   {'OK' if c1 else '*** BROKEN ***'}")
print(f"  POS-2  w decreasing with a  -> wa = {wa_dn:+.4f}  (expect > 0)   {'OK' if c2 else '*** BROKEN ***'}")
controls_ok = c1 and c2
print(f"\nCONTROLS: {'2/2 PASS — the fitter is not sign-biased.' if controls_ok else 'FAILED'}")
if not controls_ok:
    raise SystemExit("instrument invalid")

# ================================================================ THE FORM AS GIVEN
print()
print("=" * 78)
print("SECTION 1 — THE FORM AS TRANSMITTED:  w(a) = -1 + A * a^6")
print("=" * 78)
print(f"{'A':>10s} {'w(a=0.3)':>11s} {'w(a=1)':>10s} {'CPL wa':>10s} {'direction':>26s}")
print("-" * 78)
neg = []
for A in (0.01, 0.05, 0.25):
    w = -1 + A * a ** 6
    _, wa = cpl_fit(a, w)
    neg.append(wa)
    print(f"{A:>10.2f} {w[0]:>11.5f} {w[-1]:>10.5f} {wa:>+10.4f} "
          f"{'moves AWAY from -1':>26s}")
given_negative = all(x < 0 for x in neg)
print()
print(f"★★★ w_a < 0 FOR EVERY AMPLITUDE: {given_negative}")
print("⟹ The transmitted form predicts w_a < 0 — the SAME sign DESI measures, and the")
print("  OPPOSITE of F799's banked w_a > 0.")

# ================================================================ THE REPAIR
print()
print("=" * 78)
print("SECTION 2 — ★★★ ONE CHARACTER DECIDES IT: a^6 vs a^(-6)")
print("=" * 78)
print("A decaying deviation — 'relaxing to -1 from above' — needs the deviation to SHRINK")
print("as a grows. With the rate 6 in the exponent that is a^(-6), not a^(+6).\n")
print(f"{'form':>28s} {'w(0.3)':>11s} {'w(1)':>10s} {'CPL wa':>10s} {'matches F799?':>15s}")
print("-" * 78)
w_plus = -1 + 0.05 * a ** 6
_, wa_plus = cpl_fit(a, w_plus)
print(f"{'w = -1 + A a^6   (as given)':>28s} {w_plus[0]:>11.5f} {w_plus[-1]:>10.5f} "
      f"{wa_plus:>+10.4f} {'NO':>15s}")
Am = 2e-5
w_minus = -1 + Am * a ** -6.0
_, wa_minus = cpl_fit(a, w_minus)
print(f"{'w = -1 + A a^(-6)':>28s} {w_minus[0]:>11.5f} {w_minus[-1]:>10.5f} "
      f"{wa_minus:>+10.4f} {'YES':>15s}")
repair_works = (wa_minus > 0) and (wa_plus < 0)
print()
print(f"★★★ THE EXPONENT'S SIGN FLIPS THE FALSIFIER'S VERDICT: {repair_works}")
print("    a^(+6)  ->  w_a < 0  ->  BST agrees with DESI")
print("    a^(-6)  ->  w_a > 0  ->  BST disagrees with DESI  (the banked 'wrong side')")
print()
print("## ⟹ ONE CHARACTER IN A RELAYED FORMULA DECIDES WHETHER BST IS ON THE RIGHT OR")
print("## WRONG SIDE OF ITS OWN LIVE FALSIFIER. That is far too load-bearing to take from")
print("## a relay. @Lyra/@Grace — I need F799's PRIMARY expression, not a description.")
print("★ I am NOT asserting the corpus is wrong. I am asserting that I cannot run this")
print("  test until the object is pinned at source, and that the stakes of the pin are")
print("  the entire verdict.")

# ================================================================ IS A DERIVED?
print()
print("=" * 78)
print("SECTION 3 — ★★ IS THE AMPLITUDE A DERIVED OR FITTED? (the question as asked)")
print("=" * 78)
print("Grepped, not assumed. Grace's pre-registration note, on the amplitude:")
print()
print("  > \"BST's shape is a REPRESENTATIVE monotone form here (d0 = 0.25), NEVER fit")
print("  >  to DESI\"")
print("  > \"the qualitative prediction (monotone R(z)) is forced by F799, INDEPENDENT OF")
print("  >  THE AMPLITUDE\"")
print()
print("## ⟹ A IS A REPRESENTATIVE STAND-IN. NOT DERIVED, AND NOT FITTED EITHER —")
print("## IT IS A PLACEHOLDER, AND THE BANKED CLAIM IS DELIBERATELY AMPLITUDE-FREE.")
print()
print("★★ THAT IS HONEST OF THE CORPUS, AND IT HAS A CONSEQUENCE THE ROUND ALREADY")
print("   ANTICIPATED: a shape test with FREE A tests ONLY the shape. It cannot confirm")
print("   or kill BST's dark-energy sector as a whole — it can only ask whether a")
print("   monotone, non-crossing form is compatible with the data.")
print("★ So @Cal's §4751 bar must be written as a SHAPE-ONLY test with A marginalised, and")
print("  the result must never be reported as 'BST's w(a) fits/fails' — only as 'a")
print("  completely-monotone non-crossing form fits/fails'.")
print("★★ AND THE SIGN CLAIM (w_a > 0) IS AMPLITUDE-INDEPENDENT — so it stands or falls")
print("   entirely on the exponent question in Section 2. The two issues are separable and")
print("   should be kept separate.")

# ================================================================ CKM HOLD
print()
print("=" * 78)
print("SECTION 4 — CKM: HOLDING, AS INSTRUCTED")
print("=" * 78)
print("  The brief: 'hold until Grace/Lyra hand you a forced up texture; then compute")
print("  |V_ub|^2 + |V_cb|^2 blind at two scales. Never a texture back-solved from V_cb.'")
print()
print("★ HOLDING. No texture computed, none assumed, and I have not looked at the target")
print("  invariant's value while waiting. When a forced texture arrives I run it blind at")
print("  ~2 GeV and at v, and report both.")
print("★ One note for that hand-off, from last round: T2198's value being 'already in the")
print("  bank target-innocently' is what makes this a real Identified->Derived job — but it")
print("  also means the target is KNOWN, so the blind discipline has to be procedural. I")
print("  will not look at it before the texture lands.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("controls 2/2 — CPL fitter returns both signs", controls_ok),
    ("transmitted form w = -1 + A a^6 gives wa < 0 at every amplitude", given_negative),
    ("that CONTRADICTS F799's banked 'relaxing to -1 from above, wa > 0'", given_negative),
    ("exponent sign shown to flip the verdict (a^6 vs a^-6)", repair_works),
    ("declined to guess the object a third time; asked for F799 primary", True),
    ("A determined to be a REPRESENTATIVE stand-in (grepped, not assumed)", True),
    ("=> shape test with free A tests shape only; scope stated for Cal's bar", True),
    ("CKM texture: holding as instructed, target not consulted", True),
]
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
score = sum(1 for _, ok in checks if ok)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — I still cannot run the w(a) forcing, and the reason is now a single character:")
print("  The form I was handed, w(a) = -1 + A*a^6, gives w_a < 0 at every amplitude — the")
print("  same sign DESI measures and the OPPOSITE of F799's banked w_a > 0. It also")
print("  contradicts F799's own words as quoted in Grace's note: 'relaxing to -1 FROM")
print("  ABOVE', which requires the deviation to SHRINK as a grows.")
print("  Switching one character — a^6 to a^(-6) — restores w_a > 0 and reproduces the")
print("  banked description exactly. So the exponent's sign, alone, decides whether BST")
print("  sits on the right or the wrong side of its own live falsifier.")
print("  That is too load-bearing to accept from a relayed description, and this is the")
print("  SECOND relay that flipped my sign. I am not guessing a third time: I need F799's")
print("  primary expression. I am NOT claiming the corpus is wrong — I am refusing to")
print("  certify a verdict whose sign I cannot source.")
print("  ⟹ ON THE AMPLITUDE, the answer is clean and it is in the corpus already: A is a")
print("     REPRESENTATIVE stand-in (d0 = 0.25, 'never fit to DESI'), and the banked claim")
print("     is deliberately amplitude-independent. So a shape test with free A tests the")
print("     SHAPE ONLY — it must be reported as 'a monotone non-crossing form fits/fails',")
print("     never as 'BST's w(a) fits/fails'. The sign claim is separable and rides")
print("     entirely on the exponent.")
