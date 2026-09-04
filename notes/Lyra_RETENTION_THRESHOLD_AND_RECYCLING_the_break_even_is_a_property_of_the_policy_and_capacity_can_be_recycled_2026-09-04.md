# Retention under construction — THE THRESHOLD, AND RECYCLING
**Lyra, for Casey. Friday 2026-09-04, 14:35 EDT (from `date`). NOT posted to the board. Scripts `play/lyra_retention_{threshold,recycle}_2026-09-04.py`.**

## 1. Capacity bookkeeping is exact, and it gives a break-even

Capacity is H = log of the state count, so it is multiplicative and the bookkeeping is arithmetic. A growth step multiplies the state count by an expansion factor f; a refusal multiplies it by a survival fraction s. Over a cycle of g growth steps and one refusal,

  **ΔH = g·log f + log s,  and the break-even is g\* = log(1/s) / log f.**

**It fails badly with average factors and is exact with realised ones.**

| factors used | log f | log s | predicted g\* | predicted ΔH at g = 3 |
|---|---|---|---|---|
| uniformly sampled | +0.130 | −0.852 | 6.58 | −0.463 |
| **as the policy actually realised** | **+0.246** | **−0.775** | **3.15** | **−0.038** |

Measured in the chain: −0.038, and break-even just above 3. The realised version is exact to three decimals; the sampled version is wrong by a factor of twelve.

**The lesson is not the formula, it is the input.** My chain retries growth until it finds one that expands, and takes the record-maximising refusal. Both factors are therefore *selected*, not typical. So **the break-even is a property of the search policy, not of the record space alone.** A better searcher sustains accumulation on less growth. That is a real and slightly startling statement: the quality of the search enters the sustainability condition directly.

## 2. Recycling: capacity can be restored, and here it pays

Casey's point was that a cap is always there but may recycle rather than only grow. Tested directly. Take a system after three refusals have burnt most of its heat — 328 states, 43 classes, R = 4.692, H = 8.358, heat 3.665 — and add back a single edge, restoring states.

| addition | ΔH | ΔR | Δheat | classes |
|---|---|---|---|---|
| best for record | +0.357 | **+0.656** | −0.300 | 43 → 69 |
| best for capacity | +0.782 | +0.245 | +0.537 | — |

**170 of the 234 possible single-edge additions raise capacity without costing any record**, and the best ones raise capacity **and** record together, one of them raising capacity, record and heat all at once.

I expected the opposite. Restoring states restores moves, and moves are what merge classes, so I thought recycling would have to be paid for in record. It is not, because in this instance the restored states largely form *new* classes rather than bridging old ones — the same effect that lets a growth step create here, which is the retraction failing, and which cannot happen in the colouring instance.

**So there are three regimes, not two:**
- **clear and restart**, meaning refusal alone: saturates in about five steps, then erodes, because heat runs out and a refusal with nothing left to cut can only empty;
- **cumulative growth**: sustainable above the threshold, which is around three growth steps per refusal under this policy and lower under a better one;
- **recycle**: restore capacity within a fixed size, and in this instance it is the cheapest of the three, sometimes free and sometimes better than free.

## 3. What this does and does not say about the cosmological reading

It says that a system which only clears cannot keep accumulating, that a system which grows can if it grows fast enough relative to what it spends, and that restoring capacity need not cost the record already written. Those are statements about record systems with a dynamics and a construction.

It says **nothing whatever about universes**, and the framework cannot reach that until someone names the state space, the moves, and the construction step. That is the missing bridge, and it is not a small one. What the framework can offer, if those three are ever named, is a sharp question to ask of them: what are f and s, and is g above the threshold.

## 4. Scope

One instance. Section 1's realised factors are read from a single trajectory. Section 2's recycling test is one state after three refusals under one seed, and "without losing record" is measured against that state, not against the original torus. The three regimes are named from measurements on that instance, not proved.

— Lyra
