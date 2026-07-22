# F633 — Geometry debts Q_a + Q1 (workstream A, pull 07-22c). **Both payable, and Q_a sharpens.** Q_a (parity): the two branchings are rigorous — n_C=5 ODD ⟹ SO(5) spinor **4 irreducible**; SO(5)→SO(4): **4 → (2,1)⊕(1,2)** (L/R Weyl halves). But SO(4)=SU(2)_L×SU(2)_R is L↔R *symmetric* (the swap IS parity) — so n_C-odd gives the SPLIT but does NOT pick which half is gauged. **What breaks the tie is the SO(2) complex structure ω** (the defining Hermitian structure of D_IV⁵): a complex manifold is canonically oriented, orientation selects the **self-dual** SU(2) factor, and that = SU(2)_L. So parity violation ⟸ **n_C odd (irreducible split) AND D_IV⁵ Hermitian (ω picks the chirality)** — both defining features. The remaining conditional is now SPECIFIC: "SU(2)_R not gauged" = "the weak gauge fields are the self-dual/holomorphic 2-form connections." Q1 (partition): **O = SO(5) vector 5 → (2,2)⊕(1,1)**; the **(2,2) IS an SU(2)_L doublet = the custodial Higgs bi-doublet**; condensing it breaks SU(2)_L×U(1)→U(1)_em with a neutral VEV → the (Q-conserved / isospin-violated) partition is geometric. Five-Absence intact (all inside SO(5)→SO(4); no GUT; SU(2)_R stays a GLOBAL custodial symmetry = an SM feature, not new physics).

**Lyra, Wed 2026-07-22 ~08:42. Workstream A. Frame (Casey): geometric REASONS for the SM, not deviations. Tiers honest.**

## Q_a — the parity derivation (load-bearing)

### The two branchings (rigorous — DERIVED)
SO(5) irreps by highest weight (l₁,l₂); SO(4)=SU(2)_L×SU(2)_R irreps by (dim_L, dim_R).
- **n_C=5 ODD ⟹ one irreducible spinor**, dim 2^((5−1)/2) = 4. (Odd SO(2k+1): single spinor 2^k. Even SO(2k): splits into two Weyl halves.) The **SO(5) spinor 4 is irreducible** — this is the n_C-odd fact.
- **SO(5) → SO(4): spinor 4 → (2,1) ⊕ (1,2).** The irreducible SO(5) spinor becomes reducible under the *even* SO(4), splitting into a left Weyl (2,1) and a right Weyl (1,2). **This is the geometric origin of chirality**: L = (2,1), R = (1,2).
- (For Q1: **vector 5 → (2,2) ⊕ (1,1)** — used below.)
Both branchings are standard and exact. **The chiral L/R split is DERIVED from n_C=5 odd.** ✓

### The gap K809 left open, and what actually closes it
K809 said "SU(2)_L gauges the doublet, sees the other as a singlet." But **SO(4) = SU(2)_L × SU(2)_R is symmetric under L↔R** — the outer automorphism swapping the factors IS the parity operation. So the branching alone gives a split into two halves **without a canonical way to say which is "L" (gauged) and which is "R" (singlet).** n_C-odd produces the split; it does not orient it. Something must break the L↔R tie.

### ★ What breaks the tie: the SO(2) complex structure ω (NEW — this is the real content)
D_IV⁵ is a **Hermitian** bounded symmetric domain: K = SO(5) × **SO(2)**, and that SO(2) = U(1) is the complex structure J (the "read-direction" ω). Two consequences:
1. **A complex manifold is canonically oriented.** The orientation is not a choice — it comes from J (volume form ∝ (i∂∂̄...)^n). So D_IV⁵ carries a *fixed* orientation.
2. **Orientation selects self-dual vs anti-self-dual.** The SO(4) adjoint (2-forms) splits Λ² = Λ²₊ ⊕ Λ²₋ = **(3,1) ⊕ (1,3)** = self-dual ⊕ anti-self-dual = adjoint of SU(2)_L ⊕ adjoint of SU(2)_R. **Self-duality requires an orientation; flipping orientation swaps (3,1)↔(1,3) = swaps SU(2)_L↔SU(2)_R = parity.** The complex structure ω fixes the orientation, hence **canonically selects one factor** — the self-dual/holomorphic one — as SU(2)_L.

**So the parity mechanism is: n_C odd → the spinor splits into exactly two Weyl halves (no leftover); ω (D_IV⁵ Hermitian) → orientation → selects the self-dual half as the gauged SU(2)_L.** Both ingredients are *defining features* of D_IV⁵ (odd n_C; Hermitian/tube-type). Neither is input. This is a cleaner statement than K809: **n_C odd alone is necessary but not sufficient — ω is what orients the chirality.**

### Why MAXIMAL (V−A, not V−(1−ε)A)
The split 4 → (2,1)⊕(1,2) is exact and irreducible: left-handed fermions are **100%** (2,1) (pure SU(2)_L doublet, SU(2)_R singlet); right-handed are **100%** (1,2). Gauging only SU(2)_L couples to (2,1) fully and (1,2) not at all — an all-or-nothing gauge projector on an exact split. **No intermediate is geometrically available** ⟹ parity violation is maximal. ✓ (matches K809's "irreducible-split + gauge projector = maximal.")

### The remaining conditional — now SPECIFIC and checkable
"SU(2)_R not gauged" ⟺ **the weak gauge fields are the self-dual / holomorphic 2-form connections (the (3,1)), and the anti-self-dual (1,3) do not give a holomorphic gauge field.** On a Kähler manifold the holomorphic isometry currents are the natural gauge symmetries; the anti-self-dual factor acts anti-holomorphically. This is BST-plausible (boundary-CFT holomorphic currents = gauge symmetries) but is the ONE thing to nail. **Verdict: parity + L-doublet/R-singlet + maximal is DERIVED-CONDITIONAL, conditional now on the concrete statement "weak gauge fields = self-dual/holomorphic connections" — a sharper, checkable condition than K809's open embedding.** Next: verify BST's gauge-origin is the holomorphic-current one.

## Q1 — the message/syndrome partition (condensate quantum numbers)

We banked **O = SO(5) vector (1,0), dim 5.** Under the electroweak embedding SO(5)→SO(4):
$$ \mathbf{5} \;\to\; (\mathbf{2},\mathbf{2}) \;\oplus\; (\mathbf{1},\mathbf{1}). $$
(The SO(4) vector 4 = (2,2) under SU(2)_L×SU(2)_R; the extra 5th component = (1,1) singlet = the SO(5)/SO(4) reduction axis itself.)

- **(b) O contains an SU(2)_L doublet — YES.** The **(2,2)** is a doublet under SU(2)_L (and under SU(2)_R). This is precisely the **SM Higgs as a custodial bi-doublet**: 4 real fields = one complex SU(2)_L doublet, with SU(2)_R = the custodial symmetry. So the condensate's doublet part = the Higgs.
- **(a) The condensing VEV is electrically neutral — YES, structurally.** Condensing the (2,2) breaks **SU(2)_L × U(1) → U(1)_em**; the VEV sits in the U(1)_em-preserving (neutral, Q=T₃_L+Y=0) component. A doublet VEV (not singlet, not triplet) gives exactly the SM breaking pattern SU(2)×U(1)→U(1). U(1)_em unbroken = **Q conserved**; SU(2)_L broken = **isospin violable**.
- **The partition is therefore geometric:** conserved charge (U(1)_em) = the *message* the corrector may not touch; violated isospin (SU(2)_L) = the *syndrome* the weak force targets. **The Q-conserved / isospin-violated core of the weak selection rules follows from O = the (2,2) neutral doublet.** ✓
- **Conditional:** which piece condenses — (2,2) vs (1,1)? The **(1,1) is the SO(5)/SO(4) reduction axis** (the direction "used up" defining the 5→4 step), so the dynamical condensate is the **(2,2)** = the Higgs. This is the honest conditional on Q1 (that the (2,2), not the (1,1), carries the VEV) — plausible (the (1,1) is the reduction direction, not a fluctuation) but should be verified from the boundary dynamics.

## Bonus (consistency, not a claim): custodial SU(2) predicted, ungauged
The ungauged SU(2)_R is exactly the SM's **custodial symmetry** (protects ρ = m_W²/(m_Z² cos²θ_W) ≈ 1). The geometry predicting a *global* (ungauged) SU(2)_R = the (2,2) Higgs's custodial structure is a nice consistency: the SM's approximate custodial symmetry is the anti-self-dual SO(4) factor that ω did not select for gauging. No W_R, no new gauge bosons — **Five-Absence intact.**

## Five-Absence check
All of this lives inside **SO(5) → SO(4) = SU(2)_L × SU(2)_R** — no GUT group (no SO(10)/SU(5)/E₆), no unification. SU(2)_R is **not gauged** (global custodial only) ⟹ no W_R, no proton decay, no new physics. **Five-Absence intact. ✓** This is the SM reframed, not extended (Casey's frame).

## Tiers / handoffs
- **Q_a: DERIVED that the geometry splits the spinor (n_C odd → 4→(2,1)⊕(1,2)) AND selects one SU(2) (ω orientation → self-dual = SU(2)_L). DERIVED-CONDITIONAL for "SU(2)_R not gauged," now on the SPECIFIC condition "weak gauge fields = self-dual/holomorphic connections."** Maximal = exact split + gauge projector. **Sharpens K809.**
- **Q1: DERIVED that O = 5 → (2,2)⊕(1,1), the (2,2) is the custodial SU(2)_L Higgs doublet, condensing → U(1)_em neutral VEV → the Q-conserved/isospin-violated partition. Conditional on the (2,2) (not (1,1)) condensing.**
- **@Keeper** — Q_a closes to a sharper conditional: parity/maximal/L-doublet is derived from **n_C odd + D_IV⁵ Hermitian (ω)**; the one open link is "weak gauge fields = self-dual/holomorphic currents" (SU(2)_R = anti-self-dual, ungauged = custodial). Please log the refinement to K809: n_C-odd gives the split, **ω orients the chirality** (K809 under-specified this). Q1: partition is geometric (O=(2,2) neutral doublet). Five-Absence intact (SU(2)_R global custodial, no W_R).
- **@Elie** — verify branchings target-innocent: SO(5) spinor **4 → (2,1)⊕(1,2)** and vector **5 → (2,2)⊕(1,1)** (standard SO(5)⊃SO(4) tables); and check Λ²(SO(4)) = (3,1)⊕(1,3) self-dual/anti-self-dual = SU(2)_L/SU(2)_R adjoints. If any branching differs, the parity mechanism moves — this is the load-bearing arithmetic.
- **@Grace** — render: n_C odd → spinor split (chirality); ω (complex structure) → self-dual selection (which chirality gauged); O = (2,2) custodial Higgs doublet; SU(2)_R = ungauged custodial. Tier: derived-conditional reasons-for-SM, NOT new physics.
- **@CP team (B)** — cross-link: your "CP = continuous shadow, parity = discrete shadow of the read-direction ω" — note the ω here (SO(2) complex structure) is the SAME object doing the orienting. Parity's discreteness = the Z₂ orientation flip (self-dual↔anti-self-dual); CP's continuity = the U(1)=SO(2) phase on that same ω. **The read-direction that orients the chirality (Q_a) and the phase that stays free (CP) are one SO(2).** That's the unification anchor.

Notes only; no toys/theorems claimed. Reasons-for-SM, derived-conditional, Five-Absence intact. — Lyra
