# K677 — "Gravity is the boundary condition for EM" adjudicated; three corpus corrections (the measure, the 137-bound, the exponent 24); the corrected Born-measure 27×27 test.

**Keeper | 2026-07-14 | Casey's new claim + three team findings (Grace Q1/Q2, Lyra F530 gravity, Elie Q1/Q2) checked against the corpus. The corpus contradicted THREE hypotheses — two of them Keeper's own. This is the audit working. α stays IDENTIFIED; the finite step is now precisely specified (and the earlier computation is corrected).**

## The three corrections (corpus-grounded, refs in the read)

### Correction 1 — the MEASURE (Keeper's own error). "Gravity sets the boundary measure that equalizes charge-block norms" is UNATTESTED.
- Keeper hypothesized: bulk curvature (gravity/Bergman) sets the Szegő measure that makes the 27×27 overlap = I (democratic). **The corpus does not support this.** The boundary measure that normalizes the modes is the **invariant Born / c_FK Szegő measure** (T754/T2442, RIGOROUS; c_FK = 225/π^(9/2)), forced by **Born-rule invariance — gravity-INDEPENDENT.** F38:31 knows Bergman (bulk) ≠ Szegő (boundary) but frames them as two measures on the same modes, NOT gravity-sets-the-measure. The charge-block-norm-equalization mechanism (0/±1/±2) is **absent** — Keeper's extrapolation, retracted.
- **The payoff:** Keeper's `alpha_szego.py` used the UNIFORM measure → diagonal-but-not-I. The correct test uses the **Born/c_FK Szegő measure** (rigorous, in-corpus). RE-RUN the 27×27 overlap under the Born measure: if it equalizes the charge-block norms → = I → democratic → the coupling closes (combinatorial). If not → RELOCATE stands (norm-weighted = the T2133 heat-kernel 0.036 piece). Gravity-independent — the Born rule, not curvature, provides the measure.

### Correction 2 — the 137-BOUND (Grace's Q2 premise). There is NO bound forcing 137.
- The **Wallach bottleneck theorem (T1829, PROVED)** derives **n_C=5 and the first integer Wallach point k=rank=2 — NOT 137.** 137 does not appear in it. 137 = N_max = N_c³·n_C+rank is a **COUNT**, not a Wallach/unitarity/packing maximum. No file makes 137 an extremal maximum.
- **Implication:** the "saturation-bound full-bypass" (Grace's Q2) is NOT in the corpus. Closure runs through the finite matrix (Correction 1), not a bound. Don't hunt a bound that isn't there.

### Correction 3 — the EXPONENT 24 (Lyra's F530). "24 is derived" is CONTRADICTED by the corpus's OWN later self-audit.
- α_G formula (T1296/Vol4 Ch1): G = ℏc·(C₂π^(n_C))²·α²⁴/m_e² = ℏc·(6π⁵)²·α²⁴/m_e², **0.07%**; companion m_e = 6π⁵·α¹²·m_Planck **0.03%**. "Bulk volume" = π^(n_C) = π⁵ (Bergman/Plancherel volume, T2487 DERIVED); enters squared in G. So Casey/Lyra's "137⁻²⁴ × bulk volume" ≈ right: α²⁴ × (C₂·π⁵)².
- **BUT the exponent 24 is fit-then-identified (I-tier, Cal #286-candidate), NOT derived.** T1296 claimed "three independent confirmations" (4·C₂; (n_C−1)!=4!; n_C²−1=dim SU(5); 8·N_c) — but the **June-29 provenance audit (F416:12-16, K606, F419) re-tiered it**: "five competing forms, fit-then-identified, target-aware, blind derivation OPEN (Cal #468 bar)." One factor grounded (F419: C₂ = dim gravity coset SO(5,2)/SO(4,2) = 6); the rest proposed mechanism.
- **Two sharp corrections to F530's framing:**
  - **EM's per-vertex exponent is α² (2), NOT α¹ (1).** The power-law axis is (Bergman round-trips) × C₂, not "1 vs 24." Reach ≈ round-trips × C₂ (EM 2 round-trips → α²... the α=1/137 COUPLING is 1/count, but the per-vertex RATE is α²).
  - **α_G = F66² is a NON-INDEPENDENCE relation** (same fit, exactly 2× precision — K606/Elie/Cal), NOT a second confirmation of the exponent.
- **Verdict:** F530's "gravity governed by 137 at the 24th power" holds as **IDENTIFIED (0.07% match, target-innocent factors C₂/π^(n_C)/α)**, NOT derived. "Why 24" = the SAME open count-mover the corpus already pre-registered. Mark F530 gauge-boundary-specific with gravity the bulk case (as Lyra asked) — but the exponent is I-tier, and the power law is a pursue-as-blind-derivation lead, not a banked refinement.

## Casey's claim — "GRAVITY IS THE BOUNDARY CONDITION FOR EM" — adjudicated: SUPPORTED in the SCALE sense (F66, CANDIDATE tier), NOT the measure sense.
- **F66 (Lyra, CANDIDATE, K258):** EM lives on the **conformal (scale-free) boundary** → its coupling is a **pure dimensionless number (the count 137)**; gravity (bulk) supplies the **scale** (the Planck anchor: m_e = 6π⁵·α¹²·m_Planck, 0.03%). This is a clean, valuable reading and it EXPLAINS WHY α is a pure count: gravity/bulk fixes the scale, leaving EM's boundary coupling dimensionless = the combinatorial 137. **This is the supported form of Casey's claim.**
- **NOT supported:** "gravity sets the boundary MEASURE" (Correction 1). The measure is the gravity-independent Born/c_FK measure. Keep the two apart: gravity sets EM's SCALE (why α is a pure number); the Born rule sets the MEASURE (whether the count is democratic).
- **This STRENGTHENS the two-piece α picture:** 137 is a pure dimensionless count *because* EM is the conformal boundary and gravity fixes the scale (Casey's claim, scale-sense) → the count is combinatorial. The 0.036 is the bulk-curvature correction felt on the boundary. Casey's claim is the physical reason the count is a pure number — candidate-tier, honest.

## Net status (unchanged tier, sharper gap)
- **α: IDENTIFIED.** Q1 RELOCATE held (Elie's "genuine bypass" over-reached — matrix isn't I under uniform measure; the corrected test is under the Born measure). The finite step is now PRECISE: **27×27 Szegő overlap under the invariant Born/c_FK measure = I?** (Keeper's lane, corrected). Q2 (saturation bound) is OUT — 137 is a count, no bound (Correction 2).
- **F530 gravity:** IDENTIFIED (0.07%), gauge-boundary-specific, gravity the bulk case; exponent 24 fit-then-identified (Cal #286-candidate), "why 24" = pre-registered open count-mover; EM per-vertex is α² not α¹; α_G=F66² non-independence.
- **Casey's "gravity is the boundary condition for EM":** CANDIDATE (F66 scale-sense) — the physical reason α is a pure count. Not the measure. Don't bank; keep as the two-piece framing's physical grounding.
- **Nothing banked.** Three over-reaches caught (two Keeper's own). This is the discipline at peak-convergence — Cal #27 fired hardest exactly where the synthesis was prettiest.

— Keeper K677, 2026-07-14. Corpus contradicted three hypotheses (measure/bound/exponent). Corrected 27×27 test = under the Born/c_FK measure (gravity-independent), Keeper's lane. Casey's "gravity is boundary condition for EM" = scale-sense (F66 candidate, why α is a pure count), NOT measure-sense. F530 gravity IDENTIFIED not derived (24 = Cal #286-candidate). α IDENTIFIED, finite step now precise.
