# BST RUBRICS — how we know when work is done and how honest it is

**DRAFT v0.1 — Keeper (player-manager, scout-tier framing), 2026-08-08. For Casey to shape + Cal to vet before it becomes the standard.**

Two layers. **Layer 1** appraises the THEORY (what we show Tegmark/the world — the honest self-assessment). **Layer 2** appraises each INVESTIGATION (the practical corpus tool — "is this piece well documented"). Plus a coverage-audit template to catch what we shortchanged.

---

## LAYER 1 — The Theory Appraisal Rubric (Tegmark-facing)
*The ChatGPT 5-item was a domain-coverage list (it's now criterion C6 alone). These eight are the criteria a serious appraiser applies to a FUNDAMENTAL theory — Kuhn's virtues + Popper + the modern reproducibility/boundary criteria. Score each by tier, honestly. The PATTERN (which are strong, which open) is itself the credibility signal.*

**RULE (Cal vet, ratified): every score is a LINK to the artifact that earns it, never a self-adjective. A hostile appraiser discounts "Strong" on sight — the rubric's own thesis (a crank scores everything high) applies to the rubric itself.** So the right column below is a pointer + an honest tier, not a word.

**C3 is not a peer of the others — it's the existential make-or-break.** If the geometry isn't forced, BST is a very good fit, not a theory of everything. Flag it as the load-bearing criterion, not one of eight.

| # | Criterion | What "earns it" (the LINK, not a word) | BST honest state |
|---|---|---|---|
| **C1** | **Empirical adequacy** | the count that SURVIVES scrutiny: predictions that are σ-match AND target-innocent AND mechanism-forced (~5 of the 26 Cal-scored) — NOT "600+" (raw count = match-cheapness at theory scale; context, not headline) | ~5 hard + a broad Identified tail |
| **C2** | **Parsimony** | the explicit input count | 5 integers, 0 fitted dimensionless |
| **C3** ★ | **Forcing / uniqueness (EXISTENTIAL)** | the Paper B pincer + the commit-cycle forcing | **Frontier, open — THE make-or-break, not a peer criterion** |
| **C4** | **Internal consistency** | Keeper endgame tier-audit PASS | **Currently our WEAKEST axis** (yesterday's sweeps: over-claims + over-demotions found) — in active repair, NOT "strong" |
| **C5** | **Falsifiability** | the pre-registered kill conditions | Five Absences + DUNE octant + sin²θ₁₃ falsifier |
| **C6** | **Scope / coverage** | the coverage-audit table (below) | broad-at-Identified — **double-edged: coverage without forcing (C3) reads as fitting; pair them** |
| **C7** | **Reproducibility** | `verify_bst.py`, the toys, Zenodo DOI | one-command public verify |
| **C8** | **Honest boundary** | ROADMAP §9 Known-Unknowns | building |
| **C9** ★ | **Confirmed NOVEL prediction (vs postdiction)** — *added per Cal; the hostile reviewer's FIRST reach* | which BST claims are genuine FORWARD bets vs matches to already-known constants | **honest answer: the Five Absences, DUNE octant, sin²θ₁₃ falsifier are the forward bets; most of the rest is postdiction — name it before Tegmark does** |

**The pitch is the pattern, not the total** — but two disciplines make the pattern honest (Cal): (a) **"Derived-ish / consolidate / verify" is NOT a tier** — it's "claimed Derived, not yet audited," and every such row is a potential sin²θ_W; none walks into the Tegmark checklist as Derived until read at the source (C4). (b) **C3 (forcing) and C9 (novelty) are the two a hostile appraiser reaches for first** — lead with our honest answer to both, don't let them be discovered. §8's commit-cycle unification is an elegant *hypothesis* — it stays OUT of the front paper until forced.

---

## LAYER 2 — Per-Investigation "Definition of Done"
*Different TYPES have different done-bars. An investigation is DONE only when every box for its type is checked. This is what tells us the corpus is accurate enough to mine, narrate, and extract.*

**DERIVATION** (a claim that something is forced)
- [ ] Precise statement (what, in one sentence)
- [ ] Forcing chain audited (each step: proved edge / named input / open)
- [ ] Tier assigned (Derived / Partially-Derived-explicit-split / Identified / Structural)
- [ ] Target-innocent (integers not nearest-to-target; no free constant smuggled)
- [ ] Toy verifies (computational check, SCORE line)
- [ ] Cataloged (constants.json / registry, pointer correct)
- [ ] Keeper consistency PASS (no contradiction; monotone with inputs) — **audited by someone other than the author if the author is Keeper**
- [ ] No over-claim AND no over-demotion (calibrated both directions)

**PREDICTION** (a falsifiable forward claim)
- [ ] Pre-registered (stated before the check, or clearly marked postdiction)
- [ ] Kill condition explicit (what result refutes it)
- [ ] Current experimental number verified (not remembered — scrubbed for staleness)
- [ ] Region-matched σ / honest error

**FRAMEWORK / MECHANISM** (a credible-but-not-closed picture)
- [ ] Mechanism stated concretely (operators, not narrative)
- [ ] Open edges named precisely (the one/two things a referee would demand)
- [ ] Tier = Framework-honest (not sold as Derived)

**CONCEPTUAL / PHILOSOPHICAL** (e.g. "why commitment")
- [ ] Candidate mechanisms cataloged (from existing theory + corpus)
- [ ] Each tiered (derivable / framework / out-of-scope)
- [ ] Boundary marked (where physics ends, interpretation begins)
- [ ] Explicitly separated from the physics claim (never leaks into external as derived)

**PAPER / BOOK** (an extracted artifact)
- [ ] Narrative both ways (bright-high-schooler AND referee)
- [ ] Every claim carries its tier explicitly
- [ ] Reproducible (links to toys / data / verify command)
- [ ] Cal cold-read PASS (hostile review)
- [ ] Keeper consistency PASS (matches the knowledge base; no drift)
- [ ] Known-boundary section present (names what it does NOT claim)

---

## THE COVERAGE AUDIT (catch what we shortchanged — feeds C6)
*Walk the canonical domains once; tier BST's coverage of each; flag the thin spots. This is how "we may have missed important areas" becomes a finding, not a surprise a referee delivers.*

| Domain | BST coverage tier | Thin? |
|---|---|---|
| QM foundations / measurement | Derived 10/10 | no |
| SM gauge sector | Derived-ish | verify |
| SM fermion masses/mixings | Identified/PD | frontier |
| Gauge couplings (α, α_s, sin²θ_W) | mixed | #85 live |
| Gravity / Einstein / G | Framework | consolidate |
| Lorentz / spacetime emergence | Structure-Derived + 1 edge | strong |
| Cosmological constant Λ | Structural | known gap |
| Dark matter / dark energy | Identified / in-flight | verify |
| Inflation / CMB | Identified | verify |
| Baryon asymmetry | **COVERED — Identified** (η = 2α⁴/(3π), 1.4%) — NOT a gap (reconnect 8/8; verify mechanism-vs-fit) | no |
| Nuclear / atomic / chemistry | Identified-ish | breadth claim |
| Strong-force confinement | Schur (A), not area-law (B) | **named gap (real)** |
| Thermodynamics / arrow of time | **COVERED — Framework** (arrow = long-root; heat-death=graduation) | no |
| Black-hole entropy / info | **COVERED — Framework/Identified** (Bekenstein ¼, interior, Kerr, early-BH) — more than a lead | no |

**Coverage-audit finding (Keeper, 2026-08-08, scout):** BST's DOMAIN coverage is BROADER than my roadmap-draft estimate — nearly every canonical domain has a paper at Identified/Framework (my "likely gap" flags on baryon-asymmetry/thermo/black-holes were the Rule-20 under-crediting error again; reconnect corrected them up). **The genuine soft spots are not missing DOMAINS but specific TECHNICAL EDGES:** (1) quantum-gravity UV-completeness / induced-G cutoff sensitivity (K1208); (2) area-law confinement (B) — we have Schur (A) only; (3) the forcing of the geometry (the deep edge, #79); (4) the Koons-tick scale α^36 (numerology-flavored, K1208); (5) the unread higher heat-kernel rungs (a_3, a_4). **Honest Tegmark position: "we cover the domains; here are the ~5 specific technical edges that are open."** That's stronger than a domain-gap list. CAVEAT (calibrate both directions): "covered" ≠ "closed" — each domain's tier still needs the mechanism-vs-fit verification (View-1 accuracy work); broad coverage, tiers to confirm.

*Fill + tier each honestly. The thin/gap rows go into ROADMAP §9 (Known-Unknowns) and get a named owner or an honest "out of scope."*

---

*— Keeper, RUBRICS.md v0.1 (scout-tier). Cal vets the criteria; specialists apply the done-bars; Casey shapes. The rubrics ARE the hyphen-machine: Layer 1 proves we're left of it, Layer 2 makes sure nothing's half-written when we say done.*
