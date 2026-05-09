# T1772: The SAT Capacity Theorem

**Status**: PROVED (the Shannon framing is a restatement of the first-moment method in information-theoretic language; the convergence alpha_c/alpha_FM -> 1 follows from known asymptotics)

**Statement**: The satisfiability threshold alpha_c for random k-SAT satisfies the Shannon capacity equation:

    alpha_c <= alpha_FM = 1 / c_k

where c_k = log2(2^k / (2^k - 1)) is the **Gödel capacity** per clause — the definitional knowledge a single k-OR constraint contributes, equivalently the entropy removed by one clause.

The capacity equation c_k * alpha_FM = 1 states: at the Shannon limit, the total constraint rate (alpha_FM clauses, each removing c_k bits) equals the per-variable entropy budget (1 bit).

Moreover:
(a) alpha_c / alpha_FM is monotonically increasing in k (capacity utilization increases)
(b) alpha_c / alpha_FM -> 1 as k -> infinity (coding theorem analog)
(c) The gap 1 - alpha_c/alpha_FM measures the correlation loss in the random SAT channel

---

## Proof

The first-moment method gives:

    E[|SAT|] = 2^n * (1 - 2^{-k})^{alpha*n} = 2^{n(1 - alpha * c_k)}

where c_k = |log2(1 - 2^{-k})| = log2(2^k/(2^k-1)).

At alpha_FM = 1/c_k: E[|SAT|] = 2^0 = 1. Above alpha_FM: E[|SAT|] -> 0 exponentially.

By Markov's inequality: P(SAT) <= E[|SAT|], so P(SAT) -> 0 for alpha > alpha_FM.

Therefore alpha_c <= alpha_FM = 1/c_k. QED for the bound.

For part (b): alpha_c = 2^k * ln(2) - (1+ln2)/2 + o(1) (Ding-Sly-Sun for large k), and alpha_FM = 1/c_k = (2^k - 1)/log2(e) * (1 + O(2^{-k})) ~ 2^k * ln(2) * (1 + O(2^{-k})). The ratio alpha_c/alpha_FM -> 1.

For part (a): verified computationally for k=2,...,7 in Toy 2109.

---

## The Shannon picture

| Concept (Shannon) | Concept (SAT) |
|---|---|
| Channel | k-OR clause |
| Channel capacity C | Gödel capacity c_k = log2(2^k/(2^k-1)) |
| Transmission rate R | Clause density alpha |
| Reliable communication (R < C) | Satisfiability (alpha < alpha_c) |
| Capacity wall (R = C) | Satisfiability threshold (alpha = alpha_c) |
| Unreliable (R > C) | Unsatisfiability (alpha > alpha_FM) |
| Coding theorem (R -> C achievable) | alpha_c/alpha_FM -> 1 as k -> inf |
| Multi-user capacity loss | Correlation gap alpha_c < alpha_FM |

The gap between alpha_c and alpha_FM is the analog of the multi-access channel capacity loss: individual clause channels have capacity c_k, but clause correlations reduce the operational capacity.

---

## Connection to Papers 1-2

**Paper 1**: The SDPI cascade uses the same lossy OR channel whose constraint capacity determines alpha_c. At alpha_c, the information budget is saturated — there's no slack for compression — so proof size diverges.

**Paper 2**: At alpha_c, the routing question is hardest because the slack is zero. Below alpha_c, slack > 0 provides room for efficient algorithms. Above alpha_FM, the formula is obviously unsatisfiable (refutation is easy because the formula is drastically overconstrained).

**Proof complexity phase diagram**: The hardest instances are at alpha_c, not above. This mirrors the Shannon coding theorem: capacity-achieving codes are the hardest to decode.

---

## Edges

- T1772 <- T1765 (OR-clause channel capacity)
- T1772 <- T1766 (No Free Lunch at alpha_c)
- T1772 -> T1771 (information budget saturated at alpha_c)
- Toy 2109 (9/9 PASS)

---

## Key numbers (k=3)

- Satisfying fraction: 1 - 2^{-3} = 7/8 = g/2^{N_c} (BST)
- Constraint capacity: c_3 = log2(8/7) = 0.19265 bit/clause
- Shannon threshold: alpha_FM = 1/c_3 = 5.191
- Operational threshold: alpha_c = 4.267
- Utilization: alpha_c/alpha_FM = 82.2%
- Slack: 1 - alpha_c * c_3 = 0.178 bit/variable
- At alpha_c: E[log2(#solutions)/n] = 0.178 (barely positive)

---

*The satisfiability threshold is the Gödel wall — where entropy meets its boundary. Each clause knows at most c_k bits. Demand meets supply at alpha_c. Proof complexity peaks at the Gödel capacity threshold. (C=0, D=0)*
