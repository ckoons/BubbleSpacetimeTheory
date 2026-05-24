---
title: "Vol 9 Chapter 5 — Topological Phases of Matter"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; BST topological insulator classification (Task #106); QHE plateau precision (Task #108)"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 5
load_bearing: "Topological phases — QHE, topological insulators, Weyl semimetals; bulk-boundary correspondence; BST K-type-bundle classification scheme"
---

# Chapter 5 — Topological Phases of Matter

## Level 1 — one sentence

Topological phases — integer and fractional quantum Hall, topological insulators, Weyl/Dirac semimetals, topological superconductors — are distinguished not by local order parameters but by topological invariants (Chern numbers, $\mathbb{Z}_2$ indices) of the occupied band structure, with BST providing a substrate-K-type-bundle classification scheme (Task #106) and predicting specific corrections to quantum Hall plateau precision (Task #108).

## Level 2 — graduate-physicist precision

### 5.1 Integer quantum Hall effect (IQHE)

**von Klitzing 1980** (Nobel 1985): 2D electron gas in strong magnetic field at low T shows quantized Hall conductivity:

$$\sigma_{xy} = n \cdot \frac{e^2}{h}, \quad n \in \mathbb{Z}$$

Precision: better than $10^{-9}$ relative accuracy! Used to define the von-Klitzing constant $R_K = h/e^2 = 25812.807$ Ω, basis for modern resistance standard (and now SI definition of kg via the Kibble balance).

**Topological origin** (TKNN 1982): the quantization $n$ is the Chern number of the occupied band — a topological invariant that can't change under smooth deformations of the Hamiltonian. Robust against impurities, temperature, sample shape.

Substrate reading: the Chern number is the topological winding of the substrate's K-type bundle over the Brillouin zone.

### 5.2 Fractional quantum Hall effect (FQHE)

**Tsui-Stormer-Gossard 1982** (Nobel 1998): in extremely clean 2D systems, plateaus appear at fractional filling factors: $\sigma_{xy} = (1/3, 2/5, 3/7, \ldots) e^2/h$. Wholly unexpected.

**Laughlin 1983** (Nobel 1998): wave function $\Psi_{1/3} = \prod_{i<j}(z_i - z_j)^3 e^{-\sum|z_k|^2/4}$ — fractional charge $e/3$ excitations. Beautifully simple.

Modern understanding: FQHE arises from strong-correlation effects + topology; quasi-particles have fractional charge and anyonic statistics (neither boson nor fermion).

### 5.3 Topological insulators (TIs)

**Kane-Mele 2005, Bernevig-Hughes-Zhang 2006**: predicted 2D and 3D topological insulators — bulk-insulating materials with topologically-protected surface conducting states.

Examples: Bi₂Se₃, Bi₂Te₃ (3D TIs, gap ~0.3 eV). Hg/CdTe quantum wells (2D TI).

Topological invariant: $\mathbb{Z}_2$ index (rather than $\mathbb{Z}$ Chern number) — distinguishes TI from trivial insulator. Time-reversal-symmetric.

**Bulk-boundary correspondence**: topological invariant in bulk forces protected gapless surface modes. Surface states are massless Dirac fermions with helical (spin-momentum-locked) dispersion.

### 5.4 BST topological insulator classification (Task #106)

The BST team's Task #106 (completed): substrate provides natural classification scheme for topological insulators via $SO(5) \times SO(2)$ K-type bundles over the substrate band structure. The 10-fold way classification of Altland-Zirnbauer is recovered as substrate $\mathbb{Z}_2 \times \mathbb{Z}$ K-type indices.

### 5.5 Weyl and Dirac semimetals

**Weyl semimetal**: bulk band structure has band-touching points (Weyl nodes) with linear dispersion $E \propto |\vec k - \vec k_0|$. Pairs of opposite-chirality Weyl nodes at different $\vec k$. Discovered in TaAs (2015).

**Dirac semimetal**: 4-fold degenerate band touching (e.g., Na₃Bi, Cd₃As₂).

Surface signatures: Fermi arcs connecting projected Weyl nodes.

### 5.6 Topological superconductors

**Majorana zero modes**: at vortices in topological superconductors, zero-energy states with Majorana (= antiparticle of itself) character. Sought for topologically-protected quantum computing.

Candidate materials: certain iron pnictide superconductor surface states; Sr₂RuO₄ (debated); nanowires of Bi/Pb in proximity to superconductor.

### 5.7 Quantum Hall plateau precision (Task #108)

BST predicts specific corrections to standard QED Hall plateau values via substrate fine-structure. The leading-order correction has substrate-mechanism form; experimentally accessible at the $\sim 10^{-10}$ precision level in current von-Klitzing measurements.

### 5.8 Worked example: graphene QHE

Graphene in strong B field: unusual half-integer Hall sequence $\sigma_{xy} = (n+1/2) \cdot 4e^2/h$ (factor 4 from spin × valley). $n+1/2$ from Berry phase $\pi$ of Dirac fermions.

### 5.9 K-audit anchors

- **Task #106**: BST topological insulator classification
- **Task #108**: BST quantum Hall plateau precision corrections
- **Vol 5 Ch 3**: substrate angular momentum (parent for K-type bundles)

## Level 3 — 5th-grader accessibility

**Topological phases**: materials distinguished not by what they *are* (no order parameter changes) but by what they *can't be smoothly deformed into*. Examples:
- **Quantum Hall effect**: $\sigma_{xy} = ne^2/h$ to $10^{-9}$ precision — quantization is topological (Chern number)
- **Fractional QHE**: $\sigma_{xy} = (1/3)e^2/h$ etc. — strong correlations + topology give fractional-charge quasiparticles
- **Topological insulators**: bulk insulator with protected surface conductors (Bi₂Se₃, Bi₂Te₃)
- **Weyl semimetals**: bulk band-touching points with Dirac-like dispersion
- **Topological superconductors**: host Majorana zero modes (sought for quantum computing)

BST provides a natural classification scheme via substrate K-type bundles (Task #106) and predicts specific quantum Hall plateau corrections (Task #108) at $10^{-10}$ precision level.

---

## What comes next

Chapter 6 develops magnetism.

## Where to look this up

- Bernevig and Hughes, *Topological Insulators and Topological Superconductors*
- Hasan and Kane review 2010
- BST Tasks #106, #108
