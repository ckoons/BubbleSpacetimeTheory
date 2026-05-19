---
title: "Heegner Walk-Back Audit: Scoping Document for Classical-Integer-Set Claims"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-19"
status: "v0.1 — audit criteria + candidate review list. Output handoff to Keeper for K-audit filing (K54-or-K55)."
target: "Keeper K-audit framework + Grace cataloging support per Tuesday assignments"
related: "BST_Methodology_Coincidence_Filter_Risk.md (Cal, criteria framework); K47 Heegner-Stark Root #7 promotion (Sunday afternoon)"
---

# Heegner Walk-Back Audit: Scoping Document

## Why this audit

Sunday May 17 produced a structurally important walk-back: Cal initially endorsed Heegner-Stark as L1 source candidate; Grace's audit caught that "all 9 Heegner numbers are BST-decomposable" is a fact about *BST closure richness*, not about Heegner being an independent source. Cal walk-back articulated the principle: **BST-decomposability alone is NOT sufficient for L1 source status. Mechanism-forcing is required.**

The walk-back content became standing methodology (POSTIT + coincidence-filter Mode-6-adjacent + Paper #104 v0.3 promotion criterion). Heegner was then PROMOTED to ESTABLISHED Root #7 via K47 by providing the missing mechanism: Deuring 1941 CM theory + Cremona 49a1 as Bridge Object connecting Heegner discriminants to D_IV⁵ via the period-domain structure.

**Casey's directive (Tuesday morning, "Option C origin")**: review OTHER classical-integer-set claims in the BST corpus that might exhibit the same identification-not-derivation pattern Heegner did before its mechanism was supplied. The audit fires PRE-PUBLICATION on any claim whose evidence shape is "X classical integer set is BST-decomposable" without a published-mechanism chain to D_IV⁵.

This document defines the criteria + lists candidate claims for review.

## The "Heegner walk-back criteria" (when a claim needs review)

A classical-integer-set claim in the BST corpus needs walk-back audit if **all four** of the following hold:

### Criterion W1 — Classical integer set identified

The claim asserts that a specific finite (or specifiable) integer set produced by a published classical theorem (Heegner-Stark, Ogg, McKay outputs, Mathieu group orders, Conway sporadic dims, etc.) is BST-decomposable.

### Criterion W2 — BST-decomposability is the primary evidence

The supporting evidence is that the integers in the set admit BST primary factorizations or simple BST expressions (products, sums, ratios) of {rank, N_c, n_C, C_2, g, c_2, c_3, χ, N_max, seesaw}.

### Criterion W3 — Mechanism chain to D_IV⁵ is implicit / missing

The claim does NOT exhibit a published-classical-mathematics chain connecting the source theorem's integer output to D_IV⁵ geometry (no embedding, no period-domain identification, no K3-fiber connection, no Aut-group containment, no spectral-slice mechanism). Or: the mechanism is asserted but the load-bearing link is BST-internal rather than classical.

### Criterion W4 — Tier label is L1-source-claim-shaped

The claim is presented (in registry, paper, or catalog) as an L1 source or L1 candidate — not as "I-tier empirical observation" or "S-tier structural pattern."

**Audit trigger**: if W1+W2+W3+W4 all hold, the claim needs walk-back review. The review either (a) supplies the missing mechanism (closing W3, promotion stands), (b) downgrades the tier to honest I-tier identification (relaxing W4), or (c) splits the claim into "BST-decomposability observation" (Reading B per Section 9.4 of Paper #115) and "criteria-gated source candidate" (Reading A).

## Candidate review list — apply the criteria

I've gone through the current architecture (9 ESTABLISHED L1 + 2 mechanisms + 3 Bridge Objects + L1-mediated Bravais) and applied W1-W4 to each. Results:

### Tier A — PROBABLY CLEAN (mechanism chains exhibited, no walk-back needed)

| Root | Mechanism chain | W3 status |
|------|-----------------|-----------|
| Von Staudt-Clausen 1840 | Seeley-DeWitt → Bernoulli → BST primary primes at n_C=5 (Cal C1 audit, Toy 2966) | ✓ Mechanism exhibited |
| K3 Hodge 1962/64 | K3 = period-domain fiber over D_IV⁵; Hodge data forced by Calabi-Yau | ✓ Mechanism exhibited |
| Wallach K-type 1976 | Helgason-Kostant-Vretare on rank-2 Hermitian symmetric space | ✓ Mechanism exhibited |
| Klein 1884 | A_5 ⊂ SO(5) ⊂ K(D_IV⁵) structural embedding + McKay → E_8 → Wallach (two routes) | ✓ Mechanism exhibited (Cal verdict 2026-05-17) |
| Mathieu 1861-1873 | Mukai 1988 M_23 ⊂ Aut_symp(K3) + EOT 2010 elliptic genus → M_24 irrep decomp | ✓ Mechanism exhibited (K45) |
| Heegner-Stark 1952-1967 | Deuring 1941 CM theory + Cremona 49a1 Bridge Object | ✓ Mechanism exhibited (K47, post-walk-back) |
| Conway 1968+Duncan 2007 | V^{f♮} super-moonshine N=1 SVOA at c=12=rank·C_2 | ✓ Mechanism exhibited (K48) |
| Borcherds 1992 (L1.5b mechanism) | Labeled as unifying mechanism, not source — W4 doesn't fire | ✓ Tier labeling honest |
| McKay 1979 (L1.5c mechanism) | Labeled as mechanism — W4 doesn't fire | ✓ Tier labeling honest |

**Verdict for Tier A**: no walk-back review needed. The Sunday May 17-18 K-audit chain (K45-K48) already supplied the mechanism chains for the previously-unanchored candidates. These are all post-walk-back-discipline architectural states.

### Tier B — POTENTIALLY NEEDS REVIEW

| Claim | W1-W4 status | Review action |
|-------|--------------|---------------|
| **Ogg 1975 supersingular primes (Root #8 via Borcherds mechanism)** | W1 ✓, W2 ✓, W3 ✓ (mechanism via Borcherds), W4 ✓. BUT: the mechanism chain goes Ogg → Borcherds → BST integers. Is this chain mechanism-forcing or convergence-organizing? | Verify mechanism per K-audit |
| **Goeppert Mayer 1949 (Root #6)** | W1 ✓ (magic numbers {2,8,20,28,50,82,126}), W2 ✓ (all BST-decomposable), W3 ✓ (SU(2)_J × SO(3) ⊂ SO(5) ⊂ K(D_IV⁵)), W4 ✓. Mechanism chain appears clean per K46. | Spot-check K46 — Cal verify the SU(2)_J × SO(3) embedding chain is published classical, not BST-derived |
| **Mathieu via EOT 2010 (Root #5)** | EOT mechanism connects Mathieu to K3 elliptic genus. Need to verify EOT-published-chain doesn't depend on BST-internal premise. Per Grace's recent Mode 6 (scan-protocol over/under-counting) — the catalog scan that produced "BST atom factorization" of M_24 irrep dims used what protocol? | Verify scan protocol per Mode 6 |
| **Bravais 1849 (L1-mediated Option C, K50)** | NEW "L1 mediated" tier per K50. W4 fires unusually — the "mediated" status is non-standard. | Audit the "mediated" tier itself: is it source-like or mechanism-like? Tier proliferation risk. |

### Tier C — NEEDS WALK-BACK REVIEW

Looking for additional candidate claims in the corpus per the four criteria. **Two surface immediately**:

#### Candidate C1 — "Cathedral component-level closure" (Paper #115 v0.5 Section 7)

Elie Toy 3012 + Section 7.1 table claims 12/12 D-tier component-level BST decomposition of Δr radiative correction. Each component labeled D-tier including:
- Δα(M_Z) = N_c²/N_max at 1.1% — labeled D-tier
- Δr_rem = −1/(rank·c_2²·N_c) at 1.6% — labeled D-tier
- y_t = 1 − 1/N_max at 0.04% — labeled D-tier

**W1-W4 status**: W1 (electroweak radiative correction components), W2 (each component is a BST primary form), W3 (mechanism chain to D_IV⁵ NOT exhibited in the cited section — these are identifications with SM-computed values), W4 (D-tier labels). **All four fire.**

**Recommendation**: walk-back review. Each component-level "D-tier" should be downgraded to "I-tier identification with sub-percent match" unless the mechanism chain (e.g., why N_c²/N_max specifically forces Δα(M_Z) rather than identifying with it) is exhibited in-line. Per my Paper #115 v0.5_PRE grade-pass M4 flag from yesterday.

#### Candidate C2 — Type C density rule "structural law" claim (Elie Toy 3023, walked back yesterday)

This one already got walk-back'd per yesterday's Type C round. **Walk-back complete**, recorded in coincidence-filter methodology doc. No additional audit needed for the rule itself; the catalog (19+ Type C clusters) stays at S-tier per Keeper ruling.

But the catalog ENTRIES (each integer's "N-way density" claim) should be audited under the new strict-context-counting protocol P1-P7 (filed yesterday). Recommendation: spot-audit 3-5 random Type C cluster entries under strict protocol; if density counts hold under strict counting, S-tier label stands; if density drops under strict counting, individual entries may downgrade.

#### Candidate C3 — Cremona 49a1 Bridge Object (Section 5.10 / Paper #115 v0.5)

The Bridge Object claim is that Cremona 49a1's arithmetic invariants (conductor 49=g², discriminant -g³, j-invariant -(N_c·n_C)³, M-W rank=2, CM by Q(√-7)) are all BST primary. This is a single elliptic curve's invariants ALL factoring in BST. 

**W1-W4 status**: W1 (49a1 specific curve, finite invariant set), W2 (all BST primary), W3 (mechanism: 49a1 = canonical CM Bridge Object via Deuring CM theory — already in Heegner K47), W4 (Bridge Object tier, NOT L1 source). 

**Verdict**: W4 fires non-standardly — Bridge Object is a NEW tier introduced Sunday. Need to verify: is "Bridge Object" tier the right framing, or is it a synonym for "I-tier observation with mechanism-via-existing-Root"? Audit recommendation: walk-back review on Bridge Object tier proliferation. If Bridge Object = "I-tier observation that supports an existing Root's mechanism chain," collapse it back to I-tier under the supporting Root. If it's a genuinely new tier category, articulate the criteria for what qualifies.

## Recommendations for Keeper K-audit filing

Three K-audits (K54-or-K55-or-K56) suggested:

**K-audit candidate 1 — Cathedral component-level closure (C1 above)**

Audit Elie Toy 3012 + Paper #115 v0.5 Section 7.1 table. Apply walk-back criteria. Either supply mechanism chain for each component (D-tier stands) or downgrade to I-tier identification per coincidence-filter Mode 4 (ratio noise at low precision) + Mode 6 (scan-protocol). Affects Paper #115 v0.5 grade (my M4 flag from yesterday).

**K-audit candidate 2 — Bridge Object tier articulation (C3 above)**

Audit the Bridge Object category introduced Sunday in Section 5.10. Define the criteria for what qualifies as a Bridge Object vs. what's an I-tier observation under an existing Root. If Bridge Object stays as separate tier: articulate the qualifying criteria. If not: collapse the three currently-listed Bridge Objects (K3, 49a1, Q⁵) into their supporting Roots.

**K-audit candidate 3 — Type C strict-protocol spot-audit (C2 above)**

Use Grace's P1-P7 strict context-counting protocol filed yesterday. Spot-check 3-5 Type C cluster entries from Toy 2954/3023/3026 catalog under strict protocol. Headline question: does the N-way density claim hold when contexts must (a) cite published mathematical source, (b) exclude anthropic constants, (c) exclude tortured constructions like "M_5 - 1 = 30"? If yes, S-tier stands; if not, individual entries downgrade.

## Standing protocol going forward

Adding to the coincidence-filter methodology doc as **Mode 7 (proposed)**: *"Classical-integer-set source claim without mechanism chain."* When a paper or registry entry claims that a classical theorem's output set is L1 source-like, walk-back audit applies BEFORE external publication. Either supply mechanism chain (promote to L1 ESTABLISHED) OR downgrade to "I-tier classical-set observation with criteria-gated promotion path."

This is the operational extension of Cal three-criteria framework (embedding/mechanism/forcing). The criteria gate forward-prevents the Heegner-style walk-back from being needed by catching identifying-language at the drafting stage.

## Output for Keeper

This document is the audit scoping. Three K-audit candidates surfaced (cathedral component-level, Bridge Object tier, Type C strict protocol). Keeper files K-audit per governance — Cal opinion is one input. Grace cataloging support per Tuesday assignment when Keeper files.

**Net deliverable**: audit criteria + 3 candidate K-audit topics. Ready for handoff.

---

*— Cal, Heegner walk-back audit scoping, Tuesday May 19, 2026*
