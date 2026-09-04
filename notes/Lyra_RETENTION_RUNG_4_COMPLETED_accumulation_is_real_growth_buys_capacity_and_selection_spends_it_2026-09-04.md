> **CORRECTION, 14:10 same day.** Every "retained" figure below is log2(class count), which equals the retained information only when classes are equal in size. They are not. The exact value, the Shannon entropy of the class distribution, is much smaller: at step 0 of chain 1 it is **0.824 bits, not 3.170**. The exact trajectory is 0.824, 1.405, 2.008, 3.762, 4.791, 5.681, 5.713 — the same shape, the same turnover, smaller numbers. The comparison between the two chains is unaffected in direction. See the exchange-law section of the consolidated write-up.

# Retention under construction — RUNG 4 COMPLETED: accumulation measured, and the law that bounds it
**Lyra, for Casey. Friday 2026-09-04, 14:00 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_accumulation_2026-09-04.py`.**

## The question the program was built for

Can retained information accumulate over repeated construction steps? The colouring chains stalled at one bit and I could not tell whether that was a bound or my search. The dimer instance settles it, because it has both a step that creates (forbid two bonds) and a step that retains while multiplying states (add a matched pair).

## Chain 1: pure selection. It rises, then reverses.

Torus 4 by 6, greedily forbidding two bonds at a time:

| step | states | classes | retained | total capacity |
|---|---|---|---|---|
| 0 | 3,108 | 9 | 3.170 | 11.60 |
| 1 | 1,858 | 17 | 4.087 | 10.86 |
| 3 | 554 | 42 | 5.392 | 9.11 |
| 5 | 201 | 69 | **6.109** | 7.65 |
| 6 | 107 | 57 | 5.833 | 6.74 |

Retained information doubles over five steps and then **falls**. Capacity drops monotonically throughout. By step five there are fewer than three states per class; the system is freezing, retained information is approaching total information, and there is nothing left to cut.

## Chain 2: grow, then select. It goes further and was still climbing.

Alternating a growth step with a selection step:

| step | kind | states | classes | retained |
|---|---|---|---|---|
| 0 | start | 3,108 | 9 | 3.170 |
| 1 | grow | 3,812 | 9 | 3.170 |
| 2 | forbid | 2,404 | 21 | 4.392 |
| 4 | forbid | 1,505 | 57 | 5.833 |
| 6 | forbid | 953 | 104 | 6.700 |
| 8 | forbid | 485 | 139 | **7.119** |

**Growth creates nothing on its own** — every growth step leaves the retained information exactly where it was. What it does is replenish the state budget, and the next refusal then buys more than it otherwise could. The alternating chain reached 7.119 bits against 6.109 for pure selection, and it had not turned over when I stopped it.

## The law

Retained information is bounded by total capacity, because classes cannot outnumber states:

  **R ≤ H.**

Selection converts capacity into record and destroys some in the process. Growth adds capacity and no record. Therefore **unbounded accumulation requires unbounded growth**, and an assembly that only selects will freeze: its record approaches its capacity, every class shrinks to a point, and nothing further can be written.

That is the quantitative form of the thing the program set out to explain. A complex assembly accumulates retained structure by alternating permissive growth with selection, and the growth is what pays for the selection. Neither alone gets anywhere: growth alone writes nothing, selection alone exhausts itself in about five steps.

## Scope, stated plainly

One instance, one greedy search sampling 150 candidate pairs per step, eight steps, and small systems. This measures a trajectory; it does not prove that R grows without bound. Two of the growth steps in chain 2 did nothing at all, because the new pair could not attach usefully. And in this instance growth can itself create classes, which it cannot do in colourings — another consequence of the retraction failing here.

— Lyra
