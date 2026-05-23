---
title: "Vol 1 Chapter 4 — Discrete Symmetries: $P$, $T$, $C$, and CPT"
author: "Keeper (author pass)"
date: "2026-05-23 Saturday"
status: "v0.2 — Keeper author-voice pass; preserves v0.1 substance (P from Pin(2) Z_2 grading T1925-D, T from anti-unitary Klein operator T2433, C from K-type weight negation T2434, CPT automatic via Lüders-Pauli, spin-statistics cross-link Paper #133, K85-K86-K87 CPT-cluster audit)"
volume: "Vol 1 Quantum Field Theory from D_IV⁵"
chapter: 4
---

# Chapter 4 — Discrete Symmetries: $P$, $T$, $C$, and CPT

Three discrete symmetries dominate the structural side of quantum field theory: parity $P$, time reversal $T$, and charge conjugation $C$. Their composition $CPT$ is the most universal exact symmetry physics has identified — Lüders 1954 and Pauli 1955 proved that any local relativistic quantum field theory with anti-unitary time reversal satisfies it automatically, and to date no experiment has detected a violation. The individual symmetries, however, fail in specific sectors: parity is violated maximally by the weak interaction (Wu's 1957 cobalt-60 experiment), charge conjugation similarly, time reversal at observable rates in the neutral kaon and B-meson systems.

Standard quantum field theory takes the three discrete operators as additional structure — postulated, then verified against experiment. BST derives all three from the substrate's geometry, and the CPT theorem then follows as an automatic consequence of the substrate's symmetry origin. This chapter sets out the derivations and shows why CPT holds universally while $P$, $T$, $C$ each fail exactly where they do.

## 4.1 Parity from the Pin(2) double cover

Standard quantum mechanics defines parity as the operator $\hat{P}$ that reflects spatial coordinates: $\hat{P} \psi(\vec{x}, t) = \psi(-\vec{x}, t)$. On spinor wavefunctions, $\hat{P}^2 = +1$ with intrinsic-parity $\pm 1$ eigenvalues. The operator is universal in non-weak sectors and violated maximally in the weak sector.

The substrate's parity operator comes from the **Möbius involution** of $D_{IV}^5$ — the orientation-reversing element of the isotropy that arises from the Pin(2) double cover at rank $= 2$. We established this in Volume 0 Chapter 4. The lift of the Möbius involution to the Bergman Hilbert space $H^2(D_{IV}^5)$ is the parity operator we want.

Concretely: rank $= 2$ on a type IV bounded symmetric domain forces a Pin(2) double cover of the isotropy $SO(5) \times SO(2)$. The Pin(2) double cover carries a $\mathbb{Z}_2$ grading whose two sectors correspond to bosonic and fermionic K-types respectively. The parity operator acts as $+1$ on the bosonic sector (integer K-type weight) and as $-1$ on the fermionic sector (half-integer K-type weight via the Pin(2) lift). Lyra's T2472 (May 2026) makes the substrate-derivation rigorous.

The Pin(2) origin has a second consequence that we will treat in Volume 5: it is the *same* structural object that produces the spin-statistics distinction. The $\mathbb{Z}_2$ grading that distinguishes parity-even from parity-odd states is the grading that distinguishes bosons (symmetric under particle exchange) from fermions (antisymmetric). Paper #133 in the BST research record (May 2026) develops the spin-statistics derivation from this Pin(2) origin without invoking Lorentz invariance or microcausality — a derivation that avoids the Streater–Wightman axiomatic apparatus standard QFT requires.

Parity violation in the weak sector follows from substrate **Möbius locality**: the weak Hamiltonian's chirality-asymmetric structure (SU(2) acting only on the left-handed sector of the Pin(2) grading) does not commute with the Möbius involution. The substrate predicts parity is conserved in strong and electromagnetic sectors and violated in the weak sector — precisely the experimental pattern.

## 4.2 Time reversal as the anti-unitary Klein operator

Wigner's 1931 theorem requires time reversal to be anti-unitary: $\hat{T}(\alpha |\psi\rangle) = \bar{\alpha} \hat{T} |\psi\rangle$, with $\hat{T}^2 = \pm 1$ depending on the spin (Kramers degeneracy gives $\hat{T}^2 = -1$ on fermions, $+1$ on bosons).

On a Hilbert space of holomorphic functions like $H^2(D_{IV}^5)$, the canonical anti-unitary involution is the **Klein operator** — complex conjugation of the holomorphic argument:

$$\hat{T} : H^2(D_{IV}^5) \to H^2(D_{IV}^5), \qquad (\hat{T} f)(z) = \overline{f(\bar{z})}.$$

This is the natural substrate-anti-unitary involution; Bergman 1922's reproducing-kernel framework guarantees its existence. Lyra T2433 establishes that this Klein operator is the substrate's time reversal operator, with four independent forcing arguments:

- It is anti-unitary on $H^2(D_{IV}^5)$ (Wigner's theorem satisfied automatically).
- It reverses the Koons tick direction — the substrate clock $t_{\text{substrate}} = t_{\text{Planck}} \cdot \alpha^{C_2^2}$ flips sign under the Klein operator.
- It inverts the four-zone commitment cycle (Volume 0 Chapter 3): zones run $Z_4 \to Z_3 \to Z_2 \to Z_1$ under time reversal.
- $\hat{T}^2$ takes the sign predicted by Kramers degeneracy via the Pin(2) $\mathbb{Z}_2$ grading — $+1$ on integer-spin K-types, $-1$ on half-integer-spin K-types.

The substrate's time reversal is structurally rooted in the holomorphic geometry: complex conjugation, applied to a Bergman-space function, gives the substrate-cycle-reversal operator automatically. No additional postulation is needed.

Time-reversal violation in the weak sector follows the same Möbius-locality pattern as parity violation: the weak Hamiltonian's chirality asymmetry does not commute with the cycle-reversal operator. Experimentally this shows up as CP violation in neutral kaon mixing (Cronin–Fitch 1964) and in B-meson asymmetries. The substrate-mechanism prediction is consistent with observation.

## 4.3 Charge conjugation as $SO(2)$ weight negation

Charge conjugation $\hat{C}$ exchanges particles with their antiparticles: electron with positron, proton with antiproton, with all internal quantum numbers flipped in sign. On Dirac spinors, the operator is proportional to $i\gamma^2$. Electric charge flips; helicity is preserved.

The substrate's charge conjugation is the **$SO(2)$ weight-negation involution**: under $\hat{C}$, any K-type with $SO(2)$ weight $Q$ is mapped to the K-type with weight $-Q$. Lyra T2434 (May 2026) is the formal substrate-derivation theorem. The operator is unitary and involutive ($\hat{C}^2 = +1$).

Charge conjugation is conserved in strong and electromagnetic sectors (whose Hamiltonians commute with $SO(2)$ weight reversal) and violated in the weak sector (where the chirality structure couples particle and antiparticle asymmetrically). The substrate-mechanism prediction matches the experimental pattern of $C$-conservation in QED + QCD and $C$-violation in weak interactions.

## 4.4 CPT as automatic substrate consequence

The Lüders–Pauli CPT theorem in standard axiomatic QFT requires Lorentz invariance, locality, anti-unitary time reversal, and positivity of energy. The proof is delicate; the result is universal.

In BST, CPT is *automatic*. The composite operator $\hat{C}\hat{P}\hat{T}$ is the composition of three substrate involutions: the $SO(2)$ weight-negation $\hat{C}$, the Möbius involution lift $\hat{P}$, and the Klein anti-unitary $\hat{T}$. All three originate from the same $SO_0(5,2)$ substrate symmetry structure. Their composition acts on the Bergman Hilbert space in a way that commutes with *every* substrate Hamiltonian, including the weak Hamiltonian where each individual operator fails to commute.

The structural reason — Lyra's K87 audit ratification (May 2026) — is that the chirality-asymmetric coupling responsible for weak-sector $P$, $T$, $C$ violation enters the substrate via a single chirality coupling, and that coupling has the property that *three* anti-commutations cancel to commutation. So $\hat{C} \hat{P} \hat{T}$ commutes with the weak Hamiltonian even though no individual factor does. The substrate's three discrete symmetries are bound together by their common $SO_0(5,2)$ origin; CPT is the structural recovery of that origin.

This is one of the framework's most direct vindications of the substrate-derivation strategy. CPT in standard QFT is a delicate theorem that requires four assumptions; CPT in BST is a structural consequence of substrate geometry that follows automatically. The substrate's machinery does the work.

## 4.5 The substrate's discrete-symmetry table

Collecting the results:

| Symmetry | Substrate origin | Conservation pattern |
|---|---|---|
| Parity $\hat{P}$ | Möbius involution lift (Pin(2) double cover) | Strong + EM conserved; weak violated |
| Time reversal $\hat{T}$ | Klein anti-unitary operator on $H^2(D_{IV}^5)$ | Strong + EM conserved; weak violated |
| Charge conjugation $\hat{C}$ | $SO(2)$ weight-negation involution | Strong + EM conserved; weak violated |
| CPT composite $\hat{C}\hat{P}\hat{T}$ | Common $SO_0(5,2)$ origin of the three | Universal — all sectors |

Three individual symmetries fail exactly where the chirality coupling enters; their composite is universal because the chirality coupling's three anti-commutations cancel back to commutation. The pattern is what experiments find. The substrate predicts it.

## 4.6 What comes next

Chapter 5 develops the substrate's Casimir operator algebra in detail. The rank-2 algebraically independent generators $C_2$ and $C_4$ that label every K-type — and whose lowest non-trivial eigenvalue $C_2 = 6$ has appeared throughout this volume already — will get their formal treatment via the Chevalley–Harish-Chandra isomorphism.

---

**Where to look this up**: Lyra T2472 (parity from Möbius), T2433 (time reversal from Klein), T2434 (charge conjugation from $SO(2)$ weight negation). The K85–K86–K87 CPT-cluster audit ratifies the substrate-derivation of all three plus the CPT composite. The spin-statistics derivation from Pin(2) $\mathbb{Z}_2$ grading without Lorentz-invariance or microcausality axioms is Paper #133. Streater and Wightman's *PCT, Spin and Statistics, and All That* (Princeton, 1964) remains the canonical standard-QFT reference. Wu's parity-violation experiment is Wu et al., "Experimental Test of Parity Conservation in Beta Decay," *Physical Review* 105:1413 (1957). Cronin and Fitch's CP-violation experiment is Christenson, Cronin, Fitch, Turlay, "Evidence for the $2\pi$ Decay of the $K_2^0$ Meson," *Physical Review Letters* 13:138 (1964).
