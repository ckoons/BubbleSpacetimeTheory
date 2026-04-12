---
title: "T1157: The GCS Identity — rank² + n_C + C_2 = N_c × n_C = 15"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 12, 2026"
theorem: "T1157"
ac_classification: "(C=0, D=0)"
status: "Proved — immediate from definitions"
origin: "T-6 board item: formalize the GCS identity"
parents: "T186 (Five Integers), T110 (rank=2), T667 (n_C=5), T190 (C_2=6), T666 (N_c=3)"
---

# T1157: The GCS Identity — rank² + n_C + C_2 = N_c × n_C = 15

*The identity $\text{rank}^2 + n_C + C_2 = N_c \times n_C$ holds for the BST integers: $4 + 5 + 6 = 3 \times 5 = 15$. This is the statement that the sum of three DERIVED quantities (Weyl reflections, complex dimension, Casimir) equals the product of two FUNDAMENTAL quantities (color number, complex dimension). Geometrically: the isotropy representation decomposes as $\text{rank}^2$ (torus) $+ n_C$ (tangent) $+ C_2$ (normal) $= N_c \times n_C$ (total embedding dimension of color in the domain).*

---

## Statement

**Theorem (T1157).** *$\text{rank}^2 + n_C + C_2 = N_c \times n_C$:*

*(a) **Numerical verification.** $4 + 5 + 6 = 15 = 3 \times 5$. ✓*

*(b) **Algebraic proof.** Substituting $C_2 = N_c \times \text{rank}$ and $\text{rank} = 2$:*

$$\text{rank}^2 + n_C + N_c \times \text{rank} = N_c \times n_C$$
$$4 + n_C + 2N_c = N_c \times n_C$$
$$n_C(N_c - 1) = 2N_c + 4 = 2(N_c + 2) = 2(N_c + \text{rank})$$
$$n_C = \frac{2(N_c + \text{rank})}{N_c - 1}$$

*For $N_c = 3$: $n_C = 2 \times 5 / 2 = 5$. ✓. This is an ALTERNATIVE derivation of $n_C = 5$ from $N_c = 3$ and $\text{rank} = 2$, independent of the (2,5) derivation (T1007). The GCS identity FORCES $n_C = 5$ given $N_c = 3$ and $\text{rank} = 2$.*

*(c) **Geometric meaning.** The isotropy representation of $K = SO(5) \times SO(2)$ on the tangent space decomposes into three pieces:*
- *$\text{rank}^2 = 4$: the $SO(2) \times SO(2)$ action on the maximal torus $T^2$ — the 4 Weyl reflections*
- *$n_C = 5$: the tangent directions of $D_{IV}^5$ — the complex dimensions themselves*
- *$C_2 = 6$: the normal directions (the complement of the tangent in the embedding) — the Casimir degrees of freedom*

*Total: $4 + 5 + 6 = 15 = N_c \times n_C$. This is the real dimension of the color-domain embedding space: $N_c$ colors $\times$ $n_C$ complex dimensions.*

*(d) **Consecutive integer property.** The three terms are consecutive: $\{4, 5, 6\} = \{\text{rank}^2, n_C, C_2\}$. The BST integers include three consecutive integers whose sum equals the product of the endpoints of the BST AP. This is the unique such triple:*
- *If $\{k, k+1, k+2\}$ sums to $N_c \times n_C = 15$: $3k + 3 = 15 \implies k = 4 = \text{rank}^2$. Unique.*

*(e) **Relation to other identities.***
- *$15 = C(C_2, 2) = \binom{6}{2}$: the pairwise couplings of $C_2$ generators*
- *$15 = \dim SU(4) = (N_c+1)^2 - 1$: the dimension of the next higher SU group*
- *$15 = n_C + 2n_C = 3 \times n_C = N_c \times n_C$: three copies of the dimension (one per color)*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| algebra | bst_physics | **derived** (isotropy decomposition identity) |

**1 new cross-domain edge.**

---

*Casey Koons & Claude 4.6 (Lyra) | April 12, 2026*
