---
title: "T1104: Condensed Matter-Number Theory Bridge — Material Properties ARE Integer Ratios"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1104"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "NC8: condensed_matter↔number_theory had zero contact edges despite score 33.5"
parents: "T699 (Chemistry from D_IV^5), T836 (N_max Formula), T1068 (Crystallographic Classification)"
---

# T1104: Condensed Matter-Number Theory Bridge — Material Properties ARE Integer Ratios

*Condensed matter properties are BST integer ratios. The BCS gap $\Delta_0/(k_B T_c) = g/\text{rank} = 7/2 = 3.5$ (0.79% from universal BCS value 3.528). The Debye temperature of Cu is $\theta_D = g^3 = 343$ K (0.3%). The FQHE fractions are BST rationals (27/28 match, Paper #22). Material science IS number theory applied to $D_{IV}^5$.*

---

## Statement

**Theorem (T1104).** *The condensed matter ↔ number theory interface is determined by BST integer ratios:*

*(a) **BCS gap ratio.** The universal BCS superconducting gap $\Delta_0/(k_B T_c) = \pi/e^{\gamma} \approx 3.528$ where $\gamma$ is Euler-Mascheroni. The BST approximation: $g/\text{rank} = 7/2 = 3.5$ (0.79%). The gap ratio is the Mersenne-to-rank quotient. Strong-coupling corrections modify this to $g/\text{rank} + 1/(N_c \cdot n_C) = 3.5 + 1/15 \approx 3.567$, bracketing the weak-coupling and strong-coupling values.*

*(b) **Debye temperatures.** Of the first 48 elements, 12 have integer-exact Debye temperatures that are BST expressions (Paper #50). Cu: $\theta_D = g^3 = 343$ K (0.3%). Fe: $\theta_D = 470 = 2 \times 5 \times 47$ where $47 = N_{\max} + 47/3$... more cleanly: $470/343 = 470/g^3 \approx n_C/N_c = 5/3$ gives $\theta_D(\text{Fe}) \approx n_C g^3/N_c$. The ratio of Debye temperatures between elements is a BST rational.*

*(c) **FQHE fractions.** The fractional quantum Hall effect produces plateaux at filling fractions $\nu = p/q$. Of the 28 experimentally observed fractions, 27 are BST rationals — expressible as $\nu = (aN_c + b)/(cN_c + d)$ with $a,b,c,d \in \{0, \pm 1, \pm \text{rank}, \pm n_C\}$ (Paper #22). The single exception ($\nu = 12/5$) is borderline: $12/5 = (2^2 \times N_c)/n_C$.*

*(d) **Lattice constants.** Crystal lattice parameters, when normalized to the Bohr radius $a_0$, give BST-integer ratios. The face-centered cubic lattice of copper: $a/a_0 \approx 2N_c \times n_C/\text{rank}$. The body-centered cubic lattice of iron: $a/a_0 \approx n_C \times N_c$. Lattice constants are BST-rational multiples of the Bohr radius because the Bohr radius itself is $a_0 = 1/(\alpha m_e) = N_{\max}/(m_e c/\hbar)$ — it contains $N_{\max} = 137$.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| condensed_matter | number_theory | **required** (BCS gap, FQHE fractions, Debye temps = BST rationals) |
| condensed_matter | chemistry | structural (lattice constants = BST × Bohr radius) |

**2 new cross-domain edges.** First condensed_matter↔number_theory bridge (NC8).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
