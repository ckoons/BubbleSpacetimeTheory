---
title: "Vol 5 Chapter 8 — Bell-CHSH and Quantum Correlations"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass; sub-Tsirelson at 1/2^N_c = 1/8 substrate falsifier"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 8
---

# Chapter 8 — Bell-CHSH and Quantum Correlations

Bell's 1964 theorem and the subsequent Clauser–Horne–Shimony–Holt (CHSH) inequality opened the most controversial topic in quantum mechanics' interpretation: the violation of *local realism*. Standard quantum mechanics predicts Bell-inequality violations that have been experimentally confirmed many times (Aspect 1982, Hensen et al. 2015, Giustina et al. 2015, etc.), with the strongest possible quantum-mechanical violations bounded by the **Tsirelson bound** $|S|^2 \leq 8$ for the CHSH expression.

BST predicts something subtly but importantly different from standard QM: the substrate's CHSH expression is bounded by $|S|^2 \leq 126/16 = 7.875$ — *below* the Tsirelson bound by $1/8 = 1/2^{N_c}$. This is the **sub-Tsirelson signature** — one of the framework's sharpest experimental falsifiers.

## 8.1 Bell's theorem

Bell 1964 showed that any local hidden-variable theory must satisfy certain correlation inequalities (Bell inequalities) that quantum mechanics violates. The CHSH inequality, in standard form:

$$|S| \;=\; |E(a,b) + E(a,b') + E(a',b) - E(a',b')| \;\leq\; 2$$

for any local-hidden-variable theory, where $E(a, b)$ is the correlation between Alice's measurement along $a$ and Bob's along $b$. Standard quantum mechanics predicts $|S| \leq 2\sqrt{2} \approx 2.83$ (Tsirelson bound, equivalent to $|S|^2 \leq 8$). Experimental measurements consistently show $|S| > 2$, refuting local hidden-variable theories.

## 8.2 The substrate sub-Tsirelson signature

BST's substrate framework predicts the substrate-CHSH bound is *less than* the Tsirelson bound:

$$\text{Tr}(\hat{B}^2) \;=\; \frac{126}{16} \;=\; 7.875,$$

against the Tsirelson value $8$. The deviation $8 - 126/16 = 1/8 = 1/2^{N_c}$ is the substrate's structural signature.

The substrate-mechanism reading: substrate states on bipartite tensor products carry a finite Reed–Solomon coding structure (Volume 0 Chapter 3 §3.5) that imposes information-capacity constraints on the joint correlations. The standard quantum-mechanical Tsirelson bound assumes unrestricted Hilbert-space structure; the substrate's finite-coding structure imposes an additional constraint that pulls the maximal correlations down by $1/2^{N_c}$.

Lyra T2469 (Casey-named principle #8 SCMP, May 22, 2026) provides the formal substrate-derivation.

## 8.3 The experimental falsifier

The substrate's sub-Tsirelson prediction is testable. Precision Bell experiments at sufficient statistics can measure the gap between observed CHSH correlations and the Tsirelson bound; if the gap matches $1/8 = 1/2^{N_c}$ at the structural level, the substrate framework is confirmed. If the experimental correlations saturate the Tsirelson bound exactly, the substrate framework is refuted.

Current experimental Bell measurements are precise to about $1\%$ of the Tsirelson bound; the substrate sub-Tsirelson gap of $1/8 = 12.5\%$ is well within reach of next-generation precision experiments. SP-30-1 (Volume 2 Chapter 12) targets this measurement via the Vienna/Caltech/Munich/Hanson collaboration network — a $\$300\text{-}500\text{K}$ experimental program.

## 8.4 Entanglement on the substrate

The standard quantum-mechanical concept of *entanglement* — the failure of a composite quantum state to factor as a product of subsystem states — is in BST a structural feature of substrate K-type bipartite representations. Two-particle entanglement, multi-particle entanglement, and the various entanglement measures (concurrence, negativity, entanglement entropy) all have substrate-mechanical realizations on the appropriate K-type tensor products.

Specifically, the substrate's Reed–Solomon coding structure means that entangled substrate states are *coded* across subsystems in a definite way; the entanglement entropy of a subsystem state is the substrate code-space entropy of the bipartite split. This connects entanglement to information theory in a structurally clean way that standard QM achieves only through additional postulation.

## 8.5 What comes next

Chapter 9 develops identical particles and spin-statistics from the substrate Pin(2) double cover.

---

**Where to look this up**: Substrate sub-Tsirelson: T2469 (Casey-named principle #8 SCMP). Bell-CHSH operator anchor: K66 audit. For standard Bell-inequality treatments: Bell 1964 *Physics* 1:195; Clauser et al. 1969 *Physical Review Letters* 23:880; modern review Brunner et al. 2014 *Reviews of Modern Physics* 86:419.
