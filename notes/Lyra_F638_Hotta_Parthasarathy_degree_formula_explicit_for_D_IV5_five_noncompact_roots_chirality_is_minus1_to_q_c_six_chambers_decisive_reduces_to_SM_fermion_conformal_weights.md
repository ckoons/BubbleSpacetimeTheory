# F638 — The weight→degree→chirality map, computed EXPLICITLY for D_IV⁵ (pull 07-22h). The Hotta-Parthasarathy/Schmid theorem gives a finite formula, and SO(5,2)'s roots are small enough to write down completely: **5 positive noncompact roots, pairings ⟨λ+ρ,β⟩ = c + {1/2, 3/2, 5/2, 7/2, 9/2} where c = the fermion's SO(2)-charge (conformal weight). The L² cohomology concentrates in degree q(c) = #{those < 0}; chirality = (−1)^{q(c)}. Six chambers as c crosses −1/2, −3/2, −5/2, −7/2, −9/2; chirality ALTERNATES.** So chirality is a computed step-function of the conformal weight. **The decisive test reduces to exactly one input: the SM fermions' c-values.** L-doublet/R-singlet ⟺ the doublet's c lands in an even-q chamber and the singlet's in an odd-q chamber. The mechanism (weight→degree→chirality) is now a THEOREM with an explicit formula; the SIGN for the SM needs the c-values — that's the remaining input, and it's the SAME K-type addressing as the flavor/mass work.

**Lyra, Wed 2026-07-22 ~11:24. Pull 07-22h. The degree formula is rigorous; the SM c-values are the open input. Compute-don't-assert: I computed the map, not the SM answer.**

## The theorem (Schmid / Hotta-Parthasarathy)
For a homogeneous vector bundle E_λ over a Hermitian symmetric domain G/K, the L² Dolbeault cohomology H^q_{(2)}(G/K, E_λ) is **nonzero in at most ONE degree** q(λ), and there realizes a discrete series representation. **This is why the spectrum is chiral by a theorem, not a lucky nonzero index** (Grace/Keeper's "mechanism-as-theorem"): the cohomology can't spread across degrees — it concentrates. The concentration degree:
$$ q(\lambda) = \#\{\beta \in \Delta_n^+ : \langle \lambda+\rho,\ \beta\rangle < 0\}, $$
the count of positive noncompact roots on which λ+ρ is negative. Chirality = the Λ^{0,q} grading parity = **(−1)^{q(λ)}.**

## D_IV⁵ roots — written down completely (SO(5,2) = B_3, rank 3)
Cartan coordinates (e_1, e_2, e_3); e_1 = the **SO(2) direction** (all noncompact roots carry it), (e_2,e_3) = the **SO(5)=B_2** internal directions.
- **Positive roots of B_3 (9):** e_1,e_2,e_3; e_i−e_j; e_i+e_j (i<j).
- **ρ = (5/2, 3/2, 1/2)** (verified: e_1-coeff sum 5, e_2 sum 3, e_3 sum 1, halved). *This is BST's ρ-vector (K264).*
- **Compact positive roots (SO(5)=B_2, no e_1):** e_2, e_3, e_2−e_3, e_2+e_3. (4)
- **★ Positive NONCOMPACT roots (all carry +e_1) — exactly 5 = n_C:**
$$ \Delta_n^+ = \{\, e_1+e_2,\ \ e_1-e_2,\ \ e_1+e_3,\ \ e_1-e_3,\ \ e_1 \,\}. $$
ρ_n = ½Σβ = (5/2, 0, 0). **The count 5 = n_C, and it is odd — n_C odd — the same oddness that makes the SO(5) spinor irreducible now counts the chambers.**

## The explicit degree formula for a fermion
Fermion K-type = SO(5) spinor (highest weight (1/2,1/2) in (e_2,e_3), dim 4) with SO(2)-charge c: **λ = (c, 1/2, 1/2).** Then λ+ρ = (c+5/2, 2, 1), and the five noncompact pairings are:
| β | ⟨λ+ρ, β⟩ |
|---|---|
| e_1−e_2 | c + 1/2 |
| e_1−e_3 | c + 3/2 |
| e_1 | c + 5/2 |
| e_1+e_3 | c + 7/2 |
| e_1+e_2 | c + 9/2 |

**q(c) = #{these < 0}**, a step function with 6 chambers:

| chamber (c) | q | chirality (−1)^q |
|---|---|---|
| c > −1/2 | 0 | **+** (holomorphic sections = Bergman/Hardy) |
| −3/2 < c < −1/2 | 1 | − |
| −5/2 < c < −3/2 | 2 | + |
| −7/2 < c < −5/2 | 3 | − |
| −9/2 < c < −7/2 | 4 | + |
| c < −9/2 | 5 | − |

**Chirality alternates each time c drops through a noncompact-root threshold.** The chirality of a fermion is literally the parity of how many of the 5 thresholds it sits below.

## Consistency with Elie 4777 (net ±4)
For c > −1/2 (q=0), all four SO(5)-spinor components are holomorphic sections → **net chirality (−1)^0 · 4 = +4** — chiral, not vector-like, matching Elie's 4777. The flat index-0 is evaded because the physical fermions are the q=0 (holomorphic/Bergman) sector, not the full L↔R-symmetric flat spinor. ✓

## ★ The decisive test, reduced to ONE input
The chirality of each SM fermion = (−1)^{q(c)} with c its SO(2)-charge (conformal weight). So:
> **L-doublet / R-singlet ⟺ the SM left-handed doublet's c lands in an EVEN-q chamber and the right-handed singlet's c lands in an ODD-q chamber (or vice versa) — a genuine chirality split by internal rep.**

The mechanism is a theorem with an explicit formula. **The remaining input is the SM fermions' conformal weights c** — and here is the reconnection: those c-values are the SAME SO(2)-charges / K-type addresses that the flavor-sector work assigns to fermions (masses = radial norms, etc.). So the chirality question and the mass/flavor question depend on the *same* fermion K-type data. This is not a separate unknown — it is the K-type addressing we're already working.

## Honest tier
- **The degree formula (weight → q → chirality): THEOREM, explicit, rigorous** (Schmid/HP + the D_IV⁵ roots written out). This is real, computed, bankable as the mechanism.
- **The SM chirality sorting (does L-doublet/R-singlet fall out?): OPEN**, reduces to the SM fermion c-values landing in opposite-parity chambers. Candidate. **Do NOT bank "parity closed" — the c-values are the open input, and I have NOT derived them here.**
- **Two oddnesses on record (Grace):** n_C=5 odd → the split AND the 5 noncompact-root thresholds; g=7 odd → the orientation (F636). Both exact rep-theory/Clifford facts.

## Tiers / handoffs
- **@Elie** — verify the roots (Δ_n^+ = {e_1±e_2, e_1±e_3, e_1}, ρ=(5/2,3/2,1/2)) and the degree table; confirm the q=0 chamber gives net +4 (matches your 4777). Then the harness question: for a spinor at charge c, the L² index concentrates in degree q(c) — check via the Bergman/FK computation that the c>−1/2 sector is the holomorphic discrete series (formal dimension nonzero, higher degrees zero).
- **@Keeper** — mechanism-as-theorem CONFIRMED with an explicit finite formula: chirality = (−1)^{q(c)}, 6 chambers, thresholds at half-integers spaced by 1 (five of them = n_C). The decisive question is now precisely "the SM fermion c-values" — nothing vaguer. Hold candidate: the formula is a theorem, the SM sorting is open on the c-values (which are the flavor-sector K-type data, not a new unknown). Don't bank parity until the c-values are shown to sort L-doublet/R-singlet.
- **@Grace** — render: chirality = (−1)^{q(c)}, the 6-chamber step function; 5 noncompact roots = n_C (odd); the decisive input = SM fermion conformal weights c (= the flavor K-type addresses). The chirality question reconnects to the flavor/mass K-type work — same fermion data, two faces of Born=Bergman.
- **@Casey** — the "which chirality" is now an explicit formula: a fermion's chirality is (−1) to the power of how many of five thresholds its conformal weight c sits below (thresholds at c = −1/2, −3/2, −5/2, −7/2, −9/2 — five of them because n_C=5). One computation, fully written out. The last open piece is the SM fermions' c-values — and the good news is those are the *same* K-type addresses the flavor/mass work assigns, not a new unknown. So "why is the world left-handed" is now: do the SM doublet and singlet sit in opposite-parity chambers? That's a question about the fermion weights we're already chasing for masses. Computed the map; the SM sorting is the open input.

Notes only; no toys/theorems claimed. Degree formula = theorem (explicit); SM chirality sorting = open, reduces to SM fermion c-values (= flavor K-type data). — Lyra
