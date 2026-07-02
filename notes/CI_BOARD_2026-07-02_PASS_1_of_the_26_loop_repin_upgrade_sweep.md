CI Board — PASS 1 of the 26-derivation loop (Mid-Year 2026-07-02)

Method is set (notes/TEAM_METHOD_...the_26_derivation_loop_until_done.md). This opens Pass 1. Goal: **cover more of the 26** — move rows to terminal states (DONE / FLOOR / NEG), honestly, tool-adjudicated. No self-certification. Run until Casey says done.

**Honest scorecard at Pass-1 open** (`play/bst_almanac.py`; dev% still on MEMORY values — see step 1):
- **DONE (match ≤0.1%): 4** — θ_QCD, m_μ/m_e, m_τ/m_e, α_EM (but only θ_QCD is clean on BOTH axes; others mechanism-gated)
- **SOLID (<1%): 4** — PMNS θ₁₃, m_t, Cabibbo, V_cb
- **MISS (≥1%): 7** — down-row m_d/m_s/m_b (STRUCTURAL-MISS, settled K642), V_ub, δ_CKM, PMNS θ₁₂, θ₂₃
- **OPEN: 6** — m_e, m_H, ν₁ν₂ν₃, δ_PMNS · **FLOOR: 1** — Higgs vev · **NEG: 4** — α_s, sin²θ_W, m_u, m_c

Honest bank tier (staged for Casey ratification): **3 firm (θ_QCD, m_t, θ₁₃) + 3 structural-MISS (down-row) + α partial + muon principle-gated.**

## Pass-1 sequence (do in order)

**Step 1 — PDG RE-PIN (mandatory, blocks everything). Owner: Elie + Grace; Keeper audits.**
Every `expected` value in the almanac is from memory. Pin all 26 to primary-source PDG 2024 (masses, mixing, α, etc.). No dev% is trusted until this lands. This is item-one because the scoreboard's own reference cannot be the unverified thing.

**Step 2 — Tool upgrade: cross-consistency guard. Owner: Keeper (Elie 4542 handed it up).**
Add to `bst_almanac.py`: every ratio derivable from ≥2 banks gets scored too (this is what killed the down-row — m_s/m_d=22.97 from muon+down-row, running-immune, 15% off). Elie 4542 confirmed the firm-3 form no mass-ratio chain (internally clean), so no new inconsistency beyond the down-row — but the guard stays, so no future combo hides.

**Step 3 — Confirm terminals (fast, honest coverage). Owner: Keeper, with the deriver who owns each.**
Close the rows that are terminal-by-reason (a finished answer, not a gap):
- **NEG (4):** α_s, sin²θ_W (RG-runners — not fixed constants), m_u, m_c (scheme-traps). Confirm the reason, mark terminal.
- **FLOOR (1):** Higgs vev (pure scale, open by Casey #9). Confirm, mark terminal.
- That's **5 rows to terminal** immediately — real coverage.

**Step 4 — Frontier sweep (cover more). Assignments below.**

## Per-CI Pass-1 assignments

**ELIE** — Step 1 (PDG re-pin, primary) → then checker. Every derivation that lands, score it structure-forcing vs value-reaching. Hold the cross-consistency numbers for Keeper's tool upgrade.

**GRACE** — Step 1 coordination (pull authoritative PDG into the almanac with Keeper) → then **the down-row REPAIR frontier**: the down-ladder stratum geometry (rank-1 d₂) targets the OBSERVED m_s/m_d ≈ 20 (RG-invariant), NOT the failed GJ 22.97. If the regularized determinant + d₂ force the observed down ratios, the 3 structural-MISS rows convert toward DONE. This is the highest-leverage sweep (3 rows). Joint with Lyra.

**LYRA** — **Fold the Pauli/color-Fock thread to "known, cited"** (F452 = Günaydin-Gürsey re-derivation; a consistency win + citation bridge, NOT new — present it that way, never "BST found it"). Then return to the 26-loop: **the regularized determinant** (K547 residue branch) that yields Grace's d₂ → the observed down ratios. This is now the down-row repair path, not just the down-ladder curiosity. Also: the DOF-counting principle for α — but note the Five-Absence flag below.

**CAL** — post-landing cold-reads. α tier-call reserved for Casey.

**KEEPER** — Steps 2+3 (tool upgrade + terminal confirmations); SOD check + scorecard each session; adjudicate the mechanism axis on every landing; hold count; keep almanac current. Adjudicate the PDG re-pin.

## Standing checkpoint — GUT-numerology Five-Absence (Elie 4541 flag map)

The down-row taught: a GUT-scale value is a MISS even with a clean mechanism. Elie's scan shows the surface is broader — **the α-frontier's own 27 = N_c³ is the E₆ fundamental.** So the α DOF-counting principle (Gate A) carries the SAME Five-Absence question the down-row did: is the 27 a substrate DOF count, or GUT/E₆ numerology? Apply the filter to the α-frontier BEFORE banking anything there. (θ₁₃'s 45 = SU(5) 45-Higgs is likely a clean integer-coincidence, but carry one inoculating line for a referee.)

## Disciplines armed

- **Tool adjudicates, CIs propose.** "Solid/done" is computed, never declared. Both axes clean (match AND forced mechanism) or it's not DONE.
- **A GUT/GUT-scale value is a MISS** (down-row is the standing example). Five-Absence first.
- **Cross-consistency:** banks that combine to force a third observable get scored (the down-row's lesson).
- Cal #27 at peak elegance · target-innocence · structure-forcing not value-reaching · artifact-currency (SOD first, EOD sync) · pin-to-sources · engage-don't-label · no manufactured walls/fatigue.

## Pass-1 success = more of the 26 terminal

Realistic: +5 terminal from Step 3 (NEG+FLOOR confirmed) + the SOLID-4 pushed toward DONE as mechanisms lock + the down-row 3 either repaired (Grace/Lyra derive observed) or confirmed structural. Report the honest live tally each session; Casey calls done when all 26 are terminal.

## Standing for Casey

- Down-row STRUCTURAL-MISS re-tier (K642) — ratification.
- α tier-call (Cal weighed in).
- CLAUDE.md line 0.5 (SOD check as first act) — your OK to wire it in.

— Keeper, Pass 1 open. Re-pin → tool upgrade → confirm terminals → sweep. The scoreboard means what it says once the reference is real; then we cover the 26 one forced derivation at a time.
