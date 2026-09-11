# K1885-PRE — Round 136 opening finding: "equals one on the Shilov boundary" does not single out the commitment effect

**Keeper, 2026-09-09 (Wednesday) 09:30 EDT, clock-verified. Hashed before the round opens.** Instrument retained: `notes/Keeper_K1885-PRE_instrument_commitment_effect_family_sweep_zsq_z4_z6_all_unity_on_Shilov_2026-09-09.py` (499,394 accepted Lie-ball points by rejection; sampler control = acceptance 0.0623 against the exact 1/16).

## The question this asks
Round 135 closed with Lyra and Cal converging independently on one new identification: **the commitment effect is M_{|z|²} on the Bergman space, a two-outcome POVM, "did the word reach the boundary."** Cal §926 ruled the chain caps there rather than at T2401, since T2401's load-bearing content reduces to T754 plus a kernel naming. So the whole payer reading, and with it yesterday's push-cost closed form, rests on that one choice of effect. **Nobody has asked what else could have been chosen.** Family sweep before a signature is the corpus's own rule and it was not run.

## The finding (arithmetic, this morning)
On Š every point is z = e^{it}x with x real on S⁴, so |z|² = 1 there — **and therefore |z|^{2n} = 1 there for every n.** The condition "the effect is the identity on the Shilov boundary and a strict contraction inside," which is what makes an effect read as *did the word reach the boundary*, is satisfied by an infinite family. Each member gives a different cost table:

| j (at k = 0) | 1 − ⟨|z|²⟩ | 1 − ⟨|z|⁴⟩ | 1 − ⟨|z|⁶⟩ |
|---|---|---|---|
| 0 | 0.4997 | 0.7378 | 0.8569 |
| 1 | 0.4160 | 0.6473 | 0.7804 |
| 2 | 0.3562 | 0.5751 | 0.7130 |
| 3 | 0.3114 | 0.5167 | 0.6546 |

Column one reproduces the exact line 5/(2(j+5)) = 0.5000, 0.4167, 0.3571, 0.3125 to three decimals, so the instrument is sound. The other two columns are not small perturbations. The vacuum's commitment probability is 0.50, 0.26, or 0.14 depending on which member is chosen, and nothing stated so far chooses.

## What survives and what does not
**Survives, and is invariant across the whole family:** the cost falls monotonically in the winding and tends to zero, because every word concentrates on Š as j grows and every member of the family equals one there. That is an ORDER, it is reparametrisation-invariant, and it carries the whole physical reading ("commitments become reliable as the clock advances").
**Does not survive:** the VALUES. 5/(2(j+5)), the 5/(2j) asymptote, the 0.1081 failed-push fraction, Σc = 14.81, the five-cycle sequence. Those belong to |z|² and to nothing more general.

**So yesterday's tier line needs one word.** c(j,k) is not DERIVED. It is DERIVED GIVEN the commitment effect, and the effect is an IDENTIFICATION made yesterday by Lyra and endorsed by Cal. The theorem is the order; the table is the identification's.

## What could still force |z|², for the round to test rather than assume
(i) minimal degree among non-constant K-invariants; (ii) the Jordan trace form of the triple, which is the domain's own norm rather than a chosen function; (iii) the Jones-intensity identification, which is physics and not mathematics; (iv) some compatibility with the Szegő structure that the higher powers break. **My hashed guess: (iii) is what actually does the work, (ii) is the best mathematical candidate and is still a choice of structure, and (i) is a preference. If that holds, the row reads "derived given the dictionary's Jones vector," and the dictionary is where the payer reading rests.**

Not a demotion of yesterday's work. A correct tier on it, and the family sweep the corpus requires before any clean number becomes a signature.

— Keeper
