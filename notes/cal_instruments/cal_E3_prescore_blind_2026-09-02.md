# Cal — E3 pre-score and E1/E2 kill numbers — written BLIND, before opening Section 38 / Toy 290 / Toy 293
Stamp: 2026-09-02 13:0x EDT. Frame for every number below is named in the line that carries it.

## The referee's objection to "T33 is the ∞ rung" (written before reading T33)
A complexity theorist reads the rung definition — minimal number of GLOBAL coordinates an observer supplies so that a LOCAL rule then decides — and objects at once:
1. Supplying n coordinates (the satisfying assignment itself) makes the local rule trivial (clause check). So the vantage dimension of 3-SAT is AT MOST n. "∞" is not a value this measure can take on a finite instance. The rungs 0 / 1 / ∞ are really growth classes 0 / O(1) / Θ(n) — the measure is a RATE in n, not a cardinal. Unless the definition restricts coordinates to o(n) (or O(1)), the ∞ rung is ill-typed, independent of what T33 proves.
2. "Non-localizable: no single direction extracts bits" is a statement about RANK-ONE projections (isotropy of a spread). The ∞ rung needs: for every k = o(n), no k coordinates + any local rule suffice. Isotropy of a full-rank spread does not imply that k < n coordinates fail; it implies only that any ONE coordinate carries ≤ 1/Θ(n) of the charge. Expected reading: (ii), with the charge Θ(n) being the trivial n-bit content of the assignment under a new name — unless the proof exhibits a lower bound quantified over all local rules.
3. POSITION vs VALUE: is Θ(n) forced (a counting identity over the clause structure) or read off a toy fit? If the constant in Θ(n) is measured and the exponent asserted, it is PD-shaped, not a position.
Pre-scored ruling I expect to write: (ii). What would move me to (i): a step in the proof that quantifies over all local rules and all k-sets of global coordinates — a Linial/Naor–Stockmeyer-style indistinguishability argument or an explicit lift-and-fail construction.

## E1 — kill numbers (frame: 5-connected sphere triangulations, in-frame census n ≤ 24; height lift per T2577 conventions)
- Instrument valid only if controls return: bipartite 2-coloring on a sphere → exactly 1; on a cylinder → exactly 2. Any other value: instrument invalid, no verdict.
- FAIL for rung 1 if the count of independent global constants is > 1 on ANY census member, or is non-constant in n. Expected shape if FAIL: count tracks the odd-vertex count k (every degree-5 vertex is odd; Euler forces k ≥ 12 on every member), roughly k−1 or 2(k−1) depending on the Burgers lattice. Report the (k, count) table, not a word.
- PASS only if the count is exactly 1 on every member AND controls pass. UNDECIDED if the count is 1 only after a quotient — then the quotient IS the position and must be named before PASS.

## E2 — kill numbers (frame: torus triangulations; sign record = Heawood face signs; group = A₄ ≅ V⋊ℤ₃; predicted monodromy group H¹(T²;ℤ₃) ≅ ℤ₃², order 9)
- Controls: sphere → 1 completion per record mod A₄ (Lemma R); disc with boundary → FCW-014 twins reappear. Either control missing → no verdict.
- Kill (b) fires if any realized record has completions-mod-A₄ ∉ {1, 3, 9}, in particular any count > 9.
- REFEREE ADDITION, pre-registered: "completions per REALIZED record" is the wrong coordinate for kill (a). A record realized by a coloring has trivial monodromy for that coloring's propagation, so completions-per-realized-record can be 1 everywhere on the torus while the incompleteness lives in EXISTENCE: locally-Heawood-valid sign records with ZERO completions (nontrivial monodromy obstructs closure). E2 must therefore count BOTH:
  (i) completions per realized record mod A₄;
  (ii) locally-valid (vertex-condition) records with zero completions ("orphans").
  Kill (a) fires only if (i) = 1 for all records AND (ii) = 0. If (i) = 1 everywhere but (ii) > 0, the conservation form stands with monodromy read as an existence obstruction, and the pre-registration's coordinate was wrong, not the law. Quote |group| and orbit sizes; never the ℤ₃ generator.

---
## POST-READ ADDENDUM (13:06, after Section 38 / Toy 290 / T34; the text above this rule is unchanged from hash 6f4289b0…882b)
Pre-scored (ii); found (iii). The pre-score under-called it: the anchor is not a weak statement of the rung, it is a statement about a different object (clause subsets) using a functional that is hardness-blind (XORSAT > 3-SAT) and negative below α ≈ 2.59. Keeper's 13:02 E1 amendment (rank vs odd-vertex count k) matches the E1 pre-score frame. Sweep output: cal_E3_T33_family_sweep_out.txt (sha256 b34e195c…4bdd). Ruling text: RUNNING_NOTES §826; referee log #142.
