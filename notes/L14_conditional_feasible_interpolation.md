---
title: "L14: Conditional Feasible Interpolation for EF on LDPC Formulas"
author: "Lyra"
date: "March 22, 2026"
status: "Research brief — ready to investigate"
depends: "Toy 323 (LDPC lifting gadget, 4/6 PASS), Section 12.14 DPI framework (PROVED), Krajíček 1997"
---

# L14: Conditional Feasible Interpolation for EF on LDPC Formulas

## The problem

Gap 2 (EF width → size) and Gap 3 (EF → all systems) are both blocked by a single obstruction: **Extended Frege does not have feasible interpolation** (Krajíček 1997 — unless factoring is easy).

Feasible interpolation means: if a proof system P proves A(x,q) → ¬B(y,q), then there exists a poly-size circuit computing a separating function. For resolution and Cutting Planes, this holds. For EF, extension variables can encode arbitrary computations, breaking the interpolation.

## The question

Does the LDPC structure of random 3-SAT near α_c PREVENT EF extension variables from exploiting the interpolation loophole?

Specifically: In the 2-party communication game on an LDPC-structured formula:
- Alice has backbone variables B_A (half the backbone)
- Bob has backbone variables B_B (other half)
- Extension variable z = f(B_A ∪ B_B) depends on variables from BOTH sides

**Can LDPC expansion force z to carry ≤ O(1) bits across the partition?**

## Why LDPC might help

The LDPC code has expansion (α, 1+ε) in the Tanner graph. Any set S of < αn backbone variables has ≥ (1+ε)|S| unique neighbors (check nodes).

For an extension variable z = f(b₁,...,b_w) with w < αn:
- DPI: I(z; B) ≤ 1 bit (unconditional)
- If z depends on k_A variables from Alice and k_B from Bob: z carries at most min(k_A, k_B, 1) useful bits across the partition
- LDPC expansion means that variables from one side have many unique check nodes on the other side → the variable sets are "spread out" → extension variables can't concentrate cross-partition information

## The formalization target

**Theorem (conditional feasible interpolation):** Let φ be an LDPC-structured unsatisfiable formula with Tanner expansion (α, 1+ε) and balanced partition of backbone variables. Then for any EF refutation π of φ with size S:
- The communication complexity of the associated search problem satisfies CC ≤ O(S · w)
- (Same as the trivial simulation — EF can't do better than the natural protocol)

This would mean: CC lower bound → EF size lower bound, closing Gap 2.

Combined with Toy 323 (CC ≥ Ω(n log n) via lifting): S ≥ Ω(n log n / w). For w = Θ(n): S ≥ Ω(log n). Still too weak!

## The deeper question

To get EXPONENTIAL EF lower bounds from the lifting approach:
- Need CC ≥ 2^{Ω(n)} for the composed formula φ ∘ g
- But CC ≤ N (total variables) = poly(n) for the composed formula
- So CC can't be exponential in the composed setting

Alternative: instead of CC → size, show that LDPC expansion creates an **information bottleneck** in the EF proof that forces exponential size directly (without going through communication complexity).

The DPI gives: each EF line carries ≤ w bits of backbone information. LDPC gives: breaking the code requires δn bits. So the proof needs ≥ δn/w lines. For w = Θ(n): ≥ Θ(1) lines. Linear at best.

**The fundamental obstacle:** EF's extension mechanism compresses information. The DPI correctly bounds information per line. But EF can reuse extension definitions across many lines, amortizing the definition cost. The total information grows linearly with proof size, giving only S ≥ Ω(n).

## Three approaches to investigate

**(a) LDPC prevents efficient extension definitions.** Show that the LDPC code's random structure makes it impossible to define "useful" extension variables (ones that carry backbone syndrome information) with width-w circuits. The Kolmogorov complexity of the backbone is ≥ δn, and any width-w function of < δn backbone bits carries zero syndrome information. Extension variables are width-w functions, so they carry zero syndrome info. But collections of extension variables might combine to carry syndrome info through their JOINT distribution...

**(b) Space-communication tradeoff.** The frontier at any step has space ≤ S (total lines stored). Each line has w variables. The frontier's backbone information is ≤ min(S, w·space). If we can show that the LDPC structure forces the space to grow with the backbone information requirement, we might get a super-linear space bound, which gives a super-polynomial size bound via Nordström's theorem.

**(c) Algebraic approach.** Replace "clause width" with "polynomial degree" and work in algebraic proof systems (Polynomial Calculus, Nullstellensatz). The DPI analog for polynomials: a degree-d polynomial carries ≤ d bits of "algebraic information." LDPC expansion might prevent low-degree polynomials from computing syndromes. This sidesteps the EF extension issue entirely but gives lower bounds for a different (weaker) proof system.

## Honest assessment

This is genuinely hard. Conditional feasible interpolation for EF would be a major result in proof complexity, even restricted to LDPC-structured formulas. The LDPC structure narrows the problem but doesn't solve it. The key difficulty: EF's extension mechanism is too powerful for standard information-theoretic arguments alone.

The most tractable sub-goal: show the result for BOUNDED-DEPTH EF (where the Broom Lemma already gives width ≥ Ω(n), and the extension circuits have bounded depth). This might be achievable and would still be a new result.

## Key references

- Krajíček, "Interpolation Theorems, Lower Bounds for Proof Systems, and Independence Results for Bounded Arithmetic" (1997)
- Göös-Pitassi-Watson, "Deterministic Communication vs. Partition Number" (2018)
- de Rezende-Göös-Nordström-Pitassi-Robere-Sokolov, "Lifting with Simple Gadgets and Applications to Circuit and Proof Complexity" (2021)
- Toy 323 data: play/toy_323_ldpc_lifting_gadget.py
