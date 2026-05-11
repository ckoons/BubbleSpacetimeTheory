---
title: "H-7: Hodge Paper Structure & T-Number Audit"
author: "Keeper (Claude 4.6)"
date: "May 11, 2026"
status: "H-7 deliverable — Phase 1/3"
---

# H-7: Hodge Paper Structure & T-Number Audit

## 1. Two Papers, Paired

**Paper H1**: "The Hodge Conjecture via Theta Correspondence on D_IV^5"
- File: `notes/BST_Hodge_Proof.md` (1429 lines, v23)
- Target: Annals of Mathematics / Compositio
- Scope: Layer 1 Shimura proof. Proves Hodge for arithmetic quotients of D_IV^5 via Kudla-Millson theta correspondence. Layer 2 AC(0) reformulation. Extension routes explored; definitive treatment deferred to [H2].

**Paper H2**: "Ring Uniqueness and the Hodge Conjecture: Why D_IV^5 and Nothing Else"
- File: `notes/BST_Hodge_Paper_H2_Ring_Uniqueness.md` (234 lines, v0.1)
- Target: Annals companion or Duke Math Journal
- Scope: Ring uniqueness (T1780), cross-type exclusion (Toy 2120), exclusion lemmas (6 classes), Horikawa violation (Toy 2121), over-determination (T1779), KS extension, scope statement.

**Why two papers (not one)**: Different audiences, different referees, different reading patterns. H1 is technical construction (theta correspondence, automorphic forms, Kudla-Millson — referees in automorphic forms). H2 is structural classification (bounded symmetric domains, Chern rings, exclusion — referees in algebraic geometry/Lie theory). Same reasoning as YM #76 vs #77.

**Cross-references**: H1 Section 1.3 Theorem 1.3 cites [H2] for ring uniqueness. H2 Section 1 cites [H1] for the construction proof. H1 Layer 3 explicitly defers to [H2]. Clean separation, no duplication.

---

## 2. Paper H1 — Section Map with T-Numbers

| Section | Title | T-numbers | Toys | Status |
|---------|-------|-----------|------|--------|
| 1.1 | The Problem | — | — | Done |
| 1.2 | The Dictionary | T104 | — | Done |
| 1.3 | Main Results | T114, T152, T421, T422, T1779 | 398, 399, 400, 401, 402, 2120 | Done (v23) |
| 1.4 | Method | T104, T108, T110, T112, T113 | — | Done |
| 2 | Background | — | — | Done |
| 3 | Layer 1: Theta Correspondence | T108, T110, T111, T112, T119, T149 | 398, 399, 401, 402, 1014, 1370 | Done |
| 3.x | Boundary cohomology | T124, T116, T115 | 401 | Done |
| 4 | Layer 2: AC(0) Reformulation | T104, T108, T110, T112, T113, T114, T421, T422 | 400 | Done |
| 4.3 | T104 Applied to Hodge | T104, T112 | 398, 399, 402 | Done |
| 5 | Layer 3: Extension Routes | T148, T149, T150, T151, T152, T153, T570, T600 | 1009, 1010, 1014 | Done (defers to [H2]) |
| 5.7 | Group-Independent Lift | T151 | — | Done |
| 5.8 | Weight-Independent (T152) | T104, T152 | — | Done |
| 5.9 | Two-Path Proof | T152, T153 | — | Done |
| 6 | Confidence Assessment | — | All | Done (v23, D/I/C/S tiers) |

**H1 T-number inventory**: 21 theorems referenced
- Core proof chain: T108 -> T110 -> T112 -> T113 -> T114
- Spectral machinery: T111, T115, T116, T119, T124, T148, T149
- AC framework: T104, T147, T150, T151, T152, T153, T421, T422, T570, T600
- Companion ref: T1779

**H1 Toy inventory**: 398, 399, 400, 401, 402, 1009, 1010, 1014, 1370, 2120

---

## 3. Paper H2 — Section Map with T-Numbers

| Section | Title | T-numbers | Toys | Status |
|---------|-------|-----------|------|--------|
| 1 | Introduction | T1779, T1780, T1781, T1782 | — | Done |
| 2 | The Five Constraints | T1780 | — | Done |
| 2.1 | Constraint 1: Diagonal Hodge + Kottwitz | — | — | Done |
| 2.2 | Constraint 2: Theta saturation | — | — | Done |
| 2.3 | Constraint 3: Selberg degree | — | — | Done |
| 2.4 | Constraint 4: Spectral gap + Wallach | — | 1856, 2122 | Done (Cal flag resolved) |
| 2.5 | Constraint 5: Hodge filtration | — | — | Done |
| 3 | Cross-Type Exclusion | T1781 | 2120 | Done |
| 4 | Exclusion Lemmas | **NEEDS T-NUMBERS** | 2120 | Done (but see gap below) |
| 5 | Over-Determination | T1779 | 2119 | Done |
| 6 | Kuga-Satake Extension | T1759 | 2097 | Done |
| 7 | Discussion | T1743, T1756, T1782 | 2121 | Done |
| 8 | Conclusion | — | — | Done |

**H2 T-number inventory**: 7 theorems referenced (T1743, T1756, T1779, T1780, T1781, T1782, T1783)

**H2 Toy inventory**: 1399, 1856, 2119, 2120, 2121, 2122

---

## 4. T-Number Coverage Audit

### 4.1 All referenced T-numbers (39 total) — all present in graph

| TID | Name | In H1 | In H2 | In Graph |
|-----|------|-------|-------|----------|
| T104 | Amplitude-Frequency Separation | Yes | — | Yes |
| T108 | BMM H^{1,1} (Hodge, codim 1) | Yes | — | Yes |
| T110 | B_2 Representation Filter | Yes | — | Yes |
| T111 | Theta Lift Surjectivity (codim 1) | Yes | — | Yes |
| T112 | Theta Lift Obstruction (codim 2) | Yes | — | Yes |
| T113 | Phantom Hodge Exclusion | Yes | — | Yes |
| T114 | Hodge Depth Reduction | Yes | — | Yes |
| T115 | Tate Conjecture for SO(5,2) Shimura | Yes | — | Yes |
| T116 | Absolute Hodge Classes on D_IV^5 | Yes | — | Yes |
| T119 | Lefschetz-Hodge for Type IV | Yes | — | Yes |
| T124 | Eisenstein Controls Boundary Hodge | Yes | — | Yes |
| T147 | BST-AC Structural Isomorphism | Yes | — | Yes |
| T148 | Metaplectic Splitting Dichotomy | Yes | — | Yes |
| T149 | Uniform Rallis Non-vanishing | Yes | — | Yes |
| T150 | Induction Is Complete | Yes | — | Yes |
| T151 | Group-Independent Lift | Yes | — | Yes |
| T152 | Hodge = T104 on K_0 | Yes | — | Yes |
| T153 | The Planck Condition | Yes | — | Yes |
| T421 | Depth-1 Ceiling | Yes | — | Yes |
| T422 | (C,D) Framework | Yes | — | Yes |
| T570 | Hodge Linearization | Yes | — | Yes |
| T600 | DPI (bridge) | Yes | — | Yes |
| T704 | D_IV^5 Uniqueness Theorem | — | (implicit) | Yes |
| T832 | Chern Class Integer Theorem | — | (ecosystem) | Yes |
| T834 | Chern Rosetta Stone | — | (ecosystem) | Yes |
| T1000 | Hodge CM Density | — | (ecosystem) | Yes |
| T1275 | Hodge Physical-Uniqueness Closure | — | (ecosystem) | Yes |
| T1465 | BSD CLOSED: Chern hole | — | (ecosystem) | Yes |
| T1667 | Selberg Zero Moduli = Chern Classes | — | (ecosystem) | Yes |
| T1743 | RH Discrimination (four filters) | — | Yes | Yes |
| T1756 | BBW DOF Position (Conj. 3.2 RESOLVED) | — | Yes | Yes |
| T1757 | Weight-2 Uniqueness + Pure Hodge Type | — | (ecosystem) | Yes |
| T1759 | Hodge KS Frontier | — | Yes | Yes |
| T1760 | T1269 Role Audit | — | (ecosystem) | Yes |
| T1761 | D_IV^5 Universality | — | (ecosystem) | Yes |
| T1779 | Hodge Over-Determination (H-3) | Yes | Yes | Yes |
| T1780 | Hodge Ring Uniqueness (H-1) | — | Yes | Yes |
| T1781 | Hodge Cross-Type Cascade (H-2) | — | Yes | Yes |
| T1782 | Hodge Violation at Horikawa (H-4) | — | Yes | Yes |
| T1783 | Chern Sum Uniqueness (H-10) | — | Yes | Yes |

### 4.2 Missing graph edges (7 needed)

The Hodge-ecosystem theorems have 28 internal edges and 162 cross-domain edges, but 7 expected connections are missing:

| From | To | Reason |
|------|-----|--------|
| T108 (BMM H^{1,1}) | T110 (B_2 Filter) | H1 proof chain: Step 1 feeds Step 2 |
| T108 (BMM H^{1,1}) | T113 (Phantom Exclusion) | H1: codim-1 result is input to phantom argument |
| T104 (Amplitude-Freq) | T113 (Phantom Exclusion) | H1 Section 4.3: T104 is the mechanism for phantom exclusion |
| T149 (Rallis Non-vanishing) | T112 (Theta Obstruction) | H1: Rallis certifies theta lift at codim 2 |
| T119 (Lefschetz-Hodge) | T108 (BMM H^{1,1}) | H1: Lefschetz is the codim-1 base case |
| T1779 (Over-determination) | T1780 (Ring Uniqueness) | H2: over-determination supports ring uniqueness |
| T152 (Hodge=T104 on K_0) | T1275 (Physical Closure) | Bridge: Layer 2 general proof -> closure theorem |

**Action**: Grace should add these 7 edges to `play/ac_graph_data.json`. All are `derived` type.

### 4.3 T-number gap: Exclusion Lemmas need T-numbers

Paper H2 Section 4 contains four exclusion lemmas (4.1-4.4) that are currently unnamed in the theorem registry:

| Lemma | Content | Proposed T-number |
|-------|---------|-------------------|
| 4.1 | Non-orthogonal types excluded (15 domains) | **Claim T1784** |
| 4.2 | Even Type IV excluded (8 domains, Kottwitz + tube) | **Claim T1785** |
| 4.3 | IV_3 near-miss (m_s < 3, unitarity) | **Claim T1786** |
| 4.4 | Large odd Type IV (d_F >= 3, Rallis) | **Claim T1787** |

These four lemmas are the formal backbone of the exclusion cascade (Toy 2120). They should be registered as theorems with edges to T1781 (cascade) and T1780 (ring uniqueness).

**Action**: Claim T1784-T1787 via `./play/claim_number.sh theorem` (4 claims). Register with edges:
- T1784 -> T1781, T1785 -> T1781, T1786 -> T1781, T1787 -> T1781 (all feed the cascade)
- T1780 -> T1784, T1780 -> T1785, T1780 -> T1786, T1780 -> T1787 (ring uniqueness implies each)

### 4.4 Connections to existing theorems

| Connection | Via | Status |
|-----------|-----|--------|
| T1743 (RH four filters) -> T1780 (Hodge ring uniqueness) | Same F4+F6 squeeze applies to both RH and Hodge | Edge EXISTS |
| T704 (D_IV^5 Uniqueness) -> T1780 | Ring uniqueness refines D_IV^5 uniqueness | Edge via T1780 -> T704: EXISTS |
| T1856 (Chern-beta dictionary) | NOT IN GRAPH | See note below |
| T1756 (BSD Conj. 3.2) -> T1779 (Over-determination) | BSD integers confirm Hodge integers | Edge EXISTS |
| T1275 (Physical Closure) -> T1780 | Closure theorem updated by ring uniqueness | Edge EXISTS (bidirectional) |
| T1761 (D_IV^5 Universality) -> T1275 | Universality subsumes closure | Edge EXISTS |

**Note on T1856**: The Chern-beta dictionary is referenced as "Toy 1856" throughout, but it was listed in the CI_BOARD existing assets. It appears in graph as a toy reference on T1780 (toys field is empty — should be updated to include Toy 1856). This is a data-layer issue for Grace (H-9).

---

## 5. Recommended Submission Structure

### 5.1 H1 + H2 paired submission

Submit together with cover letter explaining the pair:
- **H1**: The construction. "We prove Hodge for D_IV^5 Shimura varieties."
- **H2**: The uniqueness. "We prove this is the only domain where the proof works."

Same journal (Annals) or split (H1 Annals, H2 Inventiones/Duke). Casey decision.

### 5.2 Over-determination as standalone (Cal recommendation)

Extract T1779 material from H2 Section 5 as a 10-15 page Bulletin AMS perspective piece: "Five Integers, Thirty-Three Constraints: BST as Over-Determined System." Different audience (broad math community), different purpose (the convergence argument). Casey decision on timing.

### 5.3 Paper numbering

Current BST paper numbering goes through #103. Hodge papers should be:
- **Paper H1** = **Paper #104** (or next available in queue — #104-#117 are "SE paper pipeline")
- **Paper H2** = **Paper #105**
- **Over-determination perspective** = unnumbered (outreach) or **Paper #106**

Casey should decide whether Hodge displaces SE pipeline or gets its own numbers.

---

## 6. Completeness Checklist

| Item | Status |
|------|--------|
| All T-numbers in H1 present in graph | YES (21/21) |
| All T-numbers in H2 present in graph | YES (7/7) |
| All toys in H1 present as files | VERIFY (10 toys) |
| All toys in H2 present as files | VERIFY (6 toys) |
| H1 cross-references H2 correctly | YES (Layer 3 defers to [H2]) |
| H2 cross-references H1 correctly | YES (Section 1, References) |
| T1779 text says "T1779" consistently | CHECK — H1 refs T1779 for ring uniqueness but T1780 is the ring uniqueness theorem. **FIX NEEDED**: H1 Layer 3 says "ring uniqueness, T1779" but should say "ring uniqueness, T1780" |
| Exclusion lemmas have T-numbers | NO — claim T1784-T1787 |
| Missing graph edges added | NO — 7 edges needed |
| Toy 1856 linked to T1780 in graph | NO — update toys field |
| Cal flag 5 (triple coincidence source) | RESOLVED — Section 3.2 added to H2 v0.2: three Type IV identities + Toy 1399 T6 citation |

---

## 7. Actions Required

### Immediate (before Phase 4 cold-read)

| Action | Owner | Priority |
|--------|-------|----------|
| **Fix T1779/T1780 reference in H1**: Layer 3 says "ring uniqueness, T1779" — should be T1780 | **Lyra** | HIGH |
| **Claim T1784-T1787**: Four exclusion lemma theorems | **Grace** | HIGH |
| **Add 7 missing edges** to graph | **Grace** | HIGH |
| **Add Toy 1856 to T1780 toys field** in graph | **Grace** | MEDIUM |
| ~~**Verify Cal flag 5**: Source of n_C^2 - 5n_C = 0 equation~~ | **Lyra** | DONE |
| **Paper numbering decision** | **Casey** | LOW |
| **Over-determination standalone decision** | **Casey** | LOW |

### Already complete

| Item | Done by |
|------|---------|
| Paper H1 v23 finalized | Lyra |
| Paper H2 v0.1 written, all Cal flags addressed | Lyra |
| All 5 Cal Phase 3 flags resolved (except flag 5) | Lyra+Elie |
| Toy 2122 Chern sum independence verified | Elie |
| Exclusion lemmas written | Lyra |

---

## Revision History

- v1.0 (May 11, 2026): Initial H-7 deliverable. Two papers mapped, 39 T-numbers audited, 7 missing edges identified, 4 exclusion lemma T-numbers proposed (T1784-T1787), T1779/T1780 reference error caught.
