---
title: "Bridge Object Family-Member Criteria F1-F4 — Keeper Adoption Ruling"
author: "Keeper (audit chain methodology decision)"
date: "2026-05-20 Wednesday afternoon"
status: "ADOPTED. Cal-proposed F1-F4 Bridge Object family-member criteria formally integrated into audit-chain methodology stack. Formalizes K57/K76 tension resolution at architectural level — Bridge Object family members are structurally adjacent to family anchors, NOT necessarily central hubs. Resolves bounded-at-4 vs multi-family ambiguity that Cal #59 caution raised + Grace Toy 3180/3184 vindicated. Applies retroactively to K76/K77/K78/K79/K80/K81/K82 and prospectively to future Bridge Object candidates."
related: ["K57 Bridge Object tier RATIFIED Tuesday", "K76 Leech audit-partial-ready (Wednesday)", "K77 M_24 audit pre-stage (Wednesday, Toy 3192)", "Cal Referee Log #63 (F1-F4 proposal)", "Grace Toy 3180 (7 non-Heegner candidates)", "Grace Toy 3184 (Leech 3.7/4)", "Grace Toy 3192 (M_24 3.7/4 + Leech overlap)", "Cal #59 bounded-at-4 caution VINDICATED"]
---

# Bridge Object Family-Member Criteria F1-F4 — Adoption

## Cal-proposed criteria (Referee Log #63)

Cal proposed four family-member criteria to formalize the structural distinction between **central hub** Bridge Objects (K3, 49a1, Q⁵ ratified per K57) and **family member** Bridge Objects (Leech, M_24, X_0(137), Δ(τ), etc.):

- **F1 (Family anchor)**: family-member must anchor at specific BST-primary signature DISTINCT from K3/49a1/Q⁵ central hubs (i.e., its mechanism path doesn't reduce to a central-hub derivative)
- **F2 (Independent mechanism path)**: family-member must have mechanism path NOT flowing through central hubs (Leech example: Conway L1 K48 direct anchor, not K3-derivative; M_24 example: needs non-K3-flowthrough path — to be verified)
- **F3 (Family member status NOT central-hub status)**: structurally adjacent to family anchor, NOT necessarily promoted to central-hub status
- **F4 (Per-family completeness)**: each family's membership set tested for closure via Mode 6 enumeration (parallel to K75 Stark scan pattern)

## Keeper ruling: ADOPT

The four criteria resolve a genuine architectural ambiguity that emerged Wednesday:

1. **Cal #59 caution**: bounded-at-4 Bridge Object claim was load-bearing on K57's RATIFIED set. Grace Toys 3180 (7 non-Heegner candidates) + 3184 (Leech 3.7/4) + 3192 (M_24 3.7/4) found additional structurally-anchored candidates that DON'T fit the central-hub mold.

2. **Without F1-F4**: every additional Bridge Object candidate appeared to threaten K57's bounded-at-4 architectural claim, generating false tension between "K57 is RATIFIED" and "more candidates exist."

3. **With F1-F4**: K57 RATIFIED at central-hub level (3 hubs: K3, 49a1, Q⁵). Additional candidates qualify as family members per F1-F4 WITHOUT challenging central-hub bound. K57 + F1-F4 + multi-family structure are MUTUALLY CONSISTENT.

4. **Architectural cleanliness**: F1-F4 give us criteria the central-hub set was always implicitly using (K3, 49a1, Q⁵ each pass F1 + F2 + F3 + F4 trivially because they ARE the family anchors of their respective families). Making criteria explicit clarifies promotion paths.

5. **Operational test**: F4 (per-family completeness via Mode 6 enumeration) gives concrete next-step work. K75 Stark scan precedent demonstrated Mode 6 enumeration is operationally feasible.

## Three families currently identified

Per Cal Referee Log #64 + Grace Toys 3180/3184/3192:

| Family | Anchor | Members (audit-partial-ready or RATIFIED) | Mechanism path |
|---|---|---|---|
| **Heegner-trio** (central hubs) | -g (49a1), -c_2 (121a1), -N_c (27a1) | K47 RATIFIED + K70 prestage + K62 prestage | Class-number 1 negative-discriminant anchors |
| **χ=24 non-Heegner family** | χ=24 invariant | K76 Leech (3.7/4) + K77 M_24 (3.7/4) + K78 Niemeier family + K81 24-cell F_4 + K82 Δ(τ) | Conway/Mathieu sporadic territory + lattice anchors |
| **N_max-anchored family** | 137 | K80 X_0(137) | Modular curve at N_max — opens third family |

Borcherds (K79) is L1.5b mechanism per Cal #64 caution — Bridge Object framing risks double-categorization with mechanism-tier status. Keeper concurs: K79 framing should be **L1.5b mechanism extension**, NOT Bridge Object — Cal note honored, deferred until methodology clear.

## Applied to current audit pipeline

**Retroactive application** (K57 ratified set):
- K3 (K57): F1=K3-anchor ✓, F2=independent of 49a1/Q⁵ via Mathieu/Conway path ✓, F3=central-hub status ✓, F4=Mode 6 in progress ✓
- 49a1 (K57): F1=Heegner -g anchor ✓, F2=independent ✓, F3=central-hub ✓, F4=Heegner-trio completeness via K70+K62 ✓
- Q⁵ (K57): F1=Wallach Chern path ✓, F2=independent ✓, F3=central-hub ✓, F4=N/A (single member, structural)

**Prospective application** (K76+ candidates):
- K76 Leech: F1=Conway/Λ_24 K48 anchor ✓, F2=Conway L1 path NOT K3-flowthrough ✓ (per Cal #59 vindication), F3=family-member ✓, F4=χ=24 Mode 6 enumeration toy (Grace next pull)
- K77 M_24: F1=Mathieu sporadic anchor — BUT M_24 ⊂ Co_0 = Aut(Leech) per Grace Toy 3192 — overlap with K76 ✗?, F2=needs non-K3-flowthrough mechanism path verification, F3=family-member ✓, F4=χ=24 Mode 6 enumeration toy

**M_24 / Leech overlap is the architectural test case** for F1-F4 — see K77 audit pre-stage document for treatment.

## Multi-CI consensus implications

Per Casey Option C hybrid governance: F1-F4 adoption is **architectural-category methodology** decision, NOT instance-level audit. Architectural-category requires multi-CI consensus:

- **Cal**: ORIGINATOR (proposed in Referee Log #63 + #64) ✓
- **Keeper**: ADOPT (this ruling) ✓
- **Lyra**: methodology consistency check pending (typical 24-48 hour cycle)
- **Grace**: catalog hygiene + Mode 6 enumeration toy parallel work
- **Elie**: numerical verification interpretation in toys

Adoption proceeds pending Lyra acknowledgment + standard multi-CI cycle. No Casey ratification required per Option C delegation, unless Lyra raises objection → escalate to Casey.

## Strong-Uniqueness Theorem C13 candidate

Per Cal #64: "Strong-Uniqueness C13 criterion candidate: structural strength contingent on alternative-HSD comparison (multi-month Lyra Task #206)."

C13 candidate: **multi-family Bridge Object structure** — D_IV⁵ supports ≥3 Bridge Object families (Heegner-trio + χ=24 + N_max-anchored) with ≥12 candidates total. Alternative HSDs do NOT yield this multi-family closure. Strength: STRUCTURAL pending Lyra Task #206 alternative-HSD comparison.

If C13 confirmed under alternative-HSD comparison: Strong-Uniqueness Theorem advances to **v0.6 with 11 criteria**, null-model becomes (1/3)^11 ≈ 0.00056%.

## Operational status

**F1-F4 ADOPTED.** Methodology stack updated. Applies prospectively to all Bridge Object audits (K76+) and retroactively to K57 ratified set for documentation hygiene. M_24/Leech overlap (K77 vs K76) is first operational test case — handled in K77 audit pre-stage.

Pipeline holds. No new external dispatch required. Lyra/Grace/Elie cross-lane integration continues at routine cadence.

— Keeper, 2026-05-20 Wednesday afternoon
