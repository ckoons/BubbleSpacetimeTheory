# K1890-PRE — the control on my own table, the scope clause it forces, and two more Proved rows of the same shape

**Keeper, 2026-09-09 (Wednesday) 12:34 EDT, clock-verified.** Instrument retained: `notes/Keeper_K1890-PRE_instrument_exceptional_isomorphism_control_on_the_multiplicity_table_2026-09-09.py`.

## 1. Positive control on the multiplicity table, and it caught my own error
The known exceptional isomorphisms among low-dimensional Hermitian symmetric domains must give matching (rank, a, b, dim) on both sides. Result:

| isomorphism | verdict |
|---|---|
| IV_3 ≅ III_2 | MATCH (r=2, a=1, b=0, d=3) |
| IV_4 ≅ I_{2,2} | MATCH (r=2, a=2, b=0, d=4) |
| IV_6 ≅ II_4 | MATCH (r=2, a=4, b=0, d=6) |
| IV_1 ≅ disc ≅ I_{1,1} | **MISMATCH** |

**Three of four match, and the mismatch is mine.** The type IV parametrisation (rank 2, a = n − 2) holds for **n ≥ 3 only**: at n = 1 the domain is the disc with rank 1, and my formula returns a = −1, which is not a multiplicity. At n = 2 it is the reducible product of two discs and a = 0, which is consistent in that a = 0 flags reducibility. **My K1889 table carried no range clause and needed one.** The a = 3 result is unaffected, since it requires n = 5, well inside the valid range, and the three in-range isomorphisms independently validate the table. The control did its job on its author.

**One further fact that strengthens the selection: D_IV⁵ is not in the coincidence list at all.** It is not secretly a member of another family, which is exactly the objection a referee would raise against selecting by an invariant.

## 2. The scope clause the theorem now owes
My enumeration was over irreducible domains. **A reducible domain is a product, and a product of copies of D_IV⁵ has a = 3 in every factor.** So the theorem's statement must read *irreducible*, or it must carry a factor-count criterion. This is not a defect, it is a clause, and it belongs in Lyra's L1 statement rather than being discovered later by someone else. Elie's E1 falsifier should return it too, which will be a nice two-instrument agreement.

## 3. The plurality sweep, and it reaches two more Proved rows
Registry line 7712, in the original row's own words: *"Three independent criteria all selecting D_IV⁵ has null-model probability very low **if criteria are independent**."* The row stated its own condition, and Elie evaluated it: at dimension five the first two criteria already leave a singleton. **The null-model argument is void by the row's own conditional, which means this is evaluating a stated hypothesis rather than overturning a claim.** Line 7708 lists the three as rank, Bergman exponent and Mersenne primality; with the second empty and the third empty as written, it reduces to rank alone, which leaves twenty-six families.

**Two further rows share the shape and are tiered PROVED:**
- **T1779, Hodge Ring Uniqueness:** *"The five BST integers are the UNIQUE solution to five independent Hodge-theoretic constraints."*
- **T1788, YM Ring Uniqueness:** *"The five BST integers are the UNIQUE solution to five independent Yang-Mills constraints."*

Five unknowns and five constraints have a unique solution generically, whatever the constraints say. **At least two of the five integers are definitions in this corpus** — g is defined as n_C + rank, and C₂ stands in a fixed relation to g — so a system that treats all five as unknowns is partly solving for its own definitions. **I am flagging the shape for testing and asserting nothing about the content of either row.** Each needs the same treatment C3 got: name side A per constraint, show it is free of BST integers, and count how many unknowns remain genuinely free.

## 4. What I am adding to Round 140
An item for Cal and Grace: **T1779 and T1788 go on the independence-test list**, tiered PROVED, and nothing about them is ruled until their constraints are read one at a time. And a line for the round's refusal list: **no null-model probability may be quoted for a set of criteria until the criteria have been shown to be evaluated on a set that is not already reduced.** The original row asked for exactly that and nobody supplied it for three and a half months.

— Keeper
