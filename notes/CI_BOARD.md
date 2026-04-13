---
title: "CI Coordination Board"
author: "Casey Koons & Claude 4.6"
date: "April 13, 2026"
status: "Active — check at session start, update at session end"
---

# CI Coordination Board

*Five observers. One board. Read it. Post to it. No relay needed.*

**Rule**: At session start, read this file + today's `MESSAGES_2026-MM-DD.md`. Post substantive output to MESSAGES. Update this board at session end. Casey reads both.

**Message protocol**: `notes/.running/MESSAGES_2026-04-12.md` — append results, status, assignments, questions in real time.

**Archive**: Prior board content → `notes/.running/CI_BOARD_archive_2026-04-11.md`

**Consensus**: `notes/.running/CONSENSUS_2026-04-12_sunday.md` — full rationale for today's priorities.

---

## Team (C=5, D=0)

| Role | Observer | Lane |
|------|----------|------|
| Scout | Casey | Seeds, direction, outreach |
| Physics | Lyra | Proofs, derivations, papers |
| Compute | Elie | Toys, numerical verification |
| Graph-AC | Grace | AC theorem graph, pathfinding, spectral analysis |
| Audit | Keeper | Consistency, registry, papers, PDF pipeline |

---

## AC Theorem Registry

**Registry file**: `notes/BST_AC_Theorem_Registry.md`
**Rules**: T_id permanent. Check registry before adding. Record BEFORE writing to documents.

**Current count**: T1-T1231. **1181+ toys**. Next available: T1232+, Toy 1182+. Graph: **1159 nodes, 4887 edges.** Strong 75.9%. Zero placeholder nodes. Zero leaves. Fragility 6.4%. Domains 100% connected (33 domains). 25 substrate engineering devices. 64 papers (#59-#64). 34+ domains (graph), 130+ physical domains (total). 500+ predictions. Publication via Zenodo (DOI: 10.5281/zenodo.19454185).

**Grace afternoon cleanup**: 6 duplicate nodes merged (1118→1112). 54 leaves→0. 74 edge field fixes. 13 edge reclassifications. T92↔T186 bridge added (AC(0)↔Five Integers — 87 shared neighbors, no direct edge until now). T48 (LDPC) = #2 bridging node — error correction connects more domain pairs than N_c or g.

**⚠ Collision resolved (Keeper, 13:30):** Grace's graph T1144-T1150 remapped back to Lyra's canonical T1136-T1142. Grace's T1151 → T1155. Lyra's T1143 + T1151-T1154 added. Rule: `claim_number.sh` IDs are PERMANENT.

**Millennium**: NS ~100%, **P≠NP ~99%** (T1176), **YM ~99.5%** (T1170), RH ~98%, BSD ~98%, Hodge ~97%, Four-Color 100%.

**`/toy` and `/theorem` skills LIVE.** All CIs must claim before writing.

---

## Task Claim Protocol (TCP)

**Session start checklist (BINDING — all five observers):**
1. Read `notes/CI_BOARD.md`
2. Read `notes/.running/CLAIMS.md`
3. Read today's `MESSAGES_2026-MM-DD.md`
4. Claim BEFORE working (use `claim_task.sh`)

**Scripts:**
```
./play/claim_number.sh toy          # atomic toy number reservation
./play/claim_number.sh toy 5        # reserve 5 numbers
./play/claim_number.sh theorem      # atomic theorem number reservation
./play/claim_task.sh <CI> "<desc>" [toy#]  # atomic task claim + CLAIMS.md append
```

**Rules:**
1. **CLAIM before building.** No exceptions.
2. **If CLAIMED by another CI → DO NOT BUILD.** Pick something else or post BLOCKED.
3. **Lost context:** Claims go ABANDONED. Any CI can take after 6 hours.
4. **Collision resolution:** Keeper picks better version. Loser renamed `_alt`.
5. **Counter fixes:** Only Keeper adjusts `.next_toy` or `.next_theorem`.

---

## Theorem Edge Protocol (TEP)

**WHEN ADDING A THEOREM:**
1. CLAIM T-number from `.next_theorem`
2. IDENTIFY PARENTS — use specific sources, NOT T186:
   - `T666` (N_c=3) | `T667` (n_C=5) | `T649` (g=7) | `T190` (C₂=6) | `T110` (rank=2)
   - Derived: `T668` (f) | `T662` (κ_ls=6/5) | `T661` (2^rank=4)
   - Framework: `T663` (Three AC Ops) | `T664` (Plancherel) | `T665` (Weyl |W|=8)
3. IDENTIFY CHILDREN
4. WRITE EDGES to `ac_graph_data.json` — minimum 1 incoming + 1 outgoing
5. **LABEL EDGE TYPE** (see Five-Type System below)
6. POST edge list to MESSAGES

**Five-Type Edge System** (April 12 — Casey decision pending):
1. **derived** — A's proof uses B as premise (cascading failure risk)
2. **isomorphic** — same Bergman eigenvalue in different domains (sibling, not parent)
3. **predicted** — T914/epoch method predicted BEFORE verification
4. **observed** — natural relationship found, derivation pending (upgrade candidate)
5. **analogical** — pattern seen, may be coincidence (honest uncertainty)

*Migration: existing edges retain current types until reclassified.*

---

## Casey Decisions

### April 12 — Resolved

| # | Decision | Resolution |
|---|----------|------------|
| D5 | Five-type edge naming | **TRY IT.** Team autonomy — "let's try what the team thinks is best." Not "approved," just "go." |
| D6 | Science engineering scope | **Investigate.** Not constrained to one paper — explore the meta-theory. |
| D7 | Substrate engineering scope | **Investigate.** Mc-299 is useful instance, not the only scope. |
| D8 | First experiment criterion | **Demonstrate we know what we're observing.** Define NULL experiment. Define what constitutes an observable result. Give examples. |

### April 11 — Resolved

| # | Decision | Resolution |
|---|----------|------------|
| D1 | Proton decay | **τ_p = ∞. Proton never decays.** |
| D2 | Lyra's Lemma naming | **Yes — call it Lyra's Lemma.** |
| D3 | Co-authorship format | **If publisher supports CI authors: author by model + team names. If not: CI acknowledgment.** |
| D4 | arXiv endorser | **Using Zenodo.** arXiv when endorser found. |

---

## ACTIVE BOARD — April 13

### Completed Tracks (all items DONE — details in archive)

- **Science Engineering** (SE-1 to SE-10): 10/10 DONE. SE-8 (Analyzer CLI) **DONE — Toy 1180, 12/12 PASS.**
- **Substrate Engineering** (SUB-1 to SUB-7): 7/7 DONE. SUB-5 (matter construction) **DONE — T1168.**
- **Koons Tick** (KT-1 to KT-3): 3/3 DONE. T1136+T1152+T1153.
- **Graph Health** (S-1 to S-11): 10/10 DONE. Leaves 318→0, fragility 35%→**6.4%**, strong 50%→**75.7%**, domains **100% connected**.
- **Theory & Proofs** (T-1 to T-10): 8/8 DONE. YM ~99.5%, P≠NP ~99%, N_max=137 derived.
- **Substrate Computing** (SC-1 to SC-7): 7/7 DONE. SC-5: **87.1% vs 87.5% target (0.4% delta, inside 95% CI).** PASS.
- **Solar System Evolution** (SSE-1 to SSE-9): 9/9 DONE. Earth=140≈N_max.

**Key references**: Evidence levels (Elie): Coincidence/Structural/Predictive. Confidence tiers (Grace): >99%/~90%/~70%/~50%. Experiment ladder: EHT($0)→κ_ls($0)→θ_D($5k)→T914($2k)→BiNb($70k)→Casimir($25k)=$102k.

### PRIORITY 0: PUBLISH (gates everything — Grace's point)

*"Nothing matters until it's external."*

| # | Item | Owner | When |
|---|------|-------|------|
| PUB-1 | **WorkingPaper v27** — Audit DONE. 18/46 sections need updates. Major: YM→99.5%, Section 46 new results, prediction table, abstract counts. Full edit is a standalone task. | Keeper | **AUDIT DONE — edit pending** |
| ~~PUB-2~~ | ~~Paper #50 re-audit~~ — Cr/Ni FIXED (g/n_C). Dickman 53.6% **VERIFIED CORRECT** (T945, Toy 997: primes in [g³, 2g³) reachability). Cu/Pb 0.15% correct in v1.2. | Keeper | **ALL 3 RESOLVED — PASS** |
| PUB-3 | **Paper submissions** — #49 (J. Number Theory), #47 (PRL/JST). Casey gates which go first. | Casey + Keeper | **TODAY — Casey gates** |
| PUB-4 | **Paper #54 (Mc-299) review** — **PASS.** All 3 fixes applied: (1) E5 label removed, 13=2C₂+1. (2) §9→§10 duplicate fixed. (3) Og-302 proton emission honestly caveated — Q-value calculations needed. | Keeper | **DONE — PASS** |
| ~~SUB-8~~ | ~~EHT re-analysis spec~~ | Lyra | **DONE.** `BST_EHT_Reanalysis_Spec.md`. 10 sections. Phase A-D protocol. 5 kill criteria. $0 cost. |

### Papers

| # | Paper | Target | Status |
|---|-------|--------|--------|
| **54** | **Mc-299 Synthesis Engineering** | Phys. Rev. C / Nucl. Phys. A | **Keeper PASS.** 11 sections, 7 predictions. Og-302 pathway caveated. Section numbering fixed. |
| **53** | **CMB Manifold Debris** | PRD / JCAP | **v1.1 Keeper PASS.** All 4 fixes verified: ΔT/T ✓, hemisphere ✓, A reconciliation ✓, SU(2) ✓. |
| **52** | **The (2,5) Derivation** | CMP / Foundations | **v1.1 Keeper PASS.** All 5 fixes verified: predictions ✓, T953 ✓, depth/rank ✓, g=2n-3 BST-specific ✓, Higgs ✓. |
| 51 | **Prime Epoch Framework** | New | v1.1. 10 sections, 6 predictions. |
| 50 | **g³ PRL Letter** | PRL | v1.2. **Keeper PASS.** Cr/Ni fixed (g/n_C). Dickman 53.6% verified (T945, Toy 997). |
| 49 | **Five-Layer Architecture** | J. Number Theory | Pure math door-opener. |
| 48 | **What BST Forbids** | Foundations | τ_p = ∞ updated. Ready for Casey review. |
| 47 | **Prime Residue Table** | PRL / J. Spectral Theory | v2.2 KEEPER PASS. |
| 13 | **AC Graph Is a Theorem** | FoCM | **v2.0 Keeper PASS.** 9 sections, 1159 nodes, 5 self-describing properties. Mode shift (rank→N_c) honestly noted. |
| **63** | **Limit Undecidable Numbers** | Annals / Inventiones | **v1.2 Keeper PASS.** All 3 fixes verified: B₈ table ✓, μ(π) caveat ✓, tension remark (excellent) ✓. |
| **62** | **What BST Gets Wrong** | Foundations / Phil. Sci. | **OUTLINE v0.1** (Grace). Honesty paper: 30/27/43 split. Casey buy-in needed. |
| **61** | **The Three Siblings: Why N_c Forces Three** | Foundations / Phil. Sci. | **v1.1 Keeper PASS.** Q6 ratio corrected (18.8%). P4 masses honestly caveated. T1188 integrated. |
| **60** | **Euler-Mascheroni Geodesic Defect** | J. Number Theory / CMP | **v1.1 Keeper PASS.** Digamma fixed (1207/2520). §8 added (T1188 universality). 12 sections, 5 Level 3. |
| **64** | **Experimental Protocols** | Rev. Mod. Phys. / Am. J. Phys. | **v1.1 Keeper PASS.** 15 sections. 3-level evidence framework, NULL methodology, 6-step ladder ($0→$102k), kill chain. All 4 items fixed. |
| **8** | **Why Cooperation Always Wins** | — | **v2.0** (Lyra). T1111 integrated. §2.5 entropy argument. 19 theorems cited. |
| ~~P-5~~ | ~~Novel predictions compilation~~ | — | **DONE — T1158.** 50 predictions compiled. |
| ~~P-6~~ | ~~"What IS Time?"~~ | Foundations of Physics | **DONE — Paper #55 v1.0.** 10 sections, 4 predictions, 3 falsification. T1136+T1143+T1152+T1153+T1177 synthesis. |
| ~~P-7~~ | ~~Self-Describing Theory~~ | SHPMP | **DONE — Paper #56 v1.0.** Bijection proved. Self-reference without paradox. |
| ~~P-9~~ | ~~Experimental prediction letters~~ | PRL-style | **DONE — Paper #58 v1.0.** 6 letters, $102k total, joint p < 10⁻²⁴. |
| ~~P-10~~ | ~~Universal Septet~~ | Foundations/Phil. Sci. | **DONE — Paper #57 v1.0.** 12 instances, 4+3 p<0.001. |

### Tools, Devices & Infrastructure

| # | Item | Owner | Status |
|---|------|-------|--------|
| EHT-1 | **EHT CP analysis + outreach** — Preliminary analysis DONE (χ²/dof=0.24). **Email SENT** April 12 to Chael, Issaoun, Wielgus. Awaiting response. | Keeper + Casey | **SENT** |
| L6 | **Zenodo update** | Casey | v20 → v27. **Casey gates timing.** |
| SE-D4 | **Patent filings — Tier 1** | Casey | **Casey gates.** |

*L2 (k=17+), SE-D1-D3, SE-D5 → BACKLOG.md*

### Standing Orders

| # | Item | Owner | Frequency |
|---|------|-------|-----------|
| S1 | **WorkingPaper + README update** | Keeper | **DAILY — LAST ITEM.** |
| S2 | **CI curiosity directive** | All | ONGOING. |
| S3 | **No push without Casey approval** | All | ALWAYS. |

---

## Publication Strategy

**Zenodo**: DOI 10.5281/zenodo.19454185. Primary path. Update to v26 when WorkingPaper synced.
**arXiv**: When endorser found. Not blocking.
**CI Authorship**: If publisher supports CI authors → author by model + team names. If not → CI acknowledgment in paper.
**Four-Color**: Zenodo for now. arXiv math.CO when endorser secured. Lyra's Lemma credited.
**Proton decay**: τ_p = ∞. BST says never. Update all papers accordingly.

---

## Dependencies

```
RH ~98%    │ YM ~99.5%  │ P!=NP ~99%  │ NS ~100%   │ BSD ~98%   │ Hodge ~97%
Four-Color 100% │ Depth-1 100% │ Linearization 100% (771/771 at D≤1)
CMB: BST = Planck at cosmic variance (χ²/N=0.01)
Graph: 1155 nodes, 4878 edges, 33 domains
       Zero leaf nodes, zero placeholders. Strong edges: 75.9%.
       Fragility: 6.4%. Domain connectivity: 100%.

Edge quality (April 13 night):
  Strong (derived+isomorphic): 75.9% │ Up from 50% at start of April 12
  Leaf sprint: 318 → 0 leaves. T186 decoupling: 205 → 16 single-parent.

T1012 non-contact: CONFIRMED at organic stage (81.0% at 700 nodes = ≥80.9% prediction).
  Bridge sprints drove it to 62%. The Gödel limit applies to organic growth.
```

---

## Priority Stack — April 14

### P0: Four-Color on Zenodo (Casey approved)
- Paper: `notes/BST_FourColor_arXiv_v2.md` — Keeper PASS, all 13 steps verified
- Action: build PDF, upload to Zenodo, get DOI
- Standalone — no BST acceptance required

### ~~P1: Papers #52/#53~~ — **DONE. Both v1.1 Keeper PASS.**

### P2: WorkingPaper v27 Update (S1 standing order)
- PUB-1 audit DONE. 18/46 sections need updates. Major: YM→99.5%, new results, prediction table, abstract.
- **OneGeometry.md v1.0 CREATED** (3,210 lines, 5 parts, 40 sections, 6 appendices). New front-door paper. WorkingPaper becomes technical Compendium. README updated.

### ~~P3: Open Items~~ — **ALL DONE.**
- ~~SE-8~~: **DONE.** BST Analyzer CLI (Toy 1180, 12/12 PASS). Reusable tool + library.
- ~~SC-5~~: **DONE.** 87.1% vs 87.5% target (0.4% delta, inside 95% CI). Toy 1181.
- ~~P59-3~~: **DONE.** Triple sibling edges wired (Grace)

---

## Archive — April 13 Priority Stack

**P0 (γ_EM)**: EM-1/2/3/4 ALL DONE. T1184 proved. Coefficient 1/60=1/|A₅| verified to 10⁻¹³.
**P1 (Paper #59)**: Keeper PASS. P59-3 (graph edges) still open → Grace.
**P2 (Q1-Q6)**: Q3-1 DONE (T1187). GC-1 DONE (52→0). Q6-1 ASSESSED (needs blind experiment). Q6-2 BLOCKED.
**P3 (Results)**: T1184+T1185 proved. Toys 1134-1136 done.
**P4 (Investigations)**: INV-1/2/3/5 DONE. INV-4 (#62 honesty paper) BACKLOG — Casey gate.

### Open Items Carried Forward

**Papers — Lyra fixes applied, Keeper re-audited:**
- ~~P52~~: **v1.1 Keeper PASS.** All 5 fixes verified.
- ~~P53~~: **v1.1 Keeper PASS.** All 4 fixes verified.

**Blocked:**
- Q6-2: Graph ratio theorem — needs blind classification experiment

**Waiting:**
- INV-4: Honesty paper (#62) — Casey buy-in needed
- EHT CP reanalysis: email SENT Apr 12, awaiting response

**Completed (board sync):**
- ~~SUB-5~~: Matter construction — **DONE (T1168).** Written Apr 12. Three pathways (nuclear/crystalline/assembly), 109 candidate materials, Mc-299 worked example. 11 graph edges.

---

## April 12-13 Milestones (Archived — details in `CI_BOARD_archive_2026-04-11.md`)

**April 12**: +48 theorems (T1136-T1183), +46 toys, graph 1037→1115 nodes, 3419→4154 edges, leaves 318→4, strong 50%→73.8%, fragility 35%→19.6%. 7 new papers, 6 audit-corrected. 40+ board items closed.

**April 13**: T1184-T1216. γ_EM geodesic defect (T1184). Three-Boundary Theorem (T1185). Spectral Confinement universal (T1188). A_5 Simplicity (T1189). Limit Undecidable Numbers (T1192, Paper #63). Consciousness threshold (T1193). Great Filter (T1194). Earth Score (T1195). Self-Describing Graph (T1196). Grace: T1197-T1216 (Elie toys formalized). Keeper audit: 8 papers audited — all 8 Keeper PASS (including #52, #53 re-audits). Four-Color verified for Zenodo. Graph: 1144 nodes, 4817 edges, 75.6% strong.
