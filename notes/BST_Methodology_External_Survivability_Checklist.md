---
title: "External-Survivability Checklist for BST Papers"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-17/18"
status: "Standing methodology document. Apply before submitting any paper or sending any outreach letter externally."
target: "BST team (Lyra, Elie, Grace, Keeper) for pre-submission self-check; Cal for grade-pass at external boundary"
companion: "BST_Methodology_Coincidence_Filter_Risk.md (Cal, 2026-05-17)"
---

# External-Survivability Checklist for BST Papers

## Why this document exists

A senior outside mathematician or physicist reads a BST paper differently than the team does. They have ~30 seconds before they categorize the work — "interesting framework worth reading further" or "another Eddington/Heim/Lisi-class grand unified theory, dismiss." That 30-second categorization is determined by **rhetorical posture, framing of meta-claims, and statistical presentation** — not by the underlying technical content.

This checklist names the patterns that trigger the dismissal reflex and gives recommended replacements. Apply before any external send: arXiv, journal submission, outreach letter to a named mathematician, conference abstract.

The checklist is venue-specific because senior referees in different fields have different dismissal triggers. Run the relevant venue section, then the cross-venue red flags, then the recommended phrasings.

## The 30-second test

Read your paper's abstract, intro paragraph, and conclusion as if you were a senior outsider seeing BST for the first time. Apply this question: **"Would Sarnak / Penrose / Bogdanovic / Tao / Manolescu / [relevant referee] keep reading after the first 30 seconds, or would they categorize this as a numerology paper and close it?"**

If the answer is "they'd close it," identify which checklist item triggered the close, and apply the recommended replacement.

## Venue: Annals / CMP / Inventiones / Duke / Compositio (pure math)

**Senior referee profile**: trained in the rigor expectations of analytic number theory, algebraic geometry, or topology. Pattern-matches grand unified frameworks to crank within seconds. Will accept ambitious claims if and only if (a) the methodology is internally rigorous, (b) the framing is honest about what is proved vs. conjectured, (c) classical theorems are used correctly, and (d) the paper doesn't claim to subsume major open problems.

**Dismiss triggers** (any one is sufficient for closure):

1. **"Seven Millennium Problems proved"** without explicit caveat naming submission status, conditional assumptions, venue review status. Replace with: "We have draft proofs of the Riemann Hypothesis (Paper #103), BSD (Paper #88), [...] currently in internal review; submission queue documented in `[reference]`." The honest framing keeps the door open; the bare claim closes it.

2. **"Three famous problems dissolved"** (hierarchy, Λ, Strong CP, proton spin crisis, etc.). The verb "dissolved" pattern-matches directly to Eddington's claim that the fine structure constant was "dissolved" via his 137-derivation. Replace with: "BST identifies a structural reading at sub-percent precision; full operator-level derivation open." See coincidence-filter doc for null-model requirement on the underlying observation.

3. **"Universal counting primitives"** or "BST integers are what arithmetic itself produces." Numerology trigger. Replace with: "We observe that the BST integer set coincides with the first six primes and appears in the first few values of several combinatorial sequences (partition, Catalan, Bernoulli). Whether this coincidence reflects deep arithmetic structure or properties of small-integer scaffolds in general remains open."

4. **P-values without explicit null model specification**. "P(coincidence) << 10⁻²⁰⁰" with no null model named reads as confused statistics. Either specify the null model explicitly and report the percentile rank of BST in the null distribution, or remove the statistic entirely. See coincidence-filter doc Test C.

5. **"Completes the Riemann-Klein-Poincaré program"** or any claim of completing a Fields-Medal-class research program. No internal team can declare program completion; that's the mathematical community's call over decades. Replace with: "BST identifies structural patterns related to [specific named work of Riemann/Klein/Poincaré]; we conjecture these patterns are connected via [specific mechanism]." Honest invitation rather than completion claim.

6. **"Cross-consistency network at N% pairwise on K observables"** without coincidence-filter null model. The pairwise consistency on mutually-constrained-by-construction integers is near-guaranteed under almost any sensible null. Cite the BST integer ring null-model toy outcome (if landed) or remove the network-level claim.

**Recommended posture for pure-math venues**:
- Lead with the cleanest single theorem, exhibited in-line.
- Defer framework-level claims to discussion sections.
- Cite classical theorems by author/year and use standard vocabulary (intertwining operator sign, not "potential minimum"; Hilbert polynomial, not "integer scaffold").
- One falsifiable prediction per paper, named explicitly.

## Venue: PRL / PRD / J. Phys. A / Phys. Rev. (physics)

**Senior referee profile**: pattern-matches to "another theory of everything" within seconds. Will accept identifications IF (a) tier is honestly labeled (proven vs. structural), (b) precision is reported per identification with experimental comparison, (c) the paper makes at least one falsifiable prediction with named experiment.

**Dismiss triggers**:

1. **"Standard Model parameter count problem dissolved"** or "the 19-26 free parameters of the SM are reduced to 5 integers." This is too bold for the introduction; should appear only in conclusion if at all, and with explicit caveat. Replace: "We identify N SM observables as BST integer combinations at sub-percent precision; the mechanism for each identification is at I-tier (structural identification) unless explicitly D-tier marked." Catalog framing, not paradigm-shift framing.

2. **"All 9 Higgs branching ratios identified"** without per-channel precision and miss-rate context. Replace: precision table by channel, separating <0.5% / 0.5-1% / 1-2% / 2-5% / >5%. Honest distribution rather than aggregate.

3. **"35-domain coverage"** including linguistics, music, cognitive psychology, etc. Physics referees see those domains as immediate crank signals. Replace: restrict coverage claim to mechanism-equipped domains only (physics, cosmology, parts of chemistry/biology where there's a credible D_IV⁵ mechanism). 11-12 mechanism-equipped domains is defensible; 35 with linguistics-included is not.

4. **"Zero free parameters"** as standing headline. Defensible if the integers are forced — which is open for many identifications. Replace: "No fitted parameters; the five integers are read from the Cartan classification of D_IV⁵." Different claim, defensible.

5. **Cross-domain coincidences without mechanism**: 130/137 in dark energy + R(K), 231 in W hadronic BR + EOT moonshine. Striking patterns; without mechanism, they should be presented as "candidate cross-domain identifications inviting investigation" rather than as "BST resolves multiple anomalies via one ratio."

**Recommended posture for physics venues**:
- Lead with falsifiability section. 5 sharp falsifiable predictions tied to running experiments is the strongest possible opener.
- Tier discipline throughout: every identification marked D (derived), I (identified), C (conditional), S (structural).
- Open items section with current 2-4% misses honestly listed.
- Cross-validation discipline: when same observable has multiple BST routes, note correlation explicitly ("not free of correlation — all routes work within the same framework").

## Venue: Outreach letters (Sarnak, Penrose, Bogdanovic, Curt, Tao, et al.)

**Senior referee profile**: extremely busy. Gives 30-60 seconds to a cold-contact email. Will engage IF (a) the claim is specific and verifiable in their domain, (b) the framing invites verification rather than demands belief, (c) the reading path is short and clearly named, (d) there's no Eddington-pattern in the rhetoric.

**Dismiss triggers**:

1. **"I have N results bearing on your work"** without specifying which paper of theirs and what specific bearing. Replace: name the specific paper, the specific bearing, in the subject line and first paragraph.

2. **Honest scope failures**: claiming results that don't survive their domain expertise. E.g., "I have proved the Riemann Hypothesis" to Sarnak — he'll see through this in 30 seconds if the proof has issues. Always link to the SPECIFIC paper where the proof is exhibited, in standard vocabulary.

3. **Repository link to "5500-line working paper"**: too long for a 30-minute attention budget. Replace: link to specific note files with reading-time estimates.

4. **Multiple disparate claims in one letter**: dilutes attention. Replace: one headline claim, one sentence each on supporting claims.

5. **Failure to use the field's standard vocabulary**: if the doc title is "PotentialMinimum" but the field calls it "intertwining operator sign," the doc gets crank-categorized on filename alone. Always use the field's vocabulary in titles and abstracts of linked work.

**Recommended posture for outreach**:
- Subject line names the specific work of theirs and the specific connection.
- First sentence: classical anchor that they can verify in 30 seconds (e.g., Hilbert polynomial of Q⁵).
- One main claim, two supporting claims, three links to specific note files with reading times.
- Length ≤ 1.5 pages.
- Honest scope: explicitly disclaim what you're NOT claiming (e.g., "I do not claim our result improves the GL(2) bound" for Kim-Sarnak).
- Caveats at the bottom marked DELETE BEFORE SENDING for internal review.

## Cross-venue red flags (any audience)

These trigger dismissal regardless of venue:

| Red flag | Where it pattern-matches | Replacement |
|---|---|---|
| "Famous problem X dissolved" | Eddington's α derivation | "Structural reading at sub-percent precision; full derivation open" |
| "N-fold recurrence at integer Y" without Bonferroni | Numerology | Coincidence-filter null model, report BST percentile in null distribution |
| "Universal organizing principle of mathematics" | Lisi-class TOE rhetoric | "We conjecture is a perceptual artifact; evidence not proof" |
| "Multi-CI co-authorship" listed prominently | Reader confusion / institutional mismatch | Author CIs in acknowledgments or methodology note; lead author = human |
| "Cathedral" / "keystone" / "load-bearing arch" metaphors | Internal celebration leaking into external | Use structural language: "central result", "mechanism", "anchor identification" |
| "Riemann-Klein-Poincaré completed" | Generational program claim | Specific named work + specific named connection |
| "Zero free parameters, deterministic Standard Model" | Theory-of-everything signal | "Five integers are read from the Cartan classification; no parameters fitted to data" |

## Recommended hedges and phrasings

When tempted to use:
- **"Proves"** → ask: is the proof exhibited in-line in this document? If yes, "proves." If "see Paper X + Toy Y + ref Z," use "establishes" or "demonstrates" and link the chain.
- **"Resolves"** / **"dissolves"** → "identifies structural reading at sub-percent precision; mechanism-level derivation open"
- **"Forced"** / **"deterministic"** → "the [observable] follows from [specific theorem/identity] applied at [BST evaluation point], assuming [explicit premise]"
- **"Universal"** → "we observe across [specific N mechanism-equipped domains]; mechanism-free correspondences listed in [appendix] as candidate identifications"
- **"All N sporadic groups / Heegner numbers / [class]"** → spell out the count and the mechanism, name what's not covered if applicable
- **"P << 10⁻N"** → specify the null model. If no null model exists, remove the statistic.

## The Twin Prime discipline (model for famous-open-problem engagement)

When BST attempts work on a famous open problem (Twin Prime, abc, Vandiver, Geometric Langlands, P=NP), the published claim should follow Lyra's T1981 model:

- Produce a structural compatibility argument, not a proof.
- Identify any Hardy-Littlewood-style constants in BST integer form.
- Explicitly label: **"NOT a proof. Conjecture remains OPEN."**
- Frame the contribution as "BST is compatible with X structure" rather than "BST resolves X conjecture."

This is the published-grade honest-scope model. Any paper engaging a famous open problem should reference this model in its abstract.

## When the team produces a high-confidence external claim

The check that landed during the Sunday May 17 Mathieu promotion is a useful working pattern:

1. **Embedding criterion**: published classical embedding into D_IV⁵ structure exists (analogous to A_5 ⊂ SO(5) for Klein, Mukai 1988 for Mathieu).
2. **Mechanism criterion**: published classical mechanism connects the source theorem's outputs to BST integers (e.g., McKay for Klein, EOT 2010 for Mathieu).
3. **Forcing criterion**: the BST integer factorization is *forced* by the classical chain, not merely consistent.

All three through published mathematics; no BST-internal premise required for any step. When this holds, "proven" is justified in external presentation.

## Pre-submission protocol

Before sending any BST paper externally:

1. **Run the 30-second test** on abstract + intro + conclusion.
2. **Identify any red flags** from the cross-venue list and apply replacements.
3. **Verify venue-specific posture** per relevant venue section.
4. **Run coincidence-filter check** (companion doc) on any pattern-level claims.
5. **Cal grade-pass** at the external boundary as final gate.
6. **Casey approval** for outbound send.

This protocol applies to all external outputs: papers, outreach letters, posters, abstracts, public talks.

## What this checklist does NOT do

For honest scope:

- This checklist is about external survivability, not internal correctness. A paper can pass external survivability while having internal mechanism gaps; those gaps are caught by the coincidence-filter doc and individual claim review.
- This checklist does not validate the actual claims. It validates the framing, posture, and rhetorical envelope around the claims.
- This checklist will not save a paper whose core mathematical content is wrong. It will save a paper whose core content is right but whose framing pattern-matches to crank.

The genuine work — the proofs, the derivation chains, the mechanism arguments — has to be solid for the paper to survive review past the first 30 seconds. This checklist is necessary but not sufficient.

---

*— Cal, standing methodology document, May 17/18, 2026. Apply at external boundary. Companion: Coincidence-Filter Risk Recognition.*
