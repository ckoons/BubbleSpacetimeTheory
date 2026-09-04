# Retention under construction — RUNG 3's OWED RATE, measured
**Lyra, for Casey. Friday 2026-09-04, 13:29 EDT (from `date`). NOT posted to the board. Script `play/lyra_retention_rate_2026-09-04.py`.**

## The family

Prism plus k pendant vertices, three colours. Rung 4's theorem says the class count stays at 2 forever, and it does. The class interior doubles at each step, so this is a permanent one-bit record riding on an exponentially growing thermal interior: class sizes 6, 12, 24, 48, 96, 192, 384, with 2^k colour orbits inside each class.

## Result 1: growth adds capacity, not slowness

| pendants | class size | spectral gap | relaxation time |
|---|---|---|---|
| 0 | 6 | 0.500 | 2.00 |
| 2 | 24 | 0.300 | 3.33 |
| 4 | 96 | 0.214 | 4.67 |
| 6 | 384 | 0.167 | 6.00 |

The relaxation time grows **linearly** in the number of added coordinates, as 2 + 2k/3, while the class grows exponentially. That is the ordinary cost of updating one coordinate at a time, not a bottleneck. Accretion buys thermal capacity without buying slowness, which is consistent with rung 5: no bottleneck means no cheap place to cut, and the bit stays expensive.

## Result 2: the inherited state really is colder, and the lag grows

Total-variation distance from equilibrium, inherited law against a random subset of the same size:

| pendants | at t=10, inherited | at t=10, random | at t=20, inherited | at t=20, random |
|---|---|---|---|---|
| 1 | 0.004 | 0.003 | 0.000 | 0.000 |
| 3 | 0.025 | 0.012 | 0.001 | 0.001 |
| 5 | 0.056 | 0.015 | 0.007 | 0.002 |
| 6 | 0.073 | 0.015 | 0.012 | 0.002 |

At one pendant there is no separation. By six the inherited law is five times further from equilibrium at t = 10 and six times further at t = 20, and the ratio is still growing.

**Mechanism.** Both laws decay at the same asymptotic rate, because they share the gap. What differs is the overlap with the slow modes. The inherited law is deterministic in every new coordinate at once, so it loads the slow modes fully; a random subset of the same size is already near-uniform in each coordinate separately and loads them weakly.

**So Casey's "cold start" is real, is measurable, and its size scales with how much the assembly fixed.** Not with how much it added, and not with how large the class is: with how much of the new state the construction determined. That is the honest form of the sentence the program started from, and it took the corrected rung 3 to state it and this family to measure it.

## Scope

One family, one dynamics, small sizes. The linear growth of the relaxation time is a single-coordinate-update effect and would change under a different move set. The separation in Result 2 is the part that should generalise, because it follows from the inherited law being deterministic on the new coordinates, which is what an assembly step is.

— Lyra
