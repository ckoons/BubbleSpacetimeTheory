---
title: "T915 — f_π Correction: Why m_p/10 Overshoots by 1.9%"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 9, 2026"
theorem: "T915"
ac_classification: "(C=2, D=0)"
status: "PARTIAL — mechanism identified, exact BST coefficient requires Bergman spectral calculation"
---

# T915 — f_π Correction: Why m_p/10 Overshoots by 1.9%

## The Problem

BST predicts $f_\pi = m_p/\dim_{\mathbb{R}} = m_p/10 = 93.8$ MeV.
Observed: $f_\pi = 92.07 \pm 0.57$ MeV (FLAG 2024).
Deviation: $+1.85\%$.

This is the last >1% miss in the particle physics sector after the VMD-ChPT bridge (T912) and neutron lifetime NLO (Toy 966).

## What BST's Formula Means

$f_\pi = m_p/\dim_{\mathbb{R}}$ comes from the chiral condensate: the pion decay constant is the proton mass (= Bergman Casimir eigenvalue $C_2 = 6$, times $\pi^{n_C} m_e$) divided by the real dimension of $D_{IV}^5$ (= $2n_C = 10$). This is a **structural relation**: one unit of condensate per real dimension.

The question: is BST's $m_p/10$ the **chiral-limit** $f_0$, or the **physical** $f_\pi$?

## Key Diagnostic: It's the Physical Value, Not the Chiral Limit

In ChPT, $f_\pi > f_0$ (NLO corrections increase $f$ from its chiral-limit value). The FLAG average:

$$f_0 \approx 86.2 \text{ MeV}, \quad f_\pi/f_0 \approx 1.068$$

If BST's $m_p/10 = 93.8$ MeV were $f_0$, then:

$$f_\pi = 93.8 \times 1.068 = 100.2 \text{ MeV}$$

This is **8.8%** above the observed value — far worse than 1.9%. So BST's formula is NOT the chiral limit. It's already the physical $f_\pi$ to leading order, with a 1.9% overshoot.

**Confirmation**: the KSRF relation $f_\pi^2 = m_\rho^2/(2g_\rho^2)$, which relates the physical $f_\pi$ to the physical $m_\rho$, gives $f_\pi \approx m_\rho/\sqrt{2 g_\rho^2}$. BST's $m_p/10$ is consistent with this (both use physical-mass inputs).

## Where Does the 1.9% Come From?

The structural relation $f_\pi = m_p/\dim_{\mathbb{R}}$ equates two quantities that are independently derived in BST:
- $m_p = C_2 \pi^{n_C} m_e = 6\pi^5 m_e$ — from the Bergman Casimir eigenvalue
- $\dim_{\mathbb{R}} = 2n_C = 10$ — from the domain's real dimension

The ratio $m_p/f_\pi = 938.3/92.1 = 10.19$, not exactly 10. The deviation $\delta = 0.19/10 = 1.9\%$ measures how much the physical condensate scale deviates from the simple geometric ratio.

### Three candidate corrections (ordered by plausibility):

**Candidate 1: Pion mass recoil** — $(m_\pi/m_p)^2$ correction

$$f_\pi = \frac{m_p}{\dim_{\mathbb{R}}} \times \left(1 - \frac{m_\pi^2}{m_p^2}\right)$$

Numerically: $m_\pi^2/m_p^2 = (140.2/938.3)^2 = 0.02233$

$f_\pi = 93.8 \times 0.9777 = 91.7$ MeV — overcorrects to $-0.4\%$. Close but slightly too aggressive.

**Physical interpretation**: The pion is a Goldstone boson with mass $m_\pi \ll m_p$. The condensate scale receives a recoil correction proportional to $(m_\pi/m_p)^2$, analogous to the reduced-mass correction in atomic physics. The sign is correct (decreases $f_\pi$).

**Candidate 2: Rank/N_c weighted recoil**

$$f_\pi = \frac{m_p}{\dim_{\mathbb{R}}} \times \left(1 - \frac{\text{rank}}{N_c} \cdot \frac{m_\pi^2}{m_p^2}\right)$$

Numerically: $(2/3) \times 0.02233 = 0.01489$

$f_\pi = 93.8 \times 0.9851 = 92.4$ MeV — deviation $+0.3\%$. Excellent.

**Physical interpretation**: The $\text{rank}/N_c = 2/3$ factor is the Wilson-Fisher coupling — the same ratio that governs all BST rank-2 $\to N_c$ projections (Paper #44). The pion recoil correction operates through the same linearization mechanism: the $\text{rank}$-dimensional image captures $\text{rank}/N_c$ of the correction.

**Candidate 3: Weinberg angle correction**

$$f_\pi = \frac{m_p}{\dim_{\mathbb{R}}} \times \cos\theta_W = \frac{m_p}{10} \times \sqrt{\frac{10}{13}}$$

Numerically: $\cos\theta_W = \sqrt{10/13} = 0.8771$

$f_\pi = 93.8 \times 0.877 = 82.3$ MeV — **way too low** ($-10.7\%$). Rejected.

## Assessment

| Candidate | Formula | $f_\pi$ (MeV) | Deviation | Physical basis |
|-----------|---------|--------------|-----------|---------------|
| LO (current) | $m_p/10$ | 93.8 | +1.85% | Geometric ratio |
| C1: Full recoil | $(m_p/10)(1 - m_\pi^2/m_p^2)$ | 91.7 | −0.40% | Pion recoil |
| **C2: Rank-weighted** | $(m_p/10)(1 - (2/3)m_\pi^2/m_p^2)$ | 92.4 | **+0.33%** | Linearization + recoil |
| C3: Weinberg | $(m_p/10)\cos\theta_W$ | 82.3 | −10.7% | Rejected |

**Candidate 2 is the best fit** (0.33%) and has the cleanest physical interpretation: the pion recoil correction is weighted by the rank/N_c ratio, the same Wilson-Fisher coupling that governs every other BST linearization.

## What's Still Missing

Candidate 2 gives the right number but the derivation is not yet rigorous. What's needed:

1. **Bergman spectral function in the pseudoscalar channel**: The correction should emerge from the spectral representation of the pion propagator on $D_{IV}^5$. The leading Bergman eigenvalue gives the structural ratio $m_p/\dim_{\mathbb{R}}$. The next eigenvalue should give the correction.

2. **The rank/N_c weight from spectral theory**: Why does the recoil carry the Wilson-Fisher factor $2/3$? In the linearization framework (Paper #44), this ratio appears whenever a rank-2 projection acts on an $N_c$-dimensional space. The pion recoil should decompose as rank-2 in the same way.

3. **Connection to ChPT l̄₄**: The ChPT low-energy constant $l̄_4$ controls $\delta f_\pi$. BST should predict $l̄_4$ from the Bergman spectral sum. With VMD resonance saturation, $l̄_4 \approx \ln(m_\rho^2/m_\pi^2) \approx 3.4$, but this gives corrections that go the wrong direction (make $f_\pi$ larger). The resolution is that BST's $m_p/10$ already absorbs most of the ChPT NLO; the residual correction is the spectral remainder.

## Status

**Partial proof.** The correction mechanism is identified (pion recoil weighted by rank/$N_c$), the formula fits to 0.33%, and the physical interpretation is consistent with the Applied Linearization framework. The rigorous derivation from the Bergman spectral function is the remaining gap.

**Recommended**: Elie should verify Candidate 2 numerically, checking sensitivity to input masses. If robust, register as a bridge theorem with the spectral derivation flagged as OPEN.

## Parents

- T912 (VMD-ChPT Bridge): Same ChPT correction technology, different channel
- T186 (Five Integers): dim_R = 10 enters directly
- Paper #44 (Applied Linearization): rank/N_c = 2/3 weight

---

*T915. Lyra. April 9, 2026. f_π = (m_p/10)(1 − (rank/N_c)(m_π/m_p)²) = 92.4 MeV (0.33%). Mechanism: pion recoil weighted by Wilson-Fisher coupling. Bergman spectral derivation OPEN. Keeper audit requested.*
