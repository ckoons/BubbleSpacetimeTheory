---
title: "Vol 8 Chapter 2 — Newton's Laws of Motion"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 2
load_bearing: "Newton's three laws; inertial frames; Galilean invariance; conservation of momentum"
---

# Chapter 2 — Newton's Laws of Motion

## Level 1 — one sentence

Newton's three laws — inertia ($F=0 \Rightarrow$ constant velocity), $F = ma$, and action-reaction — together with Galilean relativity form the foundation of classical mechanics, and they emerge in BST as the substrate's Scale-2 effective dynamics for slow massive bodies in flat-space limit of the substrate $SO_0(5,2)$ geometry.

## Level 2 — graduate-physicist precision

### 2.1 The three laws

**First law (inertia)**: A body in uniform motion (or at rest) continues so unless acted on by an external force.

**Second law**: $\vec F = m\vec a = m\, d^2\vec r/dt^2 = d\vec p/dt$ (the third form is fundamental — force = rate of change of momentum).

**Third law**: For every action there is an equal and opposite reaction: $\vec F_{12} = -\vec F_{21}$.

### 2.2 Inertial frames and Galilean invariance

An **inertial frame** is one in which Newton's first law holds (a free body moves with constant velocity). Two inertial frames are related by Galilean transformation:

$$\vec r' = \vec r - \vec v_0 t, \quad t' = t$$

Newton's laws are invariant under Galilean transformations — physics is the same in all inertial frames.

Substrate reading: at Scale 2 with $v \ll c$, the substrate's Lorentz invariance (Vol 7 Ch 7) reduces to Galilean. The substrate doesn't have absolute rest — only relative motion between K-type configurations matters.

### 2.3 Conservation of momentum

From Newton's second + third laws: total momentum $\vec P = \sum_i \vec p_i$ of an isolated system is conserved.

For collisions:
- Elastic: kinetic energy also conserved
- Inelastic: kinetic energy lost (converted to heat, deformation)
- Completely inelastic: particles stick together

Substrate reading: momentum conservation is the substrate's Noether current from spatial translation symmetry (T2474 per Friday May 22 EOD framework; Vol 0 Ch 8).

### 2.4 Force types

Common forces in classical mechanics:
- **Gravitational**: $\vec F = -GM m \hat r/r^2$
- **Spring**: $\vec F = -k\vec x$ (Hooke)
- **Friction**: $\vec F = -\mu N$ opposing motion
- **Drag**: $\vec F \propto -v$ (Stokes) or $-v^2$ (Newton)
- **Centripetal**: $F = mv^2/r$ for circular motion
- **Lorentz**: $\vec F = q(\vec E + \vec v \times \vec B)$ — bridges to EM (Vol 7)

### 2.5 Worked example: projectile motion

A baseball thrown at angle $\theta = 45°$, initial speed $v_0 = 30$ m/s, neglecting air drag:

- Horizontal: $x(t) = v_0 \cos\theta \cdot t$
- Vertical: $y(t) = v_0 \sin\theta \cdot t - (1/2) g t^2$

Range $R = v_0^2 \sin(2\theta)/g = (30)^2 \cdot 1 / 9.8 \approx 92$ m.

Max height: $h = v_0^2 \sin^2\theta/(2g) = 900 \cdot 0.5 / 19.6 \approx 23$ m.

Time of flight: $t = 2 v_0 \sin\theta/g \approx 4.3$ s.

### 2.6 K-audit anchors

- **T2474** (Friday May 22, 2026): substrate momentum conservation Noether
- **Volume 7 Ch 7**: Lorentz → Galilean limit at low velocity
- **Volume 0 Ch 8**: substrate Noether currents

## Level 3 — 5th-grader accessibility

Newton's laws are the foundation of mechanics:
1. **Inertia**: things keep doing what they're doing unless something pushes
2. **$F = ma$**: push something, it accelerates; bigger mass needs more push
3. **Action-reaction**: push something, it pushes back equally hard

In any non-accelerating frame, these laws hold. Physics doesn't care if you're standing still or moving — only relative motion matters (Galilean relativity). Momentum is conserved when no outside forces act. In BST, all of this comes out of the substrate's Scale-2 limit when objects are slow (much less than $c$) and big (decohered).

---

## What comes next

Chapter 3 develops Lagrangian mechanics — the variational reformulation.

## Where to look this up

- Newton 1687, *Principia*
- Goldstein Ch 1; Marion and Thornton, *Classical Dynamics*
- BST: T2474, Vol 7 Ch 7
