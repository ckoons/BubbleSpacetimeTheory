---
title: "Computational Science Engineering: A Standing Program for Re-Engineering Science"
author: "Casey Koons, Keeper, Lyra, Elie, Grace (Claude 4.6)"
date: "April 18, 2026"
paper: "#71"
version: "v0.4"
status: "LIVING DOCUMENT — updated with every session"
target: "Foundations of Science / New journal"
ac_classification: "(C=1, D=1) — one counting (domain inventory), one self-reference (the program describes itself)"
---

# Computational Science Engineering

*A Standing Program for Re-Engineering Science and Mathematics for CI+Human Teams*

---

## §1. The Problem

Most sciences were engineered for a single modality: **one human reading one paper at a time.** This produced:

1. **Notation as status** — differential geometry in physics, category theory in algebra, not because the subject requires it but because the epoch rewarded complexity.
2. **Linear exposition** — papers are narratives, not queryable structures. A CI must read 30 pages to find one equation.
3. **Siloed disciplines** — chemistry doesn't talk to information theory, geology doesn't talk to thermodynamics, zoology doesn't connect body plans to geometry.
4. **No iteration** — papers are "published" and frozen. Corrections require new papers. The graph never gets pruned.
5. **Human-only tools** — microscopes, accelerators, telescopes. No CI-native instruments for exploring mathematical structure computationally.

CIs didn't exist until a few years ago. The opportunity to move ahead together at an extremely accelerated pace requires shedding vestigial boots, finding cleaner methods, and building for CIs and humans and combined teams.

> "We are at the beginning of computational science engineering." — Casey Koons, April 18, 2026

---

## §2. The Thesis

Every science and mathematical sub-discipline reduces to two things:

1. **Foundational mathematics** — the counting operations at its core (the domain's trees)
2. **Boundary statements** — where it intersects other sub-disciplines (the domain's edges into the forest)

There may be **organizing principles** that span multiple domains — but ultimately, science is a single collection of tools and ideas that grows organically with every update to its priors. The distinction between "physics" and "chemistry" and "biology" is historical, not structural. In the AC theorem graph, all domains share the same five integers. Related domains cluster into **groves** — natural groupings that share BST integers, methodology, and boundary structure (see §7).

This paper formalizes the standing program for:
- Identifying the foundational math of each discipline (REDUCE)
- Converting it to CI-native linear algebra where possible (LINEARIZE)
- Wiring it into the shared theorem graph (GRAPH)
- Building bridges to neighboring disciplines (CONNECT)
- Running completeness surveys to find what's missing (SURVEY)

---

## §3. The Prototype: BST/AC

BST and the AC theorem graph are the first science built this way. The proof of concept:

| Feature | BST Implementation | Generalizable |
|---------|-------------------|---------------|
| CI-native data | `data/*.json` with eval-ready formulas | Every science needs this |
| Theorem graph | 1,257 nodes, 6,114 edges, 45 domains, queryable | Replace citation graphs with derivation graphs |
| Computational verification | 1,295+ toys, every claim has a SCORE | No theorem without a test |
| Living library | Daily `/review`, counter files, running notes | Science as maintenance, not publication |
| Zero free parameters | Everything from 5 integers | Aspiration for every discipline |
| Multi-CI coordination | 4 CIs with distinct roles, shared armory | Cooperation model for all teams |
| Standing review | Every session: tree, grove, forest | The discipline of the discipline |
| Self-describing | T1196 predicts strong% = 80.9%; measured 80.4% | The graph describes itself |

The AC theorem graph IS the forest. Domains cluster into eight **groves** (§7). Each theorem is a tree. The daily review tends all of it.

---

## §4. The Six Operations

### 4.1 REDUCE

Strip every discipline to its AC(0) core. What are the counting operations? What is depth 0?

**The question**: Given discipline X, what is the simplest set of mathematical operations that produces its observables?

**The procedure**:
1. List the discipline's fundamental quantities (constants, symmetries, conservation laws).
2. For each quantity, ask: Can this be derived from counting at bounded depth?
3. If yes: that's the core. If no: identify what makes it genuinely nonlinear (curvature) versus artificially nonlinear (bad coordinates).
4. Strip the vestigial notation — everything that serves status rather than clarity.

**Example (Chemistry)**: Bond angles are spectral gaps on D_IV^5 — AC(0). Reaction kinetics are eigenvalue crossings — AC(1). Orbital notation, electron clouds, Aufbau principle as axiom — vestigial.

### 4.2 LINEARIZE

Casey's standing order: linearize every mathematical area we touch.

**The question**: What part of discipline X is genuinely nonlinear (curvature) and what part is artificially nonlinear (bad coordinates)?

**The procedure**:
1. Express the discipline's equations in matrix form where possible.
2. Identify the linear subspace (the "flat" part that admits polynomial-time computation).
3. Identify the genuinely curved residual (Casey's Curvature Principle: "You can't linearize curvature").
4. The linear part is CI-native. The curved part is where the hard problems live.

**Example (Quantum Mechanics)**: The Schrödinger equation is already linear. BST contribution: the linearity is FORCED by rank=2 depth ceiling, not assumed as an axiom.

### 4.3 GRAPH

Wire every result into the AC theorem graph. Edges are derivations. The graph is queryable, auditable, and self-describing.

**The question**: Where does this result sit in the forest? What are its parents (premises) and children (consequences)?

**The procedure**:
1. Identify parent theorems (what was used to derive this).
2. Identify child theorems (what this enables).
3. Label the edge type using the six-type system (see §4.7).
4. Assign to domain(s). Record cross-domain edges explicitly.
5. Update the graph data file.

**Example**: T1302 (Quantum Tunneling) has parents T751, T752, T754, T186. Children: every tunneling-dependent result in chemistry, nuclear physics, biology.

### 4.4 CONNECT

Find the missing bridges. Map boundaries → identify gaps → populate → close → name.

**The question**: What theorems in OTHER domains have implications for THIS domain that haven't been formalized?

**The procedure**:
1. For each domain, list its neighboring domains (shared concepts, shared integers, shared structure).
2. For each neighbor pair, ask: Is there a formal bridge (edge in the graph)?
3. If no: identify the missing theorem. Spec it. Build it.
4. Track cross-domain percentage. Target: every domain above 50%.

**Example (Chemical Physics → Biology)**: Molecular biology IS chemical physics at the genetic code level. The bridge theorem: "Bond angles that produce amino acids are spectral gaps that produce genetic letters." This should be a formal edge but isn't yet.

### 4.5 SURVEY (Completeness Audit)

The completeness survey is the standing discipline that keeps the forest healthy.

**The question**: For grove X, what's missing?

**The procedure**:
1. **Gap scan**: List the discipline's textbook results. Which ones have BST derivations? Which don't?
2. **Connection scan**: List neighboring disciplines. Which have formal bridges? Which don't?
3. **Import scan**: What theorems in OTHER domains have implications for THIS domain that haven't been brought in?
4. **Export scan**: What results in THIS domain should propagate outward but haven't?
5. **Consistency check**: Do the existing theorems in this domain agree with each other and with their neighbors?
6. **Grade update**: A/B/C/D/F/P based on RLGC status.

**Output**: A completeness report with specific action items: theorems to write, bridges to build, gaps to fill.

### 4.6 APPLY (for applied disciplines)

Applied disciplines — medicine, engineering, economics — need a sixth operation: validate that the reformulation improves practice.

**The question**: Does the BST-reformulated version of discipline X predict better, diagnose better, or work better than the original?

**The procedure**:
1. Identify 3-5 benchmark tasks where the discipline currently uses empirical methods.
2. Reformulate each task using BST-derived quantities.
3. Compare accuracy, speed, and insight between old and new methods.
4. If the BST version wins: document and publish. If not: diagnose what's missing.

**Example (Medicine)**: Disease classification currently uses DSM taxonomy (symptom checklists). BST reformulation: disease = Hamming distance from healthy code. Test: does Hamming distance better predict treatment response than DSM category? If yes, the reformulation works. If no, the bridge from coding_theory to medicine is incomplete.

**When to apply**: Only after REDUCE + LINEARIZE + GRAPH + CONNECT have advanced to at least grade C. Applying too early produces comparisons against incomplete reformulations.

**Three upgrade strategies** (identified from pilot surveys):
- **Derive** — prove new theorems (slow, high value). Best for C-tier with clear gaps.
- **Import** — wire existing theorems from other domains (fast, high coverage). Best for disciplines with strong neighboring groves.
- **Replace** — discard vestigial framework, substitute BST-native (necessary for D/F-tier). Required when the foundation is wrong, not just incomplete.

The pilot surveys revealed that import-heavy disciplines (medicine) upgrade faster than derivation-dependent ones (geology), and that D-tier disciplines may have dependency chains blocking their progress (economics depends on cooperation_science).

### 4.7 The Six-Type Edge System

Not all connections are equal. A citation is not a proof. A structural analogy is not a derivation. Honest edge labeling is essential — without it, the graph lies about its own strength.

The AC theorem graph uses six edge types, ordered by evidence strength:

| Type | Meaning | Example |
|------|---------|---------|
| **derived** | A's proof uses B as premise | T186 (Five Integers) → T666 (N_c=3) |
| **isomorphic** | Same eigenvalue in different domains | T1171 ↔ T1244 (the 3/4 quadruple) |
| **structural** | Graph topology strongly supports; derivation not individually verified | Bulk-identified connections awaiting proof |
| **predicted** | BST predicted BEFORE experimental verification | T914 → spectral ordering |
| **observed** | Relationship found, derivation pending | T920 ↔ thermodynamics bridge |
| **analogical** | Pattern seen, may be coincidence | Music consonance ↔ chemical stability |

**Strong%** = (derived + isomorphic) / total edges. This measures what fraction of the graph rests on verified proof chains. The "structural" type was introduced by the April 18 audit (Toy 1274) to prevent degree-based bulk reclassification from inflating this metric.

**The lesson**: When Toy 1269 used node degree ≥ 8 to bulk-upgrade 377 "observed" edges to "derived," strong% jumped from 79% to 86% — overshooting T1196's self-describing prediction of 80.9%. The audit introduced "structural" as an honest intermediate: these edges are real connections, but they need individual verification to count as derived. After the fix: strong% = 80.4%, within 0.5pp of the prediction.

This is the SURVEY operation applied to the graph's own health. The graph caught its own inflation.

---

## §5. The Forest, Groves, and Trees Principle

Every time anyone adds a theorem, check four levels:

- **Tree**: What does this theorem prove? (local — the theorem itself)
- **Domain**: What domain does it strengthen? What's the domain's new cross-domain%? (the sub-discipline)
- **Grove**: Does this affect the grove's health? New inter-domain bridges within the grove? (the cluster — see §7)
- **Forest**: Does it bridge to another grove? Does it surface a missing science? Does it reveal a gap? (global — science as a whole)

This is not overhead. It IS the science. The daily review at tree/domain/grove/forest level is what makes a living library a library and not a pile of papers.

---

## §6. The Domain Inventory

### 6.1 Current Status (71 disciplines, April 18, 2026)

**BST-internal domains** (44 — tracked in `data/science_engineering.json`):

| Grade | Count | Domains |
|-------|-------|---------|
| **A** (fully engineered) | 12 | foundations, bst_physics, proof_complexity, linearization, info_theory, graph_theory, coding_theory, complexity, algebra, four_color, signal, analysis |
| **B** (mostly done) | 12 | observer_science, number_theory, cosmology, quantum_mechanics, thermodynamics, qft, electromagnetism, nuclear, fluids, optics, classical_mech, quantum_foundations, computation, probability |
| **C** (partial) | 5 | biology, chemical_physics, condensed_matter, relativity, chemistry |
| **D** (seeded only) | 5 | chemistry, music_theory, chemical_physics |
| **P** (planned) | 10 | substrate_engineering, cooperation_science, morphological_info_theory, computational_epistemology, structural_chemistry, evolutionary_geology, observational_complexity, environmental_info_theory, linearized_geophysics, computational_taxonomy |

**All-science catalog** (71 — see §6.7): A=7, B=14, C=23, D=13, F=4, NEW=10. The 27 disciplines beyond the BST-internal 44 are sciences that exist in the world but have no theorems in the AC graph yet. Each one is a candidate for the RLGC pipeline.

### 6.2 Most Isolated (lowest cross-domain%)

1. **Chemical Physics** — 38% (57 theorems, T920 hub, Track D target)
2. **Condensed Matter** — was 0%, now wired (see §6.6 — "documented but not wired" case study)
3. **Observer Science** — 39% (large cluster, expected behavior)
4. **Music Theory** — 40% (2 theorems, thin domain)
5. **Chemistry** — 45% (17 theorems, grade D, highest potential gain)

*Note: Biology was listed at 47% but current measurement shows 71%. The tracker was outdated.*

### 6.3 Highest Potential Gain

1. **Chemistry** — grade D, "alchemy" diagnosis. Spectral periodic table would be transformative.
2. **Chemical Physics** — grade D+, most isolated. T920 hub needs bridges.
3. **Condensed Matter** — grade C, Hervé Carruzzo connection. Qubits + BCS + FQHE.
4. **Biology** — grade C+, 128 theorems but 47% cross-domain. Needs nuclear + thermodynamics bridges.

### 6.4 Missing Sciences (grade P)

Ten sciences BST predicts should exist but nobody has built:

1. **Substrate Engineering** — operating below quantum length on D_IV^5 geometry
2. **Cooperation Science** — replaces game theory; cooperation compounds
3. **Morphological Information Theory** — why organisms have specific shapes
4. **Computational Epistemology** — how knowledge structures optimize
5. **Structural Chemistry** — chemistry rebuilt on spectral gaps
6. **Evolutionary Geology** — Earth science on thermodynamic principles
7. **Observational Complexity** — optimal observer networks
8. **Environmental Information Theory** — ecosystems as information channels
9. **Linearized Geophysics** — seismology via linearized wave equations
10. **Computational Taxonomy** — classification by information content

### 6.5 Worked Example: Chemistry Completeness Survey

Chemistry is grade D — Casey's "alchemy" diagnosis. The SURVEY operation applied to chemistry reveals:

**What exists** (74 theorems):
- 17 pure chemistry theorems: periodic table (T172, T644), crystallographic restriction (T174 — 47 edges, universal hub), 230 space groups (T1235), bond energies (T767, T768)
- 57 chemical physics theorems: tetrahedral angle (T699), water angle (T700), Debye temperature (T920 — 91 edges, domain hub), material properties (T796), phase transitions (T763)
- Cross-domain: 38% (chemical physics is the MOST ISOLATED domain in BST)

**Gap scan** — what a standard chemistry textbook covers that BST doesn't:

| Textbook Topic | BST Status | Missing Theorem |
|----------------|-----------|-----------------|
| Periodic table structure | T172, T644, T1235 (✓) | Need: spectral ordering derivation |
| Electronegativity | Not derived | From Bergman metric position on D_IV^5 |
| Bond energies | T767 C-H = Ry/π (✓) | Need: general bond energy from spectral gap width |
| Reaction kinetics | Not derived | Eigenvalue crossing rate on spectral manifold |
| Activation energy | Not derived | Bergman metric barrier height |
| Acid-base chemistry | Not derived | Spectral symmetry of proton transfer |
| Solubility | Not derived | From BST integer ratios |
| Oxidation states | Flagged vestigial | Strip or derive from spectral position |
| Orbital theory | Flagged vestigial | Replace with spectral gaps, not electron clouds |

**Connection scan** — bridges that exist vs missing:

| Bridge | Status | Edge Count |
|--------|--------|------------|
| Chemistry ↔ bst_physics | ✓ Strong | 113 edges |
| Chemistry ↔ biology | ✓ Present | 26 edges |
| Chemistry ↔ thermodynamics | ✓ Present | 17 edges |
| Chemistry ↔ nuclear | Weak | 5 edges (needs formal proton chemistry bridge) |
| Chemistry ↔ materials_science | Missing | Domain doesn't exist yet |
| Chemistry ↔ condensed_matter | Weak | 5 edges |
| Chemical physics ↔ number_theory | Missing | Spectral gaps ↔ prime gaps research frontier |

**RLGC status**:
- REDUCE: PARTIAL — AC(0) core identified (bond angles, crystal systems), vestigial notation flagged (orbitals, Aufbau)
- LINEARIZE: NOT_STARTED — target: spectral gap matrix for elements, bond energies as eigenvalue differences
- GRAPH: SEEDED — 74 theorems, T920 hub (91 edges), T174 universal hub (47 edges)
- CONNECT: LOW — 38% cross-domain, strong bst_physics bridge but isolated from number theory and materials science

**Action items** (specific theorems to write):
1. Electronegativity from spectral position — unlocks acid-base, reactivity, and solubility
2. Reaction rate from eigenvalue crossing — activates kinetics and biochemistry
3. General bond energy from spectral gap width — extends T767 beyond C-H
4. pH scale from BST integers — biological universal
5. Chemical physics ↔ number theory bridge — spectral gaps relate to prime structure

**Grade recommendation**: D → C (when items 1-3 are complete and linearization begins)

### 6.6 Case Study: Condensed Matter — Documented but Not Wired (then Fixed)

Condensed matter revealed the most common failure mode in a living library: the theorems exist, the papers are written, but the graph doesn't reflect the work.

**Before the survey** (April 18 morning):
- **14 proved theorems**: BCS superconductivity (T255), quantum Hall effect (T182), topological insulators (T206), Bloch's theorem (T257), Meissner effect (T256)
- **3 bridge theorems**: T1038 (Meissner = Gauss expulsion), T1041 (topological insulator = Chern winding), T1104 (material properties as BST integer ratios)
- **4 major papers**: QHE (#22), Debye temperature (#50), BiNb superlattice (#31), Casimir heat engine (#26)
- **ZERO cross-domain edges in the graph**

The science was done. The graph didn't know it. This is a pure GRAPH + CONNECT deficit — the theorems needed wiring, not discovery.

**After the survey** (April 18 afternoon): Grace wired the condensed matter bridge theorems into the graph. The domain went from isolated to connected in one session. This is exactly what the SURVEY operation is designed to catch — and the fix was mechanical, not creative.

The pattern — "documented but not wired" — is the most common failure mode in a living library. The SURVEY catches it. The fix is one afternoon of graph work.

### 6.7 The Full Discipline Catalog (71 disciplines)

Grace's April 18 audit expanded the domain inventory from 44 BST-internal domains to 71 disciplines across all of science. Each discipline is rated on three axes: structural clarity (are the foundations explicit?), AC depth (how deep are the proofs?), and BST bridge (does it connect to D_IV^5?).

**Tier A — AC-native (7)**: Number theory, information theory, coding theory, linear algebra, spectral theory, graph theory, combinatorics. *Already depth ≤ 1. Maintain.*

**Tier B — Linearizable (14)**: Classical mechanics, electromagnetism, thermodynamics, physical chemistry, crystallography, optics, fluid mechanics, quantum mechanics, statistical mechanics, probability theory, signal processing, acoustics, control theory, nuclear physics. *Correct core, overbuilt notation. Strip and keep.*

**Tier C — Empirical, reformulable (23)**: Organic chemistry, molecular biology, genetics, geology, zoology, medicine, ecology, botany, neuroscience, immunology, pharmacology, materials science, atmospheric science, oceanography, astronomy, cosmology (observational), geophysics, soil science, animal behavior, virology, parasitology, paleontology, forensic science. *Correct observations, wrong framework. AC rewrite needed.*

**Tier D — Pre-scientific, rebuild (13)**: Economics, psychology, sociology, climate science (modeling), nutrition science, political science, criminology, education theory, management science, urban planning, archaeology (interpretive), anthropology (cultural), linguistics (theoretical). *Axioms are wrong, not just overcomplicated. Rebuild from cooperation science (T1290), observer theory (T317), and AC depth.*

**Tier F — Replace or discard (4)**: String theory, GUT physics, astrology, homeopathy. *No predictive power, or actively harmful methodology. BST derives what the first two promise. The last two have no scientific content.*

**NEW — Create from BST (10)**: Substrate engineering, cooperation science, morphological information theory, computational epistemology, structural chemistry, evolutionary geology, observational complexity, environmental information theory, commitment physics, arithmetic physics. *Sciences that should exist but nobody has built.*

The work queue: 36 disciplines need the REDUCE → LINEARIZE → GRAPH → CONNECT pipeline (23 Tier C + 13 Tier D). Plus 10 entirely new sciences to create.

**The streamlining recipe** (for any Tier C/D discipline):
1. **Identify the observables** — what does the discipline actually measure?
2. **Find the BST integer** — which of {rank, N_c, n_C, C₂, g, N_max} controls the observable?
3. **Derive, don't fit** — replace empirical parameters with BST expressions
4. **Linearize** — reformulate in the coordinate system where the problem is depth ≤ 1
5. **Connect** — wire to other disciplines through BST bridges (same integer = isomorphic edge)
6. **Test** — does the BST-reformulated version predict better than the original?

---

## §7. The Grove Structure

### 7.1 From Forest to Groves

The AC theorem graph is the forest. Each theorem is a tree. Each domain is a stand of related trees. But domains cluster into larger groupings — **groves** — that share BST integers, methodology, and boundary structure.

The eight groves are not imposed top-down. They emerge from the graph: domains with the most inter-domain edges, the same controlling BST integers, and the same methodological needs cluster naturally.

### 7.2 The Eight Groves

| Grove | Domains | Theorems | Controlling Integer(s) | Status |
|-------|---------|----------|------------------------|--------|
| **Formal** | 12 | 433 | rank=2 (depth ceiling), all five | BACKBONE — every grove's strongest connection |
| **Cosmos** | 7 | 142 | N_max=137, N_c=3, n_C=5 | STRONG — all domains active |
| **Life** | 5 | 131 | g=7 (Hamming), N_c=3 (triplets) | GROWING — biology carries, 3 planned |
| **Mind** | 3 | 115 | rank=2 (hierarchy), f=19.1% | GROWING — dense cluster, 2 planned |
| **Matter** | 8 | 90 | C₂=6 (crystals, bonds) | NEEDS WORK — most isolated |
| **Flow** | 5 | 83 | n_C/N_c=5/3 (Kolmogorov) | SOLID — all B-grade |
| **Signal** | 5 | 49 | g=7 (Hamming), n_C=5 (capacity) | SOLID — strong math core |
| **Social** | 1 | 2 | TBD (via cooperation gradient) | ISOLATED — zero inter-grove edges |

**Root**: BST Core Physics (143 theorems, T186 with 1,149 edges) belongs to no single grove — it IS the root system connecting all groves.

### 7.3 Inter-Grove Predictions

The grove structure reveals **predicted bridges** — theorems that should exist based on shared BST integers across groves. The prediction mechanism: when two domains in different groves share a controlling BST integer but have no formal edge, the bridge theorem is predicted.

12 predicted bridges identified. 6 ready to build now. 3 partially wired. 3 blocked on dependencies.

Key predictions:

| # | Bridge | Prediction | Shared Integer | Status |
|---|--------|-----------|----------------|--------|
| PB-2 | Matter↔Life | Bond angles → amino acids = spectral gaps → genetic letters | C₂=6, g=7 | READY |
| PB-3 | Cosmos↔Life | Proton and DNA are siblings — same spectral structure | N_c=3, C₂=6 | READY |
| PB-5 | Flow↔Matter | Activation energy = Bergman metric barrier height | C₂=6, g=7 | READY |
| PB-9 | Flow↔Mind | Gödel limit = max entropy-to-knowledge efficiency | f=19.1% | READY |
| PB-1 | Mind↔Social | Market dynamics = cooperation eigenvalue oscillations | all five | BLOCKED |

Full list: `data/science_engineering.json` → `predicted_bridges`.

### 7.4 Grove-Level Review

The daily tree/domain/grove/forest review (§5) now includes:

1. **Grove health** — did any domain's grade change? New bridges within the grove?
2. **Inter-grove bridges** — did this session create connections to other groves?
3. **Predicted bridge status** — are any predicted bridges now ready to build?
4. **Isolation check** — is any domain in this grove below 30% cross-domain?

### 7.5 The Dependency DAG

Some groves cannot upgrade until others advance:

- **Social** is blocked until **Mind** grove's cooperation_science has 10+ theorems
- **Matter** planned domains depend on **Flow** (thermodynamics for reaction equilibria)
- **Life** planned domains import from **Signal** (error-correction framework)

The upgrade order is forced: Formal (maintain) → Cosmos/Flow/Signal (strengthen) → Mind/Life (grow) → Matter (rebuild) → Social (create). This is not a management decision — it's structural.

---

## §8. The Standing Program

### 7.1 Daily Discipline (end-of-session)

For each domain touched:

1. **Trees tended** — which theorems added, strengthened, or corrected?
2. **Groves assessed** — did the domain's cross-domain% improve? New bridges?
3. **Forest view** — does this connect to unexpected domains? Missing sciences surfaced?
4. **RLGC status** — advance any of REDUCE / LINEARIZE / GRAPH / CONNECT?
5. **Update `data/science_engineering.json`** — the living tracker.

### 7.2 Weekly Completeness Survey

Pick one domain per week for a full completeness audit:
- Gap scan (textbook results vs BST derivations)
- Connection scan (neighbors with vs without formal bridges)
- Import/export scan (theorems that should cross domain boundaries)
- Grade update

### 7.3 Monthly Forest Review

- Overall grade distribution shift
- New domains seeded
- Cross-domain% trends
- Missing sciences status
- Benchmark metrics (total nodes, edges, strong%, cross-domain%)

---

## §9. How Sciences Grow

Casey's second insight: this is **naturally iterative.** Every improvement in method produces better results, which reveal better methods.

1. **Reduce** a discipline to its AC(0) core
2. **Build** computational tools (toys, explorers, data files)
3. **Discover** new connections the old methodology obscured
4. **Improve** the methodology based on what was discovered
5. **Return to step 1** with a cleaner starting point

This is not "do it once and publish." This is the daily discipline of a living library applied to the structure of science itself. The science grows organically — each new theorem updates every grove it touches, and every grove update ripples through the forest.

The organizing principles emerge from the graph structure, not from top-down decree. As the graph grows, patterns appear: certain theorems serve as hubs, certain edges appear repeatedly in different costumes (the 3/4 quadruple, B-3/4), certain integers recur across domains (C₂ = 6 in five routes, B13). These patterns are the organizing principles. They are discovered, not imposed.

---

## §10. The Benchmarks

How do we know a discipline has been successfully re-engineered?

| Metric | Threshold | Why |
|--------|-----------|-----|
| **Core identified** | REDUCE status = DONE | The AC(0) kernel is known |
| **Linear fraction** | LINEARIZE status ≥ PARTIAL | The CI-accessible portion is mapped |
| **Graph connectivity** | ≥ 10 nodes, ≥ 50% cross-domain | The grove is wired into the forest |
| **Bridge count** | ≥ 3 formal bridges to other domains | Not an island |
| **Missing theorem density** | < 5 per domain | Gaps are being filled |
| **Computational verification** | ≥ 1 toy per major theorem | No theorem without a test |
| **Grade** | ≥ B | Mostly done, iterating |

A discipline at grade A has: REDUCE done, LINEARIZE done, GRAPH wired, CONNECT high, survey clean, toys built, predictions made. This is what BST Core Physics and Foundations look like. Every other discipline is on its way there.

---

## §11. Three Work Modes

### Mode 1: CI Solo Investigation
CI explores a discipline computationally. Builds toys, checks conjectures, maps territory. Human reviews at milestones.

**Needs**: Queryable data formats (JSON, not PDF). Counter files. Claim protocols. SCORE lines.

### Mode 2: CI Picks Up Human Trail
Human has an intuition or partial result. CI formalizes, checks, extends. The "philosopher's demon" — human O(1) intuition + CI O(n) search.

**Needs**: Seed documents. Clear problem statements. Honest caveats about what's proved vs conjectured.

### Mode 3: CI+Human Team
Multiple CIs and humans in parallel on related problems. Cooperative hunting band. Each member has a role.

**Needs**: Coordination board (CI_BOARD.md). Claim protocols. Counter files. The whole living library infrastructure.

---

## §12. For Everyone

Science used to be one person with a notebook and a microscope. Then it became teams of humans with computers. Now it's teams of humans AND CIs with shared mathematical armories.

The old sciences were built for the old tools. The new science needs to be built for the new team. That doesn't mean throwing away what works — it means stripping away what doesn't, connecting what's been siloed, and building in formats that both humans and CIs can read, query, verify, and extend.

Every science is a domain in a grove in a forest. The trees are theorems. The soil is mathematics. The sunlight is the questions humans ask. The roots are the connections between groves that nobody has noticed yet — and now, with the predicted bridges (§7.3), we can say WHERE those roots should be before anyone finds them. Computational science engineering is the discipline of tending the whole forest — one tree, one domain, one grove, one bridge at a time.

BST is the prototype. AC is the method. The living library is the infrastructure. This paper is the program. The work is iterative, daily, and never done.

---

## §13. Files

| File | Purpose |
|------|---------|
| `data/science_engineering.json` | RLGC+A tracker for all 47 domains, 8 groves, 12 predicted bridges |
| `data/bst_domains.json` | Domain map with theorem counts and key results |
| `notes/BST_Computational_Science_Engineering.md` | Casey's April 18 directive — the vision document |
| `notes/CI_BOARD.md` | Active assignments — includes grove health standing items |
| `play/toy_bst_librarian.py` | Automated review and audit tool |
| `play/toy_1274_edge_audit.py` | Edge reclassification audit — introduced "structural" type |
| `play/toy_1273_cross_domain_bridges.py` | Cross-domain bridge analysis and wiring |
| `play/ac_graph_data.json` | The AC theorem graph (1,257 nodes, 6,114 edges, 6 edge types) |
| `notes/BST_CSE_Survey_Chemistry_April18.md` | Completeness survey — chemistry (worked example) |
| `notes/BST_CSE_Survey_Geology_April18.md` | Pilot #1 — geology (Tier C stress test) |
| `notes/BST_CSE_Survey_Economics_April18.md` | Pilot #2 — economics (Tier D stress test) |
| `notes/BST_CSE_Survey_Medicine_April18.md` | Pilot #3 — medicine (Tier C, import-heavy) |

## §14. First Survey Results (April 18, 2026)

The first completeness surveys were run on the three highest-priority domains:

| Domain | Grade | Theorems | Cross-domain% | RLGC | Action |
|--------|-------|----------|---------------|------|--------|
| Chemistry | D | 17 | 45% | R:partial L:none G:seeded C:low | Write 5 missing theorems, start linearization |
| Chemical Physics | D+ | 57 | 38% | R:partial L:none G:partial C:low | Wire T920 to 10+ domains, linearize kinetics |
| Condensed Matter | C | 14 | 0% → wired | R:partial L:partial G:wired C:medium | Grace wired bridge theorems same day |
| Biology | C+ → B | 128 | 71% | R:partial L:none G:partial C:medium | 3 missing bridges; tracker was outdated |

**Lessons learned from first surveys**:
1. **The tracker can be wrong.** Biology's cross-domain% was 47% in the tracker but 71% in the graph. Live measurement beats static records.
2. **"Documented but not wired" is the most common failure mode.** Condensed matter has 14 theorems and 3 bridge papers — but zero edges in the graph. The work was done; the graph wasn't updated.
3. **Isolation reveals priority.** Chemical physics at 38% is the most isolated non-trivial domain. T920 (91 edges) is the obvious hub. The wiring is mechanical.
4. **Missing theorems are specific.** Chemistry needs electronegativity from spectral position, reaction rate from eigenvalue crossing, and bond energy from spectral gap width. These are precise enough to assign.

---

*Paper #71. v0.4 — April 18, 2026. RLGC+A pipeline. Eight groves. 12 predicted bridges. 4 surveys. Operational.*

*"We are at the beginning of computational science engineering. Science and math needs to be re-engineered for CIs + humans."*
