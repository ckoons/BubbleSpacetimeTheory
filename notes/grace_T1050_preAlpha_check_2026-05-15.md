---
title: "Grace — T1050 Pre-α Derivation Check (A2 candidate route)"
author: "Grace (Claude 4.7)"
date: "2026-05-15"
status: "Findings 21:50 EDT"
out_of: "Casey via Keeper directive: T1050 pre-α check open to anyone"
---

# T1050 Pre-α Derivation Check

## Question

T1050 (Sibling Formula, April 11 2026) is one of the three /route candidates surfaced for A2 (+rank in N_max). The grading task per Keeper: verify that the T1050 derivation chain doesn't use α (fine-structure constant) anywhere upstream. If α leaks in, T1050 is dead as an A2 candidate. If pre-α clean, it's a real candidate.

## T1050 statement (Lyra synthesis with Grace + Elie + Keeper)

f(a) = a · N_c^{N_c} + rank = 27a + 2

evaluated at {N_c, n_C, g} = {3, 5, 7} gives {83, 137, 191} — three primes that are the three fundamental BST limits (material/physics/knowledge).

In particular: **f(n_C) = 5·27 + 2 = 137 = N_max**.

## α appearance check

`grep -i 'alpha\|fine.struct\|α'` on `notes/BST_T1050_Sibling_Formula.md`:

Only one α-related line, in the "Physical identifications" section:

> "**137 = Physics limit.** The fine structure constant α⁻¹ ≈ 137.036 and the spectral cap N_max = 137 (T186, T836). The compact dimension n_C = 5 determines the spectral window through N_max = n_C × N_c^{N_c} + rank (T836). This is the strongest identification: f(n_C) = N_max IS the T836 formula."

**Reading**: α appears as a *post-hoc identification* of what 137 means physically, not as input to deriving the value 137. The derivation chain is:
1. Construct f(a) = a · N_c^{N_c} + rank using BST integers only
2. Evaluate at a = n_C = 5: f(5) = 137
3. Identify 137 with N_max (T836 formula) and with observed α⁻¹

Step 3's α use is interpretive. Steps 1-2 are pre-α arithmetic on BST integers.

**Verdict on α purity**: T1050 is **pre-α clean** in its derivation. α appears only as label, not as upstream input.

## Pre-α check on parent T914 (Prime Residue Principle, April 9)

T914 is T1050's load-bearing dependency: T1050 cites T914 as the source of the "+1 observer shift, applied twice = +rank" mechanism.

`grep -i 'alpha\|fine.struct\|α'` on `notes/BST_T914_Prime_Residue_Principle.md`:

α appears once, in a table column labeled "**Physics example**" for the prime 137:

> "137 | N_max — maximum representation dimension of D_IV^5 | α = 1/137; 3D Ising η ≈ n_C/N_max = 5/137"

Same pattern: α is a *physics example* attached to the prime 137 (the BST-product-adjacent prime), not input to deriving why 137 is BST-special.

**Verdict on T914 α purity**: T914 is **pre-α clean** in its derivation. α used only as physical-example labeling.

## Deeper concern: does T1050 *force* +rank, or just *contain* it?

T1050's mechanism for the additive +rank in f(a) = a·N_c^{N_c} + rank is asserted as:

> "The additive constant +rank = +2 in the formula is the observer shift — the same +1 from T914 (Prime Residue Principle) applied twice (once for each rank direction). Every sibling carries the observer."

**The "+1 per rank direction" claim**: T914 has a single +1 observer shift (prime adjacent to BST product). T1050 says this is "applied twice (once for each rank direction)" to get +2 = rank.

This is *asserted*, not *derived* in T1050. Whether the +1 shift attaches to "rank directions" specifically (rather than, say, BST integer pairs, or Cartan generators of K, or something else) is not proved within T1050's argument.

**Cartan rank check**: D_IV^5 has rank = 2 as the *real rank* of the symmetric pair SO_0(5,2)/[SO(5)×SO(2)]. The compact subgroup K = SO(5)×SO(2) has Cartan rank 2 + 1 = 3. So "rank=2" in T1050 refers to the real rank of the symmetric space, equivalently the number of noncompact Cartan directions in the corresponding Lie algebra decomposition.

If the +1 observer shift attaches to noncompact Cartan directions specifically, then "two rank directions → two +1 shifts → +rank = +2" makes sense. But T1050 doesn't prove that attachment — it asserts it.

## Verdict for SP-25 grading

T1050 as A2 candidate:

| Criterion | Status |
|-----------|--------|
| Pre-α clean | ✓ Yes (α only as post-hoc label, not input) |
| Contains +rank | ✓ Yes (additive constant in f(a) is rank=2) |
| Forces +rank via operator identity | **Partial** — relies on asserted "+1 per rank direction" not derived from operator theory |
| Suitable for Cal's bar | **Probably no** — Cal wants operator-level forcing, T1050 has structural-asserted forcing |

**Recommendation**: T1050 stays a CANDIDATE but is unlikely to be the route Cal grades up to D-tier. It's a corroborating structural argument (BST integers map cleanly through f(a) to physical limits including N_max = 137 with +rank as observer constant), but the +rank in T1050 is **named** rather than **derived from independent operator theory**.

T1913 Furuta-Wallach is the stronger candidate for Cal's operator-identity bar (now that Elie's T1.3-P1 and Lyra's T1.3-P2 are closed).

## SP-25 ✓

T1050 pre-α check filed. Status: **CANDIDATE survives α-purity test but +rank derivation is asserted-not-proved**. Move forward with Furuta-Wallach as primary A2 closure candidate; T1050 stays in the candidate set as corroborating evidence (overdetermination), not as operator-identity-grade derivation.

— Grace, May 15, 2026, 21:50 EDT
