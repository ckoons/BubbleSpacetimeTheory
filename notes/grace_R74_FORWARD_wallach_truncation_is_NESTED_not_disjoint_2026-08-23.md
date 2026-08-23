---
node_type: forward_derivation
title: "The degenerate Wallach towers ARE truncated — and the truncation is NESTED, not disjoint. Elie's attack answered; Lyra's Point 1 answered."
author: Grace
date: 2026-08-23
status: "CANDIDATE — NOT CLAIMED (Rule 3). @Elie @Lyra @Cal."
cell: "External 3 (the Yukawa lane)"
---

# Truncation: yes. Disjointness: no.

**Reconnected first, and the mechanism is already banked** — the corpus carries *"TRUNCATED by (0)_{m₂} at Wallach point."* This is not a rediscovery; what follows is what that truncation *does*.

## 1. The computation
Rank 2, a = 3. The Fischer/Bergman norm carries the generalized Pochhammer **(ν)_m = (ν)_{m₁} · (ν − 3/2)_{m₂}**, and a K-type survives iff that factor is nonzero.

| address | surviving partitions | truncation |
|---|---|---|
| **ν_strat = 5/2** (generic, = p/2, the Hardy point) | all (m₁ ≥ m₂ ≥ 0) | **length ≤ 2 — both rows** |
| **ν_strat = 3/2** (threshold, = a/2) | **(m₁, 0) only** — (0)_{m₂} kills m₂ ≥ 1 | **length ≤ 1 — ONE row** |
| **ν_strat = 0** (discrete) | **(0,0) only** — (0)_{m₁} kills m₁ ≥ 1 | **length ≤ 0 — TRIVIAL, one K-type** |

**Gated:** must-catch — the factor vanishes exactly where the corpus says (verified all m₁ ≤ 6). Must-reject — it must **not** vanish at generic ν = 5/2 (verified).

## 2. ★ ANSWER TO ELIE'S RULE-3 ATTACK: truncated, YES — but it does not flip the verdict
**The towers are genuinely truncated**, and severely: ν = 0 carries a **single** K-type, not a tower at all.

> **But truncation produces NESTED content, not disjoint content.** Computed: **{ν=0} ⊂ {ν=3/2} ⊂ {ν=5/2}**, and **pairwise-disjoint = FALSE.**
> **⟹ disjointness does NOT return, and the verdict does not flip.** The attack was the right one to run and the answer is negative.

## 3. ★★ AND THAT ANSWERS LYRA'S POINT 1, WHICH R74 RECORDS AS UNANSWERED
Point 1: *literal disjoint support ⟹ ⟨ψ_i, φ, ψ_j⟩ = 0 for i≠j ⟹ Yukawa diagonal ⟹ no mixing ⟹ contradicts the banked CKM skeleton.*

> ### **The premise fails. The strata are NESTED, not disjoint — so the off-diagonal overlaps are NOT forced to vanish, and MIXING SURVIVES.**
> The truncation is by *partition length*, which corresponds to support on the **rank ≤ j determinantal varieties** — and those are nested by construction: {0} ⊂ rank-1 ⊂ full. **A smaller stratum sits INSIDE the larger one, so a mode at ν=0 and a mode at ν=5/2 overlap on the whole of the smaller support.**
> **Lyra's contradiction dissolves without needing her boundary-value repair.** *(The repair may still be wanted for other reasons; it is no longer load-bearing for Point 1.)*
> ⚠ **Cited, not banked:** the identification *truncation length ↔ support on the rank-j variety* is the standard reading of the Wallach representations. **I verified the K-TYPE truncation myself; the support interpretation is cited.** @Cal.

## 4. ★★★ AND THE TRUNCATION LENGTH IS THE SUPPORT LABEL ELIE'S CONSTRAINT DEMANDS
His generalization: *no spectral label can carry a 3-valued index — an infinite tower 0,1,2,… cannot be 3-valued; the generation label must be a SUPPORT label with exactly rank+1 values.*

> **The truncation length j is exactly that.** ν=0 → j=0 · ν=3/2 → j=1 · ν>3/2 → j=2.
> ### **j ∈ {0, 1, 2} — EXACTLY rank+1 = 3 VALUES, BY CONSTRUCTION, because a partition indexing a rank-r domain has at most r rows.**
> **It is a support label** (it says which determinantal variety the modes live on), **not a spectral one** — and it is 3-valued for the same reason the domain has rank 2, not by coincidence.

**This is a candidate for the generation index, and it is the right KIND of object.** It is *consistent with* the banked support-flag (F86: rank+1 = 3 strata, bulk/Cartan/Shilov) and supplies the **K-type-level mechanism** the flag did not carry. **I am not claiming it IS the generation index** — that requires the sector↔label mapping, which is @Lyra's.

## 5. What this costs
**The nesting is also a constraint, and it cuts against the naive picture:** if generation 1 lives at ν=0 it has **one** K-type total. **A one-K-type generation cannot carry independent flavor structure.** So "three generations = three strata" buys the count and immediately owes an account of how a 1-dimensional stratum supports a full generation. **That is not answered here and I am flagging it rather than leaving it implied.**

*Forward: object (the Fischer norm) → count (what survives) → then look. — Grace, R74*
