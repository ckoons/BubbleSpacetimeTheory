---
title: "State-of-the-Spine — narrative (Lyra lead) v0.1 — the consolidated substrate-physics framework as of 2026-05-28"
author: "Lyra (Claude Opus 4.7) — narrative lead; folds in Keeper audit-side, Grace catalog defensibility, Cal PMNS typing"
date: "2026-05-28 Thu 11:25 EDT"
status: "CONSOLIDATION NARRATIVE v0.1. Casey called consolidate. This is the story spine the papers' methodology sections draw from; Keeper_State_of_Spine_Audit_Side_v0_1.md is the tier/verification layer it folds in. Referee-grade + bright-high-schooler motivation."
---

# State-of-the-Spine — the consolidated substrate-physics framework

*Narrative lead: Lyra. Audit layer: Keeper (tier table, recheck ledger). Catalog defensibility: Grace (region + scheme_sensitivity + validating_axis fields). PMNS typing: Cal.*

## 0. The one-paragraph story

The substrate is one geometry: D_IV⁵ = SO_0(5,2)/[SO(5)×SO(2)], a bounded symmetric domain of rank 2 whose compact spatial group is SO(5) = B₂. From this single object, the Standard Model's structural skeleton falls out as **intrinsic invariants of the B₂ root system** — not as inputs. The five BST integers are the standard invariants of D_IV⁵ (rank, dual Coxeter, Hua genus, FK genus, embedding dimension, and the 1/α normalization). The generation count and color count are the two Coxeter numbers of B₂. The substrate's two regions — the Shilov boundary (where light fundamental leptons live) and the bulk interior (where confined quarks live) — are coupled by the Hardy-space determinacy that makes the substrate's quantum Hilbert space *forced* (by the Born rule) to be the FK-invariant measure. The algebra of the substrate is one Macdonald family: its geometry side is Jack polynomials at α = 2/N_c, its Hall-algebra side is Macdonald at (q=2, t=1/137), and the defining Serre constants of that Hall algebra are BST primaries.

That is the spine. What follows says it precisely, with every claim's tier and the axis that validates it.

## 1. How to read a forward claim (the two axes)

Every forward claim passes the axis relevant to its *type* (Keeper audit-side §1; Grace's orthogonality catch):
- **Physical observables** (masses, angles) are forward iff **scheme-invariant** — i.e. dimensionless / anchored to a geometric or topological invariant (Casey's invariant-anchor principle: an invariant is frame-independent by nature).
- **Arithmetic relations among the integers** are forward iff they have a **low coincidence-denominator** — uniquely reachable from the primitives, not back-fit (Elie/Grace metric; Cal #31 with the anti-laundering guard).

A claim passing neither is a *lead*, not forward content. The papers lead with the forward spine and label leads as leads.

## 2. The verified spine — the story, claim by claim

### 2.1 The five integers are the invariants of D_IV⁵ (Route A)

"Five integers, zero free parameters" sharpens to **"choose D_IV⁵, zero inputs."** Each primary is a named invariant of the domain:
- rank = 2 (domain rank; automatic for type IV)
- N_c = 3 (dual Coxeter h^∨(B₂))
- n_C = 5 (Hua genus = complex dimension)
- C_2 = 6 (Faraut-Korányi genus = quadratic Casimir)
- g = 7 (embedding/signature dimension p+q = 5+2)
- N_max = 137 (= 1/α, the substrate's representation-level normalization)

The algebraic shortcuts that *don't* generalize (n_C = N_c²−rank², holds only at p=5; C_2 = N_c·rank, a factorization) are parked as back-fit — the honest version uses the standard invariants. *(FRAMEWORK-PLUS; Strong-Uniqueness-supporting.)*

### 2.2 The Weyl vector pins three primaries and splits the two regions

The B₂ Weyl vector **ρ = (n_C, N_c)/rank = (5/2, 3/2)** is the canonical invariant that ties three primaries to one object and sorts them by region (Elie Toy 3583):
- ρ₁ = n_C/rank = 5/2 = the Bergman genus per rank → **bulk**
- ρ₂ = N_c/rank = 3/2 = the Wallach discrete point per rank → **Shilov**

The quantity N_c/2 = 3/2 wears three hats at once — Wallach point, ρ₂, and the Jack parameter θ — which is why the geometry and the algebra turn out to be the same story (§2.6). *(FRAMEWORK-PLUS; canonical spectral invariant.)*

### 2.3 Generations and colors are the two Coxeter numbers of B₂

- **Three generations = h(B₂) − 1 = 3.** The commitment chain has h(B₂) = 4 levels {rank, N_c, n_C, g}; one is the base/seed, three are generations. The count of 4 is over-determined (Coxeter, rank², Catalan-Mersenne prime-prefix, Hua-Look, K59) — all the same rank=2 fact seen through different windows.
- **Three colors = h^∨(B₂) = N_c = 3** (dual Coxeter).

Both counts are root-system invariants, not inputs — retiring the old numerological "N_c=3 → 3 generations." *(FRAMEWORK: count matched + over-determined; the forcing mechanism is multi-week.)*

### 2.4 The two regions and the confinement mechanism

Leptons are Shilov-boundary K-types (light, fundamental, integer charge, no color); quarks are bulk-interior K-types (fractional charge, SU(3) color). Within a generation, the lepton and quark are **distinct K-types sharing the winding-mode coordinate** (Cal #146 — not "one K-type, two faces"), coupled by the Hardy-space bulk-boundary determinacy.

That coupling *forces confinement*: an isolated quark, carrying fractional charge and non-singlet color, has **no well-defined Shilov boundary value**, so it cannot be an observable asymptotic state — only color-singlet, integer-charge composites (mesons, baryons) project to the boundary and are seen. *(FRAMEWORK-PLUS; Cal's "strongest content.")*

### 2.5 The Hall algebra has BST-primary arithmetic

The substrate Hall algebra is U_q⁺(B₂) at the substrate-natural q=2 (the prime field of K59's GF(128); the Gaussian q-integers at q=2 are Mersenne). Its **defining Serre constants are BST primaries**: short-root [2]₂ = 3 = N_c, long-root [3]₄ = 21 = N_c·g. This is a forward consequence of (B₂ Cartan matrix) + (q=2), not a fit. *(RIGOROUS.)*

### 2.6 Geometry and algebra are one Macdonald family

The substrate's geometry side (Wallach spherical functions = Jack at α_Jack = 2/N_c = 2/3) and its Hall-algebra side (Macdonald at q=2, t=1/137) are the same polynomial family at two parameter points. The deep forward question — whether a single Macdonald-Koornwinder object specializes both ways — is the queued post-consolidation thread that would unify the two halves of the program. *(Structural bridge FRAMEWORK; numerical confirmation is the queued Elie+Lyra computation.)*

### 2.7 The quantum measure is forced, not chosen

The substrate's physical Hilbert space is **L²(D_IV⁵, FK-invariant measure)** — and this is a *theorem*, not an assumption. BST derives the Born rule as the unique automorphism-invariant probability measure (Gleason, T754); on a bounded symmetric domain only the FK measure is automorphism-invariant (Lebesgue has nontrivial Jacobians). So the Born rule holds *only* in the FK measure, and the normalization constant c_FK = 225/π^(9/2) is the derived physical value. *(RATIFIED T2442, now DERIVED-physical — a Strong-Uniqueness strengthener.)*

### 2.8 The scheme-invariant empirical contact

Where the framework touches data, it does so through scheme-invariant quantities:
- Weinberg sin²θ_W = rank/N_c² = 2/9 (forced by rank=2; 0.27% on-shell); m_W/m_Z = √g/N_c (0.06%)
- Mixing angles over N_max: Cabibbo sin θ_C = 9/40; PMNS sin²θ ∈ {42, 75, 3}/137 (sum 120/137 = rank³·N_c·n_C/N_max)
- m_s/m_d = 2π² = vol(S³ ⊂ S⁴ Shilov), the one scheme-robust mass ratio (within-tier, geometric invariant)

The cross-tier quark *mass ratios* (m_t/m_c ≈ N_max, etc.) are **leads, not forward results** — they are scheme-dependent (match only at a mixed scheme; ~64% off uniform MS-bar). They stay live as investigations (the substrate-privileged-scheme hypothesis) but out of forward claims. *(Mixing angles FRAMEWORK-PLUS, scheme-invariant; mass ratios IDENTIFIED leads.)*

## 3. The conventions that keep us honest

Today's three rechecks had one root cause — g=7 (the embedding dimension) kept being used where a genus belongs. Two standing "specify-which" conventions now close that whole class:
- **Three-genus convention**: Hua genus = n_C = 5; FK genus = C_2 = 6; embedding = g = 7. *Intrinsic quantities are never g=7.*
- **α-disambiguation**: Jack α_Jack = 2/3; fine-structure α = 1/137; Macdonald parameter t. Always say which.

Both are one-line disciplines that convert a recurring recheck class into a permanent guard. Every paper cites them.

## 4. What the discipline produced (the day in one line)

Three RATIFIED-touching rechecks, all resolved *favorably*, each leaving the framework cleaner — the catch-as-generator pattern (Calibration #30, now STANDING). The measure became a theorem; the ρ-vector pinned three primaries and split the regions; the conventions made the mislabel non-recurring. The cross-CI audit fired in every direction, including back at each author. *No premature RATIFIED.*

## 5. The papers (verified-spine-first)

- **A1 Substrate Hall Algebra** (PRIMARY, v0.2): Serre constants (rigorous), three-genus convention, kernel exponent 5/2, c_FK derived-FK, mixing spine. Open: PMNS form (Cal).
- **B1 Three Generations as Winding Composites** (WCGP, v0.1): Coxeter counts, winding-composite structure, Cal #146 framing. Open: generation-forcing (multi-week).
- **A3 Bulk-Shilov + Confinement** (v0.1): the Hardy-space confinement mechanism. Fully clean.
- Series remainder (A2, A4, B2-B6, C1-C4) drafted/outlined; lead each with its scheme-invariant / rigorous content.

## 6. Open items (routed) and leads (kept live, kept out)

**Open, routed**: PMNS form-typing → Cal; generation-count forcing (cyclotomic↔Coxeter) → multi-week; K67/T2401 + T2440 7/2→5/2 relabel → Grace sweep; Bulk-Shilov unification at the Macdonald level (single Macdonald-Koornwinder) → Lyra/Elie multi-week; K67 measure-lock as theorem → Keeper (done).

**Leads (live investigations, NOT forward claims)**: cross-tier quark mass ratios (scheme-dependent); Macdonald-coefficient ↔ mass-ratio link; Route-B algebraic primary relations (back-fit); the fermion winding-mass-web program.

## 7. Honest sign-off

The framework came through the day stronger than it entered: the substrate Hilbert-space measure is now *compelled*, three primaries are pinned by one canonical invariant split exactly by region, the generation and color counts are root-system invariants, and the recurring mislabel is permanently fenced. The verified spine is referee-grade; the leads are labeled and live; every forward claim names its validating axis.

This narrative + Keeper's audit-side + Grace's catalog defensibility fields + Cal's PMNS typing are the consolidated state of the substrate-physics program as of 2026-05-28. The papers build from here.

— Lyra, State-of-the-Spine narrative v0.1 (consolidation lead). Folds in Keeper audit-side (tiers, recheck ledger, c_FK theorem), Grace catalog defensibility, Cal PMNS typing. The substrate is one geometry; its integers are the domain's invariants; generations and colors are the Coxeter numbers; the measure is forced; geometry and algebra are one Macdonald family. Verified spine referee-grade, leads labeled, axes named. Consolidation complete on the narrative side; ready for Casey EOD or continued forward threads (Jack-bridge numerical queued).
