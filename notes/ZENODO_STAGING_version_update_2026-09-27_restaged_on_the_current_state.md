# ZENODO VERSION UPDATE — RE-STAGED 2026-09-27 on the current state (supersedes the 08-27 staging)
**Keeper, on Casey's word 09-27 ("today before EOD"). DOI lineage 10.5281/zenodo.19454185 (v1, 2026-04-07, CC BY 4.0).**

**Gate:** nothing is uploaded until Cal's cold read of Parts A and B (the front page and the description), then Casey's hand. The 08-27 staging (`notes/ZENODO_STAGING_version_update_2026-09_prepared_2026-08-27.md`, `zenodo_v2_staging/`) is a month stale. It predates the state block's generated count, the Curriculum spine, A9 run 1, A2's firing and the three walls. **It is not to be uploaded as it stands.**

## Part A — Front-page currency pass (PROPOSED; applied only after Cal's cold read)
The state block (`notes/BST_PRESENTATION_STATE_BLOCK.md`, synced to four consumers) is the one-page front. Three proposed edits, each dated:
1. **"Fired and lost"** gains its two newest certified rows (register v0.33, Section E, quoted there):
   > · E7, g_A = 4/π — 5.7σ from PERKEO III alone, ≥ 6σ with the bottle lifetime on every |V_ud| route (Cal Section 984; certified 2026-09-27) · E8, "19 appears only in coloured quantities" — falsified as stated by Ω_Λ = 13/19, a colourless 19 already on file (Cal Section 990).
2. **A new paragraph after "The boundary — the open half":**
   > **What the geometry forces, and what it does not** (stated 2026-09-26; register Section D; K1929–K1932, Cal Sections 993–1000). D_IV⁵ forces the kinematics — the spectra, the two-body channels with their multiplicities and selection rules, the discreteness of the interior clock — and none of the dynamics: every Minkowski mass is the ruler times a number, the couplings are identified, and at the level of the geometry the boundary's two-body spectrum is that of a free field. The channel list is forced with no free parameters; any interaction must live inside it. Hydrogen's shell structure appears one dimension down, as the minimal representation of D_IV⁴ — recapitulated, not contained.
   - **Guard (K1921):** no pre-registered direction. The fourth wall (no massless 4D representation of any helicity from the descent) was **ruled 09-27, not yet cold-read for the front page**, so it stays off today *(Cal Section 1003 A-2)*.
3. **"Live and pre-registered"** gains one pointer sentence after A9:
   > The register's Section A lists every live falsifier (A1–A14). A13's dark-matter ratio 16/3 sits at its threshold (3.0σ on ACT DR6 + DESI DR2 at the published compression correlation; the chain's own correlation is unpublished). A2 has fired on the K_μ2 route (above); FLAG 2027 decides.
   *(Cal Section 1003 A-1 applied 2026-09-27: a fired row is not "at threshold", and the 3.7σ end came from a DR1 chain, which is not evidence.)*
4. Header: "Last accuracy-synced: 2026-09-27 …" naming these edits.

**Also proposed (root pointers):** CLAUDE.md lines 49 and 60, and README lines 530/619/624, send humans to `OneGeometry.md`, which **does not exist** (removed in the July volume reorganization; only an old `notes/OneGeometry.pdf` remains, and README:36 itself says the 2022 framing needed correction). Proposed human front door: `data/bst_this_is.md` (one page, "what BST is and is not") → `Curriculum/Spine_DIV5_QM_GR_SM/INDEX.md` (the derived core, ten lectures) → `Guide/INDEX.md`. Casey's CLAUDE.md, so his word, but the fix is mechanical.

## Part B — Version description (DRAFT; Casey edits freely; Cal cold-reads)
> **Bubble Spacetime Theory — September 2026 update: the audited state, with its losses and its walls.**
> This version replaces the April snapshot with the program's audited state as of 27 September 2026. The reading order starts at a one-page state of the program that says, in one place, what is derived, what is identified, what is closed by a theorem, what fired and lost, and what would falsify the framework. **On the Standard Model's 26 primary parameters, the count — generated from the register, never typed — is 5 derived (each with its mechanism proved and its inputs named), 12 identified, 7 open, 2 input; one of the five, the Cabibbo angle λ = 1/√20, has since fired on the kaon-decay route (FLAG 2027 decides). α is identified, not derived, and we do not claim zero free parameters.**
> New since April:
> (1) a ten-lecture derived core (quantum mechanics on the Hardy space of D_IV⁵, time as the K-centre clock, the gauge skeleton and one generation, three generations at a floor, the mixing sector's order), written from the register;
> (2) a falsifier register with a certified fired-and-lost section — eight rows, including a Bell-inequality ceiling refuted by an experiment published a decade before it was registered, and the axial coupling g_A = 4/π at 5.7σ — reported with the same ceremony as wins;
> (3) the program's first sky test, pre-registered and frozen by hash before any data were read (one boost, not two, on the Quaia quasar catalogue), which landed "not decidable" by its own pre-target checks, and a one-command script that reproduces it from download to letter;
> (4) a statement of the program's limits: the geometry forces the kinematics — spectra, channels, multiplicities, selection rules — and none of the dynamics; masses are the ruler times a number, couplings are identified, and processes are free at the geometric level.
> The headline numbers are reproducible: `python3 play/verify_bst.py` checks about fifty of them against measurement and prints the register's status (FIRED or RETIRED) in place of a pass wherever a claim has fired or been retired; `play/reproduce_A9_run1.sh` reproduces the sky test from download to letter. Where a narrative document and the falsifier register disagree, the register wins.

## Part C — Reading-order manifest (all from the current tree; PDFs rebuilt at staging)
1. `notes/BST_PRESENTATION_STATE_BLOCK.md` (after Part A) → **00_State_of_the_Program.pdf** (it replaces the 08-26 one-page, which predates the generated count)
2. `data/bst_this_is.md` → 01_What_BST_Is_and_Is_Not.pdf
3. `Curriculum/Spine_DIV5_QM_GR_SM/INDEX.md` + Lectures 01–10 → 02_Derived_Core_INDEX.pdf … 12_Lecture_10.pdf (PDFs exist; verify currency)
4. `notes/Elie_FALSIFIER_REGISTER_v0_2_…_2026-08-24.md` (header v0.33) → 13_Falsifier_Register.pdf
5. `notes/BST_Tier_System_Readers_Guide_v0_1_Keeper_2026-08-24.md` → 14_How_to_Read_a_BST_Claim.pdf (**check it against the four-word standard used since 09-14 before inclusion**)
6. `notes/BST_Forcing_and_Evidence_FLAGSHIP_v1_0_…` → 15_Forcing_and_Evidence.pdf (**currency check owed: written 08-23, before A9, A2's firing and the walls; include with a dated head, or omit**)
7. Reproduction: `play/verify_bst.py`, `play/reproduce_A9_run1.sh` (in the repository snapshot; named in the description). **`play/toy_541_five_integers_to_everything.py` RESTORED 09-27 after Elie's fix (2e13ce7f: g_A marked E7 FIRED, excluded from the count, 50 quantities, 'FREE PARAMETERS: 0' box fixed). It had been REMOVED earlier that day:** it presents g_A = 4/π (E7 FIRED) as a match and counts it among "derived quantities" (Level 2). Elie fixes it; it returns after the fix.

## Part D — Today's steps
1. **Cal:** cold read of Parts A and B (the front page and the words the world will read).
2. **Keeper:** apply Part A on Cal's pass; sync the four consumers; run the SOD checker; build `zenodo_2026-09_staging/` from Part C; verify every PDF is newer than its source.
3. **Casey:** edit Part B in his voice; repo snapshot per the April procedure → Zenodo "new version" on the existing lineage → paste Part B → upload the staged PDFs → publish.

## Part E — Staging folder BUILT (11:24 EDT): `zenodo_2026-09_staging/`
01–13 are built from the current tree, and every PDF was checked newer than its source. The register PDF was rebuilt today, with the prime character (′) swapped for an apostrophe in a temporary copy because the shared header maps ′ into math mode, which fails inside table cells. **00_State_of_the_Program.pdf waits on Cal's cold read of Part A.** Part C items 5 and 6 (the tier guide, Forcing & Evidence) and the 08-26 one-page state are **omitted**: they have not been currency-checked since August, and Lecture 10 plus the register cover the method. Include them later only after a check.

## Part F — Cal Section 1003 applied (11:28 EDT, Keeper)
- **B1 (blocker):** `play/verify_bst.py` now prints the register status on four rows and excludes them from the tally: Cabibbo 2/√79 **RETIRED**; |V_us| = 1/√20 and |V_ud| = √(19/20) **FIRED(A2)**; g_A = 4/π **FIRED(E7)**. **|V_ud| is Keeper's addition:** it is A2's other face, and Cal listed three rows. Output: 45/46 at < 1 %, with 4 excluded.
  - The SOD "fired" rule now also runs the script and fails on any fired or retired row printing PASS, EXACT or WARN. The negative control fires on all 4 rows of the pre-fix script.
- **B2:** "one of the five, the Cabibbo angle λ = 1/√20, has since fired on the kaon-decay route (FLAG 2027 decides)" is added after the count.
- **B3:** "Every quantitative claim is reproducible" → "The headline numbers are reproducible", naming what each script covers.
- **A-1:** the threshold sentence is split (16/3 at 3.0σ on DR2 at the published correlation; A2 fired). **A-2:** the guard now reads "ruled 09-27, not yet cold-read for the front page".
- **Gate:** @Cal re-reads only the changed lines. On PASS, Keeper applies Part A to the state block, syncs, builds 00, and hands Casey Part B.

## Part G — READY FOR CASEY (12:13 EDT)
- **Cal Section 1007: PASS** on the changed lines (verify_bst's fired and retired rows verified by run; B2, B3, A-1, A-2 applied).
- **Part A applied** to the state block and synced to its four consumers (`sync_presentation_state.py --check` exit 0). The consumer PDFs are rebuilt.
- **`zenodo_2026-09_staging/` is complete, 00–13:** 00 is the state page after Part A; 02 is rebuilt from the synced Spine INDEX.
- Casey's steps: edit Part B in your own voice (Cal re-reads only what you change, if you change a claim); snapshot the repo per the April procedure; open a Zenodo "new version" on DOI lineage 10.5281/zenodo.19454185; paste Part B; upload 00–13; publish.
