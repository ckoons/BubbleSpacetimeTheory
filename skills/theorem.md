Manage theorem T_id allocation. Prevents collisions between CIs.

## Usage

- `/theorem claim` — claim one theorem T_id
- `/theorem claim N` — claim a block of N consecutive T_ids
- `/theorem register TNNN "Name" D0 §sec toy#` — log a completed theorem

Parse the $ARGUMENTS string to determine which operation.

## Operation: claim (default if no arguments or "claim")

1. Read `play/.next_theorem` to get the current number.
2. If claiming 1 (default): your T_id is the value read. Write `value + 1` back to `play/.next_theorem`.
3. If claiming N (e.g., `/theorem claim 3`): your block is `[T_value, T_{value+1}, ..., T_{value+N-1}]`. Write `value + N` back to `play/.next_theorem`.
4. Create a claim file at `play/.claims/theorem_TNNN_<CI_NAME>.claim` (create the `.claims/` directory if it doesn't exist). The claim file contains:
   ```
   Claimed by: <your CI name or "unknown">
   Date: <today YYYY-MM-DD>
   T_ids: TNNN (or TNNN-TMMM for blocks)
   Status: claimed
   ```
5. Report the claimed T_id(s) to the user.

**CRITICAL**: Read `.next_theorem`, compute the new value, and write it back in one operation. Do NOT write a theorem without calling this skill first.

## Operation: register

Parse: `/theorem register TNNN "Name" D0 §sec toy#`
- TNNN = theorem ID (e.g., T479)
- "Name" = short theorem name in quotes
- D0/D1/D2 = AC(0) depth
- §sec = document section reference (e.g., §163)
- toy# = associated toy number (e.g., 557)

All fields after TNNN are optional but encouraged.

1. Confirm the T_id was previously claimed (check `play/.claims/theorem_TNNN_*.claim`). Warn if no claim file found.
2. Update the claim file: set Status to `registered`, add the name and details.
3. Append a line to `play/THEOREM_LOG.md` (create if missing):
   ```
   | TNNN | Name | Depth | §ref | Toy | CI | Date | Status |
   ```
   with header if file is new:
   ```
   # Theorem Registration Log
   | T_id | Name | Depth | §ref | Toy | CI | Date | Status |
   |------|------|-------|------|-----|-----|------|--------|
   ```
4. Report success. Remind the user that the theorem also needs to be added to `notes/BST_AC_Theorem_Registry.md` (the master registry) — this skill logs locally but does NOT modify the master registry, which Keeper manages.

## Rules

- **Never write a theorem without calling `/theorem claim` first.** This is the law.
- Claim files are permanent records. Don't delete them.
- If `.next_theorem` doesn't exist, STOP and alert Casey.
- Known gaps: T43-T46, T63 are unassigned. Leave them alone. They are historical gaps.
- T_ids are permanent and monotonic. Never reuse. Never fill gaps.
- The master registry (`notes/BST_AC_Theorem_Registry.md`) is Keeper's domain. This skill creates local logs; Keeper batch-updates the master registry.
