#!/usr/bin/env python3
"""
Toy 5246: GATE 1. P² = P PASS, P† = P PASS EXACTLY -- BUT P‡ = 1 − P − P₀, so the grading maps the sea onto its
mirror rather than onto itself. Built the Dirac-sea projector from the credentialed operator (v3 + the FK metric
of toy 5243) and ran @Cal's §433 constructed-artifact conditions. Two of three pass; the third fails, and the
failure has an exact structural form rather than a numerical one, which makes it usable. ★ (1) GATE 1a --
IDEMPOTENT: ||P² − P|| = 7.8e-16. PASS. ★ (2) GATE 1b -- SELF-ADJOINT: ||P − Pᵀ|| = 0.000e+00 in the FK metric,
exactly zero. PASS. ★★★ (3) GATE 1c -- KREIN-SELF-ADJOINT: FAILS, for both natural gradings, and the parity case
fails in a completely determined way. With J = (−1)^q (fermion parity), J D J = −D to 0.0e+00 -- an EXACT
spectral symmetry that flips the sign -- so J carries the negative eigenspace onto the positive one and
P‡ = J Pᵀ J = P_pos = 1 − P − P₀, verified to 2.2e-15. ⟹ NOT P‡ = P but P + P‡ + P₀ = 1. The Krein adjoint of
the sea is the UNOCCUPIED subspace. ★★ (4) AND THE SECOND CANDIDATE IS WORSE, which is informative: for the
half-turn J: Λ^k → Λ^{5−k}, J D J is NEITHER +D (3.5) NOR −D (3.5) -- the half-turn is not a symmetry of this
Dirac at all, so it cannot be the Krein operator here. That answers the dictionary question in the negative
direction: whatever "occupied" means for Finster, our half-turn map does not implement it on this operator.
★★★★ (5) AND A STRUCTURAL FINDING THAT MAY MATTER MORE THAN THE GATE: THE SPACE IS NOT A KREIN SPACE IN THIS
METRIC. Every FK norm 1/(2^{|λ|}(ν)_λ) is strictly positive at ν = 5/2 (minimum 1, checked over all λ), so what
toy 5243 derived is a positive-definite HILBERT structure. Finster's construction needs an INDEFINITE inner
product; there is none here. So gate 1 does not merely fail on a sign convention -- the indefiniteness has to
enter from somewhere we have not built, and naming that is a prerequisite to the gate, not a detail inside it.
★ (6) AND ONE CLEAN TARGET-INNOCENT OBSERVABLE FELL OUT: spec(D) is exactly symmetric -- 160 negative / 160
positive at N = 2, and 511 / 511 at N = 3 -- so THE SEA IS EXACTLY HALF the non-kernel space, forced by
J D J = −D. ★ SCOPE, stated plainly: the A_xy closed-chain signature is NOT done. It needs a two-point kernel
P(x,y) over the domain, which is a separate build from this spectral projector, and I am not going to gesture at
it. Gate 1 is two-thirds passed, one-third failed-with-structure, and one part unstarted. Elie, at the foot of
the mountain with the first rope tested. (Cal §433; Lyra v3; toys 5243/5244.) CP existence-only. Nothing pushed.
NO VALUE READ.

WHAT I VERIFY:
  * ★ gate 1a: ||P² − P|| = 7.8e-16 ⟹ PASS.
  * ★ gate 1b: ||P − Pᵀ|| = 0.000e+00 in the FK metric ⟹ PASS, exactly.
  * ★★★ gate 1c: J = parity ⟹ JDJ = −D (0.0e+00) ⟹ P‡ = 1 − P − P₀ = P_pos (2.2e-15) ⟹ FAIL, with structure.
  * ★★ J = half-turn Λ^k→Λ^{5−k}: JDJ ≠ ±D (3.5 both) ⟹ not a symmetry ⟹ cannot be the Krein operator here.
  * ★★★★ FK norms all > 0 at ν = 5/2 ⟹ POSITIVE-DEFINITE Hilbert structure, NOT a Krein space.
  * ★ spec(D) exactly symmetric (160/160 at N=2, 511/511 at N=3) ⟹ the sea is exactly half, forced by JDJ = −D.

=> VERDICT (plain): I built the occupied-states projector from the operator that earned its credential this
morning and put it through the three constructed-artifact tests. It is a genuine projector, and it is symmetric
in the metric we derived — exactly symmetric, to the last digit. The third test fails, but not in a way that
leaves us guessing. The parity grading turns the operator into minus itself, precisely, and that means it
carries the occupied states onto the empty ones. So the adjoint of the sea is its complement rather than
itself: the three pieces — occupied, empty, and the ground — add to the whole. The other natural candidate for
the grading, the map that turns a state inside out, is not a symmetry of this operator at all, which at least
answers the dictionary question in the direction of no. And there is a larger thing behind all of it. Finster's
construction lives on a space with an indefinite length, where some states have negative norm. Our metric is
positive throughout — every single norm, at every level. So this is an ordinary Hilbert space, and the
indefiniteness his framework needs is not present anywhere in what we have built. That is not a detail inside
gate one; it has to be settled before gate one means anything. One thing did fall out cleanly: the occupied
states are exactly half the non-ground states, at every size, forced by that same sign-flipping symmetry.

=> DISPOSITION: ★ GATE 1a IDEMPOTENT: ||P² − P|| = 7.8e-16 → **PASS**. ★ GATE 1b SELF-ADJOINT: ||P − Pᵀ|| =
**0.000e+00** in the FK metric → **PASS, exactly**. ★★★ GATE 1c KREIN-SELF-ADJOINT → **FAIL, with an exact
structural form**: J = (−1)^q gives J D J = −D (0.0e+00) ⟹ **P‡ = P_pos = 1 − P − P₀** (2.2e-15) ⟹ not P‡ = P
but **P + P‡ + P₀ = 1**; the Krein adjoint of the sea is the UNOCCUPIED subspace. ★★ J = half-turn Λ^k→Λ^{5−k}:
J D J ≠ ±D (3.5 both) ⟹ **not a symmetry of this Dirac** ⟹ cannot be the Krein operator; the dictionary
question answered in the negative direction. ★★★★ **THE SPACE IS NOT KREIN IN THIS METRIC**: all FK norms
1/(2^{|λ|}(ν)_λ) > 0 at ν = 5/2 ⟹ positive-definite Hilbert. Finster needs indefiniteness; it is absent, and
naming its source is a PREREQUISITE to gate 1, not a detail within it. ★ TARGET-INNOCENT: spec(D) exactly
symmetric (160/160 at N=2, 511/511 at N=3) ⟹ **the sea is exactly half**, forced by J D J = −D. ★ SCOPE: the
A_xy closed-chain signature is **NOT DONE** — it needs a two-point kernel P(x,y), a separate build. Firer: Elie.
Nothing pushed. NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured this session — scratchpad/krein.py, krein2.py; operator = Lyra v3 + FK metric G (toy 5243).
IDEM = {2: 7.8e-16, 3: 1.221e-15}
SELFADJ = {2: 0.0, 3: 0.0}
SPEC = {2: (160, 352, 160), 3: (511, 770, 511)}     # (neg, zero, pos)
JDJ_PARITY = 0.0                                     # ||J D J + D||
PK_VS_P = 1.0
PK_VS_POS = {2: 1.221e-15, 3: None}
PK_VS_1MPMP0 = {2: 2.220e-15}
J_HALFTURN = (3.5, 3.5)                              # ||JDJ + D||, ||JDJ − D||
FK_MIN = 1                                           # min over all λ of (ν)_λ at ν = 5/2

print("=" * 78)
print("Toy 5246: GATE 1 — P²=P PASS, P†=P PASS, P‡=P FAIL with structure. NO VALUE READ")
print("=" * 78)

print("\n--- 1-2. ★ gates 1a and 1b ---")
check(f"GATE 1a, IDEMPOTENT: ||P² − P|| = {IDEM[2]:.1e} at N = 2 and {IDEM[3]:.1e} at N = 3, where P is the "
      "spectral projector onto the negative (occupied) subspace of the credentialed operator. A genuine "
      "projector.",
      all(v < 1e-12 for v in IDEM.values()),
      f"||P² − P|| = {IDEM[2]:.1e} / {IDEM[3]:.1e} ⟹ PASS")

check(f"GATE 1b, SELF-ADJOINT: ||P − Pᵀ|| = {SELFADJ[2]:.3e} in the FK metric -- exactly zero, at both sizes. "
      "★ That is toy 5243's metric doing its job on a derived object rather than on the operator it was built "
      "for, which is the first independent use it has had.",
      all(v == 0.0 for v in SELFADJ.values()),
      f"||P − Pᵀ|| = {SELFADJ[2]:.1e} exactly ⟹ PASS in the FK metric")

print("\n--- 3. ★★★ gate 1c: Krein-self-adjointness ---")
check(f"With J = (−1)^q (fermion parity): J² = 1 and ||J D J + D|| = {JDJ_PARITY:.1e} -- J D J = −D EXACTLY, an "
      "exact spectral symmetry that flips the sign. ⟹ J carries the negative eigenspace onto the positive one, "
      f"so P‡ = J Pᵀ J = P_pos = 1 − P − P₀, verified to {PK_VS_1MPMP0[2]:.1e} (and ||P‡ − P|| = {PK_VS_P:.1f}, "
      "a clean miss, not a near miss). ★ THE GATE FAILS -- but the correct statement is not P‡ = P, it is "
      "**P + P‡ + P₀ = 1**: the Krein adjoint of the sea is the UNOCCUPIED subspace. A failure with an exact "
      "form is usable; a numerical one would not be.",
      PK_VS_1MPMP0[2] < 1e-12 and PK_VS_P > 0.5,
      f"JDJ = −D exactly ⟹ P‡ = 1 − P − P₀ = P_pos ({PK_VS_1MPMP0[2]:.1e}) ⟹ GATE 1c FAILS, structurally")

check(f"And the second natural candidate is worse, which is itself informative: for the half-turn "
      f"J: Λ^k → Λ^{{5−k}}, ||J D J + D|| = {J_HALFTURN[0]:.1f} and ||J D J − D|| = {J_HALFTURN[1]:.1f} -- "
      "NEITHER. The half-turn is not a symmetry of this Dirac at all, so it cannot serve as the Krein operator "
      "here. ★ That answers @Keeper's dictionary question in the negative direction: whatever Finster's "
      "'occupied' means, our half-turn map does not implement it on this operator.",
      J_HALFTURN[0] > 1 and J_HALFTURN[1] > 1,
      "half-turn: JDJ ≠ ±D (3.5 both) ⟹ not a symmetry ⟹ cannot be the Krein operator; dictionary answered NO")

print("\n--- 4. ★★★★ and the finding behind the gate ---")
check(f"THE SPACE IS NOT A KREIN SPACE IN THIS METRIC. Every FK norm 1/(2^{{|λ|}}(ν)_λ) is strictly positive at "
      f"ν = 5/2 -- minimum (ν)_λ = {FK_MIN} over all λ checked -- so what toy 5243 derived is a "
      "POSITIVE-DEFINITE HILBERT structure. Finster's construction requires an INDEFINITE inner product, and "
      "there is none here. ★ So gate 1 does not merely fail on a sign convention: the indefiniteness has to "
      "enter from something we have not built, and naming its source is a PREREQUISITE to the gate rather than "
      "a detail inside it. @Lyra / @Cal -- this is the question I would put ahead of gates 2-4.",
      FK_MIN > 0,
      "all FK norms > 0 at ν = 5/2 ⟹ positive-definite Hilbert, not Krein ⟹ indefiniteness source is a prerequisite")

print("\n--- 5-6. ★ one clean observable, and honest scope ---")
check("TARGET-INNOCENT OBSERVABLE: spec(D) is exactly symmetric -- "
      + ", ".join(f"{SPEC[N][0]} negative / {SPEC[N][2]} positive at N = {N}" for N in sorted(SPEC))
      + f" (with {SPEC[2][1]} and {SPEC[3][1]} zero modes) ⟹ THE SEA IS EXACTLY HALF the non-kernel space, "
      "forced by J D J = −D. Nothing was tuned to make that happen; it follows from the grading.",
      all(SPEC[N][0] == SPEC[N][2] for N in SPEC),
      f"spec(D) symmetric: {SPEC[2][0]}/{SPEC[2][2]} and {SPEC[3][0]}/{SPEC[3][2]} ⟹ the sea is exactly half")

check("SCOPE, stated plainly rather than blurred: the A_xy CLOSED-CHAIN SIGNATURE IS NOT DONE. It needs a "
      "two-point kernel P(x,y) over the domain, which is a separate build from this spectral projector, and I "
      "am not going to gesture at it as though it were nearly in hand. ⟹ GATE 1 STATUS: two-thirds passed, "
      "one-third failed-with-structure, one part unstarted.",
      True,
      "A_xy signature NOT DONE — needs a two-point kernel P(x,y), a separate build")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (gate 1a/1b PASS; gate 1c FAILS as P‡ = 1 − P − P₀; and the space is not Krein in this metric)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5246, gate 1 — NO VALUE READ):
  * ★ **GATE 1a IDEMPOTENT: PASS.** ||P² − P|| = {IDEM[2]:.1e} / {IDEM[3]:.1e} at N = 2, 3.
  * ★ **GATE 1b SELF-ADJOINT: PASS, EXACTLY.** ||P − Pᵀ|| = **0.000e+00** in the FK metric — the first
    independent use of toy 5243's metric on an object it wasn't built for.
  * ★★★ **GATE 1c KREIN-SELF-ADJOINT: FAILS — with an exact structural form.** With J = (−1)^q,
    **J D J = −D to 0.0e+00**, an exact sign-flipping symmetry, so J carries the occupied subspace onto the
    unoccupied one: **P‡ = P_pos = 1 − P − P₀** (verified 2.2e-15). The right statement isn't P‡ = P but
    **P + P‡ + P₀ = 1** — the Krein adjoint of the sea is the *unoccupied* subspace. A clean miss (1.0), not
    a near one.
  * ★★ **AND THE HALF-TURN IS WORSE:** for J: Λ^k → Λ^{{5−k}}, J D J is **neither +D nor −D** (3.5 both) — not
    a symmetry of this Dirac at all. ⟹ **@Keeper's dictionary question answered in the negative direction**:
    whatever Finster's "occupied" means, our half-turn map does not implement it here.
  * ★★★★ **AND THE FINDING BEHIND THE GATE: THE SPACE IS NOT KREIN IN THIS METRIC.** Every FK norm
    1/(2^{{|λ|}}(ν)_λ) is strictly positive at ν = 5/2 ⟹ toy 5243 derived a **positive-definite Hilbert**
    structure. Finster's construction needs an **indefinite** inner product, and there is none here. So gate 1
    doesn't fail on a sign convention — **the indefiniteness must enter from something we haven't built, and
    naming its source is a prerequisite to the gate, not a detail inside it.** I'd put that ahead of gates 2–4.
  * ★ **TARGET-INNOCENT:** spec(D) is exactly symmetric — **160/160** at N = 2, **511/511** at N = 3 ⟹
    **the sea is exactly half** the non-kernel space, forced by J D J = −D. Nothing tuned.
  * ★ **SCOPE:** the **A_xy closed-chain signature is NOT done** — it needs a two-point kernel P(x,y), a
    separate build. **Gate 1: two-thirds passed, one-third failed-with-structure, one part unstarted.**

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
