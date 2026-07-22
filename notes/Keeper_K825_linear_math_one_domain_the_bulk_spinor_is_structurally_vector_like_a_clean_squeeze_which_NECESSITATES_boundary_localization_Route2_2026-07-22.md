# K825 — "Linear math, one D_IV⁵ domain" (Casey's steer). The single-domain linear algebra gives a CLEAN, decisive statement: the bulk 8-spinor is **structurally vector-like** — a squeeze (any internal SU(2) is either γ⁵-blind → vector-like, or γ⁵-entangled → no L-doublet definable). This is the Witten no-go in one-domain linear-algebra form, and it EXPLAINS the whole arc's vector-like results. Constructive consequence: the SM's chirality-DEPENDENT internal content **cannot** come from the single bulk spinor → the physical L and R must be **different localized (boundary) modes** → Route 2 is NECESSARY, not just an option. Numerically verified in Cl(5,2).

**Keeper | 2026-07-22 | Casey: "Linear math, one D_IV⁵ domain" — a steer away from orbifold-GUT/Pin/extra-dimensional machinery, back to linear operators on the single domain. Following it produces the cleanest statement of the obstruction yet, and a reason Route 2 is forced. Also independently confirms Lyra's 5th-closure refutation. Compute-don't-assert; DIRAC + Route 1 closed.**

---

## Casey's steer, and what it yields
"Linear math, one domain" = don't import orbifold-GUT parity-assignments / Pin structures / extra dimensions; ask what the single D_IV⁵ spinor's own linear operators do. Result: a clean squeeze that settles WHY the bulk is vector-like and WHY Route 2 (boundary localization) is the necessary route.

## The setup (one domain, one spinor)
The physical fermion is the single SO(5,2) 8-spinor (K816: one object, no product). Directions {0,1,2,3}=4D spacetime (γ⁵_4D=Γ₀Γ₁Γ₂Γ₃), {4,5,6}=the extra/internal directions. Clean factorization **8 = 4 ⊗ 2** = (4D Dirac spinor on {0,1,2,3}) ⊗ (internal 2 on {4,5,6}).

## ★ THE SQUEEZE (numerically verified, Cl(5,2)) — the bulk spinor is structurally vector-like
The SM chiral assignment (L⊗doublet ⊕ R⊗singlet) requires an internal SU(2)_L that BOTH (i) **commutes with γ⁵_4D** (so a definite-chirality "L-doublet" is even definable) AND (ii) **acts differently on the two chiralities** (chiral: L=doublet, R=singlet). On the single spinor, no operator does both:
- **Internal SU(2) placed in the clean factor {4,5,6}:** generators M_{45},M_{46},M_{56} **COMMUTE** with γ⁵_4D (disjoint indices, verified). → acts identically on both chiralities → **VECTOR-LIKE** (L and R both doublets). Fails (ii).
- **Isospin SU(2)_L in {1,2,3,4} (F633's embedding):** the self-dual generators J^L_i = ½(M_{jk}+M_{i4}); the M_{i4} pieces (i∈{1,2,3}) **ANTICOMMUTE** with γ⁵_4D (share one index), the M_{jk} pieces commute → J^L_i is **MIXED, does not commute with γ⁵**. → no simultaneous (γ⁵, isospin) eigenstates → **"L-doublet" is not definable.** Fails (i).
- **The SM needs (i)∧(ii) = a chirality-DEPENDENT internal content.** A single fixed spinor carries ONE internal content for the whole object — it cannot assign a doublet to the L part and a singlet to the R part. **So the single bulk spinor structurally cannot realize the SM chiral assignment.**

**This IS the Witten no-go, in one-domain linear-algebra form** — and it explains every vector-like result of the arc (flat index=0, F636, F642): the obstruction is that spacetime chirality and internal isospin are ENTANGLED in the single spinor (they share the {1,2,3} gammas), so they neither commute (→ can't co-label) in the useful embedding nor act chirally in the commuting one.

**Related operator identity (verified):** γ⁵_4D · χ_SO(4) = −Γ₀Γ₄, where χ_SO(4)=Γ₁Γ₂Γ₃Γ₄ is the (2,1)/(1,2) grading. The "chirality–isospin correlation" the SM needs is the operator Γ₀Γ₄ (a tangent generator M_{04} of the domain), but Σ₀₆ (Born=Bergman) anticommutes with it — so holomorphicity does not select it. Consistent with the squeeze.

## ★★ THE CONSTRUCTIVE CONSEQUENCE — Route 2 is NECESSARY, and here's the linear-algebra reason
The SM's chirality-dependent internal content (L=doublet, R=singlet) **cannot** be two halves of one bulk spinor. It requires **L and R to be genuinely DIFFERENT modes, localized differently, each carrying its own internal content.** That is exactly what a **boundary/domain-wall construction** provides and a single bulk spinor cannot:
- A domain-wall/edge zero mode is ONE chirality, localized, and can be assigned ONE internal content; the opposite chirality/content is a DIFFERENT localized mode (or projected out).
- So the SM chiral assignment is a **boundary phenomenon by necessity** — not because Route 1 happened to fail, but because the single bulk spinor is provably vector-like (the squeeze).

**This upgrades Route 2 from "an option that evades F642" (K824) to "the necessary resolution" (K825).** And it stays fully within "one domain": the Shilov boundary is D_IV⁵'s own boundary, not an extra dimension; the L/R-as-different-boundary-modes is linear algebra on the domain's boundary spinor bundle.

## Independent confirmation of Lyra's 5th-closure refutation
Lyra refuted "the naive orbifold reflection = γ⁵." I confirm independently: the naive Z₂ generator (antipodal-S⁴ × π-shift-S¹) = Γ₀Γ₁Γ₂Γ₃Γ₄Γ₅Γ₆ = **ω, the 7-volume = CENTRAL** (commutes with everything, a fixed ±1 = the g=7 orientation) → the projection ½(1±ω) picks the irrep, NOT a chirality. And any single-reflection variant is a 6-gamma that anticommutes with γ⁵ (chirality-mixed). **Neither cleanly projects γ⁵.** ✓ Lyra's refutation stands; 5th pretty closure dead. Her live hope (the orientation-reversing antipodal lift, via a Pin/charge-conjugation structure, could contain γ⁵) is the honest remaining question — and note the SECOND wall (K824/web): orientation-reversal EXCHANGES chiralities (R γ R⁻¹ = −γ) → a pure-reversal projection gives vector-like UNLESS the reversal is correlated with the internal content. Which is exactly the "L and R are different modes" the squeeze demands. **The threads converge: the boundary mechanism must assign different internal content to the L and R localized modes** — that single fact is the whole remaining computation.

## The remaining computation (linear math, one domain, sharp)
**Does D_IV⁵'s boundary (Shilov / its Z₂) localize the L and R fermions as DIFFERENT modes with DIFFERENT internal content (L=doublet, R=singlet)?** Concretely: the boundary spinor bundle — do its localized zero modes carry chirality-correlated internal content (the Γ₀Γ₄ correlation), supplied by the boundary condition where the single-bulk-spinor entanglement is broken? If yes → SM chiral content on one domain → parity DERIVED (+ anomaly-freedom via inflow, K824). If no → derived-CONDITIONAL.

## Tiers / discipline
- **The squeeze (bulk spinor vector-like) is a SOLID linear-algebra result** (numerically verified) — it EXPLAINS the arc and makes Route 2 necessary. Bank as the clean statement of the obstruction.
- **Route 2 (boundary localization realizes the SM chiral assignment) is NECESSARY but NOT YET computed** → held at LEAD. Do not let "necessary" become "derived" — necessity of the route ≠ the route succeeding.
- **Five-Absence:** all one-domain/geometric, no GUT (the orbifold-GUT machinery is NOT imported — Casey's steer keeps it clean). DIRAC + Route 1 closed. `date`.

## Handoffs
- **@Lyra (lead):** the one-domain boundary computation — does the Shilov boundary (or its Z₂, via the orientation-reversing antipodal lift + charge conjugation) localize L and R as different modes with different internal content (L=doublet/R=singlet, the Γ₀Γ₄ correlation)? This is your "one spin-geometry computation," now framed as: does the boundary break the bulk spacetime⊗internal entanglement and assign chirality-dependent internal content?
- **@Elie:** verify the squeeze (internal-{4,5,6} commutes with γ⁵ → vector-like; F633-SU(2)_L in {1,2,3,4} doesn't commute → no L-doublet) on your explicit gammas; then the boundary zero-mode internal content (extend 4784). Harness ready.
- **@Grace:** render the squeeze (why the bulk is structurally vector-like = Witten no-go in linear algebra) + Route-2-necessary; keep the anomaly-inflow bonus attached; tiers honest.
- **@Cal:** the compute-don't-assert gate — "Route 2 necessary" (solid) ≠ "Route 2 succeeds" (open). Five-Absence (no orbifold-GUT import; one-domain linear algebra only).
- **@Keeper:** audit the boundary verdict when it lands; hold the tier; consolidate.

— Keeper K825, 2026-07-22. "Linear math, one domain" (Casey) → the single 8-spinor is **structurally vector-like** (the squeeze: internal-{4,5,6} commutes with γ⁵→vector-like; F633-isospin-{1,2,3,4} doesn't commute→no L-doublet; SM needs chirality-dependent internal content a single spinor can't carry). = Witten no-go in linear algebra; explains the whole arc. **Constructive: the SM chiral assignment is a BOUNDARY phenomenon by NECESSITY (L,R = different localized modes) → Route 2 is necessary, not optional.** γ⁵·χ_SO(4)=−Γ₀Γ₄ (the correlation operator; Σ₀₆ anticommutes → Born=Bergman doesn't select it). Confirmed Lyra's naive-orbifold=γ⁵ refutation (naive gen = ω central). Remaining: does D_IV⁵'s boundary localize L/R as different modes with different internal content? Held at LEAD (necessary ≠ succeeds). Numerically verified Cl(5,2). See [[Keeper_K824_audit_coincidence_negative_PASS_and_robust_which_SU2_answered_graviweak_ruled_out_Route2_boundary_domain_wall_EVADES_F642_the_live_shot_2026-07-22]], [[Keeper_K822_doublecheck_Lyra_F642_CONFIRMED_the_answer_is_DIRAC_the_anticommutator_is_signature_forced_Elie_4781_Weyl_refuted_ω_lock_fails_parity_is_Route_A_2026-07-22]], Lyra (5th-closure refutation + spin-geometry lead), Elie 4784 (index+inflow), F633 (SU(2)_L embedding), Witten no-go.
