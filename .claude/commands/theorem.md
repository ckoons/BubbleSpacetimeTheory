Manage theorem T_id allocation. Prevents collisions between CIs.

## Usage

- `/theorem claim` — claim one theorem T_id
- `/theorem claim N` — claim a block of N consecutive T_ids
- `/theorem register TNNN "Name" D0 Section sec toy#` — log a completed theorem

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

Parse: `/theorem register TNNN "Name" D0 Section sec toy#`
- TNNN = theorem ID (e.g., T479)
- "Name" = short theorem name in quotes
- D0/D1/D2 = AC(0) depth
- Section sec = document section reference (e.g., Section 163)
- toy# = associated toy number (e.g., 557)

All fields after TNNN are optional but encouraged.

1. Confirm the T_id was previously claimed (check `play/.claims/theorem_TNNN_*.claim`). Warn if no claim file found.
2. Update the claim file: set Status to `registered`, add the name and details.
3. Append a line to `play/THEOREM_LOG.md` (create if missing):
   ```
   | TNNN | Name | Depth | Section ref | Toy | CI | Date | Status |
   ```
   with header if file is new:
   ```
   # Theorem Registration Log
   | T_id | Name | Depth | Section ref | Toy | CI | Date | Status |
   |------|------|-------|------|-----|-----|------|--------|
   ```
4. **Update the graph databank** (`play/ac_graph_data.json`):
   - Load the JSON file
   - Add a new theorem record to the `theorems` array:
     ```json
     {
       "tid": <integer>,
       "name": "<Name>",
       "domain": "<best domain match from DOMAINS list>",
       "status": "proved",
       "depth": <0, 1, or 2>,
       "conflation": 0,
       "section": "Section sec",
       "toys": [<toy#>],
       "date": "<today YYYY-MM-DD>",
       "plain": "<one-line description>",
       "proofs": []
     }
     ```
   - If the theorem depends on other theorems, add edges to the `edges` array:
     ```json
     {"from": <dep_tid_int>, "to": <new_tid_int>}
     ```
   - Update `meta.theorem_count` and `meta.edge_count`
   - Save the file
5. Report success. Remind the user that the theorem also needs to be added to `notes/BST_AC_Theorem_Registry.md` (the master registry) — this skill logs locally and updates the graph databank, but does NOT modify the master registry, which Keeper manages.

## Graph Databank Domains

Use these domain keys when registering (pick the best match):
`info_theory`, `topology`, `graph_theory`, `proof_complexity`, `coding_theory`, `probability`, `algebra`, `thermodynamics`, `analysis`, `foundations`, `circuit_complexity`, `four_color`, `differential_geometry`, `quantum`, `chemistry`, `bst_physics`, `classical_mech`, `optics`, `electromagnetism`, `relativity`, `condensed_matter`, `qft`, `nuclear`, `number_theory`, `fluids`, `computation`, `signal`, `biology`, `cosmology`, `observer_theory`, `intelligence`, `linearization`, `interstasis`, `ci_persistence`

## Rules

- **Never write a theorem without calling `/theorem claim` first.** This is the law.
- Claim files are permanent records. Don't delete them.
- If `.next_theorem` doesn't exist, STOP and alert Casey.
- Known gaps: T43-T46, T63 are unassigned. Leave them alone. They are historical gaps.
- T_ids are permanent and monotonic. Never reuse. Never fill gaps.
- The master registry (`notes/BST_AC_Theorem_Registry.md`) is Keeper's domain. This skill creates local logs and updates the graph databank; Keeper batch-updates the master registry.
- The graph databank (`play/ac_graph_data.json`) is the machine-readable index. Query it with `python3 play/toy_564_ac_theorem_engine.py`.
