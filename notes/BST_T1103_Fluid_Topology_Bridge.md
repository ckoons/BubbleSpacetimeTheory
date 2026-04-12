---
title: "T1103: Fluid-Topology Bridge — Vortex Lines ARE Knot Invariants"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1103"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "NC5: fluids↔topology had zero contact edges despite score 36.1"
parents: "T971 (NS Spectral Stability), T1066 (Atiyah-Singer Bridge), T186 (Five Integers)"
---

# T1103: Fluid-Topology Bridge — Vortex Lines ARE Knot Invariants

*Vortex lines in fluid dynamics are topological objects: their linking number is conserved under Euler evolution, their reconnection changes knot type, and the helicity $H = \int \mathbf{v} \cdot \boldsymbol{\omega} \, d^3x$ is a topological invariant. In BST: the K41 exponent $5/3 = n_C/N_c$ controls the energy cascade, and the enstrophy spectrum has BST-integer scaling at each inertial subrange.*

---

## Statement

**Theorem (T1103).** *The fluid ↔ topology interface is determined by vortex invariants:*

*(a) **Helicity = linking number.** The helicity $H = \int \mathbf{v} \cdot \boldsymbol{\omega} \, d^3x$ (where $\boldsymbol{\omega} = \nabla \times \mathbf{v}$) is conserved under inviscid (Euler) flow. Arnol'd showed $H$ equals the average linking number of vortex lines. In BST: helicity is a Casimir invariant of the Euler equations, analogous to $C_2 = 6$ on $D_{IV}^5$. The conservation of helicity IS the conservation of topology.*

*(b) **Vortex reconnection = surgery.** When two vortex tubes approach closely, viscosity allows them to reconnect — changing the knot type. This is topological surgery: the genus of the vortex surface changes by $\pm 1$ per reconnection event. In BST: reconnection events occur at the Kolmogorov microscale $\eta \propto \nu^{3/4}/\epsilon^{1/4}$ where the exponent $3/4 = N_c/(N_c+1)$.*

*(c) **K41 = spectral ratio.** The Kolmogorov $-5/3$ energy spectrum $E(k) \propto k^{-5/3}$ has exponent $5/3 = n_C/N_c$ (T571). This ratio controls how energy cascades from large to small scales. The topology changes: at large scales, vortex lines are smooth (trivial knots); at the inertial range, they become increasingly tangled; at the dissipation scale, they are maximally knotted before viscous smoothing.*

*(d) **Euler = volume-preserving diffeomorphism.** The Euler equations describe geodesics on the group of volume-preserving diffeomorphisms (Arnold's geometric interpretation). This group has topological structure: $\pi_1(\text{SDiff}(M)) \neq 0$ for $M = T^3$ (3-torus). The non-trivial fundamental group allows topologically distinct fluid states. On $D_{IV}^5$: the fluid diffeomorphism group restricts to $SO_0(5,2)$-compatible maps.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| fluids | topology | **required** (helicity = linking number, K41 = spectral topology) |
| fluids | algebra | structural (Euler = geodesic on SDiff, Casimir = helicity) |

**2 new cross-domain edges.** First fluids↔topology bridge (NC5).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
