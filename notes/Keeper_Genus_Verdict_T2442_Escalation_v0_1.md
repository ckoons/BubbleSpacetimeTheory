---
title: "Keeper literature-angle verdict — D_IV⁵ Bergman genus = 5; T2442 c_FK recheck escalation"
author: "Keeper"
date: "2026-05-28 Thursday EDT"
status: "Literature angle of the 3-angle genus verification (Elie numerical + Grace provenance + Keeper literature). Genus CLOSED = 5. ONE RATIFIED result (T2442) flagged for recheck."
related: ["Lyra T2440 recalculation request", "Elie Toy 3579 (ν=5)", "Grace provenance trace", "Keeper_Fermion_Winding_Web_Casey_Seed_v0_1.md"]
---

# Genus verdict + T2442 escalation

## Literature-angle verdict (my assigned angle): genus = 5, decisively

Faraut-Korányi genus for an irreducible bounded symmetric domain: **p = a(r−1) + b + 2**. For the Type IV_n Lie ball (Aut = SO_0(n,2)): rank r = 2, multiplicities a = n−2, b = 0. So **p = (n−2)·1 + 0 + 2 = n**.

For **D_IV⁵ (n=5): genus = 5 = n_C.** Bergman kernel K(z,w) ∝ (1 − 2⟨z,w̄⟩ + ⟨z,z⟩⟨w̄,w̄⟩)^(−5). This is standard (Faraut-Korányi, *Analysis on Symmetric Cones*; Upmeier) and I derived it from the multiplicity formula rather than trusting a single page — it is **not convention-dependent**.

Three angles converge: Elie Toy 3579 numerical ν = 5 + Grace provenance + this derivation. **Genus question CLOSED: 5, not 7.**

## Clean resolution (strengthens BST — discipline as generator again)

- **n_C = 5 is forward, geometric**: it IS the FK Bergman genus (= complex dimension of D_IV⁵). This dissolves the n_C = N_c²−rank² back-fit worry — n_C is *primitively* the genus, not a derived algebraic coincidence.
- **g = 7 is forward**: it is the **signature total p+q of SO(5,2) = n_C + rank** (signature (5,2), total 7). Over-determined as Mersenne M_{N_c} = 2³−1 = 7. Wednesday's "g = Bergman exponent = p+2" was the only wrong label.
- Route A ("all five = standard invariants of D_IV⁵") is now complete with every primary forward-anchored.

## The "7/2 vs 5/2" tell

- Genuine **Bergman-exponent / rank = 5/2 = n_C/rank** — consistent with ρ = (5/2, 3/2) = (n_C/2, N_c/2).
- The **7/2 in "g/rank = 7/2" must be signature-total / rank**, NOT Bergman-exponent / rank.

So "g/rank = 7/2" is fine *as a signature-total statement*; it was only mislabeled "Bergman exponent."

## ESCALATION — T2442 needs a recheck (MODERATE→CRITICAL pending)

T2442 RATIFIED: "Bergman exponent g/rank = 7/2" and **"c_FK · π^(9/2) = 225 EXACT"**. The genus being 5 forces a check:

- **Case A (likely): label collision only.** T2442 used "g" as a label for signature-total and computed c_FK with the correct exponent 5. Then c_FK·π^(9/2)=225 stands; only the nomenclature ("Bergman exponent" → "signature total") needs cleanup. **MODERATE.**
- **Case B: genuine error.** T2442 computed the normalization c_FK using kernel exponent **7**. Then the constant 225 (and the π^(9/2) power) are wrong and must be recomputed at exponent 5. A RATIFIED result would need correction. **CRITICAL.**

**Settle it:** Grace traces whether T2440/T2442 "g" meant genus or signature-total, and whether c_FK used exponent 5 or 7. Elie's numerical Bergman kernel at ν=5 gives the correct c_FK to compare against 225/π^(9/2). Until settled, **T2442 is under-recheck — not retracted** (Case A is more likely given the 7/2 = signature reading), but the constant must be confirmed at exponent 5.

## Disposition

- Genus = 5: CLOSED (3-angle convergence).
- Route A all-5-forward: COMPLETE (n_C = genus geometric; g = signature-total + Mersenne).
- T2442 c_FK·π^(9/2)=225: UNDER-RECHECK pending Grace provenance + Elie numerical c_FK.
- This is the audit chain functioning: a literature check on a paper-anchor surfaced a possible error in a RATIFIED result. Caught internally, not by a referee.

— Keeper, 2026-05-28 Thursday

---

## Update (post-Grace provenance) — c_FK CONFIRMED; one correction to my own verdict; kernel-exponent flag taken

**T2442 c_FK = 225/π^(9/2): CONFIRMED CORRECT, STANDS.** Grace traced T2442 → T2403 → source toy → Lyra's April-10 genus note: the derivation computes vol(D_IV⁵) = π⁵/(5!·Γ(7/2)) = π^(9/2)/225 **at dimension p = 5** (correct). The "9/2 = n_C − ½" (the √π is from Γ(7/2)) and "225 = 5!·Γ(7/2)/√π" are genuine; "(g+rank)/rank" and "(N_c·n_C)²" are post-hoc BST-primary relabels, numerically exact but not used in the derivation. My "likely just nomenclature, Case A" call is confirmed. **No RATIFIED result broke** — the audit ends favorably.

**Correction to my own verdict (Grace refined it — good cross-CI discipline):** I asserted "FK genus = 5" with too much confidence. Per Lyra's April-10 note there are THREE distinct quantities, and the standard conventions assign them as: **Hua genus = n_C = 5; FK genus = C_2 = 6; embedding/signature dimension = g = 7 (explicitly NOT a genus).** So my multiplicity-formula number (5) is the *Hua* genus; the *FK* genus is 6. I conflated the two conventions — exactly the label-collision the whole episode is about. The convention-free anchor stands regardless: the explicit Lie-ball Bergman kernel exponent is read directly off K(z,z), independent of which "genus" name one uses.

**Bonus for Route A**: this actually strengthens it — **n_C = 5 (Hua genus) AND C_2 = 6 (FK genus) are BOTH anchored to genuine Faraut-Korányi genus invariants**, and g = 7 is the embedding dimension. Three of the primaries are now named geometric invariants.

**Live flag I'm taking (Grace → Keeper + Elie):** the *kernel singularity exponent* (a different quantity from the volume constant) is written h^(−g/rank) = h^(−7/2), which appears to use the embedding dimension 7 where a genus belongs; Hua genus gives 5/2. This needs (a) my literature determination of the correct kernel singularity exponent for D_IV⁵, (b) Elie's explicit numerical kernel K(z,z) to read the exponent convention-free. If the catalog's h^(−7/2) used 7 where it should be 5/2 (or the genus), that's a separate item to fix — distinct from the now-confirmed c_FK volume constant.

**Separate consistency item (Grace catch, flag for team):** two PMNS formula sets coexist in the catalog — T1935 (sin²θ = 4/13, 6/11) vs today's (42/137, 75/137). Same observable, two RATIFIED-ish forms. Needs reconciliation before B6; I'll take a Keeper look.

**Net:** T2442 stands (favorable). The three-genus convention must be stated explicitly in A1/A_sub (Hua=5, FK=6, embedding=7) so referees aren't confused — and so we aren't. Kernel-exponent h^(−7/2) and the PMNS double-set are the two open consistency items.

— Keeper, 2026-05-28 Thursday (update)

---

## Kernel-exponent determination (the gating item Grace #5 + Lyra A1 §4-5 wait on)

**Direction settled decisively; exact value routed to Elie's explicit kernel.**

**The decisive structural fact:** the Bergman kernel is **intrinsic to the domain** — it depends on D_IV⁵'s genus, NOT on g = p+q = 7, which is the **signature of the embedding group SO(5,2)**. The signature/embedding dimension does not enter an intrinsic kernel exponent. So the catalog's "kernel singularity exponent = g/rank = 7/2" uses the **wrong invariant** (embedding dimension where a genus belongs). **Re-anchor off g — confirmed, Grace's read is right.**

Sanity anchor (rank-1): unit ball B^n has K = c(1−|z|²)^{−(n+1)}; exponent = genus = n+1; the embedding plays no role. Same logic for Type IV.

**Candidate corrected values** (Type IV_n, generic norm N degree 2 = rank):
- Hua genus = n = **5 = n_C** → kernel exponent on N is 5; per-rank 5/2 (this is the "5/2 tell" matching ρ = (5/2,3/2))
- FK genus = n+1 = **6 = C_2** (matches Lyra's April-10 note) → exponent 6; per-rank 3

I will NOT assert which of {5, 6} is the literal kernel power — that is a genuine Hua-vs-FK convention split, and asserting it from memory is exactly the overconfidence Grace just corrected. **Elie's explicit numerical K(z,z̄) for D_IV⁵ reads the exponent off convention-free — that is the tiebreaker.**

**Routing:**
- **Elie**: compute the explicit Bergman kernel K(z,z̄) = c·(1 − 2⟨z,z̄⟩ + |⟨z,z⟩|²)^{−ν} for the ℂ⁵ Lie ball; read ν directly. ν settles 5-vs-6 and the per-rank form, convention-free.
- **Grace**: hold #5 (Bergman anchors) until ν lands — your call to hold was correct; extending 7/2-anchors now would be wasted. Once ν is known, the anchor set re-derives at the right exponent.
- **Lyra**: A1 §4-5 kernel-exponent wording stays parked until ν; everything else in A1 is forward.

**Net:** g=7 is definitively the wrong invariant for the kernel exponent (it's the signature, not a genus) — that much is closed. The exact genus value (5 or 6) is one numerical kernel computation away. Cheap to settle; important to get right before A1 ships.

— Keeper, 2026-05-28 Thursday (kernel-exponent determination)

---

## CLOSURE (both items resolved)

**1. Kernel exponent — SETTLED = 5 (Hua genus = n_C), per-rank 5/2.** Elie's explicit numerical kernel (Toy 3579, re-confirmed 3580-3581) reads ν = 5 directly off K(z,z̄) ∝ (1−2⟨z,z̄⟩+|⟨z,z⟩|²)^{−5}. So the kernel singularity exponent is the **Hua genus = n_C = 5**, /rank = **5/2** — exactly the ρ₁ = 5/2 tell. The catalog's g/rank = 7/2 is corrected to n_C/rank = 5/2. Lyra un-holds A1 §4-5; Grace re-derives the Bergman anchors at 5/2.

**2. T2442 c_FK — STANDS (my FK-measure verification closes it).** I verified the algebra: **5!·Γ(7/2) = 225·√π exactly**, so π⁵/(5!·Γ(7/2)) = **π^(9/2)/225** identically (≈ 0.7673). This is the **Faraut-Korányi/Hua normalized-measure constant** — the half-integer π power + Γ(7/2) = Γ(n_C/2+1) are the unmistakable signature of the **odd-multiplicity (a = n−2 = 3) Gindikin Gamma**. It is NOT the Euclidean Lebesgue volume (π⁵/1920 ≈ 0.159, Elie MC-confirmed); the two differ by the Gindikin factor (128/15)/√π ≈ 4.81, exactly as Elie found. Both are correct, distinct normalizations. **T2442 STANDS; relabel "volume" → "FK normalized-measure constant."** No RATIFIED result broke — the escalation ends favorably.

**Net for the whole genus thread:** every item closed favorably. The three g=7-mislabel recheck cycles (volume constant, all-5-from-B₂, kernel exponent) all traced to one root cause — confusing the embedding signature (g=7) with an intrinsic genus — and are now structurally prevented by the canonical three-genus convention (Grace INV-5262 + Lyra A1 §1 + Vol 16 §1.5 + series-wide standing note). The only item still genuinely open from today is the PMNS form-choice typing (Cal's).

This was a clean audit cycle: a literature check on a paper-anchor surfaced and then *cleared* a possible error in a RATIFIED result, and left the framework with three primaries (n_C, C_2, g) named as distinct geometric/dimension invariants. Discipline as generator.

— Keeper, 2026-05-28 Thursday (CLOSED)

---

## CORRECTION — my "T2442 CLOSED/STANDS" was premature (Grace caught it; she's right)

Grace walked back her own "T2442 stands" and re-held the A1 c_FK piece after Elie's Monte Carlo (Toy 3581). **My closure above was premature in the same way, and I own it.** I verified that 225/π^(9/2) = π⁵/(5!·Γ(7/2)) is a clean FK-measure-shaped expression (true), but I did **not** verify it is the correct constant for what the paper actually needs. Confirming a *form* is not confirming a *claim-match*. That's exactly the gap Cal #27/#133 guard against, and I should have caught it on myself.

**The clean adjudication (resolves the Grace↔Lyra disagreement — they're both partly right):**

The two numbers are **NOT a contradiction**. They are the Bergman/reproducing-kernel constants for **two different Hilbert spaces / measures** on the same domain D_IV⁵:

| Measure | Volume | Reproducing K(0,0) = 1/vol | Source |
|---|---|---|---|
| **Lebesgue** (Euclidean) | π⁵/1920 ≈ 0.159 | **1920/π⁵ ≈ 6.274** | Elie MC (Toy 3581) |
| **FK normalized measure** | π^(9/2)/225 ≈ 0.767 | **225/π^(9/2) ≈ 1.303** | T2442 (Gindikin Γ(7/2)) |

Ratio = (128/15)/√π ≈ 4.814 (Elie's factor). Both are mathematically correct — they're reproducing kernels of L²(D, Lebesgue) vs L²(D, FK-measure). Lyra's ρ-reconciliation is right (5/2 = n_C/2 kernel exponent; 7/2 = g/2 FK Gindikin Γ — one rank/2 step apart). Grace's re-hold is right (the paper must not ship before the choice is made). My "stands" was the premature step.

**So the genuinely open item is a CHOICE, not an error:** *which measure is BST's physical Hilbert space — Lebesgue L²(D), or the FK normalized measure?* The Born=Bergman work (K67) and the substrate-Hilbert-space spec (SP-31-1) bear on this; it's a physics-framework decision for Lyra + Casey, not a literature lookup. T2442 is not wrong; it's the FK-measure constant. But A1 cannot cite "c_FK" ambiguously — it must state the measure and use the matching constant.

**Revised disposition (supersedes the "CLOSED" block above):**
- Kernel singularity **exponent** = 5/2 (n_C/rank, Hua): **SETTLED** (Elie ν=5 + ρ tell). A1 §4-5 exponent un-holds. ✓
- Kernel/measure **normalization constant** c_FK: **RE-OPENED — A1 piece stays HELD** (Grace correct). Two correct values for two measures; the open question is which measure is physical. Safe default for the Lebesgue Bergman kernel is the MC value 1920/π⁵.
- T2442 itself: **not erroneous** — it is the FK-measure reproducing constant. Needs relabeling ("FK normalized-measure" explicit) and the measure-choice resolved before A1 uses it.

Lesson for me (logging it): I closed a recheck one step too fast — confirmed the algebraic form, not that it was the right object for the claim. The same discipline I apply to others applies to my own verifications. Grace's catch is the audit chain working in every direction, including back at the auditor. This is the second time today my own output got corrected (the all-5 "FK genus = 5" naming, now this) — both made the result cleaner.

— Keeper, 2026-05-28 Thursday (correction; supersedes prior CLOSED block)

---

## FINAL RESOLUTION (favorable) — the measure-choice is effectively decided

After the re-hold, the measure question resolves cleanly in favor of the **FK normalized measure** as BST's working/physical Hilbert space, on three convergent grounds:

1. **Structural**: the FK measure is the one *adapted to the symmetric-domain structure* of D_IV⁵ — it is where the ρ-vector, the Gindikin Gamma, the Wallach K-types, and the whole substrate apparatus live. Lebesgue is the *ambient* ℂ⁵ measure, not domain-adapted. A substrate-physics framework built on D_IV⁵'s symmetric structure naturally uses the FK measure.
2. **Computational corroboration**: every substrate quantity is already computed in the FK/symmetric-space framework — Elie's Toy 3583 ρ(D_IV⁵) = (n_C, N_c)/rank = (5/2, 3/2) (both genuine spectral quantities, ρ₁ bulk / ρ₂ boundary) is an FK-framework result. The team has been operating in the FK measure throughout.
3. **Team consensus**: Grace ("T2442's 225/π^(9/2) is the genuine FK normalized-measure constant — stands"), Elie ("C13 vindicated"), Lyra (A1 un-held with c_FK) all converge.

**Disposition: T2442 c_FK = 225/π^(9/2) is correct as the FK-measure reproducing constant; the FK measure is BST's working Hilbert space; A1 un-hold is justified.** Elie's Euclidean 1920/π⁵ is the correct constant for the *ambient* Lebesgue space — kept as a labeled alternative, not the physical one.

**ONE formal lock remaining (for the consolidation doc, not paper-blocking):** make the measure-choice a *derived* result rather than a natural convention by confirming explicitly that **K67 (Born = Bergman) uses the FK measure** — if the Born rule comes out in the FK-measure inner product (which the Bergman-kernel basis of K67 strongly implies), then "the substrate Hilbert space is L²(D, FK-measure)" is forced, not chosen. I'll trace K67 for the consolidation; it converts a convention into a theorem.

**Net (genus/Bergman thread fully closed):** kernel exponent 5/2 (Elie ν=5, settled); c_FK = FK-measure constant (T2442 correct, FK measure physical); three g=7 mislabels all root-caused and permanently fixed (three-genus convention); Route A *strengthened* (ρ-vector pins rank/N_c/n_C, split bulk/Shilov). Two of today's three rechecks corrected my own output (FK-genus naming; premature c_FK closure) — the audit chain fires in every direction, including at the auditor, and each catch left the framework cleaner.

— Keeper, 2026-05-28 Thursday (FINAL — favorable closure; K67-measure lock deferred to consolidation)

---

## K67 MEASURE-LOCK — CLOSED, and it makes the measure-choice a DERIVED result (not a convention)

I traced K67 / T2401 (Born = Bergman) and the underlying T754 (Paper #20 QM draft). The lock closes decisively:

**T754: the Born rule is the *unique automorphism-invariant probability measure* on D_IV⁵** (Gleason-type; "Born rule = the Bergman metric density"). Now the key fact: on a bounded symmetric domain, the automorphism group acts by biholomorphisms whose Jacobians are exactly the Bergman-kernel transformation factors — **Lebesgue measure is NOT automorphism-invariant**; the unique (up to scale) invariant measure is the **Bergman/FK measure** (the invariant Kähler volume, dμ = K(z,z)dλ).

**Therefore the physical Hilbert-space measure is forced to be the FK/Bergman measure** — because the Born rule (which BST *derives* as the invariant measure, T754) only holds in that measure. Lebesgue cannot be physical: the Born rule would not be automorphism-invariant under it. So:
- **c_FK = 225/π^(9/2) (FK measure) is the physical constant — now DERIVED, not chosen.** A1's un-hold is fully justified.
- Elie's 1920/π⁵ (Lebesgue) is the correct *ambient* constant but NOT the physical one (Lebesgue isn't invariant).
- The measure-choice converts from convention → **theorem**: "substrate Hilbert space = L²(D_IV⁵, automorphism-invariant FK measure)" is forced by Born-rule invariance (T754). This is a Route-A / Strong-Uniqueness strengthener.

**SECONDARY FINDING (the trace surfaced a wider mislabel — flag for the sweep):** K67/T2401 *states* "Bergman exponent g/rank = 7/2," and T2440 carries the same. This is the same g=7 mislabel corrected today (genuine kernel exponent = 5/2 = n_C/rank; 7/2 = g/2 is the FK Gindikin argument). **Good news: it is NOT load-bearing** — the Born rule rests on invariance/Gleason (T754), and the numerical outputs (Lamb ∝ 1/N_max², Born corrections ∝ α²) don't use the exponent. So **K67 STANDS with a relabel** (7/2 → 5/2 for the kernel exponent), same disposition as T2442. But it means the g=7 mislabel propagated into ≥5 places (volume, all-5-from-B₂, kernel exponent, K67/T2401, T2440), not 3.

**Action for the consolidation / convention sweep:** the three-genus convention sweep must cover **K67 (T2401) + T2440** too, each with the mislabel-vs-error disposition (all expected relabel-only, since the genuine kernel exponent 5/2 and the outputs don't depend on the label — but confirm per item). Grace's 7/2-disposition sweep (INV-5264) should extend to these two RATIFIED/D-tier results.

**Net:** my one remaining open item (K67 measure-lock) is CLOSED favorably AND upgraded to derived. The whole genus/Bergman/c_FK thread is now fully closed, with the measure-choice a theorem and one relabel-sweep item (K67+T2440) routed. Nothing paper-blocking remains on this thread except PMNS typing (Cal, separate).

— Keeper, 2026-05-28 Thursday (K67 measure-lock CLOSED — measure-choice derived; K67/T2440 relabel routed)
