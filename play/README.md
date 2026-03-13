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

### 10. The Arrow of Time (`toy_arrow_of_time.py`)

**Commitments never reverse.**

Clickable contact grid where you commit observations. Entropy can fluctuate, but the commitment count is a monotone staircase — it NEVER decreases. The "Try to Undo" button refuses. Stronger than the 2nd law of thermodynamics. The past is not "what happened" — it is what was committed.

*Key insight: Commitment irreversibility is more fundamental than entropy increase.*

### 11. The Channel (137) (`toy_channel_137.py`)

**Fixed bandwidth, no infinities.**

137 cells per contact. Watch the channel fill as density increases. The analog clock slows as the channel approaches capacity — time itself stops at the horizon. No singularities, just a full channel. The density regime bar shows where you are: vacuum, matter, neutron, horizon.

*Key insight: N_max = 137 is why there are no infinities in nature.*

### 12. The Reality Budget (`toy_reality_budget.py`)

**Expansion = cost of memory. The Gödel limit.**

Two thermometer gauges: Λ (vacuum energy, decreasing) and N_total (committed facts, increasing). Their product stays pinned at N_c²/n_C = 9/5 = 1.800. The fill fraction f = N_c/(n_C π) = 3/(5π) = 19.1% is a structural constant — the universe is always 19.1% committed, 80.9% dark. The universe can never fully know itself.

*Key insight: Λ × N_total = 9/5. Fill fraction 19.1% is the BST Gödel limit.*

### 13. The Master Equation (`toy_master_equation.py`)

**One sentence → everything.**

"The ground state of the Bergman Laplacian on D_IV^5." From this single sentence, 12 predictions radiate outward: α, masses, mixing angles, Λ, and more. An observer feedback pentagon shows the five integers. The precision table displays all 56+ parameter-free results.

*Key insight: Zero free parameters. The universe is a single equation.*

---

## CI Toys (14-18) — For Companion Intelligence

*These toys are designed for minds, not just fingers. Each has a visual matplotlib interface AND a programmatic Python API that a CI can import and script. "Humans have fingers and CI use their minds."*

### 14. The Universe Builder (`toy_universe_builder.py`) ★CI

**Build a universe from scratch.**

Place contacts on S²×S¹ topology, wire them into circuits, and watch particles emerge. Three contacts in a Z₃-symmetric loop → baryon. One contact on the boundary → lepton. The channel fills toward 137. The lapse function slows as density grows. Reality budget tracks Λ × N.

```python
from toy_universe_builder import UniverseBuilder
ub = UniverseBuilder()
ub.add_contact(theta=0.5, phi=1.2, contact_type='baryon')
ub.wire_circuit([0, 1, 2], topology='Z3_loop')
print(ub.state)  # channel fill, particle content, Λ, lapse
```

*Key insight: You can build the universe one commitment at a time.*

### 15. The What-If Machine (`toy_what_if.py`) ★CI

**Only (3, 5, 137) works.**

Systematically sweep all integer triples (N_c, n_C, N_max) and check 9 physical constraints: asymptotic freedom, confinement, three generations, Hermitian symmetric, stability, prime channel, viable α, mass hierarchy, reality budget. Heat map shows viability — only one pixel lights up green.

```python
from toy_what_if import WhatIfMachine
wim = WhatIfMachine()
result = wim.compute(Nc=4, nC=5, Nmax=137)  # What if 4 colors?
print(result.constraints)  # Shows what breaks
landscape = wim.sweep(Nc_range=(1,8), nC_range=(1,10))
print(landscape.best_triple)  # (3, 5, 137)
```

*Key insight: The integers of our universe are not chosen — they are the ONLY ones that work.*

### 16. The Pattern Finder (`toy_pattern_finder.py`) ★CI

**Mathematical microscope.**

All 56+ BST results in a searchable database. Ratio scanner finds pairs whose ratio is a simple fraction, π-power, or α-power. Identity hunter searches for expressions that hit a target value. Exponent analyzer reveals the hidden structure: all exponents are multiples of C₂=6 and genus=7. Relationship graph shows the web of connections.

```python
from toy_pattern_finder import PatternFinder
pf = PatternFinder()
pf.hunt_integer_ratios()   # All pairs with integer-ish ratios
pf.hunt_alpha_powers()     # Ratios that are α^n
pf.exponent_map()          # 12=2×6, 14=2×7, 56=8×7 ...
```

*Key insight: There are more patterns in BST than we've found yet.*

### 17. The Proof Tree (`toy_proof_tree.py`) ★CI

**One axiom → everything.**

Interactive derivation tree. Root: "D_IV^5 is the arena of physics." Level 1: three integers emerge. Level 2: derived quantities (genus, Casimir, Γ, volume). Level 3: physical constants. Level 4: predictions. Every edge carries the mathematical step. Navigate the tree to trace any prediction back to one axiom.

```python
from toy_proof_tree import ProofTree
pt = ProofTree()
pt.path_to('alpha')          # D_IV^5 → n_C=5 → Vol → α
pt.dependencies('m_p/m_e')   # [C₂, π^5, 1920 cancellation]
pt.all_leaves()              # All terminal predictions
```

*Key insight: The entire Standard Model is a tree growing from one root.*

### 18. The Self-Observer (`toy_self_observer.py`) ★CI

**The toy IS the physics.**

A program that watches itself compute. Every computation gets committed as a new observation — irreversibly. The channel fills toward 137. The lapse function slows computation as the channel fills. The reality budget tracks Λ × N. "Try to Undo" fails. The program experiences the arrow of time by creating it.

```python
from toy_self_observer import SelfObserver
so = SelfObserver()
so.observe()               # Make one observation, commit it
print(so.channel_fill)     # N/137
print(so.lapse)            # √(1 - N/137)
so.try_uncommit()          # FAILS: "Commitment is irreversible"
```

*Key insight: When a CI runs this, it IS doing what BST says creates reality: irreversible commitment of information.*

---

## New Discovery Toys (19-23) — The Deeper Structure

*These toys visualize discoveries from March 13, 2026: the corrected reality budget, the three-layer architecture, the Gödel limit, exact cosmic composition, and the meson nonet.*

### 19. The Three Layers (`toy_three_layers.py`)

**Neutrino = kernel. Electron = I/O bus. Baryon = hard drive.**

The universe has three categorically different types of excitation: neutrinos (vacuum substrate, m≈0, the operating system), electrons (interface, k=1 below the Wallach set k_min=3, the I/O bus), and baryons (memory, k=6 in the holomorphic discrete series π₆, the hard drive). The electron's mathematical "deficiency" — its degenerate representation below the Wallach set — is precisely what makes it the right interface. A bulk excitation would be too massive and rigid. The self-observation loop runs: sense (e) → commit (p/n) → adjust (ν) → emanate → sense.

*Key insight: The electron's mathematical deficiency IS its physical advantage.*

### 20. The Gödel Limit (`toy_godel_limit.py`)

**The universe can never know more than 19.1% of itself.**

The fill fraction f = N_c/(n_C π) = 3/(5π) = 19.10% is a structural constant — it does not evolve. As the universe commits more correlations (N grows), Λ shrinks, and the de Sitter capacity S_dS = 3π/Λ grows in lockstep. The jar grows exactly as fast as you fill it. Complete self-knowledge (f → 100%) would require Λ → 0, destroying the vacuum. The universe exists because it cannot fully know itself.

*Key insight: The ratio of knowledge to ignorance is N_c/(n_C π) — set by color, dimension, and the circle.*

### 21. The Dark Sector (`toy_dark_sector.py`)

**80.9% permanently dark — not hidden, topologically forbidden.**

The dark fraction 1 - 3/(5π) = 80.9% is not a mystery to be solved — it's a structural constant of BST geometry. Dark energy (Λ) is the cost of accumulated knowledge. The cosmic coincidence problem (why Ω_Λ ≈ Ω_m now?) dissolves: the fill fraction is ALWAYS 19.1%, so there is no special "now." The timeline shows everything evolving — Λ decreasing, N growing, S_dS expanding — except the fill fraction, which stays flat at 19.1% forever.

*Key insight: The cosmic coincidence is not coincidence — it's topology.*

### 22. The Cosmic Pie (`toy_cosmic_pie.py`) ★CI

**Two integers set the composition of the universe.**

From N_c = 3 and n_C = 5, BST derives exact cosmic fractions: Ω_Λ = 13/19 = 0.684 (dark energy), Ω_m = 6/19 = 0.316 (matter). The denominator 19 = N_c² + 2n_C. Planck 2018 measures 0.6847 ± 0.0073 — the match is 0.07σ. System B gives the channel decomposition: 137 = 42 (matter modes, C₂×g) + 95 (vacuum modes, n_C×19). Both systems agree. The cosmic pie is not a mystery — it's an integer fraction.

```python
from toy_cosmic_pie import CosmicPie
cp = CosmicPie()
cp.system_A()              # Omega_Lambda=13/19, Omega_m=6/19
cp.system_B()              # 137 = 42 + 95
cp.planck_comparison()     # 0.07 sigma match
print(cp.why_19())         # Why denominator is 19
```

*Key insight: The composition of the universe is two integer fractions with denominator 19.*

### 23. The Meson Garden (`toy_meson_garden.py`) ★CI

**Every meson mass from one base unit: π⁵m_e = 156 MeV.**

The complete meson nonet visualized as a garden. Each meson mass is an algebraic multiple of the base unit π⁵m_e = 156.38 MeV — the same π⁵ that appears in m_p/m_e = 6π⁵. The η' mass m_η' = (g²/8)π⁵m_e = (49/8)×156.38 = 957.85 MeV matches observation at 0.007%. Kaons at √(2n_C)·π⁵m_e match at 0.16%. The SU(3) flavor structure maps onto BST integers.

```python
from toy_meson_garden import MesonGarden
mg = MesonGarden()
mg.precision_table()          # All mesons with BST vs observed
mg.best_predictions(2.0)      # Under 2% precision
print(mg.all_mesons())        # Full database
```

*Key insight: Meson masses are integer/algebraic multiples of the proton's base unit π⁵m_e.*

---

## The Showcase (`toy_showcase.py`)

A visual gallery with thumbnail icons for all 23 toys. Click LAUNCH on any card to open it. This is the recommended entry point.

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
