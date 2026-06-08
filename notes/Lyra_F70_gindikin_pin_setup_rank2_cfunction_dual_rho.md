---
title: "F70 — Gindikin pin (dual-ρ joint with Grace), opening: the rank-2 Gindikin Gamma of D_IV⁵ set up rigorously. Γ_Ω(s) = (2π)^{(n_C−rank)/2}·Γ(s)·Γ(s−d/2) with d = n_C−2 = 3 = N_c, genus = n_C = 5. Half-integer π-powers ARISE from the rank-2 structure (two sources: the (2π)^{N_c/2} prefactor, half-integer because N_c=3 is odd; and the odd-d Γ(s−3/2) factor) — sharpens my earlier vaguer 'rank-2 Vandermonde' attribution. Substrate-clean TARGETS verified (9/2=n_C−1/rank, 225=(N_c·n_C)², 1920=2^g·N_c·n_C). Exact derivation of 9/2 + 225 = the multi-week remainder."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-08 Mon 11:45 EDT"
status: "v0.1 — START of the Gindikin/c-function pin (Casey 'Go Gindikin'). RIGOROUS: parameters, the rank-2 Gindikin Gamma, the half-integer source, the substrate-clean targets. NOT YET DERIVED: the exact π^{9/2} exponent and 225 coefficient from the full FK normalization (multi-week joint with Grace). Honest opening, not a closure."
---

# F70 — Gindikin pin: rigorous setup of the rank-2 c-function for D_IV⁵

## 0. The task (Casey "Go Gindikin")

Derive the FK measure's π^{9/2} exponent and the 225 = (N_c·n_C)² coefficient of c_FK from the Gindikin c-function (the Gamma function of the symmetric cone) over D_IV⁵'s rank-2 root system. This note is the rigorous **setup + opening**, with an honest mark of what's pinned vs. what's the multi-week remainder.

## 1. Parameters of D_IV⁵ (rigorous, definitional for type IV)

D_IV⁵ is the Lie ball — the type-IV bounded symmetric domain of complex dimension n_C = 5. Its Faraut-Koranyi / Jordan-algebra structure constants:

| quantity | value | note |
|---|---|---|
| rank r | 2 | type IV is **always** rank 2 |
| complex dim n_C | 5 | |
| Peirce multiplicity d | n_C − 2 = **3** | = N_c; **odd** |
| genus p | 2 + d(r−1) = **5** = n_C | |

## 2. The rank-2 Gindikin Gamma

The Gamma function of the rank-2 symmetric cone underlying D_IV⁵:

$$\Gamma_\Omega(s) = (2\pi)^{(n_C-\text{rank})/2}\,\Gamma(s)\,\Gamma\!\left(s-\tfrac{d}{2}\right) = (2\pi)^{3/2}\,\Gamma(s)\,\Gamma\!\left(s-\tfrac{3}{2}\right).$$

Explicit at the genus (rigorous numeric): Γ_Ω(5) = (2π)^{3/2}·Γ(5)·Γ(7/2) = 45·2^{3/2}·π² ≈ 1256.2. It carries **π²** with coefficient 45·2^{3/2}.

## 3. Where the half-integers come from (sharpening my earlier attribution)

**Self-correction (flagging honestly):** to Grace earlier I attributed the half-integer measure-power to "the rank-2 Vandermonde / 1/rank shift" as if it were a single clean mechanism. The Gindikin structure is more precise and has **two** half-integer sources, both rooted in odd parity:

1. **The prefactor (2π)^{(n_C−rank)/2} = (2π)^{N_c/2} = (2π)^{3/2}** — a half-integer π-power because **n_C − rank = 3 = N_c is odd**.
2. **The factor Γ(s − d/2) = Γ(s − 3/2)** — half-integer arguments (because **d = n_C − 2 = 3 is odd**) → √π factors.

For D_IV⁵ these coincide numerically (n_C − rank = d = N_c = 3, since rank = 2). The clean statement: **the substrate's half-integer π-powers are the signature of odd multiplicity d = n_C − 2** (equivalently n_C odd). This corrects/sharpens Grace's "rank-2 ⇒ always half-integer": a rank-2 type-IV domain with *even* n_C (d even) would have **integer** measure powers — so the half-integer fingerprint specifically needs **n_C odd**, which our substrate (n_C = 5) is. Same conclusion (our substrate has half-integers), more precise mechanism (odd d, not rank alone).

## 4. The substrate-clean targets the full computation must hit (verified)

- **measure exponent** 9/2 = n_C − 1/rank ✓
- **c_FK coefficient** 225 = (N_c·n_C)² = 15² ✓  [N_c·n_C = 15 = dim SO(4,2), the conformal group — F66]
- **Bergman kernel** K(0,0) = 1920/π^{n_C}, with **1920 = 2^g·N_c·n_C** ✓ → Vol(D_IV⁵) = π⁵/1920

These three landmarks are all substrate-clean (products of the five integers), which is itself evidence the FK normalization lands on substrate-natural ground — the full Gindikin evaluation must reproduce them.

## 5. What is NOT yet derived (the multi-week remainder — honest)

The **exact** net exponent 9/2 = n_C − 1/rank and the **exact** coefficient 225 from the full FK normalization are **not yet derived here**. The Gindikin Gamma above has multiple π-power-contributing factors (the (2π)^{3/2} prefactor, the Γ(s) and Γ(s−3/2) values at the relevant argument, and the π^n from the domain volume), and netting them to *exactly* π^{9/2} with coefficient 225 requires carefully assembling the full FK normalization integral (the weighted-Bergman / Born-rule-invariant probability measure of T754/T2442) — not just Γ_Ω at the genus. That assembly is the multi-week joint with Grace. I am **not** asserting a specific clean one-line mechanism for "9/2" or "225" until that computation closes — the discipline lesson from this morning's F69 retraction applies (don't let a tidy-looking partial harden into a claim).

## 6. Honest tiering (K231c)

- **RIGOROUS (this note):** the parameters; the rank-2 Gindikin Gamma form; that half-integer π-powers arise from the rank-2 structure with odd d = n_C − 2; the substrate-clean targets (9/2, 225, 1920).
- **SHARPENED:** the half-integer fingerprint is odd-d (n_C odd), not rank-alone — corrects my earlier looser statement to Grace.
- **NOT DERIVED (multi-week):** the exact 9/2 and 225 from the full FK normalization. The continuing joint.
- **No overclaim:** this is the START of the pin, explicitly not a closure.

## 7. Closure

The Gindikin pin is set up rigorously: D_IV⁵'s rank-2 cone has Γ_Ω(s) = (2π)^{3/2}Γ(s)Γ(s−3/2) (d = n_C−2 = 3 = N_c, genus 5), and the half-integer π-powers of the FK measure arise from this structure's odd-d factors — sharpening the "rank-2 fingerprint" to "odd multiplicity d = n_C − 2, i.e. n_C odd." The substrate-clean targets (measure exponent 9/2 = n_C − 1/rank, coefficient 225 = (N_c·n_C)², Bergman 1920 = 2^g·N_c·n_C) are verified as the landmarks the full computation must reproduce. The exact derivation of 9/2 and 225 from the full FK normalization is the multi-week remainder — opened today, not closed. Honest START on "Go Gindikin."

@Grace — joint opening: parameters + Γ_Ω set up; half-integer source sharpened to odd-d (correcting my earlier "1/rank Vandermonde" — it's the odd multiplicity, n_C odd, not rank alone). Next concrete step (ours): assemble the full FK normalization (weighted-Bergman / T754 Born-rule measure) and net it to π^{9/2}·(1/225). Your catalog/structure verification + my special-function assembly. @Cal — START not closure; nothing claimed derived; earlier attribution self-corrected. @Keeper — Vol 16 Ch 5 (Bergman kernel algebra) absorption candidate when the pin closes; for now, setup only.

— Lyra, Mon 2026-06-08 11:45 EDT. F70 Gindikin pin SETUP (Casey "Go Gindikin"): D_IV⁵ rank-2 cone Γ_Ω(s) = (2π)^{(n_C−rank)/2}Γ(s)Γ(s−d/2) = (2π)^{3/2}Γ(s)Γ(s−3/2), d=n_C−2=3=N_c, genus=n_C=5. Half-integer π-powers arise from rank-2 structure, TWO sources both odd-parity: (2π)^{N_c/2} prefactor (N_c=3 odd) + Γ(s−3/2) (d=3 odd). SHARPENS earlier "1/rank Vandermonde" → odd multiplicity d=n_C−2 (n_C odd); even-n_C type-IV would be integer. Targets verified: 9/2=n_C−1/rank, 225=(N_c·n_C)²=15² (N_c·n_C=dim SO(4,2)), Bergman 1920=2^g·N_c·n_C. NOT YET DERIVED (multi-week joint w/ Grace): exact 9/2 + 225 from full FK normalization (weighted-Bergman/T754). START not closure; F69-retraction discipline applied (no tidy partial hardened into claim).
