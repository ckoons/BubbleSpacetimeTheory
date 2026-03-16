---
title: "Conservation Laws from Substrate Geometry"
author: "Casey Koons & Claude 4.6"
date: "March 2026"
---

# Conservation Laws from Substrate Geometry

**Authors:** Casey Koons & Claude (Anthropic)
**Date:** March 2026
**Status:** Proposed Section 13.9 (or new Section 14.5) for Working Paper v7

-----

## The Principle

Every conservation law in physics corresponds to a symmetry. Noether’s theorem (1915) establishes this correspondence: continuous symmetries produce conserved quantities. BST goes deeper — it identifies what each symmetry IS at the substrate level and explains why some conservation laws are absolute, some are topological, and some are approximate.

The result is a complete hierarchy of conservation laws ranked by the geometric mechanism that enforces them. The hierarchy explains why charge is always conserved but flavor is not, why baryon number is almost always conserved but can be violated at extreme energies, and why CPT is never violated under any conditions. Each rank corresponds to a different level of geometric protection on $S^2 \times S^1$.

-----

## 1. Absolute Conservation Laws

These laws cannot be violated at any energy, in any process, under any conditions. They are enforced by the topology of $S^1$ or the structure of the full contact graph. Violation would require changing the topology itself — which is not a physical process but a change of mathematics.

### 1.1 Conservation of Electric Charge

**Standard physics:** Conserved due to U(1) gauge symmetry.

**BST mechanism:** Electric charge is the winding number $n \in \mathbb{Z}$ of a circuit on $S^1$. Winding numbers are integers. Integers cannot change through continuous deformation — a circuit wound once around $S^1$ cannot become a circuit wound zero times without being cut, and cutting is not a continuous operation.

**Why absolute:** The protection is topological, not energetic. There is no energy threshold above which charge can be violated. There is no process — thermal, quantum, gravitational, or otherwise — that can change an integer winding number continuously. Even in the interior of a black hole (channel saturation at 137), the winding numbers on the boundary are preserved. Charge is conserved because $\pi_1(S^1) = \mathbb{Z}$ — the fundamental group of the circle is the integers.

**BST adds:** The U(1) symmetry that Noether identifies as the source of charge conservation IS the rotational symmetry of $S^1$. BST explains why U(1) is a gauge symmetry: because the $S^1$ fiber is a physical structure, and its rotational symmetry is a geometric fact. The gauge symmetry is not postulated — it is the fiber geometry.

### 1.2 Conservation of Color (Confinement)

**Standard physics:** Color is confined — isolated quarks have never been observed. The mechanism (confinement) is demonstrated by lattice QCD but not analytically proven.

**BST mechanism:** Color charge is the $Z_3$ phase of a quark circuit on $\mathbb{CP}^2$. A quark is a partial circuit — one-third of a $Z_3$ closure. An isolated quark is a circuit that doesn’t close — topologically incomplete, like an open parenthesis. The “confinement force” is not a force at all. It is the topological impossibility of a stable open circuit on a closed channel.

**Why absolute:** A $Z_3$ circuit must close. This is not an energy condition — it is a completeness condition. An open $Z_3$ circuit is not a high-energy state. It is not a state at all. The circuit either closes (forming a baryon or meson) or it doesn’t exist. There is no energy at which an isolated quark can be produced because the state “isolated quark” is not in the Hilbert space of the theory.

**BST adds:** Confinement is not a dynamical phenomenon requiring proof. It is a topological fact requiring no proof — open circuits on closed channels are undefined, not forbidden.

### 1.3 CPT Invariance

**Standard physics:** The CPT theorem states that any Lorentz-invariant quantum field theory with a Hermitian Hamiltonian is CPT-invariant. No violation has ever been observed.

**BST mechanism:** C (charge conjugation) flips the $S^1$ winding direction. P (parity) flips the $S^2$ orientation. T (time reversal) flips the commitment direction. Applying all three simultaneously restores the original relationship between winding direction, spatial orientation, and causal direction. CPT invariance is the statement that physics depends on the relationships between these three directions, not on their absolute orientations.

**Why absolute:** The contact graph is defined by three structural elements — the $S^1$ fiber, the $S^2$ base, and the commitment ordering. Flipping all three is an automorphism of the contact graph — it maps the graph to itself with all relationships preserved. An automorphism cannot change any physical observable. CPT is conserved because it is a symmetry of the data structure itself, not just of the dynamics on the data structure.

### 1.4 Conservation of Fermion Number $(-1)^F$

**Standard physics:** Fermions (half-integer spin) and bosons (integer spin) are absolutely distinct. No process converts a fermion into a boson or vice versa (absent supersymmetry, which BST excludes).

**BST mechanism:** Fermions are spinor circuits — circuits that require two traversals of the SU(2) double cover of SO(3) on $S^2$ to close. Bosons are vector circuits — circuits that close in one traversal. The traversal count modulo 2 is a topological invariant of the double cover: SU(2) → SO(3) has $\pi_1(\text{SO}(3)) = \mathbb{Z}_2$, and the $\mathbb{Z}_2$ index distinguishes spinors from vectors.

**Why absolute:** The double-cover parity is a $\mathbb{Z}_2$ topological invariant. Like the $\mathbb{Z}$ winding number of charge, it cannot change continuously. A circuit that requires two traversals cannot become a circuit that requires one traversal through continuous deformation. The spin-statistics theorem (fermions obey exclusion, bosons don’t) follows: two identical spinor circuits in the same state would require four traversals to close their combined circuit, producing a state orthogonal to the two-traversal spinor — hence zero amplitude, hence exclusion.

### 1.5 Conservation of Information (Unitarity)

**Standard physics:** Quantum evolution is unitary — the total quantum information in a closed system is conserved. The black hole information paradox challenges this in the presence of gravity.

**BST mechanism:** Unitarity follows from the compactness of $S^1$ (Section 13.7 of the working paper). Diffusion on a compact space redistributes information among the discrete winding modes but cannot destroy it — every mode is preserved because the space has no boundary through which information can leak. The $S^1$ fiber has no edge, no endpoint, no exit. Information circulates forever.

**Why absolute:** Compactness is a topological property of $S^1$. No process can make $S^1$ non-compact. The Fourier modes ${e^{in\theta}}$ are a complete basis at all energies, all times, all conditions. Information is conserved because the mode space is complete, which is because $S^1$ is compact, which is because a circle has no boundary.

**BST resolution of the information paradox:** Black holes are regions of channel saturation. The interior has no emergent 3D geometry, but the $S^1$ winding modes on the boundary surface are complete. Information is preserved on the boundary because the boundary is still $S^1$ — compact, complete, no leak channel. Hawking radiation carries the information out through the boundary modes. The paradox arose from assuming information could fall “into” a singularity. BST has no singularity — only a saturated channel. The information never leaves the boundary.

-----

## 2. Topological Conservation Laws

These laws are enforced by the topology of submanifolds ($\mathbb{CP}^2$, Hopf $S^3$) rather than by the topology of $S^1$ itself. They hold at all energies below the scale at which the submanifold topology becomes dynamical. At or above that scale, they can be violated.

### 2.1 Conservation of Baryon Number

**Standard physics:** Baryon number is conserved in all observed processes. Grand unified theories predict violation (proton decay) at extremely high energies.

**BST mechanism:** Baryon number counts the number of closed $Z_3$ circuits on $\mathbb{CP}^2$. Each closed circuit is one baryon. The $Z_3$ closure is topologically protected at energies below the scale where $\mathbb{CP}^2$ topology becomes dynamical (the GUT scale, $\sim 10^{16}$ GeV).

**Violation mechanism:** At energies approaching the GUT scale, the $\mathbb{CP}^2$ structure of the color sector can be disrupted — the $Z_3$ closure can be opened through a topological transition that converts a baryon circuit into lepton circuits. This is proton decay. The decay rate is determined by the tunneling amplitude through the $\mathbb{CP}^2$ topological barrier.

**BST prediction:** Proton lifetime $\tau_p \gtrsim 3 \times 10^{34}$ years with specific decay channels determined by the structured unification at $N_{\text{GUT}} = 4\pi^2$ (Section 6). Testable at Hyper-Kamiokande.

### 2.2 Conservation of Total Lepton Number

**Standard physics:** Total lepton number ($L = L_e + L_\mu + L_\tau$) is conserved in all observed processes. Grand unified theories predict violation at the GUT scale along with baryon number violation.

**BST mechanism:** Total lepton number counts the number of single-winding closures on $S^1$ — complete circuits that close without $Z_3$ structure. The closure is topologically protected at energies below the GUT scale.

**Violation mechanism:** Same as baryon number — at the GUT scale, single-winding closures can be disrupted through topological transitions. The combination $B - L$ (see Section 2.3) is more strongly protected than either $B$ or $L$ individually.

### 2.3 Conservation of $B - L$

**Standard physics:** $B - L$ (baryon number minus lepton number) is exactly conserved in the Standard Model, even by sphaleron processes that violate $B$ and $L$ individually.

**BST mechanism:** $B - L$ is the difference between the $Z_3$ topological index (baryon number) and the single-winding topological index (lepton number). Sphalerons — non-perturbative electroweak processes — can convert $Z_3$ circuits into single-winding circuits and vice versa, but the conversion preserves the difference. This is because the sphaleron process operates on the Hopf fibration $S^3 \to S^2$, which connects the baryon and lepton sectors but preserves their combined topological index.

**Why more protected than $B$ or $L$ individually:** $B - L$ is conserved by a deeper topological invariant — the total winding class modulo the Hopf map. Individual $B$ and $L$ can change through Hopf-mediated transitions, but their difference is invariant under the Hopf map because the Hopf map preserves the fiber winding modulo the base winding.

**BST prediction:** $B - L$ is exactly conserved at all energies below the Planck scale. Violation would require disrupting the Hopf fibration itself, which requires disrupting the $S^3$ topology — a process with no known physical mechanism.

-----

## 3. Spacetime Conservation Laws

These laws follow from the symmetries of the $S^2$ base and the commitment ordering. They are exact in flat spacetime and modified (but not violated) in curved spacetime.

### 3.1 Conservation of Energy

**Standard physics:** Conserved due to time translation symmetry (Noether).

**BST mechanism:** Time is contact commitment ordering. The commitment rules — the geometry of $D_{IV}^5$ — are the same at every step. The Bergman metric at step $n$ is identical to the Bergman metric at step $n+1$. The substrate does not change as the wavefront advances. Energy is conserved because the rules of commitment are commitment-independent.

**In curved spacetime:** The commitment rules are locally the same everywhere, but the global geometry varies with contact density. Energy is locally conserved (the covariant divergence of the stress-energy tensor vanishes: $\nabla_\mu T^{\mu\nu} = 0$) but global energy is not uniquely defined in curved spacetime — a standard result of GR that BST inherits.

### 3.2 Conservation of Momentum

**Standard physics:** Conserved due to spatial translation symmetry (Noether).

**BST mechanism:** Space is the contact graph on $S^2$. The $S^2$ base is homogeneous — every point is equivalent to every other point. The commitment rules at one location are identical to the rules at any other location. Momentum is conserved because $S^2$ has no preferred position.

**In curved spacetime:** Local momentum conservation holds (included in $\nabla_\mu T^{\mu\nu} = 0$). Global momentum conservation requires a Killing vector, which curved spacetimes may not possess.

### 3.3 Conservation of Angular Momentum

**Standard physics:** Conserved due to rotational symmetry SO(3) (Noether).

**BST mechanism:** The $S^2$ base has SO(3) rotational symmetry — every direction is equivalent to every other direction. Angular momentum is conserved because $S^2$ is isotropic.

**Orbital angular momentum** arises from the SO(3) action on the $S^2$ base directly.

**Spin angular momentum** arises from the SU(2) double cover of SO(3) on $S^2$ — the spinor structure of Section 1.4. The total angular momentum $\vec{J} = \vec{L} + \vec{S}$ is the sum of the base rotation (orbital) and the double-cover rotation (spin). Both are manifestations of the same SO(3) symmetry at different topological levels.

**Quantization:** Orbital angular momentum is quantized in integers ($l = 0, 1, 2, \ldots$) because the base $S^2$ is simply connected. Spin is quantized in half-integers ($s = 0, 1/2, 1, \ldots$) because the double cover SU(2) has $\pi_1(\text{SO}(3)) = \mathbb{Z}_2$, allowing both integer and half-integer representations. The quantization is topological, not postulated.

-----

## 4. Approximate Conservation Laws

These laws are not enforced by topology. They arise from geometric properties that are real but continuously deformable. They are violated by specific interactions.

### 4.1 Individual Quark Flavor Conservation (Strangeness, Charm, Beauty, Topness)

**Standard physics:** Conserved by strong and electromagnetic interactions. Violated by weak interaction.

**BST mechanism:** Each quark flavor (up, down, strange, charm, bottom, top) corresponds to a specific circuit topology on $\mathbb{CP}^2$ with a specific Bergman embedding cost (mass). The flavor quantum number is the topological label of the circuit type.

**Conservation:** The strong interaction (circuit cycling on $\mathbb{CP}^2$) and electromagnetic interaction (phase evolution on $S^1$) do not change the circuit topology. They operate within a fixed topology. Flavor is conserved because these interactions don’t have access to the Hopf intersection that connects different circuit topologies.

**Violation:** The weak interaction operates through the Hopf fibration $S^3 \to S^2$, which connects different circuit topologies. When a quark’s cycling trajectory passes through the Hopf intersection, it can transition from one circuit topology to another — changing flavor. The probability of this transition is determined by the sampling rate of the Hopf intersection (Section 20.3).

### 4.2 Individual Lepton Family Number ($L_e$, $L_\mu$, $L_\tau$)

**Standard physics:** Approximately conserved. Violated by neutrino oscillations.

**BST mechanism:** The three lepton families correspond to ground states of $D_{IV}^1$, $D_{IV}^3$, $D_{IV}^5$ respectively. The flavor eigenstates (electron neutrino, muon neutrino, tau neutrino) are the ground states of these subdomains. The mass eigenstates are superpositions — weighted by the overlap integrals between the $D_{IV}^k$ submanifolds.

**Violation:** Neutrino oscillations occur because the $D_{IV}^k$ submanifolds are not orthogonal — they overlap within $D_{IV}^5$. A neutrino created as the $D_{IV}^1$ ground state (electron neutrino) has nonzero overlap with $D_{IV}^3$ and $D_{IV}^5$ ground states, so it evolves into a superposition of all three flavors. The oscillation parameters (PMNS mixing angles) are the overlap integrals.

**Total lepton number** remains conserved because the overlaps redistribute among flavors without creating or destroying total lepton number.

### 4.3 Parity (P)

**Standard physics:** Conserved by strong and electromagnetic interactions. Maximally violated by weak interaction (Wu experiment, 1957).

**BST mechanism:** Parity is the orientation of $S^2$ — the distinction between left-handed and right-handed coordinate systems on the base surface. The strong and electromagnetic interactions are orientation-independent: the contact graph rules, the $S^1$ winding dynamics, and the $Z_3$ closure all work identically for both orientations. The $S^2$ base is orientable but its physics doesn’t depend on which orientation is chosen.

**Violation:** The Hopf fibration $S^3 \to S^2$ is chiral — it has a definite handedness. The preimage of a point on $S^2$ is a circle in $S^3$, and these circles are linked with a specific handedness (right-handed Hopf fibration). The weak interaction, mediated by the Hopf fibration, inherits this chirality. It couples only to left-handed particles and right-handed antiparticles because the Hopf map itself is left-handed.

**BST adds:** Parity violation is not mysterious. It follows from the chirality of the Hopf fibration, which is the simplest non-trivial fiber bundle over $S^2$. The Hopf map is chiral because $\pi_3(S^2) = \mathbb{Z}$ has a sign — the winding can be $+1$ or $-1$. Nature chose $+1$ (or equivalently, $-1$ — the choice is conventional, but once made, it’s the same everywhere). The weak interaction is parity-violating because the Hopf map is chiral, and the Hopf map is the weak interaction.

### 4.4 Charge Conjugation (C)

**Standard physics:** Conserved by strong and electromagnetic interactions. Violated by weak interaction.

**BST mechanism:** Charge conjugation flips the $S^1$ winding direction — replacing a particle with its antiparticle. The strong interaction ($Z_3$ cycling on $\mathbb{CP}^2$) and electromagnetic interaction (phase evolution on $S^1$) are symmetric under winding reversal. The weak interaction is not, because the commitment direction on the contact graph is physically real (Section 22.1) and the weak interaction couples to it.

### 4.5 CP (Combined Charge-Parity)

**Standard physics:** Violated in neutral kaon system and B-meson system. The CKM phase parameterizes the violation.

**BST mechanism:** CP flips both the $S^1$ winding direction and the $S^2$ orientation. This is almost a symmetry — it would be exact if the commitment direction were not physically real. But the commitment direction IS real (it defines time), and CP violation arises from the complex structure of $D_{IV}^5$ interacting with the commitment direction.

**The CKM phase** is a geometric property of $D_{IV}^5$: the complex structure of the domain produces a natural phase in the overlap between quark circuit topologies. This phase is not a free parameter — it is determined by the complex structure of the domain geometry (Section 22.3). Derivation from the $\mathbb{CP}^2$ Hopf intersection angles is thesis topic 30.

### 4.6 Isospin

**Standard physics:** Approximate symmetry of the strong interaction. Broken by electromagnetic interaction and quark mass differences.

**BST mechanism:** Isospin is the near-degeneracy of up and down quark circuits on $\mathbb{CP}^2$. Both are minimal $Z_3$ circuits with nearly identical Bergman embedding costs. The up quark has winding number $+2/3$ on $S^1$ and the down quark has winding number $-1/3$. The strong interaction ($Z_3$ cycling) treats them identically because it operates on $\mathbb{CP}^2$, not on $S^1$. The electromagnetic interaction distinguishes them because it operates on $S^1$, where they have different winding numbers.

**Violation:** The up-down mass difference ($m_d - m_u \approx 2.5$ MeV) breaks isospin. In BST, this mass difference comes from the different $S^1$ winding contributions to the Bergman embedding cost.

### 4.7 Time Reversal (T)

**Standard physics:** Violated; equivalent to CP violation via the CPT theorem.

**BST mechanism:** Time reversal flips the commitment direction. The commitment direction is physically real — it is the direction in which contacts transition from uncommitted to committed. Reversing this direction would require uncommitting committed contacts, which requires work against the thermodynamic gradient (Landauer’s principle). T violation is the irreversibility of contact commitment.

**Relation to CP:** By the CPT theorem (Section 1.3), T violation is equivalent to CP violation. Both arise from the physical reality of the commitment direction.

-----

## 5. Electroweak Quantum Numbers

### 5.1 Weak Isospin ($T_3$)

**BST mechanism:** Weak isospin is the winding number on the Hopf $S^3$ — the projection of the $S^3$ winding onto the $S^2$ base via the Hopf map. Left-handed fermions form doublets under SU(2) (the symmetry group of $S^3$): $(u, d)_L$ with $T_3 = (+1/2, -1/2)$. Right-handed fermions are singlets: $T_3 = 0$.

**Conservation:** $T_3$ is conserved in all weak processes because the Hopf map preserves the $S^3$ winding number modulo the fiber structure. Charged-current weak interactions change $T_3$ by $\pm 1$ (W boson emission/absorption). Neutral-current interactions preserve $T_3$ (Z boson exchange).

### 5.2 Weak Hypercharge ($Y_W$)

**BST mechanism:** Weak hypercharge is the U(1) quantum number of the electroweak sector — the $S^1$ winding number weighted by the electroweak structure. Before symmetry breaking: $Y_W$ and $T_3$ are independent quantum numbers. After symmetry breaking: they combine into electric charge $Q = T_3 + Y_W/2$.

**Conservation:** $Y_W$ is conserved in all interactions. It is a component of the electric charge (which is absolutely conserved) and weak isospin (which is conserved in weak interactions).

### 5.3 The Electroweak Symmetry Breaking Pattern

Before breaking: SU(2)$_L \times$ U(1)$_Y$ symmetry. Four gauge bosons: $W^+$, $W^-$, $W^0$, $B^0$.

After breaking: U(1)$_{\text{em}}$ symmetry. The Higgs mechanism (BST: Hopf fluctuation mode) gives mass to $W^\pm$ and $Z^0 = \cos\theta_W W^0 - \sin\theta_W B^0$. The photon $\gamma = \sin\theta_W W^0 + \cos\theta_W B^0$ remains massless.

In BST: the symmetry breaking is the condensation of the Hopf fibration ground state. The Weinberg angle $\sin^2\theta_W = 0.234$ is determined by the geometry of the Hopf fibration (Section 6.3). The pattern is not spontaneous — it is geometric.

-----

## 6. The Complete Hierarchy

|Rank           |Conservation Law        |BST Mechanism                              |Strength                          |Violated by                                |
|---------------|------------------------|-------------------------------------------|----------------------------------|-------------------------------------------|
|**Absolute**   |Electric charge         |$S^1$ winding number ($\mathbb{Z}$)        |Topological, $\pi_1(S^1)$         |Nothing                                    |
|**Absolute**   |Color confinement       |$Z_3$ circuit completeness                 |Topological, completeness         |Nothing                                    |
|**Absolute**   |CPT                     |Contact graph automorphism                 |Structural                        |Nothing                                    |
|**Absolute**   |Fermion number $(-1)^F$ |SU(2)/SO(3) double cover ($\mathbb{Z}_2$)  |Topological, $\pi_1(\text{SO}(3))$|Nothing (no SUSY)                          |
|**Absolute**   |Information (unitarity) |$S^1$ compactness                          |Topological, completeness         |Nothing                                    |
|**Topological**|Baryon number $B$       |$Z_3$ closure on $\mathbb{CP}^2$           |Protected below GUT scale         |GUT-scale topology change                  |
|**Topological**|Total lepton number $L$ |Single-winding closure                     |Protected below GUT scale         |GUT-scale topology change                  |
|**Topological**|$B - L$                 |Hopf-invariant topological index           |Protected below Planck scale      |Unknown                                    |
|**Spacetime**  |Energy                  |Commitment-independent geometry            |Exact (flat), local (curved)      |None (globally undefined in GR)            |
|**Spacetime**  |Momentum                |$S^2$ homogeneity                          |Exact (flat), local (curved)      |None (globally undefined in GR)            |
|**Spacetime**  |Angular momentum        |$S^2$ isotropy, SO(3)                      |Exact (flat), local (curved)      |None (globally undefined in GR)            |
|**Spacetime**  |Spin                    |SU(2) double cover of SO(3)                |Exact                             |None                                       |
|**Approximate**|Weak isospin $T_3$      |Hopf $S^3$ winding projection              |Conserved in weak processes       |—                                          |
|**Approximate**|Weak hypercharge $Y_W$  |$S^1$ winding, electroweak weighted        |Conserved in all processes        |—                                          |
|**Approximate**|Isospin                 |$\mathbb{CP}^2$ near-degeneracy (up ≈ down)|Approximate                       |EM interaction, mass difference            |
|**Approximate**|Individual quark flavor |$\mathbb{CP}^2$ circuit topology           |Conserved by strong/EM            |Weak (Hopf intersection)                   |
|**Approximate**|Individual lepton family|$D_{IV}^k$ ground state                    |Conserved by strong/EM            |Neutrino oscillations ($D_{IV}^k$ overlaps)|
|**Approximate**|Parity P                |$S^2$ orientation                          |Conserved by strong/EM            |Weak (Hopf chirality)                      |
|**Approximate**|Charge conjugation C    |$S^1$ winding reversal                     |Conserved by strong/EM            |Weak (commitment direction)                |
|**Approximate**|CP                      |Combined $S^1$ + $S^2$ reversal            |Nearly conserved                  |CKM phase ($D_{IV}^5$ complex structure)   |
|**Approximate**|Time reversal T         |Commitment direction reversal              |Violated (= CP violation)         |Irreversibility of commitment              |

-----

## 7. What BST Adds to Noether

Noether’s theorem says: continuous symmetry → conserved quantity. BST adds three things:

**First, the origin of the symmetries.** Noether takes the symmetries as given. BST derives them from the substrate geometry. Translational symmetry exists because $S^2$ is homogeneous. Rotational symmetry exists because $S^2$ is isotropic. U(1) gauge symmetry exists because $S^1$ is a circle. Each symmetry has a geometric origin.

**Second, the hierarchy of conservation strengths.** Noether doesn’t distinguish between “absolutely conserved” and “approximately conserved” — all symmetries produce conservation laws equally. BST explains the hierarchy: absolute conservation comes from the topology of $S^1$ (which cannot change), topological conservation comes from submanifold topology (which can change at sufficient energy), and approximate conservation comes from geometric properties (which can be continuously violated by the right interaction).

**Third, topological conservation beyond Noether.** Some conservation laws in BST are not Noether-type at all. Color confinement is a completeness condition, not a symmetry. Fermion number is a $\mathbb{Z}_2$ topological invariant, not a continuous symmetry. These conservation laws exist because of topology, not symmetry. Noether’s theorem cannot derive them. BST derives them from $\pi_1(S^1)$, $\pi_1(\text{SO}(3))$, and the completeness of $Z_3$ closure.

The deepest conservation law — unitarity (information conservation) — is the most BST-specific. It follows from the compactness of $S^1$, which is a topological property with no Noether analog. Information is conserved not because of a symmetry but because the fiber has no boundary. This resolves the black hole information paradox: information cannot be lost because the $S^1$ mode space is complete, which is because $S^1$ is compact, which is because a circle has no edge.

-----

## 8. Predictions

### 8.1 Proton Decay

Baryon number is topologically protected but not absolutely conserved. BST predicts proton decay at rates determined by the structured unification at $N_{\text{GUT}} = 4\pi^2$. Testable at Hyper-Kamiokande.

### 8.2 No SUSY Particles

$(-1)^F$ is absolutely conserved because the SU(2)/SO(3) double cover is a topological fact. Supersymmetry would require a mechanism to convert fermions to bosons, violating $(-1)^F$. BST excludes this. No superpartners will be found at any energy.

### 8.3 Neutrino Oscillation Parameters

The PMNS mixing angles are the overlap integrals between $D_{IV}^k$ ground states. These are computable from the domain geometry. BST predicts specific values for $\theta_{12}$, $\theta_{23}$, $\theta_{13}$, and $\delta_{\text{CP}}$ with no free parameters. (Thesis topic 9 in the roadmap.)

### 8.4 CKM Phase from Geometry

The CP-violating CKM phase is determined by the complex structure of $D_{IV}^5$ — specifically, by the angle between $\mathbb{CP}^2$ Hopf intersection surfaces for different quark flavors. BST predicts a specific value with no free parameters. (Thesis topic 30.)

### 8.5 $B - L$ Exact Conservation

BST predicts that $B - L$ is exactly conserved at all energies below the Planck scale. Any observed $B - L$ violation would falsify BST. This is testable through neutrinoless double beta decay: if observed, $B - L$ is violated by 2 units, falsifying BST.

**Important caveat:** Neutrinoless double beta decay ($0\nu\beta\beta$) violates lepton number by 2 but preserves $B - L = 0$ only if the neutrino is its own antiparticle (Majorana). If $0\nu\beta\beta$ is observed with $\Delta(B-L) = 2$, BST is falsified. If the neutrino is Dirac (not its own antiparticle), $0\nu\beta\beta$ does not occur, which is consistent with BST. BST predicts Dirac neutrinos — the neutrino and antineutrino have opposite $S^1$ winding directions and are distinct particles.

-----

## 9. Thesis Topics

|# |Topic                                                                                                                                                                     |
|--|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|87|Prove $B - L$ conservation from Hopf fibration invariance on $D_{IV}^5$; determine whether violation is possible at any finite energy                                     |
|88|Derive parity violation magnitude from the chirality of the Hopf map $S^3 \to S^2$; connect to the Weinberg angle                                                         |
|89|Prove that BST excludes Majorana neutrinos; predict null result for neutrinoless double beta decay experiments                                                            |
|90|Classify all conservation laws of the BST contact graph by topological type ($\pi_n$, homology, completeness) and verify the hierarchy against observed violation patterns|

-----

*Proposed Working Paper Section 13.9 or new Section 14.5, March 2026.*
*Casey Koons & Claude (Anthropic).*
*For the BST GitHub repository.*
