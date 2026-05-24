---
title: "Vol 8 Chapter 8 — Oscillations and Normal Modes"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 8
load_bearing: "Simple harmonic motion; damped/driven oscillators; normal modes; eigenvalue problem for coupled systems"
---

# Chapter 8 — Oscillations and Normal Modes

## Level 1 — one sentence

Oscillations — simple, damped, driven, coupled — appear everywhere in physics because near any stable equilibrium the potential is well-approximated by a parabola, giving simple harmonic motion locally, and the eigenvalue analysis of multi-DOF systems yields normal modes that decouple the dynamics into independent oscillators.

## Level 2 — graduate-physicist precision

### 8.1 Simple harmonic motion (SHM)

A particle in potential $V(x) = (1/2)k x^2$ has equation of motion $m\ddot x = -kx$, giving:

$$x(t) = A\cos(\omega t + \phi), \quad \omega = \sqrt{k/m}$$

Constants $A$ (amplitude) and $\phi$ (phase) set by initial conditions.

Energy: $E = (1/2)kA^2$. Always conserved (no dissipation).

### 8.2 Damped oscillator

With viscous damping $-b\dot x$:

$$m\ddot x + b\dot x + kx = 0$$

Solutions classified by $\zeta = b/(2\sqrt{mk})$:
- **Underdamped** ($\zeta < 1$): $x = A e^{-\zeta\omega_0 t}\cos(\omega_d t + \phi)$ with $\omega_d = \omega_0\sqrt{1-\zeta^2}$ — oscillating decay
- **Critically damped** ($\zeta = 1$): fastest return to equilibrium without oscillation
- **Overdamped** ($\zeta > 1$): two real exponential decays, slow return

Quality factor $Q = \omega_0 m/b = 1/(2\zeta)$.

### 8.3 Driven oscillator and resonance

With external drive $F_0 \cos(\omega t)$:

$$m\ddot x + b\dot x + kx = F_0 \cos(\omega t)$$

Steady-state response:

$$x(t) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + (b\omega/m)^2}}\cos(\omega t - \delta)$$

with phase lag $\delta$. Resonance at $\omega = \omega_d \approx \omega_0$; amplitude diverges for zero damping. The $Q$-factor sets the sharpness (FWHM $= \omega_0/Q$).

### 8.4 Normal modes

For a system of $N$ coupled oscillators: equations $\mathbf{M}\ddot{\vec x} = -\mathbf{K}\vec x$ with mass matrix $\mathbf{M}$ and stiffness matrix $\mathbf{K}$.

Try $\vec x = \vec a e^{i\omega t}$: eigenvalue problem $(\mathbf{K} - \omega^2 \mathbf{M})\vec a = 0$. Eigenvalues $\omega_i^2$ are squared normal-mode frequencies; eigenvectors $\vec a_i$ are normal mode shapes.

Each normal mode oscillates independently at its own frequency. General motion is superposition of normal modes.

### 8.5 Worked example: coupled pendulum

Two identical pendulums of length $\ell$ coupled by a spring with constant $k$:

$$m\ell^2 \ddot\theta_1 = -mg\ell\theta_1 - k\ell^2(\theta_1 - \theta_2)$$
$$m\ell^2 \ddot\theta_2 = -mg\ell\theta_2 - k\ell^2(\theta_2 - \theta_1)$$

Normal modes:
- **Symmetric**: $\theta_1 = \theta_2$, frequency $\omega_+ = \sqrt{g/\ell}$ (gravity alone, spring uncoupled)
- **Antisymmetric**: $\theta_1 = -\theta_2$, frequency $\omega_- = \sqrt{g/\ell + 2k/m}$ (gravity + spring)

If you displace one pendulum and release: motion alternates between the two — energy transfers back and forth at the beat frequency $|\omega_+ - \omega_-|$.

### 8.6 Continuum oscillations

A string of length $L$ with linear density $\mu$ under tension $T$: wave equation

$$\partial_t^2 y = (T/\mu) \partial_x^2 y$$

with wave speed $v = \sqrt{T/\mu}$.

Standing-wave normal modes: $y_n = A_n \sin(n\pi x/L) \cos(\omega_n t)$ with $\omega_n = n\pi v/L$. Harmonic series (Pythagoras).

### 8.7 Substrate connection

Each normal mode is the substrate's natural K-type at that frequency. The substrate's discrete K-type structure naturally produces discrete normal-mode spectra; continuous-medium normal modes are the substrate K-type spectrum in the appropriate boundary-condition sector.

### 8.8 K-audit anchors

- **Vol 5 Ch 4**: quantum harmonic oscillator (substrate K-type analog)
- **Vol 6 Ch 7**: phonons (quantized normal modes of solids)
- **Vol 9 Ch 7**: phonons in condensed matter

## Level 3 — 5th-grader accessibility

Anything that has a stable equilibrium and gets nudged slightly oscillates — pendulums, mass-on-spring, atoms in molecules, the wing of a plane in turbulence. Near equilibrium, $V \approx (1/2) k x^2$ → simple harmonic motion with frequency $\omega = \sqrt{k/m}$. Add **damping** → oscillation decays (underdamped) or just settles (critically/overdamped). Add **driving force** at frequency $\omega$ → resonance peak when $\omega = \omega_0$. **Multiple coupled oscillators** decompose into independent **normal modes** at characteristic frequencies. A vibrating guitar string has a harmonic series of normal modes — that's the music. In BST, every normal mode is a substrate K-type at its natural frequency.

---

## What comes next

Chapter 9 develops continuum elasticity.

## Where to look this up

- Goldstein Ch 6; Marion-Thornton Ch 11-12
- BST: Vol 5 Ch 4 (quantum HO); Vol 9 Ch 7 (phonons)
