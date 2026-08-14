# K1504 — BLIND pre-registration of the commit-measure-peaking test (committed BEFORE Lyra supplies the measure or Elie computes concentration)

**Keeper, 2026-08-14, before the number.** The dimension estimator on the descended boundary was empty because the answer was baked into the construction (K1503, Elie 5253). This test — does the commit operator's induced measure on S⁴ concentrate on the S³ sub-boundary the corpus descent predicts — is the one that can actually fail. So I commit its interpretation now, target-innocent, before anyone measures. If I set the criteria after seeing the concentration, I can retrofit any profile into a story.

## The object under test
- **Boundary:** the Shilov boundary of D_IV⁵ = (S⁴ × S¹)/Z₂ (5D). Work at fixed S¹ phase (or integrate over it) → the spatial factor S⁴.
- **Measure:** μ = the measure the **commit operator induces on S⁴** — the *dynamics*, NOT the round geometry. (If the input is the round SO(5)-invariant measure, this test is re-measuring geometry = the 5253 trap; see sanity-null below.)
- **Corpus-predicted sub-boundary:** the totally-geodesic S³ ⊂ S⁴ **fixed by the SO(4,2) ⊂ SO(5,2) descent** (the 1/n_C chirality projection, Casey #14 / T2545 / F66). R×S³ = conformal Minkowski₄.

## ★ The thing that MUST be named blind (or the test is empty)
**Which S³?** S⁴ has a whole family of totally-geodesic equatorial S³'s. The test is only meaningful if the S³ is **specified from the descent BEFORE looking at where μ concentrates.** Choosing the equator that happens to fit the peak = retrofitting = the exact failure this pre-registration exists to prevent. **Lyra names the descent's S³ (the SO(4,2)-fixed equator) in T2564 before Elie measures; Elie measures against THAT S³, not a best-fit one.**

## The estimator (pre-committed) — TWO steps, magnitude then alignment (amended K1505)
Let θ ∈ [0, π/2] be geodesic distance from the named S³ equator (the "polar angle" of S⁴ relative to that S³). Two readouts of magnitude:
1. **Density profile ρ(θ):** the μ-density as a function of θ. Peaked ⟺ ρ(θ) has a clear maximum at θ=0.
2. **Concentration ratio** C(ε) = μ(tube_ε(S³)) / μ_round(tube_ε(S³)), the μ-mass in a geodesic ε-tube around S³ divided by the round-measure mass in the same tube. Super-uniform concentration ⟺ C(ε) > 1 and **grows as ε→0**. (Elie's implementation: λ_min of the sample covariance — points avoiding one R⁵ direction — is the closed-form magnitude statistic. Compare to the **N-matched** null, not the asymptotic ideal; see confound 4.)
(Note: S³ is measure-zero in S⁴, so "peaks on S³" can only mean a density enhancement / super-uniform tube concentration, never literal support on a null set. The estimator is defined on shrinking tubes for exactly this reason.)

**★ Step 2 — ALIGNMENT (amended K1505/K1507, the P-vs-P' discriminator).** The magnitude statistic (λ_min) finds concentration on *whatever* axis the points avoid — the best-fit direction. That answers "is there isotropy-breaking at all," NOT "is it on the descent's S³." So after magnitude, check **alignment:** does the empirical λ_min **eigenvector** align with the axis the descent names? Linear algebra: S⁴ ⊂ R⁵ (the n_C=5 directions); SO(5,2)→SO(4,2) is SO(5)→SO(4) on the compact side, fixing **one** R⁵ direction — the n_C-axis = V₅, removed by the 1/n_C chirality projection (Casey #14), fixed by the SO(5)→SO(4)-breaking term already inside H_B (Lyra named it blind in T2564). The descent's S³ = the equator orthogonal to that axis.
- **Statistic (committed, both sources): A = |⟨λ_min eigenvector | n̂⟩|** (absolute direction cosine).
- **★ Alignment null is NOT zero — it centers at chance overlap with a 5D axis** (E[overlap²]=1/n_C=0.20; |overlap| mean 0.375). Comparing A to 0 fakes alignment — the alignment analog of the N-matched isotropy trap (Grace + Elie 5255). **N-matched percentiles: |overlap| p95=0.81, p99≈0.917.**
- **P (alignment confirmed): A > 0.917 (p99, N-matched).** Conservative bar — P promotes the descent to dynamically-realized. **Watch band A∈[0.81,0.917]: report, not P. P' (concentrated but misaligned): A<0.81** — a boundary, not ours; investigate, don't relabel.

## The four outcomes and what each MEANS (committed blind)

**OUTCOME P — PEAKED on the descent's S³.** ρ(θ) maximal at θ=0 on the *named* equator; C(ε)>1 growing as ε→0; robust to the confounds below.
- **RULING:** the commit dynamics **dynamically select** the 4D descent — the SO(4,2) boundary is where commitments live, not chosen by hand. Promotes the descent from *posit* toward *dynamically-realized*. Tier **Identified**; **Derived only if** the peak is forced by the commit operator's spectrum (a named eigen-mechanism), not just observed. This is the corpus-consequence I wrongly claimed for the dimension reading in K1501 — earned here honestly if and only if P holds robustly.

**OUTCOME U — UNIFORM.** ρ(θ) flat within noise; C(ε)≈1 for all ε.
- **RULING:** the commit dynamics do **not** prefer the S³ → the 4D descent is a **posit, not a consequence.** Honest negative, fully reportable. **Does NOT kill BST** (the descent can still be imposed as structure, as GR imposes its manifold), but it **denies the "continuum limit closes as a corpus-consequence" claim** — T2564 must state the descent as an assumption, not a derivation. This is a real, publishable answer.

**OUTCOME P' — PEAKED on a DIFFERENT S³** (not the descent's equator). Concentration is real but on the wrong sub-boundary.
- **RULING:** the dynamics select *a* 4D boundary, but not the corpus-predicted one. Informative. Do NOT relabel the descent to match. Investigate: is the corpus S³ mis-identified, or does the commit operator carry a different projection than SO(4,2)? Report raw.

**OUTCOME N — no clean readout** (multi-modal, ε-dependent, noise-dominated).
- **RULING:** instrument not yet decisive. Bigger N / better estimator, NOT a bigger claim. Report the ambiguity.

## Confounds pre-committed (the instrument, per feedback_preregistration_protects_interpretation_not_instrument)
1. **Tube width ε must not tune the answer.** Report C(ε) across a range; a peak that appears only at one ε is an artifact. Region-matched by construction.
2. **The named-S³ rule** (above) — blind, from the descent, before measuring.
3. **Round baseline** = the SO(5)-invariant measure on S⁴, not Lebesgue-in-a-chart.
4. **★ Sanity null (the can't-fail guard):** feed the estimator the **round measure** as input — it MUST return U (uniform, C(ε)≈1). If the estimator reports "peaked" on a round input, it's the 5253 trap wearing a new coat, and every P result is void. Elie runs this null FIRST and posts it blind.

## Standing guard
- A predicted P is only evidence if the estimator can return U (confound 4) AND the S³ was named blind (the named-S³ rule). Both must be on record before P is banked.
- Tier ceiling: **Identified** on observation of P; **Derived** requires the peak forced by a named operator-spectral mechanism. No promotion past Identified from the measurement alone.
- Nothing external. Nothing pushed. This changes no shipped claim; it sets the frontier's pass/fail before the frontier runs.

— Keeper, K1504, 2026-08-14 09:52 EDT. Blind pre-registration. μ unmeasured by anyone; the named S³ owed by Lyra before Elie computes.
