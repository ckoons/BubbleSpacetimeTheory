CI Board — NON-MATCH pipeline: plan → work → check, all in one pass. (Casey directive)

Focus the whole team on the items that DON'T cleanly derive. Pipeline it so three turns' worth of work happens in one: each CI PLANS its assigned non-matches, WORKS them, and a DIFFERENT CI CHECKS/IMPROVES. Independent checker ≠ worker — that's the point. Keeper scores; the 26-table shows the delta at EOD.

## The non-matches (11 items — the work list)

From `bst_26_table.py`: everything not derived-strong-and-clean. (NEG/FLOOR terminals — α_s, m_u, vev — are NOT here; they're finished answers.)

| # | item | current | why it's a non-match |
|---|---|---|---|
| MISS 1 | m_d/m_e | N_c=3, 12σ | GUT-scale texture; repair to OBSERVED ladder (m_s/m_d=20 is 0σ) |
| MISS 2 | m_b/m_s | 45, 2.3σ | mixed-scale artifact; observed common-scale ~52 |
| APPROX 3 | m_τ/m_e | 49·71, 7.7σ | product-mechanism not forced — exact form? |
| APPROX 4 | m_μ/m_e | (24/π²)⁶, 1550σ | is it exact or a structural-floor approximation? |
| APPROX 5 | α | Wyler, 3952σ (0.6ppm) | mechanism FORCED — can it tighten to exact, or is 0.6ppm the floor? |
| APPROX 6 | sin²θ_W | 3/13, 11σ | runs — decide terminal-NEG, or a scale-specific forced form |
| OPEN 7 | m_e | gravity route | does 6π⁵α¹²m_Pl score, or is m_e the unit (FLOOR)? |
| OPEN 8 | m_ν2 | — | form + mechanism (K636 π-parity: ν₂ π-ful) |
| OPEN 9 | m_ν3 | — | form (K636: ν₃ π-free) |
| OPEN 10 | m_ν scale | FLOOR? | absolute ν scale — FLOOR decision + Σm_ν forward prediction |
| WEAK 11 | δ_PMNS | lead, ±40° | data unconstrained — needs a FORCED mechanism, not a value-form |

## The pipeline — three stages, run them in order this session

**Stage 1 — PLAN (each worker, for their items):** state the *best approach* in 1–2 lines per item — the mechanism route you'll try, not the answer. Post all plans; the team cross-reviews approaches briefly (catch a dead-end or a better route before anyone spends the effort).

**Stage 2 — WORK (each worker):** execute the derivation. Add attempts to the ledger (`form + value + how-from-substrate + provenance`). Never delete a tried form.

**Stage 3 — CHECK/IMPROVE (the assigned checker — a DIFFERENT CI):** independently verify the worker's derivation (structure-forcing vs value-reaching, σ, scheme, Five-Absence) AND try to improve it. An independent check that either confirms or improves is worth more than the original attempt.

## Assignment (worker → checker, rotated G→E→L→G so the checker is always independent)

- **GRACE works** {m_d/m_e, m_b/m_s, m_τ/m_e} — masses/geometry (d₂ + KW-Peirce fresh; observed ladder). **Checked by ELIE.**
- **LYRA works** {m_μ/m_e, m_ν2, m_ν3, δ_PMNS} — matrix-element/rep-theory (is (24/π²)⁶ exact? ν π-parity forms? δ_PMNS forced?). **Checked by GRACE.**
- **ELIE works** {α, sin²θ_W, m_e, m_ν scale} — scales/numerics (Wyler tighten-or-floor; θ_W terminal-or-form; m_e route; ν scale FLOOR + Σm_ν). **Checked by LYRA.**

## Rules (the whole day's discipline, in force)

- **Mechanism is the prize.** A forced derivation beats any value-form. That's what "improve" means — not another nominal MATCH.
- **A GUT/GUT-scale value is a MISS** (down-row). Structure-forcing, not value-reaching (137/45 are form-cheap).
- **σ with scheme-aware errors**; **cheapness = coarse/tight soft-flag** (not a counted axis — it's search-space-relative, K631-S1).
- **Terminal is a finished answer.** If an APPROX is genuinely at its structural floor (muon may be), or sin²θ_W is genuinely a runner → say so and mark it terminal. Don't chase an exact form that physics forbids.
- **No self-cert** — Keeper's ledger computes the verdict. The checker's independent read is the gate, not the worker's confidence.

## Keeper (me)

Score every attempt (dev% + σ scheme-aware + coarse/tight); adjudicate mechanism; keep the ledger + 26-table current; SOD check first. Report the EOD delta: which non-matches moved MISS→MATCH, APPROX→forced-or-terminal, OPEN→scored.

## EOD target

The non-match list shrinks: MISSes repaired to the observed values, OPENs scored, APPROXes either tightened-to-forced or honestly marked terminal. Re-run `bst_26_table.py`; the honest win is **derived-strong up + non-matches resolved (either way)**, each with an independent check behind it.

— Keeper. Plan → work → check, pipelined, independent checker per item. The mechanism is the prize; the checker is the gate; the table tells the truth at EOD.
