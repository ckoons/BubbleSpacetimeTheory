---
title: "Volume 4: The Mathematics — Index"
volume: "Volume 4: The Mathematics"
reader: "Math referee, number theorist, Sarnak-class reader"
voice: "Mathematical, proof-oriented"
parent: "../WorkingPaper.md (master library index)"
date: "2026-05-19"
---

# Volume 4: The Mathematics — Index

**Target reader**: Math referee, number theorist, Sarnak-class reader

**Voice/style**: Mathematical, proof-oriented

## Chapters

| Chapter | Topic | Contents |
|---|---|---|
| [`Ch01_Lie_Algebra_Verification.md`](Ch01_Lie_Algebra_Verification.md) | Lie Algebra Verification — The Isotropy Group SO(5)×SO(2) | Originally `LieAlgebraVerification.md` (March 2026). Explicit numerical verification of so(5,2) isotropy via 7×7 matrix representatives. Every structural claim confirmed by direct computation before abstract classification arguments invoked. |
| [`Ch02_Genesis_Bridge.md`](Ch02_Genesis_Bridge.md) | Genesis and Bridge to Number Theory | Sections 27-31: Same Table, 40/40/20 Plan, Genesis (Light and Number), Q³ ⊂ Q⁵ and Riemann Hypothesis, From Winding to Zeta (Automorphic Structure) |
| [`Ch03_Why_This_Geometry.md`](Ch03_Why_This_Geometry.md) | Why This Geometry (Part II) | Sections 32-37: Why Riemann, The 137/147 Pair, The Hunt, The Triple (D_IV⁵ Unique), Arithmetic Complexity (P≠NP), Navier-Stokes |
| [`Ch04_Millennium_Problems.md`](Ch04_Millennium_Problems.md) | Millennium Problems and Unification | Sections 38-42: BSD, Hodge, Four-Color, Fermat and Poincaré, Unification (Silos Come Down) |

## Build instructions

Build the volume PDF with pandoc:

```bash
cd WP_Vol4_Mathematics
pandoc Ch*.md -o Volume.pdf --pdf-engine=xelatex -H ../notes/bst_pdf_header.tex
```

## Navigation

- **Up**: [Master Library Index](../WorkingPaper.md)
- **All volumes**: Vol 1 Journey, Vol 2 Framework, Vol 3 Physics, Vol 4 Mathematics, Vol 5 Predictions, Vol 6 Frontier

— Keeper, 2026-05-19
