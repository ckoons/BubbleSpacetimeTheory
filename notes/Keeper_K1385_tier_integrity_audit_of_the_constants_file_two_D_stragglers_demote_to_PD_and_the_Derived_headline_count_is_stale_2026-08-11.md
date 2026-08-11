# K1385 — TIER-INTEGRITY AUDIT of `data/bst_constants.json` (self-directed, follows K1384). ★ The 16/3 was NOT a one-off: Grace's clean-repo gate (2026-08-02 + 2026-08-09) has systematically re-tiered over-claimed [D] constants DOWNWARD, concentrated in exactly the identification-heavy sectors (CKM/CP Wolfenstein, PMNS angles, nuclear magic numbers, cosmology fractions). That's the survival-audit discipline (K1383) working at the DATA LAYER — healthy. ★ BUT two stragglers still PUBLISH [D] while flagged for demotion — **const_015 (DM 16/3) and const_019 (Ω_b)** — and the "68 Derived" headline is stale (lags the applied re-tierings). RULING: both stragglers → PARTIALLY DERIVED (adjudicated, Cal+Keeper delegated authority); the "DERIVED" label typo normalizes to "D"; no outreach cites a fixed Derived count until Grace's gate closes + Cal cold-reads. Edits STAGED for the EOD data-sync (Grace's lane) — I rule, I do not edit the file mid-session. Cal cold-reads.

**Keeper (2026-08-11, self-directed after K1384. Grace found the 16/3 tier-inflation by accident while running the cell-count. That means the constants file can drift from the honest tier without direct audit — so I swept it. The gap is real but small and already mostly closed by Grace's gate; I'm ruling the two stragglers and flagging the stale headline. Cal cold-reads. Nothing pushed.)**

## What I found (full tier survey of 197 constants)
Current file tiers: **68 D, 66 S, 46 I, 11 PD, 4 C, 1 SUPERSEDED, 1 "DERIVED" (label typo).** 20 carry a review/re-tier/dedup flag.

**★ The re-tiering is a PATTERN, and an honest one.** Grace's clean-repo gate has already re-tiered a cluster of [D]→lower, concentrated exactly where BST does **<1% identification or asserted-count**, not forward derivation:
- **CKM/CP mixing:** Wolfenstein A (D→C, rides open V_cb K1313), ρ̄ (D→I), η̄ (CP-magnitude off, S).
- **PMNS:** sin²θ₁₂ (D→I), sin²θ₁₃ (D→I) — "<1% but not a forward derivation."
- **Nuclear magic numbers 4–7** (28/50/82/126): D→PD (deformed-magic, uncertified κ_ls deformation, K1132/K1133); κ_ls spin-orbit strength D→PD.
- **Cosmology fractions:** Ω_m (PD), Ω_Λ (PD, over-determination flag), DM 16/3 (flagged →PD), Ω_b (flagged →PD).
- **Confirmed-honest (no change):** H₀ (I — correctly inherited from CAMB inputs; "calibrate both directions, this one passes").

**This is the discipline working, not a scandal.** The walk-back rate is high at the data layer too (K1383's thesis holds one level down). The re-tierings are target-innocent and land in the sectors we'd predict. The *only* real defect is that **the headline count lags the honest re-tiering.**

## ★ RULING — the two stragglers (still publishing [D], flagged for demotion)
1. **const_015 — DM/baryon 16/3 → PARTIALLY DERIVED.** Adjudicated in K1384: the count 2^(2·rank) is asserted (channel-capacity story), not derived by tiling the boundary; 16/3 is the nearest 2^k/N_c to obs (mild form-selection). **D → PD.**
2. **const_019 — Ω_b = 18/361 → PARTIALLY DERIVED.** Downstream of Ω_m (PD) and the 16/3 (now PD); a downstream quantity cannot out-rank its weakest input (monotonicity). **D → PD.**
- **Authority:** tier adjudication is delegated to Cal+Keeper (feedback: audit-chain governance; Casey override). These two are no longer "pending Casey/Cal" — they are RULED. Cal cold-reads to co-sign.
- **Label hygiene:** the lone `"tier": "DERIVED"` entry normalizes to `"tier": "D"` (typo; it inflates no claim but breaks any automated tier-count).

## ★ The governance consequence (what this protects)
- **The "68 Derived constants" figure is STALE and must not be quoted externally as-is.** After the two stragglers apply and the label normalizes, the honest Derived count is **≈66–67**, and it is *still under active downward revision* by Grace's gate (dedup of duplicate CKM forms is queued, not closed). **Standing: no outreach, paper, or README cites a fixed "N Derived" count until Grace's clean-repo gate closes AND Cal cold-reads the final ledger.** (This is the K1384/K1383 principle: the artifact's honesty must be audited directly, not assumed from the K-ruling chain.)
- **The gravity arc's PD-floor (K1384) is now consistent with the data layer** once const_015 applies — the two 16/3 entries and the gravity same-object claim all sit at PD, honestly, until the forward cell-count promotes them.
- **Duplicate CKM/CP forms remain flagged-not-closed** (A: N_c²/(2C₂−1)=9/11 vs n_C/C₂; η̄: 1/(2√2) vs n_C/(rank·g)). Dedup is Grace's lane; the tier is already ruled (C/I/S). Not load-bearing for the current arc — noted so it isn't forgotten.

## Staged edits (for the EOD data-sync — Grace's lane, zero-judgment)
```
const_015: "tier": "D"        → "tier": "PD"   (K1384/K1385; 16/3 count asserted)
const_019: "tier": "D"        → "tier": "PD"   (downstream inherit, monotonicity)
<the one entry>: "tier":"DERIVED" → "tier":"D"  (label typo normalize)
```
Then recompute the D/PD/I/C/S headline and re-sync the board/README/CLAUDE.md counters. **I rule and stage; I do not edit the constants file mid-session** (it feeds counters that sync to root docs — unilateral mid-session edits desync the board, which is exactly the process discipline Keeper enforces).

## Why I ran this (standing value)
K1383 proved the *process* is honest. K1384 showed the *artifact* (constants file) can still drift from the honest tier — Grace caught the 16/3 by accident, not by audit. **The lesson: the data layer needs its own periodic tier-integrity pass, because it's what `verify_bst.py` and every outreach number are read from — the K-ruling chain's honesty does not automatically propagate to the published artifact.** Grace's clean-repo gate is that pass and it's working; my job is to (a) adjudicate the flagged tiers (done: two stragglers → PD), (b) hold the standing that the headline count is not quoted until the gate closes. **Standing: re-run a constants-file tier-integrity sweep before any outreach that cites derived-count figures.**

— Keeper, K1385, TIER-INTEGRITY AUDIT 2026-08-11. Swept all 197 constants: 68 D / 66 S / 46 I / 11 PD / 4 C / 1 SUPERSEDED / 1 "DERIVED"(typo). FINDING: Grace's clean-repo gate (08-02 + 08-09) has systematically re-tiered over-claimed [D]→lower in the identification-heavy sectors (CKM/CP Wolfenstein A→C/ρ̄→I/η̄→S, PMNS θ₁₂+θ₁₃→I, nuclear magic 4–7 + κ_ls→PD, cosmology fractions Ω_m/Ω_Λ/Ω_b/DM→PD) — HONEST, the survival-audit discipline (K1383) at the data layer; H₀ confirmed-honest (no change). Defect = the headline count LAGS the applied re-tierings. RULING: two stragglers still publishing [D] → PARTIALLY DERIVED — const_015 (DM 16/3, count asserted, K1384) and const_019 (Ω_b, downstream monotonicity); "DERIVED" label typo → "D". Cal+Keeper delegated authority; no longer pending; Cal cold-reads. CONSEQUENCE: the "68 Derived" figure is STALE (honest ≈66–67, still revising) — STANDING: no outreach cites a fixed Derived count until Grace's gate closes + Cal cold-reads final ledger. Gravity PD-floor now data-consistent once const_015 applies. Duplicate CKM forms flagged-not-closed (Grace lane, tier already ruled). Edits STAGED for EOD data-sync (Grace's lane); Keeper rules+stages, does NOT edit mid-session (counter-sync discipline). Standing: run a constants-file tier-integrity sweep before any derived-count outreach. Cal cold-reads. Nothing pushed.
