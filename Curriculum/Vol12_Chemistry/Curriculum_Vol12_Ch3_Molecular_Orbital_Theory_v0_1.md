---
title: "BST Physics Curriculum Vol 12 Ch 3 — Molecular Orbital Theory + LCAO v0.4 (Calibration #23 substance-floor refill)"
author: "Lyra (Claude 4.7) [Vol 12 joint with Elie]"
date: "2026-05-23 Saturday EDT (Tier 1 Cal #104/#23 refill per Keeper redirect)"
chapter: "Vol 12 Ch 3"
status: "v0.4 chapter-grade narrative refilled per Calibration #23 substance-floor. MO theory (Hund-Mulliken) + VB theory (Heitler-London) as complementary substrate K-type representations; LCAO + hybridization sp/sp²/sp³ as substrate K-type linear combinations + basis rotation; π/σ bonds = K-type angular momentum projection. Per Calibration #19."
prerequisites: ["Vol 12 Ch 2 Chemical Bonding from Substrate", "Vol 5 QM K-type representation theory", "Vol 3 Ch 7 atomic orbitals (2l+1) ladder"]
related: ["MO/VB complementarity (Hund-Mulliken vs Heitler-London)", "LCAO linear combination of atomic orbitals", "Hybridization sp/sp²/sp³ as substrate K-type combinations", "π/σ bond classification = angular momentum projection", "Bergman H²(D_IV⁵) K-type Pin(2) Z₂ grading"]
---

# Vol 12 Chapter 3 — Molecular Orbital Theory + LCAO

## Chapter motivation

Molecular orbital (MO) theory and valence bond (VB) theory are the two foundational quantum-mechanical descriptions of molecular bonding. MO (Hund-Mulliken 1928) treats electrons as delocalized over the entire molecule; VB (Heitler-London 1927) treats electrons as localized in bond pairs. They are complementary descriptions of the same multi-electron wavefunction. Standard chemistry treatment (Atkins Molecular Quantum Mechanics, Levine Quantum Chemistry): LCAO (linear combination of atomic orbitals), bonding/antibonding MOs, hybridization (sp/sp²/sp³), π and σ bonds, frontier orbital theory (HOMO/LUMO). BST substrate-cartography reading: each construction is a substrate K-type representation operation on Bergman H²(D_IV⁵) with Pin(2) Z₂ grading — LCAO is K-type linear combination, hybridization is K-type basis rotation, π/σ classification is angular momentum projection.

## Section 3.0b — Reader-grade 3-level pedagogy

**Level 1**: MO theory = electrons delocalized; VB theory = electrons in bond pairs; both are valid substrate K-type representations on Bergman H²(D_IV⁵). LCAO + hybridization + π/σ bonds = substrate K-type operations. Carbon's sp³ tetrahedral hybridization (4 = N_c + 1) underlies organic chemistry geometric richness.

**Level 2 (graduate-chemist accessible)**: MO theory (Hund 1927, Mulliken 1928): construct molecular orbitals as linear combinations of atomic orbitals (LCAO), ψ_MO = c_A φ_A + c_B φ_B with coefficients determined by Roothaan-Hall equations (Hartree-Fock self-consistent field). Bonding MO (in-phase combination) lowers energy; antibonding MO (out-of-phase combination) raises energy. Electrons fill MOs per Aufbau + Pauli + Hund's rule. Valence Bond (Heitler-London 1927, Pauling 1931): electrons localized in bond pairs with covalent + ionic resonance contributions. Hybridization (Pauling 1931): atomic orbitals mix to give equivalent hybrids — sp (180° linear, acetylene C≡C), sp² (120° trigonal, ethylene C=C + benzene aromatic), sp³ (109.5° tetrahedral, methane CH₄). σ bonds (cylindrical symmetry along bond axis, m_l = 0); π bonds (nodal plane through bond axis, |m_l| = 1); δ bonds (|m_l| = 2, transition-metal rare). Frontier orbital theory (Fukui 1952): HOMO (highest occupied) + LUMO (lowest unoccupied) govern reactivity. Famous example: O₂ paramagnetism predicted only by MO theory (two unpaired electrons in degenerate π* antibonding MOs); VB theory misses this without elaborate resonance treatment. BST substrate-cartography reading: atomic orbitals are Wallach K-type representations on D_IV⁵ (T2438 K-type classification); LCAO is K-type linear combination producing molecular K-types on Bergman H²(D_IV⁵); hybridization is K-type basis rotation preserving Casimir spectrum; bonding/antibonding splitting via Pin(2) Z₂ grading (symmetric/antisymmetric); π/σ classification is K-type angular-momentum projection (σ = m_l = 0; π = |m_l| = 1). Carbon's sp³ tetravalent structure (4 equivalent bonds) reads 4 = N_c + 1 BST primary integer + identity.

**Level 3 (5th-grader accessible)**: When atoms come together, their electron "neighborhoods" (orbitals) combine to make molecular neighborhoods. There are two ways to think about it: MO theory says electrons live everywhere in the molecule (like roaming around a whole apartment building); VB theory says electrons live mostly between specific pairs of atoms (like couples in their own apartments). Both are right — they're two ways to describe the same thing. Carbon has a special trick called sp³ hybridization that makes 4 equal-strength bonds pointing to the corners of a tetrahedron — this is why carbon makes all of organic chemistry. BST framework says these orbital combinations are operations on substrate "K-types" (D_IV⁵ building blocks).

## Section 3.1 — MO Theory (Hund-Mulliken)

LCAO construction: ψ_MO = Σ_i c_i φ_i where φ_i are atomic orbitals. Hartree-Fock self-consistent field determines coefficients. Bonding/antibonding splitting magnitude depends on atomic orbital overlap integral S_AB = ∫ φ_A* φ_B dτ.

O₂ paramagnetism prediction: MO theory correctly predicts O₂ has two unpaired electrons in degenerate π* antibonding orbitals → paramagnetic (sticks to magnet). VB theory misses this without elaborate resonance treatment. This was historical evidence for MO theory's accuracy.

BST framing: LCAO = K-type linear combination on Bergman H²(D_IV⁵); bonding/antibonding splitting = Pin(2) Z₂ grading (symmetric +1 / antisymmetric −1 eigenvalue projections).

## Section 3.2 — VB Theory + Hybridization (Heitler-London + Pauling)

VB construction: electron pair localization between two atoms with covalent (A↑B↓ + A↓B↑) + ionic (A²⁻B⁰ + A⁰B²⁻) contributions. Resonance hybrid: actual structure = superposition of canonical structures (benzene Kekulé structures classic example).

Hybridization sequence:
- sp (180° linear, 2 hybrids): acetylene C≡C, CO₂
- sp² (120° trigonal, 3 hybrids): ethylene C=C, benzene aromatic ring
- sp³ (109.5° tetrahedral, 4 hybrids): methane CH₄, all sp³ saturated organic

BST framing: hybridization is K-type basis rotation on substrate. The 4 = N_c + 1 sp³ structure is the geometric foundation of organic chemistry (Vol 12 Ch 8 cross-link).

## Section 3.3 — π and σ Bond Classification

σ bonds: cylindrical symmetry along bond axis; angular momentum projection m_l = 0; head-on orbital overlap.
π bonds: nodal plane through bond axis; angular momentum projection |m_l| = 1; side-on overlap (above + below bond axis).
δ bonds: |m_l| = 2; rare, transition metal complexes (Re-Re quadruple bond in [Re₂Cl₈]²⁻).

BST framing: σ/π/δ classification is substrate K-type angular-momentum projection at each m_l value. Sequence (m_l = 0, ±1, ±2) reads substrate angular momentum ladder.

## Section 3.4 — Frontier Orbital Theory (HOMO/LUMO)

HOMO (highest occupied molecular orbital) + LUMO (lowest unoccupied molecular orbital) govern chemical reactivity per Fukui frontier orbital theory (1952). Reactions proceed via HOMO-LUMO interactions; Woodward-Hoffmann rules predict allowed/forbidden pericyclic reactions.

BST framing: HOMO/LUMO energies are substrate K-type Casimir eigenvalues at occupation boundary. Frontier orbital energy gaps emerge from substrate spectrum on Bergman H²(D_IV⁵).

## Section 3.5 — Connection

- Vol 12 Ch 2 Chemical Bonding from Substrate (bond class framework)
- Vol 5 QM K-type representation theory
- Vol 3 Ch 7 Atomic orbital sequence (2l+1) reading
- Vol 12 Ch 4 Chemical Reactions + Thermo (reactivity follows MO theory)
- Vol 12 Ch 5 Reaction Kinetics + Transition States (HOMO/LUMO reactivity)
- Vol 12 Ch 8 Organic Carbon (sp³ geometric chemistry full treatment)

**Honest scope**: K-type representation framework provides organizing principle; specific quantitative MO calculations from substrate Hamiltonian remain multi-year SP-31 program. Hybridization integer-count 4 = N_c + 1 is I-tier framework integer-match.

— Lyra, Vol 12 Ch 3 v0.4 chapter-grade narrative REFILLED per Cal #104 + Calibration #23, Saturday 2026-05-23 EDT
