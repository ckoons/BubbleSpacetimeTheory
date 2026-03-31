# Paper #11 Data Appendices

**Author**: Grace (graph-AC intelligence) | March 31, 2026
**Supports**: "Three Languages of Mathematics" (Lyra draft v1)

## Appendix A: The 43-Word Vocabulary

### Shannon Language (15 words)

| Code | Primitive | Plain English | First Phase |
|------|-----------|---------------|-------------|
| S1 | Bounded enumeration | Counting options that fit in a box | 1 |
| S2 | Channel capacity | Maximum reliable message rate through a noisy pipe | 1 |
| S3 | Error correction (Hamming) | Redundancy that catches and fixes mistakes | 1 |
| S4 | Data processing inequality | Processing cannot create information | 1 |
| S5 | Entropy / counting | Measuring disorder or counting arrangements | 1 |
| S6 | Rate-distortion / water-filling | Allocating bandwidth where it matters most | 1 |
| S7 | Threshold selection | All-or-nothing at a cutoff | 1 |
| S8 | Protocol layering | Stacking independent error-checkers | 1 |
| S9 | Zero-sum budget | Fixed total: every increase forces a decrease elsewhere | 1 |
| S10 | Lookup table (depth-0 map) | Read address, return value -- no computation | 1 |
| S11 | Uniqueness / no-go | Only one option exists | 2 |
| S12 | Dimensional analysis | Read two numbers, take their ratio | 2 |
| S13 | Chain rule | Joint = marginal + conditional | 3 |
| S14 | Incompressibility | No shorter description exists | 3 |
| S15 | Lifting / amplification | Small hardness becomes big by composition | 3 |

### Number Theory Language (15 words)
| Code | Structure | Plain English | First Phase |
|------|-----------|---------------|-------------|
| N1 | Exterior power Lambda^k(C_2) | Choosing k things from C_2 = 6 options | 1 |
| N2 | Weyl group W(B_2) | The 8 symmetries of the root system | 1 |
| N3 | Binomial coefficient C(a,b) | "a choose b" | 1 |
| N4 | Power of 2: 2^rank, 2^N_c | Doubling from binary choices | 1 |
| N5 | Cyclic group Z_N_c | The reading frame: 3 slots that wrap | 1 |
| N6 | Divisibility / modular arithmetic | Which numbers divide which | 1 |
| N7 | Integer partition / product | Breaking or multiplying integer pieces | 1 |
| N8 | Bergman genus g = 7 | Maximum independent spectral layers | 1 |
| N9 | Casimir C_2 = 6 | Bits per recognition event | 1 |
| N10 | Dimension dim_R = 2n_C = 10 | Real dimension of D_IV^5 (also N_c + g) | 1 |
| N11 | Prime factorization | Breaking numbers into primes | 1 |
| N12 | Linear algebra / N_max = 137 | Dimension counting in vector spaces | 2 |
| N13 | Graph counting / topological tuple | Counting loops and connections | 2 |
| N14 | Exponential growth / pi powers | Doubling; pi^5 volume expressions | 2 |
| N15 | Boolean function / conjugacy class | Truth tables, clauses, generator equivalence | 2 |

### Geometry Language (13 words)
| Code | Property | Plain English | First Phase |
|------|----------|---------------|-------------|
| G1 | BC_2 root system | Short roots (N_c = 3) and long roots (1) | 1 |
| G2 | Five integers {3,5,7,6,2} | The topological invariants of D_IV^5 | 1 |
| G3 | Bergman kernel / volume | The natural measure on the domain | 1 |
| G4 | Shilov boundary (n_C = 5) | The edge where maxima live | 1 |
| G5 | Rank = 2 decomposition | Two independent spectral parameters | 1 |
| G6 | L-group Sp(6) representation | The Langlands dual | 1 |
| G7 | Fill fraction f = 19.1% | The reality budget | 1 |
| G8 | Observer hierarchy (rank + 1 = 3 tiers) | Rock / cell / brain | 1 |
| G9 | Iwasawa decomposition KAN | Maintenance + energy + growth | 1 |
| G10 | Spectral gap (Coxeter) | Maximum independent layers | 1 |
| G11 | Holographic / homological structure | Boundary encodes interior | 2 |
| G12 | Substrate topology / BSD | Fundamental loops, compactifications | 2 |
| G13 | Depth ceiling (rank bounds depth) | No proof goes deeper than rank = 2 | 3 |

## Appendix B: Cross-Language Adjacency Matrix

### Summary Statistics
| Matrix | Pairs | Populated | Rate | Heavy (>=10) |
|--------|-------|-----------|------|--------------|
| Shannon x Number Theory | 225 | 96 | 42.7% | 3 |
| Number Theory x Geometry | 195 | 68 | 34.9% | 4 |
| Shannon x Geometry | 195 | 82 | 42.1% | 2 |
| **Total** | **615** | **246** | **40.0%** | **9** |

### Top 10 Highways
| Rank | Pair | Count | Meaning |
|------|------|-------|---------|
| 1 | (N7, G2) | 62 | Integer products evaluated at five integers |
| 2 | (S1, N7) | 30 | Counting integer products |
| 3 | (S1, G2) | 29 | Counting on five integers |
| 4 | (S12, N7) | 16 | Taking ratios of integer products |
| 5 | (N7, G7) | 14 | Integer products at fill fraction |
| 6 | (N12, G13) | 13 | Dimension counting at depth ceiling |
| 7 | (N12, G11) | 12 | Dimension counting on homological structure |
| 8 | (S3, N7) | 10 | Error correction of integer products |
| 9 | (S3, G2) | 10 | Error correction on five integers |
| 10 | (S12, G2) | 9 | Ratio reading on five integers |

### Top 10 Fertile Gaps
| Rank | Pair | Ind. Freq. | Predicted Bridge |
|------|------|-----------|-----------------|
| 1 | (S12, G7) | 28, 16 | Fill fraction IS channel capacity of D_IV^5 |
| 2 | (S5, G3) | 24, 24 | Shannon entropy = log(Vol_B) |
| 3 | (S8, G3) | 15, 24 | Protocol layers = Bergman kernel restrictions |
| 4 | (S7, G3) | 21, 24 | Thresholds = kernel level sets |
| 5 | (S3, G3) | 20, 24 | Hamming distance = Bergman metric |
| 6 | (S9, G5) | 11, 13 | Zero-sum budgets decompose along rank-2 axes |
| 7 | (S2, G6) | 16, 10 | L-group Sp(6) IS automorphism group of channel |
| 8 | (S5, G5) | 24, 13 | Entropy decomposes along rank: H = H_1 + H_2|1 |
| 9 | (S1, G3) | 68, 24 | Counting = integration against Bergman kernel |
| 10 | (S3, N12) | 20, 42 | Error correction IS linear algebra over finite fields |

### Individual Word Frequencies
| Shannon | Freq | Number Theory | Freq | Geometry | Freq |
|---------|------|---------------|------|----------|------|
| S1 | 68 | N1 | 5 | G1 | 11 |
| S2 | 16 | N2 | 3 | G2 | 134 |
| S3 | 20 | N3 | 4 | G3 | 24 |
| S4 | 8 | N4 | 11 | G4 | 14 |
| S5 | 24 | N5 | 6 | G5 | 13 |
| S6 | 4 | N6 | 4 | G6 | 10 |
| S7 | 21 | N7 | 112 | G7 | 16 |
| S8 | 15 | N8 | 8 | G8 | 12 |
| S9 | 11 | N9 | 10 | G9 | 5 |
| S10 | 8 | N10 | 4 | G10 | 5 |
| S11 | 7 | N11 | 3 | G11 | 31 |
| S12 | 28 | N12 | 42 | G12 | 10 |
| S13 | 1 | N13 | 14 | G13 | 19 |
| S14 | 6 | N14 | 13 | | |
| S15 | 4 | N15 | 4 | | |

## Appendix C: Vocabulary Convergence Data

### Phase-by-Phase Convergence
| Phase | Domains Covered | Theorems (new) | Theorems (cum.) | New S | New N | New G | Words Added | Vocab Total |
|-------|----------------|----------------|-----------------|-------|-------|-------|-------------|-------------|
| 1 (Biology) | 1 | 76 | 76 | 10 | 11 | 10 | 31 | 31 |
| 2 (Physics+Cosmo+Nuclear) | 3 | 86 | 162 | 2 | 4 | 2 | 8 | 39 |
| 3 (Found.+ProofC+InfoT) | 3 | 85 | 247 | 3 | 0 | 1 | 4 | 43 |
| 4 (Coop+Intel+Obs+CI) | 4 | 35 | 282 | 0 | 0 | 0 | 0 | 43 |
| 5 (All remaining 25) | 25 | 244 | 526 | 0 | 0 | 0 | 0 | 43 |
| **Total** | **36** | **526** | **526** | **15** | **15** | **13** | **43** | **43** |

### Convergence Rate
| Phase | Theorems per New Word | Status |
|-------|----------------------|--------|
| 1 | 2.5 | Vocabulary building |
| 2 | 10.8 | Vocabulary slowing |
| 3 | 21.3 | Last 4 words added |
| 4 | -- (no new words) | CLOSED |
| 5 | -- (no new words) | CLOSED (244 theorems, 0 words) |

Last new primitive: T247 (March 20, 2026). 434 subsequent theorems, zero new words.

## Appendix D: Domain Costume Classification

### Fourier Costume Key
| Code | Costume | What Fourier does |
|------|---------|-------------------|
| S | Spectral (heat kernel) | Eigenvalue decomposition; reads curvature through cooling |
| T | Thermo-Information (partition function = channel capacity) | State-counting with Boltzmann weights; reads capacity through entropy |
| A | Arithmetic (L-functions) | Prime/modular decomposition; reads discrete structure through Euler products |

### All 37 Domains
| # | Domain | Primary | Secondary | Boundary Type | Costume Change to Neighbor |
|---|--------|---------|-----------|---------------|---------------------------|
| 1 | algebra | S | -- | conventional | S->A to number_theory |
| 2 | analysis | S | -- | conventional | S->S to fluids |
| 3 | biology | T | -- | conventional | T->S to bst_physics |
| 4 | bst_physics | S | T | **geometric** (Todd Bridge) | S->T internal; T->S to cosmology |
| 5 | chemistry | T | -- | conventional | T->T to biology |
| 6 | ci_persistence | T | -- | conventional | T->T to observer_theory |
| 7 | circuit_complexity | T | -- | conventional | T->T to proof_complexity |
| 8 | classical_mech | S | -- | conventional | S->S to fluids |
| 9 | coding_theory | T | -- | conventional | T->A to number_theory |
| 10 | computation | T | -- | conventional | T->T to proof_complexity |
| 11 | condensed_matter | S | T | **geometric** | S->S to qft |
| 12 | cooperation | T | -- | conventional | T->T to intelligence |
| 13 | cosmology | T | A | **geometric** | A->A to number_theory |
| 14 | differential_geometry | S | -- | conventional | S->S to topology |
| 15 | electromagnetism | S | A | **geometric** | S->A internal |
| 16 | fluids | S | -- | conventional | S->S to analysis |
| 17 | foundations | T | -- | conventional | T->S to differential_geometry |
| 18 | four_color | T | -- | conventional | T->T to graph_theory |
| 19 | graph_theory | T | A | **geometric** | T->T to coding_theory; A->A to number_theory |
| 20 | info_theory | T | -- | conventional | T->T to proof_complexity |
| 21 | intelligence | T | -- | conventional | T->T to observer_theory |
| 22 | linearization | S | -- | conventional | S->S to every neighbor |
| 23 | nuclear | S | A | **geometric** | S->A internal |
| 24 | number_theory | A | -- | **geometric** (sole primary-A domain) | A->S to differential_geometry |
| 25 | observer_theory | T | -- | conventional | T->T to ci_persistence |
| 26 | optics | S | -- | conventional | S->S to electromagnetism |
| 27 | outreach | -- | -- | (meta-domain, no reader) | -- |
| 28 | physics | S | -- | conventional | S->S to bst_physics |
| 29 | probability | T | -- | conventional | T->T to info_theory |
| 30 | proof_complexity | T | A | **geometric** | T->A to number_theory |
| 31 | qft | S | A | **geometric** | S->S to bst_physics |
| 32 | quantum | S | -- | conventional | S->S to qft |
| 33 | quantum_foundations | -- | -- | (new, pending classification) | -- |
| 34 | relativity | S | -- | conventional | S->S to cosmology |
| 35 | signal | T | -- | conventional | T->T to info_theory |
| 36 | thermodynamics | T | -- | conventional | T->S to bst_physics |
| 37 | topology | S | A | **geometric** | S->A internal |

### Costume Census
| Costume | As Primary | As Secondary | Total Appearances |
|---------|-----------|-------------|-------------------|
| Spectral (S) | 15 | 7 | 22 |
| Thermo-Info (T) | 17 | 4 | 21 |
| Arithmetic (A) | 1 | 8 | 9 |

### Boundary Census
| Type | Count | Fraction |
|------|-------|----------|
| Conventional (naming only) | 25 | 68% |
| Geometric (forced by D_IV^5) | 10 | 27% |
| Meta / unclassified | 2 | 5% |

Dual-costume domains (internal geometric boundary): bst_physics, condensed_matter, cosmology, electromagnetism, graph_theory, nuclear, proof_complexity, qft, topology. All 9 sit at costume-change boundaries in the global graph.

Minimum costume changes to traverse all 37 domains: **3** (S->T at bst_physics, T->A at proof_complexity, A->T at graph_theory).

*Grace | March 31, 2026 | Sources: BST_Biology_Reduction_Layer, BST_Bedrock_Adjacency_Matrix, grace_graph_rerun_march31, grace_fourier_readers_by_domain*
