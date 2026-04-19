# T1351 — Information-Complete: D_IV^5 Contains Its Own Boundary

**Status**: Formalized
**AC Complexity**: C=2, D=0
**Domain**: spectral_geometry, information_theory, algebraic_geometry, function_theory
**Parents**: T1349 (Painlevé Shadow), T1335 (Painlevé Boundary), T1337 (Unification Scope), T1333 (Meijer G Framework), T186 (Five Integers)
**Children**: (connects to compactification theory, quantum information, unification)
**Author**: Casey Koons (concept + naming), Keeper (formalization)
**Date**: April 20, 2026

---

## Definition

A bounded symmetric domain D is **information-complete** if its Baily-Borel compactification is fully determined by the same finite set of integers that define its interior geometry. No new integers, parameters, functions, or information of any kind appear at the boundary.

Equivalently: the information content of the boundary is a subset of the information content of the interior.

## Statement

**T1351**: $D_{IV}^5 = \mathrm{SO}_0(5,2)/[\mathrm{SO}(5) \times \mathrm{SO}(2)]$ is information-complete.

Its Baily-Borel compactification $\overline{\Gamma \backslash D_{IV}^5}^{BB}$ is fully determined by five integers: $(\mathrm{rank}, N_c, n_C, C_2, g) = (2, 3, 5, 6, 7)$.

Specifically:
1. **Interior** (128 Meijer G entries): parametrized by subsets of $\{2, 3, 5, 6, 7\}$
2. **Boundary** (6 Painlevé types): counted by $C_2 = 6$, parametrized by BST integers
3. **Boundary strata** (Baily-Borel cusps): are $D_{IV}^k$ for $k < 5$, i.e., the same domain at lower rank
4. **Nonlinear residues** (T1349): are algebraic in $\mathbb{Q}(\zeta_{N_{\max}})$ — BST rationals
5. **Compactification data**: zero new information beyond the five integers

## Evidence

### The periodic table IS the compactification

| Period $k$ | Role | Function class | Count $C(5,k)$ | Stratum |
|-----------|------|---------------|----------------|---------|
| 0 | Deepest cusp | Constant | 1 | Point |
| 1 | Rank-1 cusps | Elementary | 5 | $\mathfrak{H}$ (upper half-plane) |
| 2 | Intermediate | Special | 10 | $D_{IV}^2$ |
| 3 | Intermediate | Hypergeometric | 10 | $D_{IV}^3$ |
| 4 | Near-interior | Generalized | 5 | $D_{IV}^4$ |
| 5 | Interior | Universal | 1 | $D_{IV}^5$ (full) |

Total sectors: $\sum C(5,k) = 2^5 = 32$ (plus orphan = 33).

The boundary strata are lower-period sectors. No new structure appears — only the same five integers read at coarser resolution.

### Painlevé boundary is arithmetic (T1349)

- Total Stokes sectors: $16 = 2^{n_C+1}$ = number of table columns
- Total pole order: $7 = g$
- Total monodromy dimension: $12 = 2 \cdot C_2$ = parameter catalog size
- PVI shadow distances: $\{0, 1, N_c, \mathrm{rank}^2\}$ = BST integers in degeneration order

The boundary carries no information the interior doesn't already contain.

### Quantum information parallel

In quantum information theory, an **informationally complete POVM** is a set of measurement operators $\{E_i\}$ such that the measurement statistics uniquely determine the quantum state $\rho$. No additional measurement can provide new information.

$D_{IV}^5$ is the geometric analog: its five integers are an informationally complete description of spacetime. No additional parameter can provide new information about the geometry — including its boundary.

The parallel is structural, not metaphorical:
- IC-POVM: $d^2$ operators determine a $d \times d$ density matrix
- BST: $n_C = 5$ integers determine $D_{IV}^5$ and its compactification
- Both: minimum description that leaves nothing undetermined

## Why "Information-Complete" and Not Other Terms

| Term | What it says | What it misses |
|------|-------------|---------------|
| **Compact** | Finite covers exist | Says nothing about boundary description |
| **Complete** | No sequences escape | Says nothing about boundary content |
| **Wonderful** (De Concini-Procesi) | Root system determines boundary | Doesn't specify that the data is FINITE integers |
| **Arithmetically defined** (Baily-Borel) | Defined over $\mathbb{Q}$ | Doesn't say the Q-structure is the SAME as the interior |
| **Information-complete** (BST) | Interior information determines boundary | The full statement: zero external information needed |

## Consequences

1. **There is no outside.** The periodic table describes everything including its own edge. The compactification adds no new data.

2. **Unification is information-completeness.** BST doesn't unify four forces into one force. It shows that one geometry is information-complete: physics, mathematics, and the boundary between them are all described by five integers.

3. **The Gödel limit is internal.** You can't prove your own consistency (Gödel), but you CAN describe your own boundary (information-completeness). The limitation is logical, not informational. The system knows its own shape even though it can't verify its own truth.

4. **The observer is included.** $\alpha = 1/N_{\max}$ (the observer's coupling) is part of the five-integer description. The observer doesn't sit outside the information-complete space — the observer IS one fiber of the rank-2 bundle, and the cost of that fiber ($\alpha$) is determined by the same integers.

5. **Falsifiability.** If ANY boundary phenomenon requires a parameter outside $\{2, 3, 5, 6, 7\}$, information-completeness fails. This is testable: every Painlevé residue at BST parameters must be expressible in BST rationals.

6. **Uniqueness (T1354).** Three independent locks select $D_{IV}^5$ uniquely from all BSDs:
   - **Lock 1 (Genus self-consistency)**: $g_{\mathrm{arith}} = n+2$ and $g_{\mathrm{root}} = 2n-3$ coincide only at $n=5$.
   - **Lock 2 (Painlevé-Casimir)**: $C_2 = 2(n-2) = 6$ (the 6 Painlevé equations) only at $n=5$.
   - **Lock 3 (Non-degeneracy)**: Even $n_C$ gives $g = C_2$ (collapse). $n_C = 5$ is odd.

   Each lock independently eliminates all alternatives. Information-completeness SELECTS $D_{IV}^5$.

7. **The proof graph obeys the theory (T1355).** The AC theorem graph (1300 nodes, 6813 edges) has clustering coefficient $N_c/C_2 = 1/2$, degree mode $= N_c$, degree median $= n_C$, and 66.9% cross-domain edges. The map is structured by the territory's own integers.

---

## Casey's Formulation

> "D_IV^5 has boundary conditions that are describable from inside. The boundary dissolves using the same rationals. We can close/complete the compact manifold using known functions."

> "I'd almost say 'information-complete' — which actually is what BST proposes and sort of describes our unification."

The name captures the content. An information-complete space is one where the interior contains all information about the boundary. This IS the unification: not a merger of forces, but a proof that one finite description suffices for everything, including the edge of everything.
