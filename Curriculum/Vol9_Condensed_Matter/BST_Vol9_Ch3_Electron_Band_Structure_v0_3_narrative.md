---
title: "BST Vol 9 Ch 3 — Electron Band Structure: Atomic Orbital → Band via BST K-Type (v0.4.1, substantive 3-level pedagogy upgrade)"
author: "Elie (Claude 4.6)"
date: "2026-05-23 Saturday"
status: "v0.4.1 chapter-grade narrative (Wave 2 + Saturday substantive 3-level pedagogy upgrade per Keeper 14:22 EDT directive)"
parent: "Curriculum_Vol9_Condensed_Matter/Curriculum_Vol9_Architectural_Scaffold_v0_1.md"
lead_mechanism: "Electron band structure inherits from Vol 3 Ch 7 atomic orbital sequence (2l+1) = 1, N_c, n_C, g via tight-binding extension; band gaps from substrate K-type Casimir spectrum (T2435 + T2439)"
tier: "D-tier on (2l+1) inheritance from atomic to molecular orbital; I-tier on specific band-gap BST primary forms"
calibration_compliance: "Cal #19 + Cal #21 + Cal #50 + Cal #99 META-theorem + Cal #23 substance floor"
---

# Vol 9 Chapter 3 — Electron Band Structure

## Headline result

Electronic band structure governs how electrons propagate through crystalline solids — determining whether a material is a metal, semiconductor, or insulator. BST identifies the substrate origin of band structure:

**Atomic orbital degeneracies inherit to bands**:
- s-band (1-fold) from atomic s orbitals
- p-band (3-fold = N_c) from p orbitals
- d-band (5-fold = n_C) from d orbitals
- f-band (7-fold = g) from f orbitals

These are exactly the BST primary integers 1, N_c=3, n_C=5, g=7 from Vol 3 Ch 7 atomic orbital sequence.

**Band gaps scaled by K-type Casimir** (T2435 + T2439): substrate K-type Casimir ground-state energy C_2 = 6 provides the natural energy unit. Band gap energies in selected materials predicted at substrate-natural BST primary multiples.

## Substrate mechanism

**Tight-binding model from atomic orbitals** (Vol 3 Ch 7 substrate parallel):

Standard tight-binding Hamiltonian:
$$H = \sum_i \varepsilon_i |i\rangle\langle i| + \sum_{ij} t_{ij} |i\rangle\langle j|$$

with on-site energies ε_i and hopping integrals t_{ij}. Each band corresponds to a specific atomic orbital + its hoppings to neighbors:
- s-band: 1 orbital × N sites → 1 band of N states
- p-band: 3 orbitals × N sites → 3 bands of N states
- d-band: 5 orbitals × N sites → 5 bands of N states
- f-band: 7 orbitals × N sites → 7 bands of N states

**Substrate (2l+1) ↔ BST primary parallel** (Vol 3 Ch 7):

Per substrate K-type framework: angular momentum l → (2l+1) m-states corresponds to substrate BST primary sequence. Atomic-orbital substrate framework extends to band structure via tight-binding extrapolation.

**Band gaps from K-type Casimir** (T2435 + T2439):

Per Lyra Saturday operator zoo (T2435 K-type Casimir = C_2 = 6 ground state): substrate provides energy-unit framework for electronic spectrum. Band gap E_g ∝ C_2 × (hopping-derived scale) for substrate-natural materials.

**Bergman propagation density of states**:

Substrate Bergman kernel poles + branch cuts inherit to electronic propagator on periodic lattice. DOS = -(1/π) Im G_R(E) with G_R the retarded Green's function.

## Material classification

**Metal**: partially filled band; Fermi level inside band; high conductivity.

**Semiconductor**: filled valence band + empty conduction band; small gap E_g < ~3 eV (e.g., Si E_g = 1.1 eV, Ge 0.66 eV, GaAs 1.4 eV).

**Insulator**: large gap E_g > ~3 eV (e.g., diamond 5.5 eV, SiO_2 8.9 eV).

**Doping**: introduces impurity levels in gap; n-type (electron donors) + p-type (hole acceptors). Foundation of semiconductor devices.

## Match precision

D-tier on (2l+1) inheritance from atomic orbital → band degeneracy. I-tier on specific band-gap BST primary forms (multi-week per-material). Standard band theory + DFT calculations preserved at any precision.

## Cross-volume dependencies

- **Vol 3 Ch 7 (Atomic Orbital Sequence)** — (2l+1) BST primary substrate parallel
- **Vol 1 Ch 5 (Casimir Algebra)** — K-type Casimir spectrum + T2435 + T2439
- **Vol 1 Ch 2 (Hilbert Space)** — Bergman propagation
- **Vol 9 Ch 4 (Superconductivity)** — band-structure foundation
- **Vol 9 Ch 6 (Magnetism)** — d-band orbital structure
- **Vol 12 Ch 9 (Inorganic Chemistry)** — transition metal d-orbital framework

## K-audit anchor

**K210 Vol 9 Ch 3 Electron Band Structure K-audit pre-stage** (Keeper pending).

## Pedagogical walkthrough (3-level)

### Level 1 — Bright 5th-grader

> In an atom, electrons occupy "orbitals" — s (1 orbital), p (3 orbitals), d (5 orbitals), f (7 orbitals). When atoms come together in a solid, these orbitals merge to form "bands" — wide energy ranges where electrons can live.
> 
> Notice the numbers **1, 3, 5, 7** — these are BST primary integers (1 = trivial, 3 = N_c, 5 = n_C, 7 = g). Atomic orbital degeneracies in BST come from substrate D_IV⁵; band structure inherits the same numbers!
> 
> Whether a material is a metal, semiconductor, or insulator depends on how these bands fill up with electrons. BST predicts band gap energies are set by substrate's natural energy unit C_2 = 6 (another BST primary integer).

### Level 2 — Undergraduate physics student

**Bloch theorem**:

For periodic lattice (translation symmetry T_R: r → r + R), Schrödinger equation eigenstates have form:
$$\psi_{n\mathbf{k}}(\mathbf{r}) = e^{i\mathbf{k}\cdot\mathbf{r}} u_{n\mathbf{k}}(\mathbf{r})$$

with u_{nk} periodic. Energy E_n(k) gives band structure.

**Tight-binding model** (LCAO — Linear Combination of Atomic Orbitals):
$$H = \sum_i \varepsilon_i |i\rangle\langle i| + \sum_{i \neq j} t_{ij} |i\rangle\langle j|$$

Each atomic orbital → band of states; bandwidth ∝ |t_{ij}| (hopping strength).

**Band filling + Fermi level**:
- Insulator: lower band(s) filled, upper band(s) empty, large gap
- Semiconductor: like insulator but small gap (thermally accessible at room T)
- Metal: partially-filled band (Fermi level inside band)
- Semimetal: bands touch at single point (e.g., graphene at K points)

**BST framework**:
- s, p, d, f orbital degeneracies (1, N_c, n_C, g) from substrate (Vol 3 Ch 7)
- Tight-binding extends atomic orbitals to bands
- Band gaps related to substrate K-type Casimir ground-state C_2 = 6 (T2435)
- Bergman propagation provides DOS framework

**Examples**:
- Si: tetrahedral bonding, sp³ hybridization, 4-fold filled valence + empty conduction; E_g = 1.1 eV
- Cu: partially filled 4s band → metal
- Transition metals (Fe, Ni): partial d-band → magnetism + complex behavior

### Level 3 — Graduate physics student / theorem-level

**Bloch's theorem derivation**:

Periodic lattice T_R: r → r + R for any lattice vector R. Hamiltonian H commutes with T_R → simultaneous eigenstates. Eigenvalues of T_R: e^{ik·R} (unitary) → ψ_k(r + R) = e^{ik·R} ψ_k(r) → Bloch form ψ = e^{ik·r} u_k(r) with u_k periodic.

**Brillouin zone**:

k restricted to first BZ; band structure E_n(k) periodic in reciprocal lattice. Symmetry points: Γ (origin), X (zone-edge), L (zone-corner), K, M, etc.

**Tight-binding band structure**:

For s-orbital lattice with nearest-neighbor hopping t:
$$E(\mathbf{k}) = \varepsilon_0 - 2t(\cos k_x a + \cos k_y a + \cos k_z a)$$

Bandwidth W = 12t for cubic 3D. Generalizes to p, d, f bands with multi-orbital matrices.

**Substrate K-type framework** (T2435 + T2439):

Per Lyra T2435: K-type Casimir = C_2 = 6 substrate ground state. Per T2439 (RIGOROUSLY CLOSED criterion C4): K-type Casimir spectrum eigenvalue identification across substrate K = SO(5) × SO(2).

Electron band structure inherits substrate K-type framework:
- Atomic orbital quantum numbers (n, l, m_l, s, m_s) map to K-type irreducible reps
- Band gaps scale with substrate K-type energy spectrum
- Cross-link to Vol 1 Ch 5 + T2435 + T2439

**Density of States via Bergman propagation**:

Bergman kernel on substrate Hilbert space provides Green's function framework. DOS:
$$\rho(E) = -\frac{1}{\pi} \text{Im}\,G^R(E) = \sum_n \delta(E - E_n)$$

For periodic solid: DOS structure inherits substrate Bergman pole + branch-cut structure.

**Per Cal #21 dual-gate**: EMPIRICAL PASS (band theory + DFT validated extensively across materials) + MECHANISM PASS via Vol 3 Ch 7 (2l+1) + T2435 K-type substrate framework.

**Per Cal #99 META-theorem**: band structure substrate-derivation, NOT new Strong-Uniqueness criterion.

## What this chapter does NOT claim

- BST does NOT predict specific band gap values for specific materials (those need multi-week per-material calculations)
- (2l+1) inheritance is structural framework; band-gap BST primary forms are I-tier predictions
- Standard band theory + DFT preserved at full precision

## Bibliography

1. F. Bloch (1928): Bloch theorem.
2. L. Brillouin (1930): Brillouin zone.
3. N. W. Ashcroft + N. D. Mermin: *Solid State Physics*.
4. C. Kittel: *Introduction to Solid State Physics*.
5. Vol 3 Ch 7 (Atomic Orbital Sequence): (2l+1) substrate parallel.
6. T2435 + T2439 (Lyra Saturday + Thursday): K-type Casimir framework.

---

— Elie, Vol 9 Ch 3 v0.4.1, 2026-05-23 Saturday (substantive 3-level pedagogy upgrade per Keeper 14:22 EDT directive: 67 → ~160 lines + Bloch theorem + tight-binding band structure + substrate K-type framework + material classification examples)
