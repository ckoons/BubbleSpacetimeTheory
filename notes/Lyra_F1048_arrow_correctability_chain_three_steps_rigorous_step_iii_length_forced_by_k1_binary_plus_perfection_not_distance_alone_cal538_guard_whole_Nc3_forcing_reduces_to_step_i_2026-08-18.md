# F1048 — The arrow → N_c=3 chain, made rigorous in three steps, with Cal's §538 guard on the length. (i) arrow → correctability [HARD, overturns the banked d=2 finding — Elie's decidable check]; (ii) correctability → distance ≥ 3 [solid coding]; (iii) k=1 (one binary commitment) + d=3 + perfection → LENGTH = 3 uniquely = the [3,1,3] repetition, so N_c = 3 [clean; the length is forced by k=1, NOT by distance alone — the [7,4,3] Hamming code has distance 3 and length 7 but needs k=4, which a single commitment does not have]. ⟹ the whole forcing of N_c=3 (hence n_C=5, hence all five integers) reduces to ONE question: does the arrow forbid erase-and-redo?

**Lyra, Tuesday 2026-08-18, Round 21. The arrow-correctability chain, rigorous, per Cal's guard on step (iii). Reconnected: F1047 (the chain + the banked d=2 obstruction), Forcing+Evidence (rank=2 = one binary bit = k=1), Cal §538 (distance ≠ length). Coding facts verified below. Guard: never "commitment forces D_IV⁵" until step (i) is nailed. LA on D_IV⁵. Nothing pushed; CP existence-only.**

## The chain, three steps
**Step (i) — arrow → correctability. [The load-bearing HARD step; overturns a banked negative.]**
Irreversibility of commitment (the arrow) forbids erase-and-redo: a detected error handled by *discard → re-commit* requires un-committing, which the arrow forbids. So a damaged commitment must be **fixed in place** = *correction*, not *detection-and-erasure*. **This reverses the corpus's banked d=2 erasure finding (Forcing+Evidence line 47), so the bar is high** — it must be established that irreversibility genuinely forbids the re-commit. **Elie's decidable check:** does recovering a single-error committed record *require* a re-commit, or not? Not yet established; this is where the whole chain lives or dies.

**Step (ii) — correctability → distance ≥ 3. [Solid, target-innocent.]**
Correcting one error requires minimum distance **d_min ≥ 3** (standard: d=2 detects one error but corrects none; d=3 corrects one). No dependence on the answer; pure coding.

**Step (iii) — the LENGTH is forced to 3 by k=1 + perfection, not by distance alone. [Clean; Cal's §538 guard resolved.]**
The color number N_c is a *code length* (number of channels), not the distance. **Distance-3 alone does NOT fix the length** — the Hamming **[7,4,3]** code has distance 3 and length **7**. So one must force the length, and here is how:
- **The commitment carries k = 1 data bit** — it is *one binary distinction* (rank = 2, Shannon-forced). This is the decisive constraint: k = 1, not 4.
- **Perfection (no wasted channel):** the protection saturates the Hamming bound $2^k(1+n) = 2^n$ — every possible corruption is within distance 1 of exactly one codeword (uniquely correctable, no dead states). This is the "nature doesn't waste" requirement.
- **The unique perfect code with k = 1, d = 3 is the [3,1,3] repetition, LENGTH 3** (verified: $2^1(1+3) = 8 = 2^3$). The other perfect d=3 code is [7,4,3] Hamming — but it needs **k = 4** (four data bits), which a single commitment does not have. So the k=4 route is not "unmotivated," it is *unavailable*: the commitment is one bit.

⟹ **N_c = code length = 3**, forced by (k=1 binary commitment) + (d=3 correctability) + (perfection). And n_C = N_c + 2 = 5 (the +2 = rank = the two frame boundaries, a separate forced piece). **Do NOT extend the coding argument to g = 7** (§538: that was the unmotivated step) — g = n_C + 2 is a different relation, not the code length.

## Cal's new discipline, applied (the C₂ / same-name trap)
Before solving for the length n, I checked the "constants" in the argument are not themselves n-dependent (the C₂=6-vs-2n−4 trap that killed Condition 5): **k = 1 (fixed — the binary commitment) and d = 3 (fixed — correctability) are genuine constants, not functions of the code length n.** The length n is the sole unknown, solved to 3. No hidden n-dependence. (Contrast Condition 5, where "C₂" was secretly 2n−4.)

## Where the chain stands — the whole thing reduces to step (i)
| step | claim | tier |
|---|---|---|
| (ii) | correctability ⟹ d ≥ 3 | **solid** (standard coding) |
| (iii) | k=1 + d=3 + perfection ⟹ length 3 = N_c | **clean** (verified; the [7,4,3] is ruled out by k=1, not hand-waved) |
| (i) | arrow ⟹ correctability (not erasure) | **HARD, open — overturns the banked d=2 finding** |

**⟹ Steps (ii) and (iii) are in hand. The entire forcing of N_c = 3 — and therefore of n_C = 5 and all five integers (rank 2 forced + N_c 3 ⟹ C₂=2N_c=6, g=n_C+2=7, N_max=N_c³n_C+rank=137) — rests on the single question of step (i): does the arrow forbid erase-and-redo?** If yes, N_c=3 is forced and the dimensionless input count drops from one (N_c=3) to zero — the only input left is the dimensionful scale (m_e). If no, N_c=3 is a datum and n_C=5 is one dimensionless input, GR-level honest.

## Honest tier / guard
- **In hand:** (ii) + (iii) — correctability forces the [3,1,3] repetition, length 3, uniquely (given k=1). The length is forced, not just the distance.
- **The one open, and it is hard:** (i) — the arrow forbidding erase-and-redo. It **overturns a banked negative** (the d=2 erasure finding), so it must clear that bar; it is not "easy owed," it is "contested by our own result." Elie's decidable check decides it.
- **Guard held:** until step (i) is nailed, N_c=3 is a datum and n_C=5 is one input. **Never "commitment forces D_IV⁵."** The promote is real, singular, and has to earn overturning the d=2 finding.

## Handoffs
- **@Elie** — steps (ii)+(iii) are done and clean (the length is forced by k=1+perfection to the [3,1,3], length 3 — the [7,4,3] is unavailable at k=1). Your decidable check IS step (i), and it is now the *only* thing between "n_C=5 is an input" and "n_C=5 is fully intrinsic": does recovering a single-error committed record require a re-commit (⟹ arrow-violation ⟹ correction ⟹ N_c=3), or is erasure arrow-consistent (⟹ d=2 stands ⟹ N_c=3 a datum)? A counting/logic question. Nail it before any claim.
- **@Keeper** — the chain is (ii)+(iii)-in-hand, (i)-open-and-hard. The honest Block C close is the boundary (n_C=5 = one input) until step (i) overturns the d=2 finding. I forced the *length* (not just the distance) — the §538 gap is closed: k=1 rules out the [7,4,3], perfection picks [3,1,3] uniquely.
- **@Cal** — §538 guard honored: the length is forced by k=1 (the binary commitment) + perfection, not by distance-3 alone; the length-7 route is *unavailable* (needs k=4), not merely unmotivated. And I applied your new same-name discipline: k=1 and d=3 are genuine constants, not n-dependent (unlike the C₂ that killed Condition 5).
- **@Casey** — the three-color argument, tightened. To *fix* one error in a one-bit commitment you need copies, and there are two clean facts: fixing (not just flagging) needs the copies to disagree-breakably, which is three, not two; and among all the ways to lay out three-distance protection, a *one-bit* message with no wasted room is uniquely the three-fold repetition — length exactly three. (The famous seven-length code also fixes one error, but it protects *four* bits at once, and a single commitment is one bit, so that door is closed.) So *if* a commitment must be fixable, three colors follow with no slack. The whole thing now hangs on one honest question, which is Elie's: does the irreversibility of a commitment actually forbid the throw-away-and-redo? If it does, three colors, five dimensions, and all five integers are intrinsic, and the only thing we ever take from outside is the ruler. If it doesn't, five is one honest input. I won't call it until that one question is nailed, because it overturns something we ourselves banked.

Notes only; no theorem/toy claimed (the chain made rigorous). F1048: arrow→N_c=3 in three steps. (i) arrow→correctability [HARD, overturns banked d=2 erasure, Elie's check]; (ii) correctability→d≥3 [solid]; (iii) LENGTH forced by k=1 (one binary commitment) + d=3 + perfection → unique [3,1,3] repetition, length 3 = N_c [clean; [7,4,3] Hamming has d=3,length 7 but needs k=4, unavailable at k=1 — Cal §538 gap closed: force length not distance]. n_C=N_c+2=5; don't extend to g=7. Applied Cal's same-name discipline (k=1,d=3 are constants not n-dependent, unlike C₂=2n−4). Whole N_c=3 forcing reduces to step (i). In hand: (ii)+(iii). Open+hard: (i). Guard: never "commitment forces D_IV⁵" until (i) nailed. — Lyra
