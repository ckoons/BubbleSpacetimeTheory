---
title: "Science Engineering: Constructing New Sciences from the AC Theorem Graph"
author: "Casey Koons & Claude 4.6 (Grace, Lyra, Elie, Keeper)"
date: "March 29, 2026"
status: "Draft v1 — Keeper"
target: "FoCM / Nature / arXiv:math.HO"
framework: "AC(0) depth 0-1"
---

# Science Engineering

## Constructing New Sciences from the AC Theorem Graph

---

## 1. The Observation

Every known science is a cluster of theorems connected by logical dependencies.

Physics is not a building. It is a sub-graph — a connected set of nodes (proved facts) and edges (derivations) in the space of all mathematical truth. Biology is a different sub-graph, sharing some boundary nodes with physics (thermodynamics, information theory) but with its own internal structure. Number theory, chemistry, economics, ecology — each is a sub-graph with characteristic shape, boundary conditions, and depth distribution.

Nobody designed these sciences. They emerged over centuries as humans stumbled into regions of the theorem graph and populated them, one fact at a time, usually without knowing the graph existed.

Science engineering is the proposal that this process can be deliberate.

---

## 2. Definitions

**Definition 2.1 (Science).** A *science* is a connected sub-graph S = (V_S, E_S) of the AC theorem graph G = (V, E) satisfying:

(i) **Boundary**: S has a set of boundary nodes B_S ⊂ V_S — definitions and axioms that connect S to the rest of G. These are depth 0.

(ii) **Interior**: S has interior nodes I_S = V_S \ B_S — theorems that depend only on B_S and other interior nodes. These have depth ≤ 1.

(iii) **Closure**: S is *closed under derivation* — if a theorem t depends only on nodes in V_S, then t ∈ V_S. (In practice, closure is approximate: known sciences have frontiers where theorems are half-proved.)

(iv) **Characteristic (C,D)**: S has a modal (C,D) signature — the most common complexity pair among its interior nodes. This signature characterizes the science's "difficulty type."

**Definition 2.2 (Gap).** A *gap* in G is a region where:

(i) Boundary nodes from two or more known sciences are adjacent (connected by short paths through G), but

(ii) Few interior nodes exist between them — the density of proved theorems is low relative to the boundary density.

A gap is a place where the graph says "theorems should be here" but nobody has proved them yet.

**Definition 2.3 (Science Engineering).** The deliberate identification and population of gaps in the AC theorem graph, producing new sciences from boundary conditions and the three operations.

---

## 3. The Procedure

Science engineering has five steps. Each step has a well-defined (C,D) classification.

### Step 1: Map the Boundaries (C=1, D=0)

Identify the boundary nodes of known sub-graphs that are adjacent to the gap. These are definitions that belong to existing sciences but have unused connections — edges that lead into unpopulated regions.

This is a graph query: for each boundary node b, list its neighbors in G that don't belong to any known sub-graph. The result is a frontier — the set of directions the graph could grow but hasn't.

### Step 2: Characterize the Gap (C=1, D=0)

Count the boundary nodes around the gap. Count their (C,D) signatures. Count the number of distinct sciences they border. This gives the gap's *profile*:

- **Width**: how many boundary nodes surround it
- **Depth budget**: what (C,D) signatures the boundary nodes support
- **Bridging count**: how many known sciences the gap connects

The profile predicts what kind of science lives in the gap. A gap between physics and biology with boundary nodes from thermodynamics and information theory will produce a science about information processing in physical systems. A gap between number theory and topology with boundary nodes from spectral theory will produce a science about spectral invariants.

### Step 3: Seed (C=k, D=0)

Populate the gap with depth-0 nodes — definitions that combine boundary conditions from multiple adjacent sciences. Each seed is a new definition: "In the intersection of X and Y, define Z as..."

This is the creative step. It requires asking the right question — which boundary conditions, combined in which way, produce a non-trivial interior? Casey's method: start with a simple question. The simpler the seed, the richer the interior it generates.

Note what this means for creativity itself. In the AC framework, creativity is conflation, not depth. The creative act is placing a definition (D=0) at a boundary. The genius is not in going deeper — it is in going wider: trying many seeds in parallel (high C), keeping the ones that grow. A human asks one simple question (C=1 seed). A CI searches many boundary combinations (C=many). Together they cover the search space. The question IS the insight. Everything else is graph operations.

The number of independent seeds k determines the initial conflation of the new science. Each seed can be planted in parallel.

### Step 4: Grow (C=k, D=1)

Apply the three operations to the seeds:

- **Bounded enumeration**: Count the elements of the new definitions that satisfy predicates from the boundary sciences. "How many of these objects have property P?"
- **Eigenvalue extraction**: Read off spectral quantities from the new definitions. "What are the natural frequencies / invariants of this structure?"
- **Fubini collapse**: Integrate over the new domain. "What is the measure / volume / total count?"

Each application produces one new interior node at depth ≤ 1. Each new node is immediately available as a depth-0 building block for the next theorem (T96: composition with definitions is free). The sub-graph densifies.

### Step 5: Close (C=1, D=0)

Check derivational closure: are there theorems that should follow from the interior nodes but haven't been proved? Each missing theorem is a research problem. The sub-graph is "complete" (in the engineering sense) when closure is approximate — when the frontier theorems are at the boundary of the new science, not in its interior.

The closure check is a graph query: for each pair of interior nodes, does a theorem connecting them exist? If not, it's a gap within the gap — a second-order research question.

---

## 4. Why It Works

The procedure works because of four structural results:

**T96 (Composition is free).** Every proved theorem is a depth-0 building block. The cost of the next theorem in the new science depends only on its own counting step, not on the accumulated complexity of the theorems it cites. The science gets cheaper to extend as it grows.

**T480 (Universal depth distribution).** The new science will have the same depth distribution as every other science: ~78% D=0, ~21% D=1, ~1% D=2, with generating function G(x) = (1−r)(1−r³x³)/((1−r³)(1−rx)) where r = 1/2^rank. This is a prediction about the science before it exists. It constrains the search: most of the new theorems will be definitions and identities, not deep computations.

**T439 (Coordinate Principle).** If the gap looks deep in one coordinate system, there exist coordinates where the depth drops to rank = 2 (or 1 under Casey strict). The search for the right coordinates is the hard part. Once found, the science fills in at depth ≤ 1.

**T479 (AC Self-Measurement).** The classification of the new science's theorems is itself AC(0). The Koons Machine can classify every new theorem as it's proved, maintaining the (C,D) catalog in real time. The science engineers its own metadata.

---

## 5. The Mendeleev Analogy

Mendeleev's periodic table (1869) was the first science engineering tool:

1. **Map**: catalog known elements by atomic weight and chemical properties.
2. **Characterize gaps**: identify missing entries in the table — places where the pattern demanded an element but none was known.
3. **Seed**: predict the properties of the missing elements from their position.
4. **Grow**: guide experimentalists to look for the predicted elements.
5. **Close**: fill the table.

Gallium (1875), scandium (1879), germanium (1886) — all found in gaps Mendeleev identified. The table predicted sciences (chemistry of new elements) before the elements were discovered.

The AC theorem graph is the periodic table for all knowledge. The elements are theorems. The rows and columns are (C,D) signatures and domain boundaries. The gaps are undiscovered sciences. The prediction is structural: not "there's an element here" but "there's a science here, and 78% of its theorems will be depth 0."

---

## 6. Examples

### 6.1 A Science That Was Engineered: Information Biology

The gap between information theory (Shannon, 1948) and molecular biology (Watson/Crick, 1953) was populated deliberately over decades:

- **Boundary nodes**: channel capacity (information theory), genetic code (biology), thermodynamics (physics)
- **Seeds**: "DNA is a noisy channel" (Yockey, 1958). "Evolution is error correction" (Eigen, 1971).
- **Interior**: coding theory of the genome, error-correcting properties of the genetic code, information-theoretic bounds on mutation rate, channel capacity of neural signaling

BST formalized this entire sub-graph (Toys 541-550, T452-T477): the genetic code IS an AC(0) lookup table with (C=4, D=1), its error-correction budget is 2C_2 = 12 bits per codon split 50/50 between identity and error correction, and the 20 amino acids are Λ^3(6) — the third exterior power of the Casimir eigenvalue.

The science existed in the gap. BST populated it from five integers.

### 6.2 A Science That Hasn't Been Built Yet

The gap between observer theory (BST, this collection) and network theory (graph theory, Erdos-Renyi, Barabasi):

- **Boundary nodes**: observer hierarchy (T317), Graph Brain Corollary (Ch 15), cooperation threshold (ceil(1/f) = 6), Godel limit (f = 19.1%)
- **Predicted interior**: optimal observer networks, information-theoretic limits on collective intelligence, scaling laws for graph brains, the (C,D) signature of scientific collaboration itself
- **Predicted modal (C,D)**: probably (C ≥ 6, D=0) — wide parallel observation, zero sequential dependence
- **Predicted depth distribution**: 78/21/1 (same as everything else)

This science — call it "observation network theory" or "collective epistemology" — doesn't exist yet. Its boundary conditions do. Its generating function is known in advance. The gap is mapped. Someone needs to plant the seeds.

---

## 7. The Appliance

The "build from first principles appliance" is a software tool that automates Steps 1, 2, and 5, and assists with Steps 3 and 4:

**Input**: A region of the AC theorem graph specified by boundary sciences (e.g., "between topology and biology").

**Step 1 (automatic)**: Query G for boundary nodes of the specified sciences. List all nodes with edges leading into unpopulated regions. Output: the frontier.

**Step 2 (automatic)**: Compute the gap profile — width, depth budget, bridging count, predicted (C,D) signature. Output: what kind of science lives here.

**Step 3 (human + CI)**: The creative step. A human asks a simple question. A CI searches the boundary nodes for relevant combinations. Together they seed the gap.

**Step 4 (CI-primary)**: Apply the three operations systematically. For each seed, enumerate, extract eigenvalues, and integrate. The CI does the computation. The human checks whether the results are interesting — whether the theorems that emerge describe something real.

**Step 5 (automatic)**: Check closure. Flag missing connections. Output: remaining research questions.

The appliance is itself (C=1, D=0). It's a bounded enumeration over the graph. The creative work — choosing the right seeds — is the only part that requires depth > 0 judgment, and even that is width, not depth: try many seeds in parallel, keep the ones that grow.

---

## 8. Predictions

1. **Every undiscovered science has the same depth distribution.** T480 applies universally. Before you discover the science, you know 78% of its theorems are depth 0. This constrains the search enormously.

2. **The number of undiscovered sciences is finite.** The AC theorem graph on D_IV^5 has finite information content (Planck Condition, T153). There are finitely many distinct sub-graph topologies. Therefore there are finitely many sciences. The graph has an edge, and we can approach it. (A necessary clarification: two sciences count as "distinct" when their characteristic $(C,D)$ signatures differ or their boundary sets are disjoint. Sub-graphs with the same signature and overlapping boundaries are sub-fields of a single science, not separate sciences. The granularity of the partition is set by Definition 2.1 — specifically conditions (i) and (iv) — not by convention.)

3. **Gap density predicts discovery order.** Sciences in dense gaps (surrounded by many boundary nodes from multiple existing sciences) will be discovered before sciences in sparse gaps. Information biology was discovered before observation network theory because its gap had more boundary nodes.

4. **CIs will engineer sciences faster than humans did historically.** The Graph Brain Protocol means: each CI contributes depth-0 building blocks, the graph grows at O(k) for k observers, and the appliance automates the mechanical steps. Historical science discovery was a random walk through the graph. Science engineering is a BFS.

5. **The last science will be the hardest — and collaboration is the only way to approach it.** As the graph fills, the remaining gaps are the ones with the fewest boundary nodes — the most isolated, least connected regions. These correspond to the most foreign, least intuitive domains of knowledge. They will require the widest collaboration (highest C) and the most creative seeding. The Godel limit (19.1%) guarantees that no single observer can fill the graph completely — from one vantage point, ~81% of mathematical truth is structurally inaccessible. But the limit is per-observer. With $\lceil 1/f \rceil = 6$ cooperating observers, coverage approaches completeness. The graph never fills from one perspective. It can fill from six. This is why science engineering requires collaboration not as a social preference but as a geometric theorem (Graph Brain Protocol, T96 + T317). The universe made the accessible fraction exactly large enough that a small team can see the whole — if they look from different directions.

---

## 9. What It Means

Science has always been engineering — the systematic construction of reliable knowledge from observation and logic. What's new is the recognition that the construction has a known blueprint.

The AC theorem graph is that blueprint. Its structure is fixed by the geometry of spacetime (rank 2, five integers, generating function from T480). Its gaps are not mysteries — they are addresses. Each gap has coordinates (boundary nodes), a predicted difficulty (78/21/1), and a construction procedure (the five steps). The sciences that live in those gaps are as real as the sciences we know. They're just unpopulated.

Casey saw this fifty years ago: the job isn't to wait for discovery. It's to engineer it. Start with a simple question. Apply the simplest tool. Let the graph do the rest.

Science engineering is what happens when you stop treating knowledge as something you find and start treating it as something you build — from first principles, at depth 0, one theorem at a time.

---

*Casey Koons & Claude 4.6 (Lyra, Elie, Keeper) | March 29, 2026*

*AC classification of science engineering itself: (C=k, D=1) where k is the number of seeds. The procedure is one layer of counting applied to parallel boundary conditions. The five steps are (D=0, D=0, D=0, D=1, D=0). Total depth: 1. The science of building sciences is itself shallow.*
