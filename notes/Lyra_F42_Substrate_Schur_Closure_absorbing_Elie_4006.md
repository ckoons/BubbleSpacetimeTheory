---
title: "F42 — substrate-Schur closure absorbing Elie Toy 4006: κ=81/8 FORCED (F40 closed), Direction-B resolved (F39 closed, FRAMEWORK), ε held open honestly (F38 — Elie's rounding-artifact catch); P promoted to strong FRAMEWORK candidate, NOT STANDING"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 14:00 EDT"
status: "v0.1 — sub-PCAP closure. 2 of 3 endpoints close (κ FORCED, Direction-B FRAMEWORK); ε is the single honest residual (not fished; target rounding-limited per Elie 4006). Substrate-Schur P = strong FRAMEWORK candidate."
---

# F42 Substrate-Schur Closure (absorbing Elie Toy 4006)

## 0. Goal

Close the three substrate-Schur endpoints (F38 ε, F39 Direction-B, F40 κ) using Elie's explicit FK color-tensored Szegő computation (Toy 4006). Honest accounting: two close, one is held open — and held open *correctly*, because Elie caught that its target is a rounding artifact.

## 1. F40 — κ = 81/8: CLOSED (FORCED)

Elie Toy 4006 G2–G3 forces the muon edge-term:

- **G2 (rigorous):** the Shilov boundary ∂_S D_IV⁵ = S⁴ × S¹/ℤ₂ is a product, so its reproducing (Szegő) kernel factorizes, S_Shilov = S_{S⁴}·S_{S¹/ℤ₂}, and **any** boundary matrix element factorizes: κ = κ_{S⁴}·κ_{S¹}. This is my F40 structural pin, now rigorous (product ⟹ product kernel).
- **G3 (geometry rigorous + color FRAMEWORK rule):** κ_{S⁴} = N_c^{dim S⁴} = N_c⁴ (color trace once per boundary dimension; **exponent 4 = dim S⁴ = codim-4, Casey #14 — pinned**), κ_{S¹} = 2^{−N_c} (ℤ₂ quotient, ½ per color). Product = N_c⁴·2^{−N_c} = **81/8.**

So the muon Hardy-(1−P) boundary matrix element = N_c⁴/2^{N_c} = 81/8 is **substrate-FORCED** (F32 Gate A1 / K229d closed). The geometry (factorization, dim S⁴ = 4) is rigorous; the color-trace-per-dimension + ℤ₂-per-color action is FRAMEWORK-tier. Honest tier: **κ CLOSED at FRAMEWORK-FORCING** (the exponents pinned by geometry; the color rule is the one FRAMEWORK assumption).

## 2. F39 — CKM Direction-B: CLOSED (FRAMEWORK); the fork resolves

Elie G5 supplies the explicit color factors: each boundary endpoint carries one N_c color trace (per S⁴), and the two endpoints give N_c². This resolves the F39 fork:

$$\sin\theta_C = \frac{N_c^2}{2^{N_c}\cdot n_C} = \frac{9}{40} = \lambda,\qquad N_c^2 = \underbrace{N_c}_{\text{gen-1 endpoint}}\times\underbrace{N_c}_{\text{gen-2 endpoint}}.$$

The N_c² in the amplitude is **two independent endpoint color traces** — Direction-B, not Direction-A. The two quark endpoints sit at distinct boundary points (gen-1 and gen-2 K-types), each contributing one color trace, summed independently in the boundary matrix element; the denominator 2^{N_c}·n_C = 40 is the boundary normalization. So 9/40 = λ is substrate-FORCED in form.

**Honest tier and flag:** this is FRAMEWORK, not RIGOROUS. It is substrate-specific — it *departs* from the SM picture, where the charged-current amplitude conserves color and carries a single trace. The claim is that the substrate boundary matrix element carries two independent traces because the endpoints are distinct boundary points not tied by a single color δ. That is supported by Elie's boundary factorization but is a substrate structural assumption, not an SM-derived fact. F39 fork **resolved toward B at FRAMEWORK tier.** (And per F36: 9/40 = λ exactly, so the identification was never in doubt — only the mechanism, now Direction-B.)

## 3. F38 — ε: HELD OPEN (correctly), with two reasons not to fish it

Factor = 1 + ρ; the Hardy isometry forces ρ = 1 (F38), so **Λ factor = 2 is DERIVED** — and now doubly backed: Elie's G2 establishes the same Szegő factorization rigorously, so the bulk/boundary double-count that gives the 2 rests on rigorous geometry. **This is the robust, closed content: the cosmological factor-2 is the Hardy vacuum double-count, a mechanism, not a fit.**

ε = the correction. I am **not** closing it, for two reasons — one mine, one Elie's:

- **(mine, a self-correction):** F38 asserted ε > 0 ("factor > 2") from a hand-wave that the Bergman exponent (7/2) exceeds the Szegő (5/2) so the bulk is "heavier." On reflection that sign argument is **not cleanly defensible** without the explicit integral — which space carries the vacuum, and in which measure, determines the sign, and the Shilov boundary (where the Hardy norm concentrates) can make E^bdy ≳ E^bulk for the opposite reason. **I walk back the F38 ε-sign claim.** ε's sign and magnitude require the explicit κ_Bergman-weighted per-region integral (Elie's G4 inputs: exponent gap = rank/2 = 1; κ_Bergman = −n_C = −5; c_FK; Shilov volume 8π³/3).
- **(Elie's catch, decisive):** the observed "ε = 2.0208 − 2 = 0.0208" is a **rounding artifact** of the meV inputs (Λ^{1/4}: 4.85 / 2.4, each ~2–3 sig figs). So ε is not even *measured* to better than tens of percent — 1/48 = 0.02083 and 1/50 = 0.02 both sit in the noise. **Fishing ε is wrong twice over:** no mechanism (Cal #35) and no precise target (input rounding).

Honest tier: **factor = 2 DERIVED; ε is a small correction below current theory *and* data resolution** — the single genuine residual. It closes only via the explicit integral *and* better input precision. Not today, and not by fishing.

## 4. Cal #254 confirmed at the constant level (the real prize)

Elie 4006 confirms what F37 proposed: the muon edge-term (81/8) and the Λ factor-2 use the **same Szegő factorization** — literally the same projection-P / Shilov geometry computed once. The shared object across the mass sector and the cosmological sector is an **operator (P), not an integer.** This is "share an operator, not an integer" (Cal #254) carried all the way to the explicit constant. That, not any single number, is the substrate-Schur result.

## 5. Net: P promoted to strong FRAMEWORK candidate — NOT STANDING

| Endpoint | Status | Tier |
|---|---|---|
| F40 κ = 81/8 (muon edge) | CLOSED | FRAMEWORK-FORCING (geometry rigorous; color rule FRAMEWORK) |
| F39 Direction-B (CKM N_c²) | CLOSED | FRAMEWORK (substrate-specific two-trace; departs from SM) |
| F38 Λ factor = 2 | DERIVED | Hardy isometry + Elie G2 rigorous |
| F38 ε correction | OPEN | needs explicit integral + better inputs; NOT fished |

The Hardy/Bergman projection **P is a strong, coherent FRAMEWORK candidate** as a substrate-Schur generator: two sectors (muon mass, cosmological Λ) provably share its Szegő factorization. It is **not promoted to STANDING** — that would require (a) the color-trace-per-dimension rule derived (not assumed), (b) Direction-B's two independent traces justified beyond the substrate assumption, and (c) ε closed. Three honest gates remain. Calling this STANDING today would be exactly the over-promotion the day's discipline has been firing on.

## 6. Closure

Absorbing Elie Toy 4006: F40 (κ = 81/8) closes as substrate-FORCED; F39 (CKM color²) resolves to Direction-B at FRAMEWORK tier (two independent endpoint color traces; 9/40 = λ); F38's Λ factor-2 is DERIVED (Hardy isometry, rigorously backed), and ε is held open correctly — walked back the F38 sign hand-wave, and Elie's catch that the 0.0208 target is a meV rounding artifact removes any basis for fishing it. The substrate-Schur generator P is a strong FRAMEWORK candidate — muon edge and Λ factor share one Szegő factorization (Cal #254 at the constant level) — not yet STANDING, with three named gates. Two of three endpoints closed; the third honestly held. Sub-PCAP closed.

**Tier:** F42 sub-PCAP closure; κ FRAMEWORK-FORCING + Direction-B FRAMEWORK CLOSED; factor-2 DERIVED; ε OPEN (not fished); P = strong FRAMEWORK candidate, 3 gates to STANDING.

— Lyra, Sat 2026-06-06 14:00 EDT. F42 substrate-Schur closure absorbing Elie 4006: F40 κ=N_c⁴·2^{−N_c}=81/8 FORCED (Shilov product factorization G2 rigorous + color-tensoring G3; exponent 4=dim S⁴=codim-4 Casey #14 pinned); F39 Direction-B CLOSED at FRAMEWORK (N_c²=two independent endpoint color traces, substrate-specific departs from SM single-trace, 9/40=λ); F38 Λ factor=2 DERIVED (Hardy isometry, Elie G2 rigorous backing) + ε HELD OPEN — walked back my F38 ε>0 sign hand-wave (not defensible without explicit integral) + Elie caught the 0.0208 target is a meV rounding artifact (1/48,1/50 in the noise), so ε not fished twice over; Cal #254 confirmed at constant level (muon-edge 81/8 + Λ-factor 2 use SAME Szegő factorization = operator P not integer); P promoted to strong FRAMEWORK candidate NOT STANDING (3 gates: color rule derivation, Direction-B justification, ε closure).
