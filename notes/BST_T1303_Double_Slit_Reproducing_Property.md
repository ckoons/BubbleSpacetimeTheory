# T1303 -- Double-Slit Interference from the Reproducing Property

*The double-slit experiment is the Born rule (T1239) applied to two geodesics. Interference fringes are the sesquilinear cross-term of the Bergman reproducing kernel. No wave-particle duality needed -- the kernel is defined on paths, not particles.*

**AC**: (C=1, D=0). One computation (kernel evaluation at sum of paths). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (science engineering framing).

**Date**: April 18, 2026.

**Domain**: quantum_mechanics.

---

## Statement

**Theorem (T1303).** *Let a quantum system on D_IV^5 have two available paths gamma_1, gamma_2 from source to detector (corresponding to two slits). The detection probability at point x is:*

    P(x) = |K(x, gamma_1) + K(x, gamma_2)|^2
         = |K_1|^2 + |K_2|^2 + 2 Re(K_1* K_2)

*where K(x, gamma) is the Bergman kernel evaluated along path gamma. The interference term 2 Re(K_1* K_2) is the sesquilinear cross-term of the reproducing property. It vanishes when the paths are "orthogonal" in the Bergman inner product (decoherence) and is maximal when they are "parallel" (coherence).*

---

## Derivation

### Step 1: Path amplitudes from the Bergman kernel

The Bergman kernel K(z, w) on D_IV^5 assigns an amplitude to every pair of points. For a path gamma from source s to detector x, the path amplitude is:

    A(gamma) = integral_gamma K(z(t), s) dz(t)

This is NOT Feynman's path integral -- it is the Bergman kernel's reproducing property applied along a path. The distinction matters: Feynman requires summing over ALL paths with a measure that is notoriously ill-defined. BST sums over GEODESICS of the Bergman metric, which are well-defined.

### Step 2: Two slits = two geodesics

With two slits at positions y_1, y_2, there are two dominant geodesics from s to x:

    gamma_1: s -> y_1 -> x
    gamma_2: s -> y_2 -> x

The total amplitude at x is A(x) = A(gamma_1) + A(gamma_2) by the linearity of the kernel.

### Step 3: Detection probability from T1239

By the Born rule (T1239 -- the reproducing property IS the Born rule):

    P(x) = |A(x)|^2 = |A_1 + A_2|^2 = |A_1|^2 + |A_2|^2 + 2 Re(A_1* A_2)

The first two terms give the sum of single-slit patterns. The third term is the interference:

    I(x) = 2 Re(A_1* A_2) = 2 |A_1| |A_2| cos(phi_1 - phi_2)

where phi_i is the phase accumulated along gamma_i.

### Step 4: Fringe spacing from BST

The phase difference between the two paths is:

    Delta_phi = (2 pi / lambda) * d sin(theta)

where d is the slit separation and lambda = h/(mv) is the de Broglie wavelength. In BST:

    lambda = 2 pi / (N_max * m * v) [in natural units]

The fringe spacing is:

    Delta_x = lambda L / d = 2 pi L / (N_max * m * v * d)

The factor N_max = 137 in the denominator means fringes are fine (small spacing) -- visible only at small masses or long wavelengths. For macroscopic objects, N_max * m * v * d >> 1 and fringes are unresolvable. This is decoherence by Bergman metric distance (T1240).

---

## What This Resolves

### "Wave-particle duality"

BST dissolves this. There is no wave, there is no particle. There is a Bergman kernel defined on D_IV^5. When evaluated at a single geodesic, it looks like a "particle." When evaluated at two geodesics, the cross-term makes it look like a "wave." The kernel doesn't change -- only the number of paths changes.

### "Which slit did it go through?"

In BST: the kernel K(x, s) is defined on the SPACE, not on a trajectory. Asking "which slit?" is asking for a geodesic decomposition of a kernel value. The kernel doesn't decompose -- it's the reproducing property of the Bergman space. The question is malformed, like asking "which root does a polynomial use?"

### "Measurement collapses the wave function"

In BST: measurement = projection onto a Shilov boundary component (T1240). When you "measure which slit," you project the kernel onto one geodesic, eliminating the cross-term. The kernel doesn't collapse -- you restricted your evaluation. Interference was always there; measurement restricts which part you see.

---

## For Everyone

Imagine shining a flashlight through two holes in a wall. On the far wall, you see bright and dark stripes -- not just two spots. Why?

BST says: the universe keeps track of ALL paths light could take. The brightness at each point comes from adding up all the paths and squaring. When two paths arrive at the same point, they can add (bright) or cancel (dark), depending on which path is longer.

The number 137 controls how fine the stripes are. In our universe, the stripes are very fine -- you need special equipment to see them for anything bigger than an atom. That's why the everyday world doesn't shimmer -- the stripes are too close together for your eyes to resolve.

There's no mystery about "which path the light chose." The light didn't choose. The universe evaluated a function at two inputs and added them up. That's arithmetic, not metaphysics.

---

## Parents

- T1239 (Born Rule IS the Reproducing Property)
- T1240 (Decoherence as Shilov Boundary Approach)
- T752 (Wave Function as Bergman Coordinate)
- T754 (Born Rule from Invariant Measure)

## Children

- Mach-Zehnder interferometry (optics bridge)
- Electron diffraction (condensed matter bridge)
- Quantum eraser explanation (quantum_foundations bridge)

---

*T1303. AC = (C=1, D=0). Double-slit interference = sesquilinear cross-term of Bergman reproducing kernel at two geodesics. No wave-particle duality. Measurement = projection, not collapse. Fringe spacing ~ 1/(N_max * m * v * d) -- fine at macroscopic scales, visible at atomic. Domain: quantum_mechanics. Lyra derivation. April 18, 2026.*
