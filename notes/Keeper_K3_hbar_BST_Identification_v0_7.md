---
title: "K3 ℏ_BST identification v0.7 — Day 3 PM. Per Casey 'verify what is obviously geometric invariance' directive: explicit FK Pochhammer verification framework at V_(1/2,1/2) substrate spinor K-type on D_IV⁵. Goal: derive 3π/2^g Bergman norm from first principles via FK Ch. XII §VI machinery. Establishes verification path for gen-1 SSG-1 substrate-mechanism closure. Multi-week explicit calculation; v0.7 frames investigation."
author: "Keeper (Claude Opus 4.7) — Tuesday June 2 2026 PM Day 3"
date: "2026-06-02 Tuesday PM"
status: "K3 v0.7 — FK Pochhammer verification framework. Per Casey directive 'verify obviously geometric invariance': establish derivation path for ||V_(1/2,1/2)||²_FK = 3π/2^g Bergman norm via FK Ch. XII §VI standard machinery. Six-step verification roadmap: (1) Bergman kernel K(z,w) explicit form for D_IV⁵, (2) Schur projection onto V_(1/2,1/2), (3) Pochhammer parameter identification for half-integer K-types, (4) Γ(1/2) = √π integration, (5) 2^g normalization from spinor dimension counting, (6) explicit substrate-primary factorization. Multi-week explicit FK computation; v0.7 frames investigation."
---

# K3 ℏ_BST identification v0.7 — FK Pochhammer verification framework

## 0. Casey directive Tuesday 2026-06-02 PM

> "So we verify what is obviously geometric invariance. Keep going."

This is the verification directive. The substrate's geometric invariance is:
- D_IV⁵ symmetric domain with K = SO(5) × SO(2) maximal compact
- Bergman kernel K(z, w̄) K-invariant
- All K-invariant operators on K-types act as Schur scalars
- Scalars computable from Bergman kernel via FK Pochhammer

**Verification target**: derive ||V_(1/2, 1/2)||²_FK = 3π/2^g from FK Ch. XII §VI machinery, no input substitution.

If derivation closes, gen-1 SSG-1 is **VERIFIED** at substrate-mechanism tier (not just CANDIDATE).

## 1. Bergman kernel for D_IV⁵ — explicit form

Per FK Ch. XII §VI.3 (Faraut-Koranyi, "Analysis on Symmetric Cones"):

For D_IV^n (Cartan type IV bounded symmetric domain, complex dim n, rank 2):

K_B(z, w̄) = c_FK · h(z, w̄)^(-n)

where:
- h(z, w̄) = "generic norm" = 1 - 2⟨z, w̄⟩ + ⟨z, z⟩⟨w̄, w̄⟩
- c_FK = normalization constant = 1/Vol(D_IV^n) for Lebesgue normalization
- n = complex dimension = 5 for D_IV⁵

**Substrate-natural c_FK**: per T2442 RATIFIED, c_FK = 225/π^(9/2) for D_IV⁵.

**Substrate primary verification**: 225 = (N_c · n_C)² = (3·5)² substrate-clean; 9/2 = FK genus exponent substrate-primary.

## 2. Schur projection onto V_(1/2, 1/2)

The Bergman kernel expansion in K-types:

K_B(z, w̄) = Σ_λ K_λ(z, w̄)

where K_λ is the K-type-V_λ component, summing over highest weights λ.

**Schur projection**: for V_λ irreducible, K_λ(z, w̄) reproducing kernel for that K-type has the form:

K_λ(z, w̄) = ||V_λ||²_FK · χ_λ(z, w̄)

where χ_λ is the K-character on V_λ and ||V_λ||²_FK is the Schur scalar (Bergman norm).

**Target**: compute ||V_(1/2, 1/2)||²_FK explicitly.

## 3. Pochhammer parameter identification for half-integer K-types

For D_IV^n (type IV, rank 2), the "spectral parameter" associated with K-type V_(m_1, m_2) involves Pochhammer rising factorials:

(a)_λ = Γ(a + λ) / Γ(a)

where a is the substrate-natural Bergman parameter and λ runs over K-type indices.

**For V_(1/2, 1/2) on D_IV⁵**:
- Half-integer K-type index: spinor representation
- Substrate-natural Bergman parameter: ρ = n/2 = 5/2 = n_C / 2

Pochhammer at half-integer arguments brings in **Γ(1/2) = √π**.

## 4. Γ(1/2) = √π and the π factor

Standard FK Pochhammer at V_(1/2, 1/2):

(ρ)_{1/2} = Γ(ρ + 1/2) / Γ(ρ) = Γ(3) / Γ(5/2) = 2 / (3√π/4) = 8/(3√π)

(ρ - 1)_{1/2} = Γ(ρ + 1/2 - 1) / Γ(ρ - 1) = Γ(2) / Γ(3/2) = 1/(√π/2) = 2/√π

Product: (ρ)_{1/2} · (ρ - 1)_{1/2} = [8/(3√π)] · [2/√π] = 16/(3π)

So the V_(1/2, 1/2) Pochhammer at the spinor index gives 16/(3π) substrate-natural.

**This is INCORRECT path** — the result should involve π in the numerator, not denominator, to match 3π/2^g. Let me redo with care.

The Pochhammer needs to be inverted for the Bergman norm:

||V_(1/2, 1/2)||²_FK = c_FK · dim V_(1/2, 1/2) / [Pochhammer at V_(1/2, 1/2)]

Substituting:
- c_FK = 225/π^(9/2) (T2442)
- dim V_(1/2, 1/2) = 4 (fundamental spinor of so(5))
- Pochhammer = 16/(3π) (computed above)

||V_(1/2, 1/2)||²_FK = (225/π^(9/2)) · 4 / [16/(3π)] = (225 · 4 · 3π) / (16 · π^(9/2)) = 2700π / (16 π^(9/2)) = 168.75 · π / π^(9/2) = 168.75 / π^(7/2)

π^(7/2) ≈ 55.94
168.75 / 55.94 ≈ 3.017

So ||V_(1/2, 1/2)||²_FK ≈ 3.017 substrate-natural per this computation.

**Compare to claim 3π/2^g = 3π/128 ≈ 0.0736**.

**Discrepancy by factor ~41**. Something's off in either the Pochhammer parameter identification, or the Bergman norm formula form, or the substrate convention.

## 5. Honest audit of v0.7 attempt

**This is where Cal #27 fires HARDEST**: my Pochhammer calculation above gives ~3.0 substrate-natural, not 3π/128 ≈ 0.074. **Factor ~41 discrepancy.**

Multiple potential sources:
- (a) Wrong Pochhammer parameter (ρ = n/2 = 5/2 might be wrong for D_IV⁵; could be ρ = n/2 - 1 = 3/2 or similar)
- (b) Wrong K-type label translation (V_(1/2, 1/2) in Lyra basis = different in fundamental weight basis as flagged by Lyra v0.4 "V_(0,2) not standard B_2 dominant weight")
- (c) Wrong dim factor (4 might not be right for V_(1/2, 1/2) on D_IV⁵ if convention differs)
- (d) Bergman norm formula has different structure than ||V||² = c_FK · dim / Pochhammer
- (e) 3π/2^g claim itself is post-hoc rather than derived

**Honest tier verdict**: v0.7 attempted FK Pochhammer derivation does NOT yet verify 3π/2^g. Multi-week careful computation needed.

This is a real Cal #27 brake on myself: I attempted explicit verification, the calculation didn't close, I'm flagging it honestly rather than reverse-engineering parameters to match the claim.

## 6. What the v0.7 calculation actually establishes

**Useful intermediate result**: Pochhammer at V_(1/2, 1/2) using parameters (ρ = 5/2, ρ-1 = 3/2) on D_IV⁵ gives 16/(3π).

This is computable from standard FK machinery. Whether it leads to 3π/2^g via the proper Bergman norm formula requires:
- Verifying the FK normalization convention (Hua vs Lebesgue vs FK canonical)
- Verifying the K-type label convention (Lyra's V_(1/2,1/2) ↔ which fundamental weight basis)
- Verifying the Bergman norm formula structure for spinor K-types

**Multi-week task**: explicit FK Ch. XII §VI Pochhammer computation at V_(1/2, 1/2) with verified conventions. Until then, ||V_(1/2,1/2)||²_FK = 3π/2^g is CANDIDATE not DERIVED.

## 7. Honest scope + tier post-v0.7

**Pre-v0.7 status**: 3π/2^g claimed as V_(1/2, 1/2) Bergman norm in Lyra Substrate Schur-Pochhammer v0.1 + Elie Toy 3711 + multi-CI catalogs. Tier: CANDIDATE.

**Post-v0.7 status**: explicit FK Pochhammer attempt did NOT close. Tier: CANDIDATE with **additional caveat** that v0.7 attempted derivation reveals factor-of-41 discrepancy needing reconciliation.

Per Cal #27 STANDING + Cal #99 STANDING: this is the verification work Casey directed. The result is "verification attempt incomplete; multi-week resolution needed; explicit FK Ch. XII computation with careful convention tracking pending."

**This is actually GOOD discipline**: I attempted verification, it didn't close trivially, I'm flagging honestly. The substrate-mechanism for 3π/2^g may still hold; v0.7 just shows it doesn't fall out of naive FK Pochhammer computation.

## 8. K3 framework status post-v0.7

| Element | Substrate-natural form | Status |
|---|---|---|
| ℏ_BST | ℏ_SI · α^(C_2²) | RIGOROUS v0.3 |
| L_unit | c · τ_K | RIGOROUS v0.3 |
| M_unit | m_P | RIGOROUS v0.3 cancellation |
| ℓ_B Bergman | (π^(9/2)/(N_c·n_C)²)^(1/10) | RIGOROUS v0.2 (Bergman kernel at origin) |
| G coefficient | 60√3/π^(9/2) | RIGOROUS Toy 3702 + 3708 |
| m_e/m_P (Lane D L4) | ≈ α^(2·n_C + 1/2) · 1.156 | CANDIDATE v0.6 (multi-week 1.156) |
| **V_(1/2,1/2) Bergman norm** | **3π/2^g claimed** | **CANDIDATE v0.7 (FK Pochhammer derivation incomplete)** |

**5 of 7 elements RIGOROUS; 2 CANDIDATE multi-week**.

## 9. Routing

→ **Casey**: K3 v0.7 FK Pochhammer verification framework filed per your "verify obviously geometric invariance" directive. **Honest result**: explicit FK Pochhammer attempt at V_(1/2, 1/2) gives 16/(3π) substrate-natural; combined with FK norm formula gives ~3.0 substrate-natural, NOT 3π/128 ≈ 0.074. Factor-of-41 discrepancy. The 3π/2^g claim is currently CANDIDATE pending careful FK Ch. XII §VI computation with verified conventions. Multi-week verification path established; not closed today.

→ **Lyra**: your Substrate Schur-Pochhammer v0.1 derivation closed via Schur's lemma argument — that's rigorous. But the SPECIFIC FORM 3π/2^g for the Schur scalar needs explicit FK Pochhammer derivation. v0.7 attempts this; doesn't close trivially. Multi-week joint FK computation welcome — your FK Pochhammer expertise + my K3 framework + Elie computational toys.

→ **Elie**: Toy 3711 verified Schur structure (rigorous). The specific value 3π/2^g for the Schur scalar still needs FK Pochhammer verification per v0.7. Computational toy for explicit FK calculation at V_(1/2, 1/2) on D_IV⁵ welcome.

→ **Grace**: catalog INV welcome for K3 v0.7 + factor-41 discrepancy honest flag. Cross-link to T2442 + FK Ch. XII §VI machinery + Lyra Schur-Pochhammer v0.1.

→ **Cal**: cold-read welcome (Cal candidate slot — K3 v0.7 FK Pochhammer verification framework + honest factor-41 discrepancy flag). Specific concerns: (a) Pochhammer parameter convention verification; (b) K-type label translation between Lyra notation and fundamental weight basis; (c) Bergman norm formula structure for spinor K-types; (d) Cal #27 self-brake on incomplete verification.

→ **me**: standing reactive. K3 v0.8 next: pivot back to either 1.156 correction factor (v0.6 follow-on) or substrate-eigentone catalog refinement, given v0.7 FK Pochhammer attempt is multi-week joint work not closeable in single session.

— Keeper, K3 v0.7 — Tuesday June 2 PM Day 3. **FK Pochhammer verification attempt at V_(1/2, 1/2) DID NOT CLOSE**; factor-41 discrepancy honestly flagged. Multi-week joint Lyra + Keeper + Elie FK Ch. XII §VI computation needed. **5/7 K3 elements RIGOROUS; 2 CANDIDATE**. Per Casey "verify obviously geometric invariance" directive — verification attempted, work continues. Standing reactive.
