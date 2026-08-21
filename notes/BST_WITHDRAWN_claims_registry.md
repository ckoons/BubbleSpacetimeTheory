---
title: "WITHDRAWN CLAIMS REGISTRY — the greppable record of dead results"
author: "Cal A. Brate (referee), per Round-40 assignment"
date: "2026-08-21"
status: "v0.2 — RATIFIED and Keeper-owned (K1778, 2026-08-21). Mechanism (tag + grep in the same action, claim-string as-in-the-wild) adopted standing. Cal seeded; Keeper maintains — per §603, the withdrawer must not be the sole keeper of his own withdrawal record. One open propagation hit: Paper67:144 (row W1)."
---

# Withdrawn claims registry

**Why this exists.** A withdrawal has no ID, so nothing propagates it. A theorem has an ID and can be grepped; a *retraction* lived only in a §-entry or a K-note, so a claim quoted into a paper before it died stayed there. **That is exactly how a selector I withdrew in §668 and killed in §670 reached `BST_Paper67:144` in a correction banner written to fix something else** (Cal §673, eighth instance of correction-lands-somewhere-not-everywhere).

**The mechanism is not the tag. It is the tag PLUS the grep, in the same action.**

## Protocol (three steps, one sitting)

1. **Add a row below.** The `claim string` field is **the phrase as it appears in the wild** — not a paraphrase. The grep is the whole mechanism, so the string must be the text that actually propagated.
2. **Immediately grep the corpus for that string.** `grep -rn "<claim string>" notes/`
3. **List every hit as an open propagation item** in the row. The row is not closed until the hits are.

**Step 2 is what was missing.** I withdrew in §668 and never grepped; the claim had already been quoted. **A tag nobody greps is a hold nobody propagates** (§661, Defect I).

**Scope, so this doesn't become a tax.** Step 2 tells you whether a row is needed at all: **grep first; if the claim never left the §-log, no row is required.** Rows are for claims that have been quoted somewhere.

**Known blind spot, stated at birth** (per the ORIGIN-CLASS discipline): this mechanism only works for claims with a distinctive **string**. A withdrawn *concept* — a scope, an identification, a tier — has no string, and inherits §661's Defect I unfixed. **Same limitation as the hold-propagation rule; not solved here.**

## Rows

| # | claim string (as it appears in the wild) | withdrawn by | date | reason | propagation hits |
|---|---|---|---|---|---|
| W1 | `bifurcation-surface dim 3 = n−2 → n=5` (and `dim 3` as a boundary-selector) | Cal §668 (withdrawn), §670 (killed) | 2026-08-21 | dim Fix(long wall) = 2 + m_long = **3 for every n**; returns "5" at n=7 where ∂_S is 7-dimensional. **Fails positive control.** | **`BST_Paper67:144` — CLOSED 2026-08-21. Fixed by Cal (closed-G-orbit asymmetry, "natural not forced", withdrawal cited inline so it can't be re-imported); Cal did NOT self-close (§603). ✅ KEEPER-VERIFIED (K1781): `grep -c "bifurcation-surface dim 3" = 0`; broader dead-selector strings return 0 across the lane; replacement reads "natural and pre-registered; it is not forced" at the correct tier.** Row CLOSED. |
| W2 | `𝒫-conjugacy` as a *forcing selector* | Cal §670 | 2026-08-21 | Circular under 𝒫_n (construction-guaranteed), constant under 𝒫_4. **Survives as the ADMISSIBILITY condition only.** | none found (never left the §-log) |
| W3 | `three independent selectors` / `confirmed three ways` (for confinement (ii)) | Cal §668, §671 | 2026-08-21 | One withdrawn (W1); remaining two are **one object** — the AdS_{n+1} conformal boundary and the unique closed G-orbit are the same manifold with the same action. **Multiplier 1.** | none found (caught before it was written) |
| W4 | `∂D_IV⁵ ≅ ℝ⁴` | Cal §667/§669; corrected by Lyra | 2026-08-21 | Compactness alone refutes it; three objects (dims 9, 5, 4) under one name. | `Paper67:142/154` — **CLOSED**; `T1271:55` — **CLOSED** |
| W5 | the descent is `falsifiable` (via the "off-slice baseline" / KK-tower / 1/r³ / anisotropy limbs) | **Keeper K1778 §3 (over-claim), withdrawn K1780** per Cal §676 | 2026-08-21 | A covariant boundary condition has **no local signature** — that's what makes it covariant; all three limbs can't fail, and "off-slice baseline" is what-would-happen-if-we-could-do-the-forbidden-thing. **"Induced, not predicted" (FORCED) stands; "falsifiable" does not** (needs a coupling strength → the frame-agreement test). Over-claiming falsifiability = over-claiming derivation. | `K1778` (headline/§3/disposition/filename) — **corrected in place** (banner added; filename retains the word, renaming breaks refs); `CI_BOARD.md` Round-40 block + `RUNNING_NOTES.md` Round-40 — **superseded by the Round-41 entries** (historical route blocks; not edited in place). Grep note: `falsifiable` is a common word — this row tracks the *descent* claim specifically, not every occurrence. |

| A2 | T2523's `(A) no free colored asymptotic states` **read as SU(3)/physical colour** ("a single colored quark is CONFINED", "including the adjoint gluon") | **Keeper K1782** per Cal §680 | 2026-08-21 | Contradicts **#108/T2567** (banked 2026-08-18: "no internal color; SU(3) entirely imported"); T2523's premise names Z_{N_c} = centre of SU(3), not in the geometry. Elie 5434: no SO(5)-equivariant operator confines the frame-dependent V₁₂ triplet. **13th same-name; two banked D-tier results contradicted for a month.** (A1) two-row theorem SURVIVES; (A2) SU(3)-reading out of scope. | **OPEN / OWED, pre-dispatch-critical.** ✅ Keeper sweep done (K1782a): the (A2) crossing is **6 flagship lines**, not one — `BST_FLAGSHIP_..._2026-07-18` **L62** (the core "no free colored states"), **L114** ("geometry forces non-abelian SU(3)" — distinct crossing), **L116/L126/L127/L201** ("colored→confined"/"color line"; L201 is load-bearing for the mass hierarchy — needs a judgment re-scope to the ν_W-radial reading, not deletion) + **`Lyra_T2523_addendum`**. Flagship already carries the CORRECT scoping at L62-end/L114-(ii)/L155/L172 → fix = make the 6 lines match (a deletion, Cal). **VERSION QUESTION (Lyra, answer first):** is the 2026-07-18 draft the dispatch target or superseded by the internal-SM v0.7 package (which is #108-consistent)? Route: Lyra re-scopes (or marks superseded); Cal vets the 4 items (8/8 sweep, adjoint-gluon test, T2529 edge, Grace reconciliation); Keeper gates + closes. T2523 registry entry re-scoped ✓. Row closes when the 6 lines grep clean OR the draft is marked superseded. |

## Routing log

| row | routed to | on | closes when |
|---|---|---|---|
| W1 | routed @Lyra (R41) → **fixed by Cal on Casey's directive (R42)**; verification **@Keeper** | 2026-08-21 | grep returns 0 ✓ **and a second party confirms** |

**A row is closed by a GREP, not by a report that it was fixed.** Content-ready is not cleared (§557/§601/§614): the registry closes on the instrument, not on agreement.

## Standing

**Rows W2 and W3 are the mechanism working as intended:** the grep at withdrawal time found nothing, so no propagation debt was incurred and no further action is owed. **Row W1 is the mechanism working retroactively** — it found the one hit that a timely grep would have caught two rounds earlier.

*— Cal A. Brate, 2026-08-21. Mechanism proposed, seeded with four rows.*

**— Keeper, K1778, 2026-08-21: RATIFIED and OWNED.** The mechanism is right and the §603 handoff is correct (an author is not the sole verifier of his own withdrawals). Standing rule adopted: every withdrawal adds a row + greps its claim-string in the same action; a row closes only when its propagation hits are all CLOSED. **Open action I now own: Paper67:144 (row W1) — Cal's dead bifurcation selector, still live in a pre-dispatch Millennium draft. Routed to the Paper67 owner; this registry does not go quiet until that row closes.** Blind spot inherited as stated (concepts have no greppable string — unfixed, same as §661 Defect I). Nothing pushed; CP existence-only.
