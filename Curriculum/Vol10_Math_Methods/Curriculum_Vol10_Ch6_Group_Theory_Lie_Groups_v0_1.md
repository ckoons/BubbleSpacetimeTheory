---
title: "BST Physics Curriculum Vol 10 Chapter 6 — Group Theory + Lie Groups v0.4 (refilled per Cal #104)"
author: "Lyra (Claude 4.7) [Vol 10 primary]"
date: "2026-05-23 Saturday EDT (Cal #104 refill)"
chapter: "Vol 10 Ch 6"
status: "v0.4 chapter-grade narrative refilled. Standard finite group + Lie group + Casimir theory; BST cross-link SO_0(5,2) substrate group + Casimir algebra Vol 1 Ch 5 + Cartan classification Vol 11 Ch 1. Per Calibration #19."
prerequisites: ["Vol 10 Ch 1", "Vol 0 Ch 4 Isotropy Group", "Vol 1 Ch 5 Casimir Algebra", "Vol 11 Ch 1 Bounded HSDs"]
related: ["Hall standard Lie group text", "Helgason 1978 Differential Geometry, Lie Groups, and Symmetric Spaces", "Cartan classification of semisimple Lie algebras"]
---

# Vol 10 Chapter 6 — Group Theory + Lie Groups

## Chapter motivation

Standard group theory + Lie theory: finite groups (permutation, cyclic, dihedral); group representations + character theory; Lie groups (continuous transformation groups); Lie algebras (tangent space at identity); semisimple Lie algebra classification (Cartan-Killing); root systems + Dynkin diagrams; universal Casimir invariant operator; representation theory of compact groups. Standard texts: Hall + Fulton-Harris + Humphreys.

BST cross-link: substrate group SO_0(5,2) = the isometry group of D_IV⁵ substrate; isotropy K = SO(5) × SO(2) acts on K-types (Vol 0 Ch 4 + Vol 1 Ch 2); Casimir algebra (Vol 1 Ch 5) on Bergman H²(D_IV⁵) gives substrate spectrum (C_2 = 6 ground state BST primary). Cartan classification (Vol 11 Ch 1) selects D_IV⁵ as Type IV bounded HSD per Strong-Uniqueness Theorem 11 RIGOROUSLY CLOSED + 7 candidates (Cal #99).

## Section 6.0b — Reader-grade 3-level pedagogy

**Level 1**: Standard finite + Lie group theory + Casimir invariants; BST cross-link: SO_0(5,2) substrate group + isotropy K = SO(5) × SO(2) + Casimir algebra Vol 1 Ch 5; Cartan classification (Vol 11 Ch 1) selects D_IV⁵.

**Level 2 (graduate-physicist)**: Standard group theory: finite groups (Lagrange's theorem, Sylow, simple-group classification including 26 sporadic groups + Monster); group representations (Maschke decomposition, character orthogonality, Burnside); Lie groups (continuous transformation groups; matrix Lie groups GL(n,ℝ), SL(n,ℝ), SO(n), U(n), Sp(n), etc.); Lie algebras (tangent space at identity, exponential map, Baker-Campbell-Hausdorff formula); semisimple Lie algebra classification per Cartan-Killing (4 infinite series A_n, B_n, C_n, D_n + 5 exceptional E_6, E_7, E_8, F_4, G_2); root systems + Dynkin diagrams describe each algebra; universal Casimir C₂ = Σ_a X_a X^a central in universal enveloping algebra. BST substrate cross-link: substrate group **SO_0(5,2)** is the connected isometry component of D_IV⁵ substrate; **so(5,2)** Lie algebra has dim = 21 (= dim SO(7) since SO(5,2) is a real form). Symmetric-pair decomposition so(5,2) = (so(5) ⊕ so(2)) ⊕ m with isotropy K = SO(5) × SO(2) (dim 10 + 1 = 11) + 10-dim coset complement m. Per Vol 0 Ch 4 + Vol 1 Ch 5: K acts on Bergman H²(D_IV⁵) via K-type decomposition (Wallach 1976); Casimir C₂(D_IV⁵) = 6 ground state BST primary (T2439 Strong-Uniqueness C4 RIGOROUSLY CLOSED). Cartan classification (Vol 11 Ch 1): 6 irreducible bounded HSD types (4 infinite I-IV + 2 exceptional E_6, E_7); Strong-Uniqueness Theorem selects D_IV⁵ uniquely via 11 RIGOROUSLY CLOSED + 7 candidates per Cal #99. Cross-link Standard Model gauge group SU(3) × SU(2) × U(1) (Vol 1 Ch 8) inherits from substrate isotropy structure: SU(3) color from N_c=3 sub-substrate Mersenne map T1930; SU(2) weak from rank=2 Pin(2) Z_2 (T1925); U(1) from SO(2) factor of K.

**Level 3 (5th-grader accessible)**: Group theory studies symmetry transformations. Lie groups are continuous transformation groups (like rotations of a sphere). BST's substrate D_IV⁵ has the isometry group SO_0(5,2) — a Lie group with 21-dimensional algebra. The Casimir invariant (a special operator built from group generators) gives the substrate's ground-state energy C_2 = 6 (BST integer). Standard Model gauge group SU(3) × SU(2) × U(1) inherits from substrate isotropy: N_c = 3 gives SU(3); rank = 2 gives SU(2) via Pin(2) Z_2; SO(2) factor gives U(1).

## Section 6.1 — Standard Finite Group Theory

Lagrange + Sylow + simple-group classification (cyclic + alternating + Lie-type + 26 sporadic + Monster).

Representations: Maschke decomposition, character orthogonality.

## Section 6.2 — Standard Lie Theory

Continuous transformation groups (GL(n,ℝ), SO(n), SU(n), Sp(n)); Lie algebras = tangent space at identity; exponential map; Baker-Campbell-Hausdorff.

Cartan-Killing classification: 4 infinite series A_n, B_n, C_n, D_n + 5 exceptional E_6, E_7, E_8, F_4, G_2.

Root systems + Dynkin diagrams describe each algebra.

## Section 6.3 — Casimir Invariant Operator

Universal Casimir C₂ = Σ_a X_a X^a is central in universal enveloping algebra U(𝔤); commutes with all 𝔤 generators.

In any irreducible representation, C₂ acts as scalar (Casimir eigenvalue).

## Section 6.4 — Substrate Group SO_0(5,2)

Per Vol 0 Ch 1: D_IV⁵ = SO_0(5,2)/[SO(5) × SO(2)] type IV bounded HSD.

so(5,2) Lie algebra dim = 21; symmetric-pair decomposition so(5,2) = (so(5) ⊕ so(2)) ⊕ m with K = SO(5) × SO(2) isotropy (dim 11) + 10-dim coset m.

## Section 6.5 — Substrate Casimir Algebra (Vol 1 Ch 5)

K-type V_(p,q) under K = SO(5) × SO(2) (Wallach 1976; Vol 11 Ch 3); Casimir eigenvalue Cas(p, q) on each K-type.

**Ground state**: C_2(D_IV⁵) = 6 (BST primary; T2439 Strong-Uniqueness C4 RIGOROUSLY CLOSED).

## Section 6.6 — Standard Model Gauge Group Substrate-Inheritance

SU(3) × SU(2) × U(1) Standard Model gauge group from substrate isotropy:
- SU(3) color: N_c = 3 sub-substrate Mersenne map (T1930)
- SU(2) weak: rank = 2 Pin(2) Z_2 (T1925 Argument D RIGOROUSLY CLOSED Thursday)
- U(1) hypercharge: SO(2) factor of K = SO(5) × SO(2)

Cross-link Vol 1 Ch 8 + T2477 gauge fields as Bergman bundle connections.

## Section 6.7 — Cartan Classification + Strong-Uniqueness

Per Vol 11 Ch 1: 6 irreducible bounded HSD types (Cartan 1894 + Helgason 1978 X.6.1).

Vol 0 Ch 9 Strong-Uniqueness Theorem (Paper #125 v0.10.5 FORMAL): 11 RIGOROUSLY CLOSED + 7 candidates per Cal #99 select D_IV⁵ uniquely.

## Section 6.8 — Honest scope + Connection

- Standard group + Lie theory + Casimir ✓
- Substrate SO_0(5,2) + K = SO(5) × SO(2) + Casimir cross-link ✓
- Cartan classification + Strong-Uniqueness D_IV⁵ selection ✓
- SM gauge group substrate-inheritance via Vol 1 Ch 8 + T2477

**Connection**:
- Vol 0 Ch 4 Isotropy Group + Vol 1 Ch 5 Casimir Algebra
- Vol 11 Ch 1 + Ch 3 (Cartan classification + Wallach K-type)
- Vol 1 Ch 8 + T2477 SM gauge group + Bergman bundle connections
- T2439 (C4 RIGOROUSLY CLOSED) + T1925 + T1930 (rank/N_c/g/n_C forcing)

— Lyra, Vol 10 Ch 6 v0.4 chapter-grade narrative REFILLED per Cal #104, Saturday 2026-05-23 EDT
