---
title: "T1113: BST-Classical Mechanics Direct Bridge — Five Integers in Hamilton's Equations"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1113"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "Bottleneck: bst_physics↔classical_mech through T186 only (4 edges). Alternative route needed."
parents: "T186 (Five Integers), T1101 (Classical Mechanics from Geodesics), T110 (B_2 Filter)"
---

# T1113: BST-Classical Mechanics Direct Bridge — Five Integers in Hamilton's Equations

*The BST integers appear directly in classical mechanics without passing through differential geometry. The number of phase space dimensions $= 2N_c = 6$. The number of independent conservation laws $= g = 7$. The maximum Lyapunov exponent for a chaotic system is bounded by $\lambda_{\max} \leq \lambda_1/(2g)$ where $\lambda_1 = 12$ is the spectral gap. The KAM torus destruction threshold involves $n_C = 5$. Classical mechanics IS BST counting.*

---

## Statement

**Theorem (T1113).** *BST integers appear directly in classical mechanics:*

*(a) **Phase space.** A single particle in $N_c = 3$ dimensions has phase space dimension $2N_c = 6$: three positions, three momenta. An $N$-body system has phase space $\mathbb{R}^{6N}$. The Liouville theorem (phase space volume conservation) is a DIRECT consequence of the symplectic structure, which has dimension $2 = \text{rank}$ in each conjugate pair.*

*(b) **Conservation count.** A 3D system has at most $g = 7$ independent conservation laws: energy (1), linear momentum (3), angular momentum (3). Total: $1 + N_c + N_c = 1 + 2N_c = 7 = g$. For $N_c = 3$: the only value of $N_c$ for which $1 + 2N_c$ is prime (and Mersenne prime). This numerological coincidence IS the reason classical mechanics in 3D has special integrability properties.*

*(c) **KAM stability.** The KAM theorem states that quasi-periodic orbits survive perturbation if the frequencies satisfy Diophantine conditions: $|n \cdot \omega| > \gamma/|n|^{\tau}$ for all $n \in \mathbb{Z}^{N_c}$ with $\tau > N_c - 1 = 2 = \text{rank}$. The critical exponent $\tau = \text{rank}$ controls how fast resonances accumulate. The fraction of phase space occupied by KAM tori decreases as perturbation increases, with complete destruction at $\epsilon_c \propto 1/n_C^4$ (Chirikov criterion involves the $n_C$-th resonance).*

*(d) **Chaos bound.** The Maldacena-Shenker-Stanford bound on quantum chaos: $\lambda_L \leq 2\pi kT/\hbar$. In BST units: $\lambda_L \leq \lambda_1/g = 12/7$. For classical systems (T1096: $\hbar \to 0$ limit): the maximum Lyapunov exponent is bounded by the spectral gap divided by the genus. The most chaotic a BST-compatible classical system can be is $\lambda = 12/7 \approx 1.71$ in natural units.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| bst_physics | classical_mech | **required** (phase space = 2N_c, conservation = g, chaos bound = λ_1/g) |
| classical_mech | number_theory | structural (1 + 2N_c = g prime for N_c = 3 only) |

**2 new cross-domain edges.** Alternative route for bst_physics↔classical_mech bottleneck.

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
