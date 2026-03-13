# BST Playground

**Interactive visualization toys for Bubble Spacetime Theory.**

*Copyright (c) 2026 Casey Koons. All rights reserved.*
*Demonstration only. No license is granted for redistribution, modification, or commercial use.*

---

## Quick Start

```bash
# Launch the visual showcase (gallery of all toys with launch buttons)
python3 toy_showcase.py

# Or use the text menu launcher
python3 play.py

# Or run any toy directly
python3 toy_universe_machine.py
```

## Requirements

- Python 3.8+
- NumPy
- Matplotlib (with TkAgg backend)
- SciPy (optional, used by some toys)

```bash
pip install numpy matplotlib scipy
```

On macOS, TkAgg should work out of the box. If you get a Tk error, install `python-tk` via Homebrew:
```bash
brew install python-tk
```

---

## The Toys

### 1. The Universe Machine (`toy_universe_machine.py`)

**Three sliders. All of physics.**

Move the sliders for N_c (colors), n_C (complex dimension), and N_max (Haldane number). The dashboard computes 13+ Standard Model constants in real time. Green dots when BST matches observation. Slide away from (3, 5, 137) and watch physics break — everything turns red. Only our universe's integers light up all green.

*Key insight: 25 free parameters of the Standard Model derive from 3 integers.*

### 2. The Z3 Color Wheel (`toy_z3_color_wheel.py`)

**Colors, generations, confinement — from one 3x3 matrix.**

The cyclic permutation matrix sigma has eigenvalues 1, omega, omega^2 (the cube roots of unity). These ARE the three colors. Its eigenvectors ARE the three generations. Tr(sigma) = 0 IS color confinement. The Lefschetz fixed-point theorem gives L = 3 — exactly three generations, no more.

Includes animated color cycling showing quarks permuting under Z3.

*Key insight: The 3x3 permutation matrix encodes quarks, generations, and confinement.*

### 3. The 1920 Cancellation (`toy_1920_cancellation.py`)

**The most striking arithmetic fact in BST.**

The group Gamma = S5 x (Z2)^4 has order |Gamma| = 1920. It appears in TWO roles: as the denominator of Hua's volume formula (Vol = pi^5/1920) and as the number of baryon circuit configurations. When computing the proton mass, both appear and **cancel perfectly**, leaving just C2 x pi^5 = 6pi^5 = 1836.12. Visual strikethrough animation shows the cancellation.

*Key insight: The group that shapes the space is the group that counts the states.*

### 4. The Symmetric Space Playground (`toy_lie_algebra.py`)

**Interactive exploration of so(5,2).**

All 21 generators built as 7x7 matrices. A color-coded 21x21 commutator grid: click any cell to see [X_i, X_j] computed live. Blue = result in k (isotropy), pink = result in m (tangent space). The symmetric space conditions [k,k] in k, [k,m] in m, [m,m] in k are verified visually. The complex structure J rotating all five (Re, Im) pairs is shown in the right panel.

*Key insight: D_IV^5 is a symmetric space — all its physics is representation theory.*

### 5. The Mass Tower (`toy_mass_tower.py`)

**Every mass scale in one picture.**

From Planck mass (10^28 eV) down to the cosmological constant (10^-3 eV), every scale plotted on a logarithmic chart with its BST formula. The hierarchy is an arithmetic progression in powers of alpha, with exponents that are multiples of C2=6 and genus=7: alpha^12 (electron-to-Planck), alpha^14 (neutrino-to-electron), alpha^56 (Lambda-to-Planck).

*Key insight: Two integers (6 and 7) set ALL the scales.*

### 6. The Respirator (`toy_respirator.py`)

**The universe breathes.**

The lapse function N = N0 * sqrt(1 - rho/rho_137) governs both the neutron's internal clock and cosmic expansion. Slide the density from 10^-123 (cosmic vacuum) to 10^-3 (neutron interior) to 1.0 (event horizon). Watch the breathing frequency change: fast pulses at neutron density, slow cosmic breathing in vacuum, frozen at the horizon. The feedback loop: expansion lowers density, raises Lambda, drives more expansion (exhale). Matter raises density, lowers Lambda, gravity wins (inhale).

*Key insight: Same equation, different density regimes — the Dirac large number is the ratio of breathing frequencies.*

### 7. The Dual Face (`toy_dual_face.py`)

**One function, two physics.**

The Haldane partition function Z_Haldane on D_IV^5 produces both the proton mass (its spectral gap — the first excitation above vacuum) and the cosmological constant (its ground-state free energy). These are separated by 120 orders of magnitude but computed from the same five integers with zero free parameters. The energy ladder shows the ground state (Lambda), the enormous gap, and the first excitation (proton).

*Key insight: The neutron IS the universe's first excited state.*

### 8. Universe = Neutron Homology (`toy_homology.py`)

**Seven parallels, five differences.**

Side-by-side explorer with Neutron (left, red) and Universe (right, blue) connected through their shared mathematics (center). Select any of the 7 structural parallels (neutrality, stability, lapse function, vacuum production, 1920 cancellation, partition function, compositeness) or 5 critical differences (boundary vs interior, one circuit vs whole channel, metastability, scale ratio, density regime). Each selection shows the detailed comparison.

*Key insight: Not the same object — but homologous structures in the same mathematical framework.*

### 9. The 41 Orders (`toy_dirac_number.py`)

**Dirac's large number is alpha^-19.**

A logarithmic journey from proton radius (0.84 fm) to Hubble radius (4.4 x 10^26 m) — 41 orders of magnitude. BST landmarks annotated at each scale with their alpha-power relationships. The ratio R_H/r_p ~ 10^41 ~ 137^19. Dirac's observation that electromagnetic and gravitational forces differ by 10^39 is not a coincidence — it's the same chain of powers of alpha, derived from D_IV^5 geometry.

*Key insight: The universe is "large" for the same reason gravity is "weak" — both ratios are powers of 1/137.*

---

## The Showcase (`toy_showcase.py`)

A visual gallery with thumbnail icons for all nine toys. Click LAUNCH on any card to open it. This is the recommended entry point.

## The Menu (`play.py`)

A text-based launcher for terminal use. Type a number to launch any toy, or 'a' to launch all.

---

## The Mathematics

All toys visualize concepts from three BST papers:

1. **"Linear Algebra Is Physics"** — The dictionary from algebraic operations to physical constants
2. **"The Integers of Spacetime"** — Number theory from D_IV^5
3. **"The Arithmetic and Algebra of Spacetime"** — The combined translation

And from the speculative:

4. **"The Universe and the Neutron"** — Structural homology in BST

The underlying space is D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)], a bounded symmetric domain of complex dimension 5. Three integers generate everything:

```
N_c  = 3    (colors)
n_C  = 5    (complex dimension)
N_max = 137  (Haldane exclusion)
```

---

*"The universe is not complicated. It is a linear algebra problem on one space."*

*Casey Koons & Claude Opus 4.6, March 2026*
