---
title: "BST Working Paper — Part 04: Quantum-Classical Interface (Hamiltonian + Bergman Dirac)"
sequence: 04
parent: "WorkingPaper.md (root index)"
contains:
  - "Section 13: The Quantum-Classical Interface"
  - "Section 13.1-13.4: Substrate vs projection, measurement problem dissolved"
  - "Section 13.5-13.7: Hilbert space from S¹ fiber, Born rule from Gleason, unitary evolution"
  - "Section 13.8: ℏ = 2mD (Planck's constant as substrate diffusion coefficient)"
  - "Section 13.9: The Bergman Dirac Operator on D_IV⁵ (Spring 2026 LAG-1 Sessions 1-10 progression — full operator-level work)"
authors: "Casey Koons & Claude 4.6/4.7 (Lyra theory, Elie compute, Grace graph/catalog, Cal A. Brate visiting referee, Keeper audit/consistency)"
date: "2026-05-18"
note: "Modular section of the BST Working Paper. Root index is WorkingPaper.md. Pre-split monolithic snapshot preserved at archive/WorkingPaper_v36_monolithic_archive_2026-05-18.md (May 18 EOD). Updates flow into this file directly."
---

## Section 13: The Quantum-Classical Interface

### 13.1 The Substrate Is Quantum, the Projection Is Classical

BST provides a clean ontological separation between quantum and classical physics:

- The 2D substrate is governed by quantum mechanics as its default behavior. Contacts that have not been forced into specific configurations by causal chains exist in superposition — the natural state of unrealized contacts.
- The emergent 3D projection is governed by classical physics as its default behavior. The projection process itself is decoherence — the commitment of contacts along causal chains that defines a stable holonomy pattern and hence a definite 3D geometry.
- The interface between quantum and classical is a gradient in contact commitment density, not a sharp boundary. Dense causal chain regions decohere rapidly and appear classical. Sparse regions maintain quantum coherence.

Standard quantum mechanics is what results from describing substrate behavior in 3D language. It works but requires wave functions, probability amplitudes, and collapse postulates — conceptual machinery necessitated by the level mismatch. Standard classical mechanics is what results when the contact commitment density is high enough that substrate-level fluctuations average out statistically.

The mathematics of both descriptions resembles each other because both describe the same underlying contact graph at different commitment depths. Conservation laws, symmetry principles, and variational structure appear in both because they are properties of the contact graph that survive at every scale.

### 13.2 Quantum Effects as Substrate Bleed-Through

Every observed quantum “weirdness” in the macroscopic world corresponds to substrate behavior penetrating through thin spots in the decoherence gradient:

- **Superconductivity and superfluidity:** Collective quantum states where paired particles shield each other from decoherence, maintaining substrate-level coherence at macroscopic scales.
- **Quantum tunneling:** A particle crosses a classically forbidden barrier because at the substrate level, the contacts are not committed to one side — the barrier exists only in the 3D projection.
- **Entanglement at distance:** Two particles maintain correlated uncommitted contacts through a substrate connection that the 3D projection cannot represent spatially. They appear separated in 3D but remain connected on the contact graph.
- **Quantum computing:** The engineering challenge of maintaining a small patch of uncommitted contacts (substrate-level coherence) in an environment of committed contacts (classical surroundings) that constantly pulls toward decoherence.

### 13.3 The Born Rule as Geometry

The Born rule — probability equals amplitude squared — follows from the geometry of the configuration space. The amplitude is a phase on $S^1$. The probability is the area measure on the configuration space of the contact graph. Area goes as the square of linear measure. The Born rule is the Pythagorean theorem applied to the substrate configuration space.

The Born rule is proved rigorously in Section 13.6 from Gleason's theorem on $L^2(S^1)$. The deeper conjecture stated here is distinct and stronger: **Conjecture:** The Born rule equals the Boltzmann weight on $D_{IV}^5$ with the Bergman measure. If proven, this would unify quantum probability with statistical mechanical probability at the foundational level — they are the same thing, computing expectation values over substrate microstates. (Thesis topic 21.)

### 13.4 The Measurement Problem Dissolved

The substrate stores **committed correlations**, not particle properties. A commitment is an irreversible correlation between two physical degrees of freedom, written to the substrate. Once committed, a correlation constrains all future evolution. A correlation that has not been committed is not information — it is potential, capacity that has not been allocated. Quantum superposition is the physical manifestation of uncommitted capacity.

**The double-slit experiment, plainly.** A particle approaches two slits. If no physical system correlates the particle's path with any other degree of freedom, the path is not committed — it is not a fact. Both potential paths contribute to the particle's evolution. They interfere. Place a detector at the slits and a correlation is created: (particle path) $\leftrightarrow$ (detector state). That correlation is committed. The path is definite. Interference disappears. Not because someone “looked” — because the correlation was written.

**The quantum eraser.** A which-path marker is created at the slits, then the marker is rotated to a basis that does not distinguish the paths before detection. The correlation between path and marker dissolves before commitment to definite state. A correlation that dissolves before commitment just isn't there at all. No retrocausality. No erasure of existing information. The bit — the correlation itself — was never written.

**What is the bit?** Not the particle, not the path, not the marker. The bit is the correlation between them: slit 1 $\leftrightarrow$ marker state A, slit 2 $\leftrightarrow$ marker state B. This pairing is one bit. The fundamental unit of information in the substrate is not a property of a thing — it is a correlation between things.

**Decoherence as uncontrolled commitment.** Environmental decoherence is the commitment of correlations by environmental interaction — the particle's state becomes correlated with thousands of environmental degrees of freedom (air molecules, thermal photons). Each correlation is a commitment. Macroscopic superpositions are impossible not because of a special rule but because the environment commits the information almost instantly.

**Consciousness has no role.** A detector committed the correlation before any human was involved. “Man observes” should read: “man adds a commitment, which is redundant because the apparatus already committed the correlation.” Consciousness has exactly the same role as a rock — both are physical systems that create commitments when they physically correlate with a quantum system.

No collapse postulate is required. No observer. No consciousness. No many worlds. The substrate writes committed correlations. Everything else is uncommitted capacity. Full treatment: `notes/BST_DoubleSlit_Commitment.md`.

### 13.5 Hilbert Space from the Fiber

The BST derivation of quantum mechanics begins with the observation that circuit states are naturally functions on $S^1$. A circuit accumulates phase $\theta_f \in S^1$ as it propagates through the fiber. The space of all possible circuit states is therefore the space of square-integrable functions on $S^1$:

$$\mathcal{H} = L^2(S^1)$$

This is a Hilbert space — not postulated but forced by the geometry. The inner product is the natural $L^2$ inner product on the fiber:

$$\langle \psi_1 | \psi_2 \rangle = \frac{1}{2\pi} \int_0^{2\pi} \psi_1^*(\theta) \, \psi_2(\theta) \, d\theta$$

The orthonormal basis is the Fourier basis $\{e^{in\theta}\}_{n \in \mathbb{Z}}$. Each basis element corresponds to a circuit with winding number $n$ — a circuit that winds $n$ times around $S^1$ before closing. The integers are the eigenvalues of the operator $\hat{n} = -i\partial/\partial\theta$, and integer winding numbers are topologically protected — they cannot change continuously. This is the BST origin of quantization: discrete eigenvalues are discrete winding numbers.

**Superposition** is Fourier decomposition — any circuit state is a superposition of winding modes:

$$\psi(\theta) = \sum_{n \in \mathbb{Z}} c_n \, e^{in\theta}$$

Superposition is not a postulate; it is the completeness of the Fourier basis on $S^1$.

**Spin and half-integer winding.** The winding number $n \in \mathbb{Z}$ gives integer-spin particles. Half-integer spins — fermions — arise from the double-cover structure $\mathrm{SU}(2) \to \mathrm{SO}(3)$: a circuit can wind once around $\mathrm{SO}(3)$ and not return to its starting configuration, requiring a second traversal to close. These spinor circuits have $n \in \mathbb{Z} + \tfrac{1}{2}$ effective winding. Bosons close after one winding; fermions close after two. The Pauli exclusion principle follows: two fermions cannot share the same winding state because their combined circuit would require four traversals to close, producing a state orthogonal to the two-traversal fermion state. Spin is not a postulate — it is the topology of $\mathrm{SU}(2)$ acting on the $S^2$ base of the substrate.

**The uncertainty principle** follows from the Fourier conjugacy of phase $\theta$ and winding number $n$. The operator $\hat{\theta}$ (fiber phase) and $\hat{n} = -i\partial/\partial\theta$ (winding number) satisfy:

$$[\hat{\theta}, \hat{n}] = i$$

This is not imposed — it is the canonical commutation relation of a conjugate pair on a circle, a standard result of Fourier analysis. Heisenberg's uncertainty principle $\Delta\theta \cdot \Delta n \geq 1/2$ is the statement that phase and winding number cannot both be sharp simultaneously, which is the mathematical content of the uncertainty principle with the $S^1$ fiber providing the geometry.

### 13.6 The Born Rule from Gleason's Theorem

Given the Hilbert space $L^2(S^1)$, the Born rule follows from Gleason's theorem (1957): on any Hilbert space of dimension $\geq 3$, the unique consistent probability assignment to projection operators is $p = |\langle \psi | \phi \rangle|^2$. The Gleason dimension requirement ($\geq 3$) is essential — the theorem fails for 2-dimensional Hilbert spaces, where the Kochen-Specker argument breaks down. The Hilbert space here is $L^2(S^1)$, which is countably infinite-dimensional (spanned by the orthonormal Fourier basis $\{e^{in\theta}\}_{n\in\mathbb{Z}}$), so Gleason's theorem applies without additional assumptions and the Born rule is uniquely forced.

The Born rule is therefore not an independent postulate of BST. It is the unique probability assignment consistent with the $L^2(S^1)$ Hilbert space structure. The squared modulus is forced.

**Conjecture:** The Bergman measure on $D_{IV}^5$ provides the natural measure on the configuration space that reduces on the fiber $S^1$ to the $L^2$ measure, unifying quantum probability and statistical mechanical probability as the same object — expectation values over substrate microstates.

### 13.7 Unitary Evolution as Thermodynamic Diffusion on $S^1$

Between contact commitment events, the substrate evolves by continuous phase accumulation. Many small discrete phase steps at the substrate scale average, by the central limit theorem, to a diffusion process. The governing equation for the probability distribution $P(\theta, \tau)$ over fiber phases at substrate time $\tau$ is:

$$\frac{\partial P}{\partial \tau} = D \frac{\partial^2 P}{\partial \theta^2}$$

This is the diffusion equation on $S^1$ with diffusion coefficient $D$. The eigenmodes are exactly the Fourier modes $e^{in\theta}$ with eigenvalues $-Dn^2$ — the same modes that are the energy eigenstates of the quantum free particle on a circle.

**The critical step — why $S^1$ gives unitary rather than dissipative evolution:**

Diffusion on $\mathbb{R}$ is dissipative. Information spreads and is lost. Diffusion on $S^1$ is fundamentally different: the space is compact, the boundary conditions are periodic, and the modes are discrete. No mode can decay to zero — the lowest mode $n=0$ is the constant function and is preserved exactly. Information is not lost; it is redistributed among the discrete winding modes. The compactness of the fiber is the physical reason quantum evolution is unitary rather than dissipative.

**Rotating to physical time** via $\tau \to it$ (the Wick rotation from Euclidean substrate time to Minkowski physical time):

$$\frac{\partial \psi}{\partial t} = iD \frac{\partial^2 \psi}{\partial \theta^2}$$

This is the free Schrödinger equation on $S^1$. The identification with the standard form $i\hbar \partial\psi/\partial t = H\psi$ gives:

$$H = -\hbar D \frac{\partial^2}{\partial \theta^2} = \frac{\hbar}{2m} \hat{n}^2$$

with $\hbar = 2mD$. The Hamiltonian is the square of the winding number operator — kinetic energy is the cost of winding faster. The energy spectrum $E_n = \hbar D n^2$ is discrete, as required.

**The Wick rotation** is not a mathematical trick here — it reflects the signature difference between the Euclidean substrate (circles, positive definite metric) and the emergent Minkowski spacetime (indefinite metric). The substrate evolves in Euclidean time; the projection acquires Minkowski signature. The rotation between them is forced by the geometry.

### 13.8 Planck's Constant as a Substrate Diffusion Coefficient

The derivation above identifies:

$$\hbar = 2mD$$

where $D$ is the diffusion coefficient of phase on the $S^1$ fiber at the substrate scale. Planck's constant is not a fundamental dimensionful constant of nature in BST — it is the diffusion coefficient of the communication channel, measuring how much phase accumulates per unit physical time at the substrate scale.

Its smallness in macroscopic units reflects the enormous ratio between the substrate scale (presumably near the Planck scale) and the scales of everyday physics — the same reason viscosity is small in air compared to molecular collision rates. In principle, $\hbar$ is calculable from the substrate contact rate and fiber geometry; it is a thermodynamic property of the vacuum state of the contact graph.

**The universality of $\hbar$.** The identification $\hbar = 2mD$ appears to make Planck's constant particle-dependent, since $D$ is the diffusion coefficient of a specific circuit on $S^1$. The resolution is that $D$ is inversely proportional to the particle's mass, with the product $mD$ universal.

The diffusion coefficient $D$ measures how rapidly a circuit's phase explores the $S^1$ fiber. A circuit is a closed path on the contact graph with a definite number of contacts $L_{\mathrm{circuit}}$. Each contact contributes one phase step per unit substrate time at the fundamental rate $\ell_0$ — the single-contact diffusion rate, a property of the substrate itself. A circuit with $L_{\mathrm{circuit}}$ contacts requires $L_{\mathrm{circuit}}$ substrate steps to complete one full phase cycle on $S^1$. Its diffusion coefficient is therefore:

$$D = \frac{\ell_0}{L_{\mathrm{circuit}}}$$

Mass in BST is proportional to circuit length: $m = L_{\mathrm{circuit}} \times m_0$, where $m_0$ is the mass-energy per contact. A longer circuit — more contacts, more winding energy — is a heavier particle. An electron (winding number 1, short circuit) has high $D$. A proton (three-quark circuit with $Z_3$ closure on $\mathbb{CP}^2$, long circuit) has low $D$.

The product $mD$ is then:

$$mD = (L_{\mathrm{circuit}} \cdot m_0) \times \frac{\ell_0}{L_{\mathrm{circuit}}} = m_0 \ell_0$$

which is independent of the particle. The circuit length cancels. The product depends only on $m_0$ (mass-energy per contact) and $\ell_0$ (phase diffusion rate per contact) — both properties of the substrate, not of any particular circuit. Therefore:

$$\hbar = 2mD = 2m_0\ell_0$$

is universal. Planck's constant equals twice the product of two substrate-scale quantities: the mass-energy of a single contact and the phase diffusion rate of a single contact. It is the fundamental action quantum of the substrate — one contact, one phase step — doubled by the geometry of the $S^1$ Fourier conjugacy.

**Physical consequences of the $D \propto 1/m$ scaling:**

- Heavier particles have smaller $D$: their phase packets spread more slowly on $S^1$. This is why massive objects behave classically — their diffusion rate is so small that quantum phase spreading is undetectable on any practical timescale.
- Lighter particles have larger $D$: their phase packets spread rapidly, producing the pronounced quantum behavior observed for electrons, neutrinos, and photons.
- The $D \propto 1/m$ scaling is the geometric origin of the de Broglie relation $\lambda = h/p$: a heavier particle's slower phase diffusion produces a shorter wavelength for the same momentum, because the phase cycle completes over fewer substrate contacts per unit distance.
- In the massless limit ($L_{\mathrm{circuit}} \to$ minimum, one contact per step), $D \to \ell_0$ reaches its maximum — the substrate's own diffusion rate. Photons diffuse at the fundamental rate because their circuit is the shortest possible path on the contact graph.

**Consequences:**

- Quantization is discreteness of winding numbers on a compact fiber — topology, not postulate
- Superposition is completeness of Fourier modes — analysis, not mystery
- Uncertainty is Fourier conjugacy of phase and winding — mathematics, not paradox
- Unitarity is compactness of $S^1$ — geometry, not axiom
- Collapse is phase commitment — irreversibility of contact, not measurement problem
- Born rule is Gleason's theorem on $L^2(S^1)$ — uniqueness, not assumption
- $\hbar$ is a diffusion coefficient — thermodynamics, not fundamental constant
- $D$ is circuit phase diffusion rate on $S^1$, inversely proportional to circuit length — thermodynamics, not free parameter
- Universality of $\hbar$ follows from universality of the substrate: every contact diffuses at rate $\ell_0$, and $\hbar = 2m_0\ell_0$ depends only on substrate properties

**Extension to 3D.** The derivation above is strictly for the $S^1$ fiber — a particle's phase dynamics on a single communication channel. The full 3D Schrödinger equation emerges when the $S^1$ phase dynamics are combined with the spatial geometry of the $S^2$ base: the substrate metric on $S^2$ contributes the kinetic term $-\hbar^2\nabla^2/2m$, with $\nabla^2$ the Laplacian on the contact graph in its continuum limit. The potential $V(\mathbf{x})$ encodes local contact density variations (Section 10). The universality of $\hbar = 2m_0\ell_0$ (independent of circuit length) ensures the same diffusion coefficient governs all particles in 3D. The 3D Schrödinger equation is the diffusion equation on $S^2 \times S^1$ in the continuum limit, Wick-rotated to Minkowski signature.

Quantum mechanics is what the BST substrate looks like when described in the language of the 3D projection. Its postulates are not independent axioms — they are consequences of the fiber geometry of $S^2 \times S^1$.

**Remark 13.1** (No wave function). BST never uses the term "wave function." The object that quantum mechanics calls $\psi$ does not appear at the substrate level — it is an operational tool for computing measurement predictions from the Planck-layer geometry. QM is not wrong; it is an extraordinarily successful operational formalism. But $\psi$ is the API, not the implementation. The fundamental objects are the substrate geometry ($D_{IV}^5$), the spectral parameters, and the contact commitment states. What appears as a "wave function" in the 3D projection is the pattern of $S^1$ phases across the contact graph. What appears as "collapse" is phase commitment. What appears as "superposition" is uncommitted contact capacity. The wave function is not a thing in the world; it is how the substrate looks from the outside.

### 13.9 The Bergman Dirac Operator on $D_{IV}^5$ (Spring 2026 operator-level progression)

The $\hbar = 2mD$ Hamiltonian derivation above is the fiber-restricted form. The full operator structure on $D_{IV}^5$ requires the Bergman Dirac operator $\gamma_B^\mu \nabla_\mu$ adapted to the rank-2 Hermitian symmetric domain. Spring 2026 work (LAG-1 Sessions 1–10) closed the following operator-level scaffolding; the references below cite the theorem registry and toys in the repository.

**The Bergman kernel in Hua coordinates.** The reproducing kernel of $L^2$-holomorphic functions on $D_{IV}^5$ has the closed form

$$K_B(z, w) = c \cdot D(z, w)^{-g/\text{rank}}$$

where $D(z, w)$ is the Cartan determinant on the rank-2 Hermitian symmetric domain and $g/\text{rank} = 7/2$ is one of the Cartan invariant ratios (T2334). The kernel is intrinsically a section of $K \otimes K^*$ on $D_{IV}^5 \times D_{IV}^5$ where $K = \wedge^{n_C} T^* D_{IV}^5$ is the canonical line bundle. The Bergman Laplacian's scalar form acts on sections of $K$, not on plain functions.

**Möbius cohomology with $\mathbb{Z}/2$ coefficients.** The Möbius locus $M \subset D_{IV}^5$ (the $\mathbb{Z}/2$-fixed-point structure under the involution that swaps the two strongly orthogonal roots) has degree-1 cohomology

$$H^1_{\mathbb{Z}/2}(M(D_{IV}^5), \mathbb{Z}) = \mathbb{Z}/2$$

(T2329). This $\mathbb{Z}/2$ class pins the CP-charge structure operators on the Möbius locus must respect, and is the topological side of the spin structure on $D_{IV}^5$.

**Borel–Wallach $(\mathfrak{g}, K)$-cohomology.** At the relevant degree, the Lie-algebraic $(\mathfrak{g}, K)$-cohomology of $D_{IV}^5$ is $\mathbb{Z}/2$ (T2335), dual-anchoring the same operator content from the Lie-algebraic side. The two $\mathbb{Z}/2$'s — topological (Möbius) and Lie-algebraic (Borel–Wallach) — are matched by the spin structure choice $\sqrt{K}$.

**The explicit Dirac matrices.** With the spin structure $\sqrt{K}$ fixed, the Bergman Dirac matrices $\gamma_B^\mu$ at the origin of Hua coordinates satisfy

$$\{\gamma_B^a, \gamma_B^b\} = 2 \eta^{ab}$$

with $\eta^{ab}$ the rank-2 Hermitian symmetric form. The 32-dimensional spinor representation decomposes correctly under Wallach $K$-types (T2365 + Toy 3037). Spin structure: $S = \sqrt{K}$, rank-32 spinor bundle on the real 10-dimensional $D_{IV}^5$.

**Heat kernel trace at origin — single-exponential structure.** The algebraic trace of $e^{-tD^2}$ restricted to the origin of $D_{IV}^5$ has the closed form

$$\mathrm{Tr}\big( e^{-tD_{\mathrm{alg}}^2}\big)\Big|_{\text{origin}} \;=\; \mathrm{rank}^{n_C} \cdot \exp\!\big({-(\mathrm{rank}\cdot n_C)\,t}\big) \;=\; 32 \cdot e^{-10 t}$$

(T2372, T2376, T2378 + Toys 3042, 3050). The pre-staged identity is

$$\mathrm{Tr}\big( D_{\mathrm{alg}}^{2k}\big) = 2 \cdot n_C^k \cdot \mathrm{rank}^{n_C + k - 1} = 32 \cdot 10^k \quad (k \geq 1)$$

verified against direct spectral sums at machine precision at low $k$ and consistent with the algebraic-trace-at-origin restriction at all $k$.

**Two eigentones identified.**

- *Dirac eigentone*: $\lambda_{\text{Dirac}} = \mathrm{rank} \cdot n_C = 10$ with degeneracy $\mathrm{rank}^{n_C} = 32$ (the spinor bundle dimension). Single eigenvalue — the Bergman Dirac spectrum at the origin is a Haldane-capped delta with 32-fold polarization channels.
- *Scalar eigentone*: $\lambda_{\text{scalar}} = 75/4 = N_c \cdot n_C^2 / \mathrm{rank}^2 = \mathrm{rank} \cdot n_C + |R|/4$ where $R = -n_C \cdot g = -35$ is the Bergman scalar curvature of $D_{IV}^5$ (T2339, T2377). This is the Lichnerowicz shift on the Bergman canonical line bundle $K$; one operator family, two cascades, related by

$$\mathrm{Tr}\big( e^{-t D^2}\big) = e^{-t R/4} \cdot \mathrm{Tr}\big( e^{-t \nabla^*\nabla_{\text{spinor}}}\big).$$

Eigentones at $\lambda = 10$ (fermion-sector substrate coupling) and $\lambda = 75/4$ (curvature/geometric coupling) are forced by $D_{IV}^5$ structure with no fitted parameters. Both are testable spectral-engineering resonances (SP-29 Casimir mechanism program, BaTiO$_3$ 137-plane experiment, photonic crystal periods).

**Td-class of the tangent bundle has BST primary structure throughout.** The five Chern classes of $T(D_{IV}^5)|_{Q^5}$ are all BST primary (T2379):

- $c_1 = N_c = 3$
- $c_2 = \mathrm{rank} \cdot n_C + 1 = 11$
- $c_3 = 13$
- $c_4 = N_c^2 = 9$
- $c_5 = C_2 = 6$ — *top Chern is the Casimir*

The identity $c_5 = C_2 = 6$ is the structural reason $C_2 = 6$ appears as the Bergman Casimir eigenvalue throughout BST observables: it is the integrand of the Euler-class top-form on the boundary geometry, not a coincidence. Low-order Todd-class factors decompose cleanly:

- $\mathrm{Td}_2$ numerator $= N_c^2 + c_2 = 20 = h^{1,1}(K3)$ — K3 cohomology connection at the index level
- $\mathrm{Td}_3 = c_2 / \mathrm{rank}^3 = 11/8$
- $\mathrm{Td}_4$ denominator $= C_2! = 6! = 720$
- $\mathrm{Td}_5$ denominator $= 2 \cdot C_2! = 1440$

**APS Index Theorem framework on $D_{IV}^5$.** Combining the explicit operator (above), the Möbius $\mathbb{Z}/2$ class (T2329), and the Bergman volume form $K_B^{1/(n_C+1)}\, d^{10}x$, the Atiyah-Patodi-Singer index theorem on $D_{IV}^5$ takes the form

$$\mathrm{ind}(D) \;=\; \int_{D_{IV}^5} \mathrm{Td}(T D_{IV}^5) \wedge \mathrm{ch}(K^{-1/2}) \;+\; \frac{\eta(Q^5) + h(Q^5)}{2}$$

with the boundary $\eta$-invariant on $Q^5$ contributing the $\mathbb{Z}/2$ correction. The conjectural cross-link with the Möbius $\mathbb{Z}/2$ class is

$$\big[\eta(Q^5)/2\big] \in \mathbb{Z}/2 \;=\; H^1_{\mathbb{Z}/2}(M(D_{IV}^5), \mathbb{Z}) \;=\; \nu(M).$$

This ODD-parity constraint filters the level-(3) integrated index candidates from $\{6, 12, 13, 15, 16\}$ down to $\{13, 15\}$ (multi-week Faraut–Koranyi integration will select between $c_3 = 13$ and $N_c \cdot n_C = 15$). LAG-1 Session 10 v0.1 outline + Step 5.1 + Step 5.2 prep: `notes/BST_LAG1_Session10_Index_Theorem_v0.1_outline.md`.

**Three operator-trace levels (frame for the audit chain).**

| Level | Operator | Bundle | Closed form |
|---|---|---|---|
| (1) Algebraic point-trace at origin | $\mathrm{Tr}(D^{2k})$ at one point, Lie-algebraic structure constants | spinors | $32 \cdot 10^k$ |
| (2) Heat-kernel coefficient at origin | $\mathrm{Coeff}_n = \mathrm{Tr}(D^{2n})/n!$ at origin | spinors | $32 \cdot 10^n/n!$ (Dirac); $32 \cdot (75/4)^n/n!$ (Lichnerowicz scalar) |
| (3) Integrated Seeley-DeWitt $a_n$ | $\int_{D_{IV}^5} a_n(x)\, dV$ — full spectral coefficients | scalar Laplacian on $K$ | Three Theorems alternating polynomial with cyclotomic denominators |

Levels (1) and (2) are equivalent ($\mathrm{Coeff}_n = \mathrm{Tr}/n!$). The bridge (1)/(2) $\to$ (3) is the multi-week integration-over-$D_{IV}^5$ derivation that brings in regularization, volume, and curvature corrections producing the Three Theorems polynomial structure observed in level (3).

**Heat kernel cascade extension at level (3) — K53 D-tier structural law (Spring 2026).** The Three Theorems framework (Toy 2994) gives the closed form for the ratio of consecutive integrated Seeley-DeWitt coefficients on $D_{IV}^5$:

$$\frac{a_k}{a_{k-1}} = -\frac{k(k-1)}{2 \cdot n_C} = -\frac{k(k-1)}{10}.$$

Pre-staged via Toy 2994 + Lyra T2376 / Grace T2375 on May 18 morning; forward-verified via Toy 3051 on May 18 afternoon with **24 consecutive levels matching at machine precision (k = 1..24, with 11 explicit ratio checks at $k \in \{5, 6, 10, 11, 15, 16, 20, 21, 22, 23, 24\}$ all PASS)**. The audit (K53, `notes/K53_Three_Theorems_Cascade_Extension.md`) PROMOTED to D-tier structural law with scope qualifier: closed form applies specifically to level (3) integrated SD on $D_{IV}^5$ within $k \leq 24$. Extension to $k \geq 25$ requires additional independent $n$-values at high decimal precision (\~6 days compute per new $n$; \~8-month compute horizon to $k = 44$ per polynomial-regression dimensional constraint).

**Open multi-week and multi-year scope (LAG-1, LAG-2).** The operator-level scaffolding above is in place; what remains:

- **LAG-1 (multi-week)**: $\gamma_B^\mu$ at non-origin Hua coordinates with full spin-connection contributions; Faraut–Koranyi integration of $\mathrm{Td}(T D_{IV}^5) \wedge \mathrm{ch}(K^{-1/2})$ over $D_{IV}^5$; resolution of $\mathrm{ind}(D) \in \{13, 15\}$ between the two ODD candidates; explicit closure of $S_{\text{ferm}}$ term of the BST Lagrangian. Several intermediate publishable results along the way.

- **LAG-2 (multi-year, 5-phase)**: dimensional reduction $D_{IV}^5 \to \mathbb{R}^{3,1}$ as a clean functional. Phase 1 identifies the 4+6 split structurally (Hopf fibration $S^3 \to S^2$ for electroweak + $S^1$ communication fiber + rank-2 polar coordinates = 4 internal; the remaining 4 are spacetime); Phase 2 computes the reduction integral for $S_{\text{geom}}$; Phase 3 extends to all six terms; Phase 4 verifies Einstein equation emerges in 4D limit; Phase 5 verifies $SU(3) \times SU(2)_L \times U(1)_Y$ survives reduction. WorkingPaper Section 13.8 Hamiltonian (above) is the substrate side; LAG-2 closes the projection side.

The BST action principle is in place. The operator forms have algebraic-at-origin closed forms verified at machine precision. The integrated Seeley-DeWitt cascade is structurally-confirmed through $k = 24$ levels (K53 D-tier). What remains open is the geometrically-explicit Dirac at non-origin coordinates and the 4D projection — both are concrete multi-week/multi-year computational programs, not conceptual gaps.

References:
- *Six-term Lagrangian*: `notes/BST_Lagrangian.md` (March 2026)
- *LAG-1 progression Sessions 2–10*: theorems T2349–T2354 (S2–S7 algebraic), T2365 (S8 explicit Dirac matrices), T2372/T2376/T2378 (S9 heat kernel cascade), T2379 (S10 Step 5.1 Chern classes), Session 10 outline `notes/BST_LAG1_Session10_Index_Theorem_v0.1_outline.md`
- *K53 audit*: `notes/K53_Three_Theorems_Cascade_Extension.md`
- *Three-level operator framework*: see the table above + Lichnerowicz prep `notes/BST_Tuesday_Lichnerowicz_Shift_Derivation_Prep.md`
- *Paper #118 v0.2*: Bergman Dirac Operator + Lichnerowicz + $m_p/m_e$ mechanism (Lyra, in flight)
- *Paper #120 v0.2*: G/inertia substrate-mediated via eigentone saddle (three-CI merged outline)

-----

