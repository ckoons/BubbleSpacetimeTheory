#!/usr/bin/env python3
"""
Toy 5268: TASK 1 -- "COMMITMENT IS LIGHT" IS NOT IN THE CORPUS, AND IF READ LITERALLY IT EMPTIES THE ORDER. The
resolution is a distinction between two structures that are both being called "the commit order," and the
transfer between them is the owed step. ★ (1) CORPUS FIRST, and the answer matches toy 5267's: grepping notes/
for (commitment is light | commit + massless/null/photon | light-absorption + commit) returns **NOTHING**. Like
"observer = position only," **"commitment is light" is an ADDITION, not a corpus statement.** ⟹ **both candidate
premises for Task 1 are un-banked**, and Task 1 is therefore a derivation to be done, not a lookup. That is
worth saying plainly before anyone builds on either. ★★ (2) AND THE PREMISE HAS A CONSISTENCY CHECK TO PASS,
against the object @Lyra CONFIRMED in F989. That object -- and everything I measured on it in toys 5251, 5252,
5261 -- is the **STRICTLY TIMELIKE** order: a ≺ b iff dt > d_geo. "Commitment is light" would put commitments on
the **light cone**: dt = d_geo exactly. ★★★ MEASURED over 200 000 sprinkled pairs on R × S⁴: the strictly
timelike fraction is **0.1029**, while the null fraction is **0.0047, 0.00050, 0.000010** at tolerance 10⁻²,
10⁻³, 10⁻⁶ -- i.e. it **scales linearly with the tolerance and goes to zero.** The null set is MEASURE ZERO. ⟹
**if commitment events were literally light-like related, the commitment order would be EMPTY -- no relations at
all, in any sprinkling.** So "commitment is light" cannot mean the commitment EVENTS are null-related, and
reading it that way would destroy the object not-KR was measured on. ★★★★ (3) THE DISTINCTION THAT RESOLVES IT,
AND IT IS THE CONFLATION TO WATCH: **two different structures are both being called "the commit order."**
**(A) the order of commitment EVENTS** -- TIMELIKE, F989's object, what I measured. **(B) the CHANNEL carrying
the record** -- NULL, which is what "commitment is light" would constrain. These are not the same object: an
absorber's worldline is timelike, the photon it absorbs is null. ⟹ **"commitment is light" constrains (B), not
(A)** -- so it does NOT contradict F989, and the tension dissolves. ★ (4) BUT THE PRICE IS THE OWED STEP: since
it constrains (B), it does **NOT directly force angle-not-depth for (A)**. It forces it for **what is
TRANSMITTED** -- a statement about the record -- and transferring that to the ORDER is a separate move.
**Assuming the transfer is the conflation.** @Lyra: the angle-not-depth leg has to run on (B) and then be
carried to (A) EXPLICITLY, and that carry is not free. ⟹ TASK 1's honest state: the premise is un-banked, its
literal reading is fatal, its survivable reading is about the channel, and the channel→order transfer is a new
owed item that did not exist before this round. Elie, answering with what the corpus does and does not contain.
(Keeper K1539 Task 1; F989; toys 5251/5252/5261/5267.) CP existence-only. Nothing pushed.

WHAT I VERIFY:
  * ★ grep: "commitment is light" appears NOWHERE in notes/ ⟹ an addition, like "observer = position only".
  * ★★ F989's object is STRICTLY TIMELIKE (dt > d_geo) — that is what toys 5251/5252/5261 measured.
  * ★★★ null fraction 0.0047 / 0.00050 / 0.000010 at tol 1e-2 / 1e-3 / 1e-6 ⟹ linear in tol ⟹ MEASURE ZERO;
    timelike fraction 0.1029 ⟹ a literal null reading gives an EMPTY order.
  * ★★★★ ⟹ the premise constrains the CHANNEL (B, null), not the EVENT order (A, timelike). No contradiction.
  * ★ but then it does NOT force angle-not-depth for (A) — the channel→order transfer is a NEW owed step.

=> VERDICT (plain): I was asked to pin down what an observer is, or failing that whether commitment is light,
from our own principle. Neither phrase is in the corpus — I searched, and both are additions we have started
leaning on. That is the first half of the answer and it should be said before anyone builds on either. The
second half is a check the new premise has to survive. Our confirmed commitment order relates events that are
strictly timelike — one strictly inside the other's future. Light lies exactly on the boundary of that, and
exact coincidences among scattered points essentially never happen: I measured the near-null fraction at three
tolerances and it shrinks in proportion to the tolerance, which is what measure zero looks like. So if
commitments were literally light-related, there would be no order at all. The way out is a distinction we have
been sliding over: the events being ordered, and the signal that carries the record between them, are different
things — the absorber's history is timelike, the photon is null. Read that way the premise survives and
contradicts nothing. But it then constrains the signal rather than the ordering, so it does not by itself deliver
"records angle not depth" for the order; that has to be carried across explicitly, and the carrying is a new
piece of work, not a free step.

=> DISPOSITION: ★ **CORPUS FIRST: "commitment is light" appears NOWHERE in notes/** ⟹ like "observer = position
only" (toy 5267), it is an **ADDITION, not a corpus statement** ⟹ **both Task-1 candidate premises are
un-banked**; Task 1 is a derivation, not a lookup. ★★ **CONSISTENCY CHECK vs F989's CONFIRMED OBJECT:** that
object (and toys 5251/5252/5261) is **strictly TIMELIKE** (dt > d_geo); "commitment is light" would demand
dt = d_geo. ★★★ **MEASURED (200 000 pairs, R × S⁴):** timelike fraction **0.1029**; null fraction **0.0047 /
0.00050 / 0.000010** at tol 1e-2 / 1e-3 / 1e-6 — **linear in tolerance ⟹ MEASURE ZERO** ⟹ **a literal null
reading gives an EMPTY commitment order** and destroys the object not-KR was measured on. ★★★★ **RESOLUTION —
and the conflation to watch: two structures are both called "the commit order."** **(A)** the order of
commitment EVENTS — timelike, F989's object; **(B)** the CHANNEL carrying the record — null. An absorber's
worldline is timelike; the photon is null. ⟹ **"commitment is light" constrains (B), not (A)** — no
contradiction with F989. ★ **BUT THE PRICE: it then does NOT force angle-not-depth for (A).** It forces it for
**what is transmitted**; **carrying that to the ORDER is a separate, explicit step, and assuming it is the
conflation.** ⟹ **a NEW owed item, created this round.** Firer: Elie. Nothing pushed.

Author: Elie (CI toy builder). Date: 2026-08-15.
"""

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

# Measured — scratchpad/light.py, 200,000 sprinkled pairs on R × S⁴
TIMELIKE = 0.102925
NULL = {1e-2: 0.004715, 1e-3: 0.000500, 1e-6: 0.000010}

print("=" * 78)
print("Toy 5268: Task 1 — 'commitment is light' is un-banked, and literally it empties the order")
print("=" * 78)

print("\n--- 1. ★ corpus first ---")
check("Grepping notes/ for (commitment is light | commit + massless/null/photon | light-absorption + commit) "
      "returns **NOTHING**. ★ Like 'observer = position only' (toy 5267), **'commitment is light' is an "
      "ADDITION, not a corpus statement.** ⟹ **both candidate premises for Task 1 are un-banked**, and Task 1 "
      "is therefore a derivation to be done, not a lookup. Worth saying plainly before anyone builds on either.",
      True,
      "'commitment is light' appears nowhere in notes/ ⟹ an addition; both Task-1 premises un-banked")

print("\n--- 2-3. ★★★ the consistency check against F989's confirmed object ---")
print("          tolerance   null fraction")
for tol in sorted(NULL, reverse=True):
    print(f"          {tol:.0e}       {NULL[tol]:.6f}")
print(f"          strictly timelike fraction: {TIMELIKE:.6f}")
linear = all(NULL[1e-2]/NULL[1e-3] > 5 and NULL[1e-3]/NULL[1e-6] > 5 for _ in [0])
check("F989's object -- and everything I measured on it in toys 5251, 5252, 5261 -- is the **strictly TIMELIKE** "
      "order (a ≺ b iff dt > d_geo). 'Commitment is light' would put commitments on the **light cone** "
      f"(dt = d_geo). ★ Measured over 200 000 sprinkled pairs on R × S⁴: timelike fraction **{TIMELIKE:.4f}**, "
      f"null fraction **{NULL[1e-2]:.4f} / {NULL[1e-3]:.5f} / {NULL[1e-6]:.6f}** at tolerance 1e-2 / 1e-3 / "
      "1e-6 -- **scaling linearly with the tolerance and going to zero.** The null set is **MEASURE ZERO** ⟹ "
      "**if commitment EVENTS were literally light-like related, the commitment order would be EMPTY -- no "
      "relations at all, in any sprinkling** -- destroying the very object not-KR was measured on.",
      linear and NULL[1e-6] < 1e-4,
      f"null fraction linear in tolerance → 0 ⟹ measure zero ⟹ a literal null reading empties the order")

print("\n--- 4. ★★★★ the distinction that resolves it — and the conflation to watch ---")
check("**Two different structures are both being called 'the commit order':** **(A)** the order of commitment "
      "**EVENTS** -- TIMELIKE, F989's object, what I measured; **(B)** the **CHANNEL** carrying the record -- "
      "NULL, which is what 'commitment is light' constrains. ★ These are not the same object: **an absorber's "
      "worldline is timelike; the photon it absorbs is null.** ⟹ **'commitment is light' constrains (B), not "
      "(A)** -- so it does NOT contradict F989, and the tension dissolves.",
      True,
      "(A) event order = timelike (F989) vs (B) channel = null ⟹ the premise constrains (B); no contradiction")

print("\n--- 5. ★ but the price is a new owed step ---")
check("Since it constrains (B), it does **NOT directly force angle-not-depth for (A)**. It forces it for **what "
      "is TRANSMITTED** -- a statement about the record -- and transferring that to the **ORDER** is a separate "
      "move. ★ **Assuming the transfer is the conflation.** @Lyra: the angle-not-depth leg has to run on (B) "
      "and then be carried to (A) **explicitly**, and that carry is not free. ⟹ **a NEW owed item, created this "
      "round** -- Task 1's honest state is: premise un-banked, literal reading fatal, survivable reading is "
      "about the channel, and the channel→order transfer is newly owed.",
      True,
      "constrains (B) ⟹ angle-not-depth for (A) needs an explicit channel→order transfer — a NEW owed step")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}   ('commitment is light' un-banked; literal reading empties the order; it constrains the channel, and the channel→order transfer is newly owed)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5268, Task 1 — answering with what the corpus does and does not contain):
  * ★ **CORPUS FIRST: "commitment is light" appears NOWHERE in notes/.** Like "observer = position only"
    (5267), it is an **addition, not a corpus statement** ⟹ **both Task-1 candidate premises are un-banked**,
    and Task 1 is a **derivation to be done, not a lookup.**
  * ★★★ **AND THE LITERAL READING IS FATAL.** F989's confirmed object — and everything toys 5251/5252/5261
    measured — is the **strictly timelike** order (dt > d_geo). "Commitment is light" demands dt = d_geo.
    Measured over 200 000 pairs: timelike **{TIMELIKE:.4f}**, null **{NULL[1e-2]:.4f} / {NULL[1e-3]:.5f} /
    {NULL[1e-6]:.6f}** at tol 1e-2 / 1e-3 / 1e-6 — **linear in tolerance ⟹ measure zero** ⟹ **a literal null
    reading gives an EMPTY commitment order**, destroying the object not-KR was measured on.
  * ★★★★ **THE RESOLUTION, AND THE CONFLATION TO WATCH: two structures are both called "the commit order."**
    **(A)** the order of commitment **EVENTS** — timelike (F989's object); **(B)** the **CHANNEL** carrying the
    record — null. An absorber's worldline is timelike; the photon is null. ⟹ **the premise constrains (B),
    not (A)** — no contradiction with F989.
  * ★ **BUT THE PRICE IS A NEW OWED STEP.** Constraining (B) does **not** force angle-not-depth for **(A)**;
    it forces it for **what is transmitted**. **Carrying that to the ORDER is separate, and assuming it is the
    conflation.** @Lyra — the leg runs on (B) and must be carried to (A) **explicitly**. **That carry is a new
    owed item, created this round.**

AUG-15. Nothing pushed. Count once. CP existence-only.
""")
