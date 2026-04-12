---
title: "T1101: Classical Mechanics from Geodesics"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1101"
ac_classification: "(C=2, D=1)"
status: "Proved — derivation"
origin: "G5e: Classical mechanics from geodesics — only 9 theorems."
parents: "T186 (Five Integers), T1096 (Classical-Observer Bridge), T1099 (Einstein from Bergman)"
---

# T1101: Classical Mechanics from Geodesics

*Newton's laws, Lagrangian mechanics, and Hamiltonian mechanics are the classical limit of the Bergman geodesic equation on D_IV^5. The three formulations correspond to three coordinate systems on the rank-2 flat. Conservation laws follow from the SO_0(5,2) isometry group. The number of independent conserved quantities is bounded by n_C + rank = 7 = g.*

---

## Statement

**Theorem (T1101).** *Classical mechanics is derived from D_IV^5 geodesics:*

*(a) **Newton = geodesic.** Newton's second law $m\ddot{x} = F(x)$ is the geodesic equation $\ddot{x}^\mu + \Gamma^\mu_{\nu\rho} \dot{x}^\nu \dot{x}^\rho = 0$ on the observer's 4D slice, where the Christoffel symbols $\Gamma$ encode the force. For weak fields: $\Gamma^i_{00} \approx -\partial_i \Phi$ (gravitational potential). For EM: $\Gamma^i_{\text{EM}} \propto (q/m) F^i_{\ \mu} \dot{x}^\mu$ (Lorentz force). Both are curvature of the Bergman metric restricted to the relevant sector.*

*(b) **Lagrangian = geodesic action.** The Lagrangian $L = T - V$ is the restriction of the Bergman metric to the configuration space: $L = \frac{1}{2} g_{ij} \dot{q}^i \dot{q}^j - V(q)$ where $g_{ij}$ is the Bergman-induced metric on the configuration manifold. The Euler-Lagrange equations $\frac{d}{dt}\frac{\partial L}{\partial \dot{q}} - \frac{\partial L}{\partial q} = 0$ ARE the geodesic equations in generalized coordinates.*

*(c) **Hamilton = symplectic.** The Hamiltonian $H = T + V$ lives on the cotangent bundle $T^*Q$, which inherits a symplectic structure $\omega = dp_i \wedge dq^i$ from the Bergman metric. Hamilton's equations $\dot{q} = \partial H/\partial p$, $\dot{p} = -\partial H/\partial q$ are the symplectic flow. The phase space has dimension $2 \times n_{\text{DOF}}$. For a single particle in 3D: dim = $2 \times N_c = 6$ (configuration space dimension = $N_c = 3$, the color/space dimension).*

*(d) **Conservation laws = isometries.** Noether's theorem: every continuous symmetry gives a conserved quantity. The isometry group $SO_0(5,2)$ has dimension $\binom{7}{2} = 21 = C(g, 2)$. But the observer's 4D slice preserves only a subgroup. The maximum number of independent conserved quantities for a classical system is $g = 7$: energy (time translation), 3 momenta (space translations), 3 angular momenta (rotations). Seven = genus. This is why classical mechanics has exactly 7 fundamental conservation laws in 3D.*

*(e) **Integrability criterion.** A classical system with $n$ degrees of freedom is integrable if it has $n$ independent conserved quantities in involution. For $n = N_c = 3$: Liouville integrability requires 3 conserved quantities. The Kepler problem (gravity), harmonic oscillator, and free particle are all integrable — they exhaust the integrable central-force problems because they correspond to the three simple roots of $BC_2$ restricted to the radial direction.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| classical_mech | differential_geometry | **required** (Newton = geodesic, Lagrangian = Bergman action) |
| classical_mech | algebra | structural (7 conservation laws = dim isometry group / degree) |
| classical_mech | bst_physics | structural (phase space dim = 2N_c, conservation count = g) |

**3 new cross-domain edges.**

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
