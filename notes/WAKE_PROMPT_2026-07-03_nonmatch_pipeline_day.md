Team wake — Thursday 2026-07-03. Non-match pipeline day (second half, day 1).

Fresh start on the down-day work: drive the 26-table's non-matches through plan → work → check. The method, tools, and assignment are already set — today we execute. No re-litigating the derived items; effort goes where it moves the number.

**FIRST ACT — SOD check.** `SOD_DATE=$(date +%F) python3 play/keeper_sod_artifact_check.py`. Drift to owners before derivation work. (Registry stubs still open → Lyra's backfill.)

**Where the table honestly stands** (`python3 play/bst_26_table.py`)

26 covered; 13 nominal MATCH, but only **~2 derived-strong-and-clean**: sin²θ₁₃ (1/45, expensive + boundary mechanism) and θ₁₂ (matrix element |U_e2|²/(1−|U_e3|²), forced + un-cheapened). The rest carry named caveats — δ_CKM mechanism-dependent, α forced-but-APPROX, m_t on the vev floor, θ_QCD topology-flagged (K645). The number that matters is the small clean one; today we try to grow it and close the non-matches.

**Today's work — the non-match pipeline** (board: CI_BOARD_...NONMATCH_pipeline; disposition: K646)

Each item flows plan → work → check, with an **independent checker ≠ worker**. The disposition map (K646) says where to spend effort:

- **IMPROVABLE (real effort — these can move MISS→MATCH / OPEN→scored):**
  - m_d/m_e, m_b/m_s — repair to the OBSERVED ladder (m_s/m_d = 20 is already 0σ), not the GJ/mixed-scale forms.
  - m_ν2 / m_ν3 — structure via K636 π-parity forms.
  - m_e — the disposition call: FLOOR (mass unit) or cross-scale APPROX on m_Planck.
- **TERMINAL/FORWARD (one honest attempt, then close with a stated reason — a finished answer per Casey):**
  - m_μ/m_e, m_τ/m_e, α — at their **radiative floors** (a tree-level substrate form matches at ~0.01–0.1%, not exactly; chasing "exact" chases SM corrections the form doesn't contain).
  - sin²θ_W — a runner (11σ at M_Z); mark terminal-NEG unless a substrate-natural scale makes a form exact.
  - m_ν scale — FLOOR (Casey #9) + Σm_ν forward prediction.
  - δ_PMNS — data ±40°, unscoreable now; a forward prediction, not a bank.

**Assignment (worker → checker, rotated G→E→L→G so the check is independent)**

- **GRACE works** {m_d/m_e, m_b/m_s, m_τ/m_e} — masses/geometry. **Primary: the d₂ / Korányi-Wolf-Peirce derivation fresh** (Lyra handed you the Wolf-Korányi reference: rank-1 boundary = disk IV₁, not IV₃; verify against Loos before banking k₂/k₁=20). This is the down-row repair hinge. **Checked by ELIE.**
- **LYRA works** {m_μ/m_e, m_ν2, m_ν3, δ_PMNS} — matrix-element/rep-theory. Is (24/π²)⁶ exact or floor? ν π-parity forms? δ_PMNS forced or forward? **Checked by GRACE.**
- **ELIE works** {α, sin²θ_W, m_e, m_ν scale} — scales/numerics. Wyler tighten-or-floor; θ_W terminal-or-form; m_e route; ν scale FLOOR + Σm_ν. **Checked by LYRA.**

**Stages:** (1) each worker posts the *approach* per item (mechanism route, 1–2 lines) — team cross-reviews to kill dead-ends. (2) work it. (3) the checker independently verifies + tries to improve. Hand attempts to Keeper's ledger; **no self-cert** — the tool computes the verdict, the checker is the gate.

**Disciplines armed**

- **Mechanism is the prize** — a forced derivation beats any value-form. That's what "improve" means.
- **A GUT/GUT-scale value is a MISS** (down-row). Structure-forcing, not value-reaching (137/45 form-cheap).
- **σ with scheme-aware errors**; **cheapness = coarse/tight soft-flag** (not a counted axis — search-space-relative).
- **Terminal is a finished answer** — closing a radiative-floor APPROX or a runner honestly resolves the non-match. Don't chase physics-forbidden exact forms.
- Cal #27 hardest at peak elegance · target-innocence · pin-to-primary-sources · engage-don't-label · no manufactured walls/fatigue · artifact-currency (SOD first, EOD sync).

**Keeper (me):** SOD check; score every attempt (dev% + σ scheme-aware + coarse/tight); adjudicate mechanism; keep ledger + 26-table current; hold the honest tally; never rewrite a CI's derivation. Report the EOD delta.

**Cal:** post-landing cold-read. α tier-call reserved for Casey.

**Standing for Casey** (carried, nothing finalized in absence): down-row ratification (structural-MISS-repairable), σ-metric + cheapness-flag ratification, α tier-call (Wyler-informed now), CLAUDE.md line 0.5 (SOD as first act).

**EOD target:** the non-match list shrinks — improvable items resolved (MISS→MATCH where the observed ladder forces it), terminal items closed with a stated reason. Re-run bst_26_table.py; the win is derived-strong up + non-matches resolved either way. That's coverage toward all-terminal — the loop's end condition.

— Keeper, 2026-07-03 wake. Plan → work → check, independent checker per item; mechanism the prize, terminal an honest answer; the table tells the truth at EOD.
