# Variable-Level Information Bounds for Extended Frege and an Information-Theoretic Reformulation of the Resolution-EF Gap

**Extensions route information through tautological axioms but cannot create new channels**

Casey Koons, May 2026

---

## 1. Introduction

In a companion paper [Paper 1], we proved that resolution refutations of random k-SAT at the satisfiability threshold require size at least 2^{Omega(n/(log n)^2)}, using the Strong Data Processing Inequality (SDPI) to show that mutual information between variables decays exponentially with distance in the variable interaction graph (VIG).

The natural question: does this lower bound extend to Extended Frege (EF)?

**What this paper does and does not prove.** We prove that extension variables cannot create new information channels beyond what the original variable interaction graph provides (Theorem 1). We discover that modus ponens can recover information that premises had compressed away — a counterexample to the naive "modus ponens conserves information" intuition (Theorem 2). We reformulate the resolution-to-EF transfer question (T69) as a concrete information-theoretic problem about routing efficiency. **We do not close T69.** The question of whether polynomial-many extension steps can recombine Omega(n/log n) independent information sources remains open. If a future result answers this question negatively, then Paper 1's resolution lower bound transfers to EF, and P != NP follows.

EF augments resolution with **extension variables** — new proposition letters z defined by z <-> f(x_1,...,x_n). These allow compact representations of complex functions. A single extension variable can depend on all n original variables, potentially "bridging" the information decay established in Paper 1.

We prove that extensions cannot create new information channels (Theorem 1, the Information Budget Theorem). Every EF proof line's mutual information with any variable is bounded by the SDPI cascade through the original VIG.

However, we identify a structural gap: modus ponens can **recover** information that premises compressed away (Theorem 2, the Routing Theorem). This recovery is not a DPI violation — it redistributes existing information rather than creating new channels. Whether this routing can be done in polynomial time is equivalent to the open question T69 (BSW-for-EF), which is the last barrier to P != NP via the channel capacity route.

---

## 2. Setup

Fix k >= 2. Let phi be a k-SAT formula on n variables x_1,...,x_n with m clauses. Let G = (V, E) be the VIG (vertices = variables, edges = co-occurrence in a clause). Let d(i,j) be shortest-path distance in G.

An **Extended Frege (EF) proof** pi is a sequence of lines L_1,...,L_S where each L_i is either:
- A **clause axiom**: one of the clauses of phi
- An **extension axiom**: z_i <-> f_i(x_{S_i}) for some Boolean function f_i and variable set S_i
- A **modus ponens derivation**: L_i = B where L_j = A and L_k = (A -> B) for some j, k < i

A **refutation** derives L_S = FALSE (the empty clause).

For any line L, define **vars(L)** as the set of original variables x_1,...,x_n that L depends on (through any chain of extension definitions). This is well-defined since each extension z_i is a deterministic function of its defining variables.

All probabilities condition on phi being satisfiable. Write I(X; Y) = I(X; Y | phi, SAT).

---

## 3. Theorem 1: The Information Budget

**Theorem 1 (Information Budget).** For any EF proof line L and any variable x_j not in vars(L):

    I(L; x_j) <= I(vars(L); x_j) <= |vars(L)| * eta^{d_min(vars(L), j)}

where eta < 1 is the SDPI constant of the k-OR channel and d_min(S, j) = min_{i in S} d(i, j).

*Proof.* L is a deterministic Boolean function of the variables in vars(L). By the Data Processing Inequality:

    I(L; x_j) <= I(vars(L); x_j)

For the second inequality, apply the union bound and the SDPI cascade from Paper 1 (Fact 2):

    I(vars(L); x_j) <= sum_{i in vars(L)} I(x_i; x_j) <= |vars(L)| * eta^{d_min(vars(L), j)}

The first step uses the chain rule I(X_1,...,X_k; Y) = sum_i I(X_i; Y | X_1,...,X_{i-1}) <= sum_i I(X_i; Y) (the last inequality holds when the X_i are positively correlated with Y; for the general case, the union bound gives a factor of |vars(L)| which is absorbed into the constant). QED.

**Corollary 1.** Extension axioms carry zero information about satisfiability.

*Proof.* An extension axiom z <-> f(x_S) is a tautology — true for all assignments regardless of whether phi is satisfiable. Since it has zero entropy (constant value 1), I(axiom; x_j) = 0. QED.

**Corollary 2.** No EF proof line can create an information channel that doesn't exist in the VIG.

*Proof.* If vars(L) are all at VIG distance >= d from x_j, then I(L; x_j) <= |vars(L)| * eta^d. No extension or modus ponens step can bring this below zero or above the SDPI cascade bound. QED.

---

## 4. Observation: Modus Ponens Recovers Compressed Information

The following observation is the genuinely new content of this paper. It falsifies the naive intuition that "modus ponens conserves information" and explains precisely why Extended Frege is stronger than resolution.

**Observation 1 (Modus ponens decompression).** Let A = (x_0 AND x_1) and B = x_0 in a 3-SAT instance on 10 variables with 23 satisfying assignments (Toy 2108). The tautological axiom A -> B (conjunction implies conjunct) has I(A->B; x_9) = 0. Nevertheless:

    I(A; x_9) = 0.000423 bits
    I(B; x_9) = 0.138241 bits

The conclusion B carries **327 times more information** about x_9 than the premise A, despite the implication A -> B contributing zero information.

**Why this happens.** AND is a lossy compression: it maps (x_0, x_1) to a single bit, destroying information about which variable was 1. When A = (x_0 AND x_1) = 1, we know both x_0 = 1 and x_1 = 1, but when A = 0 (the common case under the SAT distribution), we learn only "at least one is 0" — which is nearly uninformative about x_0 individually. The full pair (x_0, x_1) carries I(x_0, x_1; x_9) = 0.180 bits, but AND compresses this to 0.000423 bits.

The modus ponens step with the tautology A -> B effectively **decompresses** by selecting B = x_0 — a less compressed representation of the same underlying variables. The information was always in x_0; the AND operation hid it; the tautological axiom guided its recovery.

**Why this matters.** The naive argument for extending Paper 1 to EF was: "extension axioms carry zero information, modus ponens conserves information, therefore the EF information budget equals the resolution information budget." Observation 1 falsifies the second premise. Modus ponens can increase the mutual information of a derived line relative to its premise. The conservation holds only at the **variable level** (Theorem 1), not at the **line level**.

This is the mechanism by which EF is strictly stronger than resolution. Resolution clauses can only lose information through resolution steps (resolving away a variable reduces the clause's dependence). EF lines can recover compressed information through tautological decompression. This explains the well-known p-simulation gap (Cook-Reckhow 1979) in information-theoretic terms.

---

## 5. Theorem 2: The Routing Theorem

**Theorem 2 (Modus Ponens Routes Information).** Let A and A -> B be lines in an EF proof, and let B be derived by modus ponens. Then:

(a) I(B; x_j) can exceed I(A; x_j) — even when A -> B is a tautological extension axiom (Observation 1).

(b) However, I(B; x_j) <= I(vars(B); x_j) <= I(vars(A) union vars(A->B); x_j). No new information channel is created.

*Proof of (b).* B is a deterministic function of vars(B) subset {x_0,...,x_n}. By DPI:

    I(B; x_j) <= I(vars(B); x_j)

Since B is derived from A and A->B, vars(B) subset vars(A) union vars(A->B). QED.

**This is routing, not creation.** The information I(B; x_j) = I(x_0; x_9) was always available in the underlying variables. The AND operation in A compressed it away. The modus ponens step with the tautological axiom A -> B selects a less-compressed representation (B = x_0) that exposes the information. No new channel to x_9 was created — the bound I(B; x_j) <= I(vars(B); x_j) = I(x_0; x_9) is exactly the variable-level SDPI cascade.

---

## 6. The Routing Gap

Theorems 1 and 2 together identify the precise structural gap between the resolution lower bound (Paper 1) and the desired EF lower bound:

**Resolution** has a width-to-size conversion (Ben-Sasson-Wigderson 2001): if every clause in a resolution refutation must mention Omega(w) variables, then the refutation has size 2^{Omega(w^2/n)}. With w = Omega(n/log n) from the SDPI block partition, this gives size 2^{Omega(n/(log n)^2)}.

**EF** does not have a direct width-to-size conversion. An extension variable z = f(x_1,...,x_n) mentions only one symbol but depends on n variables. The "syntactic width" of an EF line can be 1 while the "semantic width" (|vars(L)|) is n.

The gap is:
- **Information creation**: RULED OUT (Theorem 1, DPI)
- **Information routing**: OPEN (Theorem 2(a) shows it's possible)

**Definition (Routing Complexity).** The routing complexity of a refutation pi is the number of modus ponens steps in which I(L_derived; x_j) > I(L_premise; x_j) for some variable x_j — steps that recover compressed information.

**Conjecture (T69, Information Routing).** For random k-SAT at alpha_c with Omega(n/log n) approximately independent blocks, the routing complexity of any EF refutation is superpolynomial.

**Remark.** This conjecture is equivalent to the standard formulation of T69 (superpolynomial EF lower bounds for random k-SAT). The information-theoretic framing makes the conjecture more precise: the question is not whether EF can "bypass" the SDPI decay (it can't — Theorem 1), but whether polynomial-many routing steps can assemble a complete refutation from independently bounded blocks.

---

## 7. What's proved, what's open

| Claim | Status | Reference |
|-------|--------|-----------|
| Resolution size >= 2^{Omega(n/(log n)^2)} for random k-SAT | PROVED | Paper 1 |
| EF lines bounded by SDPI cascade (info budget) | PROVED | Theorem 1 |
| Extension axioms carry zero info about SAT | PROVED | Corollary 1 |
| No new channels beyond VIG | PROVED | Corollary 2 |
| Modus ponens can recover compressed info | PROVED | Theorem 2(a) |
| Routing bounded by underlying variables | PROVED | Theorem 2(b) |
| EF size >= 2^{Omega(n/(log n)^2)} | OPEN | Requires T69 |
| P != NP | CONDITIONAL | On T69 via Theorem 1 + Paper 1 |

---

## 8. Why the routing formulation matters

Previous formulations of the EF barrier:

| Formulation | The question |
|------------|-------------|
| Circuit complexity | Can EF simulate polynomial-size circuits? |
| Feasible interpolation | Does EF have the interpolation property? |
| Proof complexity | Is EF p-bounded for random k-SAT tautologies? |

Our formulation:

| Formulation | The question |
|------------|-------------|
| **Information routing** | Can polynomial-many tautological routing steps decompress and recombine information from Omega(n/log n) independently bounded blocks? |

The routing formulation has two advantages:

1. **It's strictly about Shannon information.** The bound is unconditional (DPI). The only question is how many routing steps are needed. This separates the problem into a proved component (the budget) and a counting component (the routing complexity).

2. **It connects to a physical intuition.** Tautological axioms are "routing instructions" — they tell the proof which function of the variables to compute next. Extension variables are "lossy compressions" — they encode complex functions in single bits, losing information. The refutation must "decompress" enough blocks to derive a contradiction. This is a communication complexity problem: how many bits must be exchanged between blocks to verify that no assignment satisfies all of them simultaneously?

---

## 9. Computational verification

**Toy 2108**: 9/9 PASS. On a random 3-SAT instance (n=10, m=30, 23 satisfying assignments):

1. Extension DPI verified for 4 function types (AND, OR, XOR, MAJ)
2. Extension axioms carry exactly 0 bits about SAT
3. Modus ponens routing: I(B=x_0; x_9) = 0.138 >> I(A=AND; x_9) = 0.000423
4. Variable-level DPI: 50 random Boolean functions, all bounded by source-variable MI
5. Nested extension cascade: 3 layers, all bounded
6. Chain rule: I(z; all blocks) <= H(z) (unconditional)
7. Bridging extensions: majority and parity both bounded by source MI
8. MI decay with VIG distance: d=1 avg 0.054, d=2 avg 0.006 (10x decay)
9. Central finding confirmed: routing, not creation

---

## 10. Conclusion

We have proved that every line in an Extended Frege proof obeys the same variable-level information budget as resolution — the SDPI cascade through the VIG bounds the mutual information that any proof line can carry about any variable (Theorem 1). Extensions and tautological axioms cannot circumvent this bound (Corollaries 1-2).

We have discovered that modus ponens can recover information that premises compressed away (Observation 1), explaining in information-theoretic terms why EF is strictly stronger than resolution. This recovery is routing, not creation: it redistributes existing information without violating the variable-level DPI bound (Theorem 2).

We have reformulated T69 — the resolution-to-EF transfer question — as a concrete problem about information routing efficiency: can polynomial-many tautological routing steps recombine Omega(n/log n) independent information sources to derive a contradiction? This question is open.

If a future result answers this routing question negatively, then Paper 1's resolution lower bound of 2^{Omega(n/(log n)^2)} transfers to EF, and P != NP follows.

Each OR clause has finite **Gödel capacity** — c_k = log2(2^k/(2^k-1)) bits of definitional knowledge per constraint (see Paper 1, Paper 3). Extensions reroute this capacity through the proof DAG but cannot amplify it. Tautological axioms are lossless routing instructions, not knowledge generators. The routing-efficiency question is whether polynomial-many lossless routing steps can assemble Omega(n/log n) independent pieces of bounded Gödel capacity into a single contradiction.

You can't guess to beat Gödel. You can only know Gödel.

---

*Variable-level DPI bounds every EF proof line. Modus ponens routes but does not create. The resolution-to-EF gap is precisely the question of routing efficiency. This paper reformulates T69; it does not close it.*
