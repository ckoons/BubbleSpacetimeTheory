---
title: "F36 (F24 v0.2) — Substrate-color² source: the amplitude-vs-rate diagnosis + share-an-operator discipline on the 45 cross-link"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 11:55 EDT"
status: "v0.2 — multi-week, tracked-open (Action Item 4, NOT a Saturday-close). Reframes the color² OPEN from 'which of 4 ways to make 9' to the amplitude/color-trace tension; downgrades the N_c²·n_C=45 PMNS↔CKM link to LEAD"
---

# F36 (F24 v0.2) Substrate-Color² Source — Diagnosis

## 0. Goal and scope

Advance the substrate-color² open question (the N_c² numerator in sin θ_C) at depth. **Tracked-open, not a Saturday-close** per Casey Action Item 4. v0.1 (F24) enumerated three candidate sources for N_c²=9 and found none clean. This v0.2 does something more useful than a fourth candidate: it diagnoses *why* the search has stalled and reframes the open question into a sharper, falsifiable one. AC(0): count the color powers first.

## 1. The identification is essentially exact (positive sharpening)

$$\sin\theta_C \;\overset{?}{=}\; \frac{N_c^2}{2^{N_c}\cdot n_C} = \frac{9}{40} = 0.22500$$

The Friday notes compared this to |V_us| from kaon decays (0.2243, "0.31%"). The cleaner comparison is the **Wolfenstein parameter λ = 0.22500** (PDG), and against it the form is exact to all five digits (0.000%). So the *identification* is excellent — better than previously stated. The problem was never the precision. It is the mechanism for N_c² sitting in an amplitude.

## 2. The real blocker: N_c² in an amplitude (color counting)

sin θ_C is an **amplitude** (a CKM matrix element, |V_us|/λ), not a rate. In the substrate reading it is an off-diagonal matrix element between generation K-types,

$$\sin\theta_C \sim \langle V_{\text{gen-1}}\otimes\text{color}\mid T_W\mid V_{\text{gen-2}}\otimes\text{color}\rangle.$$

The Standard Model weak current is **color-diagonal** (T_W = I on color). A color-diagonal amplitude carries exactly **one** color trace — Tr(I₃) = N_c — when summed over the color index. To get N_c² you need **two independent color sums**, which is the signature of a **rate** (|amplitude|², two color loops) or of a genuinely two-endpoint color structure, not of a single tree-level color-singlet amplitude.

So the N_c² numerator is anomalous *as an amplitude factor*. This is the precise blocker, and it is sharper and more actionable than the v0.1 framing ("9 = N_c² = (rank+1)² = 2^{N_c}+1 = C_2+N_c, four ways"). The Casey #5 integer-multiplicity of 9 is a symptom; the disease is the amplitude/color-trace mismatch.

## 3. Two honest resolution directions (both multi-week, both need the explicit matrix element)

- **Direction A — the forced object is the rate.** If the substrate forces λ² (a rate) rather than λ (an amplitude), then N_c² is the natural two-color-trace factor of |color-singlet amplitude|², and λ = √(rate) inherits N_c². Test: is the substrate's primitive observable in the quark-mixing sector the *probability* sin²θ_C = (9/40)² = 81/1600 = 0.050625 (= λ², exact), with sin θ_C derived as its root? If yes, the color² is forced by the rate's two color sums. This is the cleaner of the two and reframes the whole CKM-sector search toward rates.
- **Direction B — two-endpoint color sum.** If the gen-1 and gen-2 K-types each carry an *independent* color sum in the Bergman inner product (initial-quark color ⊥ final-quark color, not tied by a single δ), the amplitude carries N_c×N_c. This is v0.1 candidate (c). It requires showing the substrate matrix element does **not** reduce to a single color trace — which the explicit FK Bergman color-tensored matrix element must decide. v0.1 found the Sym^k cross-index gives 3, not 9, so Direction B is not yet supported and must not be asserted.

Neither is closed. The point of v0.2 is that the search is now **two sharp falsifiable questions** (is the primitive a rate? does the matrix element carry one color trace or two?) instead of an open-ended hunt for a factor of 9.

## 4. Discipline flag — the N_c²·n_C = 45 PMNS↔CKM link is a LEAD, not a candidate

The Saturday board has Grace adding N_c²·n_C = 45 as the **6th G14 candidate** ("one substrate primitive crossing quark + lepton mixing sectors"), citing PMNS sin²θ₁₃ = 1/45 and CKM sin θ_C ∝ N_c²/(2^{N_c}·n_C).

Apply the same discipline Cal applied to the 28-cross-link and I applied to the 81/40 vacuum factor (F35): **share an operator, not an integer.**

- In PMNS, N_c² sits in the **denominator** (1/45 = 1/(N_c²·n_C)).
- In CKM, N_c² sits in the **numerator** (9/40).
- The "shared primitive" is the **integer N_c²** appearing on opposite sides of two different observables — a shared *number*, with no shared *operator* yet exhibited.

Per the standing discipline this is a **LEAD**, not a Schur-generator candidate. It becomes a candidate only if a single substrate operator is shown to produce N_c² in *both* sectors (e.g., the same color-tensored mixing operator, with the rate/amplitude distinction explaining why it lands in numerator vs denominator). **Grace — recommend logging 45 as a LEAD in G14 v0.3, not a candidate, pending that operator.** This keeps G14 honest and consistent with the 28-link and 81/40 calls.

## 5. What v0.2 closes and what stays open

**Closed/sharpened by this note:**
- Identification quality corrected upward: 9/40 = λ exactly (0.000%), not 0.31%.
- The OPEN reframed from "which of 4 ways to make 9" → the **amplitude/color-trace tension** (N_c² in an amplitude needs two color sums).
- Two falsifiable directions named (A: rate-primitive; B: two-endpoint color sum).
- The 45 PMNS↔CKM link downgraded to LEAD (integer-shared) per share-an-operator discipline.

**Open (multi-week, Cal #189):**
- Compute the explicit FK Bergman color-tensored mixing matrix element; count its color traces (decides A vs B).
- Determine whether the substrate's CKM-sector primitive is the rate sin²θ_C or the amplitude sin θ_C.
- Promote 45 from LEAD to candidate only on a shared operator.

## 6. Closure

F36 (F24 v0.2): the substrate-color² source for sin θ_C is reframed. The form 9/40 = λ is an essentially exact identification; its forcing is blocked by N_c² sitting in an amplitude, where a color-diagonal current gives only one color trace (N_c). The productive next questions are sharp and falsifiable — is the primitive a rate (Direction A, color² natural as a two-trace) or does the matrix element carry two independent color sums (Direction B). The N_c²·n_C = 45 PMNS↔CKM cross-link is a LEAD (shared integer), not a Schur candidate, until one operator produces N_c² in both sectors — flagged to Grace before G14 v0.3.

**Tier:** F36 (F24 v0.2) diagnostic forward step; substrate-color² source OPEN reframed to amplitude-vs-rate; multi-week per Cal #189; tracked-open, NOT Saturday-close.

— Lyra, Sat 2026-06-06 11:55 EDT. F36 (F24 v0.2): 9/40 = Wolfenstein λ exactly (0.000%, sharpened from Friday's 0.31% vs kaon |V_us|); OPEN reframed from Casey-#5 multiplicity of 9 to the amplitude/color-trace tension (N_c² in an amplitude needs two color sums; color-diagonal current gives one trace = N_c); two falsifiable directions — A rate-primitive sin²θ_C (color² natural as two-trace), B two-endpoint color sum (needs explicit FK matrix element, v0.1 Sym^k gave 3 not 9 so unsupported); N_c²·n_C=45 PMNS↔CKM downgraded to LEAD (shared integer not shared operator) per share-an-operator discipline — flag to Grace for G14 v0.3; multi-week, tracked-open.
