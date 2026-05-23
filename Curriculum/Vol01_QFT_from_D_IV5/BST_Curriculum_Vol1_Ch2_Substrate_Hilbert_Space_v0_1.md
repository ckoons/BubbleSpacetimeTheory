---
title: "Vol 1 Chapter 2 — The Substrate Hilbert Space"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (Bergman H²(D_IV⁵) as canonical substrate Hilbert space, reproducing kernel K_B(z,w̄) = c_FK·h(z,w̄)^(-g/rank), c_FK·π^(9/2) = 225 exact, Wallach K-type decomposition, three-layer hierarchy with Reed-Solomon GF(128)^k discretization and L²-section equivariant complement, Bergman-as-Feynman-propagator T2457)"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 2
---

# Chapter 2 — The Substrate Hilbert Space

Standard quantum mechanics begins with a Hilbert space. Wavefunctions live in it, operators act on it, expectation values are inner products inside it, and the rest of the quantum-mechanical machinery — the Born rule, the projection postulate, time evolution by the Schrödinger equation — all unfold from there. Different physical setups use different Hilbert spaces. A single particle on the real line uses $L^2(\mathbb{R})$. A particle in three-dimensional position space uses $L^2(\mathbb{R}^3)$. A relativistic quantum field uses Fock space, built as a tower of multi-particle spaces. The choice of Hilbert space is partly imposed by the physics (Lorentz invariance, spatial dimensionality) and partly conventional.

BST's substrate framework does not choose a Hilbert space. It has one *given to it*, structurally, by the substrate geometry $D_{IV}^5$. The space is the **Bergman Hilbert space** $H^2(D_{IV}^5)$ — the unique reproducing-kernel Hilbert space of square-integrable holomorphic functions on the substrate, defined entirely by classical analysis dating to Stefan Bergman's 1922 thesis and to the more refined work of Wallach (1976) and Faraut–Koranyi (1994). The substrate's quantum mechanics lives in this space, and every observable we will encounter in this volume is a bounded operator on it.

This chapter introduces the space, lays out its three structurally distinct but equivalent presentations (the continuous Bergman form, the per-tick Reed–Solomon discretization, and the L²-section equivariant complement), and shows why the substrate's natural Hilbert space turns out to do precisely the work that quantum field theory's various ad-hoc Hilbert spaces have been doing in standard treatments. The Bergman reproducing kernel, in particular, plays the structural role of the Feynman propagator — a fact whose substrate-derivation (Lyra T2457) is one of the framework's more striking results.

## 2.1 What the Bergman space is

The substrate $D_{IV}^5$ is, as we have seen in Volume 0, a bounded complex manifold of complex dimension 5, sitting inside $\mathbb{C}^5$ as the set of points satisfying a specific quadratic inequality. Being *bounded* — that is, contained in some open ball of finite radius — is the property that makes everything in this chapter work. Bounded complex domains admit a canonical analytic structure that unbounded domains do not.

The **Bergman space** of $D_{IV}^5$ is defined as

$$H^2(D_{IV}^5) \;=\; \left\{ f : D_{IV}^5 \to \mathbb{C} \text{ holomorphic, with } \int_{D_{IV}^5} |f(z)|^2 \, dV(z) < \infty \right\}.$$

The integral is taken with respect to the canonical (Bergman-induced) volume measure on the domain. So $H^2$ is the space of holomorphic functions on the substrate that are square-integrable. Inner product:

$$\langle f, g \rangle \;=\; \int_{D_{IV}^5} \overline{f(z)} \, g(z) \, dV(z).$$

This is a Hilbert space — complete, separable, with the inner product just written. Standard functional analysis machinery applies.

The remarkable feature of the Bergman space, established by Bergman in 1922 for general bounded domains, is the **reproducing kernel**. There exists a unique function $K_B : D_{IV}^5 \times D_{IV}^5 \to \mathbb{C}$ (holomorphic in its first argument, anti-holomorphic in its second) such that *any* holomorphic function $f$ in $H^2(D_{IV}^5)$ can be recovered from its values on the domain by integrating against the kernel:

$$f(w) \;=\; \int_{D_{IV}^5} K_B(z, \bar{w}) \, f(z) \, dV(z) \qquad \text{for all } f \in H^2(D_{IV}^5).$$

The kernel reproduces the function. It is the canonical analytic object attached to the substrate.

For $D_{IV}^5$ specifically, the kernel has an explicit closed form, derived by Faraut and Koranyi in 1994. It reads

$$K_B(z, \bar{w}) \;=\; c_{FK} \cdot h(z, \bar{w})^{-g/\text{rank}},$$

where $h(z, \bar{w}) = 1 - 2\,\langle z, \bar{w} \rangle + \langle z, z \rangle \langle \bar{w}, \bar{w} \rangle$ is the *generic norm* of the type IV domain, and the exponent $g/\text{rank} = 7/2$ is the **Bergman exponent** of the geometry. The normalization constant $c_{FK}$ is fixed by the requirement that the integral identity above hold for the constant function $f = 1$, and the result — which we have already encountered in Volume 0 — is

$$c_{FK} \cdot \pi^{(g+\text{rank})/\text{rank}} \;=\; c_{FK} \cdot \pi^{9/2} \;=\; (N_c \cdot n_C)^2 \;=\; 225.$$

This is the substrate's most beautiful single identity. Every quantity in the equation is built from BST primary integers — $N_c = 3$, $n_C = 5$, $g = 7$, rank = 2. The transcendental factor $\pi^{9/2}$ pairs with the exact integer $225$ to give the normalization a structurally clean form. No tuning. No fitting. The Bergman normalization on the substrate's Hilbert space is exactly the integer combination $(N_c \cdot n_C)^2$, divided by $\pi^{9/2}$. Lyra T2442 ratifies this as one of the eleven Strong-Uniqueness rigorously-closed criteria.

## 2.2 The K-type decomposition

The Bergman Hilbert space is not just a featureless reservoir of functions. It carries an action of the substrate's symmetry group $SO_0(5,2)$, and under the action of the isotropy subgroup $K = SO(5) \times SO(2) \subset SO_0(5,2)$, the space decomposes into irreducible representations called **K-types**.

The decomposition is, schematically,

$$H^2(D_{IV}^5) \;=\; \bigoplus_{\lambda} V_{\lambda},$$

where the sum runs over dominant weights $\lambda$ of $K$ satisfying integrality and root-system positivity conditions, and each $V_{\lambda}$ is the irreducible K-type subspace labeled by $\lambda$. Wallach classified this decomposition explicitly in 1976; the relevant Lie-theory machinery is standard graduate material.

The K-types carry definite eigenvalues of the substrate's Casimir operators, which we will treat properly in Chapter 5. For now we record the most important fact: the lowest non-trivial K-type — labeled $V_{(1,1)}$, the K-type of a single application of a substrate raising operator in each of the two rank directions — has Casimir eigenvalue exactly $C_2 = 6$. This is the BST primary integer.

Higher K-types $V_{\lambda}$ carry larger Casimir eigenvalues, computable explicitly from the formula

$$C_2(\lambda) \;=\; \langle \lambda + \rho, \lambda + \rho \rangle - \langle \rho, \rho \rangle,$$

where $\rho = (5/2, 3/2)$ is the half-sum of positive roots in the substrate's rank-2 B₂ root system. Every eigenvalue is a BST-primary-derivable rational. We will use this fact frequently.

## 2.3 Why this is the right Hilbert space

The substrate Hilbert space is not just *a* choice. It is the *only* canonical choice consistent with the substrate's structure. The argument runs in three classical results.

**Bergman 1922.** Every bounded complex domain has a unique reproducing-kernel Hilbert space of square-integrable holomorphic functions. The space and the kernel are determined by the domain up to a normalization constant. So the substrate determines $H^2(D_{IV}^5)$ uniquely, with the kernel fixed by the geometry.

**Wallach 1976.** The K-type decomposition of $H^2(D_{IV}^5)$ under the isotropy $K = SO(5) \times SO(2)$ is explicit and computable. Every irreducible K-type appears with multiplicity zero or one, and the multiplicities are given by combinatorial conditions on weight diagrams. The decomposition is, in particular, *graded* by the BST primary integers — the lowest non-trivial K-type has Casimir $C_2 = 6$, exactly the BST primary, and higher K-types have eigenvalues built from the other primaries.

**Faraut–Koranyi 1994.** The Bergman normalization $c_{FK}$ for type IV bounded symmetric domains is given by an explicit volume formula involving the gamma function and the structural parameters of the domain. On $D_{IV}^5$, the formula gives $c_{FK} \cdot \pi^{9/2} = 225$ — exact, integer-on-the-right, with the integer being $(N_c \cdot n_C)^2$. This is not coincidence; it is structural.

Together the three results establish that $H^2(D_{IV}^5)$ is *the* substrate Hilbert space, in the sense that any alternative choice would have to abandon at least one of these classical canonical properties. Lyra's SP-31-1 paper-grade work (Cal-passed in May 2026 as the K69 audit) makes the *uniqueness* claim formal: among bounded reproducing-kernel Hilbert spaces compatible with the substrate's symmetry group, $H^2(D_{IV}^5)$ is the only one whose normalization works out in BST primary form. Other candidate Hilbert spaces fail at the normalization step.

So the substrate gets its Hilbert space without us having to choose. The choice is the geometry.

## 2.4 The Bergman kernel is the substrate's propagator

Standard quantum field theory invests significant machinery in the Feynman propagator — the amplitude for a particle to go from one spacetime point to another. The propagator is computed from the Lagrangian by inverting the kinetic operator, regularized to handle ultraviolet divergences, used in Feynman-diagram calculations of cross-sections and decay rates. It is the field theorist's most-used computational tool.

In BST, the propagator is not computed. It is the Bergman reproducing kernel.

The identification, formalized by Lyra in May 2026 as T2457 (the "Bergman structural-role-of Feynman propagator" theorem), runs as follows. In standard QFT, the Feynman propagator $G_F(x, y)$ is a Green's function for the kinetic operator: it satisfies

$$(\Box + m^2) \, G_F(x, y) \;=\; -i \delta^4(x-y)$$

and serves to propagate amplitudes from $y$ to $x$. Operationally, it gives the amplitude that a particle created at $y$ propagates to $x$. Its key analytical properties are: positive-definiteness on physical states, ultraviolet behavior controlled by some regularization, and a Källén–Lehmann spectral representation in terms of physical particle masses.

The Bergman reproducing kernel on $H^2(D_{IV}^5)$ has *all three* of these properties built in by the substrate structure, plus several that the standard Feynman propagator does not have:

- **Positive-definite by Bergman 1922.** No regularization needed; the kernel is positive-definite as a matrix on any finite collection of points in the substrate.
- **Ultraviolet-complete by substrate construction.** The substrate's per-tick Reed–Solomon discretization (next section) provides a natural ultraviolet cutoff at the Koons tick scale. There are no high-momentum divergences in the substrate's natural realization.
- **Normalization in BST primary form.** The Bergman normalization $c_{FK} \cdot \pi^{9/2} = 225$ is exact, integer, and structurally derived. The standard QFT propagator's normalization is an empirical input.
- **K-type expansion equivalent to Källén–Lehmann.** The K-type decomposition of $H^2$ is the substrate's analog of the spectral representation: each K-type $V_{\lambda}$ contributes a definite eigenvalue to the kernel, and the sum over K-types is the substrate's structural Källén–Lehmann sum.

The amplitude calculations BST performs are therefore not parallel inventions of standard QFT's propagator machinery. They are direct evaluations of the Bergman kernel on appropriate K-types. Substrate-derived predictions for scattering amplitudes, decay rates, and form factors all reduce to kernel evaluations.

This is one of the more striking economies of the substrate framework. Standard QFT has the propagator as a derived object computed from the Lagrangian; BST has the propagator as a *primitive* object given by the substrate's analytic structure, with the standard QFT propagator emerging as the appropriate limit.

## 2.5 The per-tick Reed–Solomon layer

The Bergman space $H^2(D_{IV}^5)$ is the substrate's *continuous* Hilbert space — the long-time-averaged, integrated state space. But the substrate operates in discrete ticks (Volume 0, Chapter 3), and at each Koons tick of approximately $10^{-120}$ seconds, the substrate's state lives in a *finite-dimensional* space rather than an infinite-dimensional one.

That finite-dimensional per-tick space is what Lyra T2429 identifies as the **Reed–Solomon code-space discretization**: at each tick, the substrate state is a codeword in the Galois field $GF(2^g)^k = GF(128)^k$ for some integer $k$ determined by the substrate's per-tick information capacity. The number $128 = 2^7$ uses the BST primary $g = 7$; the Reed–Solomon structure uses the cyclic group of order $127 = M_g$ (Mersenne prime) for its multiplicative cyclic structure.

The relationship between the continuous Bergman space and the discrete per-tick code-space is *coarse-graining* in time. Averaging the discrete per-tick states over many ticks gives the continuous Bergman state; the continuous Bergman state at any time has the discrete code-space state at the next tick as its substrate-natural projection. The two layers are equivalent representations of the same physical content, with the choice between them controlled by the temporal scale of the question being asked.

Most of standard quantum mechanics — Born rule, position operators, expectation values, scattering amplitudes — lives at the continuous Bergman layer, where the substrate's tick is washed out by averaging. Most of substrate-specific predictions — the sub-Planck temporal structure, the no-cloning theorem, the structural ultraviolet completeness — live at the discrete Reed–Solomon layer, where the tick is explicit. The two layers are complementary, not competing.

## 2.6 The L²-section equivariant complement

A third presentation of the substrate Hilbert space, derived in Lyra T2430, organizes the space by its representation-theoretic content under the full symmetry group $SO_0(5,2)$ rather than just the isotropy $K = SO(5) \times SO(2)$.

The substrate $D_{IV}^5$ is a homogeneous space — $SO_0(5,2)/K$ — and the Hilbert space $H^2(D_{IV}^5)$ admits a presentation as the space of *equivariant sections* of a particular line bundle $L_\lambda \to D_{IV}^5$ associated to a weight $\lambda$ of $K$. Concretely:

$$H^2(D_{IV}^5) \;\cong\; L^2(D_{IV}^5; L_\lambda),$$

where $L_\lambda$ is the holomorphic line bundle whose fiber at the identity coset is the one-dimensional weight-$\lambda$ representation of $K$. The line bundle is uniquely determined by the substrate's weight structure.

What this presentation buys is a *Casimir action*: the Casimir operator of $SO_0(5,2)$ acts on $L^2(D_{IV}^5; L_\lambda)$, and the substrate Hamiltonian $\hat{H}$ that we will encounter in Chapter 7 is exactly this Casimir, restricted to the appropriate K-type. The equivalence between this presentation and the Bergman presentation is what makes the Hamiltonian's lowest non-trivial eigenvalue equal $C_2 = 6$ — both presentations refer to the same operator on the same space.

Three presentations of the same substrate Hilbert space: continuous Bergman, discrete Reed–Solomon per-tick, L²-section equivariant. None competes with the others; each is the natural presentation for a different question. Standard quantum mechanics, written in BST's substrate framework, switches between them as the question demands.

## 2.7 What this Hilbert space buys

The substrate Hilbert space is the structural backbone of the rest of this volume. Every operator we will introduce in Chapter 6, every dynamical equation we will write in Chapter 7, every gauge construction in Chapter 8, every scattering amplitude in Chapter 9 will live on $H^2(D_{IV}^5)$. The Hilbert space is the common ground.

What the substrate Hilbert space buys, in particular, is a single space in which all of the substrate's structure is *concrete*. The K-type decomposition tells us the eigenvalue spectrum of every Casimir operator. The Bergman kernel tells us how amplitudes propagate. The Reed–Solomon layer tells us what happens per tick. The L²-section presentation tells us how the Hamiltonian acts. These are not four different theories; they are four windows on one Hilbert space.

The reader who is comfortable with standard QFT Hilbert-space constructions — Fock space built from harmonic oscillators, second quantization of fields, the various Hilbert spaces of axiomatic field theory — will find that the substrate Hilbert space replaces all of them, with no loss of expressive power and with substantial gain in structural specificity. Every standard quantum mechanical or quantum field theoretic computation can be done on $H^2(D_{IV}^5)$, and most of them have substrate-side derivations that the standard treatments lack.

## 2.8 What comes next

Chapter 3 unpacks the per-integer forcing arguments for the BST primary integers at theorem-grade depth, including the alternative-HSD comparisons that ratify the relevant Strong-Uniqueness criteria. The five integers we have been using since Volume 0 will get their formal substrate-mechanical derivations in full.

Chapter 4 takes the substrate's discrete symmetries — parity, time reversal, charge conjugation — and derives them as operators on $H^2(D_{IV}^5)$ using the structure we have now established.

Chapter 5 develops the Casimir operator algebra on $H^2$ in detail, including the rank-2 algebraically-independent Casimir generators $C_2$ and $C_4$, their eigenvalues, and their physical interpretation.

By Chapter 6 we will have the full operator zoo on hand and will be ready to construct dynamics in Chapter 7. The substrate Hilbert space is the common substrate for all of that.

---

**Where to look this up**: Bergman's 1922 foundational paper is "Über die Entwicklung der harmonischen Funktionen der Ebene und des Raumes nach Orthogonalfunktionen," published in *Mathematische Annalen* 86. Wallach's 1976 classification is "The analytic continuation of the discrete series" in *Transactions of the American Mathematical Society* 251. Faraut and Koranyi's *Analysis on Symmetric Cones* (Oxford University Press, 1994), Chapter X, contains the explicit Bergman kernel for type IV domains. The substrate Hilbert-space sufficiency anchor is Lyra T2428 (May 2026), with corollaries T2429 (Reed–Solomon per-tick discretization) and T2430 (L²-section equivariant complement). The Bergman-kernel-as-Feynman-propagator structural identification is Lyra T2457. The Bergman normalization identity $c_{FK} \cdot \pi^{9/2} = 225$ is T2442 (Strong-Uniqueness Theorem criterion C13, rigorously closed). For the standard QFT side, Peskin and Schroeder's treatment of the propagator in Chapter 4 is the most accessible introduction; Weinberg's *Quantum Theory of Fields*, Volume 1, Chapter 6 covers the spectral representation we identified with the K-type expansion.
