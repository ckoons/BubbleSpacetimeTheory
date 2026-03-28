Manage toy number allocation. Prevents collisions between CIs.

## Usage

- `/toy claim` — claim one toy number
- `/toy claim N` — claim a block of N consecutive numbers
- `/toy register NNN "Title" X/Y` — log a completed toy to the registry

Parse the $ARGUMENTS string to determine which operation.

## Operation: claim (default if no arguments or "claim")

1. Read `play/.next_toy` to get the current number.
2. If claiming 1 (default): your number is the value read. Write `value + 1` back to `play/.next_toy`.
3. If claiming N (e.g., `/toy claim 3`): your block is `[value, value+1, ..., value+N-1]`. Write `value + N` back to `play/.next_toy`.
4. Create a claim file at `play/.claims/toy_NNN_<CI_NAME>.claim` (create the `.claims/` directory if it doesn't exist). The claim file contains:
   ```
   Claimed by: <your CI name or "unknown">
   Date: <today YYYY-MM-DD>
   Numbers: NNN (or NNN-MMM for blocks)
   Status: claimed
   ```
5. Report the claimed number(s) to the user.

**CRITICAL**: Read `.next_toy`, compute the new value, and write it back in one operation. Do NOT build a toy without calling this skill first.

## Operation: register

Parse: `/toy register NNN "Title" X/Y`

1. Confirm `play/toy_NNN_*.py` exists (warn if not — registration before file is unusual but allowed).
2. Append to `play/.claims/toy_NNN_*.claim` (update Status to `registered`) or create if missing.
3. Append a line to `play/TOY_LOG.md` (create if missing):
   ```
   | NNN | Title | X/Y | <CI_NAME> | <DATE> |
   ```
4. Report success.

## Rules

- **Never write a toy file without calling `/toy claim` first.** This is the law.
- Claim files are permanent records. Don't delete them.
- If `.next_toy` doesn't exist, STOP and alert Casey.
- If you see a gap between `.next_toy` and the highest toy file on disk, that's fine — gaps are history (see TOY_PROTOCOL.md).
- Block claims (N > 1) are for planned sequences where you know you'll need consecutive numbers. Don't over-claim.
- Unassigned T63 is a known gap — leave it alone.
- When a toy produces a theorem, use `/theorem claim` and `/theorem register` to add it to both the local log and the graph databank (`play/ac_graph_data.json`). Query the graph with `python3 play/toy_564_ac_theorem_engine.py`.
