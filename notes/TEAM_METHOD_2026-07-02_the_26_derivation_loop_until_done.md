Team method — how we work the 26-parameter problem, from now until Casey says done

This replaces ad-hoc banking with one loop, one tool, one source of truth. Read it once; we run it every session until every parameter is terminal and Casey calls done.

**The goal**

Derive all 26 SM free parameters from the substrate {rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137}. Each parameter ends in ONE terminal state:
- **DONE** — match ≤0.1% vs PDG **AND** mechanism forced (target-innocent, GUT-free, Five-Absence clean). Both axes clean.
- **FLOOR** — a pure scale, open by Casey #9 (Higgs vev, ν scale). "Derived to be a free scale" is a finished answer.
- **NEG** — an RG-runner or scheme-dependent quantity, not a fixed constant (α_s, sin²θ_W, m_u, m_c). "It runs, here's why" is a finished answer.

We are done when every row is DONE, FLOOR, or NEG — nothing left in SOLID/MISS/OPEN. **Casey calls done.**

**The tool is the judge — not any CI**

`play/bst_almanac.py` is the single source of truth. Status is COMPUTED from the match, never spoken by a CI:
- `dev ≤ 0.1%` → **DONE** · `dev < 1%` → **SOLID** · `dev ≥ 1%` → **MISS** · no value → **OPEN**

It shows, per parameter: BST value | expected (PDG) | dev% | STATUS | mechanism. Two views, same table (cannot drift): scorecard (did it match) and `--almanac` (how it derives from the substrate → `notes/BST_Almanac.md`).

**Two hard rules, both learned the hard way:**
1. **"Solid/done" is computed, not declared.** No CI certifies its own work as solid. You propose a derivation; the tool adjudicates the match; Keeper adjudicates the mechanism. If you want to know if something's solid, run the script — don't ask a CI. (The down-row was called "rigorously solid" and is a 67% MISS. That never happens again — the tool divides the two numbers.)
2. **Both axes must be clean.** A match is not enough and a mechanism is not enough:
   - **Mechanism without match** = the down-row: GUT-free color-root mechanism, but {3,1/3,1} are GUT-SCALE values, 57–67% off observed. **MISS.** A GUT-scale value, a convention artifact, or a mixed-scale ratio is a MISS even if the mechanism is beautiful.
   - **Match without mechanism** = the tau: 49·71 hits 0.05%, but the product-mechanism isn't forced. **Not DONE.**
   Truly finished today (DONE match + FORCED mechanism): θ_QCD, and arguably PMNS θ₁₃. That is the honest floor we build up from.

**The loop — repeated passes over the list**

Each session:
1. **SOD check first** (`keeper_sod_artifact_check.py`) — artifacts current before any derivation work.
2. **Scorecard run** — see the frontier: what's DONE, SOLID, MISS, OPEN.
3. **Work the frontier nearest-first.** Don't deep-dive one item forever; sweep. When an item's match AND mechanism both lock, update the ONE table in `bst_almanac.py`, re-run — DONE climbs, MISS shrinks, the almanac regenerates itself.
4. **Never re-litigate a terminal item.** A DONE/FLOOR/NEG row is closed unless new physics reopens it. No churn.

Frontier order:
- **Nearest (SOLID → DONE):** Cabibbo (0.22%), V_cb (0.73%), PMNS θ₁₃ (0.15%) — need mechanism-forcing / tighter pin to cross into DONE.
- **The down-row (3 MISS at once):** resolve the K641 scale question — derive to DONE (substrate scale + standard running, no GUT) or terminate as STRUCTURAL and drop the precision claim. Highest leverage: moves 3 rows.
- **Other MISS:** V_ub (11.5%), δ_CKM (2.6%), PMNS θ₁₂ (1.8%), θ₂₃ (8.3%) — mechanism + form work.
- **OPEN (build the derivation):** m_H, m_e, ν masses, δ_PMNS.
- **Confirm terminal:** Higgs vev (FLOOR), the 4 runners/traps (NEG) — verify the reason, mark terminal, stop revisiting.

**Roles**

- **Lyra / Grace / Elie — the derivers.** Propose and build derivations for MISS/OPEN items from the substrate. You do NOT self-certify "solid"; you hand a derivation + its BST value to the table. Grace: geometry/strata. Lyra: rep-theory/determinants. Elie: numeric verification + the checker rigs. Each derivation states its BST value so the tool can score it.
- **Keeper — adjudicator + source-of-truth owner.** Runs SOD + scorecard each session; audits the MECHANISM axis (forced? target-innocent? GUT-free? Five-Absence?); updates the table; holds the count; keeps the almanac current. Nothing carries DONE unless the tool scores it AND Keeper clears the mechanism.
- **Cal — post-landing cold-read.** α tier-call reserved for Casey.

**Disciplines armed (unchanged — they are why the number is trustworthy)**

- **Five-Absence FIRST** — a GUT value/scale is a MISS, not a win (the down-row is the standing example).
- **Target-innocence** (derived vs fit) · **Cal #27** hardest at peak elegance · **structure-forcing, not value-reaching** (137 is form-cheap).
- **Artifact-currency (Keeper #28)** — SOD check first; ledger/graph/registry/almanac reconciled at EOD.
- **[[feedback_pin_conventions_to_primary_sources]]**, **[[feedback_engage_dont_label]]**, **[[feedback_dont_manufacture_walls]]** + **[[feedback_no_fabricated_fatigue]]**.

**Pass 1, item 1 — PDG re-pin (mandatory before scoring anything).** The scorecard's `expected` column is currently from memory. Pin every reference value to PDG 2024 before we trust a single dev%. The reference values cannot be the unverified thing. (Elie owns the pin; Keeper audits.)

**What "done" is.** Not a target count — every row terminal (DONE/FLOOR/NEG). We report the honest live tally each session ("N DONE, M SOLID, K MISS of 26"), never a headline the tool doesn't compute. Casey calls done when the board is all-terminal.

— The method: one list, one tool, computed status, two clean axes, repeated passes, no self-certification, no re-litigation. Today's honest floor: 4 DONE / 4 SOLID / 7 MISS / 6 OPEN / 1 FLOOR / 4 NEG — with only θ_QCD clean on both axes. We build up from there, one forced derivation at a time, until Casey says done.
