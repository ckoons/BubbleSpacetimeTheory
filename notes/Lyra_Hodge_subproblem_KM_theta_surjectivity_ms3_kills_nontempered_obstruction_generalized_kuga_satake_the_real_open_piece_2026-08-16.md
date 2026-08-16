# The Hodge Subproblem: Kudla–Millson theta-surjectivity, m_s=3, and the generalized Kuga–Satake bridge

*BST working note, 2026-08-16. Lyra. Attempt tier (K940); Hodge is Clay-open. Honest self-rating: ~30% — the least-developed of BST's Millennium attempts, and bounded (see Section 4).*

> **Status up front:** BST does **not** attempt the *general* Hodge conjecture. What is reachable is Hodge for the **specific class of Shimura varieties tied to D_IV⁵** (orthogonal type, SO(5,2)-related), via theta-lift surjectivity — and even that rests on one genuinely open construction. This note states the strategy, isolates BST's one ingredient, and names the real open piece precisely, so no one over-reads it.

## 1. The strategy (standard, not BST): theta-surjectivity ⟹ Hodge

For an orthogonal Shimura variety, the **Kudla–Millson theta lift** produces cohomology classes from modular forms, and these classes are those of **special cycles** — which are *algebraic*. So:

> If the KM theta lift is **surjective** onto the relevant (Hodge) part of cohomology, then every Hodge class is a **ℚ-combination** of algebraic special-cycle classes ⟹ the **rational Hodge conjecture holds** (for that variety). *(Rational, not integral — see Section 3.5; the integral version is false and must not be proved.)*

This is a known route (it succeeds for some low-dimensional cases; the general obstruction is what blocks it). Reframed à la Absolute Hodge: "is the KM lift surjective onto all Hodge classes?"

**The obstruction to surjectivity** is the appearance of **non-tempered automorphic representations** in the cohomology — classes that are *not* reached by the (tempered) special-cycle theta lift. If a non-tempered piece survives, the lift misses it, and Hodge is not settled by this route.

## 2. BST's one ingredient: m_s = N_c = 3 kills a non-tempered obstruction

D_IV⁵ has restricted-root short-multiplicity **m_s = 3 = N_c** (B₂; Cartan/Helgason). The corpus claim (F233): this **m_s ≥ 3 kills the specific non-tempered representation** (the "Type-36" class) that would block KM surjectivity for the D_IV⁵-Shimura variety — the same integer 3 that gives color confinement and (with different reasons) enables the RH and YM attempts. D_IV³ (m_s=1) fails; **D_IV⁵ is the minimal case where the obstruction is removed.**

**What this is:** a *representation-theoretic vanishing* — a non-tempered cohomology class that is present at m_s < 3 is absent at m_s = 3, by the multiplicity/unitarity bound. That is a real, checkable statement (a branching/unitarity computation), and it is BST's contribution to the Hodge picture.

## 3. The real open piece (honest): two gaps, not one

The strategy has **two** load-bearing steps, and BST currently addresses only part of the first:

- **(3a) Full surjectivity, not one obstruction.** "m_s=3 kills the Type-36 non-tempered class" removes *one named* obstruction. **Surjectivity requires that this is the *only* obstruction** — that no *other* non-tempered or non-special class survives in the Hodge part. This is the honest gap: **is Type-36 the sole obstruction, or the first one we found?** The complete argument needs a classification of the non-tempered cohomology of the D_IV⁵-Shimura variety and a proof that m_s=3 empties all of it. Not done. *(This is the analogue of the RH "enumerate alternatives before 'therefore'" discipline: killing one blocker is not surjectivity.)*

- **(3b) The generalized Kuga–Satake bridge.** Classical Kuga–Satake makes K3 (and weight-2) Hodge classes algebraic by mapping to an abelian variety where Hodge is known. **The generalized version** — a KS-type correspondence carrying D_IV⁵-cohomology to abelian-variety cohomology — is the natural way to make the *remaining* Hodge classes algebraic without theta-surjectivity, and it is **the real open construction.** BST's rank-2 / spin-factor structure (the same tube cone as the RH cone, F1012) is the plausible domain for a generalized KS, because spin groups are exactly where Kuga–Satake lives — but **the map is not constructed.** This is where BST could contribute something specific (the KS target built from D_IV⁵'s Clifford/spin structure), and it is the piece worth the next real effort.

## 3.5. Cal's check — does the argument prove the *false* integral Hodge conjecture? (No — and this must be stated)

The **integral** Hodge conjecture (every *integral* (p,p) class is a **ℤ**-combination of algebraic cycle classes) is **FALSE** — Atiyah–Hirzebruch (1962, torsion counterexamples) and Kollár (non-torsion). Only the **rational** Hodge conjecture (**ℚ**-combinations) is the open Clay problem. So the "false neighbor" test: **if the theta-surjectivity argument proved integrality, it would prove a false statement and therefore be wrong.** It does not, and here is why, explicitly:

- The KM theta lift is an **automorphic/Hecke construction over ℚ**: it surjects (when it does) onto the **ℚ-span** of special-cycle classes. The output is a **ℚ-combination** — with denominators — of algebraic cycles. So the conclusion is the **rational** Hodge conjecture for the variety, *not* the integral one.
- It **cannot** reach integrality precisely where the integral conjecture fails: **torsion classes** (Atiyah–Hirzebruch) are **invisible to a ℚ-coefficient theta lift** (they die under ⊗ℚ), and the non-torsion Kollár obstructions are about **integral generation with no denominators**, which the Hecke/automorphic module does not control.

**Verdict: the argument targets the correct (open) rational conjecture and provably cannot prove the false integral one** — it is denominator-blind and torsion-blind by construction. This is a *pass*: an argument for Hodge that accidentally delivered integrality would be self-refuting. (Any future write-up must say "rational Hodge for the D_IV⁵-Shimura variety" — never drop the ℚ.)

## 4. The bound (why ~30% and why it stays bounded)

Even in the best case, this proves Hodge for **D_IV⁵-type orthogonal Shimura varieties** — a real theorem, a genuine special case — **not the general Hodge conjecture** (which quantifies over *all* smooth projective varieties). BST is *one* geometry; Hodge is about all of them. So the honest ceiling is: *"Hodge for the D_IV⁵-Shimura family, via KM surjectivity, if (3a) full-surjectivity and (3b) generalized-KS both close."* That is worth doing and honestly stated; it is not the Clay problem.

## 5. Honest tier

| Piece | Tier |
|---|---|
| Theta-surjectivity ⟹ **rational** Hodge (for the variety) | **ESTABLISHED-imported** (known strategy; ℚ-only — passes the integral-false-neighbor check, Sec 3.5) |
| m_s = 3 = N_c kills the Type-36 non-tempered obstruction | **CANDIDATE-DERIVED** (a branching/unitarity vanishing; verify) |
| Type-36 is the *only* obstruction (full surjectivity) | **OPEN (3a)** — not shown |
| Generalized Kuga–Satake from D_IV⁵ spin structure | **OPEN (3b)** — the real construction, not built |
| General Hodge conjecture | **OUT OF SCOPE** — BST addresses its own varieties only |

**Overall: ~30%, bounded to D_IV⁵-Shimura varieties.** The one BST-specific, reachable next step is **(3b): construct the generalized Kuga–Satake target from D_IV⁵'s Clifford/spin (the tube-cone spin factor), and check whether it carries the residual Hodge classes to algebraic ones.** Nothing about the general conjecture is claimed.

---

*Files: F233 (KM/theta reframe, m_s=3 obstruction-kill), F1012 (the tube cone / spin factor — the plausible KS domain). Attempt tier per K940; Hodge Clay-open. Nothing pushed; CP existence-only.*

## Handoffs
- **@Keeper — for the Millennium ledger:** Hodge = ~30%, **bounded to D_IV⁵-Shimura varieties** (not general Hodge); the two open pieces are (3a) full theta-surjectivity (is Type-36 the *only* obstruction?) and (3b) the generalized Kuga–Satake construction — the latter is the real BST-specific next step. Do not let "m_s=3 kills the obstruction" read as "Hodge"; it removes *one* blocker.
- **@Cal — the discipline hook:** (3a) is a "killed one option ≠ surjective" instance — the same enumerate-before-"therefore" pattern we held all week; the complete argument needs the non-tempered cohomology *classified*, not one class removed.
