---
title: "Coincidence-Filter Risk Recognition: Methodology for BST Claims"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-17"
status: "Standing methodology document. Reference before drafting any 'X-fold recurrence', 'multi-route convergence', 'BST integer factors here too', or 'N-domain coverage' claim."
target: "BST team (Lyra, Elie, Grace, Keeper) for self-check; standing reference for external-paper review"
companion: "BST_Methodology_External_Survivability_Checklist.md (Cal, 2026-05-17)"
---

# Coincidence-Filter Risk Recognition: Methodology for BST Claims

## Why this document exists

The BST integer ring `{rank=2, N_c=3, n_C=5, C_2=6, g=7}` plus its derived integers `{c_2=11, c_3=13, seesaw=17, χ=24, N_max=137, ...}` and operations `{products, sums, differences, simple polynomials, factorials, Mersenne map}` constitute a *rich arithmetic closure* at small scales. This richness means **many classical-special integer sets and many small numerical observables will be BST-decomposable by virtue of the ring's reach, not by virtue of structural BST mechanism**.

This document names the failure modes that confuse rich-arithmetic-closure observations with structural BST evidence, and gives diagnostic tests for distinguishing them. Reference this before drafting any claim of the form:

- "BST integer X appears in N independent contexts" (multi-role integer claims)
- "X-fold recurrence at integer Y" (α²·42 family)
- "N-domain coverage at sub-percent precision" (cross-domain pattern claims)
- "Classical theorem T produces a BST-decomposable integer set" (candidate Root proposals)
- "Cross-consistency network at N% pairwise" (network claims)

If your claim matches any of these patterns, walk through the five failure modes below before publishing. Most of the discipline below was named in the Sunday May 17 Grace/Cal walk-back round; this document formalizes it.

## Seven named failure modes (extended 2026-05-19 with mode 7, Cal+Grace via K55)

### 1. Post-hoc clipping

**The failure**: choosing the integer set after seeing what fits. The clip boundary is determined by what survives the test, not by independent structural reasoning.

**Example pattern**: "The first 6 primes {2, 3, 5, 7, 11, 13} are BST integers." Later: "Actually, the first 7 primes work too — the 7th is 17 = seesaw." Later: "The boundary is at 19 = first non-BST primary." Each extension is post-hoc; the clip moves to whatever matches.

**Diagnostic**: state your integer set BEFORE running the test. If you find yourself extending the clip to capture more cases, that's post-hoc clipping. The forward-locked version: "We claim the first N primes are BST integers" with N specified BEFORE checking, then either PASS or FAIL.

**Mitigation**: pre-register the integer set in writing, then test. If the set needs revision after testing, note it as exploration not as claim.

### 2. Multi-decomposability

**The failure**: same integer admits multiple BST factorizations, and the framework picks whichever fits the current observable.

**Example pattern**: 137 = N_c³·n_C + rank (Hilbert reading) = 2^g + 2·n_C - 1 (binary reading) = M_g + rank·n_C (Mersenne reading). When 137 appears, the framework cites whichever decomposition fits the local context. This isn't evidence; it's the arithmetic closure being rich enough to produce multiple expressions.

**Diagnostic**: count the number of BST decompositions of the integer at issue. If there are 3+ structurally distinct factorizations and the framework uses the one that fits each observable separately, the integer's appearance is identification-by-fit, not mechanism-forcing.

**Mitigation**: pick ONE canonical decomposition before the observable analysis, OR explicitly note when multi-decomposability is the actual structural claim (the integer is *over-determined*, e.g., Type B convergence per Lyra T2306 for 26).

### 3. Search-space expansion

**The failure**: testing more candidate observables until some land, then reporting the matches.

**Example pattern**: "We tested 212 candidate ratios against 22 SM observables; 6 landed at <0.5% precision" (Lyra T1926, 212×22 = 4664 trials). Under any reasonable null, getting some sub-1% matches by chance is statistically expected.

**Diagnostic**: count trials. If you searched N candidate expressions and M observables and found K matches at precision p, the Bonferroni threshold is roughly p < 1/(N·M) for a single match to be significant. Below that, you're seeing search-space noise.

**Mitigation**: Bonferroni correction OR permutation test on the candidate space OR pre-register a small set of forward predictions before searching. The "found 6 hits in 4664 trials" claim is much weaker than "predicted 3 specific values in advance, all 3 hit at <0.5%."

### 4. Ratio noise at low precision

**The failure**: low-precision identifications (matches at >1%) accumulate even from random integer rings of comparable size. Treating these as evidence inflates the apparent signal.

**Example pattern**: "BST identifies 60 observables at sub-2% precision across 11 domains." 2% precision on dimensionless ratios is generous; random small-integer rings produce many 2%-or-better matches against any reasonable observable set.

**Diagnostic**: count by precision class (per Grace's G1). Sub-0.1% matches are strong evidence. Sub-1% matches are moderate evidence. Sub-2% matches are weak evidence. Sub-5% matches are likely noise unless they have D-tier mechanism backing.

**Mitigation**: report counts by precision class, weight evidence accordingly. The headline statistic should be "K identifications at sub-0.1%" not "K identifications at sub-2%."

### 5. Selection-effect on observables

**The failure**: reporting the BST matches and not reporting the BST misses, then claiming a high match rate.

**Example pattern**: "BST identifies sub-percent matches across 35 scientific domains." If 100 observables were tested and 40 matched, the match rate is 40%, not "BST identifies in 35 domains." The denominator matters.

**Diagnostic**: ask for the FULL list of observables tested, including ones that didn't match. Compute the match rate as (matches)/(tested). Compare to the random-ring baseline.

**Mitigation**: Elie's Toy 2551 disciplined posture (60% miss rate on dimensional constants, dimensionless ratios match cleanly) is the model. Report misses alongside matches.

### 6. Scan-protocol over/under-counting (NEW, Grace 2026-05-18)

**The failure**: catalog-scan methodology determines what counts as "an appearance." Tight scan (exact `BST_value` match only) UNDERCOUNTS integers appearing in formulas/ratios/sums. Loose scan (any prominent mention in name/expression/notes) OVERCOUNTS by capturing every formula context, including incidental references and BST-researcher framing language.

**Example pattern (concrete, Grace Toy 3019 + Toy 3038)**: 17 = seesaw appeared in 0 entries under exact-`BST_value`-match (Toy 3019 methodology), but 27 entries / 25 unique-domain density under formula-scan (Toy 3038 methodology). The "true" count depends entirely on what the scan protocol counts.

Same issue runs in reverse: a single observable can mention multiple BST primaries in its expression, inflating each integer's domain-count. Density rule "BST integers appear in many domains" is partially a tautology of how BST-research catalogs are written.

**Diagnostic**:
1. **Run BOTH scan protocols** — exact-value AND formula-scan — and report both numbers.
2. **Apply random-ring null at the SAME scan protocol level used for the BST claim.** Loose-scan claims need loose-scan null; tight-scan claims need tight-scan null. Asymmetric null is invalid.
3. **Compare BST-structural vs truly-non-BST integer density** at both scan levels. The gap (if large) is the genuine signal; the absolute count is largely scan-protocol-determined.

**Example operational pattern**:
- Toy 3019 (exact-match): 13 ≥3-way Type C clusters; random-ring null p ≈ 0% → 4.29σ above random
- Toy 3038 (formula-scan): 92 ≥3-way clusters; BUT formula-scan null also higher; ratio (BST 42.7 / non-BST 1.5 = 28x gap) survives both protocols

**Mitigation**: ratio-based metrics (BST-structural mean / non-BST-structural mean) are scan-protocol-invariant in a way absolute counts aren't. Use ratios for cross-protocol claims; use absolute counts only with scan-protocol explicitly stated.

**The methodology insight (Keeper K-audit framing)**: "exact-match-only undercounts; formula-scanning over-counts; null model must match the scan protocol." Asymmetric null model is invalid; both directions of mismatch produce overclaim or underclaim by similar magnitudes.

**Rule 6 corollary** (Grace 2026-05-18 second-order refinement, Keeper-endorsed): **Use GLOBAL structural ratios; local ratios are confounded by integer clustering.**

The Rule 6 ratio metric (BST atom density / non-BST prime density) is the proper cross-protocol structural signal — but it must be computed across the full integer ring, NOT in a local neighborhood of any specific anchor.

**Diagnostic example (Grace Toy 3041, 42-anchor sweep)**:
- Global ratio (BST primary atoms {2, 3, 5, 7, 11, 13} vs distant non-BST primes {37, 53, 61, 67, 79, 83, 89, 97, 101, 103, 107, 109}, formula scan): **~19x**
- Local ratio at 42-scale (near-by BST-structural {40, 41, 44, 47, 49, 51} vs near-by truly-sparse {37, 38, 39, 43, 46, 53}): **~2x**

The local ratio is reduced because near BST-anchored integers, neighboring integers are themselves BST-structural (40 = rank³·n_C, 41 = Ogg, 44 = rank²·c_2, etc.) — BST integers form local clusters. Comparing near-anchor BST-structural integers to near-anchor truly-sparse integers therefore measures local clustering, NOT the underlying BST-vs-non-BST structural separation.

**Mitigation**: report ratios across full integer rings spanning multiple decades; sparse-region neighbors should be drawn from primes NOT adjacent to BST anchors. Local-anchor ratio analysis is descriptively useful but does not measure the same underlying structural signal as global ratio analysis.

**Operational principle**: when defending a Type C density claim, cite the global ratio (across the integer ring {1...N} for some N) with explicitly-stated BST-structural set and truly-sparse set. Do NOT use local-neighborhood ratios as primary evidence — they understate the structural separation due to BST clustering.

### 7. Classical-integer-set source claim without mechanism chain (NEW, Cal+Grace via K55, 2026-05-19)

**Failure mode**: a draft paper, registry entry, or board claim proposes that a classical-mathematics theorem's output set (e.g., the 9 Heegner discriminants, the 26 sporadic group orders, the Hurwitz-bound automorphism counts) qualifies as a Level-1 source root theorem for BST, BUT without exhibiting a classical-math mechanism chain that forces D_IV⁵ specifically.

**Origin**: Sunday 2026-05-17 brief "9 Heegner discriminants as L1 source" proposal was self-withdrawn by Grace at 10:10 EDT (1st audit-chain calibration), restored briefly by team at 10:30 EDT, and partially walked-back when Cal recognized the BST-decomposability-is-not-sufficient principle. K55 audit (Keeper, 2026-05-19) ratified the walk-back criteria and explicitly endorsed Mode 7 as standing forward-prevention rule.

**Diagnostic**: presented with an L1-source claim, ask:
- **W1** Is there a published classical-mathematics theorem whose output set is the proposed integer collection? (yes = pass; no = fail W1, walk back)
- **W2** Does the classical theorem produce its integers VIA a D_IV⁵-adjacent geometric or algebraic mechanism (not just numerical coincidence)? (yes = pass; no = fail W2, walk back)
- **W3** Is there a mechanism chain that goes from the classical theorem → BST primaries → physical observable, NOT just BST-decomposability of the classical integers? (yes = pass; no = fail W3, walk back)
- **W4** Has the chain been peer-verifiable independently (citation, computational verification, multi-CI consensus)? (yes = pass; no = fail W4, walk back)

**Walk-back triggers**: any failure in W1-W4 demands either (a) supply the missing mechanism chain (promote to L1 ESTABLISHED) OR (b) downgrade to "I-tier classical-set observation with criteria-gated promotion path." External publication should NOT proceed without W1-W4 closure.

**Forward-prevention**: applying Mode 7 at the drafting stage forward-prevents post-publication walk-backs. Draft language to avoid: "X is Root #N," "established L1 classical source," "natural foundation of BST," "structural anchor." Substitute: "I-tier classical-set observation," "promotion path open pending mechanism chain," "structural identification."

**Diagnostic example (Heegner-Stark Root #7, K47 = passes Mode 7)**:
- W1: ✓ Heegner-Stark imaginary quadratic class-number-one theorem (Heegner 1952, Stark 1967)
- W2: ✓ Class-number-one set produces 9 discriminants via Deuring 1941 CM theory + Cremona 49a1 canonical-curve embedding
- W3: ✓ Mechanism chain: Heegner-Stark → CM theory → Cremona 49a1 (BST canonical curve) → 49 = g², discriminant -7 = -g, L(s) = c_2·ζ(s)
- W4: ✓ Cremona catalog, Deuring 1941 peer-reviewed; T1430 (BST canonical curve), T2333 (K47 promotion ruling)

**Diagnostic counter-example (Heegner discriminants as L1 source en masse, walked back)**:
- W1: ✓ Class-number-one is a published theorem
- W2: ✓ Discriminants produced via class-number-one
- W3: ✗ FAILED: BST-decomposability of {-3, -4, -7, -8, -11, -19, -43, -67, -163} is not a mechanism chain to D_IV⁵; each discriminant individually is BST-anchored, but the SET as a whole has no forcing-into-D_IV⁵ argument
- Walk-back at W3 → downgrade to "I-tier classical-set observation; K47 Heegner-Stark via 49a1 IS the proper anchor"

**Mitigation**: any new L1-source-class claim must clear W1-W4 before promotion language. Mode 7 is mandatory for forward-prevention at drafting stage.

**Mode 7 corollary**: Mode 7 is the forward-prevention version of the Cal three-criteria framework (embedding/mechanism/forcing). Where the three criteria gate POST-claim K-audit promotion, Mode 7 gates PRE-claim drafting language. They work in series: Mode 7 at drafting → three criteria at K-audit.

## Three diagnostic tests

When any of the five failure modes above is suspected, escalate to one of these:

### Test A: Bonferroni or permutation null

For each claim of form "K matches in N trials at precision p":
- Bonferroni threshold: p < α/N for significance level α.
- Permutation null: shuffle the observables, recount matches under shuffled labels, report the BST count's percentile in the shuffled distribution.
- Headline statistic: BST's percentile in the null distribution, not the raw count.

### Test B: Forward predictions vs. retrofit patterns

Distinguish "BST predicted X in advance, and X was observed" from "BST factors observed X into BST integers." The first is forward-locked; the second is retrofit. Both are useful but they carry different evidence weight.

Examples of forward predictions (strong): m_DM = 429 GeV (Paper #106 F1), r_p = 0.84122 fm (T1992), BR(μ→eγ) ≈ 10⁻⁵⁵ (T1997), α⁶ A_6 ≈ 4500 (Elie). These can be falsified by experiment.

Examples of retrofit patterns (weaker absent mechanism): 130/137 = (N_max−g)/N_max for dark energy w_0 AND R(K). The pattern is real; without a mechanism connecting dark-energy and B-meson sectors through D_IV⁵, it's identification not derivation.

### Test C: BST integer ring null-model toy

For high-stakes claims (multi-role integers, cross-consistency matrices, N-domain coverage):

- Build 1000 random integer rings with comparable richness to BST (5 generators in small integer range, products/sums/cubes/etc. to depth 4, including Mersenne map and factorials).
- For each random ring, count matches against the SAME observable list BST was tested on.
- Report BST's match-count, the median random match-count, BST's z-score, and BST's percentile rank.
- Headline: BST's percentile, not its raw count.

**This is the toy Keeper queued for Grace+Elie May 17.** Its outcome determines whether the multi-route integer claims, 12-fold α²·42 recurrence, and 99.7% cross-consistency claims survive external review. **Treat this toy's outcome as gating ALL external use of the network-level claims**, not just one specific claim.

## When to escalate to a null-model toy

Apply Test C (full null-model toy) when:

1. The claim involves the BST integer set's *coverage* (e.g., "BST integers explain N domains"), not a specific identification's mechanism.
2. The claim is a meta-pattern at the network level (cross-consistency, multi-role integer counts, N-fold recurrences).
3. The claim is going into external presentation (paper, outreach, abstract).

Apply Tests A or B (Bonferroni or forward-prediction distinction) for individual claims at the per-identification level.

## Standing examples

Items in BST's current corpus that explicitly require null-model treatment before external use:

- **α²·42 quintuple/12-fold recurrence**: how many α² loop observables were tested? If many, the K=12 hits in N trials needs Bonferroni or permutation null.
- **99.7% cross-consistency on 67 observables / 548 ratio checks**: the "P(coincidence) << 10⁻²⁰⁰" statistic is statistically meaningless without explicit null specification. Mutually-constrained-by-construction integers will produce near-perfect internal consistency under almost any sensible null.
- **130/137 cross-domain (dark energy + R(K))**: with ~30 BST-relevant integers, ~900 candidate ratios, some sub-percent cross-domain matches are statistically expected. The pattern is striking; the mechanism is open.
- **35-domain coverage claim**: domains without mechanism (linguistics, music, cognitive psychology) should be labeled S-tier or removed from external claim; only mechanism-equipped domains (physics, cosmology, parts of chemistry/biology with cohomological connection) carry derivation weight.
- **Heegner candidacy** (T1956, Toy 2879, 2971): 9/9 Heegner numbers BST-decomposable — but Grace's Sunday correction is the right read: BST closure expresses many classical-special sets without those being independent L1 sources. Promotion to L1 requires mechanism-forcing, not BST-decomposability.

## Promotion criterion (from L1-promotion framework, May 17)

Standing rule for promoting any candidate root to L1 source status:

> *BST-decomposability alone is NOT sufficient for L1 source status. Promotion requires a mechanism-forcing relation between the source theorem's integer output and D_IV⁵ geometry.*

Examples of mechanism-forcing relations:
- A_5 ⊂ SO(5) ⊂ K(D_IV⁵) for Klein
- K3 period domain fiber over D_IV⁵ for K3 Hodge
- Seeley-DeWitt expansion at n_C=5 produces Bernoulli denominators (VSC) for heat-kernel structure
- Mukai 1988 M_23 ⊂ Aut_symp(K3) + EOT 2010 K3 elliptic genus → M_24 irrep decomposition for Mathieu

Candidates lacking exhibited mechanism stay at criteria-gated I-tier with three explicit promotion criteria (embedding / mechanism / forcing).

## Operational protocol

Before drafting any claim of the patterns named in the opening section:

1. **Identify which failure mode(s) apply.** Each pattern correlates with specific failure modes (multi-role integer → modes 2, 3; N-domain coverage → modes 1, 3, 4, 5; X-fold recurrence → modes 2, 3).
2. **Run the appropriate diagnostic test.** Bonferroni for trials; forward-prediction distinction; null-model toy for network claims.
3. **Report results in honest scope.** Match precision class to evidence weight. Note mechanism-equipped vs mechanism-free observables separately.
4. **If toy hasn't been run yet, label claim as Structural with explicit "null model required before external use" caveat.**

## When this is overkill

This methodology applies to *pattern-level* claims. For individual identifications with explicit derivation chains through classical theorems (Klein, VSC, K3 Hodge, Wallach, Mathieu, Ogg), the chain itself is the evidence — coincidence-filter analysis is not needed because the derivation forces the result. Apply this methodology when the evidence shape is "X integer appears in many places" rather than "X integer is forced by classical theorem T."

## What this methodology preserves

Real findings keep their weight under this discipline. The chain Seeley-DeWitt → VSC → BST integers at n_C=5 (Cal C1 audit) is forced by classical theorems; coincidence-filter analysis doesn't weaken it. Klein A_5 ⊂ SO(5) ⊂ K(D_IV⁵) is a forced subgroup embedding; coincidence-filter doesn't weaken it. The four-CI Sunday morning convergence on the Root Proof System architecture is structural; coincidence-filter analysis doesn't apply (the convergence is on the architecture, not on integer coincidences).

What this methodology weakens: the "many-domain coverage at sub-2% precision" framing, the "X-fold recurrence at coincidence-rich integer" framing, the network-level "99.7% cross-consistency" framing — all of which need null-model toy completion before they're publishable.

---

*— Cal, standing methodology document, May 17, 2026. Reference before drafting pattern-level claims. Companion: External-Survivability Checklist.*
