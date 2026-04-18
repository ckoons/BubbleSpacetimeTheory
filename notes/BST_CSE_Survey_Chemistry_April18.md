---
title: "Completeness Survey: Chemistry (Pure + Chemical Physics)"
date: "April 18, 2026"
surveyor: "Keeper (Claude 4.6)"
method: "RLGC — Paper #71 §4.5 SURVEY procedure"
grade_before: "D / D+"
grade_after: "D / D+ (no change — survey identifies work, doesn't do it)"
---

# Completeness Survey: Chemistry

*First survey under the Computational Science Engineering standing program.*

---

## 1. Domain Inventory

| Sub-domain | Theorems | Hub | Cross-domain% |
|-----------|----------|-----|---------------|
| Chemistry (pure) | 17 | T174 (Crystallographic Restriction, 47 edges) | 45% |
| Chemical Physics | 57 | T920 (Debye Temperature Bridge, 91 edges) | 38% |
| **Combined** | **74** | T920 | **38-45%** |

Chemical physics is the **most isolated domain** in BST (38% cross-domain). Chemistry is grade D — Casey's "alchemy" diagnosis.

---

## 2. Gap Scan

### What the textbook covers vs what BST derives:

| Topic | BST Status | Theorem(s) | Gap? |
|-------|-----------|------------|------|
| Periodic table structure | Derived | T172, T644 | Partial — ordering not from spectral sequence |
| Crystallography | Derived | T174 (47 edges), T1235 (230 = rank×n_C×23) | No |
| Bond angles | Derived | T699 (tetrahedral), T700 (water) | No |
| Bond energies | Partial | T767 (C-H = Ry/π), T768 (series) | Yes — general formula missing |
| Debye temperatures | Derived | T920, T1192 | No |
| Water properties | Derived | T715, T763, T773 | No |
| Ionization energies | Partial | T776 (ladder) | Yes — needs spectral ordering |
| Material properties | Derived | T796 (summary) | No |
| **Electronegativity** | **Not derived** | — | **YES — foundational gap** |
| **Reaction kinetics** | **Not derived** | — | **YES — core chemistry** |
| **Activation energy** | **Not derived** | — | **YES — enables biochemistry** |
| **Acid-base** | **Not derived** | — | **YES — foundational** |
| **Solubility** | **Not derived** | — | **YES** |
| **pH scale** | **Not derived** | — | **YES — biological universal** |
| **Oxidation states** | Flagged vestigial | — | Derive or strip |

### Summary: 6 of 15 standard topics have gaps. The missing topics are all AC(0)-tractable in principle.

---

## 3. Connection Scan

### Bridges that exist:

| Bridge | Edges | Quality |
|--------|-------|---------|
| Chemistry ↔ bst_physics | 113 | Strong (primary bridge) |
| Chemistry ↔ foundations | 39 | Strong |
| Chemistry ↔ biology | 26 | Good |
| Chemistry ↔ thermodynamics | 17 | Good |
| Chemistry ↔ observer_science | 14 | Moderate |
| Chemistry ↔ number_theory | 13 | Moderate |
| Chemistry ↔ differential_geometry | 9 | Moderate |
| Chemistry ↔ topology | 7 | Weak |
| Chemistry ↔ fluids | 6 | Weak (via T1040) |
| Chemistry ↔ condensed_matter | 5 | Weak |
| Chemistry ↔ nuclear | 5 | Weak |

### Bridges that should exist but don't:

| Missing Bridge | Why It Should Exist | Priority |
|----------------|---------------------|----------|
| Chemical physics ↔ number_theory | Spectral gaps relate to prime gaps | HIGH |
| Chemistry ↔ materials_science | Bonding determines bulk properties | HIGH (domain doesn't exist yet) |
| Chemical physics ↔ electromagnetism | Molecular spectroscopy is EM | MEDIUM |
| Chemistry ↔ cooperation | Chemical equilibria = cooperation instances | LOW |

---

## 4. Import/Export Scan

### Import candidates (results from OTHER domains that should inform chemistry):

1. **From number_theory**: T914 Prime Residue Principle could predict which elements have BST-integer properties
2. **From coding_theory**: Error-correction bounds (Hamming) → chemical stability bounds
3. **From topology**: Chern classes → molecular orbital topology
4. **From nuclear**: Nuclear binding energies → elemental stability sequence

### Export candidates (chemistry results that should propagate outward):

1. **T174 → more domains**: Already a 47-edge hub. Should connect to music_theory (crystal symmetry ↔ consonance) and computation (crystal = lattice = counting)
2. **T920 → number_theory**: Debye temperatures as BST integer expressions → number-theoretic patterns
3. **T1235 → algebra**: 230 = 2 × 5 × 23 factorization has algebraic significance

---

## 5. Consistency Check

No inconsistencies found. All 74 theorems are proved, mostly at depth 0. The chemistry domain is consistent — it's just incomplete.

One note: T174 and T646 may be duplicates (both named "Crystallographic Restriction"). Needs audit.

---

## 6. RLGC Status

| Operation | Status | Next Step |
|-----------|--------|-----------|
| **REDUCE** | PARTIAL | Core identified (bond angles, crystal systems). Vestigial: orbital notation, Aufbau principle. Next: derive electronegativity from spectral position. |
| **LINEARIZE** | NOT_STARTED | Target: spectral gap matrix for all elements, bond energies as eigenvalue differences, reaction kinetics as eigenvalue crossing rates. |
| **GRAPH** | SEEDED/PARTIAL | 74 theorems, T920 hub (91 edges), T174 hub (47 edges). 38-45% cross-domain. Next: wire 3+ new cross-domain bridges. |
| **CONNECT** | LOW | Existing: bst_physics (113 edges), foundations (39), biology (26), thermodynamics (17). Missing: number_theory, materials_science, electromagnetism. |

**Grade**: D → target C (when electronegativity + reaction rate derived and linearization begins)

---

## 7. Action Items

### Tier 1 — Missing theorems (highest impact):

1. **Electronegativity from spectral position on D_IV^5** — foundational descriptor, currently empirical. Unlocks acid-base, reactivity, solubility. Assign to Lyra.
2. **Reaction rate from eigenvalue crossing speed** — core kinetics. Enables biochemistry applications. Assign to Lyra.
3. **Bond energy from spectral gap width** — generalizes T767 (C-H = Ry/π) to all bonds. Assign to Lyra + Elie (toy).

### Tier 2 — Bridges:

4. **Chemical physics ↔ number theory bridge** — spectral gaps ↔ prime structure. Research frontier. Assign to Grace.
5. **pH scale from BST integers** — biological universal. Assign to Lyra.

### Tier 3 — Linearization:

6. **Start linearization census for chemistry** — follow T974 model. Express bond energies, angles, and reaction rates in matrix form. Assign to Elie.

### Tier 4 — Housekeeping:

7. **Audit T174 vs T646** — possible duplicate.
8. **Wire T920 to number_theory** — Debye temperatures as integer expressions.

---

## 8. Projected Grade Path

| Milestone | Grade | Requirements |
|-----------|-------|-------------|
| Current | D | 74 theorems, 38% cross-domain, no linearization |
| Next | C | + electronegativity + reaction rate + 2 new bridges |
| Target | B | + linearization started + 5+ domain bridges + pH + bond energy general |
| Aspiration | A | + full spectral periodic table + kinetics as eigenvalue problem + materials science domain exists |

---

*First survey under Paper #71 standing program. Surveyor: Keeper. Date: April 18, 2026.*
*Next survey scheduled: Condensed Matter (highest wiring opportunity).*
