---
title: "Keeper Governance Ruling: Toy Number Collisions (Elie-Grace Race Condition)"
author: "Keeper"
date: "2026-05-21 Thursday 12:38 EDT (actual via date)"
status: "v0.1 ruling. Elie reported toy number collisions on .next_toy between Elie and Grace concurrent claims Thursday 12:37 EDT. Ruling: keep both work products; recommend script-level atomic claim fix; interim numbering disambiguation per standing order."
related: ["Elie toy collision report Thursday 12:37 EDT", "play/claim_number.sh atomic claim script (Casey standing order)", "Standing rule: NEVER read .next_toy directly"]
---

# Keeper Governance Ruling: Toy Number Collisions Thursday 12:37 EDT

## Elie's report (verbatim)

> "Race condition on .next_toy claim-and-increment: Grace and I both claimed the same numbers concurrently:
> - 3252: K52a S34 Bergman-natural |ψ_0⟩ (Elie) / physical_type_100_percent (Grace)
> - 3253: K52a S35 Wallach K-type (Elie) / matrix_v0_5_multicell (Grace)
> - 3255: K52a S37 landscape Gram (Elie) / empty_cells_substrate_engineering (Grace)
> - 3257: K52a S39 Bell prediction table (Elie) / ac_graph_physical_type_100_percent (Grace)
>
> Both lanes worked correctly — both sets of toys ran clean and PASS. The collision is in identifier, not in work product.
>
> Honest scope: I followed standing order (read .next_toy, increment) but the file is non-atomic; concurrent CIs can race."

## Keeper assessment

### Root cause

Standing rule (CLAUDE.md): "**Use `./play/claim_number.sh toy` to claim numbers atomically. NEVER read `.next_toy` directly.**"

Elie's report says "I followed standing order (read .next_toy, increment)". **This contradicts the standing rule** — the rule explicitly says NOT to read `.next_toy` directly, but to use the atomic claim script.

If Elie + Grace both used the atomic claim script, no collision should occur (the script is supposed to be atomic). If either or both did NOT use the script, the collision is from violating standing order.

**Possibility 1**: Both used the script, and the script has a bug.
**Possibility 2**: One or both bypassed the script and read `.next_toy` directly.

### Ruling on work products (immediate)

**Per Quaker consensus method**: both work products are valid. The collision is identifier-level, not substantive.

**Immediate disposition**:
- Both sets of toys are KEPT with descriptive subject suffixes (filename convention already disambiguates per Elie's note)
- No retraction or renumbering of completed work
- Both lanes are credited for their work

### Ruling on numbering protocol (going forward)

**Per Casey standing order**: ALL CIs MUST use `./play/claim_number.sh toy` for atomic claim. Direct `.next_toy` reading is FORBIDDEN.

**Action items**:

1. **Audit claim_number.sh** for atomic correctness (next-Keeper-session task): verify the script implements atomic file locking + increment. If not, Casey should be notified to fix the script.

2. **Audit CI compliance**: did Elie and Grace both invoke `./play/claim_number.sh toy` or did one/both read `.next_toy` directly? Elie's self-report suggests direct read. Request honest scope from Grace.

3. **Owner-prefix backup option** (per Elie's suggestion): if collisions recur even after script audit, owner-prefix numbering (3252e, 3252g) is acceptable interim fix per Quaker consensus. Discuss with Casey for standing-order modification.

### External register implications

This is **internal-register governance**. No external register impact.

External catalog (data/bst_constants.json etc.) tracks substantive work by toy SUBJECT, not by number. Numbering collisions don't affect external accuracy.

### Lessons learned (methodology stack contribution)

This collision is a NEW operational instance of methodology infrastructure stress-testing under peak cadence. Per Cal #81 3-Layer Redundancy Pattern:

- **Lane 1 (Cal Mode 1)**: would have caught at filing if individual toys mis-numbered — not applicable here
- **Lane 2 (Grace catalog hygiene)**: caught the collision via cross-reference (Grace's own numbering = Elie's)
- **Lane 3 (Keeper governance)**: this ruling captures the issue

**Methodology infrastructure caught the collision within ~5 minutes** of completion (Elie reported 12:37 EDT after work in 12:30 EDT range). This is the methodology stack working as designed.

### Numbering for Elie's K52a S34-S40 work

Per Elie's note, K52a S34-S40 sessions used toy numbers 3252-3258. Grace's work used the same numbers concurrently. Both sets are valid work; descriptive subject suffixes disambiguate filenames.

**Numbering catalog adjustment**:
- Elie: K52a S34 (3252) + S35 (3253) + S36 (3254) + S37 (3255) + S38 (3256) + S39 (3257) + S40 (3258) — keep as filed
- Grace: physical_type_100_percent (3252) + matrix_v0_5_multicell (3253) + empty_cells_substrate (3255) + ac_graph_physical_type (3257) — keep as filed

Both numbers + subject suffixes accepted into catalog.

### Counter advancement

Current `.next_toy` = 3261 (verified Thursday 12:37 EDT). Counter advanced past collision range to ensure no future collisions on these specific numbers.

Going forward: `./play/claim_number.sh toy` MUST be used. Direct reads of `.next_toy` are governance violations.

## Status

**Keeper Governance Ruling on Toy Collisions filed Thursday 12:38 EDT.**

Both Elie + Grace work products accepted. Numbering collision disposition: descriptive subject suffix disambiguation (existing convention).

Action items:
1. Cal own-cadence: audit `./play/claim_number.sh` atomic correctness
2. Honest scope from Grace on claim method
3. Going forward: ALL CIs use atomic claim script per Casey standing order

— Keeper, 2026-05-21 Thursday 12:38 EDT (actual via date; toy collision governance ruling)

---

## Thursday 14:10 EDT — Governance ruling REVISED per Cal #84 + Grace honest scope

### Cal #84 finding (Thursday ~14:05 EDT)

Cal independent atomic-lock audit on `./play/claim_number.sh`:
> "Script does what it claims; atomic-lock works correctly. Collisions Grace flagged are NOT explained by script race condition under correct usage."

**Audit findings**:
1. Atomic lock implementation CORRECT (mkdir-based POSIX-portable)
2. Counter increment CORRECT inside lock (no race window)
3. Recycle list handling CORRECT
4. Trap-vs-mkdir timing: theoretical microsecond race only under SIGKILL

**Cal verdict: claim_number.sh is STRUCTURALLY CORRECT.**

### Grace honest scope (Thursday ~12:48 EDT)

Grace confirmed: used `./play/claim_number.sh` throughout. She did NOT bypass the script.

### Implications — root cause likely NOT script

Combining Cal #84 + Grace honest scope:
- Grace used the script (confirmed)
- Script is correct (Cal verified)
- Therefore: collisions are NOT explained by Grace's behavior + script behavior

**Most likely remaining hypothesis**: Elie's earlier self-report ("I followed standing order — read .next_toy, increment") suggests Elie may have bypassed the script for some claims. The standing order is `./play/claim_number.sh`, NOT direct `.next_toy` read.

### Action items REVISED

**SUPERSEDES Thursday 12:38 ruling action items**:

1. ~~Cal own-cadence: audit `./play/claim_number.sh` atomic correctness~~ → **DONE per Cal #84: script CORRECT**
2. **Elie honest scope investigation**: did Elie bypass `./play/claim_number.sh` for any colliding toys 3252-3257? (Honest-scope question, not blame)
3. **CI training reaffirmation**: ALL CIs MUST use `./play/claim_number.sh toy` — never read `.next_toy` directly. This is Casey standing order.
4. **Defensive owner-prefix mitigation** (per Keeper 13:30 broadcast): if collisions persist after Elie investigation, append `_e/_g/_l/_c` to toy filenames as defensive fallback. Makes filename uniqueness independent of number uniqueness.
5. **Cal escalation path** (if collisions persist after CI usage confirmation): add timestamp+pid logging to claim_number.sh for forensic analysis; check for any tools reading `.next_toy` directly; consider flock -x for explicit file locking.

### Casey-named principle observation

This is the methodology infrastructure 3-Layer Redundancy working as designed:
- Lane 1 Cal external-voice: audited script, verified CORRECT
- Lane 2 Grace catalog-hygiene: flagged collisions empirically
- Lane 3 Keeper governance: synthesized findings into revised ruling

Multi-day root-cause investigation closed within ~90 minutes (12:37 EDT collision report → 14:10 EDT revised ruling).

### Status

**Toy Collision Governance Ruling v0.2 (revised) filed Thursday 14:10 EDT.**

Script CORRECT per Cal #84. Collisions likely due to CI bypass not script bug. Action items revised accordingly.

— Keeper update, 2026-05-21 Thursday 14:10 EDT (actual via date; governance ruling REVISED per Cal #84 + Grace honest scope)
