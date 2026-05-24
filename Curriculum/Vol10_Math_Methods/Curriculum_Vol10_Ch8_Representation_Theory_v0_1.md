---
title: "Vol 10 Chapter 8 — Representation Theory"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — LOAD-BEARING; Wallach representations; K-types; Cartan-Weyl theory"
volume: "Vol 10 Mathematical Methods (for BST)"
chapter: 8
load_bearing: "Representation theory; K-types; Wallach 1976 unitary representations; particle physics + condensed matter applications"
---

# Chapter 8 — Representation Theory

## Level 1 — one sentence

Representation theory expresses abstract groups as concrete linear actions on vector spaces, with irreducible representations the building blocks — and the BST substrate's Wallach 1976 unitary representations of $SO_0(p,2)$ supported on bounded symmetric domains organize the substrate's K-type spectrum that anchors particle masses (Vol 2 Ch 6) and the substrate operator zoo (Vol 5).

## Level 2 — graduate-physicist precision

### 8.1 Representations

A representation $\rho: G \to GL(V)$ of group $G$ on vector space $V$ is a homomorphism: $\rho(g h) = \rho(g)\rho(h)$.

**Irreducible**: no proper invariant subspaces. **Completely reducible**: every rep is a direct sum of irreducibles (true for compact, semisimple, finite groups).

**Character** $\chi_\rho(g) = \text{Tr}\,\rho(g)$: invariant under conjugation; complete invariant for rep.

### 8.2 Compact Lie group representation theory

For compact Lie group $K$: every irreducible representation is finite-dimensional and unitarizable. Classified by highest weights (Cartan-Weyl theory).

**Weyl character formula**: $\chi_\lambda$ in terms of highest weight $\lambda$ and Weyl group.

### 8.3 SO(5) and SO(5)×SO(2) representations

For $SO(5)$ (rank 2): irreducible reps labeled by highest weights $(\lambda_1, \lambda_2)$ with $\lambda_1 \ge \lambda_2 \ge 0$ integers (or half-integers for spinor reps).

Dimensions via Weyl formula. Casimir eigenvalues: $C_2(\lambda) = \lambda_1(\lambda_1+3) + \lambda_2(\lambda_2+1)$.

The (1,1) rep has Casimir = $4 + 2 = 6$ = BST primary $C_2$. The (1,0) "vector" has $C_2 = 4$. The (1/2, 1/2) "spinor" has $C_2 = 15/4 + 3/4 = 9/2$.

For $SO(5) \times SO(2)$: pairs (SO(5) highest weight) × (SO(2) weight $k$). K-types of BST.

### 8.4 Wallach representations

**Wallach 1976**: constructed family of unitary representations of $SO_0(p,2)$ supported on bounded symmetric domains. Each is realized on a Bergman-type space.

For BST $SO_0(5,2)$: Wallach family organizes into 5 layers (corresponding to BST primary $n_C = 5$). Used to anchor particle mass hierarchy via Wallach layer index (Vol 2 Ch 6).

### 8.5 Applications

- Standard Model particles classified by representations of $SU(3) \times SU(2) \times U(1)$
- Atomic spectroscopy: SO(3) angular momentum reps give multiplet structure
- Nuclear shell model: SU(3) Elliott model
- Condensed matter: lattice group reps classify band structure
- BST: $SO_0(5,2)$ Wallach reps anchor everything

### 8.6 K-audit anchors

- **Wallach 1976** (L1 ESTABLISHED): unitary reps on bounded symmetric domains
- **Vol 5 Ch 1**: K-type decomposition of substrate Hilbert space
- **Vol 2 Ch 6**: mass hierarchy from Wallach layer index

## Level 3 — 5th-grader accessibility

**Representation theory**: how abstract groups act on vector spaces. **Irreducible** reps = basic building blocks. For Lie groups: classified by **highest weights** (Cartan-Weyl). For SO(5): irreducible reps labeled by $(\lambda_1, \lambda_2)$. The (1,1) rep has Casimir = 6 = BST primary $C_2$. **Wallach 1976**: classified unitary reps of $SO_0(p,2)$ on bounded symmetric domains. BST uses Wallach's classification to organize the substrate's K-type spectrum. Particle masses follow Wallach layer index (Vol 2 Ch 6).

---

## What comes next

Chapter 9 develops special functions.

## Where to look this up

- Fulton and Harris, *Representation Theory*
- Wallach 1976
- BST: Vol 5 Ch 1; Vol 2 Ch 6
