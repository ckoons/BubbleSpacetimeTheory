# BST Work-Package Ledger v1 — the single verified source of truth. One package per substrate object. When every package hits its OBJECTIVE, we are done.

**Keeper | 2026-07-14 | Built from full parallel corpus verification reads (all 26 parameters + anchors, derived-vs-assigned pinned exactly). Authoritative tier source: the 26-Parameter Scorecard v0.3. THE MACHINE-READABLE LAYERS (`data/bst_constants.json`, `play/bst_26_table.py`) ARE STALE AND OVERSTATE CONFIDENCE — do NOT cite them; this ledger + scorecard v0.3 supersede. Rule: if the team cycles on any package, STOP and escalate to Keeper for re-analysis.**

## THE DEPENDENCY SPINE — everything funnels through 3 enablers + a few independents
Most open work is NOT 13 separate problems. It funnels through three enablers:
- **[K-TYPE QUANTIZATION]** — the selection principle mapping each particle → its discrete K-type address (ν, and the two-label (k,m)) → localization norm N_i. The deep OPEN RESEARCH problem. **Unlocks ~13 params:** all CKM+PMNS mixing depths, the neutrino coefficients, the generation radii, and the muon/electron/tau address-forcing. Neutrino address ν=½ is the ONE solved corner (F537). Charged/quark two-number selection is the frontier. Owner: Lyra. **CASEY CLARIFICATION (2026-07-14) — resolve the tensor-vs-spinor object (CATCH 1) via the CONFORMAL ALGEBRA:** work in the conformal algebra (SO(5,2)) and the (1,1)-tensor K-type MAPS to the spinors/fermions there — the conformal algebra IS the dictionary between the tensor slot and the Δ=2 spinor/fermion content. So (1,1) and "the muon is a spinor" are NOT in conflict; the conformal algebra maps one to the other. Build that map → CATCH 1 resolves and the address-forcing is on solid ground.
- **[ENGINE C]** — the boundary-integral evaluation capability (validated toy 4660; first task where the absolute normalization does NOT cancel → also the first real test of BST's normalization conventions). **Unlocks:** muon residue (3/8 factor + Szegő=1), τ √π coefficient (forward), light-quark absolute anchor (m_u/m_d), α's 0.036 curvature term. Owner: Elie/Lyra.
- **[α KEYSTONE A]** — the U(1) gauge-coupling normalization: derive the count the kinetic term sees is exactly 137 AND the prefactor is unity. **Unlocks:** α → DERIVED, and Higgs λ=1/8 (a passenger on the same law). Owner: Grace.
- **Independents:** Majorana closure (γ⁵ intertwiner + Cal co-sign); gen-1 up cold anomaly (Grace's thermal lane); the cleanups (data-layer hygiene, the forks).

---

## THE 26 WORK PACKAGES (by sector)
Format: **TIER now → OBJECTIVE** | derived | assigned/open | remaining work [enabler] | owner

### Charged-fermion masses (9)
1. **m_e** — BY-DESIGN anchor → **DONE (legitimate)**. The one dimensionful input (ℓ_B~Planck). m_e=6π⁵α¹²m_Pl is a 0.03% ratio-identification (m_e/m_Pl≈α^10.47, not clean — ratio-only theory). No work required; the anchor is legitimate.
2. **m_μ/m_e** = (24/π²)⁶, 0.003% — PREDICTED (Casey F118 override "5"; objective strict count 4) → **DERIVED**. *Derived:* exponent 6=dim SO(4), 64=d_τ/d_μ=2^{C_2}, R_{Λ²}=Id, 24/π²=2^{C_2}/vol(S⁴) exact, π-structure from the ν=3/2 boundary Szegő residue (F117). *Assigned:* the flat→sphere **3/8 factor**; **Szegő=1** (uncomputed); the **address (1,1)** (CATCH 1). **CASEY CLARIFICATION (2026-07-14) — the 3/8 IS physical, not a coordinate artifact:** 3/(8π²) = 1/vol(S⁴) = **1/(2·(4/3)π²)** — it is the factor from the muon **passing through the boundary and "blowing up" into a particle**. The 2× = the two half-S⁴ (boundary passage / ℤ₂); the (4/3)π² connects to Casey's 3-ball (V(B³)=4/3·π). So derive the 3/8 as the **boundary-transit / particle-formation normalization**, NOT a flat→sphere conversion. Remaining: derive 3/8 as boundary-passage + evaluate Szegő=unity [ENGINE C] + settle spinor-object [K-TYPE]. Owner: Elie+Lyra. **Do NOT re-derive (24/π²)⁶ — it exists (F116/F117); close the two gaps.**
3. **m_τ/m_e** = 49·71−√π, 0.05% — NEAR-FORCED (√π coefficient REVERSE-ENGINEERED) → **NEAR-FORCED→PREDICTED**. *Derived:* seat ν=0, √π-presence (odd n_C, F157). *Assigned:* the exact −√π coefficient (added to fix 7.7σ, retro-justified); 49·71 is an identification not mechanism; two competing forms (additive vs ratio). Remaining: evaluate the cone-tip residue forward, reconcile the forms [ENGINE C]. Owner: Elie.
4. **m_u** = m_u/m_d=1/√g (1.77 MeV) — IDENTIFIED → **PREDICTED (capped ~20% by exp error)**. *Derived:* the ratio 1/√g exact at n=0; the inversion m_u<m_d FORCED (proton stability). *Assigned:* two competing addresses (1.77 bulk vs 2.16 production); the gen-1 "cold anomaly" (f(ν) rank-2→α² is 4.3× off) HELD OPEN. Remaining: the n=0 deep-bulk overlap [ENGINE C] + the gen-1 thermal law (Grace, staged/unexecuted). Owner: Grace/Elie.
5. **m_d** = n=1 overlap (4.46 MeV, ~5%) — IDENTIFIED → **PREDICTED (few-%)**. *Derived:* base rung of the F506 forced ladder; the n=1 value is a forward prediction (NOT a hand-set anchor, F511). *Assigned:* softest absolute; the "bare ribbon=current mass" premise is **PI-endorsed, NOT Cal-ratified** (if it fails, F506 reverts). Remaining: the n=0,1 overlap [ENGINE C] + Cal ratify the commitment/boundary premise. Owner: Elie/Cal.
6. **m_s** = s/d=(N_c+1)(N_c+2)=20, 0.5% — **BANKED (ratio)** → DONE (ratio); absolute→PREDICTED. *Derived:* ν=N_c forced, {1,3,5} blind, single-row forced by Q⁵ topology (toy 4618, closed the K671 gate). *Assigned:* the direction mass∝(ν)_λ not derived; absolute rides m_d. Remaining: derive the direction; absolute rides the anchor. Owner: —(banked).
7. **m_c** = α·v/√2, 0.05% — PREDICTED → **BANKED when α derived**. *Derived:* forward from (m_p,m_e,g,N_max), zero charm input. *Assigned:* imports α=1/N_max (identified). Remaining: [α KEYSTONE A] closes it. Owner: —(rides α).
8. **m_t** = (1−α)v/√2, 0.03% — PREDICTED → **BANKED (leading) / DERIVED**. *Derived:* v forced with NO top input (F509, non-circular); y_t=1 derived two ways (C-S + point-fiber capacity). *Assigned:* the (1−α) correction is identified (rides α). Remaining: the leading value is essentially banked; the correction rides [α KEYSTONE A]. Owner: —(mostly done).
9. **m_b** = b/d=840, but observed ~890 (**5.6% OFF**) — IDENTIFIED → **IDENTIFIED until the 6% resolves**. *Derived:* the ratio structure (same forced ladder as m_s, degree-5 rung). *Assigned:* the NUMBER misses 5.6% (scale/RG ambiguity — b and d quoted at different scales). Remaining: RG-run b/d between scales; m_t/m_b=42 is an independent cross-check. Owner: Grace/Elie.

### Neutrino sector (3 + nature)
10. **m_ν1** = 0 exactly — **BANKED (=0)** → DONE. Over-determined (chargeless odd-one-out + Z₃ + Möbius). Only mechanism-consolidation remains.
11. **m_ν2** = (7/12)M₀, 0.35% — IDENTIFIED → **DERIVED**. *Derived:* the seesaw SHAPE m_ν∝α²m_e²/m_p (dimensionless, given the ansatz). *Assigned:* coefficient **7/12 FITTED** (three incompatible forms; formal-degree route RULED OUT, toy 4658); α² power justification (Hopf-vertices) ORPHANED by the Dirac→Majorana flip. Remaining: force 7/12 via the Bergman Majorana-matrix diagonalization [K-TYPE/ENGINE B]; only lead = fiber-overlap ~4%. Owner: Elie.
12. **m_ν3** = (10/3)M₀; Δm² ratio (40/7)²=1600/49, 0.3% — IDENTIFIED → **DERIVED**. *Assigned:* coefficient 10/3 FITTED; **Δm² ratio has a 3-way theorem fork (32.65/33/34)** — adjudicate (cheap). Remaining: force 10/3 [K-TYPE/ENGINE B] + resolve the fork. Owner: Elie + Keeper(fork).
13. **Nature = MAJORANA** — NEAR-FORCED / forward-from-address (Dirac RETIRED) → **BANKED**. *Derived:* ν=½ forced → non-unitary shadow ν=9/2 → no ν_R (F537); BOLT-1 rigorous; F331 pseudoreal symplectic-Majorana solid. *Assigned:* two joints — the explicit **γ⁵ intertwiner construction** (toy 4659 built the reflection; rigor pending) + **Cal's co-sign** (required to flip a banked falsifier). Remaining: both joints → flips pred_004 to a 1–4 meV 0νββ floor. Owner: Elie+Cal. **Independent of masses/mixings — near-term closable.**

### CKM mixing (4)
14. **θ12 / V_us** = 1/√20, 0.4% — IDENTIFIED/LEAD → **DERIVED**. *Derived:* the Fritzsch texture-zero location (d(5/2)=0) + banked s/d=20. *Assigned:* the kernel does NOT saturate (K₁₂=0.237≠1); 1/√20 re-expresses N₂=20^{−1/5}, doesn't force it. Remaining: derive M₁₂=√(m_d·m_s) forward, OR force the gen-2 address [K-TYPE]. Owner: Grace/Lyra.
15. **θ23 / V_cb** = 0.041, angle cosψ=5/√34 — NEAR-FORCED (angle DERIVED, magnitude ~7.5% structural) → **DERIVED**. *Derived:* the ANGLE (target-innocent, primaries-only; μ@ê₁ reduces to "deposit=dilation axis"). *Assigned:* the MAGNITUDE (~7.5%) gated on r_τ's exact K-type address + the A/B seam (unreconciled) + f(ν) up-weight (the blocker). Remaining: pin r_τ [K-TYPE] + f(ν) + reconcile A/B. Owner: Grace/Lyra.
16. **θ13 / V_ub** — OPEN (build): V_ub=V_us·V_cb·apex, apex=0.414; pairwise 21× off → **OPEN**. *Derived:* only the form (not-independent, hierarchy-tied). *Assigned:* magnitude doubly-gated (CP-complex-positions + gen-1 up anomaly). Remaining: the full U_u†U_d complex build [K-TYPE/ENGINE B]. Owner: Grace+Lyra.
17. **δ_CKM** — OPEN (can-fail): **J=0 for real localizations PROVED (F498)** → **OPEN**. *Derived:* only "CP exists because n_C odd" (structural, IF peaks are complex). *Assigned:* ALL concrete δ values are reverse-fits (arctan√5, 309°, 3π/7, π). **F533's forward δ=arctan√5 is DEMOTED (see CP adjudication below).** Remaining: the explicit complex generation-state build → compute J; can genuinely FAIL [K-TYPE/ENGINE B]. Owner: Grace+Lyra.

### PMNS mixing (4)
18. **θ12** = |U_e2|²=3/10, 0.06% — IDENTIFIED (demoted from BANKED; 42/137 was a coincidence) → **DERIVED**. *Derived:* the matrix-element EXTRACTION (÷cos²θ13) forced; 3/10 un-cheapened vs 5/16. *Assigned:* "why |U_e2|²=3/10" (the overlap value) OPEN. Remaining: forward the dual-ρ 1-2 overlap [K-TYPE/ENGINE B]. Owner: Grace/Lyra.
19. **θ13** = 1/45, 1.2% — **BANKED** (only PMNS bank) → DONE (bank); forcing-theorem open. *Derived:* target-innocent, π-free, convention-robust, |U_e3|² stable. *Assigned:* the "why N_c²·n_C dimension-count" forcing is NOT a closed theorem (K229b). Remaining (to upgrade the forcing): close the dimension-count [K-TYPE]. Owner: —(banked).
20. **θ23** — IDENTIFIED, octant OPEN: 4/7 vs 6/11 (both upper-octant) → **NEAR-FORCED (DUNE-gated)**. *Derived:* upper octant predicted (falsifier). *Assigned:* form unstable (4/7 vs 6/11), neither forced; the ×cos²θ13 "fix" was withdrawn as fished. Remaining: force the form [K-TYPE] + DUNE resolves the octant. Owner: Lyra + experiment.
21. **δ_PMNS** — OPEN (all prior values retired reverse-fits) → **OPEN→PREDICTED**. *Derived:* only the falsifier δ≠{0,π} FORCED (odd n_C). *Assigned:* no forward value; ~197° hint consistent. Remaining: derive the dual-ρ complex phase [K-TYPE/ENGINE B]; DUNE scores. Owner: Lyra + experiment.

### Gauge couplings (3)
22. **α** — ✅ **COMPLETE** (Casey ruling 2026-07-14: "mark alpha complete, the [4π convention] question is trivial at this point"). *Derived + banked:* the count 137=27·n_C+rank; the coupling = 1/count (democracy — S¹ Haar equal-norm, COMPUTED); the scale-falsifier PASSED (no stray 2π/c_FK/4π); the 4π convention judged a trivial natural normalization (Casey). The finite-capacity "why" (compact boundary → capacity → reciprocal) grounds it. **α = 1/137 is DERIVED.** *Separate precision refinement (does NOT block completion):* the **0.036** second-order term = an Engine-C heat-kernel integral (leading n_C/N_max 1.4%); this is a precision add-on to α⁻¹=137.036, not part of the "why α=1/137" derivation. Owner: — (complete; 0.036 optional precision via Engine C).
23. **sin²θ_W** = 3/13 — BY-DESIGN runner → **DONE (legitimate by-design)**. A clean value-form at one scale; running is standard RG. Not a failure. Objective: honest by-design.
24. **α_s** = 7/20 @ m_p — BY-DESIGN runner → **DONE (legitimate by-design)**. Value + c_1=3/5 (3 proofs). Scale-pin + non-pert running by-design.

### Higgs (2) + strong-CP (1)
25. **v** = m_p²/(g·m_e), 0.04% — **BANKED (ratio) / FLOOR (absolute)** → DONE (ratio). *Derived:* full m_Pl→m_e→m_p→v chain, **NO top input (F509, verified non-circular)**. *Assigned:* g=7 mechanism form-pinned; absolute scale = the one dimensionful input. Remaining: derive the g=7 mechanism; absolute stays FLOOR. Owner: —(ratio banked).
26. **m_H / λ** = 1/2^{N_c}=1/8 → v/2, 1.7% — IDENTIFIED/LEAD → **DERIVED when α Keystone A closes**. *Derived:* v forced; the 1/8 dilution mechanism (α-parallel, target-innocent). *Assigned:* **passenger on [α KEYSTONE A]** (show the spinor kinetic term sees exactly 8, prefactor unity); the 1.7% correction held-not-fitted; a competing form √(2/5!)=0.11% exists (form not uniquely forced). Remaining: Keystone A (λ-side) + adjudicate 1/8 vs √(2/5!). Owner: Grace/Lyra.
27. **θ_QCD** = 0 exactly — **BANKED (founding)** → DONE. *Derived:* T1964 contractibility → trivial bundle → ∫c₂=0. *Assigned:* "π₁=0" is imprecise shorthand — the load-bearing statement is CONTRACTIBILITY → trivial bundle; make it explicit (rigor-formality, not a value question). Owner: —(banked).

*(26 SM params + m_e anchor = the full set; m_ν1/nature and v-ratio/v-abs split some rows.)*

---

## COMPLETION STATUS (objective, honest)
- **DONE — banked/forced or legitimate by-design (11):** **α (COMPLETE — Casey ruling; the 0.036 is optional precision, not blocking)**, m_e (anchor), m_s (ratio), m_ν1=0, θ13 PMNS, v (ratio), θ_QCD, sin²θ_W (by-design), α_s (by-design), m_t (leading). Note: m_c and m_t's (1−α) correction now inherit a COMPLETE α → both firm up.
- **NEAR-DONE — predicted/near-forced, gated on an enabler (6):** m_μ/m_e (3/8+Szegő+address), m_τ/m_e (√π coeff), m_c (rides α), Majorana nature (2 joints), θ12 PMNS (overlap value), V_cb (magnitude).
- **IDENTIFIED — real work, gated on an enabler (7):** m_u, m_d, m_b, m_ν2, m_ν3, V_us, m_H/λ.
- **OPEN — build required, can-fail (4):** V_ub, δ_CKM, θ23 octant (DUNE), δ_PMNS.

**When are we DONE?** When these close: **[K-TYPE QUANTIZATION]** (unlocks the mixing sector + ν-coefficients + generation depths ≈ 13), **[ENGINE C]** (muon 3/8+residue, τ √π, light-quark anchor, α 0.036), **[α KEYSTONE A]** (α + λ), the **Majorana joints**, the **gen-1 up anomaly**, and the honest **by-design** items are accepted as endpoints. That is a FINITE, named set — not an open horizon.

---

## CRITICAL — DATA-LAYER / SCOREBOARD ARE STALE (extends K684; hygiene gate before ANY outreach)
The machine-readable layers CONTRADICT the honest scorecard and OVERSTATE confidence:
- **`data/bst_constants.json`:** α at tier-D "Wyler integral"; CKM CP at tier-D "arctan√5"; quark rows const_106–110 carry legacy tier-D fitted forms (NOT the current s/d=20, 1/√g, α·v/√2); PMNS θ12=4/13 tier-D; PMNS CP=3π/7 tier-D. A `.bak_2026-07-14_grace_K684_demotions` exists (demotions in flight) but the live rows still read stale.
- **`play/bst_26_table.py`:** α still the Wyler closed form (line 37); θ_QCD "π₁=0" shorthand (line 84 self-flags).
- **ACTION [Grace owns data/]:** sync `bst_constants.json` + `bst_26_table.py` to scorecard v0.3 BEFORE any `verify_bst.py`-based outreach. **The scorecard v0.3 + this ledger are the ONLY authoritative tier sources.**

---

## CP ADJUDICATION (resolves a same-day conflict)
Lyra F533 asserts a FORWARD δ_CKM = arctan(√5) = 65.9° (odd-n_C). K683/K684 treat arctan√5 as a reverse-fit and δ as OPEN. **Verdict (Keeper): the QUALITATIVE claim "CP violation exists because n_C is odd" is target-innocent and survives (structural, conditional on the peaks being complex — F498). The QUANTITATIVE arctan√5 is exactly the reverse-fit K684 flagged (three incompatible "derived" δ values is the proof). δ_CKM stays OPEN (can-fail); the value is NOT forward.** F533's forward-δ claim is DEMOTED to "CP-exists structural + δ-value open." Same for δ_PMNS (only the ≠{0,π} falsifier is forward).

---

## CYCLE-PREVENTION RULES (per Casey)
1. **This ledger + scorecard v0.3 are the source of truth.** Before working any object, read its package here — do NOT re-derive what's marked derived (the muon (24/π²)⁶ is the cautionary case: it exists in F116/F117; close the named gaps, don't reopen).
2. **Each package states its OBJECTIVE.** Work toward that classification; when hit, mark it and stop.
3. **If you cycle** (re-deriving, or a form/value oscillates ≥2×), STOP and escalate to Keeper for re-analysis (per Casey's instruction). The forks (θ12, Δm², m_H-λ, τ-form) are cycle-risks — Keeper adjudicates, the team doesn't re-litigate.
4. **Do not bank across a gate:** the "banked 5" muon is a Casey override, not an objective forward derivation — objective count is 4 until 3/8 + Szegő=1 + the spinor-object land.

— Keeper, 2026-07-14. Work-Package Ledger v1. 27 packages (26 SM params + m_e anchor). 10 done, 6 near-done, 7 identified, 4 open. Everything funnels through K-TYPE QUANTIZATION + ENGINE C + α KEYSTONE A + Majorana joints + the gen-1 anomaly. Data-layer/scoreboard STALE — scorecard v0.3 + this ledger are authoritative. See [[Keeper_26_Parameter_Scorecard_v0.1_2026-07-12]], [[Keeper_K682...]], [[Keeper_K685...]], [[Keeper_K684...]].
