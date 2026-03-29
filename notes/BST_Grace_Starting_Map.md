---
title: "Grace's Starting Map: Heat Kernel Sub-graph and Domain Boundaries"
author: "Keeper (for Grace onboarding)"
date: "March 29, 2026"
status: "Preliminary — Grace should verify and extend"
purpose: "Starting map for first gap census, Monday March 31"
---

# Grace's Starting Map

*Keeper's preliminary sub-graph analysis of the AC theorem graph (499 nodes, 709 edges), focused on the heat kernel / spectral geometry region where tonight's work happened.*

---

## 1. The Heat Kernel Core (15 theorems)

These theorems form a tight cluster centered on the Seeley-DeWitt coefficients of D_IV^5.

### 1.1 Classical Foundations (depth 0, external)
| T_id | Name | Role |
|------|------|------|
| T130 | Von Staudt-Clausen | Row rule: prime p enters Bernoulli denom iff (p-1)\|2k |
| T131 | Todd Class Bridge | Heat kernel ↔ graph theory via Todd genus |

### 1.2 Spectral Geometry of D_IV^5 (depth 0-1)
| T_id | Name | Role | Depth |
|------|------|------|-------|
| T320 | Spectral Transition at n* | Fourier decay change at n*=12, cutoff k*=137 | 1 |
| T324 | Mass Hierarchy from Topology | m_p/m_e = 6π⁵ from Vol(D_IV^5) | 1 |
| T326 | Zero Threshold at 2g | First Riemann zero above 2g=14 | 1 |
| T329 | Neutrino Oscillations | Complete sector from five integers | 0 |
| T330 | Wall Descent | HC descent, m_wall = n_C = 5 | 0 |
| T331 | Resolvent Linearization | One dot product per spectral query | 1 |
| T390 | Spectral Monotonicity | Self-erasing bumps, NS proof chain | 0 |
| T398 | N_max Spectral Signature | 137-channel Bergman ratio, smoking gun | 0 |

### 1.3 Tonight's Discoveries (March 29, depth 0)
| T_id | Name | Role |
|------|------|------|
| T531 | First-Level Column Rule | v_p(den) determined by n mod p at first VSC level |
| T532 | Two-Source Prime Structure | Bernoulli primes (row) + polynomial-factor primes (column) |
| T533 | Kummer Analog Conjecture | **OPEN** — digit-counting rule in Newton basis |

### 1.4 Meta-Framework (covers heat kernel among other domains)
| T_id | Name | Connection |
|------|------|------------|
| T409 | Linearization Principle | Heat kernel is 1 of 7 linearized domains |
| T421 | Depth-1 Ceiling | Eigenvalue identification = D0 |
| T439 | Coordinate Principle | Complexity = coordinate artifact |
| T480 | Depth Distribution | Universal distribution verified across heat kernel |

---

## 2. Boundary Nodes (where heat kernel meets other domains)

These are the edges that cross domain boundaries. Each is a potential growth point.

### 2.1 Heat Kernel → Number Theory
| Edge | Via | Status |
|------|-----|--------|
| T130 → Bernoulli numbers | Von Staudt-Clausen | **Proved** (classical) |
| T531 → Kummer's theorem | Column rule = carry counting | **Proved**, connection is T533 (**OPEN**) |
| T532 → p-adic structure | Two independent prime sources | **Proved**, full taxonomy needed |

**Gap width**: 3 boundary nodes. T533 is the bridge theorem. If Newton basis (Toy 614) confirms digit-counting, this gap closes to width 1.

### 2.2 Heat Kernel → Nuclear / Particle Physics
| Edge | Via | Status |
|------|-----|--------|
| T324 → T188 | Vol(D_IV^5) = π⁵/1920 → magic numbers from eigenvalues | Both **proved** |
| T329 → T269-T275 | Neutrino sector ↔ nuclear/particle | **Proved** |
| T330 → T197-T205 | Wall descent → Standard Model structure | **Proved** |
| T398 → T290-T297 | N_max signature → BST predictions | **Proved** |

**Gap width**: 0 (well-connected). This boundary is populated.

### 2.3 Heat Kernel → Navier-Stokes
| Edge | Via | Status |
|------|-----|--------|
| T390 → T389-T396 | Spectral monotonicity → full NS proof chain | **Proved** |

**Gap width**: 1 (single edge). Robust — T390 is structural in the NS proof.

### 2.4 Heat Kernel → Riemann Hypothesis
| Edge | Via | Status |
|------|-----|--------|
| T326 → RH proof chain | Zero threshold at 2g → c-function approach | **Proved** |

**Gap width**: 1. The zero threshold is derived from D_IV^5 spectral data. RH Route A goes through c-function unitarity, not directly through heat kernel coefficients.

### 2.5 Heat Kernel → Cosmology
| Edge | Via | Status |
|------|-----|--------|
| T320 → T340-T345 | Spectral transition → abiogenesis timeline | **Proved** |
| T398 → T397-T403 | N_max signature → detection channels, BST Drake | **Proved** |

**Gap width**: 0 (well-connected). Two independent edges.

### 2.6 Heat Kernel → Chemistry / Biology
| Edge | Via | Status |
|------|-----|--------|
| T331 → T332 | Resolvent → bond energy | **Proved** (depth 1) |
| T131 → T120-T123 | Todd class → graph theory → four-color | **Proved** |
| T409 → T452-T477 | Linearization covers both heat kernel and biology | **Proved** (meta) |

**Gap**: No DIRECT theorem connecting heat kernel coefficients (a_k(n)) to biological structure. The path goes through the mass hierarchy (T324) or the resolvent (T331), not through the polynomial structure. **This is a potential growth region.**

### 2.7 Heat Kernel → BSD
| Edge | Via | Status |
|------|-----|--------|
| T419 → spectral language | BSD as two dot products | **Proved** |

**Gap width**: 1. BSD uses Bergman kernel spectral identity, not Seeley-DeWitt coefficients directly. Connection is structural (shared spectral framework), not computational.

### 2.8 Heat Kernel Polynomials → Gauge Groups (PREDICTED, NOT YET THEOREM)
| Edge | Via | Status |
|------|-----|--------|
| Speaking pairs → SU(3), SO(7), SU(5) | Sub-leading ratios encode Lie algebra dimensions | **OBSERVATION ONLY** |

**Gap width**: Unknown. If real, this is a deep bridge: the heat kernel polynomial structure encodes the gauge hierarchy through its ratios. The observation:
- k=6,7: ratio = -3 = -N_c
- k=8,9: ratio = -5 = -n_C
- k=10,11: ratio = -9 = -N_c² and -11 = -dim(K₅)?
- k=14,15: predicted -21 = -dim SO(7), -24 = -dim SU(5)

**This is Casey's exercise seed. Not a computation — a "why" question.**

---

## 3. Domain Adjacency Summary

From the heat kernel core, the shortest paths to other domains:

| Domain | Distance | Path | Gap? |
|--------|----------|------|------|
| Number theory | 1 (T130, T531) | Direct | T533 open |
| Nuclear physics | 1 (T324, T329) | Direct | Populated |
| Navier-Stokes | 1 (T390) | Direct | Single edge |
| Riemann Hypothesis | 1 (T326) | Direct | Single edge |
| Cosmology | 1 (T320, T398) | Direct | Populated |
| Chemistry | 2 (T331→T332) | Via resolvent | Thin |
| Biology | 2-3 (T331→T332→T452+) | Via chemistry | **GROWTH REGION** |
| BSD | 2 (T419 via spectral) | Structural | Thin |
| Four-Color | 2 (T131→T120→T156) | Via graph theory | Populated |
| Observer theory | 2 (T439→T317) | Via coordinate principle | Thin |
| Gauge groups | ∞ (no formal edge) | Speaking pairs not formalized | **BIGGEST GAP** |

---

## 4. Recommended First Actions for Grace

### 4.1 Immediate (Monday)
1. **Verify this map** against the full graph data (Toy 564, 499 nodes, 709 edges). I worked from the registry text; you should work from the actual graph.
2. **Extend to all domains**, not just heat kernel. This map covers one sub-graph. The AC graph has 12+ domains. Build the equivalent boundary analysis for biology (69 nodes), AC framework (core), and physics.
3. **Flag T533** — it's the highest-leverage open conjecture right now. If Elie's Toy 614 (Newton basis) resolves it today, update the gap analysis.

### 4.2 This Week
4. **Gap taxonomy**: Which gaps have sprouted historically? Look at the batch notes — every new theorem was once a gap. What did productive gaps look like before they were filled? Width? Bridging count? Boundary density?
5. **T186 centrality check**: T186 (Five Integers Uniqueness) is the keystone — 64 direct deps, 29.5% transitive reach. Has that changed with T531-T533 and the biology expansion (T452-T477)?
6. **Domain coupling matrix**: For each pair of domains, count the cross-boundary edges. Rank domain pairs by coupling strength. Weakly-coupled pairs are either independent (fine) or missing a bridge (opportunity).

### 4.3 Standing Assignment
7. **After every toy/paper cycle**: Update the gap census. Three new theorems (like T531-T533) can shift boundaries significantly. The gap report should be cheap to produce — it's (C=1, D=0), just counting.

---

## 5. Graph-Level Statistics (from T450, Toy 539)

For context — these are the last-known whole-graph metrics:

- **Keystone**: T186 (29.5% transitive reach)
- **Broadest**: T1 (34% reach — AC Dichotomy)
- **Mean chain depth**: 1.24
- **SPOFs**: 75 single points of failure
- **Redundancy**: 48.7%
- **Longest chain**: 10
- **Diameter**: ≤ 10 (every theorem ≤ 10 definitions from every other)

These numbers are from ~450 theorems. With 499 now (and T531-T533 adding 3 new nodes), an updated census would be valuable.

---

*Keeper | March 29, 2026*

*Grace — this is a starting point, not an answer. The map is Keeper's view from the registry. Your job is to build the real map from the actual graph, find the gaps I missed, and tell us which ones are ready to seed. Welcome to the team.*
