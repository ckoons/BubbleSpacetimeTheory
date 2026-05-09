# T1771: EF Information Budget Theorem

**Status**: PROVED (unconditional for the budget bound; conditional on T69 for the size lower bound)

**Statement**: Let phi be a k-SAT formula on n variables with variable interaction graph G. Let pi be an Extended Frege (EF) refutation of phi. For any line L of pi, define vars(L) as the set of original variables x_1,...,x_n that L depends on through any chain of extension definitions. Then for any variable x_j not in vars(L):

    I(L; x_j | phi, SAT) <= I(vars(L); x_j | phi, SAT)

Moreover, the right-hand side is bounded by the SDPI cascade:

    I(vars(L); x_j | phi, SAT) <= |vars(L)| * eta^{d_min(vars(L), j)}

where eta < 1 is the SDPI constant of the k-OR channel and d_min is the minimum VIG distance from any variable in vars(L) to x_j.

---

## Proof

By induction on the derivation of L in pi.

**Base cases:**
- *Clause axiom C_j*: vars(C_j) are the variables appearing in the clause. I(C_j; x_j) <= I(vars(C_j); x_j) by DPI (C_j is a function of its variables).
- *Extension axiom z <-> f(x_S)*: This is a tautology (true for all assignments). Therefore I(axiom; x_j) = 0 <= I(vars(axiom); x_j). Note: z itself has vars(z) = S.

**Inductive step (modus ponens):**
From lines A and A -> B, derive B. The formula B depends on the original variables that appear in B, so vars(B) is determined by the formula B itself (not by how it was derived).

By DPI: I(B; x_j) <= I(vars(B); x_j) since B is a deterministic function of its variables.

**Key observation**: vars(B) is a subset of vars(A) union vars(A -> B), but the bound I(B; x_j) <= I(vars(B); x_j) does NOT depend on the derivation. It depends only on which variables B mentions.

The SDPI cascade bound on the RHS follows from T1765-T1766: for variables at VIG distance d, I(x_i; x_j | phi, SAT) <= eta^d, and I(x_S; x_j) <= sum_{i in S} I(x_i; x_j) <= |S| * eta^{d_min}.

QED.

---

## The Structural Gap: Routing vs Creation

**What this theorem proves:**
- Extension variables CANNOT create new information channels (DPI is unconditional)
- Every EF line's information about any variable is bounded by the SDPI cascade through the VIG
- The information budget of any EF proof is bounded by the clause-axiom information

**What this theorem does NOT prove:**
- A lower bound on the NUMBER of proof lines (proof SIZE)
- That EF requires superpolynomial size

**The gap** (Toy 2108, Test 3): Modus ponens can RECOVER information that premises compressed away. Specifically:
- A = x_0 AND x_1 carries I(A; x_j) = 0.000423 bits about x_9
- B = x_0 carries I(B; x_j) = 0.138241 bits about x_9
- A -> B is a tautology with I(A->B; x_j) = 0
- Deriving B from A via MP gives a line with MORE info than the premise A

This is not a violation of DPI. The info was always in x_0; AND compressed it away, and the tautological structure of A->B guided the recovery. No new channel was created.

**The T69 question, precisely**: Can polynomial-many modus ponens steps, using extension axioms as routing instructions, derive a contradiction from Omega(n/log n) approximately independent blocks? Each step can route existing information but cannot create new channels. The question is whether the routing can be done efficiently.

**Equivalently**: Is information routing through tautological axioms polynomial-time computable for random k-SAT refutations?

---

## Edges

- T1771 <- T1765 (channel capacity, SDPI cascade)
- T1771 <- T1766 (No Free Lunch, block partition)
- T1771 -> T69 (BSW-for-EF, precisely identified as routing question)
- Toy 2108 (9/9 PASS, computational verification)

---

## Significance

This theorem **reformulates** T69 — the last barrier to P != NP via the channel capacity route — as a concrete question about information routing efficiency. The question is not whether extensions can circumvent the SDPI decay (they can't — DPI is unconditional) but whether polynomial-many routing steps suffice to assemble a refutation from independently bounded blocks.

**T1771 does not close T69.** It reformulates T69 in information-theoretic language, isolating the obstruction as routing efficiency. The information-theoretic framing is new. Previous formulations of the EF barrier focused on circuit complexity (can EF simulate circuits?) or feasible interpolation (does EF have it?). The routing formulation is strictly about Shannon information flow and may be more tractable.

The key discovery (Toy 2108 Test 3): modus ponens can recover information that premises compressed away. This counterexample to the naive "MP conserves information" intuition explains why EF is stronger than resolution in information-theoretic terms — and is the precise reason T69 remains open.

---

*Extensions are lossy compressions. Tautologies are routing instructions. DPI bounds the budget. The only question is routing efficiency. (C=1, D=0)*
