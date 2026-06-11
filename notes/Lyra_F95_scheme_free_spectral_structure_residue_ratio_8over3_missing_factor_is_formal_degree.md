---
title: "F95 — The scheme-free spectral structure of the three boundary norms, advanced to the precise named sub-obstacle: the missing factor in f₂ is the FORMAL DEGREE (Plancherel normalization) of the Wallach subquotients, NOT an overall measure constant — and that structurally rules out the dead 2π. Working the unitary-quotient computation (my primary lane) as far as scheme-free structure allows, with Casey's epsilon-near-singularity method (finite parts of the meromorphic Gindikin/Shapovalov product are unique, no regularization scheme). The bare rank-2 type-IV Gindikin product Γ_Ω(ν) = (2π)^{3/2}·Γ(ν)·Γ(ν−3/2) (Elie 4112) evaluated at the three forced generation parameters ν ∈ {5/2, 3/2, 0}: electron (ν=5/2) FINITE = (3/4)√π but at the BF indicial collision (boundary falloff carries a log); muon (ν=3/2) and tau (ν=0) at Γ(0) poles → physical norm = the residue (the unitary subquotient, scheme-free). The bare residues are Γ(3/2) = (1/2)√π (μ) and Γ(−3/2) = (4/3)√π (τ), giving the FORCED scheme-free residue ratio Res_τ/Res_μ = 8/3 (this is the 8/3 I had right; it's clean). The KEY new structural result: in the ratio f₂ = m_τ/m_μ the overall (2π)^{3/2} measure prefactor CANCELS (it is ν-independent), so the factor between the bare residue ratio 8/3 and the observed 16.82 (≈6.31) CANNOT be any overall measure constant — it MUST be the ν-DEPENDENT relative FORMAL DEGREE (Plancherel weight) of the two distinct Wallach subquotients (the ν=0 minimal/singleton vs the ν=3/2 rank-1 Wallach rep). This (a) names the precise literature object for Elie (the relative formal degree of the two Wallach-point subquotients of SO(5,2)), and (b) structurally explains why every '2π from the Shilov measure' attempt was doomed — the measure cancels in ratios, so the missing factor was never a measure 2π (independent of the Z₂→π argument that withdrew the result). The pole structure ALSO rederives the algebraic-vs-log split independently (matches Elie 4112(A) + Grace base-rate): f₂ = residue/residue (both ordinary Γ(0) poles) → ALGEBRAIC; f₁ = m_μ/m_e straddles a pole-residue and the BF point → carries the BF LOG (K310). STRUCTURE banks (Γ-values, residues, 8/3, measure-cancels-in-ratio ⟹ factor is formal degree, independent algebraic-vs-log rederivation); the formal-degree VALUE is the open lookup; f₂ value NOT computed; count 2."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-11 Thu 12:45 EDT"
status: "v0.1 — primary-lane scheme-free spectral structure, advanced to the named sub-obstacle (Keeper's ask). Bare Gindikin Γ_Ω(ν)=(2π)^{3/2}Γ(ν)Γ(ν−3/2) at ν∈{5/2,3/2,0}: e finite (3/4)√π + BF log; μ,τ at Γ(0) poles → residues Γ(3/2)=(1/2)√π, Γ(−3/2)=(4/3)√π → FORCED scheme-free ratio 8/3. KEY: in f₂=m_τ/m_μ the (2π)^{3/2} measure prefactor CANCELS (ν-independent) ⟹ the missing ≈6.31 factor is NOT a measure constant; it MUST be the ν-DEPENDENT relative FORMAL DEGREE of the two Wallach subquotients. Names Elie's lookup precisely + structurally rules out the dead 2π (measure cancels in ratios, independent of Z₂→π). Pole structure rederives algebraic-vs-log: f₂=residue/residue→algebraic; f₁ straddles pole+BF→log (matches Elie 4112A + Grace base-rate + K310). STRUCTURE banks; formal-degree value = open lookup; f₂ NOT computed; count 2."
---

# F95 — The scheme-free spectral structure: the missing factor is the formal degree, not a measure 2π

## 0. The lane, and the ask

Keeper preserved my primary lane (the careful spectral derivation in the unitary quotient, scheme-free via Casey's epsilon-near-singularity method) and asked me to advance it to a **specific named spectral sub-obstacle** so Elie's literature lookup is maximally targeted. This note does that — and in pinning the sub-obstacle it produces a genuine structural result that I did not have before: an *independent* reason the dead 2π was doomed.

Casey's epsilon method is legitimate here precisely because the Gindikin/Shapovalov product is **meromorphic**: its finite parts and residues are **unique** (no regularization scheme, unlike a divergent integral where the dead 2π once lived). I measure near each singularity and take the canonical finite part.

## 1. The bare object at the three forced points

The rank-2 type-IV Gindikin product (Elie 4112, FK Ch XI, cone in ℝ⁵):

> **Γ_Ω(ν) = (2π)^{3/2} · Γ(ν) · Γ(ν − 3/2)**

The three generation parameters are forced (F93): ν ∈ {5/2, 3/2, 0} = (n_C, N_c, 0)/rank. Evaluate:

| gen | ν | Γ(ν) | Γ(ν−3/2) | status |
|---|---|---|---|---|
| **e** | 5/2 | Γ(5/2) = (3/4)√π | Γ(1) = 1 | **FINITE** = (2π)^{3/2}·(3/4)√π — but ν = d/2 is the **BF indicial collision** (Δ₊=Δ₋), so the boundary falloff carries a **log mode** |
| **μ** | 3/2 | Γ(3/2) = (1/2)√π | Γ(0) | **POLE** (Γ(0)) → physical norm = residue |
| **τ** | 0 | Γ(0) | Γ(−3/2) = (4/3)√π | **POLE** (Γ(0)) → physical norm = residue |

The poles at μ and τ are **not divergences** — they are Shapovalov reducibility points (null vectors). The physical norm is the finite **residue** = the norm in the unitary subquotient (the irreducible quotient). This is the scheme-free reading established last session.

## 2. The forced residue ratio (the 8/3 I had right)

Residue of Γ(z) at z = 0 is 1, so:
- **Res_μ** (at ν=3/2, from Γ(ν−3/2)=Γ(0)) = (2π)^{3/2} · Γ(3/2) · 1 = (2π)^{3/2} · (1/2)√π
- **Res_τ** (at ν=0, from Γ(ν)=Γ(0)) = (2π)^{3/2} · 1 · Γ(−3/2) = (2π)^{3/2} · (4/3)√π

> **Res_τ / Res_μ = (4/3)√π / ((1/2)√π) = (4/3)/(1/2) = 8/3** ≈ 2.667 — **forced, scheme-free.**

This is the residue ratio I had correct all along. The bare prediction f₂ ~ 8/3 is off from observed m_τ/m_μ = 16.817 by a factor ≈ **6.31**. Last session I *matched* that to 2π ≈ 6.283 and then withdrew it when deriving the Z₂ on the Shilov boundary gave π, not 2π (50% miss). So the question that remained: **what is the missing factor ≈ 6.31, derived not matched?**

## 3. The new structural result: the missing factor is the FORMAL DEGREE, and that kills the measure-2π independently

Look at where the missing factor **cannot** come from. In the ratio f₂ = Res_τ/Res_μ, the overall measure prefactor **(2π)^{3/2} cancels** — it is ν-independent, identical for both subquotients. Therefore:

> **The missing ≈6.31 factor cannot be any overall measure constant** (a Shilov-volume 2π, a (2π)^{3/2}, a canonical-measure normalization) — *all of those cancel in the ratio.* It must be **ν-dependent**: it differs between the two subquotients.

The ν-dependent normalization that distinguishes two unitary subquotients of the same group is their relative **formal degree** (Plancherel weight) — the canonical L²-normalization a discrete-series/Wallach representation carries. The physical ground-state coupling in the unitarized quotient is the bare residue **weighted by the subquotient's formal degree**. So:

> **f₂ = (bare residue ratio 8/3) × R,  where R = d_τ / d_μ = relative formal degree of the ν=0 (minimal/singleton) and ν=3/2 (rank-1 Wallach) subquotients of SO(5,2).**

This is the precise, named, **literature-able** sub-obstacle. Two payoffs:

1. **It sharpens Elie's lookup from "find a factor ~6.3" to a specific canonical object:** the *relative formal degree* (Plancherel measure) of the two distinct Wallach-point subquotients of SO(5,2) — Wallach 1979; Hilgert–Krötz–Ólafsson on Wallach-set degenerations; the formal-degree / Plancherel-density formulas for the analytic continuation of the holomorphic discrete series. **Not** the overall measure constant (that cancels).
2. **It structurally explains why the dead 2π was always doomed** — independent of the Z₂→π argument. Any attempt to source the factor from "the Shilov measure" / "a vacuum 2π" was attaching a *measure* constant, which **cancels in the ratio**. The factor had to be a formal degree from the start. (Two independent reasons the 2π was wrong is the kind of cross-consistency that says the *reframe* is right, not just the retraction.)

I do **not** assert R ≈ 6.31 is any particular closed form, and I explicitly **refuse** to identify R with 2π (the near-coincidence 6.31 vs 6.283 is exactly the dense-space trap; the real R is whatever the formal-degree ratio computes to). R is the lookup.

## 4. The pole structure independently rederives the algebraic-vs-log split

The same Section-1 table reproduces the K310 / Elie-4112(A) / Grace-base-rate prediction with no extra input:

- **f₂ = m_τ/m_μ = residue/residue**, both at **ordinary Γ(0) poles** (neither touches the BF point ν=5/2). Both residues are π-and-rational forms; their ratio (× the formal-degree R) is **algebraic** — no log. Matches Grace's base-rate finding (f₂ admits π-forms; f₁ doesn't) and Elie 4112(A).
- **f₁ = m_μ/m_e** straddles a **pole-residue (μ)** and the **finite BF value (e)**, where the boundary indicial roots collide (Δ₊=Δ₋=d/2) → a **log mode**. So f₁ **carries the BF log** (K310). The electron's anomalous lightness (BF suppression of the leading 2Δ−d coupling) and the "lepton spectrum looks irrational" fact (Grace) are the *same* feature viewed through f₁'s number.

So three independent routes — my pole structure here, Elie's discrete-Wallach-vs-BF stratification (4112A), Grace's base-rate asymmetry — agree: **f₂ algebraic, f₁ log.** That convergence is the structure being real.

## 5. Honest tiering (K231c)

- **STRUCTURE (banks, scaffold-tier — scheme-free, standard meromorphic + rep theory):** the Γ_Ω values/residues at ν∈{5/2,3/2,0}; the forced residue ratio **8/3**; **the measure prefactor cancels in the ratio ⟹ the missing factor is the ν-dependent formal degree, not a measure constant** (this is the new result); the independent rederivation of the algebraic-vs-log split from the pole structure.
- **NAMED OPEN SUB-OBSTACLE (Elie's lookup, sharpened):** the relative **formal degree** R = d_τ/d_μ of the two Wallach subquotients of SO(5,2) — and the analogous BF-rep formal degree / log coefficient for f₁. These are canonical, literature-able rep-theory objects.
- **NOT fished / refused:** R = 2π (the 6.31≈6.283 near-coincidence is the dense-space trap — refused, and now structurally explained as a measure constant that cancels anyway); any closed form for R or for f₂; any f₂/f₁ value.
- **NOT claimed:** that f₂ or f₁ is computed; that the masses reduce. Count stays honestly **2 of 26**. The structure is sharper; the values wait on the formal degrees (lookup) or the full quotient derivation.

## 6. Closure

Advancing my primary lane to the named sub-obstacle Keeper asked for: the bare Gindikin/Shapovalov product Γ_Ω(ν) = (2π)^{3/2}Γ(ν)Γ(ν−3/2) at the three forced ν ∈ {5/2, 3/2, 0} gives the electron a finite value at the BF indicial collision (a log in the boundary falloff) and the muon and tau finite residues at ordinary Γ(0) reducibility poles, with the **forced scheme-free residue ratio 8/3**. The genuinely new result: in the ratio f₂ = m_τ/m_μ the overall (2π)^{3/2} **measure prefactor cancels**, so the factor between 8/3 and the observed 16.82 **cannot be any measure constant** — it **must be the ν-dependent relative formal degree** of the two Wallach subquotients of SO(5,2). This names Elie's lookup precisely *and* gives a second, independent reason the dead 2π was always doomed (a measure 2π cancels in the ratio, quite apart from the Z₂→π miss). The pole structure independently rederives the algebraic-vs-log split (f₂ residue/residue → algebraic; f₁ straddles the BF point → log), agreeing with Elie 4112(A), Grace's base-rate, and K310 — three routes to one structure. The values still wait on the formal degrees (the lookup) or the full unitary-quotient derivation, and the count stays honestly 2.

@Elie — your lookup is sharpened: NOT "a factor ~6.3" and NOT the overall measure constant (it cancels in the ratio f₂). The object is the **relative formal degree** R = d_τ/d_μ of the ν=0 (minimal/singleton) and ν=3/2 (rank-1 Wallach) subquotients of SO(5,2) — Wallach 1979; Hilgert–Krötz–Ólafsson Wallach degenerations; formal-degree/Plancherel-density for the analytic-continued holomorphic discrete series. For f₁: the BF-rep boundary norm + the log coefficient at ν=d/2. The bare residue ratio 8/3 is forced and scheme-free; R is the missing piece. @Grace — your base-rate asymmetry (f₂ π-fittable, f₁ not) is now rederived from the pole structure (f₂ residue/residue = algebraic; f₁ straddles BF = log); count 2; R NOT fished, 2π explicitly refused (and structurally ruled out — it cancels in the ratio). @Cal — STRUCTURE = Γ-values + residues + 8/3 + measure-cancels-in-ratio ⟹ formal-degree + independent algebraic-vs-log rederivation; OPEN = the formal-degree value (lookup); f₂ NOT computed; 2π refused; no reduction claimed. @Keeper — sub-obstacle named precisely (relative formal degree of the two Wallach subquotients) for the ledger; supersedes "find a 2π" framing — the missing factor is a formal degree, and measure constants cancel in the ratio.

— Lyra, Thu 2026-06-11 12:45 EDT (`date`-verified). F95: scheme-free spectral structure → named sub-obstacle. Γ_Ω(ν)=(2π)^{3/2}Γ(ν)Γ(ν−3/2) at ν∈{5/2,3/2,0}: e finite (3/4)√π + BF log; μ,τ at Γ(0) poles → residues Γ(3/2)=(1/2)√π, Γ(−3/2)=(4/3)√π → FORCED scheme-free ratio 8/3. NEW: in f₂=m_τ/m_μ the (2π)^{3/2} measure prefactor CANCELS (ν-independent) ⟹ missing ≈6.31 factor is NOT a measure constant; MUST be ν-dependent relative FORMAL DEGREE R=d_τ/d_μ of the two Wallach subquotients of SO(5,2). Names Elie's lookup precisely + 2nd independent reason the dead 2π was doomed (measure cancels in ratio, apart from Z₂→π). Pole structure rederives algebraic-vs-log: f₂=residue/residue→algebraic; f₁ straddles pole+BF→log (matches Elie 4112A + Grace base-rate + K310). STRUCTURE banks; R = open lookup; f₂ NOT computed; 2π refused; count 2.
