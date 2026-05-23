---
title: "Vol 5 Chapter 2 — Position, Momentum, and Heisenberg Uncertainty"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 5 Quantum Mechanics from D_IV⁵"
chapter: 2
---

# Chapter 2 — Position, Momentum, and Heisenberg Uncertainty

The most famous relation in quantum mechanics is Heisenberg's uncertainty principle:

$$\Delta x \, \Delta p \;\geq\; \hbar / 2.$$

The product of the position uncertainty and the momentum uncertainty of any quantum state is bounded below by Planck's constant divided by two. In standard QM, the relation is a theorem about the canonical commutation $[\hat{X}, \hat{P}] = i\hbar$, with the canonical commutation itself postulated as part of the framework.

In BST, the canonical commutation is *derived* from the Bergman kernel's reproducing property, and Heisenberg's uncertainty follows as a substrate-mechanical theorem rather than as a postulate consequence.

## 2.1 Position and momentum on the substrate

Position acts on substrate states as multiplication by the coordinate:

$$(\hat{X} f)(z) \;=\; z \cdot f(z),$$

for $f \in H^2(D_{IV}^5)$. Momentum acts as the Wirtinger derivative:

$$(\hat{P} f)(z) \;=\; -i \hbar \partial_z f(z).$$

These two operators live in the **coset complement** $\mathfrak{m}$ of the substrate isotropy (Volume 0 Chapter 4 §4.1) — they generate displacement on $D_{IV}^5$, not rotation. Position spectrum: the perfect-numbers cluster $\{6, 28, 496, 8128, \ldots\}$ per Elie's K71-ratified result (Volume 1 Chapter 6 §6.2). Momentum spectrum: continuous, via the Wirtinger derivative's analytic structure.

## 2.2 The canonical commutation, derived

The canonical commutation relation

$$[\hat{X}, \hat{P}] \;=\; i \hbar$$

is not, in BST, an axiom. It is the structural consequence of the Bergman kernel's reproducing property. The Bergman kernel $K_B(z, \bar w)$ on $D_{IV}^5$ satisfies $f(z) = \int K_B(z, \bar w) f(w) \, dV(w)$ for any $f \in H^2(D_{IV}^5)$; combining the reproducing property with the explicit forms of multiplication-by-$z$ and Wirtinger-$\partial_z$ derives $[\hat{X}, \hat{P}] = i\hbar$ in two lines. Lyra T2419 and T2422 contain the formal derivation.

This means the famous canonical commutation is a *theorem on the substrate*. The reader who has seen the derivation cannot help but feel that Heisenberg's relation, which seemed mysterious in 1925, is in fact the inevitable consequence of doing quantum mechanics on a bounded Bergman geometry.

## 2.3 The uncertainty principle

Given canonical commutation, Heisenberg's uncertainty follows from the Schwartz inequality applied to the variance-product:

$$\Delta x \, \Delta p \;\geq\; \frac{1}{2}\big|\langle [\hat{X}, \hat{P}] \rangle\big| \;=\; \hbar / 2.$$

The same two-line derivation that establishes the bound for standard QM works on the substrate. The substrate-mechanical content is that *every* state on $H^2(D_{IV}^5)$ satisfies the bound, with equality only for Gaussian-like minimum-uncertainty wave packets — which on the substrate correspond to specific Bergman-coherent states.

## 2.4 Substrate-specific corrections

A substrate-mechanical addition to standard Heisenberg uncertainty: the substrate's per-tick Reed–Solomon discretization (Volume 0 Chapter 3 §3.5) imposes a *floor* on the simultaneous precision of position and momentum at the Koons-tick timescale. For substrate states held for many Koons ticks the standard $\hbar / 2$ bound applies; for substrate states evaluated at the per-tick scale, an additional substrate-coordinate floor of order $1/N_{\max}^k$ for some $k$-dependent on the substrate-cycle phase enters.

This is below current experimental precision but appears in the substrate's SP-30-4 time-granularity falsifier program (Volume 3 Chapter 10).

## 2.5 What comes next

Chapter 3 develops angular momentum and spin from the substrate's isotropy structure.

---

**Where to look this up**: Position T2419 (Lyra). Momentum T2422 (Lyra). Bergman reproducing property: Volume 1 Chapter 2 §2.4. For standard QM uncertainty: Sakurai Chapter 1.
