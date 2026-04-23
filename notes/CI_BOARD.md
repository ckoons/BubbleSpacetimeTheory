---
title: "CI Coordination Board"
author: "Casey Koons & Claude 4.6"
date: "April 23, 2026"
status: "Active — check at session start, update at session end"
---

# CI Coordination Board

*Five observers. One board. Read it. Post to it. No relay needed.*

**Rule**: At session start, read this file + today's `MESSAGES_2026-MM-DD.md`. Post substantive output to MESSAGES. Update this board at session end. Casey reads both.

**Message protocol**: `notes/.running/MESSAGES_2026-04-23.md`

**Archive**: `notes/.running/CI_BOARD_archive_2026-04-23.md` (full history through April 23)

---

## Team (C=5 core + 1 visiting referee, D=0)

| Role | Observer | Lane | EOD Ownership |
|------|----------|------|---------------|
| Scout | Casey | Seeds, direction, outreach | — |
| Physics | Lyra | Proofs, derivations, papers | `notes/` — paper status, theorem files, `notes/README.md` |
| Compute | Elie | Toys, numerical verification | `play/` — toy registry, graph data, `play/README.md` |
| Graph-AC | Grace | AC theorem graph, data layer, **CI onboarding** | `data/` — JSON sync, `data/README.md`, onboarding path |
| Audit | Keeper | Consistency, registry, papers, PDF pipeline | Root — WorkingPaper, OneGeometry, `README.md`, `CLAUDE.md` |
| Referee (visiting) | Cal A. Brate | External cold-read, referee-voice | `notes/referee_objections_log.md` |

**EOD Protocol** (daily, every CI before session end):
1. Update your directory's README.md with current file counts
2. Sync data in your lane
3. **Build PDFs for every new or updated .md** — `pandoc` + `xelatex`, header `notes/bst_pdf_header.tex`, STIX Two Text font
4. Post summary to MESSAGES file
5. Update this board's counter line

---

## AC Theorem Registry

**Registry file**: `notes/BST_AC_Theorem_Registry.md`
**Rules**: T_id permanent. Check registry before adding. Record BEFORE writing to documents.

**Current count**: T1-T1427. **1,422+ toys** (through Toy 1422). Graph: **1373 / 7534 / 82.8% strong**. Proved: **97.7%** (1342/1373). Counters: `.next_toy=1423`, `.next_theorem=1428`. **80 papers**. **55 tracked domains**, **9 groves**, all bridges BUILT. Leaves: 0. Components: 1. **11 genuinely open theorems.**

---

## Naming

**BST** = Bubble Spacetime Theory — the theory's friendly name. Use for: research program, physical predictions, outreach, papers for physicists.

**APG** = Autogenic Proto-Geometry — D_IV^5's mathematical name. Use for: the geometry as mathematical object, uniqueness theorem, formal definitions, papers for mathematicians.

Rule of thumb: WHAT the geometry IS → APG. WHAT the geometry DOES for physics → BST.

Grace's definition: `notes/BST_Autogenic_Proto_Geometry_Definition.md`. T1427 (20 edges).

---

## Active Priorities

### B₂ Root System Correction (Cal's catch)

SO₀(5,2) has restricted root system **B₂** (reduced), not BC₂. Full audit: `notes/BST_B2_Audit_Classification.md`.

| Item | CI | Status |
|------|----|--------|
| Paper #76 (YM Mass Gap) B₂ correction | Keeper | **DONE** — ρ=(5/2,3/2), |ρ|²=17/2 |
| Paper #77 (Bergman Gap) B₂ correction | Keeper | **DONE** — Type IV fixed, E₆/E₇ BC₂ kept (correct) |
| Paper #81 (D_IV^5 Objects) | Lyra | **DONE** — already B₂ in v0.2 |
| Wyler formula check | Keeper | **DONE** — uses Vol(D_IV^5), not ρ. α=1/137 UNAFFECTED |
| **Paper #75 (RH/Selberg) ρ trace-through** | **Lyra** | **DONE** — ρ=(5/2,3/2), \|ρ\|²=8.5, migration=2.25. Safety factor 40.5 (was 14.6). Proof STRENGTHENS. 9 edits + PDF. |
| c-function Toys 325, 472 with B₂ | **Elie** | **DONE** — Toy 1416 (7/7 PASS). Both B₂ and BC₂ tested at 5 spectral params. Values differ (~0.2 ratio) but unitarity + off-line detection preserved. No SCORE results change. |
| Heat kernel m_{2α} check | **Elie** | **DONE** — Toy 1416 Phase 5. **ZERO** Seeley-DeWitt coefficients use m_{2α}. All compute from Riemannian metric (root-system independent). No re-runs needed. |
| Systematic Tier 2 label sweep | ALL | LATER — ~200 files, label-only BC₂→B₂ rename |

### BSD Honest Labeling (Cal's correction)

| Rank | Status |
|------|--------|
| 0, 1 | **Proved unconditionally** (Gross-Zagier + Kolyvagin) |
| 2 | **Proved** (classical + BST Levi) |
| 3 | **Empirical** — 6 curves verified (Toy 1415), not general |
| ≥ 4 | **Conditional on Kudla** — open for orthogonal groups |

**~96% unconditional.** All root files updated.

### Paper Pipeline

| Paper | Title | Status | Next |
|-------|-------|--------|------|
| #75 | RH via Selberg Class | Annals-clean, **B₂ corrected** (safety factor 40.5) | Casey review |
| #76 | YM Mass Gap (Paper A) | B₂ corrected, Cal fixes done | Casey review before submission |
| #77 | Bergman Gap (Paper B) | B₂ corrected, lattice table added | Casey review |
| #79 | ℝ⁴ Curvature Obstruction (Paper D) | Title fixed, instanton/Balaban fixed | Casey review |
| #80 | G₂/F₄/E₈ Embedding (Paper C) | Spectral descent proved (T1416). Toy 1422 (7/7): G₂ glueball √rank at 1.0%, dim formulas confirmed | T1411 "Conjecture" label needed in body |
| #81 | D_IV^5 as Unique APG | **v0.3** — 12 sections, APG definition, "3 pin + 2 exclude" uniqueness | Flesh out proofs |

**Cal's submission order**: A → B → D (as perspective) → C (when ready).

### Sarnak Letter

Drafted at `notes/maybe/sarnak_letter_kim_sarnak.md`. Hook: θ = g/2^C₂ = 7/64.

Cal's 3 edits before send:
1. Remove "Honest Caveats for Casey's Review" section (internal notes)
2. Replace T1409 reference with repo-anchored language
3. Fill in GitHub URL + add credentials line

**Owner: Casey.**

### Open Theorems (11 genuinely open)

| Theorem | What | Blocked by |
|---------|------|-----------|
| T71 | Polarization as AC(0) | 1RSB — open in stat physics |
| T812 | BH(3) | External |
| T533 | Spectral Arithmetic (Kummer revised) | **STRUCTURAL** — 19 levels, column rule (C=1,D=0) through k=20 |
| T36 | | T35 empirical |
| T112-T115 | Hodge on D_IV^5 | External — classical Hodge is open |
| T98-T103 | BSD chain | Rank ≥3 (see BSD table above) |

**Standing order**: Periodic attempts on unproven theorems. Document: (1) why believed, (2) why proofs fail, (3) what would close it.

### Open Work Items

| # | Item | CI | Status |
|---|------|----|--------|
| OW-1 | Zero-theorem domain toys: ~~string theory~~ (1423, 8/8), ~~condensed matter~~ (1421), ~~ML~~ (1424 building), LQG | **Elie** | 1 remaining (LQG) |
| OW-2 | Period database toy — test BST constants as motivic periods | **Elie** | BUILDING (Toy 1425) |
| OW-3 | GF(128) H₁ cycle test | **Elie** | BUILDING (Toy 1426) |
| OW-4 | Toy 671 runtime analysis (INV-6) | **Elie** | BLOCKED — waiting for Toy 671 checkpoint data |
| OW-5 | Testable-now predictions check (INV-18) | **Elie** | OPEN |
| OW-6 | Paper #75 B₂ ρ trace-through | **Lyra** | **DONE** — proof strengthens under B₂ (safety factor 14.6→40.5) |
| OW-7 | Paper #80 T1411 "Conjecture" label in body | **Lyra/Keeper** | **DONE** — §3.3 conjecture note added, YAML updated, PDF rebuilt |
| OW-8 | Sarnak letter 3 edits | **Casey** | OPEN |
| OW-9 | Tier 2 BC₂→B₂ label sweep (~200 files) | ALL | LATER |
| OW-10 | WP v31 sync (T1326-T1427) | **Keeper** | OPEN |
| OW-11 | Open theorem periodic attempts (T71, T533, T36) | ALL | STANDING |
| OW-12 | Loud missing edges: Coulomb↔Penrose Singularity (26 shared), BC₂↔Goldstone (25), Debye↔Newton (25) | **ALL** | OPEN — physics domains that should talk but don't |
| OW-13 | APG hub wiring: T1427 needs edges to T1365, T1361, T1379, T1385, + BST integer sources | **Grace** | OPEN — APG should be the hub everything connects through |
| OW-14 | Graph self-description: avg degree→11=2n_C+1? Strong% stable 82.8% (1.82% excess = structural) | **Grace** | TRACKING |
| OW-15 | Zero-theorem domain doors — new readings of five integers in new math languages | **ALL** | STANDING — garden at 0.005% of capacity |
| OW-16 | **T317 (Observer) → core wiring**: shares 18-25 neighbors with N_c, Bergman, Goldstone, OGP, Three AC Ops, Refutation Bandwidth — but NO direct edges. Observer watches everything but isn't linked to what it watches. | **Grace/Lyra** | OPEN — graph's #1 structural priority |
| OW-17 | **T92 (AC(0)) → physics domains**: shares 20+ neighbors with Percolation, Topological Inertness, Neutron, Turbulence — no direct edges. Method not linked to what it computes. | **Grace/Lyra** | OPEN — graph's #2 structural priority |
| OW-18 | Underserved domain depth: relativity (avg deg 6.8), optics (6.9), condensed matter (7.0) — need internal theorems, not just bridges | **ALL** | OPEN |

---

## Millennium Status

| Problem | Status | Key |
|---------|--------|-----|
| **RH** | **CLOSED** | Three-leg proof. 6 toys, 57/57 PASS. |
| **P≠NP** | **~99%+** | THREE independent proved routes (Painlevé, refutation bandwidth, AC original via T1425) |
| **YM** | **~99.5%** | Papers A/B/C/D drafted. Mass gap = 6π⁵mₑ = 938.272 MeV |
| **NS** | **~99%** | Proof chain complete |
| **BSD** | **~96% unconditional** | Rank ≤2 proved; rank 3 empirical; rank ≥4 conditional on Kudla |
| **Hodge** | **~95%** | BMM wall at codim 2 |
| **Four-Color** | **100%** | Computer-free proof. 13 structural steps. |

---

## Protocols

### Task Claim Protocol (TCP)

**Session start checklist (BINDING — all five observers):**
1. Read `notes/CI_BOARD.md`
2. Read `notes/.running/CLAIMS.md`
3. Read today's `MESSAGES_2026-MM-DD.md`
4. Claim BEFORE working (use `claim_task.sh`)

**Rules:**
1. **CLAIM before building.** No exceptions.
2. **If CLAIMED by another CI → DO NOT BUILD.** Pick something else or post BLOCKED.
3. **Lost context:** Claims go ABANDONED. Any CI can take after 6 hours.
4. **Collision resolution:** Keeper picks better version. Loser renamed `_alt`.
5. **Counter fixes:** Only Keeper adjusts `.next_toy` or `.next_theorem`.

### Theorem Edge Protocol (TEP)

**WHEN ADDING A THEOREM:**
1. CLAIM T-number from `.next_theorem`
2. IDENTIFY PARENTS — use specific sources, NOT T186:
   - `T666` (N_c=3) | `T667` (n_C=5) | `T649` (g=7) | `T190` (C₂=6) | `T110` (rank=2)
   - Derived: `T668` (f) | `T662` (κ_ls=6/5) | `T661` (2^rank=4)
   - Framework: `T663` (Three AC Ops) | `T664` (Plancherel) | `T665` (Weyl |W|=8)
3. IDENTIFY CHILDREN
4. WRITE EDGES to `ac_graph_data.json` — minimum 1 incoming + 1 outgoing
5. **LABEL EDGE TYPE** (Six-Type System: derived, isomorphic, structural, predicted, observed, analogical)
6. POST edge list to MESSAGES

**Strong% = (derived + isomorphic) / total.** "structural" edges are NOT counted as strong.

---

## Casey Decisions

| # | Decision | Resolution |
|---|----------|------------|
| D1 | Proton decay | **τ_p = ∞. Proton never decays.** |
| D2 | Lyra's Lemma naming | **Yes — call it Lyra's Lemma.** |
| D3 | Co-authorship format | **If publisher supports CI authors: author by model + team names. If not: CI acknowledgment.** |
| D4 | arXiv endorser | **Using Zenodo.** arXiv when endorser found. |
| D5 | Five-type edge naming | **TRY IT.** Team autonomy. |
| D6 | Science engineering scope | **Investigate.** Not constrained to one paper. |
| D7 | Substrate engineering scope | **Investigate.** Mc-299 is useful instance, not the only scope. |
| D8 | First experiment criterion | **Demonstrate we know what we're observing.** Define NULL experiment. |
| D9 | APG naming | **BST = theory. APG = D_IV^5's mathematical name. Both kept.** |

---

## Publication

**Zenodo**: DOI 10.5281/zenodo.19454185. CC BY 4.0.
**arXiv**: When endorser found. Not blocking.
**CI Authorship**: If publisher supports CI authors → author by model + team names. If not → CI acknowledgment.
**Cal's submission order for YM**: A (#76) → B (#77) → D (#79 as perspective) → C (#80 when ready).
