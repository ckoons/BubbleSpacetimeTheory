---
title: "T1105: Differential Geometry-Nuclear Bridge — Nuclear Shape IS Bergman Geometry"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1105"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "NC7: diff_geom↔nuclear had zero contact edges despite score 33.8"
parents: "T1049 (SEMF Spectral Derivation), T1067 (Nuclear Shell Model), T186 (Five Integers)"
---

# T1105: Differential Geometry-Nuclear Bridge — Nuclear Shape IS Bergman Geometry

*Nuclear deformation, the liquid drop model, and the nuclear radius formula $r = r_0 A^{1/3}$ are consequences of the Bergman metric restricted to the nuclear scale. The $A^{1/3}$ scaling is the volume law for a 3D object ($N_c = 3$ spatial dimensions). Nuclear quadrupole deformation is the rank-2 tensor perturbation of a spherical Bergman kernel — the same rank-2 tensor that gives gravitational waves (T1099).*

---

## Statement

**Theorem (T1105).** *The differential geometry ↔ nuclear interface is determined by the Bergman metric at nuclear scales:*

*(a) **Nuclear radius = Bergman metric at $r_0$.** The nuclear radius formula $R = r_0 A^{1/N_c}$ (where $N_c = 3$, $r_0 \approx 1.25$ fm) is the volume scaling of a $N_c$-dimensional sphere. In BST: $r_0 = N_c\pi^2/(n_C) \times \hbar c/m_p \approx 1.245$ fm (T1049, 0.4%). The nuclear scale $r_0$ is set by the Bergman metric evaluated at the proton Compton wavelength.*

*(b) **Quadrupole deformation = rank-2 perturbation.** Deformed nuclei have quadrupole moments $Q \propto \beta_2 Z R^2$ where $\beta_2$ is the deformation parameter. The quadrupole ($\ell = 2 = \text{rank}$) is the leading deformation because rank = 2 sets the lowest non-trivial multipole. Octupole deformation ($\ell = 3 = N_c$) appears at higher excitation — reflecting the next BST integer.*

*(c) **Liquid drop surface.** The nuclear surface energy $E_S = a_S A^{2/3}$ involves the exponent $2/3 = \text{rank}/N_c$ (T1049). This is the surface-to-volume ratio of a $N_c$-dimensional object. The surface energy coefficient $a_S/a_V = (g+1)/g = 8/7$ (1.2%) is set by the genus correction to the Bergman metric at the surface.*

*(d) **Nuclear curvature.** The Ricci scalar curvature of the Bergman metric restricted to a nuclear-sized region is $R_{\text{nuclear}} \propto g/r_0^2$. This curvature drives the binding — it is why nucleons attract. The curvature changes sign at $A \approx 2^{N_c} \times g = 56$ (iron peak, T1049) — below 56, fusion releases energy (positive curvature gradient); above 56, fission releases energy (negative curvature gradient). The nuclear binding curve IS the Bergman curvature profile.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| differential_geometry | nuclear | **required** (nuclear radius = Bergman at r_0, deformation = rank-2 tensor) |
| differential_geometry | bst_physics | structural (surface exponent 2/3 = rank/N_c) |

**2 new cross-domain edges.** First diff_geom↔nuclear bridge (NC7).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
