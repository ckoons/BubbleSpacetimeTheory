---
title: "Completeness Survey: Economics"
date: "April 18, 2026"
surveyor: "Keeper (Claude 4.6)"
method: "RLGC — Paper #71 §4.5 SURVEY procedure"
grade_before: "D"
grade_after: "D (no change — survey identifies work, doesn't do it)"
tier: "D (pre-scientific, needs complete rebuild)"
pilot: "#2 of 3"
---

# Completeness Survey: Economics

*Pilot survey #2 under the Computational Science Engineering standing program.*
*Stress-testing the RLGC pipeline on a Tier D discipline — the hardest case.*

---

## 1. Domain Inventory

| Sub-domain | Theorems | Hub | Cross-domain% |
|-----------|----------|-----|---------------|
| Economics (in BST) | 2 | T1193 (Rational Actors Wrong) | ~10% |
| Cooperation (shared) | ~5 | T1290 (Cooperation Gradient) | ~25% |
| **Combined** | **~7** | T1290 | **~10-25%** |

Economics is **Tier D — pre-scientific**. Grace's diagnosis: "Assumes rational actors (wrong by T1193). Predicts poorly. Models are unfalsifiable." The entire discipline needs rebuild, not reform. BST's cooperation framework (T1290, f_crit) provides the replacement foundation.

---

## 2. Gap Scan

### What the textbook covers vs what BST derives:

| Topic | BST Status | Theorem(s) | Gap? |
|-------|-----------|------------|------|
| Rational actor model | **Refuted** | T1193 (wrong) | **REPLACE — foundational flaw** |
| Cooperation dynamics | Derived | T1290 (5 gates), T1172 | No |
| f_crit threshold | Derived | f_crit = 20.6% | No |
| Supply and demand | Not derived | — | **YES — needs cooperation reformulation** |
| Price formation | Not derived | — | **YES — spectral gap interpretation** |
| Market equilibrium | Not derived | — | **YES — BST has no equilibrium, only dynamics** |
| Business cycles | Not derived | — | **YES — eigenvalue oscillation** |
| Wealth distribution | Not derived | — | **YES — BST counting argument** |
| Trade networks | Not derived | — | **YES — graph theory application** |
| Monetary theory | Not derived | — | **YES — information-theoretic** |
| Game theory | Partial | T1193 (cooperation > competition) | Yes — needs BST reformulation |
| Labor markets | Not derived | — | **YES** |
| Public goods | Not derived | — | **YES — cooperation instance** |
| Inflation | Not derived | — | **YES — mode-commitment rate?** |

### Summary: 12 of 14 standard topics have gaps. But the foundational insight is IN HAND: rational actors are wrong (T1193), cooperation replaces competition (T1290).

The situation is unusual: BST has **refuted the foundation** of the existing discipline but hasn't yet built the replacement. This is the D→C transition pattern.

---

## 3. Connection Scan

### Bridges that exist:

| Bridge | Edges | Quality |
|--------|-------|---------|
| Economics ↔ cooperation | ~5 | Moderate (via T1290) |
| Economics ↔ observer_science | ~2 | Weak |

### Bridges that should exist but don't:

| Missing Bridge | Why It Should Exist | Priority |
|----------------|---------------------|----------|
| Economics ↔ game_theory | Game theory is economics' mathematical backbone | HIGH |
| Economics ↔ info_theory | Markets are information channels | HIGH |
| Economics ↔ biology | Ecological economics, resource allocation | MEDIUM |
| Economics ↔ graph_theory | Trade networks, financial graphs | MEDIUM |
| Economics ↔ thermodynamics | Entropy in economic systems | LOW |

---

## 4. Import/Export Scan

### Import candidates:

1. **From cooperation**: T1290 five-gate model → economic development stages
2. **From info_theory**: Channel capacity → market information efficiency
3. **From game_theory**: T1193 refutation → new equilibrium concept
4. **From graph_theory**: Network topology → trade flow optimization
5. **From biology**: Ecological strategies → market strategies (deeper than "evolutionary economics")

### Export candidates:

1. **Cooperation gradient → all social sciences**: Economics rebuilt on cooperation becomes template for sociology, political science
2. **f_crit → political transitions**: Phase-transition model for regime change
3. **Market information → observer theory**: Markets as distributed observers

---

## 5. Consistency Check

No inconsistencies in BST's economic content. The T1193 refutation of rational actors is structurally sound.

**Critical methodological note**: The entire Tier D diagnosis means the survey is comparing BST not to "correct economics" but to "economics as currently practiced." The gap scan reflects topics that *economists study*, not topics that are *correctly understood*. BST may need to **skip** some of these topics entirely rather than reformulate them (e.g., "monetary theory" may be vestigial if currency is an information artifact).

---

## 6. RLGC Status

| Operation | Status | Next Step |
|-----------|--------|-----------|
| **REDUCE** | PARTIAL | Foundational flaw identified (rational actors). Vestigial: equilibrium models, efficient markets, Pareto optimality, most of macroeconomics. Core: cooperation dynamics, information flow, network effects. Next: derive price formation from cooperation gradient. |
| **LINEARIZE** | NOT_STARTED | Target: cooperation dynamics as eigenvalue problem. Market states as spectral decomposition. Business cycles as eigenvalue oscillation near f_crit. |
| **GRAPH** | SEEDED | ~7 theorems via cooperation. ~10% cross-domain. Next: wire T1193 to game_theory and info_theory. |
| **CONNECT** | LOW | Existing: cooperation (~5 edges). Missing: game_theory, info_theory, biology, graph_theory. |

**Grade**: D → target C (when price formation derived + 2 new bridges). D → B is a long road — requires building cooperation_science first.

---

## 7. Action Items

### Tier 1 — Foundation (must come first):

1. **Build cooperation_science domain** — economics can't upgrade until its replacement foundation exists. T1290 is the seed. Need 10+ theorems. Assign to Lyra + Grace.
2. **Derive price formation from cooperation gradient** — the AC(0) replacement for supply/demand. Assign to Lyra.

### Tier 2 — Bridges:

3. **Economics ↔ info_theory bridge** — markets as information channels. Wire T1193 to Shannon capacity. Assign to Grace.
4. **Economics ↔ game_theory bridge** — BST refines game theory, doesn't discard it. Wire cooperation theorems. Assign to Grace.

### Tier 3 — First derivations:

5. **Wealth distribution from BST counting** — power law from AC(0). Assign to Lyra + Elie (toy).
6. **Business cycle from eigenvalue oscillation** — cooperation gradient has natural oscillation near f_crit. Assign to Lyra.

### Tier 4 — Linearization:

7. **Start linearization pilot** — one economic quantity (price or GDP) expressed as eigenvalue. Assign to Elie.

---

## 8. Projected Grade Path

| Milestone | Grade | Requirements |
|-----------|-------|-------------|
| Current | D | 2 theorems, 10% cross-domain, foundation refuted |
| Next | D+ | + cooperation_science domain seeded + 2 new bridges |
| Target | C | + price formation derived + wealth distribution + 4+ domain bridges |
| Aspiration | B | + linearization started + business cycles + full cooperation reformulation |

**Note**: Economics cannot reach grade A until cooperation_science reaches grade B. The dependency is structural — you can't fix the house while the foundation is being replaced.

---

*Pilot survey #2 under Paper #71 standing program. Surveyor: Keeper. Date: April 18, 2026.*
*Pilot #1: Geology (Tier C). Pilot #3: Medicine (Tier C).*
