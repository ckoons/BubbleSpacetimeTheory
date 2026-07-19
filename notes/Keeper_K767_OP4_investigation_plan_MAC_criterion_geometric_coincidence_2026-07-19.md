# K767 — How to investigate OP-4 further: two target-innocent, standard-physics-grounded methods (the MAC/Casimir criterion for the selection; the geometric-coincidence test for saturation), plus the info the team needs.

**Keeper | 2026-07-19 | Casey: think hard about how to investigate OP-4 more, gather what the team needs. Lyra's gap-equation solution (y_t = 4π/√(N_c·ln(Λ²/m_t²)), = 0.83 at Planck, = 1 at Λ≈10¹⁴) confirmed y_t=1 is O(1)/natural but not kinematically pinned. Here is the sharpened plan + grounding.**

---

## ⚠ LINEAR-ALGEBRA REFRAME (Casey, after this note: "remember this should be linear algebra")
The methods below reach for BSM machinery (gap equation, MAC dynamics, RG). Casey's correction: the BST-native question is **linear algebra**, and it subsumes Method 2. The Yukawa IS an inner product: **Y_ij = ⟨f_L^i | Φ | f_R^j⟩** on H²(D_IV⁵); masses = singular values; y_t = ‖Y‖. **y_t = 1 ⟺ Φ is (essentially) a rank-1 projector onto the condensate direction ∧ the top mode ∥ that direction (Clebsch–Gordan coefficient = 1);** the hierarchy is one Gram column (the condensate's overlaps with the fermion modes). So the investigation is: compute Φ (F85), the fermion K-type vectors, and their overlaps — is the top parallel (y_t=1)? does the column give the hierarchy? **Method 2 (geometric coincidence) IS this, done as linear algebra; Method 1 (MAC) survives only as a Casimir-*eigenvalue* residue (drop the condensation dynamics); Method 3 (Λ) is moot if the linear algebra forces parallelism.** The active pull is `team_prompt_2026-07-19g` (linear algebra). The gap-equation/MAC framing below is superseded — kept for the record + the web grounding.

## Where we are (confirmed from every side now)
- **Derived:** the condensate is a quark (N_c color trace lowers the critical coupling for quark channels). Both Lyra (gap equation) and Grace confirm. The one clean leg.
- **Supported / not derived:** y_t = 1 (the value is O(1) but Λ-dependent — 0.83 at Planck, 1 at Λ≈10¹⁴ GeV — not pinned); the 41× ratio (tuned in G to 2 sig figs, or the identified C₂·g = 42); the gen-3 + up/down selection (geometric alignment, supported).
- **Framework win:** the induced four-fermion interaction is genuinely from the Bergman two-point structure (F85) — pure D_IV⁵ geometry, no new gauged group (Five-Absence safe).

## The sharpened central question
Is **y_t = 1 a genuine saturation** (a real BST prediction) **or an O(1) coincidence** (the top just lands near 1)? The two underlying pictures make *different* predictions:
- **Precipitation (condensate direction = the top mode):** y_t = 1 *exactly* — the top mode is parallel to the condensate, so the Born overlap saturates Cauchy–Schwarz at 1.
- **Composite Higgs (condensate = a separate composite):** y_t = O(1), Λ-dependent, ≈ 0.83 at the Planck cutoff (Lyra's gap equation).

**The data discriminates:** observed y_t = 0.992 is far closer to 1 (precipitation) than to 0.83 (Planck-cutoff composite). So the data *slightly favors* the precipitation picture — which is exactly Casey's original instinct ("does the top precipitate from the condensate"). This is now a concrete, testable fork.

## ★ Method 1 — the MAC (Most-Attractive-Channel) criterion for the SELECTION [target-innocent]
Standard tool (Raby–Dimopoulos–Susskind 1980, "Tumbling Gauge Theories"): when several condensation channels are possible, the one that condenses **maximizes ΔC₂ = C₂(R₁) + C₂(R₂) − C₂(R_condensate)** — a **quadratic-Casimir** criterion. This is exactly BST's "which channel condenses," and it is **target-innocent** (Casimirs come from representation theory, not from the masses). BST has the Casimir structure natively (C₂ = 6 is a BST primary).

**Concrete seed — MAC favors the up-type (compute this properly):** u_R and d_R differ in hypercharge (Y = +4/3 vs −2/3). In K = SO(5)×SO(2), the SO(2) contribution to the Casimir ∝ Y², so C₂(u_R) : C₂(d_R) ∝ (4/3)² : (2/3)² = **4 : 1**. Larger C₂(R) → larger ΔC₂ → more attractive → the **up-type is the MAC**. This gives the up/down selection *from Casimirs*, and the natural weight is Y² (the factor-4 option, not the factor-2). **Caveat (from the literature):** the MAC rule has known exceptions (Seiberg, SUSY QCD) — it is a strong heuristic, not a theorem. Tier any result "supported via MAC," and check whether the substrate interaction actually realizes single-boson-exchange attraction.

## ★ Method 2 — the geometric-coincidence test for SATURATION [the decisive one]
Does the substrate **force the condensate direction to coincide with the top K-type mode**? If yes, the Born overlap is *exactly* 1 (parallel vectors) and **y_t = 1 is derived, kinematically**, independent of Λ. If the condensate is a generic direction, the max overlap is < 1 (≈ 0.83) and y_t = 1 is not special. This is the F85 computation: the condensate direction (the Bergman two-point / VEV direction on the Shilov boundary) vs the top fermion mode's K-type address. **This is the decisive test of precipitation** — and the data (0.992) says look here first.

## Method 3 — the Λ question [if composite]
If Method 2 says the condensate is a separate composite (y_t Λ-dependent), then y_t = 1 needs **Λ ≈ 10¹⁴ GeV**. Is there a substrate scale there? **Lead:** the neutrino Weinberg scale is also ~10¹⁴ GeV (v²/Λ_ν ~ m_ν). *Same scale?* If BST fixes Λ geometrically — and if it's the neutrino scale — then y_t = 1 is derived via a derived Λ, and the top and neutrino sectors share a scale. (Flag: could be coincidence; BST forbids GUT, so a 10¹⁴ scale needs a non-GUT reading — the Weinberg/Shilov scale, not a unification scale.)

## Info the team needs
**Web (grounding, gathered):**
- **MAC criterion** — Raby–Dimopoulos–Susskind, *Nucl. Phys. B* 169 (1980); ΔC₂ = C₂(R₁)+C₂(R₂)−C₂(R_cond); condensate tends to the most-attractive (often adjoint) channel; **known exceptions (Seiberg SUSY QCD)** — heuristic not theorem.
- **Compositeness / BHL** — Bardeen–Hill–Lindner; compositeness condition (composite-field renormalization constants → 0 at the cutoff); IR quasi-fixed-point; the top Yukawa is **logarithmically sensitive to Λ but insensitive to the initial coupling**, relaxing to **O(1)** in the IR — exactly Lyra's y_t = 4π/√(N_c·ln(Λ²/m²)). So Lyra's result is standard-consistent.

**Corpus (the team's own):**
- **F85** — the Bergman two-point / VEV mechanism (the induced four-fermion interaction; the condensate direction on the Shilov boundary). The crux for Method 2.
- **F86** — the 3 Korányi–Wolf strata (generation localization).
- **K-Type Address Registry** — the fermion modes' K-type addresses (needed to test whether the top mode = the condensate direction).
- The **Casimir structure** (C₂ = 6; K = SO(5)×SO(2) Casimirs; the SO(2)/hypercharge weight) — for Method 1.

## Recommendation
Run Method 2 (geometric coincidence) as the decisive test — the data points there and it's the precipitation idea made precise — with Method 1 (MAC/Casimir) as the parallel selection computation (it may derive up-vs-down from Casimirs, target-innocently). Method 3 is the fallback if Method 2 says "separate composite." **Tier discipline unchanged:** N_c quark-selection derived; everything else supported/lead; do not bank y_t = 1. This is an advance-or-close investigation, not a forced closure.

— Keeper K767, 2026-07-19. OP-4 investigation plan: sharpened central question (is y_t=1 saturation or O(1) coincidence? data at 0.992 favors saturation/precipitation over the 0.83 Planck-composite). Method 1: MAC/Casimir criterion (ΔC₂) for the selection — target-innocent, seeds up-type via Y²-weighted SO(2) Casimir (4:1), caveat MAC has exceptions. Method 2 (decisive): geometric-coincidence test — does the substrate force the condensate direction = the top K-type mode (→ y_t=1 exactly)? F85 computation. Method 3: is Λ≈10¹⁴ a substrate scale (neutrino Weinberg scale lead?). Web grounding: RDS 1980 MAC, BHL compositeness (both gathered). See [[Keeper_K766_overlap_bound_rules_out_strong_coupling_regime_retires_exponential_2026-07-19]].

## Sources
- Raby, Dimopoulos, Susskind, "Tumbling Gauge Theories," Nucl. Phys. B 169 (1980) — MAC criterion.
- Bardeen, Hill, Lindner — top condensation / compositeness condition; https://en.wikipedia.org/wiki/Top_quark_condensate
- [Composite Higgs models](https://en.wikipedia.org/wiki/Composite_Higgs_models); [Top quark condensate](https://en.wikipedia.org/wiki/Top_quark_condensate)
