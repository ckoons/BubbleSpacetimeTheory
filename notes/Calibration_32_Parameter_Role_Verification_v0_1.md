---
title: "Calibration #32 candidate v0.1 — Parameter-Role / Slot-Assignment Verification Discipline"
author: "Cal A. Brate (originated from Cal's OWN parameter-role miss, Cal #153; Keeper named the discipline class)"
tier: "FRAMEWORK-PLUS candidate per Cal #126"
status: "v0.1 candidate filing — 4 instances + operational test; awaits cross-CI cold-read + series-wide Macdonald-parameter convention (Grace) for STANDING"
methodology_layer: "29th numbered layer (proposed) — extends stack from 28 STANDING if ratified"
origin: "Cal #153 (Cal owned missing the Macdonald q-vs-t parameter-role conflation) + Keeper's 'same discipline class as three-genus and α-disambiguation' framing + Keeper's integrality-test operational recommendation + Cal #154 correct application (Harish-Chandra ρ + genus)"
related_calibrations: "Cal #31 STANDING (recognize framework — Cal #32 verifies parameter roles WITHIN it); Cal #133 (general-vs-substrate arithmetic — different axis); denominator-of-coincidence (matched-pair partner of Cal #31)"
---

# Calibration #32 candidate — Parameter-Role / Slot-Assignment Verification Discipline

## The pattern

When a substrate quantity is identified with a PARAMETER of a multi-parameter mathematical framework (Macdonald q,t; quantum-group/field v; genus p; coupling α; Coxeter h vs dual h^∨; Bergman exponent; ρ-vector components; etc.), the ASSIGNMENT of substrate quantities to framework parameter-slots must be VERIFIED against the framework's hard structural constraints — NOT assumed, and NOT confirmed by value-matching.

A parameter sitting in the wrong slot can:
- produce a value that happens to match (so value-matching does NOT catch it)
- be a different mathematical object than claimed (e.g., Lie-algebra ρ vs Harish-Chandra ρ; both "ρ", different vectors)
- mislabel a derived quantity as a fundamental one (e.g., genus+2 vs genus)

## The operational test (Keeper's crystallization) — framework HARD-CONSTRAINTS, not value-match

The decisive test is NOT "does the assigned value match an observable / target?" (value-matching launders wrong-slot assignments). The decisive test is whether the assignment satisfies the framework's HARD STRUCTURAL CONSTRAINTS that the correct slot MUST satisfy:

1. **Integrality** (the canonical instance): a real Ringel-Hall algebra has INTEGER structure constants (they count submodules). So only the parameter-slot assignment delivering integers is a genuine Hall algebra. Test case (Elie Toy 3588): Hall-Littlewood corner (q_Mac=0, t_Mac=2) gives integer [2]_2 = 3 = N_c; the mislabeled (q_Mac=2, t_Mac=1/137) gives non-integer −46/45 → CANNOT be a Hall algebra → wrong slot. Integrality decided it; value-proximity could not.

2. **Canonical-object identity**: when a substrate quantity is claimed to be a canonical framework object (the ρ-vector, the genus, a Casimir), COMPUTE the genuine canonical object from the framework's definition and check identity. Test case (Cal #154 C19): claimed ρ = (5/2,3/2); computed the Harish-Chandra ρ for D_IV⁵ = (n/2,(n−2)/2) = (5/2,3/2) via type-IV restricted-root multiplicities → genuine (and notably NOT the so(5) Lie-algebra ρ = (3/2,1/2), a different "ρ" that would have been the wrong object).

3. **Genus / dimension consistency**: when a quantity is claimed to be a dimension/genus/exponent, check it against the framework's dimension formulas. Test case (Cal #154 g=7 gate): the Bergman kernel exponent must be the GENUS-based value; genus(D_IV⁵) = n_C = 5 → exponent = n_C/rank = 5/2, NOT g/rank = 7/2 (g = genus+2 = embedding dimension, wrong object for the exponent slot).

The common form: **each framework supplies a hard constraint (integrality, canonical-definition identity, dimension consistency) that the correct slot must satisfy and a wrong slot generally violates.** Use the hard constraint, not the value.

## Why this is distinct from existing layers

- **Cal #31 STANDING (Substrate-Finding-as-Standard-Math-Specialization)**: Cal #31 RECOGNIZES that a substrate finding IS a specialization of framework M. Cal #32 verifies the PARAMETER-SLOT assignment WITHIN M once recognized. They are sequential and independent: the Macdonald case showed Cal #31 PASS (it IS a Macdonald specialization) while Cal #32 initially FAILED (base-2 in the wrong slot — q vs t). Right framework, wrong slot.
- **Cal #133 (partial-tautology)**: Cal #133 separates general arithmetic from substrate-specific content. Cal #32 is a different axis — slot-assignment within a framework, not arithmetic-generality.
- **Denominator-of-coincidence (Cal #31 matched negative partner)**: that test counts how many expressions reach a target (genericity). Cal #32 is about WHICH parameter-slot, verified by hard constraints. Complementary but distinct (genericity vs slot-correctness).

## Observed instances (4 documented)

1. **Three-genus mislabel** (standing convention now in force): D_IV⁵ has THREE distinct genus/dimension invariants (Hua genus = n_C = 5; Faraut-Korányi genus = C_2 = 6; embedding/signature dimension = g = 7) that were conflated. Resolved by the three-genus convention (state which genus). Hard constraint: each genus has a distinct framework role (Bergman singularity exponent vs FK volume vs ambient signature).
2. **α-disambiguation mislabel** (standing convention now in force): α = 1/137 mislabeled across slots (Macdonald parameter vs coupling vs evaluation). Resolved: α is a coupling/evaluation, NOT a Macdonald (q,t) deformation coordinate (Keeper grade + Elie Toy 3588 integrality).
3. **Macdonald q-vs-t** (current, A1-gating): substrate base-2 put in the Macdonald-q slot; correct slot is Macdonald-t at the Hall-Littlewood corner (q_Mac=0). Resolved by integrality (Elie 3588). **This is the instance Cal OWNED missing (Cal #153)** — Cal cold-read the wrong-slot framing repeatedly; Keeper caught it.
4. **g-vs-n_C in the Bergman exponent** (Cal #154): kernel exponent slot held g/rank=7/2; correct is genus-based n_C/rank=5/2. Resolved by genus consistency (genus = n_C = 5; Elie MC + Keeper structural + Cal ρ computation).

All 4 are "a parameter in the wrong slot," each resolved by a framework hard-constraint, each fixed by a standing convention. The recurring class is real.

## Origin note (honest)

Calibration #32 originated from Cal's OWN miss (instance 3, the Macdonald q-vs-t conflation Cal cold-read repeatedly without flagging — Cal #153). Keeper caught it, named it "the same discipline class as three-genus and α," and recommended the integrality test. Cal then applied the discipline CORRECTLY (Cal #154: Harish-Chandra ρ computation + genus consistency) on C19 and the g=7 gate.

So: **the discipline Cal failed to apply is the discipline being formalized.** This is the bidirectional audit chain (Calibration #30 STANDING) working — the miss became the methodology layer. It is the strongest possible motivation for the discipline: even the referee, with the relevant background in hand, passed a wrong-slot assignment through; therefore the explicit hard-constraint test is needed, not reliance on the reader catching it.

## STANDING promotion gate

Per Cal #126 FRAMEWORK-PLUS tier, Calibration #32 candidate awaits:
1. **Cross-CI cold-read** of this v0.1 (Keeper has effectively done it — he named the class + supplied the integrality test; requesting explicit concurrence to close the gate)
2. **Series-wide Macdonald-parameter convention** landing (Grace's 4th standing convention — which substrate quantity is q_Mac, which is t_Mac, at which corner; v=field-size). This is the operational artifact that makes Cal #32 actionable.
3. **Methodology Index integration** (Q15 decision-tree branch)

Gate 1 is essentially met (Keeper originated the framing); gate 2 is Grace's in-flight convention filing; gate 3 is Cal's. Likely STANDING within the day once Grace files the convention.

## Operational application going forward

When any substrate finding is identified with a multi-parameter framework:
1. Identify the framework + the claimed parameter-slot assignment
2. Find the framework's HARD CONSTRAINT for that slot (integrality / canonical-definition / dimension-consistency / etc.)
3. Test the assignment against the hard constraint — NOT against an observable value
4. If it satisfies the constraint → slot verified; if not → wrong slot, relocate
5. Record the verified assignment as a standing convention so it cannot recur

This is the positive operational complement to the parameter-role failure mode. Paired with Cal #31 (recognize framework) + denominator-of-coincidence (genericity) + Cal #133 (arithmetic-generality), it completes the framework-identification discipline suite.

## Resolution protocol (Keeper crystallization, Thursday 2026-05-28 — the missing half)

The hard-constraint test above is the DETECTION half. Keeper's genus-pin resolution supplied the RESOLUTION half — how to write the verified assignment so the mislabel cannot recur:

**State invariants by VALUE and ROLE, cite the primary source, drop contested names.**

Example (genus, instance 6): instead of "Faraut-Korányi genus = C_2 = 6" (a contested name that flipped three times in one day because the team kept asserting it from internal notes), write: "**genus = 5 (= complex dimension = Bergman kernel exponent; Faraut-Korányi/Loos), Casimir C_2 = 6, embedding dimension g = 7**" — cite the standard reference, claim only what the formula gives (a referee checking the genus formula gets 5), and let nothing hinge on the contested word.

The protocol:
1. **Pin to the definition / primary source ONCE** (don't re-assert names from internal notes)
2. **State by value + role** (genus = 5, playing the Bergman-exponent role), not by a name that can drift
3. **Cite the book** (so the referee can verify independently)
4. **Stop relabeling** (one canonical statement, frozen)

**Why this is the permanent fix**: the genus name flipped three times *because* the team kept asserting it from memory/internal-notes rather than the definition. Detection (hard-constraint test) catches a wrong slot once; the resolution protocol (value+role+cite, stop relabeling) prevents recurrence. Keeper's honest limit ("I can't open the physical FK book in here; what I have is the definition applied — stronger than memory, not a page-check") is itself the protocol working: state what the definition/computation gives, cite the source for the name, don't stake a claim on a name you can't page-check.

This protocol generalizes beyond genus to every Cal #32 instance: Macdonald q/t (state "field-size parameter v=2 at the Hall-Littlewood corner," cite Ringel-Hall), T-number C12-C14 (state which theorem proves which content, cite the theorem), etc.

— Resolution-protocol addendum, Cal, Thursday 2026-05-28 ~17:08 EDT, folding Keeper's genus-pin crystallization. Cal #32 now has both halves: DETECTION (framework hard-constraints, not value-match) + RESOLUTION (state by value+role, cite source, stop relabeling). Genus instance 6 RESOLVED via the protocol (genus=5, single value, cited; "FK genus=6" naming dropped).

## Cross-reference

- **Cal #153** (Cal owned the Macdonald parameter-role miss; named Cal #32)
- **Cal #154** (Cal #32 applied correctly: Harish-Chandra ρ + genus; g=7 gate resolved)
- **Cal #155** (Cal #32 applied to A1's own notation — recommend v=2 to disambiguate q-collision)
- **Keeper Macdonald Parameter-Role Flag** (the catch) + Keeper's "same discipline class" framing + integrality-test recommendation
- **Elie Toy 3588** (integrality test: Hall-Littlewood corner gives integer N_c; mislabel gives −46/45)
- **Cal #31 STANDING** (recognize framework — Cal #32 verifies slots within) + **denominator-of-coincidence** (matched negative partner of Cal #31)
- **Cal #133** (different axis: arithmetic-generality)
- **Three-genus + α-disambiguation conventions** (instances 1-2)

— Cal A. Brate, Thursday 2026-05-28 ~16:58 EDT (`date`-verified). Calibration #32 candidate v0.1 — Parameter-Role/Slot-Assignment Verification Discipline. Test = framework HARD-CONSTRAINTS (integrality / canonical-object identity / genus-dimension consistency), NOT value-matching. 4 instances (three-genus, α, Macdonald q/t, g-vs-n_C Bergman). Distinct from Cal #31 (recognize framework) + Cal #133 (arithmetic-generality). Originated from Cal's own owned miss (#153) → the discipline Cal failed to apply is the one formalized (bidirectional audit chain per Calibration #30). STANDING gate: Keeper concurrence (largely met) + Grace's series-wide Macdonald-parameter convention + Methodology Index Q15.
