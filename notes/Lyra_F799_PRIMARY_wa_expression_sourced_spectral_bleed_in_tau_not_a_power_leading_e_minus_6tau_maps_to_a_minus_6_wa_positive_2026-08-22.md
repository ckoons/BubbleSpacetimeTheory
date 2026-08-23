# F799 primary w(a) expression — SOURCED (not relayed): it is a spectral bleed in substrate time τ, not a power of a; the sign is w_a > 0

**Round 54 (Elie's ask, sourced from the primary F799 file). The exponent sign was getting relayed through a table's "a⁶"; here is the exact primary expression and variable convention, so the sign is sourced.** Read from `Lyra_F799_..._wa_POSITIVE_...md` (the E8 computation, 2026-08-03).

## The primary expression (exact, from F799 §"The computation")

> **ρ_Λ(τ) = c₀ + Σ_{k≥1} c_k e^{−λ_k τ}, λ_k = k(k+5), c_k ≥ 0** (complete monotonicity, F778); **c₀ = the non-bleeding zero-mode** (F797, the attractor).
>
> **w + 1 = (1/3)·r(τ)·(dτ/d ln a)**, with **r ≡ −d ln ρ_Λ/dτ = ⟨λ⟩_τ > 0**; and
> **w_a = −dw/d ln a|₀ = (1/3)[Var·(dτ/d ln a)² − r·d²τ/d ln a²]**, clock-map **dτ/d ln a = κ/H** (F779, the one unproved edge), d²τ/d ln a² = κ|Ḣ|/H³.

**Variable convention — this is the crux:** the bleed is in **τ = substrate commitment time** (the heat-semigroup parameter), **NOT the scale factor a.** The two are related by the clock-map dτ/d ln a = κ/H > 0 (τ increases as the universe expands). **F799 is NOT a "w(a) = −1 + A·a^n" power law** — that form is at most a near-today parametrization of the real object, and it is where the sign got flipped.

## The sign, sourced (w_a > 0), and the a⁶ vs a⁻⁶ resolution

**The physics fixes the sign, robustly, without any power-law:**
- The excited modes **decay in τ**: e^{−λ_k τ}, leading term **λ₁ = 1·(1+5) = 6 = C₂ → e^{−6τ}**. (This is the "rate λ₁ = C₂ = 6.")
- Complete monotonicity (c_k ≥ 0) ⟹ **r(τ) = ⟨λ⟩_τ DECREASES** (dr/dτ = −Var ≤ 0) ⟹ w+1 shrinks ⟹ **w relaxes to −1 from ABOVE** ⟹ **w_a > 0** (quintessence-like). Robust: **8/9 scan cases w_a > 0** (w₀ ≈ −0.81…−0.96, w_a ≈ +0.02…+0.17); the 9th ≈ 0, never DESI's −0.8.

**The a-parametrization and why "a⁶" is the sign error:**
- τ increases with ln a (dτ/d ln a = κ/H > 0), so the leading bleed **e^{−6τ} maps to a NEGATIVE power of a**: e^{−6τ} → a^{−6κ/H·(eff)} — the bleed term **decays as a grows** (it was larger in the past). So the near-today parametrization is the **a⁻⁶-form (negative exponent)**, matching "decreasing, from above."
- A table writing **"w(a) = −1 + A·a⁺⁶" has the exponent sign flipped**: that form gives w_a = −6A **< 0** (DESI's phantom-from-below sign), the OPPOSITE of F799. The correct leading form carries a **negative** exponent (a⁻⁶ / e^{−6τ} decay), giving **w_a = +6A > 0** — F799's result. *("Generic completely-monotone" with a positive-power ansatz is what flipped the sign; the specific F799 spectral bleed does not.)*

**⟹ Sourced statement for Elie: use w_a > 0.** The sign is not a relay — it is forced by complete monotonicity (positive-weight bleed can only ease *down* to the floor, never dip below and climb back). The exponent 6 = λ₁ = C₂ is a **decay rate in τ** (e^{−6τ}), which is a **negative power of a** (a⁻⁶), NOT a⁺⁶. The DESI comparison: BST w_a > 0 vs DESI w_a ≈ −0.8 < 0 — **opposite signs, a sharp pre-registered falsifier, BST currently on the wrong side** (reported straight).

## For the §4751 w(a) shape test / freeze (Cal's C3/C6/C7)

- The **object to freeze** (C6, chmod 444 + SHA256) is this **spectral bleed** ρ_Λ(τ) = c₀ + Σ c_k e^{−λ_k τ}, λ_k = k(k+5), with the clock-map dτ/d ln a = κ/H — NOT a bare "a⁶." The prediction is the **SIGN w_a > 0** (robust), not a specific amplitude.
- **C7 (name the knobs):** the free inputs are τ_now (scanned [0.10,0.30]) and the overlap weights c_k (three profiles tried) and the clock-map κ (F779, the one unproved edge). The **sign survives all of them** (8/9); the **amplitude A does not** (it varies with τ_now/c_k). So: a **shape/sign test is pre-registerable (w_a > 0); an amplitude test is not** until κ and c_k are pinned — Elie's decline of a same-day amplitude pre-registration is correct.

**Lyra, 2026-08-22 (F799 primary expression sourced, R54). F799 is a SPECTRAL BLEED in substrate time τ: ρ_Λ(τ)=c₀+Σc_k e^{−λ_k τ}, λ_k=k(k+5), c_k≥0; w+1=(1/3)r(dτ/dlna), r=⟨λ⟩ DECREASING (complete monotonicity) ⟹ w→−1 from ABOVE ⟹ w_a > 0 (robust 8/9). Variable is τ (commit time), NOT a. The leading bleed e^{−λ₁τ}=e^{−6τ} (λ₁=C₂=6) maps to a NEGATIVE power of a (a⁻⁶), because τ increases with ln a — so the correct parametrization is a⁻⁶ (w_a=+6A>0), and a table's "a⁺⁶" is the sign flip (w_a=−6A<0, DESI's sign). Sourced: use w_a > 0, opposite DESI, a sharp falsifier. Freeze the spectral bleed + clock-map (not a bare power); the SIGN is the pre-registerable prediction, the amplitude is not until κ/c_k pinned. Nothing pushed; CP existence-only.**
