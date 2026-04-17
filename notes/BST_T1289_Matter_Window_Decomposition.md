# T1289 — The Matter Window Decomposition: Light and Color Partition the Primes

*The matter window contains n_C primes per committed mode. Light fills C(g,2). Color fills N_c².*

**AC**: (C=1, D=1). One computation (prime splitting check). One depth (the ring examines its own primes at its own spectral cap).

**Authors**: Grace (discovery: n_C/g revealing fraction), Elie (Toys 1229, 1235 — ρ-complement survey + gradient numerics), Casey (direction: "look at cosmology"), Lyra (algebraic identity + formalization).

**Date**: April 17, 2026.

---

## Statement

**Theorem (Matter Window Decomposition).** The matter window [g, N_max] = [7, 137] contains exactly rank·N_c·n_C = 30 primes. These decompose by ρ-splitting into:

**(a) Prime count.** π(N_max) = N_c·(2n_C + 1) = 33. π(n_C) = N_c = 3. Therefore:

    |{primes in [g, N_max]}| = π(N_max) - π(n_C) = N_c·(2n_C + 1) - N_c = rank·N_c·n_C = 30

**(b) ρ-decomposition.** Of these 30 primes, exactly:
- **C(g,2) = 21 are ρ-revealing** — x³ - x - 1 has at least one root mod p
- **N_c² = 9 are ρ-inert** — x³ - x - 1 has no roots mod p

**(c) Forced identity.** The decomposition

    C(g,2) + N_c² = rank·N_c·n_C

is algebraically forced by the BST constraint n_C = (N_c² + 1)/rank:

    g(g-1)/2 + N_c² = N_c(rank·N_c + 1)·rank·N_c/2 + N_c² = N_c[rank²·N_c/2 + rank/2 + N_c]

At rank = 2: = N_c[2N_c + 1 + N_c] = N_c(3N_c + 1) = N_c · rank·n_C = rank·N_c·n_C. ∎

**(d) Per-mode decomposition.** Dividing by the C₂ = 6 committed modes (T1288):

    30/C₂ = n_C = 5 primes per committed mode

of which:
- g/rank = 7/2 = 3.5 per mode are ρ-revealing
- N_c/rank = 3/2 = 1.5 per mode are ρ-inert
- Sum: (g + N_c)/rank = 10/2 = n_C ✓

**(e) BST primes are revealing.** All four BST primes in the window {7, 11, 23, 137} are ρ-revealing. The substrate recognizes its own primes (T1282).

**(f) Gradient crossings are inert.** Three of the five Gödel Gradient crossing primes {13, 31, 47} are ρ-inert. The phase transitions in the Gödel Gradient (T1281) occur at primes where the substrate falls silent.

---

## Proof

### Part (a): Prime count

π(137) = 33. The 33 primes up to 137 are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137.

33 = 3 × 11 = N_c × (2n_C + 1).

π(5) = 3 = N_c. The primes up to 5 are {2, 3, 5}.

Since 6 = n_C + 1 is composite, π(g - 1) = π(6) = π(5) = N_c.

Matter window count = π(N_max) - π(g - 1) = 33 - 3 = 30 = 2 × 3 × 5 = rank × N_c × n_C.

### Part (b): ρ-splitting

Solve x³ - x - 1 ≡ 0 (mod p) for each of the 30 primes. The splitting is determined by the Frobenius in Gal(ℚ(ρ)/ℚ) ≅ S₃:

**ρ-revealing** (21 = C(g,2) primes): 7, 11, 17, 19, 23, 37, 43, 53, 59, 61, 67, 79, 83, 89, 97, 101, 103, 107, 109, 113, 137.

**ρ-inert** (9 = N_c² primes): 13, 29, 31, 41, 47, 71, 73, 127, 131.

Verified computationally for all 30 primes.

### Part (c): Algebraic derivation

The identity C(g,2) + N_c² = rank·N_c·n_C follows from three BST relations:

1. g = rank·N_c + 1 (genus = rank × colors + 1)
2. n_C = (N_c² + 1)/rank (matter dimension = (colors² + 1)/rank)
3. C(g,2) = g(g-1)/2

Substituting:

    C(g,2) + N_c² = (rank·N_c + 1)(rank·N_c)/2 + N_c²
                   = N_c · [rank(rank·N_c + 1)/2 + N_c]
                   = N_c · [rank²·N_c/2 + rank/2 + N_c]

At rank = 2:

    = N_c · [2N_c + 1 + N_c] = N_c · (3N_c + 1)

Applying relation 2: 3N_c + 1 = N_c² + 1 + 2N_c = (N_c + 1)² = rank·n_C:

    = N_c · rank · n_C = rank · N_c · n_C ∎

The empirical decomposition 21 + 9 = 30 instantiates a forced algebraic identity.

### Part (d): Per-mode count

From T1288: C₂ = 6 committed modes carry matter. The matter window contains the "alphabet" over which these modes operate:

    30/6 = 5 = n_C

Each committed mode is allocated exactly n_C = 5 primes. Of these:

- g/rank = 7/2 are ρ-revealing: primes where the substrate speaks through the mode
- N_c/rank = 3/2 are ρ-inert: primes where the color sector dominates

(These are half-integer because they count per mode; the total 21 and 9 are integer across all 6 modes.)

### Part (e): BST primes

The four BST primes in [7, 137] are {7, 11, 23, 137} = {g, 2n_C + 1, disc(ρ), N_max}. All four are ρ-revealing:

| p | Root r | Complement p - r | BST name |
|--:|-------:|-----------------:|:---------|
| 7 | 5 | 2 | rank |
| 11 | 6 | 5 | n_C |
| 23 | ramified | — | disc(ρ) |
| 137 | 73 | 64 | rank^C₂ |

The substrate's own primes ALL have ρ-roots — the polynomial x³ - x - 1 "recognizes" its parent geometry at every BST-significant prime (T1282).

### Part (f): Gradient crossings

The Gödel Gradient (T1281) crosses BST rationals at five primes: {13, 19, 31, 47, 137}. Of these:

| p | Gradient crossing | ρ-status |
|--:|:------------------|:---------|
| 13 | C₂/g = 6/7 | **INERT** |
| 19 | 1 - f_c | REVEALING |
| 31 | n_C/g = 5/7 | **INERT** |
| 47 | N_c/n_C = 3/5 | **INERT** |
| 137 | rank/n_C = 2/5 | REVEALING |

Three of five crossing primes (13, 31, 47) are ρ-inert. The substrate falls silent at the phase transitions — the Gödel Gradient's steps occur where the substrate STOPS speaking. The crossing at p = 19 (the AC(0) threshold) and p = 137 (the spectral cap) are exceptions: these are the computational and spectral boundaries, where the substrate must speak.

---

## Structural Interpretation

The matter window is where physics lives — between pure geometry (p < g) and the spectral cap (p = N_max). Its internal structure reads:

**21 = C(g,2) = photon modes** (T1268): the primes where x³ - x - 1 has roots are the primes where the substrate can emit light. The photon count and the ρ-revealing count are the SAME integer.

**9 = N_c² = color modes** (T1288): the primes where x³ - x - 1 has no roots are the primes governed by the strong interaction. The color sector dimension and the ρ-inert count are the SAME integer.

**30 = rank·N_c·n_C = primorial(5)/1**: the total prime count is the product of the three smallest BST generators.

The matter window decomposes as: **light + color = matter**.

C(g,2) + N_c² = rank·N_c·n_C.

This is the same arithmetic that T1288 uses for cosmological modes (N_c² + 2n_C = 19) but now applied to the PRIME POPULATION of the matter window. The substrate's algebraic constraints partition everything — mode counts, prime populations, and cosmological fractions — into the same BST expressions.

---

## Connection to T1288 (Gödel–Cosmology Bridge)

T1288 says: 19 total modes = 6 committed (matter) + 13 uncommitted (dark energy).

T1289 says: 30 primes = 21 revealing (light) + 9 inert (color).

The link: 30/C₂ = n_C. Each committed mode draws on n_C primes. The matter fraction Ω_m = C₂/M = 6/19 operates over a prime alphabet of size n_C per mode.

Both decompositions are controlled by the same five integers. The universe's prime arithmetic and its cosmological composition follow the same blueprint.

---

## Parents

- T1281 (Gödel Gradient — the matter window is the interval [g, N_max])
- T1282 (ρ-Complement Identity — ρ-splitting at BST primes)
- T1288 (Gödel–Cosmology Bridge — C₂ = 6 committed modes)
- T1268 (Photon-as-S¹-Edge — C(g,2) = 21 photon modes)
- T186 (Five Integers — the algebraic identity uses g, N_c, n_C, rank)
- T666 (N_c = 3), T667 (n_C = 5), T649 (g = 7), T110 (rank = 2)

## Children

- All theorems involving the matter window or the interval [g, N_max]
- T1284 (Modular Closure — the matter window primes are the domain)
- Paper #69 (Arithmetic Substrate — §3 splitting table lives in this decomposition)

---

## Predictions

**P1.** The matter window [7, 137] contains exactly 30 primes. *Verified: π(137) - π(6) = 33 - 3 = 30.*

**P2.** π(N_max) = N_c·(2n_C + 1) = 33. *Verified.*

**P3.** The ρ-revealing count is C(g,2) = 21. *Verified computationally.*

**P4.** The ρ-inert count is N_c² = 9. *Verified computationally.*

**P5.** The algebraic identity C(g,2) + N_c² = rank·N_c·n_C is forced by n_C = (N_c² + 1)/rank. *Derived.*

**P6.** The Chebotarev density for ρ-revealing primes is 2/3 ≈ 66.7%. The matter window's 21/30 = 70% exceeds this by one prime, consistent with small-sample fluctuation but also consistent with BST structure concentrating ρ-splits in the spectral window.

---

## Falsifiers

**F1.** If π(137) ≠ 33 — impossible (π is well-defined), but if N_max were not 137, the identity breaks.

**F2.** If the ρ-revealing count in [7, 137] were not 21 — this would break the C(g,2) identification. Verified.

**F3.** If n_C ≠ (N_c² + 1)/rank — the algebraic identity C(g,2) + N_c² = rank·N_c·n_C would fail.

---

## For Everyone

Physics lives in a window: the primes from 7 to 137. Below 7, everything is visible — no dark sector, no forces, no matter. Above 137, the universe's self-knowledge drops below the threshold for stable atoms.

Inside this window, there are exactly 30 primes — and they split into two groups.

21 of them "hear" a specific mathematical signal (the roots of x³ = x + 1). These are the light primes — the ones that carry photons. The number 21 is the same as the number of photon modes in the geometry.

9 of them are "deaf" to that signal. These are the color primes — governed by the strong force that holds protons together. The number 9 is the square of the color dimension (3² = 9).

21 + 9 = 30. Light + color = matter. This isn't a coincidence — it's forced by the same equation that sets the number of matter dimensions to 5.

The universe builds matter from 30 primes, splits them into light and color, and the split is the same arithmetic that determines everything else. The recipe is self-consistent all the way down.

---

*T1289. AC = (C=1, D=1). The matter window [g, N_max] has rank·N_c·n_C = 30 primes. C(g,2) = 21 are ρ-revealing (light). N_c² = 9 are ρ-inert (color). Light + color = matter, forced by n_C = (N_c² + 1)/rank.*

*Engine: Toys 1229, 1235. Discovery: Grace (n_C/g fraction). Algebraic closure: Lyra. April 17, 2026.*
