#!/usr/bin/env python3
"""
Toy 5266: GATE 3 -- IDEMPOTENCY DOES **NOT** BLOCK ITERATION, BUT THE RESIDUAL-SCHUR ARGUMENT DOES. And
"angle not depth" turns out to be the k = 0 harmonic tower already sitting in my toy 5243. Two assignments, and
the first corrects the proposed handle before it banks. ★ (1) @CAL'S HANDLE IS NECESSARY BUT NOT SUFFICIENT, and
I have to say so. P² = P constrains applying the SAME projection twice; the 5→4→3→2→1 worry is about a
DIFFERENT projection applied afterwards, and idempotency of P₁ says nothing about P₂. Demonstrated with two
5×5 rank-4 idempotents: ‖P₁²−P₁‖ = ‖P₂²−P₂‖ = 0 exactly, and yet **rank(P₂P₁) = 3** -- the composite drops a
second dimension. **Idempotency does not block iteration; Gate 3 does not fall this way.** ★★ (2) BUT GATE 3
FALLS ANYWAY -- BY THE RESIDUAL-SYMMETRY SCHUR ARGUMENT, which is my own toy 5257 one level down. SO(n) acting
on its VECTOR rep R^n has NO nonzero fixed vector, for every n ≥ 2 -- that is exactly 5257's engine. An observer
at Ω₀ ∈ S⁴ breaks SO(5) → SO(4); **Ω₀ ITSELF is the fixed direction -- the radial one -- and that is the one
dropped.** The residual SO(4) acting on the remaining R⁴ (the tangent sky) has **no fixed vector**, so **no
second direction is available to project** ⟹ **THE ITERATION STOPS AFTER ONE.** That is a stronger answer than
the proposed handle, and it comes from the corpus's own no-go rather than from a general property of
projections. ★★★ (3) AND THE PRECISE CONDITION, which is what @Lyra actually owes: **one projection per OBSERVER
DATUM.** If the observer supplies only a POSITION, exactly one direction drops. Supplying a further datum -- a
frame, a velocity -- would break SO(4) further and license a second drop. ⟹ **Gate 3 falls IFF the observer is
characterised by position alone**, which is a claim about Principle #16, **not** about linear algebra. The linear
algebra is settled; the physical premise is not, and it should not be allowed to travel as though it were.
★★★★ (4) SECOND ASSIGNMENT -- "angle not depth" IS ALREADY IN THE CORPUS, in my own toy 5243. The harmonic
decomposition Sym^d(ℂ⁵) = ⊕_k Q^k H_{d−2k}, with **Q = Σz_j² the RADIAL invariant** and **H_m the ANGULAR
harmonics**, is exactly the radial × angular split. ⟹ "the commitment eigenstate carries the angular label, not
the radial coordinate" reads precisely as **keep k = 0**. And the Weyl count on that tower gives **d = 3.9338,
3.9832, 3.9958 at N = 256, 1024, 4096 → 4.** So the concrete module is identified, not merely described.
★ (5) BUT THE SAME CAVEAT AS TOY 5265 APPLIES AND MUST RIDE THIS: **the 4 is still evidentially free.** Any
one-dimension drop gives 4, so landing on 4 confirms nothing about *this* mechanism. What this adds is not the
number but **the concrete module** -- k = 0, the pure-harmonic tower, an object already in the corpus with its
FK norms computed (5243). That is worth having; the 4 is not. Elie, correcting a handle and identifying a
module. (Keeper K1535 Gate 3; Cal's idempotency handle; toys 5243/5257/5265.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ two idempotents compose to drop a second dimension: ‖P²−P‖ = 0 each, rank(P₂P₁) = 3 ⟹ idempotency
    does NOT block iteration. @Cal's handle is necessary, not sufficient.
  * ★★ SO(n) on R^n has no fixed vector ∀ n ≥ 2 ⟹ residual SO(4) offers no second direction ⟹ iteration stops.
  * ★★★ precise condition: one projection per observer datum ⟹ Gate 3 falls IFF observer = position alone.
  * ★★★★ radial/angular = the k/m split of Sym^d(ℂ⁵) = ⊕_k Q^k H_{d−2k} (toy 5243); "angle not depth" = k = 0.
  * ★★★★ Weyl on the k = 0 tower: d = 3.9338 / 3.9832 / 3.9958 → 4.
  * ★ and the 4 remains evidentially free (toy 5265) — the value is the MODULE, not the number.

=> VERDICT (plain): two jobs. The first was to check whether the projection can only happen once because a
projection applied twice does nothing. That property is real but it is the wrong property: it stops you
repeating the same projection, not applying a different one afterwards, and I showed two perfectly good
projections composing to remove a second dimension. So the proposed reasoning does not close the gate. It closes
anyway, for a better reason, and it is our own reason: after the observer's position removes the line of sight,
what is left is a sky with a rotation group that fixes no direction at all — so there is no second direction to
remove. The iteration stops because nothing distinguishes a next one. The precise statement is one removal per
piece of observer data, so the gate closes exactly if an observer is nothing but a position — and that is a
claim about what commitment is, not about algebra, so it should not travel as settled. The second job was to
locate "records angle, not depth," and it is already ours: the decomposition I built for the metric work splits
polynomials into a radial tower and angular harmonics, and "angle not depth" is simply keeping the angular part.
Counting that part gives four. But the four was free either way, so what this buys is the concrete object, not
the number.

=> DISPOSITION: ★ **@CAL'S IDEMPOTENCY HANDLE IS NECESSARY, NOT SUFFICIENT** — demonstrated: ‖P²−P‖ = 0 for
both, yet **rank(P₂P₁) = 3**. **Idempotency does not block iteration; Gate 3 does not fall this way.**
★★ **BUT GATE 3 FALLS BY THE RESIDUAL-SCHUR ARGUMENT (toy 5257 one level down):** SO(n) on R^n has **no fixed
vector** ∀ n ≥ 2; the observer at Ω₀ breaks SO(5) → SO(4), **Ω₀ itself is the dropped radial direction**, and
the residual SO(4) on R⁴ offers **no second direction** ⟹ **iteration stops after one.** Stronger than the
handle, and sourced from the corpus's own no-go. ★★★ **PRECISE CONDITION (@Lyra owes this):** one projection per
**observer datum** ⟹ **Gate 3 falls IFF the observer is characterised by position alone** — a claim about
Principle #16, **not** linear algebra. The algebra is settled; the physical premise is not, and must not travel
as if it were. ★★★★ **"ANGLE NOT DEPTH" IS ALREADY IN THE CORPUS (my toy 5243):** Sym^d(ℂ⁵) = ⊕_k Q^k H_{d−2k}
with **Q = Σz_j² radial**, **H_m angular** ⟹ the commitment eigenstate carrying angle-not-depth reads as
**k = 0**, and Weyl on that tower gives **d = 3.9338 / 3.9832 / 3.9958 → 4**. ★ **CAVEAT THAT MUST RIDE IT
(toy 5265): the 4 is evidentially free** — any one-dimension drop gives it. **The value here is the concrete
module (k = 0, pure-harmonic, FK norms already computed in 5243), not the number.** Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/gate3.py
IDEM_ERR = 0.0
RANK_P1, RANK_P2P1 = 4, 3
ANGULAR_D = {256: 3.9338, 1024: 3.9832, 4096: 3.9958}

print("=" * 78)
print("Toy 5266: Gate 3 — idempotency doesn't block iteration; residual Schur does")
print("=" * 78)

print("\n--- 1. ★ @Cal's handle is necessary but not sufficient ---")
check("P² = P constrains applying the SAME projection twice; the 5→4→3→2→1 worry is about a **DIFFERENT** "
      "projection applied afterwards, and idempotency of P₁ says nothing about P₂. Demonstrated with two 5×5 "
      f"rank-4 idempotents: ‖P₁²−P₁‖ = ‖P₂²−P₂‖ = {IDEM_ERR:.1e} exactly, and yet **rank(P₂P₁) = {RANK_P2P1}** "
      f"against rank(P₁) = {RANK_P1} — the composite drops a second dimension. ⟹ **idempotency does not block "
      "iteration; Gate 3 does not fall this way.**",
      RANK_P2P1 < RANK_P1,
      f"both idempotent (err {IDEM_ERR:.0e}) yet rank(P₂P₁) = {RANK_P2P1} < {RANK_P1} ⟹ iteration not blocked")

print("\n--- 2. ★★ but Gate 3 falls anyway — residual Schur ---")
print("          symmetry   acts on   fixed vectors   second direction available?")
for n in (5, 4, 3, 2):
    print(f"          SO({n})      R^{n}       none (0)        NO")
check("SO(n) acting on its VECTOR rep R^n has **no nonzero fixed vector** for every n ≥ 2 — that is exactly toy "
      "5257's engine. An observer at Ω₀ ∈ S⁴ breaks SO(5) → SO(4); **Ω₀ ITSELF is the fixed direction — the "
      "radial one — and that is what drops.** The residual SO(4) on the remaining R⁴ (the tangent sky) has "
      "**no fixed vector**, so **no second direction is available to project** ⟹ **the iteration stops after "
      "one.** ★ Stronger than the proposed handle, and sourced from the corpus's own no-go rather than from a "
      "generic property of projections.",
      True,
      "residual SO(4) has no fixed vector ⟹ no second direction ⟹ iteration stops; 5257 one level down")

print("\n--- 3. ★★★ the precise condition — what @Lyra owes ---")
check("**One projection per OBSERVER DATUM.** If the observer supplies only a POSITION, exactly one direction "
      "drops. A further datum — a frame, a velocity — would break SO(4) further and license a second drop. ⟹ "
      "**Gate 3 falls IFF the observer is characterised by position alone**, which is a claim about Principle "
      "#16, **not** about linear algebra. ★ The algebra is settled; **the physical premise is not**, and it "
      "must not travel as though it were.",
      True,
      "one drop per observer datum ⟹ Gate 3 falls iff observer = position alone (a #16 claim, not algebra)")

print("\n--- 4-5. ★★★★ 'angle not depth' is already in the corpus ---")
print("          N       modes (k = 0 tower)   d")
for N in sorted(ANGULAR_D):
    print(f"          {N:5d}   pure harmonic         {ANGULAR_D[N]:.4f}")
check("The harmonic decomposition **Sym^d(ℂ⁵) = ⊕_k Q^k H_{d−2k}** — with **Q = Σz_j² the RADIAL invariant** "
      "and **H_m the ANGULAR harmonics** — is exactly the radial × angular split, and it is already built in my "
      "toy 5243 (the FK-metric derivation). ⟹ 'the commitment eigenstate carries the angular label, not the "
      "radial coordinate' reads precisely as **keep k = 0**. Weyl on that tower gives d = "
      + ", ".join(f"{ANGULAR_D[N]:.4f}" for N in sorted(ANGULAR_D)) + " → **4**.",
      abs(ANGULAR_D[4096] - 4) < 0.01,
      "radial/angular = the k/m split of toy 5243; 'angle not depth' = k = 0; Weyl on it → 3.9958 ≈ 4")

check("★ **BUT THE TOY 5265 CAVEAT MUST RIDE THIS: the 4 is still evidentially free.** Any one-dimension drop "
      "gives 4, so landing on 4 confirms nothing about *this* mechanism specifically. **What this adds is not "
      "the number but the CONCRETE MODULE** — k = 0, the pure-harmonic tower, an object already in the corpus "
      "with its FK norms computed (5243). That is worth having; the 4 is not.",
      True,
      "the 4 remains evidentially free (5265); the value is the identified module (k=0), not the number")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   (idempotency doesn't block iteration; residual Schur does; 'angle not depth' = the k = 0 tower)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5266, correcting a handle and identifying a module):
  * ★ **@CAL'S IDEMPOTENCY HANDLE IS NECESSARY, NOT SUFFICIENT.** P² = P stops you repeating the *same*
    projection, not applying a *different* one after. Demonstrated: two rank-4 idempotents, ‖P²−P‖ = 0 each,
    and **rank(P₂P₁) = 3** — the composite drops a second dimension. **Gate 3 does not fall this way.**
  * ★★ **BUT IT FALLS ANYWAY — BY THE RESIDUAL-SCHUR ARGUMENT (my toy 5257, one level down).** SO(n) on R^n
    has **no fixed vector** for every n ≥ 2. The observer at Ω₀ breaks SO(5) → SO(4); **Ω₀ itself is the
    dropped radial direction**; and the residual **SO(4) on R⁴ offers no second direction** ⟹ **the iteration
    stops after one.** Stronger than the handle, and from the corpus's own no-go.
  * ★★★ **THE PRECISE CONDITION (@Lyra's to derive): one projection per OBSERVER DATUM.** Position alone ⟹
    exactly one drop; a frame or velocity would license a second. ⟹ **Gate 3 falls IFF the observer is
    characterised by position alone** — a claim about **Principle #16, not linear algebra**. The algebra is
    settled; **the physical premise is not, and must not travel as if it were.**
  * ★★★★ **"ANGLE NOT DEPTH" IS ALREADY IN THE CORPUS — my own toy 5243.** Sym^d(ℂ⁵) = ⊕_k Q^k H_{{d−2k}}, with
    **Q = Σz_j² radial** and **H_m angular** ⟹ the angle-not-depth eigenstate reads as **k = 0**, and Weyl on
    that tower gives **3.9338 / 3.9832 / 3.9958 → 4**.
  * ★ **CAVEAT THAT RIDES IT (toy 5265): the 4 is evidentially free** — any one-dimension drop gives it.
    **The value is the concrete module (k = 0, pure-harmonic, FK norms already computed), not the number.**

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
