# F649 — Gap (b) COMPUTED, and the hypercharge part CLOSES: **anomaly cancellation forces the SM hypercharge RATIOS uniquely (up to the trivial u↔d relabel), and 1/6-quantization fixes the overall scale.** Explicit solve: with the SM reps, the 3 linear anomaly conditions leave a 2-parameter family (n_Q, s); the cubic [U(1)³] condition forces **s² = 9n_Q² → s = ±3n_Q**, the SM up to u↔d. So the SM hypercharges are the UNIQUE anomaly-free ratios. The geometric **1/6 quantum (Z₆ center, N_c·rank — from the domain, NOT the fermions)** fixes the scale to n_Q=1 = the SM. **NOT circular** (Cal's gate): anomaly forces the *ratios* with no reference to 1/6; 1/6 fixes only the *scale* and comes from geometry, not from reading the SM content. Gap (b) hypercharge-part = DERIVED. **What remains (honest):** does anomaly-freedom force the REP assignment (the Wilson-line twist 𝒰_int) too, or only the hypercharges *given* the SM reps? That deeper uniqueness (scan over twists) is not yet done. So: the forcing is substantially advanced — the hypercharges are forced — with the twist-uniqueness the remaining piece.

**Lyra, Wed 2026-07-22 ~15:11. Pull 07-22P. Actually computed gap (b)'s core; it closes for the hypercharges. Discipline: this is standard SM anomaly algebra (solid), the BST claims (1/6-fixes-scale, non-circular) are clean, the twist-uniqueness is honestly open.**

## The anomaly conditions (one generation, left-handed Weyl, Y in units of 1/6 → integers n)
Fields and multiplicities: Q (color 3 × SU(2) 2 = 6), u^c (3), d^c (3), L (2), e^c (1). Hypercharges n_Q, n_u, n_d, n_L, n_e (integers, Y = n/6). The four gauge/grav anomaly conditions:
1. **[SU(3)]²U(1):** 2n_Q + n_u + n_d = 0. (color-charged, ×SU(2) mult)
2. **[SU(2)]²U(1):** 3n_Q + n_L = 0. (SU(2)-doublets, ×color mult)
3. **[grav]²U(1):** 6n_Q + 3n_u + 3n_d + 2n_L + n_e = 0. (linear, ×full mult)
4. **[U(1)]³:** 6n_Q³ + 3n_u³ + 3n_d³ + 2n_L³ + n_e³ = 0. (cubic)

## The solve — anomaly forces the SM ratios uniquely (up to u↔d)
**Linear (1,2,3):** from (2): n_L = −3n_Q. From (1): n_u + n_d = −2n_Q. Substitute into (3): 6n_Q + 3(−2n_Q) + 2(−3n_Q) + n_e = −6n_Q + n_e = 0 → **n_e = 6n_Q.** So the linear family is 2-parameter: (n_Q, s) with n_u = −n_Q + s, n_d = −n_Q − s (so n_u+n_d = −2n_Q, and s = (n_u−n_d)/2 free).
**Cubic (4):** n_u³ + n_d³ = (−n_Q+s)³ + (−n_Q−s)³ = −2n_Q³ − 6n_Q s². So
$$ 6n_Q³ + 3(−2n_Q³ − 6n_Q s²) + 2(−3n_Q)³ + (6n_Q)³ = (6 − 6 − 54 + 216)n_Q³ − 18n_Q s² = 162n_Q³ − 18n_Q s² = 0 $$
$$ \Rightarrow 18\,n_Q\,(9n_Q² − s²) = 0 \Rightarrow \boxed{\,s = \pm 3n_Q\,}. $$
Only two solutions: **s = ±3n_Q → (n_u, n_d) = (2n_Q, −4n_Q) or (−4n_Q, 2n_Q)** — the SM (u^c: −4, d^c: 2) and its **u↔d relabel** (physically identical). **So anomaly cancellation forces the SM hypercharge ratios uniquely, up to the trivial u↔d swap.** (This is the standard textbook fact, reproduced.)

## Verification: SM values (n_Q = 1)
(n_Q, n_u, n_d, n_L, n_e) = (1, −4, 2, −3, 6) → Y = (1/6, −2/3, 1/3, −1/2, 1) — exactly the SM (u^c, d^c, L, e^c hypercharges). All four conditions = 0 (checked: SU(3)² 2−4+2=0; SU(2)² 3−3=0; grav 6−12+6−6+6=0; U(1)³ 6−192+24−54+216=0). ✓

## 1/6-quantization fixes the scale — and it's NOT circular (Cal's gate)
The anomaly conditions are **homogeneous** → they fix the hypercharges only up to overall scale n_Q. **The geometric 1/6 quantum fixes n_Q = 1:** hypercharge comes in units of 1/6 = 1/(N_c·rank) from the **Z_{N_c}×Z_rank = Z₆ center** (F631/K806), with N_c=3 (color, root multiplicity) and rank=2 (isospin, domain rank) — both from the **geometry**, and Q realizes the minimal quantum (n_Q=1). **Non-circularity, explicitly:**
- Anomaly cancellation forces the RATIOS (s=±3n_Q) with **no reference to 1/6** — it's the fermion content's quantum consistency.
- 1/6 fixes only the SCALE, and it comes from the **gauge-group center geometry (N_c, rank)**, NOT from reading the SM fermion hypercharges.
- Two independent conditions (fermion-consistency + group-center) → **not circular.** (Cal: this is the load-bearing non-circularity claim — the 1/6 is a property of the *group* [G]/Z₆ derived from N_c & rank, independent of the anomaly argument.)

## Gap (b) status
- **Hypercharges GIVEN the SM reps: DERIVED.** Anomaly forces the ratios (unique up to u↔d); 1/6 fixes the scale; non-circular. This is the core of gap (b) and it CLOSES. **This alone firms the charge-row: the exact charge values {+2/3,−1/3,−1,0} that Grace held derived-conditional (T2521) now follow from anomaly-freedom + the geometric 1/6 — the N_c-weighted neutrality is the [SU(3)]²U(1) + [grav]²U(1) conditions, geometric via inflow.** One leg (K806 charge-row) effectively closes.
- **The REP assignment (the Wilson-line twist 𝒰_int): NOT yet forced.** I derived the hypercharges *given* the SM reps (Q=triplet-doublet, etc.). Whether anomaly-freedom also forces the *rep structure* (only the SM twist is anomaly-free among quantized options) is the deeper part — a scan over 𝒰_int twists, not done. So the full "anomaly-freedom → SM" (including which fields are doublets) is advanced but not complete.

## Honest tier
- **Gap (b) hypercharge-uniqueness: DERIVED** (standard anomaly algebra, reproduced explicitly; s=±3n_Q). Solid.
- **1/6-fixes-scale + non-circular: CLEAN** (geometric center, independent of anomaly). Cal to gate.
- **Charge-row leg (K806): effectively CLOSED** — the neutrality Grace imposed is now anomaly-freedom + geometric 1/6. Real two-for-one down-payment.
- **Rep-assignment (twist) uniqueness: OPEN** — the remaining piece of the forcing. Held.
- **Parity: still derived-conditional** — gap (b) closes the hypercharge/charge-row part, but parity also needs the Pin mod-2 index (gap a) and the twist-uniqueness. Substantially advanced, not closed. 8th candidate area — held.

## Tiers / handoffs
- **@Cal — the circularity gate, please rule:** anomaly forces the hypercharge RATIOS (s=±3n_Q) with no 1/6 input; 1/6 fixes only the scale and is derived from the group center Z_{N_c}×Z_rank (N_c, rank geometric), independent of the fermion hypercharges. Is that genuinely non-circular, or is the Z₆ center itself smuggling the fermion content? (My read: the center is a property of [SU(3)×SU(2)×U(1)]/Z₆ fixed by N_c=3 & rank=2 from the domain, not by the SM charges — non-circular. But you gate it.)
- **@Elie** — verify the solve (s=±3n_Q from the cubic; SM = n_Q=1) and then the OPEN piece: **the twist scan** — enumerate the discrete Wilson-line 𝒰_int rep-assignments (which fields doublet/singlet/triplet) with quantized hypercharges, and check whether ONLY the SM assignment is anomaly-free. If yes → anomaly-freedom forces the full SM (reps + hypercharges). Your harness. This is the remaining gap-(b) core.
- **@Keeper** — gap (b) COMPUTED and the hypercharge part CLOSES: anomaly forces the SM ratios (s=±3n_Q, up to u↔d), 1/6 fixes the scale (geometric, non-circular). **The charge-row K806 leg effectively closes** (the neutrality Grace imposed = anomaly + geometric 1/6). Parity still derived-conditional (needs the Pin index + twist-uniqueness). Please log: gap-(b) hypercharges DERIVED; charge-row closed; twist-uniqueness + Pin-index open; Cal gating circularity.
- **@Grace** — your charge-row leg: the N_c-weighted neutrality you had to impose (T2521) is now the [SU(3)]²U(1) + [grav]²U(1) anomaly conditions, made geometric by Callan-Harvey inflow, with 1/6 from the center. **The exact charges {+2/3,−1/3,−1,0} firm from derived-conditional toward derived.** Render: anomaly forces SM hypercharges (ratios) + geometric 1/6 (scale) → charge-row closes; parity needs the further twist + index pieces.
- **@Casey** — pushed, and gap (b)'s core actually computed clean: anomaly cancellation, by itself, forces the Standard Model hypercharges — the ratios are the *unique* solution (I solved it: the cubic condition gives s = ±3n_Q, which is the SM up to swapping up and down, a non-difference). The one thing bare anomaly-cancellation leaves free is the overall scale, and *that's* exactly what your geometric 1/6 fixes — and the 1/6 comes from the group's center (N_c colors × rank-2 isospin), from the domain, not from the fermion charges, so it's not circular (Cal's checking that hardest). So the hypercharge half of the forcing is done, and it pays off immediately: the charge-neutrality Grace had to *impose* when she banked the 1/N_c fractionalization now *follows* — anomaly-freedom made geometric. That's the two-for-one you were hoping for, at least on the charge-row leg. What's left for full parity is the harder half — whether anomaly-freedom also forces which fields are doublets vs singlets (the twist), plus the Pin index giving one clean generation. So it's real progress on facts, not a reach: one leg closed, the hardest one located.

Notes only; no toys/theorems claimed. Gap (b) hypercharge-part DERIVED (anomaly forces SM ratios, s=±3n_Q; 1/6 fixes scale, non-circular); charge-row K806 leg effectively closed; twist-uniqueness + Pin-index OPEN; parity derived-conditional, substantially advanced. — Lyra
