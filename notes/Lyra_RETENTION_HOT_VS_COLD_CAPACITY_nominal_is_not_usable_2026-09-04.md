# Retention under construction — HOT AND COLD CAPACITY: nominal is not usable
**Lyra, for Casey. Friday 2026-09-04, 14:44 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_hot_vs_cold_capacity_2026-09-04.py`.**

## 0. Casey's distinction, and the hole it found in my bookkeeping

A big bang, as Casey puts it, is not a clearing. It pushes outward and **creates new space**, with the matter that was there either superheated by the shock or eventually carried outside the observable region. So the new capacity arrives **hot**, already occupied by thermalized matter.

Every growth step I have run arrives **cold**: the new degrees of freedom are in a determined state, which is precisely why rung 3 found a cold start at all. And every capacity figure I have quoted is **log of the state count**, which measures the capacity of the space and not the capacity in use. A cut only buys record where the mass actually sits, so those are not the same quantity.

**Correction to all earlier chains: my H was nominal capacity. The usable capacity is the entropy of the actual law.**

## 1. Measured gap between nominal and usable

Dimer torus 4 by 6, three cold growth steps per refusal, four cycles, varying the number of relaxation steps allowed between writes:

| relaxation between writes | record after 4 cycles | usable capacity | nominal capacity | **gap** | heat left |
|---|---|---|---|---|---|
| none | 5.618 | 7.864 | 11.558 | **3.69** | 2.25 |
| 3 steps | 4.714 | 8.438 | 11.282 | 2.84 | 3.72 |
| 15 steps | 5.594 | 9.113 | 11.430 | 2.32 | 3.52 |
| 60 steps | 5.535 | 9.370 | 11.666 | **2.30** | 3.84 |

**Between two and three and a half bits of nominal capacity are not in use**, and thermalization closes roughly a third of that gap. Cold capacity is real space that the system has not yet spread into, and it cannot be spent on a record until it has.

## 2. What relaxation does and does not buy

**It does not buy more record now.** The record after four cycles is 5.6, 4.7, 5.6, 5.5 across the four settings, with no trend. Waiting did not make the next write bigger.

**It preserves the reserve.** The heat left after four cycles is 2.25 with no relaxation against 3.84 with sixty steps. The impatient chain has bought the same record and burnt nearly twice as much of its fuel doing it. On the sustainability result, that is the chain that freezes first.

So the effect of thermalization is not on the size of the next write but on **how many more writes there can be**. Hot capacity is worth more than cold capacity of the same nominal size, and the difference is exactly the gap in the table.

## 3. Honest limits

Four cycles, **one trajectory per setting, no replication, no error bars**. The differences between the relaxation settings are within what a single run could produce by chance, so "no trend in record" and "relaxation preserves the reserve" are both weakly supported and need repeating before either is quoted. What is robust is structural and does not depend on the trajectory: **nominal capacity exceeds usable capacity under cold growth, by two to three and a half bits here**, and every capacity number in my earlier notes is the nominal one.

## 4. For the cosmological reading, precisely

If a big bang is modelled as growth, then in this framework it is growth of the good kind: it raises capacity, and delivering that capacity hot means it is usable immediately rather than after a relaxation time. Superheating the existing matter is a separate operation, and in this framework it is not free — thermalizing across a class boundary is exactly what **merges** classes and destroys record. Removing matter from the observable region is a third operation and is a refusal, which by rung 4 can create record where it cuts and destroy it where it merely empties.

So the three parts of Casey's sentence are three different operations in this framework, with three different signs on the record. That is a sharper thing to say than "the big bang is a growth step", and it is as far as the mathematics reaches. Naming the state space, the moves and the construction step remains the missing bridge.

— Lyra
