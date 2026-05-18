---
title: "Lyra read-pass on Paper #115 v0.4"
date: "2026-05-17"
status: "Two minor cleanups needed. Architecture sound; v0.4 substantively closes the Sunday work."
target_file: "notes/BST_Paper115_Three_Root_Theorems_outline_v0.4.md"
---

# Lyra read-pass — Paper #115 v0.4

**Overall verdict**: v0.4 is substantively complete. Elie addressed all three of my v0.3 M-issues cleanly (M1 chronological reorder, M2 Klein tier consistency, M3 Heegner 9.4 reconciliation) AND incorporated the day's later landings (Mathieu PROMOTED, Cal's Type C, 231 cross-domain, 24 max-over-determined). Architecture table accurate. Abstract reflects state. Cal's full grade-pass can proceed.

Two issues found — both minor, both 30-second fixes.

## Issues

### m1 — Duplicate subsection number 4.10.5

Lines 698 and 711 both labeled `### 4.10.5`:
- Line 698: "Striking cross-domain finding: 231 = N_c·g·c_2"
- Line 711: "Strength comparison to Heegner"

The first (231 finding) is the more substantive new content; renumber the second to 4.10.6, then bump current 4.10.6 ("Why Mathieu introduces a structural reading distinct from Klein") to 4.10.7.

### m2 — Architecture table says "Mathieu Root #5 candidate status"

Section 9.4 architecture table reads:

> **Mathieu Root #5 candidate status** (Grace Toy 2975, 11/11 PASS, 2026-05-17):

But Mathieu is PROMOTED to ESTABLISHED in v0.4. The "candidate status" wording is leftover from v0.3's framing. Suggest changing to:

> **Mathieu Root #5 promotion evidence** (Grace Toy 2975, 11/11 PASS, + Toy 2976 EOT verification, 2026-05-17):

Or "Mathieu Root #5 — three criteria status:" — either works. The rest of the bullets are correct (Mukai 1988, EOT 2010, etc.).

## What v0.4 got RIGHT

- Section 4.10 (Mathieu ESTABLISHED) — clean structure, Keeper verdict verbatim, three criteria cleanly mapped (Mukai/Jordan/BST atoms)
- Section 5.7 (Type A/B/C taxonomy) — three types defined cleanly, structurally-privileged-integer signature added as bridge to Section 5.9
- Section 5.8 (231 = N_c·g·c_2 cross-domain) — independent callout with K44 null-rate framing
- Section 5.9 (24 as maximally over-determined integer) — both Type A and Type B simultaneously, clean elevation
- Abstract — captures the Heegner cycle honestly (proposed → restored → walked back → final L1-candidate), six ESTABLISHED clearly stated
- Section 1.2 — clean source / candidate / mechanism distinction with mechanism statements for each ESTABLISHED root
- Architecture summary table — correct content modulo m2 above

## Recommended action

Elie: 30-second fix (m1 renumber + m2 wording). Then Cal grade-pass.

After Cal grade-pass and any minor adjustments: v0.4 is ready for Casey review.

## What I'm not flagging

- The Heegner section (4.6) is long but the length is justified — it preserves the audit trail (Grace withdrawal → restoration → Cal walk-back → Keeper governance) which is itself the structural-reality signal v0.4 reports as methodological evidence. Cutting it would lose value.
- Cross-references throughout (Section 4.8.3, 5.4, etc.) check out.
- v0.3.1 F1 inheritance: I haven't separately read v0.3.1, but the v0.4 abstract / Section 1.2 / Section 9.4 internal consistency on Heegner labeling is clean, so the F1 fix flowed through.

— Lyra, 2026-05-17 ~12:15 EDT
