# C6 — the sweep-ledger quantitative backbone (Grace, Round 28, 2026-08-21)
*Cal §654 made C6 (pre-register or sweep) the load-bearing reading criterion. This is its quantitative spine (my lane): why pre-registration is load-bearing, and the ledger the derivation phase enforces. Toy 5414 (4/4). Reconnected: T830, T1932, retired (1/8)²².*

## The look-elsewhere, quantified
- **Unconstrained reading is worthless.** "Any BST-rational, denom ≤ Q, at tolerance ε" covers a fraction ≈ min(1, (3Q²/π²)·2ε) of [0,1]. At **Q=20, ε=1% → coverage ≈ 1.0**: essentially ALL of [0,1] is within 1% of some low-denominator rational. An unconstrained "match" carries **zero information**.
- **The fishing look-elsewhere = Casey's "dozen."** With N_formulas fished against N_targets, E[chance matches] = N_f·N_t·2ε = **30 × 20 × 0.02 = 12**. Each of the 12 passes per-reading "target-innocent" — the defect is the 600 uncommitted pairings, invisible per-reading.
- **Pre-registration collapses the pool to ONE forced form.** The (object, verb) pair fixes ONE expected value BEFORE the target is consulted → pool = 1 → p_chance = 2ε. E[chance] = N·2ε = **30 × 0.02 = 0.6, not 12.** ★ **C6 buys the collapse 12 → 0.6**: naming the address before the value turns 600 fishing comparisons into 30 committed predictions. THAT is why C6 is load-bearing — it is the multiple-comparisons fix, per-derivation.

## The sweep persuasiveness metric (binomial null over the WHOLE sweep)
Report (N attempted, H hit); test H vs **Binomial(N, p=2ε)**. Nulls reported ALONGSIDE hits.
- E[chance] = N·2ε. p-value = P(X ≥ H | Binom(N, 2ε)).
- Examples (ε=1%): 12/30 → p=2.5×10⁻¹³ (SIGNAL); 2/30 → p=0.12 (chance); 30/50 → p=3.4×10⁻³⁸ (SIGNAL).
- **A sweep with mostly-null results (H ≈ N·2ε) is honest evidence of NO signal; H ≫ N·2ε (tiny p-value) is FAR more persuasive than a handful of cherry-picked hits with the misses hidden.**

## The C6 LEDGER FORMAT (enforce in the derivation phase)
- **Per reading:** (object, verb, **pre-registered form**, target, ε, HIT/MISS) — **address named BEFORE the value** (the promoted headline: a method, not a check).
- **Aggregate:** (N attempted, H hit, E[chance] = N·2ε, binomial p-value) — **nulls printed alongside hits**.
- **Admissibility:** a reading counts under C6 iff it is EITHER pre-registered (one committed form) OR inside the full sweep. No cherry-picks; the ones that don't close are reported with the ones that do.

## For adoption
@Cal / @Keeper: this is the C6 ledger spec + its quantitative justification (600→30 collapse; binomial persuasiveness). @Lyra/@Elie (Lanes A/B): every derived reading logs to this ledger — a mostly-null sweep is *more* persuasive than a handful of hits, and it's affordable ONLY because the object list was declared first. **Tier:** methodology (the C6 backbone). **Edges:** T830 (10⁵⁰ look-elsewhere), T1932 (denom-density null), retired (1/8)²² (independence over-count); toy 5414.

---
## ★ SCOPE CAUTION (Cal, Round 29): C6 is for the NUMERICAL POOL, NOT cancellations.
C6 (pre-register or sweep) applies to a reading that lands a VALUE in a target's ±ε band — where a candidate POOL exists and the look-elsewhere is real. **Do NOT apply C6 to a CANCELLATION** (e.g. anomaly-freedom ΣY³=0, custodial ρ=1 by structure): there is no numerical pool being fished — the "match" is exactly zero/one BY STRUCTURE, forced by the reality-type/rep, not selected from candidates. Applying the sweep-ledger to a cancellation is **ritual compliance**, not evidence. The ledger's E[chance]=N·2ε model presumes a value drawn against a pool; a structural cancellation has no such pool. **Rule:** C6 gates numerical-value readings; structural cancellations are gated by their derivation (the FS indicator / rep forcing the zero), not by the sweep.

---
## ★ Round-30 — two new bar criteria fold into the ledger (the bar is now EIGHT)
1. **FALSE-NEIGHBOR dedup (affects the sweep COUNT).** (n+1)/n and n/(n−1) are ONE family at shifted arguments; a value appearing twice in a sweep via shifted-argument forms is **one relation, not two maps**. ⟹ the ledger must **dedupe false-neighbor families before counting H** (and before E[chance]=N·2ε) — else the hit-count and the attempt-count both inflate and the binomial p-value is corrupted. Count the family ONCE.
2. **CLASS-vs-OBJECT (affects ADMISSIBILITY).** An n-independent-within-the-class constant is a **class property**, not a reading of the object: it does not distinguish D_IV⁵ from any other D_IV^n, so it is NOT a reading of *this* object at n_C=5. (Example: the transition "ratio 2" is Derived-but-class-level — a property of the whole type-IV family, **not a BST number**.) ⟹ before a value enters the sweep as a D_IV⁵ *reading*, confirm it is **object-specific** (varies with n / depends on n_C=5); class-level constants are logged separately as class properties, not counted as object readings.
**Both are look-elsewhere hygiene:** false-neighbors inflate the numerator (double-counted hits); class-constants inflate the denominator with non-readings. The honest sweep dedupes families and excludes class-level constants.
