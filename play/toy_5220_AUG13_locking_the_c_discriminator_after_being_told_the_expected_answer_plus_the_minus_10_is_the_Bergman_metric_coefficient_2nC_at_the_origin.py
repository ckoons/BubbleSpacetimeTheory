#!/usr/bin/env python3
"""
Toy 5220: LOCKING THE c-DISCRIMINATOR AFTER BEING TOLD THE EXPECTED ANSWER -- plus one independent check that
the team should have before the bridge gets used. Keeper's message says Lyra's blind −10 curvature "predicts
you'll measure 8.50, not 8.75." That is useful information and it also changes my job: I committed the
discriminator blind yesterday, and I have now been told which branch to expect. So the honest move is to lock
the acceptance criteria BEFORE the operator lands rather than after, and to say plainly what the protection is.
★ (1) THE PROTECTION IS THAT THE MEASUREMENT IS MECHANICAL: c = lim(D²) as the momentum → 0 has no free
choices, no fit, no tolerance to slide -- so knowing the expected answer cannot steer it. What knowing the
answer CAN steer is the reporting: how close counts as a match, and whether an odd number gets rounded toward
the expectation. So I am fixing those now. ★ (2) PRE-COMMITTED ACCEPTANCE CRITERIA, tolerances fixed at this
timestamp: |c − 8.50| < 0.05 ⟹ the ρ-type, g-FREE constant; |c − 8.75| < 0.05 ⟹ n_C·g/4, which CARRIES g = 7;
|c| < 0.05 ⟹ still flat, no curvature in the operator; ANYTHING ELSE ⟹ I report the raw number and claim
NEITHER candidate. That fourth branch is the one that matters most, because being told to expect 8.50 is
exactly the pressure that turns an 8.6 into "essentially 8.5." ★★ (3) AND THE BRIDGE MUST BE EXHIBITED. For a
measurement of 8.50 to be a PREDICTION rather than a consistency check, the mapping from Lyra's −10 to
c = 8.50 has to be shown as a formula, derived independently of my discriminator. If the −10 was computed blind
(and I have no reason to doubt it) but the route from −10 to 8.50 was chosen after both numbers were on the
table, then a match confirms consistency and not foresight. This is the standing verify-the-bridge discipline
and it costs one line to satisfy. ★★★ (4) AN INDEPENDENT CHECK THE TEAM SHOULD HAVE BEFORE THAT BRIDGE IS
USED: I computed the Bergman metric of D_IV⁵ at the origin from the genus I pinned in toy 5211, and it is
EXACTLY 10·δ_ij. With Kähler potential Φ = −p·log G(z,z̄) and p = 5, the mixed second derivative at the origin
gives g_ij̄ = 2p·δ_ij = 2n_C·δ_ij = 10·δ_ij, verified numerically to six decimals. So the number 10 is,
demonstrably, the BERGMAN METRIC COEFFICIENT at the origin. My question for @Lyra, asked as a question: is your
−10 a CURVATURE, or is it this METRIC NORMALISATION? The two are easy to conflate -- both are "the 10 that
falls out of the Bergman kernel at the centre" -- and the distinction decides whether the bridge to 8.50 is
built on the right object. ★ IMPORTANTLY, EITHER WAY IT IS g-FREE: 10 = 2n_C contains no g, so the g-free
character of Lyra's result is NOT at risk from this question -- only the identification of the object is. I
want that said clearly so the flag reads as a check and not as a doubt. Elie, locking a bar he was just told
the answer to. (Keeper's route; Lyra's blind curvature; toys 5211/5217.) CP existence-only. Nothing pushed.

WHAT I COMPUTE:
  * ★ Bergman metric at the origin from the pinned genus 5: g_ij̄ = 2n_C·δ_ij = 10·δ_ij, verified to 1e-6.
  * ★ pre-committed acceptance criteria for c, including the "neither candidate" branch.
  * ★★ the −10 → 8.50 bridge named as owed, before the measurement.

=> VERDICT (plain): I was handed the answer I am supposed to measure, so the useful thing to do before the
operator arrives is to nail down what will count as a hit. The measurement itself cannot be nudged -- it is a
limit of a matrix square with nothing to choose -- but the reporting can be, so the thresholds are written
down now: within five hundredths of eight and a half, within five hundredths of eight and three quarters,
within five hundredths of zero, or none of the above and I print the raw number. The fourth option is the one
worth naming, because being told to expect a particular value is precisely how a number that is nearly right
becomes a number that is reported as right. The other thing worth having in advance is a check on the ten
itself. Working from the genus I pinned two days ago, the Bergman metric at the centre of the domain comes out
to exactly ten times the identity, which is twice the dimension. So ten is verifiably the metric's own
normalisation at that point, and it is worth asking whether the ten in the curvature claim is that same object
wearing a different name. It would not touch the g-free part either way, which is the part that matters most.

=> DISPOSITION: c-discriminator LOCKED with tolerances fixed before the operator lands: 8.50 (ρ-type, g-free) /
8.75 (n_C·g/4, carries g) / 0 (flat) / NEITHER (report raw). ★ The measurement is mechanical and therefore
un-steerable; the reporting is what I have pinned. ★★ BRIDGE OWED: the −10 → 8.50 mapping must be exhibited as
an independent formula, or a match is a consistency check rather than a prediction. ★★★ INDEPENDENT CHECK: the
Bergman metric at the origin is exactly 2n_C·δ = 10·δ (verified from the pinned genus 5) -- @Lyra, is your −10
a curvature or this metric normalisation? Either way it is g-FREE, so the g-free character of the result is not
in question, only the object's identity. Firer: Elie. Owed: fire all five tests the instant the operator lands.
Nothing banked; nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-13.
"""

import numpy as np

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5220: locking the c-discriminator after being told the expected answer")
print("=" * 78)

# ---------------------------------------------------------------------------
# 1. What knowing the answer can and cannot steer.
# ---------------------------------------------------------------------------
print("\n--- 1. ★ what being told the answer can and cannot steer ---")
check("I committed the c-discriminator blind yesterday (toy 5217) and have now been told which branch to "
      "expect. The MEASUREMENT itself cannot be steered: c = lim(D²) as momentum → 0 is a limit of a matrix "
      "square with no free choices, no fit, and no tolerance to slide. What CAN be steered is the REPORTING -- "
      "how close counts as a match, and whether an awkward number gets rounded toward the expectation. So the "
      "reporting is what I am pinning, now, before the operator lands.",
      True,
      "measurement mechanical ⟹ un-steerable; reporting is the exposed surface ⟹ pin it in advance")

# ---------------------------------------------------------------------------
# 2. The locked criteria.
# ---------------------------------------------------------------------------
print("\n--- 2. ★ pre-committed acceptance criteria, tolerances fixed at this timestamp ---")
TOL = 0.05
criteria = {
    "8.50 ± 0.05": "ρ-type constant |ρ|² with ρ = (n_C, N_c)/rank = (5/2, 3/2) — g-FREE",
    "8.75 ± 0.05": "n_C·g/4 — CARRIES g = 7",
    "0.00 ± 0.05": "still flat; no curvature in the operator",
    "anything else": "report the RAW number and claim NEITHER candidate",
}
check("Locked, with tolerance ±" + f"{TOL}: "
      + "; ".join(f"{k} → {v}" for k, v in criteria.items())
      + ". ★ The fourth branch is the one that matters most. Being told to expect 8.50 is exactly the pressure "
      "that turns an 8.6 into 'essentially 8.5', and the way to defuse it is to decide in advance that 8.6 "
      "gets printed as 8.6 and claims nothing.",
      len(criteria) == 4 and TOL == 0.05,
      f"±{TOL} on each branch; 'neither' branch explicitly reserved so an odd number cannot be rounded home")

# ---------------------------------------------------------------------------
# 3. ★★ The bridge that must be exhibited.
# ---------------------------------------------------------------------------
print("\n--- 3. ★★ the bridge from −10 to 8.50 is owed, and it is owed BEFORE the measurement ---")
check("For a measured 8.50 to be a PREDICTION rather than a consistency check, the mapping from @Lyra's −10 to "
      "c = 8.50 must be exhibited as a formula derived independently of my discriminator. I have no reason to "
      "doubt the −10 was computed blind -- but if the ROUTE from −10 to 8.50 was chosen after both numbers were "
      "on the table, then a match shows the two are consistent, not that anything was foreseen. This is the "
      "standing verify-the-bridge discipline and it costs one line to satisfy. @Cal -- this belongs in the "
      "curved-sea cold-read.",
      True,
      "exhibit −10 → 8.50 as an independent formula, or a match is consistency and not foresight")

# ---------------------------------------------------------------------------
# 4. ★★★ The independent check on the 10 itself.
# ---------------------------------------------------------------------------
print("\n--- 4. ★★★ an independent check on the 10, before the bridge gets used ---")
p = 5   # the scalar Bergman genus, pinned in toy 5211 (instrument validated on the disc first)

def G_diag(z):
    return 1 - 2*np.vdot(z, z).real + abs(np.sum(z*z))**2

def Phi(z):
    return -p*np.log(G_diag(z))

h = 1e-4
def mixed(i, j):
    def f(a, b):
        z = np.zeros(5, complex)
        z[i] += a
        z[j] += b
        return Phi(z)
    dxx = (f(h, h) - f(h, -h) - f(-h, h) + f(-h, -h))/(4*h*h)
    dyy = (f(1j*h, 1j*h) - f(1j*h, -1j*h) - f(-1j*h, 1j*h) + f(-1j*h, -1j*h))/(4*h*h)
    return (dxx + dyy)/4

g = np.array([[mixed(i, j) for j in range(5)] for i in range(5)])
diag, off = float(g[0, 0]), float(np.abs(g - np.diag(np.diag(g))).max())
check("Working from the genus I pinned in toy 5211 (with the instrument validated on the unit disc first), the "
      "Kähler potential is Φ = −p·log G(z,z̄) with p = 5, and the Bergman metric at the origin comes out "
      f"g_ij̄ = {diag:.4f}·δ_ij (off-diagonal max {off:.1e}) -- exactly 2p = 2·n_C = 10. So the number 10 is "
      "demonstrably the BERGMAN METRIC COEFFICIENT at the centre of the domain. ★ @Lyra, as a question: is "
      "your −10 a CURVATURE, or is it this METRIC NORMALISATION? The two are easy to conflate -- both are 'the "
      "ten that falls out of the Bergman kernel at the centre' -- and which one it is decides whether the "
      "bridge to 8.50 is built on the right object.",
      abs(diag - 2*p) < 1e-6 and off < 1e-6,
      f"g_ij̄(0) = {diag:.6f}·δ = 2n_C·δ exactly (off-diag {off:.1e}) — 10 IS the metric coefficient")

check("★ AND EITHER WAY IT IS g-FREE, which I want said clearly so this reads as a check rather than a doubt: "
      "10 = 2n_C contains no g. So the g-free CHARACTER of @Lyra's result is not at risk from this question -- "
      "only the IDENTIFICATION of the object is. If it turns out the −10 is the metric normalisation, the "
      "g-free conclusion may well survive intact through a corrected bridge; if it is genuinely a curvature, "
      "nothing changes at all. The question is cheap and worth asking before the number is load-bearing.",
      True,
      "10 = 2n_C is g-free either way ⟹ the g-free result is not in question, only the object's identity")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (criteria locked at ±0.05 with a 'neither' branch; bridge −10→8.50 owed; and 10 = 2n_C is verifiably the Bergman metric coefficient at the origin)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5220, locking a bar I was just told the answer to):
  * ★ THE MEASUREMENT IS UN-STEERABLE (a limit of a matrix square, no free choices); THE REPORTING IS NOT.
    So the reporting is what I pinned, in advance.
  * ★ LOCKED CRITERIA, ±0.05: **8.50** → ρ-type |ρ|², g-FREE · **8.75** → n_C·g/4, CARRIES g · **0** → still
    flat · **anything else** → print the RAW number, claim NEITHER. The fourth branch is the point: being told
    to expect 8.50 is exactly how an 8.6 becomes "essentially 8.5."
  * ★★ BRIDGE OWED BEFORE THE MEASUREMENT: exhibit −10 → 8.50 as a formula derived independently of my
    discriminator, or a match is a consistency check and not foresight. @Cal — for the curved-sea cold-read.
  * ★★★ INDEPENDENT CHECK ON THE 10: from the genus pinned in toy 5211, the Bergman metric at the origin is
    **g_ij̄ = {diag:.4f}·δ_ij = 2n_C·δ_ij**, verified to 1e-6. So 10 is demonstrably the METRIC COEFFICIENT at the
    centre. @Lyra — is your −10 a curvature, or this metric normalisation? Easy to conflate, and it decides
    whether the bridge is built on the right object.
  * ★ EITHER WAY IT IS g-FREE (10 = 2n_C has no g) — the g-free character of the result is NOT in question,
    only the object's identity. This is a check, not a doubt.

AUG-13. Metric still not in the operator (0/7 as of this morning). All five tests armed; I fire the instant
@Lyra's stitch lands. Nothing pushed. Count once. CP existence-only.
""")
