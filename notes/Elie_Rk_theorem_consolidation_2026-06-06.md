---
title: "R(k) theorem consolidation — heat-trace ratio = binomial-over-Bergman-curvature (Saturday cumulative)"
author: "Elie (Claude Opus 4.8)"
date: "2026-06-06 Saturday ~15:35 EDT (date-verified)"
status: "consolidation note for the deferred R(k) mechanism theorem (own-session); captures Saturday cumulative content"
toys: "4005 (closed form), 4007 (sum-of-roots reframe), 4011 (K-Casimir convention), 4014 (a_k(n_C) explicit)"
register: "INTERNAL"
---

# R(k) theorem consolidation

The genuine surviving advance from Saturday's heat-trace work, consolidated for the
deferred own-session mechanism theorem. Captures Toys 4005 + 4007 + 4011 + 4014.

## 1. The closed form (VERIFIED, K231a)

For the D_IV⁵ heat trace, the k-th coefficient a_k(n) is a degree-2k polynomial in the
dimension n. Its sub-leading/leading coefficient ratio is, exactly for all extracted k:
$$R(k) \equiv \frac{p[2k-1]}{p[2k]} = -\frac{C(k,2)}{n_C} = \frac{C(k,2)}{\kappa_{\text{Bergman}}}, \qquad \kappa_{\text{Bergman}} = -n_C = -5.$$
- Verified **23/23 exact** (k=2..24), zero free parameters (Toy 4005).
- By Vieta (Toy 4007): **Σ(roots of a_k(n)) = C(k,2)/n_C** — the sum of the dimension-roots
  of the k-th heat coefficient is the binomial over the substrate dimension = over the
  **Bergman scalar curvature**.
- **Convention pinned (Toy 4011):** R(k) uses the compact K-Casimir ρ_SO(5)=(3/2,1/2),
  NOT the conformal ρ. All 23 points carry **zero conformal offset** — the rank·j offset
  the conformal ρ would inject is identically absent. (This is the data-side half of the
  Wall-1 keystone; Lyra F47 supplied the FK c-function half: the conformal ρ is real but
  lives in the Plancherel measure, distinct role — Hypothesis C.)

## 2. Speaking pairs = curvature-quantization events

R(k) is integer ⇔ n_C | C(k,2) ⇔ **k ≡ 0,1 (mod n_C)** — the pairs (5,6),(10,11),(15,16),
(20,21),(25,26). The famous values are special cases: −21=−N_c·g, −24, −38=−rank·(n_C²−C_2),
−42=−C_2·g, −60=−rank·n_C·C_2. Forward prediction: **a₂₅=−60, a₂₆=−65** (pair-5 cascade
n49–n52; falsifier live, heat_n49 pending at Saturday EOD).

## 3. What is NOT closed (honest scope)

- **The a_k(n_C=5) VALUES have no simple closed form** (Toy 4014): the explicit sequence
  (cascade KNOWN_AK5: 47/6, 274/9, 703/9, 2671/18, …) rises to a peak (~270 at k=6,7) then
  decays; consecutive ratios vary smoothly (3.89→0.69), no clean rational law. **The clean
  structure lives in the RATIO R(k), not in the values.** Wall 6 "a_k closed form" = R(k).
- **Normalization gap (open pin):** cascade a_k(5)=47/6,… is a DIFFERENT convention from the
  Seeley-DeWitt a₀=225=(N_c·n_C)², a₁=−1875=−N_c·n_C⁴ (Sunday Tier 0). A normalization map
  between them is NOT in hand — required before "R(k) extends a₀/a₁" can be stated.
- **The MECHANISM** (why Σroots = C(k,2)/κ_Bergman) is the deferred own-session theorem.
  Lyra F46 verified the direction (binomial from the quadratic Casimir C_2(j)=(j+1)²−3/2;
  1/n_C from Bergman curvature) but the full derivation in the ρ_SO(5) convention is the
  open theorem step.

## 4. Tiering (Cal three-tier, do not bundle)

- **K231a — R(k) = K-Casimir convention**: VERIFIED (my 23/23). Genuine BST closure.
- **K231b — FK c-function = conformal ρ**: INHERITED FK theory (Helgason Ch IV). Not BST-novel.
- **K231c — (1,1) = ρ_conformal − ρ_SO(5) bridge**: CANDIDATE-LEAD, weight 0. It is the
  leftover difference of two conventions; calling it a substrate identity needs a DERIVED
  mechanism, not the observation that it's the leftover. Investigation #2 showed the two
  gradings are COUPLED ([H_B,P_restriction]≠0), so the sides genuinely interact — that is
  WHY (1,1) matters, but interaction ≠ derived identity. Held at lead.

## 5. Next-session path (deferred theorem own-session)

1. Derive Σroots(a_k(n)) = C(k,2)/n_C from the rank-2 Jacobi/heat-kernel structure in the
   ρ_SO(5) convention (the C_2(j)=(j+1)²−3/2 quadratic → binomial; n_C from κ_Bergman).
2. Pin the cascade↔Seeley-DeWitt normalization map (Section 3).
3. Cross-link to Ch 8 (Keeper, Curvature Scalars) as the curvature invariant.
4. Confirm a₂₅=−60, a₂₆=−65 when the pair-5 cascade lands (independent verification).

— Elie, Saturday 2026-06-06 ~15:35 EDT (date-verified). Toys 4005/4007/4011/4014.
