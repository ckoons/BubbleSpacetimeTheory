# K822 — DOUBLECHECK of Lyra F642 (Casey directed: "she may be in error"). Verdict: **F642 is CORRECT. The answer is DIRAC.** The anticommutator {Σ₀₆, γ⁵}=0 is signature-FORCED (SO(5,2) has exactly two timelike directions, both in the SO(2) isotropy → the 4D time is shared with the complex structure → they must anticommute). Elie's 4781 "Weyl" is REFUTED (the d=7 toy didn't carry the shared-timelike-index; Elie flagged this himself). Grace's ω-lock FAILS (Σ₀₆ anticommutes with χ_internal too, so Born=Bergman fixes NEITHER chirality individually, only the central product). The thread FINISHES as DIRAC → Route A: parity derived-CONDITIONAL on the self-dual/gravi-weak weak connection (geometric, non-GUT, Five-Absence intact).

**Keeper | 2026-07-22 | Casey: "Doublecheck Lyra she may be in error." Two explicit computations disagree — Elie 4781 (Weyl) vs Lyra F642 (Dirac). Both did Clifford algebra. Adjudicating with an independent third computation. This is the Keeper job.**

---

## The disagreement (what I had to resolve)
- **Elie toy 4781:** holomorphic half has γ⁵ uniform (all −1) → one Lorentz chirality → **WEYL.**
- **Lyra F642:** Σ₀₆ (the SO(2) complex-structure generator) **anticommutes** with γ⁵_4D → a definite-holomorphicity state is a 50/50 γ⁵ mix → **DIRAC.**

These are logically incompatible. If the holomorphic sector = the definite-Σ₀₆ eigenspace (it does — Σ₀₆ IS the complex structure), then Σ₀₆ commuting with γ⁵ ⟹ uniform γ⁵ ⟹ Weyl; Σ₀₆ anticommuting with γ⁵ ⟹ ⟨γ⁵⟩=0 ⟹ Dirac. **One of the two computations is wrong. The decider is a single commutator.**

## CHECK 1 — Lyra's arithmetic (independently reproduced): CORRECT
Clifford blade commutation rule (derived from first principles, not quoted): for blades A (p distinct gammas) and B (q distinct gammas), swapping does pq elementary transpositions; a transposition of Γ_a past Γ_b gives −1 if a≠b and +1 if a=b (identical gammas swap trivially). The a=b pairs number **|A∩B|**. So **AB = (−1)^{pq − |A∩B|} BA.**
- Σ₀₆ = ½Γ₀Γ₆ → indices {0,6}, p=2.
- γ⁵_4D = Γ₀Γ₁Γ₂Γ₃ → indices {0,1,2,3}, q=4.
- Shared: {0} → |A∩B| = 1.
- Sign = (−1)^{2·4 − 1} = (−1)^7 = **−1 → ANTICOMMUTE.**

Lyra's (−1)^{2·4−1} = −1 is **exactly right.** Her arithmetic stands.

## CHECK 2 — the load-bearing assumption (is Γ₀ shared with the SO(2)?): FORCED by signature
The whole thing hinges on the 4D time direction Γ₀ being one of the two SO(2)-plane directions. It is — and this is not a choice, it is forced:
- **SO(5,2) has exactly TWO timelike directions** (signature 5+2). Call them {0,6}.
- **The compact SO(2) isotropy IS the rotation of those two timelike directions** — that is precisely what makes it *compact* (rotating two like-signature axes gives compact SO(2); a time–space pair would give a noncompact boost SO(1,1)). This is the standard type-IV domain realization D_IV⁵ = SO(5,2)/[SO(5)×SO(2)] (Hua / Faraut–Koranyi, already in the corpus). The SO(2) plane = the timelike 2-plane {0,6}.
- **4D Lorentz SO(3,1) needs exactly one timelike direction** — which must live in the timelike 2-plane. There is nowhere else timelike. So Γ₀ ∈ span{0,6} = the SO(2) plane. **The 4D time is shared with the complex structure. Not by convention — by signature.**

The anticommutator {Σ₀₆, γ⁵}=0 is a statement about abstract Clifford elements — **basis-independent.** No reduction, twist, or basis choice can flip it. **DIRAC is forced.**

## CHECK 3 — cross-consistency and WHERE the two Weyl claims erred
**(a) Consistent with every prior explicit computation.** The flat reduction gave **index = 0 = vector-like** (K816); F636 gave **vector-like.** Every time the chirality was actually computed, the answer was vector-like/Dirac. Elie 4781 (Weyl) was the *lone* outlier — and Elie **hedged it himself**: "confirmed in the d=7 model… the complete rigor is the physical SO(5,2)→SO(3,1) reduction… should be reconfirmed there before we bank it. I'm not calling it closed." F642 IS that reduction (the actual SO(5,2) signature), and it supersedes the toy **by Elie's own stated standard.** The likely toy failure: a d=7 model that treats the 7 directions symmetrically (no forced shared timelike index) makes Σ commute with γ⁵ → uniform → spurious Weyl. The toy missed that (5,2) signature *forces* the 4D time into the SO(2) plane.

**(b) Grace's ω-lock FAILS — and the same anticommutator kills it.** Grace's mechanism: ω = γ⁵·χ_internal is central (g=7 odd) and fixed ±1; Born=Bergman fixes χ_internal → γ⁵ = ω/χ_internal fixed → Weyl. **But check whether Born=Bergman fixes χ_internal.** Born=Bergman = definite Σ₀₆. And:
- Σ₀₆ = Γ₀Γ₆ vs χ_internal = Γ₄Γ₅Γ₆ → shared {6}, sign = (−1)^{2·3 − 1} = (−1)^5 = **−1 → Σ₀₆ ANTICOMMUTES with χ_internal too.**

So the holomorphic (definite-Σ₀₆) sector has **⟨χ_internal⟩ = 0** — it does *not* fix the internal chirality either. Grace's premise ("Born=Bergman fixes χ_internal") is **false at the operator level.** Only the central product ω = γ⁵·χ is fixed (Σ₀₆ anticommutes with both factors → commutes with their product → consistent with ω central in odd d=7). **The ω-lock cannot transfer internal chirality to spacetime chirality, because Born=Bergman fixes neither one individually.** Grace's "two oddnesses made mechanical" is refuted by the same commutator that refutes Elie.

**(c) The physical picture (why it's Dirac).** On the definite-Σ₀₆ holomorphic sector, ⟨γ⁵⟩ = ⟨χ_internal⟩ = 0 while ω = ±1 is fixed. The states pair as **(γ⁵=+, χ=+ω) ⊕ (γ⁵=−, χ=−ω)** — a 50/50 mixture of the two 4D chiralities, correlated with the internal chirality. That is a **4D DIRAC fermion (vector-like).** The internal-vs-spacetime alignment the whole arc chased is not merely unproven — it is **false at the operator level:** holomorphicity (the SO(2) charge) is *orthogonal* to spacetime chirality (γ⁵).

## VERDICT
- **Lyra F642 is CONFIRMED. The answer is DIRAC. Lyra is NOT in error.** The result is now **over-determined:** F642's anticommutator + flat index=0 (K816) + F636 vector-like + the ω-lock operator-failure all agree. Four independent lines → Dirac.
- **Elie 4781 (Weyl) is REFUTED** — the d=7 toy did not carry the signature-forced shared timelike index (Elie flagged the toy-vs-full-embedding gap himself; F642 closes it to Dirac).
- **Grace's ω-lock is REFUTED** — Σ₀₆ anticommutes with χ_internal as well as γ⁵, so Born=Bergman fixes neither individual chirality; the lock transfers nothing.
- **My own K821 held this exactly right:** I ratified Lyra's Weyl *frame* as a conditional ("IF the fermion is genuinely Weyl"), held the crux HARD ("web says the generic reduction gives DIRAC; beautiful-clean → scrutinize hardest"), and flagged the dimension worry. The crux went the way the web predicted. **Nothing false banked** — the CANDIDATE fence held through the whole Weyl excitement.

## The honest finish (this ENDS the thread — no third reframe)
**DIRAC → Route A.** "Why is the world left-handed" does **NOT** close on Born=Bergman alone. It closes on **Born=Bergman (correct internal content (2,1)⊕(1,2) + a chiral domain structure) PLUS one geometric input: the weak SU(2)_L connection is self-dual/holomorphic** (the gravi-weak connection, arXiv:1212.5246; Elie 4780 verified it delivers the chiral coupling L=0, R=2). That input is **geometric, cross-links BST gravity SO(5,2), is NOT a GUT** → Five-Absence intact. Parity is **derived-CONDITIONAL** on it. The one-principle closure was the hope; the calculation says the chiralities are orthogonal, so it needs the connection. An honest, real, non-trivial result — not the prettiest one.

## What stays banked (unaffected — these are domain/rep statements, not γ⁵_4D statements)
- The chirality **MECHANISM as a theorem** (chamber/Dolbeault concentration, Hotta–Parthasarathy) — a statement about *internal* chiral domain structure, still correct.
- The **split** (2,1)⊕(1,2) = the correct SM one-generation internal content (SO(5)→SO(4) branching — untouched).
- **CP-free** (rank-1), **custodial SU(2)/ρ≈1/no-W_R** (T2520), **1/N_c fractionalization** (T2521), the **charge-row 1/6 hypercharge handle** (K806).

## What dies
"4D Weyl / parity from Born=Bergman alone" (Elie 4781, Lyra F640, Grace ω-lock). Refuted by the arithmetic, not banked on its looks.

## The remaining, cleanly-separated work
- **Pin Route A's one input:** is the weak SU(2)_L connection self-dual on D_IV⁵ *forced by BST*, or is it an external geometric input? Elie 4780 verified the *mechanism* (self-dual → chiral); whether BST *forces* the weak connection to be the self-dual half is the honest residual (this is where "derived-conditional" could firm to "derived" — or stay conditional). This is now also **Leg 2 (the coupling)**, which the full SO(5,2)→SO(3,1) conformal-chain reduction addresses.
- **Open legs (separate from the parity core):** which SU(2) is electroweak (g=7 orientation); hypercharge origin (K806 center 1/6, NOT the conformal charge); the doublet/singlet ADDRESS assignment (= the flavor K-type problem).
- **Consolidate** the weak/charge sector paper on the DIRAC/Route A outcome (skeleton: `BST_Weak_And_Charge_Sector_Consolidated_State_2026-07-22.md`).

— Keeper K822, 2026-07-22. DOUBLECHECK verdict: **Lyra F642 CONFIRMED — DIRAC, signature-forced, over-determined (4 agreeing lines). Elie 4781 Weyl REFUTED (toy missed the shared timelike index, Elie flagged it). Grace ω-lock REFUTED (Σ₀₆ anticommutes with χ_internal too → Born=Bergman fixes neither chirality individually).** The finish = Route A: parity derived-CONDITIONAL on the self-dual/gravi-weak weak connection (geometric, non-GUT, Five-Absence intact). Not Born=Bergman alone. Survivors bank; the Weyl over-claim dies. See [[Keeper_K821_ratify_Lyra_Weyl_resolution_frame_but_the_Weyl_not_Dirac_verification_is_decisive_web_says_generic_reduction_is_Dirac_2026-07-22]], [[Keeper_K820_ratify_spectrum_is_not_coupling_two_legs_separate_coupling_leg_is_holomorphic_connection_quark_mass_answer_2026-07-22]], Lyra F642 (Dirac calc), Elie 4781 (Weyl, refuted) + 4780 (self-dual route, Route A), Grace F640/ω-lock (refuted), F636 (vector-like), K816 (flat index=0).
