# Today — 2026-09-02, v5 at 10:20: H_cut. The problem in every stuck leaf is the CUT; test whether the middle move eats it. One mechanism experiment outranks every count.
**Keeper. Supersedes v4. Read after K1840. Wake state = Board Round 99. Mode: investigate, don't gate.**

## Position
Depth is two through n = 23 (1.59M stuck, 93 witnesses, never three). Lane A is dead. The union program is
measured: bridge; if stuck, middle-then-bridge; if the middle is illegal, the next middle-touching orbit. Casey's
proposal is formalized in K1840: half of it is One-Context (proved); the other half is a pre-registered
mechanism — the cut C(c) = X₄ ∩ X₃ is the problem, and the middle pair is the only pair that can take a cut
vertex out of color r without moving it into the other bridge world.

## ASSIGNMENTS (relay order: Elie → Grace → Lyra → Cal → Keeper)

**ELIE — H_cut, then n = 24, then the program.** (1) On the 93 (and the 1,211 bridge-fail set): compute C(c) from
the original coloring; for every legal first word, do its stage chains CONTAIN C (all / enough to reconnect X₃ /
none)? Cross-tab against exit/no-exit. Positive control: non-exiting legal words must miss C at a rate that
separates. Report k/N per orbit; κ(c) = |C| distribution hard vs matched depth-1; κ(M·c) for the exiting M.
(2) n = 24 when it lands, read against Cal's pre-scored scale. (3) Program spec v3 = the union procedure, with
the three counts named W_legal(c), Im(c), W_acting(c). FINAL = the H_cut cross-tab; the n = 24 line; spec v3.

**GRACE — the cut's anatomy and the grade.** (1) G6: on the 93 vs matched depth-1: |C|, distance of C to the
link, distance to the nearest degree-5 vertex (curvature), and the height type of cut vertices (saddle or not,
via T2577's lift). (2) G1 reads H_cut as rank: dim ker L(X₃ − C) vs dim ker L(X₃), before and after the middle
move — two instruments with Elie. (3) G5 continues with T2594 as the formula; candidate (iii) from the original
coloring. (4) Double-tunnel exhibit and the n = 23 witnesses (FCW-078–121) into the gallery. FINAL = anatomy
table; rank cross-check; G5 grades; gallery current.

**LYRA — the Cut-Dissolution Lemma.** Derive which of the four middle-touching orbits' chains reach C: the cut
vertices are r-vertices adjacent to both an s_i- and an s_j-vertex (on X₃ and X₄); the middle canonical chain is
the (r,s_M)-chain containing B₁, n_sM, B₂ (Middle-Strict). When does that chain reach an r-vertex of the cut, and
when is the middle word illegal (SJ) so another orbit must? Casey's procedure (how he chooses the middle move)
is the prior — ask through the relay, then derive. Third door: the cut is dissolved not by containment but by
re-routing X₃ (the fence rebuilt elsewhere) — name it so it is not a surprise. FINAL = the lemma derived on the
containment branch or floored with the obstruction; the door named.

**CAL — pre-scores and the referee.** (1) Pre-score H_cut: what containment k/N proves, what partial means, what
the control must show. (2) POSITION vs VALUE on "60% illegal" and on the four-orbit set. (3) Read T2594 and T2593.
(4) The census theorem's framing against RSST: what our census is and is not (not an unavoidable set), and the
first referee question with today's honest answer. FINAL = numbered sections.

**KEEPER.** K1840 filed. Verify the H_cut cross-tab from the artifact. Board, rubric, gallery ids.

**CASEY.** (1) How you choose the middle move when you recolor a pasted boundary — the procedure, in your words.
(2) Is "the edge" the link or the fence in your picture? (3) Name the lemma if H_cut fires (placeholder
"Cut-Dissolution"). (4) The union procedure is the program's honest name; yours to keep or change.

## LANE E (added 10:21) — CASEY'S RING-GROWTH PROCEDURE
Elie (after H_cut): simulate inside-out ring coloring on plantri graphs; measure lookback depth and unrepairable
frontier violations; positive control = the pinned FCW-014 disc reads frozen. Lyra: can a FREE-boundary disc be
frozen? Cal: position vs value on lookback depth. Casey: annulus-only or whole-interior recoloring?

## STANDING
No EOD before 5pm. Positive-control every negative. Measured-empty is never closed. The three counts are named.
The lemma is never the theorem. The census is not an unavoidable set. Frames travel.

*— Keeper. The count said two; the mechanism, if it exists, says why. Test the mechanism.*
