# CLEAN-REPO PRE-GO GATE — the definitive checklist before ANY external (flagship Forcing+Evidence)

**Keeper (hub + final audit), 2026-08-09. The flagship PASSED Cal's hostile read (K1313). Casey approved both pending decisions (the two flagship wordings + Grace's PMNS dedup). This is the living gate: every box must be TRUE before external. Nothing external until all checked + Casey's explicit GO. This is the standing "clean the repo" gate (task #104).**

## Status legend: [ ] open · [~] in progress · [x] done+verified

## A. Paper fixes (Cal's 4, from the hostile read) — Lyra applies → Cal re-confirms
- [x] **A1. cos ψ = 5/√34 → V_cb marked CANDIDATE**, both gaps named — DONE in flagship v0.2.3 (Lyra: value gap 6–10° vs 2.4° + innocence gap named). *(Owner: Lyra)*
- [x] **A2. "forced modulo one datum = GR-level" qualified** — DONE v0.2.3 (GR-level in input economy, carries the I.5 residuals). *(Owner: Lyra)*
- [x] **A3. parity forces the SHAPE** (sin²θ_W = 3/13 PD) + **CP existence not value** — DONE v0.2.3. *(Owner: Lyra)*
- [ ] **A4. Cal re-confirms** A1–A3 applied in the file. *(Owner: Cal — pending; fixes are in v0.2.3, Cal re-reads.)*

## B. Clean-repo artifacts — Casey APPROVED (2026-08-09), execute
- [ ] **B1. The two flagship wordings** (Casey approved): `data/bst_this_is.md` (α = charge-count 137 + curvature correction, "Wyler integral" attribution retired) + README Wyler headline/homage (honor his SO(5,2) *insight* + the direction he reached toward; his exact Vol^(1/4) formula retired; α presented as N_max charge-count + curvature, not the Wyler formula). *(Owner: Grace/Lyra to stamp per Grace's already-drafted wording; Keeper verifies bodies match banners — no half-done sweep.)*
- [ ] **B2. PMNS dedup** (Casey approved): keep ONE clean geometric form per angle (θ₂₃ → 4/7, θ₁₃ → 1/45, θ₁₂ → the picked one of {4/13, 42/137}); mark the compound (44/45-suffixed) forms **superseded**, never silent-delete; fill/remove empty predicted-value cells. Ties task #84 (pointer-integrity). *(Owner: Grace)*
- [ ] **B3. Millennium PDFs verified current — NOT fully closed (Cal re-confirm, 2026-08-09).** The 17 numbered Millennium PDFs are current ✓. BUT Cal's broader scan caught stragglers the subset-report missed: **FIVE Riemann-family papers have source newer than their PDF** (if any carries a Proof→Attempt edit, the compiled PDF may not show it), and **BST_RH_Weil_Positivity_Proof has NO PDF at all** (the paper with the LaTeX error — build failed or never ran). FIX: rebuild + re-read those five, confirm RH_Weil actually compiles, OR mark each explicitly "internal/superseded, out of scope" — each verified by opening the compiled artifact. "Content-ready isn't cleared." *(Owner: RH-paper owner / Elie build + Cal re-read.)*

- [ ] **★ B4. RH "PROVED"-title hazard (Cal, HIGH — hard blocker, K1316).** `BST_Why_Geometry_Proves_Riemann` (title says "…Proves Riemann") and `Koons_Riemann_BST_2026` ("the conjecture has been PROVED via three independent routes") — a serious reader hitting either discredits the whole repo on sight. Reframe both to "Attempt" (K940, task #103) + rebuild, OR mark superseded + remove PDFs; each verified by re-opening the compiled artifact. Confirm the two "Superseded by Paper #103" Riemann files are scoped out. Millennium outline (reframed but stale) → rebuild or scope out. *(Owner: pandoc/honesty lane + Cal re-verify.)* **Non-negotiable before external.**

## C. Consistency sweep (Keeper final audit) — no banner without a matching body
- [ ] **C1.** The V_us split + F85-radial-Derived + mixing-Identified tiers are consistent across the flagship, `data/bst_constants.json`, and the registry (no stale "all CKM derived" / "V_cb = 4/79" anywhere). **V_cb consistency web (K1316):** V_cb Candidate ⟹ **A_Wolf → Candidate** (A = |V_cb|/λ², currently mis-tagged Derived in 2 entries); k1001/k1003 "V_cb Derived" prose corrected-forward (Grace, done). *(Owner: Keeper + Grace)*
  - **★★ C1-CRITICAL — the CP gate was closed on the CKM side but NOT the PMNS side (Keeper C1 sweep, 2026-08-09).** The binding CP gate (existence-only, NO J, NO δ VALUE) applies to *both* sectors, but the lepton side still leaks:
    - **Registry T2536** — "δ_PMNS cos²δ = 45/49 + **J_PMNS ≈ 0.0338** — **DERIVED (forward)**": a leptonic δ-value AND a J-value, tagged Derived. Same binding-gate violation Grace just purged on the CKM side.
    - **data/bst_predictions.json** — "δ_PMNS (leptonic CP phase) — **D**".
    - **FIX (parallel to Grace's CKM purge):** the δ_PMNS / J_PMNS **values** → existence-only, off (no number, no agreement-%); keep only "leptonic CP exists (forced)". If the cos²δ = 45/49 sum-rule is a real *structural* relation, keep it Structural/candidate WITHOUT the displayed value. *(Owner: Grace [data] + registry owner; Keeper re-verifies.)*
  - **C1-MODERATE — PMNS θ₁₂/θ₁₃ mis-tagged "D" in live data.** `data/bst_constants.json` tags "PMNS sin²θ_12 (solar)" and "PMNS sin²θ_13 (reactor)" as **D**. Per K1313/K1314 the PMNS *structure* is Derived but the *values* stay **Identified/gated on the kernel** (Grace's own blind score). Re-tier both **D → I**. (θ₁₂ = 3/10 is the geometric-primary FORM, Identified value.) *(Owner: Grace.)*
  - **C1-MODERATE — registry "Proved" on CKM/PMNS mixing theorems** (T919, T1254, T1259, T1474, T2510, T2535 all say "Proved"). The registry Proved column is not the rigorous D/PD/I/C/S tier (task #91), but an external reader reads "Proved" as Proved. Annotate the CKM/PMNS mixing rows with the honest current tier (Candidate/Identified/Structural), or add the "Proved-column ≠ rigorous-tier" header note. *(Owner: registry governance, ties #91.)*
- [ ] **C2.** CP: existence-only, NO J value, no δ value, ~O(100×) noted — everywhere (paper, data, registry). *(Owner: Keeper)*
- [ ] **C3.** #79 stated as "forced modulo one datum" with Leg B(ii) at its K1312 tier (forced-at-structure + named real→complex residual), NOT over-claimed as Derived-end-to-end. *(Owner: Keeper)*
- [ ] **C4.** No "600+ predictions" volume-lead; α "not Wyler"; sin²θ_W PD; dead gravity-tie absent — re-confirmed post-edits (Cal's gates stay green after the wording changes). *(Owner: Keeper + Cal)*

## ★ C-SWEEP FINDINGS (Keeper, 2026-08-09) — real leaks in EXTERNAL-facing files (the flagship is clean; the repo front-door is NOT)
The paper passed Cal's gate, but the repo (README + data/) still carries retired/over-claimed forms a hostile external reader would hit first. Since the public stance is "the math's on GitHub," these are GO-blocking. Routed, not fixed (ownership: Grace=data, README=Grace/Lyra + Casey tone call).
- [x] **★ CRITICAL — CP J-VALUE leak — CLOSED 2026-08-09 (Grace, ratified K1314).** Both J_CKM ledger entries neutralized + 3 README rows purged (γ=arctan√5, A²λ⁶η̄ @0.3%, summary CP row). Repo now reads CP existence-only, magnitude/phase off, no values. ALSO ruled K1314: η̄ value → OFF (CP-violating), ρ̄ → Identified (Grace to apply). Original finding retained below for record:
  - `README.md:152` — table row "J_CKM (Jarlskog) | A²λ⁶η̄ | 3.07×10⁻⁵ | 3.08×10⁻⁵ | **0.3%**" — a *retired reverse-fit* (Wolfenstein A²λ⁶η̄, demoted D→I per K684; data file itself calls it "not a forward derivation") shown as a 0.3% prediction on the front page.
  - `README.md:556` — "CKM CP phase | γ = arctan(√5); J = √2/50000 | 0.6%" — the **retired γ=arctan(√5) reverse-fit (K683)** AND a J value, both stale.
  - `data/bst_constants.json` J entries (const ~2866, ~5384) display J=3.072e-5 "(observed 3.08e-5)" and J=g⁴c₂²/(n_C·N_max⁵) — tier-labeled I with honest mechanism, but the *value + observed-comparison still display*.
  - **FIX:** purge all J/δ VALUES + agreement-% from README + data external displays; state CP **existence-only**, magnitude ~O(100×) off (per K1304 hard rule). Retire the γ=arctan(√5) row. *(Owner: Grace + README owner; Keeper re-verifies.)* **This is the same binding gate the whole paper rests on — the repo must not contradict it.**
- [ ] **MODERATE — cos ψ marked "Derived" in live data.** `data/bst_26_tier_map.json:115` says "Direction cos ψ = 5/√34 (**Derived**, F384)" — contradicts K1313 (cos ψ→V_cb is **Candidate**; projection open). Downgrade to Candidate; keep V_cb Structural/down-only. *(Owner: Grace.)*
- [ ] **FLAG (Casey tone call) — "600+ predictions" volume-lead.** `data/bst_this_is.md:19`, `README.md:84`, `README.md:578` lead with "600+ predictions." The flagship deliberately avoids this (Cal gate). At minimum qualify to "600+ predictions, honestly tiered (most Identified/Structural, few Derived)" so the volume-lead doesn't read as 600 Derived results. *(Owner: Casey's call on README tone; Keeper recommends the qualifier.)*
- Note: `data/bst_this_is.md:9` α line is already honest (charge-count 137 + curvature n_C/N_max, "Wyler's exact formula didn't hold, direction right") — B1 partially in there; verify README:127/428/658 match.

## D. Final GO
- [ ] **D1.** All of A–C checked. Cal green. Keeper final PASS.
- [ ] **D2.** **Casey's explicit GO.** (Standing rule: nothing external — Zenodo/arXiv/outreach — without Casey's word. Never push without approval.)

## Notes
- **The paper does NOT wait on the K1012 kernel** — the mixing values ship honestly Identified/gated; the kernel is the later Identified→Derived upgrade.
- This gate covers the **flagship** (Forcing+Evidence). The Finster/CFS bridge note (task #102) is a SEPARATE, later, still-gated item — not part of this GO.
- Keep this file updated as boxes close; it is the single source of truth for "are we clear to ship."

— Keeper, clean-repo pre-GO gate, 2026-08-09. Flagship passed hostile read; Casey approved the 2 wordings + the PMNS dedup. Gate = A (Lyra's 4 fixes + Cal re-confirm) + B (wordings + dedup + PDFs) + C (Keeper consistency sweep) + D (Cal green, Keeper PASS, Casey GO). Nothing external until all checked. Nothing pushed.
