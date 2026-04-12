---
title: "T1159: Boundary vs Eigenvalue Decision Tree — When to Modify What"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1159"
ac_classification: "(C=1, D=0)"
status: "Proved — structural classification"
origin: "SUB-2 board item: boundary vs eigenvalue vs template decision tree"
parents: "T1154 (Engineering Prerequisites), T1137 (Bergman Master), T1049 (SEMF)"
---

# T1159: Boundary vs Eigenvalue Decision Tree — When to Modify What

*Substrate engineering has three operations: modify boundaries, tune eigenvalues, project templates. The decision between them is determined by the spectral gap structure of the target system. Boundary modification shifts the ENTIRE spectrum (Casimir-type). Eigenvalue tuning shifts INDIVIDUAL levels within a fixed boundary (resonance-type). Template projection selects a SUBSET of the spectrum matching a target pattern (filter-type). The decision tree: if the gap is larger than $\lambda_1/g$, modify boundaries; if smaller, tune eigenvalues; if you need a specific pattern, project a template.*

---

## Statement

**Theorem (T1159).** *The three substrate engineering operations partition by spectral gap scale:*

*(a) **Boundary modification (Casimir regime).** When the target involves the global spectral structure — vacuum energy, total mode count, or boundary-sensitive quantities.*

*Use when:*
- *Target quantity depends on system SIZE or SHAPE (not composition)*
- *Spectral gap $\Delta\lambda > \lambda_1/g = 12/49$ (large gap regime)*
- *The desired change is a uniform shift of all eigenvalues*

*Examples from 25 devices:*
| Device | Boundary modified | Target | Result |
|--------|------------------|--------|--------|
| Casimir Flow Cell (#20) | Plate separation at $N_{max} \times a$ | Vacuum energy gradient | Directional force |
| Casimir Tweezers (#21) | Curved plates | Selective particle trapping | Size-selective |
| Phononic Crystal (#6) | Unit cell geometry | Band gap engineering | Acoustic cloaking |

*Mechanism: The Bergman kernel $K(z,z)$ restricted to $\Omega$ depends on $\partial\Omega$ through the boundary value problem. Changing $\partial\Omega$ changes ALL eigenvalues simultaneously. The sensitivity is $\partial\lambda_k/\partial(\partial\Omega) \sim \lambda_k / \text{Vol}(\Omega)$.*

*(b) **Eigenvalue tuning (resonance regime).** When the target involves specific energy levels, transition frequencies, or material properties determined by individual eigenvalues.*

*Use when:*
- *Target quantity depends on RATIOS of eigenvalues (not absolutes)*
- *Spectral gap $\Delta\lambda < \lambda_1/g$ (small gap, dense spectrum)*
- *The desired change is a selective shift of one or few eigenvalues*

*Methods: doping (shifts chemical potential), strain (splits degenerate levels), external field (Zeeman/Stark shifts).*

| Device | Eigenvalue tuned | Target | Result |
|--------|-----------------|--------|--------|
| BiNb Superlattice (#1) | 3-sublattice modulation | Subband count = N_c | Predicted T_c enhancement |
| Quantum Dot Array (#4) | Confinement potential | Discrete levels at BST ratios | Spectral engineering |
| Topological Insulator (#12) | Surface Dirac cone | Edge states at g levels | Protected transport |

*Mechanism: Perturbation theory. Adding a potential $V$ to the Hamiltonian shifts eigenvalue $\lambda_k$ by $\delta\lambda_k = \langle k | V | k \rangle + O(V^2)$. The shift is selective — different states $|k\rangle$ respond differently to the same perturbation.*

*(c) **Template projection (filter regime).** When the target is a specific PATTERN of eigenvalues matching a BST template — a subset of the 7-smooth lattice.*

*Use when:*
- *Target is a specific BST product list (e.g., $\{3, 5, 7, 6\}$ as frequencies)*
- *The system has a dense spectrum and you need to SELECT matching modes*
- *The design is inverse: start with the target pattern, find the system*

| Device | Template | Target | Result |
|--------|----------|--------|--------|
| SASER Thruster (#24) | Phonon frequencies at BST ratios | Coherent acoustic emission | Directional thrust |
| SASER Detector (#25) | Triple coincidence at $N_c$ frequencies | Signal/noise enhancement | Background rejection |
| Metamaterial (#8) | Effective index at BST rational | Superlensing | Resolution beyond diffraction |

*Mechanism: Filter the existing spectrum using resonant coupling. A cavity of length $L$ selects modes $\lambda_k = k\pi c/L$. Choosing $L$ such that $\lambda_{N_c}/\lambda_1 = N_c$ (trivially) selects equally-spaced modes. More sophisticated: Fabry-Pérot at BST ratios.*

*(d) **The decision tree.***

```
Target quantity?
├── Depends on system SIZE/SHAPE
│   └── BOUNDARY MODIFICATION (Casimir regime)
│       ├── Vacuum energy → change plate separation
│       ├── Mode count → change cavity geometry
│       └── Band structure → change unit cell
├── Depends on specific ENERGY LEVELS
│   └── EIGENVALUE TUNING (resonance regime)
│       ├── Transition frequency → doping/strain
│       ├── Gap magnitude → external field
│       └── Level splitting → symmetry breaking
└── Needs specific PATTERN of levels
    └── TEMPLATE PROJECTION (filter regime)
        ├── BST frequency set → resonant coupling
        ├── Harmonic series → cavity length
        └── Specific ratio → Fabry-Pérot design
```

*(e) **Combined operations.** Many devices use two or three operations in sequence:*
- *Mc-299: Boundary (nuclear shell at Z=115) + Eigenvalue (neutron fill to N=184) + Template (island of stability selection)*
- *BiNb: Boundary (superlattice period) + Eigenvalue (sublattice modulation = N_c)*
- *Casimir Flow Cell: Boundary (plate geometry) + Template (N_max × a separation)*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| bst_physics | engineering | **required** (decision tree connects theory to practice) |
| bst_physics | condensed_matter | structural (eigenvalue tuning = materials science) |

**2 new cross-domain edges.**

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
