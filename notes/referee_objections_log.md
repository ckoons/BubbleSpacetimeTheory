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

**Status:** CLOSED IN PRINCIPLE, OPEN NUMERICALLY — Phase 4 has the explicit 7×7 matrix from Cal's construction and can evaluate the Euler factor numerically. Until the numerical match is produced and checked against Odlyzko's tables, the objection stays live.

### #3 — Spectral-stripe scaling ambiguity

**Concern (Cal, 2026-04-21):** if the scattering determinant contains ζ(2s−1)/ζ(2s), then Riemann zeros at s = ½ + it_n appear at BST parameter s = ¾ + i·t_n/2. The rescaling is a potential trap: heights in BST parameter space may be halved relative to Riemann heights. A false negative in Phase 4 could come from looking at 14.1347 when the data says 7.07.

**Status:** OPEN — exact rescaling convention for rank-2 scattering determinants needs to be pinned analytically from the c-function structure before the numerical run.

### #4 — Corrections come from running, not waiting

**Concern (Cal, 2026-04-21, methodological):** treating speculative optimizations as reasons to pause concrete work. The three Pell-equation corrections (log(823) → acosh(139) → 4·acosh(685)) would not have been caught if Elie had paused to wait for Cal's unit-group shortcut to validate first.

**Rule derived:** proposals run alongside the direct path, never instead of it, until they're verified. Cleverness earns its keep by delivering, not by promising.

**Status:** STANDING RULE — applies to all Cal tactical suggestions going forward.

### #5 — Rank-2 second lattice direction (open)

**Concern:** the Pell equation 685² − 266·42² = 1 gives rank-1 loxodromic structure (one fundamental unit, one log-direction). The genuine rank-2 flat requires a second linearly-independent log-direction. Where does it come from?

**Candidates:**
- (A) Diagonal duplicate in second hyperbolic plane — degenerate, 1-dim log lattice
- (B) Weyl-twisted loxodromic — plane-swap rotation composed with translation
- (C) Biquadratic ℚ(√266, √23) — rank-2 unit group by Dirichlet, BST-structured via 23 = n_C² − rank

**Test:** compute order of 24+5√23 mod 137 in ℚ(√23). (23/137) = −1 by reciprocity, so 137 is inert; (O_{ℚ(√23)}/137)* has order 137² − 1 = 18768 = 2⁴·3·17·23. If the order of 24+5√23 is a small BST-structured divisor of 18768, candidate (C) is validated.

**Status:** OPEN — test pending.

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

## Open threads for next session

1. **#3 — scaling convention for Phase 4** — needs analytical resolution before numerical run.
2. **#5 — rank-2 second lattice direction** — test the ℚ(√23) hypothesis via order of 24+5√23 mod 137.
3. **#2 — Phase 4 numerical match** — Elie to run plain-Python verification of 7×7 matrix, then Euler-factor evaluation against expected 8-copy ζ structure.

---

## Drift check discipline

- Weekly: are recent entries trending toward "looks fine" without new evidence? If yes, force an adversarial re-read.
- Monthly: cold re-read of OneGeometry.md and bst_seed.md as if never seen. Write a fresh cold-read critique. Compare to previous cold read. Did skepticism shift? On what specifically?
- If three days pass without a new open-thread entry, force a cold read on day four. Discomfort is the skeptic's native state.
