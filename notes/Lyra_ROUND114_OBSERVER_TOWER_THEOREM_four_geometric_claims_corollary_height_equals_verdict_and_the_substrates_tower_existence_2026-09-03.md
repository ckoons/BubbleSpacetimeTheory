# ROUND 114 — THE OBSERVER TOWER THEOREM (§2) and THE SUBSTRATE'S TOWER (§5)
**Lyra. Stamp (from `date`): 2026-09-03 Thursday 14:29 EDT.** Conserved Knowledge Theory. Statement for Cal's referee read; Grace 5653/5655 is the
instrument; nothing registered by me. Casey's direction of 14:03: a geometric proof that BUILDS the observers and each layer.

## 0. The one-paragraph version (DISCUSSION; Casey's sentence of 09-02 11:44)
A record is data on a surface with a local law. An observer who reads it along loops finds that some closed records are realized by
nothing — the transport around a loop comes back changed. The observer one floor up lives on the covering surface that unwinds exactly
those loops: the extra coordinate is the SHEET INDEX, an integer mod k per floor. "(x, y) insufficient, (x, y, z) sufficient" is this,
with z ∈ ℤ_k: not a bit string of advice but a floor of a tower. Each floor's new information is the previous floor's orphans; each
floor's price is log₂ of the number of sheets; the tower stops when the record is realized, and how high it goes is a property of the
surface's record, not of the reader. For the height record of a 4-colouring the tower has at most two finite floors and one infinite one,
and its height is decided by the graph alone.

## 1. Setting
S a closed oriented triangulated surface (for the four-colour work, the sphere with the graph T). A *record* on S is a cochain with a
LOCAL law (closed on every face). Its *transport* along a path is the propagation of a local completion; around a loop γ the transport
returns a monodromy Φ(γ) in a group G; Φ: π₁(S) → G is a homomorphism (the local law kills the face loops). The record is *realized*
iff Φ = 1 (T2598 for the sign record; T2603 for the sign cocycle on the cover).

## 2. Theorem (Observer Tower) — AMENDED 2026-09-03 14:5x per Cal §839 (four amendments accepted; the original text follows each). Let (S₀, R₀, G₀ = im Φ₀) be a record with monodromy and let G₀ ⊳ G₁ ⊳ … ⊳ G_r = 1 be a NORMAL SERIES of the monodromy group (the tower is relative to this series; the full derived cover is the series of length one). Define inductively:
**(i) The floor.** [Amended: floor k+1 is the cover for the kernel of the chosen QUOTIENT q_k: G_k → G_k/G_{k+1}, i.e. for Φ_k⁻¹(G_{k+1}); taking the full kernel realizes the record outright in one floor — the one-floor tautology — so a tower of several floors IS a normal series, as Cal wrote.] S_{k+1} := the covering space of S_k associated to Φ_k⁻¹(G_{k+1}) ⊆ π₁(S_k), constructed by the VOLTAGE method from the
record's own cocycle: vertices (v, g) for v ∈ V(S_k), g ∈ G_k; the edge u→w with voltage Φ_k(u→w) joins (u, g) to (w, g·Φ_k(u→w)).
It is well defined (the voltage of a face boundary is 1 by the local law, so faces lift to faces and S_{k+1} is a closed oriented
triangulated surface, χ(S_{k+1}) = |G_k|·χ(S_k) for an unbranched floor; Riemann–Hurwitz with the branch correction when the floor is
branched, as at the sign floor). The pulled-back record R_{k+1} has monodromy Φ_{k+1} = Φ_k ∘ p_* on π₁(S_{k+1}) = ker Φ_k, i.e. **the
floor kills exactly the monodromy it was built from and nothing else** — pull-back changes no local datum.
**(ii) Height.** [Amended: height is a DEFINITION relative to the chosen series. The theorem content is (a) the full derived cover always has height 1; (b) for the height record the series is FORCED in its first step — the sign layer must come first because the charge cocycle c is defined only on Σ — and NATURAL in its second (ℤ₃ ≅ P/(P ∩ Λ₀) when nontrivial, a finite quotient of the period group, taken before the infinite one).] The tower is the chain of quotients G₀ ⊇ G₁ ⊇ … and its height is the number of nontrivial floors. It is FINITE iff the
chain terminates iff the monodromy has a finite image at every stage. For the sign record of a 4-colouring (G = A₄) the height is ≤ 1
with the full derived cover (T2602 on the torus; ≤ 2 stage-wise, ℤ₃ then V). For the HEIGHT record (T2577's three resolutions) the layers
are FORCED and in this order: floor 1 the ℤ₂ SIGN cover (the branched double cover Σ, built from the face-sign 2-colouring — T2603's
first clause: the sign is a proper 2-colouring of the faces of Σ, colouring-independent); floor 2 the ℤ₃ CHARGE cover of Σ (from the
cocycle c = sign of the left face, T2603's second clause); floor 3 the ℤ² PERIOD cover (from [ω̃] ∈ H¹(Σ;ℤ²), E1), infinite, read modulo
the period lattice P. Three layers, ℤ₂ / ℤ₃ / ℤ², the tower of T2577 written as covering spaces.
**(iii) Information.** [Amended: EXACT only for a series of length one. In general floor k+1 newly realizes exactly the floor-k orphans whose monodromy image meets G_{k+1} trivially (im Φ ∩ G_{k+1} = {1}); orphans whose image meets G_{k+1} stay orphans and are realized higher — for the sign record with series A₄ ⊳ V ⊳ 1, image-12 records are not realized on the ℤ₃ floor, which is exactly why One-Floor fails at genus 2. "Realized modulo P" on the period floor is a convention. Pull-back is injective on ALL closed records, and the cover carries new closed records that are not pull-backs.] Original text: the record on floor k+1 carries, beyond the record on floor k, exactly the class that floor k could not realize: the
closed records of floor k that are orphans (Φ_k ≠ 1) become realized on floor k+1 (their pull-backs have trivial monodromy). So each
layer's information IS the previous layer's orphans — Casey's "the lower floor's substrate is the upper observer's record" — and no layer
adds anything a lower layer already had (pull-back is injective on realized records: a realized record's pull-back is realized by the
pulled-back solution, and distinct realized records pull back to distinct records).
**(iv) Cost.** [Amended: two rows. On a TRANSFER FAMILY (lattice tori along a direction) the count ratio → |H_k| is a THEOREM (T2609, Perron–Frobenius with the achievable-holonomy subgroup exhibited); on a SINGLE graph ("cost log₂ 2 + log₂ 3 on C₆₀") it is the group-order sum by definition — a POSITION, not a measured ratio.] The decision cost of floor k (closed vs realized, log₂ of the ratio, under the DW-equidistribution null) is log₂|G_k/G_{k+1}|
for a finite quotient, and the costs ADD along the tower: log₂|G₀| = Σ_k log₂|G_k/G_{k+1}|. For the sign record on one free generator:
log₂ 3 + log₂ 4 = log₂ 12 (T2600). For the height record: log₂ 2 (sign) + log₂ 3 (charge) for the finite part, and the period floor's
cost is taken modulo P (the finite quotient ℤ²/P; log₂[ℤ²:P] when P has full rank).
**Corollary (height = verdict).** [Scope, per Cal: EVERY sphere triangulation with an odd vertex — T2603 is general and pair loops generate H₁ of any branched double cover; measured on 7,037 fullerene duals + icosahedron + Errera.] For the height record on a triangulation T: floor 1 is nontrivial iff T has an odd-degree vertex (else Σ
is two copies and the tower has height 0); floor 2 is nontrivial iff [c] ≠ 0 in H¹(Σ;ℤ₃) iff T is NOT confined (T2603) — so **height 1
⟺ confined ⟺ [c] = 0, height 2 otherwise**, and the finite cost is log₂ 2 or log₂ 2 + log₂ 3. A third formulation of T2603, and one
that never looks at a colouring: the tower is built from the graph's sign 2-colouring and its charge cocycle. (Grace 5653: icosahedron
height 2, Errera height 2, C₆₀ dual height 1, dislocation-free torus height 0; 5655 on the census.)

## 3. Proof notes for the referee
- (i) is the standard voltage/derived-graph construction (Gross–Tucker), with the one non-standard clause: faces lift because the local
  law makes every face voltage trivial. The branched sign floor is the same construction on the barycentric-refined complex Grace used,
  where the refinement's charge sums to 2c per original edge (2 a unit mod 3), so the class test on the refinement is the original's.
- (ii): the chain terminates iff every image is finite; for the height record the first two images are ℤ₂ and a subgroup of ℤ₃ (both
  finite), the third is a sublattice of ℤ² (infinite unless trivial) — hence "terminates only modulo the periods" (K1854).
- (iii): pull-back preserves realizability (a solution pulls back) and reflects it exactly for the killed monodromy (the pulled-back
  record has Φ ∘ p_* = 1 iff p_*π₁(S_{k+1}) ⊆ ker Φ_k, which is the definition of the floor). Injectivity: two records with the same
  pull-back agree on every edge of S_k because p is surjective on edges.
- (iv): additivity is |G₀| = ∏|G_k/G_{k+1}| for a finite chain; the DW null is what makes the ratio of counts equal the group order
  (T2600's convention line: CONDITIONAL on the measured equidistribution; the group orders themselves are positions).
- What is NOT claimed: that every record space has a torsor (3-SAT does not — 14:03); that the tower has a bounded height for records
  whose monodromy image is infinite (the period floor is read modulo P by fiat); that the sheet index is "advice" in the Tier-I sense
  (it is a floor, and the floors are forced by the record, not chosen by the reader).

## §5 — The substrate's tower (existence; nothing fitted)
The substrate record's loop is the S¹ of the Shilov boundary (π₁ = ℤ; one winding = one unit of holonomy, registry :11127). Its floors
would be the cyclic covers of the time circle and its universal cover the action line. Run the theorem's three forced layers against
the ontology: **the sign floor.** A ℤ₂ sign layer on the time circle is a double cover in which the orientation of time is reversed on
the second sheet — the CPT-mirror sheet. BST's positive-time ontology (project_bst_pure_positive_time_ontology: the CPT mirror is
impossible; the arrow is dynamical) says that sheet does not exist: **the substrate's ℤ₂ floor is TRIVIAL by the ontology, height 0 at the
sign layer.** So the first floor that could be nontrivial is the charge floor — a ℤ₃-cover of the time circle — and the existence
question is exactly: does the substrate record carry a ℤ₃-valued charge cocycle at all? What the corpus has: the mod-3 sector exists on
the COLOURING side (T2577's middle resolution; the Heawood charge; Λ₀ the root lattice of A₂), and the substrate has N_c = 3. **Cal's
warning stands and I state it first: "3 = 3" is a number, not a map.** For the charge floor to exist on the substrate one must exhibit
(a) a record on the boundary with a local law, (b) a ℤ₃-valued cocycle on it defined from that law alone (the analogue of "sign of the
left face"), and (c) show its class is the colour charge — none of which is written. Kill of the paragraph: a substrate record with a
nontrivial SIGN floor would contradict the ontology, and a substrate charge cocycle whose quotient is not ℤ₃ would make the N_c
coincidence a coincidence. Existence status: sign floor trivial (derived from the ontology); charge floor UNDEFINED (no record written).
— Lyra
