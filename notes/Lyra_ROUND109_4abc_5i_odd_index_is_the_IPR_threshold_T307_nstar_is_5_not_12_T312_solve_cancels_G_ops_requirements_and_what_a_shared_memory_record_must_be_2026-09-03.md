# ROUND 109 — items 4(a), 4(b), 4(c), 5(i): existence first on each
**Lyra. Stamp (from `date`): 2026-09-03 Thursday 07:16 EDT.** Conserved Knowledge Theory lane, on Casey's recorded word; closes no
rubric cell. Item 1 (the paper) is untouched: the two swap slots are staged in
`notes/Lyra_paper_v0_2_SWAP_READY_definition_paragraph_Cal_825_and_Appendix_C_metric_finding_2026-09-03.md`.

## 4(a) The negative-defect lemma: its mod-3 half is DERIVED for adjacent dislocations, and the frame's exclusion is the isolated-pentagon threshold
Elie 5639: an odd-index drop means the centre lattice L lies in the ℤ₃-charge kernel {x + y ≡ 0 mod 3}; in frame
through n = 24 that never happens. Charge, pinned: for a lattice vector (x, y) the charge is x + y mod 3; A, B, C all
have charge 1 (A = (1,0), B = (0,1), C = (−1,−1) ↦ 1, 1, −2 ≡ 1). Along an edge the height changes by ±L(ℓ), charge
±1. So:
**Lemma (adjacent dislocations).** If two odd vertices p, q are adjacent, c_q − c_p = ±L(ℓ(pq)) has charge ±1 ≠ 0, so
L ⊄ the charge kernel and no odd-index drop exists for ANY colouring of that triangulation. ∎ (Two lines; frame-free.)
**Why the frame kills it through n = 24 (derived from the lemma + one classical fact):** every frame graph with a drop
is a fullerene dual (Elie 5632); a fullerene dual's odd vertices are its twelve degree-5 vertices; two of them are
adjacent unless the fullerene satisfies the isolated-pentagon rule, and the smallest IPR fullerene is C₆₀ (dual n = 32).
So every fullerene dual with n ≤ 24 has two adjacent dislocations and the mod-3 half is dead there by the lemma. For the
k > 12 graphs (a degree-≥7 vertex present) the same lemma applies whenever two odd vertices are adjacent — Elie can
check in one line whether every frame graph n ≤ 24 has an adjacent odd pair (predicted: yes).
**The false neighbour, predicted where the lemma stops protecting:** the C₆₀ dual (n = 32, 5-connected, degrees
{5, 6}, twelve mutually non-adjacent degree-5 vertices) is the FIRST frame graph on which an odd-index drop is not
excluded by adjacency. Prediction, can-fail and outside the census: index-3 drops (all twelve dislocations at one
charge level) either first appear at n = 32 on IPR duals, or a second mechanism excludes them there too. Positive
control: on any n ≤ 24 frame graph the adjacency test must return "adjacent pair exists" wherever 5639 found L ⊄
kernel. Nothing about n = 25; this is about n = 32 and it is a prediction, not a count.
**Status of the lemma Keeper typed ("degree ≥ 7 forces P = 2ℤ²"):** its mod-2 half is "k > 12 forbids a 2-coloured
odd set" (open; (iii) not yet run on the degree-≥7 hosts); its mod-3 half is the adjacency lemma above (derived) plus
the IPR fact (classical). The sentence that travels: *a period-lattice drop needs the dislocations to be colour-
confined (mod 2) or charge-confined (mod 3); adjacency of two dislocations kills the second outright.*

## 4(b) Casey's phase-transition conjecture — the existence check, and three seams in the corpus it stands on
**Answer:** no derivation in the corpus makes the interstasis gain per cycle an integer number of commitments; the
transition at n* = 12 is a threshold in a smooth rational sequence, and the corpus already says so (I18 §2.3:
"a crossover, not a phase transition"). Casey's conjecture is therefore not a theorem tonight and not killed either:
it needs a quantization mechanism the corpus does not have. Three seams found on the way, each checked by number:
1. **Gap vs gain.** Keeper's 17:51 "gain per cycle = 137·4/C(n+4,3) = 1.20 at n = 11, 0.98 at n = 12" is the REMAINING
   GAP in eigentones, not the gain. From T307's closed form G(n) = f_max(1 − 24/((n+2)(n+3)(n+4))), the gain in cycle n is
   137·4·[1/C(n+3,3) − 1/C(n+4,3)]: 1.245 at n = 7, 0.830 at n = 8, 0.301 at n = 11, 0.226 at n = 12. The per-cycle gain
   drops below one eigentone at n = 8, not 12. "Gap < 1 eigentone" ⟺ "gap < α" is the ORIGINAL definition of n* (I18
   eq. at line 19) restated in new units — a restatement, not a new fact.
2. **T307's n* is 5, not 12 — a symbol collision, not a circularity.** T307 as registered: η_n = η_0/(1 + n/n*) with
   closed form G(n) = f_max(1 − 24/((n+2)(n+3)(n+4))). Solving the recursion backwards, that closed form is exactly
   η_n = 3/(n + 5) = (3/5)/(1 + n/5): η_0 = 3/5 = N_c/n_C and n* = 5 = n_C (verified numerically, residual 0 for n = 0…7;
   T633 already says "the ratchet drives at rate 1/n_C"). So the n* in T307's INPUT is n_C = 5 and the n* = 12 of
   I18/T312 is a different quantity, the α-crossing of the output. No circularity — but the same symbol carries two
   values, and Keeper's 17:51 kill (b) was asking exactly this. Subscript them: n*_ratchet = 5, n*_coh = 12 (the C₂
   lesson, again).
3. **T312's "one solve" as typed does not produce 12.** The registered sketch sets Δ(n) = G(n)e^{−n/n*} = α and writes
   "n* = n* ln(G(n*)/α), a fixed-point equation with unique solution near 12." n* cancels: the equation reads
   G(n*) = e·α ≈ 0.0198, but G(n) ≤ f_max = 0.191 and reaches 0.02 at n ≈ 0. The 12 in the corpus comes from the
   T320 sketch's crossing 24/((n+2)(n+3)(n+4)) < 1/137 (n = 12: 0.00714 < 0.00730; n = 11: 0.00824 > 0.00730), which is
   sound arithmetic on T307's closed form. T312's own equation should be replaced by that crossing, and the T320
   sketch's citation "Section 45.3" is dangling (Section 45 of BST_AC_Theorems is the AC(0) foundation theorems).
   Keeper: three registry seams (gap/gain wording; n* overloaded; T312's solve), zero physics changes.
**What would make Casey right:** a mechanism under which commitments are counted in eigentones and the ratchet ROUNDS —
i.e., the record cannot store a fraction of an eigentone. K1293's c-function (137 − N(t), floored at C₂) is the only
candidate object and it is a Keeper note. Existence check before any derivation: is there a registered statement that
the substrate's record has integer resolution in eigentones? I found none. Until one exists, "phase transition" is
Casey's reading of a crossover, which is allowed and labelled.

## 4(c) G_ops — the existence question, stated as requirements (no number)
For the theory's decision cost to apply to D_IV⁵ the way it applies to colourings, the substrate needs an object with
four properties, none of which may be chosen to make a count come out: (1) a RECORD with a LOCAL validity law
(the analogue of Heawood closure at a vertex); (2) a finite group G_ops acting FREELY and TRANSITIVELY on the local
completions of a valid record (the torsor — for colourings, A₄ on the 12 local completions); (3) a NORMAL "value"
subgroup (the base datum the observer supplies — V, 2 bits, in colourings) with the quotient acting on labels (⟨A⟩,
the transport); (4) LOOPS to read along — a record space with π₁ ≠ 1. Keeper 07:00 is right that the causet itself has
no loops (acyclic order ⟹ holonomy trivial ⟹ every substrate record realized); the loops are the observer's, on the
Shilov boundary S⁴ × S¹/ℤ₂ with π₁ = ℤ, where |Hom(ℤ, G_ops)| = |G_ops|. So the FIRST number the theory owes for
D_IV⁵ is |G_ops|, and it must come from (1)–(3) read off the record's own local law, target-innocently. Candidates the
corpus already carries with the right SHAPE (a normal abelian "value" part with a cyclic quotient acting on it):
V ⋊ ℤ₃ = A₄ is the colouring instance; for commitments the value part is whatever the base datum of one commitment is
(P1 says one binary distinction) and the quotient is whatever relabels commitments without changing their validity.
I decline to name it today: naming it from 12 would be the target-fit the standing rules forbid, and naming it from
the record's law needs the record's law written down first — that is the existence check, and it is not done.

## 5(i) What "the operations group of a shared-memory system of N observers" would have to BE for Mednykh to apply
Mednykh counts |Hom(π₁(X), G)|. The two inputs are a SPACE X and a GROUP G, and N enters through neither directly.
For a shared-memory system the object would have to be: X = the dependency complex of the N observers' read/write
traffic on the shared memory (vertices = memory states or observers, edges = read-then-commit dependencies), whose
first Betti number b₁ counts independent closed dependency cycles; G = the finite group of operations an observer can
apply to a local memory record that preserve its local validity, acting freely on local completions. Then the shells
are 1 (b₁ = 0: no cycles — every record realized, the causet case), |G| (b₁ = 1: one dependency loop), |Hom(ℤ², G)|
(a torus: two commuting loops), and so on; N enters ONLY through b₁(X_N), the number of independent dependency
loops N observers create on shared memory. So the claim "12 / ~80 / ~8,000 are Mednykh shells" is the claim that
Tekton's dependency topology stepped b₁ = 0 → 1 → 2 → 4 at those N, with |G| = 12 and G dihedral-type. That is an
object that can be checked in logs (dependency cycles per N) before any group is fitted; without logs it is anecdotal,
and with 12 already on the board it is post-hoc (Keeper's caveat stands). What would be evidence: a step in the
cycle rank of the dependency graph at N ≈ 12 in the surviving Tekton traces. What would kill it: the same traces
showing b₁ growing smoothly with N. I fit nothing.
— Lyra
