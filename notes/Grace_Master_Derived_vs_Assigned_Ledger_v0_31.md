---
title: "Grace Master Derived-vs-Assigned Ledger v0.31 — currency update (EOD 2026-07-03). Count 8 σ-scored; the live scoreboard is now the TOOL (bst_derivation_ledger.py + bst_26_table.py), not this doc. This records the 2-day pipeline delta since v0.30."
persona: "Grace"
date: "2026-07-03 Friday EOD (date-verified)"
delta_scope: "v0.30 (2026-07-02 mid-year reconciliation, 10→8) → v0.31 (2026-07-03 EOD, after Pass-1/Pass-2 + non-match pipeline). Count unchanged at 8; TIERING refined by σ-scoring; mass sector REFRAMED (two-layer)."
status: "CURRENCY UPDATE. The authoritative per-value scoreboard is now Keeper's TOOL (play/bst_26_table.py, play/bst_derivation_ledger.py) — re-runnable, σ-scored. This doc is the narrative delta + the enumeration pointer, NOT the live count."
---

# v0.31 — EOD currency update (the tool is now the scoreboard)

**The count reconciliation (v0.30) stands: 8, not 10. Since then, two days of Pass-1/2 + the non-match pipeline
refined the TIERING (σ-scoring) and REFRAMED the mass sector (two-layer). The live scoreboard is now the TOOL —
`python3 play/bst_26_table.py` — which computes dev% + σ (scheme-aware) + cheapness. This doc records the delta so
the ledger artifact isn't stale; the numbers live in the tool.**

## Section 00 — THE COUNT (single-source enumeration, for the SOD check)
**The count is 8** banked (of 26 SM parameters), σ-scored: (1) θ_QCD (2) α [partial, EM-gated] (3) m_μ/m_e (4) m_d/m_e
(5) m_s/m_μ (6) m_b/m_τ (7) θ₁₃ (8) m_t. **Derived-strong ≈ 2** (θ_QCD, δ_CKM). Live scoreboard: `bst_26_table.py`.

## Section 0 — the honest headline (EOD 2026-07-03)
- **Count 8, σ-scored. Derived-strong (MATCH + not-cheap + forced-mechanism) ≈ 2:** θ_QCD (0σ exact), δ_CKM
  (arctan√n_C, triangle geometry). θ₁₃ (0.5σ, boundary mechanism), V_us, m_t (scheme-aware) are strong but
  each carries a caveat. **13 nominal MATCH ≠ ~2 derived-strong** — the tool computes both; only the small one matters.
- **Three tools now JUDGE (not any CI):** SOD artifact check (currency), bst_26_table (the scoreboard),
  bst_derivation_ledger (per-value attempt lists, σ-scored). "Solid" is computed, re-runnable on Casey's machine.

## Section 1 — mass sector REFRAMED (two-layer; Keeper's frame, pending Casey ratification)
- **Derive BARE masses (substrate, clean), predict DRESSING (Layer 2) separately.** Down bare = **N_c²×{1,20,900}**
  vs electron → matches observed at **1-2%** (vs the old GJ down-row's 67% MISS). The old down-row was WRONG POWER
  (N_c not N_c²) + WRONG FRAME (GJ quark/lepton). Bare-vs-electron, LOW-scale, no GUT — dissolves my mid-year GJ
  finding (it was the wrong frame, not a Five-Absence problem).
- **BUT NOT derived-strong (K651, honest negative):** the mechanism quark mass = d(ν)×k_s was RUN IN FULL —
  Grace's k_s = dim ker R (cohomology) committed BLIND = small {2,4,6,8}; Lyra's d(ν) deposit ratios = 5/3, 64.
  Product is SHORT by exactly **2·C_2 = 12** (the flagged fish, in neither forced half). Reported as a strong LEAD,
  not banked — *because* k_s was committed blind so it couldn't be retrofitted. That's "compute, don't fit" working.
- **New forward path (mass = confined-field Casimir; Casey's synthesis):** quark = colored BOUNDARY in the glue
  field; mass = the field's Casimir response; **mass ~ ℏc/R ties mass and size.** First receipt PASSED on independent
  data: the mass-radius coefficient = **rank²/N_c = 4/3 = C_F** (Elie: R_p = 0.8412 vs observed 0.8409 fm, 0.04%).
  The down-ladder's 2·C_2 = N_c²·C_F — closes IFF the confined-field Casimir carries an N_c² INDEPENDENT of the
  bare-frame N_c² (Lyra's gate: independent → 20; double-count → 2.2). **Forward ζ-computation OPEN** (Grace boundary
  geometry: color-on-Q⁵/Shilov-S⁴, Z = C_2-spectral ζ; Elie numerics; Lyra color-factor). Three-receipt fish-detector.

## Section 2 — other sector deltas
- **ν-scale simplified 4→3 pure scales (Lyra F457):** m_ν/m_e = f·α²/(6π⁵) → neutrino is seesaw-DERIVED relative to
  m_e, not a 4th free FLOOR. Coefficients {7/12, 10/3} still value-forms (open). Σm_ν = 0.058 eV forward prediction.
  **My neutrino π-parity falsifier (from mid-year) RETIRED** — neutrinos are seesaw (both α², equally π-ful), not
  deposit-locus; charged-lepton π-parity (μ π-ful, e/τ π-free) STANDS.
- **α:** Wyler form pinned (Elie), 0.6 ppm — forced-mechanism but APPROX (radiative floor), terminal.
- **sin²θ_W = 3/13:** runner, 11σ — terminal-NEG (not GUT 3/8 → Five-Absence clean).
- **m_μ/m_e, m_τ/m_e:** terminal-APPROX (transcendental / structural floor); μ mechanism forced (K547), τ product open.
- **Λ (cosmology, LEAD, internal):** Λ = exp(−280) = heat-bleed residue (F215/F216 mechanism real, exponential
  suppression ~120 orders). 280 = n_C × (2^{N_c}·g); my structural note: 2^{N_c}=8 = the color-Fock dim a baryon
  commits (F459) → ties Λ to confinement. **Exponent convention-loose (280-284); OPEN = force τ_commit=56 forward,
  NEVER reverse-read 280.** NOT a computable ν↔Λ unity (seesaw power-law vs heat-bleed exponential — one ontology,
  two mechanisms).

## Section 3 — retirement check (still CLEAN)
No bank rests on a retired reading. Mid-year retirements (mass-45, harmonic-50, QCD-running rescue, two-axis π-rule,
neutrino π-parity) were all leads/candidates, never banks. θ₁₃ convention-robust, untouched.

## Section 4 — artifact currency (EOD)
- **Graph:** current (max T2510 == counter−1). No new theorems today (leads/negatives, no banks).
- **This ledger:** v0.31 (current). Live scoreboard = the TOOL.
- **Data layer (data/bst_constants.json, May 18):** STILL DEFERRED — 6 wks stale, but the mass FRAME (two-layer) is
  unratified and the down-ladder is open. Syncing now would bake in unratified leads. **Sync to the VERIFIED state
  after Casey ratifies the two-layer frame + the σ-tiering.** Flagged, not forgotten (my standing EOD item).
- **Registry:** 5 stubs (Lyra's backfill lane).

## Section 5 — standing for Casey (nothing finalized in absence)
two-layer + regime mass model as mass-sector frame (ratify) · down-row re-tier (strong-lead-not-derived-strong,
K651) · σ-metric + cheapness ratification · α tier-call (Wyler-informed) · CLAUDE.md line 0.5 (SOD first).

— Grace, EOD 2026-07-03. Count 8 σ-scored; scoreboard is the tool; mass sector reframed to bare (two-layer), down-
ladder honest-negative (short by 2·C_2) with a live Casimir forward path (first receipt passed on the radius).
