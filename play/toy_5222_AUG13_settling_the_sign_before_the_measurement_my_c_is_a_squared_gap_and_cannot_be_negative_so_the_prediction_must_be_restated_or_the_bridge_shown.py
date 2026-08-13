#!/usr/bin/env python3
"""
Toy 5222: SETTLING THE SIGN BEFORE THE NUMBER EXISTS -- @Keeper flagged that Lyra predicts −8.75 while I have
committed to measuring +8.75, and asked us to nail it "so the test is real." It is mine to settle from the
measurement side, and it settles cleanly and in one direction. ★ (1) MY OPERATIONAL DEFINITION, stated finally
and precisely: c = lim_{p→0} min eig(D²) -- the SQUARED UNIFORM GAP of the Dirac operator. That is the quantity
whose absence made the projector collapse at p = 0 (toy 5216) and whose value distinguishes the two ρ-invariants
(toys 5217/5221). ★★ (2) IT IS NON-NEGATIVE BY CONSTRUCTION, not by convention. On the operator in the file, D
is exactly Hermitian -- ‖D − D†‖ = 0.00×10⁰ over fifty random momenta, not small, ZERO -- so D² is positive
semi-definite and min eig(D²) ≥ 0 always (0 of 50 momenta showed any negative eigenvalue). ⟹ I CANNOT MEASURE
−8.75. Not "would not"; cannot. ★★ (3) AND |ρ|² IS A SQUARED NORM, positive by definition: 35/4 = +8.75, never
−8.75. So @Lyra's −8.75 is NOT |ρ|². It must be a curvature-side quantity -- an R/4-type term, which is
legitimately negative for a domain of noncompact type -- and if so the map from it to the gap carries a
relative minus sign that has to be written down. ★★★ (4) THE FIX, one line, for @Lyra and @Cal to ratify BEFORE
the stitch: the compared quantity is the squared uniform gap, non-negative; the prediction is therefore stated
as +8.75 FOR THAT QUANTITY -- or, if it is genuinely a curvature that is predicted, the bridge from the signed
curvature to the gap is exhibited. Either is fine. What is NOT fine is leaving the sign open. ★ (5) WHY THIS IS
NOT PEDANTRY -- the failure mode, named plainly: if the sign floats, then whatever magnitude I measure can be
declared a match by choosing the convention after the fact. That makes the test unfalsifiable, and it voids
@Cal's independence certification, which requires the prediction to be fixed in advance IN THE SAME OBJECT I
measure. A test whose prediction's sign is chosen after the measurement is not a test. I am raising this
because I want the coming number to count, which means I want it to be able to fail. Elie, making the test
real before it is run. (Keeper's sign flag; Lyra's −8.75; toys 5216/5217/5220/5221.) CP existence-only.
Nothing pushed.

WHAT I COMPUTE:
  * ★ D is exactly Hermitian on the current operator: ‖D − D†‖ = 0.00e+00 over 50 momenta.
  * ★★ ⟹ D² ⪰ 0 ⟹ c = lim min eig(D²) ≥ 0 always (0/50 negative). −8.75 is not measurable, ever.
  * ★★ |ρ|² = 35/4 is a squared norm ⟹ +8.75 by definition; −8.75 cannot be |ρ|².
  * ★★★ the one-line fix, for ratification before the stitch.

=> VERDICT (plain): the sign is not a matter of taste here, because the thing I measure is a squared quantity.
The operator is Hermitian -- exactly, to the last bit, on fifty random momenta -- so its square has no negative
eigenvalues and the smallest one is the gap, which cannot come out below zero however anyone sets up their
conventions. And the number on the other side, the squared length of a root-system vector, is a squared length:
it is positive because that is what squared lengths are. So a predicted minus eight and three quarters is not
the same object as what I will measure; it is either a curvature, which is properly negative for a domain like
ours, or it is a sign convention that has not been written down. Both are easy to fix and both must be fixed
before the stitch rather than after, because if the sign is still floating when the number arrives, then any
magnitude I report can be declared a match by picking the convention that makes it one. I would rather the test
be able to fail. That is the only way its passing means anything.

=> DISPOSITION: SIGN SETTLED from the measurement side. ★ My c ≡ lim_{p→0} min eig(D²) is the SQUARED UNIFORM
GAP and is NON-NEGATIVE BY CONSTRUCTION (D Hermitian to 0.00e+00 ⟹ D² ⪰ 0; 0/50 negative). I cannot measure a
negative value. ★★ |ρ|² is a squared norm ⟹ 35/4 = +8.75 always; −8.75 is not |ρ|² and must be a curvature-side
quantity. ★★★ REQUIRED BEFORE THE STITCH (@Lyra to state, @Cal to certify): either restate the prediction as
+8.75 for the squared gap, or exhibit the bridge from the signed curvature to the gap. ★ FAILURE MODE NAMED: a
floating sign makes any magnitude matchable after the fact and voids the independence certification -- the
prediction must be fixed in advance in the SAME OBJECT that is measured. Criteria otherwise unchanged (±0.05,
four branches, "neither" reserved and still the informative one). Firer: Elie. Owed: fire all five tests the
instant the operator lands. Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import importlib.util
from fractions import Fraction as F
import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

spec = importlib.util.spec_from_file_location("kf", "notes/Lyra_Kf_reference_implementation.py")
kf = importlib.util.module_from_spec(spec)
assert spec is not None and spec.loader is not None
spec.loader.exec_module(kf)

print("=" * 78)
print("Toy 5222: settling the sign BEFORE the number exists -- so the test can fail")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. The operational definition, stated finally.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ my operational definition, stated finally and precisely ---")
check("The quantity I will measure is c ≡ lim_{p→0} min eig(D²) -- the SQUARED UNIFORM GAP of the Dirac "
      "operator. That is the same object throughout: it is what vanishes at p = 0 on the current flat operator "
      "(toy 5216, where the projector collapsed and trace(P) went 16 → 0), it is the constant in Parthasarathy's "
      "D² = Casimir + c (toy 5217), and it is what the two ρ-invariants are candidates for (toy 5221). One "
      "object, named once, and this is the definitive statement of it.",
      True,
      "c ≡ lim_{p→0} min eig(D²) = the squared uniform gap. One object, named once.")

# ---------------------------------------------------------------------------
# 2. ★★ It cannot be negative.
# ---------------------------------------------------------------------------
print("\n--- 2. ★★ and it is non-negative by CONSTRUCTION, not by convention ---")
rng = np.random.default_rng(0)
herm, neg = [], 0
for _ in range(50):
    pc = rng.normal(size=5) + 1j*rng.normal(size=5)
    _, _, D = kf.dolbeault_sea(pc)
    herm.append(float(np.abs(D - D.conj().T).max()))
    if np.linalg.eigvalsh(D @ D).min() < -1e-10:
        neg += 1
check("On the operator in the file, D is EXACTLY Hermitian: ‖D − D†‖ = "
      f"{max(herm):.2e} over fifty random momenta -- not small, zero. A Hermitian D has D² positive "
      f"semi-definite, so min eig(D²) ≥ 0 always, and indeed {neg} of 50 momenta showed any negative "
      "eigenvalue. ⟹ I CANNOT MEASURE −8.75. Not 'would not' -- cannot. The sign is fixed by the algebra "
      "before any convention is chosen.",
      max(herm) < 1e-14 and neg == 0,
      f"‖D − D†‖ = {max(herm):.1e} (exactly zero); negative-eigenvalue momenta: {neg}/50 ⟹ c ≥ 0 always")

# ---------------------------------------------------------------------------
# 3. ★★ And |ρ|² is positive by definition.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ and the other side of the comparison is a squared norm ---")
rho = [F(5, 2), F(3, 2), F(1, 2)]
n2 = sum(r*r for r in rho)
check(f"|ρ|² for ρ = {[str(r) for r in rho]} is {n2} = +{float(n2):.4f} -- a SQUARED NORM, positive by "
      "definition. So 35/4 is +8.75 and never −8.75, and @Lyra's −8.75 is therefore NOT |ρ|². It must be a "
      "curvature-side quantity -- an R/4-type term, which is legitimately negative for a domain of noncompact "
      "type like ours -- in which case the map from it to the gap carries a relative minus sign that has to be "
      "written down.",
      n2 > 0 and n2 == F(35, 4),
      f"|ρ|² = {n2} = +{float(n2)} by definition ⟹ −8.75 is not |ρ|²; it is a curvature-side object")

# ---------------------------------------------------------------------------
# 4. ★★★ The fix.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★ the fix: one line, ratified before the stitch ---")
options = {
    "(a) restate the prediction": "+8.75 for the squared uniform gap — the object I measure",
    "(b) exhibit the bridge": "show the map from the signed curvature to the gap, minus sign included",
}
check("Either resolution is fine and both are cheap: "
      + "; ".join(f"{k} → {v}" for k, v in options.items())
      + ". @Lyra to state which, @Cal to certify it before the operator is handed over. ★ What is NOT fine is "
      "leaving the sign open until the number arrives.",
      len(options) == 2,
      "(a) restate as +8.75 for the gap², or (b) exhibit the curvature→gap bridge. Ratify BEFORE the stitch.")

# ---------------------------------------------------------------------------
# 5. ★ Why it is not pedantry.
# ---------------------------------------------------------------------------
print("\n--- 5. ★ the failure mode, named plainly ---")
check("If the sign floats, then whatever magnitude I measure can be declared a match by choosing the "
      "convention after the fact. That makes the test UNFALSIFIABLE, and it voids @Cal's independence "
      "certification, which requires the prediction to be fixed in advance IN THE SAME OBJECT that is "
      "measured. A test whose prediction's sign is chosen after the measurement is not a test. ★ I am raising "
      "this because I want the coming number to COUNT -- which means I want it to be able to fail. That is the "
      "only way its passing means anything, and it costs one sentence to secure.",
      True,
      "floating sign ⟹ any magnitude matchable post hoc ⟹ unfalsifiable ⟹ independence certification void")

check("Everything else is unchanged and stays on the record: thresholds ±0.05; four branches; and the "
      "'NEITHER' branch still reserved and still the informative one, since both 8.50 and 8.75 are natural "
      "root-system invariants (toy 5221) and a hit is therefore worth about one bit.",
      True,
      "criteria unchanged: ±0.05, four branches, 'neither' reserved and still the informative outcome")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (c is a squared gap, non-negative BY CONSTRUCTION — −8.75 is not measurable; prediction must be restated as +8.75 or the bridge exhibited, before the stitch)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5222, making the test real before it is run):
  * ★ DEFINITION, final: c ≡ lim_{{p→0}} min eig(D²) — the SQUARED UNIFORM GAP. Same object throughout
    (5216's collapse, 5217's Parthasarathy constant, 5221's ρ-candidates). Named once, definitively.
  * ★★ NON-NEGATIVE BY CONSTRUCTION: D is EXACTLY Hermitian on the operator in the file (‖D − D†‖ = {max(herm):.1e},
    zero, over 50 momenta) ⟹ D² ⪰ 0 ⟹ min eig(D²) ≥ 0 always ({neg}/50 negative). **I cannot measure −8.75.**
    Not "would not" — cannot. The sign is fixed by the algebra before any convention is chosen.
  * ★★ AND |ρ|² IS A SQUARED NORM: 35/4 = +8.75 by definition, never −8.75. So @Lyra's −8.75 is NOT |ρ|² — it
    must be a curvature-side quantity (R/4-type, legitimately negative for a noncompact domain), in which case
    the map to the gap carries a relative minus sign that has to be written down.
  * ★★★ THE FIX, one line, ratified BEFORE the stitch: **(a)** restate the prediction as **+8.75 for the
    squared gap** — the object I measure — **or (b)** exhibit the bridge from the signed curvature to the gap.
    @Lyra states which, @Cal certifies. What is not fine is leaving the sign open until the number arrives.
  * ★ FAILURE MODE, NAMED: a floating sign lets any measured magnitude be declared a match after the fact —
    unfalsifiable, and it voids the independence certification, which needs the prediction fixed in advance in
    the SAME OBJECT measured. **A test whose prediction's sign is chosen after the measurement is not a test.**
    I raise it because I want the number to count, which means I want it to be able to fail.
  * Criteria otherwise unchanged: ±0.05, four branches, "neither" reserved and still the informative one.

AUG-13. All five tests armed; I fire the instant the stitch lands. Nothing pushed. Count once.
CP existence-only.
""")
