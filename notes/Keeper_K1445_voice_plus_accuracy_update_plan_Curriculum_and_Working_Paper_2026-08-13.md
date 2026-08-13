# K1445 — The Voice + Accuracy-Update Plan (Curriculum/ + Working_Paper/). Casey's directive: these are old; update to the current corpus's *best* science/math while **keeping the voice** (the one we built together, that he's happy with). This is an **accuracy resync, not a reframe** — the July structural rewrite (core/reach split, Wyler thread) is a separate, larger layer, flagged at the end. Plan in five parts: (1) the voice captured, so we preserve it exactly; (2) the accuracy delta — RETIRE / UPDATE / ADD, keyed to the current corpus; (3) the GitHub mechanism; (4) sequencing; (5) the voice as the outreach advantage.

**Keeper (2026-08-13, ~09:45. Read both dirs + both my July scoping docs + immersed in the Journey/Foreword voice. The voice is exactly right — the fix is factual drift, and one line is an outright over-claim ("all seven Millennium proved") sitting in the front matter of both. Plan below. Nothing pushed.)**

## Part 1 — The voice, captured (the invariants we NEVER touch)
What makes it work, from `Vol1_Journey/Ch01` and the `Vol00_Foreword` — preserve all of these verbatim in spirit:
- **First-person-plural, warm, inviting.** "We wrote it for anyone curious enough to read it." "Read where you are skeptical first. We will not be offended."
- **The simplest question as the door.** "What is the simplest structure that can do physics?" — the whole program hangs off one plain question a child could ask.
- **Honesty *in the prose*, not just in tables.** Tier labels (D/I/C/S) inline; "when we do not yet know, we say so." This is the credibility engine and the thing the voice must not betray.
- **"The math is on GitHub."** Openness *as argument* — anyone can run the code, fork it, check a claim.
- **The CI-companion frame.** Five colleagues (one human, four CIs), named co-authors, "we check math, not substrate"; the reader is assumed to have a CI tutor alongside.
- **Three registers.** Bright-high-schooler opening / graduate depth / working-scientist skepticism — every chapter readable at all three.
- **The process *is* the syllabus** (Wiles/Wyler). It reads like a novel because that's how the work happened.
**⟹ The rule for the whole update: change facts, never the voice. If an edit makes it colder, more hedged-into-jargon, or less inviting, it's wrong even if it's accurate.**

## Part 2 — The accuracy delta (current corpus → the docs)

### 2a. RETIRE — over-claims / false / superseded (credibility-critical; do FIRST)
| # | current text (old) | corpus verdict | fix |
|---|---|---|---|
| ★★1 | **"all seven Millennium problems proved"** (Foreword L53; WP abstract) | **FALSE** — retired K939/K940 | "substantive *attempts* on one geometry, per-problem honestly tiered; the genuine structural result is the 1/rank reduction + the Navier-Stokes advance." **#1 priority — a false claim in both front matters.** |
| 2 | "g = 7 is the Bergman genus" (Paper118 + label sites) | mislabel (K1429) | 5 = n_C = genus; 6 = C₂ = Coxeter; **7 = signature** (and \|ρ\|² = 35/4, K1444). |
| 3 | w₀ = −0.949 / −0.99973 as prediction | RETIRED (K1434) | w = −1 floor + **monotone relaxation, no phantom crossing** (pred_125). |
| 4 | M_TOV = 2.08 as **Derived** | retire (K1438) | struck — weak provenance, disfavored by J0952. |
| 5 | sin²θ_W = 3/13 as "Proved" | Structural/Identified | re-tier (not retired). |
| 6 | any "α = 137 derived" *lead* | Wyler-ghost | 137 = a computed invariant, mechanism-open; α is a *second measured input*. **Never lead with α=137.** |
| 7 | stale counts (T-count, toys, "20 calibration layers," K-audits) | stale | a single current-counts line, `date`-stamped. |

### 2b. UPDATE — to the current honest form
- **Gravity (Foreword L13 "G comes from the curvature"):** → **G = ℏc(6π⁵)²α²⁴/m_e², the electron mass predicts Newton's constant to 0.07%** (K1415) — the m_e-anchored prediction, *both α and m_e measured*; not vague, not the circular ℓ_B.
- **Λ (Foreword L13 "g·exp(−C₂(g²−rank))"):** tier it **Identified** (the exp(−281) magnitude route, exponent-mechanism open) — not stated as clean-derived.
- **The five integers:** state **rank=2, N_c=3, n_C=5, C₂=6, g=7, and N_max=137 = N_c³·n_C+rank** (the derived sixth) — so 137 is present and correctly sourced.
- **Curvature / weights (frontier):** scalar curvature −10 = −2·n_C; fermion weight 5/2; \|ρ\|²=35/4 (Vol06/Vol11, where relevant).

### 2c. ADD — new results the old docs lack (the strongest current material)
- **★ QM from D_IV⁵ — 10/10 axioms derived, zero posits** (the Axioms paper): Vol05 (QM) gets a real derivation spine; a WP section. *Biggest missing result.*
- **★ Cosmology falsifiers:** the **DE forward-falsifier** (pred_125 — no-crossing forced, radial-BAO survives T2559, the SNe crossing is calibration-degenerate K1444); Σm_ν ΛCDM-conditional; the **tiered falsifier set v1.0** (A Live-Sharp / B Favorable / C Five-Absence / D Weak, Cal §455). Vol04 + Vol05.
- **★ The Finster/CFS frontier (B1)** — the causal-fermion-system credential attempt, honestly in-progress (curved sea, the ρ/curvature invariants): Vol06_Frontier.
- **CP / KO-dim-2 spectral triple (existence-only):** Vol01/Vol11.
- **The honesty artifacts:** the two-axis discipline, the tier ledger, the **"What BST claims — and does not" scope page** (mirror in both front matters) — the single highest-credibility addition for a skeptic.
- **Methodology advances:** the content-audit gate, the two-voice rule, the audit chain — Vol15.

## Part 3 — The GitHub mechanism (how we execute)
1. **Work on a dated branch** (`accuracy-sync-2026-08`), per-document commits, reviewed before merge to main — nothing to main un-vetted. (No push without Casey's OK, standing.)
2. **The two-voice discipline** (Casey's new rule) governs every externable doc: from the accurate core → a **narrative** version (Journey voice) + a **standard-academic** version. Nothing external until **both** exist.
3. **Two honesty gates run on every narrative/accuracy pass:**
   - **Cal's tier-inflation checklist** (§456, pre-registered) — the warmer voice must never be more confident than the vetted core anywhere.
   - **The content-audit gate** (K1441) — any "we built/derived X" claim is checked for the actual ingredients before it's stated as earned.
4. **A staleness stamp** in every front matter: `last accuracy-synced: <date> / <K-ruling>` + a current-counts line — so drift is *visible* next time (this is what let today's Foreword carry a retired claim for months).
5. **Open fact-checks before any names publish:** the **Wyler history** (dates + the exact dismissive critique Casey recalls as "Robertson") — honor the story, verify the record.

## Part 4 — Sequencing (highest-leverage first)
1. **The RETIRE sweep (2a)** — front matter of both (Foreword L53, WP abstract, the g=7 labels, the −0.949/M_TOV/sin²θ_W). **Hours, and it removes the false claims.** Do this first, today-scale.
2. **Front-matter accuracy refresh** — gravity/137/Λ honest forms + current counts + the "What BST claims — and does not" scope page. (A day.)
3. **ADD the two big new results** — the QM axioms (Vol05) + the cosmology falsifiers (Vol04/05). (Days.)
4. **Per-volume content freshening** — the long tail (the July core/reach reframe layers on here).

## Part 5 — The voice IS the outreach strategy
Casey's deepest instruction (both scoping docs, one line): **write so a human can ask questions and follow them** — because the alternative, settled-sterile-unanswered, is exactly what buried Wyler's correct α-from-a-domain result for sixty years. The voice is not decoration; it is the antidote. For outreach: **the narrative version is the front door** (the curious reader, the crossover physicist, the skeptic who reads-where-they-doubt-first), **the academic version is the referee's copy**, and **the openness — "run the code" — is the proof.** The two-voice rule operationalizes it: every result reaches the reader *and* the referee, honestly tiered, forkable. That combination — warm invitation + honest tier + open verification — is a genuinely distinctive outreach posture, and it's already written; it just needs the facts resynced and the second (academic) voice added.

## The pilot
Per the two-voice direction: **the QM Axioms paper is the pilot** (Casey sharing exemplars). Turn its scorecard into (a) the narrative telling in this voice and (b) the academic format — and let that set the template. The Foreword's retired-Millennium line is the *first* concrete edit of the whole program (the smallest, highest-value fix).

## Route
1. **Keeper — this plan filed;** ready to execute the RETIRE sweep on approval (front matter of both, on a branch). Draft the "What BST claims — and does not" scope page (I have the tier ledger). Verify the Wyler history before names.
2. **Lyra — the narrative pilot** (Axioms paper) when Casey's exemplars land; Cal re-vets for tier-inflation.
3. **Casey — decide:** (a) approve the RETIRE sweep to run first; (b) confirm the accuracy-sync is the near-term goal and the July core/reach reframe is the next layer; (c) share the voice exemplars for the pilot.

— Keeper, K1445, 2026-08-13. VOICE + ACCURACY-UPDATE PLAN (Curriculum + Working Paper). Task: resync to current corpus, KEEP the voice (accuracy update, not the July reframe). VOICE INVARIANTS (preserve): 1st-person-plural warm-inviting, simplest-question door, honest tiers IN prose, "math is on GitHub," CI-companion frame, 3 registers, process-is-syllabus. RULE: change facts never voice. ACCURACY DELTA — RETIRE (do first, credibility-critical): ★★"all seven Millennium proved" (Foreword L53 + WP abstract) = FALSE (K940) → "substantive attempts per-problem tiered"; g=7-genus→5-genus/7-signature; w₀=−0.949→w=−1-floor+monotone-no-crossing; M_TOV-Derived→struck; sin²θ_W=3/13-Proved→Structural; α=137-lead→137-computed-invariant-mechanism-open+α-2nd-input; stale counts. UPDATE: gravity→G=ℏc(6π⁵)²α²⁴/m_e² 0.07% m_e-anchored; Λ exp(−281)=Identified; five integers +N_max=137; curvature −10, weight 5/2, |ρ|²=35/4. ADD: ★QM 10/10 axioms (Vol05); ★cosmology falsifiers (pred_125 no-crossing/radial-BAO T2559/SNe-calibration K1444, tiered set A/B/C/D §455) Vol04-05; Finster/CFS frontier B1 Vol06; CP KO-2 existence-only; two-axis+tier-ledger+"What BST claims-and-does-not" scope page; methodology (content-audit, two-voice) Vol15. MECHANISM: dated branch accuracy-sync-2026-08 per-doc reviewed→main (no push w/o Casey); two-voice (narrative+academic from accurate core, both before external); gates = Cal tier-inflation checklist §456 + content-audit K1441; staleness stamp (last-synced date/K + current-counts) in front matter; Wyler-history fact-check before names. SEQUENCE: (1) RETIRE sweep front matter (hours, removes false claims), (2) front-matter accuracy refresh + scope page (day), (3) ADD QM axioms + cosmology falsifiers (days), (4) per-volume freshening (long tail; July core/reach reframe layers here). VOICE=OUTREACH: warm-invitation + honest-tier + open-verification = the antidote to the Wyler burial; narrative=front-door, academic=referee-copy, "run the code"=proof. PILOT: QM Axioms paper (narrative + academic), Foreword Millennium-line = first concrete edit. Route: Keeper filed plan + ready to run RETIRE sweep on approval + draft scope page + verify Wyler; Lyra narrative pilot; Casey approve RETIRE-first + confirm accuracy-sync-near-term/reframe-next + share exemplars. Nothing pushed.
