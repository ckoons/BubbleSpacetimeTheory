---
node_type: k_audit
id: K1012
title: THE UP-FRAME TARGET SPEC + the unifying idea — the up-quark frame U_up and the lepton off-diagonal are the SAME open object: the CROSS-ADDRESS two-point overlap kernel on D_IV⁵ (modes at DIFFERENT radial/ν positions). The down-quark Jack(α=2/3) binomial is the SAME-ν special case (cross-degree), already validated — so it is the built-in consistency check. This is Casey's "deeper relationship" between quarks and leptons made concrete: mass = radial boundary-distance in every sector; only the DOWN happens to sit at integer degrees. Resume approach, honestly tiered (insight/target, not banked). Do NOT re-run the fixed-ν weighted-norm (K1011 forced null); the cross-address kernel is a different object.
date: 2026-07-30
author: Keeper
verdict: The two open pieces (up frame, lepton off-diagonal) are ONE object — the cross-address two-point kernel — with a built-in check (reduce to the validated Jack binomial on the same-ν slice). Approach specified; this is the defined computation to resume, not an open question.
---

# K1012 — The up frame, and why it's the same object as the leptons

Casey asked: write up the up-frame boundary derivation as a *defined* computation. Doing that precisely reveals the payoff — the up frame and the lepton off-diagonal are the same open object, and the down-Jack is its already-validated special case.

## ★ The organizing idea: mass = radial boundary-distance (every sector)
Across all four sectors, a fermion's mass is set by **how far its mode sits from the Shilov boundary** of D_IV⁵ (Casey's "higher generations are farther to the edge"):
- **Down quarks:** the three modes sit at **integer degrees {1,3,5}** (single-row K-types at the *same* Bergman weight ν=5). Same-ν, different degree.
- **Up quarks:** the three modes sit at **boundary-distances (Yukawas) {y_t=1, y_c=α, y_u=soft}** — top ON the boundary, charm one α-shell in, up deep interior. Different radial position.
- **Charged leptons:** the three modes sit at **ν-addresses {5/2, 3/2, 0}** (interior / edge / boundary). Different radial position.
- **Neutrinos:** rank-2 Majorana, m₁=0, separate condensate.

**The unifying observation:** UP and LEPTONS are both indexed by *radial/ν position* (cross-ν); DOWN is indexed by *degree at fixed ν* (cross-degree). So the DOWN's Jack(α=2/3) binomial is the **same-ν special case** of a more general object — the **cross-address (different-ν) two-point overlap kernel.** That kernel is the single missing input for BOTH the up frame and the lepton off-diagonal.

## ★★ THE UP-FRAME TARGET SPEC (the defined computation)
The up-sector overlap matrix Y_up[i,j] = ⟨u_i | Φ_up | u_j⟩ on the three up modes at radii {1, α, soft}. What U_up (its left singular vectors) SHOULD be:
1. **The masses are DONE** (the diagonal / boundary reading): y_t=1 (top saturates the boundary, m_t=v/√2), y_c=α (m_c=α·v/√2), y_u soft (Tier-2). These are the singular values.
2. **The 23-block (charm–top) is DONE and ≈ 0:** the up 23-mode refracts *past* the boundary (radius √(2/3)·N_c/rank=1.225>1) → **vanishes** (K711/K1001). So **the top decouples** — U_up is nearly a 2×2 (up–charm) block ⊕ a top singlet. This is why V_cb is down-only.
3. **The ONE open piece = the 12-block (up–charm mixing):** set by the **soft up ground-state mode's overlap with the α-shell charm mode** — i.e. an overlap between two modes at *different* boundary-distances. **This is a cross-address overlap**, not a same-ν degree hand-off (F738 proved "up = down + one box" gives charm/up=20, wrong — so it is NOT the Jack hand-off).
4. **Consequence for CKM:** since U_up ≈ (up–charm 2×2) ⊕ (top singlet) with a small 12-block, **CKM = U_up†·U_down** is dominated by the (already-derived) down frame, with a small up 12-correction — consistent with V_us=1/√20 landing at 0.8σ from the down alone. V_ub then lives in the up 12/13 × down structure.

## ★★ THE APPROACH — build the cross-address two-point kernel (one object, three payoffs)
Define the general overlap **K( (ν_i, m_i), (ν_j, m_j) )** = ⟨ mode at (ν_i,m_i) | Φ | mode at (ν_j,m_j) ⟩ on D_IV⁵, a genuine **two-point** kernel (a function of two addresses), NOT a fixed-ν weighted norm.
- **Built-in CONSISTENCY CHECK (this is what makes it a defined computation):** restricted to the **same-ν slice** (ν_i=ν_j), K must reduce to the **validated Jack(α=2/3) binomial** — the down engine (toy 4923, checked 3 ways). If a candidate two-point kernel fails the down slice, it's wrong before it reaches up/leptons. Same discipline as the α=1 Schur canary, one level up.
- **Payoff 1 — the up 12-block:** K at (charm α-shell) × (up soft) → U_up's open block → completes the quark matrix → CKM fires (with V_cb already banked).
- **Payoff 2 — the lepton off-diagonal:** K at the ν-addresses {5/2,3/2,0} × {5/2,3/2,0} → the colorless-frame off-diagonal → PMNS.
- **Payoff 3 — the "deeper relationship" (Casey):** quarks and leptons "mimic each other" because they are the same two-point kernel evaluated at different address-sets; the down is the degenerate same-ν corner where it simplifies to a binomial.

## ★ SHARPENING — it's the OFF-DIAGONAL matrix element (a different element than the null)
The cleanest insulation from yesterday: the two-point cross-address kernel is the **OFF-DIAGONAL** entry ⟨mode_i | Φ | mode_j⟩ with **i ≠ j** (the inter-generation overlap = the mixing content). Yesterday's K1011 forced null was a **DIAGONAL** object — a same-mode self-overlap norm-ratio (a mass-localization *depth*), where Γ_Ω cancels. **Different matrix element, different object**, even though both live on the same lepton modes:
- **Diagonal ⟨i|Φ|i⟩ = mass-depth** — for leptons this is the banked route that yesterday's fixed-ν norm tried (and failed) to re-derive; but the lepton masses are already banked anyway (6π⁵, (24/π²)⁶ via e=n, 49·71), so nothing hangs on it.
- **Off-diagonal ⟨i|Φ|j⟩ = the mixing** — this is the resume object, and it is NOT the norm-ratio that nulled. The two modes are at *different* addresses, so the two Γ_Ω factors differ and do not cancel.
- **Caveat (honest):** once you SVD the full 3×3, the off-diagonal entries feed the singular *values* (masses) too, not only the singular *vectors* (mixing). So the kernel is not "mixing-only." But the masses have independent banked derivations; the kernel's job here is the **frame/mixing** (U_up 12-block → CKM, lepton U → PMNS), and it need not re-derive the masses to succeed. Judge the kernel on the mixings + the down-slice check, not on reproducing (24/π²)⁶.

## ★ CRITICAL GUARDRAIL (do not repeat yesterday)
- **This is NOT the K1011 null.** Yesterday's forced null was the *fixed-ν weighted-norm* reading of the lepton MASS (a same-structure mode-ratio → Γ_Ω cancels → π-less). The **cross-address two-point kernel is a different object** (modes at *different* ν; the Γ_Ω's do NOT cancel because the two addresses differ). The K1011 resume point named exactly this: "the genuine cross-term construction, a two-point kernel, NOT a single-ν weighted norm."
- **Do NOT re-surface the retracted forms:** c₅/c₃ = Γ(5)/π² (F669, lives in the null fixed-ν world), θ₂₃ = π/4 (corpus holds 4/7).
- **Tier:** this note is APPROACH/INSIGHT (a defined target with a consistency check), **not banked.** The unification is a hypothesis until the two-point kernel is exhibited and passes the down-slice check.

## ★ NEXT (what the team needs)
1. **★ LYRA — write the two-point kernel K((ν_i,m_i),(ν_j,m_j)) explicitly** (the FK/Bergman two-point reproducing structure on D_IV⁵), and verify it reduces to the Jack(α=2/3) binomial on the same-ν slice (the down check). This is the one object; the up frame and lepton off-diagonal both read off it.
2. **★ ELIE — the moment the kernel form lands, run the down-slice consistency check** (must reproduce {3,60,2520}, V_us=1/√20), THEN evaluate the up 12-block (charm α-shell × up soft) and the lepton {5/2,3/2,0} off-diagonal. Numerical/MC allowed. Post blind.
3. **★ CAL — audit the two-point kernel target-innocent + the down-slice reduction** (is it the exhibited FK two-point object, or fit to reproduce known mixings?).
4. **★ KEEPER — rule the down-slice check first (consistency), then the up 12-block and lepton off-diagonal against the bar (K1002/K1003).** Reject any re-run of the fixed-ν weighted norm.
5. **★ GRACE — ledger: up masses Derived (m_t=v/√2, m_c=α·v/√2), V_cb Derived-value; the up frame + lepton off-diagonal = the one open two-point kernel.**

## Honest state
The up-quark boundary work is mostly done — the masses (y_t=1, y_c=α) and V_cb are banked; what's open is the up *frame*, specifically its 12-block, which is a cross-address overlap. Writing that precisely shows it's the *same* object the leptons need. So "complete the process" is now one defined computation — the cross-address two-point kernel on D_IV⁵ — with a built-in check (reduce to the validated down-Jack). That's the resume target, tiered as approach until exhibited. The down engine already works; the general kernel it's a special case of is the last real piece.

— K1012, Keeper, 2026-07-30. Up frame: masses+V_cb done, the open piece is the 12-block (up–charm), a cross-address overlap. UNIFYING IDEA: up frame + lepton off-diagonal = ONE object, the cross-address two-point kernel K((ν_i,m_i),(ν_j,m_j)) on D_IV⁵; down-Jack is the same-ν special case = the consistency check. NOT the K1011 fixed-ν null (different object). Approach/insight tier. See [[Keeper_K1011_RULING_F323_null_is_STRUCTURALLY_FORCED_c_function_route_CLOSED_muon_stands_on_e_n_unified_lepton_engine_PARKED_fermion_sector_BANKED_resume_point_documented_2026-07-29]], [[Keeper_K1008_Jack_engine_VALIDATED_three_ways_canary_caught_all_three_auditors_Gate_A_confirmed_four_ways_NEW_flag_2var_vs_full_ring_fire_quarks_first_leptons_need_nu_address_object_2026-07-29]], K995, K997, K1001, F728, F738.
