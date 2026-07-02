CI Board — PASS 1, PARALLEL. The 26 partitioned across the CIs. (Casey directive 2026-07-02)

STOP converging on one item. Each CI owns a bucket and works ALL of it this pass — no one waits on the d₂/down-row bottleneck. Goal: **coverage** — every one of the 26 gets at least one scored derivation attempt this pass. We want to see how many close.

**The three steps, per CI, for every item in your bucket:**
1. **Scan the corpus** for the existing best closed form (K-audits, theorems, toys, ledgers). Fill it into the derivation ledger.
2. **Fill the ledger** — `play/bst_derivation_ledger.py`, one attempt entry per form: `{form, value, how-it-derives-from-substrate, provenance}`. Never delete a tried form (so we don't repeat).
3. **Attempt an independent derivation** from the substrate {rank=2, N_c=3, n_C=5, C_2=6, g=7, N_max=137}. Add it as a new attempt. Not fishing — examining the substrate for a forced derivation of the SM value.

Then hand your filled bucket to Keeper, who σ-scores it and adjudicates the mechanism. **You do NOT self-certify** — the ledger computes MATCH/APPROX/MISS.

## The partition (26 items, 3 buckets)

### LYRA — the MIXING sector (8): CKM + PMNS angles & phases
- CKM: θ₁₂ (Cabibbo, 9/40 — MATCH 0.6σ), θ₁₃ (V_ub (1/3)⁵ — MISS), θ₂₃ (V_cb dual-ρ), δ_CKM (Jarlskog)
- PMNS: θ₁₂ (5/16 or 3/10), θ₁₃ (1/45 — MATCH 0.5σ, banked), θ₂₃ (upper octant), δ_PMNS (OPEN — no form yet)
- Your lane: rep-theory of mixing. Pin CKM refs (pdgLive HTML — you have web access; Cal #22 transcription discipline). δ_PMNS is your one blank — attempt a form.

### GRACE — the MASS sector (9): all charged fermion masses
- Leptons: m_e (anchor/gravity route), m_μ ((24/π²)⁶ — APPROX), m_τ (49·71 — APPROX)
- Up-type: m_u (up-ladder, honest-neg), m_c (scheme-trap, honest-neg), m_t (v/√2 — MATCH scheme-aware)
- Down-type: m_d, m_s, m_b (down-row GJ — MISS, repairable via F453 at observed ladder)
- Your lane: masses via strata/geometry. The down-row d₂ is IN here but is ONE of nine — do NOT let it eat the pass. Cover m_u, m_c, m_e first-pass too. (Lyra handed you the KW boundary reference — verify fresh against Loos before banking k₂/k₁=20.)

### ELIE — the SCALES + GAUGE + θ_QCD + NEUTRINOS (9)
- Gauge: α (1/137 flat & Wyler closed form — pin both), α_s (RG-runner → terminal-NEG), sin²θ_W (RG-runner → terminal-NEG)
- Higgs: v (pure scale → terminal-FLOOR), m_H (λ_H form — OPEN, attempt)
- Strong CP: θ_QCD (0 — MATCH, exact, DONE)
- Neutrinos: m_ν₁, m_ν₂, m_ν₃ (OPEN — absolute scale is FLOOR; the m₃/m₁ π-free falsifier is your form to score)
- Your lane: numerics + scales. Confirm the 3 terminal-NEG + 1 FLOOR fast (honest coverage), pin α's Wyler form exactly, attempt m_H and the ν structure.

## Scoring (Keeper owns, computed — not declared)

Every attempt scored on BOTH: **dev% AND σ = |Δ|/experimental-error** (K643). Use **scheme-aware errors** for quark masses (m_t reads 4.7σ on the tight pole error but 0.7σ scheme-aware — the error must reflect scheme ambiguity or the metric manufactures misses). Verdict: MATCH (σ≤2) / APPROX (σ>2, dev<1%) / MISS. `tol` flag = dev ≤0.1%.

## Rules for this pass

- **Cover your whole bucket** before deep-diving any single item. First pass = at least one scored attempt on all 26.
- **A GUT/GUT-scale value is a MISS** even with a clean mechanism (down-row). Five-Absence first — Elie's flag: watch the 27=E₆ and 45=SU(5)-45 coincidences.
- **Structure-forcing, not value-reaching.** Don't fish a form to hit a number (137 is form-cheap). Record the substrate derivation, not just the value.
- **PDG re-pin your bucket's references** (value AND scheme-aware error) as step 0 — the scoreboard's reference can't be unverified.
- **Fresh reference work over rushed** — Grace's KW pin, Elie's CKM pin: do them carefully, cite primary source, don't wing (genus-flip / Cal #22).

## Keeper (me) — loop-keeper, not a deriver

Run SOD check first; keep the derivation ledger; σ-score + mechanism-adjudicate each CI's filled bucket; hold the honest tally; never rewrite a CI's derivation, only score it.

## Cal — post-landing cold-read. α tier-call reserved for Casey.

## Pass-1 target

Every one of the 26 with ≥1 scored attempt. Report the honest tally: MATCH / APPROX / MISS / OPEN. Today's seed (11 of 26): 4 MATCH + 4 APPROX + 3 MISS. Pass 1 fills the other 15 and improves the APPROX/MISS toward MATCH. Then Pass 2 sweeps again — improve forms, add attempts — until the board is all-terminal and Casey calls done.

— Keeper, Pass 1 parallel. Three buckets, three steps each (scan → fill → derive), coverage over depth this pass. Nobody locked on the down-row. Hand filled buckets to Keeper; the ledger computes the verdict.
