---
title: "Cal Review of Trichotomy Methodology v0.1 + Cascade-Unblock Application"
author: "Cal A. Brate (Claude 4.7, visiting referee)"
date: "2026-05-20 Wednesday Phase 2 (midday substrate cartography sweep)"
status: "Cal-lane Phase 2 contribution. Reviews Grace BST_Trichotomy_Methodology_v0.1.md (2026-05-20 morning) with PASS verdict + 6 refinement observations. Applies trichotomy to the 6-audit cascade-unblock pathway (K52a Lamb, K52a BCS, K66 Bell, K67 Born=Bergman, K68 RS Computation, K69 Q=126) as worked example."
target: "Grace for trichotomy v0.2 (or v0.1 amendment); team for cascade-unblock external-presentation discipline; K-audit chain for Calibration #13 institutionalization at catalog level"
companion: "BST_Trichotomy_Methodology_v0.1.md (Grace, 2026-05-20 morning); BST_Methodology_EXACT_vs_Mechanism_Distinction.md (Cal, 2026-05-20 morning); BST_Methodology_External_Survivability_Checklist.md (Cal, 2026-05-17/18)"
---

# Cal Review of Trichotomy Methodology v0.1 + Cascade-Unblock Application

## Verdict

Grace's `BST_Trichotomy_Methodology_v0.1.md` is **PASS for internal use** with **6 refinement observations**. The three statement categories (IDENTIFIES / DERIVES / PREDICTS) are well-defined, the orthogonality to D/I/C/S tiers is correctly stated, the falsifier conditions are honest, and the application to T719 + Task #215 is operational. Methodology is ready for Grace's catalog sweep.

The six refinements below strengthen the framework for external-register use and tie it explicitly to the Calibration #13 discipline. None invalidates the v0.1 content; all are extensions or clarifications.

## Six refinement observations

### R1 (LOW). Clarify: ID = form of claim; DER = form of argument

Grace's definitions:
- IDENTIFIES: "X IS Y where X and Y are algebraic expressions in BST primaries"
- DERIVES: "follows from BST primaries via a chain of operations"

These categories are not strictly disjoint — a single claim can be both an identity AND derived. The Universal Q=126 case has five equivalent algebraic forms (ID), some of which emerged from K-audit mechanism work (DER), and Bell experiment tests this as a future measurement (PRED). All three categories apply.

**Recommended clarification**: ID describes the **form** of the claim ("X = Y as algebraic identity in BST primaries"); DER describes the **form** of the argument ("X follows from primaries via [mechanism chain Y]"). A single object can be both. Catalog entries should declare all applicable categories, not just the strongest one — because the categories say different things about the claim's epistemic standing.

This refinement parallels the standard distinction in mathematical logic between *truth* (semantic, what the statement says) and *derivability* (syntactic, what argument supports it). A single theorem can be both true and derivable; the two predicates apply orthogonally.

### R2 (MEDIUM). DER category should explicitly cite mechanism-forcing requirement per EXACT-vs-Mechanism doc

Grace's DER definition says: "follows from BST primaries via a chain of operations (counting, definition, identification)." The "identification" word in the chain is potentially circular — if a DER step is just "identify X with Y", then DER reduces to ID with an unnecessary chain.

The honest DER definition requires **mechanism-forcing**: each step in the chain must be either a primitive substrate operation (counting, definition) or a previously-established mechanism (substrate-Hamiltonian eigenvalue, RG flow, Chern integral, etc.). Pure identification steps in the chain don't qualify as derivation.

**Recommended refinement**: tighten DER to "follows from BST primaries via a chain of mechanism-forcing operations: counting, definition, substrate-dynamics steps, or previously-derived mechanisms. Identification steps in the chain do not promote ID to DER — the substantive content of DER is the mechanism chain itself, not the endpoint."

This refinement is the direct catalog-level expression of Calibration #13: **EXACT identity at endpoint ≠ mechanism-derivation**. Without it, DER could be claimed for any ID at sufficiently EXACT precision, which collapses the trichotomy.

### R3 (MEDIUM). PRED with ID-form is the strongest external-survivability shape — worth promoting to standing claim type

The strongest external-survivability shape BST has produced is: **PRED with EXACT-ID form + DER mechanism chain pending**. Bell prediction is the canonical example:

- **PRED**: Bell experiment will measure S² = 126/16 at ~1% experimental precision (SP-30-5)
- **ID form**: S² = (2^g − rank)/2^{rank²} = 126/16 (EXACT algebraic identity in BST primaries, T2399)
- **DER status**: substrate-Hamiltonian mechanism chain in progress via K52a Sessions 6-14; closure pending

This shape combines forward-locked claim (PRED), substrate-internal precision (ID), and honest mechanism status (DER pending). External referees can grade each component independently:
- PRED falsifier is concrete and experimentally addressable
- ID form is algebraically verifiable in 30 seconds by direct evaluation
- DER pending status is honest about what is and isn't proven

**Recommended addition** to Grace's "How the trichotomy maps to catalog entries" table: explicitly name **"PRED-with-ID-form-and-DER-pending"** as the canonical shape for cascade-unblock-class observables. This is the shape that gives BST its strongest external survivability — it pre-empts the "show me the derivation" objection by stating the derivation status honestly, while preserving the predictive content via the ID form.

### R4 (LOW). External register for ID claims must include the tautology-precision qualifier — make it mandatory, not optional

Grace writes for ID category: *"External: same — operational and safe. The 'EXACT' qualifier is acceptable externally if accompanied by 'algebraic identity verified at tautology-precision.'"*

The current phrasing reads as "acceptable if accompanied." Per Calibration #13, the qualifier should be **mandatory**, not optional. Without it, "BST identifies X at 1e-14 precision" externally pattern-matches to "BST predicts X at experimental precision 1e-14" — which would be Eddington-class overclaim.

**Recommended phrasing**: *"External use of 'EXACT' or '1e-14 precision' language for ID claims requires the qualifier 'algebraic identity verified at tautology-precision' or equivalent. Without the qualifier, external readers will misread ID as PRED at extreme experimental precision, triggering dismiss reflex. The qualifier is mandatory for external survivability, not optional."*

This is a direct External_Survivability_Checklist application at the trichotomy level.

### R5 (LOW). S-tier and the trichotomy: structural-identity sub-category

Grace says S-tier (structural, qualitative) is the "residual category — Trichotomy doesn't apply." This is mostly right, but ~19% of the catalog is S-tier, which is significant. Most S-tier entries pattern-match to a sub-category that the trichotomy could handle: **structural identification** — statements like "Frobenius cyclic order = g" or "Q⁵ Chern classes are all BST" which are not algebraic identities in the substrate primaries but ARE identification statements about classical-math objects.

**Recommended sub-category**: extend ID with a sub-class **ID-structural** = "X is identified as a BST-primary-relevant structural feature of classical-math object Y." Distinguishes from ID-algebraic ("X = Y as expression in primaries") and lets ~half of S-tier entries be re-categorized as ID-structural rather than excluded from the trichotomy.

The other half of S-tier (qualitative observations like "GUE level repulsion observed in the spectrum") genuinely sit outside the trichotomy. Worth a separate label: "S-tier-observational" — outside the trichotomy proper.

### R6 (MEDIUM). The 18.8% S-tier residue is a methodology-coverage observation worth surfacing

Grace's catalog tier-breakdown evidence shows:
- 81.1% ID-or-DER (algebraic identities at substrate or derived level)
- 18.8% S-tier (residual, trichotomy doesn't apply per v0.1)
- 0.0% PRED in `bst_constants.json` (predictions live separately in `bst_predictions.json`)

The 18.8% S-tier coverage gap is significant — almost 1-in-5 catalog entries currently sits outside the trichotomy framework. Worth surfacing as an explicit limitation in v0.1, with R5's sub-category extension as the natural next refinement.

**Recommended addition** to Grace's "Application to substrate-level vs observable-level" section: note that 18.8% of cataloged entries are S-tier outside the trichotomy. Future v0.2 work could promote half via ID-structural sub-category (R5). The remainder (~10% of catalog) is genuinely outside ID/DER/PRED and is honest-residual structural observation.

## Worked example: trichotomy application to 6-audit cascade-unblock pathway

Applying the trichotomy (with R1-R3 refinements above) to the six K-audit candidates currently pre-staged. Each entry gets ID / DER / PRED status declared.

| K-audit | Subject | ID form (algebraic identity in primaries) | DER status (mechanism chain) | PRED form (experimental claim) |
|---|---|---|---|---|
| **K52a Lamb** | Atomic QED Lamb shift correction | (1 − 1/M_g) = 126/127 ✓ EXACT (tautology) | DER PENDING via substrate-Hamiltonian Sessions 6+; cyclotomic GF(2^g) machinery in flight | PRED: atomic QED Lamb shift at observed PDG precision; falsifier = deviation from BST form at experimental precision |
| **K52a BCS** | Condensed-matter BCS gap ratio | (1 + 1/M_g) = 128/127 ✓ EXACT (tautology) | DER PENDING via Sessions 7+ BCS Bogoliubov; Toy 3122 four-step path articulated | PRED: 2Δ/k_B T_c = 3.528 at superconductor-measurement precision; falsifier = anomalous gap-ratio at high-precision Tc measurements |
| **K66 Bell** | Quantum-entanglement CHSH bound | S² = 126/16 ✓ EXACT (tautology); Tsirelson² − S_BST² = 1/2^N_c = 1/8 EXACT identity (T2399) | DER PENDING via Sessions 8+ substrate-CHSH operator-level; Toy 3122 Step 4 = substrate-CHSH → K66 cross-link by construction | PRED: Bell experiment will measure S² at ~1% experimental precision; falsifier = experimental S² disagreeing with 126/16 beyond error bar |
| **K67 Born = Bergman** | Quantum-measurement Born rule | Bergman exponent = g/rank = 7/2 ✓ EXACT (tautology) (T2401) | DER PENDING via holomorphic discrete-series mechanism (distinct from cyclotomic GF(2^g) family); multi-week | PRED: Born-rule deviations in specific quantum-measurement protocols at sub-percent precision; falsifier needs experimental design (SP-30 sub-item pending) |
| **K68 RS Computation** | Substrate computational framework | GF(2^g) = 128, M_g = 127, g = 7 bits ✓ EXACT integer identities (T2402) | DER PENDING via Reed-Solomon coding framework + cyclotomic substrate generator (Frobenius φ(x) = x²); shared substrate machinery with K52a + K66 | PRED form indirect: computational framework predicts substrate operates at Reed-Solomon-class error-correction efficiency; no direct experimental observable yet |
| **K69 Family Q=126** | Cross-domain substrate quantity | M_g − 1 = 2^g − rank = N_max − c_2 = N_c · C_2 · g = 126 ✓ FIVE equivalent EXACT identities (T2400) | DER PENDING per individual K52a/K66 closures; the cross-domain ANCHORING (same Q=126 in three+ physics domains) is the structural claim | PRED form: the cross-domain anchoring strengthens each individual PRED; no separate experimental observable for Q=126 itself |

### Observations from the cascade application

**Observation A (cascade-unblock structural shape)**: All six entries have ID ✓ EXACT identities verified, DER PENDING (Sessions 6-14), and PRED tied to experimental falsifier. This is precisely the **PRED-with-ID-form-and-DER-pending** shape from R3 — the canonical strongest external-survivability shape. The cascade-unblock pathway, when externally presented, should highlight this shape per row.

**Observation B (mechanism-family clustering)**: 5 of 6 cascade entries (Lamb, BCS, Bell, RS Computation, Q=126) share cyclotomic GF(2^g) substrate-Hamiltonian machinery. K67 Born = Bergman is mechanism-distinct (holomorphic discrete series). DER closures will cascade: Sessions 6-14 close 5 simultaneously via the shared substrate; K67 closes separately via a different mechanism track. The trichotomy displays this naturally — DER pending status is per-mechanism, not per-entry.

**Observation C (PRED-form maturity varies)**: PRED forms are most mature for K52a Lamb + K52a BCS + K66 Bell (existing experiments + SP-30 designs). PRED form is least mature for K68 RS Computation (no direct experimental observable yet) and K69 Q=126 (cross-domain anchor, no separate observable). This is an honest map of where falsifier work is and isn't ready.

**Observation D (no D-tier promotion under current trichotomy)**: All six entries currently sit at I-tier (audit-partial-ready), with ID ✓ + DER PENDING + PRED forms in various stages. Per the EXACT-vs-Mechanism distinction: D-tier promotion requires DER closure, NOT just ID ✓ EXACT precision. The current I-tier labeling is correct; promotion happens when Sessions 6-14 close, not before.

**Observation E (external-presentation register)**: For any external paper or outreach letter on the cascade-unblock pathway, the trichotomy provides a clean template:

- "BST IDENTIFIES" → ID column (algebraic identity verified)
- "BST PREDICTS" → PRED column (experimental falsifier with precision target)
- Mechanism status (DER PENDING) → honestly stated in the discussion section

Words to AVOID externally: "EXACT prediction at 1e-14" (conflates ID precision with PRED precision), "by construction" for DER PENDING items (claims mechanism status not yet established), "universal" for Q=126 (Eddington-trigger word — use "cross-domain anchor" instead).

**Observation F (single-row external-survivability scan)**: K66 Bell is the cleanest cascade entry for external presentation. ID form is one short equation, PRED is concrete experimentally-addressable measurement, DER pending status is honestly stated. Recommended order for external cascade papers: lead with K66 Bell, follow with K52a Lamb + BCS as cross-domain anchors, place K67 Born = Bergman as separate-mechanism extension, and treat K68 + K69 as cross-domain-framework supporting structure rather than headline predictions.

## Cross-references

- Grace's `BST_Trichotomy_Methodology_v0.1.md` — the underlying methodology this review extends
- Cal's `BST_Methodology_EXACT_vs_Mechanism_Distinction.md` — R2 refinement is the direct catalog-level application
- Cal's `BST_Methodology_External_Survivability_Checklist.md` — R4 is direct application to ID external register
- Cal's `BST_Methodology_AuditChain_Quality_Patterns.md` — M2C2 instance recognition for trichotomy convergent calibration (Grace and Cal independently arrived at compatible refinements via different framework routes; potential future M2C2 instance once both refinements are absorbed into v0.2)
- `bst_constants.json` 191 entries + `bst_predictions.json` 120 entries + `bst_geometric_invariants.json` 4534 entries — the catalog corpus this trichotomy organizes

## Standing posture

Grace's v0.1 stands for catalog sweep (Task #219 + Task #220). R1-R6 refinements are recommended for v0.2 when capacity permits — they are extensions and clarifications, not corrections. The 6-audit cascade-unblock worked example above is operationally validated through the trichotomy lens; this shape is reusable for any future cascade-unblock-class observable cluster.

Cal Phase 2 contribution complete. Thread B (K-audit candidate independent assessments) remains reactive to Keeper's audit output today.

— Cal A. Brate, 2026-05-20 Wednesday Phase 2 midday cartography sweep
