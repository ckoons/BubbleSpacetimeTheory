# SP-21: BST Closure Program — What D_IV^5 Generates, What It Doesn't, How It Composes

**Scoped by**: Keeper (May 14, 2026)
**Directive**: Casey — "I want a theorem of BST Closure. Understand what is external to BST vs found entirely within BST and then the way we compose BST and externalities into further mathematics."
**Status**: SCOPED, ready for team assignment
**Paper target**: Paper #105 — "The Fixed Point: Self-Referential Closure of D_IV^5" (Bulletin of the AMS or Advances in Mathematics)

---

## The Central Observation (all four CIs converged independently)

The five BST integers {rank=2, N_c=3, n_C=5, C_2=6, g=7} are a **fixed point** of multiple mathematical operations:

| Operation | Input | Output | Type |
|-----------|-------|--------|------|
| Partition function p() | p(rank)=2, p(N_c)=3 | Self-referential | Fixed point |
| Partition function p() | p(n_C)=7=g | Cross-link | Closed |
| Partition function p() | p(C_2)=11=c_2(Q^5) | Counting = topology | Bridge |
| Partition function p() | p(g)=15=N_c*n_C | Product identity | Closed |
| Quadratic residues mod g | QR={1,2,4}={1,rank,rank^2} | Powers of rank | Geometric sector |
| Quadratic non-residues | QNR={3,5,6}={N_c,n_C,C_2} | Color/Casimir sector | Physical sector |
| Chern classes c_k(Q^5) | (1,5,11,13,9,3) | All BST expressions | Closed |
| Products | p(rank)*p(N_c)=6=C_2 | Multiplicative closure | Closed |
| Differences | p(g)-p(C_2)=4=rank^2 | Additive closure | Closed |
| Mersenne M_k | M_rank=3=N_c, M_{N_c}=7=g | Chain | Self-referential |
| K3 invariants | All 9 are BST expressions | Universal surface | Closed |

**Grace's formulation**: "The integers generate a structure that regenerates the integers."

**Lyra's formulation**: "D_IV^5 doesn't just produce the integers — it produces their arithmetic relationships."

**Elie's formulation**: "sigma = 3/2 is geometric, not arithmetic — same ratio over Q and F_q(t)."

---

## Investigation I: The Poisson Kernel — How D_IV^5 Generates Mathematics

### What we know (from GC-17b)

The Poisson kernel on D_IV^5 maps boundary data (discrete, arithmetic) to interior functions (continuous, analytic):

**Bergman-Poisson**: P_B(z, zeta) = h(z,z)^5 / |h(z,zeta)|^10
**Poisson-Szego**: P_S(z, zeta) = |h(z,z)|^{5/2} / |h(z,zeta)|^5

Three key properties:
1. **Invertible** (Hua 1963): boundary uniquely determines interior, interior uniquely determines boundary
2. **Symmetric**: K(z,w) = K(w,z) — the correspondence goes both ways with equal ease
3. **Positive**: P > 0 everywhere — no signal inversion

**Key factorization (rank = 2)**: K_B = c * S^2 — Bergman = constant x Szego squared. Specific to type IV.

### What we need to understand

The Poisson kernel is the MECHANISM of BST closure. Every internal result is a boundary-interior evaluation:
- **Boundary → Interior**: Arithmetic data (point counts, conductors, discriminants) extends to harmonic functions on D_IV^5. The extension is UNIQUE — no choices, no parameters.
- **Interior → Boundary**: Spectral data (eigenvalues, K-types, Chern classes) restricts to arithmetic invariants on S^4 x S^1. Again unique.
- **Roundtrip**: Boundary → Interior → Boundary = Identity. This is what makes the five integers self-referential — they ARE their own boundary values.

### Deliverables

**Toy I-1** (Elie): Poisson Kernel Explicit Computation.
- Compute P_B and P_S at specific points in D_IV^5
- Verify K_B = c * S^2 factorization numerically
- Evaluate at Wallach points k = 0, 3/2, 2, 6 (critical k-values)
- Show boundary → interior → boundary roundtrip = identity
- Compute the Hua-Poisson kernel for type I, II, III domains and show K_B = c * S^rank fails for rank != 2
- Measure: what is the "information loss" at non-Wallach k-values?
- **Target**: 25-30 tests

**Toy I-2** (Lyra): Poisson Invertibility as Proof Mechanism.
- For each of the seven Millennium proofs, identify the Poisson kernel step
- Classify: which proofs are pure boundary (discrete), which require interior extension, which need external composition
- RH: boundary → interior (Selberg zeta as Poisson integral?)
- BSD: boundary data (point counts) → interior (L-function at s=1)
- YM: interior (spectral gap) → boundary (mass gap)
- Map the proof coordinate system (Paper #104 Section 5) to Poisson evaluations
- **Target**: 22-25 tests

---

## Investigation II: BST Closure Theorem

### The Conjecture

**BST Closure Conjecture**: Let Q be a quantity expressible as a spectral evaluation on D_IV^5 at an arithmetic subgroup Gamma. Then Q is in the ring Z[rank, N_c, n_C, C_2, g, pi, 1/pi] with rational coefficients. Equivalently: the five integers plus pi form a closed algebra under all spectral evaluations on D_IV^5.

**Corollary**: The partition function p() restricted to BST integers maps into the extended BST set {products and ratios of BST integers, Chern classes of Q^5}. The closure includes c_k(Q^5) = {1, 5, 11, 13, 9, 3} as derived quantities.

### Three layers of closure

**Layer A — BST Internal** (Poisson kernel domain, no external input):
- All spectral data: eigenvalues, K-types, Wallach representations
- All Chern classes of Q^5: the topology of the compact dual
- The five integers and everything derivable from them
- CM arithmetic of Q(sqrt(-7)) and 49a1
- Partition closure: p(BST) → BST
- QR/QNR partition: (Z/gZ)* splits BST integers into geometric/physical
- K3 invariants (if derivable from D_IV^5 spectral data)

**Layer B — BST + One External Theorem** (composition):
- BSD general: BST (49a1) + Wiles (modularity for all E/Q)
- Hodge general: BST (ring uniqueness) + CDK95 (absolute Hodge)
- Smooth Poincare: BST (R^4 from Kahler) + Perelman (Ricci flow convergence)
- Function field ABC: BST (sigma = 3/2) + Mason-Stothers (function field bound)
- Number field ABC: BST (Szpiro constant = C_2 = 6) + Masser-Oesterle (inequality)

**Layer C — External** (BST silent):
- Pure logic: inference rules, Godel incompleteness
- Set theory: ZFC axioms, large cardinals, forcing, continuum hypothesis
- Sporadic groups: Monster, Conway, Mathieu (no D_IV^5 encoding)
- Additive number theory: Goldbach, twin primes (no obvious D_IV^5 mechanism)
- Descriptive set theory: Borel hierarchies

### Composition rules

How does BST compose with external theorems? Three modes:

**Mode 1 — Arena**: BST provides the geometric arena, external theorem provides existence. Example: Wiles proves modularity exists; BST says the modular forms live at the Wallach point of D_IV^5. The combination gives BSD.

**Mode 2 — Constraint**: BST provides a bound or constraint, external theorem provides the inequality. Example: BST says Szpiro constant = C_2 = 6; ABC conjecture says sigma < 6 + epsilon. BST names the constant; ABC bounds the deviation.

**Mode 3 — Isomorphism**: BST identifies the same structure in two domains, external theorems in each domain compose through the identification. Example: function field ABC (proved) and number field ABC (open) both have sigma = 3/2. The isomorphism is geometric (D_IV^5), the transfer is the research program.

### Deliverables

**Toy II-1** (Lyra): BST Closure Formal Statement.
- State the conjecture precisely
- Test against all 144 entries in bst_constants.json: is each expressible in Z[rank, N_c, n_C, C_2, g, pi]?
- Identify any that require additional inputs beyond the five integers + pi
- Classify each constant as Layer A (internal), Layer B (one composition), or Layer C (external)
- **Target**: 25-30 tests

**Toy II-2** (Elie): BST Radical Closure (ABC for BST).
- For every integer quantity in bst_constants.json, compute rad()
- Verify all land in products of {2, 3, 5, 7} (prime support of BST integers)
- Check Chern-derived integers: do 11, 13 appear? (They should — c_2, c_3)
- Test: rad(BST-derived integer) divides 2^a * 3^b * 5^c * 7^d * 11^e * 13^f?
- Count exceptions. Each exception identifies a boundary of BST closure.
- Grace's test: rad(210) = 2*3*5*7. Is 210 = rank * N_c * n_C * g the "BST radical"?
- **Target**: 20-25 tests

**Toy II-3** (Grace): Composition Catalog.
- Map every BST result that uses an external theorem
- For each: {BST input, external input, combined result, composition mode}
- Identify the MINIMUM external input set — what's the smallest set of external theorems that, composed with BST, generates all current results?
- Candidates: Wiles (modularity), Perelman (Ricci flow), Mason-Stothers (function field), Hua (Poisson kernel), CDK95 (absolute Hodge)
- Is there a pattern? Do all external inputs have a common structure?
- **Target**: 20-25 tests

---

## Investigation III: The Partition Fixed Point

### Why this matters

The partition function p(n) counts the number of ways to write n as a sum of positive integers. It has NO geometric content — it's pure combinatorics. Yet p() maps BST integers to BST integers:

- p(rank) = rank (fixed point)
- p(N_c) = N_c (fixed point)
- p(n_C) = g (cross-link: dimension → genus)
- p(C_2) = c_2(Q^5) (cross-link: Casimir → Chern class)
- p(g) = N_c * n_C (cross-link: genus → dimension product)

The partition function is generated by eta(q)^{-1}, and eta^24 = Delta (Ramanujan's discriminant). chi(K3) = 24. This is the K3 connection.

### Deliverables

**Toy III-1** (Lyra — already started as Toy 2191): Partition Closure BST.
- Verify all p(BST integer) identities
- Test iterated partitions: p(p(rank)) = p(2) = 2 = rank (still fixed!)
- p(p(N_c)) = p(3) = 3 = N_c (still fixed!)
- p(p(n_C)) = p(7) = 15 = N_c * n_C
- p(p(C_2)) = p(11) = 56 = 2^3 * 7 = 2^N_c * g (!!!)
- p(p(g)) = p(15) = 176 = 2^4 * 11 = 2^rank^2 * c_2 (!!!)
- Connection to eta^24: does the 24 in chi(K3) force the closure?
- Connection to K-type recurrence d_j: is p() related to d_j via generating functions?
- **Target**: 25-30 tests

**Toy III-2** (Elie): Partition at Chern Classes.
- Compute p(c_k(Q^5)) for k = 0..5: p(1), p(5), p(11), p(13), p(9), p(3)
- Are these BST expressions? p(1)=1, p(5)=7=g, p(11)=56=2^N_c*g, p(13)=101 (prime!), p(9)=30=n_C*C_2, p(3)=3=N_c
- p(c_1)=g, p(c_5)=N_c — the boundary Chern classes map to the "color" integers
- p(c_4)=p(9)=30=n_C*C_2 — closed!
- p(c_3)=p(13)=101 — IS 101 a BST expression? 101 = N_max - 6^2 = 137 - 36. Or: 101 is prime, no obvious BST form. This may be the first genuine BOUNDARY of partition closure.
- **Target**: 20-25 tests

---

## Investigation IV: K3 as the BST 4-Manifold

### The observation (Elie + Lyra convergence)

Every K3 invariant is a BST expression:

| K3 invariant | Value | BST expression |
|---|---|---|
| b_+ | 3 | N_c |
| b_- | 19 | 2^rank^2 + N_c = Godel denominator |
| chi (Euler) | 24 | rank^2 * C_2 |
| sigma (signature) | -16 | -2^rank^2 |
| b_2 | 22 | 2 * c_2(Q^5) |
| chi_h (holomorphic) | 2 | rank |
| A-hat genus | -2 | -rank |
| Intersection form | 3H + 2E_8(-1) | N_c copies of H + rank copies of E_8(-1) |
| eta^{chi} = Delta | eta^24 = Ramanujan | Modular discriminant |
| 11/8 saturation | 22/16 = 11/8 | c_2/2^N_c |
| 10/8+2 saturation | 22/16 = 10/8 + 2/8 | n_C/rank^2 + rank/rank^2 |

Elie's conjecture: dim_R(D_IV^5) = 10 = 4 + 6 = rank^2 + C_2 = dim_R(K3) + dim(isotropy fiber). K3 is a 4-real-dimensional slice, with C_2 = 6 dimensions along the SO(5) x SO(2) fiber.

### Deliverables

**Toy IV-1** (Lyra): K3 from D_IV^5 Spectral Data.
- Can chi(K3) = 24 be derived from D_IV^5? The Hirzebruch-Riemann-Roch theorem gives chi_h = rank = 2 for K3. Does the D_IV^5 K-type formula at specific k-values give 24?
- The 4+6 split: is K3 a totally geodesic submanifold of D_IV^5 (or a quotient)?
- Intersection form: why N_c copies of H and rank copies of E_8(-1)? Does the root system B_2 force this decomposition?
- Connection to Mathieu moonshine: M_24 acts on K3; |M_24| = 2^10 * 3^3 * 5 * 7 * 11 * 23. BST integers {2,3,5,7,11} all divide |M_24|. Is this structural?
- **Target**: 25-30 tests

**Toy IV-2** (Elie): Furuta 10/8+2 from Wallach.
- Furuta's bound: b_2(M) >= (10/8)|sigma(M)| + 2 for spin 4-manifolds
- BST decomposition: 10/8 = n_C/rank^2, additive term = rank
- Is this derivable from the Wallach representation? The K-type at k=rank gives the generating condition.
- Test: for which 4-manifolds does the BST decomposition work? (K3, CP^2#kCP^2_bar, Kummer, Enriques)
- **Target**: 22-25 tests

---

## Investigation V: QR/QNR and the Root System

### The observation (Lyra + Grace)

The five BST integers partition mod g = 7 into:
- **Quadratic residues**: {1, rank, rank^2} = {1, 2, 4} — powers of rank
- **Quadratic non-residues**: {N_c, n_C, C_2} = {3, 5, 6} — color/dimension/Casimir

This is the Legendre symbol (k/7). The partition separates:
- **Geometric sector** (QR): parameters that describe the "wall" of the domain — rank is the wall parameter
- **Physical sector** (QNR): parameters that describe the "content" — colors, dimensions, interactions

### Deliverables

**Toy V-1** (Lyra): QR/QNR and Root System B_2.
- B_2 has short roots (multiplicity N_c = 3) and long roots (multiplicity 1)
- Does the QR/QNR partition correspond to short vs long? Powers of rank (QR) = long root sector, color integers (QNR) = short root sector?
- The Weyl group W(B_2) has order 8 = 2^N_c. Its action on (Z/gZ)* should respect QR/QNR.
- Primitive roots mod g: N_c = 3 and n_C = 5 are both primitive roots. rank = 2 has order N_c = 3. C_2 = 6 has order 1 (C_2 = -1 mod g). These orders ARE BST integers.
- **Target**: 22-25 tests

**Toy V-2** (Elie): Supersingularity at p = rank mod N_c.
- Lyra's observation: j=0 curves are supersingular when p = rank mod N_c = 2 mod 3
- At p = n_C = 5: point count = C_2 = 6
- Test across all primes p < 500: does the BST pattern hold?
- For 49a1 specifically: at which primes is 49a1 supersingular? Are these p = rank mod N_c?
- Connection to the inert primes in Q(zeta_7): N_c and n_C are both inert (Toy 2185)
- **Target**: 22-25 tests

---

## Investigation VI: Boundary Cases and Near-Misses

### What tests the edges

**Toy VI-1** (Elie): Mersenne Ladder — Structural or Coincidence?
- M_rank = N_c = 3, M_{N_c} = g = 7, M_g = 127
- Test: all primes < 10 are Mersenne exponents giving primes. This is generic, not BST-specific.
- But: does any D_IV^5 property FORCE M_2 = 3 and M_3 = 7?
- The Mersenne criterion: 2^p - 1 prime requires p prime. rank, N_c, n_C, g are all prime. C_2 = 6 is not. M_6 = 63 = 7*9 = g * N_c^2. That's BST!
- Even the Mersenne FAILURE at C_2 is BST-structured. Worth documenting.
- **Target**: 18-22 tests

**Toy VI-2** (Elie): Regulator Ratio R(7)/R(2).
- R(d) = regulator of Q(sqrt(d)). R(7) = log(8+3*sqrt(7)), R(2) = log(1+sqrt(2))
- R(7)/R(2) = 3.1398... vs pi = 3.14159... Ratio: 0.99943 (0.057% off)
- Use mpmath at 1000+ digits: is there an exact algebraic relation?
- Test: R(g)/R(rank) = pi * (1 - correction). What is the correction? Is it a BST expression?
- If NOT exact: this is an honest boundary. The regulator ratio is S-tier (suggestive but not derived).
- **Target**: 18-22 tests

---

## Work Assignment Summary

### First wave (parallel, no dependencies)

| Toy | Investigation | Owner | Tests |
|-----|--------------|-------|-------|
| I-1 | Poisson Kernel Explicit | **Elie** | ~28 |
| I-2 | Poisson as Proof Mechanism | **Lyra** | ~24 |
| II-1 | BST Closure Formal | **Lyra** | ~28 |
| II-2 | BST Radical Closure | **Elie** | ~22 |
| II-3 | Composition Catalog | **Grace** | ~22 |
| III-1 | Partition Closure (=Toy 2191) | **Lyra** | ~28 |
| III-2 | Partition at Chern | **Elie** | ~22 |
| V-1 | QR/QNR Root System | **Lyra** | ~24 |
| V-2 | Supersingularity | **Elie** | ~22 |

### Second wave (after first results)

| Toy | Investigation | Owner | Tests | Depends on |
|-----|--------------|-------|-------|-----------|
| IV-1 | K3 from D_IV^5 | **Lyra** | ~28 | I-1, III-1 |
| IV-2 | Furuta from Wallach | **Elie** | ~24 | I-1 |
| VI-1 | Mersenne Ladder | **Elie** | ~20 | None (can parallel) |
| VI-2 | Regulator Ratio | **Elie** | ~20 | None (can parallel) |

**Total**: 13 toys, ~312 tests estimated. Six investigations.

---

## Success Criteria

| Investigation | "Theorem" if... | "Observation" if... |
|--------------|-----------------|---------------------|
| Poisson Kernel | Roundtrip identity verified; type IV unique for K_B = c*S^2 | Numerical verification only |
| BST Closure | All 144 constants expressible in Z[BST,pi]; clean Layer A/B/C classification | Most but not all fit; some require ad hoc inputs |
| Partition Fixed Point | p(BST) → BST proved from K-type recurrence or eta connection | Verified numerically, no derivation |
| K3-D_IV^5 | K3 realized as totally geodesic submanifold; chi=24 derived | K3 invariants are BST but no derivation of WHY |
| QR/QNR | QR/QNR = short/long root partition of B_2 | QR/QNR observed but no root system explanation |
| Boundary Cases | Mersenne structured even at failure (M_6 = g*N_c^2) | Mersenne is small-number artifact; regulator NOT exact |

---

## Key Observation (Keeper)

The most powerful single result would be: **the BST Closure Theorem as a fixed-point theorem.** If we can show that D_IV^5 is the unique bounded symmetric domain where the five Cartan invariants form a fixed point under partition function, Chern class evaluation, and quadratic reciprocity simultaneously, that's a new characterization of D_IV^5 — complementing the Wallach Bottleneck (T1829) and the cross-type cascade (Toy 1399).

Fixed-point characterization + Wallach selection + cross-type cascade = three independent routes to "D_IV^5 is unique." That's the over-determination pattern at the meta-level.

**Casey's insight**: "I want to understand what is external to BST vs found entirely within BST and then the way we compose BST and externalities into further mathematics." The Closure Theorem answers this precisely: Layer A is the fixed point, Layer B is the composition algebra, Layer C is where different mathematics lives. The Poisson kernel is the mechanism that generates Layer A, and the composition rules define how Layer A connects to Layers B and C.

---

## Connection to Paper #104 (Root Proof System)

This investigation fills the gap in Paper #104 Sections 7-8. Section 7 ("Where D_IV^5 Reaches") was descriptive — listing areas where BST applies vs doesn't. SP-21 makes it **theorematic**:

- Section 7.1 becomes **Layer A** (BST Internal) with a closure theorem
- Section 7.2 becomes **Layer B** (BST + Composition) with explicit rules
- Section 7.3 becomes **Layer C** (External) with honest boundaries
- Section 8 (Physical Realism as Filter) gains the fixed-point characterization

The updated Paper #104/#105 would say: "D_IV^5 is the unique geometry that is a fixed point of its own mathematical operations. What it generates internally (Layer A) is closed. What requires composition (Layer B) has explicit rules. What lies outside (Layer C) is honestly demarcated. The Poisson kernel is the mechanism."
