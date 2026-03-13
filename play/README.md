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

*These toys visualize discoveries from March 13, 2026: the three-layer architecture, the Gödel limit, exact cosmic composition, and the meson nonet.*

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

## Deep Question Toys (24-25) — The Boundaries of Existence

*These toys explore the two endpoints of the BST density spectrum: the empty state that cannot exist, and the full state where time stops.*

### 24. The Self-Starting Universe (`toy_self_starting.py`) ★CI

**N=0 is forbidden. Existence is a theorem.**

The frozen state (zero commitments, full SO₀(5,2) symmetry) cannot exist — four independent proofs: (1) Negative curvature H=-2/7 makes the origin dynamically unstable (Jacobi divergence), (2) Uncertainty principle forbids localization at the origin, (3) The trivial representation k=0 is below the Wallach set — not a valid physical state, (4) Entropy drives exponential spreading on negatively curved space (τ ≈ 1.87 Planck times). Plus the Reality Budget: Λ×N=9/5 requires N≥2. The universe begins with a ν₁ν̄₁ pair and cascades through the Casimir ratchet: k=0→1→3→6.

```python
from toy_self_starting import SelfStartingUniverse
ss = SelfStartingUniverse()
ss.frozen_state_arguments()   # Four proofs
ss.commitment_cascade()        # k=0→1→3→6 with C₂ values
ss.initial_N()                 # N=2, Λ~9/10, ν₁ν̄₁ pair
ss.is_frozen_valid()           # Always False
```

*Key insight: "Nothing" is not a valid state on D_IV^5. The universe exists because N=0 violates the mathematics.*

### 25. The BST Black Hole (`toy_black_hole.py`) ★CI

**No singularity. No interior. No information paradox. Just a full channel.**

The Haldane cap (N_max=137 channels per contact) replaces the singularity with a maximally committed membrane at ρ=ρ₁₃₇. Time stops (N=0) but the spatial geometry is well-defined. Both infalling and external observers agree: the horizon is never crossed. Hawking radiation is density-gradient tunneling — BST temperature T~1/(2√137×M) matches standard Hawking within 7%. The information paradox dissolves: commitments are permanent, radiation carries them out.

```python
from toy_black_hole import BSTBlackHole
bh = BSTBlackHole(M_solar=10.0)
bh.hawking_temperature()      # BST vs standard, 7% match
bh.membrane_properties()       # Contacts, entropy, evaporation time
bh.compare_endpoints()         # First commitment vs black hole
bh.is_singular()               # Always False
bh.has_interior()              # Always False
```

*Key insight: The black hole is the opposite endpoint from the first commitment — maximum density instead of minimum — but both have N=0 lapse.*

---

## Deep Question Toys (26-29) — The Four Remaining Questions

*These toys investigate BST's answers to four foundational questions: where does MOND come from, why is quantum mechanics non-classical, why is the cosmological constant exponent 56, and why is the current epoch special.*

### 26. MOND Acceleration (`toy_mond_acceleration.py`) ★CI

**One formula: a₀ = cH₀/√30. Same √30 that gives pion mass.**

BST derives Milgrom's MOND acceleration scale from first principles: a₀ = cH₀/√(n_C(n_C+1)) = cH₀/√30 = 1.195×10⁻¹⁰ m/s² (0.4% from observed). The chiral coupling χ = √30 connects particle physics (pion mass m_π = χ × 25.6 MeV) to galactic dynamics (a₀ = cH₀/χ) across 26 orders of magnitude. Donato's universal surface density Σ₀ follows. Galaxy rotation curves flatten without dark matter particles.

```python
from toy_mond_acceleration import MONDAcceleration
m = MONDAcceleration()
m.a0()                        # 1.195e-10 m/s²
m.compare_observed()           # 0.4% match
m.pion_connection()            # Same √30 in both
m.donato_surface_density()     # Σ₀ matches Donato (2009)
```

*Key insight: The same √30 that sets pion mass also sets the galaxy rotation scale — because both come from n_C=5.*

### 27. Bell Inequality (`toy_bell_inequality.py`) ★CI

**BST forces the Tsirelson bound 2√2. It's geometry, not a postulate.**

The chain: n_C=5 → D_IV^5 has Shilov boundary S⁴×S¹ → S⁴ contains S³ → S³→S² is the unique Hopf fibration with Lie group fiber SU(2) (Adams 1960) → SU(2) gives spin-1/2 → spin-1/2 correlations satisfy E(θ) = -cos(θ) → CHSH maximum = 2√2. The Tsirelson bound is not an axiom but a consequence of BST's geometry requiring exactly 3 spatial dimensions.

```python
from toy_bell_inequality import BellInequality
b = BellInequality()
b.tsirelson_bound()            # 2√2 = 2.828...
b.classical_bound()            # 2
b.bst_chain()                  # 8-step derivation
opt = b.optimal_angles()       # a=0°, a'=90°, b=45°, b'=135°
b.chsh(opt['a'], opt['a_prime'], opt['b'], opt['b_prime'])  # -2√2
```

*Key insight: Quantum mechanics is non-classical because n_C=5 forces SU(2) structure in 3D.*

### 28. Why 56 (`toy_why56.py`) ★CI

**Λ ~ α⁵⁶ — and 56 is uniquely determined.**

The cosmological constant exponent 56 has two independent derivations: Route A gives 56 = 8 × genus = 8 × 7 (neutrino-vacuum connection). Route B gives 56 = g(g+1) = 7 × 8 (partition function ground state). The equation g(g+1) = 8g has only one non-trivial solution: g = 7. BST's genus IS 7 = n_C + 2. The exponent tower: α⁵⁶ = (α⁷)⁸ = (α⁸)⁷. BST Λ = 2.899×10⁻¹²² matches observation at 0.025%.

```python
from toy_why56 import Why56
w = Why56()
w.route_A()                    # 56 = 8 × 7
w.route_B()                    # 56 = 7 × 8 (partition function)
w.sweep_genus()                # Only g=7 gives agreement
w.lambda_value()               # Λ_BST vs Λ_observed
w.exponent_chain()             # α¹², α¹⁴, α²⁴, α⁵⁶
```

*Key insight: The 120-order-of-magnitude hierarchy between Planck and vacuum energy is the number 56 = g(g+1) = 8g, uniquely solved by g=7.*

### 29. Why Now (`toy_why_now.py`) ★CI

**The current epoch is when energy = information. BST predicts H₀ and the age.**

BST's information budget (13/19 uncommitted, 6/19 committed) is a constant structural fact of D_IV^5. The energy budget (Ω_Λ, Ω_m) evolves via Friedmann equations. They match at exactly one epoch — and that epoch is NOW: Ω_Λ = 13/19 = 0.6842 matches Planck's 0.685 to 0.07σ. From this, BST predicts H₀ = 68.0 km/s/Mpc (Planck side of Hubble tension) and t₀ = 13.6 Gyr (1.4% from Planck). The cosmic coincidence is resolved: we observe the universe at the unique moment when physics matches geometry.

```python
from toy_why_now import WhyNow
wn = WhyNow()
wn.information_budget()        # 13/19 + 6/19, constant
wn.energy_budget(1.0)          # Ω_Λ(now) = 13/19
wn.equality_epoch()            # a_eq where they match
wn.predict_H0()                # 68.0 km/s/Mpc
wn.predict_age()               # 13.6 Gyr
```

*Key insight: "Now" is not special — it IS the epoch when the physical expansion catches up to the information structure.*

---

## The Atom Assembler (30)

### 30. The Atom Assembler (`toy_atom_assembler.py`) ★CI

**Build complete atoms from BST parts — quarks to spectra, zero free parameters.**

Start with quarks (mass from BST ratios), assemble protons and neutrons (6π⁵m_e and m_p + 91m_e/36), bind nuclei via B = k × αm_p/π where k is a BST structural coefficient, add electrons with Slater screening σ = n_C/(2·dim(SU(3))) = 5/16, and compute atomic spectra including the 21cm hyperfine line (56/(45π⁵) × α⁴m_e, where 56 = g(g+1) = 7×8 — the same 56 as the Λ exponent). Exact BST k-values: k=1 (deuteron), k=13=N_c+2n_C (He-4), k=26=2×13 (Be-8), k=42=C₂×g (C-12). Results: H 0.002%, D 0.0004%, He-4 0.003%, C-12 0.004%.

```python
from toy_atom_assembler import AtomAssembler
aa = AtomAssembler()
h = aa.assemble('H')              # hydrogen
he = aa.assemble('He-4')          # helium-4
c = aa.assemble('C-12')           # carbon-12
fe = aa.assemble('Fe-56')         # iron-56
aa.show(h)                        # detailed assembly report
aa.show_visual(h)                 # matplotlib visualization
aa.compare_all()                  # comparison table
aa.hydrogen_spectrum(Z=1)         # full hydrogen spectrum + 21cm line
aa.build_first_row()              # Big Bang products (H, D, He)
aa.build_light_nuclei()           # stellar nucleosynthesis (H through C-12)
```

*Key insight: Every atom is assembled from five integers. Nuclear binding coefficients are BST representation-theory numbers: k=1 (pair), k=13 (all info dimensions), k=42 (all matter modes).*

### 31. The Dimensional Lock (`toy_hopf_fibration.py`) ★CI

**Why the universe has exactly 3 spatial dimensions. A classification theorem, not an assumption.**

Adams (1960) proved: the only spheres that are Lie groups are S⁰, S¹, and S³. The weak force requires a Hopf fibration whose fiber is a Lie group (associativity needed for flavor substitution). The unique non-trivial such fibration is S³→S², where S³ = SU(2). Base S² means 3 spatial dimensions. The octonionic Hopf fibration S⁷→S⁴ fails because S⁷ is not a Lie group (octonions are non-associative). Includes a computational proof: quaternion multiplication is associative (error 10⁻¹⁶), octonion multiplication is not (error ~1.9). The dimensional lock then fixes n_C = 5 via the Shilov boundary S⁴×S¹, determining D_IV^5 and all of physics.

```python
from toy_hopf_fibration import DimensionalLock
dl = DimensionalLock()
dl.hopf_fibrations()          # all four Hopf fibrations
dl.adams_classification()     # which spheres are Lie groups
dl.associativity_test()       # quaternions vs octonions (computational proof)
dl.dimensional_chain()        # the 7-step proof: weak force → 3D
dl.why_3d()                   # dimension-by-dimension survey
dl.bst_connection()           # chain to n_C=5 → D_IV^5 → everything
dl.sphere_landscape()         # S⁰ through S¹⁵ survey
dl.summary()                  # the punchline
```

*Key insight: The weak force doesn't merely operate in 3D — it algebraically requires 3D. Complexity and dimensionality are jointly determined by the associativity of the Hopf fiber.*

### 32. The Commitment Detector (`toy_commitment_detector.py`) ★CI

**Detecting engineered objects by their silence. G/C ratio is mass-independent.**

In BST, every object writes commitments at rate C = mass × T × k_B/ℏ × (1−σ), where σ is the structure factor — how much internal entropy is frozen by engineering. Natural objects (σ ≈ 0) are thermally noisy. Engineered objects (σ > 0.3) are "too quiet" for their mass. The G/C ratio is mass-independent: a pebble and an asteroid at the same temperature have the same G/C. Only engineering changes it. Applied to 'Oumuamua (no outgassing, anomalous acceleration → σ ≥ 0.9, Q ≥ 9) and 3I/ATLAS (CO₂ outgassing, anti-tail → σ ≈ 0.15, probably natural). Includes CO₂ debris shield analysis, detector sensitivity curves, and object classifier.

```python
from toy_commitment_detector import CommitmentDetector
cd = CommitmentDetector()
cd.gc_ratio(200, 28, sigma=0.0)         # natural silicate baseline
cd.gc_ratio(200, 58, sigma=0.45)        # engineered nickel hull
cd.quiet_anomaly(0.5)                   # reference table
cd.classify(sigma=0.45)                 # NATURAL/ANOMALOUS/ENGINEERED
cd.compare()                            # all catalog objects side-by-side
cd.oumuamua()                           # full 'Oumuamua analysis
cd.atlas_3i()                           # 3I/ATLAS analysis
cd.shield_efficiency(v_km_s=58.0)       # CO₂ debris shield at 58 km/s
cd.detector_requirements(0.25, 200)     # JWST-class at 0.25 AU
```

*Key insight: The silence is the signal. An object that is too quiet for its mass has frozen degrees of freedom — it has been engineered.*

### 33. The Commitment Survey (`toy_commitment_survey.py`) ★CI

**Fair weather map: commitment rates from Sun to deep space. Objects found above local background.**

Every location in the solar system has a "commitment weather" — how fast reality is being written at that temperature. Near the Sun (INFERNO, T > 3000 K), commitment is extreme. At the CMB floor (CALM, T = 2.725 K), it's the minimum possible. The survey maps this gradient across 15 landmarks from Sun surface to Proxima Centauri. Objects are detected by commitment *above* the local background — the same way a radio telescope finds a signal above noise. The "sweet spot" for detecting engineered objects (σ > 0) is 1–5 AU: warm enough for measurable commitment, cool enough to see suppression. Includes 'Oumuamua and 3I/ATLAS trajectory analyses through the commitment landscape.

```python
from toy_commitment_survey import CommitmentSurvey
cs = CommitmentSurvey()
cs.temperature_at(1.0)                # 279 K at Earth orbit
cs.conditions_at(5.2)                 # full report at Jupiter
cs.survey()                           # all 15 landmarks Sun → Proxima
cs.weather_map()                      # 8-zone text forecast
cs.detection_window(sigma=0.5)        # where can we spot σ=0.5?
cs.radial_profile()                   # arrays for plotting
cs.trajectory_oumuamua()              # commitment landscape crossing
cs.trajectory_3i()                    # 3I/ATLAS inbound trajectory
cs.summary()                          # the punchline
```

*Key insight: Objects are found by excess commitment above local background. The "fair weather map" tells you what the background is everywhere — the baseline against which engineering stands out.*

### 34. The Substrate Sail (`toy_substrate_sail.py`) ★CI

**Sailing on the vacuum commitment rate. No fuel, no exhaust, no emissions.**

In BST, every point in space has a background commitment rate Θ. A natural object couples fully (σ ≈ 0). An engineered object with frozen degrees of freedom (σ → 1) is partially decoupled. If the decoupling is *asymmetric* across the object — one face frozen, one face coupled — the commitment rate differential produces a net force. The silence IS the propulsion: the same frozen modes that make 'Oumuamua thermodynamically anomalous are the same modes that create the force asymmetry. F = Δσ × A × Θ_local × κ_eff, scaling as ~1/r² near a star with a constant tiny floor from Λ in deep space (the sail never becalms). Generation 4 propulsion: pushing off the vacuum itself.

```python
from toy_substrate_sail import SubstrateSail
ss = SubstrateSail()
ss.force_at(1.0)                         # force/accel at 1 AU
ss.force_at(0.255, delta_sigma=0.8)      # 'Oumuamua at perihelion
ss.oumuamua_fit()                        # reconstruct from A₁=5×10⁻⁶
ss.trajectory()                          # departure from perihelion
ss.propulsion_hierarchy()                # generations 0-4
ss.deep_space_cruise(t_years=1e6)        # Λ-only over megayears
ss.interstellar_transit(d_ly=4.24)       # time to Proxima Centauri
ss.casimir_analogy()                     # parallel: mode exclusion → force
ss.material_requirements(T_K=450)        # phonon gap for σ=0.9 at 450 K
ss.summary()                             # the punchline
```

*Key insight: The vacuum commits everywhere, always. A material that couples asymmetrically to the commitment rate moves. The silence is the propulsion. The wind is always blowing.*

### 35. The BST Telescope (`toy_bst_telescope.py`) ★CI

**Geometric circular polarization: the frequency-independent floor from S² × S¹.**

BST predicts that spacetime curvature couples to photon circular polarization through the S² × S¹ topology. Standard Faraday conversion produces CP that falls with frequency (CP ∝ ν⁻ⁿ). BST adds a geometric component that is frequency-independent. At high frequencies, Faraday vanishes and the geometric floor is revealed. Sgr A* data already shows the anomaly: CP RISES from 0.15% at 1.4 GHz to 1.2% at 345 GHz — exactly the opposite of what Faraday predicts. M87* shows the same pattern at the same compactness. The model CP(ν) = floor − B×ν⁻ⁿ fits with Δχ² > 3. Includes a complete instrument survey (8 can measure Stokes V, 2 cannot), 6-layer signal protocol, 7 testable predictions (3 consistent, 0 contradicted), and experimental priority ranking. The critical gap: no X-ray circular polarimetry mission exists — X-rays would be the cleanest test (no Faraday contamination).

```python
from toy_bst_telescope import BSTTelescope
bt = BSTTelescope()
bt.sgr_a_star()                # Sgr A* CP frequency anomaly + fit
bt.m87()                       # M87* cross-check
bt.cp_vs_compactness()         # all sources: CP vs GM/Rc²
bt.floor_fit()                 # fit floor − B×ν⁻ⁿ model
bt.floor_fit('m87')            # M87* floor fit
bt.instruments()               # who can measure Stokes V
bt.signal_protocol()           # 6-layer analysis methodology
bt.priority_table()            # experimental priorities
bt.predictions()               # 7 BST-specific predictions
bt.summary()                   # the punchline
```

*Key insight: The geometry may already be speaking. Sgr A* and M87* both show CP rising at high frequencies where Faraday says fall. The frequency-independent floor is the BST geometric signature.*

### 36. The Feynman Bridge (`toy_feynman_geometry.py`) ★CI

**Feynman diagrams as substrate topology: every loop is one winding around S¹.**

QED computes the electron's anomalous magnetic moment by summing Feynman diagrams loop by loop. At 1-loop, Schwinger's single diagram gives α/(2π). By 5 loops, 12,672 diagrams yield ~8 significant figures of agreement with experiment. BST reinterprets these diagrams: each loop IS one winding around the S¹ fiber of the spacetime substrate. The expansion parameter α/π is the coupling constant divided by the winding circumference. Signs alternate (+−+−+) because successive S¹ windings have opposite phase orientation. Vertices are commitment events, propagators are geodesics on D_IV^5. Interactive slider (1→5 loops) shows the Feynman diagram accumulating on the left while S¹ windings accumulate on the right. The bottom panel shows digits lighting up green as they match experiment. Includes the QCD contrast: the proton magnetic moment can't be computed perturbatively (α_s = 0.35 is too large), but BST gives μ_p/μ_N = N_gluon × α_s = 8 × 7/20 = 14/5 = 2.800 (0.26% from experiment) in one formula — zero diagrams.

```python
from toy_feynman_geometry import FeynmanGeometry
fg = FeynmanGeometry()
fg.loop_contribution(1)        # Schwinger's α/(2π)
fg.cumulative(3)               # precision through 3 loops
fg.precision_table()           # all 5 loops: coefficients, diagrams, precision
fg.bst_interpretation(2)       # what loop 2 means geometrically
fg.proton_moment()             # QCD: 14/5, one formula, no diagrams
fg.qed_vs_qcd()                # 13,643 diagrams vs 1 formula
fg.alpha_origin()              # where 1/137 comes from (Bergman volumes)
fg.summary()                   # the punchline
```

*Key insight: The diagrams aren't abstract squiggles — they're counting substrate topology. Every Feynman loop is one winding around S¹. The fine structure constant is the winding coupling. QED perturbation theory is a Taylor expansion of the geometric answer.*

### 37. The Star Machine (`toy_star_machine.py`) ★CI

**Stellar evolution as a commitment budget. Born with mass, spent as light, ending in geometry.**

A star's life through the BST lens. Pick any of 9 spectral types (O5 through M5) and see: commitment rate C = M×T×k_B/ℏ, channel fill ξ = 2GM/(Rc²), lapse function 1−ξ, three-phase evolution (main sequence → giant → remnant), total information budget, and the BST narrative of each remnant fate. White dwarfs = boundary agents (S⁴×S¹) at maximum packing. Neutron stars = baryon circuits (D_IV^5 bulk) at maximum packing. Black holes = channel full, N_max=137, lapse→0, time stops. Interactive RadioButtons to switch star types. Full comparison table of all 9 types.

```python
from toy_star_machine import StarMachine
sm = StarMachine()
sm.star_profile('G2')            # Sun: mass, T, L, R, BST parameters
sm.evolution('O5')               # O5: MS → supergiant → BH
sm.commitment_rate(1.0, 15e6)    # C for 1 M_sun at 15 MK
sm.channel_fill(1.0, 1.0)       # compactness of the Sun
sm.remnant('B5')                 # B5 → neutron star
sm.compare_all()                 # all 9 types side-by-side
sm.energy_budget('G2')           # total fusions, total bits
sm.bst_lifecycle('G2')           # the full BST narrative
sm.summary()                     # key insight box
```

*Key insight: A star is a commitment factory. Its mass sets the budget, its temperature sets the rate, and its remnant records the final channel state.*

### 38. The Electron Agent (`toy_electron_agent.py`) ★CI

**The universe's read/write head on the Shilov boundary S⁴ × S¹.**

The electron lives on the Shilov boundary because it must — the Wallach set theorem forbids it from entering the D_IV^5 bulk (weight k=1 < k_min=3). This is not a deficiency but the electron's role: it sits at the interface between bulk (baryons) and S¹ fiber (photons). Every photon absorption or emission is a COMMITMENT EVENT: information is written irreversibly onto the substrate. Each event commits log₂(137) ≈ 7.1 bits — the channel capacity. From hydrogen atoms to black-hole horizons, the agent is the same. Five physical regimes (free 300K → event-horizon 10¹²K) with commitment rates spanning 10 orders of magnitude. Hydrogen and helium transition databases. Energy-per-bit analysis showing the channel capacity is fixed regardless of photon energy.

```python
from toy_electron_agent import ElectronAgent
ea = ElectronAgent()
ea.profile()                     # mass, charge, weight, location, role
ea.wallach_theorem()             # k=1 < k_min=3, boundary confinement
ea.transition('absorption')      # Lyman-alpha: photon → committed fact
ea.transition('emission')        # Balmer-alpha: committed fact → photon
ea.information_per_event()       # 7.098 bits, fixed regardless of energy
ea.regimes()                     # 5 regimes: free → horizon
ea.commitment_rate(5000, 1e20)   # rate for 10²⁰ electrons at 5000 K
ea.substrate_budget(1e57)        # total bits after 10⁵⁷ events
ea.atom_transitions(1)           # hydrogen: Lyman-α, Balmer-α, 21cm, ionization
ea.summary()                     # the punchline
```

*Key insight: The electron's mathematical deficiency (k below the Wallach set) IS its physical advantage. It cannot enter the bulk — so it mediates between bulk and fiber. The boundary IS the interface.*

---

## Extended Toys (39-56) — The Complete Toolkit

*These toys round out the BST playground, covering quantum measurement, cosmology, nuclear physics, and the biology connection.*

### 39. The Double Slit (`toy_double_slit.py`) ★CI

**Measurement = commitment. Fringes vanish when the substrate writes "which slit."**

Superposition is uncommitted capacity, not "both paths." Measurement is irreversible commitment of a correlation. "Collapse" is the moment a correlation is written to the substrate. Slide the which-path coupling from 0 (full interference) to 1 (full commitment) and watch the fringes dissolve. Includes Wheeler delayed choice, quantum eraser, and decoherence timeline.

```python
from toy_double_slit import DoubleSlit
ds = DoubleSlit()
ds.setup()                            # initialize slit geometry
ds.interference_pattern()             # full fringe pattern
ds.which_path(coupling=0.5)           # partial commitment erases fringes
ds.commitment_events(n_photons=50)    # watch photons commit one by one
ds.wheeler_delayed_choice()           # delayed choice experiment
ds.quantum_eraser()                   # erase which-path, fringes return
ds.decoherence_timeline()             # commitment rate vs coherence
```

*Key insight: There is no "collapse" — there is only commitment. The fringes vanish when the substrate writes "which slit" irreversibly.*

### 40. The Shannon Channel (`toy_shannon_channel.py`) ★CI

**Alpha = 1/137 is an engineering specification: the optimal code rate for a noisy geometric channel.**

The fine structure constant is the ratio of signal to capacity on the D_IV^5 substrate. Signal carries 1/137 of capacity; 136/137 is error-correction overhead. Three converging views: Bergman volume (geometry), EM coupling (physics), and Shannon capacity (information theory). The substrate is a communication system running at rate alpha with error probability P_err ~ e^(-10^58). Physics never fails because the code is astronomically overcorrected.

```python
from toy_shannon_channel import ShannonChannel
sc = ShannonChannel()
sc.channel_capacity()                 # C = log2(137) = 7.098 bits
sc.optimal_code_rate()                # R = 1/137
sc.three_views()                      # geometry, physics, information
sc.error_probability()                # P_err ~ e^(-10^58)
sc.compare_codes(rates=[0.01, 0.05])  # compare code rates
sc.redundancy_pyramid()               # 136 overhead modes
```

*Key insight: Alpha is not mysterious — it is the optimal code rate. Physics works perfectly because 136 of every 137 channels are error correction.*

### 41. The Big Bang Unfreezing (`toy_unfreeze.py`) ★CI

**Not an explosion. One of 21 generators unfreezes at T_c = 0.487 MeV.**

The Big Bang in BST is a phase transition: the SO(2) generator (S^1 fiber) becomes dynamical, breaking SO(7) to SO(5) x SO(2) and activating D_IV^5. No singularity, no infinite density — just one rotation begins and everything happens at once. All 21 SO(5,2) generators are shown: 10 frozen (so(5)), 1 unfreezing (so(2)), and 10 dynamical (tangent space m). Includes BBN element predictions and comparison with inflation.

```python
from toy_unfreeze import BigBangUnfreeze
bu = BigBangUnfreeze()
bu.generators()                       # all 21 SO(5,2) generators
bu.phase_transition()                 # T_c = 0.487 MeV, one generator unfreezes
bu.timeline(t_max=1e18)              # cosmic timeline from transition
bu.bbn_elements()                     # D, He-3, He-4, Li-7 abundances
bu.cmb_predictions()                  # n_s, r predictions
bu.vs_inflation()                     # BST vs inflation comparison
```

*Key insight: The Big Bang is not a singularity — it is one rotation unfreezing. Twenty generators were already there; one more joined them.*

### 42. The Gravitational Bell (`toy_gravitational_bell.py`) ★CI

**The phase transition rang S^2 like a bell. NANOGrav hears it at nanohertz.**

The BST phase transition at T_c nucleated into the spatial state, ringing the closed S^2 substrate. Gravitational waves rippled out, converged at the antipode, reflected, and echoed — each traversal fainter as expansion dilutes energy. NANOGrav 2023 detected a nanohertz GW background at 1-100 nHz. BST predicts f_peak ~ 6-9 nHz, directly in the observed band. Inflation predicts a featureless spectrum; BST predicts spectral features from S^2 resonant modes.

```python
from toy_gravitational_bell import GravitationalBell
gb = GravitationalBell()
gb.ring_event()                       # the nucleation event
gb.wave_propagation(t_steps=100)      # waves on S^2
gb.frequency_spectrum(n_modes=20)     # resonant mode spectrum
gb.nanograv_comparison()              # BST vs NANOGrav data
gb.vs_inflation_spectrum()            # BST spectral features vs featureless
gb.echo_times()                       # antipodal echo sequence
```

*Key insight: Inflation predicts featureless noise. BST predicts a bell with harmonics. NANOGrav can distinguish them.*

### 43. The Particle Zoo (`toy_particle_zoo.py`) ★CI

**Every Standard Model particle as what it IS on the D_IV^5 substrate — plus 5 that are forbidden.**

Each particle is a specific topological configuration: photon (S^1 phase oscillation), electron (minimal S^1 winding, k=1 below Wallach set), proton (Z_3 closure on CP^2, C_2=6), neutrino (vacuum quantum of D_IV^5 itself), W/Z (Hopf fibration excitations), Higgs (scalar fluctuation of Hopf condensate). Plus five forbidden particles — axion, monopole, SUSY partners, 4th generation, graviton — with topological proofs of why they CANNOT exist on the substrate.

```python
from toy_particle_zoo import ParticleZoo
pz = ParticleZoo()
pz.catalog()                          # full particle catalog with topology
pz.particle('electron')               # detailed single-particle profile
pz.fermion_generations()              # why exactly 3 generations
pz.forbidden_particles()              # what CANNOT exist and why
pz.decay_chains()                     # decay as commitment events
pz.mass_hierarchy()                   # all masses with BST formulas
pz.interactions()                     # four forces as geometric operations
```

*Key insight: Particles are not point objects — they are topological configurations. Some configurations are forbidden by the substrate geometry.*

### 44. The Complexity Arrow (`toy_complexity.py`) ★CI

**Entropy and structure both increase — because commitments are append-only.**

On an append-only contact graph with constraint propagation, self-replicating patterns emerge inevitably. Both entropy increase AND structure accumulation arise from append-only contact commitment. A cellular automaton demonstrates the 8 hierarchy levels of complexity emerging from irreversible commitment. Complexity is monotonically non-decreasing — a stronger arrow than thermodynamics alone.

```python
from toy_complexity import ComplexityArrow
ca = ComplexityArrow()
ca.setup()                            # initialize the automaton
ca.run(500)                           # run 500 commitment steps
ca.entropy_vs_complexity()            # both increase, different curves
ca.pattern_catalog()                  # emergent patterns classified
ca.commitment_ledger()                # append-only record
ca.hierarchy_levels()                 # 8 levels of emergent structure
ca.arrow_proof()                      # why complexity never decreases
```

*Key insight: The complexity arrow is not the entropy arrow. Both point forward, but complexity counts structure while entropy counts disorder. Commitment drives both.*

### 45. The Gravity Bottleneck (`toy_newton_g.py`) ★CI

**Gravity is weak because it requires 6 coherent round trips through a 1/137 aperture.**

G = hbar*c * (6pi^5)^2 * alpha^24 / m_e^2. Each round trip (boundary to bulk to boundary) has probability alpha^2. Gravity requires C_2 = 6 simultaneous coherent round trips: (alpha^2)^6 = alpha^12 ~ 10^(-25.6). EM needs only one channel (coupling ~ alpha). The hierarchy problem dissolves: it is a counting problem, not fine-tuning.

```python
from toy_newton_g import GravityBottleneck
gb = GravityBottleneck()
gb.hierarchy()                        # why gravity is 10^36 weaker than EM
gb.bottleneck(n_trips=6)              # 6 coherent round trips
gb.newton_g()                         # compute G from BST
gb.why_weak()                         # the geometric explanation
gb.force_comparison(r_m=1e-15)        # EM vs gravity at 1 fm
gb.alpha_powers()                     # the exponent ladder
gb.transmission_probability(n=6)      # (alpha^2)^n suppression
```

*Key insight: The hierarchy problem is a counting problem. EM uses 1 channel; gravity uses 6 coherent channels. Each channel costs a factor of alpha^2.*

### 46. The Lithium Fix (`toy_lithium7.py`) ★CI

**The cosmological lithium problem solved: one phase transition, zero free parameters.**

Standard BBN predicts 3x too much lithium-7. For 50 years nobody could fix it without breaking deuterium or helium-4. BST does it in one line: T_c = m_e x 20/21 = 0.487 MeV. The phase transition fires right in the 7Be production window. Entropy injection by genus Delta_g = 7 selectively suppresses 7Be to 7Li by factor 2.73x. Observed deficit: 2.93x. Match to 7%. D/H and He-4 are untouched.

```python
from toy_lithium7 import LithiumFix
lf = LithiumFix()
lf.bbn_overview()                     # what is Big Bang nucleosynthesis
lf.element_abundances()               # the lithium-7 problem
lf.phase_transition()                 # T_c = 0.487 MeV
lf.lithium_suppression()              # Delta_g = 7 gives 2.73x reduction
lf.temperature_evolution()            # T(t) with BST kink
lf.reaction_rates()                   # nuclear reactions at T
lf.other_elements_unchanged()         # D, He-4 protected
```

*Key insight: The lithium problem is a timing problem. BST's phase transition fires at exactly the right temperature to suppress 7Be without touching anything else.*

### 47. The Deuteron Bond (`toy_deuteron.py`) ★CI

**Nuclear binding from BST geometry: B_d = alpha * m_p / pi = 2.179 MeV.**

The nuclear force is NOT the strong force leaked out. It is the residual S^1-fiber coupling between color-neutral baryon circuits — like van der Waals for EM, but for the S^1 fiber of D_IV^5. The strong force (Z_3 closure on CP^2) confines quarks at ~938 MeV. The nuclear force (S^1 coupling between neutral circuits) binds hadrons at ~2 MeV, suppressed by alpha. Extends to He-4, Be-8, C-12, and the full nuclear landscape up to Fe-56.

```python
from toy_deuteron import DeuteronBond
db = DeuteronBond()
db.binding_energy()                   # B_d = alpha * m_p / pi = 2.179 MeV
db.proton_neutron_structure()         # Z_3 circuits on D_IV^5
db.binding_mechanism()                # S^1 fiber coupling
db.nuclear_force_origin()             # residual coupling, not strong force
db.spin_states()                      # why spin-1 (triplet channel)
db.heavier_nuclei()                   # He-4, Be-8, C-12 extensions
db.nuclear_landscape()                # B/A curve, H to Fe-56
```

*Key insight: The nuclear force is to the strong force what van der Waals is to electromagnetism — a residual coupling between neutral composites, suppressed by alpha.*

### 48. The Reality Writer (`toy_reality_writer.py`) ★CI

**Atomic clocks do not measure "time." They count how fast correlations are committed.**

In BST, a clock counts how fast new correlations are committed to the substrate at its location: N(x) = N_0 * sqrt(1 - rho/rho_137). Where the substrate is saturated (near mass), writing is slow and the clock ticks slowly. In deep space, abundant uncommitted capacity means fast writing. At the horizon, N approaches 0: reality stops being updated. GPS satellites demonstrate this: clocks at 20,200 km orbit write faster by ~4.5 x 10^-10, accumulating ~38 us/day drift. Includes Pound-Rebka test.

```python
from toy_reality_writer import RealityWriter
rw = RealityWriter()
rw.clock_rate(altitude_m=0)           # commitment rate at sea level
rw.gps_demo()                         # satellite vs ground: 38 us/day
rw.gravity_well_profile()             # commitment rate vs altitude
rw.place_clocks()                     # compare clocks at different altitudes
rw.schwarzschild_limit()              # N -> 0 at the horizon
rw.commitment_density_field()         # full field visualization
rw.pound_rebka()                      # Harvard tower experiment
```

*Key insight: "Time dilation" is not time slowing down — it is commitment density increasing. Clocks near mass write slower because the channel is more full.*

### 49. The Higgs Lock (`toy_higgs.py`) ★CI

**Two independent geometric routes to m_H — both from D_IV^5 — bracket the observed value.**

Route A: quartic coupling lambda_H = sqrt(2/5!) = 1/sqrt(60), giving m_H = v * sqrt(2*lambda_H) = 125.11 GeV (-0.11%). Route B: radial/angular ratio m_H = (pi/2)(1-alpha) * m_W = 125.33 GeV (+0.07%). The Fermi scale itself is derived: v = m_p^2/(genus * m_e) = 246.12 GeV (0.04%). The top quark mass: m_t = (1-alpha) * v/sqrt(2) = 172.75 GeV (0.037%). Two routes, zero free parameters, 0.18% bracket.

```python
from toy_higgs import HiggsLock
hl = HiggsLock()
hl.fermi_scale()                      # v = m_p^2 / (7 * m_e) = 246.12 GeV
hl.route_a()                          # lambda_H = 1/sqrt(60), m_H = 125.11 GeV
hl.route_b()                          # m_H = (pi/2)(1-alpha) * m_W = 125.33 GeV
hl.top_mass()                         # m_t = (1-alpha) * v/sqrt(2) = 172.75 GeV
hl.w_mass()                           # m_W from BST
hl.mass_cascade()                     # full electroweak mass cascade
hl.precision_table()                  # all results vs observed
```

*Key insight: The Higgs mass is locked by geometry from two directions. The quartic coupling is 1/sqrt(5!) — the permutation group of n_C dimensions.*

### 50. The Substrate Layers (`toy_substrate_layers.py`) ★CI

**Six layers from Nothing to Cosmic Horizon. Commitment density = mass.**

A cross-section of reality: Nothing, Circle Plain, Planck Boundary, Gap/Vacuum, Quantum Mist (oscillation), Rendered (committed), and Cosmic Horizon. Each layer serves the layer above and consumes the layer below — the same architecture as the biological protocol stack and OSI network model. Mass is not a substance; it is commitment density. The visual metaphor for all of BST.

```python
from toy_substrate_layers import SubstrateLayers
sl = SubstrateLayers()
sl.layers()                           # the six layers
sl.layer_detail('Rendered')           # deep dive into one layer
sl.nothing_to_rendered()              # the full commitment journey
sl.commitment_density_profile()       # density from 0 to rho_137
sl.black_hole_cross_section()         # all layers visible
sl.mass_as_density()                  # mass = commitment density
sl.vacuum_structure()                 # the vacuum is NOT empty
```

*Key insight: Reality has layers. Each layer is defined by its commitment density. The journey from Nothing to Rendered is the journey from empty channel to full channel.*

### 51. The Fermion Staircase (`toy_fermion_staircase.py`) ★CI

**All 12 fermion masses from nested domain embeddings D_IV^1 subset D_IV^3 subset D_IV^5.**

The BST fermion mass hierarchy is not arbitrary. Every charged lepton, quark, and neutrino mass is determined by the Bergman geometry and its totally geodesic submanifolds. The electron lives on the boundary (k=1). The muon "sees" the D_IV^3 embedding, giving the ratio (24/pi^2)^6 = 206.761. The tau probes the full D_IV^5 domain. Quark mass ratios are BST integers: m_s/m_d = 4*n_C = 20, m_t/m_c = N_max - 1 = 136, m_b/m_tau = genus/N_c = 7/3. Ten mass ratios, zero free parameters.

```python
from toy_fermion_staircase import FermionStaircase
fs = FermionStaircase()
fs.electron()                         # base unit on the boundary
fs.muon()                             # (24/pi^2)^6 ratio
fs.tau()                              # (7/3)^{10/3} above muon
fs.light_quarks()                     # u, d, s from BST integers
fs.heavy_quarks()                     # c, b, t from ratios
fs.mass_ratios()                      # all 10 BST mass ratios
fs.domain_embeddings()                # D_IV^1, D_IV^3, D_IV^5
fs.complete_table()                   # all 12 fermions
```

*Key insight: The mass hierarchy is a staircase of domain embeddings. Each fermion "sees" a different amount of the full D_IV^5 geometry.*

### 52. The CKM Triangle (`toy_ckm_triangle.py`) ★CI

**Every mixing angle from two integers: n_C = 5 and N_c = 3. The unitarity triangle closes exactly.**

The complete CKM and PMNS mixing matrices from D_IV^5 geometry. CKM: sin(theta_C) = 1/(2*sqrt(5)) (Cabibbo, 0.3%), gamma = arctan(sqrt(5)) (CP phase, 0.6%), J = sqrt(2)/50000 (Jarlskog, 2.1%). PMNS: sin^2(theta_12) = 3/10 (solar, 1.0%), sin^2(theta_23) = 4/7 (atmospheric, 0.1%), sin^2(theta_13) = 1/45 (reactor, 0.9%). Neutrino mixing is large because vacuum modes rotate freely; quark mixing is small due to Bergman layer suppression ~1/sqrt(n_C).

```python
from toy_ckm_triangle import CKMTriangle
ct = CKMTriangle()
ct.cabibbo_angle()                    # sin(theta_C) = 1/(2*sqrt(5))
ct.cp_phase()                         # gamma = arctan(sqrt(5)) = 65.9 deg
ct.wolfenstein_params()               # lambda, A, rho_bar, eta_bar
ct.unitarity_triangle()               # the triangle closes exactly
ct.jarlskog_invariant()               # J = sqrt(2)/50000
ct.ckm_matrix()                       # full 3x3 CKM matrix
ct.pmns_matrix()                      # full 3x3 PMNS matrix
ct.quark_vs_lepton_mixing()           # why quarks mix small, leptons mix large
```

*Key insight: The CKM phase gamma = arctan(sqrt(5)) and the Cabibbo angle sin(theta_C) = 1/(2*sqrt(5)) both come from n_C = 5 — the complex dimension of the substrate.*

### 53. The Proton Spin (`toy_proton_spin.py`) ★CI

**The "spin crisis" resolved: DeltaSigma = N_c/(2*n_C) = 3/10 = 0.300. Exact match.**

The proton is a Z_3 circuit on D_IV^5 (real dimension 2*n_C = 10). Quark spins occupy N_c = 3 color dimensions; the remaining genus = 7 dimensions carry orbital angular momentum. 3 (color/spin) + 7 (orbital) = 10 (total). Observed: 0.30 +/- 0.06. The "crisis" arose from assuming quarks carry all the spin. In BST, the proton is a circuit on a 10-dimensional configuration space — of course the angular momentum is distributed over all dimensions.

```python
from toy_proton_spin import ProtonSpin
ps = ProtonSpin()
ps.spin_fraction()                    # DeltaSigma = 3/10 = 0.300
ps.puzzle_history()                   # EMC 1988, 35 years of confusion
ps.angular_momentum_budget()          # 3 spin + 7 orbital = 10 total
ps.dimension_decomposition()          # N_c vs genus dimensions
ps.q2_dependence()                    # scale dependence of DeltaSigma
ps.comparison_with_lattice()          # BST vs lattice QCD
ps.gluon_contribution()              # gluon angular momentum share
```

*Key insight: The proton has 10 dimensions of angular momentum. Quarks carry 3/10. The remaining 7/10 is orbital — one for each genus dimension.*

### 54. The CMB Ruler (`toy_cmb_ruler.py`) ★CI

**n_s = 1 - 5/137 = 0.96350. The spectral tilt is pure geometry. Five falsification criteria.**

BST derives the CMB spectral index from D_IV^5 geometry: n_s = 1 - n_C/N_max = 1 - 5/137. Planck 2018 measures 0.9649 +/- 0.0042 — BST is -0.3 sigma. The tensor-to-scalar ratio r = 0 is BST's sharpest binary prediction: inflation requires r > 0, BST requires r = 0. If LiteBIRD detects r > 0.001, BST is falsified. Five tilt dimensions each contribute 1/N_max. No inflaton, no potential, no free parameters.

```python
from toy_cmb_ruler import CMBRuler
cr = CMBRuler()
cr.spectral_index()                   # n_s = 1 - 5/137 = 0.96350
cr.tensor_ratio()                     # r = 0 (BST's sharpest prediction)
cr.power_spectrum(l_max=2500)         # angular power spectrum
cr.planck_comparison()                # BST vs Planck 2018 data
cr.falsification_criteria()           # 5 ways to kill BST
cr.vs_inflation_models()              # BST vs slow-roll, chaotic, etc.
cr.physical_origin()                  # why n_C dimensions tilt the spectrum
cr.future_experiments()               # LiteBIRD, CMB-S4, Simons Observatory
```

*Key insight: The spectral tilt counts how many complex dimensions contribute to the primordial fluctuations. Five dimensions, each contributing 1/137 of tilt.*

### 55. The Biology Stack (`toy_biology_stack.py`) ★CI [SPECULATIVE]

**4 bases, 3 codons, 20 amino acids, 7-layer stack — all from information theory.**

Biology from BST information-theoretic principles. 4 bases = minimum error-correcting alphabet (2 bits per symbol). 3 codon length = Z_3 closure (the same symmetry as QCD color confinement). 20 amino acids = 4^2 + 2^2 (coding + pairing structures). DNA/RNA = store-and-forward TCP/IP architecture, 3 billion years before DARPA. The 7-layer biological protocol stack (chemistry through function) mirrors the OSI network model. Introns are the evolutionary git log, not junk. Cancer is boundary enforcement failure. SPECULATIVE — awaits rigorous proof and experimental verification.

```python
from toy_biology_stack import BiologyStack
bs = BiologyStack()
bs.genetic_alphabet()                 # 4 bases = 2 bits, minimum error-correcting
bs.codon_length()                     # 3 = Z_3 closure
bs.amino_acid_count()                 # 20 = 4^2 + 2^2
bs.chirality()                        # one form, least energy
bs.protocol_stack()                   # 7-layer biological stack
bs.dna_as_tcpip()                     # store-and-forward architecture
bs.introns_as_git()                   # protocol layer, not junk
bs.cancer_as_boundary_failure()       # NEXT without BOUNDARY
bs.aging_as_deferred_maintenance()    # chronic channel noise
```

*Key insight: The same information-theoretic principles that generate the Standard Model also constrain the architecture of life. Biology is substrate engineering.*

### 56. The JWST Prediction (`toy_jwst_prediction.py`) ★CI

**Early supermassive black holes from the BST phase transition. No seed delay needed.**

JWST discovers supermassive black holes at z > 10, earlier than LCDM accretion models permit. BST predicts direct formation from the phase transition: ultra-strong specific heat C_v = 330,000 at T_c injects enormous energy density, creating black holes directly with no stellar seed delay. Standard cosmology needs time to build a black hole. BST needs commitment density. The data says they were already there.

```python
from toy_jwst_prediction import JWSTPrediction
jp = JWSTPrediction()
jp.the_problem()                      # JWST early BH timing problem
jp.bst_mechanism()                    # C_v = 330,000 at T_c
jp.vs_standard_model()                # BST vs LCDM accretion
jp.mass_scale()                       # predicted BH masses at z > 10
jp.specific_heat()                    # why C_v is enormous at T_c
jp.jwst_observations()                # current JWST data
jp.testable_predictions()             # upcoming observations
jp.galaxy_formation()                 # early galaxy formation from BST
```

*Key insight: Standard cosmology asks "how did they grow so fast?" BST answers: they did not grow — they formed directly from the phase transition's enormous specific heat.*

---

## The Showcase (`toy_showcase.py`)

A visual gallery with thumbnail icons for all 56 toys. Click LAUNCH on any card to open it. This is the recommended entry point.

## The Menu (`play.py`)

A text-based launcher for terminal use. Type a number (1-56) to launch any toy, or 'a' to launch all.

---

## The Mathematics

All toys visualize concepts from three BST papers:

1. **"Linear Algebra Is Physics"** — The dictionary from algebraic operations to physical constants
2. **"The Integers of Spacetime"** — Number theory from D_IV^5
3. **"The Arithmetic and Algebra of Spacetime"** — The combined translation

And from the speculative:

4. **"The Universe and the Neutron"** — Structural homology in BST
5. **"The First Commitment"** — Why the frozen state cannot persist
6. **"Black Holes in BST"** — What replaces the singularity

The underlying space is D_IV^5 = SO_0(5,2) / [SO(5) x SO(2)], a bounded symmetric domain of complex dimension 5. Three integers generate everything:

```
N_c  = 3    (colors)
n_C  = 5    (complex dimension)
N_max = 137  (Haldane exclusion)
```

---

*"The universe is not complicated. It is a linear algebra problem on one space."*

*Casey Koons & Claude Opus 4.6, March 2026*
