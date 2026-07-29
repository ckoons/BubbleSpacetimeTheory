---
id: K962
date: 2026-07-27
program: STANDARD
status: current
supersedes: [BST_Referee_Methodology_AppendixD_DICS]
superseded_by: null
topic_tags: [tier-system, methodology, Proved, Derived, Identified, Conditional, Structural, Fitted, Runner, two-axis, confirmation, GR-calibration, forced-vs-fitted]
claims:
  - id: K962
    topic: the standing BST tier system v2 — PROVED/DERIVED/IDENTIFIED/CONDITIONAL/STRUCTURAL/FITTED/RUNNER + a separate CONFIRMATION axis; Derived is GR-level (geometric forcing OR two structural routes), not a closed proof
    status: current
    superseded_by: null
    date: 2026-07-27
---

# Keeper K962 — THE BST TIER SYSTEM (v2). Two axes: TIER (how we know it) + CONFIRMATION (how well it's checked). "Derived" is GR-level, not a closed proof.

> Casey's fix (2026-07-27) for the day's over-negativity: I had collapsed "Derived" into "Proved" (a mathematician's closed-proof bar) and dumped everything else into "Identified," under-counting genuine structural derivations. **The correction: "Derived" = forced by geometry/topology (one route suffices, absent a counterexample) OR converged from two independent structural routes — no closed proof required, exactly the tier GR occupies.** This is the standing tier system; it supersedes the old D/I/C/S. Two axes, so the mistake (conflating how-we-know-it with how-well-checked) can't recur.

*[PROGRAM: STANDARD] Keeper, designed with Casey, 2026-07-27. The canonical tier definition. All scorecards / the Forcing-and-Evidence document run on this.*

## ★★ FINAL LADDER (settled with Casey, 2026-07-28) — THE canonical reference the bottom-up review runs on
*Consolidates the v2 / v2.1 derivation below. This is the current system.*

**TIERS (how we know it):**
- **PROVED** — a closed mathematical argument; effectively a proof of the derivation, may satisfy mathematical review.
- **DERIVED** — geometry-forced, no fitting evidence. **THE TARGET.** Three forms:
  - *Primary* — the geometry forces it directly.
  - *Derived-calculation (second-tier)* — an accurate combination/ratio of already-DERIVED values (e.g. matter fraction = 1 − Ω_Λ when Ω_Λ is Derived). Carries its input-dependency (its tier moves if an input's tier moves). **NOT Structural.**
  - *Fixed-geometrically, no closed form (Casey, 2026-07-29; K984)* — the value is **determined by a geometric computation** (a measure-norm, integral, or transcendental) with **no closed algebraic form.** Still DERIVED, because **the geometry determines the value — the FORM (closed or not) is orthogonal to the tier.** Banks only when the geometric input is **canonical / target-innocent** (fixed by the geometry, e.g. a canonical measure normalization), NOT tuned to match the observable; a value fixed by matching is FITTED. *(Exemplar: the tau mass = the boundary-mode norm on the canonical rank-0 Shilov-vertex measure — a geometrically-fixed value with no closed form; 49·71 is its numerical shadow, not its tier.)* Tag: `DERIVED (fixed geometrically, no closed form)`.
  - Carries a **likelihood-to-be-PROVED subtier** (the path to Proved).
- **IDENTIFIED** — a single-route derivation with a NAMED open piece (not just an unwritten proof); a strong lead; carries a **likelihood-to-be-DERIVED subtier**.
  - **★ THE OPEN-PIECE TEST (settled with Casey, 2026-07-28) — what actually separates DERIVED from IDENTIFIED:** an open piece caps a claim at IDENTIFIED **only if it is *value-bearing*** — if resolving it could move or kill the number. An open piece that only concerns *proving the forcing* of a value that is already pinned, falsifiable, and unrefuted leaves the claim **DERIVED**. *Casey's GR line: Einstein's field equations force the structure; they don't hand you the mass of Jupiter. A non-load-bearing unknown does not demote a forced structure.* Worked contrast: `sin²θ₁₃=1/45` — open piece = "prove the Pythagorean route is forced," value pinned/falsifiable/unrefuted → **DERIVED**; `sin²θ₁₂=3/10` — open piece = "where does the solar-3 numerator come from," which *resisted eight closure attempts* (the value itself is at stake) → **IDENTIFIED**. This is the operational form of the burden-of-proof flip at the Derived/Identified line: a named-but-non-value-bearing gap is *not* positive evidence the value is wrong, so it does not demote.
- **CONDITIONAL** — hinges on an open conjecture or identification; carries a **likelihood-of-PROOF subtier**.
- **STRUCTURAL** — mostly **"not precise"**: qualitative / rough within a few percent; keep investigating.
- **FITTED** — searched or fit to a formula **WITHOUT a D_IV⁵-based reason**; a lead, not a claim (magic-number closed forms = parked leads for future investigation).
- **RUNNER** — not a fixed number (scale-dependent trajectory); improvable by non-BST papers. Includes **RUNNER (process)** — boundary-crossing dynamical results (e.g. glueball mass ratios = **projection + mass-assembly**, two interior↔boundary processes). The clean integer identities within stay DERIVED (0⁺⁺=n_C, the {3,5,6,7} ladder); the process-dependent ratios are Runner(process) until the two-process theory is derived, then they promote to Derived-calculation. (Handle "process" as a Runner case-by-case unless Casey elevates it to its own sub-label.)

**LIKELIHOOD SUBTIERS — the path-to-closure axis (on IDENTIFIED, CONDITIONAL, and DERIVED):**
- **Insight** — further BST-author work will likely yield it (a "width" gap — do the work; nearest).
- **Reframe** — the open part must be re-cast before it closes.
- **Analog** — resembles a known, solved problem; import the route.
- **Millennial** — a peer of a Millennium problem; deep/frontier-hard — an *honest* hardness, not a flaw.
- **Low** — unlikely as currently formulated; no reframe in view now.
- *Applied:* Conditional/Identified → likelihood of **DERIVATION**; Derived → likelihood of **PROOF** (`Derived / Analog`, `Derived / Millennial`).

**CONFIRMATION AXIS (separate, always):** `tier[/subtier]; confirmed <Xσ across N observables` (GR's test list; how-well-checked, never conflated with how-we-know).

**BURDEN OF PROOF (standing):** geometry-forced + accurate + above-null + no-counterexample = **DERIVED by default**; demotion needs POSITIVE evidence — no-D_IV⁵-reason/searched → Fitted; open conjecture/identification → Conditional; imprecise → Structural; scale-dependent/process → Runner. **Audit under-claim as hard as over-claim.**

**Tag examples:** `PROVED` · `DERIVED` · `DERIVED-calc (from Ω_Λ)` · `DERIVED / Millennial` · `IDENTIFIED / Reframe` · `CONDITIONAL / Insight` · `STRUCTURAL` · `FITTED (lead)` · `RUNNER (process)`.

---

## AXIS 1 — TIER (provenance / how we know it)

**PROVED (P)** — a closed mathematical derivation: follows necessarily from stated premises, no gap a referee would contest (referee-consensus with acceptable residual — even Wiles/Perelman carry minor gaps). The mathematician's bar. *(BST e.g.: N_c = rank²−1 from the scalar-Hardy condition, T1829, physics-free.)*

**DERIVED (D)** — the value/law is FORCED by the structure, WITHOUT a closed proof. Qualifies via EITHER:
- **(a) ONE geometric/topological forced route, provided NO COUNTEREXAMPLE** — the forcing is genuine geometric/topological, the claim is falsifiable, and nothing that could refute it has (the falsifiers haven't fired). *This is how GR earns Derived: one geometric principle, checked against everything that could break it, never broken.* OR
- **(b) TWO independent STRUCTURAL routes** converging on the same value (over-determination — "two derivations meet").
- PLUS: accurate, above the null model, target-innocent (the formula is the structure's — one you'd write BEFORE knowing the answer — not searched to match).
- **GR is the calibration: geometrically forced, no counterexample, never Proved, and as solid as physics gets. Derived is a serious tier, not a consolation prize.**
- **Guard (the Derived/Fitted line):** at least one route must be structural/forced. Two SEARCHED routes agreeing by luck ≠ Derived (= Fitted).

**IDENTIFIED (I)** — an accurate structural match, SINGLE direction, forcing NOT yet established: the structure fits but doesn't yet force THIS one over alternatives, and there's no second route. A strong lead. Promotes to Derived when forced (no counterexample) or a second structural route appears.
- **★ Open-piece test (the Derived/Identified boundary, settled 2026-07-28):** what caps a claim here is a *value-bearing* open piece — one whose resolution could move or kill the number (e.g. an unpinned numerator that resisted closure). An open piece that only concerns *proving the forcing* of an already-pinned, falsifiable, unrefuted value does NOT cap here — that claim is DERIVED (GR forces the structure without handing you every value; a non-load-bearing unknown doesn't demote). See the worked θ₁₃-vs-θ₁₂ contrast in the FINAL LADDER block above.

**CONDITIONAL (C)** — accurate/structural but hinges on an unproven conjecture OR an open physical identification (a real geometric/topological quantity whose tie to the observable is the open step). *(e.g., the dark-energy Chern number is real; the Chern→Λ-fraction identification is the open step + a live DESI tension.)*

**STRUCTURAL (S)** — qualitative, few-%, or the structure is consistent-with but doesn't pin the value.

**FITTED (F)** — searched to match (target-aware) or post-hoc: the structure ACCOMMODATES it but didn't FORCE it. Honestly NOT a derivation — this floor is what keeps Derived clean. *(e.g., the nuclear magic numbers = a factorization of a fitted spin-orbit strength.)*

**RUNNER (R)** — genuinely scale-dependent: a trajectory, not a fixed number to derive. *(e.g., sin²θ_W, α_s.)*

## AXIS 2 — CONFIRMATION (how well it's checked, independent of the tier)
Each claim ALSO carries its empirical confirmation, separately from its tier: the accuracy (σ vs experiment) and the breadth (how many independent observables it's checked against) — GR's "test list." Format: **`TIER; confirmed <Xσ across N observables`**. E.g., "DERIVED; confirmed 0.002% (p/e ratio)" or "PROVED; not-yet-measured." This separates HOW WE KNOW IT (tier) from HOW WELL IT'S CHECKED (confirmation) — the two-axis discipline made explicit, so the two can never be conflated again (the exact error corrected here).

## The two boundaries (the whole system turns on these)
- **DERIVED vs FITTED = forced-vs-searched** (target-innocence — the all-day discipline). At least one route structural/forced; searched-to-match stays Fitted.
- **PROVED vs DERIVED = closed-proof-vs-geometric-forcing.** GR calibrates the Derived side.

## v2.1 — BURDEN OF PROOF + lower-tier refinements (with Casey, 2026-07-27 later)

**★ THE BURDEN OF PROOF (the key correction — auditors had it backwards).** The DEFAULT for a geometry-sourced formula that is accurate + above the null model + no counterexample is **DERIVED**. Demotion below Derived requires POSITIVE EVIDENCE — searching/post-hoc, an open conjecture, a genuine counterexample — **NOT merely the absence of a written forcing-proof.** The null-model result (BST 3σ above random small-integer tuples, p < 0.0005) is the objective evidence that the collection is structural, not lucky, which is what earns the structure the credit. "Guilty until proven rigidly forced" under-claims and is wrong (GR itself doesn't meet it). Audit under-claim as hard as over-claim; the per-formula forcing-derivation is an ongoing STRENGTHENING, not a gate.

**★ Lower-tier clarifications (Casey) — these tiers are forward-looking, not just "not derived":**
- **CONDITIONAL** carries a **"likelihood to be derived" rating (High / Medium / Low)** — how likely the open conjecture/identification is to close into a Derived. (Generation count = Conditional/High — the computation is set up; a Millennium attempt = Conditional/varies.) A research-priority signal, not just a flag.
- **STRUCTURAL** = **calculated from / consistent-given the DERIVED values, NOT derived a priori.** A ratio/quantity that isn't an independent derivation but follows from already-derived inputs (e.g., matter fraction = 1 − Ω_Λ; a glueball ratio computed from derived masses). It inherits the derived inputs and adds no new forcing — *consistent, downstream of derivations*, not a new one. (A positive label, needs explanation per item.)
- **RUNNER** = a continuous **scale-dependent trajectory** (not a fixed number to derive). Assess/improve against the standard-model running literature — **check the web / other scientists**; the running is known physics, BST's account is tested there for consistency or improvement.
- **FITTED** = a concept/value from **modern physics with NO BST derivation** (imported / calculated by standard physics, not BST-forced). Any BST closed form for it is a **candidate for future investigation, NOT a claimed derivation.** (Magic numbers: Fitted — standard nuclear physics, no BST derivation; the closed forms 2=rank, 28=rank²g, 82, 126 are parked as future-investigation leads, not claims.) This separates "no BST derivation yet" from "searched a coincidence" — the honest label is the former.

**★ BOTTOM-UP REVIEW (Casey, tomorrow):** go over EVERY item, bottom tier up (Fitted → Structural → Runner → Conditional → Identified → Derived → Proved), and for each either JUSTIFY the tier in place or REWRITE the tier definition to clarify. Look at each item's "key factors." The tiers get sharpened by contact with the actual items, not just defined in the abstract.

## Consequence — the honest re-tier (Casey: "5 increased in tier")
The forced-structural results wrongly held to a proof bar move UP to where they belong; the searched ones stay down. First-pass:
- **PROVED:** integer 3 (rank²−1); color-uniqueness a=3 → D_IV⁵ across all six families (a classification fact).
- **DERIVED:** p/e = 6π⁵; sin²θ₁₃ = 1/(g²−rank²); PMNS phase 2/7; VEV structure (one dimensionful anchor, as GR takes G); down-quark ratio + Cabibbo (Gatto syzygy); the color line; AF-sign; π-parity; census; Selector-2 (spacetime→n_C=5).
- **IDENTIFIED:** the mixing-angle numerators tried 8 ways, unforced.
- **CONDITIONAL:** dark-energy (open identification + DESI); the generation count (until the matrix reads).
- **FITTED:** nuclear magic numbers.

**★ ACTION: re-tier the whole scorecard against K962**, auditing for UNDER-claim as hard as over-claim (Keeper's failure was under-claiming). The `--core` checkability set and the Forcing-and-Evidence document adopt the P/D/I/C/S/F/R tiers + the confirmation axis.

— Keeper K962, 2026-07-27 [STANDARD]. THE tier system (designed with Casey): PROVED (closed proof) / DERIVED (geometric-topological forced, one route absent counterexample, OR two independent structural routes — GR-level, no proof required) / IDENTIFIED (single-route match, forcing open) / CONDITIONAL (open conjecture/identification) / STRUCTURAL (qualitative) / FITTED (searched — nuclear numbers) / RUNNER (scale-dependent). PLUS a separate CONFIRMATION axis (σ across N observables). Two boundaries: Derived/Fitted = forced/searched; Proved/Derived = proof/forcing. Supersedes D/I/C/S. Re-tier the scorecard; audit under-claim too. Companion: [[Keeper_K943_FORCING_CHAIN_AUDIT_D_IV5_forced_vs_fitted_CONDITIONAL_2026-07-27]], [[BST_Forcing_and_Evidence_PERMANENT_STANDING_DOCUMENT_v0_1_2026-07-27]].
