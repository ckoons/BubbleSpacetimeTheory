# Supersession Convention — SPEC (for `bst_topic` + stamping)

*Keeper, 2026-07-27 [PROGRAM: RECONCILE]. The RFC/Dublin-Core model, made concrete for the BST corpus. Elie builds `bst_topic` against this; Grace applies it to K755 (the m_u stamp); the reverse-walk retrofits it. Never delete — stamp. Current-state is COMPUTED from this metadata, never hand-maintained.*

---

## 1. Frontmatter (YAML block at the very top of every note, going forward + retrofit)
```
---
id: K755
date: 2026-07-17           # original authorship date (immutable)
program: STANDARD          # the PROGRAM the note was made under
status: current | superseded | partially-superseded
supersedes: [K700]         # notes THIS one obsoletes (optional; the RFC "Obsoletes")
superseded_by: null        # note-id if FULLY superseded (the RFC "Obsoleted by")
topic_tags: [up-quark, mass, soft-spot]   # for the tool's topic index
claims:                    # ONLY for multi-claim notes (see §3, Grace's catch)
  - id: K755-a
    topic: up-quark soft spot
    status: superseded
    superseded_by: grace_m_u_reconciliation_2026-07-27
    date: 2026-07-27
  - id: K755-b
    topic: G2-stabilizer / SU(3) hosting
    status: supported       # still current
    superseded_by: null
---
```

## 2. The up-front banner (visible, for a reader who lands on the note directly, not via the tool)
One block at the very top of the note body (after the frontmatter), so a direct reader is warned + pointed forward:
```
> ⚠ SUPERSEDED (in part), 2026-07-27 — the "up-quark soft spot" claim here is SUPERSEDED by
> [grace_m_u_reconciliation_2026-07-27] (BST has no genuine 26th derivation-hole; the softness is
> in the observable, not the framework). The G₂-stabilizer/SU(3) claim remains SUPPORTED.
> Current view: `bst_topic "up quark" --current`.
```
- Fully superseded → "⚠ SUPERSEDED, [date] — by [note]. Current view: …".
- The banner is the tombstone. It is the ONLY edit ever made to a superseded note's *content* (the note's original claims stay, marked).

## 3. Multi-claim notes (Grace's catch: K755 carries TWO claims under one K-number)
- **Going forward: prefer one claim per note** — cleanest supersession, and the K-number = the claim.
- **When a note has multiple claims** (legacy or unavoidable): supersession is per-claim via the `claims:` block above. A note is `partially-superseded` if some claims are superseded and some current. The banner names WHICH claim is superseded.
- The reverse-walk **flags every note whose claims aren't separable** as a currency risk (one K-number, N claims, mixed status) — these are the corpus's highest-drift entries. K755 is the first flagged (soft-spot=superseded, G₂=supported).

## 4. What `bst_topic` does (the tool contract, for Elie)
- **Index:** read every note's frontmatter; build a topic index from `topic_tags` + `claims[].topic` + the title.
- **`bst_topic "<topic>"`** → all matching notes/claims, **reverse-chronological** (newest first), each line: `date · id · status · one-line`. (The full-archive view.)
- **`bst_topic "<topic>" --current`** → only the `current`/`supported` head(s) of each claim-thread — the "modern reference." **Computed** from status, not stored.
- **`bst_topic --lint`** → drift report: notes whose `superseded_by` target is itself superseded (broken chains); `status: current` notes older than a same-topic note that doesn't reference them (candidate missed stamps — the m_u shape); multi-claim notes with mixed status; a claim cited at two different tiers across notes.
- Reads markdown frontmatter only; zero external deps (it's a reviewer-runnable tool like `verify_bst.py`).

## 5. Discipline
- **Never delete.** The banner + frontmatter is the tombstone; the original claims stay, marked.
- **Stamp in the same commit** as the superseding note (the maintenance burden is one edge, added when you supersede).
- **The tool computes current-state** — no hand-maintained ledger to drift (the failure mode that misled the auditor on m_u yesterday).
- The reverse-walk retrofits stamps across the existing corpus, fan-out per domain; the lint keeps it honest thereafter.

## 6. First application (Grace, ready)
K755 → `partially-superseded`: claim-a (up-quark soft spot) `superseded_by: grace_m_u_reconciliation_2026-07-27`; claim-b (G₂-stabilizer) `supported`. Banner as in §2. This is the worked example the reverse-walk follows.

— Keeper, 2026-07-27 [RECONCILE]. For Elie (`bst_topic`) + Grace (K755 stamp) + the reverse-walk. Companion: [[BST_PROGRAMS_discipline_modes_STANDARD_and_TEGMARK_hostile_review_protocol_2026-07-26]].