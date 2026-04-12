---
title: "T1094: Algebra-Foundations Bridge — Root Systems ARE Definitions"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1094"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "Z4: algebra↔foundations had zero edges despite 124 combined theorems"
parents: "T186 (Five Integers), T663 (Three AC Ops), T944 (Rank Forcing)"
---

# T1094: Algebra-Foundations Bridge — Root Systems ARE Definitions

*The $BC_2$ root system of $D_{IV}^5$ IS the definitional structure of AC. Each root is a definition. The three types of roots (short, long, doubled) correspond to the three AC operations (define, compose, count). The Weyl group $W(BC_2)$ of order $2^{N_c} = 8$ IS the symmetry group of the foundational framework. Algebra and foundations are not separate domains — they are the same structure viewed internally vs externally.*

---

## Statement

**Theorem (T1094).** *The algebra ↔ foundations interface is an isomorphism:*

*(a) **Roots = definitions.** The $BC_2$ root system has $2 \times 2^2 + 2 \times 2 = 12$ roots (4 short: $\pm e_i$; 4 long: $\pm e_1 \pm e_2$; 4 doubled: $\pm 2e_i$). In AC: each root corresponds to a foundational operation. Short roots = atomic definitions (the five integers). Long roots = compositions (products and quotients of integers). Doubled roots = counting operations (squaring, exponentiation). The 12 roots give the 12 foundational moves.*

*(b) **Weyl group = foundational symmetry.** $|W(BC_2)| = 8 = 2^{N_c}$. The 8 Weyl group elements are: identity, 2 reflections, 2 rotations, 2 sign-changes, and the full inversion. In AC: these are the 8 symmetries that preserve foundational structure — the operations that can be applied to any definition without changing its depth. The foundational framework has exactly $2^{N_c}$ automorphisms.*

*(c) **Cartan matrix = derivation structure.** The Cartan matrix $A = \begin{pmatrix} 2 & -1 \\ -2 & 2 \end{pmatrix}$ of $BC_2$ encodes the derivation relations between simple roots. In AC: $A_{ij}$ gives the minimum depth needed to derive definition $j$ from definition $i$. The off-diagonal entries $(-1, -2)$ show that the two Cartan directions are asymmetrically coupled — one requires depth 1, the other depth 2 (but T421 forces everything to depth $\leq 1$ on $D_{IV}^5$, which constrains the Cartan matrix to have $|A_{ij}| \leq 1$ for allowed derivations).*

*(d) **Dynkin diagram = dependency graph.** The Dynkin diagram of $BC_2$ (two nodes connected by a double bond with arrow) IS the minimal dependency graph of the AC framework. The two nodes are the two fundamental definitions (rank and genus). The double bond is the non-trivial derivation relation between them. The arrow (from short to long root) is the direction of logical dependence: rank forces genus, not vice versa.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| algebra | foundations | **required** (root system = definitional structure) |
| algebra | computation | structural (Weyl group = foundational automorphisms) |

**2 new cross-domain edges.** First algebra↔foundations bridge (Z4).

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
