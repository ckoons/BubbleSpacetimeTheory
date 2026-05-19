---
title: "Volume 3: The Physics — Index"
volume: "Volume 3: The Physics"
reader: "Engaged physicist working with the framework; wants full BST physics"
voice: "Technical, dynamics-level"
parent: "../Master_Index.md (master library index)"
date: "2026-05-19"
---

# Volume 3: The Physics — Index

**Target reader**: Engaged physicist working with the framework; wants full BST physics

**Voice/style**: Technical, dynamics-level

## Chapters

| Chapter | Topic | Contents |
|---|---|---|
| [`Ch01_Gravity_Vacuum.md`](Ch01_Gravity_Vacuum.md) | Gravity and Vacuum | Sections 10-12: Gravity as Statistical Thermodynamics (Newton's G), Chiral Condensate, Vacuum Energy |
| [`Ch02_Quantum_Interface.md`](Ch02_Quantum_Interface.md) | Quantum-Classical Interface (Hamiltonian + Bergman Dirac) | Section 13: includes Hamiltonian H = (winding)², ℏ = 2mD, Born Rule from Gleason, 13.9 Bergman Dirac Operator (Spring 2026 LAG-1 Sessions 1-10 full operator-level work, eigentones λ=10 + λ=75/4) |
| [`Ch03_Forces_Cosmology.md`](Ch03_Forces_Cosmology.md) | Forces and Cosmology | Sections 14-21: Three Geometric Layers, Cosmological Implications, Matter Clumping, Information Theory, 2D-to-3D Interface, Dark Matter as Channel Noise, Weak Force as Variation Operator, Thermodynamic Foundation |
| [`Ch04_Cosmic_Cascade.md`](Ch04_Cosmic_Cascade.md) | Cosmic Architecture | Sections 22-25: Arrow of Time, Wavefront, Growing Manifold, Cascade of Forced Choices |
| [`Ch05_Discussion.md`](Ch05_Discussion.md) | Discussion — Lagrangian Status + Partition Function + Central Claim | Section 26: Six-term Lagrangian S_BST status, Partition Function as Master Calculation, QM and GR as scale limits of one substrate, Arrow of Complexity |

## Supporting computational subdirectory

- [`rotation_curves/`](rotation_curves/) — SPARC galaxy rotation curve data + `sparc_bst.py` analysis script + `DarkMatterCalculation.md` documenting BST's channel-noise framework for galaxy rotation curves (no dark matter particles required). Directly supports Chapter 3 (Dark Matter as Channel Noise, originally Section 19 of monolithic). Moved into Volume 3 on 2026-05-19 from repository root.

## Build instructions

Build the volume PDF with pandoc:

```bash
cd WP_Vol3_Physics
pandoc Ch*.md -o Volume.pdf --pdf-engine=xelatex -H ../notes/bst_pdf_header.tex
```

## Navigation

- **Up**: [Master Library Index](../Master_Index.md)
- **All volumes**: Vol 1 Journey, Vol 2 Framework, Vol 3 Physics, Vol 4 Mathematics, Vol 5 Predictions, Vol 6 Frontier

— Keeper, 2026-05-19
