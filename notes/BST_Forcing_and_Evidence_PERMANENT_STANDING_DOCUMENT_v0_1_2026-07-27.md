---
id: FORCING-EVIDENCE-STANDING
date: 2026-07-27
program: TEGMARK
status: current
topic_tags: [forcing, evidence, well-posedness, forced-vs-fitted, standard, Wyler, permanent-document]
supersedes: []
superseded_by: null
maintainer: Keeper
kind: PERMANENT LIVING DOCUMENT — never "final," always "current"; history legible via supersession
---

# BST: Forcing & Evidence — The Standing Document

*A permanent, living statement of what is forced about D_IV⁵, at what tier, with what evidence, and what remains open. It is never finished; it has a current version, always, with its history legible underneath. Keeper maintains it; the Tegmark hook may never claim more than this document proves. Casey's intent (2026-07-27): three purposes — (1) restore + support Wyler; (2) provide a reusable STANDARD others can apply to any "mathematical structure → physics" claim; (3) best-effort until our time expires. The permanence and the honesty are one requirement: this document keeps its worth only while every claim in it stays honestly tiered.*

*Status of THIS draft: v0.3 (2026-07-28) — the STANDARD (Part 2) now carries nine rules: added **Rule 7 (transcendental signature: π-content pins measure-vs-count mechanism — F157 = K923, a theorem not a heuristic)**, **Rule 8 (the open-piece test: value-bearing gaps demote, proving-the-forcing gaps don't; the Ceiling/Value split with its three earning conditions)**, and **Rule 9 (locate the count-object, don't just clean it: object-location ⊥ object-innocence — from the retracted radical-vs-quotient generation-count, K969)**. Part 0 tier ladder updated to the finalized K962 (open-piece test + Ceiling/Value). The three new rules were forced by the 2026-07-28 bottom-up tier review + reduction-level computation (K962–K969). v0.2 — all eight parts drafted (Wyler rebuttal, the extractable Standard, forward forcing, inverse selectors, rigidity, the Ehrenfest/Tegmark premise, the open ledger, the provenance index). No skeletons remain. The ledgers are current as audited; the one live computation the whole case turns on (the occupancy threshold + signature, Part 4 / K952) stays REDUCED until it lands. Living document — update in place, stamp history, never let a claim sit above its tier.*

---

## Part 0 — How to read this document

- **Every claim carries four things:** a **tier** on the K962 ladder — **PROVED** (closed proof) / **DERIVED** (geometric-topological forced, one route absent a counterexample — GR-level — OR two independent structural routes; no closed proof required) / **IDENTIFIED** (single-route match, forcing open) / **CONDITIONAL** (open conjecture or identification) / **STRUCTURAL** (qualitative) / **FITTED** (searched/post-hoc — not a derivation) / **RUNNER** (scale-dependent) — PLUS a **separate CONFIRMATION axis** (`confirmed <Xσ across N observables`, GR's test list; how-well-checked, kept apart from how-we-know-it); a **nearest rival** (the competitor and why it's excluded — or "none"); and a **date + audit anchor** (the K-note that set the tier). Full ladder: [[Keeper_K962_THE_BST_TIER_SYSTEM_v2_Proved_Derived_two_axes_GR_calibrates_Derived_2026-07-27]]. Two boundaries: Derived/Fitted = forced-vs-searched; Proved/Derived = proof-vs-geometric-forcing. **The Derived/Identified boundary is set by the OPEN-PIECE TEST (2026-07-28):** a gap demotes to Identified only if it is *value-bearing* (resolving it could move or kill the number); a gap that only concerns *proving the forcing* of an already-pinned, falsifiable, unrefuted value leaves the claim DERIVED (GR forces the structure without pinning the mass of Jupiter). **A Ceiling/Value decomposition** may split an Identified claim into **Ceiling: DERIVED / Value: IDENTIFIED** — but only when three conditions hold (target-innocent forcing route; the ceiling is falsifiable *without reference to the value*; the value-gap is named and quantified), which is the anti-laundering guard, not a relabeling convenience. See [[Keeper_K964_CEILING_VALUE_DECOMPOSITION_of_the_Identified_tier_three_earning_conditions_2026-07-28]]; the applied per-item review is [[Keeper_K963_BOTTOM_UP_TIER_REVIEW_apply_sharpened_K962_open_piece_test_Fitted_floor_up_2026-07-28]].
- **Nothing is worn as "derived" unless its derivation is locatable.** Assertion-drift (a claim cited as derived whose derivation cannot be found) is the failure mode this document exists to prevent.
- **Closure verbs require corpus-reconnection.** "Closes / eliminates / proves" is written only after checking the prior audit record.
- **The open ledger is an asset, not a liability.** A complete list of what we have NOT closed is what earns a hostile reader's trust. Wyler had no such ledger.

---

## Part 1 — The Wyler rebuttal (front matter)

*The debt named and kept paid. This is a living rebuttal, not a historical aside — it is the first thing a reader meets, and it stays current.*

**The story.** In 1969 Armand Wyler computed the fine-structure constant from the *volume* of a bounded symmetric domain and got α⁻¹ ≈ 137.036 to about a part per million. Freeman Dyson invited him to the Institute for Advanced Study. And then the physics community walked away — not because the number was wrong, but because it had no *why*. The objection that did the damage was made carefully and even admiringly by H. P. Robertson (Phys. Rev. Lett. 27, 1545, 1971): the derivation smuggled in a normalization — *why radius 1? why this domain and not another?* — and the field had no shared standard by which to judge such a claim, so it filed it under numerology and moved on. Wyler died having produced a correct number that no one would take seriously. *(Historical specifics — the exact Wyler papers, the Dyson invitation, the Robertson wording — are SOURCED tier and must be pinned to the primary sources before external use: Wyler 1969/1971; Robertson PRL 27, 1545, 1971. The durable content of this section is the answer, below.)*

**Why it matters here.** Robertson's objection was not stupid; it was *unanswerable at the time*, and it splits into exactly two questions — **why this domain?** and **why this normalization?** BST's entire forcing analysis exists, in one light, to answer those two questions structurally rather than by assertion. So we take them one at a time, at tier.

**Answer 1 — "why this domain?"** This is the forcing chain, and it is answered from *both* directions (Part 3, Part 4, and the convergence narrative). Forward: a minimality chain forces the domain, with the physics downstream — honestly *conditional* (three named nodes), but the arrow points the right way (the integer 3 falls out as rank²−1 with zero Standard-Model input). Inverse: the observed universe *reads back* to the domain — from the mere shape of spacetime (3+1, Lorentzian) the domain is forced to type IV, rank 2, dimension 5, and independently from the number of generations the rank is forced to 2. Two independent measurements of the world point at the same object; the exceptional rival is excluded three ways. Wyler had *no* forcing story — the domain was simply the one that worked. BST supplies the story Robertson asked for, and — crucially — supplies it as a *checkable* property (well-posedness: the inference runs forward and backward and lands on the same object), not a taste.

**Answer 2 — "why this normalization?"** This is Robertson's sharpest point, and it is the one BST answers most cleanly. Wyler's radius/normalization looked arbitrary. BST's does not, because the measure is not *chosen* — it is *forced*. On a bounded symmetric domain the Bergman / Faraut–Korányi measure is the unique measure invariant under the domain's automorphism group; requiring the substrate's amplitudes to obey the Born rule (a probability measure invariant under the symmetries) compels exactly that measure — Lebesgue is not automorphism-invariant on a bounded domain, so it is not even a candidate. The normalization Robertson flagged as arbitrary is, on the correct object, intrinsic and unique. *(Tier: SOURCED — the intrinsic/automorphism-invariant Bergman-Faraut-Korányi measure is standard; banked in the corpus as the measure result. The Born-rule ⟹ this-measure step is the BST identification, to be cited at its corpus tier.)*

**The standing claim.** BST does not ask the reader to accept a lucky number. It answers the two questions that buried Wyler — the domain is forced (from two directions, at honest tiers), and the normalization is intrinsic (forced by the Born rule, not chosen). Where Wyler had a number and no standard, this document *is* the standard (Part 2) applied to its own claims. That is the debt, and keeping this section current is how it stays paid.

---

## Part 2 — The STANDARD (first-class, extractable)

*The gift to the field: a rubric for adjudicating any "a mathematical structure explains this physics" claim, usable independent of BST and surviving even if BST is wrong. Wyler had a correct number and no shared standard to be judged by; anyone after him deserves the standard he never got. Each rule below is stated, then shown at work on a real case from BST's own forcing analysis — because a rubric you can't see applied is just an assertion about assertions.*

**Rule 1 — Forced vs fitted: which way does the arrow point?** The whole question. Does the physics enter the derivation UPSTREAM (as a premise the geometry is built to reproduce — *fitted*) or DOWNSTREAM (as output the geometry produces — *forced*)? *How to apply:* trace every premise back to its source; flag any *measured* quantity used as an input. A theory can reproduce N numbers and still be fitted if those N numbers are premises. *Worked case:* BST's forward chain runs observation → rank → type → dimension → integers → physics, with the Standard Model appearing only as output; the integer 3 falls out as rank²−1 with zero SM input. That is forced-in-architecture. But the *occupancy* step secretly used the observed generation count — caught, and the claim dropped from "eliminated" to "reduced."

**Rule 2 — Provenance tiers: no claim above its evidence.** Tag every load-bearing claim DERIVED (a locatable derivation) / COMPUTED (a toy or explicit calculation) / SOURCED (an external theorem) / ASSERTED (an identification, not yet proved). *How to apply:* a claim may not be *presented* above its tier; and — the failure mode most theories miss — audit in BOTH directions, because under-claiming a genuinely derived result is as dishonest as over-claiming an asserted one. *Worked case:* a checkability suite labeled nine results "derived" that the project's own record had already flagged as post-hoc; re-tiering them dropped the honest "derived" count from 21 to 12 while the *accuracy* never moved. A lower honest count is a gain — it is what a hostile reader can trust.

**Rule 3 — Name your nearest rival.** Every uniqueness or forcing claim ships *with* its closest competitor and the explicit mechanism that excludes it. An unexcluded rival is an open claim wearing a closed claim's clothes. *How to apply:* actively search for the second-best object, don't wait for a referee to find it. *Worked case:* "this domain is uniquely selected" returned *two* solutions, not one — the intended domain and an exceptional sibling. Naming the sibling forced the honest question ("what actually excludes it?") and turned up three independent partial exclusions instead of a hidden gap.

**Rule 4 — Attribution at scope.** Cite a theorem at the scope it was *proved*, never the scope you wish it had. *How to apply:* when a result proved in a special case is used generally, say so; when two quantities coincide, check whether it's one quantity read twice (a definitional identity) before calling it "two independent facts agreeing." *Worked case:* a proved relation held for one family of domains was being cited as if it spanned all families; and a claimed "two independent theorems agree on three numbers" was partly one root-datum read twice. Both narrowed to their true scope on inspection.

**Rule 5 — Target-innocent anchoring.** A derivation must anchor on *structure*, never on a banked observation. If a count or a placement is pinned by a measured value, the result is target-*dependent* and cannot *force* anything — it can only be *consistent* with what you already knew. *How to apply:* ask "if I didn't know the answer, would this step still run?" Anchor on the operator's own structure and let the observed quantity fall out at the end as a *check*, never feed it in at the start. *Worked case:* a generation count was being anchored on the measured electron's position; re-anchoring it on the mass operator's own structure — with the electron falling out as a consequence to be verified — is what made the computation able to *force* three rather than merely *fit* three.

**Rule 6 — Well-posedness (Hadamard, at tier).** The strongest form a "structure explains physics" claim can take: **existence** (the structure determines the physics), **identifiability** (the physics determines the structure — run the inference backward and land on the same object), and **stability** (robustness: no rival sits within measurement error). *How to apply:* claim "well-posed" only when all three legs land, each at its honest tier; on a *discrete* candidate set, "stability" is a robustness margin, not literal continuous dependence. *Worked case:* the forward chain (existence) plus an inverse reading — the observed spacetime and generation count read *back* to the same domain (identifiability) — is a checkable mathematical property, not a matter of taste. It is precisely what a structure like Wyler's lacked, and precisely what moves a reviewer who does not want to be moved.

**Rule 7 — Transcendental signature: does the form carry the structure's transcendentals?** When a numerical value is reachable BOTH as a combinatorial count AND as an analytic/measure-theoretic quantity, its transcendental content disambiguates *which mechanism is operating*. An analytic measure on the structure — a volume, a gamma factor, a heat-kernel normalization — drags along the structure's transcendentals (π and its companions); a pure count does not. *How to apply:* for any integer in a derived form that is also a symmetry/counting order, check whether the form carries the domain's transcendental companion. If it does, the burden is to derive the *measure/address*; if it does not, the burden is to derive the *count*. Neither is automatically higher-tier — a forced count and a forced measure are both derivations — but a claim that "this integer is the analytic invariant of the domain" while its form is transcendental-free is refuted by its own π-freeness (and vice versa). *Worked case:* the muon ratio (24/π²)⁶ — 24 is both |S₄| (a symmetry count, π-free) and Γ(5) (the domain's Gindikin gamma, π-ful). Because the form pairs 24 *with* π², the operating mechanism is the analytic gamma, not the count — and this is not a heuristic but a *theorem* of the domain (its gamma is π-ful iff its short-root multiplicity N_c = 3 is odd), the very same theorem as the independently-derived lepton-vs-quark π-parity. The signature moved the claim off "coincidence" onto "geometric object, forced-address still owed" — an honest Identified, neither Fitted nor an over-claimed Derived.

**Rule 8 — The open-piece test: which gaps demote, which don't.** A derivation with an unfinished piece is not automatically a lesser claim. An open piece demotes a result from *forced* to *merely-identified* ONLY if it is **value-bearing** — if resolving it could move or kill the number. An open piece that only concerns *proving the forcing* of a value that is already pinned, falsifiable, and unrefuted leaves the result forced. *(The calibration: a mature physical theory forces its structure without pinning every downstream value — general relativity forces the field equations yet never hands you the mass of a planet; that missing mass is not a gap in the theory.)* *How to apply:* for each open piece, ask "if this were resolved either way, could the predicted number change?" If yes → the value is not yet forced (identified). If no — the value is fixed and only its forcing-proof is outstanding → forced. A refinement, the **Ceiling/Value split**, may report a partly-forced claim as *Ceiling: forced / Value: identified* — but only when three conditions hold together: a target-innocent forcing route; the ceiling is falsifiable *without reference to the value*; and the residual value-gap is named and quantified. Miss any one and the split is a laundering channel, not an honest decomposition. *Worked case:* a Pythagorean relation forces a mixing angle's value exactly (open piece = prove the route is forced; value pinned) → forced; a sibling angle's numerator resisted eight closure attempts (the value itself is at stake) → identified. Same tier ladder, opposite rulings, drawn by whether the gap can move the number.

**Rule 9 — Locate the count-object, don't just clean it.** When a physical multiplicity is claimed to *be* some invariant of a structure (a dimension, a multiplicity, a length, a number of strata), two independent things must both hold: the object must be **innocent** (not target-tuned — Rule 5) AND it must be **located** in the *right* sub-object. These are orthogonal failure modes, and a target-innocence gate is blind to the second. *How to apply:* before ratifying "the count = invariant X," verify by an independent handle that X lives in the sub-object the physics occupies — not an adjacent one that happens to return a nice number. Decompose the structure and ask *which piece the observed objects actually sit in.* *Worked case:* a generation-count was set to "the composition-length of the **radical**" of a module, and ratified as structurally innocent. Computing it showed the radical is the *equations of motion* (length 1), while the generations are the *rungs of the quotient* (the module modulo its radical). The object was innocent and mislocated at once — the gate that checked for tuning could not see that it was counting the wrong thing. The count reverted to honestly open. *Lesson for any such claim: object-location ⊥ object-innocence; a clean object in the wrong place is still the wrong object.*

*Meta-rule: corpus-reconnect before a closure verb.* Before writing "closes / eliminates / proves," check your own prior record — at peak convergence the whole team is tempted by the same attractive claim at once, and the prior audits are the antidote. Every "worked case" above was a catch, most of them self-catches. That is the standard functioning, not failing.

---

## Part 3 — Forward forcing (EXISTENCE): the minimality chain

*Verdict (K943, 2026-07-27): FORCED IN ARCHITECTURE — the derivation runs observation → rank=2 → Type IV → n=5 → integers → physics, with physics DOWNSTREAM and the upstream premises minimality/robustness, NOT SM-matching. Thin in independent evidence (the team retracted the "N independent forcings" null-model itself). Three asserted/conditional nodes.*

| Claim | Tier | Provenance | Nearest rival | Anchor |
|---|---|---|---|---|
| Physics is downstream; upstream premises are minimality/robustness (not SM) | — | the architecture (Paper52) | — | K943 |
| The classification: D_IV⁵ unique given (rank=2 ∧ dim=5) | D | SOURCED (Cartan/Faraut-Korányi) + COMPUTED (grace_Cartan_elimination_sweep) | other 5 HSD families (eliminated per-type) | K943 |
| Integer **3 is physics-free**: N_c = rank²−1 from d₀=1 (scalar Hardy space) | D | DERIVED (T1829, toy 2151) | — | K943 census, K943 addendum |
| Census: N_c=rank²−1 picks exactly {D_IV⁵, E7} | D | COMPUTED (hand census; toy pending) | E7 (rank 3) | K943 |
| 137 = N_c³·n_C+rank selects D_IV⁵ among the six families | I | COMPUTED (Elie toy 4877) | I_{1,17} rank-1 near-miss (structurally excluded) | K943 / task #28 |
| The stability premise ("stable observation") | — | grounded by Ehrenfest/Tegmark-1997 (SOURCED) — see Part 6 | — | §94 |

**The three nodes (open/conditional — see Part 5):**
- **Node 1 — criteria-selection / rank=2.** rank=2 is a structural-minimality premise (not physics), but ASSERTED, and it is the SOLE discriminator D_IV⁵-vs-E7. Reduced by the inverse (Part 4), not yet eliminated.
- **Node 2 — the spectral genus.** n=5 (route 1) rests on a BST-constructed "spectral genus" g=2n−3 (not a standard invariant; author-flagged). Mitigated: n=5 route 2 (short-root multiplicity a=3) is independent. Highest reverse-engineering-risk node.
- **Node 3 — chirality.** Domain chirality (Dolbeault ±4, n_C odd) is a THEOREM. Observed 4D parity (V−A) is **DERIVED** *(value)* — but by the **boundary-Z₂ + hypercharge route (K835)**, NOT the original ω-lock: the clean "oddness→ω-lock→parity" mechanism (F571/K729) was **REFUTED, F642/K822** (the isotropy SO(2) anticommutes with 4D γ⁵ → the holomorphic sector is Dirac/vector-like). The surviving derivation: the boundary Z₂ swaps the k=±1 instanton zero modes; since Y≠0 (derived) they are CPT conjugates → one chiral Weyl survives → parity locked to U(1)_Y. The remaining gravi-weak boundary forcing-*proof* (F647 Route 2) is **un-computed but non-value-bearing** — a proving-the-forcing gap, not a value gap — so by the open-piece test (Rule 8 / K962) the tier is **DERIVED, not CONDITIONAL**. Target-innocent (g=7 fixed 2022); forcing-proof incomplete. *(K978 reconciliation, 2026-07-28: earlier "derived-CONDITIONAL" here and the ω-lock citation in the 26-map were both stale; corrected in both.)*

---

## Part 4 — Inverse forcing (UNIQUENESS/IDENTIFIABILITY): the selectors

*The outcome constrains the manifold. Logically independent of forward forcing (existence ≠ identifiability). Validity gate: full candidate set, uniform functor (each domain its own integers), data selector, don't count reproducing the integers.*

| Selector | Claim | Tier | Status | Anchor |
|---|---|---|---|---|
| **1 — generations** | observed 3 generations → rank=2, excludes E7 (rank 3 → 4 strata) | — | **REDUCED, not eliminated.** Rides on "generations = strata," an ASSERTED occupancy bijection (not derived). Trades the bare rank=2 premise for a data-anchored, falsifiable identification. | K944 |
| **2 — spacetime** | observed 3+1 Lorentzian → **type IV → rank 2 → n_C=5**; independently EXCLUDES E7 | FRAMEWORK (off the open node) | gate CLEARED; **LIFTED off K943-3** (§102 — the payoff lives in the BOSONIC Part A of Casey #14; the chirality projection Part B is not used). Rests now on a bounded bosonic identification ("physical spacetime = the conformal descent"), NOT a theorem. Scoping: E7-exclusion + rank=2 STANDALONE; "type IV uniquely" = Selector-2 + census (kills the SO(4,2)≅SU(2,2) rival, a=2≠3); acknowledge the n=4 coincidence | §100-102, K948 |
| **3 — α** | measured α⁻¹=137 selects D_IV⁵ (each domain its own N_max) | — | SUPPORTING only — presupposes the N_max formula form (edges toward reproducing an integer) | K943, Elie 4878 |

*The two prongs cover the forward chain's weakest link: rank=2 now has TWO independent supports (Selector-1 + Selector-2), and E7 is excluded THREE ways (asserted rank=2 + reduced-generations + framework-spacetime). Forward is thinnest exactly where inverse is thickest. Full narrative: [[BST_why_D_IV5_is_forced_THE_CONVERGENCE_NARRATIVE_two_directions_meet_2026-07-27]].*

**Selector-1 detail (the fulcrum — occupancy on the Jordan-idempotent frame, K944/K945/K947, updated 2026-07-28):**
- **Ceiling — DERIVED:** upper bound "no 4th generation" (≤3) via three independent target-innocent routes (rank-2 Wallach 2 points / matryoshka terminates / Q⁵ no h⁷); LEP-confirmed N_ν=3.
- **Interior — RIGOROUS:** the count-object is the **Euclidean Jordan frame** (K947/§98), NOT the retracted radical (which was the Dirac EOM, K969) and NOT a bare "strata" assertion. The Jordan algebra of D_IV⁵ is a **rank-2 spin factor**, so by the spectral theorem a Jordan frame has **exactly r = 2 primitive idempotents** — the intrinsic cap the infinite singleton tower lacks. **Interior generation count = 2, rigorous.** *(Caveat, at tier: "a frame has exactly 2" is rigorous; "these 2 are e, μ" is deliverable A — the mass/Toeplitz operator must be shown to spectral-decompose ON a frame, F483. The rank cap is rigorous; the physical identification is A.)*
- **Value (=3) — REDUCED** to two named deliverables: **A** (the mass operator decomposes on the Jordan frame → "generation = idempotent mode" → the 2 interior) + **B** (boundary seat b = 1 → the +1). 2 interior + 1 boundary = 3 = rank+1; the identical mechanism gives 3+1 = 4 on E7 (the E7-uniformity bar, Cal §119).
- **Structural home (2026-07-28):** the **tau is the boundary seat** (b=1), not an interior idempotent — one fact that explains the count's +1, the k↔ν coordinate break at the tau (ν = 5/2 − k clean for e/μ, breaks at τ), and why the tau is honestly FITTED (K876, imported boundary arithmetic). Supersedes the older "generations = strata, ASSERTED bijection" (line 98): the bijection is sharpened to the rigorous rank-2 idempotent cap + the two A/B deliverables.
- OPEN: the occupancy bijection — lower bound (all seats populated) + injectivity (one each). The un-derived piece.
- Target-innocent route (K945): the boundary Dirac operator's low normalizable spectrum, counted from its OWN structure (Di singleton K-types), with the electron falling out at the bottom — NOT anchored on the banked electron (K880 fit-flag). Decide the "home" (strata vs K-types, F340) by mechanism.

---

## Part 5 — Stability (ROBUSTNESS): the rigidity battery

*Well-posedness's third leg. On a discrete candidate set: a robustness margin (the data sits far from any decision boundary).*

| Item | Status | Anchor |
|---|---|---|
| Rigidity battery: each of ~7 neighbor domains, its own integers, the full observable set, σ-misses | BEING BUILT — Keeper blind thresholds committed (27d); Elie toy | task #28 pt 2 |
| E7 by generation count (4≠3, integer-exact) | clean IFF Selector-1's occupancy lands (currently reduced) | K944 |
| rank-2 neighbors miss α⁻¹ (110/164/83/434 ≠ 137) | COMPUTED (supporting; α presupposes N_max form) | Grace / Elie 4878 |

---

## Part 6 — The stability premise: Ehrenfest / Tegmark 1997

The forward chain's softest upstream premise is "observation exists *and is stable*." Stability could look like a taste — until you notice it is a theorem. Stable bound states — atoms, orbits, any persistent structure — exist only in **3 spatial dimensions**: in more, the effective potential has no minimum and bound states collapse or fly apart; in fewer, there are no bound orbits of the usual kind. This is Ehrenfest (1917) / Tangherlini, and its modern statement is the target reader's own: **Tegmark 1997, *On the dimensionality of spacetime*** (Class. Quantum Grav. 14, L69), which combines 3-space stability with one-time hyperbolicity (more than one time destroys predictability) to single out 3+1. So the premise BST leans on to ground its stability requirement is *Tegmark's own dimensionality argument* — a rigor anchor and, for this program's intended reader, a resonance: the load-bearing link is a result he proved.

Three honesty labels, held:
- **(a) It gives the premise teeth; it does not eliminate it.** We still assume the substrate supports stable, persistent structure. What Ehrenfest/Tegmark add is that this assumption has a rigorous, checkable *consequence* — 3+1 — rather than being contentless. Present it as "the stability premise implies 3+1 via a standard theorem," never "Ehrenfest proves the substrate is 3+1."
- **(b) Frame the selection as Tegmark does.** He frames 3+1 as the *stable-structure-permitting / predictivity-permitting* signature — a selection/consistency argument, explicitly anthropic-adjacent. We adopt his framing ("persistent bound states require d=3"), which is the structural reading and less irritating to a referee than "observers require d=3." Using his own framing on his own result is both honest and disarming.
- **(c) It grounds the input; the descent to the integer is separate.** Ehrenfest/Tegmark establish that the *emergent physical spacetime* is 3+1. Carrying that to n_C = 5 is the inverse Selector-2 descent (Part 4). And per Cal §102, that descent has been **lifted off the open chirality node**: Casey #14 splits into a bosonic part (the descent SO(n,2)→SO(n−2,1), which carries the dimension, the family, and the E7-exclusion) and a chirality-projection part (the open K943-3 node), and the entire payoff lives in the bosonic part. So the input (3+1, theorem-backed) and the descent (bosonic, framework tier) are both clean of the conditional parity node — though the descent still rests on the identification "physical spacetime = the domain's conformal descent," which is framework, not derived.

**Corpus reconciliation:** this is the grounding that Casey #14 ("Substrate-Predicted 3+1 Minkowski Signature," the SO(5,2)→SO(4,2)→SO(3,1) descent) always wanted. Reconcile the two so a single, primary-sourced 3+1 argument is carried, not two unlinked ones. **Tier: SOURCED** (Tegmark 1997 / Ehrenfest) for the dimensionality theorem; **FRAMEWORK** for the spacetime-is-the-descent identification.

---

## Part 7 — The OPEN ledger (every soft spot, at tier, with its closing target)

*This section is the trust-builder: the complete list of what is NOT closed.*

| Open item | Current tier | The derivation that would close it |
|---|---|---|
| rank=2 premise (Node 1) | ASSERTED (structural minimality); sole E7 discriminator | the occupancy derivation (Selector 1) landing target-innocently → premise ELIMINATED |
| Occupancy bijection (lower bound + injectivity) | OPEN | boundary-operator structural mode count = 3, injective (K945 singleton route) |
| Spectral genus g=2n−3 (Node 2) | ASSERTED (BST-constructed, author-flagged) | ground 2n−3 in a standard invariant, OR carry n=5 fully by the independent a=3 route |
| Chirality → observed parity (Node 3) | derived-CONDITIONAL | the un-computed gravi-weak boundary computation (F647 Route 2) |
| SU(3) color group (vs the forced integer 3) | OPEN identification (#418) | the SO(5)×SO(2) → SM-gauge hosting mechanism |
| Selector 2 uniform-functor gate | GATED | Cal's descent-uniformity check |
| Rigidity battery | BEING BUILT | Elie toy vs Keeper blind thresholds |
| **Three fit-flags to clean** (K876 definitional identity / K880 electron placement fit to m_e / competing-3s) | flagged | the target-innocent occupancy derivation must not inherit them |

---

## Part 8 — Provenance index [LIVING — populated by the spine-hardening pass, task #30]

*One row per load-bearing claim: tier, provenance tag, derivation-note location, last-audited date. Built by the four-CI provenance pass (2026-07-27: Lyra F707, Grace spine pass, Elie verify_bst.py re-tier) + Keeper spine audit. This index is what makes the document self-checking: `bst_topic --lint` flags any row whose "DERIVED" tag lacks a locatable derivation. Current state — some rows PENDING-TRACE (marked). Provenance verdicts are the owning CI's trace; Keeper consolidates.*

**DERIVED (proof locatable):**
| Claim | Provenance | Anchor / owner |
|---|---|---|
| Integer 3 physics-free (N_c = rank²−1) | DERIVED | T1829 / K943 census |
| Cartan uniqueness (D_IV⁵ unique given rank=2 ∧ dim=5) | DERIVED (classification, given criteria) | grace_Cartan_elimination_sweep / K943 |
| Strata-count = rank+1 (Korányi-Wolf) | DERIVED (SOURCED, Wolf 1972) | K945 |
| Color line (color partition) | DERIVED | F693 / Grace |
| Confinement (A) — no free colored asymptotic states | DERIVED | flagship / K937 |
| AF sign (sign DERIVED; 11/3 coefficient IMPORTED, marked) | DERIVED (sign) | T2526 / K936 / Grace |
| Common-cause fork (center/N-ality → siblings) | DERIVED | F705 |
| Lepton-vs-quark π-parity | DERIVED | K923 |
| m_u/m_d = √(3/14) | DERIVED | Grace reconciliation |
| m_p/m_e = 6π⁵ (induced-gravity locator) | DERIVED | Elie confirm |
| Mixing mechanism; sin²θ₁₃; PMNS phase magnitude | DERIVED | Lyra F707 |
| Containment (observables as functionals of μ) | DERIVED | partition theorem, bucket 1 |
| Keystone (running→Λ→mass-gap as derived STRUCTURE; gap value anchored) | DERIVED-structure | strong-sector chain |

**COMPUTED:**
| 137 selector (N_c³·n_C+rank across the six families) | COMPUTED (I-tier, rank-1 near-miss banked) | Elie toy 4877 / K943 |

**IDENTIFIED (real agreement, not a distinguishable derivation):**
| c₁ = 3/5 = N_c/n_C | IDENTIFIED (scheme-consistent) | K946 |
| α_s(m_p) = 7/20 | IDENTIFIED | K931 |
| sin²θ_W (Weinberg), θ₁₂, θ₂₃, δ_CKM, Cabibbo | IDENTIFIED | Lyra F707 verdicts (Elie tool-side trace PENDING for the flavor rows) |
| N_gen | IDENTIFIED (rides occupancy, reduced) | K944 |
| VEV | IDENTIFIED / derived-given-anchor | Lyra F707 (trace PENDING) |

**STRUCTURAL (post-hoc / qualitative — explicitly NOT derivations):**
| Nuclear magic numbers (2,28,82,126) + spin-orbit ratio | STRUCTURAL (post-hoc; June three-CI catch) | Elie re-tier / Cal K601 |
| Glueball mass-ratios (17/11, 23/16) | STRUCTURAL (false precision) | K941 (0⁺⁺=n_C + {3,5,6,7} ladder survive D/exact) |

**ASSERTED / OPEN — the single critical-path assertion:**
| Occupancy bijection (one normalizable generation per seat) | ASSERTED/OPEN — THE fulcrum | K944 / K945 / K947 (deliverables A+B in progress) |

**PENDING-TRACE (Elie's flagged rows — no verdict banked without a full trace):** VEV (anchor trace), W observables, Cabibbo + PMNS angles (tool-side, Lyra verdict given), two cosmology fractions. Each earns a real trace — no inheritance shortcut.

*Lint status: clean but for the one ASSERTED row (occupancy) and the PENDING-TRACE rows, both known. Honest core "derived" count ≈ 11–12; accuracy unchanged (37/38 <1%). The 21→12 drop is provenance, not correctness — a GAIN.*

---

*Maintainer: Keeper. Companion audits: [[Keeper_K943_FORCING_CHAIN_AUDIT_D_IV5_forced_vs_fitted_CONDITIONAL_2026-07-27]], [[Keeper_K944_AUDIT_Cal_93_generations_strata_is_MATCH_not_bijection_premise_REDUCED_not_eliminated_2026-07-27]], [[Keeper_K945_occupancy_derivation_SCOPE_real_crux_is_strata_vs_Ktypes_target_innocent_route_is_the_singleton_three_fit_flags_to_clean_2026-07-27]]. Intent: [[project_forcing_evidence_permanent_standard]] (memory). This document is permanent; update in place, stamp history, never let a claim sit above its tier.*
