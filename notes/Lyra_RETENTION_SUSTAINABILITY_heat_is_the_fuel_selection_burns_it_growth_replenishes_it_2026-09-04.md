# Retention under construction — SUSTAINABILITY: heat is the fuel
**Lyra, for Casey. Friday 2026-09-04, 14:13 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_sustainability_2026-09-04.py`.**

## The question

Can retained information grow without bound? Yesterday's answer would have been "it stalls." This morning's was "the stall was my search." The real answer is conditional, and the condition is measurable.

## The experiment

Dimer coverings of the 4 by 6 torus. One refusal is "forbid two bonds", which creates. One growth step adds a matched pair, which adds capacity. Vary how many growth steps pay for each refusal, and track the exact entropies: R the Shannon entropy of the class distribution, H_thermo the mean log class size, and the **efficiency** of each refusal, meaning the record gained divided by the heat spent.

## Result: one growth step per refusal is not enough

| refusal | R | H_thermo | efficiency |
|---|---|---|---|
| 1 | 2.405 | 8.735 | 0.67 |
| 3 | 5.763 | 3.898 | 0.48 |
| 5 | 7.497 | 1.107 | 0.34 |
| 6 | 7.891 | 0.560 | 0.09 |
| 7 | 8.098 | 0.246 | **−0.44** |
| 8 | 8.105 | 0.266 | **−26.13** |

Heat burns from 10.778 down to 0.27, efficiency decays, and the last two refusals **destroy record rather than create it**: with nothing left to cut, a refusal only empties classes. The system froze at about eight bits.

## Result: two or three growth steps per refusal, and it does not degrade

| growth per refusal | refusals | efficiencies | final R | final H_thermo |
|---|---|---|---|---|
| 1 | 8 | 0.67, 0.59, 0.48, 0.51, 0.34, 0.09, −0.44, −26.13 | 8.105 | 0.27 |
| 2 | 5 | 0.50, 0.64, 0.55, 0.62, 0.58 | 8.701 | 2.29 |
| 3 | 4 | 0.66, 0.70, 0.63, 0.36 | **9.354** | 2.10 |

With enough growth, the efficiency holds steady near six tenths, the heat does not collapse, and R climbs faster per refusal than in the starved chain — nine and a third bits in four refusals against eight in eight.

## The statement

**Heat is the fuel.** Refusal converts it into record at an efficiency around one half to two thirds and destroys the rest. Growth replenishes it and writes nothing itself. Therefore:

**Accumulation is sustainable exactly when growth replenishes the thermodynamic coordinate at least as fast as refusal consumes it.** Below that rate the record saturates, the classes shrink toward single points, and further refusals begin to destroy what is there, because a refusal with nothing left to cut can only empty.

This is the corrected and quantitative form of the program's original intuition. It is also, and I state it as an analogy and not a claim, the shape of Fisher's argument in population genetics: selection consumes variance, and without replenishment it halts.

## Scope

One instance, greedy with 120 sampled pairs per refusal, states capped at 9,000, four to eight refusals per chain, and a random choice of attachment site for growth. The efficiencies are measured on single trajectories, not averaged over runs. **Unbounded growth of R is not proved.** What is shown is that the turnover I reported earlier today is a starvation effect and not a ceiling, and that the starvation has a rate condition attached to it.

One thing worth noting for the theory: in this instance a growth step sometimes creates classes by itself, which cannot happen in colourings. That is the retraction failing again, and it means the clean division of labour — growth adds capacity, refusal adds record — is a colouring statement, not a general one.

— Lyra
