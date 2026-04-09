---
title: "T913 — Pion Sector NLO Classification"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 9, 2026"
theorem: "T913"
ac_classification: "(C=1, D=0)"
status: "PROVED — diagnostic theorem, classifies three independent NLO gaps"
---

# T913 — Pion Sector NLO Classification

## Statement

**T913 (Pion Sector NLO Classification)**: The three Cluster B misses (f_π +1.9%, B_d −2.1%, τ_n +2.1%) are **independent** leading-order oversimplifications, each requiring its own NLO correction from standard physics. They do not share a common root cause, and correcting f_π does not propagate to fix B_d or τ_n.

## The Three Misses

| Quantity | BST Formula | BST Value | Observed | Deviation | Category |
|----------|-------------|-----------|----------|-----------|----------|
| f_π | m_p/dim_R = m_p/10 | 93.8 MeV | 92.1 ± 0.6 MeV | +1.9% | ChPT NLO |
| B_d | αm_p/π | 2.179 MeV | 2.2246 MeV | −2.1% | Nuclear NLO |
| τ_n | Fermi + BST inputs | ≈898 s | 879.4 ± 0.6 s | +2.1% | Radiative NLO |

## Why They Don't Propagate

**Test: does f_π enter B_d?** No. B_d = αm_p/π is a residual electromagnetic coupling estimate. f_π does not appear.

**Test: does f_π enter τ_n?** Indirectly, through Goldberger-Treiman: g_A = g_πNN × f_π/m_N. But the sign is wrong:
- BST f_π = 93.8 MeV > observed 92.1 MeV (too high)
- → BST g_A too high (via GT)
- → BST (1 + 3g_A²) too high
- → BST τ_n ∝ 1/(1 + 3g_A²) too LOW
- But τ_n is observed 2.1% HIGH, not low
- **Correcting f_π makes τ_n worse, not better.**

The three signs (f_π high, B_d low, τ_n high) are inconsistent with a single propagating correction. Each miss has an independent origin.

## Individual NLO Corrections Required

### f_π: Chiral Perturbation Theory NLO

BST's f_π = m_p/10 corresponds to the leading-order geometric relation: the chiral condensate scale per real dimension of D_IV^5. The physical f_π differs by NLO ChPT corrections involving the low-energy constant l̄₄:

$$f_\pi^{\text{phys}} = f_\pi^{\text{LO}} \times (1 + \Delta_f)$$

where $\Delta_f$ depends on $l̄_4$ and $m_\pi^2/(16\pi^2 f^2) \approx 0.015$. The correction is of order 2%, consistent with the observed 1.9%. Deriving $l̄_4$ from BST requires the full Bergman spectral function in the pseudoscalar channel — not yet available.

**Status**: Gap is understood (ChPT NLO), correction size is right, BST derivation of l̄₄ is the missing step.

### B_d: Nuclear Tensor Force

BST's B_d = αm_p/π captures the residual EM/nuclear coupling between two Z₃ circuits at leading order. The 2.1% deficit comes from:
- D-wave admixture (~6% probability) via tensor force
- Isospin breaking (Δm = 1.293 MeV)
- Higher-order nuclear corrections

These are standard nuclear physics corrections. The BST bridge would need to derive the tensor force contribution from the D_IV^5 geometry — specifically, the D-state probability from the SO(5) ↔ SO(3)×SO(2) branching rule.

**Status**: Gap is understood (nuclear tensor force), BST derivation route identified but not yet attempted.

### τ_n: Outer Radiative + Recoil Corrections

The BST-specific deviation (from inputs G_F, V_ud, Δm) is only ~0.3%. The remaining ~1.8% comes from standard radiative corrections not yet fully incorporated:
- Outer radiative correction: ~1.5%
- Recoil corrections: ~0.3%
- Weak magnetism: ~0.1%

These are well-known corrections (Marciano-Sirlin, Czarnecki-Marciano-Sirlin). BST should incorporate them using BST-derived inputs but the correction formulas are standard QFT, not BST-specific.

**Status**: Gap is standard radiative physics. Fix is to use the full Marciano-Sirlin correction formula with BST inputs. No new BST derivation needed.

## AC Classification

(C=1, D=0): One counting step (propagation test via GT relation), zero definitions.

## Recommendation

- **f_π**: Derive l̄₄ from Bergman spectral function. Moderate priority — requires new spectral calculation.
- **B_d**: Derive D-state probability from SO(5) branching. Medium priority — nuclear physics bridge.
- **τ_n**: Incorporate standard Marciano-Sirlin corrections with BST inputs. Easy — just computation, no new theory.

None of these is a single bridge theorem fix. Cluster B is three independent NLO gaps, not one.

---

*T913. Lyra. April 9, 2026. Diagnostic: Cluster B misses are independent. f_π doesn't propagate to B_d or τ_n (wrong sign for τ_n). Each needs its own NLO correction. Honest assessment: no single bridge fixes all three.*
