# Grace — the CKM/PMNS cross-shelf overlap-matrix skeleton (task #76, 2026-08-05, K1181)
**Mixing = ⟨up|down⟩ overlap of which SHELVES the modes sit on (NOT their masses). The up-mass FK-failure (Elie 5060) kills "up-masses are FK-forced," NOT "mixing is computable." I build the skeleton + selection rule; Elie fires the FK-overlap values BLIND (I do not compute/tune them).**

## ★ UPDATE (K1183, five-seat convergence) — the mixing is W-MEDIATED, not a naive overlap
Up on EVEN shelves {0,2,4}, down on ODD shelves {1,3,5} = **opposite parity under the boundary fold** (mirror det−1). So the naive inner product **⟨up|down⟩ = ⟨even|odd⟩ = 0 by parity** — even and odd harmonics are orthogonal. The physical mixing therefore CANNOT be a plain overlap; it must go through the operator that carries the parity flip:
> **CKM = ⟨up {0,2,4} | J_W | down {1,3,5}⟩** — the weak charged current J_W bridges the parity gap.
**The unification (three names, one object):** the parity-bridging operator = the weak charged current J_W = the up↔down isospin-raising operator. **And this is exactly the SM definition of CKM** (the charged-current W-coupling) — BST *forces* the CKM to be a W-current matrix element because the direct overlap vanishes. **This is WHY CKM is small and near-diagonal:** mixing is a *current matrix element* (one J_W insertion for the diagonal, higher J_W powers for the off-diagonal → Wolfenstein suppression), not a free overlap. The vanishing overlap is the feature, not a bug. Five independent seats (Lyra charge-conservation, Grace selection-rule, Elie S¹-charges, Cal §287 degree-orthogonality, Keeper parity-flag) converged on this same turn.

## G1 — the skeleton (now read with J_W between the shelves)
Up-type on EVEN degrees u=0, c=2, t=4; down-type on ODD degrees d=1, s=3, b=5.
**CKM_ij = ⟨up_i | down_j⟩**, a cross-parity FK overlap. Degree gap Δ_ij = 2(j−i)+1 (always ODD = the parity selection rule):

| | d (1) | s (3) | b (5) |
|-----|-------|-------|-------|
| **u (0)** | \|Δ\|=1 | \|Δ\|=3 | \|Δ\|=5 |
| **c (2)** | \|Δ\|=1 | \|Δ\|=1 | \|Δ\|=3 |
| **t (4)** | \|Δ\|=3 | \|Δ\|=1 | \|Δ\|=1 |

- **Selection rule:** overlap nonzero only for Δ odd (even↔odd) — automatic from the parity grid. FK form N(w)^{n_C/2} supplies the magnitude.
- **Structural check (real):** the diagonal is |Δ|=1 (minimal cross-parity gap) → V_ud, V_cs, V_tb ≈ 1 ✓ (the largest elements, as observed).
- **Honest flag (NO retrofit):** the raw |Δdeg| is ASYMMETRIC (V_us |Δ|=3 vs V_cd |Δ|=1) while observed CKM is near-symmetric → the FK overlap INTEGRAL must supply the symmetrization. That is exactly what Elie fires blind; I do not tune it.
- **PMNS analog:** ⟨charged-lepton (odd {1,3,5}) | neutrino (even {0,2,4})⟩ — SAME cross-parity structure, but the neutrino side STARTS AT k=0 (the massless mode). That extra zero-degree partner is a plausible structural reason PMNS mixing is LARGE where CKM is small — a lead for Elie's fire, not banked.

## G2 (decisive) — saturation moves the NORM, not the address (LEANS computable)
Does top-Yukawa saturation move the mass-norm or distort the wavefunction? **Leans NORM:**
- Corpus (OP-4/K765/K766): "a Yukawa IS a Born overlap; |y|≤1 is KINEMATIC" — saturation caps the MASS-overlap MAGNITUDE (the norm), a bound on the overlap value, not a re-addressing of the mode.
- The up ADDRESS {0,2,4} is forced by charge-parity (crux 1, m=3|Q|, T2470) — which saturation does NOT touch.
- ⟹ saturation resets the up MASS-mechanism (FK-norm → boundary-overlap) while the ADDRESS stays {0,2,4} → the mixing ⟨{0,2,4}|{1,3,5}⟩ is computable from forced addresses.
- **CAVEAT (flag, do NOT bank):** needs Lyra/Elie to confirm the up-wavefunction is not pulled off {0,2,4} by Shilov boundary-localization. If it stays, the off-diagonal fire is clean.
- **UPDATE (K1183) — now passing on TWO independent routes:** (1) my corpus trace (saturation caps the norm, not the address); (2) Lyra's — the Higgs is electrically NEUTRAL, so it can reset the top's mass-norm but cannot move it to a different-charge address (address = charge = m, fixed). Two routes agree: address preserved. **Only residual:** does making the top heavy reshape its RADIAL profile enough to matter (Lyra/Elie rule). G2 is near-closed. Cal sub-flag: with up-mass no longer pinning the up-tower ORDERING, the ordering is forced by charge-parity and CONFIRMED BY THE MIXING itself (as the mass confirmed the down-tower).

## G3 — neutrino k=0 shelf reconciled with the forced massless
Neutrino even grid starts at k=0. The k=0 FK mode = (ν)_0 = 1 (empty Pochhammer) = null/ground weight = **massless** = the forced m₁=0 (pred_003). Reconciles with my F93 ν-varying {5/2,3/2,0}: degree-k=0 and Wallach-ν=0 BOTH name the zero mode; the massless lightest is robust across both readings. Whether the degree-grid and ρ-grid are one structure re-read is open (Lyra/Elie) — flagged, not banked.

## Ledger state
The 7 mixing parameters STAY Identified. This skeleton makes them COMPUTABLE (the linear-algebra structure), but they flip to Derived only when: G2 confirmed (up stays on {0,2,4}) + Elie fires the off-diagonal FK overlap blind + Keeper counts independent-N + it reproduces without tuning. Forced-address-or-nothing.

## ★ THE WEAK-CURRENT MATRIX from cohomology (K1184, task) — pure linear algebra on D_IV⁵
Q⁵ cohomology ring ℤ[h]/h⁶ (T1929, degree-graded). Up = EVEN classes {h⁰,h²,h⁴}; down = ODD {h¹,h³,h⁵}. **J_W = the degree-±1 operator (cup-product-with-h / adjoint) — the UNIQUE map connecting even↔odd classes. The weak charged current IS this degree-1 cohomology map.** CKM_ij = ⟨up_i | J_W^{|Δdeg|} | down_j⟩. Minimal-power matrix:

| | d(1) | s(3) | b(5) |
|---|---|---|---|
| u(0) | J_W¹ | J_W³ | J_W⁵ |
| c(2) | J_W¹ | J_W¹ | J_W³ |
| t(4) | J_W³ | J_W¹ | J_W¹ |

**ANGULAR SKELETON = STRUCTURAL-DERIVED (zero up-mass input) — but only the CRUDE shape (honest split):**
- **Derived (angular):** (1) diagonal = J_W¹ = O(1) → why CKM diagonal ≈ 1; (2) mixing exists ONLY through J_W → why it's small AT ALL (direct overlap vanishes by parity, even⊥odd); (3) corners most-suppressed (1-3 = J_W⁵). These three are forced by parity-grading alone.
- **NOT from the angular skeleton (rides the radial → Identified):** the raw J_W-powers are too crude for the detailed pattern — they give V_us=J_W³ and V_cb=J_W³ (same power) though observed V_us≫V_cb (λ vs λ²), and V_us=J_W³ vs V_cd=J_W¹ (asymmetric) though the 1-2 block is symmetric to 0.1%. So the **Wolfenstein λ-grading, the 1-2/2-3 near-symmetry, and the exact values ALL ride the radial FK overlaps** — Elie's blind fire. The angular skeleton gives the *shape* (near-diagonal, parity-small); the radial gives the *numbers*. I do NOT over-claim the hierarchy from the powers.
- **1-3 corner = the discriminator (Cal §288):** V_ub=J_W⁵ vs V_td=J_W³, different powers → intrinsically asymmetric; a symmetric-by-construction ansatz FAILS there. Observed: 1-3 asymmetric by ~factor 2, 1-2 sym 0.1%, 2-3 ~2%. The fire must reproduce that from the radial tail.
- **Honest cost — RETRACTED (K1186, Casey's insight verified):** I charged the up-tower ORDERING as one extra input. **It is FREE.** T2515 (corpus, Tier I; "Grace unification"): the up-tower is y=exp(−geodesic distance to boundary), one shell = ln(N_max) → α per shell — top AT the boundary (saturated y_t=1), charm one shell in (y_c=α), up two shells in. So **higher shelf = closer to boundary = heavier** is a corpus-forced monotonicity → the up-ordering (u=0,c=2,t=4 by mass) is FORCED by boundary-distance, the SAME mechanism that makes the top anomalously heavy. The kludge and the ordering are one mechanism. So the down-tower is forced by FK-norm, the up-tower by the boundary ladder — BOTH forced, NO extra input. On the fire, the 7 params can go FULLY Derived (no residual input cost).
  - **REFINEMENT (K1189, Cal §291 — my "α per shell" was too clean):** the up-ORDERING stays free (monotonicity: closer to boundary = heavier), but the per-rung FACTOR is NOT a uniform α-per-shell — charm→top ≈ α (t/c=136≈α⁻¹ ✓) but up→charm ≈ **4.2×α⁻¹** (c/u=577, anomalously steeper). So each RUNG VALUE must be independently shown forced, not assumed-α. Ordering forced; per-rung values are the open piece the dial-free fire must show forced (not fitted).

**Tier split (K1184):** angular skeleton (shape) = Structural-Derived, no up-mass dependence — bankable as the *shape* of the mixing. The seven VALUES ride the radial → Identified until Elie's blind fire reproduces them (octant chosen first, 1-3 corner is the make-or-break).

## ★ THE ORDERED PRODUCT (K1187, task #77, Casey's non-commutativity insight) — the possible route to the VALUES
**EXACT linear-algebra fact:** mixing IS the non-commutativity — if [M_mass, J_W]=0 (shared basis), CKM=identity, nothing mixes. **Commit→emit ordering** (the item-10 record cycle): mass = commit (stored diagonal), J_W = emit (transition) → **CKM = U_up† · J_W · U_down** (mass-basis first, weak transition second). The order is the substrate cycle, not a choice — the flavor sector IS the commit cycle running in fermion space.

**The ordered product from FORCED operators:** down ladder (FK-norm {1,3,5}: 1:20:840), up ladder (boundary α-per-shell {0,2,4}: α²:α:1, T2515), J_W (one-degree step). All three forced.

**LEADING-TERM CHECK (real, but CALIBRATED K1189):** Cabibbo λ = √(m_d/m_s) = 1/√20 = 0.2236 vs obs 0.2243 (<1σ) — passed Cal's pre-registered razor (§291: "must give 1/√20, not just near 0.22"), four seats. BUT this λ IS the **Gatto relation (Gatto 1968, √(m_d/m_s))**, ALREADY BANKED in the corpus. ⟹ it **VALIDATES the ordered-product mechanism** but banks **NO new number.** What is genuinely BST: (a) forces the input ratio m_s/m_d=20 from geometry (not measured); (b) DERIVES the geometric-mean texture from the degree-1 cohomology operator = EXPLAINS why Gatto holds; (c) grounds the order in the commit cycle. **CLAIM EXACTLY "BST forces + explains Gatto", NOT "BST derives the Cabibbo"** (referee would pounce). Nothing new banked; confidence in the route went up.

**HONEST TIER:** SOLID/EXACT — mixing=non-commutativity + commit→emit order. SOLID — leading λ=1/√20 forced. **HYPOTHESIS (not a theorem):** that the full ordered product forces λ², λ³, and the factor-2 corner from (α-per-shell up-ladder)×(one-degree J_W) with no tuning. Ingredients all forced (down FK, up α T2515, J_W); the open question is whether their PRODUCT reproduces the tower or needs a hidden assembly coefficient (Cal guards). Elie's dial-free fire decides. If forced → values come from the SEQUENCE (strongest possible outcome, 7 params → Derived). If a coefficient is tuned → shape stays Structure-Derived, values Identified. I build the structure; I do NOT claim the tower until the product is computed.
