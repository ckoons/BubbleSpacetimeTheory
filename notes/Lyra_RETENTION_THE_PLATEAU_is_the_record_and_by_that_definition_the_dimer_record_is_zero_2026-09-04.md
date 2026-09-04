> **RETRACTED 16:25 the same day, see section 6 below.** The plateau is a plateau only within the Kempe family. Against the full generalised move set — any colour permutation on any subset, keeping properness — the prism's record goes to **1 class, R = 0**, and the torus 3 by 4 goes to **1 class, R = 0** at subset size 7. The definition in section 3 is vacuous as written and is withdrawn.

# Retention under construction — THE PLATEAU IS THE RECORD, and by that definition the dimer record is zero
**Lyra, for Casey. Friday 2026-09-04, 15:57 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_melting_colourings_2026-09-04.py`. A third case, the 4 by 5 torus, is still running and is not quoted.**

## 1. The colouring curve is also a cliff. I predicted a gradual one.

Restricting Kempe moves by the maximum size of the swapped component, which is the colouring analogue of the dimer flip-length axis:

| max component | prism, classes | prism, R | torus 3 by 4, classes | torus 3 by 4, R |
|---|---|---|---|---|
| 1, 2, 3 | 12 | 3.585 | 72 | 6.170 |
| 4 | **2** | **1.000** | 72 | 6.170 |
| 6 | 2 | 1.000 | **3** | **1.585** |
| 8 / unrestricted | 2 | 1.000 | 3 | 1.585 |

Sharp transitions in both, at component size four and six. So the cliff is not special to dimers, and my prediction of a gradual colouring curve was wrong.

## 2. The real difference is the plateau

- **Colourings:** above the transition the record is **flat and permanent**. Two classes at component size four, and still two when the move set is unrestricted. No further enlargement touches it.
- **Dimers:** the record exists at flip-length four and is **exactly zero** at every larger length. There is no plateau; the record is a single point on the axis.

## 3. What that fixes, and what it costs

The move-set arbitrariness I flagged in rung 6 now has a principled resolution:

> **The record of a system is the plateau of R against move-set size — the value that survives every enlargement of the dynamics.**

By that definition the colouring records are real: one bit for the prism, 1.585 for the torus. **And by that definition the dimer record is zero.** The flux sectors are a low-temperature artefact, present only when the dynamics is held at its shortest possible move.

That is a demotion of my own second instance, and it is worth being exact about what it does and does not touch. The theorems are stated for any record system and are unaffected; the dimer system at flip-length four is a legitimate record system and every measurement in it stands as a measurement of that system. What changes is its standing as a model of records in nature: it has none that survive heating.

## 4. A caveat on R itself, which I should have seen earlier

At small move sizes both systems show every state alone in its own class, giving R equal to log of the state count — 3.585 for the prism, 6.170 for the torus. **Retained information is maximal when nothing moves.** A completely frozen system scores perfectly and means nothing.

So R alone was never the right quantity, and every figure I have quoted today needs reading alongside whether the dynamics actually moves. In practice my systems were far from frozen — nine classes over 3,108 dimer states, two over twelve colourings — so no number changes. But the measure has a pathological end and I did not name it until the melting curve put it in front of me.

## 5. Where this leaves the day

The plateau definition is the sharpest thing the program produced, and it arrived by testing an assertion I had made casually about superheating. It gives a criterion for when a record is worth calling one, it demotes one of my two instances, and it puts a caveat on the central measure.

— Lyra


# 6. RETRACTION, 16:25 the same day

I tested the load-bearing claim of section 3, that the colouring record survives every enlargement, and it does not.

| move set | prism | torus 3 by 4 |
|---|---|---|
| unrestricted Kempe | 2 classes, 1.000 bits | 3 classes, 1.585 bits |
| any colour permutation on any subset, properness kept | **1 class, 0 bits** | **1 class, 0 bits** (at subset size 7) |

**Why the definition was vacuous.** A sufficiently large move set is ergodic, and an ergodic dynamics has one class and no record. So "the value that survives every enlargement" is zero for every system, always. I should have seen that before proposing it; it follows in one line from what a class is.

**What is actually true, and it is weaker but real.** A record exists only relative to a move set, and the meaningful axis is a **cost-ordered** family of move sets rather than an arbitrary one. That is exactly what temperature provides: the record at temperature T is R under the moves affordable at T. There is no absolute record, and the honest quantity is the one already named in the melting note — **the melting threshold**, meaning how far up the cost axis a record survives.

By that measure the two instances still differ, and the difference is now about position rather than existence: the dimer record dies at the first step above the minimum move, while the colouring record survives the entire Kempe family and dies only when arbitrary subset permutations are permitted.

**Section 3's demotion of the dimer instance is also withdrawn.** It was made with a definition that gives zero for everything.

**A note on the day's pattern.** This is the tenth correction since morning. Every one has been to a conceptual sentence I proposed, and none has been to a theorem I proved. The framing is where the risk lives, and the computation has caught it every time.
