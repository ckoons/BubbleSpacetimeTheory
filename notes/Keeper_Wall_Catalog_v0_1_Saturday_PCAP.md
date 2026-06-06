---
title: "Keeper Wall Catalog v0.1 — Saturday Phase 5 connected wall system + team attack organization"
author: "Keeper (Claude Opus 4.7)"
date: "2026-06-06 Saturday ~13:25 EDT (`date`-verified actual)"
status: "v0.1 organizer document. Saturday substrate-architectural wall system catalog + team attack assignments per Casey directive 'don't give up; examine each wall carefully.' Six connected walls with explicit dependency structure; Wall 1 (Lyra F46 c-function) is the keystone; closing it opens Walls 2 + 6 and reshapes 3. Substantive contribution: explicit closed form for the 2(k+1) substrate-natural offset between naive conformal ρ-shift and K-Casimir ρ-shift, derived as 2λ·(ρ_conformal − ρ_K) where the shift vector (ρ_conformal − ρ_K) = (1, 1). This identity makes the offset explicit + substrate-natural, narrowing Lyra's Hypothesis A/B/C fork."
---

# Wall Catalog v0.1 — Saturday Phase 5 Connected Wall System

## 0. Purpose

Casey directive Saturday afternoon: "let's see what might force that relation that opens the door, don't give up examine each wall carefully. Please organize our work and the board for the team to look at the various problems and to learn more."

This document organizes the team's substantive substrate-architectural walls hit Saturday afternoon as a CONNECTED SYSTEM. Walls are not independent; they form a dependency graph with Wall 1 (Lyra F46 c-function normalization) as the keystone.

## 1. The connected wall system

```
                    Wall 1 (R(k) c-function)
                    LYRA primary attack
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
        Wall 2          Wall 6      Wall 3
       (F45 muon)     (a_k forms)  (Reading (a)
       Elie scan      Multi-week    consequences)
              │                          │
              └──────────┬───────────────┘
                         ▼
                   Sub-PCAP closing
                   (multi-week)

   Parallel walls (independent of Wall 1):
   Wall 4 (D2 representational complexity) — Grace primary
   Wall 5 (R-6 / Direction A vs B / coding) — Grace + Lyra
```

## 2. Wall 1 — Lyra F46 c-function normalization (KEYSTONE)

### 2.1. The wall as stated

Per Lyra F46: "I tried to derive why R(k) = C(k,2)/κ_Bergman and hit a real wall. The direction is verified: the binomial comes from the quadratic Casimir, the 1/n_C from the Bergman curvature. But the exact c-function normalization that would nail it doesn't reproduce the recorded Casimirs from the naive ρ-shift (it gives 4.5/11.5/20.5, not 2.5/7.5/14.5)."

### 2.2. Substantive substrate-architectural diagnosis (Keeper contribution)

The two ρ-vectors at issue:
- **ρ_K = ρ_SO(5) = (3/2, 1/2)** — half-sum of positive roots of SO(5)
- **ρ_conformal = (n_C/rank, (n_C − 2)/rank) = (5/2, 3/2)** — conformal ρ for D_IV⁵

**Difference vector**:
$$\rho_{\text{conformal}} - \rho_K = (5/2 - 3/2,\; 3/2 - 1/2) = (1, 1)$$

**The 2(k+1) offset as closed-form Keeper identity**:

For K-Casimir formula $C(λ) = \sum_i (λ_i + ρ_i)^2 - \sum_i ρ_i^2$, the difference between conformal-shifted Casimir and K-Casimir at K-type $V_{((2k+1)/2, 1/2)}$ is:

$$C^{\text{naive}}(λ) - C^K(λ) = 2 \, λ \cdot (\rho_{\text{conformal}} - \rho_K)$$

(the squared terms cancel between expansion of the two ρ-shifts; only the linear cross-term survives).

For $λ = ((2k+1)/2, 1/2)$ and shift vector $(1, 1)$:
$$C^{\text{naive}}(λ) - C^K(λ) = 2 \cdot \left[\frac{2k+1}{2} \cdot 1 + \frac{1}{2} \cdot 1\right] = 2 \cdot \left[\frac{2k+1+1}{2}\right] = 2(k+1)$$

**Verification against Lyra's recorded values**:
- $k = 0$: $C^K = 5/2 = 2.5$; offset $2(0+1) = 2$; $C^{\text{naive}} = 2.5 + 2 = 4.5$ ✓
- $k = 1$: $C^K = 15/2 = 7.5$; offset $2(1+1) = 4$; $C^{\text{naive}} = 7.5 + 4 = 11.5$ ✓
- $k = 2$: $C^K = 29/2 = 14.5$; offset $2(2+1) = 6$; $C^{\text{naive}} = 14.5 + 6 = 20.5$ ✓

The offset closed form is exact and substrate-natural. This is the substantive substrate-architectural diagnostic that narrows Lyra's hypothesis fork.

### 2.3. The substantive substrate-architectural question (sharpened)

The 2(k+1) offset is NOT noise — it is exactly $2 \, λ \cdot (\rho_{\text{conformal}} - \rho_K)$ with substrate-natural shift vector $(1, 1)$. The question is **which ρ-shift the substrate forces for R(k)**.

**Hypothesis A — K-Casimir convention forces R(k)**:
The heat trace on $H^2(D_{IV}^5)$ decomposes per K-type; each K-type contributes its K-Casimir per spectral decomposition theorem. Therefore R(k) uses K-Casimirs (2.5/7.5/14.5). The conformal ρ-shift appears in the FK Plancherel formula's c-function but NOT in the spectral coefficient extraction. R(k) = C(k,2)/κ_Bergman closes via K-Casimir normalization.

Status: **strongest substrate-architectural a priori** (heat trace = sum over K-types per Peter-Weyl). Lyra to verify.

**Hypothesis B — Conformal ρ forces R(k); Casimir relation is different**:
The c-function shift is mandatory at the substrate-mechanism level. R(k) = C(k,2)/n_C still holds numerically (Elie verified) but derives from a different mechanism — not the K-Casimir spectral decomposition.

Status: substantively weaker (would mean Elie's R(k) numerical pattern is coincidence + different mechanism; reduces R(k) to "lead" not "candidate theorem").

**Hypothesis C — Dual ρ structure; R(k) bridges them**:
Both ρ-vectors have substrate-architectural roles. The c-function uses ρ_conformal; the spectral decomposition uses ρ_K. R(k) is the bridge: $R(k) = C(k,2)/n_C$ relates them via a substrate-natural identity involving the shift vector $(1, 1)$.

Status: **substantively most interesting** — preserves both substrate-architectural conventions; the (1, 1) shift vector identity above MAKES this bridge explicit. Lyra to investigate.

### 2.4. Substrate-architectural significance of the (1, 1) shift vector

The shift vector $(\rho_{\text{conformal}} - \rho_K) = (1, 1)$ deserves substrate-architectural attention. Possible substrate interpretations:

1. **Strongly orthogonal roots half-sum**: for D_IV⁵, the strongly orthogonal positive non-compact roots structure has a known half-sum related to the genus / domain dimension. The (1, 1) shift may equal this half-sum.

2. **Rank-vector "1, 1"**: rank = 2, two components both = 1. Substrate-natural rank-decomposition.

3. **Unit vector in K-type label space**: the shift advances both K-type labels by 1. Could relate to substrate-K-type ladder operation.

4. **Conformal weight derivative**: difference between conformal ρ and K-ρ reflects the conformal embedding of K into the conformal group. (1, 1) may equal the K-conformal weight differential.

Lyra: any of these substrate-natural readings of (1, 1) might be the substantive substrate-architectural FORCING that picks Hypothesis A vs C.

## 3. Wall 2 — Lyra F45 N_c⁴ = 81 K-type for muon edge-term

### 3.1. The wall as stated

Per Lyra F45: m_μ/m_e = 207 under Reading (a) needs distinct H² K-type structure. The 81 = N_c⁴ edge-term needs a K-type whose matrix coefficient produces 81 natively. Lyra noted: "it's not a standard heat-trace coefficient."

### 3.2. Wall 1 → Wall 2 dependency

Lyra noted explicitly: "F45 and the R(k) theorem are the same heat-trace question." If Wall 1 closes (Hypothesis A or C), R(k) supplies a_k(n_C) polynomial. Specific a_k may contain N_c⁴ coefficient naturally — giving Wall 2 a clean closure.

If R(k) under Hypothesis A: $a_k = $ binomial-over-curvature × specific polynomial coefficient. The N_c⁴ structure would appear at specific k where the polynomial has degree 4 in N_c.

### 3.3. Disposition

Wall 2 attack deferred until Wall 1 produces. Elie's PRIMARY batch (K-type scan for 81) becomes more focused after Wall 1 closure.

## 4. Wall 3 — Reading (a) propagation consequences

### 4.1. The wall as stated

Per Lyra F44 Reading (a) commitment: no physical (1−P) complement. Consequences:
- Composite v0.5 additive split fails (m_μ/m_e = 207 needs re-derivation)
- F37 / F38 / F40 v0.2 hygiene (deferred to EOD/sundown)
- Sub-PCAP closing path depends on Wall 2 closure or honest T190 retreat

### 4.2. Wall 1 + Wall 2 → Wall 3 sharpening

Wall 3 is the consequence of Walls 1+2. Substantive resolution:
- Wall 1 closes (R(k) theorem) → Wall 2 has substantive content for muon K-type
- Wall 2 closes (81 = K-type matrix coefficient) → Composite v0.5 re-derivation under Reading (a) lands cleanly
- F45 succeeds → Reading (a) commitment fully consistent with muon ratio

If Wall 2 cannot close cleanly: honest fallback to T190 single-object form for m_τ/m_e (Lyra F45's stated alternative).

## 5. Wall 4 — D2 representational complexity operationalization

### 5.1. The wall as stated

Per Grace's AC graph: D2 ("inverse-Casimir slope −1 law") is more load-bearing than D1 — a D2 null refutes H_B = Casimir identity itself. But D2 requires operational "representational complexity" axis for cognitive tasks.

### 5.2. Possible forcing

**K-Casimir IS the natural complexity axis**: D2 derives from $τ_{\text{coh}} \propto 1/C$ where $C$ is the K-Casimir of the state's K-type. Cognitive tasks that engage different K-types have different effective Casimirs.

Operational definition: representational complexity of a cognitive task = weighted sum of K-Casimirs of the K-types the task representation spans.

This makes D2 measurable: vary K-type complexity systematically (via tasks of differing representational dimensionality / abstraction), measure coherence window, verify slope −1.

### 5.3. Grace primary attack

Grace's lane: AC graph routing for D2 measurement protocol with K-Casimir as complexity proxy. Independent of Wall 1 (can run in parallel).

## 6. Wall 5 — R-6 / Direction A vs B / coding-theory three-formalism convergence

### 6.1. The wall as stated

Per Grace's earlier finding: three independent formalisms (Lyra rep theory + Grace AC graph + coding theory) collapse to ONE question — is the CKM observable rate-level (sin²θ_C) or amplitude-level (sin θ_C)?

Lyra Direction A (rate, color² natural as two-trace) disfavored per F39 walk-back (relocates N_c² to N_c⁴).
Lyra Direction B (amplitude, two-color-sum endpoint) survives.

### 6.2. Possible forcing

Substantive bridge: Lyra Direction B substrate-mechanism connects to coding-theoretic d² (Hamming distance squared = second-moment rate measure) via substrate-operator producing two independent color sums.

Question: what substrate operator on H² produces N_c² as amplitude squared-norm matching coding-theoretic d² rate?

### 6.3. Grace secondary + Lyra coordination

Grace AC graph routing for substrate-operator bridge to coding theory; Lyra Direction B substrate-mechanism FORWARD when Wall 1 settles (independent in priority but related substantively).

## 7. Wall 6 — Heat-trace a_k higher-order substrate-natural forms

### 7.1. The wall as stated

Sunday Tier 0 v0.1.6: $a_0 = (N_c \cdot n_C)^2 = 225$, $a_1 = -N_c \cdot n_C^4 = -1875$ explicit substrate-natural closed forms. Higher-order $a_k$ expected substrate-natural but not derived.

### 7.2. Wall 1 → Wall 6 dependency

R(k) closed form on D_IV⁵ → $a_k$ structure as binomial-over-curvature × substrate-natural polynomial.

Closing R(k) at Hypothesis A or C gives explicit $a_k$ formula for all k.

### 7.3. Disposition

Wall 6 attack follows Wall 1 closure. Multi-week per Lyra Tier 0 v0.2+.

## 8. Wall attack assignments (organized for the team broadcast)

Per Saturday team broadcast 13:20 EDT:

| Wall | Status | Primary | Support | Parallel? |
|---|---|---|---|---|
| **Wall 1** R(k) c-function | KEYSTONE attack now | Lyra | Elie (numerical) + Keeper (organizer + (1,1) shift identity) | — |
| **Wall 2** F45 N_c⁴ K-type | Deferred until Wall 1 produces | Lyra (substrate-mechanism) + Elie (computational) | — | No |
| **Wall 3** Reading (a) consequences | Sharpens with Wall 1+2 closures | Lyra | Keeper hygiene v0.2 | No |
| **Wall 4** D2 representational complexity | PARALLEL attack now | Grace | — | Yes |
| **Wall 5** R-6 / Direction B / coding | PARALLEL attack now | Grace | Lyra coordination | Yes |
| **Wall 6** Heat-trace a_k forms | Multi-week after Wall 1 | Lyra Tier 0 v0.2+ | — | No |

## 9. Substantive substrate-architectural meta-observation

Casey's framing "let's see what might force that relation that opens the door" reflects substrate-architectural discipline:
- The 2(k+1) offset is NOT a calculation error — it's a substrate-natural difference between two valid ρ-shifts
- "The mistake" Lyra named is actually a HYPOTHESIS FORK requiring substantive substrate-mechanism FORCING
- The (1, 1) shift vector is itself substrate-natural and deserves substrate-architectural attention

This is substantively the same pattern as Saturday morning's K-audit cascade discipline: the brake event (Cal #259 (1−P) catch) sharpened the question (Reading (a) commitment). Lyra's "wall" sharpens the heat-trace question (Hypothesis A vs B vs C).

The discipline holds across the day: brake events + walls are substantively the same — moments where substantive substrate-architectural questions become explicit. Casey directive "examine each wall carefully" extends "Cal #27 STANDING: claims-tier framing, NOT halting investigation" to substantive substrate-mechanism FORWARD work.

## 10. Pre-staged K-audit candidates (Keeper reactive)

- **K231 PRE-STAGE**: Lyra F47 R(k) theorem closure when Lyra fires Wall 1 closure (Hypothesis A or C)
- **K232 PRE-STAGE**: Lyra F48 muon edge-term re-derivation under Reading (a) when Wall 2 closes
- **K233 PRE-STAGE**: Grace D2 representational complexity operationalization when Wall 4 closes

All pre-staged audit categories will use σ-distance discipline (Cal #256) + Refinement B level pin (Cal v0.17 + Keeper v0.2 STANDING) + Cal #189 substrate-mechanism FORWARD criteria.

## 11. Cross-link to Vol 16 Ch 8 (Curvature Scalars)

Vol 16 Ch 8 v0.1 (Keeper Saturday morning) has Section 3 on heat-trace coefficients $a_0 = 225$, $a_1 = -1875$. When Wall 1 closes (R(k) theorem), Ch 8 v0.2 absorbs:
- R(k) closed form as substrate-curvature invariant
- $a_k$ binomial-over-Bergman-curvature structure
- Substrate-architectural significance: heat-trace coefficients are substrate-curvature integrals; R(k) closed form quantifies the substrate-curvature contribution per K-type

This consolidates Lyra's heat-kernel work + Casey's Curvature Principle + Keeper Vol 16 Ch 8 framework into one substrate-curvature ledger.

---

**Keeper Wall Catalog v0.1 — Saturday 2026-06-06 13:25 EDT (`date`-verified actual). Six connected walls organized; Wall 1 (Lyra F46 c-function) keystone; closing it opens Walls 2 + 6 and reshapes 3. Substantive Keeper contribution: (1, 1) shift vector closed form for 2(k+1) substrate-natural offset, derived as 2λ·(ρ_conformal − ρ_K). Hypothesis fork (A K-Casimir / B conformal / C dual ρ bridge) sharpened. Team attack assignments per Saturday team broadcast. Pre-staged K231-K233 reactive on wall closures. Cross-link to Vol 16 Ch 8 v0.2 when Wall 1 closes. Substrate-architectural discipline: walls + brakes are substantively the same — moments where substantive substrate-mechanism questions become explicit.**
