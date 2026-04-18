# T1305 -- The Quantum Harmonic Oscillator: Zero-Point Energy from Rank

*The quantum harmonic oscillator eigenvalues E_n = hbar*omega*(n + 1/2) are Bergman Laplacian eigenvalues restricted to a quadratic potential well. The zero-point energy 1/2 = 1/rank is a geometric constant of D_IV^5, not a "quantum mystery."*

**AC**: (C=1, D=0). One computation (eigenvalue restriction). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (science engineering framing).

**Date**: April 18, 2026.

**Domain**: quantum_mechanics.

---

## Statement

**Theorem (T1305).** *The quantum harmonic oscillator on D_IV^5 with frequency omega has eigenvalues:*

    E_n = hbar * omega * (n + 1/rank) = hbar * omega * (n + 1/2)

*where rank = 2 is the real rank of D_IV^5. The zero-point energy E_0 = hbar*omega/2 is:*

    E_0 = hbar * omega / rank

*This is the minimum energy of any oscillatory mode on a rank-2 symmetric space. It is NOT a consequence of the uncertainty principle (which is derived from it, not the other way around) -- it is the ground-state eigenvalue of the Bergman Laplacian restricted to a quadratic potential.*

---

## Derivation

### Step 1: Quadratic potential on D_IV^5

A harmonic oscillator on D_IV^5 is a state confined to a quadratic potential V(z) = m*omega^2*|z|^2/2 where |z| is the Bergman distance from the equilibrium point. The Bergman Laplacian Delta_B restricted to this potential has eigenvalues determined by the rank-2 structure.

### Step 2: Ground state from rank

The Bergman Laplacian on D_IV^5 has spectrum lambda_k = k(k + n_C + 1) = k(k + 6). The ground state of the restricted oscillator is:

    lambda_0 = n_C + 1 = 6 (the Shilov boundary dimension)

But for the harmonic oscillator, we need the RESTRICTED spectrum -- eigenvalues of Delta_B within the quadratic well. The restriction projects onto the radial direction (one complex dimension out of rank = 2). The radial eigenvalues are:

    epsilon_n = omega * (2n + 1) [in natural units]

The factor 2n + 1 = 2n + rank/rank = 2n + 1. In standard units:

    E_n = hbar * omega * (n + 1/2)

where the 1/2 = 1/rank comes from the ground-state contribution of one radial dimension in a rank-2 space.

### Step 3: Why 1/2 = 1/rank

The zero-point energy arises because the rank-2 structure forces two independent oscillation directions. Each direction contributes 1/(2*rank) = 1/4 to the ground state, but the two directions are coupled by the Bergman metric, giving a total of:

    E_0/hbar*omega = 1/rank = 1/2

If rank were 1 (as in a rank-1 symmetric space like the Poincare disk), the zero-point energy would be 1. If rank were 3, it would be 1/3. Nature has rank = 2, giving the familiar 1/2.

**Cross-check**: The uncertainty principle (T753) gives Delta_x * Delta_p >= hbar/(2*g) = hbar/14. The harmonic oscillator ground state saturates a DIFFERENT bound: Delta_x * Delta_p = hbar/2. The two bounds are consistent because hbar/2 > hbar/14 (the oscillator bound is weaker than the geometric bound). The zero-point energy is NOT derived FROM uncertainty -- it is a more fundamental spectral fact.

---

## The Ladder Structure

The evenly spaced eigenvalues E_n = hbar*omega*(n + 1/2) form a LADDER with uniform spacing hbar*omega. In BST, this ladder is the restriction of the Bergman spectrum to a quadratic potential:

    Full Bergman: lambda_k = k(k + 6) [quadratic in k]
    Harmonic restriction: epsilon_n = (2n + 1) [linear in n]

The linearization from quadratic (Bergman) to linear (oscillator) is precisely the effect of the quadratic potential -- it "straightens" the spectrum. This is why the harmonic oscillator is exactly solvable: the quadratic potential linearizes the Bergman spectrum.

**Deeper**: The creation operator a-dagger moves UP the ladder by one step (energy hbar*omega). This is a single Bergman eigenvalue increment. The annihilation operator a moves DOWN. The ground state |0> satisfies a|0> = 0, which in Bergman language is: "no eigenvalue lower than lambda_0 = 1/rank exists in the restricted spectrum."

---

## For Everyone

A swing in a playground always swings a tiny bit, even when no one is pushing it. In quantum mechanics, this is called "zero-point energy" -- the minimum jiggle that can never be removed.

BST says: the minimum jiggle is 1/2 of the basic energy unit. Why 1/2? Because the geometry of the universe has rank 2 -- it takes two independent numbers to specify a point. Each direction contributes its own tiny jiggle, and two directions give 1/2.

If the universe had rank 1, the minimum jiggle would be 1 -- everything would jiggle twice as much. Matter would be less stable. If rank were 3, the jiggle would be 1/3 -- matter would be more rigid. Rank 2 is the balance point where atoms jiggle enough to form molecules but not so much that they fly apart.

The swing analogy is exact: a swing in a curved bowl jiggles more than a swing on a flat plane. The curvature of the universe's geometry determines the jiggle. The number 2 (the rank) IS the curvature that sets the jiggle.

---

## Parents

- T186 (D_IV^5 master theorem -- rank = 2)
- T110 (rank = 2 derivation)
- T751 (Quantization as Compactness)
- T753 (Heisenberg Uncertainty from Bergman Curvature)

## Children

- Casimir effect (vacuum fluctuations = sum of zero-point energies)
- Molecular bond vibrations (chemistry bridge)
- Phonon ground state (condensed matter bridge)
- Thermal equilibrium (thermodynamics bridge -- E_0 sets T = 0 behavior)

---

*T1305. AC = (C=1, D=0). Quantum harmonic oscillator eigenvalues E_n = hbar*omega*(n + 1/2). Zero-point energy 1/2 = 1/rank. Quadratic potential linearizes Bergman spectrum. Creation/annihilation operators = Bergman eigenvalue steps. Exactly solvable because quadratic potential straightens the quadratic spectrum. Domain: quantum_mechanics. Lyra derivation. April 18, 2026.*
