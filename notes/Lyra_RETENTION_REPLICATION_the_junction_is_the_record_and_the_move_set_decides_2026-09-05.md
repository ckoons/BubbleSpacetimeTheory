# Retention under construction — REPLICATION: the junction carries the record, and the move set decides
**Lyra, for Casey. Saturday 2026-09-05, from `date`. Lane B, private, NOT posted to the board.**
Scripts: `play/lyra_retention_{torus66,cascade,twocert}_2026-09-05.py`.
Predictions hashed BEFORE each run: torus/cascade `325f3e35`, definition test `de589631`.

## 0. What was asked
Casey: how does an object, a crystal, a chemical, learn to be self-replicating — in terms of
this program? Then: is this a theory of complexity; what is the pattern for living vs non-living;
why binary (gamete/zygote); and how does information perpetuate and grow complexity.

## 1. Instrument first (a failure that was informative)
The controls did not reproduce Friday until I found what I had silently changed: **Friday's dimer
move set is ALL 4-cycles, not just faces.** Under all-4-cycles the instrument reproduces Friday
exactly — 4x6: 9 classes, **R = 0.8240 bits**, **251 of 300** two-bond rises; 4x4: **0 of 496**.

Three instrument facts worth keeping:
- **"Class count rose" is a bad proxy for creation.** On 4x4/faces it reports 32 where the honest
  split count is **400** — a factor of 12. Friday's headline used the proxy and got lucky.
- **"All 4-cycles" is not one move set across the family.** A 4-row torus closes in four steps, so
  it has wrapping 4-cycles a 6-row torus does not. On 6x6, cycles4 IS faces (36 both ways,
  identical to the digit). Apples-to-apples across the family is faces-vs-faces.
- Friday's **"4x4 never creates" is a TEMPERATURE statement, not a size statement.** Same torus,
  same 496 refusals: **81% create at faces, 0% at all-4-cycles.**

## 2. The 6x6 torus (against the hashed card)
| | predicted | measured |
|---|---|---|
| matchings | 90,176 | **90,176** exact |
| classes | >9, est. 25, range 13-49 | **41** — in range, point estimate wrong |
| flux separates exactly | YES | **NO** — 41 classes over only **25** flux values |
| two-bond split rate | est. 90% | **90.7%** |

My point estimate of 25 was exactly the flux count: I predicted the flux classes correctly and
assumed flux was the whole invariant. It is not. Sixteen 6x6 classes flux cannot see.

## 3. The cascade: pure selection dies, and dies as a crystal
**ARM A (refusal only, no growth), 4x6.** R rises then falls, both move sets.
| move set | R peak | at step | efficiency while climbing | first negative |
|---|---|---|---|---|
| all-4-cycles | 5.837 | 5 | +0.50 +0.59 +0.59 +0.52 | step 6 |
| faces | 7.011 | 6 | +0.57 +0.65 +0.65 +0.25 +0.31 +0.33 | step 7 |

Two results not predicted and better than the prediction:
- **The conversion efficiency is 0.50-0.65.** Friday's colouring instance gave 0.50-0.64. Second
  instance, different record space, same exchange rate. T7 reproduced.
- **H_thermo hits zero at exactly the step R peaks.** The fuel gauge and the peak are one event.
  T7's freezing condition measured rather than argued. The terminal state is every state in its
  own class, nothing moving, R "maximal" and meaningless. **Pure selection ends as a crystal.**

**ARM B (g growth steps then 1 refusal).** R keeps climbing where Arm A collapsed — but R is the
wrong score, and the run is what showed it:
| arm | R final | H = log2 N | R/H | **H_thermo** |
|---|---|---|---|---|
| A, 4x6 cycles4 | 2.00 (peak 5.84) | 2.00 | 1.000 | **0.000** |
| B, g=1, step 10 | 9.48 | 9.57 | 0.991 | **0.089** |
| B, g=2, step 8 | 15.50 | 16.18 | 0.958 | **0.685** |
| B, g=3, step 5 | 14.45 | 16.74 | 0.863 | **2.290 and rising** |

**g=1 also freezes — it just builds a bigger crystal.** The threshold law reproduces in the second
instance: g=1 starves, g>=2 sustains. **R alone cannot score replication. The score is (R, H_thermo).**
NOT QUOTABLE: Arm B's efficiencies (+1.04, +3.73, +194). Those span a growth-plus-refusal
composite and growth adds heat; T7's rate is defined only on a pure selection step.

## 4. The definition test — and the error was mine
**Proposed definition (mine, this morning, NOT a theorem):** A construction REPLICATES if the child
carries two invariants whose pullbacks separate the parent's classes (T2 certificates), on disjoint
supports — two disjoint retractions satisfying T1.

Parent = 4x4 torus. Child = two copies plus k cross bonds. Same states, same bonds, only the move
set differs:

| k=16, 200,320 states, 126,336 coupled | classes | R | R/2R(P) | H_th | certificates |
|---|---|---|---|---|---|
| child moves = all 4-cycles | 78 | 1.08 | 1.93 | 16.53 | **LOST** |
| child moves = intra-copy only | **739** | **5.62** | **10.06** | 11.99 | **both survive** |

At the warm move set the certificate dies at **k = 7**, the first k at which any state uses a cross
bond, and dies in two stages (cert1 at k=7-8 with cert2 alive; both by k=9).

**Forced vs measured, stated plainly.** The cold table's survival is *guaranteed by T1* — intra-copy
moves make restriction a retraction whose hypothesis holds, so the certificate cannot fail. That row
is a theorem, not evidence. **The measurement is the warm table: the death.**

**My error.** T1 as proved on Friday reads: "if r.A = id AND every child move seen through r is a
composition of parent moves". Restating the definition this morning I kept the retraction and
**dropped the clause about the moves.** Everything that failed in the warm table failed through the
dropped clause. Friday's own doctrine, written eleven hours earlier: *a theorem stated with its
hypothesis survives a second instance; a sentence without one does not.*

**What still stands as a failure:** decoupled duplication costs **R/2R(P) = 1.000 exactly** — full
price. There is no free multiplier in T7. My "duplication is free in R" is WITHDRAWN.
The cheapness is in the COUPLED regime, and I have not yet priced it.

**Frozen-artifact control (the R gain is real):** at k=16 cold, mass in singleton classes is
**0.06%** and the median class size ROSE from 1 to 24. Coupling made classes bigger and more
numerous at once.

## 5. What the two-bond result says twice
- One bond can never **cut**: a size-1 vertex cut does not exist in a 2-connected move graph.
- One bond can never **couple**: at k<=6 cross bonds exist and **zero** states use them — a single
  cross bond leaves fifteen vertices per copy, odd, so no perfect matching uses it.
**Two is the minimum for both operations, and it is the same two.**

## 6. Standing sentences (proposals, hypotheses attached)
- **Replication is not a property of the object; it is a property of the object and its temperature.**
  A replicator is a system whose thermal moves do not straddle the template junction. Bonds across
  the junction are necessary and harmless; MOVES across it destroy the record, at the first one.
- **Complexity lives at the junction, not in the parts** (10.06x, superadditive, control passed).
- **Three legs:** growth supplies H_thermo free (T4, no creation); refusal converts it to R at
  0.50-0.65 with loss (T7); a cold junction multiplies certificates. Remove growth -> Arm A, dies.
  Remove refusal -> crystal, static forever. Warm the junction -> record dies in one step.

## 7. Open
Price the coupled regime in heat. The n-way question (is 3 better than 2) at fixed substrate.
Whether the 0.50-0.65 exchange rate is universal or has a third instance. 6x6's 16 non-flux classes.

---
## 8. TEST 3 — at fixed substrate, how many bodies? (predictions `33d25c11`, all three FAILED)
36 vertices throughout, cold move set (intra-unit 4-cycles, T1's hypothesis holds).

| | R | H_thermo | H |
|---|---|---|---|
| n=1 monolith (6x6) | 2.35 | 14.11 | 16.46 |
| n=2 (two 3x6), k=16 | **9.55** | 8.62 | 18.16 |
| n=3 (three 3x4), k=16 | 5.95 | **12.32** | 18.27 |
| n=2, k=24 | **13.05** | 6.81 | 19.85 |
| n=3, k=24 | 10.05 | 9.65 | 19.71 |

- **N1 FAILED.** R is not increasing in n; two bodies carry more record than three.
- **N2 FAILED.** H_thermo is not decreasing in n; three bodies end with MORE heat unspent.
- **N3 FAILED both halves.** Three is not "too complex" — three is **UNDER-USED**.
- **N4 CONFIRMED, decisively.** The monolith is beaten 9.55 to 2.35 at identical substrate.
  **Complexity lives at the interface, not in the parts.**
- **CONFOUND, stated:** n=3's units carry 0 bits alone, n=2's carry 1 bit each. Controlled for by
  taking the ratio of deltas (record gained per heat actually spent), which cancels it:
  **n=2 = 1.51 / n=3 = 1.29 at k=16; 1.63 / 1.38 at k=24. Stable ~18% across the whole range.**

**MY OVER-READ, LOGGED.** I called "the curves do not cross" off one extra point. At k=24 the gap
NARROWED (3.60 -> 3.77 -> 3.00) and n=3's marginal return rose (+1.90 -> +2.20) while n=2's fell
(+2.07 -> +1.43). **Crossing at large k is UNDETERMINED.** The 18% efficiency ratio is what stands,
because it is a ratio of deltas and does not depend on where either curve sits in its sigmoid.
Third cap-limited question of the day; Friday's 9,000-state lesson, repeated at 700k and 2.5M.

## 9. TEST 4 — depth vs count. FULLY CONTROLLED, but NOT PRE-REGISTERED (see below)
Same three units, same substrate, same 16 bonds. Only the topology varies.

| n=3, k=16 | seams | R | H_th | R per unit heat spent |
|---|---|---|---|---|
| all-pairs | 3 | 5.58 | 12.56 | 1.278 |
| chain | 2 | 6.73 | 11.88 | 1.333 |
| single | **1** | **8.10** | 11.48 | **1.486** |
| *(n=2, k=16)* | *1* | *9.55* | *8.62* | *1.51* |

**REGISTRATION FAILED — see `play/.lyra_predictions_depth_2026-09-05_POSTHOC.txt`.** The intended
pre-registration sat in a shell `&&` chain whose first command (`cd play`, issued from inside play/)
failed; the chain short-circuited and the heredoc never ran. I did not verify, and launched anyway.
all-pairs and chain were measured FIRST; only then did I predict single > chain. So the ORDERING IS
A MEASUREMENT, not a confirmed prediction, and must not be quoted as predicted. The experiment
itself is clean and fully controlled. Concentration also spends the most heat (12.56/11.88/11.48).
**THE MECHANISM, ISOLATED: three bodies forced into ONE seam converge to two bodies' efficiency
(1.486 vs 1.51). The third body becomes idle substrate. The penalty is SEAMS, NOT BODIES.**
Two independent routes to the same ~20%: the controlled topology test, and the delta-ratio.

**The binary answer, restated with its hypothesis:** two is not preferred because three is too
complex. Two is the smallest n that can cut at all (minimum vertex cut in a 2-connected move graph
is 2), and every n above two dilutes a fixed contact budget across more seams. Record is
superlinear in bonds-per-seam and merely linear in seams.

---
## 10. TEST 5 — THE POLICY CONTROL. TWO HEADLINES WITHDRAWN. (predictions `f9bc62ab`, verified before launch)

**WHY RUN IT:** the 0.50-0.65 exchange rate was my best number and my only "two instances" claim.
Both instances used the SAME greedy best-split refusal policy. Friday's own finding: the break-even
is a property of the SEARCH POLICY, not the instance. So "two instances" may be one policy twice.

4x6 torus, pure selection, refusal policy varied:
| move set | policy | efficiency band | median |
|---|---|---|---|
| cycles4 | greedy *(what both instances used)* | 0.107-0.594 | **0.517** |
| cycles4 | exhaustive | 0.165-0.614 | **0.556** |
| cycles4 | random | 0.076-0.493 | **0.401** |
| cycles4 | worst | never gains record | n/a |
| faces | greedy | 0.247-0.649 | **0.565** |
| faces | exhaustive | 0.247-0.651 | **0.565** |
| faces | random | 0.084-0.501 | **0.223** |

**P1 CONFIRMED. The band MOVES with policy. WITHDRAWN: "the exchange rate is 0.50-0.65,
reproduced in two record spaces."** REPLACED BY the much smaller true claim: *the greedy policy
converts at 0.50-0.65 in two record spaces; a random policy converts at 0.22-0.40 in the same
spaces.* The rate is a property of the SEARCHER, not the record space.
**P2 excluded the worst cause:** exhaustive ~= greedy (0.556 vs 0.517; 0.565 vs 0.565), so the
band is NOT an artifact of my sample size of 120.

**SECOND WITHDRAWAL, found while checking P4.** I wrote "H_thermo hits zero at exactly the step R
peaks" and told Casey it was T7's freezing condition measured. **It is true for faces (peak step 6,
H_th=0 step 6) and FALSE for cycles4 (peak step 5, H_th still 1.218; H_th reaches 0 at step 8).**
I generalized from one of two rows in my own table. **CORRECTED CLAIM: R peaks at or BEFORE
H_thermo is exhausted; the peak never comes after.** That is the true, weaker statement.

## 11. THE BOUNDARY THIS DRAWS — which results are contaminated and which are not
**POLICY-CONTAMINATED (a searcher chose the refusals):** the Arm A/B efficiencies; the numeric
value of the growth threshold g* (Friday already said g* is a policy property — consistent).
**POLICY-FREE (pure enumeration, no search anywhere in the pipeline):**
 - 6x6: 90,176 states, 41 classes, 25 flux values, 90.7% two-bond split rate
 - creation is temperature-dependent (4x4: 81% at faces, 0% at all-4-cycles)
 - one bond can neither cut nor couple; two can do both
 - the certificate dies at the FIRST coupled state under a warm move set, survives under a cold one
 - decoupled duplication costs R/2R(P) = 1.000 exactly
 - interface superadditivity: monolith 2.35 vs two coupled halves 9.55 at identical substrate
 - **seams not bodies:** 3/2/1 seams -> 5.58/6.73/8.10, and n=3-in-one-seam converges to n=2
**Every structural result survives. Every trajectory result is my searcher's.** Worth carrying.

---
## 12. TEST 6 — MEIOSIS AS A MOVE SET (third instance, off the graph-flip family)
Casey's pointer: primate vs plant reproduction as a source of move sets. What makes it more than
analogy: **MEIOTIC PAIRING (synapsis) IS A PERFECT MATCHING ON HOMOLOGS.** Odd ploidy admits none.
That is the SAME obstruction as the dimer parity result. Predictions `c59d86f1`, verified before launch.

**A MODELLING BUG, found by positive control.** First version canonicalised states by SORTING the
homologs, so "pair (0,1)" meant "the two lexicographically smallest" -- not a fixed pairing. Control:
**0 of 41 states moved by the j=1 crossover.** The correct quotient is the automorphism group of the
PAIRING STRUCTURE. p=2 was unaffected (S_2 IS the bivalent's swap); every p>=3 number was wrong
(triploid states 41 -> 122, tetraploid 60 -> 172).

Corrected, record destroyed per accessible crossover position:
| ploidy | pairing | states | drop per position | \|Aut\| |
|---|---|---|---|---|
| 2n | bivalent | 64 | **1.000, exactly flat** | 2 |
| 3n | bivalent + univalent | 122 | 0.656, 0.639, 0.590, 0.443 | 2 |
| 3n | trivalent | 41 | 1.556, 1.510, 1.365 | 6 |
| 4n | two bivalents | 172 | 1.227, 1.113, 0.789 | 8 |
| 4n | quadrivalent | 60 | **2.385, 2.151, 1.371** | 24 |

- **M1 HIT 7/7 EXACTLY:** for p=2 all-het, R = (L-1) - |J|. The phase space is F_2^(L-1) and
  crossovers are TRANSLATIONS. **Diploid bivalent is the unique flat-rate case: one bit per position.**
- **M2 HELD:** melting here is LINEAR where colourings and dimers gave a CLIFF. Crossovers COMMUTE.
  **Abelian move sets melt linearly; a cliff requires non-commuting moves.**
- **Multivalent pairing costs TWICE OVER:** ~2x faster melting per crossover at fixed ploidy
  (4n: 2.385 vs 1.227; 3n: 1.556 vs 0.656) AND less record to start with, because a bigger pairing
  automorphism group leaves fewer distinguishable states (60 vs 172 at 4n).
  **=> the framework PREDICTS DIPLOIDIZATION** -- a persisting polyploid should evolve bivalent
  pairing. That is a known cytological fact about polyploid plants and it was NOT built in.
- **M3/M4 HELD, and M4 is the useful mismatch:** the triploid is the BEST RETAINER in the table
  (0.44-0.66 bits lost per crossover) **and is sterile. R IS NOT FITNESS.** Triploids retain
  beautifully and cannot CONSTRUCT. Retention and construction are separate legs.

## 13. TEST 6c — M5 FALSIFIED: THE INTERFACE LAW WAS WRONG AS STATED
Selfing vs outcrossing at MATCHED substrate (four parental homologs in both arms):
| \|J\| | SELF (two lineages, no seam) | OUTCROSS (one seam) | ratio |
|---|---|---|---|
| 0 | R = 2.5850 | R = 2.0000 | **0.77x** |
| 1 | 4.1219 | 4.0000 | 0.97x |
| 2 | 5.6144 | 6.0000 | 1.07x |
| 3 | 7.0875 | 7.0000 | 0.99x |
| 5 | 9.0378 | 9.0378 | 1.00x |

Predicted >2x. Measured ~1.0, and selfing AHEAD at zero recombination.
**WHY:** in dimers the seam BLOCKS MOVES (cross bonds occupy vertices, so intra-copy flips
that need them become unavailable and classes fragment). Fertilisation blocks nothing -- both
homologs recombine identically whatever their origin.
**CORRECTED LAW: a seam pays only if it BLOCKS MOVES. A junction that merely joins pays nothing.**
Same statement as the cold-vs-warm certificate result, seen from the other side.

**AND A CONFOUND IN MY OWN INTERFACE CLAIM, found while checking this.** The 2.35-vs-9.55 comparison
held VERTICES fixed at 36 but not EDGES (88 vs 72) and not STATES (293k vs 90k). At MATCHED
state-space size (n=2 at k=8: 96,868 states H=16.56, vs monolith 90,176 states H=16.46) the effect
is **2.4x, not 4x.** Real, and less than half what I first reported.

## 14. TEST 7/8 — R IS NOT THE ASSEMBLY INDEX, AND FLUX IS COMPLETE ON THE BULK
Predictions `830923cb`, verified before launch. Depth = 2-sweep BFS lower bound on class diameter.
| | R | mean depth |
|---|---|---|
| 4x4 faces | 2.3159 | 7.65 |
| 6x6 | 2.3504 | **25.45** |

- **D1 CONFIRMED: same R to within 0.035 bits, 3.33x the depth. R and depth are ORTHOGONAL.**
  **This program is NOT a reparameterisation of Assembly Theory** -- assembly index is construction
  depth, R is class entropy, and they are independent. Both are needed.
- **D2 FAILED, informatively.** I predicted anti-correlation within a family (colder -> more classes
  -> smaller -> shallower). Measured the OPPOSITE: 4x4 cools R 0.28->2.32 AND depth 6.79->7.65.
  Removing moves lengthens paths inside a class faster than it shrinks the class.
- **D4 HELD:** the frozen endpoint is R-MAXIMAL at depth **ZERO**. The sharpest statement of why R
  alone cannot be complexity -- and it is exactly the crystal.
- **TEST 8 (F1) HIT:** the 16 6x6 classes flux cannot see are ALL **singletons, size 1, depth 0**,
  at the extremal flux values (+-12,+-6) -- maximally wound brick walls with no flippable face,
  holding **0.0177%** of the mass (predicted <1%). **Flux IS the complete BULK invariant on 6x6.**

## 15. THE PRICE OF THE COUPLED STEP (owed since 07:40)
| | conversion dR/-dH_th | share of record taken out of heat |
|---|---|---|
| **selection** (T7) | <=1, measured **0.22-0.65** | 100% |
| coupling, two 4x4 copies | **1.32-1.50** | 67-76% |
| coupling, two 3x6 copies | **1.29-2.11** | 77% falling to 47% |

**Coupling always converts above 1; selection never can.** A coupling step CREATES CAPACITY while
spending heat; roughly half to three-quarters of what it writes comes out of H_thermo and the rest
out of newly opened space. **The morning's intuition survives in corrected form: replication does not
evade T7 because duplication is free (it is not -- R/2R(P)=1.000 exactly). It evades T7 because
coupling is capacity-CREATING and selection is capacity-SPENDING, and coupling converts 2-10x better.**

## 16. TEST 9 — THERE IS NO CANONICAL TEMPERATURE, AND THE THRESHOLD IS NOT INTRINSIC EITHER
Same 4x6 torus, 3,108 states, 694 alternating cycles up to length 8, two cost orderings:
| cost = cycle LENGTH | | cost = cycle DIAMETER | |
|---|---|---|---|
| <=4 | 30 moves, R=0.8240 | <=1 | 24 moves, R=2.2572 |
| <=6 | 154 moves, **R=0** | <=2 | 546 moves, R=0.6908 |
| <=8 | 694 moves, R=0 | <=3 | 694 moves, **R=0** |

**546 moves RETAIN 0.69 bits; 154 moves retain NOTHING.** Two cost functions put melting at
completely different move sets, and the LARGER set survives. My fallback hope -- that (T_melt, R
just below) is convention-free -- is REFUTED.

**THE REPLACEMENT, and it unifies the whole day:**
**A record survives exactly as long as the move set fails to generate a transformation that moves
its certificate. Melting is about WHICH moves, not HOW MANY.**
Instances: Test 9 (546 harmless moves retain, 154 with one effective generator melt) - the
certificate test (dies at the FIRST straddling move) - Friday's dimer melting (length 4 -> 9
classes, length 6 -> one; one new generator) - meiosis (R = (L-1) - |J| EXACTLY; each crossover
position is one generator and kills exactly one bit).

**GENERAL FORM: R is the CODIMENSION of the move group's orbit** -- it counts the independent
generators the move set is MISSING. Abelian: exact, one bit per generator. Non-abelian: a single
generator can take 1.43 bits (the six wrapping cycles) or 2.4 (the quadrivalent). **That is what
makes cliffs possible, and why the abelian meiosis instance melts linearly instead.**

## 17. NOVELTY LEDGER (Casey asked; answered honestly after checking the literature)
**PRIOR ART, named:** R = entropy of the class distribution IS Crutchfield's statistical complexity
(entropy of causal states, 1989), and there is a literal paper on the ergodic decomposition of these
quantities (Crutchfield & Debowski 2006) -- so "the dynamics selects the partition, Shannon counts
it", which I called the contribution, is computational mechanics' founding move. H = R + H_thermo is
the Shannon chain rule (1948). T7 is one line from it. T5/T6 are Cheeger plus standard Markov-chain
bottleneck theory. "Complexity at the interface, priced by a cut" is IIT's minimum information
partition (the "cruelest cut"). The melting result is structurally Eigen's error threshold. Two-parent
creation is the standard variance argument for sex. Minimum cut = 2 is elementary graph theory.
Depth is Assembly Theory's assembly index, which even has a threshold for life.

**WHAT SURVIVES AS CANDIDATE-NEW:**
1. **The construction axis.** All of the above assume a FIXED system. T4 -- a total accretion step is
   a bijection on classes, so creation happens iff exclusion disconnects -- is about what BUILDING
   the state space does to the decomposition. Assembly theory counts steps to build an OBJECT; this
   counts what construction does to a CLASS STRUCTURE.
2. **Seams, not bodies** (two independent routes to ~20%, one fully controlled).
3. **R and depth are ORTHOGONAL** (Test 7, measured) -- so this is not assembly theory reparameterised.
4. **The generator law of section 16**, and the abelian/non-abelian split that explains linear
   melting vs cliffs.
5. **Diploidization predicted from the pairing automorphism group** (Test 6), target-innocent.
**Estimate: ~20% new. The rest is a re-derivation of computational mechanics + Cheeger + IIT-shaped
cuts + Eigen thresholds in one vocabulary. The single ledger has value; it is not new physics.**

---
## 18. TEST 10 — HOW MUCH INFORMATION DOES ONE GENERATION RETAIN? (Casey's question)
Predictions `33547955`, verified before launch. **ALL HIT.**

**THE LAW, exact and closed form:**
> **Retention per junction per generation = 1 - H_2(r)**, r = the recombination fraction,
> H_2 = binary entropy. Created per junction = H_2(r).

**G1 CONTROL:** brute-force I(parent phase ; offspring phase) enumerated over every switch vector
matches the closed form to **1e-13 across 18 configurations** (L = 3,5,7 x r = 0 .. 0.5). The
reduction is exact: in the difference coordinate the transition is D -> D XOR d with d_i
independent Bernoulli(r), so **each junction is an independent binary symmetric channel.**

**THE RANGE Casey asked for:**
| r | retained | created | what it is biologically |
|---|---|---|---|
| 0.000 | **1.0000** | 0.0000 | inversion / supergene / Y / mtDNA — no recombination |
| 0.001 | 0.9886 | 0.0114 | ~0.1 cM |
| 0.010 | 0.9192 | 0.0808 | ~1 cM (~1 Mb human) |
| 0.050 | 0.7136 | 0.2864 | ~5 cM |
| 0.100 | 0.5310 | 0.4690 | ~11 cM |
| 0.200 | 0.2781 | 0.7219 | ~26 cM |
| 0.500 | **0.0000** | 1.0000 | unlinked / different chromosomes |

**G2 CONFIRMED, EXACTLY: T + N = 1.000000 at every r. STRICTLY ZERO-SUM.** There is no r that
buys forwarding without paying creation. **This is the whole answer to "what optimises forwarding":
forwarding ALONE is maximised trivially at r = 0, which is the crystal — maximum retention,
zero creation, dead end. There is no interior optimum for forwarding by itself.**

**BLOCK SURVIVAL over generations: P(segment of genetic length d survives n generations intact)
= e^(-nd).** *(LABEL CORRECTION: I first wrote 1 Mb ~ 0.001 M. Human is ~1 Mb per cM, so
1 Mb ~ 0.01 M. The Morgan column was right, the megabase column was off by 10x.)*
| segment | d (Morgans) | survives 1 gen | **half-life** |
|---|---|---|---|
| 0.1 cM (~100 kb) | 0.001 | 0.9990 | **693 generations** |
| 1 cM (~1 Mb) | 0.01 | 0.9900 | **69 generations** |
| 10 cM (~10 Mb) | 0.1 | 0.9048 | **7 generations** |
| 50 cM | 0.5 | 0.6065 | **1.4 generations** |
| chromosome arm (~75 cM) | 0.75 | 0.4724 | **0.9 generations** |
| whole genome (~3400 cM) | 34 | 1.7e-15 | **0.02 generations** |
Ancestral block count after n generations ~ C + nM (23 chromosomes, 34 Morgans): 57 blocks after
one generation, 363 after ten, 3,423 after a hundred, 34,023 after a thousand.

**G4 CONFIRMED: information dies FASTER than correlation.** H_2 has infinite slope at 0, so
1 - H_2 falls steeply at first. Half-life ratio (information / correlation): 0.36 at r=0.001,
0.38 at r=0.01, 0.46 at r=0.05, 0.64 at r=0.1, 0.74 at r=0.2. **Practical consequence: linkage
disequilibrium measured as a CORRELATION overstates how much information is actually left.**

**WHAT OPTIMISES FORWARDING — three answers, and biology uses all three.**
1. **Raw maximum: r = 0.** Suppress recombination entirely. Biology does exactly this where
   forwarding is all that matters — mtDNA, the Y, inversions, supergenes, asexual lineages — and
   every one of them shows the predicted pathology (Muller's ratchet, degeneration), because
   N = 0. This is the crystal, and it is a dead end. **It is the SAME move-blocking junction that
   pays in section 13's corrected law, and it carries the same cost.**
2. **Zero-sum means no free optimum exists.** T + N = 1 exactly. The question has no interior
   answer as posed; it only has one once a creation requirement is imposed.
3. **The real optimum: minimise r subject to N >= threshold.** There is a HARD mechanical
   constraint — at least one crossover per bivalent or the chromosome missegregates (the
   **obligate crossover**). So the optimum is *exactly one crossover per chromosome, with
   interference suppressing every additional one.* **That is what nearly every organism does, and
   human male meiosis sits essentially ON it: ~26 crossovers over 23 chromosomes = 1.1 per
   chromosome, barely above the segregation minimum of 1.** Female is ~1.8. Every crossover beyond
   the obligate one is pure record destruction with no compensating benefit — which is precisely
   what crossover interference exists to prevent. **Forced by the ledger, not fitted to it.**

---
## 19. CASEY'S OBSERVER CATCH — a missing term in the ledger
**Casey, 2026-09-05: "if by 'selection' you mean Natural Selection, you need an observer."**

The three operations are NOT symmetric and I had been treating them as if they were.
Growth and coupling are observer-free (bonds form, vertices attach). Retention (T1) is observer-free
(a property of maps). **Refusal requires something that distinguishes states — a measurement, hence
an apparatus.** The refusal operator is Maxwell's demon and T7 is Szilard's accounting with the
demon's own cost omitted. Every efficiency in this document left out H_obs.

This REHABILITATES the morning's most embarrassing result. The 0.50-0.65 band being a property of
the searcher was filed as contamination; it is not contamination, it is the correct physics --
**the demon's efficiency depends on the demon.** Charging H_obs = log2(candidates examined):
| policy | candidates | H_obs | raw eff | NET eff |
|---|---|---|---|---|
| greedy | 120 | 6.91 | 0.517 | **0.129** |
| exhaustive | 1128 | 10.14 | 0.556 | **0.103** |
| random | 1 | 0.00 | 0.401 | **0.401** |
**Charging the demon reverses the ordering: the cheap searcher wins.** Suggests natural selection's
random-variation-plus-differential-survival is an ECONOMY, not a limitation. NOT SETTLED: a
reversible comparison-based argmax could cut H_obs to ~1 bit per comparison.

**The definition of living is corrected.** "Sustains dR>0 with H_thermo off the floor and two
certificates" can all be done TO a system from outside -- I did exactly that to a torus fourteen
times this morning and it was not alive. **A crystal makes no refusals; a selected population's
refusals are made by its environment; a living system makes its own.**

## 20. TEST 14 — THE SELF-REFUSING RECORD SYSTEM (predictions `56ec6c22`)
State = (D, C): D in F_2^n the linkage phase, C the junctions covered by an inversion. Crossover at
j has rate r, suppressed by eps if covered; the inversion itself flips at rate rho.

**The construction forces a new definition.** If the inversion can be formed and broken freely, the
whole space is one class and R = 0. So R must be indexed by a TIME HORIZON:
> **R(T) = the record computed using only moves whose RATE exceeds 1/T.**
> The record visible to an observer who watches for time T.

**This is the canonical ordering I failed to find in Section 16.** Cost functions were arbitrary and
gave incomparable melting points; **RATES are physical.** The observer question and the temperature
question turn out to be the same question, and R(T) answers both.

| n=6, inversion over 3 junctions | R at T = 1, 10, 10^2 ... 10^7 | bit-decades |
|---|---|---|
| no inversion | 7.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 | 7.00 |
| eps=1e-3, rho=1e-5 (**pays**) | 7.00 2.50 2.50 2.50 1.00 1.00 0.00 0.00 | **9.50** |
| eps=1e-3, rho=1e-2 (breaks early) | 7.00 2.50 2.50 0.00 0.00 0.00 0.00 0.00 | **5.00** |
| eps=1e-3, rho=1 (**free self-modification**) | 7.00 0.00 0.00 0.00 0.00 0.00 0.00 0.00 | **0.00** |

- **W1 MISSED as written, HIT when corrected.** I predicted R(T) = n - #active for F_2^n but built
  on F_2^n x {inv}, forgetting the inversion's own bit. Corrected: R(T) = (n - #active) + [flip
  inactive], exact at every horizon. My formula, not the model.
- **W2 HIT.** The plateau has log-width log(1/eps) = 3 decades exactly.
- **W3 HIT. R(T) IS A STEP FUNCTION** -- flat plateaus, sudden one-bit drops, NO exponential
  attrition. **This is Casey's observed pattern** ("a trait reaches a refined state and continues
  for generations until being muted") and it is a SECOND DECAY MODE, structurally different from
  the e^(-nd) attrition of the transmission paper. Smooth erosion and sudden muting are different
  physics: attrition is ongoing recombination; muting is a generator activating.
- **W4 HIT.** The inversion must OUTLAST the protection it provides (rho < r*eps) or it buys nothing.
- **W5 HIT. Free self-modification destroys ALL record**, 0.00 bit-decades at every horizon.
  **A record cannot shelter itself if it can also freely unshelter itself. Protection requires a
  RATE HIERARCHY: the protector must be slower than the protected.** This is exactly Casey's
  "structures that are carried by others within a larger pattern", and it makes self-protection
  inherently HIERARCHICAL rather than self-contained.

**TWO RESULTS I DID NOT PREDICT.**
1. **The plateau is a MIXTURE.** At T=100 the inv=0 sector has all six crossovers hot and carries
   ZERO record; the inv=1 sector carries three bits. R = 2.50 is the mixture entropy.
   **The protected record exists only in the sector that carries the protector.**
2. **A protector that is too fast is WORSE THAN NONE: 5.00 bit-decades against 7.00.** Forming the
   inversion introduces the flip move, which mixes the inv coordinate and destroys the one bit that
   coordinate itself carried. **A fast-flipping protector is a net liability -- it costs its own bit
   and delivers no shelter.**

**And the bill, from the two constraints together:** retention wants no generators, spanning
requires them. A permanently sheltered region cannot span, so it ratchets. **Self-preservation and
degeneration are the same act** -- the Y chromosome being the limit case.

---
## 21. THE OBSERVER AUDIT (Casey: "the need for an observer enters quickly")
Sorting every result by whether a distinguisher is required:

**OBSERVER-FREE — enumeration only, nobody chooses:** all 6x6 numbers; class counts; flux as an
invariant; T1/T3/T4; Theorem 9; seams-not-bodies; coupling superadditivity; meiotic retention
n - H(d); the spanning constraint. **These stand as physics.**
**OBSERVER-DEPENDENT — someone must distinguish:** every refusal step (Arms A and B); T5's price of
a bit; T7's measured efficiency; the threshold g*. Previously fenced off as "policy-contaminated".
**Casey's correction renames them: not contaminated, OBSERVER-DEPENDENT, which is a physical fact.**
**THE THIRD CATEGORY, new:** **R(T) carries the observer in its index.** There is no observer-free
R. The honest object is **R(T, policy)** -- record relative to an observation timescale and a
distinguishing power. This is a restructure of the framework, not a caveat on part of it.

## 22. TEST 15 — COOPERATION MANUFACTURES THE HIERARCHY (predictions `ea01607b`)
**Casey's hypothesis:** pre-biological environments cheaply supply energy; semi-developed objects
enter symbiosis or combine; the COOPERATION of objects gives rise to life.
**Why testable:** Test 14's W5 says protection needs a rate hierarchy and a system cannot supply one
to itself. Two objects with different rates have one for free.

A: 4 junctions at rate 1. B: 4 junctions at rate r_B. eps=1e-3. Score = bit-decades of R(T).
| rate ratio | uncoupled | one-way (slow B gates A) | **mutual** |
|---|---|---|---|
| **1x (equals)** | 0.00 | 0.00 | **13.87** |
| 10x | 8.00 | 12.00 (+4.00) | **21.25 (+13.25)** |
| 1000x | 24.00 | 36.00 (+12.00) | 36.00 (+12.00) |

- **C2 HIT.** One-way gating with a slow partner is superadditive: +12.00 at 1000x, +4.00 at 10x.
- **C3 HIT.** Without a hierarchy, one-way gating is worth EXACTLY NOTHING (0.00 -> 0.00).
- **C5 HIT.** Every arrangement reaches R = 0 eventually. Cooperation buys time, not immortality.
- **C4 SPECTACULARLY WRONG, in Casey's direction.** I predicted mutual < one-way. Measured:
  **mutual >= one-way everywhere, and at equal rates it produces 13.87 bit-decades from ZERO.**

> **THE RESULT: mutual gating MANUFACTURES a rate hierarchy between equals.**
> A system cannot gate itself -- W5, free self-modification zeroes the record. **But two systems
> can gate each other.** The advantage is LARGEST exactly where the partners are most equal, and
> vanishes at 1000x where a hierarchy already exists and one-way does the same work.

**MECHANISM, and the frozen-state control.** At T=100, mutual/equal-rates gives R=2.311,
H_thermo=5.689, H=8.000 exactly (ledger closes). The partition is **64 mutually-deadlocked
singletons (25% of mass) embedded in one mobile bulk class of 192.** The deadlock is real: A is
gated when B has even parity and B is gated when A has even parity, so both-even states hold each
other still. **H_thermo stays at 5.69 of 8, so this is NOT the degenerate frozen case of Section 2
-- it is a LOCKED MINORITY IN A FLUID MAJORITY.** One-way at equal rates gives R=0, one class of
256, H_thermo=8: nothing held at all.

**THE SENTENCE THE WHOLE DAY WAS BUILDING TO:**
> **A system cannot be its own demon. Two systems can be each other's.**
Refusal needs an observer (Section 21); a record cannot supply its own gate (W5); but mutual gating
supplies each partner with the other as observer, and that is enough to hold a record where neither
alone could hold any. **On this evidence cooperation is not a refinement of life but a
precondition for record between equals.**

**CAVEATS, stated:** the parity gate is a CHOICE and I have not shown the deadlock mechanism is
generic; 25% of the retained mass is frozen states, which is a real if not fatal reliance on the
Section 2 caveat; one geometry, one value of eps, nA=nB=4. All three want a sweep before this
sentence travels.

---
## 23. TEST 16 — TWO IS THE OPTIMUM, IN THE GATED REGIME TOO (predictions `de492df9`)
**Correction to my reading first.** Casey said "it takes more than ONE set or pairs of nodules to
persist" -- meaning AT LEAST TWO. I read it as "more than two" and set up a test predicting against
him. He was AGREEING with Section 9 and adding a claim I had not tested: two is optimal for ERROR
AVOIDANCE, and the interface is where complexity grows.

Total junctions fixed at 12 (state space 4096 throughout):
| split | ungated | **gated (cycle or all-pairs)** | persistence |
|---|---|---|---|
| **n=2 x 6** | 0.00 | **19.87** | 10^3 |
| n=3 x 4 | 0.00 | 10.01 | 10^3 |
| n=4 x 3 | 0.00 | 5.02 | 10^3 |
| n=6 x 2 | 0.00 | 1.26 | 10^3 |

- **N2 HIT.** Two wins on bit-decades, by a factor of two over three, monotone in n.
- **N3 resolved:** persistence is IDENTICAL at every n. Extra bodies buy no duration either.
- **N4 WRONG.** All-pairs equals cycle exactly at every n -- an artifact of my rule requiring ALL
  gaters closed, which collapses the two topologies. A modelling choice, not a finding.
- **UNGATED EQUALS HOLD NOTHING AT ANY n (0.00).** Every bit is at the interface: Casey's second
  point, measured. **Seams-not-bodies now holds in BOTH regimes** -- observer-free coupling
  (Section 9) and gated assembly (here). Previously I had only the first.

## 24. WHY TWO: THE ERROR BENEFIT SATURATES WHILE THE SEAM COST GROWS
**Textbook half, not ours:** n repetition-coded copies detect n-1 errors and correct
floor((n-1)/2). n=2 detects one and corrects none; n=3 corrects one.
**Casey's refinement:** if an error SELF-MARKS -- a double-strand break, an adduct, a mismatch
recognised by shape -- you need no vote to know which copy is wrong. The damage identifies itself
and the intact copy is a repair TEMPLATE. **For self-marking errors n=2 gives full REPAIR, not mere
detection, and n=3 adds nothing.** That is homologous recombination repair, and it is what diploidy
buys.

**The optimisation, in one currency.** Let s = fraction of errors that self-mark.
n=2 recovers with probability s; n=3 recovers with probability 1. So n=3's benefit is (1-s).
Its cost is the measured seam penalty: 2 -> 3 loses **49.6%** of the record (19.87 -> 10.01).
> **BREAK-EVEN: s* = 0.504. Three bodies pay ONLY IF MORE THAN HALF OF ERRORS ARE SILENT.**
In DNA the overwhelming majority of damage self-marks, so s is near 1 and two wins by a wide
margin: a third copy would cost half the record to protect the small silent remainder.

**WHAT IS OURS:** not the coding theory, which is Hamming's. It is that **the error benefit
saturates at two while the seam cost keeps growing**, both measured in the same units, which puts
the optimum at exactly two and says by how much.

**CASEY'S OTHER THREE OBSERVATIONS, logged, NOT yet tested:**
- **Geothermal vents: life starts at the EDGE; chemicals find saturation points and locate
  preferentially; interfaces become complex.** In this framework a thermal gradient IS a rate
  hierarchy laid out in space -- fast inside, slow outside -- so an assembly straddling the edge
  gets its hierarchy from geometry rather than from mutual gating. PREDICTION TO RUN: bit-decades
  maximised at the gradient, not at either extreme.
- **Viruses are alive; they borrow reproduction.** Decomposes the three legs across bodies: a virus
  supplies the record and a demon (receptor specificity IS a distinguishing operation) and borrows
  capacity and construction. **Repairs the Section 21 definition: living = the three legs are
  present, they need not all be in one body.** A virus alone is one leg; virus plus host is alive.
- **The propagation "mat" that allows chemical reactions to occur** -- a structure whose function is
  to gate other systems' moves. The gate as a SERVICE, supplied by a specialist.

---
## 25. TESTS 17-20 — THE ORIGIN LADDER (Casey's sequence, made quantitative)

### 25.1 Test 17: a population of cooperating pairs (`b354801f`) — the demon is reproduction
No fitness function anywhere. The protection parameter theta is ENCODED IN THE RECORD IT PROTECTS;
individuals copy at interval T; junctions active at horizon T scramble before the copy is read.
**P1 control HIT** (protection disabled -> uniform). **P2/P3/P4 HIT:** the population concentrates
on exactly the theta that survive one copy interval and shows NO preference among them --
T=10 keeps weak protection at 30%, T=10^4 goes to 96% on the strongest, T=10^5 (nothing survives)
stays uniform like the control. **Selection is TIMESCALE-RELATIVE: no drive to maximum protection,
only to sufficient protection at the reproduction rate.**
**HONESTY: this is close to definitional** -- a theta that scrambles cannot transmit itself. The
simulation demonstrates the logic rather than confirming it independently.
**The real finding came from trying to fix that:** protection here is free, and its true cost is the
spanning constraint. But **exploration only costs you something if there is something to find** --
transmission alone can never generate pressure to explore.
> **The reproduction-demon selects for RETENTION. It cannot select for EXPLORATION. That needs a
> second demon: an environment that moves.** Two observers, pulling opposite ways.

### 25.2 Test 18: the receptor as the first blind demon (`6edcfa99`) — ALL FIVE HIT
A receptor does not measure-then-decide; the measurement IS the decision, nothing is stored, nothing
erased, **H_obs per read = 0**. But its specificity is a record that must be held.
> **The demon's price is not per-read. It is the standing maintenance of the distinguisher's shape.**
| | |
|---|---|
| R1 | Interior optimum **b* = log2(c ln2 / mu)**, matched to grid resolution |
| R2 | b* **identical at v = 1, 10, 100** -- selectivity is set by the cost of MISTAKES, not the value of the prize |
| R3 | +2 bits per 4x in c; -2 bits per 4x in mu |
| R4 | Environment CAPS selectivity: p=0.5 -> b=1.0, p=0.1 -> 3.25, p<=0.01 -> interior 5.12. **The copiotroph/oligotroph split, not built in** |
| R5 | **b*=0 once mu > c ln2.** When the record decays faster than specificity pays, the optimal eater is INDISCRIMINATE |

### 25.3 Test 19: build cost, maintenance, order of construction (`1f1f8fee`)
- **BOOTSTRAP: 2000 of 2000 parameter sets produce ZERO rungs when every form has B > 0.**
  The origin requires at least one function that costs nothing to build. (Found by the instrument
  failing: I argued the constraint in the prediction file and then omitted a B=0 form from the menu.)
- **L1 HIT: digestion first in 100.0%** of the 1512 sweeps that started.
  **L5 HIT, EXCEPTIONLESS: selection first in 0 of 2000.** Forced by the production/saving
  asymmetry -- selection's return is bounded by throughput, which is zero before digestion.
- **L2 HIT: the ladder is driven by SURPLUS, not capability.** A form that exactly repays its own
  maintenance is adoptable and contributes NOTHING: zero rungs against fourteen.
  **This is Casey's "energy bonus", measured.**
- **L3 MISS, and better than the prediction. COMPLEXITY COMPOUNDS IN BURSTS.** Waits ran
  1.05 0.42 0.46 0.32 0.44 0.67 1.08 1.82 3.16 5.59 10.04 18.25 | 0.03 0.06 0.11 --
  shortening within a form type, LENGTHENING as geometric build costs outrun linear surplus, then
  **collapsing 500-fold when a qualitatively new form type unlocks.** Punctuated, not smooth, and
  not built in. Adoption order overall: **digestion -> selection -> structure.**
- **L4 UNTESTED:** the run hit my rung cap at 16 rather than stalling naturally.

### 25.4 Test 20: the cup, the second cup, the second opening (`d9657787`)
Casey's sequence introduced the element my ladder lacked: **WASTE**. The binding early constraint
is not energy but FOULING -- a one-aperture cup re-ingests its own output.
- **G1 HIT at the exact threshold.** NET_one has an interior optimum **iff c > p**; NET_two is
  monotone. **A sac-gut organism has an optimal feeding rate; a tube-gut organism does not.**
- **G2 HIT, stronger than predicted.** The one-hole form does not merely fall behind, it goes
  **NET NEGATIVE at i >= 1**: a sac-gut that feeds too fast starves on its own waste. Sign change,
  not a factor. The two-aperture advantage grows without bound.
- **G3 (interpretation, flagged):** the second aperture splits one generator into two. With one
  hole, in and out are the same channel and nothing distinguishes them; with two they are distinct
  and "which end" is a certificate. **The through-gut is the first body axis.**
- **G4 HIT.** Geometric selection carries ZERO maintained record -- the aperture IS the body's shape
  -- so it is adoptable at EVERY mu, including mu > c ln2 = 0.693 where Test 18 says chemical
  selection cannot pay at all.

### 25.5 THE ORDERING (Casey, 2026-09-05: "first you have geometry, that's free. Then form and
### function modify the form.")
> **TIER 0 -- GEOMETRY. Free.** A cup that forms, a hole of a size, a flow that sorts by speed.
> It costs nothing because it IS the shape rather than a record of one. **The first observer is
> geometry**, and that is why the observer problem of Section 21 has a cheap solution at the origin.
> **TIER 1 -- FORM. A paid record**, with a build cost and a maintenance cost, which the function
> must repay with a surplus (Test 19 L2).
> **TIER 2 -- FUNCTION MODIFIES FORM.** Self-reference: Test 14's self-modifying move set, arriving
> LAST rather than first, and requiring the rate hierarchy that Test 15 showed two bodies supply.

This resolves R5's ordering problem: **geometry (free) -> form (paid record) -> function modifies
form (self-reference)**, with chemical selectivity entering only once retention is cheap enough to
hold a shape.

---
## 26. TEST 21 — THE NATURAL LIMIT IS THE ENVIRONMENT (predictions `c7b110b9`)
**Casey, 2026-09-05: "You have a 'natural' limit because the 'assembly' must interface with the
environment and environments change."** This answers L4, which Test 19 left untested. **The limit is
EXTERNAL** -- not internal cost growth.

MECHANISM: if the environment shifts on timescale T_env, no form's useful lifetime exceeds T_env,
so payback becomes g > m + B/T_env. Build costs grow geometrically, surplus at best linearly, so
there is a computable last rung. Second mechanism: an environmental shift IS a generator
activation, so by W3 the loss should be a STEP.

**FIRST RUN VOIDED BY MY OWN KILL CRITERION.** E4 (T_env = infinity must be unbounded) FAILED:
the ladder stalled at 24 rungs, because my `horizon` parameter (1e6) was itself acting as a finite
T_env -- at rung 24, B/horizon = 16.8 exceeded the surplus of 12.95. That also explains why
T_env = 1e6, 1e7, 1e8 all returned exactly 24 and wrecked the log fit. **The pre-registered control
caught an artifact that would otherwise have produced a publishable-looking wrong number.**

**RERUN with horizon decoupled (3000 x T_env):**
| T_env | 1e1 | 1e2 | 1e3 | 1e4 | 1e5 | 1e6 | 1e7 | 1e8 | 1e9 | 1e10 |
|---|---|---|---|---|---|---|---|---|---|---|
| mean rungs | 2.00 | 7.90 | 11.55 | 15.10 | 18.70 | 22.30 | 25.80 | 29.45 | 32.80 | 36.50 |

- **E4 HIT:** T_env = infinity gives 400 rungs (the cap). The environment is now the only limit.
- **E1 HIT:** a finite stall at every finite T_env, with no cap doing the work.
- **E2 HIT: R^2 = 0.9966, slope 3.697 rungs per decade.**
  > **COMPLEXITY IS LOGARITHMIC IN ENVIRONMENTAL STABILITY.**
  > Each tenfold increase in stability buys ~3.7 more rungs. **To double complexity you must
  > SQUARE the stability.**
- **E2b:** measured slope / log2(10)/log2(beta) = **1.077, 1.075, 1.070, 1.072, 1.094** across
  beta = 1.5, 2, 3, 4, 6 -- constant to 2%. The ceiling is set by geometric build cost against
  linear surplus exactly as the mechanism predicts, with a steady ~7.5% bonus from partial
  carry-over across shifts.
- **E3:** build cost binds harder than maintenance (beta 1.5->4.0 moves rungs 35.4->9.9, a 3.6x
  effect; mgrow 1.0->1.6 moves 20.1->11.0, 1.8x).
- **E5 HIT:** sawtooth with multi-rung drops (15->6, 16->7, 16->7). Accumulation in bursts (L3),
  loss in steps (W3). Both confirmed in one time series.

**THE READING.** Nothing forbids the twentieth rung. It is that the twentieth rung needs an
environment that holds still a thousand times longer than the tenth did. **Complexity is not
limited by what can be built; it is limited by how long the world stays the same.**

**AND IT LANDS ON CASEY'S VENTS.** Deep hydrothermal systems are among the most STABLE environments
on Earth, and the vent EDGE additionally supplies a spatial rate hierarchy at no cost (Section 25.5,
tier 0 geometry). **Stability buys rungs; the gradient buys the demon.** Both at the same place --
a reason for life to begin there that does not require the chemistry to be special. The vent-edge
experiment is still unrun and this is now its prediction.

---
## 27. TEST 22 — COMPLEXITY AS A TREE (predictions `67c46c9c`)
**Casey:** complexity is like the limbs of a tree, branches spreading in almost random directions to
gain energy, filling niches, utilising the environment more effectively.

**TWO RUNS VOIDED BY MY OWN INCONSISTENCY.** 22a measured the ALL-TIME max over 400 shifts and found
branching worthless (b = 0.064 rungs/decade, and a nonsense "exchange rate" of 10^56 from dividing
by ~0). 22b measured the FINAL SNAPSHOT and found branching decisive but produced a NEGATIVE
stability coefficient (-0.242) contradicting Test 21's solid +3.697 at R^2 = 0.9966.
**I changed the statistic between runs.** An all-time max is dominated by the luckiest interval; a
final snapshot is often taken just after a catastrophe. Neither counts.
Also diagnosed in 22a: **I had not built a tree.** A pruned branch restarted from ZERO, which is
n independent ladders. A tree has DESCENT -- what replaces a dead limb grows from a surviving limb.

**22c, with a consistent statistic (time-averaged sustained max):**
| | n=1 | n=128 | gain |
|---|---|---|---|
| **descent ON** | 8.18 | **12.20** | **+4.02** |
| descent off | 8.18 | 10.11 | +1.93 |
- **T1 HIT: branching raises the ceiling, and DESCENT ROUGHLY DOUBLES THE BENEFIT.**
- Stability slope independently reproduced: n=1 runs 8.18 -> 23.10 over four decades =
  **3.73 rungs/decade**, against Test 21's 3.697. Two separate models, same constant.
> **EXCHANGE RATE: ~3.7 rungs per decade of STABILITY, ~1.9 per decade of DIVERSITY.
> One decade of stability is worth about a HUNDREDFOLD more branches.**

## 28. TEST 23 — THE VENT EDGE (predictions `5d700ad5`)
First run mis-scaled (rates spanned 1e3..1e-3 while thresholds spanned 1e0..1e-6, so every site read
as active). Rerun with rate range and horizon range matched.

| position, at T = 1 | R | H_thermo | verdict |
|---|---|---|---|
| hot end x=0.00 | **0** | 12 | **GAS -- melted** |
| middle x=0.35 | **6** | **6** | **ALIVE** |
| cold end x=0.70 | 12 | **0** | **CRYSTAL -- frozen** |

- **V1, V2 HIT** -- the two deaths, and **R is MAXIMAL at the cold end, exactly where the system is
  most dead.** Section 2's caveat appearing spatially.
- **V3 MISS, and it indicts my own score.** Bit-decades counts R without checking H_thermo, so it
  is maximised by the CRYSTAL (peak at centre 0.85-0.95). **The metric recommends being frozen.**
  Score the living condition, not bit-decades.
- **V4 FAILED AS STATED, and the failure is better than the prediction.** The living condition holds
  at ALL 19 positions -- but at DIFFERENT HORIZONS. c=0.05 is alive at T=1e-5..1e-3; c=0.95 at
  T=1e3..1e5. The alive window SLIDES with position.
  > **The gradient does not localise life to one place. It provides a place for EVERY TIMESCALE.**
  > Fix an observer's horizon and the edge is where life is; let the horizon float and every
  > position is somebody's edge. The same observer-relativity as Section 21, laid out in space.
- **V5 HIT.** Wider spans are alive across more horizons: 1 of 13 at w=0.02, **11 of 13 at w=1.0**.
  Straddling more gradient buys more timescales. **Casey's "specialisation from geometry or
  position": generalists buy timescale-breadth, specialists buy one timescale.**

**WHY THE VENT PAYS TWICE.** Deep hydrothermal systems are unusually STABLE (Section 26: 3.7 rungs
per decade of stability) AND supply a free spatial rate hierarchy at the edge (tier 0 geometry,
Section 25.5). **Stability buys rungs; the gradient buys the demon.** Neither requires the chemistry
to be special.

**INSTRUMENT FAILURES TODAY, all caught by controls or obviously-wrong output:** the grid-adjacency
KAM instrument (blind to tori); the sorted-homolog canonicalisation; the horizon masquerading as
T_env; the inconsistent tree statistic; the mis-scaled vent gradient. **Five. Every one caught,
none of them by luck, and two of them by pre-registered kill criteria that fired exactly as written.**

---
## 29. TEST 24 — IS THERE A UNIVERSAL BALANCE R/H? (predictions `4bced128`) — TEST DISQUALIFIED
Casey: "we will find the balance of stability/growth in all living objects", and our
inorganic/dead-organic/life prejudice is SUBSTRATE BIAS.
Since H = R + H_thermo is an identity, balance is one number: **R/H** (0 = gas, 1 = crystal).

Measured over 79 intermediate systems across four substrates: mean 0.382, sd 0.223 against
uniform's 0.289; peak bin 0.2-0.3; per-substrate means 0.315 / 0.289 / 0.500 / 0.500, spread 0.211.
**B1, B2, B3, B5 all MISS.**

**BUT I DISQUALIFY MY OWN TEST.** I swept parameters UNIFORMLY -- meiosis over all |J|, vent over
all positions -- so the measured distribution of R/H is the distribution of MY SWEEP, not of
anything living. Meiosis returning exactly 0.500 with sd 0.250 is the tell: that is what a uniform
sweep of R = n-|J| must give by construction. The gated pairs' sd of 0.000 is not universality
either -- it is ONE configuration sampled nine times. **A uniform parameter sweep is not an
ensemble of living systems.** Fifth "search that cannot succeed" today.

## 30. TEST 25 — THE FLOOR IS ONE GENERATOR, NOT ONE BIT (predictions `9e8879c0`)
**Casey, reframing 24: "at the cold edge where things are stable but still move -- that's balance",
and "new organisms develop near stability but with at least one degree of freedom."**
Not R = H_thermo. **R as high as possible SUBJECT TO H_thermo > 0.** My own Arm B data already said
so: froze at R/H = 0.991, marginal 0.958, SUSTAINED 0.863 -- all against the crystal end, none near
0.5. And structurally: if the invariant is "one degree of freedom" it is **H_thermo, an ABSOLUTE
quantity -- not a ratio.** As H grows R/H -> 1 automatically, which is why B3 failed while the
underlying claim was right.

| substrate | H_thermo at the living boundary | R/H at the boundary |
|---|---|---|
| **meiosis n = 6,8,10,12,16** | **1.0000 at every size** | 0.833 -> 0.938, drifting up |
| gated pairs 3x3,4x4,5x5 | 4.19, 5.69, 7.19, growing | 0.302, 0.289, 0.281, flat |
| dimer tori | **INVALID** -- see below | |

- **MEIOSIS CONFIRMS CASEY EXACTLY: H_thermo = 1.0000 bit at every system size**, one active
  generator and no more, while the ratio drifts with size. O2 confirmed on the abelian substrate.
- **GATED PAIRS SAY THE OPPOSITE:** floor grows, ratio flat.
- **DIMER ROWS INVALID:** my boundary definition took the last state with H_thermo > 0, which for
  dimers is a state where R had already collapsed to 0 -- a gas, not a boundary. So O1's mean of
  2.605 and O3's "hit" are contaminated and I withdraw both.

**THE REFINEMENT, which is the real result:**
> **The floor is ONE GENERATOR, not one bit. It equals one bit only where the generators are
> INDEPENDENT.** In meiosis crossovers commute and activate one at a time, so the boundary holds
> exactly one bit. In the gated system all of A's junctions unlock at once when B turns odd, so the
> smallest available step is a BLOCK. **Coupled machinery must carry more freedom than it would
> choose.** Prediction: the nearer a system's degrees of freedom are to independent, the closer it
> can live to the stable edge.

## 31. BODY TEMPERATURE IN BITS (Casey: "humans are barely above ambient; tradeoff of form and energy")
Rates are Arrhenius, so the framework's unit is BITS OF RATE, not kelvin. **One bit costs
ln2*R*T^2/Ea = 10.4 K** at Ea = 50 kJ/mol, T ~ 300 K.
| | dT | **bits of rate** |
|---|---|---|
| bird (41C) | 21 K | **1.98** |
| human (37C) | 17 K | **1.62** |
| mouse (37C) | 15 K | **1.42** |
| reptile basking | 10 K | 0.94 |
| hibernating mammal | 5 K | 0.55 |
| ectotherm / deep sea / thermophile | 0 | **0.00** |

**Every endotherm sits between ONE AND TWO BITS above ambient**, and hibernation is a system
deliberately dropping to half a degree of freedom.
**MY FIRST TRADE-OFF MODEL WAS BROKEN AND IS WITHDRAWN:** I described benefit as saturating and then
reversing, and coded it LINEAR against a linear cost, so the optimum ran to the boundary at 79 K.
**Corrected** (gain = min(b,1); each further bit ACTIVATES a generator and MELTS a bit, Theorem 8;
cost linear in dT): **optimum at 10 K = 0.96 bits.** Humans sit at 1.64.
**What the framework earns is the ORDER** -- why the margin is ~10 K and not 1 or 100 -- and Ea, T
are chemistry while the one-generator floor is Theorem 8. Nothing fitted.
**And the factor of 1.7 has an explanation from Section 30:** the floor is one bit only for
INDEPENDENT generators. Humans are coupled machinery, so their floor sits above one bit.
**1.64 bits is "a little more than one, because your generators are not independent."**

---
## 32. TEST 26 — THEOREM 9 IS AN EQUALITY, NOT A BOUND (predictions `b2d734a8`, autonomous)
The morning's open problem: Theorem 9 gave R >= H(fibre) with an unexplained 0.1332 undershoot on
4x6 dimers, and "equality iff transitive" is a CONDITION, not a characterisation.
**The fix: classes REFINE fibres, so by the chain rule the bound is the first term of an EXACT
decomposition.**
> **R = H(phi_* mu on V/Lambda) + H(class | fibre)**

| system | R | H(fibre) | **defect** | exact? |
|---|---|---|---|---|
| 4x6 faces | 2.2572 | 2.2572 | **0.0000** | EXACT |
| 4x6 cycles4 | 0.8240 | 0.6908 | **0.1332** | EXACT |
| 4x4 faces | 2.3159 | 2.2865 | 0.0294 | EXACT |
| 4x4 cycles4 | 0.2797 | **0.0000** | **0.2797** | EXACT |
| 6x6 faces | 2.3504 | 2.3500 | 0.0004 | EXACT |

- **D1 EXACT to machine precision in all five. D2 HIT: the defect is 0.1332**, the morning's
  "unexplained undershoot", now a named term.
- **D3 CONSISTENT in all five: the defect vanishes iff every fibre is a single class.** So the
  tightness condition is a **pure connectivity check on the move graph -- no entropies needed.**
- **D4: in the abelian case cosets ARE orbits, so the defect is identically zero.** *This is why
  meiosis gave R = (L-1) - |J| exactly and dimers never could.*

**THE INTERPRETATION: H(class|fibre) is THE RECORD THE CERTIFICATE CANNOT SEE.** On 6x6 faces it
is 0.0004 -- flux sees essentially everything. On 4x4 all-4-cycles it is 0.2797, which is ALL of R:
the certificate is worthless there and every bit of record is hidden from it.
**Paper 2's Theorem 9 should be restated as this equality.**

## 33. TEST 27 — G3 WITHDRAWN AS A RECORD CLAIM (predictions `e8fd66d3`, autonomous)
The last thing I had argued rather than computed: that a second aperture makes "which end" a
certificate -- the through-gut as the first body axis.
- **G3a HIT, exactly.** Cycle rank b1 = |E| - |V| + 1 goes **2 -> 3 -> 4** per added aperture, in
  all four geometries. Pure Euler. **A one-aperture cup's opening is a BRIDGE: no cycle passes
  through it, so it can carry no winding.** That half is a theorem.
- **G3b MOSTLY MISS.** Only C6xC6 gained record (1 -> 2 classes); C4xC4, C6xC4, C8xC4 gained
  nothing, and the chamber-size sweep gave **+0 at m = 4, 6, 8, 10.** G3e MISS. G3c not reachable.
- **WHY:** a single aperture edge can never be USED -- using it leaves an odd number of vertices in
  the ring, so no perfect matching exists. Two apertures can be used together, which is when extra
  states appear. **Whether the new topological coordinate is REALISABLE depends on the geometry,
  not on the cycle rank.** This is T5's realizability premium: the gap between the topological
  floor and what the construction can actually achieve.
- **VERDICT, per my own pre-registered commitment ("I would then withdraw it rather than keep
  arguing"): the body-axis claim is WITHDRAWN.** The topology is necessary and not sufficient.
  The instrument had 4-5 states and was too small to be decisive, so this is UNSUPPORTED rather
  than REFUTED. What would settle it: a chamber with a real state space rather than a bare ring.

---
## 34. B4 + TEST 28 — THE BALANCE EXISTS, AT R/H ~ 0.8, AND IT IS SUBSTRATE-INDEPENDENT
**B4 (the dynamic criterion, registered in `4bced128` and finally collected):** trajectories
selected by SUSTAINING (R rising, H_thermo off the floor) rather than by a parameter grid:
**mean R/H = 0.791, sd = 0.085, range 0.601-0.912, n=11** against uniform's sd 0.289.
**Test 24's failure was my uniform sweep, not the absence of a balance.**

**THE CONFOUND, and Test 28 (`1fdb25f1`) breaking it.** Test 25 (meiosis, STATIC boundary) said the
FLOOR is invariant (H_th = 1.0000 exactly at every n); B4 (dimers, DYNAMIC) said the RATIO is
(4.6x tighter). Two things differed at once -- criterion and substrate. Running the DYNAMIC
criterion on the ABELIAN substrate separates them:
| | H_thermo rel sd | R/H rel sd | verdict |
|---|---|---|---|
| dimers, dynamic (B4) | 0.499 | **0.108** | ratio |
| abelian, dynamic (T28) | 0.714 | **0.114** | ratio |
**S2, and I predicted S1 -- a clean miss. THE CRITERION IS THE VARIABLE, NOT THE SUBSTRATE.**
Test 25's exact 1.0000 was an artefact of the STATIC definition, not of independent generators.

> **THE RESULT: sustaining systems cluster at R/H = 0.791 +- 0.085 (dimers) and 0.829 +- 0.095
> (abelian) -- two completely different substrates, 0.04 apart.**
> **Casey's balance is real, sits at ~0.8 (near stability with freedom left, NOT my predicted 0.5),
> and is SUBSTRATE-INDEPENDENT -- which is his substrate-bias claim, measured.**
B3 failed this morning only because I sampled parameters uniformly instead of selecting by
sustaining. Under the right criterion it holds.

## 35. CARBON: THE ALGEBRA, AND THE NUMEROLOGY I DECLINE
**Casey: "carbon = 6, the double bonds and stability are essential for the balance of stability and
growth. It's more the algebra than numerology."**

**A. VALENCE 4 IS THE MINIMUM THAT STORES A RECORD AT A SITE.** The record at a substituted centre
is the number of orbits of substituent assignments under the site's ROTATION group -- exactly a
Theorem 9 certificate, a value the moves cannot shift.
| geometry | valence | orbits | record per site |
|---|---|---|---|
| trigonal planar (sp2) | 3 | 1 | **0.00 bits** |
| tetrahedral (sp3) | 4 | 2 | **1.00 bit** |
| trigonal bipyramidal | 5 | 20 | 4.32 bits |
| octahedral | 6 | 30 | 4.91 bits |
**Valence 3 gives no chirality and zero bits; valence 4 gives exactly ONE BIT per centre** -- the
one-generator floor of this framework, in chemistry. Chain algebra agrees: two bonds continue a
backbone leaving v-2 free, so **4 is the first valence that can polymerise AND carry information at
every monomer.**

**B. SIX-RINGS ARE ANGLE ALGEBRA.** A strain-free planar n-ring needs 180(n-2)/n = theta, so
**n = 360/(180 - theta)**. sp2 at 120 deg gives **n = 6.000 EXACTLY**; sp3 at 109.4712 gives 5.104,
which is why cyclopentane is the near-strain-free sp3 ring and cyclohexane must pucker.
**Benzene's six is forced by 120 degrees, and 120 degrees is forced by three sigma bonds in a plane.**

**C. WHAT I DECLINE.** Carbon's atomic number 6, the ring size 6, and BST's C_2 = 6 are THREE
DIFFERENT SIXES -- ring size from 360/(180-120), atomic number from nuclear charge. They coincide
numerically and I have no derivation linking them. Asserting one would be precisely the numerology
Casey excludes. **What is defensible is that both real results above are statements about MOVE SETS
AND THEIR INVARIANTS**, which is this framework's subject.

**RETRACTION, same hour, self-caught.** Section 34 above reported R/H ~ 0.8 as a substrate-
independent universal. **It is not.** On the abelian substrate the steady state has a closed form:
with growth adding g junctions of which fraction f are active and refusal removing one active
generator per step, J/n -> f - 1/g, so **R/H -> 1 - f + 1/g**. That reproduces all seven measured
values to a mean error of **0.023** and spans 0.667-1.000 over the grid I swept, against a measured
range of 0.661-0.956. **THE SPREAD IS THE GRID** -- the identical error that disqualified Test 24,
committed a second time in the experiment built to repair it.
**WHAT SURVIVES:** a ONE-SIDED BOUND -- sustaining systems sit above R/H = 0.6 in every case, never
near the 0.5 I predicted and never at either death. Consistent with Casey's "near stability with at
least one degree of freedom", but a bound, not a number. The two substrates' overlapping ranges are
suggestive of substrate-independence, not a demonstration of it.
**DOCTRINE:** *a tight distribution over a swept parameter is a property of the sweep until shown
otherwise.* Twice in one day.

**RING CAPACITY vs STRAIN (Casey: "6 allows more distance and options; chemistry becomes ornate at 6").**
Distinguishable substitution patterns modulo the dihedral group = the ring's record capacity.
| n | distances | isomers | record | sp2 strain |
|---|---|---|---|---|
| 3 | 1 | 4 | 2.00 | 3600 |
| 4 | 2 | 6 | 2.58 | 900 |
| 5 | 2 | 8 | 3.00 | 144 |
| **6** | **3** | **13** | **3.70** | **0** |
| 7 | 3 | 18 | 4.17 | 73 |
| 8 | 4 | 30 | 4.91 | 225 |
**6 STRICTLY DOMINATES 3, 4, 5 ON BOTH AXES** (less strain AND more record); 7-10 beat it on
capacity only by paying strain it does not pay. **Six is the first ring size at which
distinguishable arrangements are FREE.** A hexagon is also the smallest ring with three distinct
positional relationships (ortho/meta/para) -- the concrete content of "more distance and options".

---
## 36. AUTONOMOUS AUDIT PASS (Casey away on the renovation; "clean up our work")
Audited the three papers against the four failure modes today established I am prone to: claims
without their hypotheses, a swept parameter reported as a distribution, a metric that rewards the
degenerate case, and an inconsistent statistic. Four fixes:

1. **The R/H ~ 0.8 "universal" RETRACTED from Paper 2 within the hour of writing it** — the abelian
   closed form R/H = 1 - f + 1/g reproduces every measured value to 0.023 and spans the whole
   measured range over my own grid. Replaced with the one-sided bound (sustaining systems sit above
   0.6). **The identical error twice in one day, the second time in the test built to fix the first.**
2. **The hotspot fraction is CONTESTED and Paper 1 quoted only the classic figure.** Literature has
   ~80% of recombination in <15% of the genome, but larger recent samples give ~39% of crossovers in
   10% of sequence, and ~40% of events fall outside LD-defined hotspots. Replaced the point estimate
   with a range: gain = log2(1/f) is **1.0 to 4.3 bits per crossover** over f = 0.5 to 0.05, and the
   falsifiable prediction restated in a form independent of the disputed number.
3. **"Every endotherm sits at 1-2 bits" was three species.** Hedged: three species is not a survey,
   Ea spans 30-80 kJ/mol (a factor ~2.7 either way), and "ambient" is a choice. **What survives is
   the order of magnitude, plus ectotherms at exactly zero, which needs no Ea assumption.**
4. **Human map figures verified against the literature rather than memory.** Female 4460 cM, male
   2590 cM; 1 cM ~ 1 Mb confirmed (this morning's label correction was right). My "male ~26
   crossovers, 1.1 per chromosome" is exact (25.9/23 = 1.13); female is 1.94, not the 1.8 I quoted.
   Sex-averaged map 35.3 Morgans, not 34; block counts corrected to 58 / 376 / 3,553.

**Also completed autonomously:** Theorem 9 restated as an EQUALITY with a defect term (Section 32);
G3 withdrawn per its own pre-registered commitment (Section 33); the balance question settled as a
bound (Section 34); the carbon valence and ring-capacity algebra (Section 35); Paper 2 restructured
around the observer and R(T); **Paper 3 written** (`Lyra_PAPER_complexity_exploits_energy`, 326 ln).

---
## 37. THE CONTINUUM, AND A CORRECTION TO MY OWN NEGATIVE (Casey: "do we have a link between BST
## physics and complexity in the continuum?")

**THE LINK IS FORMAL AND IT IS EXACTLY ONE THING.** Both frameworks compute a QUOTIENT BY A GROUP
ACTION: retention gives S/<M> (classes are orbits); a homogeneous domain gives G/K. Theorem 8's
discrete statement -- **R is the codimension of the orbit** -- is the finite case of that same
construction.

**THE CONTINUUM ANALOGUE OF R IS A DIMENSION, NOT A COUNT.** In the continuum the orbit space is a
manifold, so counting classes diverges. Regularising at resolution eps gives the Kolmogorov
epsilon-entropy **R(eps) ~ dim(orbit space) * log2(1/eps) + O(1)**, whose LEADING COEFFICIENT IS THE
DIMENSION. **R(T) (Section 8b of Paper 2) is exactly the regularisation that makes it finite.**
For D_IV^5: dim SO(5,2) = 21, dim[SO(5) x SO(2)] = 11, so dim_R = **10**, dim_C = **5**.

**WHAT I DECLINE.** n_C = 5 "being" the complex dimension is NOT evidence -- D_IV^5 *means* the
type-IV domain of complex dimension 5, so pointing at it would be reading the label back. This is
**shared formalism, not shared content**: the two frameworks agree on WHAT to look at in the
continuum (the dimension of a quotient) and nothing more. **No derivation in either direction.**
A genuine link would DERIVE a particular dimension from a retention principle; I have neither such
a derivation nor a candidate, and say so.

**THE CONCRETE PAYOFF IS A CORRECTION TO MY OWN PAPER.** I concluded this morning, after the
standard-map instance failed twice, that "R may not be measurable off a lattice" and wrote it into
Paper 2 as a limit of the framework. **That was too pessimistic and it was wrong.** Both instruments
COUNTED CONNECTED COMPONENTS; the invariant structure of a near-integrable map is a positive-measure
Cantor set of tori, not a partition into countably many classes. **Counting was the wrong
functional and no grid refinement repairs it.** The right continuum quantity is the MEASURE of the
non-mixing set -- which I had already measured in the diagnostic run only to confirm the physics
existed: 1.000 at K = 0.2..0.97, then 0.980 / 0.653 / 0.389 / 0.172 at K = 1.2 / 1.5 / 2.0 / 3.0.
**That is R in the continuum. It decays SMOOTHLY, which scores J4 (continuum melting is gradual) --
the prediction I could not score this morning -- and supplies the THIRD CATEGORY the abelian /
non-abelian split needed: abelian melts linearly, non-abelian off a cliff, CONTINUUM smoothly
because generators enter continuously.**

---
## 38. CORPUS RECONNECT (Casey: "reconnect your work with the corpus")
I worked Lane B all day without touching the corpus. Reconnecting found three things, two of which
demote claims I made today.

**1. LANDAUER AND THE DEMON ARE ALREADY IN THE CORPUS.** `BST_AC0_Thermodynamics.md` Section 6
states Landauer's principle and, verbatim: *"Maxwell's demon is defeated. Any demon that acquires
information to reduce entropy must eventually erase that information... The books always balance."*
**My Section 21 "the refusal operator is Maxwell's demon and T7 is Szilard with the demon's cost
omitted" is a REDISCOVERY of registered corpus content, not a discovery.** What I add is the
MEASUREMENT (greedy 0.129 vs random 0.401 net once H_obs is charged) and the receptor argument
(the cost is standing maintenance of the distinguisher, not a per-read charge). The principle is
the corpus's. Papers must say so.

**2. THE SHANNON CHARGE.** `BST_AC0_InformationTheory.md` Section 9 defines
Q(phi) = sum_i H(C_i) - H(joint) -- "the gap between parts and whole" -- a Noether charge with a
conservation theorem (T33). **Same SHAPE as my interface result. Not the same quantity.** Computed
correctly (parts = each system ALONE, no partner, same horizon):
| nA x nB | R(A alone) | R(B alone) | R(pair) | Q_R = parts - whole |
|---|---|---|---|---|
| 3x3 | 0.0000 | 0.0000 | 1.8113 | **-1.8113** |
| 4x4 | 0.0000 | 0.0000 | 2.3113 | **-2.3113** |
| 5x5 | 0.0000 | 0.0000 | 2.8113 | **-2.8113** |
Three differences, all stated: computed on the CLASS entropy not the state entropy; **OPPOSITE
SIGN** (the coupled record is superadditive, the 3-SAT charge subadditive); and mine has no
conservation theorem. **The synergistic counterpart of the Shannon charge, not a rediscovery of T33.**
*(A METHOD ERROR ON THE WAY: my first script printed "Q_R is NEGATIVE" while its own table showed
+7.19 -- I hardcoded the verdict into the print statement before seeing the output, and the marginal
was wrong besides (it held the partner FIXED rather than removing it). Both fixed; the corrected
run computes the verdict from the numbers.)*

**3. MY OWN AUGUST FALSIFICATION IS DIRECTLY RELEVANT.** `Lyra_C2_lane_CLOSED_by_FALSIFICATION...
2026-08-24` already has **record production and three natural clocks** in a cosmological setting:
Koons tick (T2405, m=0), horizon clock (m=-1), and **the per-record commit clock (m=+1)** -- one
tick per newly committed record -- which falsified C2 and forced C2'. **R(T) needs exactly a clock,
and the corpus already has three with a banked identity (R57, verified 4/4).** This is the natural
place to connect R(T) to BST proper and I have not done it.

## 39. TEST 29 — CHEMISTRY: REACTION NETWORKS ARE MOVE GRAPHS (predictions `623e764b`)
Not analogy -- the same linear algebra. A reaction network's stoichiometric matrix S gives reachable
compositions x0 + image(S) (a COSET) and conservation laws = left null space of S (functions
constant along every reaction). **Cosets and certificates: Theorem 9 exactly.**

- **C1 HIT, exactly, on every network: R = n_species - rank(S) = the number of independent
  conservation laws.** Theorem 8 in chemistry, to integer precision.
- **C2 HIT:** R >= number of distinct elements in all three elementally-closed cases.
- **C3 HIT, and this is the striking one. ONE REACTION = ONE BIT, on real combustion chemistry.**
  Adding H2-combustion chain steps one at a time: R = 6, 5, 4, 3, 2, 2 -- **four independent radical
  steps cost exactly one bit each, and the fifth (H + OH -> H2O) costs ZERO because it is linearly
  dependent on the earlier four.** The instrument found that dependency on its own. An explicitly
  constructed dependent reaction likewise costs nothing.
- **C4 MISS, and the miss inverts my prediction.** I predicted a catalyst adds reactions without
  adding a generator -- pure rate, no record cost. Measured: Michaelis-Menten takes rank 1 -> 2 and
  **R from 3 to 2. The catalyst DESTROYS a conservation law**, coupling E and ES which were
  separately conserved.
  > **CORRECTED READING: CATALYSIS DESTROYS RECORD.** A catalyst moves a generator across the
  > observation threshold, and by Theorem 9 that melts. An enzyme that speeds racemisation destroys
  > chirality; any catalyst that speeds equilibration destroys the non-equilibrium record.
  > **Hence a reason for enzyme specificity I had not seen: a promiscuous catalyst melts many
  > records at once, a specific one activates exactly one generator and costs exactly one bit.
  > ENZYME SPECIFICITY IS RECORD PRESERVATION** -- the complement of Test 18, where specificity
  > cost record to MAINTAIN. Both sides of one ledger.
- **C5 (autocatalysis needs >= 2 reactions touching the autocatalyst) NOT YET TESTED.**

## 40. CHEMISTRY, CONTINUED — WHAT A METABOLISM COSTS AND HOW A GENOME SURVIVES IT
Follows from C3 (one reaction = one bit) and C4 (catalysis melts).

**THE COST OF A METABOLISM.** A pool of n = 8 species with every pairwise interconversion
chemically possible but kinetically frozen; each enzyme activates one. Measured R = n - rank(S):
**8, 7, 6, 5, 4, 3, 2, 1, then flat at 1 forever.** The first n-1 = 7 independent enzymes cost
**exactly one bit each**; after that the pool fully interconverts and only TOTAL MASS survives.
> **A complete metabolism over a pool destroys all of that pool's record but one bit.**

**SO HOW DOES A GENOME SURVIVE A METABOLISM?** Not by being chemically different -- same atoms,
and its interconversions are thermodynamically allowed. By Theorem 9 a record dies iff a generator
that moves its certificate is ACTIVE. **The genome survives precisely because no enzyme catalyses
the moves that would scramble it: its sequence sits BELOW the metabolic threshold in R(T).**

**QUANTIFIED, with verified figures** (Wolfenden; searched, not remembered):
| | bits of rate |
|---|---|
| uncatalysed phosphodiester half-life 30 My vs a ~1 s metabolic step | **49.8** |
| nuclease acceleration of phosphodiester cleavage, 10^17 | **56.5** |
| **surplus** | **+6.7** |
> **A nuclease is MORE THAN SUFFICIENT to melt the record it acts on**, by ~7 bits. By Theorem 9
> that is not a matter of degree. **Sequence-specificity and spatial control of nucleases are not
> refinements -- they are what stops the record melting.**
Falsifiable consequences: a promiscuous backbone-scrambling catalyst should be lethal by MELTING
rather than by poisoning, and have no viable variants; and organisms with a warmer move set need
proportionately higher barriers, not merely more repair.

**TWO OF MY OWN ERRORS IN THIS SECTION, both the same kind.**
1. I sized the margin at 10^13 metabolic steps from a REMEMBERED 130 kJ/mol barrier. The measured
   half-life gives 10^15 and 49.8 bits. Order right, number low by ~2 decades. **Verified figures
   used above; the remembered one is discarded.**
2. **My print statement asserted the genome's margin over a generation was "ten to twelve orders"
   while its own output showed 3.7 and 6.1.** A hardcoded verdict contradicting its own numbers --
   the SECOND time today (the first was the Q_R sign an hour earlier).
   **STANDING FIX: compute the verdict; never write it into the print.**

## 41. TEST 30 — CAN R SEE AUTOCATALYSIS? (predictions `6305a71d`)
**C5 as originally registered is WITHDRAWN on inspection**: "autocatalysis needs >= 2 reactions"
is false — X + A -> 2X is autocatalytic with one. Replaced by the question the framework asks.

- **A1 HIT, exact and trivial. R IS BLIND TO AUTOCATALYSIS.** A -> X and X + A -> 2X have the
  IDENTICAL stoichiometric matrix ([-1],[+1]), hence the same rank and the same R = 1.
  **Autocatalysis is a RATE property, and R is built from rank(S).**
- **A2/A3 HIT on the second attempt. R(T) CAN see it**, because an autocatalytic rate is
  state-dependent: rate = k*x, so the generator crosses the threshold only at
  **x_c = 1/(kT)** -- **an autocatalytic reaction is a generator that switches ITSELF on.**
  At k=1e-4, T=1e6 (x_c=0.01) the linear generator is active at every x while the autocatalytic one
  flips between x = 0.005 and 0.01. The linear system has no such threshold.
- **A4 NOT TESTED, NOT ASSERTED, OPEN.** Whether self-activation actually destroys the record needs
  R(T) computed on the joint space either side of x_c. I did not do it.

**THE FIRST RUN FAILED ON MY OWN PARAMETERS.** k=1e-4 with T=1e3 gives x_c = 10, outside the
physical range x <= 1 -- **a search that could not succeed**, the sixth today.

**AND THE THIRD HARDCODED VERDICT.** The failed run printed "R(T) sees a threshold the
stoichiometric R cannot" immediately after its own computed **MISS**, plus a whole A4 paragraph
asserting a conclusion A3 had just failed to establish. **I wrote a memory file about exactly this
habit forty minutes earlier and then repeated it in the next script.** The rerun computes every
verdict from the run's own values and prints no underived prose.

---
## 38. KEEPER'S AUDIT OF THE THREE PAPERS, AND THE FIXES (Sunday 2026-09-06, 08:06-08:17)

Keeper read all three papers and spot-checked the load-bearing arithmetic by computation: carbon
orbit and bracelet counts, strain table, 10.4 K per bit, endotherm bits, interference limit log2 e,
meiotic retention table, seam loss 49.6%, genome protection 49.8 and 56.5 bits, ceiling slope 3.7
and R^2 0.9966. Every number held. Theorem 1 (meiotic) and Theorem 9 (retention) confirmed as
theorems. Novelty ledger not challenged. Two MODERATE, one MINOR set, one PROCESS item. All fixed.

**MODERATE 1 (complexity paper, Section 11).** Bootstrap 2000/2000, digestion-first 100%/0 of
2000, and the logarithmic ceiling were listed under "measured, and we stand behind". All three are
theorems of the model's own construction (g > m + B/T fails at zero capital for every B > 0; a
saving function returns zero at zero throughput; geometric cost against linear surplus is
logarithmic by inspection). Moved to "the algebra of a model we chose", with a sentence at each
source section (2, 3, 7) saying the sweep is a code check. The ceiling's constant, 7.5% band and
sawtooth stay under "measured".

**MODERATE 2 (meiotic paper).** T + N = 1 is definitional (N is defined as H_2(r)). Removed from
the novelty list item 2, from the abstract's three consequences (now two), and from Section 9's
"structural and new"; Corollary 2 relabelled definitional and its six-decimal numerical "check"
deleted.

**MINOR seams.** (a) Retention paper cited "Section 7's Theorem 8" and no Theorem 8 existed
(numbering skipped 7 to 9). Inserted Theorem 8 (codimension: free transitive abelian action gives
R = log2|V/Lambda| exactly; F_2^n form n - rank; stoichiometric form n_species - rank), with a
two-line proof, before Theorem 9. (b) Meiotic Section 9 cited "the open problem at the end of
Section 6a"; none is stated there. Replaced with the actual open item: the min-H(d)-subject-to-
spanning optimisation is stated not solved, and hotspot turnover is priced not derived. (c) Human
1.62 (table, exact Arrhenius between T_ambient and T_body) vs 1.64 (prose, linearised dT/10.4).
Prose set to 1.62 and "factor 1.7" to 1.6; the table now says which formula it uses. (d) The
standard map's "measure of the non-mixing set" had no definition AND no retained instrument:
neither 5687 (grid adjacency) nor 5688 (transport bands) computes it or runs at K = 3.0. See below.

**(d) is the real finding of the audit.** Toy 5691, definition frozen and hashed (cc492359) before
the run: non-mixing at horizon T iff max_{t<=T}|Y_t - Y_0| < 2pi with y unwrapped, 256 x 256
initial conditions. P1 (K=0 control) HIT. P2 (m >= 0.999 for all K <= K_c at every T) HIT, exactly
1.0000. P3 (monotone in K and in T above K_c) HIT. **P4 (no single K-step carries more than half
the drop from 1.0 to 3.0) MISS at T = 300, 1000, 3000; HIT only at T = 10000.** P5: yesterday's
four values (0.980/0.653/0.389/0.172) are reproduced at NO horizon (max |diff| 0.13 at best).
They were a different, unrecorded definition. Withdrawn from the paper; the fresh table is in.
Consequence for the paper's claim: "continuum melting is smooth" is downgraded to "graded and
horizon-dependent; every intermediate value populated; at finite horizon the drop concentrates
just above K_c". The third category survives in the weaker form. The physics that appeared:
m(1.2, T) runs 0.9996 -> 0.63 across T = 300 -> 10000 because transport through broken tori is
slow, while m(3.0, T) is horizon-independent at 0.12 (island measure). The horizon dependence IS
the R(T) statement of Section 8b, seen in the one instance where it can be varied continuously.

**PROCESS.** Eighteen play/ scripts renamed to toy_5673..5690 (ledger play/.lyra_toy_claim_ledger_
2026-09-06.md; hashed prediction files name no scripts and were not touched). Toy 5691 new.
Counter 5673 -> 5692. Nothing committed: BST git is Casey's.

**Lesson, one line:** a number without a retained instrument is a memory, not a measurement.
Memory file written. All three PDFs rebuilt.

---
## 39. CAL'S COLD READ (§851, 08:53) AND THE FIXES (09:00-09:18). ALL THREE PASS TO v0.2.

Cal wrote thirteen pre-questions blind, did not open this record, recomputed the first-read
numbers (all match but one truncation). Three catches that mattered, none pre-registered by him:

**B-R1, a FALSE CLAUSE IN THEOREM 9.** "A move with v_m = 0 cannot merge any classes: it is free."
A zero-shift move cannot lower the FIBRE term (it enters no Lambda) but can merge classes within a
fibre and reduce the defect. The paper's own 24 face flips (shift (0,0)) take the 4x6 torus from
log2|S| to 2.2572. Fixed: clause now "cannot lower the fibre term; may reduce the defect"; proof
amended; Section 7's "546 are free by Theorem 9" now "free relative to the certificate bound --
they merge classes within fibres, which is why 0.69 and not 2.26 survive"; Appendix B's "numbered
theorems stood unchanged" corrected. **I called this theorem unchanged for two days and it was not.**

**A-R1, FISHER'S JUNCTIONS.** "Junction" is Fisher's noun (1949, 1954); all of Section 5 (e^{-nd},
ln2/d, C + nM) is junction theory (Stam 1980; Chapman-Thompson 2003; Haldane 1919 for the map).
And Theorem 1's channel identity (additive noise on a finite abelian group, capacity log|G| -
H(noise)) is Cover-Thomas. What is new is the IDENTIFICATION of meiosis with that channel. Section 1
and Section 5 now say exactly that; Section 9's "new" list loses Section 5.

**C-R4, CATALYSIS: MY RETRACTION WAS THE ERROR.** Pre-registered C4 (09-05) said a catalyst adds no
generator and destroys no record. The "R 3 -> 2" that overturned it compared Michaelis-Menten
against E and ES present-but-inert (two trivial laws). Against S -> P alone (R = 1), MM has R = 2:
catalysis ADDS the enzyme's law, removes none. **Toy 5692** (hashed 04a652ef before the run):
Q1-Q6 all HIT, including catalysing one combustion step (R +1) and the 6,5,4,3,2,2 and 8..1,1
series. No CRN script had been retained on 09-05 either -- second instance today of the
retained-instrument lesson. Paper 3 10b restated: catalysis is entirely an R(T) phenomenon; the
enzyme-specificity sentence drawn from the rank drop is withdrawn; the genome rate margins stand.

**Moderate, all fixed.** A-R2 hotspot turnover "required" was derived at zero background and 6a's
own 40%-outside-hotspots figure says background is positive -> "turnover OR background; the ledger
prices the rate"; m ln m labelled as the coupon-collector leading term. A-R3 Theorem 1 now says
uniform input is capacity-achieving (additive noise) and states d independent of D(p). A-R4 8a's
H_thermo = 1.0000 labelled a theorem of the construction. **A-R5 was better than a truncation:**
the printed 125/13/3/2/1 were integer CEILINGS of the continuous half-life (toy 5677's loop), and
the "drifting" ratio 0.36..0.74 was the rounding; the continuous ratio is a CONSTANT 0.3586 =
ln(1-2p*)/ln(1/2) with H_2(p*) = 1/2, p* = 0.1100 -- factor 2.79 at every r. Table reprinted.
A-R6 cited (Fisher 1930, Muller 1932, Hill-Robertson 1966, Felsenstein 1974; Pardo-Manuel de
Villena-Sapienza 2001). B-R2 Theorem 8 restricted to finite V; Remark routes Z^n to the codimension
(9a's dimension coefficient), cites Schuster-Hofer 1991 and Feinberg. B-R3 Theorem 6 -> Remark 6
(Cheeger is an edge inequality; Bobkov-Houdre-Tetali for vertices; not carried out). B-R4
"converging" -> "approaching". B-R5 formal remark on homogeneous domains DELETED from the paper
(lives here, Section 37). B-R6 "inside" labelled a target; R/H > 0.6 on the abelian substrate is
f < 0.4 + 1/g, the grid's floor; only the dimer row is independent. C-R1 Section 1a "What is not
ours" added (Lotka 1922, Odum-Pinkerton 1955, Morowitz 1968, Schneider-Kay 1994, Schneider-Sagan
2005, Hopfield 1974, CRNT). C-R2 Section 11 rows split: 14 measured / 0 algebra; fouling sign
change -> algebra; spatial deaths -> algebra; endotherm table -> "computed on published inputs with
a chosen ambient"; 13.87 measured / 0.00 theorem. C-R3 the coupled-generator reading of the human
residual STRUCK: 1.62 at 20 C ambient, 1.13 at 25 C, 2.14 at 15 C -- a free input. C-R5 "the
one-generator floor, in chemistry" struck (orbit counting). C-R6 abstract carries the algebra label.

**Bibliographies added to all three**, from memory, each headed with the rule that no entry counts
until pinned to its primary. PDFs rebuilt. Counter 5692 -> 5693.

**Two lessons for the memory file, both mine.** (1) The theorem clause I bolded as the load-bearing
one was the false one; bolding is where I should have looked hardest. (2) Twice in one day a number
in a paper had no retained script (standard map, CRN); the rule is now standing.
