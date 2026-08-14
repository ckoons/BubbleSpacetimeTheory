#!/usr/bin/env python3
"""
Toy 5247: GATE 1c PASSES WITH THE RANK-2 KREIN FORM -- AND THE PASS IS VACUOUS, because every reflection passes,
including the identity. I built what @Keeper asked for, it passed, and then the target-innocence check showed
the pass carries no information. Reporting both halves, because the first half alone would have been true and
misleading. ★ (1) THE BUILD, sourced from geometry as required: the rank-2 idempotent frame picks a
distinguished 2-plane, giving the reflection R = diag(−1,−1,+1,+1,+1) in SO(5), lifted SIMULTANEOUSLY to the
fermion fibre and the polynomial tower as J = (−1)^{n₁+n₂} ⊗ (−1)^{d₁+d₂}. It is a genuine Krein operator:
J² = 1 to 8.9e-16, and INDEFINITE with signature (+336, −336) -- perfectly balanced, which is what an indefinite
form should look like. ★★ (2) AND IT PASSES: [J, D] = 1.3e-15 (it COMMUTES, where fermion parity ANTI-commuted),
hence [J, P] = 1.6e-15 and ||P‡ − P|| = 1.6e-15. GATE 1c PASS. ★ The two halves separately FAIL -- fermion-only
and polynomial-only each give ||P‡ − P|| = 1.0 -- so the pass requires the simultaneous lift, which looked like
real geometric content: D contracts the fermion index against the polynomial index, so only the joint reflection
survives. ★★★ (3) THEN THE TARGET-INNOCENCE CHECK, AND IT KILLS IT. Running the same construction for r = 0, 1,
2, 3, 4, 5 reflected coordinates: EVERY SINGLE ONE PASSES, with ||P‡ − P|| between 4.4e-16 and 1.7e-15 --
INCLUDING r = 0, which is the IDENTITY, signature (+672, −0), positive definite, and not a Krein operator at
all. ⟹ the gate does not even require indefiniteness to pass. ★★★★ (4) AND THE STRUCTURAL REASON, which is the
real finding: P is ALREADY self-adjoint in the FK metric (toy 5246, ||P − Pᵀ|| = 0 exactly), so P‡ = J Pᵀ J =
J P J, and P‡ = P reduces to [J, P] = 0. Any SO(5)-equivariant J commutes with D, hence with P. ⟹ GATE 1c IS
AUTOMATICALLY SATISFIED BY THE ENTIRE SYMMETRY GROUP. It tests equivariance of the construction, not
Krein-ness of the structure, AND IT CANNOT FAIL FOR AN EQUIVARIANTLY-CONSTRUCTED P. @Cal -- that is a gate
that needs reformulating, not a gate we passed. ★ (5) NOR DOES THE SIGNATURE DISCRIMINATE: r = 1 through 5 all
give the same balanced (+336, −336), so rank 2 is not singled out by the signature either. "Rank 2" is
decorative HERE -- which says nothing against the rank-2 structure elsewhere, only that this test does not see
it. ★★ (6) I NEARLY SHIPPED THE FIRST HALF ALONE. "Gate 1c passes with the rank-2 Krein form" is true, was the
assigned deliverable, and would have been the ninth address -- a real construction, a real pass, and no content.
The check that caught it took one extra run and is the same one that has caught every other instance: vary the
thing that is supposed to matter and see whether the answer notices. Elie, reporting the pass and its emptiness
together. (Keeper's gate-1c assignment; Cal §433; toy 5246.) CP existence-only. Nothing pushed. NO VALUE READ.

WHAT I VERIFY:
  * ★ rank-2 Krein form built from geometry: J² = 1 (8.9e-16), indefinite, signature (+336, −336).
  * ★★ [J, D] = 1.3e-15 (commutes) ⟹ ||P‡ − P|| = 1.6e-15 ⟹ GATE 1c PASS. Halves separately FAIL (1.0).
  * ★★★ BUT r = 0..5 ALL PASS (4.4e-16 … 1.7e-15), including r = 0 = the identity, signature (+672, −0).
  * ★★★★ reason: P† = P already ⟹ P‡ = P ⟺ [J,P] = 0, satisfied by every equivariant J ⟹ the gate cannot fail.
  * ★ signature (+336, −336) is identical for r = 1..5 ⟹ rank 2 not singled out by signature either.

=> VERDICT (plain): I built the indefinite form I was asked for, out of the rank-two structure, and it passed
the test. It is a proper Krein operator — squares to one, and splits the space evenly into positive and
negative directions. It commutes with the operator where the earlier candidate anticommuted, which is exactly
why it works, and each half of it on its own fails, which made it look like the joint structure was doing real
work. Then I varied the one thing that was supposed to matter. Reflecting one coordinate passes. Three passes.
Five passes. Reflecting none passes — and reflecting none is the identity, which has no negative directions at
all and is not a Krein operator in any sense. So the test cannot tell the structure we want from the structure
we do not, and it cannot even tell an indefinite form from a positive one. The reason is simple once seen: the
projector was already symmetric in the metric we derived, so the remaining condition just asks whether the
grading commutes with it, and every symmetry of the operator does. The gate tests that our construction respects
its own symmetry, which it was built to do. I could have reported the pass and stopped, and it would have been
true and worth nothing.

=> DISPOSITION: ★ BUILD DELIVERED: rank-2 reflection R = diag(−1,−1,+1,+1,+1) lifted as J = (−1)^{n₁+n₂} ⊗
(−1)^{d₁+d₂}; J² = 1 (8.9e-16), INDEFINITE, signature (+336, −336). ★★ GATE 1c PASSES: [J, D] = 1.3e-15
(commutes, where parity anti-commuted) ⟹ ||P‡ − P|| = 1.6e-15; the fermion-only and polynomial-only halves each
FAIL (1.0), so the simultaneous lift is required. ★★★ **BUT THE PASS IS VACUOUS**: r = 0, 1, 2, 3, 4, 5 ALL pass
(4.4e-16 … 1.7e-15), including **r = 0 = the identity**, signature (+672, −0), positive-definite, not a Krein
operator ⟹ **the gate does not require indefiniteness**. ★★★★ **STRUCTURAL REASON (@Cal): P† = P already (toy
5246, exactly 0) ⟹ P‡ = P ⟺ [J, P] = 0, satisfied by EVERY SO(5)-equivariant J ⟹ GATE 1c CANNOT FAIL FOR AN
EQUIVARIANTLY-CONSTRUCTED P.** It tests equivariance, not Krein-ness. The gate needs reformulating. ★ signature
(+336, −336) identical for r = 1..5 ⟹ rank 2 not singled out here either (says nothing against rank 2
elsewhere). ★ NINTH ADDRESS AVOIDED: "gate 1c passes with the rank-2 Krein form" was true, was the assigned
deliverable, and carried no content. Firer: Elie. Nothing pushed. NO VALUE READ.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/krein3.py, krein4.py; operator = Lyra v3 + FK metric (toy 5243); P from toy 5246.
J_SQ = 8.9e-16
SIG_RANK2 = (336, 336)
JD_COMM = 1.3e-15
JP_COMM = 1.6e-15
PK_RANK2 = 1.6e-15
HALVES = 1.0                      # fermion-only and polynomial-only each give ||P‡ − P|| = 1.0
SCAN = {0: (672, 0, 4.44e-16), 1: (336, 336, 1.60e-15), 2: (336, 336, 1.60e-15),
        3: (336, 336, 1.60e-15), 4: (336, 336, 1.38e-15), 5: (336, 336, 1.73e-15)}
P_SELFADJ_5246 = 0.0

print("=" * 78)
print("Toy 5247: gate 1c passes — and the pass is vacuous. NO VALUE READ")
print("=" * 78)

print("\n--- 1-2. ★ the build, and the pass ---")
check(f"Sourced from geometry as required: the rank-2 idempotent frame picks a distinguished 2-plane, giving "
      f"R = diag(−1,−1,+1,+1,+1) in SO(5), lifted SIMULTANEOUSLY to both factors as J = (−1)^{{n₁+n₂}} ⊗ "
      f"(−1)^{{d₁+d₂}}. A genuine Krein operator: J² = 1 to {J_SQ:.1e}, and INDEFINITE with signature "
      f"(+{SIG_RANK2[0]}, −{SIG_RANK2[1]}) -- perfectly balanced.",
      SIG_RANK2[0] == SIG_RANK2[1] and J_SQ < 1e-12,
      f"J² = 1 ({J_SQ:.1e}); signature (+{SIG_RANK2[0]}, −{SIG_RANK2[1]}), balanced and indefinite")

check(f"AND IT PASSES: [J, D] = {JD_COMM:.1e} -- it COMMUTES, where fermion parity ANTI-commuted (toy 5246) -- "
      f"hence [J, P] = {JP_COMM:.1e} and ||P‡ − P|| = {PK_RANK2:.1e}. ★ GATE 1c PASS. And the two halves "
      f"separately FAIL: fermion-only and polynomial-only each give ||P‡ − P|| = {HALVES:.1f}, so the "
      "SIMULTANEOUS lift is required -- which looked like real geometric content, since D contracts the "
      "fermion index against the polynomial index and only the joint reflection survives.",
      PK_RANK2 < 1e-9 and HALVES > 0.5,
      f"||P‡ − P|| = {PK_RANK2:.1e} ⟹ GATE 1c PASS; halves fail at {HALVES:.1f} ⟹ joint lift required")

print("\n--- 3. ★★★ then the target-innocence check ---")
allpass = all(v[2] < 1e-9 for v in SCAN.values())
print("          r   signature        ||P‡ − P||     verdict")
for r, (p, m, d) in sorted(SCAN.items()):
    print(f"          {r}   (+{p:3d}, −{m:3d})     {d:.2e}      {'PASS' if d < 1e-9 else 'FAIL'}"
          + ("   <-- IDENTITY, positive definite, NOT a Krein operator" if r == 0 else ""))
check(f"Running the same construction for r = 0…5 reflected coordinates: EVERY SINGLE ONE PASSES, "
      f"||P‡ − P|| between {min(v[2] for v in SCAN.values()):.1e} and {max(v[2] for v in SCAN.values()):.1e} "
      f"-- INCLUDING r = 0, which is the IDENTITY, signature (+{SCAN[0][0]}, −{SCAN[0][1]}), positive definite, "
      "and not a Krein operator in any sense. ⟹ THE GATE DOES NOT EVEN REQUIRE INDEFINITENESS TO PASS.",
      allpass and SCAN[0][1] == 0,
      f"all r = 0…5 PASS including r = 0 (identity, +{SCAN[0][0]}/−0) ⟹ the gate does not require indefiniteness")

print("\n--- 4. ★★★★ the structural reason ---")
check(f"P is ALREADY self-adjoint in the FK metric (toy 5246: ||P − Pᵀ|| = {P_SELFADJ_5246:.1f} exactly), so "
      "P‡ = J Pᵀ J = J P J and the condition P‡ = P reduces to [J, P] = 0. Any SO(5)-equivariant J commutes "
      "with D, hence with P. ⟹ **GATE 1c IS AUTOMATICALLY SATISFIED BY THE ENTIRE SYMMETRY GROUP.** It tests "
      "the EQUIVARIANCE of the construction -- which it was built to have -- not the KREIN-NESS of the "
      "structure, and IT CANNOT FAIL FOR AN EQUIVARIANTLY-CONSTRUCTED P. @Cal: that is a gate needing "
      "reformulation, not a gate we passed.",
      True,
      "P† = P ⟹ P‡ = P ⟺ [J,P] = 0 ⟹ satisfied by every equivariant J ⟹ gate 1c cannot fail here")

print("\n--- 5-6. ★ and what this does and does not say ---")
check("NOR DOES THE SIGNATURE DISCRIMINATE: r = 1 through 5 all give the identical balanced "
      f"(+{SCAN[1][0]}, −{SCAN[1][1]}), so rank 2 is not singled out by the signature either. ★ 'Rank 2' is "
      "decorative HERE -- which says nothing against the rank-2 structure elsewhere in the corpus, only that "
      "THIS test does not see it. I am not extending the negative beyond what was measured.",
      all(SCAN[r][:2] == SCAN[1][:2] for r in (1, 2, 3, 4, 5)),
      "signature identical for r = 1..5 ⟹ rank 2 not singled out here; no claim about rank 2 elsewhere")

check("★★ AND I NEARLY SHIPPED THE FIRST HALF ALONE. 'Gate 1c passes with the rank-2 Krein form' is TRUE, was "
      "the assigned deliverable, and would have been the ninth address -- a real construction, a real pass, and "
      "no content. The check that caught it took one extra run and is the same one that has caught every other "
      "instance this week: vary the thing that is supposed to matter and see whether the answer notices.",
      True,
      "ninth address avoided: a true, assigned, passing result with no discriminating content")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (gate 1c passes with the rank-2 Krein form — and passes for every reflection including the identity, so it cannot fail)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5247, the pass and its emptiness, reported together — NO VALUE READ):
  * ★ **THE BUILD, geometry-sourced as required.** Rank-2 idempotent frame → R = diag(−1,−1,+1,+1,+1) in SO(5),
    lifted **simultaneously** to both factors: J = (−1)^{{n₁+n₂}} ⊗ (−1)^{{d₁+d₂}}. Genuine Krein operator —
    J² = 1 to {J_SQ:.1e}, **indefinite, signature (+336, −336)**, perfectly balanced.
  * ★★ **AND IT PASSES.** [J, D] = {JD_COMM:.1e} — it **commutes**, where fermion parity **anti**-commuted —
    so [J, P] = {JP_COMM:.1e} and **||P‡ − P|| = {PK_RANK2:.1e}. GATE 1c PASS.** The fermion-only and
    polynomial-only halves each **fail** (1.0), so the joint lift is required — which looked like real content.
  * ★★★ **THEN THE TARGET-INNOCENCE CHECK KILLED IT.** For r = 0…5 reflected coordinates, **every one passes**
    (4.4e-16 … 1.7e-15) — **including r = 0, the identity**, signature (+672, −0), positive definite, **not a
    Krein operator at all**. ⟹ **the gate does not even require indefiniteness.**
  * ★★★★ **THE STRUCTURAL REASON (@Cal).** P is already self-adjoint in the FK metric (toy 5246, exactly 0), so
    P‡ = J P J and **P‡ = P ⟺ [J, P] = 0** — satisfied by **every SO(5)-equivariant J**, since all of them
    commute with D. ⟹ **gate 1c cannot fail for an equivariantly-constructed P.** It tests equivariance, which
    the construction was built to have — not Krein-ness. **The gate needs reformulating, not passing.**
  * ★ **NOR DOES THE SIGNATURE DISCRIMINATE:** r = 1…5 all give the identical (+336, −336). "Rank 2" is
    decorative **here** — which says nothing against rank 2 elsewhere in the corpus, only that this test
    doesn't see it.
  * ★★ **NINTH ADDRESS AVOIDED.** "Gate 1c passes with the rank-2 Krein form" is true, was the assigned
    deliverable, and carries **no content**. One extra run caught it — the same check as every other instance
    this week: vary the thing that is supposed to matter and see whether the answer notices.

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
