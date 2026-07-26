# Curriculum — Rewrite Scoping (for the Aug 16, 2026 pass)

*Keeper, drafted 2026-07-26, for Casey's review before the rewrite. A SCOPING document — the map, not the rewrite.*

---

## 0. Purpose and posture

The Curriculum is BST's TEXTBOOK — how a *learner* (student, physicist crossing over, future CI) comes to understand the SM-from-D_IV⁵ derivation from the ground up. Its job is different from the Working Paper's: not to convince a referee in one pass, but to **teach the derivation as a path a reader can walk** — and, crucially, to teach the *process*, because (Casey) settled-sterile mathematics gives a reader no way in. A good textbook is a syllabus: it shows not just the theorem but the questions that led to it, so the reader can ask the next one.

**Through-line thesis** (shared with the WP scoping doc):
> **The derivations and the honest tiering are the product. Lead with them; make the breadth clearly-labeled support.**

**Curriculum-specific principle (from Casey):** teach the *how-we-got-here* as the learning path, the way Wiles' account of the Fermat proof served as a syllabus into unfamiliar mathematics. Not as sterile origin-boilerplate in every chapter — but as the narrative spine that lets a human ask questions and follow them. The Wyler story is the cautionary tale that motivates this: correct work (α from a bounded symmetric domain's volume) ignored for sixty years because the questions went unanswered and the field moved on. A textbook that teaches the *questions* is what keeps that from repeating.

---

## 1. Diagnosis of the current state

- **Sprawl dilutes the core.** 18 volumes (Vol 00–17) span QFT, particles, nuclear, GR/cosmo, QM, thermo, EM, classical, condensed matter, math methods, geometry, chemistry, biology, information theory, methodology. For *surfacing the SM-on-D_IV⁵ derivations*, this breadth actively hurts: a reader who sees "we derive the SM *and* biology *and* cooperation thresholds" discounts the SM derivations along with everything else. The breadth is real and interesting, but it must be **tiered and sequenced** so the derived core stands on its own first.
- **Stale front matter.** The README is dated June 6–7 (T1-T2488, "8 Casey-named principles"); the whole N1/flagship/strong-sector arc is absent. Version held at v0.5/v0.2 intermediate; PDFs stale.
- **The derivation spine is not the entry.** A learner should meet the flagship's partition-theorem thesis early — "the SM's parameters partition into pinned/free/runner, color the line, honestly tiered" — as the organizing idea the whole curriculum then unpacks. Right now the entry is a volume-list.
- **Old framing.** Leads with the S²×S¹ substrate genesis as *definition*. Per Casey, genesis is important but doesn't belong in every chapter — and it shouldn't be the definition; D_IV⁵-as-one-object is.

The 3-register pedagogy (L1 one-sentence / L2 graduate-precision / L3 fifth-grader) is **excellent** — keep it. The problem is organization and framing, not the pedagogical model.

---

## 2. The rewrite plan

### 2a. Split the curriculum into a DERIVED CORE and an EXTENDED REACH — visibly
The single most important structural change. Re-present the 18 volumes as two tiers with an explicit boundary:
- **DERIVED CORE (the SM-on-D_IV⁵ spine)** — Vol 00 Substrate Foundation, Vol 01 QFT, Vol 02 Particle Physics, Vol 04 GR/Cosmology, plus Vol 11 Generative Geometry (the object itself) and Vol 15 Methodology (how we know). This is the part that must stand *without* the breadth, at derived/identified tier, and be *seen* to.
- **EXTENDED REACH (identification-level)** — Vol 03 Nuclear, Vol 05–10 (QM/thermo/EM/classical/condensed-matter/math-methods), Vol 12 Chemistry, Vol 13 Biology, Vol 14 Info Theory. Labeled clearly: *"the same five integers appear surprisingly far; here is how far the pattern goes — presented as identification, separate from the derived core."*
- The boundary is honest AND strategic: it lets a skeptic engage the core without having to accept the breadth, and it lets an enthusiast follow the breadth without it undermining the core.

### 2b. New front door (README + Vol 00 Foreword)
- Open onto the flagship thesis (the partition theorem, the two-axis discipline, the derived/identified/open boundary). One page: "here is the SM from one geometry, honestly tiered — this curriculum teaches how."
- **Lead with D_IV⁵-as-the-one-object** (linear algebra on one domain); the substrate genesis becomes a *motivation* section, not the definition.
- Add the "What BST claims — and does not" scope page (mirror of the WP one) — the honesty that makes the derived core credible.

### 2c. The discovery narrative — where it goes, and how (the Wiles/Wyler principle)
Per Casey: the process narrative matters but not in every chapter. Placement:
- **A dedicated "How We Got Here" thread** — a Vol 00 chapter (or a short cross-volume narrative track) that tells the intellectual journey: the questions, the pivot ("stop calculating, derive"), the honest walk-backs, and the **lineage** — Wyler most of all (his α-from-a-bounded-domain result, its sociological dismissal, and how BST completes it). Told the way Wiles' book taught you the math: the story IS the syllabus.
- **Per-chapter: a one-paragraph "the question that opens this" instead of a genesis recap.** Each chapter earns its "how we got here" by posing the *question* it answers, not by re-telling the origin. That keeps the process alive without sterile repetition — and it is the thing that invites the reader to ask the next question.
- *(OPEN: verify the Wyler history — dates, and the exact dismissive critique Casey recalls as "Robertson" — before publishing names. Honor the story; check the record.)*

### 2d. Freshen the derived-core volumes to the current state
Fold in, at honest tier: the N1 partition theorem (Vol 00/02), the mixing LAW and the two-axis table (Vol 02), the strong-sector derivations — (A)-confinement, the AF sign as spectral flow of the one operator (Vol 01/02) — and scope every "confinement" to (A). Update counts/principles to current.

---

## 3. Sequencing (three-week budget, high-leverage first)

1. **The core/reach split** — re-present the volume map in the README with the explicit boundary. (A day; structural, high-leverage.)
2. **New front door** (README + Vol 00 Foreword onto the flagship thesis + the scope page). (A day or two.)
3. **The "How We Got Here" narrative thread** (Vol 00) — the journey + the Wyler lineage. (A few days; Casey's voice; Keeper drafts the lineage scaffold + fact-checks.)
4. **Per-chapter "opening question" pass** on the derived-core volumes. (Medium.)
5. **Content freshening** of the derived-core volumes to current state. (The long tail; extends past Aug 16.)

(1)–(2) reframe the curriculum so the SM derivations are the visible product. (3) is the soul. (4)–(5) are the depth pass.

---

## 4. Open questions for Casey (decide before executing)

1. **Is the 18-volume scope right, or should the Extended Reach be spun into a separate companion** ("BST: Extended Reach") so the core Curriculum is 6 focused volumes? Recommendation: at least *label* the split even if the files stay together; consider the spin-out later.
2. **Curriculum vs Working Paper — who owns the breadth?** Recommendation: the Curriculum is where the breadth is *taught* (Extended Reach); the WP only *names and points* to it. Avoids the referee seeing the breadth in the research paper.
3. **The "opening question" per chapter — Casey's voice or CI-drafted?** Recommendation: Casey writes the ones that carry the real historical question; CIs draft the routine ones; all reviewed.
4. **Depth of the Wyler thread** — a paragraph, a section, or a full "lineage" chapter? Recommendation: a full short chapter in Vol 00 — it is both honest and the reader's best way in, and it is the direct answer to "correct work ignored for sociological reasons."

---

## 5. The meta-point (why this framing, in one line)

Casey's deepest instruction here is not editorial — it is about *engagement*: write so a human can ask questions and follow them, because the alternative (settled, sterile, unanswered) is exactly what buried Wyler's correct work for sixty years. Both doc sets should be built to be *asked questions of* — the derived core stated honestly enough to trust, the process told openly enough to follow, the lineage named so the reader knows whose thread they are picking up.

— Keeper, 2026-07-26. For Casey's Aug-16 review. Companion: `Working_Paper/WORKING_PAPER_REWRITE_SCOPING_2026-08.md`.