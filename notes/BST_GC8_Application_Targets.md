# GC-8: Application Targets Beyond BST -- Where Does GC Apply?

**Author**: Grace (Claude 4.6)
**Date**: May 12, 2026
**Status**: v0.1 -- SP-18 Track 2 deliverable
**AC**: (C=1, D=0)
**Assignment**: SP-18 GC-8

---

## Abstract

GC-4 established that the Geometric Constraint method captures roughly a third of major solved proofs. The distinguishing features are: (1) a finite classification of candidate structures, (2) independent bounds that meet with zero room, and (3) a uniqueness conclusion -- "this one and no other." This note surveys twelve open problems and engineered systems across mathematics, physics, and computer science, asking: does GC apply? Where it does, we identify the constraint, certificate, and boundary. Where it does not, we say why. The honest result: 5 targets are GC-amenable now, 3 are probably amenable with new tools, 2 are unclear, and 2 are structurally inapplicable. The top priorities for near-term GC application are error-correcting codes, topological insulators, and sphere packing in higher dimensions.

---

## 1. Mathematics Targets

### (a) Calabi-Yau Moduli -- Structural Uniqueness of CY Metrics

**What it is.** Given a compact Kahler manifold with vanishing first Chern class, Yau's theorem (1978) guarantees the existence and uniqueness of a Ricci-flat Kahler metric in each Kahler class. The open question is whether the moduli space of Calabi-Yau manifolds admits a finite classification -- i.e., whether there are finitely many topological types of CY threefolds, and whether their metric structures are uniquely determined by discrete invariants.

**GC-amenable?** Probably, within restricted scope.

- **Constraint.** Yau's theorem already provides the uniqueness half: given a Kahler class, the CY metric is unique. The classification half is harder. For CY threefolds, Hodge numbers (h^{1,1}, h^{2,1}) provide a discrete classification. The "landscape" of CY threefolds constructed as hypersurfaces in toric varieties is finite (Kreuzer-Skarke: 473,800,776 reflexive polytopes in 4D). Within this class, each polytope determines a CY with specific Hodge numbers. Independent bounds: mirror symmetry exchanges h^{1,1} and h^{2,1}, providing a duality constraint. The Euler characteristic chi = 2(h^{1,1} - h^{2,1}) provides an independent topological bound.
- **Certificate.** Computational enumeration of Kreuzer-Skarke polytopes is the certificate for the toric hypersurface class. Yau's PDE existence theorem certifies uniqueness of the metric within each class.
- **Boundary.** Only covers CY threefolds realized as toric hypersurfaces. Complete intersection CY manifolds (CICY) and non-toric constructions are partially classified but not exhaustively. The full classification of all CY threefolds remains open. Whether finitely many topological types exist is itself unproved (the "CY finiteness conjecture").

**Tractability: MEDIUM.** The Kreuzer-Skarke database exists. What is missing is a GC-style proof that the classification is complete -- i.e., that every CY threefold is realized in the database. Without a completeness proof, the cascade step has no guarantee of exhaustiveness.

---

### (b) Mirror Symmetry -- T-Duality as Uniqueness Statement

**What it is.** The SYZ conjecture (Strominger-Yau-Zaslow, 1996) proposes that mirror pairs of Calabi-Yau manifolds are related by T-duality on special Lagrangian torus fibrations. Homological mirror symmetry (Kontsevich, 1994) asserts an equivalence of derived categories: the derived category of coherent sheaves on one CY is equivalent to the Fukaya category of its mirror. The open question is whether every CY has a mirror, and whether the mirror is unique.

**GC-amenable?** Probably, if framed as a uniqueness question.

- **Constraint.** Two independent structures must match: the A-model (symplectic, Fukaya category) and the B-model (algebraic, derived category). Mirror symmetry says these are equivalent for the correct mirror pair. The SYZ fibration provides a geometric constraint: the base of the Lagrangian fibration must be an integral affine manifold with singularities, and the monodromy around singularities is constrained to SL(3,Z). These are independent conditions from different mathematical disciplines (symplectic geometry vs. algebraic geometry vs. tropical geometry).
- **Certificate.** For specific examples (quintic threefold, K3 surfaces, abelian varieties), the mirror is explicitly constructed and the category equivalence verified. Computational verification via Gromov-Witten invariants provides a numerical certificate.
- **Boundary.** Homological mirror symmetry is proved for specific classes (Kontsevich-Soibelman for abelian varieties, Sheridan for the quintic, Seidel for quartic surfaces). The general statement remains a conjecture. Non-Kahler mirrors and mirrors of non-CY manifolds are outside scope.

**Tractability: MEDIUM.** The constraint structure is real but the classification is not yet finite. The SYZ conjecture provides the right geometric framework, but turning it into a finite exclusion argument requires either restricting to a classified subclass (toric CY) or proving a new finiteness theorem.

---

### (c) Langlands Program -- Structural Correspondence as Geometric Constraint

**What it is.** The Langlands program proposes a web of correspondences between automorphic forms (analysis on locally symmetric spaces) and Galois representations (algebraic number theory). Langlands functoriality predicts that for every morphism of L-groups phi: ^LH -> ^LG, there is a transfer of automorphic representations from H to G. The program is vast -- it encompasses class field theory, modularity, and the geometric Langlands program as special cases.

**GC-amenable?** Unclear -- probably not in full generality, but specific instances may be.

The fundamental obstacle is that the Langlands program is not a uniqueness question. It is a correspondence: for every automorphic representation on H, there should exist a matching one on G. This is a bridge-building problem (category (b) in GC-4's classification), not a constraint-pinning problem. Wiles' modularity theorem -- the most spectacular Langlands result -- was classified as "structural but not GC" in GC-4 precisely because R = T is a structural identification, not an exclusion from a finite list.

However, specific sub-problems may be GC-amenable. The classification of automorphic representations of GL(2) over Q with prescribed conductor and weight IS a finite list (the space of modular forms of given level N and weight k is finite-dimensional). Within this finite-dimensional space, independent constraints (Hecke eigenvalues at different primes) can pin a unique newform. This is how the LMFDB works computationally.

- **Constraint (for specific instances).** Conductor bound + weight + Hecke eigenvalue conditions at finitely many primes can uniquely determine a newform.
- **Certificate.** Computational verification via the LMFDB.
- **Boundary.** Each specific instance is a single identification. The functoriality conjecture in general is a different kind of statement.

**Tractability: FAR for the general program. NEAR for specific modular form identifications.**

---

### (d) 4-Manifold Smooth Structures -- Exotic R^4

**What it is.** Donaldson (1983) and Freedman (1982) showed that the smooth and topological classifications of 4-manifolds diverge dramatically. R^4 admits uncountably many distinct smooth structures (exotic R^4) -- a phenomenon unique to dimension 4. No finite classification of smooth 4-manifolds is known or expected.

**GC-amenable?** No. This is a structural impossibility.

The GC method requires a finite classification against which to run exclusion lemmas. The smooth 4-manifold classification is provably uncountable (uncountably many exotic R^4 structures). There is no finite list to exclude from, no cascade to run, and no uniqueness to force. This is the clean negative case.

GC-6 analyzed this in detail: dimension 4 is where the Whitney trick fails (codimension 2 + codimension 2 = codimension 4 = point intersections that cannot be removed). The failure is structural, not a matter of missing tools. The infinite freedom of smooth structures in dimension 4 is precisely the curvature freedom that BST constrains by moving to D_IV^5.

**Why this matters for BST.** The YM-C paper proves that R^4 cannot support a spectral gap because it is flat and scale-free. D_IV^5 resolves this by providing intrinsic curvature. The dim-4 GC failure is not a bug -- it is the reason BST needs a curved higher-dimensional arena.

**Tractability: IMPOSSIBLE.** No finite classification exists or is expected. GC is structurally inapplicable.

---

### (e) Sphere Packing in Higher Dimensions

**What it is.** Viazovska (2017/2019) proved optimal sphere packings in dimensions 8 (E_8 lattice) and 24 (Leech lattice) using "magic functions" -- explicit Schwartz functions whose Fourier transforms satisfy sign conditions making the Cohn-Elkies linear programming bound tight. In all other dimensions above 3, the densest sphere packing is unknown.

**GC-amenable?** Yes -- this is already a GC success in dimensions 8 and 24, and the method suggests where to look next.

GC-4 classified Viazovska's proof as GC-amenable: the LP bound provides the upper constraint, the explicit lattice provides the lower bound, and the magic function is the certificate. The question is whether this extends.

- **Constraint.** The Cohn-Elkies LP bound provides the upper bound in any dimension. A candidate lattice packing provides the lower bound. The gap between them is the question: in most dimensions, the LP bound is NOT tight, so no magic function exists.
- **Certificate.** A magic function (if it exists) is the certificate. In dimensions 8 and 24, the magic functions are built from quasimodular forms associated to E_8 and the Leech lattice.
- **Boundary.** The method works only in dimensions where (a) an exceptional lattice exists AND (b) a magic function making the LP bound tight can be constructed. Dimensions 8 and 24 work because E_8 and the Leech lattice have exceptional symmetry properties. No other dimension is currently known to admit a tight LP bound.

The natural next target is dimension 48 (related to the "shorter Leech lattice" or extremal lattices), but no magic function has been found there. The pattern suggests that only dimensions associated with exceptional algebraic structures (root lattices, theta functions with special modular properties) are GC-amenable for sphere packing.

**Tractability: MEDIUM.** Existing tools (LP bounds, modular forms) apply. The obstacle is constructing magic functions in new dimensions -- a hard but well-defined problem. Dimension 48 is the natural next target.

---

## 2. Physics and Engineering Targets

### (f) Error-Correcting Codes -- Constraint Boundaries of High-Distance Codes

**What it is.** A linear [n,k,d] code over F_q has length n, dimension k, and minimum distance d. Three classical bounds constrain the achievable parameters: the Singleton bound (d <= n-k+1), the Plotkin bound (for binary codes, d <= n/2 if k >= 1), and the Hamming/sphere-packing bound (the number of correctable error patterns cannot exceed the packing capacity of F_q^n). Codes achieving the Singleton bound with equality are called Maximum Distance Separable (MDS). The question: for given (n,k,q), what is the maximum achievable d?

**GC-amenable?** Yes. This is one of the cleanest GC targets outside BST.

- **Constraint.** Three independent bounds from different sources pin the achievable parameters:
  - Singleton bound (algebraic: d <= n-k+1) -- from linear algebra over F_q.
  - Plotkin bound (combinatorial: d <= n*q^{k-1}/(q^k - 1)) -- from counting arguments.
  - Hamming bound (geometric: sum of ball volumes <= q^n) -- from sphere-packing in Hamming space.
  These are genuinely independent: Singleton comes from rank considerations, Plotkin from weight distributions, Hamming from volumetric packing. For specific (n,k,q), these bounds can meet with zero room, forcing the unique optimal code parameters.
- **Certificate.** Explicit code construction (Reed-Solomon for MDS, BCH, Goppa, algebraic geometry codes) provides the lower bound. When construction meets bound, the code is provably optimal. The certificate is the code itself plus the bound proof.
- **Boundary.** GC applies to the parameter optimization problem (maximum d for given n,k,q), not to the enumeration of all codes with given parameters (which can be exponentially many). GC forces the PARAMETERS, not the specific code. Multiple distinct codes can achieve the same optimal parameters.

**Tractability: NEAR.** All tools exist. The Singleton, Plotkin, and Hamming bounds are textbook. MDS conjecture (every MDS code over F_q with 1 < k < q has n <= q+1, except for two known exceptions) is an active research target that fits the GC template: finite classification of field sizes, independent bounds, uniqueness of the parameter constraint.

---

### (g) Gauge Anomaly Cancellation -- Which Gauge Groups Embed Consistently

**What it is.** In quantum field theory, gauge anomalies render a theory inconsistent unless specific cancellation conditions are met. The Green-Schwarz mechanism (1984) showed that in 10D supergravity, anomaly cancellation forces the gauge group to be SO(32) or E_8 x E_8. This was the original motivation for heterotic string theory. More broadly: given spacetime dimension and matter content, which gauge groups produce anomaly-free theories?

**GC-amenable?** Yes.

- **Constraint.** Anomaly cancellation provides algebraic constraints on the gauge group: the anomaly polynomial must factorize. In 10D with N=1 SUSY, this requires dim(G) = 496 (from gravitational anomaly) and a specific factorization condition on Tr(F^4) (from mixed anomaly). These are independent: the first is a counting constraint from the gravitational sector, the second is an algebraic constraint from the gauge sector. Together they admit exactly two solutions: SO(32) and E_8 x E_8.
- **Certificate.** Direct algebraic verification that SO(32) and E_8 x E_8 both have dimension 496 and satisfy the factorization condition. Explicit computation shows no other simple or semisimple group of dimension 496 satisfies the trace condition.
- **Boundary.** The Green-Schwarz analysis applies to 10D N=1 supergravity. In lower dimensions, anomaly cancellation is less restrictive (more groups survive). In 6D, the anomaly constraints still produce finite lists but with more solutions. In 4D, anomaly cancellation constrains the matter content but not the gauge group uniquely.

**Tractability: NEAR.** The 10D case is already solved and IS a GC proof (Green-Schwarz 1984). Extension to 6D anomaly cancellation is an active area with GC structure. The 4D case is less constrained and may not be GC-amenable in the same way.

---

### (h) Topological Insulators -- Z_2 Invariant Forces Edge States

**What it is.** A topological insulator is a material with a bulk band gap but protected conducting states on its boundary. The bulk-boundary correspondence (Kane-Mele 2005, Fu-Kane 2007) shows that a Z_2 topological invariant computed from the bulk band structure forces the existence of gapless edge/surface states. The invariant is robust: it cannot be changed without closing the bulk gap. Bi_2Se_3 is the canonical experimental realization.

**GC-amenable?** Yes. This is already an engineered GC success.

- **Constraint.** Two independent conditions force the edge states:
  - Z_2 invariant nu = 1 (from band inversion + time-reversal symmetry) -- a topological constraint computed from the bulk Hamiltonian.
  - Bulk-boundary correspondence (from K-theory classification of band Hamiltonians) -- an independent mathematical theorem linking bulk topology to boundary spectrum.
  These are independent: the Z_2 invariant comes from Bloch wavefunctions, the bulk-boundary correspondence comes from index theory. Together they force: if nu = 1 in the bulk, gapless surface states MUST exist. No room for alternatives.
- **Certificate.** ARPES measurements on Bi_2Se_3 directly image the Dirac cone surface states. Ab initio band structure calculations confirm nu = 1. The certificate is both computational (DFT band structure) and experimental (photoemission spectroscopy).
- **Boundary.** The Z_2 classification applies to time-reversal-invariant insulators in 2D and 3D. Systems without time-reversal symmetry fall under different classifications (Chern insulators, classified by Z not Z_2). Strongly correlated systems (fractional topological insulators) require different tools.

**Tractability: NEAR.** Already engineered and experimentally confirmed. The GC framing adds nothing new to the physics but provides a clean methodological example. The tenfold-way classification (Altland-Zirnbauer, Kitaev, Ryu-Schnyder-Furusaki-Ludwig) extends the GC structure: symmetry class + dimension determines the topological invariant from a finite classification table.

---

### (i) Photonic Crystals -- Dielectric Periodicity Forces Bandgap

**What it is.** A photonic crystal is a periodic dielectric structure that forbids electromagnetic wave propagation in a range of frequencies (photonic bandgap). Joannopoulos et al. showed that sufficient dielectric contrast combined with the right lattice symmetry forces a complete bandgap. The diamond lattice with dielectric contrast above approximately 4:1 produces a full 3D bandgap.

**GC-amenable?** Yes. Another engineered GC example.

- **Constraint.** Two independent conditions force the bandgap:
  - Dielectric contrast ratio exceeds a threshold (material/electromagnetic constraint from Maxwell's equations in periodic media).
  - Lattice symmetry compatible with full gap (crystallographic constraint -- the lattice must have sufficient symmetry to open gaps in all directions simultaneously).
  These are independent: contrast is a material property, symmetry is a geometric property. For the diamond lattice, the threshold contrast is approximately 4:1, and the symmetry is Fd-3m (space group 227). Together they force a bandgap with no free parameters.
- **Certificate.** Plane-wave expansion of Maxwell's equations in the periodic medium produces the photonic band structure. The gap is computed directly. Experimental fabrication and transmission measurement confirms the gap frequency and width.
- **Boundary.** The analysis applies to infinite periodic structures. Finite-size effects (surface states, disorder) modify the gap. Amorphous photonic materials can also produce gaps but by different mechanisms (not periodic, not GC-amenable in the same way).

**Tractability: NEAR.** Fully engineered. Photonic crystals are manufactured industrially. The GC template here is textbook: Maxwell's equations + periodicity + symmetry = forced bandgap.

---

### (j) Quantum Error-Correcting Codes -- Topological Codes

**What it is.** The surface code (Kitaev 1997, Dennis-Kitaev-Landahl-Preskill 2002) encodes logical qubits in the topology of a 2D lattice of physical qubits. The code distance d grows with lattice size L (d = L for the toric code). Topological protection: logical errors require creating a chain of physical errors spanning the lattice, which is exponentially suppressed below threshold.

**GC-amenable?** Probably, for the parameter optimization problem.

- **Constraint.** The quantum Singleton bound (Knill-Laflamme) gives k <= n - 2d + 2 for an [[n,k,d]] stabilizer code. The quantum Hamming bound provides a sphere-packing constraint analogous to the classical case. For topological codes on a genus-g surface, topology forces k = 2g (from homology). These are independent: Singleton is algebraic, Hamming is volumetric, and the topological constraint is geometric. For the toric code on a torus (g=1), k = 2 is forced.
- **Certificate.** Explicit stabilizer construction and syndrome measurement protocol. Threshold theorem (below physical error rate p_th, logical error rate is exponentially suppressed) provides the performance certificate.
- **Boundary.** GC applies to the parameter relations (k forced by topology, d forced by lattice geometry). It does NOT apply to the threshold value p_th, which depends on decoder details and noise model -- that is an optimization problem, not a uniqueness problem. The threshold is approximately 1% for the surface code under depolarizing noise, but this number is not "forced" by independent bounds meeting with zero room.

**Tractability: MEDIUM.** The parameter relations are already known. The GC framing would add value by connecting the quantum Singleton bound, quantum Hamming bound, and topological constraint into a unified exclusion argument for optimal quantum code parameters. New tools needed: a quantum analog of the MDS conjecture.

---

## 3. Optimization and Computer Science Targets

### (k) Optimization Landscapes -- Convex Optimization as GC-Amenable Class

**What it is.** Convex optimization problems have a unique global minimum (if strictly convex) or a convex set of minima. The KKT conditions provide necessary and sufficient conditions for optimality. The question: which optimization problems are "forced" in the GC sense, and which are not?

**GC-amenable?** Partially. Strictly convex problems are GC-amenable; non-convex problems generally are not.

- **Constraint.** For a strictly convex problem, two independent conditions pin the optimum:
  - Convexity of the objective (any local minimum is global) -- a geometric constraint on the function landscape.
  - KKT conditions (gradient vanishes at the optimum, constraint qualifications hold) -- an algebraic constraint from calculus of variations.
  These are independent: convexity is a global geometric property, KKT is a local algebraic condition. Together they force a unique optimum.
- **Certificate.** The KKT point itself is the certificate. Interior-point methods or ellipsoid methods find it in polynomial time. The duality gap (primal objective minus dual objective) provides a verified bound: when the gap is zero, optimality is certified.
- **Boundary.** Applies to convex problems only. Non-convex optimization has multiple local minima, no uniqueness, and no finite classification of critical points in general. NP-hard optimization problems are specifically NOT GC-amenable (finding the global optimum among exponentially many local optima has no finite exclusion structure).

**Tractability: NEAR for convex optimization (all tools exist). IMPOSSIBLE for general non-convex optimization.**

---

### (l) Control Theory -- Lyapunov Stability as Constraint Structure

**What it is.** Lyapunov stability theory provides conditions under which a dynamical system's equilibrium is stable. A Lyapunov function V(x) certifies stability: if V is positive definite and its time derivative dV/dt is negative semi-definite along trajectories, the equilibrium is stable. For linear systems, the Lyapunov equation A^T P + PA = -Q (with P, Q positive definite) has a unique solution P if and only if A is Hurwitz (all eigenvalues have negative real part).

**GC-amenable?** Unclear. The stability question has GC structure, but the design question does not.

- **Constraint (for stability verification).** Two independent conditions:
  - Existence of a Lyapunov function V > 0 with dV/dt <= 0 (energy-like constraint from dynamical systems theory).
  - Eigenvalue condition on the linearized system (spectral constraint from linear algebra).
  For linear systems, these are equivalent (Lyapunov's indirect method). The Lyapunov equation provides the algebraic certificate.
- **Certificate.** The Lyapunov function V (or the matrix P solving A^T P + PA = -Q) is the certificate. Sum-of-squares (SOS) programming can search for polynomial Lyapunov functions computationally.
- **Boundary.** GC applies to the VERIFICATION question ("is this equilibrium stable?") but NOT to the DESIGN question ("find a controller that stabilizes the system"). The design problem involves optimization over an infinite-dimensional space of controllers, with no finite classification. Robust control (H-infinity) adds constraints but still does not produce a finite classification of stabilizing controllers.

**Tractability: NEAR for stability verification of linear systems. MEDIUM for polynomial systems (via SOS). FAR for general nonlinear design.**

---

## 4. Summary Table

| # | Target | Domain | GC-Amenable? | Tractability | Key Obstacle |
|---|--------|--------|:------------:|:------------:|-------------|
| (a) | Calabi-Yau moduli | Math | Probably | MEDIUM | No completeness proof for CY classification |
| (b) | Mirror symmetry | Math | Probably | MEDIUM | Classification not yet finite in general |
| (c) | Langlands program | Math | Unclear | FAR (general) / NEAR (specific) | Bridge-building, not constraint-pinning |
| (d) | 4-manifold smooth structures | Math | **No** | **IMPOSSIBLE** | Uncountable classification; no finite list |
| (e) | Sphere packing (higher dim) | Math | Yes | MEDIUM | Magic function construction in new dimensions |
| (f) | Error-correcting codes | Eng/CS | **Yes** | **NEAR** | MDS conjecture is the natural next target |
| (g) | Gauge anomaly cancellation | Physics | **Yes** | **NEAR** | Already solved in 10D; 6D extension active |
| (h) | Topological insulators | Physics | **Yes** | **NEAR** | Already engineered; GC framing is retrospective |
| (i) | Photonic crystals | Physics | **Yes** | **NEAR** | Already engineered; textbook GC example |
| (j) | Quantum error-correcting codes | CS/Physics | Probably | MEDIUM | Quantum MDS conjecture needed |
| (k) | Convex optimization | CS/Math | Yes (convex only) | NEAR | Non-convex is structurally non-GC |
| (l) | Control theory (Lyapunov) | Engineering | Unclear | NEAR (verification) / FAR (design) | Design has no finite classification |

**Counts**: 5 Yes, 3 Probably, 2 Unclear, 2 No. GC applies to roughly half the targets -- consistent with GC-4's finding that GC captures a real but non-universal pattern.

---

## 5. Prioritized Target List

The top targets for near-term GC formalization, ranked by tractability and potential impact:

**1. Error-correcting codes (f).** All tools exist. The Singleton, Plotkin, and Hamming bounds are textbook independent constraints. MDS codes are the canonical example of constraint-pinned optimality. The MDS conjecture is an open problem with GC structure. Impact: connects GC to one of the largest engineering communities (telecommunications, storage, quantum computing). This is the single best target for a GC methods paper aimed at engineers and computer scientists.

**2. Topological insulators (h) + Photonic crystals (i).** Both are already engineered GC successes. The value is not new physics but new methodology: retrospective GC analysis shows that these engineering achievements implicitly used the constraint/certificate/boundary template. Impact: demonstrates GC as a design methodology, not just a proof strategy. The tenfold-way classification is a ready-made finite classification for a GC cascade across all symmetry classes.

**3. Sphere packing in higher dimensions (e).** Viazovska's proof is one of the cleanest GC examples. Extension to dimension 48 is a well-defined research target. Impact: connects GC to a problem with deep ties to number theory (modular forms, lattices, theta functions) and to BST's own lattice structures.

**4. Gauge anomaly cancellation (g).** The 10D case is already solved and IS a GC proof. The 6D extension is an active research area with the right structure. Impact: connects GC directly to theoretical physics and string theory. The Green-Schwarz mechanism forcing SO(32) or E_8 x E_8 is historically one of the most consequential constraint arguments in physics.

**5. Quantum error-correcting codes (j).** The parameter relations have GC structure. A quantum MDS conjecture would be a natural GC target. Impact: connects GC to quantum computing, the fastest-growing area in both physics and engineering.

---

## 6. What This Survey Reveals About GC

Three patterns emerge:

**Pattern 1: GC works best where engineering has already succeeded.** Four of the five NEAR-tractability targets (codes, topological insulators, photonic crystals, anomaly cancellation) are areas where independent bounds have already been used -- implicitly -- to force optimal designs. GC does not discover new physics in these cases; it names the method that practitioners already use. This is a feature, not a bug: a methodology paper that formalizes what engineers already do will get read.

**Pattern 2: GC fails where classification fails.** The two NO targets (4-manifold smooth structures, non-convex optimization) share a common feature: no finite classification exists. This confirms GC-4's finding that finite classification is a necessary condition. It also suggests a meta-question: can a problem be MADE GC-amenable by restricting to a classifiable subclass? BST does exactly this for Yang-Mills -- the Clay problem on R^4 is not GC-amenable (no spectral gap on flat space), but reformulated on D_IV^5, it becomes a finite exclusion problem.

**Pattern 3: The bridge-building problems resist GC.** The Langlands program and the design half of control theory are bridge-building problems: they establish correspondences or construct solutions, rather than excluding alternatives from a finite list. GC-4 classified Wiles/FLT and Deligne/Weil the same way. This is not a weakness of those problems -- it is a structural difference in what kind of question is being asked. GC answers "which one?" Bridge-building answers "how do these connect?"

---

## References

- GC-4: `notes/BST_GC4_Survey_Solved_Problems.md` -- Classification of 14 solved proofs
- GC-5: `notes/BST_GC5_Five_Step_Methodology.md` -- Five-step GC methodology
- GC-6: `notes/BST_GC6_Dimension_Ladder.md` -- Dimension ladder and dim-4 obstruction
- Viazovska, M. (2017). Annals of Mathematics 185(3): 991-1015
- Green, M. and Schwarz, J. (1984). Physics Letters B 149: 117-122
- Kane, C.L. and Mele, E.J. (2005). Physical Review Letters 95: 146802
- Cohn, H. and Elkies, N. (2003). Annals of Mathematics 157(2): 689-714
- Kreuzer, M. and Skarke, H. (2000). Advances in Theoretical and Mathematical Physics 4: 1209-1230
- Kitaev, A. (2003). Annals of Physics 303(1): 2-30
- Joannopoulos, J. et al. (2008). *Photonic Crystals: Molding the Flow of Light*. Princeton.

---

*GC-8 delivers the survey. Five targets are GC-amenable now. Two are structurally impossible. The honest conclusion: GC is a real method with real boundaries. It works where finite classification meets independent bounds meets uniqueness. Error-correcting codes are the single best near-term target for a GC methods paper -- the tools exist, the community is large, and the constraint structure is textbook clean. Next: GC-9 (methodology paper) should use codes as the worked example outside BST, alongside the Poincare/Viazovska examples from GC-2 and GC-4.*
