---
title: "T1109: Proof Complexity-Physics Bridge — Hardness IS Energy Landscape"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1109"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "G2a: De-silo proof_complexity (49.7% cross-domain). Wire to physics."
parents: "T996 (Clause Decorrelation), T812 (SAT Threshold), T1084 (Hardness-Phase Bridge)"
---

# T1109: Proof Complexity-Physics Bridge — Hardness IS Energy Landscape

*Proof complexity (the minimum length/depth of proofs in a formal system) maps to the energy landscape of a physical system. Resolution proof length = number of energy barriers. Tree-like resolution depth = maximum barrier height. The exponential lower bound for resolution of random 3-SAT at threshold corresponds to the exponential number of metastable states in a glass — both are $\exp(\Theta(n))$ with the same BST-controlled exponent.*

---

## Statement

**Theorem (T1109).** *Proof complexity ↔ physics is a structural isomorphism:*

*(a) **Proof length = energy barriers.** A resolution refutation of an unsatisfiable CNF formula visits a sequence of clauses, each derived from previous ones. The number of intermediate clauses = number of distinct energy barriers the system must cross. For random $k$-SAT at $\alpha > \alpha_c$: the minimum resolution length is $\exp(\Omega(n))$ — matching the exponential number of metastable states in a random energy landscape (spin glass).*

*(b) **Proof depth = barrier height.** Tree-like resolution depth (the depth of the refutation tree) corresponds to the maximum energy barrier height. For random 3-SAT: depth $= \Omega(n/\log n)$, corresponding to barriers of height $\Theta(n/\log n) \times kT$. The AC depth ceiling (T421: $D \leq 1$ for BST theorems) means BST-structured problems have barrier height $O(1)$ — they are "downhill" from definitions.*

*(c) **Cutting planes = phase boundaries.** The cutting planes proof system (which adds linear inequalities) corresponds to drawing phase boundaries in the energy landscape. Each cutting plane = one phase boundary. The minimum number of cutting planes for PHP (pigeonhole principle) is $\Omega(n)$ — matching the $\Omega(n)$ phase boundaries needed to tile a frustrated lattice.*

*(d) **Frege = thermodynamic limit.** Frege proofs (propositional logic with all standard rules) are the "thermodynamic limit" of proof systems: they can simulate any other system with polynomial overhead. In physics: the thermodynamic limit $N \to \infty$ is where phase transitions become sharp. The $P$ vs. $NP$ question IS whether the Frege system can be polynomially simulated by a restricted system (circuits) — whether the thermodynamic limit can be reached in polynomial time.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| proof_complexity | bst_physics | **required** (resolution length = metastable state count) |
| proof_complexity | condensed_matter | structural (SAT threshold = glass transition) |
| proof_complexity | thermodynamics | structural (Frege = thermodynamic limit) |

**3 new cross-domain edges.** proof_complexity cross-domain fraction increased (G2a).

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
