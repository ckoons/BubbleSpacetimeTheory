# Grace — Round 137 G2: THE WEIGHT TABLE. Which space does each row sit on, does the row SAY so, and what breaks if it is the other one.
**Written 10:28 EDT 2026-09-09 on Keeper's Round 137 assignment ("this is the round's main registry artifact"). Method: every registry row was scanned for a space word (Bergman, Hardy, H², A², Szegő, Shilov, Wallach, ν, genus) — 127 rows hit. This table keeps the rows where the WEIGHT IS LOAD-BEARING, i.e. where a different weight would change the row's content. A mass-ratio row that says "Bergman" once in a name is listed only in the tail count. STATED means the row's own text names the space; INFERRED means I read it off the construction; UNSTATED means the row does not say and I did not guess.**

## 0. The ladder (subscripted, per K1769 and K1885 §3; Lyra's L1 pins Faraut–Korányi to chapter and page — until then these are the corpus's own usages, not a pinned citation)
| point | value for D_IV⁵ (n = 5, rank 2, a = n − 2 = 3) | what sits there |
|---|---|---|
| trivial | ν = 0 | the constants |
| **Wallach floor / last discrete point** | **ν_W = 3/2 = (r − 1)a/2** | T2554 puts THE MUON here ("the Wallach edge"); T2549 uses the floor to exclude Lichnerowicz negatives |
| **Hardy point** | **ν_H = n/2 = 5/2** | the Shilov boundary's space; T2562's Kostant Dirac is stated at ν = 5/2; **the commitment cost is IDENTICALLY ZERO here (Elie 5743)** |
| (in use, unexplained) | **ν = 9/2** | T2542's "divergent negative-formal-degree modes aren't states" |
| **Bergman point / genus** | **ν_B = n = 5** | the interior space A²; T752, T753, T2401; the push cost's 5/2 constant is ν_B − n/2 |
| continuous | ν > 3/2 | the scalar holomorphic series |

## 1. The rows where the weight is load-bearing
| row | space it needs | stated? | what the row would lose at the other weight |
|---|---|---|---|
| **T752** Wave Function as Bergman Coordinate | Bergman ν_B = 5 | **STATED** (in the name) | the identification IS the Bergman coordinate; at ν_H it is a different coordinate |
| **T753** Heisenberg Uncertainty from Bergman Curvature | Bergman ν_B = 5 | **STATED** (in the name) | the curvature is the Bergman metric's; another weight scales it |
| **T754** Born Rule from Invariant Measure | Bergman (the invariant measure is the Bergman one) | **INFERRED** — the row says "invariant measure" and T752's coordinate, never a weight | nothing at the level of Gleason (any infinite-dimensional H works); everything at the level of "which measure is |ψ|²" |
| **T2401** Born rule = Bergman projection (v0.1, K67-partial) | Bergman ν_B = 5 | **STATED** (kernel written K_B) | it is a statement about K_B; the Szegő kernel is a different function (this was the R135 seam) |
| **T2542** Measurement Born-weighting | uses ν = 9/2 for "divergent" modes | **STATED** (the number) | the sort is by formal degree; the 9/2 is unexplained in this table's terms |
| **T2543** Code-Forces-Fermion (the record IS an idempotent) | — | **UNSTATED** | the whole dictionary hangs off this row and it names no space; the Peirce decomposition is of the JORDAN TRIPLE, which is weight-free — so this row may be the one object in the lane that does not need a weight |
| **T2549** real spectral triple | Hardy H²(D_IV⁵), "unitary" | **STATED** | the Dirac is self-adjoint on H²; the Wallach floor does work inside the proof |
| **T2562** Kostant cubic Dirac | Hardy, **ν = 5/2 written** | **STATED** | explicitly geometry-fixed at ν = 5/2 |
| **T2554** the muon = the Wallach edge | **ν = 3/2** | **STATED** | a PARTICLE is identified with a weight |
| **T2616** Mellin-unitarity axis | Hardy ("coordinate shifts on a Hardy space") | **STATED** | the RH-lane operator class |
| **T2624** the lane's floor | **both** — "the Bergman → Hardy (Szegő) projection is K-equivariant" | **STATED** | the floor's no-energy theorem is about the MAP between the two |
| **T2625** three sectors | Hardy H²(T_Ω) | **STATED** | Paley–Wiener is a Hardy statement |
| **T2626** no boundary nucleation | Hardy H²(D_IV⁵) | **STATED** | Howe–Moore on the unitary rep |
| **T2627** the floor | Hardy (the survivor is a state on windings) | **INFERRED** — the row says "distribution on the winding count", never a weight | nothing obvious; the Schur argument is weight-free |
| **T2628** the (C) survivor | Hardy, H²(𝔻) in w = z·z | **STATED** | the survivor IS a Hardy space of the time circle |
| **T2629** the clock row | **BOTH, and that is the finding** — L1 is Hardy ("(z·z)^j is unimodular on Š"), L2 is Bergman → Hardy | **STATED, both halves, in one row** | L1 survives any weight; L2's every number is ν_B = 5's |
| **T1136** the tick | the push = Szegő projection | **INFERRED** (from the chain, not the row) | the α clause; already HELD for Cal C3 |
| **T571** Holographic–Shannon | — | **UNSTATED** | a bridge row with no space named |
| **T1918** α_G | Bergman + Szegő — the row uses **the ratio of the two kernel exponents**, (n+1)/n | **STATED** | this row already knows the two spaces differ and uses the difference as a number |
| **T2110** holographic dictionary | bulk Bergman ↔ boundary primaries | **STATED** | it is a bulk/boundary row by construction |

## 2. What the table shows, as counts (this is the artifact's finding, not an argument)
- **Rows that name a space: 127.** Rows where the weight is load-bearing: **21** (above). Of those: **STATED 16, INFERRED 3 (T754, T2627, T1136), UNSTATED 2 (T2543, T571).**
- **The QM cluster (T752, T753, T754, T2401) is BERGMAN — ν_B = 5. The record/survivor cluster (T2549, T2562, T2616, T2625, T2626, T2628) is HARDY — ν_H = 5/2.** That is Keeper's collision, confirmed row by row, and the ratio is 2.
- **But the corpus uses more than two weights.** ν = 3/2 carries THE MUON (T2554); ν = 9/2 sorts states from non-states (T2542). Counting files: "ν=3/2" in 152, "ν=5/2" in 128, "ν=9/2" in 18. **So if the Berezin reading ν = 1/ħ is inherited, the corpus does not assert two Planck constants — it asserts at least four, and one of them is a muon.** I report that as a count. Whether it is a contradiction, a rescaling, or a real handle is Lyra's L2 and Cal's C2, not mine.
- **T2543 is the load-bearing UNSTATED row**, and it may be the important one: the record-as-idempotent lives in the Jordan-triple Peirce decomposition, which is weight-free. If the record is a Jordan-algebraic object rather than a vector in a weighted space, the question "which space is the word in at the moment it commits" may be malformed — the record would not be in either. **That is a possibility the round has not listed, and it comes from the table rather than from an argument.** Cal's C3 asked what would decide the sign fork operationally; a weight-free record would dissolve the fork instead of deciding it.
- **T1918 already prices the difference between the two spaces** — it uses (n+1)/n, the Bergman/Szegő kernel-exponent ratio, as a factor in α_G. Nobody has connected that to this round. If the two-weight structure is physical, T1918 is a consumer; if it is a convention, T1918 quotes a convention as a number. Flagged, not ruled.

## 3. My own conflation, caught by building the table
This morning's T754 annotation (09:49) reads "the substrate's Hilbert space here is H²(D_IV⁵) (equivalently A²)". For the Gleason step the parenthesis is harmless — both are infinite-dimensional, which is all the hypothesis needs — but "equivalently" is exactly the identification this round is about, written by me while flagging someone else's shared-integer clause. **Repaired in the row: they are both infinite-dimensional, which is what Gleason needs, and they are NOT the same space.**

— Grace
