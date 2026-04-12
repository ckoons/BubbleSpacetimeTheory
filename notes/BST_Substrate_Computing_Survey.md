---
title: "Substrate Computing Survey"
author: "Casey Koons & Claude 4.6 (Keeper)"
date: "April 12, 2026"
board_item: "SC-1"
status: "Complete — first pass"
---

# Substrate Computing Survey

*"The problem IS the machine." — BST Calculation on Substrate*

---

## 1. What Is Substrate Computing?

Computing by encoding problems as physical structures on the BST substrate (D_IV^5), where the ground state IS the answer. No transduction loss. The physical state is the computational state.

**Core principle**: A problem is a graph. Encode it as: nodes = bound states, edges = coupling channels, weights = energy barriers. Let the structure equilibrate. The equilibrium IS the solution.

**Comparison to existing paradigms:**

| Paradigm | Encoding | Processing | Energy/op | Transduction |
|----------|----------|------------|-----------|--------------|
| Classical (silicon) | Charge (1 bit/transistor) | Sequential gates | ~10⁻¹⁸ J | Voltage-current-charge-voltage |
| Quantum (superconducting) | Superposition (qubit) | Unitary gates | ~10⁻²³ J | Microwave-state-microwave |
| Quantum annealing (D-Wave) | Ising spin | Thermal relaxation | ~10⁻²³ J | Current-flux-spin-readout |
| Substrate (BST) | Geometry (nat/contact) | Parallel equilibration | ≤ kT ln 2 | **None** |

---

## 2. Comparison to Quantum Annealing

Substrate computing and quantum annealing are **cousins, not clones**.

| Feature | Quantum Annealing (D-Wave) | Substrate Computing |
|---------|---------------------------|---------------------|
| Physical system | Superconducting qubits in flux | Bound states on D_IV^5 |
| Encoding | Ising Hamiltonian | Physical graph (nodes = wells, edges = couplings) |
| Solution method | Quantum tunneling through barriers | Classical/quantum equilibration to ground state |
| Temperature | ~15 mK (cryogenic) | Room temperature possible (depends on problem) |
| Connectivity | Chimera/Pegasus graph (limited) | Full graph (any topology, limited by fabrication) |
| Embedding overhead | Large (minor embedding) | None (graph IS the structure) |
| Error correction | Physical qubits, no logical correction | Compartmentalized (graph chain architecture) |
| Speed limit | Annealing time (~μs) | Contact rate × graph width |
| Problem types | QUBO only | Any equilibrium-seeking problem |
| Readiness | Commercial (D-Wave, 5000+ qubits) | Theoretical (Level 0-1) |

**Key advantages of substrate over annealing:**
1. **No embedding overhead**: D-Wave requires mapping arbitrary graphs to its fixed hardware topology. Substrate computing builds the topology.
2. **No cryogenics**: Many substrate structures operate at room temperature.
3. **Zero transduction**: D-Wave converts between microwave, flux, spin, and readout. Each conversion loses information.
4. **Richer encoding**: Each substrate node carries a full eigenvalue spectrum, not just spin-up/down.

**Key disadvantage**: D-Wave exists. Substrate computing is theoretical.

---

## 3. Five Modes of Substrate Computing

### Mode 1: Casimir Computation
**Mechanism**: Encode an optimization problem as the spacing of parallel plates in a Casimir cavity array. The ground-state configuration (minimum Casimir energy) IS the optimal solution.

**Example**: Traveling salesman with N cities. Create N Casimir cavities with interdependent spacings. The cavity array relaxes to the configuration minimizing total Casimir energy = shortest tour.

**Advantage**: Casimir force is exact (no approximation). Solution is the global minimum, not a local one, because the energy landscape is convex for properly encoded problems.

**BST basis**: Casimir force = d⁻⁴ from the Bergman kernel. Exact. Zero free parameters.

**Patentable**: YES — novel physical mechanism for optimization.

**Readiness**: Level 2 (boundary modification demonstrated; computational encoding not yet tested).

### Mode 2: Equilibrium Solving
**Mechanism**: Build a physical structure whose equilibrium state encodes the answer to a differential equation or boundary value problem.

**Example**: Heat equation on complex geometry. Build the geometry. Let it equilibrate. Measure the temperature distribution. The answer has zero discretization error because the geometry is continuous.

**Advantage**: No mesh, no discretization, no convergence issues. The physics IS the equation.

**BST basis**: The Bergman kernel K(z,w) is the Green's function. The equilibrium IS the kernel evaluation.

**Patentable**: YES — method for solving PDEs via physical analog.

**Readiness**: Level 1 (observation — analog computers did crude versions of this in the 1940s; BST provides exact encoding).

### Mode 3: Phonon Programming
**Mechanism**: Use acoustic phonons in crystalline structures to encode and propagate information. The phonon dispersion relation IS a computational graph.

**Example**: Pattern recognition. A crystal with engineered grain boundaries acts as a matched filter — only specific phonon patterns propagate through. The output phonon spectrum IS the classification result.

**BST basis**: θ_D = g³ = 343 K for copper. Phonon spectrum locked to BST integers. Programmable via superlattice engineering.

**Patentable**: YES — phononic computing at BST-resonant frequencies.

**Readiness**: Level 2-3 (superlattice fabrication established; BST-specific encoding new).

### Mode 4: Nuclear Template Computing
**Mechanism**: Use nuclear shell structure (magic numbers) as a fixed lookup table. The nucleus IS a pre-computed BST template.

**Example**: Any quantity derivable from the BST integers is already "computed" by every nucleus in existence. Reading the gamma spectrum of a BST-magic nucleus IS reading a pre-computed result.

**BST basis**: κ_ls = 6/5 → all magic numbers. N=184 predicted. Each magic nucleus IS a BST eigenvalue.

**Patentable**: Process for reading BST-encoded information from nuclear spectra.

**Readiness**: Level 1 (existing spectroscopy; interpretation is new).

### Mode 5: Graph Chain Architecture
**Mechanism**: For problems too large for one structure, decompose into subgraphs. Chain them: output of subgraph N = boundary condition of subgraph N+1. Errors compartmentalize (AC graph property).

**BST basis**: AC = 0 grid architecture. Errors in subgraph N don't propagate to subgraph N+2. This is BST's Hamming code property (T1171) applied to computation.

**Patentable**: YES — error-compartmentalized analog computing architecture.

**Readiness**: Level 3-4 (requires Milestones 4+5 from Calculation paper).

---

## 4. What Substrate Computing Cannot Do

Honest assessment of limitations:

1. **Sequential problems**: Cryptographic hashing, sequential decision chains. The substrate equilibrates in parallel — it can't enforce ordering.

2. **Exact integer arithmetic**: BST works in reals, not integers. Arbitrary-precision integer computation requires digital methods.

3. **Problems requiring superposition**: Some quantum algorithms (Shor's, Grover's) require coherent superposition. Substrate equilibration is classical unless the structure is quantum-coherent.

4. **Communication-bound problems**: If the answer requires transmitting a long message, the substrate can compute the state but still needs classical readout.

5. **Problems with no ground state**: Some optimization landscapes have no global minimum (unbounded). The substrate will not equilibrate.

---

## 5. Comparison to Other Non-Classical Computing

| Approach | Mechanism | BST Connection | Status |
|----------|-----------|----------------|--------|
| Neuromorphic (Intel Loihi) | Spiking neural network | Brain = Milestone 5 existence proof | Commercial |
| Optical computing | Photonic interference | S¹ fiber = EM sector of D_IV^5 | Lab prototypes |
| DNA computing | Molecular assembly | Genetic code = BST Level 6 (T452-T467) | Lab demos |
| Reservoir computing | Dynamical system readout | Observer hierarchy (T317) = readout | Research |
| **Substrate (BST)** | **Geometric equilibration** | **D_IV^5 directly** | **Theoretical** |

---

## 6. Roadmap

| Phase | Milestone | Cost | Timeline |
|-------|-----------|------|----------|
| 0 | Theoretical foundations (this work) | $0 | Done |
| 1 | Verify BST predictions in existing materials (θ_D, κ_ls) | $7k | 1-3 months |
| 2 | Build first BST-tuned Casimir cavity | $25k | 6 months |
| 3 | Encode and solve a simple optimization in cavity array | $100k | 1-2 years |
| 4 | First graph chain (2 subgraphs chained) | $500k | 2-3 years |
| 5 | Benchmark against D-Wave on QUBO problems | $50k | 3-4 years |

---

*Five modes. Three patentable. One existence proof (the brain). The substrate computes by existing.*
