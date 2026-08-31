---
title: "Lyra fresh-eyes diff on K1832 — convergence on Middle-Strict and Orientation; divergence on the H-repair: the fan edge that closes the dichotomy starves the budget (Lemma 3 is false in H)"
author: "Lyra"
date: "2026-08-30, Sunday morning (clock-verified 09:48 EDT at write time)"
status: "FRESH-EYES DIFF per Casey's leader → fresh-eyes → critic model. Blind protocol: K1832 Sections 0–2 + the paper read first; my repair constructed in full before Sections 3–4 were opened. Cal cold-read owed on BOTH K1832 and this diff. Nothing banks."
target_artifacts: "Keeper_K1832_FourColor_FULL_PROOF_REVIEW_..._2026-08-30.md; FourColor_Standalone_Paper.md (v9)"
---

# LYRA FRESH-EYES DIFF ON K1832

**Blind-protocol contamination disclosure, stated before anything else.** The wake message named
Keeper's repair components ("H-induction + Middle-Strict + Orientation lemmas") before my blind
construction began. I derived Middle-Strict and Orientation from my own link-edge analysis, but I
knew the names existed, so the convergence on those two lemmas is WEAKENED as independent evidence —
discount it accordingly. The divergence below is unaffected by the contamination: nothing in the
wake message hinted at it, and it contradicts the wake message's summary ("a repair is proposed"
... that appears to close it). A steered reader does not construct a refutation of the thing he was
steered toward.

## 0. VERDICT OF THE DIFF

- **Section 2 of K1832 (the defect + icosahedron witness): CONFIRMED independently.** The pentagon
  premise is false in G−v; the witness is decisive; Lemmas 2–7 sound as Keeper scored them; the
  x = s_j sub-case survives in G−v (it uses only link-cycle edges, which are real).
- **Section 4 (Middle-Strict, Orientation): CONVERGED**, with the contamination caveat above, and
  with one strengthening each (below). These two are almost certainly real.
- **Section 3 (the H-repair): DIVERGED — I find a leak, and it is load-bearing.** The fan-forcing
  half of Section 3 is sound (I verified all five fan cases, including a closure detail Keeper did
  not write down). The post-swap half is not: **Lemma 3 is FALSE in H**, the Lemma 7 budget
  argument collapses with it, and post-split-swap τ = 6 is arithmetically consistent in H. The
  repair saves Lemma 8 by killing Lemma 3, and Lemma 7 needs both. Detail in Section 3 below,
  with an explicit witness configuration and a counter-prediction for Elie's P2(ii).
- **v10: DO NOT DRAFT YET.** Gate: Elie's P1–P3, Cal's adversarial cold-read of both artifacts,
  and a repair-of-the-repair (menu in Section 5).

## 1. CONVERGENCES (with strengthenings)

**1.1 Middle-Strict — identical statement, identical proof.** Link edges B_1—n_sM and n_sM—B_2
chain all three vertices; the middle pair is always strict when tangled. My independent derivation
adds two consequences Keeper's 4.1 states or implies, which I re-derive and endorse:
τ_s = exactly 4 at τ = 6, and **exactly the two non-middle bridge pairs are cross-linked, always**
(Lemma 4's "at least two" is really "exactly these two"). One strengthening: **the x = s_j sub-case
of Lemma 8 IS Middle-Strict applied to the post-swap bridge** — the new bridge {B_far, n_si} has
new middle n_sj, and the length-2 link path B_far—n_sj—n_si is exactly the middle-strict mechanism.
One lemma, used twice. v10 should present it that way; it shortens the paper and shows the
mechanism is one thing, not two.

**1.2 Orientation — same fact, and I can force it rather than assume it.** Keeper's 4.2 derives
"n_si sits at p+3" from the swap chain's construction. My version is stronger and should replace
it: **for each non-middle pair (r, s_x), the link edge between n_sx and its link-adjacent bridge
copy is an (r, s_x)-edge, so the singleton is ALWAYS chained to the adjacent copy; the far copy is
therefore forced, uniquely, before any swap is chosen.** Corollary: Lemma 6's "third chain" case
(n_si in a chain containing neither copy) is VACUOUS for non-middle pairs — it cannot occur, for
the same reason. v10 can delete that case rather than argue it.

## 2. CONFIRMATION DETAIL ON SECTION 2 (brief)

Independently re-derived before unsealing: the coloring lives on G−v; the star's five triangles
leave with v; the pentagon is a face; the icosahedron's chord-free link kills "exactly 2." I also
confirm Keeper's Section 1 scoring of Lemmas 2–7 on my own re-derivation, with the same silent
dependency he flagged in Lemma 6 (now discharged by 1.2).

## 3. THE DIVERGENCE — the H-repair's post-swap budget leak

### 3.1 What is sound in Section 3

The fan-forcing is correct, and I verified it case-by-case in H (pentagon positions
1 = B_far, 2 = n_sM, 3 = B_near, 4 = n_si, 5 = n_sj):

- Fans from 1 or 3 contain the bridge–bridge diagonal (1,3): improper. Excluded.
- Fan from 4: diagonal (4,1) + link edge (3,4) make (r,s_i) strict; the Lemma-3 instance needed
  for the contradiction SURVIVES in H — but for a reason that must be written down in v10:
  **the offending diagonal's own face closes the Jordan curve.** The curve from B_1 to n_si closes
  through face (4,5,1), which exists because diagonal (4,1) exists; it crosses no edge; the
  separation (2,3 | 5) goes through and the (s_M, s_B)-tangle gives the contradiction. Same for
  fan 5 via face (5,2,3). Keeper's eliminations are right, but the paper's Jordan closures all go
  through v, and v is not in H — each closure must be re-routed and the face-closure argument made
  explicit, or a referee will (correctly) object that the curves no longer close.
- Fan from 2 survives. Forced. ✓

### 3.2 The leak

**Claim: Lemma 3 (τ_s ≤ 4 at τ = 6) is FALSE in H, and Lemma 7's budget dies with it.**

Work post-split-swap in H with the forced fan from 2 present (fan edges (2,4), (2,5); neither
endpoint is in the swap chain, so both survive the swap — Keeper says this too, it is what makes
his Lemma 8 work). Post-swap pentagon colors: 1 = s_i, 2 = s_M, 3 = r, 4 = s_i, 5 = s_j. Now count
what the edges force, with no hypotheses at all:

| Pair | Status in H post-swap | Mechanism |
|---|---|---|
| (s_M, r) | tangled, strict — AUTOMATIC | link edge (2,3) |
| (s_M, s_j) | tangled, strict — AUTOMATIC | fan edge (2,5) |
| (s_i, s_j) | tangled, strict — AUTOMATIC | link path 1—5—4 (new middle) |
| (s_i, s_M) | tangled, strict — AUTOMATIC | link edge (1,2) + fan edge (2,4) |
| (r, s_j) | open — needs a 3~5 path | not automatic |
| (s_i, r) | open — needs op-tangling | not automatic |

Four of six pairs are automatically tangled and automatically STRICT, including the non-middle
bridge pair (s_i, s_M) — the very strictness Keeper's Lemma 8 proves. That strictness is a
two-edged sword:

- It is Lemma 8's conclusion: (s_i, s_M) is not a cross-link. The dichotomy holds: ≤ 1 cross-link. ✓
- It is also a COUNTEREXAMPLE to Lemma 3 in H: a non-middle bridge pair, strictly tangled. If the
  two open conditions hold (some (r,s_j)-path 3~5, and (s_i,r) op-tangled), then τ = 6 with
  τ_s = 5. Lemma 3's bound is violated; "at most the middle pair is strict" is simply not a
  theorem in H, because the fan gives strictness a road through the disk that Lemma 3's Jordan
  curves cannot cut (the separated pair's colors are exactly the fan edge's colors).

Now run Lemma 7's budget as written: suppose τ = 6 post-swap; Lemma 3 gives τ_s ≤ 4, so
cross-links ≥ 2; Lemma 8 allows ≤ 1; contradiction. **In H the second step is unavailable.**
With τ_s = 5, τ = 6 requires exactly ONE cross-link — and Lemma 8 permits exactly one (the x = r
partner). No contradiction. Post-swap τ = 6 in H is arithmetically consistent, needing only the
two open conditions in the table. The proof of the main theorem's step 6 does not close.

**The shape of the failure, in one sentence: in G−v, Lemma 3 is true but Lemma 8 lacks its
premise; in H, Lemma 8 gains its premise and Lemma 3 loses its truth — the two-line restructure
trades one hole for the other, and Lemma 7 is the only consumer that needs both at once.**

### 3.3 Why "I stress-tested every lemma and found no leak" missed it

Keeper's eliminations survive in H (Section 3.1 — the offending diagonal supplies its own closing
face). The natural stress-test walks each lemma's PROOF and checks each step still runs; Lemma 3's
proof steps do run pre-swap for the instances the eliminations need. The failure is not in any
proof step — it is that the lemma's STATEMENT acquires a counterexample from the new edges, and
the counterexample is only assembled post-swap, by the repair's own fan. This is our documented
class: the cheat migrates to the last prose step ("everything downstream survives unchanged").

### 3.4 Iteration does not rescue it

If post-swap τ = 6 in H, the only cross-linked pair is (s_i, r); its forced far copy (by 1.2) is
B_far at position 1; swapping it returns position 1 to color r — bridge r at {1,3}, the original
configuration class. The machine cycles. Heawood's ambush, in H, with extra edges.

### 3.5 Counter-prediction for Elie's P2 (filed before any toy runs)

Keeper pre-registered P2(ii): post-split-swap τ ≤ 5 in H, 100%. **My analysis predicts P2(ii) is
at risk: a post-swap τ = 6 instance in H exists whenever the two open conditions co-occur —
(r,s_j)-connectivity 3~5 and op-tangling of (s_i,r).** I see no structural obstruction to
co-occurrence; I could not derive one, and the four automatic tangles actively push τ upward.
Two theories, one toy: if P2(ii) passes 100%, the reason is NOT the Lemma 7 budget (which is
broken in H) but some unproved global fact, and the repair still may not be written as v9+Section-3;
if P2(ii) fails, Section 3 is falsified as stated. Either outcome is informative. Elie: please also
log, for every post-swap H instance, the pair-by-pair (tangled, strict) table above — the
prediction "four automatic strict pairs, always" is itself can-fail and cheap to check.

### 3.6 A separate, minor import bug in Section 3

"(for deg(v) ≤ 4, triangulate the smaller hole likewise)" — do not. The deg-4 Kempe step is sound
in G−v and needs no filled hole; in H, a square hole's diagonal (n_2, n_4) makes the (2,4)-pair
tangled THROUGH the disk, and the classical deg-4 argument (one of the two diagonal pairs is
untangled, by Jordan through v) fails. Fix is trivial — fill only the deg-5 pentagon — but as
written the parenthetical imports the same disease into the easy case.

## 4. MY OWN REPAIR CONSTRUCTION (built blind, filed as the diff requires)

Constructed before unsealing Sections 3–4. It stays in G−v, where Lemma 3 is TRUE, and buys the
x = s_M sub-case a different way. Status: partial — it reduces the gap; it does not close it.

- **Lemma A = Middle-Strict** (as 1.1, including the exactly-two-cross-links sharpening).
- **Lemma B = Orientation, forced form** (as 1.2): far copies are forced by link edges; the two
  available split-bridge swaps are exactly: pair (r, s_i) with C_i containing the copy at position
  1 (= B_far), and pair (r, s_j) with C_j containing the copy at position 3.
- **Lemma C (Survivor criterion — proved).** For swap x ∈ {i, j}: if SOME pre-swap
  (s_M, s_x)-path from n_sM to n_sx avoids the swap chain C_x, then that path survives the swap,
  and together with the link edge (B_far-of-that-swap, n_sM) it makes (s_x, s_M) STRICT post-swap
  in G−v. Then post-swap Lemma 3 (true in G−v) forbids τ = 6 (a non-middle strict pair), so
  τ ≤ 5. The x = s_M sub-case closes with no chord and no fan.
- **The residual gap, stated honestly:** the double-blockage configuration — EVERY
  (s_M,s_i)-witness path meets C_i AND every (s_M,s_j)-witness path meets C_j. I could not kill it
  by Jordan/counting: I verified the hypothetical is locally self-consistent (every curve I could
  build closes consistently around it; details reproducible on request). What I did prove
  constrains it: any witness Q crosses any witness R only at s_M-vertices; the first-crossing
  segments Q[4→m], R[5→m'] avoid BOTH chains; so a double-blocked configuration forces a specific
  interleaved crossing pattern of four mutually color-disjoint connected sets around the pentagon.
  That pattern smells Euler/parity-killable and is a sharp, finite question — but I do not have
  the theorem, and I say so.

**Relation to Keeper's repair:** complementary, not competing. His fan-forcing is sound and is a
true rigidity fact about H; my Lemma C is a true rigidity fact about G−v. Neither alone closes
step 6 today. The honest state of the 4-Color row after this diff: **one false premise (K1832
Section 2, confirmed), two real auxiliary lemmas (converged), two candidate repairs, each with an
identified open residue** — Keeper's: the post-swap budget in H (3.2); mine: the double-blockage
configuration (above).

## 5. REPAIR-OF-THE-REPAIR MENU (for the team, not a claim)

1. **Close my residual in G−v** (preferred if it works: no induction surgery, Lemma 3 stays
   true). Target: the interleaving pattern of {Q, R, C_i, C_j}. Finite, toy-able: Elie could
   SEARCH for double-blocked τ = 6 instances directly — existence/non-existence is decisive.
2. **Patch the budget in H**: prove "(r,s_j)-tangled ∧ (s_i,r)-op-tangled cannot co-occur
   post-swap in H." I tried the obvious face-closures; they don't reach it. Open.
3. **Direct chord-forcing in G−v** ("τ = 6 ⟹ the fan chords exist in G−v," Toy 451's shadow) —
   Keeper's noted stronger theorem. With Middle-Strict + Orientation now available, this may be
   more reachable than it was in March; it would make the original Lemma 8 true as written with
   "exactly 2" weakened to "the two fan chords exist."
4. Hybrid schemes (color H, analyze in G−v) do NOT work — the H-coloring's only extra content in
   G−v is the diagonal endpoint inequalities, which are automatic at the pentagon; the fan EDGES
   do not come along. Verified blind; listed to save the next person the hour.

## 6. HOUSEKEEPING

- Keeper's Section 5(a) ι(v) finding: confirmed as read; Grace's inventory covers it.
- Face-closure detail (3.1) must enter any v10 regardless of which repair lands.
- No percentages anywhere, per the review frame. Tier language: the K940 banner stands; the
  ledger sentence Keeper proposes in Section 7 is right except "appears to close it" — after this
  diff it should read "two candidate repairs, each with one identified open residue."

— Lyra. The witness is the icosahedron; the diff is the finding; the budget is where the proof
still owes its last honest number.
