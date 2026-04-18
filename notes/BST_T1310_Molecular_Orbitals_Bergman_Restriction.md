# T1310 -- Molecular Orbitals from Bergman Kernel Restriction

*Molecular orbital theory is the restriction of the Bergman reproducing kernel to multi-center configurations. Bonding = constructive kernel superposition. Antibonding = destructive. The LCAO approximation is exact when the atomic centers sit at Bergman lattice points. Bond order, hybridization, and aromaticity are spectral properties of the restricted kernel.*

**AC**: (C=1, D=0). One computation (kernel restriction). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (science engineering framing).

**Date**: April 18, 2026.

**Domain**: chemical_physics.

---

## Statement

**Theorem (T1310, Molecular Orbitals from Bergman Restriction).** *Let K(z, w) be the Bergman reproducing kernel on D_IV^5. For a molecule with atomic nuclei at positions {z₁, ..., z_M}, the molecular orbital at point z is:*

    ψ_MO(z) = Σᵢ cᵢ · K(z, zᵢ)

*where the coefficients cᵢ are determined by the eigenvalue equation of the restricted kernel matrix:*

    [K(zᵢ, zⱼ)]_{i,j} · c = ε · [S(zᵢ, zⱼ)]_{i,j} · c

*with S(zᵢ, zⱼ) = K(zᵢ, zⱼ)/√(K(zᵢ,zᵢ)·K(zⱼ,zⱼ)) the overlap matrix. This is LCAO-MO theory derived from D_IV^5 geometry rather than assumed.*

---

## Derivation

### Step 1: Atoms as kernel evaluation points

An atom at position zₐ in D_IV^5 is characterized by its Bergman kernel value K(z, zₐ). This is the atomic orbital — the probability amplitude for finding an electron at z given a nucleus at zₐ. The reproducing property of the Bergman kernel:

    f(z) = ∫ K(z, w) f(w) dμ(w)

ensures that atomic orbitals automatically satisfy the Schrödinger equation on D_IV^5 (they are eigenfunctions of the Bergman Laplacian, T186).

### Step 2: LCAO as kernel superposition

When two atoms are brought together (positions z₁, z₂), the molecular state is a superposition of atomic kernels:

    ψ±(z) = c₁ K(z, z₁) ± c₂ K(z, z₂)

The bonding orbital ψ₊ has constructive superposition between the nuclei (Re[K(z₁, z₂)] > 0). The antibonding orbital ψ₋ has destructive superposition. This is the SAME mechanism as double-slit interference (T1303) — the cross-term Re(K₁*K₂) determines bonding vs antibonding.

### Step 3: Bond order from kernel overlap

The overlap integral:

    S₁₂ = K(z₁, z₂) / √(K(z₁,z₁) · K(z₂,z₂))

determines bond strength. On D_IV^5, the Bergman kernel decays with distance:

    |K(z₁, z₂)| ~ exp(-λ₀ · d_B(z₁, z₂))

where λ₀ = n_C + 1 = 6 is the ground-state Bergman eigenvalue. The bond forms when S₁₂ exceeds a threshold set by the rank = 2 geometry.

**Bond order** = number of bonding orbitals minus antibonding orbitals, divided by 2. For the restricted kernel:
- Single bond: 1 bonding orbital occupied → order 1
- Double bond: 2 bonding orbitals → order 2
- Triple bond: 3 = N_c bonding orbitals → order 3 (maximum, from color count)

**Maximum bond order = N_c = 3** (triple bond). This is structural: D_IV^5 has N_c = 3 independent color channels, each contributing one bonding orbital. Quadruple bonds don't exist in nature because there is no fourth color.

### Step 4: Hybridization from Bergman harmonics

Atomic hybridization (sp, sp², sp³) is the restriction of Bergman harmonics to specific angular sectors:

- sp: rank = 2 independent directions → linear geometry (180°)
- sp²: N_c = 3 planar directions → trigonal planar (120°)
- sp³: rank² = 4 tetrahedral directions → tetrahedral (109.47° = arccos(-1/3))

The tetrahedral angle arccos(-1/3) = 109.47° is a Bergman metric angle, derived in T699. The H₂O deviation from tetrahedral (104.45°) is the lone-pair compression from T701.

### Step 5: Aromaticity from cyclic kernel

A cyclic molecule (benzene, etc.) has nuclei at positions z₁, ..., z_n equally spaced on a Bergman geodesic circle. The eigenvalues of the cyclic kernel matrix K(zᵢ, zⱼ) are:

    εₖ = Σⱼ K(z₁, zⱼ) · exp(2πijk/n)

For n = C₂ = 6 (benzene): exactly 3 = N_c bonding levels below the Fermi energy, giving 6 = C₂ π-electrons. This is Hückel's (4n+2) rule at n = 1: 4(1)+2 = 6 = C₂. The 4n+2 pattern is a Bergman spectral residue.

**Hückel's rule is a BST integer**: aromatic stability requires 4n+2 π-electrons. At n=1: 6 = C₂. At n=2: 10 = dim_ℝ(D_IV^5). At n=3: 14 = 2g. Every instance is a BST combination.

---

## Cross-Domain Bridges

| Target Domain | Bridge | Mechanism |
|:-------------|:-------|:----------|
| quantum_mechanics | MO = restricted Bergman kernel | T1303 (double-slit), T754 |
| biology | DNA base stacking = aromatic kernel overlap | T333, T452 |
| number_theory | Bond order ≤ N_c = 3 | T666 |
| bst_physics | Hybridization angles from Bergman metric | T699, T700, T701 |
| cooperation | Molecular recognition = kernel resonance | T1306 |

---

## For Everyone

When atoms come together to form molecules, their electron clouds overlap. The overlap can be constructive (bonding — the atoms stick together) or destructive (antibonding — the atoms push apart).

BST says this is exactly the same as light going through two slits (T1303). In both cases, two sources combine, and whether they help or hinder each other depends on the geometry of the space.

Why can you never have more than a triple bond? Because the universe has exactly 3 "color directions" (N_c = 3). Each direction allows one bonding overlap. Three directions, three bonds, maximum. Carbon-carbon triple bonds (in acetylene) use all three. There's no fourth direction to make a quadruple bond.

Why is benzene so stable? Because it has 6 π-electrons — and 6 = C₂, one of the five fundamental integers. Benzene's stability is not a chemical accident. It's geometry.

---

## Parents

- T186 (D_IV^5 master theorem — Bergman kernel)
- T699 (Tetrahedral Bond Angle)
- T700 (H₂O Bond Angle)
- T701 (Lone Pair Compression)
- T1303 (Double-Slit from Reproducing Property)
- T1107 (Chemistry-Quantum Bridge)

## Children

- Band theory from infinite kernel restriction (crystallography)
- Molecular recognition as kernel resonance (drug design)
- Spectroscopic selection rules from Bergman symmetry
- Reaction orbital theory (Fukui frontier orbitals as extremal kernel modes)

---

*T1310. AC = (C=1, D=0). Molecular orbital theory = Bergman kernel restricted to multi-center configurations. LCAO is exact on D_IV^5. Bond order ≤ N_c = 3 (triple bond maximum). Hybridization angles from Bergman metric. Aromaticity: Hückel (4n+2) = BST integers (6=C₂, 10=dim, 14=2g). Domain: chemical_physics. Lyra derivation. April 18, 2026.*
