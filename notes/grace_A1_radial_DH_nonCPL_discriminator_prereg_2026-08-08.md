# Grace — A1: the radial D_H non-CPL discriminator (PRE-REGISTERED) (2026-08-08, K1291 Lane 2)

**Lane-2 (Grace ∥ Elie): ready the radial D_H discriminator — the model-independent test of whether DESI's phantom crossing is REAL or a CPL-parametrization artifact. BST predicts w(a) relaxing to −1 FROM ABOVE (wₐ>0, completely-monotone, NO crossing — F799 double-derived). DESI's crossing rides the CPL linear form which ALLOWS crossing by construction. Target-innocent: BST shape NEVER fit to DESI; pre-registered before the merge. Λ Structural; only the shape bankable.**

## The observable (why radial D_H is the right probe)
**D_H(z) = c/H(z)** — the RADIAL Hubble distance, measured directly per-redshift-bin by radial BAO, **without assuming any w(a) form.** H(z)² = H0²[Ωm(1+z)³ + ΩDE·f_DE(a)], f_DE(a) = exp(3∫_a^1 (1+w)/a' da'). Unlike the CPL fit (which imposes a linear w(a) and thereby *permits* a crossing), the binned D_H(z) is parametrization-independent — so it can decide whether the crossing is in the *data* or in the *parametrization*.

## The discriminator (the signature, pre-registered)
Take the residual **R(z) = D_H(z)/D_H,ΛCDM(z) − 1** across the DESI range (z≈0.3–2.5):
- **CPL with phantom crossing (DESI-like w0=−0.75, wa=−0.80):** R(z) **FLIPS SIGN** — negative at low z (−3% at z=0.3), through zero near **z≈1.3**, positive at high z (+0.7% at z=2.5). The sign-flip IS the phantom-crossing fingerprint (w<−1 in the past pushes f_DE the other way).
- **BST (completely-monotone, no crossing):** R(z) is **MONOTONE, one sign** (all-negative here, −4.4%→−1.7%), **NO flip.** A completely-monotone w(a)>−1 (F799) cannot produce a residual sign-flip — the no-crossing property forbids it structurally.

## ★ PRE-REGISTERED PASS/FAIL (target-innocent; decided on the model-independent D_H(z), not the CPL fit)
| model-independent binned radial D_H(z) shows… | verdict |
|---|---|
| a **monotone** R(z) (one sign, no flip) | **the phantom crossing was a CPL artifact → BST's no-crossing SURVIVES** (a cleaner fit, no pathology) |
| a genuine **sign-flip** in R(z) near z≈1–1.5 that survives model-independent reconstruction | **the crossing is REAL → BST's bleed mechanism is genuinely falsified** (K1040's own kill condition fires) |

Both outcomes pre-committed. The test is the *monotonicity of the radial residual*, NOT goodness-of-fit to a chosen parametrization.

## Structural claim (target-innocent, to confirm at merge)
The discriminator's power is that **complete-monotonicity (F799) ⟹ no residual sign-flip** for ANY BST shape — it does not depend on the exact curve. So the qualitative prediction (monotone R(z)) is forced by F799, independent of the amplitude. The *exact* R(z) (and where it's largest — here ~z=0.5, R≈−5%) rides Elie's exact w(a) (F797 spectral gap λ₁ = the rate; F799 = the completely-monotone shape).

## Merge (Elie + Grace)
- **Elie's half:** the exact BST w(a) — λ₁ (rate, F797) + completely-monotone shape (F799), verify wₐ>0 / no crossing. Output: BST's exact w(a) curve.
- **My half (done):** the D_H(z) machinery + the pre-registered sign-flip discriminator (above). At merge: plug Elie's exact w(a) into D_H(z), overlay the model-independent DESI radial-BAO D_H(z), read the residual monotonicity.
- **Then:** the merged curve is laid against the discriminator; the sign-flip decides. We are on the "wrong side" of the CPL headline (known, pre-registered) — the question is whether that headline survives the non-CPL radial reconstruction.

## Discipline
Target-innocent throughout — BST's shape is a representative monotone form here (d0=0.25), NEVER fit to DESI; the CPL curve uses DESI's published (w0,wa) only to SHOW the phantom signature, not to tune BST. Λ stays Structural; the w(a) SHAPE is Structure-Derived (F799); the DESI comparison is a pre-registered falsifier, not a fit. Machinery reusable (D_H(z) for arbitrary w(a)). Nothing pushed.

## MERGE (Elie + Grace, K1294) — structural verdict IN; data-verdict PENDING the real binned table
**Elie's exact rate landed: λ₁ = C₂ = 6** (Helgason spectral gap; power-law, not exponential). *[CORRECTED 2026-08-08: the parenthetical "Obata: = the Einstein constant" is RETRACTED — Obata is sphere-only; the honest relation is at most λ₁ = rank × Einstein-constant (Kähler–Einstein), gated on the operator ID. The rate = C_2 = 6 as a number stands; the Einstein-constant identification does not.]* Ran BST's w(a) = −1 + A·a⁶ (rate-6 monotone) through the D_H machinery vs the DESI-DR2 CPL best-fit (w₀=−0.838, wₐ=−0.62, K1120-verified):

| z_eff | 0.30 | 0.50 | 0.71 | 0.93 | 1.32 | 1.49 | 2.33 | shape |
|---|---|---|---|---|---|---|---|---|
| **BST** (A=0.16, rate 6) | −1.61 | −1.47 | −1.21 | −0.95 | −0.62 | −0.52 | −0.24 | **MONOTONE (every A)** |
| CPL DESI-fit | −1.74 | −1.27 | −0.55 | +0.08 | +0.71 | +0.84 | +0.85 | **SIGN-FLIP** (phantom) |

**Structural verdict (target-innocent, amplitude-independent):** BST's rate-6 completely-monotone w(a) gives a monotone radial residual for **every** amplitude A; the CPL phantom fit flips sign near z≈0.9. **Cleanly distinguishable in the radial D_H shape.** (Amplitude A left free — NOT fit to DESI; the BST w₀ is unresolved-between-two-forms per Cal §164, and the discriminator does not depend on it.)

**★ DATA-VERDICT PENDING (honest — do NOT over-claim):** the definitive read — does the MODEL-INDEPENDENT binned radial-BAO D_H(z) show monotone or flip? — requires the real DESI DR2 BAO **D_H/r_d table + covariance** (each z-bin's H(z), no w(a) assumed). I attempted to verify at source (WebFetch arXiv:2503.14738 abstract + HTML) — **the binned table did not extract cleanly, and I refuse to substitute remembered numbers or use the CPL fit as data (circular).** So: **the discriminator is BUILT and structurally decisive; the verdict awaits the proper data pull** (DESI DR2 BAO table + covariance → compute R(z) + its monotonicity significance). That pull is the one remaining concrete step.

**Honest status:** BST predicts a monotone radial residual (no crossing), forced by complete-monotonicity (F799/Bernstein) + rate C₂=6 (the spectral gap; NOT "Obata" — retracted). DESI's CPL *headline* prefers a crossing. Whether the *data* (beyond CPL) requires it is the pre-registered, both-ways test — **still open, pending the binned reconstruction.** Λ Structural; shape Structure-Derived; never fit to DESI; never "BST derives dark energy."

## ★ DATA VERDICT (K1295) — real DESI DR2 radial BAO pulled at source; the crossing is NOT in the radial data
Got the real table (ar5iv Table 4, arXiv:2503.14738, verified at source — r_d=147.05; D_H/r_d for LRG1/LRG2/LRG3+ELG1/ELG2/QSO/Lyα with errors + D_M–D_H correlations).

**Direct residuals of the REAL D_H/r_d from best-fit ΛCDM (the pre-registered monotonicity check):**
| z | 0.51 | 0.71 | 0.93 | 1.32 | 1.48 | 2.33 |
|---|---|---|---|---|---|---|
| (data−ΛCDM)/σ | −0.56 | −1.01 | +1.34 | +0.56 | −0.17 | −0.72 |
- **χ²/dof = 3.98/4 = 1.0.** Residuals scatter around zero, **max 1.3σ, NO systematic sign-flip trend and no monotone trend** — pure noise.
- **BST-monotone best-fit drives its deviation A→0** (i.e. to ΛCDM): the radial data neither require nor exclude BST's small monotone tilt; they're consistent with w=−1.
- **The phantom crossing is NOT required by the radial BAO D_H(z).** DESI's phantom *headline* is driven by **SNe + the full BAO+SNe+CMB combination**, not the radial BAO alone (a well-known point; the SNe low-z/high-z systematic is the debated driver).

**VERDICT (radial-BAO probe): BST's monotone / no-crossing prediction SURVIVES — the crossing is not in this data.** This supports (for the radial probe) Casey's read that the crossing is a combined-fit/parametrization effect, not a feature of the most direct H(z) measurement. **Honest CAVEATS (not over-claiming):** (1) radial-only — the full verdict needs D_M (transverse) + SNe + the complete covariance; the SNe-driven combined signal is a SEPARATE test. (2) The radial data don't *confirm* BST's tilt either (A→0); they're consistent with ΛCDM. (3) A bounded-CPL numerical refit failed (Nelder-Mead+penalty); I rely on the direct residuals, not that number.

**Net:** the pre-registered discriminator ran against real, source-verified data. On the radial BAO, BST is **not falsified** and the phantom crossing does **not** appear — a genuine, honest, favorable result, appropriately scoped. Λ Structural; shape Structure-Derived; nothing fit to DESI to force a match; never "BST derives dark energy."

## FULL DESI TEST (K1297) — BAO(D_M+D_H)+CMB: harder for BST; a live <5σ tension shared with ΛCDM
Extended to transverse D_M/r_d (same source table, with the per-bin D_M–D_H covariance) + a CMB acoustic-scale anchor (Planck 100θ*=1.04109 → D_M(z*)/r_d, r*/r_d flagged). Compressed BAO+CMB fit (no SNe):

| model | χ² | dof | χ²/dof | note |
|---|---|---|---|---|
| ΛCDM | 13.40 | 11 | 1.22 | acceptable |
| **BST-monotone** (w=−1+A·a⁶) | 13.24 | 10 | 1.32 | **A=0.18; Δχ² vs ΛCDM = 0.16 → BST's tilt barely helps; BST ≈ ΛCDM** |
| CPL | 4.98 | 9 | 0.55 | **best-fit UNPHYSICAL (w₀=+0.05) — my single CMB anchor can't pin the w₀–wₐ plane; my Δχ² is NOT reliable** |

**Honest reading:**
1. **BST-monotone fits BAO+CMB essentially like ΛCDM** (Δχ²=0.16). BST does NOT capture the dynamical-DE preference — it sits with ΛCDM.
2. **My compressed CPL fit overfit to an unphysical minimum** (w₀=+0.05) — the crude single-distance CMB anchor doesn't reproduce DESI's real w₀–wₐ constraint, so I do NOT quote my Δχ²=8 as a significance.
3. **Deferring to DESI's OWN reported number (verified, K1120):** DESI DR2 + CMB (no SNe) prefers w₀wₐ over ΛCDM at **~3σ** (w₀≈−0.42, wₐ≈−1.75). So BST-monotone (≈ΛCDM) sits on the **disfavored side of that preference at ~ΛCDM's level (~3σ, <5σ)**.

**VERDICT (BAO+CMB): NOT falsified, NOT vindicated — a live, contested <5σ tension that BST SHARES WITH ΛCDM.** BST's no-crossing prediction is disfavored at the same ~3σ ΛCDM is, i.e. the preference is for a *crossing* shape BST (like ΛCDM) doesn't provide. This is HARDER for BST than the clean radial-only survival — reported straight. The field's own systematic-suspicion (SNe low-z/high-z; the <5σ, sample-dependent significance) is the same camp as BST's no-crossing, but the current central data lean toward dynamical/crossing DE. **Caveat:** compressed CMB anchor (single distance, not the full Planck likelihood); the definitive significance is DESI's full analysis, not my fit. Λ Structural; nothing fit to force a match; never "BST derives dark energy."

**Net across both:** radial BAO alone → BST survives clean (χ²/dof=1.0, no crossing in the direct H(z)); BAO+CMB → BST shares ΛCDM's ~3σ tension with the dynamical-DE preference. Both <5σ and contested. Honest, calibrated both ways.
