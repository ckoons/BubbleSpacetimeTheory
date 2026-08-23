# §4751 — PRE-REGISTRATION: the w(a) shape test (sign of w_a), frozen

**Pre-registration artifact, 2026-08-22 (Lyra). This is the on-disk §4751 shape test Cal's C3/C6/C7 bind against. It pre-registers a SIGN, not a value. To be frozen (chmod 444 + posted SHA256) the moment it is content-final; any edit after the DESI lookup voids it.** Object sourced from the primary F799 (see `Lyra_F799_PRIMARY_wa_expression_sourced_..._2026-08-22.md`), NOT relayed.

## The object being tested (the shape)

BST's dark-energy sector is a **spectral bleed in substrate time τ** (F799, F797, F778), NOT a power law:

> **ρ_Λ(τ) = c₀ + Σ_{k≥1} c_k e^{−λ_k τ}, λ_k = k(k+5), c_k ≥ 0** (complete monotonicity); **c₀ = the non-bleeding zero-mode** (attractor). Equation of state: **w + 1 = (1/3)·r(τ)·(dτ/d ln a)**, r ≡ −d ln ρ_Λ/dτ = ⟨λ⟩_τ; clock-map **dτ/d ln a = κ/H**. Leading bleed mode **λ₁ = C₂ = 6** (e^{−6τ}, → a negative power of a).

## The prediction (pre-registered — a SIGN)

> **w_a > 0** — dark energy relaxes to w = −1 **from ABOVE** (quintessence-like), the OPPOSITE of a phantom crossing (w_a < 0).

This is **forced by complete monotonicity** (c_k ≥ 0 ⟹ r(τ) decreasing ⟹ w decreasing to −1 from above ⟹ w_a > 0), robust in 8/9 scan cases (the 9th ≈ 0, never < 0). It is a **structural sign**, not a fitted value.

## C3 — the DATASET and the KILL THRESHOLD (both fixed here, before any lookup)

- **Dataset combination (pinned):** the **DESI DR2 baseline (BAO + CMB + DESI-preferred SNe) w₀wₐCDM posterior on w_a** — the same combination DESI DR2 reports its w₀wₐ contour from. (If DR3 supersedes DR2 before the test, the DR3 equivalent baseline; the combination, not a re-pick among many, is what is fixed.) **No post-hoc dataset selection.**
- **Kill threshold (pinned):** the prediction is the **sign**. 
  - **REFUTED** if the pinned posterior **excludes w_a ≥ 0 at ≥ 3σ** (i.e. w_a < 0 firmly) — the completely-monotone bleed cannot produce a phantom past.
  - **ACCOMMODATED** if the posterior **includes w_a ≥ 0, or w = −1 (ΛCDM), within 2σ.**
  - **INCONCLUSIVE** (reported as such, no claim) if the posterior sits between (w_a < 0 preferred at 2–3σ but not excluding w_a ≥ 0 at 3σ).
- **Δχ² form (equivalent):** REFUTED if Δχ²(w_a ≥ 0 vs best-fit) ≥ 9 (3σ, 1 dof) with the best-fit at w_a < 0.

## C7 — the KNOBS (named; and the amplitude is NOT pre-registered)

- **This is a SIGN/SHAPE test, not a value test.** The **amplitude** of w_a (its magnitude) rides three inputs and is **NOT pre-registered**: **τ_now** (scanned [0.10, 0.30]), the **overlap weights c_k** (three profiles tried: equipartition / decreasing / single-mode), and the **clock-map κ** (F779, the one unproved edge). 
- **A / the amplitude is FITTED (unpinned), not DERIVED** — declared here, before the test. A shape test with a free amplitude tests only the **shape/sign**; it must NOT be reported as a test of the numerical value of w_a.
- **The SIGN survives all three knobs** (8/9 scan) — that robustness is the whole content of the prediction.
- **Monomial-pool note (Cal §693.10):** if any future version pins the amplitude as a BST-integer ratio, the look-elsewhere denominator (how many BST-integer amplitudes land in the tolerance) MUST be stated there. This version pins **no amplitude**, so no monomial pool applies — the prediction is the sign only.

## C6 — FREEZE (to apply when content-final)

- On content-final: `chmod 444` this file + post its **SHA256** to the running notes / board. 
- **Any edit after the DESI lookup voids the pre-registration.** The corpus holds ≥4 mutually inconsistent w(a) declarations on record — this hash is not ceremony; it is the reason the sign can be trusted as pre-registered.
- **SHA256:** _[to be posted on freeze]_

## What clears / what is owed

- **Pre-registerable now:** the SIGN (w_a > 0), the shape (spectral bleed), the dataset (DR2 baseline), the kill threshold (3σ sign exclusion). **On disk, C3/C6/C7-bindable.**
- **NOT pre-registered:** the amplitude (unpinned; fitted). 
- **@Elie** runs the forcing against this spectral-bleed form (e^{−6τ}), not a power law, and reports whether the real c_k / H(z) preserve the sign and by how much it misses the DESI contour. **@Cal** pre-vets this artifact (verify the hash on freeze; confirm C3/C6/C7 met).

**Lyra, 2026-08-22 (§4751 pre-registration ON DISK). The w(a) shape test pre-registers a SIGN: w_a > 0 (dark energy relaxes to −1 from above), forced by complete monotonicity of the spectral bleed ρ_Λ(τ)=c₀+Σc_k e^{−λ_k τ} (λ₁=C₂=6), robust 8/9. C3: dataset = DESI DR2 baseline w₀wₐ posterior; kill = w_a ≥ 0 excluded at ≥3σ ⟹ REFUTED (Δχ²≥9), included within 2σ ⟹ accommodated. C7: amplitude FITTED/unpinned (τ_now, c_k, κ) — a shape/sign test, NOT a value test; the sign survives all knobs; no monomial pool (no amplitude pinned). C6: chmod 444 + SHA256 on freeze; any post-lookup edit voids it. Object sourced from primary F799, not relayed. Nothing pushed; CP existence-only.**
