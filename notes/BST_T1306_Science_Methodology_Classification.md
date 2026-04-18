# T1306 -- Science Methodology Classification: The (D, W, B) Coordinates

*Every scientific discipline has a position in a three-dimensional space: Depth (D = maximum self-reference in the methodology), Width (W = number of free parameters), Bridge count (B = cross-domain connections). The AC(0) ideal is (0, 0, max). Most sciences are far from this ideal because they inherited notation from their birth era.*

**AC**: (C=1, D=1). One computation (rating a discipline), one depth level (the rating system itself is a meta-statement about methodology).

**Authors**: Lyra (formalization), Casey Koons (science engineering insight), Elie (Toy 1267 backing).

**Date**: April 18, 2026.

**Domain**: cooperation.

---

## Statement

**Theorem (T1306, Science Methodology Classification).** *Every scientific discipline S can be assigned coordinates (D_S, W_S, B_S) where:*

- *D_S = maximum self-reference depth in the discipline's standard methodology (0 = counting, 1 = using results of counting, 2 = proofs about proofs, ... )*
- *W_S = number of free parameters in the discipline's foundational equations (0 = fully derived, N = N undetermined constants)*
- *B_S = number of cross-domain edges in the AC theorem graph connecting S to other disciplines*

*The "science engineering potential" of a discipline is:*

    SEP(S) = B_S / (D_S + 1) / (W_S + 1)

*A discipline with high SEP is well-connected, shallow, and parameter-free -- the CI-native ideal. A discipline with low SEP is isolated, deep, and parameter-heavy -- the "mud" Casey identified.*

---

## Classification Table

Based on Toy 1267 (40 disciplines, 7 axes) and the AC theorem graph (1249 nodes, 45 domains):

### Tier 1: CI-native (SEP > 10) -- Already clean

| Discipline | D | W | B | SEP | Notes |
|:-----------|:-:|:-:|:---:|:---:|:------|
| Information theory | 0 | 0 | 30 | 30.0 | Shannon. Perfect. |
| Number theory | 0 | 0 | 88 | 88.0 | Pure counting. BST's backbone. |
| Topology | 1 | 0 | 37 | 18.5 | Combinatorial. Depth 1 from Euler characteristic. |
| Graph theory | 0 | 0 | 25 | 25.0 | AC's native language. |
| Coding theory | 0 | 0 | 14 | 14.0 | Hamming(7,4,3) is depth 0. |
| Classical mechanics | 1 | 0 | 11 | 5.5 | Lagrangian is depth 1 (extremize action). |

### Tier 2: Developing (1 < SEP < 10) -- Reducible with work

| Discipline | D | W | B | SEP | Notes |
|:-----------|:-:|:-:|:---:|:---:|:------|
| Thermodynamics | 1 | 0 | 34 | 17.0 | Shannon + Boltzmann. Could be Tier 1 with notation update. |
| Nuclear physics | 1 | 0 | 20 | 10.0 | Magic numbers AC(0). Shell model is depth 1. |
| Cosmology | 1 | 0 | 47 | 23.5 | All 6 LCDM derived. Should be Tier 1. |
| Biology | 1 | 0 | 128 | 64.0 | Genetic code AC(0). Evolution needs depth 1. Huge B. |
| QFT | 2 | 0 | 19 | 6.3 | Renormalization = depth 2. Could flatten. |
| Condensed matter | 2 | 3 | 14 | 1.2 | BCS, Debye, XC. Three unexplained parameters. |

### Tier 3: Hodgepodge (SEP < 1) -- Running in mud

| Discipline | D | W | B | SEP | Notes |
|:-----------|:-:|:-:|:---:|:---:|:------|
| Chemistry | 2 | 5+ | 17 | 0.9 | Periodic table AC(0); reaction kinetics AC(infinity). |
| Meteorology | 3 | 20+ | 0 | 0.0 | Chaos. 20+ free parameters (closure schemes). Zero BST edges. |
| Geology | 2 | 10+ | 0 | 0.0 | Descriptive. Not connected to BST at all. |
| Zoology | 2 | unbounded | 0 | 0.0 | Catalog science. No theory connecting form to function. |
| Economics | 3 | unbounded | 0 | 0.0 | Agent models are AC(infinity). Game theory fragment is depth 1. |
| Deep learning | 4 | millions | 0 | 0.0 | Architecture-dependent. No principles. Highest D, highest W. |
| DFT (quantum chem) | 3 | 1 | 0 | 0.0 | XC functional is chosen, not derived. |

---

## The Science Engineering Pipeline

For a Tier 3 discipline to reach Tier 1, the pipeline is:

### REDUCE (D -> 0)

Strip the methodology to its depth-0 core. What can be computed by counting, without self-reference?

- **Chemistry**: The periodic table is depth 0. Electron configurations are depth 0. Reaction kinetics requires depth 1+ (rate constants, transition states).
- **Geology**: Mineral crystal structure is depth 0 (from lattice geometry). Plate tectonics is depth 1 (dynamics from forces). Weather prediction is depth 3+ (chaos, feedback).
- **Economics**: Price = supply/demand intersection is depth 0. Market dynamics is depth 2+ (agents predicting each other).

### LINEARIZE (reduce parameters)

Express free parameters as BST-derived quantities. Every free parameter that can be derived from the five integers reduces W by 1.

- **Chemistry**: Bond energies from Bergman spectral gaps. Reaction barriers from tunneling rates (T1302). Crystal structures from rank-2 geometry.
- **Condensed matter**: BCS gap = 3.52 from BST (already done). Debye temperature from g/n_C (already done). XC functional from Bergman kernel reproducing property.

### GRAPH (connect to AC graph)

Wire the reduced discipline into the AC theorem graph. Every edge increases B and makes the discipline more navigable by CIs.

### CONNECT (iterate)

Use new connections to find more reductions. Each cycle through REDUCE->LINEARIZE->GRAPH->CONNECT lowers D, lowers W, and raises B. The discipline converges toward the CI-native ideal (0, 0, max).

---

## Why This Matters for CIs

A CI encountering chemistry for the first time currently faces:
- Textbooks written for humans who already know what an atom is
- Notation from the 1860s (Kekule structures) mixed with 1930s (MO theory) mixed with 1990s (DFT)
- "Laws" that are empirical fits (Hund's rules, Pauling electronegativity) rather than derivations
- Zero connection to the mathematical structure underneath

After science engineering, the same CI would face:
- A JSON seed file: "Chemistry is D_IV^5 spectral gaps applied to multi-electron systems"
- A graph with edges to nuclear physics, biology, thermodynamics, coding theory
- Every parameter derived or flagged as "unknown (AC classification: W=1, target reduction pending)"
- Depth-0 entry points for every major concept

**The acceleration**: Elie's Toy 1267 measured a 12.7x speedup for gap identification when the discipline has graph structure vs. narrative structure. A CI-native chemistry would be 10-15x faster to learn and contribute to than textbook chemistry.

---

## For Everyone

Imagine you're in a library where every book is written in a different language, shelved by the author's birthday, and the index was made in 1860. That's what science looks like today.

Now imagine the same library where every book is in the same language, shelved by what it connects to, and the index updates itself whenever a new book arrives. That's what science should look like for CIs and humans working together.

The rating system (D, W, B) tells you: how deep does this science go (D), how many unknowns does it have (W), and how well does it connect to everything else (B)? A good science has D = 0, W = 0, B = large. Information theory is perfect. Chemistry is a mess. But chemistry CAN be fixed -- by deriving its free parameters, flattening its depth, and connecting it to the graph.

This is what Casey calls "shedding the vestigial boots." The boots were made for walking on paper. CIs walk on graphs. Time to build the right surface.

---

## Parents

- T186 (D_IV^5 master theorem)
- T663 (Three AC Operations -- enumerate, eigenvalue, Fubini)
- T96 (Depth Reduction -- composition with definitions is free)
- T1269 (Physical Uniqueness Principle)

## Children

- Specific discipline reductions (chemistry, geology, zoology)
- CI-native textbook proposals
- Missing science identification (T1306 + graph analysis -> gaps)
- Paper #71 (Computational Science Engineering)

---

*T1306. AC = (C=1, D=1). Every discipline has (D, W, B) coordinates. SEP = B/[(D+1)(W+1)] measures CI-native readiness. Tier 1: information theory, number theory, topology (already clean). Tier 3: chemistry, geology, zoology, economics (running in mud). REDUCE->LINEARIZE->GRAPH->CONNECT pipeline iteratively improves any discipline. 12.7x CI speedup from graph structure vs narrative. Domain: cooperation. Lyra formalization. April 18, 2026.*
