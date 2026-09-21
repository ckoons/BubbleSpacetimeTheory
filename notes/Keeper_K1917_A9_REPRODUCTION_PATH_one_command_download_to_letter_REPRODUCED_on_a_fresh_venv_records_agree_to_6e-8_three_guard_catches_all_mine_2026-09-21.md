# K1917 (09:45 EDT Mon 2026-09-21, clock) — THE STRANGER'S ONE COMMAND EXISTS AND RUNS: `play/reproduce_A9_run1.sh` — Quaia download → A9 run-1 landing letter — REPRODUCED on a fresh environment. Owed since Casey's book decision (09-17); the door's first brick.

## 1. What it does (and the stranger sees each step pass or fail by name)
(0) Builds its own venv (`.venv_a9`, gitignored) and installs numpy/scipy/astropy/healpy — no machine here had healpy; the environment Elie ran in is gone, which is exactly why the script builds its own. (1) Fetches the six Quaia v1.0.0 files from Zenodo record 10403370 (Storey-Fisher et al.) and checks each MD5 against the record's API JSON. (2) Verifies the frozen pre-registration v1.5.2 (`notes/BST_PREREGISTRATION_Part_B_1_FROZEN_v1_5_2_Cal_2026-09-15.md`, sha256 8013d9598d356a0e…) and the Ellis–Baldwin library (`play/r145_eb_lib.py`, b87a8b085780, commit 4ce873ce) by hash before anything computes. (3) Runs the chain as run on 2026-09-15: mask+bins → (v) close (outlier 0.10) → (v) addendum → (vi) dipoles → (vii) landing. (4) Compares every numeric field of the three records to the committed certified ones (git show HEAD) at a relative tolerance of 1e-6, and the letter to K1910/K1911. Quick-start line added to CLAUDE.md.

## 2. The result (final run 09:36–09:44, ~7.7 min compute, 1.4 GB peak RSS)
| record | numeric fields | max relative difference |
|---|---|---|
| .partB_v_closed.json | 242 | 5.7e-08 |
| .partB_v_addendum.json | 128 | 0 |
| .partB_vi_dipoles.json | 1300 | 5.2e-12 |
Letter: **Landing C on both samples; Section 4.4 trigger +7.50 σ_β (G<20.5), +5.02 σ_β (G<20.0)** — as certified. Every printed number of (v), (v addendum), (vi), (vii) identical to the retained 09-15 outputs (diff empty but for peak RSS and the K1911 hatch-print wording). The certified records are restored to their committed bytes; the reproduction's outputs are retained beside them (`play/.out_repro_*.txt`, `play/.out_reproduce_A9_run1_2026-09-21_0936.txt`).

## 3. Three guard catches on the way, all mine, none physics — kept in the script's comments
(a) The G20.5 selection-function MD5 I pinned from a rendered Zenodo page was one hex digit wrong (0a8e… for 0aec…); the API JSON is the source. (b) The pre-registration path glob carried the word DRAFT; the frozen file is FROZEN_v1_5_2. (c) Under nohup's C locale bash parsed `$h…` as a variable; the script is now pure ASCII (and "Section", not the sign). And one bar corrected: byte identity failed a correct run — a different numpy build reproduces to 6e-8; the check is numeric with a printed tolerance. Memory file written.

## 4. What this is not
Not a BST result: no BST input enters the pipeline; it is a pre-registered kinematic-dipole test that landed C. It is the door: a stranger can download, verify, run, and read the same letter we read, in ten minutes, and see every guard by name. The two other one-command reproductions already in CLAUDE.md (`verify_bst.py`, toy 541) are the theory's side; this is the sky's.
— Keeper. K1917. Counter next: **K1918**.
