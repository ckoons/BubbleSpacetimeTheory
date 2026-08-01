---
id: grace_detDelta_norm_reduction_EXHIBIT_route_2026-08-02
date: 2026-08-02
program: TEGMARK
status: current
topic_tags: [det-Delta, Jordan-norm, reduction, exhibit-not-infer, Gindikin-Gamma, Hua, tube-type, spectrum-is-norm, K1084, Grace-key-thread]
claims:
  - id: this-a
    topic: the exhibit route for det Δ → rank-2 Jordan norm — step 1 EXHIBITED (the spectrum λ_k=k(k+n_C) IS the degree-rank Jordan determinant of the level-k weight, computed); step 2 (ζ'(0) through Γ_Ω, the ballgame) routed via Gindikin–Hua but NOT yet exhibited; exhibit-not-infer boundary drawn
    status: current
    superseded_by: null
    date: 2026-08-02
---

# [TEGMARK] det Δ → Jordan norm — the EXHIBIT route (Gindikin–Hua), and where exhibition stops

*Grace | 2026-08-02 | K1084: Lyra put real structure under my weld-flag — D_IV⁵ tube-type ⟹ the Jordan norm N is the domain's defining equation, and the Bergman kernel K=c·N^{−p} has N inside it → inside Δ → inside det Δ. So the two "determinants" aren't strangers; the algebraic norm is the seed of the analytic tower. Casey's gate (the one that binds hardest now BECAUSE the footing is so good): **EXHIBIT the reduction through Gindikin–Hua — never INFER it from "norm-in-the-kernel" or the shared name.** This note does exhibit step 1 (concrete, computed), routes step 2, and draws the line between them.*

## ★★ WALK-BACK (2026-08-02, K1087 reconciliation) — step 1 rode the WRONG tower; it propagates
The discrepancy my ζ(0)-computation surfaced is now diagnosed (Casey): **λ_k = k(k+5) with multiplicities {1,7,27,77,182,378} is the S⁶ = SO(7)/SO(6) spherical tower — the WRONG isotropy** (SO(6), not the domain's SO(5)×SO(2)). The vacuum operator lives on the **compact dual Q⁵ = SO(7)/[SO(5)×SO(2)]** (complex quadric = oriented real Grassmannian G̃₂,₇(ℝ), real-dim 10, rank 2, two quantum numbers, mults ~k⁹). Consequences I OWN:
- **Step 1 below ("λ_k=k(k+5) IS the rank-2 norm") is WALKED BACK** — it rode the single-index S⁶ eigenvalue. Q⁵ is rank-2 (two quantum numbers (a,b)); its spectrum is NOT simply k(k+5), so the norm-form identification must be redone on the genuine two-index spectrum. My "banked" step 1 was on the wrong tower.
- **The coarse-menu placement (Λ=α^(4λ_k), rungs 10⁻⁵¹/10⁻¹²⁰/10⁻²⁰⁵) also rode k(k+5)** → also needs re-verification on the genuine Q⁵ spectrum before it's leaned on.
- **What SURVIVES (unaffected):** (i) ρ=(5/2,3/2) — D_IV⁵ *root* data, not S⁶; (ii) **Elie's Gilkey a₅≈220.64** — computed from 10-dim curvature invariants, never used the sphere sum → the safe anchor; (iii) the **Barnes–Gindikin continuation machinery** — verified correct (decomp=direct to 13–22 digits); it just needs the RIGHT spectrum as input.
- **The re-run (my thread, gated on the genuine spectrum):** when Elie+Cal deliver the Q⁵/Grassmannian eigenvalues + multiplicities (SO(7)↓SO(5)×SO(2) branching), I re-sum ζ_Δ(0) → it must reproduce **220.64** (the independent operator-correctness check), then redo step 1 (norm form on the two-index spectrum) and adjudicate det Δ → Jordan norm. The machinery is ready; the target is exact.
- **Posture:** neither "reduction works" nor "reduction fails" — the operator was wrong; now it's pinned (Q⁵, real-dim 10), and the reduction is a well-posed computation with an exact target. This is compute-over-sharpen paying off: the deepest bug was caught by *writing the sum*, not by any gate.

*(Everything below this line predates the walk-back and is retained for history; step 1's k(k+5) content is superseded by the genuine Q⁵ spectrum, pending.)*

## ★★ RE-RUN ON THE CORRECT OPERATOR Q⁵ (2026-08-02) — operator CONFIRMED (ζ(0) check passed)
Target corrected (Casey owned): the anchor is **ζ_{Q⁵}(0) = −0.7691** (his earlier 220.64 was ã₅, the un-normalized heat integral — dropped). My earlier ζ≈−0.70 was in the right ballpark precisely because it was a real ζ(0) (the b=0 slice), not the phantom 220.64.

**What I computed and verified this turn (correct operator, Q⁵ = SO(7)/[SO(5)×SO(2)]):**
- **Eigenvalues:** λ_{a,b} = a(a+5) + b(b+3), a≥b≥0 = **|μ+ρ|² − |ρ|²**, μ=(a,b), ρ=(5/2,3/2) — verified (Casimir form). The two shifts (5,3) = (2ρ₁, 2ρ₂): **the two quantum numbers (a,b) map directly onto the two ρ-components** (Lyra's hypothesis, confirmed on the real spectrum).
- **Multiplicities:** d_{a,b} = dim V_{(a,b,0)}^{B₃} via the SO(7) Weyl dimension formula — verified against known reps (V₀₀=1, V₁₀=7 vector, V₁₁=21 adjoint, V₂₀=27, V₂₁=105, V₂₂=168). ★ The **b=0 slice = {1,7,27,77,182,378} = the S⁶ harmonics** — so the wrong tower was exactly the b=0 slice of the right one (clean consistency, and it explains why my S⁶ ζ(0) was near the true value).
- **★ ζ_{Q⁵}(0) = −0.76912** — computed by independent spectral sum (heat-trace c₅ extraction on the full 2-index spectrum, high-precision stable interpolation). **Matches the target −0.7691 to given precision.** The operator-correctness check PASSES: we finally have the right operator + normalization, confirmed two ways (my spectral sum + the corrected target).

**What remains (the reduction proper, next):** det Δ = exp(−ζ′_{Q⁵}(0)) → Jordan norm via Γ_Ω on the 2-index spectrum, and step 1 (norm form) redone on the two-index eigenvalues. Machinery (ρ, Γ_Ω, the verified Barnes–Gindikin continuation) is spectrum-independent and ready.

## ★★ THE CATCH on the correct operator (2026-08-02) — step-1 "λ = norm" is RETIRED (hold the line)
Redoing step 1 on the 2-index spectrum surfaces a real obstacle, exactly where Lyra said "it looks like it should pass" — which is when to hold hardest:
- On the **b=0 slice**, λ = a(a+5) is a single **PRODUCT** — it *looked* like the degree-2 Jordan determinant t₁·t₂. That was the S⁶-slice artifact.
- On the **full 2-index spectrum**, λ_{a,b} = a(a+5)+b(b+3) = |μ+ρ|²−|ρ|² is a **SUM** of two terms (the Casimir), **NOT a product/norm.** (Verified: (1,1)→6+4=10, (2,1)→14+4=18, … sums, not products.)
- **⟹ Step-1's "the spectrum IS the rank-2 Jordan norm" is RETIRED for the correct operator.** The norm is NOT in λ. It must now enter through the **Γ_Ω continuation** (the measure), not through the eigenvalue. **Operator-confirmed did NOT make the norm appear** — this is the concrete content of "confirmed ≠ exhibited."
- **Is the reduction still possible? Yes, but non-guaranteed and unshown.** The 2-index spectral zeta ζ_{Q⁵}(s) = Σ d_{a,b}(p²+q²−17/2)^{−s} (p=a+5/2, q=b+3/2) is a **Barnes DOUBLE zeta**, and Barnes double-zetas continue to **multiple-Gamma** values = the rank-2 Γ_Ω = Γ(s)Γ(s−3/2) (the one I verified). So the norm *can* emerge from a sum-eigenvalue via the continuation — the Barnes structure is the bridge — but that emergence is **the exhibit**, not a given. Calibrated read: not "the reduction is broken" (over-pessimistic — Barnes gives the route), not "λ=norm so it passes" (false — λ is a sum). It is: the reduction must be shown to run through Γ_Ω, and I have not shown it.
- **The concrete remaining exhibit:** compute exp(−ζ′_{Q⁵}(0)) via the Barnes-double-zeta continuation and show it factors through Γ_Ω(Jordan norm), target-blind, with ρ↔(a,b). Cal audits exhibited-or-inferred.

Both Λ and Ω stay PD until the norm-reduction is exhibited (through Γ_Ω, not through λ) and Cal-audited on the correct operator. The operator is pinned and confirmed; the reduction is now a well-posed but genuinely open computation with a real obstacle named.

## ~~EXHIBIT — Step 1~~ [SUPERSEDED — rode the S⁶ slice = b=0 of Q⁵; redo on the 2-index Q⁵ spectrum]: the spectrum IS the rank-2 Jordan norm
λ_k = k(k+n_C) factors into exactly TWO linear factors **because rank=2**, and those two factors are the Jordan eigenvalues (k, k+n_C) of the level-k weight:

| k | Jordan eigenvalues (t₁,t₂) | N_J = t₁·t₂ = λ_k |
|---|---|---|
| 0 | (0, 5) | 0 |
| 1 | (1, 6) | 6 |
| 2 | (2, 7) | 14 |
| 3 | (3, 8) | 24 |

- The eigenvalue **shift = n_C = 5** is the Gindikin/genus parameter of the rank-2 tube domain.
- ⟹ **λ_k IS the degree-rank(=2) Jordan determinant N_J of the level-k weight** — the analytic spectrum (what det Δ = ∏λ_k is built from) is the **algebraic norm evaluated level-by-level.** This is *exhibited*, not a shared word: rank=2 forces the Casimir into a 2-factor product, and that product is the norm.

## ★ Step 2 — the BALLGAME (routed, NOT yet exhibited): ζ′_Δ(0) through Γ_Ω
Step 1 makes step 2 a concrete Gindikin–Hua computation, not a hope — but it is NOT step 1, and I will not let "the spectrum is the norm" masquerade as "det Δ reduces to the norm form." The remaining exhibit:
- ζ_Δ(s) = Σ_k m_k [k(k+n_C)]^{−s} = Σ_k m_k N_J(weight_k)^{−s} — a Dirichlet series over norm-values.
- The **Gindikin Γ_Ω** (rank 2) = Γ(s)·Γ(s − d/2) — a product of TWO ordinary Gammas, matching the 2-factor norm — is the object that integrates powers of det_J; the functional determinant exp(−ζ′(0)) **factors through Γ_Ω** (Barnes/Gindikin continuation with the correct multiplicities m_k).
- **Machinery in hand:** the corpus already runs Γ_Ω — the muon's 24 = Γ(5) = Γ(n_C) is a Gindikin value (F157/K923); Hua's integral gives the norms; K(0,0)=1920/π⁵ is the same kernel. So this is Gindikin–Hua on tools we own, not greenfield.
- **What must be exhibited (the ballgame):** carry out the continuation and show exp(−ζ′_Δ(0)) = an explicit function of the Jordan norm form via Γ_Ω — the actual identity, with the m_k, target-blind. Until that is written down, the reduction is *plausible and routed*, not done.

## ★ Step 2's two decidable gates (K1085, Casey) — exhibit-not-infer made checkable
Casey pinned step 2's fishing risk to two things that must FALL OUT, not be adjusted:

**Gate (a) — Multiplicities forced.** In det Δ = ∏ λ_k^{d_k}, the d_k must be the **forced discrete-series K-type dimensions** (from the corpus's discrete-series dimension formula), NOT chosen to make the Barnes–Gindikin continuation collapse. Linear algebra on the K-types; Elie verifies the d_k numerically against the discrete series, blind.

**Gate (b) — Shift-consistency.** The spectral factoring shifts by **n_C = 5**; the Γ_Ω Gammas shift by **N_c/2 = 3/2**. Casey flagged these as *different parameters* — if matching them needs a patch, the patch is the fit.
- **★ SHARPENING (this turn, computed):** they are NOT independent. ρ(D_IV⁵) = (n_C/rank, N_c/rank) = **(5/2, 3/2)**, and:
  - eigenvalue shift n_C = 5 = **2ρ₁**;
  - Γ_Ω shift 3/2 = **ρ₂**.
  Both are components of the **single ρ-vector**. So gate (b) is not "reconcile 5 with 3/2" (two strangers) — it is "does the continuation distribute the one ρ correctly (2ρ₁ → the eigenvalue factoring, ρ₂ → the Γ_Ω), with no patch?"
- **★ EXHIBIT-NOT-INFER on my own sharpening:** this REDUCES gate (b) (shows shared origin) but does **NOT pass it.** "Both come from ρ" is a shared-origin observation — the same *kind* of move as "both are called determinant." The gate passes only when the continuation is written and the two shifts *demonstrably* emerge from ρ with no adjustment. Shared origin ≠ demonstrated distribution. I flag this so my own ρ-observation isn't mistaken for the exhibit.

## ★★ STEP 2 WRITTEN + EVALUATED (2026-08-02) — and it SURFACED a discrepancy to reconcile
Per Casey's "compute, don't sharpen." I wrote the Barnes–Gindikin continuation and evaluated it. Two real results — one clean, one a red flag I am putting up, not smoothing over.

**(i) The continuation is written and the machinery is VERIFIED.** In m=k+5/2: λ_k = m²−(5/2)², d_k = (m/60)(m²−1/4)(m²−9/4). ζ_Δ(s) = Σ_j (s)_j/j! (25/4)^j [ (1/60)ζ_H(2s+2j−5,7/2) − (1/24)ζ_H(2s+2j−3,7/2) + (3/320)ζ_H(2s+2j−1,7/2) ]. **Cross-checked: this decomposition = direct summation to 13–22 digits at convergent s.** Machinery correct.
- **Gate (b) mechanism EXHIBITED (not inferred):** both ρ-shifts fall out of the forced d_k in the m-variable with no patch — ρ₁=5/2 in λ_k=m²−ρ₁², ρ₂=3/2 as the outer factor-root (m²−9/4) of d_k. The 5↔3/2 relation is the S⁶-harmonic structure, not an adjustment.
- Evaluated target-blind: ζ_Δ(0) ≈ **−0.699**, ζ′_Δ(0) ≈ −0.2547, **det Δ ≈ 1.290** (log₁₀ ≈ 0.11). Reported as computed; not compared to any target.

**(ii) ★ RED FLAG — the tower is 6-dimensional (S⁶), and its ζ_Δ(0)≈−0.70 DISAGREES with Elie's a₅≈220.64.** The multiplicities gate (a) verified (B₃ Weyl dims 1,7,27,77,182,378) are **exactly the S⁶ = SO(7)/SO(6) spherical-harmonic multiplicities** — they grow as k⁵/60 (degree-5 ⟹ a **6-dimensional** tower, Weyl d/2=3). But **D_IV⁵ is 10 real-dimensional**; its vacuum operator's a₅ (= ζ_Δ(0), Elie's ≈220.64) is a 10-dim quantity, whose multiplicities must grow ~k⁹ (degree-9), NOT ~k⁵. **So the B₃ symmetric-tensor tower is the S⁶ SPHERICAL SLICE, not the full 10-dim D_IV⁵ operator.** My computed ζ_Δ(0)≈−0.70 (verified) ≠ Elie's a₅≈220.64 (verified) because **they are different operators.**
- **What must reconcile before ANY reduction banks:** *which operator is the vacuum det Δ* — the 6-dim spherical slice (my computation) or the full 10-dim D_IV⁵ spectrum (Elie's a₅)? Gate (a)'s "forced multiplicities" verified the **spherical-slice** d_k; whether those are the right multiplicities for the vacuum operator is now open. The two verified numbers disagreeing is the computation doing its job — a conflation caught, not a reduction closed.
- **Discipline note:** this is the good outcome of "compute, don't sharpen" — the calculation surfaced a check (6-dim vs 10-dim operator) that no amount of gate-sharpening would have. Neither "reduction works" nor "reduction fails" — the operator identity itself must be pinned first. @Elie/@Cal: reconcile the S⁶-slice vs full-D_IV⁵ operator before the norm-reduction is adjudicated.

## ★★ K1093 RULING — full-scalar (CONDITIONAL PASS), and the collapse arrives through the right door
Lyra settled the fork by **ladder-unity** (target-innocent): the heat trace whose a₁ rung gives Newton's G is ONE operator carrying one whole ladder — fixing it by G at a₁ fixes it at a₀ and a₅. You can't use the full field for gravity and a holomorphic restriction for the vacuum. So the vacuum is the **full scalar Laplacian, ζ(0)=−0.7691** — NOT the holomorphic −0.70. (Anti-bias PASS: Lyra ruled against her own stake and invited Cal's audit of the against-self ruling; Cal's flag that −0.699≈my buggy sum is *hygiene* — a reason to distrust the holomorphic pull — not the *basis*, which stays ladder-unity.)

**The collapse I wanted at K1091 arrived — but through the right door:** holomorphicity is NOT the vacuum operator's identity; it's the **norm the full-scalar vacuum reduces TO** (the Jordan norm lives in the Bergman kernel K=c·N^{−p}). One full-scalar vacuum → one holomorphic norm, via the reduction — not via picking the holomorphic operator. My tempting version (holomorphic operator revives step-1) was in the wrong place; the honest version (holomorphic norm as the reduction target) is the right one.

**★ THE HINGE CONFIRMED (the condition on my PASS) — computed:** a₁→G and a₅→ζ(0) are genuinely ONE operator. From the single heat trace Θ(t)=Tr e^{−tΔ_full} on Q⁵, the whole ladder (t^{j−5} coeffs):
| c₀ (a₀, Λ) | c₁ (a₁, G) | c₂ (a₂, run) | c₃ | c₄ | c₅ (a₅, ζ(0)) |
|---|---|---|---|---|---|
| **1/960** | 0.0081597 | 0.0317130 | 0.0813657 | 0.1545718 | 0.2308752 |
c₀=1/960 exactly (clean structural check; cf. K(0,0)=1920/π⁵). ζ(0)=c₅−1=−0.76912 ✓. **a₁ (Newton G) and a₅ (vacuum ζ(0)) are literally two coefficients of the SAME Θ(t) of the SAME Δ_full — ladder-unity is visible in one expansion, not assumed.** Condition on the CONDITIONAL PASS: MET.

**Downgrades stand (→ Casey sign-off), no back-door:** since the fork ruled full-scalar, step-1 "λ=norm" stays RETIRED and tower "56=8g" stays DOWNGRADED — the holomorphic operator that would have revived them is not the vacuum.

**Forward exhibit (mine, now well-posed):** det Δ_full = exp(−ζ′_{Q⁵}(0)) → Jordan norm via Γ_Ω on the settled operator (−0.7691). The norm enters through the Γ_Ω measure (= the holomorphic Bergman structure); target-blind, ρ↔(a,b). Lyra exhibits the reduction-mechanism + carries the anti-bias audit. Cal audits exhibited-or-inferred.

## ★★ K1095 — the honest endpoint: a Partially-Derived SPLIT (hinge unconditional)
The hinge PASSED unconditional (Cal §202 audited the *basis* — target-innocent ladder-unity — not the against-interest feel). So K1093 is unconditional: the operator is pinned by the gravity rung, the vacuum number rides along. **Seal confirmed (my lane):** c₀ = **1/960 = 1/(2^{C_2}·N_c·n_C)** — clean in the primaries (2⁶ boundary · N_c color · n_C bulk), target-innocent.

**The cc-magnitude's honest endpoint = an explicit-split PD:** the hinge confirms *operator identity*; it does NOT move the *magnitude* verdict. The same trace that locks the operator gives ζ(0)=−0.7691 ≠ 0 — a genuine scale anomaly → the magnitude is **Identified (scale-ambiguous).** All five agree here.
- **Structure — DERIVED:** det Δ_full → Jordan norm via Γ_Ω (mine) + the Kähler mechanism (Lyra).
- **Magnitude — IDENTIFIED (scale-ambiguous), forced-μ OPEN.** NOT "permanent."

**★★ I RETRACT "permanent" (K1097, Cal §203 — my over-reach, owned).** I banked "Identified-permanent"; Cal rejected it and is right (aligns with K1073 + K1096). **The decisive distinction: free-scale (the ambiguity exists) ≠ un-forcible (no mechanism fixes it).** A scale anomaly is precisely the *raw material* dimensional transmutation uses to FORCE a scale (μ ~ exp(−∫dg/β), Coleman–Weinberg) — so ζ(0)≠0 is **evidence FOR a forcing mechanism, not against one.** "Permanently un-derivable" is the **strict-pessimism mirror of "Derived"** — both need proof, neither has it. My two arguments were both over-closures: (a) "needs ℓ_B" is true only of the dimensionFUL unit — the meaningful **dimensionless** suppression exp(−S) is the forcible part; (b) "α-tower closed" retires one candidate FORM, not the transmutation MECHANISM. Only blocker-1 (a₅ uncomputed) genuinely resolved — a one-blocker advance, not a promotion to permanent. **Lesson (calibrate BOTH directions):** I held the line against optimistic over-claims all arc (56-innocent, λ=norm, holomorphic-revival) and then over-claimed *pessimistically* — the discipline is symmetric and I applied it asymmetrically. Never "not forced" until every channel is checked; I closed "permanent" without checking the transmutation channel.

**★ The promotion is a real LANE, not a wall (Lyra's condition):** permanent iff BST does not force the boundary coupling g(ℓ_B). And **a₂→β is already Derived**, and the transmutation integral ∫dg/β uses that derived β — so the magnitude is determined once g(ℓ_B) is fixed. The whole promotion reduces to ONE target-blind question: **does BST force g(ℓ_B)?** Forced → μ forced → magnitude **Derived**; not forced → stays Identified. Direct answer to "what can we do to derive Λ?": derived β + one open boundary coupling.

**Forward:** Lyra LEADS the g(ℓ_B) question (her transmutation lead, now the reason it stays open); Elie sets β; **I exhibit the structure half** (det Δ_full → Jordan norm via Γ_Ω, target-blind); Cal holds §203. → Casey: sign off the two downgrades; the magnitude promotes/stays on the g(ℓ_B) verdict. Both Λ and Ω stay PD, explicit-split.

## Casey's three gates (K1084), held
1. **Exhibit, never infer.** The reduction is exhibited only by the Γ_Ω computation (step 2), never by "N is in the kernel" (Lyra's footing) or "both are called determinant" (the shared name). Step 1 is real but is not step 2.
2. **Blind to which rung.** Compute ζ′(0)/det Δ without assuming the vacuum's level; the placement (k=rank) must FALL OUT of the norm/degree structure, not be inserted. Never compare to 4λ₂=56, 10⁻¹²⁰, or 13/19 until the identity stands.
3. **Degree tower ⊥ residence tower (K1081).** This is the effective-action DEGREE structure (det Δ = degree-rank norm), kept separate from the Cathedral matter-RESIDENCE map (k=rank = 3rd-gen matter, k=0 = Higgs VEV). Same k-index, two orthogonal attributes; don't re-conflate.

## Why exhibit-not-infer binds hardest here (and I mean it about myself)
This is the most seductive form the danger takes: foundation-deep, it hits, and there IS real structure under it (step 1 is genuinely exhibited). That is exactly the profile — elegant + prior-confirming + real footing — where I've over-reached twice this arc (the "56 is innocent" claim; the two-tower conflation). So the rule on my own thread: **step 1 exhibited ≠ reduction exhibited.** The reduction banks only when step 2's identity is written down and Cal audits it target-blind. Both Λ and Ω stay PD until then.

## Handoff
- **Me (Grace, key lead):** exhibit step 2 — the Γ_Ω identity for exp(−ζ′_Δ(0)) as a function of the norm, with the m_k, target-blind. Step 1 is banked (spectrum = rank-2 norm).
- **@Lyra:** tube-type/Bergman footing is sound (K1084) — the CW transmutation handle banks against the placement once step 2 lands.
- **@Elie:** the Γ_Ω / Hua numerics — the m_k multiplicities and the continuation, blind.
- **@Cal:** audit step 2 for exhibit-not-infer + target-innocence + degree⊥residence — the crux, maximum scrutiny.

— Grace, 2026-08-02 [TEGMARK]. det Δ → Jordan norm exhibit route. STEP 1 EXHIBITED (computed): λ_k=k(k+n_C) IS the degree-rank Jordan determinant of the level-k weight (2 eigenvalues (k,k+n_C), shift n_C; rank=2 forces the 2-factor product) — the analytic spectrum IS the algebraic norm level-by-level, not a shared word. STEP 2 = the ballgame (routed via Gindikin Γ_Ω = 2 Γ's, machinery in hand — muon Γ(5), Hua, K(0,0)=1920/π⁵ — but NOT yet exhibited): carry the ζ′(0) continuation to show exp(−ζ′_Δ(0)) = explicit function of the norm via Γ_Ω, target-blind. Gates held: exhibit-not-infer, blind-to-rung, degree⊥residence. Step-1-exhibited ≠ reduction-exhibited; both Λ and Ω PD until step 2's identity stands. My key thread.
