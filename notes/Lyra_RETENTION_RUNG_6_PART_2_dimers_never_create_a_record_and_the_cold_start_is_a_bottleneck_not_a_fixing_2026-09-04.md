# Retention under construction — RUNG 6, part 2: creation and the cold start in the dimer instance
**Lyra, for Casey. Friday 2026-09-04, 13:46 EDT (from `date`). NOT posted to the board. Scripts `play/lyra_retention_dimer{3,4,5}_2026-09-04.py`.**

## 1. Creation: it does not happen here

In dimers an added matched pair always extends every parent state, so no adding step is selective. The selective step is a **prohibition**: forbid a bond, and every matching using it dies.

Over **all 80 single-bond prohibitions** on the 4 by 4 and 4 by 6 tori:

| torus | prohibitions | classes emptied | classes SPLIT | class count |
|---|---|---|---|---|
| 4 by 4 | 32 | 2 each time | **0** | 9 → 7 |
| 4 by 6 | 24 | 0 | **0** | 9 → 9 |
| 4 by 6 | 24 | 1 | **0** | 9 → 8 |

**Zero splits, always.** Prohibition removes whole records; it never cuts one in two. The set of matchings avoiding a bond is never a cut of a surviving class.

**So "a write is a refusal" does not reproduce here.** In the colouring instance exclusion was the only way to create a record. In the dimer instance the available steps merge records (rung 6, part 1), or eliminate them entirely, and **nothing creates one**. The dimer records are the winding numbers, and they are given by the topology of the surface at the outset rather than built by any construction.

**[Retracted in section 2b below, one hour later: this was an artefact of allowing only single-bond prohibitions. There is no dichotomy.]**

## 2. The cold start: my prediction was wrong, and the reason is a bottleneck

I predicted, before running, that the dimer cold start would be weak because the construction fixes only one new degree of freedom. It is instead the **strongest** in the program.

Torus 4 by 6, retaining construction, distance from equilibrium:

| class | parent → child states | t = 20 inherited | t = 20 random | t = 80 inherited | t = 80 random |
|---|---|---|---|---|---|
| largest | 2,706 → 3,279 | 0.118 | 0.015 | 0.053 | 0.002 |
| second | 152 → 241 | 0.111 | 0.046 | 0.053 | 0.020 |
| small | 24 → 37 | 0.116 | 0.058 | 0.059 | 0.026 |
| tightest | 24 → 25 | 0.025 | 0.023 | 0.012 | 0.011 |

Up to a **factor of 26** at eighty steps, against five to six in the colouring family.

**Why I was wrong.** The inherited law is not "one coordinate fixed". It places zero mass on every child state where the new pair is matched into the host, and escaping into that region requires a flip through one of the two new vertices, of which there are very few. That is a narrow channel, which is to say **a genuine bottleneck** — the first one the program has produced. The last row is the control: where the child class is barely larger than the image, there is almost nothing to escape into and the separation vanishes.

**Correction to rung 3's headline.** I wrote that the cold start scales with how much the assembly fixed. That is not it. It scales with **how narrow the channel is out of the region the construction can reach**. In the pendant family the construction missed half the class but the way out was wide, giving a factor of five. Here it misses seventeen percent and the way out is a needle, giving twenty-six.

## 2b. RETRACTION, one hour later: there is no dichotomy. My scissors were too rigid.

Section 1 concluded that dimers never create a record, and named that a dichotomy and "the program's most interesting open question". **It is wrong.** I had only allowed prohibitions of ONE bond. Allowing two:

| torus | two-bond prohibitions tested | class count rose |
|---|---|---|
| 4 by 4 | 496, exhaustive | 0 |
| 4 by 6 | 300 sampled | **251** |

Verified as genuine splitting, not an artefact of emptying. Forbidding two bonds on the 4 by 6 torus typically leaves eight of nine parent classes alive, empties one, and **splits three or four of the survivors**, taking 9 classes to 11 or 12 and creating between 0.29 and 0.42 bits. The count reached 17.

**So "a write is a refusal" reproduces in the dimer instance after all.** What failed was not the principle but the size of the refusal I permitted. A single bond is too rigid a scissor to contain a cut; two bonds are not. That is exactly rung 5's realizability premium — the gap between the information-theoretic floor and what the available construction can actually excise — and it is quantitative, not a structural difference between record spaces.

The 4 by 4 torus still never creates, even over all 496 pairs, so the story is quantitative on both axes: the refusal must be large enough to contain a cut, and the class must be loose enough to have one that the available steps can reach.

**Withdrawn:** the dichotomy, and the claim that dimer records are handed down by topology and can only be spent. **Restored:** headline 2, as a general statement with its correct qualifier.

## 3. Where this leaves the four headlines

1. A construction admitting a retraction cannot destroy a record. **General, stands.**
2. A write is a refusal, **and the refusal must be large enough to contain a cut**. General; reproduced in both instances once the scissors are allowed to be big enough (section 2b).
3. A bit costs a cut, and the price is the forgetting rate. **Stands, and is now supported from the other side** — the dimer bottleneck is where a cheap cut would be, and it is exactly where the cold start is longest.
4. The cold start scales with the narrowness of the exit, not with the amount fixed. **Restated, and stronger for it.**

— Lyra
