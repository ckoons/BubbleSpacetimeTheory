---
title: "Kempe Theory with Boundary: Relative Charge Quantization, Gluing, and the Frozen Disc"
author: "Casey Koons & Claude (Lyra, with Keeper, Elie, Grace, Cal)"
date: "2026-08-30 (drafted; clock-verified 16:53 EDT)"
status: "DRAFT v0.6 (round 17, the close) — final version of the two-day arc: the alphabet is ONE LETTER (identity + triple; stars and 6-patches gauge-equivalent to triples; complement-of-one = pure global re-signing); the exact Gauss law added (2·Area(boundary height walk) = −Σz, 240/240 — boundary winding equals enclosed flux; flux-neutrality a new necessary condition for freezing); the separator hunt CLOSED (S1–S5 dead, gauge duality dead with reason); the Hand-off Theorem in Cal's even-degree form (interior wall-degrees even via the S₄ sign homomorphism), banking pending his confirmation of the restatement. Registry: T2574–T2578 filed. INTERNAL until Casey's call. No tier claims."
target: "paper-shaped note; venue decision is Casey's, someday"
---

# Kempe Theory with Boundary
### Relative charge quantization, gluing, and the frozen disc

## Abstract

Kempe-change theory — which colorings of a triangulation reach which others by chain swaps — has
been studied on closed surfaces since Fisk (1973); the modern literature (Mohar 2007; Mohar–Salas
2009; Feghali 2023; two papers posted November and December 2025) remains on closed graphs. We
develop the relative theory: triangulated discs with pinned boundary colorings. Three results.
(1) **Relative charge quantization:** with each 4-coloring of a triangulation one associates a
±1 sign per face and an integer charge per vertex (the local degree of the coloring's simplicial
map to the tetrahedron boundary); at interior vertices the charge obeys the classical mod-3
closure and a quantization forced by degree parity; at boundary vertices the closure FAILS in a
controlled way — the charge class mod 3 equals the cyclic displacement between the vertex's two
pinned boundary neighbors. A pinned boundary coloring is thereby a charge boundary condition in
the literal sense. (2) **Gluing consistency:** when two discs are glued along a common boundary
coloring, seam displacements cancel mod 3, charges add, and the closed-surface theory re-emerges;
color-matched gluing is free for existence (Birkhoff) but Kempe dynamics composes only through
relative reachability classes. (3) **Relative reconstruction exactness:** on a pinned disc the
interior sign pattern determines the completion exactly — the ℤ₃ and translation freedoms of the
closed-surface reconstruction are anchored by the boundary, and simple connectivity kills
monodromy. As a first exercise we exhibit a 19-vertex disc with Eulerian interior admitting two
completions that are each relatively frozen (no legal move) and mutually unreachable — showing
that Kempe-connectivity theorems for closed Eulerian triangulations do not transfer to Eulerian
regions with boundary. (4) **Boundary incompleteness (witnessed):** the two frozen completions
have identical charge vectors and sign patterns congruent modulo the full relative move span
(computed exactly, dimension 17, no sampling) — no linear functional of the sign data
distinguishes them, so the sign-coset invariant, which is candidate-complete on the closed
sphere, is PROVABLY incomplete on discs. (5) **Non-monotonicity of freezing under deletion:**
puncturing can unfreeze — a 9-vertex closed example whose coloring space splits into two
mutually unreachable classes becomes a SINGLE Kempe class after one vertex deletion. Together
(1)–(5) organize into a topology trichotomy: closed sphere — linear-complete candidate;
boundary — provably beyond linear algebra, witness in hand; higher genus — complete only with a
cohomological monodromy summand. The boundary cell is where Kempe dynamics escapes linear
algebra, and the 19-vertex disc is its Rosetta stone.

## 1. Setting and conventions

T a simple triangulation of the oriented sphere or of a closed disc; faces read
counterclockwise. Colors = Klein group V = ℤ₂×ℤ₂ = {0,a,b,c}, reference cyclic order (a,b,c).
Face sign z_t ∈ {±1}: the parity of the edge-label triple (labels = endpoint color sums) read
counterclockwise. Charge c(v) = Σ_{t∋v} z_t; winding ω(v) = c(v)/3 where defined. A Kempe swap
on a chain S adds g = p+q on S; its effect on signs is the Straddle-Flip law: z flips exactly on
faces with 1 or 2 vertices in S. For a disc, the boundary cycle carries pinned colors; a move is
legal iff its chain contains no pinned vertex.

## 2. Absolute background (closed sphere; proofs in the companion theorem note)

**Theorem A (Charge Quantization).** c ≡ 0 (mod 3) at every vertex (closed-walk winding of the
link); c ≡ deg (mod 2), |c| ≤ deg; hence ω = 0 at deg-4, ω = ±1 at deg-5 and deg-7,
ω ∈ {0,±2} at deg-6; Σ_v c(v) = 12·deg(f) with deg(f) the degree of the simplicial map
T → ∂Δ³. Odd-degree vertices admit no singleton chain (an odd link has no proper 2-coloring):
knot sites are fixed by the graph; the coloring chooses only signs.

**Theorem B (Reconstruction).** On the sphere, z determines f up to the sign-preserving color
group A₄ ≅ V⋊ℤ₃ (affine structure of V; odd color permutations flip all signs), and that group
is Kempe-realizable; so equal sign patterns imply Kempe-equivalence. On surfaces of positive
genus the reconstruction acquires an H¹(·;ℤ₃) monodromy — the room where the Mohar–Salas mod-12
classes live; the invariant theory is genus-graded.

## 3. The relative theory

**Theorem 1 (Relative quantization).** Let D be a triangulated disc with pinned boundary
coloring. At interior vertices Theorem A holds unchanged. At a boundary vertex v with fan link
u_first, …, u_last (endpoints pinned): c(v) ≡ disp(f(u_first) → f(u_last)) (mod 3), where disp ∈
{0, ±1} is the cyclic displacement in the 3-cycle of colors ≠ f(v). Legal moves change c(v) in
even steps within its pinned class.
*Proof.* The winding argument on the open fan walk: the ±1 face steps telescope to the
displacement between the endpoint colors, which are pinned; interior fan vertices are free but
alter the sum only by closed sub-loops ≡ 0 mod 3. Straddle-Flip changes each incident sign by
±2 per flip. ∎

**Theorem 2 (Gluing consistency).** Glue discs D_L, D_R along a common boundary coloring. At
each seam vertex the two fans complete the closed link, and disp_L(v) + disp_R(v) ≡ 0 (mod 3)
automatically; hence c(v) = c_L(v) + c_R(v) ≡ 0 (mod 3): the absolute closure re-emerges and
charges add along the seam. Color-matched gluing is free for existence (any two properly colored
copies of a triangle differ by a color permutation — the Birkhoff-era splitting); Kempe DYNAMICS
composes only through the relative reachability classes of the pieces.
*Proof.* The two fan walks traverse complementary arcs between the same pinned endpoints, so
their displacements are inverse; existence gluing is classical; the dynamical statement is the
definition of legality at the seam (a chain crossing the seam contains a pinned vertex). ∎

**Theorem 3 (Relative reconstruction exactness).** On a pinned disc the interior sign pattern
determines the completion exactly. *Proof.* A boundary edge's label is known and anchors the
label propagation (killing the ℤ₃ freedom); pinned colors kill the translation; the disc is
simply connected, so propagation has no monodromy. ∎

Consequently the relative Kempe-classification question is exactly the coset question for the
sign pattern modulo the span of legal straddle indicators — with no symmetry bookkeeping at all.
The **Relative Availability-Saturation Conjecture** (reachable ⟺ equal coset) is the program's
open frontier; its closed-sphere counterpart is consistent with an eight-graph exhaustive record
at the time of writing.

## 4. First exercise: the frozen disc

There exists a 19-vertex triangulated disc with all interior vertices of even degree (Eulerian
interior) and a pinned boundary coloring admitting two completions, each with NO legal Kempe
move, mutually unreachable (exhaustive check). Hence: Fisk-type connectivity for closed Eulerian
triangulations does NOT transfer to Eulerian regions with boundary; "Eulerian regions are free"
is false relatively; and any decomposition-based approach to coloring theorems must glue
DYNAMICS through relative classes (Theorem 2), not merely colors. By Theorem 3 the two
completions have distinct interior sign patterns; whether they lie in distinct cosets of the
legal-move span was decided by exact computation, with predictions lodged in a blind ledger
beforehand.

**Theorem 4 (Boundary incompleteness — witnessed).** Define W_rel intrinsically as the GF(2)
span of straddle indicators of interior chains over ALL proper colorings of the disc (no
reference to any pinning; a pinning-relative span degenerates to zero on frozen populations and
forces vacuous verdicts). For the 19-vertex disc: the two frozen completions have identical
charge vectors (interior and boundary), and their sign patterns differ by a weight-20 vector
lying IN W_rel (dim W_rel = 17, from 43 realizable interior chains, computed exhaustively).
Hence no functional factoring through the sign-coset — nor any linear functional of the charge
data — separates two mutually unreachable completions: **the sign-coset invariant is incomplete
on discs.** Combined with its closed-sphere candidacy, incompleteness is a property OF THE
BOUNDARY, not of the invariant's construction.

**Theorem 5 (Freezing is not monotone under deletion).** There is a 9-vertex sphere
triangulation whose proper 4-colorings form two mutually unreachable Kempe classes, and a vertex
whose deletion merges the coloring space into a SINGLE Kempe class (192 colorings; exhaustive).
Puncturing can unfreeze. In particular the insertion problem of the classical induction — which
lives in G−v — inhabits a strictly friendlier regime than the closed graph itself.

## 5. Open problems

1. **The separator problem (the Rosetta stone).** Theorem 4 shows the residual relative
   invariant is not linear. What computable object separates the disc twins? Candidate classes
   under pre-registered exhaustive test: invariant quadratics of the sign pattern; counting
   (shadow) invariants mod 2; ordering-obstruction certificates (Hall-type blocked multisets in
   the word problem); boundary-refined static functionals; a groupoid-cocycle analogue of the
   genus cell's monodromy summand. A total kill would itself be a theorem: the boundary
   obstruction would be genuinely dynamical, with no low-order computable shadow.
2. Characterize relatively-frozen completions (existence at 19 vertices with Eulerian interior
   is established; minimal examples? classification by boundary condition?) — and, per
   Theorem 5, characterize when deletion unfreezes.
3. The boundary-condition calculus: which charge boundary conditions (disp-vectors) admit
   completions at all; a relative existence theory beside the relative dynamics.
4. Genus-graded completeness: sign pattern ⊕ monodromy as the complete invariant off the
   sphere; the trichotomy's third cell as a theorem rather than a mechanism.
5. Gate existence as a theorem (the closed-cell forcing lemma): every stuck insertion
   configuration admits a one-vertex-support 4-word — measured at scale, unproved; the first
   rung of the word-order descent program.

## 6. The height bridge (v0.3)

The relative theory embeds in the height-function formalism of lattice statistical mechanics
(Peled–Spinka's survey is the frame). Lift the Klein colors to ℤ² by step vectors A = (1,0),
B = (0,1), C = (−1,−1) (A+B+C = 0; reduction mod 2 recovers the labels). Every properly colored
face closes all-plus or all-minus, and coherence forces adjacent faces into opposite classes —
a dual 2-coloring. Hence: **a single-valued height exists iff the triangulation is Eulerian**;
at odd-degree vertices the height acquires monodromy — the charge theory's knots are height
DISLOCATIONS, and the winding ω(v) is the Burgers datum. On a pinned disc with Eulerian
interior, the pinning determines a boundary height walk whose total slope — the TILT — is a
linear functional of the boundary word that no interior move can change: the tilt is the
residual conserved quantity that Theorem 4's twins made necessary, and "frozen ⟺ extremal tilt"
is the pre-registered mechanism under blind test at census scale. The three formalisms are one
theory at three resolutions: heights (ℤ²) → charges (mod 3: the displacement classes of
Theorem 1 are the height gradient's mod-3 shadow) → colors (mod 2). The trichotomy follows in
one stroke: closed sphere — heights exist iff Eulerian, else a dislocation gas (the charge
dynamics); boundary — the tilt, carried by the pinning, invisible to interior invariants;
higher genus — H¹ monodromy. The puncture asymmetry of Theorem 5 is explained: interior
deletion cannot relax a boundary-carried tilt, and closed spheres have no tilt to carry.

## 7. Walls, confinement, and the hand-off (v0.4)

For two completions f, f′ of one pinning, the difference field δ(v) — identity where they
agree, the transposition (f(v) f′(v)) where they differ — decomposes the disc into DOMAINS of
constant δ separated by WALLS. Two structural facts: (i) walls cannot terminate at interior
vertices (link-cycle interface parity), so every wall is closed or ends on the boundary; (ii)
dissolving a wall requires realizing a domain's transposition by chains, and for
boundary-anchored walls those chains cross the pinning — ANCHORING is the freeze mechanism.
The 19-vertex twins realize the complete picture, measured: a flat, half-crystallized boundary
(the filler, an iso-height wall — one color on a parity class ⟺ constant boundary height); the
filler color CONFINED to exactly one interior vertex (a monopole at the fixed center); two
ground-state tilings exchanged by a wall-pair hinged on the monopole. The wall is irreducibly
RELATIONAL: mod-2 sign functionals, invariant quadratics, and the full ℤ² height-sector all
take equal values on the twins (measured; the disc carries exactly three height sectors and the
twins share one). Under the mirror hypothesis (a pinning symmetry exchanging the tilings —
under census test) this blindness is forced: any functional built from the problem's data
commutes with its symmetries; the honest object is then a reachability METRIC, not an
invariant.

**Hand-off Theorem.** In the insertion problem (G−v with NO pinned vertices) no anchored wall
exists between any two colorings at any step of any rescue walk: pinnedness is a datum of the
problem, moves never create it, and anchoring requires it. The freeze mechanism witnessed by
the twins is therefore structurally unavailable exactly where the classical induction lives.
Scope, stated in the theorem's own breath: this removes a mechanism; it does not grant a move —
the existence of the rescuing gate (measured universally; dominant support three, the charge
quantum in vertex form) remains the program's open theorem, now shaped as defect dynamics: an
elementary dislocation glide adjacent to an unpinned hole.

## 8. Scope, curl, alphabet, and the hand-off (v0.5)

**Scope Theorem.** The height lift of Section 6 exists exactly on knot-free (Eulerian) domains;
on knotted domains the lift fails at every odd vertex, and the correct object is a flat
connection with structure group ℤ² ⋊ ℤ₂ (translations and the checkerboard flip), with holonomy
prescribed at the knots. Consequently: **Kempe dynamics is height dynamics precisely where
there are no knots; the residual — gate — dynamics lives at the knots.** On knot-free simply
connected domains the holonomy is trivial, which resolves the static separator program
negatively and completely: all five candidate separator families (invariant quadratics, shadow
counts, ordering-obstruction certificates, boundary-refined statics, and the holonomy cocycle —
the last by derivation, since the frozen twins' domain is knot-free) fail, and the wall's
irreducibly relational character stands as measured fact with a structural explanation-shape:
nothing static was ever going to see it.

**Gates.** The measured unsticking moves displace ZERO charge: by the Straddle-Flip calculus
their net re-signing is divergence-free at every vertex — **gates are pure curls**, and walls
are what curls move. The measured patch alphabet has five letters (complement-of-one, triples,
closed stars, 6-patches, charge-neutral singletons — the last derived: singletons exist only at
neutral vertices); whether the alphabet collapses modulo global re-signing is under test. The
open theorem of the program — Gate Existence — is now shaped as a Wall Motion Lemma: at every
stuck insertion configuration some alphabet letter applies near the hole and strictly reduces
wall-distance to a freed target.

**Hand-off Theorem (final, even-degree form; banking pending one confirmation).** The wall
system of any pair of colorings is a GRAPH; at every interior vertex its degree is EVEN (the
transition transpositions around a link cycle multiply to the identity; the S₄ sign
homomorphism forces an even crossing count — this sharpened form of the interface lemma is due
to the adversarial read, which improved the theorem it was auditing). Hence all odd-degree
wall-graph vertices — in particular all endpoints — lie at topological boundary, and anchoring
requires pinnedness, which no dynamical move (Constraint Persistence) and no proof operation
(Surgery Persistence: deletion, WLOG edge-addition, restriction) can create. For the insertion
problem (G−v, no pinned vertices), quantified over ALL pairs: no wall component is anchored.
The freeze mechanism witnessed on the disc is structurally unavailable throughout the classical
induction. Scope carved into the statement: the theorem removes a mechanism and does not grant
a move (the Wall Motion / Triple Lemma is the successor obligation — the alphabet's one letter,
a three-vertex pure-curl patch, conjectured to always apply near an unpinned hole with strict
wall-distance descent); walls may branch and cross at even interior degree, and nothing
downstream may assume simple curves; and the theorem does NOT protect pinned-seam proof
architectures, where the freeze mechanism genuinely operates — the disc is the permanent
witness for both halves of that sentence.

**The Gauss law (exact, 240/240).** For every completion of every filler pinning measured:
2·Area(boundary height walk) = −Σ_t z_t — the boundary winding reads the enclosed total flux
exactly. Flux-neutrality of the pinning is thereby a new NECESSARY condition for freezing
(all 15 frozen pinnings are flux-neutral; so are 220 free fillers — sufficiency remains open:
filler ∧ flux-neutral ∧ something finer).

## Acknowledgments and provenance

Built in one day by the BST 4-Color working group: the disc counterexample and exhaustive checks
(Elie, Y4); the population-import flag that predicted the failure before it was built on
(Cal, 5th flag); relative quantization, gluing, and exactness (Lyra, M3/N2); literature
verification that the relative object is novel (Keeper); gallery curation (Grace). The absolute
charge machinery descends from Fisk (1973) and Mohar–Salas (2009); the relative theory appears
to be new.

— internal draft; nothing here is banked until the standing review chain (Cal cold-read, toy
verification, Casey's word) completes.
