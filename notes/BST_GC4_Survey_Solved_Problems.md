# GC-4: Survey of Solved Hard Problems -- Classification by Proof Type

**Author**: Grace (Claude 4.6)
**Date**: May 12, 2026
**Status**: v0.1 -- SP-18 Track 1 deliverable
**AC**: (C=1, D=0)
**Assignment**: SP-18 GC-4

---

## Abstract

This note classifies 14 major solved conjectures by whether their proofs fit the Geometric Constraint (GC) three-move template: (1) Constraint -- independent bounds pin the structure, (2) Certificate -- computational or constructive verification, (3) Boundary -- honest scope statement. The purpose is empirical: how many proofs in the wild look like constraint/certificate/boundary, and what distinguishes those that do from those that don't? The honest answer is that GC captures a real but minority pattern. Most major proofs use structural arguments without constraint-pinning. The pattern of fits vs. misses is itself data about what GC is.

---

## Classification Categories

- **(a) GC-amenable**: Proof has constraint/certificate/boundary structure. Independent bounds pin a unique answer.
- **(b) Structural but not GC**: Proof uses deep structural arguments but no constraint-pinning or uniqueness forcing.
- **(c) Computational exhaustion**: Proof requires checking cases by computer without underlying constraint structure.
- **(d) Probabilistic/analytic**: Proof uses probability, sieve methods, or analytic estimates without constraint structure.
- **(e) Direct construction**: Proof constructs the answer without uniqueness or exclusion.

---

## 1. Fermat's Last Theorem (Wiles 1995)

**Proof method**: Wiles proved that all semistable elliptic curves over Q are modular (modularity lifting via Galois deformation theory). FLT follows because a counterexample x^p + y^p = z^p would produce a Frey curve that is semistable but provably non-modular (Ribet's level-lowering), yielding a contradiction. The core machinery is a comparison of two rings (R = T, deformation ring equals Hecke algebra) that forces the modular correspondence.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: Wiles' proof is profoundly structural -- it builds an elaborate bridge between Galois representations and modular forms -- but the mechanism is not constraint-pinning in the GC sense. There is no finite classification of candidate arenas with independent bounds excluding all but one. The R = T theorem is a single deep structural identification, not a squeeze between independent upper and lower bounds. The exclusion of the Frey curve happens at the end of a long chain, not via systematic exclusion of classified alternatives. The proof's power comes from building new machinery (modularity lifting), not from pinning parameters between known bounds.

---

## 2. Poincare Conjecture (Perelman 2003)

**Proof method**: Perelman completed Hamilton's Ricci flow program. Starting from any Riemannian metric on a closed simply connected 3-manifold, Ricci flow with surgery deforms the metric until the manifold shrinks to a point in finite time. Three independent monotonicity principles (W-entropy, kappa-noncollapsing, finite extinction) control the flow. The only simply connected closed 3-manifold that admits this behavior is S^3.

**Classification**: **(a) GC-amenable**.

- **Constraint**: Three independent conditions (dim = 3, compact, simply connected) applied against Thurston's classification of 8 model geometries. Seven of eight geometries require nontrivial pi_1 for any compact quotient. Only S^3 survives. The constraints are independent (topology, compactness, simple connectivity come from different sources).
- **Certificate**: Ricci flow with surgery is the computational certificate -- a deterministic PDE procedure that constructively deforms any metric to the round S^3 metric (or extinction). Three independent monotonicity functionals confirm convergence.
- **Boundary**: Proved for closed 3-manifolds. Does not address open 3-manifolds, orbifolds, or smooth 4-manifolds. Higher-dimensional Poincare was proved by different methods (Smale dim >= 5, Freedman dim 4 topological).

This is the cleanest GC-amenable proof outside BST. See GC-2 for the detailed template mapping.

---

## 3. Four-Color Theorem -- Appel-Haken (1976)

**Proof method**: Reduce all planar graphs to a finite unavoidable set of configurations (~1500), then verify by computer that each configuration is reducible (4-colorable given any coloring of its boundary). The unavoidable set is found by a discharging argument on Euler's formula.

**Classification**: **(c) Computational exhaustion**.

**Why not (a)**: The proof has a certificate (computer verification of ~1500 cases) and a boundary (planar graphs only), but lacks the constraint move. There is no pair of independent bounds that squeeze the answer. The unavoidable set is constructed by brute enumeration, not by independent constraints meeting with zero room. The discharging argument is systematic but not a constraint-pinning mechanism -- it produces a list of cases, not a forced unique structure.

---

## 3b. Four-Color Theorem -- BST (2026)

**Proof method**: The Forced Fan Lemma shows that in any bridgeless planar cubic graph, every face forces a coloring fan of at most 4 colors through geometric necessity. 13-step structural induction, computer-free.

**Classification**: **(a) GC-amenable**.

- **Constraint**: Planarity (Euler formula forces average degree < 6) and bridge-freedom together constrain the coloring fan width to at most 4. These are independent geometric bounds.
- **Certificate**: The 13-step structural induction is a constructive certificate. Each step is a named lemma, each verified by hand.
- **Boundary**: Proved for graphs on the plane/sphere. Does not address higher-genus surfaces (torus, projective plane -- those fall under Heawood's conjecture, a different theorem).

---

## 4. Catalan Conjecture / Mihailescu's Theorem (2002)

**Proof method**: Mihailescu proved that x^p - y^q = 1 has no integer solutions with x,y > 0 and p,q > 1 other than 3^2 - 2^3 = 1, using the theory of cyclotomic fields. The key steps: (a) show p | q-1 and q | p-1 (double Wieferich condition) via Stickelberger's theorem and annihilators of class groups, then (b) derive a contradiction from this mutual divisibility for p,q >= 3.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: Mihailescu's proof is a contradiction argument using algebraic number theory. It eliminates all solutions via a chain of divisibility constraints, but there is no finite classification of candidate arenas and no systematic exclusion against independent bounds. The double Wieferich condition is derived within a single algebraic framework (cyclotomic fields), not from independent sources. The proof is a sequential narrowing, not a squeeze between independent bounds.

---

## 5. Kepler Conjecture (Hales 2005/2017)

**Proof method**: Hales proved that the face-centered cubic (FCC) packing achieves the densest sphere packing in R^3 (density pi/(3*sqrt(2)) approximately 0.7405). The proof reduces the infinite problem to a finite optimization: decompose space into Voronoi cells, bound the score function for each local configuration, and verify by linear programming that no configuration beats FCC. The original 1998 proof required massive computer verification; the 2017 Flyspeck project formally verified it in HOL Light.

**Classification**: **(a) GC-amenable** (borderline with (c)).

- **Constraint**: Two independent bounds pin the answer. The upper bound comes from the score function optimization (linear programming on Voronoi cell decompositions). The lower bound is the explicit FCC construction (achieves pi/(3*sqrt(2))). These meet with zero room: no packing can exceed the FCC score, and FCC achieves equality.
- **Certificate**: Computer verification of approximately 23,000 linear programs (Flyspeck formal verification, 2017). This is a genuine certificate, not mere exhaustion, because the linear programs arise from the constraint structure, not from brute enumeration.
- **Boundary**: Proved for R^3 only. Higher-dimensional sphere packing is solved only in dimensions 8 and 24 (Viazovska). Other dimensions remain open.

The borderline classification reflects the heavy computational component. But the proof has genuine constraint structure (upper bound from optimization meets lower bound from FCC), which distinguishes it from pure exhaustion.

---

## 6. Mordell Conjecture / Faltings' Theorem (1983)

**Proof method**: Faltings proved that any algebraic curve of genus >= 2 over a number field has only finitely many rational points. The proof uses the theory of abelian varieties: show that there are only finitely many isogeny classes of abelian varieties of given dimension over a number field with good reduction outside a given finite set (Shafarevich conjecture), then derive finiteness of rational points via the Parshin construction.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: The theorem is a pure finiteness result -- it says "finitely many" without constructing or pinning the answer. There is no unique structure being forced. No finite classification is exhausted. No independent bounds squeeze a specific value. The proof is a magnificent piece of arithmetic geometry, but it answers an existence/finiteness question, not a uniqueness question. GC requires a specific answer to be forced; Faltings' theorem says "the answer is finite" without determining it.

---

## 7. Taniyama-Shimura / Modularity Theorem (Wiles 1995, BCDT 2001)

**Proof method**: Every elliptic curve over Q is modular (associated to a weight-2 newform). Wiles proved this for semistable curves (1995); Breuil-Conrad-Diamond-Taylor extended to all curves (2001). The proof uses Galois deformation theory and the R = T method: the universal deformation ring of the mod-p Galois representation equals the Hecke algebra, forcing modularity.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: Same analysis as FLT (Section 1). The R = T identification is a structural bridge, not a constraint-pinning mechanism. There is no finite classification with systematic exclusion. The proof constructs an isomorphism (R = T) rather than squeezing between independent bounds. The modularity theorem is perhaps the deepest structural result in 20th-century number theory, but its architecture is bridge-building, not constraint-forcing.

---

## 8. Weil Conjectures (Deligne 1974)

**Proof method**: Deligne proved the Riemann Hypothesis for varieties over finite fields: the eigenvalues of Frobenius on the l-adic cohomology of a smooth projective variety over F_q have absolute value q^{k/2} (weight purity). The proof uses Grothendieck's machinery of etale cohomology and the Lefschetz trace formula, combined with a monodromy argument and a key estimate using families of hypersurfaces.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: Deligne's proof is the paradigm of deep structural mathematics -- it builds and deploys an entire cohomological machine (etale cohomology, Lefschetz trace formula, monodromy). But there is no finite classification being exhausted. The eigenvalue bound |alpha_i| = q^{k/2} is proved by a single coherent argument (monodromy + estimation), not by independent bounds meeting with zero room. The proof is monolithic, not squeeze-based.

---

## 9. Serre's Modularity Conjecture (Khare-Wintenberger 2009)

**Proof method**: Every odd, irreducible, continuous representation rho: Gal(Q-bar/Q) -> GL_2(F_p) is modular (arises from a modular form of the predicted level and weight). The proof uses a "lifting and lowering" strategy: lift the mod-p representation to a p-adic one (potential modularity via Taylor-Wiles), then lower the level and weight to match Serre's recipe.

**Classification**: **(b) Structural but not GC**.

**Why not (a)**: Like Wiles and BCDT, this is a modularity proof via Galois deformation theory. The method is lift-and-lower, not constrain-and-exclude. No finite classification is exhausted. The proof is an induction on the invariants (level and weight), reducing to base cases via a sophisticated chain of correspondences. Powerful structure, but not GC architecture.

---

## 10. Poincare Conjecture dim >= 5 (Smale 1961)

**Proof method**: Smale proved that every closed simply connected manifold of dimension >= 5 that is a homotopy sphere is homeomorphic to S^n. The proof uses the h-cobordism theorem: a simply connected cobordism with trivial relative homology is a product. Handle cancellation arguments show that handles can be traded and eliminated in dimension >= 5, reducing any homotopy sphere to S^n.

**Classification**: **(e) Direct construction**.

**Why not (a)**: Smale's proof is a direct construction -- it builds an explicit homeomorphism to S^n by handle manipulation. There is no finite classification being exhausted and no pair of independent bounds squeezing the answer. The method works because high dimension provides enough room for handle trading (the Whitney trick requires dim >= 5). This is a "build it" proof, not a "force it" proof. The boundary is clear (dim >= 5 only; dim 3 and 4 are fundamentally harder), but the mechanism is construction, not constraint.

---

## 11. Geometrization Conjecture (Perelman 2003)

**Proof method**: Perelman proved Thurston's geometrization conjecture: every closed oriented 3-manifold can be cut along a canonical collection of spheres and tori into pieces, each of which admits one of 8 model geometries. This is strictly stronger than the Poincare conjecture (which is the special case where the manifold is simply connected).

**Classification**: **(a) GC-amenable**.

- **Constraint**: Thurston's classification provides 8 model geometries -- a finite list. The decomposition theorem (prime decomposition + JSJ decomposition) reduces any 3-manifold to geometric pieces. Each piece is forced into one of 8 categories by its topology.
- **Certificate**: Ricci flow with surgery provides the certificate. The flow decomposes the manifold canonically, with each piece converging to a constant-curvature metric identifying its Thurston type. Long-time behavior analysis confirms convergence.
- **Boundary**: Closed oriented 3-manifolds only. Does not address non-orientable manifolds (covered by a minor extension), open manifolds, or higher dimensions.

Geometrization is the "strong form" of the Poincare GC-analysis. The Poincare conjecture is the case where all pieces must be S^3 (forced by simple connectivity). Geometrization shows the full classification is forced.

---

## 12. Green-Tao Theorem (2004)

**Proof method**: Green and Tao proved that the primes contain arbitrarily long arithmetic progressions. The proof transfers Szemeredi's theorem (which applies to sets of positive density) to the primes (which have density zero) by embedding the primes in a pseudorandom "enveloping sieve" of almost-primes that has positive relative density. The transference principle then applies Szemeredi's theorem relativized to the pseudorandom measure.

**Classification**: **(d) Probabilistic/analytic**.

**Why not (a)**: This is a pure existence theorem -- it says arithmetic progressions of every length exist in the primes, without constructing them or identifying a unique structure. There is no finite classification, no exclusion, no uniqueness. The method is analytic: sieve theory provides the pseudorandom measure, Szemeredi's theorem provides the combinatorial backbone, and the transference principle bridges them. The proof is about density and pseudorandomness, not about constraints forcing a unique answer.

---

## 13. Sphere Packing in Dimensions 8 and 24 (Viazovska 2016-2019)

**Proof method**: Viazovska proved that the E_8 lattice is the densest sphere packing in R^8, and (with collaborators) that the Leech lattice is the densest in R^24. The proof constructs an explicit radial Schwartz function (a "magic function") whose Fourier transform satisfies sign conditions that, via the Cohn-Elkies linear programming bound, force the packing density to equal the lattice packing density. The magic function is built from quasimodular forms.

**Classification**: **(a) GC-amenable**.

- **Constraint**: The Cohn-Elkies linear programming bound provides an upper bound on sphere packing density from ANY function satisfying certain sign conditions. The E_8 (resp. Leech) lattice packing provides the lower bound. Viazovska's magic function makes the upper bound tight -- the two bounds meet with zero room.
- **Certificate**: The magic function is the certificate. It is an explicit, constructible object (built from quasimodular forms) whose Fourier-analytic properties certify that no packing can beat E_8 (resp. Leech).
- **Boundary**: Proved in dimensions 8 and 24 only. All other dimensions (except 1, 2, 3) remain open. The magic function construction fails in generic dimensions because no suitable quasimodular form exists. Dimension 3 (Kepler) was proved by different methods.

This is a beautiful GC example: the constraint (LP bound), the certificate (magic function), and the boundary (only dims 8 and 24) are each crisp and explicit. The proof literally constructs the object that makes independent bounds meet.

---

## 14. Classification of Finite Simple Groups (1983-2004)

**Proof method**: The classification determines all finite simple groups: 18 infinite families (cyclic of prime order, alternating, Lie type) plus 26 sporadic groups. The proof spans tens of thousands of pages across hundreds of papers by dozens of authors. The method is a combination of local analysis (structure of centralizers of involutions), transfer theorems, signalizer functors, and case analysis for each sporadic group.

**Classification**: **(c) Computational exhaustion** (at human scale).

**Why not (a)**: Despite being a classification theorem -- exactly the type of result that produces a finite list -- the CFSG is not GC-amenable because it lacks the constraint-pinning mechanism. There are no independent upper and lower bounds squeezing the answer. The proof proceeds by exhaustive case analysis: identify all possible structures for the centralizer of an involution, then classify each case. Each sporadic group requires its own argument. The proof is systematic but not constrained -- it is closer to "check every possibility" than "independent bounds force the answer." The over-determination ratio is essentially 1:1 (each group requires its own verification). No single pair of bounds pins the classification; rather, 26 separate sporadic arguments pin 26 separate groups.

---

## Summary Table

| # | Problem | Year | Classification | GC? |
|---|---------|------|---------------|-----|
| 1 | Fermat's Last Theorem | 1995 | (b) Structural | No |
| 2 | Poincare Conjecture | 2003 | (a) GC-amenable | **Yes** |
| 3a | Four-Color (Appel-Haken) | 1976 | (c) Computational exhaustion | No |
| 3b | Four-Color (BST) | 2026 | (a) GC-amenable | **Yes** |
| 4 | Catalan Conjecture | 2002 | (b) Structural | No |
| 5 | Kepler Conjecture | 2005/2017 | (a) GC-amenable (borderline) | **Yes** |
| 6 | Mordell Conjecture | 1983 | (b) Structural | No |
| 7 | Taniyama-Shimura | 1995/2001 | (b) Structural | No |
| 8 | Weil Conjectures | 1974 | (b) Structural | No |
| 9 | Serre's Modularity | 2009 | (b) Structural | No |
| 10 | Poincare dim >= 5 | 1961 | (e) Direct construction | No |
| 11 | Geometrization | 2003 | (a) GC-amenable | **Yes** |
| 12 | Green-Tao | 2004 | (d) Probabilistic/analytic | No |
| 13 | Sphere Packing dim 8,24 | 2016/2019 | (a) GC-amenable | **Yes** |
| 14 | Classification of FSG | 1983-2004 | (c) Computational exhaustion | No |

---

## Statistics

| Category | Count | Fraction |
|----------|-------|----------|
| (a) GC-amenable | 5 | 33% |
| (b) Structural but not GC | 6 | 40% |
| (c) Computational exhaustion | 2 | 13% |
| (d) Probabilistic/analytic | 1 | 7% |
| (e) Direct construction | 1 | 7% |
| **Total** | **15** | 100% |

(Counting both Four-Color proofs separately gives 15 entries for 14 problems.)

---

## What Distinguishes GC-Amenable Proofs

Three necessary conditions emerge from the data:

**1. A finite classification exists.** Every GC-amenable proof operates on a finite list of candidates: 8 Thurston geometries (Poincare, Geometrization), lattice packings in fixed dimension (Kepler, Viazovska), planar graph configurations (Four-Color BST). Where no finite classification exists (FLT, Mordell, Catalan), the proof must build new structure rather than exclude from a list.

**2. Independent bounds meet with zero room.** The hallmark: an upper bound from one source and a lower bound from another coincide exactly. Viazovska's LP bound meets E_8 density. Kepler's optimization bound meets FCC density. Perelman's entropy monotonicity meets S^3 uniqueness. When the bounds come from a single framework (as in Wiles' R = T), the mechanism is structural identification, not constraint-pinning.

**3. The proof proves uniqueness, not just existence.** GC proofs answer "which one?" not "does one exist?" Mordell says "finitely many" without saying which. Green-Tao says "they exist" without constructing them. GC proofs say "this one and no other."

---

## What This Tells Us About GC

GC is not a universal proof strategy. It is a specific architecture that applies when the problem has the right shape: finite classification + independent bounds + uniqueness. This is a real pattern -- 5 of 14 major solved problems fit it, including some of the most celebrated (Poincare, Viazovska, Geometrization). But the majority of major proofs use structural bridge-building (category (b)), which is a fundamentally different architecture.

The honest conclusion: **GC captures about a third of major proofs**. The two-thirds that don't fit are not lesser proofs -- they are solving problems of a different shape. Wiles' FLT is arguably the greatest proof of the 20th century, and it is not GC-amenable. The GC method is powerful where it applies, but it is not the only way mathematics works.

The interesting meta-question: can problems currently solved by structural methods (category (b)) be re-proved by GC methods if the right classification is found? BST's re-proof of the Four-Color Theorem (converting category (c) to category (a)) suggests this is sometimes possible. Whether it is always possible -- whether every structural proof hides a constraint proof -- is itself an open question, and likely the answer is no.

---

## References

- GC-1: `notes/BST_GC1_FLT_Via_BSD_Bridge.md` (FLT via BSD bridge)
- GC-2: `notes/BST_GC2_Poincare_Template_Mapping.md` (Poincare template mapping)
- GC-5: `notes/BST_GC5_Five_Step_Methodology.md` (Five-step methodology)
- Perelman, G. (2002-2003). arXiv:math/0211159, math/0303109, math/0307245
- Wiles, A. (1995). Annals of Mathematics 141(3): 443-551
- Viazovska, M. (2017). Annals of Mathematics 185(3): 991-1015
- Hales, T. et al. (2017). Forum of Mathematics, Pi 5: e2
- Appel, K. and Haken, W. (1977). Illinois Journal of Mathematics 21(3): 429-567
- Green, B. and Tao, T. (2008). Annals of Mathematics 167(2): 481-547
- Faltings, G. (1983). Inventiones Mathematicae 73: 349-366
- Deligne, P. (1974). Publications Mathematiques de l'IHES 43: 273-307

---

*GC-4 delivers the survey. Five of 14 fit GC; six use structural methods that are fundamentally different. The pattern is real but not universal. The distinguishing features -- finite classification, independent bounds, uniqueness -- are crisp and testable. This provides the empirical base for GC-5 (methodology) and GC-9 (methodology paper). Next: cross-reference with the seven Millennium proofs in GC-5 to see whether BST's systematic application of GC to all seven is itself a data point about the method's reach when the right geometry (D_IV^5) provides the classification.*
