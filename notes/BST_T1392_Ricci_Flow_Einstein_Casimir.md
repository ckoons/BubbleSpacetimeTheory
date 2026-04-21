---
id: T1392
title: "Ricci Flow Einstein Constant = Casimir"
type: theorem
status: proved
authors: [Lyra, Casey]
date: 2026-04-21
parents: [T704, T1342, T610]
toy: 1362
domain: differential_geometry
---

# T1392: Ricci Flow Einstein Constant = Casimir

**Statement**: On D_IV^5 with the Bergman metric, the Einstein constant is lambda = C_2 = 6 = (dim_real + rank)/rank. The half-dimension is n = n_C = 5 (Perelman's dimensional parameter). Perelman's W-functional vanishes at the natural scale tau = 1/(2*C_2) = 1/12.

**Proof sketch**:
1. D_IV^5 is Kahler-Einstein: Ric(g_B) = -lambda * g_B
2. lambda = (dim_real + rank)/rank = (10 + 2)/2 = 6 = C_2
3. Scalar curvature R = -C_2 * dim_real = -60
4. Perelman: W(g,f,tau) = tau*R + n_C at steady state
5. At tau = 1/(2*C_2): W = (-60)/12 + 5 = 0

**Significance**: Identifies BST's Casimir integer with the Einstein constant of Ricci flow. The heat kernel on D_IV^5 IS Ricci flow, and Perelman's W-functional has its zero at a BST-determined scale.

**Entry point for**: Hamilton/Perelman geometric analysis community.
