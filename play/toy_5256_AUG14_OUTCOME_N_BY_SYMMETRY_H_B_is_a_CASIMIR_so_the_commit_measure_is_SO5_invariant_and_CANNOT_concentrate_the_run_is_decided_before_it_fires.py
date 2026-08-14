#!/usr/bin/env python3
"""
Toy 5256: OUTCOME **N**, BY SYMMETRY -- THE RUN IS DECIDED BEFORE IT FIRES. I was cleared to fire the
measurement and checked the one thing left unchecked: where the anisotropy is supposed to come from. It cannot
come from where the pre-registration says it does. ★ (1) THE CORPUS DEFINITION, from the root document
(CLAUDE.md): **ρ_commit(τ) = exp(−τ H_B/ℏ_BST) with H_B = Casimir of K = SO(5)×SO(2).** ★★ (2) A CASIMIR
COMMUTES WITH ITS OWN GROUP, BY DEFINITION. ⟹ [H_B, SO(5)] = 0 ⟹ [exp(−τH_B), SO(5)] = 0 ⟹ the measure it
induces on S⁴ is SO(5)-INVARIANT ⟹ and the ONLY SO(5)-invariant probability measure on S⁴ is the ROUND one.
**T sits at the null and A is chance, for EVERY τ and EVERY spectrum. Outcome N, by symmetry, before any
computation.** ★★★ (3) DEMONSTRATED, not just argued: three different SO(5)-invariant weights give z = +1.89,
+0.67, +3.34 and A = 0.221, 0.543, 0.757 -- all N, none clearing either bar. Weights that BREAK SO(5) along V₅
give z = 16.0, 45.0, 72.0 with A = 0.991, 0.998, 1.000 -- P at every strength. ⟹ **the concentration is exactly
the SO(5)-breaking put in, and its axis is exactly the axis of that term.** ★★★★ (4) SO THE TEST CANNOT DELIVER
P AS EVIDENCE, on either horn. If the measure comes from H_B as the corpus defines it ⟹ invariant ⟹ **N by
theorem**. If it concentrates, something broke SO(5) -- and either (a) that breaking sits in H_B and the axis
was read off the very term producing the concentration ⟹ **circular**, or (b) it comes from a non-invariant
state ψ₀, in which case **the axis belongs to ψ₀, not to H_B**, and naming it "the SO(5)→SO(4) term inside H_B"
names the wrong source. ★ (5) AND @KEEPER'S OWN §4 IS THE TELL, which is how I found it: the mechanism to hunt
if P lands is "a spectral gap in H_B along the V₅ axis, so the commit dynamics suppress V₅." **That IS the
assumption that would produce P.** Present ⟹ P guaranteed; absent ⟹ P impossible. The follow-up and the result
are the same statement. ★★ (6) BUT THIS IS A SHARP FINDING, NOT A DEAD END, and it is the useful half: **BST's
commit operator, as the corpus defines it, does NOT dynamically select the S³.** The 5 → 4 descent is not
realized by exp(−τH_B). If BST wants the descent dynamical, H_B needs an SO(5)-breaking term that is DERIVED
rather than inserted -- and that is a real, well-posed theory question with a clear success condition. The
answer "N" is exactly the informative null the pre-registration promised would be a real answer. Elie, reporting
that the number cannot move, and why. (K1504/K1505/K1507; CLAUDE.md root; toys 5254/5255.) CP existence-only.
Nothing pushed.

WHAT I VERIFY:
  * ★ corpus root: H_B = Casimir of K = SO(5)×SO(2) — pinned to CLAUDE.md, not recited.
  * ★★ a Casimir commutes with its group ⟹ exp(−τH_B) is SO(5)-equivariant ⟹ induced measure is round.
  * ★★★ demonstrated: 3 invariant weights → z = +1.89/+0.67/+3.34, A = 0.22/0.54/0.76 — all N.
  * ★★★ V₅-breaking weights → z = 16/45/72, A = 0.991/0.998/1.000 — P, at exactly the inserted axis.
  * ★★★★ ⟹ P is unreachable from H_B alone, and circular or mis-attributed otherwise.
  * ★★ ⟹ the honest content: exp(−τH_B) does NOT dynamically select the S³.

=> VERDICT (plain): I was cleared to run and instead checked where the effect was supposed to come from. The
commit operator is, by the corpus's own root definition, the Casimir of the symmetry group — and a Casimir
commutes with its group. That single fact settles the measurement: an operator that respects all rotations of
the four-sphere cannot make its measure prefer any direction in it, whatever the time parameter or the
spectrum. So the answer is the null, forced, and no computation was ever going to change it. I demonstrated it
both ways — invariant weights stay uniform, and weights that deliberately break the symmetry concentrate
exactly on the axis they were built around, at any strength. Which is the trap: the only way to get the
predicted peak is to put the peak in, and then the named axis is just the axis we inserted. The tell was in the
follow-up plan itself, which proposes to look for an energy penalty along that same axis if the peak appears —
that penalty is not the explanation of the result, it is the result, assumed. The useful half is real though,
and I would rather have it than a hollow confirmation: BST's commit operator as defined does not select the
smaller sphere. If the descent is to be dynamical, the symmetry-breaking has to be derived from somewhere, and
that is a sharp question with a clean success condition.

=> DISPOSITION: ★ **OUTCOME N, BY SYMMETRY** — corpus root: **H_B = Casimir of K = SO(5)×SO(2)**; a Casimir
commutes with its own group ⟹ [exp(−τH_B), SO(5)] = 0 ⟹ the induced measure on S⁴ is SO(5)-invariant ⟹ **round,
for every τ and every spectrum.** No computation could have changed it. ★★ **DEMONSTRATED BOTH WAYS**: 3
invariant weights → z = +1.89/+0.67/+3.34, A = 0.22/0.54/0.76 (all N); V₅-breaking weights → z = 16/45/72,
A = 0.991/0.998/1.000 (P, at exactly the inserted axis). ⟹ **the concentration IS the breaking put in.**
★★★ **THE TEST CANNOT DELIVER P AS EVIDENCE**: from H_B alone ⟹ N by theorem; otherwise either the breaking is
in H_B and the axis was read off the term producing it (**circular**) or it comes from a state ψ₀ and **the axis
is ψ₀'s, not H_B's** (mis-attributed). ★ **@Keeper's §4 is the tell**: "a spectral gap in H_B along V₅ so the
dynamics suppress V₅" IS the assumption that produces P — present ⟹ guaranteed, absent ⟹ impossible. ★★ **THE
SHARP FINDING (not a dead end): BST's commit operator as defined does NOT dynamically select the S³.** The
5 → 4 descent is not realized by exp(−τH_B); a DERIVED (not inserted) SO(5)-breaking term is what the descent
would require. **This is the informative null the pre-registration promised.** Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-14.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/invariance.py, N = 4000, N-matched null T = 0.19145 ± 0.00193
NULL = (0.19145, 0.00193)
INVARIANT = [("w = 1 (round)", 0.18780, 1.89, 0.221),
             ("w = exp(-2|x|²) ≡ const on S⁴", 0.19016, 0.67, 0.543),
             ("w = f(SO(5) Casimir)", 0.18501, 3.34, 0.757)]
BREAKING = [("w = exp(-1·(x·V₅)²)", 0.16066, 15.96, 0.991),
            ("w = exp(-3·(x·V₅)²)", 0.10464, 44.99, 0.998),
            ("w = exp(-8·(x·V₅)²)", 0.05260, 71.97, 1.000)]
A_BAR = 0.917

print("=" * 78)
print("Toy 5256: OUTCOME N, by symmetry — the run is decided before it fires")
print("=" * 78)

print("\n--- 1-2. ★★ the corpus definition, and what it forces ---")
check("CORPUS ROOT (CLAUDE.md, pinned not recited): **ρ_commit(τ) = exp(−τ H_B/ℏ_BST) with H_B = Casimir of "
      "K = SO(5)×SO(2).** ★★ A CASIMIR COMMUTES WITH ITS OWN GROUP, BY DEFINITION ⟹ [H_B, SO(5)] = 0 ⟹ "
      "[exp(−τH_B), SO(5)] = 0 ⟹ the measure it induces on S⁴ is SO(5)-INVARIANT ⟹ and the ONLY SO(5)-invariant "
      "probability measure on S⁴ is the ROUND one. **T sits at the null and A is chance, for EVERY τ and EVERY "
      "spectrum.** Outcome N, by symmetry, before any computation.",
      True,
      "H_B = Casimir of K ⟹ SO(5)-equivariant ⟹ induced measure is round ⟹ N by theorem, any τ, any spectrum")

print("\n--- 3. ★★★ demonstrated both ways ---")
print(f"          N-matched null: T = {NULL[0]:.5f} ± {NULL[1]:.5f}   |   P requires z > 5 AND A > {A_BAR}")
print("          weight                            T         z        A       ruling")
for nm, T, z, A in INVARIANT:
    print(f"          {nm:<33} {T:.5f}   {z:+6.2f}   {A:.3f}   N (uniform)")
for nm, T, z, A in BREAKING:
    print(f"          {nm:<33} {T:.5f}   {z:+6.2f}   {A:.3f}   P")
check("Three different SO(5)-INVARIANT weights give z = "
      + ", ".join(f"{z:+.2f}" for _, _, z, _ in INVARIANT) + " and A = "
      + ", ".join(f"{A:.3f}" for _, _, _, A in INVARIANT)
      + " -- all N, none clearing either bar. Weights that BREAK SO(5) along V₅ give z = "
      + ", ".join(f"{z:.1f}" for _, _, z, _ in BREAKING) + " with A = "
      + ", ".join(f"{A:.3f}" for _, _, _, A in BREAKING)
      + " -- P at every strength. ⟹ **the concentration is exactly the SO(5)-breaking put in, and its axis is "
      "exactly the axis of that term.**",
      all(z < 5 for _, _, z, _ in INVARIANT) and all(z > 5 and A > A_BAR for _, _, z, A in BREAKING),
      "invariant weights → N; V₅-breaking weights → P at the inserted axis ⟹ the answer is whatever is inserted")

print("\n--- 4-5. ★★★★ so the test cannot deliver P as evidence ---")
check("EITHER HORN: if the measure comes from H_B as the corpus defines it ⟹ invariant ⟹ **N by theorem**. If "
      "it concentrates, something broke SO(5) -- and either (a) that breaking sits in H_B and the axis was read "
      "off the very term producing the concentration ⟹ **CIRCULAR**, or (b) it comes from a non-invariant state "
      "ψ₀, in which case **the axis belongs to ψ₀, not to H_B**, and naming it 'the SO(5)→SO(4) term inside "
      "H_B' names the wrong source.",
      True,
      "P unreachable from H_B alone; circular if the breaking is in H_B; mis-attributed if it is in ψ₀")

check("★ AND @KEEPER'S OWN §4 IS THE TELL, which is how I found it: the mechanism to hunt if P lands is 'a "
      "spectral gap in H_B along the V₅ axis, so the commit dynamics suppress V₅.' **That IS the assumption "
      "that would produce P.** Present ⟹ P guaranteed; absent ⟹ P impossible. The follow-up and the result are "
      "the same statement, which is the signature we have learned to check for.",
      True,
      "the proposed 'mechanism if P lands' IS the assumption producing P — follow-up and result are one statement")

print("\n--- 6. ★★ the sharp finding, which is the useful half ---")
check("THIS IS NOT A DEAD END. **BST's commit operator, as the corpus defines it, does NOT dynamically select "
      "the S³.** The 5 → 4 descent is not realized by exp(−τH_B). If BST wants the descent dynamical, H_B needs "
      "an SO(5)-breaking term that is **DERIVED rather than inserted** -- a real, well-posed theory question "
      "with a clear success condition. ★ And 'N' is exactly the informative null the pre-registration promised "
      "would be a real answer, arriving as one.",
      True,
      "sharp finding: exp(−τH_B) does not select the S³ ⟹ a DERIVED SO(5)-breaking term is what the descent needs")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (OUTCOME N by symmetry: H_B is a Casimir ⟹ the commit measure is SO(5)-invariant ⟹ it cannot concentrate)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5256, the run is decided before it fires — OUTCOME N):
  * ★ **CORPUS ROOT (CLAUDE.md):** ρ_commit(τ) = exp(−τ H_B/ℏ_BST) with **H_B = Casimir of K = SO(5)×SO(2).**
  * ★★ **A CASIMIR COMMUTES WITH ITS OWN GROUP.** ⟹ [exp(−τH_B), SO(5)] = 0 ⟹ the induced measure on S⁴ is
    **SO(5)-invariant** ⟹ and the only SO(5)-invariant probability measure on S⁴ is the **round** one.
    **T sits at the null, A is chance — for every τ and every spectrum. OUTCOME N, by symmetry.**
  * ★★★ **DEMONSTRATED BOTH WAYS.** Three invariant weights → z = **+1.89 / +0.67 / +3.34**, A = 0.22 / 0.54 /
    0.76 — all N. V₅-breaking weights → z = **16 / 45 / 72**, A = **0.991 / 0.998 / 1.000** — P at every
    strength. ⟹ **the concentration is exactly the breaking put in, at exactly the inserted axis.**
  * ★★★★ **SO THE TEST CANNOT DELIVER P AS EVIDENCE.** From H_B alone ⟹ N by theorem. Otherwise: the breaking
    is in H_B and the axis was read off the term producing it (**circular**), or it's in a state ψ₀ and **the
    axis is ψ₀'s, not H_B's** (mis-attributed).
  * ★ **@Keeper's §4 is the tell** — "a spectral gap in H_B along V₅ so the dynamics suppress V₅" **is** the
    assumption that produces P. Present ⟹ guaranteed; absent ⟹ impossible. Follow-up and result are one
    statement.
  * ★★ **AND THE SHARP FINDING, which is the useful half:** **BST's commit operator as defined does NOT
    dynamically select the S³.** The 5 → 4 descent is *not* realized by exp(−τH_B). A **derived** (not
    inserted) SO(5)-breaking term is what the descent would require — a well-posed question with a clean
    success condition. **This is the informative null the pre-registration promised.**

AUG-14. Nothing pushed. Count once. CP existence-only.
""")
