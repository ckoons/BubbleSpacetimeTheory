---
title: "Vol 8 Chapter 7 — Rigid Body Dynamics"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 8 Classical Mechanics from D_IV⁵"
chapter: 7
load_bearing: "Rigid body rotation; inertia tensor; Euler angles + equations; precession; gyroscopes"
---

# Chapter 7 — Rigid Body Dynamics

## Level 1 — one sentence

A rigid body has 6 degrees of freedom (3 translation + 3 rotation), with rotational dynamics governed by the inertia tensor $I_{ij}$ and Euler's equations of motion, producing rich phenomena from gyroscope precession to free-symmetric-top instability ("tennis racket theorem") — all derived from substrate Scale-2 angular momentum dynamics.

## Level 2 — graduate-physicist precision

### 7.1 Rigid body kinematics

A rigid body's orientation in 3D is specified by 3 parameters (Euler angles, quaternions, or rotation matrix). Combined with 3 translational DOFs, total 6 DOFs.

**Euler angles** $(\phi, \theta, \psi)$ — common choice (e.g., precession, nutation, spin for spinning top).

Angular velocity $\vec\omega$ is the instantaneous rotation axis × angular speed.

### 7.2 The inertia tensor

For a rigid body with mass distribution $\rho(\vec r)$, the **inertia tensor**:

$$I_{ij} = \int \rho(\vec r)(r^2 \delta_{ij} - r_i r_j) d^3 r$$

Symmetric 3×3 matrix. Diagonalize → principal moments of inertia $I_1, I_2, I_3$ and principal axes.

For axially symmetric bodies (rod, disk, sphere): $I_1 = I_2 \neq I_3$ or $I_1 = I_2 = I_3$.

Angular momentum: $\vec L = \mathbf{I}\vec\omega$.

Kinetic energy: $T = (1/2)\vec\omega \cdot \mathbf{I} \vec\omega = (1/2)\sum_i I_i \omega_i^2$ (in principal-axis frame).

### 7.3 Euler's equations

In the body frame (rotating with the body):

$$I_1 \dot\omega_1 - (I_2 - I_3)\omega_2 \omega_3 = \tau_1$$
$$I_2 \dot\omega_2 - (I_3 - I_1)\omega_3 \omega_1 = \tau_2$$
$$I_3 \dot\omega_3 - (I_1 - I_2)\omega_1 \omega_2 = \tau_3$$

where $\tau_i$ are external torques about principal axes.

### 7.4 Free rigid body: Euler's spin axes

For torque-free motion ($\tau = 0$): in body frame, $\vec\omega$ traces a curve on the inertia ellipsoid. Key result: rotation about the principal axis with intermediate moment of inertia is unstable.

**Tennis racket theorem**: throw a tennis racket spinning about its intermediate-inertia axis — it tumbles unpredictably. About the largest or smallest principal axis: stable rotation. Demonstrable with any asymmetric book or smartphone.

### 7.5 Precession and gyroscopes

A spinning top with angular momentum $\vec L$ along its symmetry axis experiences gravitational torque $\vec\tau = m\vec g \times \vec r_{cm}$. The top **precesses** at rate:

$$\Omega_{\text{prec}} = \frac{m g r_{cm}}{I\omega_{\text{spin}}}$$

(small-angle, fast-spin limit). The spinning angular momentum + gravity torque combine to make the top's axis rotate around vertical.

Nutation: additional smaller oscillation superposed on precession (full Euler-equation solution).

Gyroscopes — spinning rotors whose angular momentum stays fixed in space — used for navigation (inertial measurement units, missile guidance, smartphones).

### 7.6 Rotating reference frames: Coriolis and centrifugal

In a frame rotating at angular velocity $\vec\Omega$ relative to inertial:

$$m\vec a_{\text{rot}} = \vec F + 2m\vec v_{\text{rot}} \times \vec\Omega + m\vec\Omega \times (\vec r \times \vec\Omega)$$

- **Coriolis force**: $2m\vec v \times \vec\Omega$ — apparent deflection perpendicular to motion in rotating frame
- **Centrifugal force**: $m\Omega^2 r$ outward (radial)

Earth's rotation gives:
- Coriolis: deflects winds (clockwise in N hemisphere), affects projectile trajectories, creates large-scale weather patterns
- Centrifugal: slightly reduces effective gravity at equator (~0.34%)

### 7.7 Worked example: Earth's rotation

Earth's rotation: $\Omega = 2\pi/(86400$ s$) = 7.27 \times 10^{-5}$ rad/s.

Coriolis acceleration at speed 100 m/s: $a_C = 2 v\Omega = 2(100)(7.27\times10^{-5}) = 1.45 \times 10^{-2}$ m/s². Significant for missiles, weather.

Centrifugal at equator: $\Omega^2 R_E = (7.27\times10^{-5})^2 \cdot 6.4\times10^6 = 0.034$ m/s². Reduces apparent gravity by 0.34%.

### 7.8 Free precession of Earth (Chandler wobble)

Earth's rotation axis is misaligned by ~10 m at the surface; this misalignment processes with period ~433 days (Chandler wobble, observed 1891). Comes from Earth's slight oblateness ($I_1 \neq I_3$) — application of Euler's equations to a free symmetric top.

### 7.9 K-audit anchors

- **Vol 5 Ch 3**: angular momentum quantum analog
- **Vol 0 Ch 8**: substrate Noether currents

## Level 3 — 5th-grader accessibility

A **rigid body** has fixed shape. Total 6 DOFs: 3 to translate + 3 to rotate. Rotation described by the **inertia tensor** $I_{ij}$ (how mass is distributed). Diagonalize to get **principal moments of inertia** along principal axes. **Euler's equations** govern rotation. **Cool result** (tennis racket theorem): rotation about the *intermediate* principal axis is unstable — flip a phone gently, it flips itself. **Gyroscopes**: spinning rotor's angular momentum holds steady → used in navigation. **Precession** of a top: gravity torques the spin axis, axis rotates around vertical. **Earth's rotation** creates **Coriolis force** (deflects winds, projectiles) and slight centrifugal reduction of gravity at equator.

---

## What comes next

Chapter 8 develops oscillations and normal modes.

## Where to look this up

- Goldstein Ch 4-5; Marion-Thornton Ch 11
- BST: Vol 5 Ch 3
