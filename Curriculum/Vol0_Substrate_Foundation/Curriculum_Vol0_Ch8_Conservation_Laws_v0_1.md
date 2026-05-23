---
title: "Vol 0 Chapter 8 — Conservation Laws"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (Noether-on-substrate framing, 10 continuous + 5 discrete conservation laws derived from substrate symmetries, SP-31-#279 T2473/T2474/T2475 substrate-derivation theorems for energy/momentum/charge, weak-sector uniqueness of P/C/T violation, CPT preservation from common SO_0(5,2) origin)"
volume: "Vol 0 Substrate Foundation"
chapter: 8
---

# Chapter 8 — Conservation Laws

Conservation laws are the bones of physics. Energy doesn't disappear. Momentum carries through collisions. Electric charge cannot be created or destroyed. Angular momentum stays put when no torque acts. Without these laws very little of the rest of physics would be tractable, and historically they were taken as foundational — the deep facts on which everything else rested.

Emmy Noether's 1918 theorem made it possible to see that the laws were not foundational but *consequential*. Every continuous symmetry of a physical system corresponds to a conservation law: time-translation symmetry to conservation of energy, spatial-translation symmetry to conservation of momentum, rotational symmetry to conservation of angular momentum, and so on. Conservation laws stopped being mysteries and became reflections of symmetries.

BST takes the next step. The substrate $D_{IV}^5$ has a *specific* symmetry structure — the $SO_0(5,2)$ Lie group of Chapter 1, the isotropy decomposition $SO(5) \times SO(2)$ plus the Möbius involution of Chapter 4, the commitment-cycle structure of Chapter 3, and the Reed–Solomon discretization of Chapter 3 — and every standard-physics conservation law is the Noether translation of one of those symmetries. There are no separate postulates. The substrate produces the symmetries; Noether produces the laws.

This chapter applies the Noether procedure across the substrate's full symmetry inventory and inventories the resulting conservation laws. There are about fifteen of them. We will not need all the detail in this volume — most laws appear in later volumes where the corresponding physics is treated — but it is useful to see the full picture once.

## 8.1 Noether on the substrate

The standard formulation of Noether's theorem says: if a Lagrangian or a Hamiltonian is invariant under a continuous symmetry group $G$, then there is a conserved current (and a conserved charge) for each independent generator of $G$. The proof is short; the operational content is that one identifies the symmetry, identifies the generator, identifies the operator, and reads off the conservation law.

BST's version of the procedure runs in the substrate setting:

1. **Identify a continuous symmetry** of the substrate Hilbert space $H^2(D_{IV}^5)$ that preserves the substrate Hamiltonian (Chapter 7's $\hat{H}$). This is a one-parameter subgroup of $SO_0(5,2)$ that commutes with $\hat{H}$.

2. **Identify the infinitesimal generator** $\hat{T}_G$ of the subgroup. By construction, $[\hat{T}_G, \hat{H}] = 0$.

3. **Read off the conservation law**. The expectation value $\langle \hat{T}_G \rangle$ is time-independent under substrate dynamics. This is the conserved quantity.

4. **Identify it with a standard-physics conservation law.** The correspondence is one-to-one across the substrate's full symmetry group.

For *discrete* symmetries — parity, time reversal, charge conjugation — the procedure is slightly modified. Instead of a one-parameter subgroup we have an involution $\sigma$ ($\sigma^2 = 1$). If $\sigma$ commutes with $\hat{H}$, eigenstates of $\sigma$ carry a conserved discrete quantum number (eigenvalues $\pm 1$). If $\sigma$ does not commute, the corresponding discrete symmetry is *violated*, and the substrate's structure tells us where and why.

We will use both procedures in this chapter.

## 8.2 The continuous laws

The ten standard continuous conservation laws of physics are each Noether-derived from a substrate symmetry. We list them with the symmetry of origin and the operator (from the zoo of Chapter 7) that they conserve.

**Energy** is conserved because the substrate Hamiltonian is time-translation-invariant. The generator is $\hat{H}$ itself; the conserved quantity is its expectation value. The substrate's Koons tick of Chapter 3 provides the natural temporal granularity, and the lowest non-trivial energy eigenvalue is $C_2 = 6$ in substrate-natural units. (Lyra T2473 documents the formal substrate-derivation.)

**Linear momentum** is conserved because the substrate is invariant under translations along the coset directions of $\mathfrak{so}(5,2)$. There are ten such directions (the dimension of the coset $\mathfrak{m}$ that we counted in Chapter 4), each producing one component of momentum. The conserved operator is $\hat{P}$ from the zoo. (Lyra T2474.)

**Angular momentum** is conserved because the substrate is invariant under the $SO(5)$ rotations of the isotropy. Ten rotation generators produce ten components, of which three — the $SO(3) \subset SO(5)$ rotations of the physical spatial dimensions — match the angular momentum of laboratory physics. The conserved operator is $\hat{L}$ (orbital) plus $\hat{S}$ (spin), with total $\hat{J} = \hat{L} + \hat{S}$.

**Electric charge** is conserved because the substrate is invariant under the $SO(2)$ phase rotation of the isotropy. The conserved operator is $\hat{Q}$. The quantization in units of $1/N_c$ for color-bearing states (the $\pm 1/3, \pm 2/3$ of quarks) versus integer units for non-color states is a structural feature of the $SO(2)$ representation theory acting on the $N_c$-fold sub-substrate. (Lyra T2475.)

**Color charge** is conserved because the substrate carries an $SU(N_c) = SU(3)$ symmetry from the $N_c = 3$ sub-structure of color-bearing K-types. Eight generators of $SU(3)$ produce eight color-conservation laws. The combination with the trefoil-confinement topology of Casey's W-23 work means that color-bearing degrees of freedom never appear in isolation — color is conserved *and* confined, two facts derived from the same substrate structure.

**Weak isospin** is conserved because the substrate carries an $SU(2)$ symmetry from the rank-2 doublet structure. Three generators give three components of weak isospin.

**Hypercharge $Y$** is conserved as the unbroken combination of $SO(2)$ and weak isospin after the Weinberg electroweak mixing. Volume 2 treats this in detail.

**Lepton number $L$** and **baryon number $B$** are conserved as global $U(1)$ symmetries on the substrate's K-type structure. Lepton number counts substrate cycles in the lepton K-types; baryon number counts cycles in the baryon K-types. Casey's W-31 "asymmetric ontology" work places leptons as a substrate residue class and baryons as the substrate primary class. Both conservation laws are exact in BST — the framework's **Five-Absence prediction set** explicitly forbids proton decay, in agreement with experimental upper limits on the proton lifetime of $\sim 10^{34}$ years.

**Probability** is conserved because substrate dynamics are unitary on $H^2(D_{IV}^5)$. The Bergman-kernel projector (Chapter 3) is, when correctly interpreted via the K67 audit-ratified Born=Bergman result, the substrate-side implementation of the Born rule for probability conservation. Standard quantum mechanics treats unitarity as an axiom; BST derives it from the substrate's Bergman geometry.

Ten continuous conservation laws, ten substrate symmetries, one Noether correspondence applied uniformly. None of the laws is independently postulated; each is the Noether translation of a specific feature of $D_{IV}^5$'s symmetry group.

## 8.3 The discrete laws

The discrete conservation laws — parity, time reversal, charge conjugation, the CPT theorem, and information conservation — each correspond to a substrate involution. Some are conserved across all sectors; some are conserved in some sectors and violated in others. The substrate tells us which.

**Parity ($\hat{P}$).** The Möbius involution of $D_{IV}^5$ (Chapter 4) lifts to an involution on the Hilbert space, which is the parity operator. It is conserved in the strong and electromagnetic sectors — $[\hat{P}, \hat{H}_{\text{strong}}] = [\hat{P}, \hat{H}_{\text{EM}}] = 0$ — but violated in the weak sector, because the weak Hamiltonian's chirality-asymmetric structure (the $SO(2)$ action on left-handed-doublet versus right-handed-singlet substrate states) does not commute with Möbius. This is the substrate-mechanism explanation for the parity violation that Wu's 1957 experiment discovered. Lyra T2472 gives the formal substrate-derivation; Chapter 4 sketched the structural argument.

**Time reversal ($\hat{T}$).** The substrate's commitment cycle has a definite direction — absorption, computation, commitment, emission — and reversing this direction defines an anti-unitary involution on the Hilbert space, which is time reversal. Lyra T2433 establishes the operator's substrate-derivation. It is conserved in the strong and electromagnetic sectors and violated in the weak sector, for the same reason parity is: the weak Hamiltonian's chirality asymmetry breaks the cycle-reversal symmetry. The experimental signature is CP violation in the neutral-kaon system (Cronin–Fitch, 1964) and similar effects in B mesons; the substrate-mechanism explanation is the same chirality asymmetry that gives parity violation.

**Charge conjugation ($\hat{C}$).** The $SO(2)$ weight-negation involution sends charge $Q$ to $-Q$. Lyra T2434 provides the substrate-derivation. It is conserved in strong and electromagnetic and violated in weak, again because of the chirality-asymmetric weak coupling.

**The CPT theorem.** This is one of the framework's most satisfying derivations. The composite involution $\hat{C}\hat{P}\hat{T}$ — charge conjugation times parity times time reversal — commutes with the substrate Hamiltonian in *every* sector, including the weak sector where the individual $\hat{P}$, $\hat{C}$, $\hat{T}$ each fail. The reason is structural: all three discrete violations in the weak sector originate from the same chirality coupling between $SO(2)$ phase and weak isospin doublet. When the composite is taken, the three asymmetries that each break one symmetry combine into the *identity* on the chirality coupling, and the Hamiltonian commutes with the composite as if no violation existed.

Stated differently: the CPT theorem holds in BST because the three discrete violations have a common substrate origin, and composing them returns to the substrate's natural symmetric configuration. The CPT theorem is therefore not coincidental cancellation but structural inevitability. Standard quantum field theory's CPT theorem (Lüders 1954, Pauli 1955) recovers this conclusion from a different set of axioms — Lorentz invariance, locality, spin-statistics, positivity of energy — but the substrate-derivation is more direct: CPT is built into the substrate's symmetry structure.

**Information conservation.** The Reed–Solomon code structure of the substrate's per-tick state (Chapter 3, K59-ratified cyclotomic mechanism) is preserved under unitary substrate dynamics. The substrate's information capacity, measured by the code-space dimension, is conserved. As a corollary, the no-cloning theorem of standard quantum mechanics follows from substrate structure: no operation on the substrate can duplicate an unknown code-space state, because doing so would require a non-unitary operation that violates the substrate's Bergman-kernel structure.

## 8.4 Why weak is the unique violator

A consequence of the substrate framework that bears on its experimental track record is its prediction that the **weak interaction is the unique sector where P, C, and T are individually violated**.

The structural reason is that four substrate asymmetries combine non-trivially only in the weak sector:

1. The rank-2 substrate doublet structure (Chapter 2's rank $= 2$),
2. Möbius locality (Chapter 4's parity origin),
3. The $SO(2)$ chiral phase action on spinors (Chapter 7's chirality),
4. The commitment-cycle directional asymmetry (Chapter 3's Zone-1-to-Zone-4 ordering).

The strong sector has $SU(3)$ cyclic structure but no Möbius locality and no chiral phase — strong interactions preserve P, C, T. The electromagnetic sector has $SO(2)$ cyclic structure that is invariant under all three involutions — electromagnetism preserves P, C, T. The weak sector is the unique location where all four asymmetries combine, and the result is individual violation of P, C, and T.

But — and this is the key — all four asymmetries originate from the *same* $SO_0(5,2)$ structure of the substrate. Their composite $\hat{C}\hat{P}\hat{T}$ therefore returns the substrate to its symmetric configuration. Hence CPT is universally conserved, even where individual P, C, T are not. Standard physics treats the weak sector's uniqueness as an experimental fact; BST shows it is a structural inevitability.

## 8.5 Operator-conservation correspondence

Each conservation law corresponds, by Noether's theorem and its discrete-symmetry extension, to an operator in the zoo of Chapter 7. The correspondence is one-to-one, and serves as the structural bridge between the inventory of Chapter 7 and the dynamics of Volume 1.

| Conservation law | Substrate symmetry | Conjugate operator | Sector validity |
|---|---|---|---|
| Energy | $SO_0(5,2)$ time-translation | $\hat{H}$ | All |
| Linear momentum | Coset translations $\mathfrak{m}$ | $\hat{P}$ | All |
| Angular momentum | $SO(5)$ rotations | $\hat{L}, \hat{S}$ | All |
| Electric charge | $SO(2)$ phase | $\hat{Q}$ | All |
| Color charge | $SU(3)$ from $N_c$ | $\hat{T}^a$ (8 of them) | All; confined |
| Weak isospin | $SU(2)$ from rank | $\hat{T}^i_w$ (3 of them) | All |
| Hypercharge | Unbroken Weinberg comb. | $\hat{Y}$ | All |
| Lepton number | $U(1)_L$ on K-types | $\hat{L}_{\text{lep}}$ | All |
| Baryon number | $U(1)_B$ on K-types | $\hat{B}$ | All (no proton decay) |
| Probability | Substrate unitarity | $\hat{1}$ (identity) | All |
| Parity | Möbius involution | $\hat{P}$ | Strong + EM only |
| Time reversal | Cycle reversal | $\hat{T}$ | Strong + EM only |
| Charge conjugation | $SO(2)$ negation | $\hat{C}$ | Strong + EM only |
| CPT | Composite involution | $\hat{C}\hat{P}\hat{T}$ | All |
| Information | RS code-space closure | (functional) | All |

The "sector validity" column records which conservation laws are universal and which fail in the weak sector. This is, again, the textbook prediction we just walked through.

## 8.6 Falsifiers

Each conservation law in this chapter is independently falsifiable. The experimental program of BST takes the form of looking for violations of the laws the framework derives — particularly violations that would distinguish the substrate's derivation from alternative theoretical frameworks.

A short list of the framework's strongest falsifiers, organized by which law they would refute:

- **Proton decay.** BST predicts no proton decay; an observed event would falsify baryon-number conservation and refute the substrate primary-class structure. Current experimental bounds place the proton lifetime above $10^{34}$ years.
- **Free quark observation.** Color confinement is structural in BST; an isolated quark in any experiment would refute the confining topology of W-16.
- **CPT violation.** The structural CPT result is the framework's deepest universal claim. The experimental precision tests of CPT — proton/antiproton mass differences at $10^{-18}$ precision, hydrogen/antihydrogen spectroscopy — are correspondingly the most stringent tests of BST's underlying $SO_0(5,2)$ structure. An observed CPT violation would refute the substrate framework at its foundation.
- **Parity, time-reversal, or charge-conjugation conservation in the weak sector.** Each of these is an active research area in standard particle physics; BST predicts violation, and to date all experiments have confirmed violation in the predicted sectors.

The framework is set up to be falsifiable across multiple independent observables. Each conservation law is the consequence of a specific substrate symmetry; each falsification would isolate a specific structural failure.

## 8.7 What comes next

Chapter 9 closes Volume 0 by proving the **Strong-Uniqueness Theorem** — the result that the geometry $D_{IV}^5$, the integers, the integer web, the operator zoo, and the conservation laws of this chapter are all forced together by a single multi-criterion convergence argument. Alternative geometries fail at least one criterion. The substrate, structurally, can only be $D_{IV}^5$.

Chapter 10 is a short methodology summary — how the team works, what discipline produced the framework so far, what to do if you want to do this kind of research yourself.

After this volume, Volume 1 begins the construction of quantum field theory on the substrate, taking the operators of Chapter 7 and the conservation laws of this chapter as the framework's input. The five integers, the integer web, the substrate geometry, the four-phase cycle, and the conservation laws are now in place. The physics begins.

---

**Where to look this up**: Noether's theorem in its original form is Emmy Noether, "Invariante Variationsprobleme," *Göttingen Nachrichten* (1918); reprinted in *Transport Theory and Statistical Physics* 1:186 (1971). The substrate-derivation theorems for energy, momentum, and electric-charge conservation are Lyra T2473, T2474, and T2475 respectively. The discrete-symmetry substrate-derivations are T2472 (parity), T2433 (time reversal), and T2434 (charge conjugation). The CPT-cluster substrate verification is the K85-K86-K87 audit trio. The Born=Bergman result identifying the Born rule with Bergman-kernel projection is the K67 audit. Standard references on CPT in axiomatic QFT remain Streater and Wightman's *PCT, Spin and Statistics, and All That*. For experimental status of conservation-law tests, the *Review of Particle Physics* (Particle Data Group) is the canonical reference and is updated annually.
