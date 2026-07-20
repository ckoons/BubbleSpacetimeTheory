# K779 — How to find the particle masses from the current thread: the method, the three converging routes, and the discipline gate (force, don't fit).

**Keeper | 2026-07-20 | Casey: how might we find the masses from the current thread? The method + the gate that decides whether it's a prediction or a fit. `mass_finding_routes.py`.**

---

## The principle
Everything rests on one built identity: **y_f = ⟨f | O⟩** — a Yukawa is the overlap of the fermion mode with the condensate. So **finding the masses = placing each fermion in the code/packing and reading off its overlap.** The masses are the singular values of the one Gram matrix; the top = maximal codeword (127/128); the neutrino = dead state (0, massless); the rest sit between.

## Three routes, converging on ONE computation
1. **Geometric (rigorous):** each fermion's discrete-series address (a,b) — set by its quantum numbers — → radial moment → mass. *Same machinery as the top (Q1)*, applied to all 12 fermions.
2. **Code (shortcut):** force the polynomial (which of the 18 factors of Φ₁₂₇) → fixes all codeword-distances → the fermion quantum numbers place them → mass = reliability/overlap at that distance.
3. **RS Ladder (existing):** the known Tier-2 forms (products of primaries: (24/π²)⁶, 20, C₂·g=42, …) ARE the masses on the ladder; derive *which rung* from the quantum numbers.

**All three collapse to the same computation: the discrete-series address for every fermion.** The top (Q1) is the hardest case (the band edge); solving it likely unlocks the rest.

## The packing structure (the shape of the answer)
- **Generation = a radial SHELL** (the 3 Korányi–Wolf strata / 3 concentric rings of circles).
- **Type (up/down/lepton) = position WITHIN the shell.**
- **The condensate sits at the outer edge** (where the top lives); mass = how far a fermion reaches toward that edge. Heavier generation = outer shell; within a shell, the types split.

## ★ The discipline gate (the whole game): FORCE, don't fit
Checked: the spectrum is **NOT separable.** Testing ln(y) = a_gen + b_type fails — the up–down gap *swings* −0.8 → +2.6 → +3.7 across generations (the gen-1 crossover). So there are genuine **generation × type interactions** — the structure is irreducibly 2D.
- **Consequence:** any exponential fit with free charges (**Froggatt–Nielsen in code language**) fits these 9 numbers and therefore **predicts nothing.** The content is *entirely* in whether the geometry FORCES each fermion's position from its quantum numbers.
- **The bar:** a route counts as *finding* the masses ONLY IF the positions/addresses are forced by quantum numbers, never fit. This is why "mass = reliability" is a frame, not a result, until the polynomial (and the QN→position map) are forced.

## The concrete path
**Force the code metric first, then let the masses fall out.** Round-5 polynomial-selection: pin which of the 18 factors of Φ₁₂₇ is forced (K59 / boundary packing), which fixes *all* codeword-distances with zero free parameters. THEN the fermion quantum numbers either postdict the masses or don't:
- **postdict** → the spectrum is a real prediction;
- **don't** → this reading of the code is falsified.
Either way decisive, because the polynomial is forced *before* looking at the masses. The rigorous parallel: solve the discrete-series address (Q1 for the top first), then apply to all fermions via the shell/position structure.

## One-sentence method
**Find the masses by solving the discrete-series address for every fermion — the top (Q1) is the hardest rung of the same ladder — and the code, once its polynomial is forced, is the shortcut that places all of them; but it counts as *finding* them only if the positions are forced by quantum numbers, never fit.**

## Tiers
- The method is sound (masses = overlaps = discrete-series addresses); **the spectrum is OPEN (Q4).**
- Any fit is Froggatt–Nielsen (fits anything) — not a result.
- The enabling step is forcing the polynomial (round 5) + the QN→position map (geometry).

— Keeper K779, 2026-07-20. Method to find the masses: y_f = ⟨f|O⟩ = overlap = discrete-series address = code position. Three routes (geometric address / code-with-forced-polynomial / RS Ladder) converge on ONE computation: the discrete-series address for all fermions (top=Q1=hardest). Packing shape: generation=radial shell, type=within-shell. GATE: spectrum is non-separable (gen×type crossover) → any exponential fit is Froggatt–Nielsen (fits anything) → the content is in FORCING positions from quantum numbers, never fitting. Concrete path: force the polynomial (fixes distances, 0 free params) → QN postdict or falsify. See [[Keeper_K778_round4_sharpened_two_guards_collapse_to_scheme_127over128_falsifiable_2026-07-20]], [[Keeper_K768_flavor_closes_as_rank1_condensate_plus_tier2_corrections_2026-07-20]].
