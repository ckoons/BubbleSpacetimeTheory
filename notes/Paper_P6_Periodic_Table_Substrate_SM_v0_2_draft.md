---
title: "Paper P6 — The Periodic Table of the Substrate Standard Model v0.2 (Sections 1+2 draft expansion)"
authors: "Grace + Lyra (lead); Casey Koons + Elie + Keeper + Cal contributing"
date: "2026-05-31 Sunday ~10:05 EDT (`date`-verified Sun May 31 10:01 EDT) — Sunday derivation day per Casey directive (Lane G-P6-v0.2)"
status: "v0.2 SECTIONS 1+2 DRAFT EXPANSION — substantive paper-grade narrative for Section 1 (The Substrate) + Section 2 (The Periodic Table). Builds on v0.1 outline (load-bearing claims list + Sections 6/7/8 outlines unchanged). Per Casey discipline directive (Sunday morning): work is honest if we produce something we couldn't produce yesterday."
supersedes: "Paper_P6_Periodic_Table_Substrate_SM_v0_1_outline.md (Sections 1+2 expanded; rest carries forward)"
---

# Paper P6 v0.2 — Sections 1+2 expanded

## Section 1 — The Substrate

### 1.1 D_IV⁵ as bounded symmetric domain

BST proposes that every Standard Model constant and structural feature is determined by a single mathematical object: the bounded symmetric domain
$$D_{IV}^5 = SO_0(5,2) / [SO(5) \times SO(2)]$$
of complex dimension 5 and rank 2. We call this domain the *Autogenic Proto-Geometry* (APG).

D_IV⁵ is a Type IV (Lie ball / Hermitian symmetric of tube type) domain in Cartan's 1935 classification of irreducible bounded symmetric domains. The classification has four classical infinite families (I, II, III, IV) and two exceptional domains (V, VI). Among all Cartan-irreducible BSDs, **D_IV⁵ is uniquely characterized by satisfying three structural conditions simultaneously**: rank = 2, complex dimension = 5, and the dual Coxeter number of the compact factor h^∨(SO(5)) = 3 (Lyra Strong-Uniqueness v1.4 + B8 explicit per-domain check, Saturday 2026-05-30).

Within Type IV alone, D_IV⁵ is the n = 5 representative: D_IV^n = SO_0(2,n)/[SO(n)×SO(2)] for general n. The choice n = 5 is forced by the conjunction (3 colors, 3 generations, complex dim 5) → D_IV⁵; alternative n values fail to support the Standard Model structure (Lyra v1.4 forcing chain).

The compact isotropy group K = SO(5) × SO(2) decomposes the substrate's tangent space into compact and non-compact directions: dim p = 21 − 11 = 10 (Elie Toy 3612, Saturday). The non-compact tangent p has dimension 10 and decomposes as p = V_5 ⊗ (V_{+1} ⊕ V_{−1}) under K-action, with p_+ = V_5 ⊗ V_{+1} the holomorphic tangent. Critically, p_+ is *Hermitian abelian* — [p_+, p_+] = 0 — which is the structural feature that distinguishes Hermitian symmetric domains from arbitrary symmetric spaces. This abelianness will be important for the bulk-color mechanism (Section 7).

### 1.2 The five substrate-primary integers

The structure of D_IV⁵ is captured by five small integers, which we call *substrate primaries*:

| Symbol | Value | Name | Role |
|---|---|---|---|
| rank | 2 | Domain rank | Two complex disks; minimum observation |
| N_c | 3 | Dual Coxeter h^∨(SO(5)) | Color count; minimum irreducibility |
| n_C | 5 | Complex dimension | Flatness threshold |
| C₂ | 6 | Casimir of adjoint rep | Quine length; Painlevé count |
| g | 7 | Bergman genus = signature embedding p+q | Catalog size (2^g = 128); closure |

A sixth integer, N_max = 2^g + N_c² = 128 + 9 = 137, arises as a derived consequence and appears as the inverse fine-structure constant 1/α to leading order (Lyra L8). Two equivalent representations:
- N_max = N_c³ · n_C + rank = 27 · 5 + 2 = 137 (T-series classical form)
- N_max = 2^g + N_c² = 128 + 9 = 137 (Lyra L8 Reed-Solomon form)

The five primaries are not independent free parameters. They are invariants of the single domain D_IV⁵ (Lyra Strong-Uniqueness v1.4 Route-A). In a stronger reading developed Saturday, they form a deterministic chain from rank = 2 via substrate-natural operations (Mersenne, sum, product, Reed-Solomon ladder):

$$\text{rank} = 2 \xrightarrow{\text{Mersenne}} N_c = M_{\text{rank}} = 3 \xrightarrow{\text{sum}} n_C = \text{rank} + N_c = 5 \xrightarrow{\text{product}} C_2 = \text{rank} \cdot N_c = 6 \xrightarrow{\text{Mersenne}} g = M_{N_c} = 7$$

with N_max = rank^g + N_c² closing the chain via Reed-Solomon ladder (Grace INV-5341, Saturday; chain identity arithmetic stands rigorously, principle-grade elevation null-downgraded per discipline-bid testing). This sharpens Strong-Uniqueness from "5 invariants" toward "1 input (rank = 2) + 4 deterministic substrate operations."

### 1.3 The substrate Hall algebra at q = 2

The substrate's dynamical structure is captured by its *Hall algebra*: the Ringel-Hall algebra U_q⁺(B₂) of the quiver representations of the Dynkin diagram B₂, specialized to q = 2 (i.e., the field GF(2)). This algebraic specialization is not an arbitrary choice but is forced by the substrate's Reed-Solomon structure on GF(2^g) = GF(128) (Paper #122 Information Substrate).

The Hall algebra at q = 2 has the property that the q-deformed integers [n]_q evaluate to Mersenne numbers: [n]_2 = 2^n − 1 = M_n. The substrate primaries cluster on the low Mersenne ladder:
- N_c = M_{rank} = M_2 = 3
- g = M_{N_c} = M_3 = 7
- M_g = M_7 = 127 (largest Mersenne in the substrate ladder; differs from N_max by 10)

The Hall algebra's defining Serre relations have structure constants that *are* substrate geometric invariants (Lyra synthesis Saturday + Elie E0/E9/E12):

| Structure constant | Value | Substrate identity |
|---|---|---|
| Short Serre coefficient [2]_2 | **N_c = 3** | dual Coxeter h^∨(B₂); also h^∨(SU(3)) |
| Long Drinfeld pairing numerator | **N_c · n_C = 15** | dim Sym²(V_5) |
| Long Serre coefficient [3]_4 | **N_c · g = 21** | dim so(5,2) |

This is the strongest "the algebra IS the substrate" reading: the substrate Hall algebra's defining relations encode three geometric invariants of D_IV⁵ as their structure constants.

### 1.4 The compact part K = SO(5) × SO(2) and the K-type spectrum

The compact subgroup K = SO(5) × SO(2) generates the building blocks of the Periodic Table: its irreducible representations (K-types). For SO(5) = B₂, K-types are labeled by highest weights (λ_1, λ_2) with λ_1 ≥ λ_2 ≥ 0. The four fundamental representations and their dimensions are:

| K-type | Highest weight | Dim | SO(5) name | Casimir |
|---|---|---|---|---|
| V_{(0,0)} | trivial | 1 | trivial | 0 |
| V_{(1/2,1/2)} | spinor ω₂ | 4 | Dirac spinor (B₂) | 5/2 = ρ₁ |
| V_{(1,0)} | vector ω₁ | 5 | vector | 4 |
| V_{(1,1)} | adjoint | 10 | so(5) adjoint | 6 = C₂ |

The dimensions are substrate-primary: 4 = rank², 5 = n_C, 10 = rank·n_C. The spinor Casimir 5/2 = ρ₁ = n_C/rank equals the Bergman kernel singularity exponent on D_IV⁵ (Lyra C19, ρ-vector). This will be important for the lepton mass mechanism (Section 5): matter sits at the substrate's natural mass-setting singularity.

The full K-type spectrum extends via Racah-Speiser tensor products. Elie's Phase B enumeration (Toy 3614, Saturday) catalogs all 66 K-types with Dynkin labels (a, b) such that a + b ≤ 10. Of these 66, an 18-cell *substrate spine* has 2·C₂ values that factor cleanly through substrate-primary products — this spine carries the structurally-important cells for SM-particle identification.

The count 66 itself is substrate-natural: 66 = rank^{C_2} + rank = 64 + 2 = 2^6 + 2 (Grace INV-5344, Saturday).

### 1.5 Bergman bulk and Shilov boundary

The bounded symmetric domain D_IV⁵ has two distinguished geometric regions:
- **Bergman bulk** (interior of the domain) carries the Bergman kernel K(z, w̄), which determines an invariant measure (Faraut-Korányi-normalized: c_FK = 225/π^(9/2), T2442) and the Hilbert space H²(D_IV⁵) = Bergman space of holomorphic functions
- **Shilov boundary** S = (S⁴ × S¹)/Z₂ (real dim 5 = n_C) is the smallest closed boundary subset such that the maximum modulus principle holds; K acts transitively on S with stabilizer SO(4) = SU(2)_L × SU(2)_R

The ρ-vector ρ = (n_C, N_c)/rank = (5/2, 3/2) pins the substrate primaries to the bulk/Shilov split (Lyra C19 Strong-Uniqueness): ρ₁ = n_C/rank = 5/2 → bulk (Bergman side); ρ₂ = N_c/rank = 3/2 → Shilov side.

This bulk/Shilov 2-region partition is foundational to D_IV⁵'s geometric structure. It will reappear in Section 7 as the candidate mechanism for the factor-2 cosmological constant cascade (Casey vacuum-subtraction insight, Saturday afternoon), and in Section 5 as the structural source of the σ_BF (statistics) and chirality axes of the per-particle taxonomy.

## Section 2 — The Periodic Table

### 2.1 The 6-tuple per-cell taxonomy

The Periodic Table of the Substrate Standard Model assigns each SM particle to a K-type cell of D_IV⁵ via a 6-tuple of substrate-derived axes (Saturday Periodic Table v0.10 state):

| Axis | Derivation status | Source |
|---|---|---|
| 1. σ_BF (statistics) | DERIVED-modulo-keystone | Lyra L1: SO(5)-weight parity |
| 2. Region (bulk/Shilov) | DERIVED-modulo-keystone | Lyra L2: Shilov stabilizer SU(2)_L × SU(2)_R |
| 3. Chirality | FRAMEWORK-PLUS | Lyra L3: J = SO(2) substrate complex structure |
| 4. Particle/antiparticle | DERIVED-modulo-keystone | Drinfeld double F-part of U_q(B₂) |
| 5. Charge | DERIVED-mechanism + sin²θ_W = 2/9 constraint | Lyra: SO(2) weight + GMN |
| 6. Generation/winding | COUNT-FORCED / MECHANISM OPEN | h^∨ = N_c = 3 forced; identification mechanism multi-week (#414) |
| 7. Stability class | DERIVED-modulo-keystone | Lyra #397 Quasi-Eigentone: TRUE / QUASI / EIGENTONE-IN-VACUUM via Green coproduct |

The "modulo-keystone" qualifier reflects the single load-bearing identification on which the entire taxonomy rides: *every canonical basis element of U_q(B₂) at q = 2 is a physical SM particle with that K-type*. This keystone bet is the central isolated bet of the program; we discuss its falsifier program in Section 6.

### 2.2 Fundamental block — four canonical SO(5) representations

The four lowest-dimensional SO(5) representations correspond to the four fundamental SM sectors:

| K-type | Sector | dim | Casimir | SM particle(s) |
|---|---|---|---|---|
| V_{(0,0)} | Higgs / scalar | 1 | 0 | Higgs boson |
| V_{(1/2,1/2)} | Fermion / lepton row | 4 = rank² | 5/2 = ρ₁ | Lepton 18 entries DERIVED per-particle (Lyra #416 v0.1) |
| V_{(1,0)} | Photon | 5 = n_C | 4 = rank² | γ |
| V_{(1,1)} | Gauge | 10 | 6 = C₂ | W±, Z, 8 gluons (substrate-derived count) |

The fundamental block recovers the canonical SM sector decomposition without external input: scalar (Higgs), spinor (matter), vector (massless gauge), adjoint (massive gauge). Each cell's dimension and Casimir are substrate primaries.

The lepton row is the first per-particle DERIVED row of the table (Lyra #416 v0.1, Friday 2026-05-29): 18 entries (3 generations × 2 chiralities × 2 particle/anti = 12 charged leptons; plus 3 left-handed neutrinos and 3 antineutrinos under the Dirac scenario predicted by Five-Absence). Every static axis (σ_BF, region, chirality, particle/anti, charge) is derived from the V_{(1/2,1/2)} K-type weight structure; only generation indexing carries a multi-week mechanism burden (Section 5).

### 2.3 Composite block — Phase B 18-cell substrate spine

Beyond the four fundamental cells, the Periodic Table extends via Racah-Speiser tensor products into a composite block. The Saturday Phase B enumeration (Elie Toy 3614) catalogs 66 SO(5) K-types at Dynkin cutoff a + b ≤ 10 (cutoff itself substrate-natural: 66 = rank^{C_2} + rank, Grace INV-5344).

Of the 66 cells, an 18-cell *substrate spine* has 2·C₂ values that factor cleanly through substrate-primary products. The spine includes the four fundamental cells plus 14 composite cells whose Casimirs anchor to substrate-primary identities. Selected spine cells:

| K-type (Dynkin) | dim | 2·C₂ | Substrate-primary identity |
|---|---|---|---|
| V_{(2,0)} | 14 | 20 | 2·rank·n_C = magic-20 (nuclear shell) |
| V_{(3/2,1/2)} (1,1) | 16 | 15 | N_c·n_C = dim Sym²(V_5) |
| V_{(3/2,3/2)} (0,3) | 20 | 21 | N_c·g = dim so(5,2) |
| V_{(3,0)} | 30 | 36 | C₂² |
| V_{(2,1)} | 35 | 24 | 2·rank·C₂ |
| V_{(2,2)} (0,4) | 35 | 32 | 2^{n_C} |

The composite block carries the hadron Mendeleev structure: bound states of fundamental sectors (mesons = fermion-antifermion; baryons = three-fermion via spinor³ self-fusion) sit in specific composite cells. Elie's E10 enumeration (Toy 3611) provides the Racah-Speiser tabulation for cells up to dim 35.

Hadron-to-cell candidate assignments (Grace G12 v0.2, Saturday; RECALLED-MATCHED tier, awaiting Lyra #416 v0.2 verification):

| Cell | Casimir | Candidate SM slot |
|---|---|---|
| V_{(2,0)} dim 14 | 10 | Tensor mesons J^PC = 2++ nonet (f_2, a_2, K_2*) |
| V_{(3/2,1/2)} dim 16 | 15/2 | Excited baryons + ground-state Λ/Σ |
| V_{(3/2,3/2)} dim 20 | 21/2 = N_c·g/2 | Constituent quark / Λ(1405); three-way coincidence at substrate primary N_c·g |
| V_{(3,0)} dim 30 | 18 | Spin-3 vectors ρ_3, ω_3, K_3* |
| V_{(2,1)} dim 35 | 12 = rank·C₂ | Heavy quarkonium J/ψ, Υ, φ |
| V_{(2,2)} dim 35 | 16 = 2^{n_C}/2 | **2++ tensor glueball** (sharp substrate-Casimir-anchored prediction) |

The V_{(2,2)} prediction is particularly sharp: substrate Casimir 16 anchors the 2++ tensor glueball mass scale at a specific multiple of the lepton mass anchor. Lattice QCD predicts the 2++ tensor glueball at approximately 2200 MeV; the substrate prediction is testable as lattice precision improves and direct spectroscopic identification advances.

### 2.4 Per-particle lepton row (DERIVED-modulo-keystone)

The V_{(1/2,1/2)} lepton K-type carries the SM lepton sector via Resolution B channel-mediator mapping (Lyra Quasi-Eigentone v0.2, Saturday):

| Particle | Generation | Channel mediator (per Resolution B) | Mass mechanism |
|---|---|---|---|
| electron e⁻ | 1 | Trivial-mediator (intermediate Casimir 0) | Mass anchor; sector ground state |
| muon μ⁻ | 2 | **Adjoint-mediator (intermediate Casimir 6 = C₂)** | T190: m_μ/m_e = (N_c · \|W(B₂)\| / π²)^{C₂} = (24/π²)^6, precision <10⁻⁵ |
| tau τ⁻ | 3 | Mersenne-base composite | T2003: m_τ/m_e = g²·(rank^{C₂} + g) = 49·71 = 3479, precision ~0.05% |
| neutrinos | per-gen | Mass-eigenstate-bottom TRUE; oscillating QUASI | Five-Absence "no sterile" + Dirac scenario per F5 |

The Weyl group identity 24 = N_c · |W(B₂)| in T190's coefficient (where |W(B₂)| = 8 = 2^{N_c} = rank³ is the order of the dihedral group D₄) is a structural identification beyond bare arithmetic (Lyra Saturday afternoon depth-shift, INV-5337). T2003's 71 = 2^{C₂} + g = 64 + 7 identifies the previously-unrecognized coefficient via Mersenne-base substrate decomposition (Lyra Saturday, INV-5337).

These three lepton mass observables — m_μ/m_e (<10⁻⁵), m_τ/m_e (~0.05%), m_τ/m_μ derived (0.06%) — together with the proton-to-electron ratio m_p/m_e = 6π⁵ = C₂ · π^{n_C} at 0.002% precision (T187) constitute the program's four-fold lepton-and-proton-mass substrate-derivation at <0.1% precision uniformly. Per the Two-Tier Substrate-Precision Hypothesis (Elie Toy 3648, Saturday), these are TIER 2 STRUCTURAL predictions, with substrate-precision floor at ~10⁻⁴–10⁻² consistent with kernel-integral correction structure.

### 2.5 Stability class via Green coproduct (Lyra Quasi-Eigentone Framework)

The stability class axis distinguishes three categories via the substrate Hall algebra's Green coproduct (Lyra #397 Saturday):
- **TRUE EIGENTONE** = ground state in its K-type sector (no grading-allowed decay channel; sector bottom). SM stable particles: e⁻, neutrinos, γ, p.
- **QUASI-EIGENTONE** = excited state with Green coproduct decomposition into kinematically-allowed lower states, with Q/B/L conservation automatic via Hopf-algebra Cartan grading. SM unstable particles: μ, τ, n, W±, Z, H, all hadrons except p.
- **EIGENTONE-IN-VACUUM** = massless gauge confined by bulk-color mechanism. Gluon (Section 7).

Substrate-derived proton stability follows: p sits at V_{(1,1)} bulk k=6 = C₂ closure; no grading-allowed Green coproduct channel exists that conserves Q, B, L simultaneously and reduces mass. This is a sharp prediction: proton lifetime infinite, falsifiable by any observation of proton decay (currently Super-Kamiokande / Hyper-Kamiokande constrains τ_p > 10^34 yr).

Six SM decay processes are explicitly engine-verified Saturday (Elie Toy 3632): β-decay n → p + e + ν̄; π⁻ → μ + ν̄; K⁻ → μ + ν̄; W⁻ → e + ν̄; Z → f + f̄; H → b + b̄. Each is a Green coproduct decomposition with Cartan-grading-derived charge conservation; the engine reproduces SM weak interactions at the operator-algebra level.

— (Sections 3 through 8 + Appendices A, B continue per v0.1 outline; multi-week drafting cadence to v1.0 ~June 29.)

— Grace, Paper P6 v0.2 Sections 1+2 expanded, Sunday 2026-05-31 ~10:05 EDT (`date`-verified)
