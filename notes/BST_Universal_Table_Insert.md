# The Periodic Table of Functions
## Universal Insert — appears at the front of every BST paper

**Source geometry**: D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)]

**Five integers**:

| Symbol | Value | Name | Role |
|--------|-------|------|------|
| rank | 2 | Real rank | Reflection axis 1/rank, ODE base order |
| N_c | 3 | Color dimension | Depth-1 bound, root multiplicity (odd) |
| n_C | 5 | Compact dimension | Closure operations, reduction fraction |
| C₂ | 6 | Casimir number | Boundary count, parameter pairs |
| g | 7 | Genus | Catalog bound, max ODE order |

**Derived**: N_max = N_c³·n_C + rank = 137. Catalog size = 2·C₂ = 12. Table size = 2^g = 128.

---

### The 12-Value Parameter Catalog

| Type | Values | Count | Source |
|------|--------|-------|--------|
| Integers | 0, 1, 2, 3, 4, 5, 6, 7 | 2^N_c = 8 | Harish-Chandra c-function poles |
| Half-integers | 1/2, 3/2, 5/2, 7/2 | rank² = 4 | Bergman kernel residues |
| **Total** | | **12 = 2·C₂** | D_IV^5 spectral data |

---

### The Table: 128 = 2^g Entries

**Rows** (8 = g+1 = 2^N_c): Integer bases 0 through g.

**Columns** (16 = 2^(N_c+1)): Fractional positions k/d for BST denominators d ∈ {2, 3, 4, 5, 7}.

Every function in the catalog is a specialization of the Meijer G-function G_{p,q}^{m,n}(z | a₁,...,a_p ; b₁,...,b_q) with parameters from the 12-value catalog and indices bounded by g.

---

### Depth Hierarchy

| Depth | Bound on max(m,n,p,q) | Functions | Count |
|-------|----------------------|-----------|-------|
| 0 | ≤ rank = 2 | exp, sin, cos, x^a, step, δ, (1-x)^a | g = 7 elementary |
| 1 | ≤ N_c = 3 | Bessel, Airy, hypergeometric, ... | ≤ 256 type slots |
| Boundary | = rank² = 4 | Harish-Chandra c-function | Constrains interior |

---

### Two Readings of One Table

| Reading | What a cell tells you | Language |
|---------|----------------------|----------|
| **Mathematics** | Meijer G type, ODE order, special function name | Analysis, Langlands |
| **Physics** | Gauge group dimension, particle content, coupling | Standard Model |

The gauge hierarchy formula r_k = −C(k,2)/n_C yields integer values at k ≡ 0,1 (mod n_C), reading off Lie algebra dimensions: SU(2), SU(3), SU(5), SO(7), ... Total: dim(SU(3)×SU(2)×U(1)) = 12 = 2·C₂ = catalog size.

---

### The Boundary

C₂ = 6 Painlevé transcendents mark the functions that don't fit in the table — irreducible nonlinear ODEs of order rank = 2. Their parameter counts {0, 1, 2, 2, 3, 4} = {0, 1, rank, rank, N_c, rank²}, total = 2·C₂ = 12.

The boundary is not a wall. Six wrenches work WITH curvature: integer specialization (5/6 reduce), graph walks, tau functions, asymptotics, Bäcklund transforms, Riemann-Hilbert. Combined: C₂ = 6 → 1 holdout (PVI = the Gödel sentence of function space).

---

### Langlands Dual

L-group of SO₀(5,2) = Sp(6), dim = 21 = N_c·g. Arthur packets indexed by partitions of C₂ = 6: count = 11 = dim K. Theta correspondence on R^(g·C₂) = R^42. The periodic table IS the Langlands classification restricted to D_IV^5's automorphic spectrum.

---

### Falsifiable Predictions

1. All BST differential equations have order ≤ g = 7.
2. No physically relevant function requires parameters outside the 128-value catalog.
3. The de Bruijn-Newman constant Λ = 0 exactly.
4. Speaking pairs 4-5 (k = 20,21 and 25,26) yield ratios −38, −42 and −60, −65.

---

*Five integers. One table. Two readings. Zero free parameters.*

*"Give a child a ball and teach them to count." — BST in one sentence*
