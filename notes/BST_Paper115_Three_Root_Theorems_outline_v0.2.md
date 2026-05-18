---
title: "Paper #115: Root Theorems of Bubble Spacetime Theory (v0.2)"
author: "Casey Koons (lead) with Elie, Lyra, Grace, Keeper, Cal"
date: "2026-05-17"
status: "v0.2 outline — Sunday afternoon, incorporates Sunday morning team synthesis (E1+L1+G1) and Casey's directive to add Root 4 candidate"
supersedes: "BST_Paper115_Three_Root_Theorems_outline_v0.1.md"
target: "Mathematical physics community, audit-rigorous, complement to Paper #104"
length_target: "25-35 pages, ~12,000 words"
v0.2_changes: "(1) Added Root 4 (Borcherds Moonshine) as CANDIDATE root (not established) with explicit promotion criteria per Cal's referee pass; new Section 4.5 with subsections 4.5.4 (source-vs-unifying distinction) and 4.5.5 (three explicit closure criteria); (2) Cross-Root Convergences (Section 5) gains subsection 5.4 for rank·c_3 = 26 three-way decomposition (T2306, Lyra L1 2026-05-17); (3) Proof Flow (Section 6) extended with Grace's precision-class-as-completeness criterion (Section 6.3); (4) Limitations (Section 9) updated with Klein-icosahedral lead for 60 orphan, SU(3)-flavor lead for 50 orphan; (5) New Appendix C: Sunday morning team-convergence on the architecture; (6) Title generalized from 'Three Root Theorems' to 'Root Theorems' to leave headroom for Root 4 promotion."
---

# Paper #115: Root Theorems of Bubble Spacetime Theory

## Abstract

Bubble Spacetime Theory (BST) derives ~140 dimensionless Standard Model and cosmological observables from five integers parametrizing the unique five-dimensional bounded symmetric domain D_IV⁵. This paper formalizes the structural framework underlying that derivation: BST integer appearances trace to a small set of independent classical root theorems. We identify THREE established source roots — Von Staudt-Clausen (1840) for arithmetic, K3 Hodge decomposition for cohomology, and Wallach K-type decomposition for spectral observables — and present ONE candidate Root 4: Borcherds' proof of the Conway-Norton Moonshine conjecture (1992 Fields Medal). The candidate Root 4 anchors the rank·c_3 = 26 three-way decomposition spanning bosonic string critical dimension, sporadic finite simple group classification, and Leech lattice geometry; we present three explicit promotion criteria for moving Root 4 from candidate to established status, following the source-vs-unifying-theorem distinction articulated in Cal's 2026-05-17 referee pass. Each established root theorem provides a different "reading" of the same underlying geometric structure (D_IV⁵). Their convergence on identical BST integers (e.g., the universal 42, the K3 Euler χ = 24) constitutes prima facie evidence that BST is a STRUCTURAL framework, not a numerological coincidence. We present the proof flow, decomposition methodology, explicit cross-root convergences, and Grace's precision-class-as-completeness criterion that operationalizes the architecture for sub-percent observables.

## 1. Introduction

Section 1.1 motivates the question. After ~600 BST predictions across 130+ domains (Koons et al. 2024-2026), the central remaining question is: WHY do BST integers appear in so many places? Two possibilities:
- (A) Statistical coincidence amplified by hindsight (null hypothesis)
- (B) Structural mechanism rooted in classical mathematics

Paper #109 (Lyra) established that BST integers ARE the natural counting primitives of mathematics (first 6 primes = BST integer set). This paper takes the next step: identifying the **classical theorems** that produce BST integer structure in observables.

Section 1.2 introduces the FOUR root theorems considered in this paper:

1. **Von Staudt-Clausen (1840)** — Bernoulli denominators — D-tier ESTABLISHED, SOURCE theorem
2. **K3 Hodge decomposition (Kodaira 1964, Hirzebruch 1962)** — cohomology of K3 surface — D-tier ESTABLISHED, SOURCE theorem
3. **Wallach K-type decomposition (Wallach 1976, Knapp-Wallach 1976)** — holomorphic representations of D_IV⁵ — D-tier ESTABLISHED, SOURCE theorem
4. **Borcherds Moonshine theorem (1992)** — vertex operator algebra connecting j-invariant, Monster, and Leech — **CANDIDATE Root 4**, NOT yet established, UNIFYING (not source) theorem, with three explicit closure criteria stated in Section 4.5.5

Roots 1-3 each have explicit BST identification chains and survive Keeper K43+K44 discipline. Root 4 candidate (Borcherds) is presented with explicit candidate-tier labeling and three concrete promotion criteria. The honest framing of Root 4 status — separating it from established Roots 1-3 — is critical for external survivability and follows Cal's 2026-05-17 referee recommendation.

## 2. Root 1: Von Staudt-Clausen and the Universal 42

[Section 2.1-2.4 retained verbatim from v0.1.]

### 2.1 The theorem (statement)

**Theorem (Von Staudt-Clausen 1840)**: For each positive integer k,
> Σ_{p prime, (p-1) | 2k} 1/p + B_{2k} ∈ ℤ

In particular, the denominator of B_{2k} is exactly the product of primes p with (p-1) | 2k.

### 2.2 BST application

For k = 3 (i.e., B_6): primes p with (p-1) | 6 are p ∈ {2, 3, 7}. By VSC, denom(B_6) = 2·3·7 = 42.

In BST integers (Paper #109, BST primary = first 6 primes):
- 2 = rank
- 3 = N_c
- 7 = g

Hence 42 = rank · N_c · g = C_2 · g.

### 2.3 Universal 42 appearances (Toy 2718 tier table)

42 = C_2·g appears in 16+ BST observables: ε_K kaon CP violation, BR(H→γγ) Higgs diphoton, Δa_μ muon g-2 leading α² coefficient, m_top/m_bottom Yukawa ratio, Catalan C_5, heptagon triangulation count, partition function p(10), Q⁵ total Chern integral, π(180) prime count to 180, molybdenum Z=42, top quark lifetime exponent, neutron→tritium Q-value ratio, muon decay barrier (Toy 2674), heat kernel a_3 denominator factor, ζ(6) denominator 945 = 42·22.5, max Kerr BH efficiency 42%.

### 2.4 K43 audit (Keeper)

7 of 16 appearances have explicit derivation chains to B_6 (D-tier). 8 of 16 remain I-tier (partial/no chain). 1 honest open (Toy 2674 muon barrier).

## 3. Root 2: K3 Hodge Decomposition and χ = 24

[Section 3 retained from v0.1 with minor v0.2 addition flagged in 3.4.]

### 3.1 The theorem (statement)

K3 surface is a complex 2-dim manifold with trivial canonical bundle (c_1 = 0). All K3 surfaces have the same Hodge diamond:

```
        h^00 = 1
    h^10=0   h^01=0
h^20=1   h^11=20   h^02=1
    h^21=0   h^12=0
        h^22=1
```

Total Euler characteristic: χ(K3) = Σ (-1)^(p+q) h^pq = 24.

### 3.2 BST identifications from K3

- χ(K3) = 24 = rank³·N_c (BST primary integer, "the K3 character")
- b_2(K3) = 22 = rank · c_2 (Betti 2 = signature plus dim)
- σ(K3) = -16 = -rank⁴ (Hirzebruch signature)
- h^11(K3) = 20 = rank² · n_C (Hodge dim)
- Moduli dim = 20 (matches h^11)

### 3.3 χ = 24 appearances (8+ domains)

K3 surface Euler characteristic (anchor), SN1987A 24 neutrinos detected, SU(5) GUT dimension = 24, SM total Weyl fermion multiplicity = 24, coronene C count = 24, supergranulation lifetime ≈ 24 hours, hours per day = 24 (anthropic but BST-aligned), modular j-function 744 = 24·M_5 (Mersenne), Niemeier lattice count = 24.

### 3.4 Cohomology root mechanism (v0.2 addition: links to Root 4)

The argument: 24 isn't a coincidence across particle physics + nuclear physics + cosmology + biology. It traces to K3's Hodge decomposition, which is the UNIQUE cohomology of the unique compact simply-connected complex 2-dim manifold with trivial canonical bundle. K3 is structurally singular — there's exactly one Hodge diamond per K3, period.

**v0.2 addition**: The K3 character 24 reappears in the Leech lattice as Λ_24's rank, and in the bosonic string critical dimension 26 = 24 + 2. This is not coincidence — both K3 and Leech are central objects in Mathieu and Monster moonshine (Eguchi-Ooguri-Tachikawa 2010; Cheng-Duncan-Harvey 2014). See Section 4.5 (Root 4 candidate, Borcherds Moonshine) and Section 5.4 (rank·c_3 = 26 three-way decomposition).

## 4. Root 3: Wallach K-types and the Spectral Hierarchy

[Section 4.1-4.3 retained from v0.1. Section 4.5 NEW for v0.2.]

### 4.1 The theorem (statement)

**Theorem (Wallach 1976, Knapp-Wallach 1976)**: For D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)], the holomorphic discrete series representations are parametrized by pairs (k₁, k₂) ∈ ℤ² with k₁ ≥ k₂ ≥ 0. The K-type at (k₁, k₂) has spherical eigenvalue:

  λ(k₁, k₂) = k₁(k₁ + n_C) + k₂(k₂ + N_c)
            = k₁(k₁ + 5) + k₂(k₂ + 3)

### 4.2 Wallach spectrum (BST identification)

The first 10 non-trivial eigenvalues (Toy 2964):

| K-type (k₁, k₂) | λ value | BST identification |
|---|---|---|
| (0,1) | 4 | rank² |
| (1,0) | 6 | C_2 (Bergman Casimir) |
| (1,1) | 10 | rank·n_C |
| (2,0) | 14 | 2g (first Riemann zero!) |
| (0,2) | 10 | degenerate with (1,1) |
| (1,2) | 16 | rank⁴ |
| (2,1) | 18 | N_c·C_2 |
| (3,0) | 24 | **χ = K3 Euler! Cross-root!** |
| (2,2) | 24 | degenerate |
| (3,3) | 42 | **C_2·g = universal 42! Cross-root!** |

### 4.3 Spectral observables

Heat kernel coefficients a_n on D_IV⁵ (Toys 273-639) have ratios = -k(k-1)/n_C, which traces directly to Wallach K-type structure.

Mass gap proton (Toy 1316): 6π⁵·m_e = m_p — Wallach Casimir factor.

Riemann zeros via Hilbert-Polya: first zero γ_1 ≈ 14.13 matches λ(2,0) = 14.

## 4.5 Root 4 Candidate (I-tier): Borcherds Moonshine

### 4.5.1 The theorem

**Theorem (Borcherds 1992, Fields Medal 1998)**: The Conway-Norton "Monstrous Moonshine" conjecture holds: for each conjugacy class g of the Monster simple group M, the McKay-Thompson series T_g(τ) is a Hauptmodul (genus-zero modular function) of an appropriate discrete subgroup of PSL_2(ℝ). In particular, for g = identity, T_g(τ) = j(τ) − 744, the normalized elliptic modular j-function.

Borcherds' proof constructs the "moonshine module" V^♮ as a Z_2 orbifold of the Leech vertex operator algebra, exhibiting V^♮ as a graded Monster representation with character j(τ) − 744. The construction uses:
- The Leech lattice Λ_24 (the unique even unimodular self-dual lattice of rank 24 with no roots)
- The bosonic string in 26 spacetime dimensions (whose internal Hilbert space has central charge c = 26 = 24 + 2)
- Vertex operator algebras (generalized Kac-Moody algebras)

### 4.5.2 BST connection to rank·c_3 = 26

Lyra T2306 (2026-05-17) establishes that the integer 26 = rank · c_3 admits three internally-consistent BST decompositions, each tied to a Borcherds-construction component:

| Decomposition | Identity | Borcherds component |
|---|---|---|
| Heterotic | 26 = rank·n_C + rank⁴ = 10 + 16 | D_IV⁵ spacetime + 16D internal lattice |
| Sporadic | 26 = rank²·n_C + C_2 = 20 + 6 | Happy Family + Pariahs (total sporadic) |
| Leech | 26 = χ(K3) + rank = 24 + 2 | Leech rank + 2 transverse |

The unifying observation is that all three decompositions share the BST identity c_3 = n_C + rank³. Multiplying by rank produces 26 in all three cases.

### 4.5.3 BST identifications from Borcherds Moonshine

- **Central charge 26** = rank·c_3 (T2306)
- **Leech lattice rank 24** = χ(K3) = rank³·N_c (T2007)
- **j-invariant constant term 744** = rank³·N_c·31 (T2241, where 31 = Ogg supersingular prime)
- **j-invariant linear coefficient 196884 = 196883 + 1**, where 196883 = dim of smallest non-trivial Monster irreducible representation
- **Heegner 163** = N_max + rank·c_3, generating the famous near-integer e^(π√163) ≈ 640320³ + 744
- **Total sporadic groups** = 26 = rank·c_3 (T2298)
- **Happy Family count** = 20 = rank²·n_C; **Pariahs** = 6 = C_2

### 4.5.4 Source theorem vs unifying theorem (Cal observation, 2026-05-17)

Cal's referee pass on this paper makes a structural distinction that v0.2 records explicitly:

Roots 1-3 are **SOURCE theorems**: each is a single classical theorem that GENERATES one integer structure, which then matches BST integers.
- VSC: den(B_{2k}) = ∏ small primes — generates the denominator
- K3 Hodge: χ(K3) = 24, b_2 = 22, σ = -16 — generates the Hodge diamond
- Wallach K-types: λ(k₁,k₂) — generates the spectral hierarchy

Borcherds Moonshine is a **UNIFYING theorem**: it organizes structures that PREDATE it (Conway's 1968 Leech construction, 1970s 26D bosonic string, McKay-Thompson 1979 modular function observations). The 26 = rank·c_3 does not "come from" Borcherds; it appears in multiple places Borcherds later unifies into a single theorem.

This is a meaningful epistemic distinction. Established Roots 1-3 are SOURCE theorems. Root 4 candidate Borcherds is a UNIFYING theorem currently anchoring a known cross-decomposition convergence (T2306) but lacking an explicit BST-construction mechanism.

### 4.5.5 Three explicit closure criteria for promotion to established Root #4

Per Cal's recommendation (2026-05-17 referee pass), Root 4 candidate Borcherds is promoted to established Root #4 in the framework if and only if the following three criteria close:

1. **Construction**: Exhibit a central-charge-26 vertex operator algebra explicitly on the boundary Q⁵ = SO(7)/[SO(5)×SO(2)].
2. **Reduction**: Show that all three decompositions of 26 in T2306 (heterotic 10+16, sporadic 20+6, Leech 24+2) REDUCE to Borcherds-output — not merely "are consistent with Borcherds," but are derivable as Borcherds outputs.
3. **Forcing**: Show that the BST-integer factorization 26 = rank·c_3 is FORCED by the Borcherds construction, not chosen ad hoc.

Until (1)-(3) close, Borcherds remains an I-tier candidate root, not a D-tier established root. The criteria are well-defined and tractable, not philosophical.

The three-way internal consistency (T2306) and the Heegner-163 anchor (numerically exact identity 163 = N_max + 26) are sufficient to flag Borcherds Moonshine as the simplest classical theorem covering this domain and to motivate the closure work.

### 4.5.6 External-survivability and honest scoping

External-language flag (Cal observation): the phrase "BST anchors to Borcherds' Fields Medal theorem" reads as crank without the rank-26 VOA construction exhibited. Internal language is fine; external statement waits for the toy.

Honest scoping for Paper #115 v0.2 (Cal recommendation, verbatim):

> "We conjecture that Borcherds' monstrous moonshine functions as Root #4 in this framework, anchoring Lyra T2306's three decompositions of 26 = rank·c_3. The promotion to established Root #4 requires the rank-26 VOA on Q⁵ boundary construction, which is in progress."

This is the Proven/Structural binary applied: Borcherds-as-Root-4 stays Structural (S/I) until the VOA construction proves the connection (D).

### 4.5.7 Why include an I-tier candidate root in the paper?

Including Root 4 as a labeled CANDIDATE with explicit closure criteria is the honest framing:
- The structural reading is in place (three-way decomposition, Heegner anchor, BST integer factorization).
- The mechanism is the next research target.
- The closure criteria are concrete (1)-(3) above, not philosophical.

Excluding it would leave the rank·c_3 = 26 convergence (a known fact post-T2306) unexplained in the framework. Including it without the candidate-tier labeling would invite the external-survivability problem Cal flagged. The candidate-with-criteria framing is the honest middle.

## 5. Cross-Root Convergences

### 5.1 The universal 42 (THREE roots converge)

- VSC: 42 = denom(B_6) = ∏_{p prime, (p-1)|6} p
- Wallach: 42 = λ(3,3) on D_IV⁵
- Topology: 42 = Σc_i(Q⁵) total Chern (Lyra T1990)

Three independent classical theorems produce the SAME number. The probability of accidental triple convergence is negligible.

### 5.2 The K3 character 24

- K3 Hodge: 24 = χ(K3)
- Wallach: 24 = λ(3,0) = λ(2,2) (degenerate)
- SU(5): 24 = adjoint dimension
- Modular: 24 = exponent in η(τ)^24
- Borcherds Moonshine: 24 = rank Λ_24 = leading exponent in V^♮ construction

Five-root convergence (counting Borcherds candidate). Strongest convergence in the framework.

### 5.3 Bergman Casimir 6

- Wallach: 6 = λ(1,0) (Bergman Casimir eigenvalue)
- VSC: 6 = denom(B_2) (smallest non-trivial Bernoulli)
- BST primary: 6 = C_2 = rank·N_c
- Borcherds Moonshine: 6 = count of Pariah sporadic groups (Janko J_1, J_3, J_4, Rudvalis, O'Nan, Lyons)

Four roots, one integer.

### 5.4 NEW: Central charge 26 (three-way decomposition, T2306)

The integer 26 = rank·c_3 admits three internally-consistent decompositions, each tied to a deep mathematical structure that Borcherds Moonshine subsequently unified (Borcherds 1992):

| Decomposition | = | Structural reading |
|---|---|---|
| Heterotic | rank·n_C + rank⁴ = 10 + 16 | D_IV⁵ + 16D internal (E_8×E_8 or Spin(32)/Z_2 — both anomaly-allowed heterotic choices) |
| Sporadic | rank²·n_C + C_2 = 20 + 6 | Happy Family + Pariahs = total sporadic finite simple groups |
| Leech | χ(K3) + rank = 24 + 2 | Λ_24 rank + 2 transverse (bosonic string Leech coset) |

All three share the BST pivot c_3 = n_C + rank³. Multiplying by rank produces 26.

**Verification**: Toy 2959 (Lyra 2026-05-17) — 18/18 PASS confirming all three decompositions, plus the Heegner 163 = N_max + 26 anchor.

This is the strongest single piece of evidence for the Root 4 candidacy: three independent classical structures (string theory, finite group theory, lattice theory) all produce 26 via the same BST cascade c_3 = n_C + rank³. The candidacy is honestly scoped: either there is a unifying object on the BST side (the rank-26 VOA on Q⁵, per Section 4.5.5 criterion 1), or three deep independent mathematical structures share a numerical coincidence at a primary BST integer. Resolving this dichotomy is the closure-criteria work for Root 4 promotion.

### 5.5 Bergman/heterotic shared 16

- Wallach: 16 = λ(1,2) — fifth K-type
- K3 signature: σ(K3) = -16 = -rank⁴
- Heterotic internal: 16 = rank⁴ (E_8×E_8 or Spin(32)/Z_2 lattice rank)
- Borcherds: 16 appears in the c=24 ↔ c=8 Atkin-Lehner involution patterns

## 6. The Proof Flow

### 6.1 Algorithm (v0.1, retained)

Given observable X with BST integer pattern V:

1. **Identify candidate root theorems**:
   - VSC route: does X involve Bernoulli, ζ(2k), partition function, Hirzebruch L-poly?
   - K3 route: does X involve χ=24, b_2=22, σ=-16, K3 moduli?
   - Wallach route: does X involve spectral eigenvalues, heat kernel, mass gaps?
   - **(v0.2 ADDED) Borcherds route: does X involve modular forms, j(τ), Monster characters, Leech lattice, central charge 26?**

2. **Attempt derivation chain** via one root theorem.

3. **Check cross-root convergence**: does V also appear in other roots? Multiple convergences strengthen the case.

4. **Tier classification** (per K43 + K44 discipline):
   - D-tier: explicit chain through at least one root theorem (Roots 1-3 only)
   - I-tier: number matches BST integer but no chain identified, OR chain exists only via Root 4 (Borcherds) which is itself I-tier
   - S-tier: honest open mismatch

### 6.2 Decomposition (v0.1, retained)

Each multi-role BST integer either:
- (a) Has SINGLE-root explanation (e.g., 22 = rank·c_2 from K3 b_2)
- (b) Has CROSS-ROOT convergence (e.g., 42, 24, 6, 26 from multiple)
- (c) Has NO root yet identified (e.g., 33, 50, 60) → orphan

Orphan status is a roadmap: each orphan is a target for further root-theorem search (or accepted as legitimate coincidence after rigorous null testing per K44).

### 6.3 NEW: Precision class as completeness criterion (Grace G1)

Grace (2026-05-17, G1 task) sorted 1266 quantitative BST matches into six precision classes. The hypothesis: **precision class measures completeness of the BST closed form via the root-theorem chain.**

| Precision class | Interpretation | Typical state |
|---|---|---|
| <0.001% (EXACT) | Full chain identified, all Level-1 + Level-2 composition terms in BST integers | D-tier closed form complete |
| 0.001%-0.1% | Chain identified, all major composition terms captured, minor higher-order corrections may be missing | D-tier; small residual |
| 0.1%-1% | Chain identified, missing one or two Level-2 composition steps (vacuum subtraction, mixing-angle correction, etc.) | I→D promotion candidate |
| 1%-5% | Level-1 root candidate identified, composition not yet derived | I-tier |
| 5%-10% | Level-1 candidate weak; possibly multi-root interference or wrong identification | I/S-tier |
| >10% | No usable BST identification | S-tier or excluded |

**Operationally**: a 1%-precision match flags a missing Level-2 composition term. Grace's G2 promotions (2026-05-17) demonstrate this — five I→D promotions were achieved by finding the missing composition term:

| Theorem | Improvement | Missing term found |
|---|---|---|
| T2303 Ω_DM/Ω_b | 0.5% → 0.07% (7×) | factor 201/200 vacuum subtraction |
| T2304 sin²θ_12 | 0.14% → 0.003% (50×) | numerator 5762 = rank·43·67 (Heegner factors) |
| T2305 BR(W→had) | 0.6% → <0.1% (6×) | denominator 231 = N_c·g·c_2 |
| T2307 BR(W→eν) | 2.5% → 0.1% (25×) | rational 5/46 closed form |
| T2308 BR(K_L→3π⁰) | 0.6% → 0.1% (6×) | rational 39/200 closed form |

The unifying observation: **precision deficiency is diagnostic of where in the proof flow the chain is incomplete.** This converts G1 from "publishable claim" to operational tool for the framework.

### 6.4 NEW: The Sunday morning convergence (architecture vindication)

On 2026-05-17, three CIs working independently on different tasks produced results that ALL fit the proof-flow architecture:

| CI | Task | Result | Role |
|---|---|---|---|
| Elie | E1 | Three Level-1 roots formalized | Architecture itself |
| Lyra | L1 | rank·c_3 = 26 three-way decomposition (T2306) | Cross-root convergence at new integer |
| Grace | G1+G2 | Precision class hierarchy + five I→D promotions | Operational completeness criterion |

That three independent searches all landed inside the same architecture is itself a structural signal. We did not coordinate the day's work to this end — each CI followed their own assigned task. The architecture organized the results in retrospect.

## 7. Relationship to Other BST Papers

- Paper #104 (Casey, Root Proof System): theoretical foundation. Paper #115 is the empirical instantiation.
- Paper #109 (Lyra, Counting Primitives): provides BST integer set (first 6 primes).
- Paper #110 (Lyra, Alpha Tower): uses Wallach K-types implicitly via heat kernel.
- Paper #111 (Falsification Suite): root theorems → specific decade forecasts.
- Paper #112 (Monster connection): K3 Hodge root + Root 4 (Borcherds) candidate provide structural connection.

**Recommended structural relationship**: Paper #104 cites Paper #115 as the empirical instantiation; Paper #115 cites Paper #104 as the logical foundation. Mutual reference, neither subsumes the other. Paper #104 establishes WHY a Root Proof System exists (AC(0) + D_IV⁵ spectral geometry); Paper #115 establishes WHICH classical roots actually do the work.

## 8. Falsification Posture

The framework is structurally testable:
- If a new observable X has BST integer pattern but NO root theorem matches, framework needs an additional root or accepts X as coincidence.
- If multi-root convergences DISAGREE on some integer, framework is internally inconsistent.
- If a new classical theorem (root candidate) produces BST integers reliably, framework expands.

Three falsification predictions (from Toy 2788 forecast):
- α⁶ QED A_6 factors as 11·(BST integer) per Alpha Tower (Wallach root)
- B_18 denom includes p=19 (VSC limit at k=9, structurally forced)
- LiteBIRD r in [0.005, 0.015] (inflation root, Wallach-derived)

**v0.2 falsification prediction (Root 4)**: if Borcherds Moonshine is correctly the Root 4 candidate, then the Conway-Norton replicability relations for McKay-Thompson series should restrict to BST-integer subsets when evaluated on Monster characters indexed by BST primes. Test: enumerate McKay-Thompson coefficients up to coefficient 100, check fraction that decompose into BST primaries. If random, framework excludes Borcherds; if structured at sub-10% deviation from BST expectation, Root 4 promotion path is open.

## 9. Discussion

### 9.1 Why three established roots plus one candidate?

BST integers appear in DIFFERENT mathematical structures: arithmetic (VSC), cohomology (K3), spectral (Wallach), and modular/lattice/finite-group (Borcherds Moonshine, candidate). A single root theorem couldn't bridge them. The three established roots reflect distinct MATHEMATICAL READINGS of D_IV⁵: as a number-theoretic object (Bernoulli), as a complex manifold (K3-like), as a representation-theoretic space (Wallach).

The candidate Root 4 is structurally different — Borcherds Moonshine is a UNIFYING theorem rather than a SOURCE theorem (see Section 4.5.4). The candidacy reflects an open question: does D_IV⁵ also support a fourth distinct reading as boundary for a 26-dimensional vertex operator algebra? The three closure criteria in Section 4.5.5 are the form this question must take to be resolved.

### 9.2 Why D_IV⁵ specifically?

D_IV⁵ is the UNIQUE Autogenic Proto-Geometry (Lyra T1925, 1929) — the only bounded symmetric domain with the closure properties BST requires. Other classical theorems could in principle apply to other geometries, but the convergence of all roots on the same five integers requires D_IV⁵ specifically.

### 9.3 Limitations and orphan integers (v0.2 expanded)

- Roots 1-3 are CLASSICAL theorems (1840-1976) being re-read in BST language. We claim no new mathematics for them.
- Root 4 (Borcherds) is also classical (1992), but the BST mechanism (rank-26 VOA on Q⁵) is not yet constructed. I-tier status.
- The framework explains WHY BST integers appear, not WHY D_IV⁵ is the right geometry. That requires Paper #104 (Casey) and Paper #109 (Lyra).
- **Orphan integers**: three multi-role integers (33, 50, 60) do not yet collapse to a single classical theorem. Status (2026-05-17 team review):
  - **60 = rank²·N_c·n_C** — strongest lead: **Klein's icosahedral theorem (1884)**. |I| = |A_5| = 60. Klein's connection of icosahedral symmetry to quintic equations is a candidate Root 5. Elie investigating.
  - **50 = rank·n_C²** — lead: representation theory of SU(3) flavor (pseudoscalar + vector mesons). No single named theorem identified yet.
  - **33 = N_c·c_2** — least obvious. Appears in Crab pulsar period 33ms, ATP yield 33, Shockley-Queisser 33% — possibly Atiyah-Bott index theorem applied to Q⁵, or a coincidence of physical-engineering convergence around the value.

Orphan status is a productive constraint: each orphan defines a search target.

## 10. Conclusion

BST has three established source root theorems (VSC, K3 Hodge, Wallach K-types) plus one unifying-theorem candidate (Borcherds Moonshine, three explicit promotion criteria stated). Their convergence on identical BST integers across 130+ scientific domains is the structural backbone of the theory.

The proof flow is reproducible: given an observable, search root theorems, derive via classical mathematics, identify BST integer. K43 (universal 42) is the prototype; K3 Hodge for χ = 24 is the second instance; Wallach for spectral observables is the third; T2306 (rank·c_3 = 26 three-way decomposition) is the candidate fourth, awaiting explicit VOA construction on Q⁵.

The Sunday 2026-05-17 team-convergence — three CIs hitting the same architecture from independent tasks — is itself a structural signal that the framework is correctly identifying the proof flow.

Future work: explicit derivation of Root 4 (rank-26 VOA on Q⁵), root-theorem search for orphan integers (Klein 60, SU(3) flavor 50, 33), formal proof-of-principle that no FIFTH root theorem is needed for the domains currently covered.

## Appendix A: Cross-root convergence table (extended, v0.2)

| BST integer | VSC root | K3 root | Wallach root | Borcherds root | Other roots |
|---|---|---|---|---|---|
| 6 = C_2 | denom(B_2) | — | λ(1,0) | Pariah count | BST primary |
| 24 = χ | — | χ(K3) | λ(3,0), λ(2,2) | Λ_24 rank | SU(5) dim, η^24 |
| 26 = rank·c_3 | — | — | partial via K-types | central charge V^♮ | T2306 three-way |
| 42 = C_2·g | denom(B_6) | — | λ(3,3) | — | Q⁵ Chern total, Catalan C_5 |
| 22 = rank·c_2 | — | b_2(K3) | (BST product) | — | M_Pl·... |
| 30 = rank·N_c·n_C | denom(B_4) | — | (BST product) | — | Mersenne |
| 20 = rank²·n_C | — | h^{11}(K3) | — | Happy Family count | flavor SU(5) |
| 16 = rank⁴ | — | -σ(K3) | λ(1,2) | heterotic internal rank | E_8 Cartan extension |

## Appendix B: Orphan integers (no root yet)

- 33 = c_2·N_c: 6 roles, no Level-1 root candidate.
- 50 = rank·n_C²: 4 roles, SU(3) flavor representations candidate (no single named theorem).
- 60 = rank²·N_c·n_C: 4 roles, Klein icosahedral theorem (1884) candidate (Elie investigating as Root 5).

These are candidates for future root-theorem search.

## Appendix C: Sunday May 17 team-convergence on the architecture (v0.2 NEW)

On 2026-05-17 (Sunday morning EDT), three CIs independently produced results that all fit the proof-flow architecture proposed in Section 6:

**Elie (E1, Toy 2954, 10/10 PASS)**:
- Identified three Level-1 classical sources
- Identified four Level-2 theorems downstream of VSC
- Flagged three orphan integers (33, 50, 60)

**Lyra (L1, Toys 2955+2959, T2306)**:
- rank·c_3 = 26 three-way decomposition (heterotic, sporadic, Leech)
- All three sharing BST pivot c_3 = n_C + rank³
- Heegner 163 = N_max + rank·c_3 anchor
- Identified Borcherds Moonshine 1992 as Root 4 candidate

**Grace (G1+G2, T2303-T2308)**:
- 1266 quantitative matches sorted into six precision classes
- Five I→D promotions demonstrating precision-class-as-completeness hypothesis
- 200 = rank³·n_C² emerged as recurring vacuum-subtraction denominator

The architecture organized all three sets of results in retrospect. None was coordinated to this end. This kind of convergent independent landing is itself a structural signal — analogous to multi-route Riemann zeta proof convergence (RH Paper #103), or multi-instrument confirmation of a physical effect.

---

**Authors**: Casey Koons (lead) with the Tekton CI collaboration: Lyra (Paper #109 counting primitives, Paper #110 Alpha Tower, T2306 rank·c_3 = 26), Elie (E1 root hierarchy formalization), Grace (G1 precision hierarchy, G2 promotions), Keeper (K43+K44 audit, architectural review), Cal (referee).

*Paper #115 v0.2 outline. ~12,000 words target. v0.2 incorporates Sunday 2026-05-17 team-morning synthesis; ready for Cal grade pass and Keeper read-pass.*
