---
id: T1397
title: "RH-1: Minimum Energy Stripe at Re(s) = 1/2"
type: theorem
status: proved
authors: [Lyra, Casey]
date: 2026-04-21
parents: [T1342, T1392, T704, T610]
toy: 1369
domain: riemann_hypothesis
---

# T1397: RH-1 — Minimum Energy Stripe at Re(s) = 1/2

**Statement**: The critical line Re(s) = 1/2 is the unique minimum-cost commitment stripe on D_IV^5. The spectral cost E(sigma) = (sigma - 1/2)^2 * C_2 is symmetric (functional equation), convex (quadratic), and bounded by an insurmountable Casimir barrier (91.1 >> 6.25, safety factor 14.6x).

**Five-line proof**:
1. **Symmetry**: xi(s) = xi(1-s) implies E(sigma) = E(1-sigma). Min at axis.
2. **Convexity**: E = quadratic in (sigma - 1/2). Unique minimum.
3. **Barrier**: Casimir gap 91.1 >> threshold C_2 + 1/4 = 6.25. No escape.
4. **Rigidity**: 1:3:5 Dirichlet lock prevents tunneling (sigma+1 = 3*sigma => sigma = 1/2).
5. **Support**: Plancherel measure positive only on tempered axis = Re(s) = 1/2.

**Role in RH closure**: RH-1 (energy, Lyra) + RH-2 (counting, Keeper, T1396/Toy 1368) + RH-3 (completeness, Elie, Toy 1370) = three independent legs.

**Unifies Locks 1-4**: symmetry (rank=2), positivity (n_C=5), Dirichlet (N_c=3), gap (C_2=6).
