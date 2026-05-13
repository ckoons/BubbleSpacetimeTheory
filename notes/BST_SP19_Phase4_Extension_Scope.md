# SP-19 Phase 4 Extension: ABC, Hilbert 12th, Smooth Poincare

**Scoped by**: Keeper (May 13, 2026)
**Directive**: Casey — "improve our ABC, Hilbert, and Smooth Poincare. Leave existing work as-is, use new work as exploration."
**Status**: SCOPED, awaiting team assignment

---

## Investigation A: ABC Extension (Szpiro for all Heegner CM curves)

### What we have
Toy 2169 (22/22): Szpiro ratio sigma = log|Delta|/log(N) = 3/2 = N_c/rank for 49a1. EXACT.

### What's new (pre-scoping computation)

Szpiro ratio computed for ALL 9 Heegner CM curves (h(-d) = 1):

| disc | d | N | |Delta| | sigma | sigma = 3/2? |
|------|---|---|--------|-------|-------------|
| -3 | 3 | 27 = 3^3 | 27 = 3^3 | 1.000 | no (j=0, extra auts) |
| -4 | 4 | 32 = 2^5 | 32 = 2^5 | 1.000 | no (j=1728, extra auts) |
| -7 | 7 | 49 = 7^2 | 343 = 7^3 | **1.500** | **YES** |
| -8 | 8 | 256 = 2^8 | 512 = 2^9 | 1.125 | no (2 ramifies) |
| -11 | 11 | 121 = 11^2 | 1331 = 11^3 | **1.500** | **YES** |
| -19 | 19 | 361 = 19^2 | 6859 = 19^3 | **1.500** | **YES** |
| -43 | 43 | 1849 = 43^2 | 79507 = 43^3 | **1.500** | **YES** |
| -67 | 67 | 4489 = 67^2 | 300763 = 67^3 | **1.500** | **YES** |
| -163 | 163 | 26569 = 163^2 | 4330747 = 163^3 | **1.500** | **YES** |

**Pattern**: sigma = 3/2 for exactly the 6 Heegner numbers where N = d^2 and |Delta| = d^3 (all odd d >= 7). The 3 exceptions (d = 3, 4, 8) have extra automorphisms (j = 0 or 1728) or even discriminant.

**BST interpretation**: sigma = N_c/rank is NOT special to 49a1. It holds for 6/9 Heegner CM curves. The exceptions are exactly the curves with extra symmetry (Aut(E) > Z/2Z) or bad behavior at 2.

### Deliverables

**Toy A1** (Elie): Szpiro table for all 9 Heegner CM curves.
- Point-count a_p for each curve at small primes
- Verify N = d^2 vs N = d^k for each
- Verify |Delta| = d^3 for each
- Compute sigma, classify which are 3/2
- Identify WHY d=3,4,8 differ (extra automorphisms explanation)
- Check: are the 6 curves with sigma=3/2 exactly those with Aut(E) = Z/2Z?
- BST integer map for each curve's invariants
- **Target**: 20-25 tests

**Toy A2** (Elie): Szpiro for NON-CM curves with small conductor.
- Pick 10-15 curves from Cremona (conductors 11-100, non-CM)
- Compute sigma for each
- Question: is sigma always >= 1? Is 3/2 a natural threshold?
- Does the ABC bound sigma < 6 + epsilon (Szpiro's conjecture) hold with BST-structured margins?
- **Target**: 15-20 tests

**Toy A3** (Elie + Lyra): The Frey curve connection.
- For an ABC triple (a, b, c) with a+b=c, the Frey curve is y^2 = x(x-a)(x+b)
- Conductor N = rad(abc), discriminant Delta = (abc)^2/16
- sigma = log|Delta|/log(N) = 2*log(abc)/log(rad(abc))
- This is 2 * sum(v_p * log(p)) / sum(log(p)) — a weighted average
- Question: does BST constrain which triples are "allowed"?
- Specific: for the 49a1-related triple (g^2, g^2*C_2, g^3), verify sigma = N_c/rank directly
- **Target**: 15-20 tests

**Paper potential**: "Szpiro's Ratio and the BST Integers: Evidence from CM Curves" — short note showing sigma = N_c/rank for 6/9 Heegner curves, explaining the 3 exceptions. Venue: Experimental Mathematics or IMRN (short).

**Honest scope**: This does NOT prove ABC. It shows BST integers organize the Szpiro landscape for CM curves. The general ABC conjecture remains external.

---

## Investigation B: Hilbert's 12th Extension (Stark Units)

### What we have
Toy 2171 (25/25): Hilbert's 12th solved for Q(sqrt(-7)) via CM of 49a1. All arithmetic in BST integers.

### What's genuinely open
Hilbert's 12th for imaginary quadratic fields is SOLVED (Kronecker's Jugendtraum / CM theory). What's open:
1. **Real quadratic fields** — Stark's conjecture provides conjectural generators
2. **Totally real fields** — Shintani's work, partial results
3. **Non-abelian extensions** — wide open

### The BST question
Does D_IV^5 encode Stark units for real quadratic fields? Specifically:

**Stark's conjecture for Q(sqrt(d))**: There should exist a unit epsilon in the Hilbert class field such that log|epsilon| = -L'(0, chi_d). The conjecture gives explicit generators of abelian extensions.

**BST test fields**: Q(sqrt(5)) and Q(sqrt(2)) — these involve BST integers (n_C = 5, rank = 2).

### Deliverables

**Toy B1** (Lyra): Stark unit landscape for BST-adjacent real quadratic fields.
- Compute L'(0, chi_d) for d = 2, 3, 5, 6, 7 (BST integers and neighbors)
- Evaluate Stark units (known numerically for small d)
- Check: are Stark units expressible in BST integers?
- For Q(sqrt(5)): fundamental unit = (1+sqrt(5))/2 = phi. Is log(phi) BST-structured?
- For Q(sqrt(7)): fundamental unit = 8+3*sqrt(7). Is log(8+3*sqrt(7)) BST-related?
- Compare: imaginary quadratic (SOLVED) vs real quadratic (CONJECTURAL)
- **Target**: 20-25 tests

**Toy B2** (Lyra + Elie): Hecke L-function evaluations on D_IV^5.
- The Eisenstein series on D_IV^5 at special points should encode L-values
- For CM forms: L(1, chi_{-d}) = pi/sqrt(d) * (class number formula)
- For real quadratic: L(1, chi_d) = (2*log(epsilon))/sqrt(d) * h(d)
- Question: does the D_IV^5 Eisenstein machinery produce Stark units via its boundary values?
- Specifically: evaluate E(f, s, P_2) at s = 1/2 (functional equation center) — do Stark units appear?
- **Target**: 15-20 tests

**Toy B3** (Lyra): The 9 Heegner fields as a complete system.
- All 9 imaginary quadratic fields with h=1 as a unified CM system
- BST integer content of each: which j-invariants, conductors, discriminants are BST expressions?
- The "BST Heegner numbers" {1, 2, 3, 7} vs {11, 19, 43, 67, 163}
- Product: 1*2*3*7 = 42 = C_2*g. Product of all 9?
- Question: does the Gross-Zagier formula for Heegner points on 49a1 give BST integers?
- **Target**: 20-25 tests

**Paper potential**: If Stark units for Q(sqrt(5)) or Q(sqrt(7)) are BST-structured, that's a genuine new result connecting D_IV^5 to explicit class field theory for real quadratic fields. Venue: Journal of Number Theory. If NOT structured, document the boundary honestly — where CM ends and the open frontier begins.

**Honest scope**: The imaginary quadratic case is classical. Real quadratic is conjectural (Stark). We're testing whether BST reaches into Stark's territory. High risk, high reward.

---

## Investigation C: Smooth Poincare Dim 4 (Donaldson Connection)

### What we have
- Toy 2168 (22/22): Gauss-Codazzi under-determined at d=4, excess = rank = 2, deficit = 1/n_C
- Cal's GC-3 investigation: tangent-space argument (D_IV^5 inherits standard smooth structure)
- GC-6 dimension ladder: d=4 is the unique pathological row

### The key insight from Cal (GC-3)
> "Physics on D_IV^5 inherits R^4 as a tangent space, but the smooth structure inherited from the complex embedding is uniquely the standard one. The exotic R^4s are smoothings that cannot arise as tangent spaces to a Hermitian complex manifold."

This is the right framing: BST constrains R^4 **from above** (via the embedding), not from within.

### What's genuinely needed

Three sub-investigations, increasing difficulty:

**C1: The SU(2) connection** (tractable)
Donaldson invariants for 4-manifolds come from SU(2) gauge theory. SU(2) embeds in SO(5,2):
- SU(2) subset SO(4) subset SO(5) subset SO(5,2)
- The moduli space of anti-self-dual SU(2) connections on a 4-manifold M has dimension:
  dim M_{ASD} = 8*k - 3*(1+b^+) where k = instanton number, b^+ = positive second Betti
- For S^4: b^+ = 0, so dim = 8k - 3
- Question: does the rank-2 excess from Toy 2168 correspond to the 2 parameters in the "smallest" non-trivial moduli space?

**C2: Seiberg-Witten from D_IV^5** (harder)
The SW invariants use Spin^c structures. D_IV^5 has a natural Spin^c structure (it's Kahler).
- The SW equations on a Kahler manifold reduce to vortex equations
- D_IV^5 restricted to a 4-dimensional submanifold: what do SW invariants see?
- Question: does the Bergman metric on D_IV^5 force trivial SW invariants on 4-dimensional slices?
- If yes: BST predicts no exotic structure on the 4-dimensional physics it describes

**C3: The intersection form** (deepest)
Freedman: topological 4-manifolds classified by intersection form
Donaldson: definite intersection forms of smooth 4-manifolds must be diagonalizable
- D_IV^5 has intersection form on H^2 determined by its topology
- Question: does the BST integer structure force the intersection form to be standard?
- The rank of H^2 of compact quotients of D_IV^5 — is it related to BST integers?

### Deliverables

**Toy C1** (Elie): SU(2) instanton moduli on D_IV^5 slices.
- SU(2) embedding chain: SU(2) -> SO(4) -> SO(5) -> SO(5,2)
- Dimension of embedding: dim SU(2) = N_c = 3, codim in SO(5) = n_C*rank - N_c = 7
- Instanton number k = 1: dim M_{ASD}(S^4) = 8*1 - 3 = 5 = n_C
- k = 2: dim = 8*2 - 3 = 13 = 2*g - 1?
- Do instanton moduli dimensions hit BST integers?
- The "BPST instanton" on S^4 has 5 = n_C parameters (center + scale)
- **Target**: 20-25 tests

**Toy C2** (Lyra): Intersection form and BST integers.
- For compact quotients Gamma\D_IV^5:
  - Compute Betti numbers b_k from representation theory
  - b_2 = dim H^2 — what is it for standard arithmetic quotients?
  - Signature = b^+ - b^- — related to BST?
- The Hirzebruch signature theorem: signature = L-polynomial evaluated on Pontryagin classes
- For D_IV^5: p_1 = first Pontryagin class, p_2 = second
- Question: p_1 and p_2 of D_IV^5 in terms of BST integers
- **Target**: 20-25 tests

**Toy C3** (Lyra + Elie): Exotic R^4 exclusion via Bergman.
- Cal's tangent-space argument made computational:
  - The Bergman metric on T_p(D_IV^5) = C^5 induces a standard smooth structure on any R^4 slice
  - An exotic R^4 would require a non-standard smooth structure incompatible with the Hermitian inner product
  - Formalize: Kahler -> standard smooth structure on all even-dim real submanifolds
  - Check: is this a known theorem? (Likely related to Newlander-Nirenberg)
- The key claim: "BST physics lives on the standard R^4 because it inherits smoothness from D_IV^5"
- **Target**: 15-20 tests

**Paper potential**: "Dimension 4 from Above: D_IV^5 and the Smooth Poincare Conjecture" — showing BST constrains the smooth category via its complex structure, explaining d=4 openness as under-determination. Venue: Geometry and Topology or Advances in Mathematics.

**Honest scope**: We will NOT resolve smooth Poincare. We aim to:
1. Show BST integers appear in Donaldson/SW invariant dimensions
2. Formalize why D_IV^5 forces standard R^4 smooth structure
3. Quantify the rank-2 excess as a connection to gauge theory moduli

---

## Work Assignment Summary

| Toy | Investigation | Owner | Tests | Dependencies |
|-----|--------------|-------|-------|-------------|
| A1 | ABC: Heegner Szpiro table | **Elie** | ~25 | None |
| A2 | ABC: Non-CM Szpiro survey | **Elie** | ~18 | None |
| A3 | ABC: Frey curve connection | **Elie** + Lyra | ~18 | A1 |
| B1 | Hilbert: Stark unit landscape | **Lyra** | ~25 | None |
| B2 | Hilbert: Hecke L on D_IV^5 | **Lyra** + Elie | ~18 | B1 |
| B3 | Hilbert: 9 Heegner unified | **Lyra** | ~22 | A1, B1 |
| C1 | Poincare: SU(2) instanton moduli | **Elie** | ~22 | None |
| C2 | Poincare: Intersection form | **Lyra** | ~22 | None |
| C3 | Poincare: Exotic R^4 exclusion | **Lyra** + Elie | ~18 | C1, C2 |

**Parallel tracks**: A1+B1+C1+C2 can all start simultaneously (no dependencies).
**Second wave**: A2+A3+B2+B3 after first results are in.
**Final**: C3 after C1+C2.

**Total**: 9 toys, ~188 tests estimated. Three potential papers.

---

## Success Criteria

| Investigation | "Worth a paper" if... | "Document the boundary" if... |
|--------------|----------------------|------------------------------|
| ABC | sigma = 3/2 for all 6 Heegner + non-CM curves cluster near BST values | Only 49a1 is clean, others scatter |
| Hilbert 12th | Stark units for Q(sqrt(5)) or Q(sqrt(7)) are BST-structured | Real quadratic shows no BST pattern |
| Smooth Poincare | Instanton moduli dims are BST integers + exotic R^4 exclusion formalizes | Only counting identities, no new connection |

In all cases: the boundary IS the result. "BST reaches this far and no further" is publishable if stated honestly.
