---
title: "Vol 14 Chapter 4 — Nyquist Sampling and the Koons Tick"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content; LOAD-BEARING"
volume: "Vol 14 Information Theory"
chapter: 4
load_bearing: "Nyquist-Shannon sampling theorem; Koons tick = t_Planck · α^(C_2^2) ≈ 10⁻¹²⁰ s as substrate clock; max-frequency = 1/(2 t_K)"
---

# Chapter 4 — Nyquist Sampling and the Koons Tick

## Level 1 — one sentence

The Nyquist-Shannon sampling theorem requires sample rate $f_s \ge 2 f_{\max}$ to losslessly reconstruct a band-limited signal — and BST identifies the Koons tick $t_K = t_P \cdot \alpha^{C_2^2} \approx 10^{-120}$ s as the substrate's sampling clock with maximum representable frequency $1/(2 t_K) \approx 5 \cdot 10^{119}$ Hz.

## Level 2 — graduate-physicist precision

### 4.1 Nyquist-Shannon theorem

For a continuous signal $x(t)$ band-limited to $|f| \le f_{\max}$, exact reconstruction from samples $\{x(n T)\}$ is possible if $T \le 1/(2 f_{\max})$.

Equivalently: sample rate $f_s = 1/T \ge 2 f_{\max}$.

Reconstruction formula (Whittaker-Shannon interpolation):

$$x(t) = \sum_n x(nT) \, \text{sinc}((t - nT)/T)$$

### 4.2 Koons tick as substrate sampling rate

BST identifies the Koons tick as the substrate's natural sampling period:

$$t_K = t_P \cdot \alpha^{C_2^2} = t_P \cdot \alpha^{36} \approx 10^{-120} \text{ s}$$

Substrate sample rate: $f_K = 1/t_K \approx 10^{120}$ Hz.

Maximum BST-representable frequency: $f_{\max}^{\text{BST}} = f_K / 2 \approx 5 \cdot 10^{119}$ Hz.

### 4.3 Spacetime as Nyquist reconstruction

Hypothesis: spacetime is the substrate's Nyquist reconstruction of discrete-sample data at sub-Planckian resolution.

What we observe as continuous spacetime is the band-limited interpolation:

$$\text{spacetime}(t) = \sum_n \text{substrate-sample}(nt_K) \, \text{sinc}((t - nt_K)/t_K)$$

### 4.4 Physical implications

If substrate operates at $10^{120}$ Hz:
- Standard model physics ($f \le m_t c^2/h \approx 10^{25}$ Hz) is heavily oversampled
- Plenty of headroom for substrate K-type computations
- Frequencies above $f_{\max}^{\text{BST}}$ are not representable — possible falsifier if observed

### 4.5 K-audit anchors

- **T2405**: Koons tick definition
- **Vol 8 Ch 3** (classical wave mechanics — Nyquist's classical origin)

## Level 3 — 5th-grader accessibility

**Nyquist-Shannon sampling**: to perfectly capture a signal with max frequency $f_{\max}$, sample at least $2 f_{\max}$. CDs sample at 44.1 kHz (twice the 22 kHz upper hearing limit). **Koons tick** ≈ $10^{-120}$ s is BST's substrate sampling period — substrate samples at $10^{120}$ Hz. **Maximum representable BST frequency**: $5 \cdot 10^{119}$ Hz. **Hypothesis**: spacetime is the Nyquist reconstruction of substrate samples. Plenty of headroom for everything we observe.

---

## What comes next

Chapter 5 develops Born = Bergman as information-theoretic measurement.

## Where to look this up

- Shannon 1949 sampling theorem
- BST: T2405; Vol 8 Ch 3
