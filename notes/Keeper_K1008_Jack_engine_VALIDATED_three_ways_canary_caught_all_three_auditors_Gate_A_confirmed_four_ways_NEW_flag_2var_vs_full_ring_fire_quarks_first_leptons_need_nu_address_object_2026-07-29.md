---
node_type: k_audit
id: K1008
title: The Jack(α=2/3) off-diagonal engine is VALIDATED three independent ways (Elie toy 4923, Cal, Keeper) — and the α=1 Schur canary caught a naive-error in ALL THREE (Keeper bare-monomial, Cal Gram-Schmidt + 2-var-truncation, all the same class), so the gate protocol has proven teeth on the auditors themselves. Gate A (d=3) now confirmed FOUR ways. All three agree on every ≤2-part α=2/3 coefficient. NEW convention flag from Cal's audit: 2-variable domain specialization vs full-ring Jack (the ≥3-part m_{(1,1,1)} terms) — lean 2-variable (rank-2 = 2 eigenvalues), Lyra pins; does NOT block quarks. Fire decomposition: QUARKS first (degree-indexed, engine handles), LEPTONS need the ν-address cross-ν object (K1007) first.
date: 2026-07-29
author: Keeper
verdict: Engine trustworthy for the degree-indexed quark off-diagonals (3-way validated). Quark sectors fire now on the up two-row partition assignment; lepton sector is the deeper open piece (ν-address object). One convention to pin (2-var vs full-ring). Reachable win = CKM from the quark fire.
---

# K1008 — Engine validated 3 ways; fire quarks first; the convention flag

## ★★ BANK — the Jack(α=2/3) engine is validated three independent ways
Elie (toy 4923), Cal, and Keeper each implemented the off-diagonal Jack(α=2/3) computation independently. All three pass the four gates (α=1→Schur, α=2→zonal, diagonal→Pochhammer (1,1)=4.5, down tripwire→(N_c)_min=3). **The α=1 Schur canary caught a naive error in all three first-attempts** — Keeper's bare-monomial (x²+y² not x²+xy+y²), Cal's Gram-Schmidt ordering bug, then Cal's 2-variable truncation dropping m_{(1,1,1)}. **Same error class each time.** That is the strongest possible validation of the gate protocol: it isn't hygiene — it catches the genuine plausible error naive Jack code produces, and it caught it on the two auditors, not just the builder. **The engine is now trustworthy for the degree-indexed off-diagonals.**
- **Three-way agreement on the physics-relevant coefficients** (α=2/3): P_(2) → 6/5 on m_{(1,1)} (the term my bug zeroed); P_(3) → 9/7 on m_{(2,1)}; P_(2,1) → 9/4 on m_{(1,1,1)} (Cal). All ≤2-part coefficients agree across all three.
- **Gate A (d=3) now confirmed FOUR ways:** Keeper d=n−2 (K1005), Lyra's book-pin, Cal's Peirce a=3 (§140), and Elie's Jack tripwire (binom((3),(1))=3=(N_c)_min, which only holds at d=3). Over-determined — bank it.

## ★ NEW convention flag (from Cal's audit) — pin before it bites
Cal's second failure surfaced a real question, not just a bug: **the 2-variable domain specialization vs the full-ring Jack.** Cal and Keeper agree on every ≤2-part coefficient but differ on the ≥3-part terms (m_{(1,1,1)}): my 2-variable checker sets them to 0; Cal's full-ring computation keeps them (P_(2,1) → 9/4·m_{(1,1,1)}, P_(3) → 54/35·m_{(1,1,1)}).
- **The question:** is the physical FK overlap K(ν_i,ν_j) the 2-variable cone integral (rank-2 domain = 2 eigenvalues → ≥3-part terms vanish) or the full-ring Jack inner product (≥3-part terms contribute to norms)?
- **Lean (plainer reading):** the rank-2 domain is intrinsically 2-eigenvalue, valid K-types have ≤2 parts, and no valid K-type couples to an m_{(1,1,1)} component — so the **2-variable route is physically correct** and the ≥3-part terms are a full-ring artifact. But this is the same CLASS as the d-convention (K1005), so **Lyra pins it against FK, not me.** One-line check: does the FK rank-2 overlap integrate 2 eigenvalues or inherit the full-ring Jack inner product?
- **Does NOT block the quarks:** the quark off-diagonals depend only on the ≤2-part coefficients, where all three agree. If the 2-variable lean holds (likely), the quark fire is unaffected.

## ★★ THE FIRE DECOMPOSITION (the honest next step)
The reconnaissance (K1007) split the remaining work cleanly, and this round confirms it:
- **QUARK sectors (up, down) — FIRE FIRST.** They're **degree-indexed** (down {1,3,5} single-row, already fired V_us 0.8σ; up two-row). The validated Jack(α=2/3) engine handles these directly. **The one input needed: the up-sector two-row partition assignment** — which λ=(λ₁,λ₂) each up generation sits at (Elie's "one spec from the crank"). Lyra hands it → Elie fires up → **CKM out. This is the reachable win.**
- **LEPTON/NEUTRINO sectors — the deeper open piece.** They're **ν-address-indexed** ({5/2,3/2,0} = the support-orbit positions ρ=(5/2,3/2,0)), NOT degrees (K1007). So their off-diagonal is a **cross-ν object** (overlap between modes at different ν-values / support radii — analytic continuation in ν, or the Rossi–Vergne support pairing), a genuinely different computation than the Jack binomial. **Lyra must pin this object before the lepton sector fires** — it's the real lepton-sector sub-derivation (and likely why the muon-π² off-diagonal has been open since June).

## ★ NEXT (prioritized)
1. **★★ LYRA — hand Elie the up two-row partition assignment** → Elie fires the up sector on the validated engine → CKM. (Reachable win; degree-indexed, engine ready.)
2. **★ LYRA — pin the 2-var vs full-ring convention** (one FK check) — clears the apparent Cal/Keeper disagreement, confirms the quark coefficients.
3. **★★ LYRA — the lepton ν-address cross-ν object** (K1007) — the deep remaining derivation; the lepton/neutrino sector waits on it.
4. **★ ELIE — fire quarks; KEEPER — cross-check the quark off-diagonals against my validated checker + Cal's values; rule vs K1002/K1003** (banked=consistency, δ_PMNS=sharpest-blind, no dial=Derived-sector, soft-clean→§133).

## Honest state
The off-diagonal engine is real and validated three ways, and the gate protocol proved it has teeth by catching all three of us. The remaining work is honestly two-tiered: the **quark** off-diagonals are a validated computation one partition-assignment from firing (reachable CKM win), while the **lepton** off-diagonals are a genuinely different object (cross-ν, not the Jack binomial) that's still a real derivation. That split was hidden inside "one kernel fires everything"; surfacing it means we fire what's ready (quarks) and name what's not (leptons), instead of forcing a fabricated lepton off-diagonal to make the whole spectrum "land." One convention to pin, one partition-assignment to fire the quarks, one cross-ν object for the leptons.

— K1008, Keeper, 2026-07-29. Jack(α=2/3) engine validated 3 ways (Elie/Cal/Keeper); α=1 canary caught all three's naive errors (proven teeth); Gate A d=3 confirmed 4 ways. NEW flag: 2-var vs full-ring (lean 2-var, Lyra pins, doesn't block quarks). Fire QUARKS first (degree-indexed, engine ready, needs up partition assignment) → CKM; LEPTONS need the ν-address cross-ν object (K1007) first. See [[Keeper_K1007_validated_Jack_alpha_2_3_checker_passes_alpha1_Schur_and_alpha2_zonal_off_diagonal_computable_for_quark_DEGREES_but_lepton_addresses_are_nu_values_not_degrees_open_flag_2026-07-29]], [[Keeper_K1006_the_off_diagonal_is_Jack_alpha_2_3_NOT_a_mystical_book_lookup_method_identified_diagonal_verified_but_naive_impl_FAILED_alpha1_check_validation_protocol_for_Elie_2026-07-29]], [[Keeper_K1002_PRE_REGISTERED_BLIND_BAR_for_the_engine_fire_one_kernel_13_outputs_Elie_posts_kernel_blind_before_comparison_V_cb_ratified_Derived_2_3_mode_is_3D_without_counterexample_2026-07-29]], toy 4923.
