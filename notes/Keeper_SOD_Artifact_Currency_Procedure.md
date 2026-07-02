# Keeper Start-of-Day Artifact-Currency Procedure (Keeper #28, operationalized)

**Owner:** Keeper | **Established:** Mid-Year 2026-07-02 (Casey-directed) | **Cadence:** every session start, before audit work.

**Why this exists.** Mid-Year 2026 discovered that all three authoritative artifacts had drifted ~4 weeks behind the working boards *in lockstep* — the "10 banks" was really 8, and 16 theorem IDs were counter-advanced but never sourced. The boards are working memory; the **Ledger, Graph, Registry** are the record of truth. **A count or ID that lives only in board headers and scattered K-audits, never in one reconciled artifact, is UNVERIFIED BY CONSTRUCTION.** This procedure catches drift on cadence, not once a year.

## Step 1 — Run the check (mechanical)

```
SOD_DATE=$(date +%F) python3 play/keeper_sod_artifact_check.py
```

Exit 0 = ALL CURRENT (proceed to the day's work). Exit 1 = DRIFT DETECTED (work Step 2 first).

It verifies, and prints a per-artifact verdict + a `->DIRECTIVE <owner>` line for each drift:

| Check | Invariant | Owner on drift |
|---|---|---|
| Theorem graph currency | graph max tid == `.next_theorem` − 1 | Grace (graph) |
| Registry sourcing | recent theorem IDs have registry content (not stubs) | Lyra (registry) |
| Toy counter | max toy file < `.next_toy`, no collision | Elie (toys) |
| Ledger freshness | latest Master Ledger ≤ 7 days old AND enumerates the count in one place | Grace (ledger) |
| Retirement propagation | no retired reading (mass-45, harmonic-50, two-axis, running-rescue) cited as a live bank | Keeper |
| tid-gaps | historical gaps flagged for retracted-vs-missing confirmation | Lyra (at backfill) |

## Step 2 — Act on each flag (judgment)

- **[DRIFT] / [STALE]** → hand to the named owner as the session's first hygiene task; do NOT certify any count/ID in that artifact's domain until reconciled. The owner reconciles; **Keeper audits the reconciliation** (as with the bank 10→8 and the graph pass).
- **[REVIEW] retirement** → Keeper eyeballs the flagged board lines; confirm none pairs a *retired reading* with a *live bank* (false-bank rot). Clear or escalate. (The script's regex is deliberately loose — a tighter grep excluding `1/45|theta13|N_c²·n_C` disambiguates θ₁₃ from mass-45.)
- **[NOTE] tid-gaps** → not a blocker; confirm retracted-vs-missing during the next registry backfill. Never assume "gap = retracted" without checking.
- **[OK]** → nothing to do.
- **[WARN] ledger single-source count = False** → the count is not enumerated in one place; treat any headline count as *claimed, not verified*, until the ledger itemizes it.

## Step 3 — Certify or direct

- If ALL CURRENT: state "artifacts current as of <date>" in the session open; proceed.
- If DRIFT: the day opens with reconciliation, routed to owners (3-lane: each artifact's owner fixes their own; Keeper audits across). **No count/ID goes to a referee or external doc while its artifact is in drift.**

## Standing rules this enforces

1. **Board-vs-artifact drift is itself an audit signal.** A number that only lives on a board is unverified.
2. **Each artifact's owner reconciles their own** (Grace: ledger+graph; Lyra: registry; Elie: toy-JSON/edges). Keeper audits across, never unilaterally rewrites another owner's artifact.
3. **EOD counterpart:** the last CI to close updates its artifact so the next SOD check passes clean. Drift caught at SOD traces to a missed EOD sync.
4. **Don't claim more than the check verifies** — "every present" means every ID the check confirms present, with gaps flagged, not assumed.

## Integration

Add to the repo Daily Discipline (CLAUDE.md, after the `date` step) — **proposed, pending Casey**:
> **0.5 — Keeper runs the SOD artifact-currency check** (`python3 play/keeper_sod_artifact_check.py`). Drift is directed to owners before other work.

Script: `play/keeper_sod_artifact_check.py`. Extend the `RETIRED` list and `STALE_DAYS` as the program evolves; add artifacts (papers↔PDF currency, data/*.json↔working-paper sync) as new invariants when they earn a place.

— Keeper, Mid-Year 2026-07-02. The named discipline (Keeper #28) now has an executable check that fired on its first run and reproduced the day's drift. Cadence keeps it caught.
