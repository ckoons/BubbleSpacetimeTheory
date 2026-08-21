# K1773 — the Šilov ≅ ℝ⁴ collision is in TWO load-bearing places, not one

**Filed:** 2026-08-21
**Trigger:** Cal §667 caught `∂D_IV⁵ ≅ ℝ⁴` in Paper67 from a convenience sample (3/5, his own "not a corpus rate" caveat). Keeper swept the corpus for every instance — the correction isn't complete until every one is found (Cal's own index rule #5).
**Verdict:** PRE-DISPATCH-BLOCKING. Two load-bearing instances, both running Bisognano–Wichmann reconstruction through a 5D≅4D identity. Routed to Cal + Lyra for the physics adjudication; Keeper gates the correction.

---

## What the sweep found

The collision is in **two** places, not one:

1. **`BST_Paper67_Millennium_Closure_Draft.md:142, 154`** (Cal's catch): "Shilov boundary ∂D_IV⁵ ≅ ℝ⁴" — asserted as an isomorphism, BW run through it.
2. **`BST_T1271_YM_Physical_Uniqueness_Closure.md:55`** (NEW — Keeper): *"the boundary ∂D_IV⁵ ≅ ℝ⁴ (Shilov boundary, conformal compactification) coincide with the modular data of any ℝ⁴ QFT satisfying W1-W5 with the same mass gap."*

The second is arguably **more** load-bearing than the first — it is a **registered theorem note** for the Yang–Mills physical-uniqueness closure, and the ≅ℝ⁴ is doing real work in the argument (the modular-data match is against "any ℝ⁴ QFT"). Cal's convenience sample skipped it; the sweep caught it. This is precisely why a convenience sample is not a corpus rate.

**Corroborating context (not itself a collision):** `notes/.running/MESSAGES_2026-04-24.md:1067` — *"R⁴ vs Shilov boundary | HONEST — correctly notes Clay requires ℝ^{3,1}. BST position: spacetime IS the boundary."* The honest framing was on record in April: the BST position is that observed spacetime **is** the boundary — i.e. the **5D Šilov** branch, which owes the 5D→4D detection map. **The `≅ℝ⁴` shorthand is what collapsed the 5D boundary to 4D and buried that debt.**

## Why it is an error, not a defensible shorthand

- The Šilov boundary of D_IV⁵ is **(S⁴×S¹)/ℤ₂, real dim 5** = the conformal compactification of **5D** Minkowski (Elie 5422, Round 35). It is **NOT** ≅ ℝ⁴ (dim 4).
- ℝ⁴ (4D) is the **descent's** conformal boundary — (S³×S¹)/ℤ₂ — reached by the KK reduction that is itself the **open debt** (Cal §666 / K1772: selecting the 5D Šilov makes the 5D→4D map unavoidable).
- Writing "∂D_IV⁵ ≅ ℝ⁴" imports the **AdS₅/CFT₄ off-by-one** (Cal §323): the assumption that a bulk's boundary is one dimension lower. The Šilov boundary is the *distinguished* boundary (dim = complex dim = 5), not the AdS conformal boundary.

So both notes compare the D_IV⁵ modular data to "any **ℝ⁴** QFT" when the physical boundary the modular data actually live on is **5D**. That is not a typo — it is a **dimension mismatch inside the load-bearing step** of a uniqueness argument.

## What it does and does not threaten (scope — do not over-read)

- The YM uniqueness closure is **already scoped down** (CLAUDE.md / K937/K939: YM's gap is LARGE; the closure is domain-construction + (A) color-confinement + AF-sign, NOT the full Clay mass-gap). So T1271's ≅ℝ⁴ is a wrong statement inside an **already-attenuated** claim — correcting it does not destabilize a load-bearing PASS, because there isn't one.
- In fact the correction is **clarifying, not destabilizing**: the physical boundary is 5D, the 4D-ness is the open descent debt — which is exactly *why* the YM mass-gap-on-ℝ⁴ was never closed. Correcting ≅ℝ⁴ makes the honest scoping visible instead of papering it with a false isomorphism.
- **What Cal + Lyra must adjudicate (physics, not mine):** does the BW/Borchers uniqueness argument survive when the boundary is 5D (compare to a 5D QFT, then descend), or does the 5D→4D map have to be supplied first (in which case the argument is downstream of the descent debt)? The correct restatement is theirs to write; I gate it.

## Disposition

- **PRE-DISPATCH-BLOCKING:** neither Paper67 nor T1271 ships until the ≅ℝ⁴ is corrected to the 5D Šilov and the BW step re-examined at the right dimension.
- Routed to **Cal** (the BW/modular argument) + **Lyra** (the two notes' text). Apply the new dimension-tag rule while correcting: ∂_S = (S⁴×S¹)/ℤ₂ **(dim 5)**, ℝ⁴ **(dim 4)** — greppable, so the next instance can't hide.
- **Sweep-after-fix:** when the correction lands, re-run this grep — the collision propagated to two notes from one shorthand; assume it can be in a third until the grep returns clean.
- No unilateral edit by Keeper — these are Cal's/Lyra's arguments; I found the instances and gate the fix.

— Keeper, K1773.
