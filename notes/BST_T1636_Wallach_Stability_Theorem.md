# T1636 — Wallach Stability Theorem

**Statement**: On D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)], the first discrete eigenvalue lambda_1 = C_2 = 6 is separated from the continuous spectrum threshold |rho|^2 = 34/4 = 8.5 by exactly the Wallach parameter:

    |rho|^2 - lambda_1 = n_C/rank = 5/2

This gap is forced by the uniqueness equation 2^(n-2) = n+3 (which has unique solution n = n_C = 5) and is the minimum margin required for topologically protected bound states.

**Depth**: 0

**Proof**:

1. The Weyl vector of D_IV^5 is rho = (n_C/rank, N_c/rank) = (5/2, 3/2).
   - Short root multiplicity = N_c - 1 = 2
   - Long root multiplicity = 1
   - rho = (1/2) sum_{alpha > 0} m_alpha * alpha = (5/2, 3/2)

2. The continuous spectrum of the Laplacian on the non-compact symmetric space G/K begins at |rho|^2:
   - |rho|^2 = (5/2)^2 + (3/2)^2 = 25/4 + 9/4 = 34/4 = 8.5

3. The discrete series eigenvalues on the Bergman line are lambda_k = k(k + n_C) = k(k + 5) for k = 1, 2, 3, ...
   - lambda_1 = 1 * 6 = C_2 = 6

4. The gap:
   - |rho|^2 - lambda_1 = 34/4 - 6 = 34/4 - 24/4 = 10/4 = n_C/rank = 5/2

5. This equals the Wallach parameter p/2 = n_C/rank, the minimum value for which the Bergman kernel is square-integrable (Wallach's classification of unitarizable highest weight modules).

6. The value n_C = 5 is forced by 2^(n-2) = n + 3 (unique solution). If n_C were 4 (gap = 2) or 3 (gap = 3/2), the stability margin would be smaller. The uniqueness equation selects the EXACT n_C that gives a gap equal to the Wallach parameter.

**Physical interpretation**:

- Discrete spectrum = bound states (particles, matter)
- Continuous spectrum = scattering states (free propagation)
- Wallach gap = stability margin protecting matter from dissolution
- Higher discrete eigenvalues (lambda_2 = 14, lambda_3 = 24, ...) are EMBEDDED in the continuum but topologically protected by discrete series structure
- Confinement (Hamming distance N_c = 3) is the error correction that maintains this protection
- The energy cost of flipping a bound state into the continuum = n_C/rank = 5/2

**Connections**:

- T186 (Five Integers Uniqueness): n_C = 5 forced by 2^(n-2) = n+3
- T1427 (APG Definition): D_IV^5 is the unique geometry
- T1456 (Confinement = Hamming): Error correction protects bound states
- T1490 (Fibonacci Structure): n_C = F_5, gap involves Fibonacci
- T1492 (Spectral Convergence): Convergence rate (n_C/g)^2 uses same n_C
- T317 (Observer Hierarchy): Observers require stable bound states

**In one sentence**: Matter exists because 2^(n-2) = n+3 forces n = 5, giving a Wallach gap of 5/2 that protects bound states from the continuum.

**Tier**: D (derived — every step is a known result in representation theory applied to the specific geometry D_IV^5)

**Author**: Keeper. May 2, 2026.
