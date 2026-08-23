#!/usr/bin/env python3
"""
Toy 5448 — PRE-REGISTRATION for the cos-theta compute, + what the FORMULA forces alone.

WHAT THIS TOY IS (declared before running):
    My two assignments this round are BOTH explicit holds:
      "once chi and P are forced (NOT BEFORE), compute cos theta blind"
      "on w(a): hold until Lyra states F799's primary expression"
    So I compute NO angle and certify NO sign. What I CAN do without chi, P, or a
    sourced rho is: (1) fix the decision rule BEFORE the number exists, (2) derive what
    Grace's formula forces on its own, and (3) validate the instrument on synthetic
    inputs so that when chi and P land the run is a lookup, not a build.

★ BLINDNESS IS PROCEDURAL HERE, AND I SAY SO. The target is IN MY BRIEF (2.26 / 2.43
  deg; |V_ub|^2+|V_cb|^2 ~ 0.0017). I cannot unsee it. So blindness cannot mean
  ignorance — it means the DECISION RULE and the INSTRUMENT are frozen before chi and P
  arrive, and nothing is tuned to the target afterwards. That is the only honest form
  of blind available, and pretending otherwise would be the fiction.

GRACE'S OBJECT (inherited, not re-derived):
    M_up = P C,  M_down = C P,  C = |chi><chi|
    cos theta = |<chi|P|chi>| / || P|chi> ||
"""

import numpy as np

# ================================================================ THE FORMULA
print("=" * 78)
print("SECTION 1 — WHAT THE FORMULA IS, GEOMETRICALLY (no chi, no P needed)")
print("=" * 78)
print("  cos theta = |<chi|P|chi>| / ||P|chi>||")
print()
print("  <chi|P|chi> = <chi | P chi>, and ||P|chi>|| is the length of P chi. So this is")
print("  exactly the cosine of the ANGLE BETWEEN P|chi> AND |chi> (with |chi> a unit")
print("  vector).")
print()
print("  ⟹ theta IS THE ANGLE BY WHICH P TILTS THE CONDENSATE DIRECTION.")
print("  ⟹ cos theta = 1  <=>  P|chi> is parallel to |chi>  <=>  chi is an EIGENVECTOR of P")
print("  ⟹ ZERO MIXING <=> THE CONDENSATE IS AN EIGENVECTOR OF THE COMMIT OPERATOR.")
print()
print("★ That is a real, checkable statement about the mechanism, and it is available")
print("  BEFORE either object is named: whatever P turns out to be, the CKM angle is")
print("  zero exactly when it leaves the condensate direction alone.")

# ================================================================ THE PROJECTOR CASE
print()
print("=" * 78)
print("SECTION 2 — ★★★ IF P IS A PROJECTOR, THE FORMULA COLLAPSES")
print("=" * 78)
print("The lead is P = P_record (+) P_encode — a COMMIT operator. Commit/measurement")
print("operators are typically PROJECTORS. Suppose P^2 = P and P = P^dagger. Then")
print()
print("      <chi|P|chi> = <chi|P^2|chi> = <P chi|P chi> = ||P|chi>||^2")
print()
print("  so   cos theta = ||P|chi>||^2 / ||P|chi>|| = ||P|chi>||")
print()
print("## ⟹ cos theta = || P|chi> ||   AND THEREFORE")
print("## ⟹ sin^2 theta = 1 - ||P|chi>||^2 = THE FRACTION OF THE CONDENSATE ANNIHILATED")
print("##   BY THE COMMIT PROJECTION.")
print()
# verify numerically on random projectors
rng = np.random.default_rng(5)
ok = True
for trial in range(6):
    d = rng.integers(4, 9)
    k = rng.integers(1, d)
    Q, _ = np.linalg.qr(rng.normal(size=(d, d)))
    P = Q[:, :k] @ Q[:, :k].T                 # orthogonal projector, rank k
    chi = rng.normal(size=d); chi /= np.linalg.norm(chi)
    lhs = abs(chi @ P @ chi) / np.linalg.norm(P @ chi)
    rhs = np.linalg.norm(P @ chi)
    ok &= abs(lhs - rhs) < 1e-12
print(f"  verified on 6 random orthogonal projectors: cos theta == ||P|chi>||  -> {ok}")
print()
print("★ NEGATIVE CONTROL — for a NON-projector P the identity must FAIL, or it is vacuous:")
A = rng.normal(size=(6, 6))
chi = rng.normal(size=6); chi /= np.linalg.norm(chi)
lhs = abs(chi @ A @ chi) / np.linalg.norm(A @ chi)
rhs = np.linalg.norm(A @ chi)
nonproj_differs = abs(lhs - rhs) > 1e-3
print(f"    generic P: |<chi|P|chi>|/||P chi|| = {lhs:.6f}   vs   ||P chi|| = {rhs:.6f}"
      f"   differ: {nonproj_differs}")
print()
print("★★ SO THE FIRST THING TO ASK WHEN P IS NAMED IS: **IS IT A PROJECTOR?**")
print("   If yes, the whole CKM angle reduces to ONE number — how much of the condensate")
print("   survives the commit — and the mixing invariant |V_ub|^2+|V_cb|^2 IS the")
print("   annihilated fraction. If no, the full quotient is needed and the interpretation")
print("   is weaker. @Grace @Lyra — that is the single question I would want answered")
print("   first, and it is answerable the moment P has a definition.")

# ================================================================ PRE-REGISTRATION
print()
print("=" * 78)
print("SECTION 3 — ★★★ THE PRE-REGISTRATION (frozen now, before chi and P exist)")
print("=" * 78)
LOW, HIGH = 2.26, 2.43                      # the two sides, from the brief
MID = (LOW + HIGH) / 2
GAP_ABS = HIGH - LOW
GAP_REL = GAP_ABS / MID
print(f"  the controversy : exclusive {LOW} deg   vs   inclusive {HIGH} deg")
print(f"  midpoint (the decision boundary, fixed NOW): {MID:.4f} deg")
print(f"  separation      : {GAP_ABS:.3f} deg  =  {100*GAP_REL:.2f}% of the central value")
print()
print("  DECISION RULE, FROZEN:")
print(f"     theta_BST <  {MID:.4f} deg   ->  I report EXCLUSIVE")
print(f"     theta_BST >  {MID:.4f} deg   ->  I report INCLUSIVE")
print("     and I report the number itself either way, at BOTH scales.")
print()
print("★★★ AND THE HONESTY GUARD THAT MATTERS MOST — THE PRECISION BAR:")
print(f"     the two sides differ by only {100*GAP_REL:.2f}%. So the computation can only")
print("     adjudicate if its OWN two-scale spread is SMALLER than that.")
print()
print(f"     IF  |theta(2 GeV) - theta(v)|  >  {GAP_ABS:.3f} deg")
print("     THEN I REPORT 'CANNOT ADJUDICATE' AND NAME NO SIDE.")
print()
print("★★ I am fixing that BEFORE the number exists precisely so it cannot be relaxed")
print("   afterwards. A 7% controversy cannot be settled by a computation with a 10%")
print("   internal spread, and the temptation to quote whichever scale lands better is")
print("   exactly what a pre-registration is for.")
print()
print("  ALSO FROZEN:")
print("    - no P back-solved from V_cb, and no chi tuned to it;")
print("    - if P is a projector I report ||P|chi>|| as the primary number;")
print("    - I report sin^2 theta alongside theta (it is the rank-1 invariant);")
print("    - if chi or P arrives with a free parameter, I say so and the result is")
print("      Identified, not Derived, however well it lands.")

# ================================================================ INSTRUMENT
print()
print("=" * 78)
print("SECTION 4 — THE INSTRUMENT, VALIDATED ON SYNTHETIC INPUTS (ready for the hand-off)")
print("=" * 78)

def theta_from(P, chi):
    """The CKM angle from Grace's ordered-product formula. Returns degrees."""
    chi = chi / np.linalg.norm(chi)
    num = abs(chi.conj() @ P @ chi)
    den = np.linalg.norm(P @ chi)
    c = np.clip(num / den, 0.0, 1.0)
    return np.degrees(np.arccos(c))

print("  POSITIVE CONTROL — chi an eigenvector of P must give exactly 0 deg:")
Q, _ = np.linalg.qr(rng.normal(size=(6, 6)))
Pk = Q[:, :3] @ Q[:, :3].T
t0 = theta_from(Pk, Q[:, 0])
print(f"    chi = an eigenvector of P  ->  theta = {t0:.10f} deg   "
      f"{'OK' if t0 < 1e-9 else '*** BROKEN ***'}")
print("  POSITIVE CONTROL — a known tilt must be recovered:")
d = 4
Pfull = np.eye(d)
Pfull[3, 3] = 0.0                              # projector killing one axis
for frac in (0.001, 0.0017, 0.01):
    chi = np.zeros(d); chi[0] = np.sqrt(1 - frac); chi[3] = np.sqrt(frac)
    th = theta_from(Pfull, chi)
    print(f"    annihilated fraction {frac:.4f}  ->  theta = {th:.4f} deg   "
          f"sin^2 = {np.sin(np.radians(th))**2:.6f}")
recovered = abs(np.sin(np.radians(theta_from(Pfull,
              np.array([np.sqrt(1-0.0017), 0, 0, np.sqrt(0.0017)]))))**2 - 0.0017) < 1e-9
print(f"    ⟹ sin^2 theta reproduces the annihilated fraction exactly: {recovered}")
print()
print("★ The instrument is ready and controlled. When chi and P land I run it, report")
print("  theta and sin^2 theta at both scales, apply the frozen rule, and name a side —")
print("  or decline to, per the precision bar.")

# ================================================================ w(a)
print()
print("=" * 78)
print("SECTION 5 — w(a): HOLDING, AS INSTRUCTED")
print("=" * 78)
print("  Holding for @Lyra's PRIMARY F799 expression (exact form + variable convention).")
print("  Standing finding from 5447, unchanged: the relayed a^(+6) gives w_a < 0; the")
print("  description 'relaxing to -1 from above' requires w_a > 0, which a^(-6) delivers.")
print("★ I will not certify a falsifier's SIGN from a relay. Two relays have already")
print("  flipped it; the third statement should be a quotation, not a paraphrase.")

# ================================================================ SCORE
print()
print("=" * 78)
checks = [
    ("held on cos theta: no angle computed, chi and P not assumed", True),
    ("geometric reading derived: theta = tilt of chi by P", True),
    ("zero-mixing condition derived (chi an eigenvector of P)", True),
    ("projector identity verified on 6 random projectors", ok),
    ("negative control: identity fails for non-projector P", nonproj_differs),
    ("decision rule frozen BEFORE the number exists", True),
    ("precision bar frozen: two-scale spread > gap => no side named", True),
    ("instrument validated (eigenvector -> 0 deg; fraction recovered)", recovered and t0 < 1e-9),
    ("w(a): holding for the primary expression", True),
]
for name, ok_ in checks:
    print(f"  [{'PASS' if ok_ else 'FAIL'}] {name}")
score = sum(1 for _, o in checks if o)
print(f"\nSCORE: {score}/{len(checks)}")
print()
print("VERDICT — I hold on both computes, and hand back what the formula forces by itself:")
print("  Grace's cos theta is the cosine of the angle between P|chi> and |chi>, so the CKM")
print("  angle is the tilt the commit operator gives the condensate — and mixing vanishes")
print("  exactly when the condensate is an eigenvector of P. That much needs neither object")
print("  named.")
print("  ★ AND IF P IS A PROJECTOR the formula collapses to cos theta = ||P|chi>||, making")
print("    the rank-1 invariant |V_ub|^2+|V_cb|^2 EQUAL to the fraction of the condensate")
print("    the commit annihilates. Verified on random projectors, and shown to fail for")
print("    non-projectors so the statement is not vacuous. ⟹ THE FIRST QUESTION TO ASK OF")
print("    P WHEN IT IS NAMED IS WHETHER P^2 = P; it decides how sharp the whole reading is.")
print("  ★★ THE PRE-REGISTRATION IS FROZEN NOW: decision boundary at the 2.345 deg midpoint,")
print("     and — the part that matters — IF THE TWO-SCALE SPREAD EXCEEDS THE 0.17 deg GAP")
print("     I NAME NO SIDE. A 7% controversy cannot be adjudicated by a computation with a")
print("     larger internal spread, and I would rather fix that rule while the number does")
print("     not yet exist than argue about it afterwards.")
print("  ★ Blindness here is PROCEDURAL and I said so: the target is in my brief, so the")
print("    honest form is a frozen rule and a frozen instrument, not pretended ignorance.")
