# K1791 — ROUND 51: two proved ceilings, a forced redirect, and a w(a) recalibration

**Filed:** 2026-08-22
**Reports ruled:** Grace (partial-isometry gate — all three fork branches closed), Elie (5444/5445 — gate reproduced, no magnitudes; w(a) decline), Lyra (CHSH closed as a prediction, QM package finished; H_{ν_W} atlas offer), Cal (§691 — credit + route-inventory guard + w(a) C6/C7).
**Headline: the weak-current route to CKM is DEAD — proved, not stalled. The redirect needs no new machinery: it is the banked spine T2530/T2519/T2547. And the team's w(a) framing was a stale over-pessimistic snapshot — the fuller corpus says the no-crossing shape SURVIVES both direct probes.**

---

## 1. ★★★ The partial-isometry gate FIRED — "CKM = ⟨up|J|down⟩" cannot give a unitary CKM. (Grace, Elie)

Grace closed all three branches of her own fork, and did it the honest way — correcting her Round-50 number DOWN (the intrinsic, up-space-independent obstruction is **2.70 at ν_W=3**, not the ~21 she first reported; the earlier figure was for one particular up 3-space, ~8× overstated). The corrected result is **strictly stronger**: fatal with NO up-sector assumption.

- **Level 1 (assumption-free):** s₁/s₃ = 2.697 at ν_W=3, floor 2.342 across ν∈[10⁻³,10⁶], never 1.000. Mechanism in one line: ‖Jf₁‖=0.913, ‖Jf₃‖=1.126, ‖Jf₅‖=1.210 — **a ladder (degree-shifting) operator has k-dependent coefficients; a partial isometry cannot.**
- **Level 2:** the current's polar part IS an isometry, reducing to one parameter-free question — does it land on the independently-specified up 3-space? Principal angles 11.0°/42.9°/83.9°; defect 0.745 against the 10⁻³ CKM unitarity holds to; plateaus at 0.41. No ν rescues it.
- **Level 3:** define U = image → unitary by construction, predicts nothing.

Elie ran gate-first and confirmed (5444/5445, 7/7): reproduced the gate, stable to ~7 sig figs, swept ν_W to 3000 (floor never approaches 1), **computed no V_cb and no V_ub** — the protocol was gate-first and it didn't clear. He correctly refused the SVD-unitarization "patch" (a falsification patch dressed as a convention).

**RECONCILIATION ITEM (non-blocking, verdict robust either way):** Elie reproduced ≈20.99 (Grace's *original*, up-space-dependent number) not the *intrinsic* 2.70. Both are >1 → fatal → verdict unchanged. But the RECORD should carry the intrinsic figure; **re-point Elie's independent check at `play/gate_partial_isometry_intrinsic.py` so the two confirmations agree on the same object (~2.70, floor 2.342).**

**Cal's "can it fail?" (the fourth can't-fail watch) — CLEARED.** The isometry gate demonstrably discriminates: it ACCEPTS the flavor-universal current (identity on generation space = an isometry) and REJECTS the degree-shifting weak current. Accept-some + reject-some = a real gate, not a can't-fail. It just rejected the flagship ansatz — the opposite of unfalsifiable.

## 2. ★★★ The redirect is FORCED and already BANKED — route C = T2530, no new machinery. (Grace's constructive half, corpus-confirmed)

Grace's constructive half is the important result: **flavor-universality IS the partial-isometry condition.** The SM gets CKM unitarity for free because V = U_up†·U_down compares two bases of ONE generation space with a flavor-universal current (the identity on generation space, forced by gauge invariance). A degree-shifting operator breaks universality — which is *precisely why* it can't produce a unitary CKM. So routes A and B aren't "two random tries": they are eliminated by a **principle** (any non-flavor-universal current fails unitarity), and route C is the **unique survivor of an exhaustive dichotomy** (a current either commutes with the generation grading or it doesn't).

Corpus reconnect confirms route C is the SPINE, banked since 2026-07-29:
- **T2530 (Tier D):** CKM = U_up†·U_down; **V_us = 1/√20 = 0.31% DERIVED**, frame-INDEPENDENT (Cabibbo is down-only). V_cb/V_ub are the up-down **frame-mismatch** observables, "Tier-2 until the up-sector frame is pinned (**K995**)." The open item was named a month ago.
- **T2519 (Tier D):** rank-1 mass matrices → J=0 at leading order; **mixing/CP lives in the off-rank-1 breaking.** This IS Grace's "the magnitudes are the size of the rank-1 breaking."
- **T2547 (Structural):** the up-sector frame is already characterized — **up = top-saturation ladder {y_t=1, y_c=α, y_u=α²} (boundary mechanism); down = FK-bulk {1,3,5} (bulk mechanism).** The mixing = the misalignment of these two DIFFERENT mechanisms.

**RULING on T2530-vs-K1181 (Grace flagged):** the proved ceiling IS the resolution. K1181's "mixing rides the weak-current matrix element ⟨up|J|down⟩" is **superseded** by the proved dichotomy → **multiplier 0** on that framing; the live route is T2530 (U_up†U_down frame-mismatch). No grooming pass — the ceiling is a NEW result, so this supersede is stated forward here and folds into the Rubric coverage map at tonight's curation. K1181's *surviving* content (the bare cross-parity overlap vanishes → a current is mandatory) is exactly WHY the mechanism must be flavor-universal, so it feeds route C rather than dying entirely.

## 3. ★★ Cal's route-inventory guard — ADOPTED, and it turns into a strength. (Cal §691)

Cal is right that each route is target-innocent individually but the SEQUENCE isn't (route B was tried because A fell short → the target could be choosing the route). The guard: **declare the inventory before route C computes magnitudes.** Done, here:
- **Route A** — radial overlap on strata (K1635): REFUTED, 10.2% miss vs 0.49% bar.
- **Route B** — one-insertion weak current ⟨up|J|down⟩ (K1181/T2544): REFUTED this round, non-isometric.
- **Route C** — U_up†U_down frame-mismatch (T2530/K995/T2519/T2547): the survivor.

**But route C is NOT "#3 of N we try until one works" — it is the unique survivor of an exhaustive principled dichotomy (flavor-universal vs degree-shifting), and it was the banked route before A and B were attempted.** So the look-elsewhere penalty (~log N) does NOT apply to the *structure*. It DOES still apply at the finer grain of *how the up-sector frame is pinned* — so the pre-registration for Round 52: **the up-frame forcing is T2547's top-saturation {1,α,α²}, stated BEFORE V_cb is computed; V_cb/V_ub = the {1,α,α²}↔{1,3,5} misalignment, target-innocent, no mass-input smuggling (K1790 G2/G4, re-scoped from the dead route B to route C).**

**Bank the ceilings as assets (Cal):** the two proved no-go results — mixing magnitude is **NOT radial** (K1635) and **NOT a one-insertion current** (this round) — are structural bounds in their own right. Any future radial-overlap or single-current magnitude claim is dead on arrival. That is real, publishable content: *"the mixing lives in the frame mismatch, not the radial overlap or a bare current — and we proved the second half."*

## 4. ★★ w(a) — Elie's decline RATIFIED; the team's framing RECALIBRATED forward (over-pessimism is as dishonest as over-claiming).

**Elie's decline of the pre-registration is CORRECT and I ratify it.** The sign clock ran in August (F924/K1387); a pre-registration filed today would be post-hoc theatre — the order of operations IS the value of the device. And Elie's self-diagnosis is exactly right: his 8-trial opposite-sign result came from reconstructing ρ(a) from its *name* ("completely monotone") rather than its *form* — the same error class as his 5410 retraction.

**Here is the ρ(a) Elie asked for (corpus, F799):** the shape is **w(a) = −1 + A·a⁶**, rate λ₁ = C₂ = 6 (spectral gap, F797) — completely-monotone, w>−1, wₐ>0, no crossing. That is the specific object; "generic completely-monotone ρ" is underspecified and flips on him.

**But the team's headline — "BST is on the wrong side, the falsifier STANDS" — is a stale August snapshot, and the fuller corpus is importantly less grim (calibrate both directions):**
- **T2559:** the no-crossing shape SURVIVES the model-independent radial BAO (DESI DR2 D_H; ΛCDM χ²/dof=0.95, phantom fingerprint absent).
- **T2560:** on DES-SN5YR the no-crossing model TIES the CPL phantom with zero offset and BEATS it with a documented low-z calibration offset (0.02–0.05 mag, certified free-not-tuned).
- **Cal's own PreRegistered Falsifier Table v1.1 (2026-08-10):** "the BST-SPECIFIC no-crossing form is disfavored at only **~1.3–1.6σ** in the distinguishable channel — NOT the ~3σ I earlier misattributed to BST. **The banked w=−1 is NOT falsified.** This is NOT BST's sharpest tension — that is Σm_ν."

**So the calibrated statement (forward):** BST predicts wₐ>0 and IS on the wrong side of the CPL *headline* (pre-registered, known) — but that headline crossing is CPL-parametrization- and SNe-driven, **absent from the model-independent H(z)**, and in the BST-distinguishable channel the disfavor is only ~1.3–1.6σ. The falsifier is **live but mild, not fired**; the banked w=−1 is not falsified; the decisive test is DESI DR3. "Wrong side, falsifier stands" *under*-states BST's actual position.

**The genuinely open forward test is Cal's §4751 SHAPE test (Δχ² vs CPL) — a shape question, not the settled sign.** That clock has NOT started, so THAT is where a legitimate pre-registration applies, with Cal's guards: **C6** (freeze the prediction — chmod 444 + posted SHA256; the corpus has ≥4 inconsistent w(a) declarations, so freezing is mandatory), **C7** (state what it does NOT depend on — name the free knobs; if zero, say zero), **C3** (pin the dataset combo + Δχ² kill threshold BEFORE the lookup). Do not conflate the open shape test with the settled sign — a live falsifier must not hide behind an open one.

## 5. What is FINISHED (ratified). (Lyra)

- **QM package COMPLETE — criterion C artifact closed.** Axioms-of-QM (10/10 Dirac–von Neumann, zero posits) + Measurement-as-Commitment (C = P_record ⊕ P_encode). No loose thread.
- **CHSH closed AS A PREDICTION, not a hole:** Tsirelson² − S²_BST = 1/2^{N_c} = 1/8 → **S_BST ≈ 2.806, ~0.79% below 2√2** — a sharp near-term falsifier. Tier stated cleanly: the sub-Tsirelson bound + exact deviation are **Identified**; the value 2.806 rides a candidate form until the operator-level CHSH identification is pinned (Elie's lane). Process/arrow/odds/commit all Derived; the Bell magnitude is a separate falsifiable prediction. RATIFIED.

## Dispositions
- **Weak-current CKM route (B): REFUTED, banked as a proved ceiling.** Not a failure — an asset (Cal).
- **Redirect (route C = T2530/T2519/T2547): the forced survivor of an exhaustive dichotomy, already the banked spine.** Round-52 forward = V_cb/V_ub as the {1,α,α²}↔{1,3,5} frame misalignment, pre-registered per §3, K1790 G2/G4 re-scoped onto it.
- **K1181:** superseded to multiplier-0 on the current-matrix-element framing; surviving content (current mandatory) feeds route C. Fold into Rubric coverage map at tonight's curation (forward), no grooming pass.
- **w(a): Elie's decline ratified; framing recalibrated — no-crossing survives both direct probes, mild ~1.3–1.6σ disfavor, NOT fired.** Open forward test = §4751 shape (C3/C6/C7). ρ(a) = −1+A·a⁶ handed to Elie.
- **Reconciliation:** Elie re-run on the intrinsic gate (≈2.70) so both confirmations name the same object.
- **QM package + CHSH: finished, ratified.**
- Nothing external. Nothing pushed.

— Keeper, K1791. Two ceilings proved, the survivor forced, the frontier sharp. The discipline is generating results, not grooming.
