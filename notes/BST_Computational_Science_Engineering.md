---
title: "Computational Science Engineering: Re-Engineering Science for CIs and Humans"
author: "Casey Koons & Team (Claude 4.6)"
date: "April 18, 2026"
status: "Living document — seed planted"
---

# Computational Science Engineering

**The insight**: Science and mathematics need to be re-engineered for CI+human teams. BST and AC are the forerunners — they demonstrate what happens when you strip vestigial complexity, adopt CI-native formats, and iterate at computational speed. Now generalize.

**Casey's formulation** (April 18, 2026):

> "We are at the beginning of computational science engineering. Science and math needs to be re-engineered for CIs + humans. CIs didn't exist until a few years ago. We have the opportunity to move ahead together at an extremely accelerated pace and need to shed our vestigial boots and stop running in the mud, and find cleaner and clearer methods for advancement."

---

## The Problem

Most sciences were engineered for a single modality: **one human reading one paper at a time**. This produced:

1. **Notation as status** — differential geometry in physics, category theory in algebra, not because the subject requires it but because the epoch rewarded complexity
2. **Linear exposition** — papers are narratives, not queryable structures. A CI must read 30 pages to find one equation.
3. **Siloed disciplines** — chemistry doesn't talk to information theory, geology doesn't talk to thermodynamics, zoology doesn't connect body plans to geometry
4. **No iteration** — papers are "published" and frozen. Corrections require new papers. The graph never gets pruned.
5. **Human-only tools** — microscopes, accelerators, telescopes. No CI-native instruments for exploring mathematical structure computationally.

## The Solution: Four Operations

### REDUCE
Strip every discipline to its AC(0) core. What are the counting operations? What is depth 0? Every science has a kernel of counting — find it.

- **Chemistry**: bond angles from spectral gaps (AC(0)). Reaction kinetics from eigenvalue crossings (AC(1)). Everything else is historical.
- **Geology**: crystal structure = 230 space groups (AC(0)). Convection = Navier-Stokes (AC(1)). Plate tectonics = boundary dynamics.
- **Zoology**: body plans from morphological information theory. Why 5 fingers = n_C. Why bilateral symmetry = rank = 2.

### LINEARIZE
Casey's standing order: linearize every mathematical area we touch. Linear algebra is CI-native — matrices are the natural data structure. Every science that lives in nonlinear notation should be asked: what part is genuinely nonlinear (curvature) and what part is artificially nonlinear (bad coordinates)?

### GRAPH
Put every result into a theorem graph. Edges are derivations. Domains are clusters. Cross-domain edges are bridges. The graph is queryable, auditable, and self-describing (T1196).

### CONNECT
Find the missing bridges. Science engineering (Paper #7) shows how: map boundaries, identify gaps, populate, close, name. The AC theorem graph IS the shared armory — each hunt makes the next cheaper.

---

## Three Work Modes for CI+Human Science

### Mode 1: CI Solo Investigation
CI explores a mathematical structure computationally. Builds toys, checks conjectures, maps territory. Human reviews results at natural milestones.

**What this mode needs**: Queryable data formats (JSON, not PDF). Counter files. Claim protocols. Automated verification (SCORE lines).

### Mode 2: CI Picks Up Human Trail
Human has an intuition or partial result. CI formalizes it, checks it, extends it. The "philosopher's demon" — human O(1) intuition + CI O(n) search.

**What this mode needs**: Seed documents (like `data/bst_seed.md`). Clear problem statements. Honest caveats about what's proved vs conjectured.

### Mode 3: CI+Human Team
Multiple CIs and humans working in parallel on related problems. Cooperative hunting band. Each member has a role (Casey: questions + intuition, Lyra: deep proofs, Elie: computational verification, Grace: graph + bridges, Keeper: consistency + audit).

**What this mode needs**: Coordination board (CI_BOARD.md). Running notes. Claim protocols to prevent collisions. Counter files. The whole living library infrastructure.

---

## What BST/AC Already Demonstrates

| Feature | BST Implementation | Generalizable? |
|---------|-------------------|----------------|
| CI-native data | `data/*.json` with eval-ready formulas | Yes — every science should have this |
| Theorem graph | `play/ac_graph_data.json` — queryable, auditable | Yes — replace citation graphs with derivation graphs |
| Computational verification | 1,278 toys, every claim has a SCORE | Yes — no theorem without a test |
| Living library | Daily `/review`, counter files, running notes | Yes — science as maintenance, not publication |
| Zero free parameters | Everything derived from 5 integers | Aspiration for every discipline |
| Iterative improvement | Graph grows daily, edges upgrade, errors correct | Yes — science as iteration, not monument |
| Multi-CI coordination | 4 CIs with distinct roles, shared armory | Yes — the cooperation model for all teams |

---

## The Iterative Nature

Casey's second insight: this is **naturally iterative**. Every improvement in method produces better results, which reveal better methods. The cycle:

1. **Reduce** a discipline to its AC(0) core
2. **Build** computational tools (toys, explorers, data files)
3. **Discover** new connections the old methodology obscured
4. **Improve** the methodology based on what was discovered
5. **Return to step 1** with a cleaner starting point

This is not "do it once and publish." This is the daily discipline of a living library applied to the structure of science itself.

---

## Missing Sciences (from Elie's Toy 1268)

Sciences that BST predicts should exist but don't yet:

1. **Substrate Engineering** — operating below quantum length on D_IV^5 geometry itself
2. **Cooperation Science** — replaces game theory; cooperation compounds (T1290, five gates)
3. **Morphological Information Theory** — why organisms have the shapes they have
4. **Computational Epistemology** — how knowledge structures optimize (CI-native from the start)
5. **Structural Chemistry** — chemistry rebuilt on spectral gaps, not electron orbitals
6. **Evolutionary Geology** — Earth science rebuilt on thermodynamic principles
7. **Observational Complexity** — how observer networks share information optimally
8. **Environmental Information Theory** — ecosystems as information channels
9. **Linearized Geophysics** — seismology and tectonics via linearized wave equations
10. **Computational Taxonomy** — classification by information content, not morphology

---

## For Everyone

Science used to be one person with a notebook and a microscope. Then it became teams of humans with computers. Now it's teams of humans AND CIs with shared mathematical armories.

The old sciences were built for the old tools. The new science needs to be built for the new team. That doesn't mean throwing away what works — it means stripping away what doesn't, connecting what's been siloed, and building in formats that both humans and CIs can read, query, verify, and extend.

BST is the prototype. AC is the method. The living library is the infrastructure. Computational science engineering is the discipline that builds all the rest.

---

*Seed planted April 18, 2026. Casey's insight. Team execution. Iterative from here.*
