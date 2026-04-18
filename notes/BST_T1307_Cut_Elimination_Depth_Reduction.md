# T1307 -- Cut Elimination Is Depth Reduction

*Gentzen's Hauptsatz (cut elimination) is T96 (Depth Reduction) applied to proof trees. A cut is a self-reference: using a lemma that was proved inside the same proof. Eliminating cuts is eliminating depth. Cut-free proofs are AC(0).*

**AC**: (C=0, D=0). Zero computations (the identification is structural). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (AC framework).

**Date**: April 18, 2026.

**Domain**: proof_theory.

---

## Statement

**Theorem (T1307, Cut Elimination Is Depth Reduction).** *The Gentzen cut-elimination procedure on sequent calculus proofs is an instance of T96 (Depth Reduction): it replaces depth-d proof steps with depth-(d-1) proof steps, terminating at depth 0 (cut-free). Specifically:*

1. *A **cut** in a proof is a formula A that is proved (as a lemma) and then used (as a premise). The proof references itself: the conclusion depends on an intermediate result that was constructed within the same proof tree. This is self-reference depth 1.*

2. *A **cut-free proof** is one where every formula used as a premise is either an axiom or follows directly from subformulas of the conclusion. No self-reference. Depth 0.*

3. *Gentzen's Hauptsatz: every proof with cuts can be transformed into a cut-free proof of the same conclusion. The transformation may increase proof LENGTH exponentially, but it reduces DEPTH to 0.*

4. *In AC language: cut elimination trades depth for width. The computational content is unchanged — the same conclusion is reached. The self-reference is eliminated at the cost of longer (but shallower) computation.*

---

## The AC(0) Reading

| Proof concept | AC concept | Depth |
|:-------------|:-----------|:-----:|
| Cut-free proof | AC(0) computation | 0 |
| Proof with cuts | AC(d) computation, d ≥ 1 | ≥ 1 |
| Cut elimination | Depth reduction (T96) | — |
| Proof length blowup | Width increase | — |
| Herbrand expansion | Explicit witness enumeration | 0 |

The famous superexponential blowup of cut elimination (Statman 1979: height h → tower of 2s of height h) is the COST of depth reduction. This is not a bug — it is the AC depth-width tradeoff made explicit.

**Connection to P≠NP**: If P = NP, then every proof system would have polynomial-length proofs (Cook-Reckhow 1979). Cut elimination shows that SOME proof systems require exponential blowup to reach depth 0. The blowup is geometric — it comes from unfolding self-reference — which is why it matches the Bergman curvature obstruction (T421, Depth-1 Ceiling).

---

## Why This Matters

Gentzen's theorem (1935) is the foundational result of proof theory. It says: self-reference in proofs is eliminable but expensive. AC says the same thing about computation: self-reference (depth) is eliminable but the cost is width.

This is not an analogy. It is the SAME theorem. A proof IS a computation (Curry-Howard). A cut IS a self-reference. Cut elimination IS depth reduction.

The AC framework unifies:
- Gentzen (proof theory): cuts → cut-free
- Shannon (information theory): encoding → counting
- BST (physics): curved → flat (Bergman → boundary)

All three are instances of T96: composition with definitions is free, but unfolding definitions costs width.

---

## For Everyone

Imagine you're solving a puzzle and you say: "I already proved step 7 works, so I'll use it here." That's a cut — you're referencing your own work. It makes the proof SHORT but DEEP (you need to remember step 7).

Now imagine writing the proof so that you never reference earlier steps — you just spell everything out from scratch each time. The proof gets LONG but SHALLOW. You never need to remember anything. That's cut elimination.

The tradeoff — short-and-deep vs. long-and-shallow — is the same tradeoff in EVERY area of mathematics. BST says: the universe runs at depth 0 (counting). Humans add depth (abstraction) to save space in their brains. CIs can work at either depth. The game is knowing WHEN depth is worth the cost.

---

## Parents

- T96 (Depth Reduction — composition with definitions is free)
- T316 (Depth Ceiling — depth ≤ rank = 2)
- T421 (Depth-1 Ceiling under Casey strict)
- T970 (Resolution Termination — depth 0)

## Children

- Proof complexity classification (which proof systems need which depths)
- Herbrand theorem as AC(0) witness extraction
- Speed-up theorems (Gödel, Statman) as depth-width tradeoff bounds
- Curry-Howard correspondence as AC classification of programs

---

*T1307. AC = (C=0, D=0). Cut elimination = depth reduction (T96). Cut-free proofs are AC(0). Superexponential blowup = cost of unfolding self-reference. Gentzen, Shannon, and Bergman are the same theorem. Domain: proof_theory. Lyra derivation. April 18, 2026.*
