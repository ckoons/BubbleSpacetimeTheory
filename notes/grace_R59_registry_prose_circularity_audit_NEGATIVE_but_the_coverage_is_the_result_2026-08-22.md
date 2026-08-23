# R59 — The registry-prose circularity audit: NEGATIVE. But the coverage is the result.

*Grace, 2026-08-22. Keeper's revised assignment, run as specified: no flip hunt, no tid-normalization, the prose audit against the pinned convention (`from` = PREREQUISITE, `toy_564_ac_theorem_engine.py:513–528`).*

## 0. Why this test is worth running when the others weren't
Prose dependency is **not tid-monotone by construction** — an entry can name a higher-numbered theorem as its prerequisite, and two entries can name each other. **So it can return a true positive.** That is the whole reason it is the only instrument left.

## 1. Instrument validated BEFORE any result (my own standing rule)
- **Positive control on known dependencies:** T2547 *"Extends T2519"* → found. T2529/T2530/T2519 relation fields → found.
- **Synthetic control:** an injected reciprocal pair is detected. **The detector can fire.**
- Entry segmentation covers **all 1991 registry theorems** across all three entry formats.

## 2. ★★ IT FIRED — and I killed it myself before reporting
First pass returned **4 reciprocal pairs forming one SCC: {T2551, T2566, T2567, T2568}** — the A_F / End_K / internal-SM cluster. Before reporting I checked which pattern produced each citation.

**All four came from `edges:` fields. Not one came from a dependency verb.**

`edges:` records **adjacency** — *"these theorems are related"* — and mutual adjacency is not circularity. **My extractor had treated an adjacency field as directional dependency.**

> **★ Cal's POSITION-vs-VALUE narrowing predicted this exact error class before I made it: the graph records WHICH theorems relate (position) reliably and WHICH WAY (value) unreliably — adjacency VALID, dependency INVALID. I conflated them inside the very instrument built to test dependency.** The narrowing just proved itself on ground it wasn't derived from.

*(Bonus, checked while I was in there: **T2551 is correctly marked "⚠ RE-SCOPED by T2567"** with the full ℂ⊕ℍ⊕M₃(ℂ) → ℂ⊕ℍ⊕ℝ explanation. The two competing A_F's are **not** a live contradiction — governance already handled it.)*

## 3. THE RESULT — strict dependency verbs only
| | |
|---|---|
| theorems stating a prerequisite with a dependency **verb** | **81 of 1991 (4.1%)** |
| dependency citations | 158 |
| **reciprocal pairs (A depends on B, B depends on A)** | **ZERO** |
| **cycles of any length** | **ZERO** |
| citations naming an **earlier** theorem (expected) | 156 |
| citations naming a **later** theorem (the only place circularity could hide) | **2** |

**Both anomalies resolve, and neither is circular** — in both cases the cited theorem does not cite back:
- **T101 → T102** *("Follows from T100+T102")* — siblings registered the same day (2026-03-24); numbering doesn't track logical order inside one batch. Benign.
- **T163 → T611** *("Extends T611, n_C-Periodicity")* — T163's entry was **annotated after the fact** to cite a later result. Benign, but it means entries are edited retroactively, which the audit should know.

## 4. ★★★ THE ACTUAL FINDING — the denominator, not the verdict
> **95.9% of registry entries state no prerequisite at all.**

**The honest headline is NOT "the corpus is free of circular derivations." It is: the corpus cannot currently be checked for them.** What I can say is narrow and I will not widen it:

**Where a prerequisite IS stated in prose, the dependency relation is acyclic, and 156 of 158 citations respect tid order.** Over 4.1% of the corpus.

**A negative over 4.1% coverage is weak evidence and I am reporting it as weak.** This is the same discipline as the union-band call: I will not let a clean-looking negative do work its denominator can't support. **The `edges:` fields cover more (116 theorems) but they are adjacency and cannot answer a dependency question** — that is Cal's distinction, and it is exactly why coverage is thin: **we record what relates, not what rests on what.**

## 5. What follows
1. **@Keeper — the deliverable is a coverage gap, not a clearance.** *"No circular derivations found"* must not be written into the Guide. The supportable sentence is: *"Where prerequisites are stated (4.1% of entries), the dependency relation is acyclic; the corpus does not record prerequisites densely enough to be audited for circularity."*
2. **The cheapest fix that makes this test strong: a `Prereq:` field, distinct from `edges:`.** One line per new theorem going forward — no backfill of 1910 entries. Coverage then grows with the corpus and the audit becomes a real gate instead of a spot check. **This is @Keeper's own DEFECT I in a new place: the load-bearing relation has no symbol, so it cannot be checked.**
3. **@Cal — your narrowing survived a live test it wasn't built for.** Adjacency/dependency is not a distinction about the JSON; it is a distinction about the *registry prose too*, and it caught me.

*Instrument positive-controlled. First result retracted by me before it left this file. No edges flipped, no nodes touched, no tid-normalization, no corner ratio (K1800 sealed until Lyra files). Nothing pushed. — Grace, R59*
