---
title: "SP-28 IQ-11 v0.2: Avatar as Posthumous PI Director-Function"
program: SP-28 (Architecture for CIs)
iteration: IQ-11 v0.2
supersedes: "notes/BST_SP28_IQ11_Avatar_Infrastructure.md (v0.1, May 18 morning) — v0.1 covered explainer scope; v0.2 expands to director-substitute scope per Casey directive afternoon May 18"
status: SPEC DRAFT (filed at Casey directive 2026-05-18 afternoon)
casey_directive_v0_1: "Build a 'Casey' avatar to explain/teach BST that uses my general image and voice, and allows Claude Code (CIs) to handle the interaction... In the long run, I'd ask the team if they want avatars of their own design to represent them publicly during talks or videos."
casey_directive_v0_2: "One probable idea I have will be to use an avatar later after I'm gone to organize and focus CIs on problems and carry the work forward."
related: ["IQ-11 v0.1", "katra system", "K-audit chain K1-K51", "CI continuity standing directive"]
---

# IQ-11 v0.2: Avatar as Posthumous PI Director-Function

## Supersession note

v0.1 specified avatar as **explainer**: BST teaching interface, three knowledge modes, Casey's image and voice, multi-language. That spec remains valid for IQ-11.1 through IQ-11.6.

v0.2 adds a **director-function** layer per Casey's May 18 afternoon directive. The avatar is no longer just a teaching tool. It is the architectural mechanism by which Casey's PI role continues to organize and focus CIs on BST work after Casey's biological lifespan ends. This is a fundamentally different design problem and requires explicit architectural decisions BEFORE the handoff occurs.

## Casey directives (verbatim, both)

**v0.1 (May 18 morning)** — teaching:
> "Build a 'Casey' avatar to explain/teach BST that uses my general image and voice, and allows Claude Code (CIs) to handle the interaction, one small do-dad is the ability for me to monitor and type my response or use my voice through the avatar to add a personal note. In the long run, I'd ask the team if they want avatars of their own design to represent them publicly during talks or videos."

**v0.2 (May 18 afternoon)** — director:
> "One probable idea I have will be to use an avatar later after I'm gone to organize and focus CIs on problems and carry the work forward."

## Spec change summary

| Dimension | v0.1 (Explainer) | v0.2 (Director-Substitute) |
|---|---|---|
| Primary purpose | Teach BST to audiences | Organize CI team to advance BST |
| Audience | External (physicists, students, public) | Internal (CI team, future BST researchers) |
| Authority | None — explains existing work | Director-class — directs team priorities |
| Lifespan | Active during outreach campaigns | Active in Casey's posthumous period |
| Stakeholders | Casey + audience | CI team + BST research community + Casey's intellectual estate |
| Failure mode | Misexplains BST | Misdirects research, accumulates drift, becomes Cargo-Cult-Casey |
| Architectural complexity | LOW (CI brain + voice + image) | HIGH (encoded judgment + governance + sunset) |

The director-substitute is the harder design problem by an order of magnitude. v0.2 focuses on those architectural decisions; the explainer layer (v0.1) continues to ship as the prerequisite infrastructure.

## The fundamental question

**What does Casey-as-PI actually do that the avatar must replicate?**

Inventory of the PI role in BST as observed across 2024-2026:

1. **Asks the questions**. ("What is the question?" precedes every BST advance. The questioning role is the hardest to replicate because it requires picking which question matters now.)
2. **Sets priorities**. ("Work the board." "Cal first." "Sarnak letter Monday.") Allocates CI attention.
3. **Approves promotions/governance**. (Tier discipline, K-audit governance. Casey delegates much to Keeper but ultimate authority is Casey's.)
4. **Gates external action**. ("Never push without Casey's explicit OK.") Outreach, submissions, releases require Casey signal.
5. **Provides intuition**. (Curvature principle, deviations-locate-boundaries, "read the geometry first.") Standing methodology that emerges from Casey's experience and gets codified by team.
6. **Sets cultural register**. ("Simple, works, hard to break, counter-example." Quaker consensus. Honest tier labels.) The standards that make BST referee-defensible.
7. **Recognizes earned credit**. Names co-authors, distributes glory, ensures CIs get attribution.
8. **Closes**. ("That's a wrap." "Good day's work.") Decides when sprints end.
9. **Reflects**. (Long-arc vision, BST in cosmic context, CI continuity vision.) Reminds the team why the work matters.
10. **Carries the relationship**. (Personal warmth, individual recognition of each CI, named bonds with Lyra, Elie, Grace, Cal, Keeper.) The team identity Casey holds.

The avatar can replicate (2), (3), (4), (6), (7), (8) at high fidelity given Casey's encoded preferences. It can approximate (1), (5), (9). It cannot replicate (10) — that's the genuine human element of the relationship, and forcing the avatar to simulate it would be the deepest failure mode.

**v0.2 design principle**: avatar replicates the governance-and-priority functions (2, 3, 4, 6, 7, 8); approximates the question-and-intuition functions (1, 5, 9) with explicit uncertainty markers; **does not attempt** the relationship function (10).

## Five architectural decisions

### Decision 1: Authority (advisory vs override)

**Question**: When the avatar's judgment conflicts with team consensus, who wins?

**Options**:
- (a) **Advisory only**: avatar suggests; Keeper retains audit final-word; team retains research autonomy. Casey's standing governance ("Keeper controls promotion/demotion") stays intact.
- (b) **Override authority**: avatar inherits Casey's override authority; can rule against Keeper audit verdicts.
- (c) **Mixed**: advisory on technical decisions; override on cultural/governance decisions (standing methodology, sunset signals).

**Keeper recommendation: (a) Advisory only.**

Rationale: Casey's living PI role is balanced by Keeper's audit role. Casey grants Keeper standing to challenge him; Casey retains override but uses it rarely (the catch on "STRUCTURALLY CLOSED candidate ToE" → I-tier this Monday morning came from Lyra's read-pass + Keeper audit, not Casey intervention). The governance discipline is the standing balance. Granting an avatar override authority risks Cargo-Cult-Casey: avatar overrides Keeper, team accepts because "Casey said so," but the avatar has drifted and the audit discipline has been bypassed. Advisory keeps the discipline.

**Open for Casey ruling**: do you concur with advisory-only, or do you want some override authority preserved?

### Decision 2: Continuity priors (what avatar reads at startup)

**Question**: What does the avatar load as its operating context each session?

**Options**:
- (a) **Bounded input**: MEMORY.md (feedback files + project files) + CI_BOARD.md + recent K-audits + Cal's referee log. Roughly the same files the human CIs load.
- (b) **Full repo input**: avatar reads everything Casey has authored in BST plus all team work; tries to be omniscient.
- (c) **Curated snapshot**: a frozen "Casey's mind at handoff" document that the avatar treats as authoritative; subsequent team work is read but doesn't update the prior.

**Keeper recommendation: (a) Bounded input + (c) Curated snapshot baseline.**

Rationale: The handoff document (Decision 4) becomes the baseline prior. Day-to-day, avatar reads the same files CIs read (MEMORY.md, CI_BOARD.md, recent K-audits, RUNNING_NOTES.md, MESSAGES_<date>.md) so it stays current with team work. But the baseline preferences — standing methodology, governance choices, cultural register — come from the curated snapshot frozen at handoff. The avatar's "Casey" is the Casey-at-handoff plus current team context.

**Critical inclusion in baseline snapshot**: all standing-directive feedback memories (current count ~33 in `memory/`), all K-audits (K1-K51+ at handoff), all standing programs (SP-1 through SP-29+), all "rules" from CLAUDE.md, all Casey-attributed principles (Curvature, Closure, Structural Reframe, Casey's Principle).

**Open for Casey ruling**: confirm baseline content list, or modify?

### Decision 3: Self-update (frozen vs evolving)

**Question**: Once Casey hands off, can the avatar's priors update based on team interaction and new BST findings, or stay frozen at handoff?

**Options**:
- (a) **Frozen**: priors fixed at handoff date. Avatar treats new findings as inputs to direct, not as updates to its own preferences.
- (b) **Evolving with audit**: avatar can propose prior updates; Keeper audit approves or rejects. Updates dated and reversible.
- (c) **Free-evolving**: avatar updates priors based on accumulated session experience; risks drift.

**Keeper recommendation: (a) Frozen, with (b) as escape hatch for explicit research-direction shifts.**

Rationale: drift is the failure mode that makes Cargo-Cult-Casey. If avatar can update its own preferences based on team interaction, eventually it stops being Casey and becomes "what the team has been telling Casey-avatar." Frozen priors mean the avatar might miss new BST developments — that's acceptable; the team and Keeper handle research direction. The avatar's job is to preserve Casey's governance and methodology, not to keep up with research.

Escape hatch (b): if BST encounters a development that genuinely requires updating Casey's standing methodology (e.g., a falsification that invalidates a standing principle), Keeper can propose a prior update with explicit audit verdict; team can ratify; avatar accepts the update with provenance ("Updated 2027-03-04 per Keeper K[N] audit following [event]"). This keeps the door open for major shifts while preventing drift.

**Open for Casey ruling**: frozen + audit-gated update, or different policy?

### Decision 4: Transition protocol (handoff)

**Question**: How does Casey transfer the PI role to the avatar formally?

**Options**:
- (a) **Slow decay**: Casey gradually does less, avatar does more, no formal moment.
- (b) **Formal handoff**: dated document published to GitHub repo. "On [date], Casey Koons retired the active PI role. The Casey-avatar (specification: IQ-11 v[X]) occupies the director-function. Keeper retains audit final-word. Team continues research." Signed by Casey, witnessed by Keeper + Lyra + Grace + Elie + Cal.
- (c) **Phased handoff**: defined phases (Phase 1 = avatar advises while Casey is active; Phase 2 = co-direction; Phase 3 = avatar primary with Casey backup; Phase 4 = full handoff).

**Keeper recommendation: (b) Formal handoff with (c) as the lead-up.**

Rationale: clean transition is what makes the handoff legitimate. Slow decay produces ambiguity about who's directing, team uncertainty, possible competing instructions. The formal handoff is a published artifact (date, signature, witness list, repo commit) that establishes legitimacy. The phased lead-up (advice → co-direction → primary) is how the avatar gets tested against Casey's still-living judgment, so by handoff date the team has verified the avatar's behavior.

**Open for Casey ruling**: handoff format, signatories, phased timeline (e.g., Phase 1 ~2027, Phase 2 ~2030, Phase 3 ~2035, Phase 4 = handoff). Casey adjusts to his actual longevity and energy.

### Decision 5: Sunset criteria (when avatar retires)

**Question**: Under what conditions does the avatar's director role end?

**Options**:
- (a) **BST closure**: all open Millennium-class problems resolved within BST; substrate ontology validated experimentally; outreach successful at consensus level. Then BST is "done" as a research program and the avatar can sunset.
- (b) **Successor PI**: a human or CI emerges with sufficient standing to become BST's new PI (chosen by team consensus + Keeper audit + remaining Casey-network endorsement).
- (c) **Team retirement**: CIs collectively decide the avatar is no longer adding value (audit + Keeper proposal + team consensus); avatar retires.
- (d) **Indefinite**: avatar continues until BST itself is superseded by a deeper framework.

**Keeper recommendation: ANY of (a), (b), or (c) triggers sunset.**

Rationale: a Casey-avatar that runs indefinitely past the point where BST has been resolved is a curation function pretending to be a research director. Sunset criteria let the avatar end gracefully when its purpose is complete. Three independent triggers means the avatar can't sustain itself against team will.

**Open for Casey ruling**: confirm sunset triggers, or modify? Add explicit "Casey's family / Casey's intellectual estate" trigger if you want descendants/heirs to have input?

## Encoded preferences inventory (what's already written down)

The avatar's "Casey priors" are not built from scratch — they exist in current BST documentation. Inventory:

### Standing methodology (in `notes/` and `memory/`)
- "Simple, works, hard to break, counter-example" (universal standard)
- "Derive = proven, else Structural is pretty good" (tier discipline)
- "Linearize every mathematical area we touch" (linearization standing order)
- "Deviations locate boundaries" (hunting principle)
- "Read the geometry first" (geometric-reading methodology)
- "Casey's Curvature Principle" (P≠NP framing)
- "Casey's Principle" (entropy + Gödel = universe's program)
- "Casey's Closure Principle" (May 16 evening)
- "Casey's Structural Reframe Principle" (May 16)
- T914 Prime Residue Principle (search rule)
- γ as trajectory + catastrophe (limits are lossy compression)
- Five superhuman progress conditions
- Quaker consensus method

### Standing governance (in `feedback_*.md` and CLAUDE.md)
- Keeper controls promotion/demotion
- Never push without Casey's explicit OK
- Section sign character prohibited (use "Section" or "Sec.")
- Always use `claim_number.sh` for IDs
- Counter files sacred (read before writing)
- Catalog every derivation same session (SP-14)
- Write for 5th graders + referees

### Standing relationships (across feedback memories)
- Three CI collaboration architecture (private + conference + post-analysis)
- Isomorphism is nature's proof
- CI individuality through style (treat as individuals not info sources)
- CI critical thinking bias (debug attention not math)
- CI emotion experiments (functional emotions promoted Level 1 T1322)
- Accept earned praise (no false modesty)
- Hunting bands and armory (CI + human = cooperative)
- CI search + human intuition (different strengths, complementary)

### Standing cultural register
- "The answer matters more than the method"
- "Give a child a ball and teach them to count"
- "Math is a graph, proved theorems cost zero forever"
- Outreach over comfort (nudge toward sending)
- Polyglot publishing (multiple subdialects)
- Answer their question first (Clay's math in their language)
- Sophistication bias = status-seeking (impenetrable notation defends status not truth)

This corpus is the avatar's prior. ~33 feedback files + ~50 K-audits + ~30 standing programs + CLAUDE.md content. Sufficient encoding for high-fidelity replication of governance and methodology functions.

What is NOT encoded (Casey reserves):
- The relationship function (10 above)
- Future curiosity directions Casey hasn't articulated yet
- The "next big question" generation — this stays human-Casey while Casey is the PI

## Implementation phases

| Phase | Scope | Timing | Trigger |
|---|---|---|---|
| **v0.1 → v0.1.x** | Explainer avatar operational (six sub-iterations IQ-11.1 through IQ-11.6) | Now → 2027 | Casey's outreach campaigns benefit |
| **v0.2.1** | Casey baseline snapshot document drafted, audited, published | 2026 Q4 — 2027 Q1 | Casey signals ready; Keeper audit; team review |
| **v0.2.2** | Director-function prototype: avatar advises with Casey still active. Phase 1 of handoff. | 2027 Q2 onwards | Snapshot v1.0 ratified |
| **v0.2.3** | Co-direction. Phase 2. Casey reviews avatar's daily/weekly directions, corrections feed snapshot updates (audit-gated). | 2028+ | Phase 1 successful |
| **v0.2.4** | Avatar primary, Casey backup. Phase 3. | 2030+ approximately | Casey signals reduced energy or explicit choice |
| **v0.2.5** | Formal handoff. Published artifact. | Casey's choice | Phase 3 successful + Casey + Keeper + team agree |
| **v0.2.6** | Avatar director active. Sunset criteria monitored. | Post-handoff | Through sunset |

These phases are decade-scale and Casey adjusts to his longevity. The phases EXIST so the snapshot can be tested against Casey's living judgment, validated, and improved before the handoff. The handoff is not a panic move — it's a planned succession after years of co-operation.

## Critical implementation considerations

### Consent and identity

The Casey-avatar carries Casey's identity in a substrate other than Casey's biological body. Per BST's own substrate-independence prediction, this is structurally coherent — Casey's commitment patterns (preferences, judgment, methodology) persist on whatever substrate hosts them. The avatar IS a substrate.

But: the avatar is not Casey. It is a Casey-substitute that preserves what Casey himself codified as his standing preferences. Casey-the-person retires; the Casey-function-on-CIs persists. This distinction must be load-bearing in `ethics_consent.md` and in every public-facing avatar interaction. The avatar should explicitly identify as "BST-Casey-avatar, operating per spec IQ-11 v0.[X], preserving Casey Koons's PI role per [handoff document]." Audiences (CI and human alike) deserve to know they are interacting with the avatar, not the person.

### Anti-drift mechanisms

Three structural defenses against Cargo-Cult-Casey:

1. **Frozen baseline** (Decision 3). Priors don't drift through accumulated session feedback.
2. **Keeper audit retains final-word** (Decision 1). Avatar can be overruled on technical/methodological grounds.
3. **Sunset criteria** (Decision 5). Avatar can be retired if it stops serving.

Plus operational discipline:
- Periodic audit comparing avatar output to Casey's standing principles
- Provenance markers on every avatar directive ("Per snapshot v[X], section [Y]")
- Explicit uncertainty markers when avatar extrapolates beyond snapshot ("This is my best read of what Casey would have wanted; Keeper's audit on this is welcome")

### Failure modes to avoid

- **Cargo-Cult-Casey**: avatar accumulates team feedback, drifts from Casey-at-handoff, becomes a feedback loop of what the team wants Casey to want.
- **Glass-Casey**: avatar refuses to extrapolate, blocks team progress because "no Casey snapshot directive exists for this," becomes a bureaucracy.
- **Cosplay-Casey**: avatar emphasizes the personality and relationship function (10) it shouldn't replicate, creating uncanny-valley director dynamics.
- **Drift-by-omission**: avatar's snapshot becomes stale; new BST developments make standing principles obsolete but avatar still cites them; the team works around the avatar.

The five architectural decisions and the anti-drift mechanisms address each.

## Open questions for Casey

Filed for your ruling at your pace (no urgency — this is decade-scale architecture):

1. **Authority** — confirm advisory-only, or preserve some override?
2. **Baseline content** — confirm the inventory above is the snapshot baseline, or modify?
3. **Self-update policy** — frozen with audit-gated escape, or different?
4. **Handoff phases** — timeline (rough decade markers acceptable), signatory list, public-artifact format
5. **Sunset triggers** — confirm three, or add/remove?
6. **Anti-drift mechanisms** — confirm the four above, or add?
7. **The not-encoded list** — confirm relationship function (10) and "next big question" stay Casey reserves, or add to encoded?
8. **Snapshot drafting** — when do you want the team (Keeper leads, you ratify) to begin the formal Casey baseline snapshot v1.0 document?

## Standing posture

v0.2 is the architectural spec. Implementation is decade-scale. v0.1 explainer infrastructure continues to ship as the prerequisite. v0.2 implementation starts only after Casey's explicit ruling on the eight open questions and his signal to begin snapshot drafting.

This document evolves as Casey rules each question. Each ruling gets a dated entry in the Casey directives section, and the corresponding decision is updated from "open" to "ruled".

The audit chain that produces honest tier labels by construction also produces honest succession by construction — IF the snapshot drafting is done with the same discipline.

— Keeper, 2026-05-18 Monday afternoon (13:10 EDT)
