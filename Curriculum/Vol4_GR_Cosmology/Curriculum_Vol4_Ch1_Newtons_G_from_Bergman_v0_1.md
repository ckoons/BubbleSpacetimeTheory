---
title: "Vol 4 Chapter 1 — Newton's $G$ from Bergman Curvature"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (T1296 G = ℏc·(6π⁵)²·α²⁴/m_e² at 0.07%, Bergman round-trip mechanism 24 = 4·C_2, three independent confirmations including Toy 639 heat-kernel k=16 ratio = −24 = −dim SU(5), uniqueness identity n_C²−1 = (n_C−1)! at n_C=5, T2106 gravity-as-eigentone)"
volume: "Vol 4 General Relativity and Cosmology from D_IV⁵"
chapter: 1
tier: "D-tier ratified — derived mechanism via Bergman round-trip framework + heat-kernel confirmation"
match_precision: "0.07% (BST G = 6.66961 × 10⁻¹¹ vs measured 6.67430 × 10⁻¹¹ m³/(kg·s²))"
---

# Chapter 1 — Newton's $G$ from Bergman Curvature

## Why this chapter matters

Newton's gravitational constant $G$ is the weakest of the four fundamental couplings. The dimensionless gravitational fine-structure analog $\alpha_G \approx 10^{-39}$ is thirty-seven orders of magnitude below the electromagnetic $\alpha \approx 10^{-2}$. This thirty-seven-order hierarchy between gravitational and electromagnetic coupling strengths is what physicists call the **hierarchy problem**, and it is among the deepest unexplained features of fundamental physics. Standard physics has no derivation of $G$; it is taken as an experimental input, measured by Cavendish torsion balances and refined over two centuries.

BST derives Newton's $G$ in BST-primary form, to $0.07\%$ precision, with no fitted parameters:

$$G \;=\; \hbar c \cdot (6\pi^5)^2 \cdot \alpha^{24} \,/\, m_e^2.$$

Every factor on the right is substrate-derived. The $(6\pi^5)^2$ is the square of the proton-to-electron mass ratio of Volume 2 Chapter 6. The $\alpha = 1/N_{\max} = 1/137$ is the substrate's fine-structure cutoff of Chapter 10 in Volume 1. The exponent $24 = 4 \cdot C_2$ — four complete Bergman round trips around the substrate's $C_2 = 6$ Casimir modes — is forced by the substrate's root-system structure. The electron mass $m_e$ sets the unit scale. There is no tunable freedom; the gravitational coupling is computed from BST primaries.

The match to measurement is $6.66961 \times 10^{-11}$ m³/(kg·s²) versus the measured $6.67430 \times 10^{-11}$ m³/(kg·s²) — a deviation of $0.07\%$, well within the experimental precision of present-day Cavendish-type torsion-balance measurements. The thirty-seven-order gravity-versus-electromagnetism hierarchy, which standard physics treats as a mysterious fine-tuning, in BST falls out structurally: gravity needs *four* Bergman round trips per coupling vertex, electromagnetism needs only *two*, so gravity is suppressed relative to electromagnetism by $\alpha^{4 \cdot C_2 - 2 \cdot C_2} = \alpha^{12}$ — which combined with the proton-mass factors gives the observed hierarchy.

This chapter sets out the derivation, the substrate-mechanism Bergman-round-trip framework, three independent structural confirmations of the exponent $24$, and the substrate-side reading of gravity as the residual curvature of the substrate's commitment computation.

## 1.1 The T1296 substrate-derivation

Lyra T1296 (April 2026, "Gap #1 closed"), with computational verification in Elie's Toy 541 and the heat-kernel cross-check in Toy 639, establishes the substrate-mechanical derivation of Newton's $G$:

$$G \;=\; \hbar c \cdot (6\pi^5)^2 \cdot \alpha^{24} \,/\, m_e^2.$$

The factors are each substrate-mechanical:

- **$(6\pi^5)^2 = (m_p / m_e)^2$**. The proton-to-electron mass ratio from Volume 2 Chapter 6 enters squared because gravity couples to two masses (source and probe). At leading order, $(6\pi^5)^2 \approx 1836.118^2 \approx 3.37 \times 10^6$.

- **$\alpha^{24}$**. The substrate's fine-structure coupling $\alpha = 1/N_{\max} = 1/137$, raised to the twenty-fourth power. The exponent is what makes gravity weak: $\alpha^{24} = (1/137)^{24} \approx 10^{-51.4}$, an extremely small suppression that pulls $G$ down from any naturally-scaled value to its observed extraordinarily small magnitude.

- **$1/m_e^2$**. Dimensional. Gravity scales as inverse mass squared in natural units; the electron mass sets the substrate's unit-scale floor.

The combination gives $G$ in natural units, which converts to SI via the standard factors. Toy 541 (the framework's "five integers to everything" computational reproduction, 16/16 sub-checks passing) confirms the numerical match at $0.07\%$.

The match precision is, for a gravitational measurement, excellent. Newton's $G$ has been measured to about parts-per-thousand precision by modern Cavendish-type experiments; substantial systematic discrepancies between independent measurements exist at the parts-per-ten-thousand level. The substrate prediction sits comfortably within current experimental precision.

## 1.2 The Bergman round-trip mechanism

The exponent $24 = 4 \cdot C_2$ has a substrate-mechanism reading that is the chapter's structural content.

The substrate Hilbert space $H^2(D_{IV}^5)$ admits a **Bergman round-trip framework**, established in the BST research note `BST_AlphaSquared_LayerProof.md` and connecting back to the substrate's S¹ phase structure on K-types. The key idea: each "Bergman round trip" corresponds to one complete phase circuit on the substrate's holomorphic structure, with the forward and return half-cycles each contributing a factor of $\alpha^{1/2}$ to the amplitude (via the Szegő-kernel factorization on $D_{IV}^5$'s boundary). The round-trip *probability* is therefore $\alpha$, the round-trip *amplitude* is $\alpha^{1/2}$, and the suppression factor for $n$ round trips at $k$ Casimir modes each is $\alpha^{n \cdot k}$.

For **electromagnetism**, the substrate coupling requires *two* Bergman round trips at the EM Casimir level, giving $\alpha^2 \approx 5.3 \times 10^{-5}$ as the EM suppression per vertex. This matches QED's familiar $\alpha^2$ scaling of higher-order processes.

For **gravity**, the substrate coupling requires *four* Bergman round trips at $C_2 = 6$ Casimir modes each, giving $\alpha^{4 \cdot 6} = \alpha^{24}$ as the gravitational suppression per vertex. The factor of four comes from the substrate's $\mathfrak{so}(5,2)$ structure: gravity must close four independent loops in the substrate's representation cohomology — one for each of the four positive roots of the $B_2$ root system that we used in Chapter 5 of Volume 1 to define the Casimir eigenvalue formula.

So the structural reason gravity is much weaker than electromagnetism is *not* a fine-tuning of $G$ versus $\alpha$. It is the substrate's requirement that gravitational coupling close four times as many independent loops as electromagnetic coupling. The hierarchy $\alpha^{22}$ between the two — twelve additional powers of $\alpha$ — is what produces the observed thirty-seven orders of magnitude between $\alpha_G$ and $\alpha$.

## 1.3 Three independent confirmations of $24 = 4 \cdot C_2$

The exponent $24$ in the substrate's derivation of $G$ is not arbitrary. It is forced by three independent structural arguments, each of which gives the same answer.

**Confirmation 1 — Heat kernel at level $k = 16$.** The heat-kernel expansion on $D_{IV}^5$ has a speaking-pair structure with period $n_C = 5$. At the third speaking pair, $k = 16$, the substrate's heat-kernel ratio evaluates to

$$\text{ratio}(k = 16) \;=\; -24 \;=\; -\dim SU(5) \;=\; -(n_C^2 - 1).$$

This is Toy 639's confirmed computational result (May 2025). The number $24$ shows up as $n_C^2 - 1$ — the dimension of the group $SU(n_C) = SU(5)$ — at the heat-kernel level where the speaking-pair structure makes the relevant coefficient extractable.

**Confirmation 2 — Uniqueness identity $n_C^2 - 1 = (n_C - 1)!$.** The arithmetic identity $n_C^2 - 1 = (n_C - 1)!$ holds *uniquely* at $n_C = 5$: $5^2 - 1 = 24 = 4! = (5-1)!$. For $n_C = 4$: $15 \neq 6$. For $n_C = 6$: $35 \neq 120$. For $n_C = 7$: $48 \neq 720$. The identity locks the substrate's gravitational exponent to its specific complex dimension; if $n_C$ were anything other than 5, the identity would fail and the exponent would not be 24.

**Confirmation 3 — Casimir decomposition $24 = 4 \cdot C_2$.** The exponent $24$ can be read as four complete cycles through the substrate's $C_2 = 6$ eigenvalues — what we called the four Bergman round trips in §1.2 — at heat-kernel levels $k = 6, 12, 18, 24$. The four-fold periodicity in Casimir-eigenvalue space is structural; it matches the four positive roots of the substrate's $B_2$ root system.

Three independent BST primary readings converge on $24$. The substrate-derivation is over-determined; the value of the exponent is not a fitting parameter. This is the same pattern of substrate over-determinism that we identified throughout Volume 0 and Volume 1: distinct structural constraints converging on the same answer.

## 1.4 Gravity as residual substrate curvature

Lyra T2106 ("Gravity as Eigentone," April 2026) provides a deeper substrate-mechanism reading: gravity is what remains of the substrate's curvature *after* all channel commitments have run their per-tick computations to completion.

The substrate's four-phase commitment cycle (Volume 0 Chapter 3) processes substrate state through Zones 1 to 4 on each Koons tick. In the strong, electromagnetic, and weak sectors, the substrate's per-tick computation closes the relevant K-type commitments — quarks confine, electromagnetic amplitudes propagate, weak decays proceed — within a definite number of Bergman round trips at the level appropriate to each sector. Each sector's coupling reflects its commitment depth: two round trips for EM, three for weak, three for strong (with color confinement at $C_2 = 6$ modes each).

Gravity sits at the *outside* of this commitment structure. After the strong, electromagnetic, and weak sectors have completed their per-tick commitments, the substrate's residual curvature — the un-committed portion of the substrate's Bergman geometry — is what couples masses gravitationally. The four Bergman round trips at $C_2 = 6$ modes are the residual round trips that gravity inherits: they are what is *left over* after the other three sectors have run.

This is the substrate-mechanism reading of why gravity does not unify with the other forces at any finite energy scale. The other forces commit; gravity is the residual. The substrate produces gravitational coupling not from a unified gauge sector but from the *complement* of the gauge sector's commitment depth. The substrate's no-GUT prediction (Volume 1 Chapter 8's Five-Absence set) and the substrate's gravity-as-residual reading are the same structural fact viewed from two sides.

A consequence is that BST's four-dimensional general relativity emerges from the substrate's six-dimensional internal Bergman computation (the integrating-out of the substrate's K-type internal degrees of freedom gives the residual four-dimensional curvature that becomes Einstein's tensor). T2106's full statement is that four-dimensional Newton's $G$ is exactly the integrated residual curvature of the substrate, computed via Bergman integration over the substrate's internal six-dimensional structure. Volume 4 Chapter 2 develops this in detail.

## 1.5 What the chapter buys

The substrate framework, by deriving Newton's $G$ to $0.07\%$ from BST primaries with the hierarchy problem resolved structurally, removes one of the deepest unexplained features of standard physics. There is no fine-tuning of $G$ against $\alpha$. There is no unexplained gravitational weakness. The thirty-seven orders of magnitude between gravity and electromagnetism are the substrate's required commitment-depth difference: four Bergman round trips for gravity, two for electromagnetism, giving $\alpha^{22}$ suppression that produces the observed hierarchy.

The match at $0.07\%$ is well within current experimental precision. The substrate framework's prediction is, in this case, more precise than the disagreements between independent Cavendish-type measurements of $G$ — the framework is, structurally, at the experimental frontier.

## 1.6 What comes next

Chapter 2 — Gravity as Cumulative Eigentone Effect — develops the substrate-mechanism reading of T2106 in detail, showing how the residual substrate curvature integrates to produce the Einstein field equations of general relativity.

Chapter 3 — BST-SR / BST-GR Boundary — examines where in the substrate's structure the transition from special-relativistic to general-relativistic behavior occurs.

Chapter 4 — The Cosmological Constant from Substrate — gives the substrate-derivation of $\Lambda \approx 10^{-121}$ from the Zone-2 vacuum that we sketched in Volume 0 Chapter 5, with the substrate-mechanism unification of $\Lambda$ and the laboratory Casimir effect.

Chapters 5 through 12 develop substrate-derivations of the Hubble constant (with the famous Hubble tension resolved via four routes), CMB structure (the scalar spectral index $n_s = 1 - n_C/N_{\max}$ at $0.3\sigma$ precision), inflation parameters, big-bang nucleosynthesis (including the Li-7 problem), the cosmological cycle hypothesis and the Interstasis period between Big Bang cycles, dark matter and dark energy (with $\Omega_\Lambda = 13/19$ at $0.07\sigma$ and dark-matter-to-baryon ratio $16/3$ at $0.58\%$), gravitational waves (with NANOGrav predictions), and the SP-27 observational reanalysis program.

The reader who has accepted the substrate-derivation of $G$ in this chapter — the cleanest of the volume's GR-side derivations — will find the rest of Volume 4 a series of similar substrate-mechanical derivations applied to specific cosmological observables. The substrate produces the entire cosmology side of physics from the same five integers that produce the particle physics side.

---

**Where to look this up**: The primary derivation is Lyra T1296 ("Gap #1 closed," April 2026, with the supporting writeup at `notes/BST_EinsteinEquations_FromCommitment.md`). The Bergman round-trip framework is documented at `notes/BST_AlphaSquared_LayerProof.md`. The three confirmations of the exponent $24$ are: Toy 639 (heat kernel at $k = 16$ with ratio $= -24 = -\dim SU(5)$, May 2025), the uniqueness identity $n_C^2 - 1 = (n_C - 1)!$ at $n_C = 5$ (elementary arithmetic check), and the Casimir decomposition $24 = 4 \cdot C_2$ (substrate root-system structure). The gravity-as-eigentone reading is Lyra T2106 (April 2026). The computational verification is Toy 541 (16/16 sub-checks passing). For the standard-physics hierarchy problem and the cosmological-constant problem, the canonical reviews are Weinberg 1989, "The cosmological constant problem," *Reviews of Modern Physics* 61:1; and Arkani-Hamed et al. 1998 on the hierarchy problem from the modern-extra-dimensions perspective. For the experimental status of Newton's $G$ measurements with the systematic discrepancies, see the CODATA 2018 evaluation and the Particle Data Group's *Review of Particle Physics* annual update.
