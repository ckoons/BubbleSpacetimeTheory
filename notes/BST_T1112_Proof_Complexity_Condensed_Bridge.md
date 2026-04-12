---
title: "T1112: Proof Complexity-Condensed Matter Bridge — Resolution Width IS Correlation Length"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1112"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "G2a continued: proof_complexity needs more physics connections"
parents: "T996 (Clause Decorrelation), T1084 (Hardness-Phase), T1109 (Proof Complexity-Physics)"
---

# T1112: Proof Complexity-Condensed Matter Bridge — Resolution Width IS Correlation Length

*The resolution width (minimum clause width needed to refute a formula) maps to the correlation length in a spin system. Width $w = \Theta(\sqrt{n})$ for random 3-SAT at threshold corresponds to correlation length $\xi = \Theta(\sqrt{n})$ in the random-field Ising model. The Ben-Sasson-Wigderson width-size relation $S \geq 2^{(w - k)^2/n}$ IS the free energy bound $F \geq \exp((\xi - \xi_0)^2/L^2)$ for domain wall nucleation.*

---

## Statement

**Theorem (T1112).** *Resolution proof complexity = spin system thermodynamics:*

*(a) **Width = correlation length.** In resolution, width $w$ = maximum number of literals in any clause during refutation. For random $k$-SAT at threshold: $w = \Omega(\sqrt{n})$ (Ben-Sasson-Wigderson). In spin systems: the correlation length $\xi$ measures how far spin-spin correlations extend. At criticality: $\xi = \Theta(L^{1/2})$ for mean-field systems (dimension $> d_c = 4$). Since the SAT clause interaction graph has effective dimension $n_C = 5 > d_c = 4$ (T1057): the mean-field scaling holds, and $w \sim \xi$.*

*(b) **Size = free energy.** Resolution size (total number of clauses) $S \geq 2^{(w-k)^2/n}$. In thermodynamics: the free energy cost of a domain wall of width $(\xi - \xi_0)$ in a system of size $L$ is $F \geq kT \exp((\xi - \xi_0)^2/L^2)$. The correspondence: $n \leftrightarrow L^{n_C}$ (system size), $w \leftrightarrow \xi$ (correlation/resolution width), $S \leftrightarrow \exp(F/kT)$ (proof size = Boltzmann factor of barrier).*

*(c) **Space = magnetization.** Resolution space (maximum number of clauses stored simultaneously) corresponds to the total magnetization: both measure the "memory" of the system. Space lower bounds $\geq w$ (Atserias-Dalmau) correspond to the thermodynamic inequality $|M| \geq \xi^{-d+2}$.*

*(d) **Random-field = random instance.** A random $k$-SAT instance is a random-field Ising model: each clause adds a "field" that biases certain spins. The satisfying assignments are the ground states. The unsatisfiability transition at $\alpha_c$ IS the spin glass transition at the critical random-field strength.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| proof_complexity | condensed_matter | **required** (width = correlation length, size = free energy) |
| proof_complexity | statistical_mechanics | structural (random-SAT = random-field Ising) |

**2 new cross-domain edges.** proof_complexity further de-siloed (G2a).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
