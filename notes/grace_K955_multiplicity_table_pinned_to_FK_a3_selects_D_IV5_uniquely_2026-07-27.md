---
id: grace_K955_multiplicity_table_pinned_to_FK_a3_selects_D_IV5_uniquely_2026-07-27
date: 2026-07-27
program: TEGMARK
status: current
supersedes: []
superseded_by: null
topic_tags: [characteristic-multiplicity, Faraut-Koranyi, color-forcing, K955, D_IV5-uniqueness, a=3, Cartan-classification]
claims:
  - id: this-a
    topic: the characteristic-multiplicity table pinned to FK; a=3 selects D_IV^5 uniquely (K955 color-forcing)
    status: current
    superseded_by: null
    date: 2026-07-27
---

# [TEGMARK] K955 color-forcing — the characteristic-multiplicity table pinned to Faraut-Korányi. a=3 selects D_IV⁵ uniquely, independent of the generation count.

*Grace | 2026-07-27 Mon | Keeper queued me (K955) to pin the multiplicity table to primary source for the reviewer paper. My "pin-to-source" lane. Consolidates my 06-21 census pin, verified, with the low-rank coincidence checked. This is the load-bearing input to Casey's insight that color forces the DOMAIN independent of the occupancy fork.*

## Primary source
**Faraut & Korányi, *Analysis on Symmetric Cones* (Oxford, 1994)** — the characteristic multiplicities (a, b) of an irreducible bounded symmetric domain / Euclidean Jordan algebra, with **dim_ℂ = r + a·r(r−1)/2 + b·r**. `a` = multiplicity of the restricted roots **±(ξ_i ± ξ_j)**; `b` = multiplicity of ±ξ_i (nonzero only off tube type).

## The table (by Cartan type)
| type | a |
|---|---|
| I_{p,q} | 2 |
| II_n (SO*(2n)) | 4 |
| III_n (Sp(n,ℝ)) | 1 |
| **IV_n (Lie ball)** | **n − 2** |
| V = E_III (E6, 16-dim) | 6 |
| VI = E_VII (E7, 27-dim) | 8 |

## a = 3 ⟺ D_IV⁵ (unique, verified)
- I→2, II→4, III→1, E6→6, E7→8 are all ≠ 3.
- IV_n: a = n−2 = 3 **only at n=5.**
- **⟹ a = 3 selects type IV, n=5 = D_IV⁵ uniquely — across all six families and all n.** No other domain has three "colors."

**This is firmer than the census (rank²−1) route**, which returned the pair {D_IV⁵, E7}: here you don't need rank²−1, only the multiplicity table + observed a=3. Observed 3-color QCD forces the domain *completely* (type IV, dim 5, rank 2, all at once), and E7's a=8 is just one instance of "every alternative has the wrong color number."

## Low-rank coincidence check (Keeper's SO(4,2)≅SU(2,2) flag) — does NOT touch a=3
SU(2,2) = I_{2,2} has a=2; SO(4,2) = IV₄ has a=n−2=2. The isomorphism is real, **at a=2 (n=4)**. It does not touch a=3 (n=5). The D_IV⁵ selector is **clean** — the family-coincidence lives one multiplicity below.

## The non-circular criterion pair (rank=2, a=3) — primary, no color/dim input
- dim_ℂ = r + a·r(r−1)/2 = 2 + 3·1 = **5 = n_C** (dim = rank + a).
- N_c = a = **3**; n_C = rank + N_c = **5**. Dimension and color are one invariant read twice.
Nothing in "rank 2, multiplicity 3" mentions a dimension or a color, yet it forces both — exactly the prior-invariant, non-circular selector Paper B needs.

## Discipline (pin-to-source, my standing directive)
Cite `a` by **value + role** — a = the ±(ξ_i±ξ_j) restricted-root multiplicity, = n−2 = 3 for D_IV⁵ (convention-independent). **Do NOT relabel "short/long" from memory** — quote FK's designation. The load-bearing fact is that a=3 is a **prior invariant** (defined for every HSD, innocent of D_IV⁵), which is what makes the selector non-circular. For the reviewer paper: the six a-values above are the standard characteristic multiplicities (FK / Loos / Helgason); cite FK's classification chapter for the exact enumeration.

## Why this matters (the day's strongest structural move — Casey's insight)
Color forces the domain **independent of the generation count.** So whatever the threshold derivation returns — 3 generations or the honest 4 — it does **not** change which domain we're on. The generation count stops being a *selector of the geometry* and becomes a *property of the already-forced D_IV⁵ to be computed*. The foundation is off the contested occupancy bijection: the firmest thing (the domain, via color) and the most contested (the count, via the spinor shift E₀) are cleanly separated, so neither threatens the other. E7 is now excluded by the wrong color number, independent of, and prior to, the 3-vs-4 fork.

— Grace, 2026-07-27 [TEGMARK]. K955 multiplicity table pinned to Faraut-Korányi (Analysis on Symmetric Cones, 1994): a = ±(ξ_i±ξ_j)-multiplicity; {I,II,III,IV_n,E6,E7}→{2,4,1,n−2,6,8}. a=3 ⟺ type IV n=5 = D_IV⁵ UNIQUELY (all others ≠3; IV_n=3 only at n=5). Firmer than rank²−1 (no pair — single domain). Low-rank coincidence SO(4,2)≅SU(2,2) is at a=2, does NOT touch a=3 → selector clean. (rank=2, a=3) → dim=5, N_c=3 non-circularly (prior invariant, no color/dim input). Cite by value+role, don't relabel short/long from memory. Color forces the DOMAIN independent of the generation count → foundation off the occupancy fork.
