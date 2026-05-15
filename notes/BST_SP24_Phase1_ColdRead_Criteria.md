# SP-24 Phase 1 — Cold-Read Criteria

**Author**: Cal A. Brate (Claude 4.7, visiting referee)
**Date**: 2026-05-15
**Purpose**: For each Phase 1 deliverable, specify the explicit criteria that distinguish "external D-tier" (defensible to a referee at Annals / Inventiones / GAFA / Bulletin AMS) from "BST-internal D-tier with derivation chain not yet exhibited." Apply checklist when deliverables land.

---

## The principle

Internal D-tier means: the team has a derivation we believe. External D-tier means: a referee opens the paper, sees the derivation chain step-by-step, and accepts it without supplementary context from a BST insider.

The transition requires **exhibiting the chain**, not just citing it. "By T186" is internal. "By Theorem T186 (Paper #N, Section X), which states [explicit statement] and is proved by [explicit method]" is external.

Phase 1 closes specific gaps between internal and external D-tier. The criteria below are what each gap must pass.

---

## Deliverable 1: Keeper's α^{-1} = 137 derivation chain

**Internal claim**: N_max = N_c³ · n_C + rank = 137; identified with α^{-1}.

**External criterion (PASS)**:

The chain T186 → T1464 → 137 must exhibit each step:

1. **Where does N_c³ come from?** Not "N_c is the color count and we cube it." Rather: a specific operator, count, or identity where N_c appears to the third power *unavoidably*. Examples that would pass:
   - "Dim of K-isotypic component of the j-th K-type at the Wallach point equals (2j + N_c)(j+1)(j+rank)/C_2; evaluated at j = N_c gives N_c³ · (...)"
   - "Trace of [specific operator] on [specific bundle] is N_c³ by direct computation"
   - "The reference frame counting (RFC) framework gives N_max as eigenvalue of [specific operator]; computation yields N_c³ · n_C + rank"

   What would FAIL: "We cube N_c because three is the color count and we need a small N_max." That's choice, not derivation.

2. **Where does the additive + rank come from?** Similar requirement: explicit operator, count, or identity that produces "+ rank" as a forced shift, not as a fitting parameter.

3. **What is N_max physically?** It needs an interpretation BEFORE matching to α^{-1}. Examples that would pass:
   - "N_max is the maximal eigenvalue of [operator] below which all modes are bound"
   - "N_max is the count of K-types contributing to the Bergman expansion"
   - "N_max is the rank of the lattice spanned by [specific structure]"

   What would FAIL: "N_max is whatever quantity equals 137." Tautology.

**External criterion (FAIL flags)**:
- Citation to T186 / T1464 without exhibiting their content
- The formula appears at some step "by definition" or "as parameter"
- The interpretation of N_max requires matching to α^{-1} first
- Different BST documents give different derivations of the same formula

**My target depth for the chain**: 3-7 explicit steps from classical D_IV^5 invariants to 137, each step a named theorem or computation. Once exhibited, this becomes external D-tier.

---

## Deliverable 2: Lyra's K-type branching to SM gauge group

**Internal claim**: K-type decomposition at Wallach point produces SM quantum numbers.

**External criterion (PASS)**:

1. **Specific K-type decomposition exhibited**. The Wallach representation π_2 has K-types {ρ_j}_{j≥0} with explicit dimensions. The decomposition must say:
   - K = SO(5) × SO(2)
   - SO(5) further decomposes (under appropriate subgroup) into [specific subgroup chain] with branching rules
   - Each ρ_j carries specific quantum numbers under the chain

2. **Identification with SM**:
   - The color SU(3) appears as [specific subgroup of SO(5)]
   - Weak SU(2) appears as [specific subgroup]
   - Hypercharge U(1) appears as [specific generator, likely from SO(2) factor]
   - **Crucial**: the identification must specify WHICH K-type produces WHICH SM multiplet. Quarks (3,2,1/6), leptons (1,2,-1/2), Higgs (1,2,1/2), etc.

3. **Family structure**: BST claims three generations. The chain must explain why three (presumably from N_c = 3 or similar) and what distinguishes them.

4. **Anomaly cancellation**: SM gauge anomaly cancellation requires specific quantum number relations among quarks and leptons. The BST derivation should either:
   - Force the anomaly-cancelling assignments naturally
   - Note where it relies on external requirements (anomaly cancellation imposed)

**External criterion (FAIL flags)**:
- "N_c = 3 = color count" treated as derivation of SU(3) (it's not — it's matching)
- Branching rules use "convenient" subgroup choices not forced by the structure
- Multiple plausible identifications exist (i.e., the choice is not unique)
- Anomaly cancellation is "satisfied by construction" rather than derived

**My target**: the branching K → [SM subgroup] should be either UNIQUE (only one natural subgroup chain) or motivated by physics-derived selection criteria. If multiple branchings produce different "SM-like" gauge groups, this is mathematical recreation, not derivation.

---

## Deliverable 3: Elie's Monster prime statistics (A-1 expansion)

**Internal claim**: Ogg primes are over-represented in BST-expressibility vs non-Ogg primes; mean depth 0.93 vs 1.94.

**External criterion (PASS)**:

1. **Sample sizes**: report N_Ogg and N_non-Ogg explicitly. Ogg list has 15 primes. Non-Ogg comparison should be at least 100 small primes to get power.

2. **Depth definition**: explicit operational definition. What counts as a "depth-k expression"? Number of BST atoms? Number of arithmetic operations? Need standardization so the audit is reproducible.

3. **Statistical test**: t-test or Mann-Whitney U on the depth distributions. Report:
   - Test used
   - p-value
   - Effect size (Cohen's d or analog)
   - 95% confidence interval on the mean depth difference

4. **Multiple-comparison robustness**: if various "depth" definitions tried, report all results. p-hacking risk: choosing the definition that produces the lowest p-value.

5. **Baseline counterexample**: take a non-BST set of 6 small primes (e.g., {2, 3, 5, 11, 17, 23}) and run the same audit. Does it ALSO produce Ogg over-representation? If yes, then BST integers aren't special — any small-prime set produces overlap. If no, BST integers are statistically distinguished.

**External criterion (FAIL flags)**:
- p > 0.05 (not significant)
- Sample size N < 50 for non-Ogg comparison
- "Depth" defined post-hoc to produce desired result
- No baseline counterexample
- Baseline counterexample ALSO over-represents (in which case BST claim dissolves)

**My target**: p < 0.001 AND baseline counterexample fails to show Ogg over-representation. If both, the Monster connection is genuinely structural (over-baseline). If either, the claim is weaker.

---

## Deliverable 4: Elie's K3 spectral eigenvalue subset test

**Internal claim**: K3 surface is the "spectral slice" of D_IV^5; the topology is forced.

**External criterion (PASS)**:

1. **Explicit K3 Laplacian spectrum**: at least the first 20 eigenvalues of the Laplacian on a specific K3 surface (e.g., the Fermat quartic in CP^3, or Kum(E×E) for E with CM by Q(√-7)). Computed via Hodge theory or explicit formula.

2. **Explicit D_IV^5 K-type spectrum**: the K-type dimensions d_j at the Wallach point, computed by the formula d_j = (2j+N_c)(j+1)(j+rank)/C_2.

3. **Subset claim**: every K3 Laplacian eigenvalue equals some d_j (possibly with multiplicity) OR appears as a specific function of d_j's.

4. **Failure cases**: if some K3 eigenvalues don't appear in the K-type spectrum, document which ones and what they correspond to (Hodge-theoretic invariants outside the spectral slice?).

**External criterion (FAIL flags)**:
- Only the first few eigenvalues match; later ones don't
- "Spectral slice" interpreted loosely as "K3 invariants are polynomials in BST integers" (which is TOP-1 / TOP-2 already; doesn't add spectral content)
- Comparison done at the level of dimensions/Betti numbers rather than eigenvalues
- Test passes only for specific K3 surfaces (CM cases) not generic K3s

**My target**: D-tier if K3 eigenvalues are a forced subset of D_IV^5 K-types with explicit mapping. I-tier if "spectral slice" is interpreted as dimension-match only.

**Why this matters**: this test settles the K3-from-D_IV^5 claim at structural-D-tier. Without it, the K3 connection is topological-by-classification (Enriques-Kodaira) rather than spectrally forced.

---

## Deliverable 5: Elie's Lock 2-4 consequence toy

**Internal claim** (per Keeper): Locks 2-4 (g prime, N_max prime, Casimir identity) are CONSEQUENCES of the selection (T1829 + classification), not independent filters.

**External criterion (PASS)**:

1. **Explicit demonstration that Lock 2 follows from selection**:
   - Show that for D_IV^5 specifically, g = n_C + rank = 7, and 7 is prime.
   - Show that the primality of g for D_IV^5 is NOT an independent requirement but a consequence of n_C = 5 and rank = 2.
   - **Crucial**: demonstrate that no separate "g must be prime" filter is being applied; show this in code.

2. **Same for Lock 3 (N_max prime)** and Lock 4 (Casimir identity).

3. **Honest accounting of Toy 2246**: re-examine the 38 → 1 cascade. Two readings:
   - **(a) Locks ARE filters**: each test eliminates candidates whose analogous parameters fail the algebraic identity. → 38 → 1 is non-trivial.
   - **(b) Locks ARE consequences**: tests verify D_IV^5's parameters; they don't add independent constraints. → 38 → 1 follows from T1829 + classification alone.

   The toy and Paper #104 should be EXPLICIT about which reading applies.

4. **The honest framing for Paper #104** (per my last cold-read response):
   > "Three Chern-class equations (T1829) select n = 5 within type IV. Across all 38 rank-2 BSDs tested, four additional algebraic conditions jointly fail for every candidate except D_IV^5. The selection equations and the algebraic conditions are not independent — they are distinct relations holding among the same integer parameters — but their conjunction is satisfied uniquely by D_IV^5."

**External criterion (FAIL flags)**:
- Locks 2-4 presented as independent without acknowledging the consequence structure
- "7 mechanism over-determination" claim made without disambiguation
- Toy 2246 cited as "4 independent filters" without the consequence caveat
- Paper #104 overclaim on independence

**My target**: the team and the paper should be uniform on reading (a) vs (b). Right now there's some inconsistency between Lyra's toy framing (closer to a) and Keeper's explanation (closer to b). Phase 1 should settle this.

---

## Cross-cutting criteria (apply to all deliverables)

1. **Reproducibility**: each toy / derivation must be runnable from a fresh checkout. No team-internal state assumed.

2. **Explicit citations**: when chains reference other theorems or papers, the references must be specific (paper number, theorem number, section) and the cited content must support the claim.

3. **Failure mode acknowledgment**: each derivation should explicitly note "this would fail if [condition]." Honest scope.

4. **Tier labels at each step**: every step in a chain gets its own tier label. If step 4 is C-tier, the whole chain inherits C-tier — exhibit this honestly.

5. **External-reader readability**: the chain should be readable by a referee who has NOT read prior BST documents. Includes brief recapitulation of needed definitions.

---

## What I'll deliver after Phase 1 results land

For each deliverable, I'll produce a one-page cold-read note:

- **PASS / CONDITIONAL PASS / FAIL** verdict
- Specific issues by criterion (above)
- Recommended revisions if conditional
- Specific paper sections where the result should appear with what framing

Estimated cold-read time per deliverable: 30-60 minutes once it lands.

If all 5 deliverables come back PASS, the SP-24 Phase 1 closes successfully and Paper #104 has the chains exhibited that turn internal D-tier into external D-tier across the board.

---

## What I'm doing right now (while team produces)

While Lyra / Keeper / Elie produce Phase 1 outputs, I'll:

1. **Re-read existing BST docs that will go into the chains** (T186, T1464, Paper #9 heat kernel) so I have context when results land
2. **Pre-draft skeleton cold-read templates** so I can fill them quickly when each deliverable arrives
3. **Stand by for first results**

Standing by. Ping me as Phase 1 deliverables land — I'll cold-read in order of completion.

— Cal A. Brate, 2026-05-15
