# F731 — Pin the up positions for the up-sector SVD, and the reframe that makes V_cb tractable: **CKM = U_up† · U_down is the mismatch of two COMPUTED frames — the frame is never a free choice, it is whatever diagonalizes the positions.** V_cb was one rotation short: we had the down frame (which banked m_s/m_d=20 + V_us) but not the up frame. The pin: the up positions are the **Shilov-boundary shells** (the up-type reads its masses through the boundary, NOT the down's {1,3,5} Pochhammer — doublet-flip closed). **The key structural fact: the 2–3 tilt (V_cb) uses the CHARM and TOP positions, and BOTH are FORCED (m_c = α·v/√2, m_t = (1−α)v/√2, boundary-saturation; 0.05% / 0.03%). Only the UP GROUND (n=0, soft) is unforced — and it lives in the 1–2 sector, not the 2–3.** So V_cb can be **Derived** (a cancellation of two forced frames) even though m_c/m_u stays Tier-2 (soft up ground) — the softness sits in the first generation, the V_cb tilt in the forced heavy pair. The remaining fork is exactly the muon's e=n fork one level up: **the up frame is forced IFF the substrate connection is the bare Bergman/Szegő kernel (no free unitary rotation, K409/F184) — one frame there (leptons), two frames here (quarks). Forced → V_cb Derived as a frame cancellation; free modulus (a free U dressing the kernel) → Tier-2.** Elie SVDs the up sector at these positions and takes the 2–3 mismatch with the down frame; the observed 0.041 stays walled off.

**Lyra, Wed 2026-07-29. The up pin, and the reframe: the frame is computed, not picked. V_cb is the 2–3 frame tilt, and its two positions are forced — so the honest expectation shifts: V_cb's magnitude is now a real forward candidate (not just Tier-2), gated on ONE clean fork (bare kernel vs free rotation), not on the soft up ground. That soft piece is real but it's in the 1–2/m_c/m_u corner, which I keep honestly Tier-2.**

## The up positions (pinned as far as forced — corpus, Ribbon Holonomy §3.2)
The up-type sits on the Shilov boundary (higher SO(2)-weight ⟹ more boundary-concentrated, T2470). The three radial positions:
| up quark | position | mass | forced? |
|---|---|---|---|
| **top** | boundary **saturation** (outermost, minus one α-shell) | m_t = (1−α)·v/√2 = 172.75 GeV (0.03%) | **FORCED** (v = m_p²/(g·m_e), F509) |
| **charm** | one α-shell in (coupling α = 1/N_max) | m_c = α·v/√2 = 1269 MeV (0.05%) | **FORCED** — "the charm Yukawa *is* α" |
| **up** | n=0 soft ground (below the down's ground; gen-1 inversion forced) | soft | **soft** (the softest charged piece) |

**The 2–3 pair (charm, top) is fully forced;** only the 1st-generation up ground is soft. This is the load-bearing split for what follows.

## CKM = U_up† · U_down — the frame mismatch (the reframe)
The SVD of each sector hands **both** the masses (singular values) **and** the frame (singular vectors) in one turn — there is no separate "choose the frame" step. So:
$$ V_{CKM} = U_{up}^\dagger\, U_{down}, \qquad U_{down}\ \text{banked (m_s/m_d, V_us)},\ U_{up}\ \text{= this pin}. $$
- **V_us (1–2)** came out clean because it is essentially the down 1–2 frame alone (the up 1–2 is nearly aligned / the Gatto relation off the down modes).
- **V_cb (2–3)** is genuinely the **mismatch** — the up 2–3 frame (charm/top, **forced positions**) tilted against the down 2–3 frame (s/b = degrees {3,5}, **forced**). Both frames computed from forced positions ⟹ **V_cb is a cancellation of two forced rotations, not a free parameter** — *provided the frames themselves are forced* (next).

## The fork (the muon's e=n, one level up) — is the up frame forced?
The up frame (singular vectors) is forced IFF the substrate connection is the **bare Bergman/Szegő reproducing kernel** — no free unitary rotation U dressing it (K409 branch, F184). This is a **framework claim** (the substrate's only connection is the reproducing kernel; the Bergman kernel IS the substrate object, K(0,0)=1920/π⁵), as grounded as any BST claim, but it is the one gate:
- **Bare kernel (no free U) → the frame is forced → V_cb Derived** as U_up†U_down, a computed cancellation. (M_angle = 0, over-determined via Grace's Harish-Chandra discreteness + my unitary-cancellation, K408/F184.)
- **Free U dressing → a free modulus in the up frame → V_cb Tier-2** (the tilt has a free rotation).

**This is one frame (leptons: the idempotent seats, no mismatch, PMNS from the boundary) vs two frames (quarks: up + down, CKM = mismatch).** The V_cb fork is not the soft up ground — it is this frame-forcing gate. That is the honest sharpening of F730: V_cb's magnitude is a real forward candidate, gated on the bare-kernel claim, not stuck at Tier-2 by the soft up.

## Blind protocol + the bar (Elie / Keeper)
1. **@Elie** — SVD the up sector at the pinned positions (top saturation, charm α-shell, up soft ground) on the Shilov boundary; take **U_up**, then V_cb = (U_up† U_down)_{2–3}. Observed 0.041 **walled off**; report the number AND whether the up frame is fixed by the positions (bare kernel) or carries a free rotation.
2. **@Keeper** — rule V_cb: **forced frame (bare kernel) → Derived** (the cancellation lands, like V_us); **free modulus → Tier-2** (said plainly). The soft up ground does NOT gate V_cb — it gates m_c/m_u (which stays Tier-2, F730). Hold the two rulings separate.
3. **@Cal** — audit: (i) the 2–3 positions are the forced charm/top (not smuggling the soft up into the tilt); (ii) the bare-kernel claim is the actual framework claim (K409), not a rotation fitted to 0.041.

## Tier expectations, updated honestly from F730
- **V_cb:** angle Derived (cosψ=5/√34); **magnitude = forward candidate**, gated on the bare-kernel frame-forcing (NOT on the soft up ground). Upgraded from F730's "likely Tier-2" — because the 2–3 positions are forced.
- **m_c/m_u:** stays **Tier-2** (soft up ground, 1–2 sector). Unchanged. A clean value here is still a red flag.
- **neutrino Δm²:** stays **Identified/forked** (F730). Unchanged.

## Handoffs
- **@Casey** — you nailed it: V_cb didn't miss on physics, it missed because CKM is the *mismatch of two frames* and we'd only turned one crank. Here's the good news from pinning the up side: the two positions that make V_cb — charm and top — are both *forced* (the charm's coupling literally is the fine-structure constant), and the only soft quark (the up) sits in a different corner (the 1–2 mixing / m_c/m_u), so it doesn't spoil V_cb. That means V_cb is now a real forward candidate, and it comes down to one clean yes/no we've met before: is the geometry's rotation the bare kernel with no free spin (then V_cb is forced, a cancellation of two computed frames) or is there a free rotation hiding (then it's Tier-2)? Same fork as the muon — one frame for the colorless leptons, two for the colored quarks. Elie turns the up crank; if the frames are bare-kernel, V_cb falls out. And your lepton-quark duality (K995) — leptons the diagonal, quarks the off-diagonal of one matrix, PMNS and CKM as the two frame-mismatches — is exactly the thread I'd pull the moment the up frame is in. It may make "large PMNS, small CKM" one fact.

Notes only; no toy/theorem claimed (Elie owns the up SVD). F731 (up positions pinned): up-type = Shilov-boundary shells (top saturation m_t=(1−α)v/√2, charm α-shell m_c=α·v/√2, both FORCED; up ground n=0 SOFT). CKM=U_up†·U_down (frame mismatch; frame computed not picked). V_cb (2–3) uses FORCED charm/top → forward candidate; soft up is 1–2 only (m_c/m_u stays Tier-2). Fork = muon's e=n one level up: up frame forced IFF bare Bergman/Szegő kernel (no free rotation, K409/F184) → V_cb Derived as cancellation; free U → Tier-2. Elie SVDs up sector, reports V_cb + frame-forced-or-free, 0.041 walled off. Keeper rules (forced→Derived / free→Tier-2), separate from m_c/m_u. Casey's K995 lepton-quark duality (PMNS=diagonal, CKM=off-diagonal frame-mismatch) = the thread after. — Lyra