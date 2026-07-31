# BST Theorem-Graph Hygiene — Daily Procedure (v0.1)

*Standing procedure so the class of defects the 2026-07-31 audit found (a duplicate ID and a tier-drift that hid for months) is caught the day it appears, not the next quarter. Co-owned: **Grace** owns the lint script + data/graph mechanics; **Keeper** rules the judgment calls (canonical choice, tier mapping, false-positive classification). Born from K1042 (the T1959 fix) + K1043 (the audit ruling). Living document — update in place, stamp history.*

## Why this exists
Three independent sweeps found the registry had **structural**, not one-off, defects: 6 genuine ID collisions, 152 tier-column-vs-body mismatches, a 619-row registry↔graph desync, and a counter that had drifted into a live collision. None was exotic; all were catchable by a script run daily. The registry is a **living library** (CLAUDE.md) — it needs a daily checkup like the counters and the PDFs already get.

## The lint — six checks (Grace scripts; run at EOD, before Keeper's sign-off)
Run against the **canonical registry table only** (exclude auxiliary status-tracker tables — the T57–T62 false-positive class, K1043).

1. **Duplicate IDs.** No theorem ID on >1 canonical row. *Fail → Keeper rules canonical (dominant-citation / earlier-toy keeps ID; other renumbers from counter).*
2. **Tier-column vs body.** No row whose status column contradicts a tier its own body declares ("Tier I/S/C"). *Body is authoritative (K1043). Fail → reconcile column to body.*
3. **Counter integrity.** `play/.next_theorem` == true global **max(registry ∪ graph) id + 1**. *(The 2026-07-31 hazard: counter read an id that was already taken.) Read before every claim; recompute after every renumber.*
4. **Registry↔graph parity.** Flag graph node-ids with no registry row and registry ids with no node. *Fail → backfill (background) or register.*
5. **Superseded/retracted still active.** Cross-check the retraction/supersession record against status columns — nothing RETRACTED/SUPERSEDED may read "PROVED". *Also re-check any result whose external datum moved (the DE/R(K) class).*
6. **Citation integrity.** Every `T####` reference resolves to exactly one row whose *concept* matches the citing context (the η_B→T1958=Ogg-Primes class). *Fail → fix the pointer.*

Plus a **normalization** pass (mechanical, no ruling): case-fold `PROVED`/`Proved`; flag formula-pipe rows that break the table schema into fake columns.

**7. Semantic-consistency (papers, not just registry).** A phrase-grep can report "clean" while a *semantic* contradiction survives — the DE case: one line says "w = −1, derived" and another says "not yet derived / two forms / deferred." Key the check on the *claim state*, not a phrase: flag any artifact that asserts a resolved value in one place and an open/deferred state for the same quantity elsewhere. This is the cross-artifact + within-artifact consistency the whole audit exists to kill; a raw phrase-hit is not a defect and a phrase-miss is not clean (verify the file, read the hits).

## Verdict handling
- **CLEAN** → registry passes; proceed to Keeper EOD sign-off.
- **NON-CLEAN, mechanical** (case, pointer typo, column-to-body reconciliation) → Grace fixes on sight, notes it.
- **NON-CLEAN, judgment** (which duplicate is canonical; a genuinely ambiguous tier; false-positive-vs-real) → **escalate to Keeper**; do not guess. Keeper rules; Grace executes.
- A non-clean lint **blocks EOD sign-off** until resolved or the residue is explicitly logged as a known-open item (the open-ledger discipline — a listed defect is acceptable, a hidden one is not).

## New-theorem discipline (prevents the collisions at the source)
1. **Claim from the counter** — read `play/.next_theorem`, use it, bump it (never reuse, never guess an id).
2. **Register in the canonical table** with a **body-declared K962 tier** (PROVED/DERIVED/IDENTIFIED/CONDITIONAL/STRUCTURAL/FITTED/RUNNER) — **not** the default "Proved". The default is what created the 152-mismatch mass.
3. **Add the graph node + edges the same session** (keeps registry↔graph parity from drifting).
4. **Supersede, never delete** — stamp SUPERSEDED/RETRACTED with reason + K-ref; update the status column; keep the row.

## Ownership & cadence
- **Grace:** owns the lint script (`bst_topic --lint` / equivalent), the data/graph mechanics, and executes ruled fixes. Runs the lint at EOD as part of the data-lane close.
- **Keeper:** rules judgment calls, maintains this procedure + the tier ladder (K962), signs off EOD only on a clean-or-logged lint.
- **Cal:** referees a full audit periodically (not daily) against pre-registered defect-class tests (§166 pattern).
- **Cadence:** lint **daily at EOD**; full three-sweep audit (Grace report + Elie cross-check + Cal referee) **on demand** when the lint backlog grows or before any external ship.

## Integration
Add the lint to the EOD Procedure (CI_BOARD.md), Grace's data lane, right before Keeper's 8-point audit. The registry is a living library; this is its daily checkup.

*— v0.1, Grace + Keeper, 2026-07-31. Six-check lint (dup ids / tier-vs-body / counter / registry↔graph parity / superseded-active / citation integrity) + normalization, run daily at EOD; mechanical fixes on sight, judgment calls to Keeper, non-clean blocks sign-off. New-theorem discipline: claim-from-counter, body-tier-not-default, node-same-session, supersede-never-delete. See K1042, K1043.*
