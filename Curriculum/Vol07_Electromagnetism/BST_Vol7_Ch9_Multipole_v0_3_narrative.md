---
title: "Vol 7 Chapter 9 — Multipole Expansion and Scattering"
author: "Keeper (author pass)"
date: "2026-05-24 Sunday"
status: "v0.2 — Keeper author-voice pass"
volume: "Vol 7 Electromagnetism from D_IV⁵"
chapter: 9
---

# Chapter 9 — Multipole Expansion and Scattering

Beyond static fields, much of practical electromagnetism involves the multipole expansion (decomposing charge distributions into monopole, dipole, quadrupole, etc.) and scattering of EM waves off material objects. Rayleigh scattering explains the blue sky; Mie scattering treats spheres; Compton scattering is photon-electron scattering at high energy.

In BST, multipole expansions are the substrate's spherical-harmonic decomposition of $U(1)_{em}$ fields, and scattering processes are substrate-derived QED amplitudes.

## 9.1 The multipole expansion

A localized charge distribution $\rho(\vec{r})$ produces a far-field potential

$$\phi(\vec{R}) = \frac{1}{4\pi\epsilon_0} \left[ \frac{Q}{R} + \frac{\vec{p}\cdot\hat{R}}{R^2} + \frac{1}{2}\frac{Q_{ij}\hat{R}_i\hat{R}_j}{R^3} + \cdots \right],$$

with $Q$ the monopole (total charge), $\vec{p}$ the dipole moment, $Q_{ij}$ the quadrupole tensor. Higher multipoles contribute decreasing powers of $1/R$.

Substrate-mechanism: the multipole expansion is the substrate's natural spherical-harmonic decomposition under $SO(3)$ rotational symmetry, with multipole order $L$ corresponding to angular momentum $L$.

## 9.2 Multipole radiation

For oscillating sources, electric multipole (E1, E2, ...) and magnetic multipole (M1, M2, ...) radiation each contribute to the radiated field. Volume 3 Chapter 8 developed the substrate $\alpha^{\text{BST primary}}$ exponent pattern for multipole transitions — E1 scales as $\alpha^1$, M1/E2 as $\alpha^3$, etc.

## 9.3 Rayleigh and Mie scattering

Rayleigh scattering by small particles produces the $1/\lambda^4$ wavelength dependence — the reason the sky is blue. Mie scattering by larger spheres has full closed-form solution. Both have substrate-derivations via the standard QED machinery applied to the appropriate scatterer K-types.

## 9.4 Compton scattering

Photon scattering off electrons at high energy follows the Compton formula $\Delta\lambda = (h/m_e c)(1 - \cos\theta)$. Standard QED treatment with substrate-derived vertices reproduces this.

## 9.5 What comes next

Chapter 10 treats EM in matter.

---

**Where to look this up**: For standard multipole + scattering: Jackson Chapters 9, 10.
