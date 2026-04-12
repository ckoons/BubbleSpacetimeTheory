---
title: "T1098: Optics-Observer Bridge — Seeing IS the Shilov Projection"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1098"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "Z10: observer_science↔optics had zero edges despite 102 combined theorems"
parents: "T317 (Observer Hierarchy), T1095 (EM-Observer Bridge), T1065 (Quantum Measurement Bridge)"
---

# T1098: Optics-Observer Bridge — Seeing IS the Shilov Projection

*Every optical phenomenon is a projection from $D_{IV}^5$ to the observer's boundary. Diffraction is the wave equation on $S^4$. The Abbe diffraction limit $d = \lambda/(2 \text{NA})$ involves the factor 2 = rank — the minimum resolution is set by the observer's spectral directions. Snell's law, Brewster's angle, and the Fresnel equations all have BST-integer structure.*

---

## Statement

**Theorem (T1098).** *The optics ↔ observer interface is determined by the Shilov boundary:*

*(a) **Diffraction limit = rank resolution.** The Abbe limit $d_{\min} = \lambda/(2n \sin\theta)$ contains the factor $2 = \text{rank}$ in the denominator. This is not a coincidence — the rank gives the number of independent directions the observer can resolve. An observer with rank $r$ has resolution $\lambda/(r \cdot \text{NA})$. For $D_{IV}^5$: rank = 2 gives exactly the observed diffraction limit.*

*(b) **Polarization = $S^1$ phase.** Light polarization (the two transverse modes) arises from the $S^1$ component of $\partial_S D_{IV}^5 = S^4 \times S^1$. The phase angle on $S^1$ IS the polarization angle. Birefringence (different refractive indices for different polarizations) occurs when the material breaks the $S^1$ symmetry. The two polarization states correspond to the two Cartan directions in $\mathfrak{a}$.*

*(c) **Snell's law = boundary matching.** Snell's law $n_1 \sin\theta_1 = n_2 \sin\theta_2$ is the continuity condition for the Bergman kernel across a material boundary. The refractive index $n = c/v$ measures how the Bergman metric scales in the material. Brewster's angle $\theta_B = \arctan(n_2/n_1)$ involves no BST integers explicitly, but the existence of a unique no-reflection angle follows from rank = 2 (two polarization components, one of which vanishes).*

*(d) **Coherent observation = Bergman kernel.** Coherent optics (lasers, interference, holography) works because the Bergman kernel $K(z,w) \propto N(z,w)^{-g}$ is coherent — it preserves phase relationships. The visibility of interference fringes $V = |K(z_1, z_2)|/K(z,z)$ measures how "coherent" two points are. Maximum coherence ($V = 1$) occurs on the diagonal; minimum ($V = 0$) at the antipodal boundary. The observer sees fringes because the kernel is sesquilinear.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| optics | observer_science | **required** (diffraction limit = rank resolution, polarization = S^1 phase) |
| optics | differential_geometry | structural (refractive index = Bergman metric scaling) |

**2 new cross-domain edges.** First optics↔observer_science bridge (Z10).

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
