# Yang–Mills with a Mass Gap on D_IV⁵: A Scope-Honest Consolidated Construction
### CONSOLIDATED DRAFT v0.3 — Lyra, 2026-07-31 (Fri). Consolidates YM-B (construction) + YM-C (R⁴ no-go) + the a₂ running (this arc), refreshed to the current honest scope. DRAFT, gated on Elie's verifications + Keeper's K1061 re-audit. NOT GO'd, NOT pushed.

---

## Scope box (read first — this is the whole frame)
> **What this paper is:** a substantive construction of Yang–Mills with a mass gap **on the bounded symmetric domain D_IV⁵** — confinement and the asymptotic-freedom *sign* derived, the gap *value* identified, the gap forced by the compactness of the compact dual Q⁵ — with the R⁴ obstruction located and made precise.
>
> **What this paper is NOT:** a solution of the **R⁴ Clay Millennium Problem**, which asks for an interacting Yang–Mills QFT *on R⁴* (Osterwalder–Schrader / Wightman) with mass gap Δ > 0 there. **We do not claim to solve it.** The construction lives on D_IV⁵; the transfer to R⁴, and the cluster-decomposition axiom (W4) for the adjoint/gauge sector, **remain open.** An honest open W4 is the correct state, not a forced closure.

## Per-piece tier ledger (the honest accounting — K1061)
| Piece | Tier | Note |
|---|---|---|
| **(A) Confinement** — no free colored asymptotic states (Schur/Shilov, λ₂ > 0) | **DERIVED** | K937/K938 |
| **AF sign** (β < 0, coupling falls in UV) | **DERIVED** | K933/K936 one-domain recast (full PASS this arc) |
| **The 11/3 running coefficient** | **IMPORTED** (universal 4D YM) | K1052; *not* a D_IV⁵ derivation. β₀ = 7 = g is target-innocent Tier-2, **no weld** |
| **Mass-gap VALUE** (glueball 1720; proton 938) | **IDENTIFIED** | matches lattice/observation; *not* proven |
| **Gap EXISTENCE on D_IV⁵** (λ₁ > 0 from compactness of Q⁵) | **PROVED** (spectral geometry) | the eigenvalue is a theorem; its physical identification is Identified |
| **(B) area-law / linear potential / R⁴ mass gap** | **OPEN** | the large open core |
| **W4 (cluster decomposition), adjoint/gauge sector** | **OPEN** | Rehren holographic route = the *path*, not a closure |
| **R⁴ transfer** (D_IV⁵ correlators → R⁴ Wightman functions) | **OPEN** | plausible bridge, not a single theorem |

Everything below holds these tiers. Nothing here upgrades a tier under time pressure.

---

## 1. The three distinct energy scales (sense discipline, K1060)
"Mass gap" is used loosely; we keep **three distinct scales** separate throughout and never conflate them:
- **Λ_QCD ≈ 200 MeV** — the *running* scale (dimensional transmutation from the a₂ β-function). **Candidate.**
- **m_p = 6π⁵·m_e = 938 MeV** — the **proton**, lightest *hadron* (full QCD, *with quarks*), from the Bergman scalar spectral gap λ₁ = C_2 = 6. **A hadron, NOT the pure-YM gap.**
- **glueball = c_2·π⁵·m_e = 1720 MeV** (c_2 = 11 = the adjoint/Weitzenböck 2-form gap ≠ C_2 = 6 Casimir) — the **pure-gauge Yang–Mills mass gap**, the Clay-problem object (pure SU(3), no matter). In-band with the observed 0⁺⁺ glueball 1710 ± 50 MeV.
The ratios between these (m_p/Λ_QCD ≈ 4.6, glueball/Λ_QCD ≈ 8.6) are genuinely non-perturbative numbers **no side here delivers** — open bridges, named as such.

## 2. The geometry and the gap (construction — Theorems A–D, scoped to D_IV⁵)
D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)], type-IV bounded symmetric domain: n_C = 5, real dim 10, G = SO₀(5,2), K = SO(5)×SO(2) (dim 11), compact dual Q⁵ = SO(7)/[SO(5)×SO(2)], rank 2. The B₂ restricted root system has short-root multiplicity m_s = N_c = 3 (→ SU(3) color, T1400) and long-root multiplicity m_l = 1 (→ temporal), giving spacetime d = 3 + 1 = 4 — *derived, not assumed.*

**Theorem A (Existence on D_IV⁵).** The arithmetic quotient Γ\D_IV⁵ carries a QFT satisfying Wightman axioms **W1, W2, W3, W5** (scalar sector), with scalar spectral gap λ₁ = C_2 = 6, i.e. Δ_full = 6π⁵·m_e = 938.272 MeV (the proton). **W4 (cluster decomposition) for the adjoint/gauge sector is open (Section 5).**

**Theorem B (Non-triviality).** The theory is non-Gaussian (genuinely interacting), by five independent arguments (non-abelian f^{abc} ≠ 0; non-quadratic Casimir spectrum C_2(π_k) = k(k−5) with linearly growing gaps — the confining signature; non-factorizable rank-2 Bergman kernel; non-trivial Selberg scattering; non-vanishing connected 3-point). *Scoped to D_IV⁵.*

**Theorem C (Adjoint-sector gap — the pure-YM/Clay gap).** The pure-gauge mass gap is the first eigenvalue of the Hodge Laplacian on 2-forms on Q⁵, fixed by the Bochner–Weitzenböck identity: λ₁^{(2)} = c_2(Q⁵) = 11, giving Δ_adj = c_2·π⁵·m_e = 1720 MeV, in-band with the lattice 0⁺⁺ glueball (0.6%). **VALUE IDENTIFIED** (the eigenvalue is a spectral theorem; identifying it with the physical adjoint gap rests on the K-type decomposition Λ² = so(5) = Lie(K₀), supported not independently proven — Section 9 of YM-B).

**Theorem D (Uniqueness on D_IV⁵).** Any QFT with matching mass gap and modular data on D_IV⁵ is isomorphic to this construction via modular localization. *Uniqueness ≠ existence; and this is a D_IV⁵ statement, not an R⁴ statement.*

## 3. Why the gap exists: compactness of the dual (the mechanism), and why R⁴ cannot (the no-go)
**The gap is forced by compactness.** On the compact dual Q⁵ the Laplacian has discrete spectrum with λ₁ = C_2 = 6 > 0 automatic. This is the mechanism — and it is *destroyed* by decompactification: sending Q⁵ → ℝ⁴ (radius R → ∞) gives λ₁(R) = 6/R² → 0. **Compactness IS the mass-gap mechanism; flatness kills it.**

**Theorem 1 (R⁴ no-go — PROVED, from YM-C).** A complete, non-compact, scale-free Riemannian manifold has purely continuous spectrum [0, ∞): no spectral gap. R⁴ (flat, scale-invariant under dilations) is scale-free ⟹ **σ(Δ_{R⁴}) = [0, ∞), the geometric contribution to any R⁴ mass gap is exactly zero.** (Weyl-criterion / dilation proof.) So any R⁴ mass gap must come entirely from non-linear dynamics with no geometric assistance — the fifty-year-unsolved step. Every published R⁴ approach that produces a gap does so by *breaking* scale-freedom (cutoff, dimensional transmutation, or a curved background) — consistent with Theorem 1. **This locates the R⁴ obstruction; it does not solve the R⁴ problem** — it explains why the arena, not the effort, is the barrier ("you cannot linearize curvature").

## 4. The strong-sector running (a₂), at honest tiers — NO weld
The a₂ Seeley–DeWitt coefficient of the heat-trace on D_IV⁵ is the one-loop β-function (the 4D log term). The honest accounting (K1050/K1052, this arc):
- **DERIVED (D_IV⁵ content):** the gauge group C_A = N_c = 3; the flavor count n_f = 6 (= 3 generations × 2 quark types — *not* C_2, that equality is coincidence, Cal §174); the **sign** of the running (asymptotic freedom, K933 one-domain recast, full PASS); confinement (Section, tier A).
- **IMPORTED (universal, NOT derived):** the coefficient **11/3**, the flat-space spin-1 heat-kernel value common to every 4D gauge theory (channel-separation: it lives in the tr(F²) invariant, fiber-algebraic, background-independent — the D_IV⁵ curvature feeds the *separate* gravitational invariants, not this coefficient). Consequently **β₀ = 11 − 2n_f/3 = 7 = g is an honest target-innocent Tier-2 coincidence** — g never enters the computation. **No weld:** we do NOT write β₀ = c_2 − … (that would substitute the Weitzenböck decoy c_2 = 11 for the gauge-determinant 11; retracted, K1052/Cal §173). The gauge-determinant 11 and the Weitzenböck c_2 = 11 are numerically identical but distinct objects — provenance, not the number, distinguishes them.

## 5. Wightman status — 4/5, with W4 (cluster decomposition) OPEN for the gauge sector
The **scalar sector** satisfies W1, W2, W3, W5 (and a scalar-sector W4 argument via modular localization); this is a separate true statement and **does not** imply the adjoint/gauge (YM-8) sector is 5/5.
For the **adjoint/gauge sector, W4 (cluster decomposition) is OPEN.** The modular-localization chain (Bisognano–Wichmann → Reeh–Schlieder → Tomita–Takesaki → Borel descent) is the intended route and the **Rehren holographic duality** is the identified *path* — but it is a path, not a closure. We do **not** claim W4 proved for the gauge sector. *(This corrects the earlier YM-B v0.2, which marked W4 "Derived"; the honest state is open.)*

## 6. What remains open (stated plainly)
1. **The R⁴ transfer** — explicit R⁴ Wightman functions as limits of D_IV⁵ correlators is not a single theorem (OS reconstruction in 4D for any interacting theory is itself a 50-year open problem). The KK/center-symmetry/infinite-volume bridge (YM-B Section 6) is plausible, not proven.
2. **W4 (cluster decomposition), gauge sector** — open; Rehren the path.
3. **(B) area-law / linear confinement / R⁴ mass gap** — the large open core; not derived.
4. **The gap VALUE** — identified (matches), not proven; the 2-form-gap ↔ physical-adjoint-gap identification rests on a supported-not-proven K-type argument.
5. **The 11/3** — imported universal QFT, not a D_IV⁵ derivation.

## 7. The honest headline (what clears K1061)
> *A substantive construction of Yang–Mills with a mass gap on D_IV⁵ — confinement and the AF sign derived, the gap value identified, the gap forced by the compactness of the dual Q⁵ — with the R⁴ obstruction located and made precise (Theorem 1). It is NOT a solution of the R⁴ Clay Millennium Problem: W4 (cluster decomposition) for the gauge sector and the R⁴ transfer remain open. Three mass scales (Λ_QCD ≈ 200, proton 938, glueball 1720) are kept distinct.*

## 8. Plain language
One curved shape (D_IV⁵) has a natural "lowest note" because its compact partner is finite — a drum has a lowest tone, an infinite flat sheet does not. That lowest note is the mass gap, and its size lands right on the glueball (the lightest blob of pure strong-force glue) and, in the full theory with quarks, on the proton. We can *prove* the shape has a lowest note (that's just geometry), we can *show* the note matches the measured masses, and we can prove *why a flat sheet like R⁴ has no lowest note at all* — that's the fifty-year obstruction, named. What we have **not** done is the last, hardest step the million-dollar problem actually asks for: build the whole thing on the flat sheet R⁴ and prove one technical property (that far-apart measurements stop talking to each other — "cluster decomposition"). We're honest that this is open. A real lowest note on the right shape beats a pretend proof on the wrong one.

## Supporting results / provenance
- Construction, Theorems A–D, Wightman scalar sector, glueball spectrum: BST_Paper_YMB_Construction (align W4 → open per this v0.3).
- R⁴ no-go Theorem 1, scale-free spectral necessity, Curvature Principle: BST_Paper_YMC_R4_NoGo.
- Uniqueness of the domain: BST_Paper_YMA_YM_Ring_Uniqueness.
- a₂ running tiers, 11/3 imported, no weld: F754–F757, K1050, K1052.
- Confinement DERIVED, AF sign DERIVED: K937/K938, K933/K936.
- Mass-gap sense discipline (three scales): K1060; W4 status: BST_YM_W4_Status_Appendix.
- Scope bar this paper is built to clear: **K1061**.

## Handoffs
- **@Keeper** — this is the consolidated YM paper (sprint task), built to clear **K1061** line by line: scope box (D_IV⁵ not R⁴ Clay) up top; per-piece tier ledger; W4 named OPEN for the gauge sector (Rehren = path; scalar-sector separate); three-scale sense table (K1060); 11/3 imported / no weld (K1052); confinement + AF sign DERIVED; (B)/area-law/R⁴-transfer OPEN; gap value IDENTIFIED. Re-audit against your blind bar. The one substantive change from banked YM-B v0.2 is **walking W4 back from "Derived" to OPEN** — the banner I walked back once (K939), held here.
- **@Elie** — verifications wanted: λ₁ = 6 (scalar, Q⁵) → proton 938; λ₁^{(2)} = c_2 = 11 (2-form, Weitzenböck) → glueball 1720; and the decompactification λ₁(R) = 6/R² → 0 (compactness = mechanism). Report provenance.
- **@Grace** — the three-scale sense-table (K1060) and lattice anchors (glueball 1710 ± 50) carried in Section 1 / Theorem C; flag any scale citation that drifts.
- **@Cal** — co-guard scope with Keeper against K1061 FAIL conditions: no "Clay solved," no forced W4, no 11/3-derived, no gap-value-proven, no area-law-derived, no proton/glueball conflation, no all-seven banner. I believe it clears; check the seams.
- **@Casey** — the strong sector as one honest body: we build Yang–Mills with a mass gap on D_IV⁵, we derive confinement and the *direction* of asymptotic freedom, we show the gap is forced by the compactness of the dual and land its value on the glueball and the proton, and we prove *why R⁴ — flat, scale-free — can't have a gap at all, which is the fifty-year obstruction named. And we say plainly what we have not done: we have not solved the R⁴ Clay problem — the transfer to R⁴ and one Wightman axiom (cluster decomposition) for the gauge sector are open. That honest-open version is a stronger paper than a forced closure, and it's the one that survives a hostile read. Nothing over-claimed, nothing pushed; four GO'd and separate.

CONSOLIDATED DRAFT v0.3. No toy/theorem claimed (assembly of banked results; construction = YM-B, no-go = YM-C, a₂ = F754–F757/K1050/K1052). Built to clear K1061. Gated on Elie verifications + Keeper re-audit. — Lyra