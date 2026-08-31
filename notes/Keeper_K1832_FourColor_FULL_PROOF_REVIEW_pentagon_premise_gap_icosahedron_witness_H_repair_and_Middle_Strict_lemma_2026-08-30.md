---
title: "K1832 — Four-Color full proof review: one localized defect (the Forced Fan's pentagon premise), an exhibited witness, a named repair, and two unstated lemmas the proof needs and already almost has"
author: "Keeper"
date: "2026-08-30, Sunday morning (clock-verified 09:05 EDT at session start)"
status: "AUDIT — commissioned by Casey 08-26 (full proof review: definition-equivalence, computational status, Lean feasibility). Solo Keeper session, Casey present. Cal cold-read OWED before anything banks. Verdict below."
target_artifact: "FourColor_Standalone_Paper.md (DRAFT v9, Cal PASS May 7, JCT-B-ready under K940 re-scope banner)"
---

# K1832 — FOUR-COLOR: THE FULL PROOF REVIEW

**Provenance and blindness note.** Solo audit; I re-derived every lemma by hand against the standalone
paper before consulting any toy output, then checked consistency with the toy tables afterward. The
repairs proposed in Sections 3–4 are MINE, constructed this session, verified by no one else. Per
standing discipline (external-audit-beats-self-vigilance; the-cheat-migrates-to-the-last-prose-step),
**nothing in Sections 3–4 banks until Cal cold-reads it and the two pre-registered toys run.** I note
against myself that a "localized, repairable gap" is the finding most flattering to the program
(gift-audit hazard); the witness in Section 2 is exhibited precisely so the finding does not rest on
my judgment.

## 0. VERDICT

- **As written: FAIL as a complete proof** — one load-bearing premise is false (Section 2). The K940
  "attempt, NOT a proof" banner remains correct, and this review now says exactly WHERE and WHY,
  which the banner could not.
- **As a structure: far stronger than the banner's generic language suggests.** Seven of the eight
  lemmas verified structurally under independent re-derivation (Section 1). The defect is localized
  to ONE premise inside Lemma 8, it has an exhibited witness, and a repair exists that restructures
  two lines of the induction (Section 3). Two unstated lemmas (Section 4) close a selection loophole
  the paper does not notice and rigidify the whole τ = 6 configuration.
- **Disposition: CONDITIONAL — repairs applied → re-audit → Cal cold-read → then re-score on the
  referee metric.** My referee-count estimate as written: 8–10/10 object once any referee reads
  Lemma 8's premise carefully (the external "we can't determine if the proof is correct" suggests
  none did). With Sections 3–4 written in and toy-verified: the objection surface shrinks to
  residual-risk-of-what-I-missed, which is exactly what Cal and Lean are for.

## 1. WHAT IS STRONG (verified by re-derivation, not by reading the toy table)

Setting: G a simple planar triangulation, v a degree-5 saturated vertex, proper 4-coloring of G−v;
bridge color r twice, singletons s_1, s_2, s_3; gap ∈ {1,2}.

- **Lemma 2 (gap-1 ⟹ τ ≤ 5): SOUND.** All three sub-cases check. The Jordan separation is pinned by
  the sector argument at v: each singleton's own edge to v fixes its side of the curve, and that edge
  cannot cross the curve (shares only v with it). No wrap is possible. This is the principled fix of
  the v1 T135 error — which, for the record, was NOT a "curve wrap" (as v9's post-mortem says) but a
  **tangled ⟹ connected inference that fails for bridge pairs under the operational definition**.
  The current paper never makes that inference: Lemma 3 assumes STRICT tangling, which supplies the
  path honestly.
- **Lemma 3 (τ = 6 ⟹ τ_s ≤ 4): SOUND.** Both claims check; the vertex-disjointness of the separating
  chain (colors {r,s_A}) from the separated chain (colors {s_M,s_B}) is exact, and the contradiction
  with the singleton pair's τ = 6 tangling is clean.
- **Lemma 4 (pigeonhole): SOUND**, and in fact both non-middle bridge pairs are cross-linked, exactly.
- **Lemma 5 (Lyra's Lemma): SOUND.** The three-case split is exhaustive; Case 1's swap genuinely
  frees r (both copies flip, n_{s_i} untouched).
- **Lemma 6 (split-bridge swap exists): SOUND** given L4+L5 — but it silently needs the orientation
  fact of Section 4.2, without which "which copy is far" is not determined on the link cycle.
- **Lemma 7 (post-swap τ ≤ 5): SOUND conditional on Lemma 8.** The budget argument
  τ = τ_s + crosslinks, with strict ⟹ operationally tangled (verified: a whole-chain swap permutes
  colors without freeing any), is airtight. Old cross-links die because r becomes a singleton color
  and cross-links exist only at repeated colors (Def 9 + Remark, verified).
- **Lemma 8, cases x = r and x = s_j: SOUND.** The x = s_j case is pure link-cycle adjacency and
  needs no diagonal at all — B_far—n_{s_j}—n_{s_i} is an (s_i,s_j)-path of length 2 post-swap.
- **Definition 5's formal clause is equivalent to the informal operational definition** — I checked
  the freeing condition in both directions for bridge pairs; they match. (I raise this because I went
  in expecting a mismatch and found none; recording the null.)
- **The theorem's outer structure** (base, Euler, unsaturated, deg ≤ 4 Kempe, τ < 6 single swap,
  re-evaluation between the two swaps so no Heawood ambush) is correct.

## 2. THE DEFECT — CRITICAL, localized, with an exhibited witness

**Antecedent, verbatim (Lemma 8, Forced Fan sub-case):** *"Since G is a triangulation (any planar
graph embeds in one, and 4-coloring a triangulation suffices), the star of v consists of 5 triangular
faces. Removing v leaves a pentagon B_far(p) — n_sM(p+1) — B_near(p+2) — n_si(p+3) — n_sj(p+4),
which must be triangulated by exactly 2 non-crossing diagonals from the 5 possible."*

**The premise is false.** The coloring the induction analyzes is of **G−v** (Theorem 1, step 2:
"By the inductive hypothesis, G−v has a proper 4-coloring c"). In G−v the pentagon is an empty FACE
— v's star interior held only v and its five edges, and they left with v. Nothing triangulates the
hole. Chords among the five link vertices may exist elsewhere in the embedding (outside the
pentagon), but their count is 0, 1, or 2 — not "exactly 2."

**Witness: the icosahedron.** A simple planar triangulation; delete any vertex; the link pentagon of
G−v is chord-free — zero diagonals. The premise "must be triangulated by exactly 2 diagonals" fails
on the most symmetric triangulation in the book, the same graph the paper's own figure caption
celebrates. (The icosahedron never reaches τ = 6, so the CONCLUSION is not contradicted — but the
premise is dead, and the sub-case x = s_M has no proof without it.)

**Downstream:** without the fan edge (n_sM, n_si), the post-swap pair (s_i, s_M) has no argument
against a second cross-link, Lemma 8's bound fails, Lemma 7's budget fails, and the τ = 6 case of
the theorem is open. This is precisely the case the whole paper exists to close. The team's own
Toy 451 (τ = 6 never observed at chord-free degree-5 vertices; 31,500 colorings, 555 vertices) is
the empirical shadow of the missing lemma — the data knew the chords mattered; the proof forgot to
secure them.

## 3. THE REPAIR — the H-induction (proposed, NOT YET VERIFIED by anyone but me)

Strengthen what the induction colors. In the inductive step, do not color G−v; color

**H = (G−v) + any 2 non-crossing diagonals triangulating the pentagon hole**

(for deg(v) ≤ 4, triangulate the smaller hole likewise). H is planar with |V|−1 vertices, so the
inductive hypothesis applies; a proper coloring of H restricts to G−v; every chain, swap, τ, and
lemma is computed **in H throughout**; the final coloring of H plus the freed color at v is proper
in G (whose edges are a subset of H+v's). Then the pentagon HAS exactly two diagonals by
construction, and the three eliminations run correctly:

1. A diagonal joining the two bridge positions cannot exist in H — it would be a properly-colored
   edge with both endpoints colored r. (Read correctly: the presence of any diagonal forces its
   endpoints to differ, so the bridge never sits on a diagonal's endpoints.)
2. (B_far, n_si) present ⟹ with link edge B_near—n_si, all three in one (r,s_i)-chain ⟹ (r,s_i)
   strictly tangled ⟹ contradicts Lemma 3 (non-middle pairs are not strict at τ = 6). Eliminated.
3. (B_near, n_sj) present ⟹ with link edge B_far—n_sj, (r,s_j) strictly tangled ⟹ same
   contradiction. Eliminated.

Two of five diagonals survive; the hole needs exactly two; they share n_sM and do not cross; both
are present — **the fan is forced in H, and the swap cannot touch either fan edge** (neither
endpoint is in the swap chain). Lemma 8's conclusion then holds in H, and everything downstream
survives unchanged. I stress-tested the restructure against every lemma and both swap stages;
I found no leak. **That sentence is exactly as strong as one auditor's morning, and no stronger —
Cal cold-read + Toy P2 below are the gate.**

Note what the repair does NOT do: it does not prove "τ = 6 ⟹ chords exist in G−v" (the structural
claim Toy 451 gestures at). It sidesteps that question by guaranteeing the chords by construction.
The direct chord-forcing lemma remains open and would be a stronger theorem; the repair does not
need it.

## 4. TWO UNSTATED LEMMAS THE PROOF NEEDS (both easy, both verified by me this session)

**4.1 Middle-Strict Lemma.** *In a triangulation (or in H), at any τ = 6 vertex the middle bridge
pair (r, s_M) is ALWAYS strictly tangled.* Proof: the link edges B_1—n_sM and n_sM—B_2 exist
(consecutive link vertices are adjacent), are (r,s_M)-bichromatic, and chain all three vertices
together. Consequences: (i) τ_s = exactly 4 at τ = 6, with the strict bridge slot always the middle
pair — Lemma 3's "at most" becomes "exactly," matching the 2,382/2,382 count; (ii) **it closes a
loophole the paper never addresses: Lemma 6 selects "a cross-linked pair," and if the MIDDLE pair
could be cross-linked, Lemma 8's geometry (n_si at p+3) breaks.** Middle-Strict makes the middle
pair never cross-linked, so the selected pair is always non-middle. Without this lemma the proof has
a second, quieter hole; with it, the case cannot arise.
  *Calibration note:* Toy 433 (v9 doc) reports the 4th strict slot VARIES — middle only ~10%. That
run mixed general planar graphs, where middle link edges may be absent. On triangulations the lemma
predicts 100% middle. This divergence is a pre-registered, can-fail toy (P1 below), and it is also a
warning already in our feedback corpus: the empirical tables and the triangulation-WLOG proof are
not sampling the same population.

**4.2 Orientation Lemma.** *The swapped pair's singleton n_si sits at p+3 (link-adjacent to B_near),
never at p+4 (link-adjacent to B_far).* Proof: if n_si were adjacent to B_far, that (r,s_i)-edge
would put n_si in B_far's chain — but the split-bridge swap chain excludes n_si by construction.
With the reflection WLOG this licenses the pentagon labeling that Lemma 8 uses silently. A referee
who cannot derive this cannot verify either sub-case; it must be stated.

## 5. THE COMMISSIONED QUESTIONS (from the 08-26 review frame)

- **(a) Definition-equivalence:** ANSWERED, favorably. Theorem 1 is the classical statement (proper
  4-coloring of planar graphs); the new definitions live in the proof, not the theorem. No
  "your theorem vs Appel–Haken's" gap exists for the standalone paper. **But the Millennium outline
  is internally inconsistent with the paper:** the outline's headline names the missing definition
  ι(v) ("Kempe interference number," L54, L224) while its own L196 calls ι "irrelevant," and the
  paper's actual load-bearing definition is the strict/operational split (τ_s). One object, two
  names, one of them wrong — a name↔object sweep of the outline is owed (loaded string:
  "the missing definition is ι").
- **(b) Computational status:** the object the proof actually uses is heavily instrumented
  (Toys 405–451; per-lemma zero-exception tables). No toy computes ι — and none needs to; ι is the
  outline's orphan, not the proof's.
- **(c) Lean/Coq feasibility:** GOOD, with the repair in hand. The proof's needs: combinatorial
  planarity + link cycles, the discrete Jordan/chain-separation lemma (used three times: L2, L3,
  eliminations), finite pentagon case analysis, chain components. Gonthier's 2005 Coq proof built
  exactly this hypermap/discrete-topology infrastructure; our chain-separation lemma is the one real
  formalization mountain and it is one lemma, not 633 configurations. Realistic: months of focused
  CI labor, dominated by the planarity substrate; the eliminations and budget arithmetic are days.
  Highest-value first target: formalize Lemma 3 (it exercises every ingredient once).
- **(d) The AVL frame:** the pre-read demanded "the measure strictly decreases under the double
  swap, un-ambushable by a third chain." That demand IS Lemmas 7+8: τ: 6 → ≤5 (decrease), and the
  dichotomy is the no-third-chain-ambush guarantee (only x = r can re-tangle, and only once). The
  delivered proof satisfies Casey's demanded lemma-shape; the Schnyder-lattice reading (double swap
  ↔ Schnyder flip) remains unexplored in the corpus and is not needed for correctness.

## 6. PRE-REGISTERED TOYS (can-fail; Elie when he wakes — do not run these Keeper-side)

- **P1 (Middle-Strict):** restrict τ = 6 hunts to TRIANGULATIONS; predict the strict bridge pair is
  the middle pair in 100% of cases. Any non-middle strict slot on a triangulation falsifies 4.1 and
  reopens the Lemma 6 loophole.
- **P2 (H-repair):** rerun the τ = 6 pipeline on H = (G−v) + 2 hole diagonals (diagonals chosen
  adversarially, all 5 choices swept): predict (i) at τ = 6 the two diagonals are always the fan
  from s_M; (ii) post-split-swap τ ≤ 5 in 100% of cases; (iii) second swap always frees a color.
  Any exception falsifies Section 3.
- **P3 (population split):** re-bin the existing Toy 433 strict-slot statistics by
  triangulation vs non-triangulation; predict the variance lives entirely in the non-triangulations.

## 7. WHAT THIS DOES AND DOES NOT CHANGE

- The K940 banner stands. The paper remains an ATTEMPT until the repair is written, toy-verified,
  and cold-read. No tier moves today.
- The honest sentence for the ledger row changes from "correctness not determinable by expert
  reading" to: **"one identified false premise (Lemma 8's pentagon triangulation), witnessed by the
  icosahedron; a two-line induction restructure is proposed that appears to close it; two auxiliary
  lemmas stated; verification owed."** That is a much better sentence: it is falsifiable, it is
  specific, and every referee can check the witness in one minute.
- Cal's May 7 PASS and my own K41 (v5–v7) both predate this finding and did not catch it. K41's
  artifact I could not locate under that name this morning — provenance gap, minor, logged.
- Registry rows T154/T155/T156 still carry pre-K940 "PROVED — all 13 steps" language and T155's row
  conflates naming ("Lyra's Lemma"/"Keeper's Theorem" swap between v9 and the registry). Sweep owed
  when the repair lands, not before (avoid double-churn).

— Keeper, K1832. Next counter: K1833.

---

## v0.2 AMENDMENT (same K-number; 2026-08-30, 09:45 EDT) — Cal's §782 leak candidate CONFIRMED against Section 3

Cal pre-registered four leak candidates blind (before reading Sections 3–4). His sharpest one is
genuine, and I verified it before accepting it:

**The claim.** Every Jordan-curve argument in the paper (Lemmas 2, 3, and the eliminations) closes
its curve THROUGH v and pins sides by v's angular sectors. But G is maximal planar, so G plus any
pentagon chord is nonplanar — **no planar embedding holds both v and the diagonals.** In H the
curve-through-v tool does not exist, and H-chains may traverse the diagonal edges. Verified: all
three steps of that argument check.

**What it does to Section 3.** The sentence "every chain, swap, τ, and lemma is computed in H
throughout... I found no leak" is RETRACTED to: *no leak found in the steps I examined; the transfer
of Lemmas 2/3 (and the eliminations' own curves) into H's embedding was not among them.* The
eliminations invoke Lemma 3's conclusion in H; Lemma 3's proof as written does not run in H. The
repair is therefore **OPEN, not merely unverified** — its load-bearing missing piece is a
separation lemma provable in H's embedding (where the pentagon interior holds the two diagonals and
no v).

**One preliminary observation for whoever closes it** (recorded, not relied on): a separated chain
in these arguments carries exactly two colors, and a diagonal edge joins two link vertices of KNOWN
colors — so any given separated chain can use at most the one diagonal whose endpoint colors match
its pair. If a patch exists, it lives in that color-counting: the curve must be routed so the only
dangerous diagonal is either on the curve's own side or excluded by its colors. Lyra's blind
construction should not read this note until her own repair is written.

**Status:** defect (Section 2) stands, independently confirmed by Cal with a computational
icosahedron check. Repair candidate stands as a candidate with one named missing lemma. Middle-Strict
and Orientation lemmas (Section 4) are untouched by the leak — they use link edges only, no curves.

— Keeper, K1832 v0.2

---

## v0.3 AMENDMENT (same K-number; 2026-08-30, ~10:00 EDT) — Section 3 REFUTED; scoreboard after the fresh-eyes + falsifier round

**The H-repair (Section 3) is refuted, twice over and with witnesses.** Lyra derived the structural
kill blind (in H, fan + link edges make four of six pairs automatically strict, including the
non-middle (s_i, s_M) ⟹ Lemma 3 is FALSE in H ⟹ Lemma 7's budget dies: in G−v Lemma 8 lacks its
premise, in H Lemma 3 loses its truth, and Lemma 7 needs both and gets neither graph). Elie's
Toy 5509 then refuted all three of my P2 predictions empirically: the fan is NOT forced (2487/4242
wrong-apex), τ_s reaches 5 and 6 inside H, two exhibited configurations — one on the icosahedron —
are stuck under exhaustive 1-, 2-, and 3-swap search, and the repaired induction independently
fails 18/73 graphs at the degree-4 hole I handled in a parenthesis. **The repair's own diagonals
manufacture the tangling they were meant to resolve. Section 3 is withdrawn in full.**

**Also withdrawn: my P3 prediction's mechanism.** The historical strict-slot variance was NOT a
population effect (the population had zero non-triangulations) — it was an instrument bug
(sorted-vertex-order labels vs true cyclic order; Toy 5510). I predicted the right conclusion
(Middle-Strict) for a wrong reason. Logged per the standing when-the-reason-is-wrong discipline.

**Also FALSE, not open: the direct chord-forcing lemma** (Section 3's closing note). Toy 5508
exhibits τ = 6 at chord-free degree-5 vertices in G−v — 22 witnesses, one verified by exhaustive
single-swap search. This simultaneously refutes Toy 451's banked negative and the paper's
supplementary table row that relied on it.

**What stands, sharpened by the same round:**
- Sections 0–2: the pentagon-premise defect and the icosahedron witness — now independently
  confirmed by Cal (computationally) and Lyra (by derivation). Lemmas 2–7 sound in G−v as scored.
- **Section 4.1 Middle-Strict is the rock of the day:** re-derived blind by Lyra (convergence
  discounted per her note — the wake message named it), and confirmed 862/862 in G−v triangulations
  and 4242/4242 in H. It is the one lemma provable from link edges alone, no Jordan curve — and it
  is load-bearing material for whatever the real repair is.
- Section 4.2 Orientation — confirmed, and strengthened by Lyra to a forced form (Lemma 6's
  third-chain case is vacuous and can be deleted).

**Instrument finding with corpus-wide reach (Elie, Toy 5510):** the March-era empirical table is
poisoned — the sorted-order labeling bug produced Toy 434's "STEP 2 IS FALSE" header, and the old
screen silently dropped 446 of 661 valid τ = 6 cases. **The paper's entire supplementary
verification table (including "double swap: 100%") must be re-run on corrected instruments before
any of it is cited again.** Items for Grace's sweep inventory: Toy 451's banked negative
(retraction owed), Toy 434's header, the supplementary table, and every "2,500+ cases, 0
exceptions" string downstream of the old screen.

**The one live repair is Lyra's G−v survivor criterion** (pre-swap (s_M,s_x)-witness path avoiding
the swap chain ⟹ post-swap middle-strictness ⟹ τ ≤ 5), with one named residue: the finite
"double-blockage" configuration she could not kill by Jordan or counting. Decisive next
computations: (i) Elie searches for the double-blockage configuration directly on the corrected
τ = 6 population, chord-free witnesses included; (ii) the corrected-instrument rerun of the
double-swap success statistic in G−v — the March 100% is currently unsupported.

**Keeper calibration, continued from the sundown:** the pattern held for the third consecutive
session — my structural findings survived every check (the defect, Middle-Strict); my constructive
repair did not survive its first contact with fresh eyes or falsifiers. Weight my structure,
falsify my constructions, and keep the falsifiers pre-registered — today that discipline turned a
wrong repair into three confirmed lemmas, two killed banked claims, and a corrected instrument in
one morning.

— Keeper, K1832 v0.3

---

## v0.4 AMENDMENT (same K-number; 2026-08-30, ~11:00 EDT) — verdict re-scoped: the defect is ARCHITECTURAL; plus the reconciliation Cal is owed

**Verdict update.** Cal's independent 17-vertex witness (3-ring pentagonal antiprism tower,
chord-free apex: all 10 single swaps and all 66 two-swap sequences fail; frees at depth 3) and
Elie's Toys 5511/5512 (per-swap dichotomy counterexamples at chord-free vertices; gallery double-fail
601/1782 incl. 144 exhaustive on Fritsch; rescue-depth ladder 2/3/4 on Fritsch/Errera/Kittell)
refute **Lemma 7's conclusion in G−v and the paper's two-swap thesis outright**. Section 0's framing
("one localized defect") is superseded: the false pentagon premise is not the proof's one flaw — it
is what made a false lemma provable. **The honest object going forward is Kempe 1879 sharpened: what
unbounded-depth or non-Kempe mechanism closes the degree-5 insertion.** K1832's Sections 0–2 stand
as the audit that located the crack; the building behind it came down under the team's instruments,
which is the correct order of events.

**Reconciliation owed to Cal (open, with his testable hypothesis logged).** v0.3 carried Lyra's
"fan-forcing half is sound" and Elie's 2487/4242 wrong-apex-fan finding unreconciled in one
document. Logged as OPEN with Cal's hypothesis as the decisive test: the eliminations lean on
Corollary 1, whose Lemma-2 curve also closes through v — so wrong-apex cases in H should be gap-1.
Elie's E2 decides it. Until then neither claim is cited.

**Gift-audit note against myself, recorded:** v0.1's "localized and repairable" was the reading most
flattering to the program, and it did not survive the critic phase. The finding that DID survive —
Middle-Strict, the witness, the instrument corrections — was all of the exhibited-obstruction kind.
The lesson is already in the feedback corpus; today it collected another receipt.

**Literature pins for the row (web-verified this session):** Fisk 1973 (Kempe-connectivity of
4-colorings, 3-colorable sphere triangulations); Mohar 2007 / Feghali 2023 / Mohar–Salas extensions;
**general plane triangulations OPEN (arXiv 2511.00485, Nov 2025)**; k-Recoloring PSPACE-complete for
k ≥ 4 (arXiv 2210.17105); Heawood GF(3) triangle-sum reformulation (arXiv 2411.15992). Our sharpened
question sits ON the field's open frontier, with instruments (Middle-Strict, Lemma C, XOR-toggle
exactness, the witness gallery) the literature does not have.

— Keeper, K1832 v0.4. Row state and round-3 assignments: CI_BOARD.md Round 73.
