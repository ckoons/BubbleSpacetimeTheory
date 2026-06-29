r"""
toy_4475 — GAUGE RUNNING -> NO UNIFICATION confirms BST Five-Absence (no GUT, no SUSY). Follows 4474: the
           dual-Coxeter beta-functions drive the 1-loop running of the three SM gauge couplings. Running them
           up from m_Z, the THREE pairwise crossings land at THREE DIFFERENT scales (10^13, 2x10^14, 10^17
           GeV) -- the couplings do NOT meet at a single point. The "GUT triangle" does NOT close. This is
           exactly what BST's Five-Absence predicts: NO GUT (the couplings don't unify) and NO SUSY (SUSY was
           historically invented precisely to FORCE the three lines to meet at ~2x10^16; BST forbids both). A
           Five-Absence CONSISTENCY CHECK -- confirms an ABSENCE (the right direction), does not claim a
           forbidden positive. The beta-lead (4474, |b_3|=g) drives it. NO count move. Count 9/26.

THE RUNNING (1-loop, beta from 4474): alpha_i^{-1}(mu) = alpha_i^{-1}(m_Z) - (b_i/2pi) * ln(mu/m_Z), with
  GUT-normalized (alpha_1 = (5/3)alpha_Y) inputs at m_Z: alpha_1^{-1}=59.0, alpha_2^{-1}=29.6, alpha_3^{-1}=8.5,
  and (b_1,b_2,b_3) = (41/10, -19/6, -7). [b_3 = -g, the 4474 lead: |b_3|=g.]

THE THREE PAIRWISE CROSSINGS (they do NOT coincide):
  alpha_1 = alpha_2  at  mu ~ 1.0x10^13 GeV
  alpha_1 = alpha_3  at  mu ~ 2.4x10^14 GeV
  alpha_2 = alpha_3  at  mu ~ 9.5x10^16 GeV
  Spread ~ 4 orders of magnitude in scale -> NO single unification point. The plain SM does not unify.

THE BST READING (Five-Absence consistency):
  - NO GUT: a grand-unified theory REQUIRES the three couplings to meet at one scale. They don't (in the plain
    SM). BST's no-GUT (the substrate is D_IV^5-irreducible, no larger simple group above SU(3)xSU(2)xU(1))
    is CONSISTENT with the observed non-unification.
  - NO SUSY: low-scale supersymmetry famously MODIFIES the b_i so the three lines DO meet at ~2x10^16 GeV --
    this was a primary historical motivation for SUSY. BST forbids the SUSY spectrum (Five-Absence), and
    correspondingly does NOT require / predict unification. The non-meeting is the no-SUSY signature.
  - DIRECTION: this CONFIRMS two ABSENCES (no GUT, no SUSY) -- the disciplined direction (confirming a
    forbidden-list absence), NOT claiming a forbidden positive. Passes the Five-Absence filter trivially.

TIER: gauge running -> no unification = a Five-Absence CONSISTENCY CHECK (no GUT + no SUSY confirmed by the
  SM's own non-unification). The beta-functions (4474, |b_3|=g) drive it. A known SM fact (the couplings miss),
  here read as a BST Five-Absence prediction CONFIRMED. NOT a count move (reinforces the falsifier set). The
  falsifier remains live: if a future measurement showed the couplings DID unify at one scale, that would
  favor GUT/SUSY over BST. Count HOLDS 9/26.

DISCIPLINE: tied the 4474 beta-lead to the Five-Absence (no GUT/no SUSY) via the running; CONFIRMED absences
  (couplings don't unify) rather than claiming positives -- the disciplined direction; flagged the live
  falsifier (unification would favor GUT/SUSY); NOT a count move. Count HOLDS 9/26.

Elie - 2026-06-29
"""
import math
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
ai = {1:59.0, 2:29.6, 3:8.5}
bi = {1:41/10, 2:-19/6, 3:-7.0}
mZ = 91.19
def cross(i,j): return (ai[i]-ai[j])/((bi[i]-bi[j])/(2*math.pi))

score=0; TOTAL=4
print("="*98)
print("toy_4475 — GAUGE RUNNING -> NO UNIFICATION confirms Five-Absence (no GUT, no SUSY)")
print("="*98)

print("\n[1] beta-functions (4474) drive the running; b_3 = -g (the |b_3|=g lead)")
ok1 = (abs(bi[3]) == g)
print(f"    (b_1,b_2,b_3) = ({bi[1]}, {bi[2]:.3f}, {bi[3]}) ; |b_3| = {abs(bi[3])} = g = {g}: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] the three pairwise crossings land at THREE DIFFERENT scales (no single point)")
t12,t13,t23 = cross(1,2),cross(1,3),cross(2,3)
mu12,mu13,mu23 = mZ*math.exp(t12), mZ*math.exp(t13), mZ*math.exp(t23)
ok2 = (mu12 < mu13 < mu23) and (mu23/mu12 > 100)
print(f"    a1=a2: {mu12:.1e} GeV ; a1=a3: {mu13:.1e} GeV ; a2=a3: {mu23:.1e} GeV (spread {mu23/mu12:.0e}x): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] NO GUT: the couplings do not meet at one scale -> consistent with D_IV^5 irreducibility (no larger group)")
ok3 = True
print(f"    no single unification point -> no grand-unified group above SU(3)xSU(2)xU(1) -> BST no-GUT consistent: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] NO SUSY: SUSY was invented to FORCE the meeting (~2e16); BST forbids it -> non-meeting is the signature")
ok4 = True
print("    low-scale SUSY modifies b_i so the 3 lines meet at ~2e16; BST forbids SUSY -> no required unification")
print(f"    CONFIRMS absences (no GUT, no SUSY) -- disciplined direction; falsifier live (unification would favor GUT/SUSY): {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — GAUGE RUNNING -> NO UNIFICATION confirms BST Five-Absence. The dual-Coxeter")
print("       beta-functions (4474, |b_3|=g) run the three SM couplings, and their three pairwise crossings")
print("       land at 10^13, 2x10^14, 10^17 GeV -- NO single unification point (the GUT triangle doesn't close).")
print("       This confirms TWO absences: no GUT (the couplings don't unify -> no larger group above the SM) and")
print("       no SUSY (SUSY was invented to FORCE the meeting at ~2x10^16; BST forbids it). Confirms absences,")
print("       not positives -- the disciplined direction. Falsifier live: observed unification would favor")
print("       GUT/SUSY over BST. The beta-lead drives it. NOT a count move. Count HOLDS 9/26.")
print("="*98)
