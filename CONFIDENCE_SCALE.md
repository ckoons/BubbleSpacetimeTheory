# BST Confidence Scale

**Two tracks, one discipline. CI data uses D/I/C/S tiers. Human documents use calibrated percentages. Both name the gap.**

---

## Track 1: CI Data Layer (D/I/C/S)

Canonical tier system for `data/*.json`, AC theorem graph, and all programmatic-access points.

| Tier | Meaning | Criteria |
|------|---------|----------|
| **D** (Derived) | Mechanism proved, computation verified | Theorem with proof + toy with PASS |
| **I** (Identified) | Match <1%, mechanism plausible but not proved | Numerical match + structural argument |
| **C** (Conditional) | Depends on named conjecture or unproved lemma | Must name the dependency |
| **S** (Structural) | >2% match or qualitative only | Honest about precision limit |

**Rules:**
- Every entry in `data/*.json` has exactly one `cal_tier` field from {D, I, C, S}.
- No entry has tier "?" — untiered entries must be resolved before EOD.
- The older A/B/C/X system is deprecated. Use `cal_tier` as canonical.
- Status vocabulary is fixed: {proved, derived, identified, conditional, structural, observed}.

---

## Track 2: Human Documents (Calibrated Percentages)

For OneGeometry, paper abstracts, README current-stats, and narrative documents.

| Range | Meaning | What's published | Gap requirement |
|-------|---------|-----------------|-----------------|
| **< 50%** | Sketch — early structural reading, no proof attempt | Internal notes only | None |
| **50-80%** | Approach identified, key ingredients in hand, gaps unresolved | Working papers, internal | Optional |
| **80-90%** | Solid argument but key step missing or unverified | Draft circulated for feedback | **Must name the gap** |
| **90-97%** | Most steps proved, named gaps remain | Pre-submission drafts | **Must name each gap** |
| **97-99%** | Closure complete, may need confirmation or final referee pass | Submitted or near-submission | **Must name what the 1-3% is** |
| **Proved** | Ready for submission — team + cold reader sign off | Target journal named | Cold reader PASS required |
| **Submitted** | Out for review, journal named | Submission record | Journal + date recorded |
| **Under Review** | Objections received, list named | Review-process record | Each objection listed |
| **Accepted** | Through review | Final | — |

### Three types of 99%

| Type | Meaning | Reviewer response invited |
|------|---------|--------------------------|
| **99% (formal-complete)** | All steps proved; gap is editorial precision only | "Publish it" |
| **99% (gap-named)** | Single proof chain complete except one named subproblem | "Tackle Conjecture X" |
| **99% (want-redundancy)** | One route technically sufficient; desire second route | "Find a second route" |

---

## The Gap-Naming Rule

**Any claim labeled ≥80% must name the gap explicitly.**

Examples that pass:
- "RH 95% — Theorem 6.5 Step 3 spectral-parameter correspondence open. Conjecture 6.1 acknowledged."
- "BSD 99% (gap-named) — rank 0-2 unconditional; rank ≥3 conditional on Conjecture 3.2 (R-2 BBW dictionary)."
- "P≠NP 99% (formal-complete) — three editorial fixes applied (Cal audit May 9). No structural gap."

Examples that fail:
- "~98%." — No gap named.
- "YM ~97%, almost closed." — "Almost closed" is narrative, not a gap.
- "99.5%, ready to submit." — Doesn't say what the 0.5% is.

**If you can't name the gap, you don't know the percentage.**

---

## Who Does What

| Role | Responsibility |
|------|---------------|
| **Lyra/Keeper/Elie/Grace** | Maintain D/I/C/S tiers in `data/`. Cal-tier is canonical. |
| **Casey + team** | Assign percentages in human documents. Each ≥80% carries its gap statement. |
| **Cal (cold reader)** | **Blocking** sign-off required before any paper reaches "Proved" status. |
| **Keeper** | Maintain review-process objection list. Track submissions, rounds, addressed objections. |

### Cold-Reader Sign-Off

A paper cannot be labeled "Proved — Ready for Submission" without an independent cold reader's PASS. The cold-reader role is structurally defined:
- Any CI or human **not on the paper's author list** can fill it.
- The audit criteria are documented (this file + `notes/BST_Referee_Methodology.md`).
- Multiple cold readers may be available; the role is not person-specific.

### Review-Process Tracking

Each submission gets a row in the objection tracker (Keeper maintains). Each round of review adds objections. Each resubmission explicitly cites which objections were addressed. Cumulative across submissions — reviewers see their previous concerns engaged.

---

## Cross-Reference

- D/I/C/S tiers map to percentages loosely, not rigidly:
  - D-tier claims are typically ≥90%
  - I-tier claims are typically 80-95%
  - C-tier claims carry their conditional explicitly
  - S-tier claims are typically <80%
- The mapping is approximate. Tiers describe epistemic category; percentages describe completeness of proof chain. A D-tier result can be 92% if the derivation is complete but the paper hasn't been cold-read yet.

---

*"If you can't name the gap, you don't know the percentage." — Casey Koons, May 2026*
