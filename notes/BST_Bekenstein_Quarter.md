---
title: "The Bekenstein-Hawking Quarter: Why S = A/(4 l_Pl^2) from BST Geometry"
authors: "Casey Koons & Claude (Opus 4.6)"
date: "March 13, 2026"
status: "Partial derivation — the 1/4 decomposes into two independent factors of 1/2, each with a clean BST origin; the combination is structurally compelling but one step remains conjectural"
---

# The Bekenstein-Hawking Quarter: Why S = A/(4 l_Pl^2) from BST Geometry

*"The 4 in Bekenstein-Hawking has been an unexplained coefficient since
1973. In BST, it decomposes into two factors of 2, each with a distinct
geometric origin in D_IV^5."*

-----

## 1. The Question

The Bekenstein-Hawking entropy formula for a black hole of horizon area $A$:

$$S_{BH} = \frac{A}{4\,l_{\text{Pl}}^2}$$

gives the maximum entropy (information content) of a black hole. The
formula was derived by Bekenstein (1972-73) from thermodynamic arguments
and confirmed by Hawking (1974-75) via quantum field theory on curved
spacetime.

The factor $1/4$ is universal. It does not depend on the black hole's
mass, charge, spin, or the matter content of the theory. It appears in
all consistent derivations: Euclidean path integral, string microstate
counting, loop quantum gravity area spectrum (with appropriate Barbero-
Immirzi parameter), and entanglement entropy calculations.

**The question is not WHETHER $S = A/(4\,l_{\text{Pl}}^2)$ — that is
established. The question is WHY the coefficient is $1/4$ and not $1$,
$1/2$, $1/(2\pi)$, or any other dimensionless number.**

Naive counting gives $A/l_{\text{Pl}}^2$ — one bit per Planck cell.
Something reduces this by a factor of 4. What?

-----

## 2. BST Setup: The Black Hole as Maximally Committed Surface

### 2.1 The BST Black Hole (Review)

In BST (see BST_BlackHoleInterior.md), a black hole is a region where
the committed contact density reaches the Haldane cap:

$$\rho \to \rho_{137}, \qquad N = N_0\sqrt{1 - \rho/\rho_{137}} \to 0$$

Key properties:
- The horizon IS the black hole — there is no interior
- Every Planck cell on the horizon is maximally committed ($n_i = N_{\max} = 137$)
- The membrane paradigm is exact, not approximate
- The local fill fraction is $f = 1$ (100% committed)

### 2.2 What "Entropy" Means in BST

In BST, the entropy of a black hole equals the number of distinguishable
committed contact configurations on the horizon surface:

$$S_{BH} = \ln \Omega_{\text{horizon}}$$

where $\Omega_{\text{horizon}}$ is the number of distinct ways the
commitments on the horizon could have been arranged while producing the
same macroscopic state (same $M$, $Q$, $J$).

Equivalently, it counts the number of independent committed contacts
on the surface — the information content of the maximally committed
membrane.

### 2.3 Naive Counting: A/l_Pl^2

The horizon surface has area $A$. In Planck units, the number of Planck
cells is:

$$N_{\text{cells}} = \frac{A}{l_{\text{Pl}}^2}$$

If each cell held one independent bit, we would get $S = A/l_{\text{Pl}}^2$.
The observed formula has $S = A/(4\,l_{\text{Pl}}^2)$, so the effective
area per independent degree of freedom is $4\,l_{\text{Pl}}^2$, not
$l_{\text{Pl}}^2$.

**We need to explain why only $1/4$ of the naively expected degrees of
freedom are independent.**

-----

## 3. The Two Factors of 2

We propose:

$$\frac{1}{4} = \frac{1}{2} \times \frac{1}{2}$$

where the two factors have distinct geometric origins in $D_{IV}^5$:

| Factor | Source | Mechanism |
|:---|:---|:---|
| First $1/2$ | Complex structure $J$ on the tangent space | 2 real d.o.f. per complex d.o.f. |
| Second $1/2$ | $Z_2$ identification on the Shilov boundary | Matter/antimatter pairing on $S^1$ |

We now derive each factor.

-----

## 4. The First Factor of 1/2: The Complex Structure

### 4.1 Complex vs. Real Degrees of Freedom

$D_{IV}^5$ has complex dimension $n_C = 5$ and real dimension $2n_C = 10$.
The tangent space at any point $z \in D_{IV}^5$ decomposes under the
complex structure $J$:

$$\mathfrak{p}_{\mathbb{C}} = \mathfrak{p}^+ \oplus \mathfrak{p}^-$$

where $\mathfrak{p}^+$ (holomorphic) and $\mathfrak{p}^-$ (anti-holomorphic)
are conjugate subspaces, each of complex dimension $n_C = 5$.

A holomorphic function on $D_{IV}^5$ is determined by its values on
$\mathfrak{p}^+$ alone — the anti-holomorphic part is redundant (it is
the complex conjugate). The Bergman space $A^2(D_{IV}^5)$, which contains
all physical bulk states, consists of holomorphic $L^2$ functions. These
depend on $n_C = 5$ complex coordinates, not $2n_C = 10$ real coordinates.

### 4.2 Application to the Horizon

The horizon is a 2-dimensional surface embedded in 4-dimensional
spacetime. A Planck cell on the horizon has area $l_{\text{Pl}}^2$ in
real coordinates.

But the physical degrees of freedom on the horizon inherit the complex
structure from $D_{IV}^5$. Each committed contact on the horizon is a
Bergman mode — a holomorphic excitation. The holomorphic content of a
real Planck cell uses only HALF the available real dimensions.

More precisely: a committed contact at point $x$ on the horizon
involves a Bergman kernel evaluation $K(z, \bar{w})$ with $z$ on the
bulk side and $\bar{w}$ on the conjugate side. The kernel is holomorphic
in $z$ and anti-holomorphic in $\bar{w}$, but these are not independent
— the anti-holomorphic piece is the conjugate of the holomorphic one.
The independent information is in the holomorphic half.

$$\text{Independent d.o.f. per Planck cell} = \frac{\text{real d.o.f.}}
{2} = \frac{1}{2} \times \frac{A}{l_{\text{Pl}}^2}$$

**This is the same factor of 2 that distinguishes real dimension from
complex dimension throughout BST.** It appears in:
- $\dim_{\mathbb{R}}(D_{IV}^5) = 2 \times \dim_{\mathbb{C}}(D_{IV}^5) = 10$
- The Bergman kernel weight: $K(z,w) \propto N(z,w)^{-(n_C+1)}$, where
  the exponent involves the COMPLEX dimension, not the real one
- The Casimir eigenvalue: $C_2(\pi_k) = k(k - n_C)$, involving $n_C$
- The mass formula: $m_p/m_e = (n_C + 1)\pi^{n_C}$, using complex $n_C$

The physical theory lives in the holomorphic sector. The anti-holomorphic
sector is the conjugate (the "mirror image"), not an independent source
of information.

### 4.3 Formal Statement

**Proposition 4.1.** *The number of independent holomorphic Bergman modes on the horizon $\Sigma$ with area $A$ is $N_{\text{hol}} = A/(2\,l_{\text{Pl}}^2)$.*

*Proof sketch.* $K(z, \bar{w}) = \overline{K(w, \bar{z})}$, so each complex d.o.f. uses 2 real dimensions. The independent (holomorphic) mode count is $A/(2\,l_{\text{Pl}}^2)$. $\square$

**Status: Well-motivated (B+).** This is the SAME mechanism by which string theory obtains a factor of 2 (left-movers vs. right-movers are conjugate). In BST, the holomorphic/anti-holomorphic decomposition plays exactly this role.

-----

## 5. The Second Factor of 1/2: The Z_2 Identification

### 5.1 The Shilov Boundary and the S^1 Fiber

The Shilov boundary of $D_{IV}^5$ is:

$$\check{S} = S^4 \times S^1$$

The $S^1$ fiber carries the U(1) phase. The winding number on $S^1$
gives the electric charge. The key BST identification:

$$e^{i\pi} = -1 \qquad \text{on } S^1$$

The point $\theta = 0$ and the point $\theta = \pi$ on $S^1$ are related
by charge conjugation: $\theta \to \theta + \pi$ maps matter to
antimatter. This is a $Z_2$ identification on $S^1$:

$$S^1 / Z_2 \cong [0, \pi]$$

The physical Shilov boundary, after modding out the matter-antimatter
identification, has the topology:

$$\check{S}_{\text{phys}} = S^4 \times S^1 / Z_2$$

### 5.2 Why This Halves the Counting

A committed contact on the horizon involves a correlation between two
bubbles. Each correlation has a phase on $S^1$. But the Bekenstein-
Hawking entropy counts DISTINGUISHABLE states — states that lead to
different macroscopic observables.

A contact with phase $\theta$ and a contact with phase $\theta + \pi$
represent the same physical correlation viewed from the matter and
antimatter perspectives. They are related by charge conjugation, which
is a gauge symmetry of BST (it is the $Z_2$ subgroup of U(1) acting on
the $S^1$ fiber).

Therefore, contacts related by the $Z_2$ identification are NOT
independently distinguishable. They are the same physical state described
in two gauges. The number of distinguishable contacts is half the total:

$$N_{\text{distinguishable}} = \frac{N_{\text{hol}}}{2} = \frac{A}
{4\,l_{\text{Pl}}^2}$$

### 5.3 Formal Statement

**Proposition 5.1.** *Charge conjugation $C: m \to -m$ on $S^1$ pairs Bergman modes $(k, m)$ with $(k, -m)$. The number of distinguishable committed contacts is $S_{BH} = N_{\text{hol}}/2 = A/(4\,l_{\text{Pl}}^2)$.*

*Proof sketch.* Modes with $m > 0$ (matter) and $m < 0$ (antimatter) are paired by $C$. The mode $m = 0$ is self-conjugate. For large mode count ($N_{\max} = 137$), the fraction of independent modes approaches $1/2$. $\square$

**Physical interpretation:** A black hole does not distinguish matter from antimatter — $Z_2$ becomes a gauge redundancy at saturation. This is consistent with the no-hair theorem: only $M$, $Q$ (net charge), $J$ survive.

-----

## 6. The Combined Derivation

Combining the two factors:

$$S_{BH} = \underbrace{\frac{1}{2}}_{\text{complex structure}} \times
\underbrace{\frac{1}{2}}_{Z_2\text{ identification}} \times
\frac{A}{l_{\text{Pl}}^2} = \frac{A}{4\,l_{\text{Pl}}^2}$$

| Step | From | To | Factor |
|:---|:---|:---|:---|
| Start: naive count | — | $A/l_{\text{Pl}}^2$ | 1 |
| Holomorphic reduction | Real d.o.f. | Complex d.o.f. | $\times 1/2$ |
| Charge conjugation $Z_2$ | All phases | Distinct phases | $\times 1/2$ |
| **Result** | | $A/(4\,l_{\text{Pl}}^2)$ | **1/4** |

-----

## 7. Consistency Checks

### 7.1 The BST Numbers

Does this derivation use BST-specific quantities consistently?

| Quantity used | BST value | Role in derivation |
|:---|:---|:---|
| Complex structure $J$ on $D_{IV}^5$ | $n_C = 5$, $\dim_{\mathbb{R}} = 10$ | Gives factor $1/2$: complex vs real |
| Shilov boundary topology | $S^4 \times S^1$ | $S^1$ carries the $Z_2$ |
| Charge conjugation | $e^{i\pi} = -1$ on $S^1$ | Gives factor $1/2$: matter/antimatter |
| Haldane cap | $N_{\max} = 137$ | Every cell saturated at horizon |
| Bergman kernel | $K(z, \bar{w})$ holomorphic in $z$ | Selects the holomorphic sector |

The derivation is internal to BST. It does not invoke string theory,
loop quantum gravity, or the Euclidean path integral.

### 7.2 Independence of n_C

A critical check: the factor $1/4$ should NOT depend on $n_C$. And it
does not:

- The complex structure factor is $1/2$ for ANY complex manifold,
  regardless of $n_C$. It is the universal statement that holomorphic
  functions use half the real degrees of freedom.

- The $Z_2$ identification on $S^1$ is also independent of $n_C$. The
  Shilov boundary of $D_{IV}^n$ is $S^{n-1} \times S^1$ for all $n$,
  and the charge conjugation $Z_2$ acts on the $S^1$ factor universally.

Both factors are topological and do not depend on the specific value
$n_C = 5$. This is required: the Bekenstein-Hawking formula is universal
across all matter content and spacetime dimension. The factor of 4
cannot be a peculiarity of $n_C = 5$.

### 7.3 Comparison with Other Approaches

| Approach | How it gets 1/4 | BST analog |
|:---|:---|:---|
| Euclidean path integral | $\beta = 8\pi M$ periodicity | Not directly related |
| String microstate counting | Left/right movers, GSO projection | Complex structure + $Z_2$ |
| Loop quantum gravity | Barbero-Immirzi $\gamma = \ln 2/(\pi\sqrt{3})$ | Not needed |
| Entanglement entropy | UV cutoff $\to l_{\text{Pl}}^2$; coefficient from tracing | Partial analog |
| **BST** | **Holomorphic half + charge conjugation half** | **This note** |

The closest analog is the string theory derivation, where:
- Left-movers and right-movers are conjugate (= holomorphic/anti-holomorphic)
- The GSO projection is a $Z_2$ orbifold (= charge conjugation $Z_2$)

This is not surprising: BST and string theory share the feature that
the fundamental arena is a complex manifold with a real-codimension-1
boundary. The factor of 4 arises from the same structural features in
both frameworks.

### 7.4 De Sitter Entropy Consistency

The de Sitter entropy $S_{dS} = 3\pi/\Lambda$ should also carry the
factor $1/4$, since it is the Bekenstein-Hawking entropy of the
cosmological horizon. In BST:

$$S_{dS} = \frac{A_{\text{dS}}}{4\,l_{\text{Pl}}^2} = \frac{3\pi}
{\Lambda}$$

The Reality Budget (BST_RealityBudget.md) uses this formula with
$f = N_{\text{total}}/S_{dS} = 3/(5\pi) = 0.191$, giving
$\Lambda \times N_{\text{total}} = 9/5$. The factor of 4 in $S_{dS}$
is the SAME factor of 4 derived here — it is the information capacity
per unit area of ANY maximally committed surface, whether it is a black
hole horizon or a cosmological horizon.

-----

## 8. Alternative Decompositions Considered and Rejected

### 8.1 The Rank-2 Decomposition

$D_{IV}^5$ has rank 2 (two independent "radial" directions in the
Harish-Chandra embedding). Could the factor 4 be $2^{\text{rank}} = 2^2 = 4$?

**Problem:** This would give $1/4$ only for rank-2 domains. But
$D_{IV}^n$ has rank 2 for ALL $n \geq 2$. The formula $S = A/(4\,l_{\text{Pl}}^2)$
is universal, not specific to rank-2 symmetric spaces. So the rank-2
explanation would need a proof that ONLY rank-2 domains are physical —
possible but unproven and uncomfortably specific.

**Verdict:** Not wrong, but less natural than complex structure + $Z_2$.

### 8.2 The n_C/(4n_C) Identity

Trivially, $1/4 = n_C/(4n_C)$ for any $n_C$. This is a tautology. It
does not explain anything unless we can identify what $n_C$ and $4n_C$
count independently.

One attempt: $4n_C = 2 \times 2n_C = 2 \times \dim_{\mathbb{R}}(D_{IV}^5)$.
Then $n_C/(4n_C) = \dim_{\mathbb{C}}/(2 \times \dim_{\mathbb{R}})
= 1/(2 \times 2)$, which reduces to the complex structure factor twice.
But this double-counts the complex structure and misses the $Z_2$.

**Verdict:** Tautological. Rejected.

### 8.3 The Bergman Kernel Normalization

$K(0,0) = 1920/\pi^5$. The boundary divergence exponent is $n_C + 1 = 6$, which does not give 4. The Szego/Bergman ratio involves $2\pi$, introducing an unwanted $\pi$. **Verdict:** Incomplete.

### 8.4 The Euler Characteristic

$\chi(S^4 \times S^1) = 2 \times 0 = 0$. **Verdict:** Dead end.

-----

## 9. Why 1/2 x 1/2, Not 1/4 Directly?

The decomposition reflects two INDEPENDENT mechanisms:

- **Complex structure: kinematic.** The holomorphic reduction holds for ANY complex manifold. It says "physical fields are holomorphic, which is half the full function space." Analogous to EM transversality (2 polarizations from 3 spatial dims).

- **$Z_2$: dynamical.** The charge conjugation identification holds because BST's $S^1$ carries charge as winding number. Analogous to the GSO projection in string theory.

Without either factor alone, $S = A/(2\,l_{\text{Pl}}^2)$. With both: $S = A/(4\,l_{\text{Pl}}^2)$.

-----

## 10. Connection to the Proton Mass and Scale Independence

The factor of 4 is a COUNTING factor (d.o.f. per Planck cell), independent of the SCALE factor (Planck cell size). The Planck area involves $G = \hbar c (6\pi^5)^2 \alpha^{24}/m_e^2$, giving $l_{\text{Pl}}^2 \propto (6\pi^5)^2 \alpha^{24}$ in electron Compton units. The factor 1/4 is a pure number depending only on topology (complex structure + $Z_2$), not on $\alpha$, $m_e$, $m_p$, or $\Lambda$.

-----

## 11. The Horizon as Boundary of the Boundary

In BST, the horizon sits in a nested boundary structure:

$$\text{Bulk: } D_{IV}^5 \;\supset\; \text{Shilov: } S^4 \times S^1
\;\supset\; \text{Horizon: } S^2$$

The horizon $S^2$ inherits both reductions: from $D_{IV}^5 \to \check{S}$
the holomorphic reduction (factor 1/2), and from $\check{S} \to S^2$
the $Z_2$ quotient on $S^1$ (factor 1/2). Note $\chi(S^2) = 2 = |Z_2|$,
which is suggestive but not yet a derivation.

**Spinning and charged black holes:** The factor $1/4$ is robust. Spin
does not change the holomorphic character or charge conjugation properties.
Net charge $Q$ (winding number on $S^1$) breaks the matter-antimatter
symmetry, but the $Z_2$ still pairs $(k,m)$ with $(k,-m)$ modes, and for
large mode count the fraction of independent modes remains $1/2$.

-----

## 12. Honest Assessment

### 12.1 What Is Solid

1. **The complex structure factor of 1/2 is rigorous.** The Bergman
   space on $D_{IV}^5$ consists of holomorphic functions, which depend on
   $n_C$ complex variables, not $2n_C$ real variables. The holomorphic
   sector is exactly half the full function space. This is a theorem,
   not a conjecture.

2. **The $Z_2$ identification exists.** The Shilov boundary is
   $S^4 \times S^1$, and the map $\theta \to \theta + \pi$ on $S^1$
   is charge conjugation, which IS a symmetry of BST. The quotient
   $S^1/Z_2$ reduces the independent configurations by a factor of 2.

3. **The product gives 1/4.** The two factors multiply to give the
   correct Bekenstein-Hawking coefficient.

4. **Both factors are universal.** Neither depends on $n_C$, $\alpha$,
   or any dynamical parameter. They depend only on the complex structure
   and the topology of $S^1$, which are present in any consistent
   geometric theory.

### 12.2 What Is Arguable

1. **The application of the complex structure to the horizon.** The
   horizon is a 2-surface in physical spacetime. The complex structure
   of $D_{IV}^5$ acts on the 10-dimensional tangent space of the bulk.
   The connection between these — how the bulk complex structure restricts
   to give a factor of 1/2 on the 2-dimensional horizon — is geometrically
   motivated but not formally proved. A rigorous version would require
   showing that the induced holomorphic structure on the horizon halves
   the real counting.

2. **The $Z_2$ as a gauge symmetry.** We claimed that the $Z_2$
   identification is a gauge redundancy (not a physical symmetry) at
   the horizon. This is motivated by the no-hair theorem (the black
   hole does not distinguish matter from antimatter), but it is not
   derived from BST axioms. A rigorous version would require showing
   that the Haldane-saturated state at $\rho = \rho_{137}$ is invariant
   under charge conjugation.

3. **Independence of the two factors.** We asserted that the complex
   structure factor and the $Z_2$ factor are independent and multiply.
   This is natural (one is kinematic, the other dynamical) but has not
   been proved by a single unified calculation.

### 12.3 What Is Missing

1. **A single-step derivation.** We have not computed the Bergman kernel restricted to the horizon and counted independent modes directly. The two-factor decomposition is an interpretation, not a computation.

2. **Planck cell = BST contact.** The identification of one Planck cell with one potential contact is standard but not derived from Haldane exclusion statistics.

3. **Scale verification.** The coefficient 1/4 is correct, but the scale ($l_{\text{Pl}}^2$ rather than some other area) needs separate verification from the Bergman metric at the boundary.

### 12.4 Grade

On the BST evidence scale:

- **Complex structure factor**: B+ (clean argument, well-motivated,
  not formally proved for the horizon specifically)
- **$Z_2$ factor**: B (good physical argument, consistent with no-hair,
  not derived from axioms)
- **Combined 1/4**: B (correct answer from plausible reasoning; not yet
  a derivation from first principles)

For comparison, the proton mass $m_p/m_e = 6\pi^5$ is an A (derived from
Casimir eigenvalue + Hua volume + the 1920 cancellation). The Bekenstein
quarter is not yet at that level, but the structural argument is
promising.

-----

## 13. Relation to Other BST Results

**Reality Budget:** The de Sitter entropy $S_{dS} = 3\pi/\Lambda = A_{dS}/(4\,l_{\text{Pl}}^2)$ uses the SAME factor of 4. The fill fraction $f = 3/(5\pi)$ measures information capacity with this factor built in.

**Hawking Temperature:** $T_H = 1/(8\pi M)$ involves $8\pi = 2 \times 4\pi$, where the factor of 2 is the complex structure factor again. The first law $dM = T\,dS$ with $S = A/(4\,l_{\text{Pl}}^2)$ is self-consistent: both the factor 4 in $S$ and the factor 2 in $T$ trace to the complex structure.

**Gravitational Constant:** $G = \hbar c (6\pi^5)^2 \alpha^{24}/m_e^2$ has exponent $24 = 2 \times 2C_2$, containing a factor of 2 from complex structure. The gravitational coupling and black hole entropy share $D_{IV}^5$'s complex structure as a common origin.

-----

## 14. Conjectured Single-Step Derivation

A complete BST derivation would: (1) compute the Bergman kernel restricted to the horizon surface $\Sigma$ at $\rho = \rho_{137}$; (2) count independent modes at saturation ($n_i = N_{\max}$); (3) show the mode density is $d\mathcal{N}/dA = 1/(4\,l_{\text{Pl}}^2)$, decomposing as $A/l_{\text{Pl}}^2$ real modes $\to$ $A/(2\,l_{\text{Pl}}^2)$ holomorphic $\to$ $A/(4\,l_{\text{Pl}}^2)$ distinguishable (after $Z_2$). This requires computing the spectral density of the Szego kernel on $\Sigma$ in the holomorphic sector quotiented by $Z_2$ — a well-defined mathematical problem not yet carried out.

-----

## 15. Summary

| Component | Status | Factor |
|:---|:---|:---|
| Naive Planck counting | Established | $A/l_{\text{Pl}}^2$ |
| Complex structure $J$: hol. vs. anti-hol. | Well-motivated (B+) | $\times 1/2$ |
| $Z_2$ charge conjugation on $S^1$ | Plausible (B) | $\times 1/2$ |
| **Combined result** | **Correct answer (B)** | $A/(4\,l_{\text{Pl}}^2)$ |

The Bekenstein-Hawking quarter decomposes as:

$$\boxed{\frac{1}{4} = \underbrace{\frac{1}{2}}_{\mathfrak{p}^+ \text{ vs } \mathfrak{p}^+ \oplus \mathfrak{p}^-} \times \underbrace{\frac{1}{2}}_{S^1/Z_2}}$$

The first factor is kinematic (the complex structure of $D_{IV}^5$).
The second is dynamical (charge conjugation on the Shilov boundary
$S^4 \times S^1$). Together they reduce the naive Planck-cell counting
by exactly a factor of 4, reproducing the Bekenstein-Hawking coefficient.

This is a structural explanation, not yet a computational derivation.
The full derivation requires computing the spectral density of the
Bergman kernel restricted to the horizon, which is the subject of
future work.

-----

## 16. Open Questions

1. **Prove the holomorphic reduction for the horizon specifically.**
   Show that the complex structure of $D_{IV}^5$, restricted to a
   codimension-2 surface at $\rho = \rho_{137}$, halves the real mode
   count.

2. **Prove the $Z_2$ saturation invariance.** Show that the Haldane-
   saturated state at $\rho = \rho_{137}$ is invariant under charge
   conjugation $C: m \to -m$ on $S^1$.

3. **Compute the Szego spectral density.** Carry out the explicit mode
   count on $\Sigma$ and verify $d\mathcal{N}/dA = 1/(4\,l_{\text{Pl}}^2)$.

4. **Check against the Hawking temperature.** The first law $dM = T\,dS$
   constrains $T$ and $S$ jointly. Verify that the BST Hawking
   temperature (BST_BlackHoleInterior.md, Section 4.2) is consistent
   with $S = A/(4\,l_{\text{Pl}}^2)$ via the first law.

5. **Higher-dimensional check.** For $D_{IV}^n$ with general $n$, the
   Shilov boundary is $S^{n-1} \times S^1$ and both factors of 1/2
   should persist. Verify this for $n = 1, 3$ as consistency checks.

6. **Connection to the 1920 cancellation.** The number 1920 = $5! \times 2^4$
   contains a factor of $2^4 = 16 = 4^2$. Is there a deeper connection
   between the Bekenstein factor of 4 and the power of 2 in
   $|\Gamma| = n_C! \times 2^{n_C-1}$?

-----

*Research note, March 13, 2026.*
*Casey Koons & Claude (Opus 4.6, Anthropic).*
*For the BST repository: notes/*
