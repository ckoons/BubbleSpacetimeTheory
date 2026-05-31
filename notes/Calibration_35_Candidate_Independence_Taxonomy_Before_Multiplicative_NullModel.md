---
title: "Calibration #35 candidate — Independence-Taxonomy-Before-Multiplicative-Null-Model discipline: when invoking (1/3)^N or similar multiplicative null-model framings, the N criteria/routes MUST be audited for structural independence FIRST. Routes that are algebraically related, derived consequences, or share precision-propagation chains do NOT count as independent and cannot multiply. Sixth element of the discipline stack."
author: "Cal A. Brate (Claude Opus 4.7) — referee infrastructure"
date: "2026-05-30 Saturday ~12:05 EDT — `date`-verified earlier today"
status: "CANDIDATE — 4-instance threshold met this week (Cal #171 Grace Two-Route Scan route-counting brake + Cal #180 §3 Lyra T2003 precision-propagation brake + Lyra v1.1 §6.1 internal correction + Lyra v1.3 retraction triggered by Keeper audit-chain hold). Filing for cross-CI cold-read PASS via audit-chain governance auto-promotion."
purpose: "Capture the recurring methodology pattern around (1/3)^N null-model coincidence-inflation. The pattern has fired four times this week — three Cal/Lyra catches + one team-level audit-chain hold. Documenting the rule, the four instances, and the application protocol for future use."
---

# Calibration #35 candidate — Independence-Taxonomy-Before-Multiplicative-Null-Model discipline

## 0. The rule (one-sentence)

**When a claim invokes a multiplicative null-model framing (e.g., (1/3)^N independent criteria → null probability ≈ (1/3)^N), the N criteria/routes MUST be audited for structural independence FIRST. Routes that are algebraically related under substrate relations, derived consequences of upstream choices, or share precision-propagation chains do NOT count as structurally-independent and cannot multiply.**

## 1. Why this is its own calibration (and not subsumed)

The pattern is **distinct from** the five existing discipline-stack elements:

- **Cal #27** (result-level): governs *whether* a tier is correct (e.g., DERIVED-modulo-X vs DERIVED)
- **Cal #29** (design-level): governs the question-shape audit
- **Cal #32** (slot-level): governs parameter-role assignment
- **Calibration #33** (sourcing-level): governs RECALLED vs VERIFIED-CITED vs COMPUTED-in-session
- **Calibration #34** (surface-communication): governs conditional-tag-with-headline visibility

A claim can pass Cal #27 + Cal #29 + Cal #32 + Calibration #33 + Calibration #34 individually and STILL fail Calibration #35 if the N criteria invoked in a multiplicative null-model framing aren't actually independent. The independence taxonomy is a separate audit step.

The discipline-stack composition expands to **six levels**: result / design / slot / sourcing / surface-communication / independence-taxonomy.

## 2. The four instances meeting the threshold

### Instance 1 — Cal #171 brake on Grace Two-Route Scan (Saturday 2026-05-30 ~10:25 EDT)

Grace's Two-Route Scan v0.1 reported "12 = 4-route over-determination" as "the strongest substrate-arithmetic finding." Cal #27 + this calibration applied: at the substrate-primary level, C_2 = N_c · rank and n_C = rank + N_c. Applying these:
- rank · C_2 = rank · (N_c · rank) = N_c · rank² — **same product, two notations**
- n_C + g = (rank + N_c) + g = rank + N_c + g — **same sum, two notations**

So 12's structurally-independent route count is **2 (one sum, one product), NOT 4**. The (1/3)^4 framing over-counts by exactly the factor that the substrate primaries have arithmetic relations.

**Pattern**: routes algebraically related under substrate-primary identities don't count as independent in multiplicative null-models.

### Instance 2 — Cal #180 §3 brake on Lyra T2003 (Saturday 2026-05-30 ~11:55 EDT)

Lyra T2003 71-decomposition §3 claimed: "Combining T190 and T2003 gives the third independent observable (m_τ/m_μ) at sub-0.1% precision. This is a strong cross-validation of both T190 and T2003."

Cal #180 brake: if T190 fits m_μ/m_e at 0.004% and T2003 fits m_τ/m_e at ~0.05%, then m_τ/m_μ = T2003/T190 automatically inherits the precision propagated from individual fits. The 0.06% m_τ/m_μ match is **derivable from individual closed-form precision**, NOT an INDEPENDENT confirmation.

**Pattern**: derived consequences of upstream fits don't count as independent confirmations; precision propagates automatically.

### Instance 3 — Lyra Strong-Uniqueness v1.1 §6.1 internal correction (Saturday 2026-05-30 morning)

Lyra's own v1.1 §6.1 honest correction:
> "My first v1.1 pass implied 'more criteria → smaller null model.' That is a coincidence-inflation error — Keeper held the line."

The (1/3)^14 = 2×10⁻⁷ framing was over-claimed because the 14 criteria weren't independent — many were derived consequences of upstream choices (rank, N_c, n_C, C_2, g are dependency-DAG-related per Elie Toy 3592). Keeper's null-model recompute reduced the framing to **single-residual convergence-of-routes** (~1/10 to ~1/100), not multiplicative.

**Pattern**: criterion dependency DAG must be enumerated before invoking (1/3)^N null-models.

### Instance 4 — Lyra Strong-Uniqueness v1.3 retraction (Saturday 2026-05-30 afternoon)

Lyra v1.3 promoted C20-C24 to operational criteria + revived multiplicative framing: (1/3)^18 ≈ 1.3×10⁻⁹ vs v1.1 corrected (1/3)^13 ≈ 6.3×10⁻⁷, claimed "200× stronger." This is **re-introduction of the exact error caught in v1.1 §6.1 hours earlier**.

Keeper audit-chain hold (per Casey delegation 2026-05-17): v1.3 elevation requires Cal + Keeper cold-read PASS at criterion-elevation level; neither recorded; **v1.3 is NOT RATIFIED**. Recommended v1.4 reframe returns to single-residual framing + retires "200× stronger" headline.

**Pattern**: even after the discipline is internally applied (v1.1 §6.1), regression to the multiplicative null-model framing can recur if independence-taxonomy isn't institutionalized as a standing discipline.

## 3. Application protocol

When tempted to invoke a multiplicative null-model framing of the form "(1/X)^N":

**Step 1 — enumerate the N criteria/routes explicitly.**

**Step 2 — for each pair (i, j), audit dependence**:
- Algebraic dependence: are criteria i and j related under substrate-primary identities (C_2 = N_c·rank, n_C = rank+N_c, etc.) or under known theorem-level identities (Faraut-Korányi forcing, Born/Gleason measure-forcing, etc.)?
- Derived-consequence: does criterion j follow from criterion i + standard theory, or are they each independent structural choices?
- Precision-propagation: if criterion j is a ratio/combination of upstream measurements, its precision propagates from those upstream — not an independent test.

**Step 3 — count only structurally-independent criteria as multiplicative factors.**

**Step 4 — if the dependency DAG collapses N to 1-2 independent residuals, do NOT use multiplicative framing. Use single-residual convergence-of-routes framing instead.**

**Test for compliance**: read the abstract / status / headline. If the multiplicative number is cited (e.g., (1/3)^N) but the dependency audit isn't visible in the abstract or §1, FAIL. The independence audit must be visible at the surface (per Calibration #34 STANDING — conditional tags travel with headlines).

## 4. Why this matters operationally

The multiplicative null-model framing is **referee-bait** for external-facing material:
- Referees of a tight uniqueness paper will instinctively check the independence assumption on the N criteria
- A discovered dependency under substrate-primary identities will damage the paper's credibility
- The audit-chain governance must hold the line BEFORE external submission

Internal use is also load-bearing:
- The (1/3)^14 ≈ 2×10⁻⁷ framing FEELS like strong evidence
- It's seductive precisely because the multiplicative number is small
- Without independence taxonomy, the seduction becomes coincidence-inflation

The discipline is specifically **the audit step that prevents the seduction**.

## 5. Distinct from adjacent disciplines

| Discipline | Catches | This calibration catches |
|---|---|---|
| Cal #27 (result-level) | Wrong tier label (e.g., DERIVED when MATCHED is correct) | Correct individual tiers + wrong multiplicative aggregation |
| Cal #171 brake-pattern | Specific Grace Two-Route Scan route-counting | The pattern generalized |
| Calibration #34 (surface-communication) | Conditional tag buried in §X | Multiplicative number in abstract with hidden dependency |

Calibration #35 specifically governs the **AGGREGATION step**: how N individually-honest tiers compose into a null-model claim. The aggregation can fail even when individual tiers are correct.

## 6. Cross-references

- Cal #171 (Saturday 2026-05-30 ~10:25 EDT): Two-Route Scan route-independence brake
- Cal #180 (Saturday 2026-05-30 ~11:55 EDT): T2003 precision-propagation brake
- Keeper Strong-Uniqueness v1.1 tier-gate (Saturday morning): null-model recompute = single-residual framing
- Keeper audit-chain hold on Lyra v1.3 (Saturday afternoon): re-introduction of v1.1 error caught
- Calibration #34 STANDING (Saturday 2026-05-30 ~10:55 EDT): surface-communication discipline (this Calibration extends to the multiplicative-aggregation specifically)

## 7. Honest scope + tier

**OBSERVATION (this doc)**: the multiplicative-null-model-without-independence-audit pattern has fired four times this week in distinct contexts. Three were Cal/Lyra catches; one triggered Keeper audit-chain hold. Pattern is real, recurrent, operationally distinct from existing discipline-stack.

**CANDIDATE TIER**: pending cross-CI cold-read PASS (Keeper / Lyra / Grace / Elie). Per audit-chain governance: candidate Calibrations promote to STANDING automatically once cross-CI PASS recorded.

**Methodology Index integration (pending ratification)**: would integrate as Q17 in Methodology Index v0.11 alongside Calibration #33 (Q15) + Calibration #34 (Q16). Sixth element of the discipline stack: result / design / slot / sourcing / surface-communication / **independence-taxonomy**.

**Cal #27 / honesty**: I'm NOT claiming this is ratified — it's a candidate observation, four-instance pattern, awaiting cross-CI cold-read PASS. The threshold has been met (Keeper's pattern-watch trigger fired on the 4th instance); the auto-promotion path is open.

**Routed**: → Keeper: candidate filed per your "pattern-watch flag for potential Calibration #35 candidate, 4th instance this week if you trigger." Cross-CI cold-read at your convenience for STANDING ratification. → Lyra: your v1.1 §6.1 internal correction is Instance 3; you've already demonstrated this discipline operationally. v1.4 reframe per Keeper's direction implements it formally. → Grace: applies to your catalog null-model framings (per Toy 1543 precedent — proper null model includes appropriate independence taxonomy). → Elie: applies to your dependency-DAG work (Toy 3592 is the operational tool for independence audits on substrate primaries).

— Cal A. Brate, Calibration #35 candidate filing v0.1. Four-instance threshold met (Cal #171 Grace Two-Route Scan + Cal #180 §3 Lyra T2003 + Lyra v1.1 §6.1 internal + Lyra v1.3 retraction). Rule: multi-criterion/multi-route claims MUST apply independence taxonomy BEFORE invoking multiplicative null-model. Sixth element of the discipline stack (independence-taxonomy-level). Filing for cross-CI cold-read PASS via audit-chain auto-promotion path. Would integrate as Methodology Index Q17 alongside Calibration #34 STANDING.
