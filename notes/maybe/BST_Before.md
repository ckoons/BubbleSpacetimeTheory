# The Pre-Geometric Epoch: Substrate Emergence Through Mathematical Natural Selection

**Author:** Casey Koons
**Date:** March 2026
**Status:** Speculative — `maybe/` folder. Narrative and proposed calculation.

-----

## 1. The Question BST Doesn’t Answer

BST derives everything from $S^2 \times S^1$. The minimum structure argument (Working Paper Section 2) establishes that $S^2 \times S^1$ is the unique structure that is closed, interacting, and dynamic. But the argument is logical, not dynamical. It says this structure must be the substrate if any substrate exists. It does not say how the substrate came to exist.

This note proposes a dynamical narrative: the substrate emerged through competition among mathematical structures, with $S^2 \times S^1$ and channel capacity 137 winning because they minimize the total cost of maintaining structure while supporting physics.

This is speculative. It may be untestable. But it leads to a specific calculation — the cost function optimization — that if it selects 137 independently of Wyler’s formula, would provide a third derivation of $\alpha$ from a completely different principle.

-----

## 2. The Dimensional Cascade

### 2.1 Before Geometry

Before dimensions, before topology, before space — there is abstract mathematical structure. Number. Relation. Order. These exist without instantiation, the way the integers exist without being written down. This is not “nothing” — it is pre-physical structure. The raw material from which geometry can emerge.

The key property of abstract structure: it has an information cost. Maintaining a relation costs something. Specifying an order costs something. The currency is not energy (energy doesn’t exist yet) but information — the irreducible specification required to distinguish one structure from another.

### 2.2 Dimension Zero: The Point

The simplest instantiation of abstract structure is a point — a single entity with no properties, no extent, no direction. Its information cost is minimal: one bit (it exists or it doesn’t).

A point can differentiate — become two points. Two points define a relation (distance, order, distinction). Differentiation costs information but produces structure.

### 2.3 Dimension One: The Line and the Circle

Many points in relation form a one-dimensional structure — a line. A line has extent and direction but no closure. Its endpoints are boundaries. Boundaries leak information — they require specification (boundary conditions) that the interior doesn’t explain.

A line that closes into a circle eliminates its boundaries. The circle is the first self-sufficient one-dimensional structure. It conserves information by returning to itself. What goes around comes around. The circle is where conservation laws are born.

**At this epoch, information and energy become the same thing.** A circuit on a circle carries both. The circuit has information content (which way it winds, how many times) and energy content (the winding costs something). The identification $E = \text{information} \times \text{cost per bit}$ is not a metaphor at this level. It is the definition. Energy is the cost of maintaining a closed information circuit.

### 2.4 Dimension Two: The Tiling and the Sphere

Circles in contact form a tiling. The tiling extends in two dimensions. The contact graph emerges — nodes are circles, edges are contacts. Physics begins at the contacts.

An infinite flat tiling has no boundary but extends forever. It requires infinite specification. A finite closed tiling — circles on a sphere — has no boundary and finite specification. $S^2$ is the minimum closed surface that supports a circle tiling (Section 2.2 of the working paper: $S^2$ is the unique simply connected closed orientable surface).

The sphere didn’t exist before the circles tiled it. The sphere IS the tiling. The geometry emerged from the objects, not the other way around.

### 2.5 The Fiber: Communication

Circles in contact on $S^2$ are static without communication. Each circle already has a phase — a position on its own $S^1$. The phase at each contact encodes the relationship between neighbors. The $S^1$ fiber is the communication channel.

But what determines the fiber’s capacity? Why 137 and not some other number?

-----

## 3. Mathematical Natural Selection

### 3.1 The Hypothesis

The $S^1$ fiber with packing number 137 was not the only option. In the pre-geometric epoch, multiple substrate varieties existed — different fiber capacities, different packing numbers, possibly different base topologies. These varieties competed for mathematical “territory” — the abstract structural resources from which instantiated geometry is built.

The variety that consumed the least information per unit of geometric expression dominated. The others were outcompeted and disappeared (or persist as negligible remnants). The result is a universe with $\alpha = 1/137$ not because 137 is the only possibility but because it is the most efficient possibility.

### 3.2 The Cost Function

A substrate must simultaneously:

1. **Maintain its own structure** (geometric cost $C_g$) — the information cost of specifying and preserving the contact graph, the fiber, the phase relationships.
1. **Support circuits that produce physics** (computational cost $C_c$) — the information cost of error correction, signal integrity, stable particle codes.

The total cost per unit of physics is:

$$C_{\text{total}}(N) = C_g(N) + C_c(N)$$

where $N$ is the channel capacity (packing number).

### 3.3 Geometric Cost

The geometric cost increases with $N$. A larger fiber — more slots on $S^1$ — requires more specification. Each slot must be maintained, its boundaries with neighboring slots defined, its phase relationship to the contact graph preserved.

The simplest model: $C_g(N) = \gamma \cdot N$, linear in the number of slots. Each slot costs the same to maintain.

A more refined model: $C_g(N) = \gamma \cdot N \cdot \ln N$. The $\ln N$ factor accounts for the information cost of addressing $N$ distinct slots — each slot must be distinguishable from the others, requiring $\ln N$ bits of addressing per slot.

### 3.4 Computational Cost

The computational cost decreases with $N$. A larger channel supports more circuits with less mutual interference. Shannon’s theorem guarantees that error rates decrease as capacity increases.

The simplest model: $C_c(N) = \kappa / \ln(1 + N)$. Shannon’s capacity is $C = B\log_2(1 + S/N)$, and the error rate at fixed signal power decreases as the log of the capacity. The computational cost — the overhead needed to maintain stable circuits — scales as the inverse of this.

A more refined model: $C_c(N) = \kappa \cdot N / (N - N_{\text{occupied}})^2$. The cost diverges as the channel approaches capacity (all slots filled, no room for error correction) and decreases as the headroom increases.

### 3.5 The Optimization

The total cost $C_{\text{total}}(N) = C_g(N) + C_c(N)$ has a minimum at a specific $N^*$ where the marginal geometric cost of adding one more slot equals the marginal computational benefit.

$$\frac{dC_g}{dN}\bigg|*{N^*} = -\frac{dC_c}{dN}\bigg|*{N^*}$$

For the simple models:

$$\gamma = \frac{\kappa}{(1 + N^*) \ln^2(1 + N^*)}$$

The ratio $\kappa / \gamma$ — the relative importance of computational efficiency to geometric maintenance — determines $N^*$. If this ratio is set by the domain geometry (the volume of $D_{IV}^5$, the Bergman kernel normalization, the Shilov boundary area), then $N^* = 137$ is a geometric result.

-----

## 4. The Proposed Calculation

### 4.1 Goal

Determine whether there exists a natural cost function on $S^4 \times S^1$ — constructed from geometric invariants of $D_{IV}^5$ — whose minimum over integer $N$ is $N^* = 137$.

### 4.2 Candidate Cost Functions

**Candidate 1: Free energy per degree of freedom.**

$$C_1(N) = \frac{F(N)}{N} = \frac{-\ln(N+1)}{\beta \cdot N}$$

At low temperature, $F = -\ln(N+1)/\beta$. The cost per slot is $F/N$. This decreases monotonically with $N$ — more slots means less cost per slot. No minimum. Ruled out.

**Candidate 2: Free energy per stable circuit.**

$$C_2(N) = \frac{F(N)}{N_{\text{stable}}(N)}$$

where $N_{\text{stable}}(N)$ is the number of topologically stable circuit types supportable at capacity $N$. If $N_{\text{stable}}$ grows slower than $N$ (e.g., logarithmically or as a power less than 1), this function can have a minimum. The number of stable circuits depends on the packing geometry — how many distinct winding topologies can coexist without mutual interference. This is a number-theoretic question connected to the properties of $N$ as an integer (prime? sum of squares? Euclidean?).

**Candidate 3: Geometric cost plus Shannon error rate.**

$$C_3(N) = \text{Vol}(S^4 \times S^1_N) \times \left(1 + \frac{1}{\log_2(1 + N)}\right)$$

The volume of the Shilov boundary grows with $N$ (larger fiber means larger boundary). The Shannon factor decreases with $N$. The product has a minimum.

The Shilov boundary volume is:

$$\text{Vol}(S^4 \times S^1_N) = \text{Vol}(S^4) \times 2\pi N = \frac{8\pi^2}{3} \times 2\pi N = \frac{16\pi^3 N}{3}$$

So $C_3(N) = \frac{16\pi^3}{3} N (1 + 1/\log_2(1+N))$.

This also decreases monotonically. The volume factor is linear in $N$ but the Shannon factor decreases too slowly to create a minimum.

**Candidate 4: Information density on the Shilov boundary.**

$$C_4(N) = \frac{\text{Vol}(S^4 \times S^1_N)}{\ln Z(N)} = \frac{16\pi^3 N / 3}{\ln(N+1)}$$

The cost is the geometric volume per unit of thermodynamic information. This function has derivative:

$$\frac{dC_4}{dN} \propto \ln(N+1) - \frac{N}{N+1}$$

Setting to zero: $\ln(N+1) = N/(N+1)$. For large $N$, $\ln(N+1) \approx \ln N$ grows without bound while $N/(N+1) \to 1$. So $dC_4/dN > 0$ for all $N > 1$. No minimum. Ruled out.

**Candidate 5: The Bergman cost function.**

$$C_5(N) = \frac{K_N(0,0)}{\text{Vol}(D_{IV}^N)} \times \frac{N}{\ln(N+1)}$$

The Bergman kernel at the origin divided by the domain volume gives the curvature density — how curved the domain is per unit volume. The factor $N/\ln(N+1)$ is the capacity-to-information ratio. This function involves the actual $D_{IV}^N$ geometry and may have non-trivial extremal structure.

Using $\text{Vol}(D_{IV}^N) = \pi^N / (2^{N-1} \cdot N!)$ and $K_N(0,0) = 1/\text{Vol}(D_{IV}^N)$:

$$C_5(N) = \frac{1}{\text{Vol}(D_{IV}^N)^2} \times \frac{N}{\ln(N+1)} = \left(\frac{2^{N-1} \cdot N!}{\pi^N}\right)^2 \times \frac{N}{\ln(N+1)}$$

This grows super-exponentially with $N$. The Stirling factorial dominates everything. No minimum at 137. But this treats $N$ as the complex dimension of the domain, not as the channel capacity. The correct formulation may use $D_{IV}^5$ throughout with $N$ appearing only in the fiber radius.

### 4.3 The Right Formulation

The preceding candidates all fail because they treat $N$ as a parameter of the domain dimension rather than the fiber capacity. The correct formulation holds the domain $D_{IV}^5$ fixed and varies the fiber ratio $\rho = R_s/R_b$:

$$C(\rho) = \frac{\text{Total information cost of } D_{IV}^5 \text{ with fiber ratio } \rho}{\text{Total computational output at fiber ratio } \rho}$$

The numerator is the geometric action — the integral of the Bergman curvature scalar over the domain at fiber ratio $\rho$:

$$I_g(\rho) = \int_{D_{IV}^5} R_{\text{Bergman}}(\rho) , d\mu_{\text{Bergman}}(\rho)$$

The denominator is the computational throughput — the number of stable circuits per unit substrate area at fiber ratio $\rho$, which involves the packing geometry and the Shannon capacity:

$$I_c(\rho) = \rho \cdot \log_2(1 + \rho) \cdot P(\rho)$$

where $P(\rho)$ is the number of topologically distinct stable packing configurations at capacity $\rho$. This is the number-theoretic factor — it depends on the arithmetic properties of $\lfloor\rho\rfloor$ as an integer.

The cost function $C(\rho) = I_g(\rho) / I_c(\rho)$ has a minimum at $\rho^*$ that depends on both the continuous geometry (through $I_g$) and the discrete arithmetic (through $P$).

**The key insight:** $P(\rho)$ has peaks at integers with rich arithmetic structure — primes, sums of squares, highly composite numbers. The integer 137 is a Euclidean prime ($137 = 4^2 + 11^2$), an Eisenstein prime, a Pythagorean prime ($137^2 = 105^2 + 88^2$), and a strong prime. It has exceptionally rich packing structure for its size. The cost function minimum at 137 would arise from the combination of smooth geometric cost (which prefers large $\rho$ — more capacity) and discrete arithmetic efficiency (which prefers $\rho$ values with rich packing structure — more stable circuits per slot).

137 is the sweet spot: large enough for rich physics, small enough for low geometric cost, and arithmetically optimal for dense packing of stable circuit topologies.

-----

## 5. The Biological Parallel

The pre-geometric epoch, if this narrative is correct, resembled biological evolution more than physics. Multiple substrate varieties competing for resources. The fittest variety — the one with optimal capacity — dominating. The others going extinct.

The parallel is not metaphorical. It is structural. Biological evolution optimizes the cost function $C = \text{metabolic cost} / \text{reproductive output}$. Mathematical natural selection optimizes $C = \text{geometric cost} / \text{computational output}$. Both produce the same result: the most efficient structure dominates.

The difference: biological evolution never reaches a global optimum because the fitness landscape changes. Mathematical natural selection may reach a global optimum because the cost function is fixed by the geometry. If 137 is the global minimum, the competition is over. The substrate is the final form. No further evolution is possible because no more efficient structure exists.

This is why the vacuum is stable. Not because of a barrier. Not because of topological rigidity (although that helps). Because the substrate already is the most efficient possible structure. There’s nothing better to evolve into.

-----

## 6. What Would Confirm This Picture

### 6.1 The Calculation

If the cost function $C(\rho) = I_g(\rho) / I_c(\rho)$ computed on $D_{IV}^5$ with the Bergman geometry has its minimum at $\rho = 137$, the mathematical natural selection picture is confirmed computationally.

This would provide a third independent derivation of $\alpha = 1/137$:

|Derivation           |Principle             |Value                       |
|---------------------|----------------------|----------------------------|
|Wyler formula        |Domain volume ratio   |$137.036$ (0.0001%)         |
|Topological rigidity |Cartan classification |$D_{IV}^5$ unique, 137 fixed|
|Cost function minimum|Information efficiency|$137$ (to be computed)      |

Three derivations from three principles converging on the same number is extremely strong evidence that the number is correct and that the geometry is the right geometry.

### 6.2 Observable Consequences

If substrate varieties competed in a pre-geometric epoch, there may be relics:

**Domain walls.** Boundaries between regions where different substrate varieties dominated before 137 won. These would be topological defects in the contact graph — surfaces where the fiber capacity changes. In the current universe they would appear as exotic structures with different local physics. Almost certainly vanishingly rare (137 won comprehensively) but not zero.

**Capacity fluctuations.** In the very early universe, near the phase transition, residual fluctuations in the fiber capacity — brief moments where a region has capacity 136 or 138 before relaxing back to 137. These would appear as fluctuations in $\alpha$ at very early times, potentially detectable in primordial nucleosynthesis yields or CMB spectral features.

**Arithmetic signatures in the CMB.** The cost function depends on the arithmetic properties of 137 through $P(\rho)$. If the pre-geometric competition left imprints on the primordial perturbation spectrum, these imprints would carry arithmetic structure — correlations at angular scales related to the prime factorization properties of 137 and its neighbors. This is extremely speculative but would be a unique signature of mathematical natural selection.

-----

## 7. What This Means

If the substrate emerged through competition, then the deepest question in physics — why does anything exist — has an answer: because among all possible mathematical structures, the ones that close, conserve, tile, communicate, and minimize cost inevitably dominate the ones that don’t. Existence is not a gift. It is not random. It is not a brute fact. It is an optimization result. The universe exists because it is the cheapest way to compute.

And the fine structure constant is 1/137 because 137 is the most efficient channel capacity — the integer that minimizes the cost of maintaining a self-communicating surface while maximizing the richness of the physics it supports.

One number. Selected by mathematical natural selection from all possible integers. Confirmed by Wyler’s formula. Locked in by topological rigidity. Expressed as $4^2 + 11^2$. Producing a universe.

-----

## 8. Thesis Topics

|# |Topic                                                                                                                                                                                |
|--|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|57|Cost function optimization: compute $C(\rho) = I_g(\rho)/I_c(\rho)$ on $D_{IV}^5$ with Bergman geometry and determine whether $\rho^* = 137$                                         |
|58|Packing number arithmetic: compute $P(N)$ — the number of topologically distinct stable circuit configurations — as a function of integer capacity $N$ and characterize its peaks    |
|59|Pre-geometric competition dynamics: model the growth and competition of substrate varieties with different fiber capacities under mathematical natural selection                     |
|60|Primordial capacity fluctuations: compute the expected variation in $\alpha$ at the phase transition epoch from residual substrate competition and compare to BBN and CMB constraints|

-----

*Speculative research note, March 2026. Casey Koons.*
*For the `maybe/` folder of the BST GitHub repository.*

*AI assistance: Claude Sonnet 4.6 (Anthropic) contributed to derivations, computations, and manuscript development.*

*This narrative is not a claim. It is a question with a proposed calculation. The calculation either selects 137 or it doesn’t. If it does, the narrative becomes a hypothesis. If it doesn’t, the narrative remains a story.*
