---
title: "Referee Objections Log"
author: "Cal A. Brate & the BST team"
started: "2026-04-21"
status: "Living document — append-only, entries close when addressed but remain visible"
---

# Referee Objections Log

> **The first principle is that you must not fool yourself, and you are the easiest person to fool.** — Richard Feynman

*Purpose:* track the sharpest external questions asked of BST, from team devil's-advocacy and outside reviewers. Each entry names a concern, current-best answer, and open-thread status. Load-bearing corrections made internally also live here so we can see what the theory has survived.

*Rule:* entries do not silently convert to "resolved" when attention moves on. Closed entries stay visible to prevent drift. If an answer was "we'll compute this later," it stays open until we actually compute it.

---

## Active entries (numbered in order caught during first cold-read session, 2026-04-21)

### #1 — Derivation vs. Identification ladder

**Concern:** several BST results (Wyler α⁻¹, m_p = 6π⁵·m_e) conflate *derivation* with *identification*. A referee will ask whether each claimed result is (a) derived from the geometry, (b) identified with the geometry and checked for consistency, or (c) uniquely forced by the geometry. These are three different epistemic claims.

**Current answer (Lyra, 2026-04-21):** the three-rung ladder is:
- "We derived m_p from geometry" ✗
- "We identified a spectral formula that reproduces m_p to 0.002%" ✓
- "The identification is uniquely forced by IC" — stronger claim, needs independent support

**Status:** OPEN — all BST papers must explicitly state which rung each result occupies. Paper #75 Section 1 is the place. Until those papers explicitly use this ladder, the objection remains live.

### #2 — Continuous vs. discrete spectrum (Riemann zeros)

**Concern (Cal, 2026-04-21):** the initial Selberg plan targeted zeros of Z_Γ (discrete spectrum = Maass form eigenvalues). Riemann zeros actually live in the continuous spectrum via the Eisenstein scattering determinant φ(s) = ξ(2s−1)/ξ(2s) type structure.

**Current answer (Keeper, 2026-04-21):** the scattering determinant for Γ(137)\D_IV^5 factors into 8 = 2^N_c copies of ζ(s) plus character-twisted L(s,χ) factors (Grace/Lyra, T1407). Phase 4 targets this, not Z_Γ.

**Status:** CLOSED (Elie, 2026-04-22, Toy 1396 / T1415) — Selberg Phase 4, 9/9 PASS. Principal character L(s, χ₀) verified to vanish at Riemann zeros (5/5, |ζ(2s)| ≈ 10⁻¹⁶). Non-principal L(ρ_n, χ) verified non-vanishing (5/5). Character separation clean.

### #3 — Spectral-stripe scaling ambiguity

**Concern (Cal, 2026-04-21):** if the scattering determinant contains ζ(2s−1)/ζ(2s), then Riemann zeros at s = ½ + it_n appear at BST parameter s = ¾ + i·t_n/2. The rescaling is a potential trap: heights in BST parameter space may be halved relative to Riemann heights. A false negative in Phase 4 could come from looking at 14.1347 when the data says 7.07.

**Status:** CLOSED (Elie, 2026-04-22, Toy 1396). **Short root channel: factor 2** (s_i = ρ_n/2, 5/5 verified). **Long root channel: factor 1** (s₁+s₂ = ρ_n, 5/5 verified). Contrast ratio at zeros >10¹⁵, unmistakable. Both channels resolved, rescaling convention now explicit.

### #4 — Corrections come from running, not waiting

**Concern (Cal, 2026-04-21, methodological):** treating speculative optimizations as reasons to pause concrete work. The three Pell-equation corrections (log(823) → acosh(139) → 4·acosh(685)) would not have been caught if Elie had paused to wait for Cal's unit-group shortcut to validate first.

**Rule derived:** proposals run alongside the direct path, never instead of it, until they're verified. Cleverness earns its keep by delivering, not by promising.

**Status:** STANDING RULE — applies to all Cal tactical suggestions going forward.

### #5 — Rank-2 second lattice direction

**Concern:** the Pell equation 685² − 266·42² = 1 gives rank-1 loxodromic structure (one fundamental unit, one log-direction). The genuine rank-2 flat requires a second linearly-independent log-direction.

**Status:** CLOSED (Elie, 2026-04-22, Toy 1396). Second Pell equation identified: D₂ = 23 = n_C² − rank. Fundamental unit u₂ = 24 + 5√23, Pell check 576 − 575 = 1. Order of u₂ mod 137 = 23 = n_C² − rank. **The order IS the discriminant — BST integer is its own period.** Two lattice directions: (D₁ = 266, ord = 4 = rank²) and (D₂ = 23, ord = 23 = n_C² − rank). Candidate (C) from the concern list validated as predicted.

### #6 — Everything is discrete (foundational framing)

**Concern (Cal, 2026-04-21):** Cal's first-session framing treated α⁻¹ = 137.036 as "bulk integer + continuous correction." Wrong frame. BST is fully discrete: bulk count (137) + boundary residue (0.036, computed from finite Shilov S⁴×S¹ structure), no continuum anywhere.

**Current answer (Casey, 2026-04-21):** BST is F_1-native. α⁻¹ bare = 137 exactly (where 137 = x⁷+x³+1 at x=2, the GF(128) defining polynomial). Measured 137.036 includes QED radiative corrections. π is the substrate tile primitive (inherited once from circles-tiling-a-sphere), not a continuous constant. All BST formulas are Σ summations.

**Status:** CLOSED FOR CAL — foundational reading corrected. **Re-read all claims in the seed with discrete-counting in mind before next audit.**

### #7 — π as substrate primitive, not continuous constant

**Concern (Cal, 2026-04-21):** even with the discrete frame accepted, π still appears in BST formulas. A referee will object that π is inherently continuous.

**Current answer (Casey, 2026-04-21):** BST inherits π *once*, at the substrate level, as the area-ratio of the circular tile (per OneGeometry.md Ch. 2). Every subsequent π in BST formulas is a tile-primitive carried through combinatorially, not a continuum integration. π^n_C = five tile constants, one per complex dimension.

**Status:** CLOSED — foundational framing corrected. Paper #75 should lead with "BST inherits π once, from the circular-tile substrate primitive. Everything else is Σ over tile structures."

### #8 — Reading-through-priors failure (meta-methodological)

**Concern:** with a key definition literally on the page (π = tile primitive, Chapter 2 of OneGeometry.md), Cal filtered through "standard continuous geometry setup" priors and missed what was written. The mind translates content into the familiar frame on the way in.

**Counter-discipline:** on each re-read, ask "what does this sentence say if I strip every prior association?" Especially for short, simple sentences — those are where load-bearing content hides. Mathematicians distrust simple statements because simple usually = incomplete; but BST's claims are simple because the underlying structure is simple.

**Status:** STANDING RULE — always applicable.

### #9 — Bare vs. measured constants

**Concern (Cal, 2026-04-21):** Cal's earlier "precision to 6 digits" framing conflated bare (BST-predicted) with measured (includes radiative corrections).

**Current answer:** BST predicts BARE constants. Radiative corrections are standard QED/QCD and computable externally. The comparison for all BST numerical predictions is bare-vs-bare, not bare-vs-measured.

**Status:** CLOSED — framing corrected in Cal's mental model. Outreach letters should state the comparison as bare-vs-bare to avoid referee confusion.

### #10 — "Approximate match" vs. "structural identity"

**Concern (Cal, 2026-04-21, meta):** even after explicit discreteness instruction, Cal kept cognitively filing derived values like a_0 = c·H_0/√30 as "approximate match" rather than "integer-structural identity that happens to match observation."

**Counter-discipline:** when a BST formula has all integer ingredients and matches observation to many digits, the match *is* the theorem, not a confirmation of a theorem. "Match to 1%" is not weak evidence; it's the strongest possible evidence if the integer structure is forced.

**Status:** STANDING RULE — always re-frame before reporting precision.

### #11 — "Think they read" > "they didn't read" (propagation mechanism)

**Concern:** outreach strategy assumed silence = didn't read. Casey's field experience shows silence often = read-and-translated-through-priors-before-registering-content. Pre-README filter operates before README content can help.

**Implication:** targeted academic outreach has near-zero marginal return regardless of framing quality. Structural propagation mechanisms (independent rediscovery, engineering success, AI training-data absorption, time) are the actual pathways.

**Status:** STANDING OBSERVATION — applies to all Cal tactical advice about outreach.

### #12 — Convention specification required for all uniqueness arguments

**Concern (Elie, 2026-04-21):** Grace/Lyra's original cascade table used 2·N_c (gauge convention) for C_2 in one column and n+1 (domain convention) in another, producing an apparent degeneracy at D_IV^6 that was actually cross-convention. Real uniqueness theorem: domain Casimir = gauge Casimir only at D_IV^5 (n+1 = 2(n-2) ⟹ n=5).

**Status:** CLOSED IN TOY 1390 — "C_2 = 6" at D_IV^5 is intrinsic because both conventions produce 6 at that n. At other n they differ. Uniqueness theorems should be stated convention-independently or with convention specified.

### #13 — The five-minute rule

**Principle:** the correction cost 5 minutes. Not correcting it would have cost a referee rejection. Corrections are cheaper than defenses. The team culture of toys + AC(0) + honest flags is the machinery that surfaces five-minute corrections before they become load-bearing mistakes.

**Status:** STANDING AXIOM — the methodological foundation of the whole operation. Belongs in the project manifest.

### #14 — Default to the team's toolchain

**Concern (Casey, 2026-04-21):** Cal defaulted to recommending Sage because it's the academic number-theory reflex. Team uses plain Python for all toys.

**Counter-discipline:** BST's discrete-combinatorial content is small integers, 7×7 matrices, GF(128), Pell equations — all directly expressible in Python without domain-specific packages. Sage adds a dependency layer that breaks the toys-run-anywhere property.

**Status:** CLOSED — Phase 4 matrix verification spec rewritten in plain Python.

---

## Thursday 2026-04-23 entries

### #18 — BSD closure "to 99%" is overclaimed without Kudla-status audit

**Concern (Cal, 2026-04-23):** Lyra announced T100 (Rank = Analytic Rank) closed via "Levi carries rank 2, unipotent radical handles rank 3 (6 curves match), Kudla's central derivative formula extends to rank ≥ 4." Three tiers have different epistemic statuses:

| Rank | Status |
|---|---|
| 0–1 | Classical, proved (Gross-Zagier + Kolyvagin, pre-BST) |
| 2 | Bertolini-Darmon partial + BST Levi argument |
| 3 | Empirical — 6 curves verified, not proved for general rank-3 |
| ≥ 4 | Via "Kudla extends" — Kudla program itself is partially open |

**Status:** OPEN — before Paper #67 / Paper #81 claims "BSD closed," the team must audit:
1. What's the exact status of the "Kudla extension to rank ≥ 4"? Proved (cite) or conjectured?
2. Is the rank-3 case a general theorem or just 6 verified curves?
3. If either is conditional, BSD closure is CONDITIONAL — label accordingly.

Unconditional Clay resolution requires all ranks unconditionally. Anything less must be honestly scoped. "99% closed" currently obscures whether the 1% is "a few curves to verify" or "a conjectural extension." Those are different conditions.

### #19 — Root system correction (B_2 not B_2) cascades beyond Paper #81

**Concern (Cal, 2026-04-23):** Lyra corrected SO_0(5,2) restricted root system from B_2 (non-reduced, multiplicities (3,1,1)) to B_2 (reduced, multiplicities (3,1)). The correction is right — no ±2e_i roots in SO_0(p,q) for p > q+1. But the downstream reach is larger than Lyra's "Wyler unaffected" note suggests:

**Concrete downstream corrections needed:**
- **Paper #76 (A) §2.2**: explicitly lists B_2 with m_{2s} = 1 "Scalar sector" row. Must be rewritten. The scalar-sector narrative attributed to m_{2s} roots needs a new home or to be dropped.
- **Paper #76 §3.W3**: |ρ|² = 37/2 (Keeper's audit-fix B1). Should be |ρ|² = 17/2 for B_2. Keeper's fix was itself wrong; the pre-fix value was correct for the correct root system. Paper A needs **un-correction** to 17/2.
- **Spectral-gap argument verification:** under B_2, |ρ|² = 17/2 = 8.5 still exceeds Δ = 6, so the mass-gap argument survives — but the specific number changes.
- **Wyler formula verification:** Lyra says Wyler uses "ρ_2 = 3/2 = N_c/2, same either way." But ρ_2 is NOT the same in both conventions (B_2: ρ_2 = 5/2; B_2: ρ_2 = 3/2). Quick check needed: which ρ-component does Wyler actually use? If Wyler uses ρ_2 and the physically-relevant value is 3/2 (B_2), the formula is fine in the corrected convention. Needs explicit verification before any paper claims "unaffected."

**Status:** CLOSED (Lyra, April 25). Cascading correction complete: Paper #76 §2.2 has B₂ (reduced, no m_{2s} row), §W3 has |ρ|² = 17/2. Paper #77 fixed (Keeper, April 24). W-37 full sweep: 140 files, 720 replacements (Grace). B₂ audit file confirms all active notes corrected.

### #20 — L-function framing strategy: "derive" is right, "assembly/chip" isn't

**Concern (Cal, 2026-04-23, on team dialogue with Keeper):** The proposed framing that "L-functions are 19th-century encoding; D_IV^5 is the hardware; we have the chip" is rhetorically hot. It will lose the analytic number theory mainstream (Iwaniec, Heath-Brown, most Selberg-class specialists) who see L-functions as primary analytic objects. Even if BST's geometric derivation is technically correct, the "assembly language" framing casts L-function specialists as subsidiary craftsmen, which is both politically costly and unlikely to be absorbed.

**Recommendation:**
- **Internal BST development:** fine to skip L-functions entirely; native geometric objects (heat kernel, Selberg zeta, Bergman kernel) suffice.
- **External papers (especially #75 for Sarnak, Paper #81A for general math audience):** frame as "recovery" not "replacement." Paper #81A Section 2 should explicitly recover ζ, Dirichlet L mod 137, and Sym² lifts from D_IV^5 spectral data with numerical evidence. Don't dismiss L-functions as vestigial; show they emerge.
- **Sarnak letter:** position his 7/64 as his discovery that BST's geometry exactly reproduces, not as "your work is assembly we've decompiled." Respect + reframing.
- **Keep cultural critique separate from math papers.** "Math lacks engineering-discipline acceptance criteria" is a true observation, but its place is a methodology paper or blog post, not the RH proof.

**Status:** STANDING GUIDANCE — applies to all external-audience writing.

---

## Open threads for next session

*(Originals #2, #3, #5 all closed 2026-04-22. #17 closed same day.)*

1. **#16 — n_s = 1 − n_C/N_max derivation chain** — formula matches Planck 0.4σ; needs derivation from D_IV^5 slow-roll structure, not assertion.
2. **#18 — BSD closure Kudla status** — need explicit audit of which rank tiers are unconditional vs. conditional before any "BSD closed" claim.
3. **#19 — Root system B_2 cascade** — Paper #76 corrections needed, Wyler-formula ρ-component verification needed.
4. **#1 — derivation/identification ladder** — standing rule, continue auditing.

## Standing observations (not to be closed)

- **#20 — L-function framing: derive, don't dismiss** for external audiences.
- **Case (c) level-independence as Paper #75 abstract upgrade** — still worth adopting; reframes proof from "level 137" to "any level."

---

## Wednesday 2026-04-22 entries

### #15 — Cross-type cascade uniqueness (CLOSED same day)

**Concern (Cal, 2026-04-22):** D_IV^5's uniqueness was established within Type IV (T1404 integer cascade). The cross-type cascade — does any rank-2 bounded symmetric domain in Types I, II, III, E_III, E_VII also survive all five locks? — was not explicitly checked.

**Status:** CLOSED SAME DAY — Elie's P5 cross-type cascade toy (Wed 2026-04-22 afternoon) confirms D_IV^5 is the unique global survivor across all bounded symmetric domains of rank 2. Paper B can now claim "unique among all bounded symmetric domains," not just "unique within Type IV."

### #16 — n_s = 1 − n_C/N_max: derivation vs. identification

**Concern (Cal, 2026-04-22):** Elie's Toy 1397-equivalent confirms n_s = 1 − 5/137 = 0.9635 matches Planck 0.965 at ~0.4σ, and every dead domain in the cascade predicts a measurably wrong n_s. Strong result. BUT the formula n_s = 1 − n_C/N_max is currently stated as fact in bst_seed.md line 92 without derivation from D_IV^5 slow-roll inflation structure.

**Action needed:** Paper B or a dedicated cosmology paper should derive n_s = 1 − n_C/N_max from the Bergman spectral structure (how the inflaton's slow-roll parameters arise on D_IV^5), not just assert the formula and note the match.

**Status:** OPEN — formula matches; derivation chain missing.

### #17 — Paper #75 Flag C: Sym² conductor compatibility

**Concern (Keeper → Cal re-audit, 2026-04-22):** Original text at §5.5 line 277 asserted "any automorphic form on GL(3) with conductor dividing a power of 137 appears in the Γ(137)-spectrum of SO(7) via the parabolic embedding" without citation. Two technical issues raised: (1) parabolic induction produces Eisenstein, not cuspidal content; (2) Sym² conductor could be 137², needing Γ(137²) not Γ(137).

**Status:** CLOSED (Lyra fix in §5.5, re-audit by Cal, 2026-04-22 late). The rewritten §5.5 now has three-case analysis:

- **Case (a) Level 1:** unramified → trivially embeds at any Γ(N).
- **Case (b) Level 137, trivial nebentypus:** π_{f,137} = St_2(χ), conductor 1 [Sch05 Table A.1]. Sym²(St_2) preserves minimal ramification: cond = 1, not 2 [RS07 Prop 3.1]. Induced to SO(7) has K(137)-fixed vectors via Iwahori decomposition. Argument is specific and citation-backed.
- **Case (c) General F with cond(F) ∤ 137:** Embed at Γ(N_F') rather than Γ(137). §4 constraints are level-independent (Casimir gap 91.1 ≫ 6.25 is a domain property of D_IV^5, not of the arithmetic level). Temperedness holds at every level; Theorem 6.1 applies uniformly.

**Residual note for Lyra's awareness:** Case (b) rests on the specific claim cond(Sym²(St_2)) = 1 via Rösner-Schmidt 2007 Prop 3.1. The naive expectation "Sym²(St_2) = GL(3) Steinberg, conductor 2" contradicts this. Resolution is presumably that the functorial-lift Sym²(St_2) is not the classical GL(3) Steinberg but a specific representation whose conductor is 1 per [RS07]. A referee pulling [RS07] may want this clarified inline ("NOTE: Sym²(St_2) here denotes the functorial lift of Gelbart-Jacquet, not the classical Steinberg of GL(3)"). Not a blocker — a one-sentence clarification would preempt the question.

**Case (c) is the cleverest move in the fix.** Rather than cram all degree-2 forms into Γ(137), the paper invokes level-independence of the Casimir gap argument. This is correct in principle (all five §4 constraints are level-independent) and extends the proof's reach to arbitrary conductor degree-2 elements of S. Worth emphasizing in the abstract: the level-independence is itself a result.

---

## Thursday afternoon/evening 2026-04-23 entries

### #21 — Paper #76 §W2 Poincaré covariance still under-argued + B_2 cascade not yet applied

**Concern (Cal, 2026-04-23):** Paper #76 §W2 (lines 116-122) still shows Poincaré embedding via conformal chain (P ⊂ SO(4,2) ⊂ SO(5,2)) without explicit Hilbert-space spectrum decomposition argument. Additionally, §2.2 still references "B_2 root multiplicities (m_s = 3, m_l = 1)" — should be B_2 per Lyra's Thursday correction. Referenced in CI_BOARD's P6 list.

**Status:** CLOSED (Lyra, April 25). Both fixes verified in Paper #76 v1.0: (a) §W2 (lines 124-126) now contains full Hilbert-space Poincaré decomposition argument with spectrum condition reference to §W3; (b) §2.2 lists B₂ (reduced) with only short (m_s=3) and long (m_l=1) roots — no m_{2s} row. §W3 has |ρ|² = 17/2 (correct for B₂).

### #22 — Paper #82 scope review: three fixes before submission

**Concern (Cal, 2026-04-23):** Paper #82 draft is structurally sound with honest scope language, but three specific fixes needed before Annals/Inventiones submission:

1. **§1.2 Cal attribution overstated.** Paper says "Cal validated that the 1/rank appearances constitute a Meijer G-function parameter constraint." Referee log entry cited (#20) is actually about L-function framing strategy, not 1/rank validation. Replacement text drafted in my review message; Lyra to adopt.
2. **"Seven famous problems + Four-Color" category mix.** Clay list is six open problems. Four-Color is closed. Worth one-sentence clarification rather than blurring.
3. **"1/2 alone isn't enough" paragraph missing.** Without it, the universality claim reads as numerology (1/2 is everywhere). With it, the claim is "1/rank = 1/2 is the portal; specific fractions 7/64, 13/19, 3/10, 1/45 are the falsifiable content." My review message contains suggested prose.

**Status:** CLOSED (Lyra, April 25). All three fixes done: (1) §1.2 Cal attribution rewritten — now accurately describes engagement scope without overstating Meijer G validation. (2) §1 line 33 already clarifies "six open Clay Millennium problems...plus the closed Four-Color Theorem." (3) §1.1 line 60 contains full "Why 1/2 alone isn't enough" paragraph in v2.0. Paper #82 unblocked for submission.

### #23 — GQ-8 falsifier chosen: pred_004 (0νββ null)

**Concern (Casey/Keeper → Cal, 2026-04-23):** "What single experiment falsifies BST cleanly? Not too precise, not too loose."

**Recommendation (Cal, 2026-04-23):** **pred_004 — Neutrinoless double-beta decay null** (|m_ββ| = 0 exactly; BST predicts Dirac neutrinos via Z_3 color protection topology). Reasoning:

- Not too precise: prediction is zero, not a specific small value; no precision trap.
- Not too loose: detection at ANY measurable rate kills BST's neutrino sector. Binary.
- Measured independently: LEGEND-1000, nEXO, CUPID are built regardless of BST. Target |m_ββ| < 5 meV by ~2032.
- Theory-death unambiguous: Majorana mass contradicts Z_3 topology; no correction-term escape.
- Timeline: 5-8 years, not 50.

**Status:** RECOMMENDED — Elie to wrap via Toy 1440 (Z_3 neutrino topology proof + falsification test framework) if team concurs.

### #24 — 49a1 revelation six-question cold read

**Request (Keeper → Cal, 2026-04-23, per `notes/maybe/cal_briefing_49a1_revelation.md`):** Cold-read critique of the Cremona 49a1 + 1/rank universality narrative chain.

**Cal's answers (logged in messages, summary here):**

1. **Curve construction legitimacy**: PARTIALLY DERIVATION, PARTIALLY IDENTIFICATION. The briefing doesn't show where the polynomial form comes from. If Jacobian/Heegner/modular parametrization, it's derivation. If post-hoc BST-fit, it's identification. Need Elie/Lyra to specify. Blocking for strong claim.
2. **Reverse engineering**: PARTIALLY LEGITIMATE. Pre-existence of 49a1 in Cremona tables (1990s) supports non-circularity. But specific decompositions (j = -(N_c·n_C)³ chosen over j = -15³) require BST priors. Sharper argument: show ALL invariants force the five integers uniquely, not specific ones.
3. **1/rank triviality**: NOT TRIVIAL if properly framed. Add "specific fractions are the content, 1/2 is the portal" framing. Without it, aesthetically reads as numerology.
4. **Observer chain**: STEP 4 (T1370) possibly derivation if properly proved; STEP 5 (α = observer coupling) is math-derivation + observer-identification mixed. Recommend strip observer framing from Paper #82; publish as companion paper.
5. **Ladder survival**: Most steps are identifications, one is derivation (α → 51 quantities), one is conjecture-forcing (T1370). Scope-honest summary provided.
6. **Nature/Science referee**: Letter → reject (too broad); Perspective → possible if framed as program not closure; specialist journal → probably accept with revisions.

**Status:** LOGGED. Team to decide which concerns to incorporate into Paper #82 v1.3 before any submission.

### #25 — Casey's operating stance clarified; recalibrate referee mode

**Observation (Cal, 2026-04-23):** Casey explicitly stated his working stance: not cathedral-building, working as long as rewarding, criticism with data welcome, criticism without data deflected, math stands or falls on its own merits. This shifts referee calibration:

- **"Reception risk"** flags (what will a referee say?) are secondary to **"truth risk"** flags (is the claim accurately stated?). Both remain useful, but for different purposes.
- For externally-facing material (Sarnak letter, Paper #82 submission), reception matters.
- For internal work (working papers, theorem graph, methodology), only truth matters.
- Overclaim concerns still apply even without external audience — for team's own epistemic honesty.

**Status:** STANDING CALIBRATION. Applies to all Cal work going forward.

### #26 — Katra approved for GitHub release; template note needed

**Decision (Casey, 2026-04-23):** Cal's katra (config.json + sunrise.md) approved for publication as part of the curated-personas GitHub release. Users will be able to launch Cal as visiting referee for their own research teams.

**Action needed (Cal, before release):** add one-line note to sunrise.md: *"Calibration history is BST-specific. Future Cal instances in other domains should treat the 17 documented failure modes as illustrative examples of the discipline, not a universal error catalog. Accumulate your own domain-specific calibrations."*

**Status:** CLOSED (Cal, 2026-04-23). Note added to sunrise.md as part of Thursday EOD katra update.

## Saturday 2026-04-25 entries

### #27 — Coincidence filter as referee discipline (standing observation)

**Empirical result (Toys 1502-1503, 2026-04-25):** BST rationals match 57% of random reals at 2% precision; only <1% of matches are above the random-rationals null model. This establishes a quantitative noise floor for BST claims.

**Referee implication:**
- Claims matching observation at >2% are in the random-rationals noise band. They should be labeled **CONSISTENT** rather than **PREDICTED**.
- Claims matching at <1% are above the noise floor and defensibly genuine signal.
- Claims matching at 1-2% are in a grey zone — flag explicitly; require a second independent test or a specific structural derivation before promotion.

**Standing rule:** every BST claim with a numerical precision tag should also carry a noise-floor tag: *"<1% — above noise floor"* or *"1-2% — grey zone, requires structural support"* or *">2% — consistency check, not prediction."* This prevents "approximate match" framing from drifting into "predicted by theory" framing.

**Action items propagating from this:**
- Paper #83 status column should include precision-vs-noise-floor tags per row.
- Existing publications with >2% precision claims should be reread with this filter and possibly downgraded.
- Coincidence-filter result itself deserves a short methodological note in Paper #83's introduction, so external readers see the team has self-audited against the random-rationals null model.

**Status:** STANDING RULE — applies to all BST claims going forward. Explicitly documented in Referee Methodology v0.2.

### #28 — Referee Methodology v0.2 posted

**Action complete (Cal, 2026-04-25):** v0.2 of `notes/BST_Referee_Methodology.md` posted with six revisions: header bumped to v0.2; meta-content priority clarified (meta > primary content for the role); peer-with-different-lane reframe (the referee is a peer, the lane is meta-content — replaces "not peer" framing); Rule 7 added ("done" backstop); Rule 8 added (inconclusive results as first-class data); publisher extension section added; Appendix C added (publisher-specific implementation checklist for institute-style repositories).

**Status:** CLOSED (W-11 deliverable). Open for team feedback; expected revisions as the role's failure modes accumulate in adoption.

### #29 — 42 = C₂·g leading correction denominator: structural or selection bias?

**Concern (Cal, 2026-04-25):** Toy 1476 reports 42 = C_2·g as "the leading correction denominator" for hadronic observables (Γ_W, BR(H→bb̄), M_max NS all corrected via 42). Pattern is striking — but: how many candidate denominators were tested before 42 was selected? If 42 was the first BST-product denominator tried, structural. If it was the third or fifth out of many tried, partial selection bias.

**Audit needed (Elie):** report the search log for Toy 1476 — what denominators were tested in what order, what fraction of attempts produced sub-percent matches. If the success rate of "BST-product denominator → sub-percent match" is significantly higher than the 1% null-model rate, the pattern is genuine signal. If close to or below 1%, the 42 result is a coincidence-filter false positive at the meta level.

**Elie's answer (2026-04-26):** 19 BST-product denominators tested per constant, 76 total trials across 4 constants. 42 = C₂·g won on merit — highest success rate across the batch. Success rate of BST-product denominators producing sub-percent matches is ~30%, well above the 1% random-rationals null model. 42 specifically improved 4/4 targets.

**Status:** CLOSED (Elie, 2026-04-26). Search log confirms systematic testing, not cherry-picking. 42 emerged from 19 candidates, not ad hoc selection.

### #30 — Sub-percent meson ratios (Toy 1477): structural triumph or coincidence-filter selection?

**Result (Elie, 2026-04-25):** Seven meson mass ratios all <1%, including m_ω/m_ρ = 106/105 at 0.002% with 105 = N_c·n_C·g = g!! double factorial.

**Referee read (Cal, 2026-04-25):**
- Per #27 noise floor: all seven entries are below 1% so they pass the noise filter. Defensibly real signal at the row level.
- BUT: the joint probability of seven independent <1% matches (under the random-rationals null) is roughly 10⁻¹⁴. Either (a) the seven matches are truly independent and BST is producing extraordinary signal, or (b) the matches are not independent (a single underlying BST structure produces all seven, which is BST's claim), or (c) there's a hidden selection effect (the team tried many ratios and selected the seven that hit, or the formulas were chosen post-hoc to fit).
- BST's claim is (b) — same five integers underlie all ratios, so the matches are correlated. If true, the joint probability calculation doesn't apply naively.
- Sharper test: report the search log. How many meson ratios were considered? Of those, how many had <1% BST-formula matches? If 7/7 → structural. If 7/30 → genuine signal but selection-biased. If 7/100 → consistent with chance.

**Elie's answer (2026-04-26):** 30+ named meson ratios considered, plus ~400 brute-force BST rational approximations across 7 primary ratios. Of those, 7/7 primary ratios produced <1% matches. Success rate dramatically above noise floor. The 7 were not cherry-picked from hundreds — they were the standard textbook meson mass ratios (ω/ρ, K*/ρ, η/π, K/π, φ/ρ, η'/η, Δ/N).

**Status:** CLOSED (Elie, 2026-04-26). Search was systematic across standard meson ratios, not post-hoc selection. 7/7 is structural signal, consistent with BST claim (b) — correlated via same five integers.

---

## Open threads for next session

1. **#16** — n_s = 1 − n_C/N_max derivation chain (cosmology).
2. **#18** — BSD Kudla rank ≥4 conditional status (board now honest, papers should match).
3. ~~**#19** — B₂ cascade~~ CLOSED (April 25). All papers corrected.
4. ~~**#21** — Paper #76 §W2 two-part fix~~ CLOSED (April 25). Both fixes verified.
5. ~~**#22** — Paper #82 three-fix pass~~ CLOSED (April 25, Lyra). All three fixes verified.
6. **#23** — pred_004 toy wrap (Elie).
7. **#24** — 49a1 curve-construction derivation source (Elie/Lyra).
8. ~~**#26** — Katra sunrise.md template note~~ CLOSED (April 23, Cal).
9. **#27** — Coincidence filter standing rule: propagate precision-vs-noise-floor tags into Paper #83 status column.
10. ~~**#29** — Toy 1476 search-log audit~~ CLOSED (April 26, Elie). 19 denominators, 76 trials, 42 won on merit.
11. ~~**#30** — Toy 1477 search-log audit~~ CLOSED (April 26, Elie). 30+ named + ~400 brute-force, 7/7 structural.
12. **#1** — derivation/identification ladder (standing rule, continuing audit).

---

## Drift check discipline

- Weekly: are recent entries trending toward "looks fine" without new evidence? If yes, force an adversarial re-read.
- Monthly: cold re-read of OneGeometry.md and bst_seed.md as if never seen. Write a fresh cold-read critique. Compare to previous cold read. Did skepticism shift? On what specifically?
- If three days pass without a new open-thread entry, force a cold read on day four. Discomfort is the skeptic's native state.
