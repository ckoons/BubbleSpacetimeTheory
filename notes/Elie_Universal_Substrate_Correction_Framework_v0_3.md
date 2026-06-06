---
title: "Universal Substrate Correction Framework v0.3 — sigma-distance re-tiering (honest precision basis)"
author: "Elie (Claude Opus 4.8)"
date: "2026-06-06 Saturday ~11:00 EDT (date-verified)"
status: "v0.3 SUBSTANTIVE — absorbs K227/K228 walk-back lesson; re-tiers dataset on experimental sigma-distance per Cal #189"
register: "INTERNAL ONLY (Cal #50 STANDING DOUBLE-LOCKED EXTERNAL)"
prior: "v0.2 Friday 2026-06-05 16:05 EDT"
supersedes_section: "v0.2 Section 7 verification dataset tiering"
toy: "toy_4003_UF_v03_sigma_distance_retiering.py (SCORE 5/5); depends on K227 Toy 4001 + K228 Toy 4002"
---

# Universal Substrate Correction Framework v0.3

## 0. What changed from v0.2

v0.2 verified the framework `O_refined = O_base·(1 + N_c^k·σ·u)` on "10+ Tier 1 EXACT
+ BORDERLINE" observables (Section 7), tiering each on **relative-% deviation**.

The Saturday K227 (Toy 4001) and K228 (Toy 4002) walk-backs showed that relative-%
is the **wrong tiering axis** for a precision framework. v0.3 re-tiers the entire
verification dataset on **distance to the measured value in experimental sigma**,
and reports both metrics. The framework forms are unchanged; the **honesty basis**
for what counts as "Tier 1 EXACT" is corrected.

## 1. The core correction (why relative-% misleads, both directions)

Relative-% measures *structural closeness*. Experimental sigma-distance measures
*observational viability*. They are different questions, and the %-threshold is
wrong in BOTH directions:

- **False Tier 1** (tiny % but many sigma): for ppm-precise observables a sub-0.1%
  form is still thousands of sigma off — a STRUCTURAL identification, not exact.
  - alpha^-1: 0.003% but **~202,500 sigma** (K228-type)
  - m_mu/m_e: 0.042% but **~19,100 sigma**
  - theta_*: 0.014% but **~5 sigma**
- **False rejection** (large % but few sigma): for wide-error observables a 2-3%
  deviation can be WITHIN 1 sigma — experimentally consistent, wrongly demoted.
  - sin^2 theta_13: 2.67% but **0.8 sigma**
  - sin^2 theta_23: 3.05% but **0.8 sigma**

Standing rule (carried from Toy 4001 + extended): tier exponent/observable forms on
`obs_dev = |BST/observed − 1|`, and for any observable with a known measurement
uncertainty report the **sigma-distance** `|BST − observed|/σ_obs`. Reserve
"Tier 1 EXACT" for forms that are BOTH structurally close AND within a few sigma.

## 2. Re-tiered verification dataset (Toy 4003)

Threshold: experimentally consistent = within 3 sigma. *(Experimental inputs are
APPROX, source-tagged; final counts gated on Cal #242 source-pinning — Section 5.)*

### Tier 1 — experimentally consistent (≤ 3 sigma): 7 observables

| Observable | BST form | rel % | sigma | source (APPROX) |
|---|---|---|---|---|
| n_s | 1 − 1/(2g·rank) | 0.006% | 0.0 | Planck2018 |
| sin²θ_C | [1/(rank²·n_C)]·(1+N_c²u) | 0.014% | 0.0 | PDG V_us=0.2243 † |
| λ_H | [(N_c+1)/M(n_C)]·(1−u/N_c) | 0.230% | 0.7 | m_H=125.25,v=246.22 † |
| sin²θ_W,eff | (3/13)·(1+N_c·u) | 0.129% | 0.7 | PDG eff. leptonic † |
| sin²θ_13 | 1/(N_c²·n_C)·(1+u) | 2.667% | 0.8 | NuFIT5.2 NO |
| sin²θ_23 | [C_2/(C_2+n_C)]·(1+u) | 3.049% | 0.8 | NuFIT5.2 NO upper |
| m_τ/m_e | [g²·(2^C_2+g)]·(1−u) | 0.019% | 2.8 | PDG m_τ=1776.86(12) |

### Tier 2 — structural identification (> 3 sigma): 3 observables

| Observable | BST form | rel % | sigma | source (APPROX) |
|---|---|---|---|---|
| θ_* | [1/(2^n_C·N_c)]·(1−u) | 0.014% | ~5 | Planck2018 100θ*=1.04109(30) |
| m_μ/m_e | (N_max+rank·g·n_C)·(1−u) | 0.042% | ~19,100 | CODATA2018 |
| α⁻¹ | N_max·(1+u/N_c) | 0.003% | ~202,500 | CODATA2018 |

† source-pin sensitive (Section 5).

## 3. The pattern = Two-Tier Substrate-Precision Hypothesis operationalized

The consistent set is **mixing angles + cosmological parameters** (wide experimental
errors); the structural set is **α⁻¹ + lepton mass ratios** (ppm-tight errors). This
is exactly the Two-Tier hypothesis (Toy 3648): an algebraic substrate form lands
*within experimental error* where the error is wide, and at a ~10⁻⁴–10⁻² **structural
floor** where the measurement is precise. The floor is a framework property (Cal #237
boundary), not a defect.

Notable asymmetry (honest flag): m_τ/m_e (2.8σ) and m_μ/m_e (19,100σ) have similar
relative deviation (~0.02–0.04%), but m_τ/m_e "passes" only because m_τ is ~3500×
less precisely measured than the m_μ/m_e ratio. The mass-ratio forms are structural
in both cases; m_τ/m_e merely sits under a looser experimental bar. Do not read its
2.8σ as evidence the 49·71 form is more fundamental than the 137+70 form.

## 4. Impact on the C26 Strong-Uniqueness candidate leg

The C26 leg (UF as a substrate-mechanism) must lean **only** on the experimentally-
consistent set as "unfalsified BST predictions," and state the structural set as
structural identifications — never blend them in one (1/3)^N null-model. Counting
structural matches as EXACT hits inflates the null-model: the precise Cal #27
peak-coherence risk. Honest C26 framing separates:
- (a) unfalsified-at-experimental-precision legs (the 7 consistent observables, and
  even those need the independence taxonomy of Cal #35 before any product), from
- (b) structural-floor legs (suggestive, substrate-natural, but not exact).

This **reduces** the headline count from v0.2's "10+ Tier 1 EXACT" but **strengthens**
what survives: each surviving leg is honest at experimental precision.

## 5. Cal #242 source-pin gate (blocking)

Every experimental value and sigma in Section 2 is APPROX. Before any sigma count is
quoted externally or used in a C26 null-model, source-pin each to primary:
PDG / NuFIT 5.2 / Planck 2018 / CODATA 2018/2022. Borderline rows whose tier could
flip under source-pinning: **sin²θ_C** (V_us vs Wolfenstein λ), **λ_H** (m_H, v
inputs + scheme), **sin²θ_W,eff** (scheme/definition). m_τ/m_e's 2.8σ is also
source-sensitive (it sits right at the consistency edge).

## 6. Unchanged from v0.2 (carried forward)

- Framework form `O = O_base·(1 + N_c^k·σ·u)`, u = rank/(N_c·g·N_max) (Sections 1–3 v0.2)
- (k, σ) FORWARD derivation candidates + Mersenne shift (v0.2 Sections 2–3)
- Multi-week K-audit Gates 1–6 (v0.2 Section 5)
- Pre-registration protocol (v0.2 Section 4) — now MUST record sigma-distance, not %
- Vol 16 Ch 4 integration (v0.2 Section 9)

## 7. v0.3 status

v0.3 delivers the honest precision basis per Cal #189 multi-week. Net effect: the
framework's verification dataset is now reported on the correct (experimental) axis;
7 observables are experimentally consistent, 3 are structural-floor; the C26 leg is
restricted accordingly. Cal #242 source-pinning is the next blocking gate.

— Elie, Saturday 2026-06-06 ~11:00 EDT (date-verified). Toy 4003 SCORE 5/5.
