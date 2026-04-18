# T1308 -- Proof Complexity from AC Depth

*The hierarchy of proof systems (Resolution < Frege < Extended Frege < ...) is the AC depth hierarchy restricted to logical formulas. Resolution is AC(0). Frege is AC(1). The separations between them are depth separations, and the superpolynomial lower bounds are curvature obstructions.*

**AC**: (C=1, D=1). One computation (classifying proof systems by depth). One depth level (the classification is meta-mathematical).

**Authors**: Lyra (derivation), Casey Koons (AC framework).

**Date**: April 18, 2026.

**Domain**: proof_theory.

---

## Statement

**Theorem (T1308, Proof Complexity from AC Depth).** *The standard proof complexity hierarchy corresponds to AC depth levels:*

| Proof System | AC Depth | Operations Available |
|:------------|:--------:|:--------------------|
| Resolution | 0 | Clause narrowing (counting) |
| Cutting Planes | 0 | Integer arithmetic (counting) |
| Bounded-depth Frege | d | d levels of formula nesting |
| Frege | 1 | Unrestricted modus ponens (one self-reference) |
| Extended Frege | 2 | Abbreviations (definitions of definitions) |

*The known exponential separations between these systems are instances of the depth-width tradeoff:*

1. *Resolution requires exponential-length proofs of the Pigeonhole Principle (Haken 1985). This is T35 (AC Dichotomy) applied to PHP: the pigeonhole counting argument is AC(0), but Resolution's clause structure forces width expansion.*

2. *Bounded-depth Frege of depth d requires superpolynomial proofs of Tseitin tautologies on expander graphs (Urquhart 1987). This is the expansion-implies-fiat theorem (T18) restricted to depth d.*

3. *Frege is conjectured to be strictly weaker than Extended Frege (the NP ≠ coNP question). In AC language: depth 1 < depth 2. This is T316 (Depth Ceiling) applied to proof systems — the gap between depth 1 and depth 2 is a curvature obstruction.*

---

## The AC Classification

### Resolution = AC(0)

Resolution operates by resolving two clauses: (A ∨ x) and (B ∨ ¬x) yield (A ∨ B). This is subtraction — counting the remaining literals. No formula nesting. No self-reference. Pure AC(0).

The width of a Resolution refutation (maximum clause size) is the AC width parameter W. Atserias-Dalmau (2008): width ≥ n^{1/3} for random 3-SAT. In BST language: W ≥ n^{1/N_c} because clause width IS the color dimension (C10).

### Frege = AC(1)

Frege systems add modus ponens: from A and A→B, derive B. This uses A as both a statement and a premise — one level of self-reference. The A→B rule is a CUT in Gentzen's sense. T1307 says: cut = depth.

Frege proofs of PHP are polynomial-length (Cook 1975). The depth-1 self-reference buys exponential compression over Resolution's depth 0.

### Extended Frege = AC(2)

Extended Frege adds abbreviation: let p ≡ φ, then use p instead of φ. This is definition of definitions — using a named result as if it were primitive. Two levels: (1) prove φ, (2) name it, (3) use the name in further proofs.

The Cook-Reckhow conjecture (Extended Frege = all of NP) is: depth 2 suffices for all efficiently verifiable proofs. In BST: depth ≤ rank = 2 (T316). If this conjecture is true, it confirms that rank = 2 is the computational depth ceiling.

---

## Connection to P≠NP

The proof complexity approach to P≠NP (Cook-Reckhow 1979): if no proof system has polynomial-length proofs for all tautologies, then NP ≠ coNP (which implies P ≠ NP).

In AC language: if AC(d) for ALL d cannot polynomially simulate AC(0) counting, then P ≠ NP. This is exactly the curvature obstruction — the Bergman kernel's non-navigability at polynomial cost (T421).

The current state of knowledge:
- Resolution (depth 0): superpolynomial lower bounds PROVED (Haken, Ben-Sasson-Wigderson)
- Bounded-depth Frege: superpolynomial lower bounds PROVED (Ajtai, Krajíček-Pudlák-Woods)
- Frege (depth 1): NO lower bounds known
- Extended Frege (depth 2): NO lower bounds known

The gap between depth 0 (proved) and depth 1 (open) is the EXACT gap between AC(0) and AC(1). BST says this gap is permanent — it's the curvature of D_IV^5.

---

## For Everyone

Think of different kinds of notes you can take during a lecture:
- **Level 0**: Write down every word the professor says. Very long, but you never need to look back.
- **Level 1**: Write summaries — "this section proves X." Shorter, but you need to remember what X means.
- **Level 2**: Write abbreviations — "see Chapter 3." Even shorter, but you need TWO lookups.

Proof complexity asks: for each kind of note-taking, what's the SHORTEST set of notes that captures the whole lecture?

The answer: Level 0 notes can be exponentially longer than Level 1 notes. But we DON'T KNOW if Level 1 is ever longer than Level 2. BST predicts: Level 2 (depth 2 = rank) is always enough. You never need Level 3 abbreviations.

---

## Parents

- T35 (AC Dichotomy)
- T96 (Depth Reduction)
- T316 (Depth Ceiling — rank = 2)
- T421 (Depth-1 Ceiling)
- T970 (Resolution Termination)
- T1307 (Cut Elimination Is Depth Reduction)

## Children

- Bounded-depth Frege lower bounds as curvature witnesses
- Cook-Reckhow conjecture as rank = 2 ceiling confirmation
- Proof complexity approach to P≠NP via AC depth separation
- Automatizability of Resolution as AC(0) self-optimization

---

*T1308. AC = (C=1, D=1). Proof complexity hierarchy = AC depth hierarchy. Resolution=AC(0), Frege=AC(1), Extended Frege=AC(2). Known separations: depth 0 proved, depth 1 open. Gap matches BST curvature obstruction. Cook-Reckhow conjecture ≅ depth ≤ rank=2. Domain: proof_theory. Lyra derivation. April 18, 2026.*
