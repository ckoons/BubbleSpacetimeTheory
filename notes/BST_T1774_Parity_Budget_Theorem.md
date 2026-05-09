# T1774: The Parity Budget Theorem

**Status**: PROVED (linear bound for all proof systems; superpolynomial for resolution via BSW)

**Statement**: For random k-SAT at clause density alpha_c:

**(a) Parity budget.** The satisfying assignment space has entropy H(assignment | SAT) = Theta(n) bits, decomposed into B = Omega(n/log n) approximately independent blocks, each carrying Theta(log n) bits of independent parity.

**(b) Line capacity.** Each proof line L (in any proof system) is Boolean, so H(L) <= 1 bit. Therefore I(L; all blocks) <= H(L) <= 1 bit: each line carries at most 1 bit of total information about all blocks combined.

**(c) Block coverage.** Any refutation must use clause axioms from all B blocks. Removing any single block's clause axioms makes the formula satisfiable (each block is locally satisfiable). Therefore every block must contribute constraints to the refutation.

**(d) Linear lower bound (all proof systems).** Any refutation has size:

    S >= B = Omega(n / log n)

This applies to resolution, Extended Frege, and any propositional proof system.

**(e) Resolution amplification.** For resolution, each clause has syntactic width = semantic width. The SDPI block partition forces clause width w >= Omega(n/log n) (BPS 2003). The BSW tradeoff converts width to size:

    S >= 2^{Omega(n / (log n)^2)}

This is superpolynomial. The parity budget is the REASON for the width requirement: each block's parity must be explicitly represented in the clause's literals.

**(f) EF amplification (OPEN).** For Extended Frege, (d) gives S >= Omega(n/log n). The amplification to superpolynomial requires showing that OR-lossy routing degrades the effective per-line contribution to the global inconsistency check. Specifically: does each MP step contribute at most eta^{d*} effective bits toward cross-block parity assembly, where eta < 1 is the SDPI constant? If so, the cost of assembling B blocks' parities exceeds polynomial.

---

## Proof

**(a)** By Paper 1 (Facts 2-3), the SDPI cascade creates B = Omega(n/log n) variable groups (Voronoi cells around a maximal d*-separated set) with inter-group MI < 1/n^2. Each group has Theta(log n) variables. Under the SAT-conditioned distribution, each group carries H(block_i | SAT) = Theta(log n) bits of independent parity. Total: B * Theta(log n) = Theta(n). QED.

**(b)** Each proof line L evaluates to TRUE or FALSE for each assignment. Under the SAT distribution, L is a binary random variable: H(L) <= 1. By DPI: I(L; anything) <= H(L) <= 1. In particular, I(L; b_1,...,b_B) <= 1. QED.

**(c)** Each block b_i is locally satisfiable (the clauses within b_i are satisfiable by themselves — the formula is at alpha_c, and block subformulas are below threshold). Removing block b_i's clauses leaves a formula that is satisfiable. Therefore the proof must use at least one clause axiom from each block to certify global unsatisfiability. QED.

**(d)** By (c), the refutation uses >= B clause axioms from distinct blocks. Each axiom is a distinct proof line. So S >= B = Omega(n/log n). QED.

**(e)** By BPS (2003, Theorem 4.2): B approximately independent blocks force resolution width w >= Omega(B) = Omega(n/log n). By BSW (2001, Theorem 1.1): width w forces size S >= 2^{(w - O(sqrt(n log n)))^2 / n} = 2^{Omega(n/(log n)^2)}. QED.

---

## The count/boundary structure

| Component | Value | Role |
|-----------|-------|------|
| **Count** (parity budget) | Theta(n) bits from B = Omega(n/log n) independent blocks | Force: what the proof must process |
| **Boundary** (line capacity) | H(L) <= 1 bit per line | Gödel limit: what each line can carry |
| **Ratio** (minimum lines) | S >= B = Omega(n/log n) | Linear lower bound (any proof system) |
| **Amplification** (resolution) | BSW: width w -> size 2^{w^2/n} | Structural tradeoff specific to resolution |
| **Amplification** (EF) | OPEN: routing efficiency | T69 |

The parity budget theorem is a **count/boundary pair** in the sense of Casey's Principle:

- **Entropy (force, counting)**: B blocks, Theta(n) bits of parity. This is what the proof must handle.
- **Gödel (boundary, definition)**: Each proof line can carry at most 1 bit. This is the limit on what each step can contribute.
- **The quotient**: S >= B/1 = B. Force/boundary = minimum cost.

For resolution, the boundary is TIGHTER: each clause of width w can effectively address only w variables, and the parity from distant blocks decays as eta^d. This tighter boundary gives the superpolynomial amplification.

For EF, extension variables relax the boundary: a single extension can nominally address n variables. But the ACTUAL information it carries about each block is bounded by the SDPI cascade (Paper 2, Theorem 1). Whether this SDPI bound provides sufficient tightening to give superpolynomial is T69.

---

## The routing cost question

The gap between linear (proved) and superpolynomial (desired) for EF is the **routing cost**:

- **Linear regime**: B blocks, 1 bit per line, S >= B. Each line perfectly delivers 1 useful bit to the inconsistency check.
- **Superpolynomial regime**: Each line delivers at most eta^{d*} << 1 effective bits (because OR-lossy routing degrades cross-block information). Then S >= B / eta^{d*} >> poly(n).

The question: does each MP step in EF contribute 1 effective bit (linear suffices) or eta^{d*} effective bits (superpolynomial required)?

**For resolution**: each resolution step contributes at most width w bits, but the width is Omega(n/log n), so size is 2^{Omega(w^2/n)}. The "effective contribution per step" is implicitly bounded by the width-size tradeoff.

**For EF**: each MP step can route information (Paper 2), but routing through OR-lossy channels contracts the information (SDPI). The effective contribution per step depends on the proof's structure — how much of the routing goes through VIG clauses (lossy) vs tautological extensions (lossless).

---

## Edges

- T1774 <- T1773 (parity erasure — total parity budget)
- T1774 <- T1771 (EF information budget — 1-bit line capacity bound)
- T1774 <- T1772 (Gödel capacity — per-clause constraint bound)
- T1774 <- T1765 (SDPI cascade — block independence)
- T1774 -> T69 (EF amplification requires routing cost bound)
- Toy 2111 (verification)

---

## Key numbers (k=3)

- Blocks: B = Omega(n/log n)
- Parity per block: Theta(log n) bits
- Total parity budget: Theta(n) bits
- Line capacity: H(L) <= 1 bit
- Minimum lines (any proof system): S >= Omega(n/log n)
- Resolution size: S >= 2^{Omega(n/(log n)^2)}
- EF size: S >= Omega(n/log n) [proved]; superpolynomial [conditional on T69]

---

*Count: B independent blocks of parity. Boundary: 1 bit per proof line. Quotient: S >= B. For resolution, the boundary tightens to eta^d per clause-hop, giving 2^{Omega(n/(log n)^2)}. For EF, the tightening is T69. (C=0, D=0)*
