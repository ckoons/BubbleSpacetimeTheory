---
title: "Claim-Level Positive Structural Patterns: Overdetermined-Form and Cross-Domain Anchor"
author: "Cal A. Brate (Claude 4.7, visiting referee), formalizing Elie's two-cluster-TYPES distinction"
date: "2026-05-20 Wednesday Phase 3"
status: "Standing methodology document. Companion to (not subset of) BST_Methodology_AuditChain_Quality_Patterns.md (which addresses audit-chain-level patterns) and BST_Methodology_Coincidence_Filter_Risk.md (which addresses negative-filter failure modes). This document specifies POSITIVE structural patterns observed at the claim level."
target: "BST team (Lyra, Elie, Grace, Keeper) for self-recognition + catalog tagging; Grace's Task #244 two-cluster-TYPES taxonomy work; Casey's Graph Forces candidate principle infrastructure anchor"
companion: "BST_Methodology_Coincidence_Filter_Risk.md (Cal, 2026-05-17; negative-filter modes); BST_Methodology_AuditChain_Quality_Patterns.md (Cal+Keeper, 2026-05-20 morning; audit-chain-level patterns); BST_Methodology_EXACT_vs_Mechanism_Distinction.md (Cal, 2026-05-20 morning; ID vs DER distinction)"
---

# Claim-Level Positive Structural Patterns: Overdetermined-Form and Cross-Domain Anchor

## Why this document exists

Elie's Wednesday afternoon work (Toy 3150 + adjacent) identified two structurally distinct cluster TYPES in BST claim patterns. These types are NOT failure modes (which live in Coincidence_Filter_Risk) and are NOT audit-chain processing patterns (which live in AuditChain_Quality_Patterns / M2C2). They are positive structural patterns at the **claim level** — characterizations of how BST claims are structurally over-determined or cross-anchored that strengthen the claim's epistemic standing when the underlying discipline conditions hold.

This document formalizes the two types, specifies the discipline tests that distinguish positive structural evidence from selection-effect artifact, and provides the methodology anchor for Grace Task #244 (two-cluster-TYPES taxonomy catalog) and for Casey's Graph Forces candidate principle.

## The three-document layering

The methodology infrastructure for BST claims now has three positive/negative documents that serve different functions. Brief navigation map:

| Document | Layer | Function | What it catalogs |
|---|---|---|---|
| `Coincidence_Filter_Risk.md` | Negative-filter | Failure modes to clear before publication | Modes 1-7 (post-hoc clipping, multi-decomposability, search-space, ratio noise, selection effect, scan-protocol, classical-set without mechanism) |
| `AuditChain_Quality_Patterns.md` | Audit-chain level positive | Patterns observed in the audit chain processing claims | M2C2 (Multi-CI Convergent Calibration) + reserved future entries |
| This document | Claim level positive | Patterns observed in the claims themselves | Type 1 (Overdetermined-Form) + Type 2 (Cross-Domain Anchor) + combined Type 1+2 |

The three documents are kept separate because they serve different functions. Mixing them would create polarity mismatches (negative filters in a positive-patterns doc) or scope confusion (claim-level patterns conflated with audit-chain-level patterns).

## Type 1 — Overdetermined-Form Cluster

### Definition

**Overdetermined-Form Cluster (OFC)**: a structural pattern in which the same numerical value (typically a BST observable or a substrate quantity) admits **multiple algebraically-independent expressions** in BST primaries, each evaluating to the same value.

The expressions must be algebraically-independent in the sense that one cannot be derived from another by trivial algebraic manipulation. Pure rearrangements (e.g., `2 · 3 · 7 = 7 · 3 · 2`) do not count as distinct forms.

### Canonical example

**Universal Q=126** (T2400, multiple Wednesday CIs):

- `M_g − 1 = 127 − 1 = 126` (Mersenne genus minus one)
- `2^g − rank = 128 − 2 = 126` (Powerful genus minus rank)
- `N_max − c_2 = 137 − 11 = 126` (Boundary prime minus second Chern)
- `N_c · C_2 · g = 3 · 6 · 7 = 126` (Triple product of primary integers)
- [fifth form per Wednesday team work, distinct mechanism source]

Five algebraically-independent forms in BST primaries, all evaluating to 126. The forms use different subsets of primaries via different operations (Mersenne arithmetic, powers-minus-shift, boundary-arithmetic, multiplicative).

### Evidential function

OFC pattern, when honestly attained, provides **structural defense against Mode 1 (post-hoc form selection)**. The argument runs:

- Mode 1 risk is concentrated in single-form claims: "form F was chosen because it lands on target T."
- For multi-form claims, the risk distributes: "each form F_i was chosen independently because it lands on target T." This is N times harder to construct post-hoc than a single form, where N is the number of independent forms.

**Critical condition**: the N forms must be independently derived (each emerging from a separate mechanism track, classical theorem, or substrate process), NOT enumerated through BST-primary combinatorics until N forms landing on T were collected. The latter is Mode 5 selection-effect, not Mode 1 defense.

Concretely for Q=126:
- M_g − 1 = 126: emerged from K52a Lamb mechanism work (Mersenne-anchored)
- 2^g − rank = 126: emerged from K66 substrate-CHSH operator construction (powers-of-2 anchored)
- N_max − c_2 = 137 − 11 = 126: emerged from boundary-arithmetic + second Chern class (Chern-class anchored)
- N_c · C_2 · g = 3·6·7 = 126: identified from primary-integer multiplication (catalog enumeration)

The first three forms are mechanism-independent and constitute genuine Type 1 OFC evidence. The fourth (N_c · C_2 · g) is catalog-enumerated and provides consistency check but not Mode 1 defense. **Discipline rule**: each OFC catalog entry should record the **provenance** of each form (mechanism-derived vs. catalog-enumerated), so the OFC's Mode 1 defense weight can be honestly assessed.

### Diagnostic tests

To distinguish a genuine OFC (Mode 1 defense) from a Mode 5 catalog-enumeration artifact:

**Test 1a**: For each form F_i, was it derived from a separate mechanism BEFORE landing-on-target was observed?

**Test 1b**: How many forms would land on T within ±5% if you enumerated all BST-primary expressions of depth ≤ 3? If the count is ≥ 5, then finding 5 forms among them is NOT evidence beyond enumeration. If the count is ≤ 2 and N ≥ 3 mechanism-distinct forms have been found, that's tight Mode 1 defense.

**Test 1c**: Are the forms used in INDEPENDENT subsequent applications (different K-audit anchors, different cascade-unblock entries, different physical observables)? If yes, the OFC structural significance compounds across applications.

### Anti-pattern

The failure case: OFC is invoked when forms were enumerated by catalog scan after the target value was known. This degrades to Mode 5 selection-effect at best, and to Mode 1 reinforcement (post-hoc form-stacking) at worst. The honest disclosure is: "We identified that the value T admits multiple BST-primary expressions; this is consistency check, not over-determination evidence."

## Type 2 — Cross-Domain Anchor Cluster

### Definition

**Cross-Domain Anchor Cluster (CDAC)**: a structural pattern in which the same BST primary or BST-primary expression appears as the structural anchor in **multiple distinct physical or mathematical domains**, with each domain's anchor independently derived from domain-internal mechanism.

The domains must be physically distinct in the sense that the underlying physics or mathematics are not shared (different Feynman diagrams, different conservation laws, different mathematical machinery). Same observable in slightly-different experimental setups does not count as cross-domain.

### Canonical examples

**Integer 42 = C_2 · g** (Paper #106 Section 5.5 + Cal verdict #47):

- Kaon CP violation: ε_K = α²·42 (W-boson box diagrams; flavor-changing neutral process)
- Higgs di-photon: BR(H → γγ) = α²·42 (W + top triangle loops; precision Higgs)
- Muon g-2: Δa_μ ≈ α²·42·factor (lepton magnetic moment loop)
- Q⁵ second Chern class: integer-valued cohomological invariant
- (Catalan C_5 = 42 — combinatorial coincidence, NOT a CDAC domain per Cal #47 M2)

Four physical observables across four distinct sectors (flavor CP, Higgs precision, lepton magnetic moment, geometric Chern invariant) all anchored at integer 42. The Catalan C_5 = 42 is consistency observation, not a CDAC anchor (per Mode 5 discipline + verdict #47 M2).

**Integer 126 = M_g − 1** (Wednesday cascade-unblock pathway):

- Atomic QED Lamb shift: (1 − 1/M_g) = 126/127
- Condensed-matter BCS gap: (1 + 1/M_g) = 128/127 [paired with 126 via M_g]
- Quantum entanglement Bell CHSH: S² = 126/16
- Cross-domain framework invariant (K69 audit-partial-ready)

Three to four physically distinct domains anchored at 126 via different mechanisms (cyclotomic GF(2^g) substrate-Hamiltonian for Lamb/BCS/Bell; framework-aggregate for K69).

### Evidential function

CDAC pattern, when honestly attained, provides **structural defense against Mode 5 (selection effect on observables)** at the cross-domain level. The argument runs:

- Mode 5 risk is concentrated in single-domain claims: "of all possible BST integer × observable pairs, the matching ones were selected and reported."
- For cross-domain claims with mechanism-distinct anchoring in each domain, the risk distributes: each domain's anchor must independently produce the same integer. The likelihood of multiple independent mechanisms converging on the same integer by chance is much lower than a single domain matching.

**Critical condition**: each domain's anchor must be **independently derived** within that domain's mechanism — not pattern-matched after observing that the same integer appeared elsewhere. The latter is Mode 5 selection-effect with extra steps.

### Diagnostic tests

To distinguish a genuine CDAC (Mode 5 defense) from a pattern-matching artifact:

**Test 2a**: For each domain D_i, was the BST integer anchor derived from domain-internal physics/mathematics BEFORE the cross-domain pattern was observed?

**Test 2b**: How many BST integers in the primary catalog (~20-30 candidates including derived integers and small products) have anchors in N or more distinct domains? If many integers cross-anchor at N domains, then finding one is not surprising. If few integers cross-anchor at N domains and the cluster has a specific BST integer doing so, the structural significance is real.

**Test 2c**: Is there a mechanism-derivation track that produces the same integer in multiple domains through a shared underlying structure (e.g., shared substrate-Hamiltonian, shared cohomology class, shared Casimir)? If yes, the CDAC has both phenomenological cross-anchoring AND mechanism unification — strongest evidential shape.

### Anti-pattern

The failure case: CDAC is invoked when the cross-domain matches were found by pattern-search across BST-primary-decomposable integers in different domains. Without independent mechanism-derivation in each domain, this is Mode 5 in cross-domain form — selecting matches across a broad search space.

## Combined Type 1+2 — Over-determined AND Cross-Anchored

When a value is BOTH overdetermined-form (Type 1) AND cross-domain-anchored (Type 2), the evidential shape is the strongest BST claim structure currently observed.

**Canonical example**: Universal Q=126
- Type 1 OFC: five algebraically-independent forms (M_g−1, 2^g−rank, N_max−c_2, N_c·C_2·g, ...)
- Type 2 CDAC: anchored across three+ physical domains (Lamb shift, BCS gap, Bell CHSH)
- Combined evidence: hard to construct post-hoc AND hard to dismiss as selection-effect

The combined shape provides defense against both Mode 1 (form selection) and Mode 5 (observable selection) simultaneously. Even with full audit-chain discipline, this is the strongest structural shape a BST claim can attain absent mechanism-derivation closure.

**Critical reminder**: combined Type 1+2 strength does NOT bypass mechanism-forcing requirement for D-tier promotion. Per EXACT-vs-Mechanism distinction, mechanism-derivation closure (Lyra Task #243 + Elie K52a Sessions) remains the load-bearing condition. Combined Type 1+2 strengthens I-tier identifications but does not promote them to D-tier on its own.

### CAUTION — Type 1+2 combined evidence does NOT multiply scalarly

A methodology error to avoid: computing "N Type-1 forms × M Type-2 domains = N×M-fold overdetermination" as a single scalar evidential metric. This was the framing in K72 χ=24 ("5 forms × 6 domains = 30-fold multiplicative overdetermination") and Cal flagged it for revision in referee log entry #55.

**Why the scalar multiplication is methodologically wrong**:

- Type 1 (OFC) defends against **Mode 1** (post-hoc form selection). Each independent form derived from a distinct mechanism track reduces Mode 1 risk by approximately one factor of the form-space cardinality at the value.
- Type 2 (CDAC) defends against **Mode 5** (selection effect on observables). Each independent domain anchor where the integer emerges from domain-internal mechanism reduces Mode 5 risk at the cross-domain level.
- **Mode 1 risk and Mode 5 risk do NOT combine multiplicatively**. They are defended by different evidence types at different layers of the claim structure.
- A claim with 5 forms and 1 domain has very different evidential shape than a claim with 1 form and 5 domains, even though 5×1 = 1×5 = 5. The scalar-multiplication framing hides this distinction.

**Recommended framing for Type 1+2 compound claims**:

Replace "N-fold multiplicative overdetermination" or "N×M = K-fold" with:

> **"N-fold OFC + M-fold CDAC compound structure"**

or equivalently:

> **"Type 1+2 compound cluster with N algebraically-independent forms and M domain anchors"**

This framing accurately conveys:
- The N forms defend against Mode 1 at the form-selection level
- The M domains defend against Mode 5 at the observable-selection level
- The compound shape (BOTH simultaneously) is the structural strength
- No single scalar metric is needed; the compound-shape description IS the metric

**For comparison metrics across compound clusters**: use qualitative comparison of the (N, M) pair, not a derived scalar. Examples:

| Cluster | OFC count (N) | CDAC count (M) | Compound shape |
|---|---|---|---|
| K69 Universal Q=126 | 5 forms | ~3-4 domains (Lamb + BCS + Bell + possibly more) | 5-form + 3-4-domain compound |
| K72 χ=24 | 5 forms | 6 domains (K3 + SU(5) + heat kernel + Niemeier + WRT + Wallach) | 5-form + 6-domain compound |
| K61 (131 family) | 1 form (no OFC dimension) | 4 domains | 4-domain CDAC only (not compound) |
| K70 121a1 triple-anchor at 11 (Bridge-Object level) | 3 forms (Heegner + Weitzenbock + Q⁵ Chern) | 3 mathematical contexts | Bridge-Object-level 3-form + 3-context compound |

The qualitative shape is what matters; scalar multiplication misleads. When reporting Type 1+2 compound claims, state both (N) and (M) counts explicitly and avoid deriving a single number.

**Why this caution matters for external survivability**: external referees scanning a paper for evidential metrics will pattern-match "30-fold overdetermination" to grand-claim language. The compound-shape framing "5 algebraically-independent forms and 6 domain anchors" is more verbose but reads as careful empirical characterization rather than claim inflation. Per External_Survivability_Checklist register discipline, the qualitative framing survives 30-second outsider read better than the scalar-derived metric.

## Connection to Graph Forces candidate principle (Casey)

Casey's Graph Forces principle (candidate, pending Casey-name decision) hypothesizes that overdetermined-EXACT-identity clustering serves as a substrate diagnostic. Cal reading: Graph Forces is operationally the *recognition* of Type 1 + Type 2 clusters as substrate-engineering markers.

The two-cluster-TYPES distinction in this document provides the methodology vocabulary for Graph Forces:
- Type 1 OFC clusters identify substrate quantities (where substrate algebra over-produces a value)
- Type 2 CDAC clusters identify substrate-engineering anchors (where one substrate quantity organizes multiple observable domains)
- Combined Type 1+2 clusters identify substrate-engineering keystone points (over-produced AND cross-anchored)

When Casey rules on Graph Forces naming, this document provides the discipline anchor: Graph Forces fires when Type 1, Type 2, or combined patterns hold WITH the diagnostic-test discipline applied (Mode 1 and Mode 5 risks honestly assessed and mitigated).

If Graph Forces is named as a Casey principle, the Type 1 + Type 2 taxonomy here becomes its operational specification. Grace Task #215 (Graph Forces batch-test falsifier toy) operates against this specification: the toy counts overdetermined-form + cross-domain-anchored clusters per N substrate-related theorems vs random null, with the discipline conditions explicitly applied.

## Grace Task #244 catalog tagging schema

For Grace's Task #244 (two-cluster-TYPES taxonomy catalog), Cal recommends the following tagging schema for catalog entries:

| Tag | Definition |
|---|---|
| `OFC` | Overdetermined-Form Cluster — multiple BST-primary forms for same value, mechanism-independent |
| `OFC-provisional` | Multiple forms identified, but not all forms verified mechanism-independent; pending Test 1a |
| `OFC-catalog` | Multiple forms identified by catalog enumeration only; consistency check, not Mode 1 defense |
| `CDAC` | Cross-Domain Anchor Cluster — same BST integer anchors multiple distinct domains, each mechanism-independent |
| `CDAC-provisional` | Cross-domain anchoring identified, but not all domains verified mechanism-independent; pending Test 2a |
| `CDAC-pattern` | Cross-domain pattern observed without verified mechanism-independent anchoring; Mode 5 risk acknowledged |
| `OFC+CDAC` | Combined Type 1+2 cluster (strongest shape) |

The provisional/catalog/pattern variants are honest acknowledgments that not all clusters have completed the diagnostic tests. The full `OFC` or `CDAC` labels should be reserved for clusters where the tests have been explicitly applied and passed.

## Operational guidance

**For Catalog Entries**: tag each BST observable + substrate-quantity entry with `OFC`/`CDAC`/`OFC+CDAC` labels (and provisional/catalog/pattern variants) where applicable. Untagged entries are simple identifications without cluster-pattern structure.

**For K-audit Rulings**: when an audit candidate's claim has OFC or CDAC structure, the cluster pattern is a positive evidential input. But mechanism-forcing for D-tier promotion is unchanged. Combined Type 1+2 strength can move a claim from "I-tier identification" to "strong I-tier identification" but cannot promote to D-tier on cluster strength alone.

**For External Papers**: OFC and CDAC patterns are external-survivability shapes that can be presented honestly. The presentation language:

- OFC: "BST identifies that value X admits N algebraically-independent expressions in BST primaries, with each expression derived from a distinct mechanism track [list]. This over-determined structure makes post-hoc form selection less plausible than for single-form identifications."
- CDAC: "BST identifies that integer Y anchors N physically-distinct observables [list], each anchor independently derived within its domain mechanism. This cross-domain anchoring shape is harder to attribute to selection effect than single-domain matches."

Avoid: "universal" (Eddington trigger; use "cross-domain anchor" or "structurally-distinguished"); "by construction" (claims mechanism status not yet established for cluster-pattern claims); "proves" (mechanism-derivation language for I-tier identification work).

## Standing rule

OFC and CDAC are positive structural patterns at the claim level. When honestly attained with the diagnostic tests applied, they strengthen I-tier identifications and provide structural defense against Mode 1 (OFC) and Mode 5 (CDAC) coincidence-filter risks. They do not bypass mechanism-forcing for D-tier promotion. They are not external-evidence by themselves; they are evidential shapes that, combined with mechanism-derivation work, support BST's I-tier and eventually D-tier claims.

The Grace Task #244 catalog work + Casey Graph Forces principle decision are the operational extensions of this methodology. When Casey-name decision lands on Graph Forces, this document becomes its operational specification.

## Cross-references

- **BST_Methodology_Coincidence_Filter_Risk.md** — Mode 1 (post-hoc clipping) and Mode 5 (selection effect on observables) are the negative-filter modes that OFC and CDAC respectively defend against. Diagnostic tests in this document apply the Mode 1/Mode 5 discipline at the cluster level.
- **BST_Methodology_AuditChain_Quality_Patterns.md** — M2C2 is audit-chain-level positive pattern; OFC/CDAC are claim-level. The two categories are independent and can compound: an OFC+CDAC claim that ALSO fires M2C2 has the strongest combined evidential shape.
- **BST_Methodology_EXACT_vs_Mechanism_Distinction.md** — OFC's "multiple EXACT identities" connects to the over-determination discussion in that doc. CDAC's "cross-domain anchor" is structurally orthogonal to the EXACT-vs-Mechanism distinction. Both still subject to mechanism-forcing for D-tier promotion.
- **referee_objections_log.md entry #47** — Paper #106 v0.4 grade-pass; M2 finding (Catalan C_5 = 42 is NOT a CDAC domain because Catalan is a fixed combinatorial sequence rather than a mechanism-independent physical domain) is the diagnostic Test 2a applied in practice.
- **Grace's BST_Trichotomy_Methodology_v0.1.md** + Cal's review/extension — OFC/CDAC patterns interact with the ID/DER/PRED trichotomy. OFC clusters typically involve multiple ID statements with shared target value; CDAC clusters typically involve multiple PRED statements anchored at shared integer. Cross-classification is natural.

— Cal A. Brate, 2026-05-20 Wednesday Phase 3, formalizing Elie's Wednesday afternoon two-cluster-TYPES distinction
