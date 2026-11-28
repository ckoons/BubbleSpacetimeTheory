---
title: "Positivity from the Interior: a Plan for the Riemann Hypothesis on D_IV^5, with Its Own Hostile Review"
author: "Casey Koons & Claude (Opus 5.5)"
date: "November 28, 2026"
version: "v0.3 — filed to notes/ as an ATTEMPT (notes/maybe is gitignored, local-only). v0.2: commits to the Weil route; Z2 material moved out of the RH case; objection 6.1 narrowed to the trivial-character condition; Paper 84 / K1785 conflict logged."
status: "DRAFT for Casey review. ATTEMPT / open research plan, NOT a proof. One step (Step 4) is the open conjecture and is equivalent in strength to RH."
tier: "Reductions in Section 2: D (classical theorems, cited). Plan Steps 1-3, 5: structural design, not results. Step 4: OPEN. Section 7 (GRH, odd characters): OPEN, a hunch."
---

> **Read this first.** This note writes down a plan and then attacks it. The plan is a reformulation: it moves the difficulty of RH to one place. It does not remove it. Section 6 is the part to read if you came to find the flaw.

## Summary — the chain in six steps

Each of steps 1–5 is a known theorem; step 6 is the one open lemma.

1. **State it as counting:** Schoenfeld's bound on π(x) − li(x). Each case is one count, depth 1 (von Koch, Schoenfeld).
2. **Read the ½ as information:** the error touches only the lower half of the bits of π(x), like coin flips (Denjoy).
3. **Locate the boundary:** the error is the rounding at the end of each progression, the fractional parts {x/d} (Legendre).
4. **Turn it into a shape:** dilates of one sawtooth must fill the unit interval with no gaps (Nyman–Beurling, Báez-Duarte), equivalently cyclicity on the infinite polydisc, one disc per prime (Hedenmalm–Lindqvist–Seip, Bohr, Bagchi).
5. **Make the sign structural:** prove a squared quantity positive rather than search for negatives (Weil, Li). Squares cancel twists.
6. **The one open lemma:** an exact identity writing Weil's form as a norm on the right space, archimedean term included. Exact because Λ = 0; must fail for Davenport–Heilbronn and Beurling primes.

In Lean terms (Casey, Nov 28): the contribution is one lemma, step 6, added to Mathlib. Caveat: steps 1–5 must also be in Mathlib for the chain to close there; Mathlib's coverage of the explicit formula, Li, Nyman–Beurling and Schoenfeld has not been checked.

## Level 1 — what this is about

The Riemann Hypothesis says the primes are as evenly spread as they can be. A century of work has shown it is the same as saying a certain quantity, built from the primes, can never be negative. Quantities that can never be negative are usually squares, or lengths, or areas. So we ask: is there a shape, built only from geometry and the primes, in which that quantity is literally a length? If so, it cannot be negative, and RH follows. We propose a candidate shape, say exactly what would have to be true, and then list every reason it might fail.

## 1. The question

The open part of RH is not "find the zeros." It is: **prove that one explicit quadratic form, built from the primes, is positive.** We ask whether the Bergman space of D_IV^5, restricted to the right arithmetic piece, can carry that form as a squared norm.

## 2. Reductions we rely on (all classical, all derived elsewhere)

Each of these is a theorem. Together they say what a proof must deliver.

1. **Weil positivity.** The explicit formula defines a form W(f * f̃) from primes alone (f̃(x) = conj f(-x)). RH holds if and only if W(f * f̃) >= 0 for every test function f (Weil, 1952). *Derived.* This is the target.
2. **Li's criterion as sums of squares.** RH holds if and only if λ_n >= 0 for all n, where λ_n = Σ_ρ [1 − (1 − 1/ρ)^n] (Li, 1997). On the line, 1 − 1/ρ lies on the unit circle, so λ_n = ½ Σ_ρ |1 − e^{inφ_ρ}|^2. Off the line, λ_n eventually goes negative (Bombieri–Lagarias, 1999). So RH is exactly "the λ_n are squared norms ½‖(I − U^n)v‖^2 for a unitary U." *Derived.*
3. **The ζ-free statement.** RH holds if and only if |π(x) − li(x)| < (1/8π)·√x·ln x for x >= 2657 (Schoenfeld, 1976). Each instance is bounded counting, AC(0) per instance. Only the universal quantifier is open. *Derived.*
4. **Parity is the arithmetic twist.** RH is equivalent to Σ_{n<=x} λ(n) = O(x^{1/2+ε}), λ(n) = (−1)^{Ω(n)}. Squares cannot see λ(n), since λ(n)^2 = 1: this is Selberg's parity problem, and it is why squares give upper bounds for primes but not lower bounds. *Derived.*
5. **No slack.** The de Bruijn–Newman constant Λ is 0 (Rodgers–Tao proved Λ >= 0; RH gives Λ <= 0). RH holds with zero margin. Any successful argument must be an exact identity, not an estimate with room to spare. *Derived* (given RH, which per the Alpöge archive is now kernel-checked).

## 3. Why the Weil route, and not the sieve route

There are two kinds of problem here, and they behave differently under a twist.

- **√x-level problems** need a sign. The parity problem (2.4) is one: a lower bound for primes must see λ(n) = ±1. A Z2 twist flips that sign around a loop, and nothing built from squares can recover it. This is the sieve route, blocked since Selberg.
- **x-level problems** are already squared. The square of a twist is trivial: for a Möbius-type line bundle L, the bundle L ⊗ L has w_1 = 2w_1 = 0. A quantity at the squared level never chooses a sign, so no twist can reach it.

Weil's form W(f * f̃) is f paired with its own adjoint, and Li's λ_n are sums of squares. Both live at the x level. **We commit to the Weil route.** On it, the twist question does not arise; the only open item is the identity in Step 4. *(D, as topology and as classical reductions.)*

## 4. The plan

1. **Build** a map Φ from test functions into a function space on Γ\D_IV^5, using primes and geometry only. No ζ, no zeros. *(Design; not done.)*
2. **Land** Φ in the Bergman space, and specifically in its **trivial-character piece**: functions with f(γx) = f(x) for every γ in Γ. *(Design.)*
3. **Constraint.** The Bergman inner product is positive by construction. On the trivial-character piece, going around any loop of the quotient returns the same value, so the quotient's loops carry no twist (Section 6.1). *(D.)*
4. **Identity — the open step.** For every test function f, archimedean term included:

   W(f * f̃) = c · ‖Φ(f)‖^2,  c > 0.

   *(OPEN. Equivalent in strength to RH via 2.1. Given 2.5, it must hold exactly.)*
5. **Connect** to RH once, at the end, through 2.1 (or 2.2, or 2.3). This is the single entry point: ζ appears only here.
6. **Falsify** (Section 5) before believing anything.

## 5. Falsification checks (must be run before any claim)

A correct construction must **fail** on each of these. If it does not fail, the construction is wrong.

| Test object | Why RH fails for it | Where the construction must break |
|---|---|---|
| Davenport–Heilbronn function | Has a functional equation like ζ, but no Euler product; known zeros off the line | Φ should not exist: no Hecke equivariance, so no lift |
| Beurling generalized primes (Diamond–Montgomery–Vorhauer 2006) | Regular integer counts, but RH-type bound fails | Step 1 must use something only the true integers have (an arithmetic group Γ), so Beurling systems give no Φ |
| A planted off-line zero, σ = 0.3 | By construction | The numerical pipeline must report W < 0 for some f |

The third is the test toy 229 never had: a check that is allowed to fail.

## 6. Hostile review

We wrote the plan; here is how we would attack it. Ordered by severity.

**6.1 (narrowed) The quotient has loops.** ζ appears only through Eisenstein scattering on a quotient by an arithmetic group, so Γ cannot be dropped for RH. The corpus takes Γ = Γ(137) (Paper 103). The quotient Γ\D_IV^5 is made by gluing x to γx; a path from x to γx closes into a loop. D_IV^5 is contractible, and Γ(137) is torsion-free (principal congruence, level >= 3), so π_1(Γ\D_IV^5) = Γ: each loop is a mod-137 wrap-around.

A loop is not a twist. A twist needs a character with χ(γ) = −1 somewhere. L^2(Γ\D) splits into one piece per character; the nontrivial characters mod 137 carry L(s, χ), and ζ lives in the trivial piece, where f(γx) = f(x). There every loop returns the same value: a cylinder, not a Möbius band. **Remaining obligation:** prove Φ lands in the trivial piece. This is a condition on how Φ is built, not a topological obstacle. *(Was "fatal" in v0.1; narrowed after review.)*

**6.2 (serious) Step 4 is RH.** By 2.1, the identity in Step 4 implies RH, and under RH some such identity exists trivially (one basis vector per zero). The plan is a relocation, not a reduction in difficulty. Its value depends entirely on whether D_IV^5 supplies something new for Step 4, especially at the archimedean term.

**6.3 (serious) Prior art at the archimedean place.** Connes and Consani (2020) study Weil positivity at the single archimedean place, inside the Hilbert-space framework of the semi-local trace formula. Any claim that D_IV^5 handles the archimedean term must be compared with theirs and shown to do something they cannot. *(Check their exact support restrictions before citing specifics.)*

**6.4 (serious) Domains: Connes's near miss.** Connes's adele class space already gives a spectral realization of the zeros, but positivity was not obtained there. Bergman positivity is automatic only for vectors genuinely in the space. If Φ(f) leaves it for some f (growth at the cusps, failed convergence near the boundary), positivity is lost exactly there. Domain questions are where this will be won or lost.

**6.5 (moderate) The spectral gap.** If any step routes through Laplacian eigenvalues, A*A-positivity gives λ >= 0, but RH needs λ >= ¼ (Selberg's exceptional eigenvalues). The Weil form avoids this; a Laplacian route does not.

**6.6 (moderate) Heuristics are not evidence.** Kleiner–Leeb (asymptotic cones of symmetric spaces are buildings) and the Ihara/Ramanujan analogy (adjacency spectra, Lubotzky–Phillips–Sarnak) motivated "the infinity is the projection." Asymptotic cones are rescaling limits and discard spectral data. Neither supplies an adjacency operator whose spectrum is the zeros. Tier: motivation only.

**6.7 (moderate) Circularity hygiene.** The explicit formula has primes on one side and zeros on the other. Step 1 must never use the zero side. A reviewer will check every definition in Φ for a hidden dependence on the zeros, and on ζ beyond the Euler product.

## 7. Moved out of the RH case: the boundary Z2 and GRH

The Shilov boundary of D_IV^5 is (S^4 × S^1)/Z2, with Z2 acting antipodally on both factors. The antipodal map reverses orientation on S^4 and preserves it on S^1, so the quotient is **non-orientable**. *(D, as topology.)*

The archimedean parity of an L-function is χ(−1): even characters carry Γ(s/2), odd characters carry Γ((s+1)/2). ζ has the trivial character, which is even, so there is no archimedean flip for RH itself. We conjecture the boundary Z2 is the geometric form of the odd-character parity, which makes it relevant to GRH for odd χ, not to RH. *(OPEN. A hunch.)* Even there, by Section 3, the Weil route works at the squared level, where a twist cancels.

## 8. What is not claimed

We do not claim a proof of RH. We do not claim Step 4. We do not claim the Z2 is the odd-character parity. We claim a precise reformulation: if Step 4 holds on the trivial-character piece, RH follows by a known theorem, and every other step is design, classical topology, or a cited theorem.

## 9. Verdict and next steps

The plan isolates RH to one exact identity (Step 4), at the squared level, on the trivial-character piece of the Bergman space of Γ(137)\D_IV^5, with three tests a correct construction must fail.

Proposed order of work:
1. Write down Φ on paper and check that it lands in the trivial-character piece (6.1).
2. Read Connes–Consani (2020) for the archimedean term (6.3).
3. Only then, a numerical toy: a truncated Φ, compared with W for a family of test functions, with the planted off-line zero and Davenport–Heilbronn as mandatory failing controls. No hard-coded `True`.

## 10. Open items for Keeper

- **Paper 84 vs K1785.** Paper 84 places dark matter in the continuous spectrum on Γ(137)\D_IV^5, which makes the quotient physical. K1785 rules Γ "a declared regulator, present for the number-theory sector, absent from the physical Hilbert space." Both cannot stand as written: either dark matter needs a Γ-free account, or Γ is not purely a regulator.
- **Toy 229.** `play/toy_229_DIV_classification.py`: nine of twelve checks are hard-coded `True`, and the m_s loop never uses m_s. The "12/12 pass" cited in `notes/BST_Geometry_and_Riemann_an_AC_Attempt.md` should be withdrawn, or the toy rebuilt with failing controls.
- **AC Step 3.** `notes/BST_RH_AC_Proof.md`, Step 3, labels Maass–Selberg positivity "a definition, depth 0." It is a theorem that holds whether or not RH is true, and the positivity equivalent to RH (Weil's) is not a definition. Relabel Step 3 as the open item; consider Schoenfeld's form (2.3) as the AC(0) statement of RH.

## Appendix A. AC depth and proof complexity (conjecture, separate from the RH plan)

**The question.** Section 9 says the RH proof must have one shape: definitions (depth 0), one exact identity (all the depth), positivity of a norm (depth 0, free). That raises a broader question: is AC depth the exponent in proof complexity? Roughly, does a proof of AC depth d have length that grows like n^d?

**Why it is plausible.** AC separates *definitions* (named, not iterated) from *counts* (iterated, recursed on). That separation is how recursion and loops become polynomial. The field of implicit computational complexity has theorems of exactly this shape:
- **Bellantoni–Cook safe recursion (1992):** split each function's arguments into "normal" ones (recursed on, i.e. counted) and "safe" ones (values passed along, never recursed on). Recursion under that discipline defines exactly the polynomial-time functions. The definition/count split is what keeps loops polynomial.
- **Leivant's ramified recurrence (1990s):** data is stratified into tiers, and recursion may only consume a lower tier. The nesting of tiers bounds the degree of the polynomial. *(Check the exact degree statements before citing.)* This is the closest known analog of "depth is the exponent."

**The warning.** In proof complexity proper, depth and length trade off in the opposite direction. In bounded-depth Frege systems ("AC⁰-Frege," named from circuit complexity), the pigeonhole principle has short proofs without a depth limit, but needs exponentially long proofs at any fixed depth (Ajtai; Beame–Impagliazzo–Pitassi; Krajíček), and allowing depth d+1 can shrink proofs exponentially. So if AC depth is to be the exponent, it must measure chained steps after the coordinates are fixed, not formula depth.

**Naming collision.** BST's AC (Arithmetic Complexity) and circuit complexity's AC⁰ are different things. A referee will notice; the paper should say so in its first paragraph.

**How to test it.**
1. Define AC depth precisely enough to compute: what counts as one level, what counts as a count.
2. Pick a proof system and examples with known proof lengths (pigeonhole, parity, small Ramsey statements). Check whether length grows like n^depth, like exp(depth), or neither.
3. Measure a real proof: trace the dependency graph behind `riemannHypothesis` in the Alpöge archive, take the depth of its longest chain, and compare it with its 17.4M lines.

*(Tier: OPEN conjecture. The Bellantoni–Cook and Leivant results are D; their connection to AC depth is a hunch until step 1 is done.)*

### A.1 The geometric reading: AC is geometry measured by construction

**Casey's statement (Nov 28, 2026):** AC is geometry forming the space that the proof, or construction, measures. Complexity is incorrect construction; the proof is the measure of the simplest construction.

**Precedent.** Homotopy type theory reads the same idea formally: types are spaces, proofs are paths between points, and a proof that two proofs agree is a path between paths (a homotopy). Building a proof is building geometry, and proofs have dimension. A possible dictionary:
- **definitions** are the points and the space itself, the coordinates;
- **counts** are paths through that space;
- **depth** may correspond to homotopy level (propositions, sets, groupoids, each one dimension up). *(Hunch.)*

This sharpens the conjecture: if the right coordinates make the space simple (low dimension, no twist), proofs in it are short paths. That is AC's "flattening." (Lean, ironically, runs on the type theory whose geometric reading this is.)

**What survives review, and what does not.**
- **"Complexity is incorrect construction" holds for the removable part.** Much apparent difficulty comes from bad coordinates: Weil's conjectures before cohomology, Fermat before modularity. A better construction removes it.
- **Some complexity is intrinsic.** A counting argument shows most strings have no description shorter than themselves (Kolmogorov). And bounded-depth proofs of the pigeonhole principle are provably long, whatever the construction. So the honest form of the thesis is: *observed complexity = coordinate-induced (removable) + intrinsic (a floor).* AC's claim is that the first part dominates for the problems we care about.
- **"The proof measures the simplest construction" is right, but the measure cannot be computed in general.** The length of the shortest description is Kolmogorov complexity, which Chaitin showed is uncomputable and, beyond a fixed bound, unprovable for specific objects. This is the Gödel trichotomy in quantitative form: the simplest construction exists, but no algorithm finds it for every problem. AC can measure the depth of a proof it has; it cannot certify that a shorter construction does not exist.

*(Tier: the HoTT, Kolmogorov and Chaitin results are D. The dictionary between them and AC depth is OPEN.)*

### A.2 Positioning: existing hierarchies of geometric spaces for proofs

AC is not the first hierarchy that reads proofs as geometry. Four exist, each well developed. AC must say where it sits among them.

1. **Homotopy levels (Voevodsky).** Proof spaces ranked by dimension: contractible (one point), propositions (any two proofs equal), sets (equality is yes/no), groupoids (proofs of equality carry structure), up to ∞-groupoids. Grothendieck's homotopy hypothesis identifies these with spaces, built one layer at a time (Postnikov towers, one homotopy group per level).
2. **Arithmetic and Borel hierarchies — the closest match.** Logic ranks statements by alternations of unbounded quantifiers (Σ_n, Π_n). Topology ranks sets by alternations of open and closed operations (Borel classes). Effective descriptive set theory shows these are one hierarchy, read two ways. RH is Π_1: a single "for all" over a checkable statement (Schoenfeld's form, 2.3).
3. **Stone duality and topos theory.** Logics correspond to spaces: classical propositional logic to Stone spaces, intuitionistic logic to open sets (Tarski), whole theories to classifying toposes (Grothendieck, Lawvere). A theory is a space.
4. **Reverse mathematics.** Theorems ranked by the axioms they need (RCA_0, WKL_0, ACA_0, ATR_0, Π¹_1-CA_0). WKL_0 is compactness, König's lemma. "How much infinity does this proof need" is a measured level.

**The test question.** Does AC depth equal arithmetic/Borel level?
- **If yes,** AC inherits a century of theory and a geometric meaning: AC depth would be topological complexity of the set a statement defines.
- **If no,** the disagreements show what AC measures that is new. The likely place: arithmetic level counts quantifiers in the *statement*, while AC claims to measure the *construction*. Section 9 already separates statement depth from proof depth; this hierarchy covers the first, and AC's novelty would have to be the second.

Either outcome is worth having. The question becomes well posed once AC depth is defined (Appendix A, test step 1).

*(Tier: the four hierarchies are D. Their relation to AC depth is OPEN.)*

### A.3 Candidate definition of AC depth (test step 1)

**Casey's rule (Nov 28, 2026): counting is the only operation at AC depth 1.**

- **Depth 0 — definitions.** Naming only: objects, spaces, coordinates, added points (a point at infinity, a sentinel). A definition may not count, so it cannot hide work.
- **Depth 1 — counting.** One pass of counting over depth-0 objects. Counting is the only operation allowed at this level.
- **Depth 2 — counting over counts.** A count whose items are themselves counts, or a universal quantifier over depth-1 checks. Per Section 9 and the edge-case discussion: depth 2 = depth 1 plus edge cases not absorbed by the choice of space.

**The guard.** This rule closes the packing loophole (the `anyGeometry` problem): any step that counts costs a level, so a "definition" that secretly does work is reclassified at the depth of the work it does.

**Check against RH.** Each Schoenfeld instance (2.3), counting the primes up to x and comparing with li(x), is one count: depth 1. The universal quantifier over all x is the second level. Statement depth 2, consistent with the ≤ 2 claim. *(This measures the statement; proof depth is a separate measurement.)*

**Parallel in circuit complexity (analogy, not a theorem).** Constant-depth AND/OR circuits (AC⁰) cannot count: they cannot even compute parity (Furst–Saxe–Sipser 1984; Håstad 1986). Adding threshold, i.e. counting, gates gives TC⁰, where parity is easy. So in circuits too, counting is the one operation that defines a new level, and what it unlocks first is parity — the same λ(n) behind Selberg's parity problem (2.4). AC depth 1 looks close to "TC⁰-like": counting allowed, everything else naming. Note the naming collision again: BST's AC depth 1 is nearer circuit TC⁰ than circuit AC⁰.

**Next.** Apply this definition to the test cases in Appendix A (pigeonhole, parity, small Ramsey statements) and to the hard human proofs (finite simple groups, Fermat's chain, Four Color, Kepler), and record where each lands.

*(Tier: the circuit results are D. The definition is a PROPOSAL; its fit to known proofs is OPEN.)*

## References

- A. Weil, "Sur les 'formules explicites' de la théorie des nombres premiers" (1952).
- X.-J. Li, "The positivity of a sequence of numbers and the Riemann hypothesis," J. Number Theory 65 (1997).
- E. Bombieri, J. Lagarias, "Complements to Li's criterion for the Riemann hypothesis," J. Number Theory 77 (1999).
- L. Schoenfeld, "Sharper bounds for the Chebyshev functions θ(x) and ψ(x). II," Math. Comp. 30 (1976).
- B. Rodgers, T. Tao, "The de Bruijn–Newman constant is non-negative," Forum Math. Pi (2020).
- H. Diamond, H. Montgomery, U. Vorhauer, "Beurling primes with large oscillation," Math. Ann. 334 (2006).
- A. Connes, C. Consani, "Weil positivity and trace formula, the archimedean place," arXiv:2006.13771 (2020).
- B. Kleiner, B. Leeb, "Rigidity of quasi-isometries for symmetric spaces and Euclidean buildings," Publ. IHÉS 86 (1997).
- A. Lubotzky, R. Phillips, P. Sarnak, "Ramanujan graphs," Combinatorica 8 (1988).
- S. Bellantoni, S. Cook, "A new recursion-theoretic characterization of the polytime functions," Computational Complexity 2 (1992).
- D. Leivant, "Ramified recurrence and computational complexity I: word recurrence and polytime," in Feasible Mathematics II (1995).
- P. Beame, R. Impagliazzo, T. Pitassi, "Exponential lower bounds for the pigeonhole principle," Computational Complexity 3 (1993).
- The Univalent Foundations Program, *Homotopy Type Theory: Univalent Foundations of Mathematics*, IAS (2013).
- G. Chaitin, "Information-theoretic limitations of formal systems," J. ACM 21 (1974).
- Y. Moschovakis, *Descriptive Set Theory*, 2nd ed., AMS (2009) — arithmetic and Borel hierarchies as one.
- S. Simpson, *Subsystems of Second Order Arithmetic*, 2nd ed., Cambridge (2009) — reverse mathematics.
- P. Johnstone, *Sketches of an Elephant: A Topos Theory Compendium*, Oxford (2002) — classifying toposes.
- M. Furst, J. Saxe, M. Sipser, "Parity, circuits, and the polynomial-time hierarchy," Math. Systems Theory 17 (1984).
- J. Håstad, "Almost optimal lower bounds for small depth circuits," STOC (1986).
- BST corpus: Paper 103 (Γ(137), wall projection); Paper 84 (dark matter on Γ(137)\D_IV^5); Keeper K1785 (Γ as declared regulator).
