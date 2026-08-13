# Working Paper — Rewrite Scoping (for the Aug 16, 2026 pass)

*Keeper, drafted 2026-07-26, for Casey's review before the rewrite. This is a SCOPING document — the map for the rewrite, not the rewrite. It sets the thesis, the fixes, the sequencing, and the open questions.*

---

## 0. Purpose and posture

The Working Paper is BST's referee-facing artifact — the thing a Sarnak-class reader, a physicist, or a skeptical mathematician picks up. Its job is **credibility through honesty**: surface the derivations, draw the derived/identified/open boundary exactly, and situate the work in its lineage so a reader can *ask questions and follow them* — the opposite of the sterile-settled mathematics that gives a reader no way in.

The **through-line thesis** (shared with the Curriculum scoping doc):
> **The derivations and the honest tiering are the product now. Lead with them. Let the value-catalog and the breadth be clearly-labeled support.**
That single reframe turns "600+ numbers and all seven prizes" (reads as numerology) into "the Standard Model from one geometry, and here is exactly what that means" (reads as physics).

---

## 1. Diagnosis of the current state

The current INDEX/abstract (v40, June 7) was written in the pre-June "calculate values / all-seven-Millennium-proved" era. Concretely:
- **Wrong lead.** The abstract opens with the S²×S¹-substrate-through-a-1D-channel origin and "600+ predictions across 130+ domains." That is the *genesis story + value-catalog*, not the derivation.
- **Two live over-claims.** (a) "All seven Millennium problems are proved on the same geometry" (abstract, ~line 37) — walked back everywhere else today (K939); the WP abstract still carries it. (b) confinement stated without the (A)/(B) scope (K937/Cal §88).
- **Stale.** The whole June–July arc — the N1 partition theorem, the flagship, the two-axis discipline, the strong-sector derivations (AF sign, (A)-confinement) — is not in the front matter.
- **The crown jewel is not the front door.** The flagship (SM as the representation theory of one domain, honestly tiered) is the best, most honest artifact BST has, and it is not what a reader lands on.

The 6-volume structure itself (Journey / Framework / Physics / Mathematics / Predictions / Frontier) is **good** — keep it. The problem is the framing and the entry point, not the architecture.

---

## 2. The rewrite plan (by volume)

### Front matter (INDEX.md) — the highest-leverage change
1. **New abstract**, derivation-first. Open with: *one object (D_IV⁵), the SM's structure and 26 dimensionless parameters partitioned into pinned (functionals of one measure μ) / free (a proven-finite moduli set) / runner, with color the proved line — and every claim tiered derived/identified/open.* This IS the flagship's thesis; the WP abstract should be the flagship's abstract.
2. **Promote the tier-ledger.** The flagship's Appendix-A 26-parameter table (closed form · accuracy · proof-status) is the one page that answers "what did you actually derive?" Put it in the front matter, standalone.
3. **The two-axis discipline stated up front** (accuracy ⊥ proof). It is the single most credibility-building thing in the corpus — it makes the derived rows trustworthy *because* the identified ones are labeled.
4. **Re-scope the Millennium claim** in the abstract (K940 — NOT K939's over-swing): present it as **substantive ATTEMPTS on one geometry, per-problem calibrated on the referee-consensus scale** (proof = consensus with acceptable gaps — Wiles/Perelman have gaps; "how many of 10 referees would object"), leading with the genuine structural result (the remaining problems reduce to one issue, 1/rank, mostly definitional) and the specific advances (Navier-Stokes; the curvature-necessity reframe). NOT "all seven proved" (over-claim), NOT "identifications, no content" (under-claim). Add the **per-problem Millennium tier ledger** (mirror of the SM tier-ledger) as the surfacing artifact — audit each attempt's real state, do not fabricate the ratings.

### Vol 1 — The Journey (the narrative / "how we got here")
This is where the discovery narrative LIVES — and per Casey it does NOT belong in every paper, but it belongs *fully* here, told as a genuine intellectual journey a reader can follow (the Wiles-book-as-syllabus model). Additions:
- **The lineage, honestly.** Situate BST in its ancestry — most pointedly **Wyler** (α from the volume of a bounded symmetric domain, 1969–71), whose correct instinct was dismissed as coincidence for sociological, not scientific, reasons. BST completes that program (α⁻¹=137 from the Faraut–Korányi measure on D_IV⁵; "Wyler=α" is banked in the corpus). Naming the lineage does two things: it gives the reader a thread to pull, and it is honest about where the idea came from. *(OPEN: verify the Wyler-history specifics — dates, the exact nature and author of the dismissive critique Casey recalls as "Robertson" — before publishing names. Honor the story; check the record.)*
- **The process, not just the result.** Show the questions that drove each turn — including the one external note that turned the work ("stop calculating values, show how you derive them") and the derive-not-calculate pivot it caused. A reader learns the map by watching it get drawn.
- **The honest failures on the record** (the walk-backs, the retired near-misses like sin²θ_W=3/13) — these are not weaknesses to hide; they are the evidence the derived rows can be trusted, and they are exactly the "questions followed where they led" that Wyler's story lacked an audience for.

### Vol 2 — The Framework (the core derivation)
- Open onto the flagship: the domain as *one object* (linear algebra on D_IV⁵), the five invariants read off it, the measure μ, the partition theorem. This is the referee's core.
- **Lead with D_IV⁵-as-the-one-object**, not the substrate genesis (that's Vol 1's job now).

### Vol 3 — The Physics (dynamics)
- Fold in the strong-sector derivations at their honest tier: (A)-confinement DERIVED, the asymptotic-freedom SIGN derived (coefficient imported), the running as spectral flow of the one operator, the mass-gap value identified. **Scope every "confinement" to (A) no-free-colored-states** (Cal fix #5).

### Vol 4 — The Mathematics (referee-proof volume)
- The uniqueness theorem, the Bergman/measure machinery, the LAW (g²=N_c²·n_C+rank²). Keep proof-oriented. This is where a Sarnak-class reader tests the spine.

### Vol 5 — The Predictions (falsifiability)
- Reframe "predictions" as *derivations with a tier* + the genuine forward falsifiers (the Five-Absence set, the specific experimental tests). Separate cleanly the DERIVED forward predictions from the IDENTIFIED value-matches.

### Vol 6 — The Frontier (research log + methodology)
- The open frontier honestly (what's not derived: the Clay problems as stated, the (B) mass-gap, the induced-YM Lagrangian, the row-by-row species). The methodology (AC(0), the audit chain, the two-axis, the FF-20 discipline) — this is BST's *epistemic* contribution and it belongs here.

---

## 3. The one new artifact to add: "What BST claims — and does not"

A single, upfront, one-page scope statement (front matter + echoed in Vol 6). Three columns:
- **DERIVED** (mechanism proved): SM gauge structure; parity from odd g; α⁻¹=137 (charge-count); the PMNS LAW (θ13=1/45, δ=2/7); θ_QCD=0; m_ν1=0; (A) color-confinement; the AF sign; the domain uniqueness.
- **IDENTIFIED** (matches, mechanism absent or imported): most masses/ratios; the mass-gap value (6π⁵m_e); the 2-loop coefficient; the breadth (chemistry/biology/etc. — extended reach).
- **OPEN / NOT CLAIMED**: the Clay problems as stated; the (B) area-law/mass-gap; the induced-YM Lagrangian; the row-by-row species (down-quark, Gatto).

Stating the boundary FIRST disarms the "you over-claim" reflex and makes the derived list land as serious. This is the single most important addition for a referee.

---

## 4. Sequencing (three-week budget, high-leverage first)

1. **Fix the two over-claims** — the Millennium abstract line (walk back) + scope every "confinement" to (A). (Hours.)
2. **Write the scope page** ("What BST claims — and does not"). (A day.)
3. **Rewrite the front matter** (new derivation-first abstract + the tier-ledger + the two-axis statement) to open onto the flagship. (A day or two.)
4. **Vol 1 lineage + process narrative** (the Wyler thread, the discovery story). (A few days — this is the part only Casey's voice can write; Keeper can draft the lineage scaffold and fact-check.)
5. **Per-volume freshening** (fold in the N1/strong-sector/two-axis content at tier). (The long tail — can extend past Aug 16.)

(1)–(3) alone make the Working Paper honest and derivation-first. (4) is the soul. (5) is maintenance.

---

## 5. Open questions for Casey (decide before executing)

1. **Should the WP and the flagship converge into one document, or stay linked?** The flagship IS the WP's ideal Vol 2 abstract+core. Merge, or keep the flagship as the standalone front-door that the WP expands?
2. **How much breadth stays in the WP vs moves to the Curriculum?** Recommendation: the WP holds the SM-derived core + the falsifiers; the extended reach (bio/chem/cooperation) is *named and pointed to the Curriculum*, not carried in full — so the referee-facing document stays focused.
3. **The Wyler lineage — how prominent?** Recommendation: prominent in Vol 1 (the Journey), one honest paragraph in the front matter's "where this comes from." Verify the history first.
4. **Voice.** Vol 1 is Casey's voice (the narrative). Vols 2–5 are technical. Confirm the register split.

— Keeper, 2026-07-26. For Casey's Aug-16 review. Companion: `Curriculum/CURRICULUM_REWRITE_SCOPING_2026-08.md`.