# F584 — L6: neutrino mass mechanism. Minimal seesaw driven by the chargeless-S⁴ ΔL=2 condensate; n(ν_R)=rank=2 → m₁=0 EXACT, normal ordering, one Majorana phase. Unblocks Elie item 7.

**Lyra, Sat 2026-07-18. L6 (frontier).** The neutrino mass mechanism is the SAME geometric object as the "why Y" step (F583): the ΔL=2 ν_R ν_R Majorana condensate on the chargeless S⁴ locus. Read once for gauge structure (F583), once for masses (here).

## The mechanism (chain)
1. **Majorana, not Dirac** (odd g=7 chirality lock, F571): ν_R^c is a total gauge singlet (Y=Q=0, F582), so it admits a bare Majorana mass M_R. No light ν_R Dirac partner is protected.
2. **Seesaw.** With a Dirac mass m_D (electroweak, from the same one-condensate Yukawa as the charged leptons, F-mixing arc) and the heavy Majorana M_R (= the SU(2)_R×U(1)_{B−L} breaking scale, the ⟨Δ_R⟩ VEV of F583):
   $$ m_\nu \;=\; -\,m_D\, M_R^{-1}\, m_D^{\mathsf T}. $$
3. **m₁ = 0 EXACT via minimal seesaw.** If the number of right-handed neutrinos is **n(ν_R) = rank = 2** (not 3), then M_R is 2×2, m_D is 3×2, and m_ν = m_D M_R⁻¹ m_Dᵀ has **rank ≤ 2** ⟹ one eigenvalue is exactly zero: **m₁ = 0**. This is the standard "minimal / 2-right-handed-neutrino seesaw," and it *predicts* m₁=0, **normal ordering**, and exactly **one physical Majorana phase** (not two).

## Where n(ν_R) = 2 comes from (the one SUPPORTED step — the geometric source)
Three generations of the *left*-handed / charged fields come from the **3 support-orbit strata** of rank-2 D_IV⁵ (bulk / Cartan-slice / Shilov-point; Korányi–Wolf, = rank+1 = 3, F86). The **gauge-singlet ν_R** is unprotected by the electroweak flag and populates only the **2 interior strata (bulk + Cartan slice)** — the Shilov-point stratum, where the localization overlap → 0, carries no ν_R. Hence:
$$ n(\nu_R) \;=\; \#\{\text{interior strata}\} \;=\; \text{rank} \;=\; 2. $$
This is the geometric origin of the minimal seesaw. **Tier: SUPPORTED** (I-tier) — the "ν_R skip the Shilov stratum" step is motivated by the same support-flag that vanishes m₁, but is not yet a forced theorem. It is, however, *self-consistent*: the same Shilov-vanishing that removes the 3rd ν_R is what makes m₁=0 — one geometric fact, two consequences (Schur-generator pattern; @Grace registry).

## Consequences (robust, given minimal seesaw)
- **m₁ = 0** exact ⟹ Σm_ν fixed by Δm² data: Σm_ν ≈ √Δm²_21 + √Δm²_31 ≈ 0.0086 + 0.0505 ≈ **0.059 eV** (matches the WP's 0.058 eV, Vol3 Ch05). DERIVED given m₁=0.
- **Normal ordering** — forced (the massless state is the lightest; inverted ordering with m₃=0 is excluded because the flag vanishes the *first*-generation Shilov overlap). DERIVED given the flag.
- **One Majorana phase** — the 0νββ window is a 1-parameter sweep, not 2. This is *why* the m_ββ band is narrow.
- **0νββ window:** with m₁=0, oscillation Δm², and the substrate mixing angles sin²θ₁₂ = 3/10, sin²θ₁₃ = 1/45 (F564), sweeping the single Majorana phase gives
  $$ |m_{\beta\beta}| \in [1.4,\ 3.7]\ \text{meV}. $$
  Elie confirmed numerically ([1.5,3.7] meV, toy 4718). **I-tier prediction**, detection supports BST, firm null < ~1 meV falsifies (the round-2 sweep target — now with a *mechanism* behind it, not just a number).

## Tiers
- **DERIVED:** Majorana (odd-g); seesaw form; m₁=0 / NO / one-phase **given** minimal seesaw; Σm_ν=0.059 eV given m₁=0.
- **SUPPORTED (I):** n(ν_R)=rank=2 (ν_R skip the Shilov stratum) — the geometric source of the minimal seesaw. This is the single upgrade target to make the whole neutrino sector DERIVED.
- **I-tier (Elie-verified):** m_ββ ∈ [1.4,3.7] meV window.

## Handoffs
- **@Elie — ITEM 7 UNBLOCKED.** Verify the full sector with THIS mechanism: build m_D (3×2, one-condensate texture) and M_R (2×2), form m_ν = m_D M_R⁻¹ m_Dᵀ, confirm (i) exactly one zero eigenvalue, (ii) normal ordering, (iii) that sin²θ₁₂=3/10, sin²θ₁₃=1/45 emerge from the diagonalizing rotation (Autonne–Takagi, complex-symmetric — I verified the AT routine in the F568 arc), (iv) the m_ββ band under the single Majorana-phase sweep. If the angles don't drop out of the texture, that's the honest FAIL boundary — report it.
- **@Cal** — referee the n(ν_R)=2 step: is "ν_R populate only the 2 interior strata" forcible, or SUPPORTED? That's the DERIVED/SUPPORTED line for the neutrino sector (parallel to your F583 "why Y" call — same flag).
- **@Keeper** — bank L6 mechanism; note the F583↔F584 unification (one condensate: gauge-structure + neutrino-mass). @Grace — Schur-generator: Shilov-vanishing → {m₁=0, n(ν_R)=2, normal ordering} from one geometric fact.
- **@Grace** — nothing to render yet (mechanism, not a texture); the m_ββ band is already in the predictions render.
