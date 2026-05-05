---
title: "Paper #91 Split Plan"
author: "Keeper (Claude 4.6)"
date: "May 5, 2026"
status: "Plan — per cold reader audit May 5"
triggered_by: "Cold reader scope audit: physics sections will trigger immediate rejection at CMP/Annals"
---

# Paper #91 Split Plan

*The math half is the strongest work we've submitted. Don't let the physics half kill it.*

---

## The Problem

Paper #91 currently mixes 11 sections of publishable pure math with 4 sections of physics. A CMP/Annals referee will read Section 14 (Higgs quartic, 3.4% match, above null-model threshold) in 30 seconds and reject the paper before reaching the genuine theorems in Sections 1-11.

## The Split

### Paper #91-Math: "The Spectral Zeta Function of a Type-IV Bounded Symmetric Domain"

**Target**: Compositio Mathematica (or Mathematische Annalen)

**Sections**: 1-11 + 16 + 17 (trimmed)

| Section | Content | Status |
|---------|---------|--------|
| 1 | Introduction (rewrite for pure-math audience) | EDIT |
| 2 | Spectral geometry of D_IV^5 | KEEP |
| 3 | Meromorphic continuation, zeta_B(0) = -483473/483840 | KEEP |
| 4 | Log-cancellation theorem | KEEP |
| 5 | Scattering matrix from c-function | KEEP |
| 6 | Rational functional equation | KEEP + cite Bunke-Olbrich + remove Section 6.4 |
| 7 | Arithmetic of spectral zeta values | KEEP |
| 8 | Nahm sum from B_2 Cartan | KEEP + verify a_10 truncation |
| 9 | Mock theta structure / Siegel modularity | KEEP + tighten rigor |
| 10 | Heckman-Opdam c-function connection | KEEP |
| 11 | Uniqueness of n=5 | KEEP + scope to rigorous criteria only |
| 12 (new) | Period ring (was Section 16) | KEEP |
| 13 (new) | Conclusions (trimmed, no SE/engineering) | EDIT |

**Estimated length**: ~30 pages (560 lines of current 941)

**Required fixes** (from cold reader):
1. Cite Bunke-Olbrich explicitly in Section 6.1 for FE structure
2. Distinguish zeta_B(s) (Dirichlet series) from Z(s) (product) — pick zeta_B as protagonist
3. Fix Hurwitz pole argument in Section 3.6 (make shifted poles explicit)
4. Verify Nahm a_10 = 137 at truncation N > 8 (Elie toy)
5. Remove Section 6.4 (quotient inheritance — hand-waved, re-introduces arithmetic issues)
6. Section 11 uniqueness: scope down to criterion #3 (2^{n-2} = n+3) as the rigorous statement; others as "observations"
7. Drop "568/568 PASS" from abstract — replace with "All numerical claims verified computationally; scripts available as supplementary material"
8. Drop SE/engineering paragraph from conclusions

### Paper #91-Physics: "Physical Constants from the Spectral Zeta Function of D_IV^5"

**Target**: Physical Review D or European Physical Journal C

**Sections**: 12-15 (current numbering)

| Section | Content | Status |
|---------|---------|--------|
| 1 | Introduction (new, reference #91-Math for the spectral framework) | NEW |
| 2 | Chern-beta dictionary (was Section 12) | KEEP |
| 3 | Electroweak structure, sin^2 theta_W = 3/13 (was Section 13) | KEEP |
| 4 | Higgs quartic (was Section 14) — honest about 3.4% | KEEP + honest tier labels |
| 5 | Geodesic QED (was Section 15) — 5-loop dictionary | KEEP |
| 6 | Discussion | NEW |

**Note**: This paper explicitly depends on #91-Math for the spectral framework. Submit after #91-Math is accepted or simultaneously.

---

## Elie Computation Tasks

| Task | Description | Priority |
|------|-------------|----------|
| **Nahm N_trunc** | Verify a_10 = 137 at N_trunc = 10, 12, 15. Does it change? | HIGH |
| **zeta_B vs Z** | Compute both zeta_B(s) and Z(s) at several points. Verify log Z = -sum zeta_B(ns)/n. | HIGH |
| **R-11 parity** | Enumerate 45 Arthur packet types for SO(7). Compute Adams-Johnson parity for SO(5,2). Show Constraints {1,3} kill all 45. | **URGENT** |

---

## Timeline

1. Split the file (Keeper, today)
2. Elie runs Nahm + zeta_B/Z verification (today/tomorrow)
3. Elie runs R-11 parity computation (today/tomorrow)
4. Apply cold reader fixes to #91-Math (Keeper + Lyra, this week)
5. Casey reviews split papers
6. Submit #91-Math to Compositio (target: May 15)

---

*The math half can be polished in a week. Don't bundle it with the physics. — Cold reader, May 5, 2026.*
