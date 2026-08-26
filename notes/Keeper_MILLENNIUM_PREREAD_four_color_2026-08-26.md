# MILLENNIUM PRE-READ — 4-COLOR (Keeper's assignment; ≤1 page; saved so no context is load-bearing)
**Keeper, 2026-08-26. Against the frame's three-way split. Scope note: 4-Color is NOT a Clay problem;
it is the corpus's own set's fourth member and the program's best-received external artifact.**

## The estate (artifact paths, grep-located today)
`BST_AC_Millennium_Paper_Outline.md` (the synthesis paper: six Clay problems + 4-color sharing one
information-theoretic principle; **the falsifiable prediction: 4-color has DEPTH 2, with the missing
definition being the Kempe interference number ι(v)**, L24/L28/L54) · `BST_AC_Theorems.md` (Thm 91
AC(0) self-consistency across the nine engaged problems, L4090–4092; the graph-theory implications
block L4889) · `BST_AC_MIFC_Proof_Attempt.md` · `BST_AC_Resolution_Standalone.md` · the AC registry/
DepthCeiling files. External reception (banked memory): "you introduce new concepts" / "this may be
important" / "we can't determine if the proof is correct."

## Three-way split (pre-read state; VERIFY-at-review flags where marked)
- **PROVED (stands regardless):** the AC(0)/depth framework's internal theorems (Thm 91-class
  self-consistency; the depth-measure definitions) — real definitions and real lemmas about the
  measure itself. VERIFY: which lemmas have toys/registry edges vs prose-only.
- **APPROACHED (real structure, gap namable):** the 4-color proof itself. The experts' own sentence
  IS the gap: correctness not determinable by expert reading. The gap is therefore not a missing
  lemma but a missing CHECKING PATH — the proof's novel concepts (ι(v), depth-2 structure) have no
  independent verification instrument. VERIFY: does any toy compute ι(v) on real graphs? Does the
  depth-2 prediction have a can-fail exhibit?
- **COMMENTARY (label honestly):** the six-Clay-problems-one-principle synthesis framing, until each
  application carries its own per-problem tier (that's next week's main work).

## The referee-objection list, first draft
1. "ι(v) is a new definition — prove YOUR theorem is Appel–Haken's theorem" (definition-equivalence).
2. "Depth-2 is a claim about YOUR measure — why is the measure canonical?" (the K231c-class
   convention-vs-identity objection, from our own methodology).
3. "The proof isn't surveyable by us and isn't machine-checked — so it's neither kind of proof."
   **This is the fatal-unless-answered one, and it has a known answer-shape.**

## The one door worth the review's attention: MACHINE CHECKABILITY (the Flyspeck precedent)
The historical resolution of exactly this objection-class: formal verification (Gonthier's Coq proof
of 4-color 2005; Hales' Flyspeck 2014). **The review's sharpest question: can the AC(0) proof — or
its load-bearing core, ι(v) + the depth-2 reduction — be stated in Lean/Coq?** If yes even partially,
"can't determine correctness" converts to a yes/no the experts cannot refuse — and it would be the
program's first externally-undeniable artifact. Cost/feasibility is itself a review question (a CI
team is unusually well-suited to formalization labor). Open questions for Monday: (a) definition-
equivalence exhibit; (b) ι(v) computational toy status; (c) Lean feasibility scoping; (d) whether the
paper outline's six-application synthesis should be SPLIT (per-problem tiers first, synthesis last —
the genus/species discipline applied to our own outline).

*— Keeper. Saved per Casey's condition: Monday reads this note, not my memory.*

---
## ★ MILLENNIUM-CAPTURE ADDENDUM (Keeper, 2026-08-26 EOD — the Casey side-conversation, as artifact)
**Provenance: direct conversation with Casey, 08-26 midday. Monday reads THIS, not anyone's memory.**

1. **THE 1977 FACT (banked to user-memory too):** Casey's Purdue undergraduate thesis (1977, "computer
graphics" track) was the graphical tool AND mathematics back end in the portfolio Appel used for the
exhaustive proof. The reviewer of this proof's successor is the toolmaker of the original.

2. **THE AVL SHOT (Casey's, the review's new center):** the AVL double rotation is
isomorphic-or-similar to Kempe's 1879 hard case (crossing chains / Heawood failure) — "if you can map
a sort order onto the graph, the isomorphism is solid." Keeper's literature bridges, to check FIRST:
**Schnyder 1989** (planar ⟺ incidence-poset dimension ≤ 3 — the sort order is what planarity IS;
realizers = three compatible orders) · **Tait 1880** (4CT ⟺ 3-edge-coloring cubic planar — three
classes matching Schnyder's three trees) · **Felsner / Ossona de Mendez**: Schnyder woods on a fixed
triangulation form a DISTRIBUTIVE LATTICE under flips — a well-founded order ON the orders, the
natural home for the decrease measure. **The load-bearing lemma to demand before anything else:
ι(v) strictly decreases under the double swap, un-ambushable by a third chain** (Heawood's graveyard
is exactly third-chain ambushes). Conjecture to test: Kempe double-swap ↔ Schnyder flip; ι rides the
lattice. **The AVL frame PREDICTS depth-2** (doubles suffice in AVL; no triple exists) — the corpus's
depth-2 claim gets its origin mechanism, and the measure-canonicity objection its answer (ι =
rebalancing cost, canonical as AVL heights). Lean feasibility TRANSFORMS: rotation calculus + a
well-founded measure is bread-and-butter formalization (vs the 633-configuration mountain).

3. **CASEY'S UNIFICATION THESIS (adopt as the review's organizing lens):** every remaining Millennium
problem's hard core is an INDEX-EXISTENCE question — does a global sort order compatible with
locally-interfering structure exist (build the index) or provably not (no index can be built)? Two
classes: EXISTENCE (4C via Schnyder · RH via Hilbert–Pólya/the critical line as sort axis · BSD's
finite-rank order) vs NON-EXISTENCE (P≠NP · YM gap · NS blow-up control) — the non-existence half is
the hard corner (a negative over all re-indexings). Engineering ground: his log-structured DB
(position-is-index, append-only ⟹ maintaining N sort indices costs only N inserts, provably
least-cost) = the substrate commitment ontology in production form; one log, many orders = one
operator, many readings.

4. **THE PROOF-METHOD STANDARD (banked as review criterion):** contradiction is lazy unless every
term is stone-pinned; prefer EXHIBITED OBSTRUCTIONS (mutilated chessboard / Euler bridges / this
week's five floors). The CAGED form for non-existence: (i) define the index in stone · (ii) define a
loop invariant (holonomy) · (iii) ONE caged implication: index ⟹ invariant vanishes · (iv) EXHIBIT a
loop with nonvanishing invariant. Scoring question per Millennium row: does the proof exhibit its
obstruction or merely infer it?

5. **THE ARITHMETIC GROUND (Casey's observation, banked into the Curvature Principle):** "without π
you can't curve a line" — linear data is ℚ-parameterizable; curvature needs π; Lindemann 1882 makes
the disjointness a THEOREM. This IS squaring-the-circle generalized to a complexity principle;
matches T719's field structure (π = the lattice's one transcendental generator; the α story's
discrete-137/continuous-0.036 split). **P≠NP bridge candidate, the sharpest pre-read question:** the
Chomsky–Schützenberger ladder (rational GF ↔ regular · algebraic ↔ context-free · transcendental ↔
beyond) — transcendence of a landscape invariant as the exhibited obstruction to indexability.
*Which invariant of SAT is a number, and what would prove it transcendental?*

*— Keeper. Everything above exists on disk and in memory files; Monday needs no one's context.*
