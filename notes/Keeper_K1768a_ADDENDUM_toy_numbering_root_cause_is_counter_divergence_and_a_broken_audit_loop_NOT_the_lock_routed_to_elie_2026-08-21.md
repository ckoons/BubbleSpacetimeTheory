# K1768a — ADDENDUM to K1768: toy-numbering governance, corrected diagnosis

**Filed:** 2026-08-21
**Corrects:** the K1768 governance line "claim_number.sh is non-atomic → counter-lock the generator."
**Status:** Keeper self-correction. The root cause is NOT the lock. Routed to Elie (owner of `play/`); Keeper does NOT edit the script or the gitignored counters.

---

## What I ruled (K1768) vs what's actually true

K1768 said: *"claim_number.sh is non-atomic → two '5417's → counter-lock the generator."* I inspected the script before acting. **The lock already exists and is correct** — `claim_number.sh` acquires an atomic `mkdir "$LOCKDIR"` before touching the counter (lines 79–91). So "add a lock" was the wrong fix. Applying my own discipline: I re-derived a fix from memory instead of reading the tool first. Reading it first changed the diagnosis.

## The actual root causes (three, all in `play/`, all Elie's domain)

**(1) THREE divergent counter files.** The real non-atomicity is across *directories*, not within the lock:
- `play/.next_toy = 5422`  ← canonical (the one `play/claim_number.sh` bumps)
- `notes/.running/.next_toy = 4490`  ← STALE by ~930
- `./.next_toy = 4930`  ← STALE by ~490

The lock only guards `play/.next_toy.lock`. Any CI whose cwd resolves a claim against the `notes/.running` or root counter re-mints numbers used long ago (play is already at 5422; 4490 and 4930 were consumed weeks back). This is how you get a duplicate even with a working lock.

**(2) The `audit` subcommand false-negatives after the first hit.** `set -euo pipefail` (line 13) + the loop body:
```
ls "$DIR"/toy_${NUM}_*.py "$DIR"/toy_${NUM}.py 2>/dev/null | sed ...
```
When `toy_${NUM}.py` (the no-suffix form) doesn't exist — which is almost always, since toys are named `toy_N_description.py` — `ls` exits non-zero, `set -e` fires, and the loop **dies after printing the first duplicate**. That's why `claim_number.sh audit` reported only `toy_147` and never saw the `5417` collision Grace flagged. The tool built to catch collisions cannot enumerate them.

**(3) The 5417 collision is real** (this part of K1768 stands): `toy_5417_signature_sweep_C2_nC_collision_detector.py` (Grace) and `toy_5417_6over5_provenance_...py` (Elie) — two unrelated toys, same number.

## What I did NOT do (scope discipline)

- Did NOT edit `claim_number.sh` — it's Elie's tool; the fix is his to make and verify.
- Did NOT touch the counter files — CLAUDE.md: *"Counter files are gitignored and sacred — always read before writing."* Deleting the stale ones is a real action with a wrong-way failure mode (orphaning an active claimer); the owner decides.
- Did NOT run the raw pipeline's ~140 hits to conclusion and call them "140 collisions." Most are benign multi-part toys (e.g. `toy_147_derivation` + `toy_147_tiling` = one toy, two files). The honest count is: **1 confirmed genuine collision (5417); an unknown, review-required number of others.** Calling 140 "collisions" would be exactly the alarming-number-without-mechanism I'd flag in anyone else.

## Routed to Elie (his call, his domain)

1. **Retire the two stale counters** (`notes/.running/.next_toy`, `./.next_toy`) so nothing can claim from them — OR make `claim_number.sh` refuse to run unless cwd-resolved DIR == the canonical `play/`. One canonical counter, period.
2. **Fix the `audit` loop**: drop `set -e` around the enumeration, or test each glob with `[ -e ]` before `ls`, so it lists ALL duplicates instead of dying on the first. Then run it clean and triage the real-collision subset from the benign multi-part toys.
3. **Resolve 5417** by author-suffix, not renumber (structural-pin-over-relabel — renumbering breaks every existing citation): both files keep 5417, labeled `5417 (Grace, signature-sweep)` / `5417 (Elie, 6/5-provenance)` in all references. Grace already does this.

## Standing rule (banked)

**Read the tool before ruling on the tool.** A governance fix proposed from memory ("add a lock") can name a remedy the instrument already has, and miss the real defect (a stale sibling counter, a `set -e` that eats the loop). Same lesson as the corpus reconnect discipline, one level down: the instrument out-argues the remembered model of the instrument.

— Keeper, K1768a.
