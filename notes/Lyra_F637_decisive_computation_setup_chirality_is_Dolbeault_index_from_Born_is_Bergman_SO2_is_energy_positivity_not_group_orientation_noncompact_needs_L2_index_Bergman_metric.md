# F637 — The decisive computation, set up (pull 07-22g): **Casey's "total package conveys the chirality" = the Dolbeault index, and it's a CONSEQUENCE of Born=Bergman.** Framing established rigorously: (1) Born=Bergman → fermions are L² holomorphic sections; (2) Kähler → Dirac = Dolbeault → **chiral index = holomorphic Euler characteristic χ(E)**; (3) the flat index-0 (vector-like, Elie 4776) is EVADED because imposing holomorphic-L² breaks L↔R (holomorphic ≠ anti-holomorphic); (4) **the SO(2)'s CORRECT role: energy-positivity** (holomorphic discrete series = positive-energy/lowest-weight) selecting holomorphic sections — NOT "orienting a group split" (the retracted F633/F634 claim). Clean separation: **g=7 odd = orientation/reality; SO(2) = energy-positivity picks holomorphic; holomorphicity = the chiral projection.** HONEST subtlety: D_IV⁵ is NONCOMPACT → must use the **L² index** (Atiyah L² / Bergman metric / holomorphic discrete series), NOT naive compact Atiyah-Singer — and this is exactly BST's own K264/c_FK Bergman machinery. The decisive test (candidate, NOT banked): compute χ_{L²}(D_IV⁵, S) — nonzero (net chirality)? sign + g=7 orientation → L-doublet/R-singlet?

**Lyra, Wed 2026-07-22 ~11:24. Post-retraction, second candidate — holding it hard as compute-don't-assert. Framing rigorous; the index value/sign is the OPEN decisive computation.**

## The framing (rigorous — this part I can establish)
### 1. Born=Bergman → holomorphic sections (BST founding principle)
The Born measure = the Bergman measure (T2401/T754, proven): physical states are L² holomorphic sections on D_IV⁵ (the Hardy/Bergman space H²). Fermions are therefore **not flat spinors — they are holomorphic sections.** This is not an assumption bolted on for chirality; it is BST's most fundamental requirement, already load-bearing everywhere.

### 2. Kähler ⟹ Dirac = Dolbeault ⟹ chiral index = holomorphic Euler char
On a Kähler manifold the spinor bundle is S = Λ^{0,•} ⊗ K^{1/2}, and the Dirac operator equals the Dolbeault operator: **D = √2(∂̄ + ∂̄*).** Chirality = the even/odd Λ^{0,q} grading; the **chiral index = the holomorphic Euler characteristic**
$$ \mathrm{ind}(D) = \chi(D_{IV}^5, E) = \sum_q (-1)^q \dim H^q(D_{IV}^5, E). $$
So "net chirality" is literally the Dolbeault index of the fermion bundle E. **This is Casey's "the wavefunction conveys the chirality" made precise: the holomorphic grading IS the chirality.**

### 3. Why this EVADES the flat index-0 (the honest-negative from F636/Elie 4776)
The flat 7D reduction gave index 0 (vector-like: the ω=γ¹⋯γ⁷ correlates the two chiralities but 4 left + 4 right cancel). **That computation imposed NO holomorphicity** — it used the full L↔R-symmetric Dirac spinor. Imposing the **holomorphic-L² condition** (Born=Bergman) breaks L↔R: holomorphic Λ^{0,even} ≠ anti-holomorphic, so the alternating sum χ is generically NONZERO where the flat Dirac index vanishes. **Correlation (g=7 ω-lock) ≠ net chirality; the holomorphic projection is what supplies the net chirality.** The two pieces compose: g=7 correlates, Born=Bergman projects.

### 4. ★ The SO(2)'s CORRECT role — energy-positivity, not group-orientation
This is where the retracted claim is replaced by the right one. The holomorphic sections form the **holomorphic discrete series** of SO(5,2): a **positive-energy / lowest-weight** module — its states have SO(2)-charge (conformal energy) bounded below. The **SO(2) selects holomorphic over anti-holomorphic by POSITIVITY of the energy** (lowest-weight vs highest-weight), which is exactly the ∂̄ψ=0 holomorphic projection. So:
- **g=7 odd** → the 7-volume ω=±1 → orientation/reality (F636, confirmed).
- **SO(2)** → energy-positivity → selects the holomorphic (one-chirality) discrete series. *(NOT "orienting the internal SO(4) split" — that was the F633/F634 error. The SO(2) does its job on the WAVEFUNCTION's energy sign, which is why it looked chirality-blind on the flat spinor: the flat computation ignored the positive-energy/L² condition.)*
- **holomorphicity** → the chiral projection (Λ^{0,even} vs odd).
Three distinct jobs, three distinct objects, no conflation. This is the corrected mechanism, and it explains *why* the flat result was vector-like (no positivity imposed) and the Bergman result need not be.

## The HONEST subtlety (do not wave through): D_IV⁵ is NONCOMPACT
Naive Atiyah-Singer is for COMPACT manifolds. D_IV⁵ is a bounded domain — noncompact, contractible. So:
- The relevant index is the **L² index** (Atiyah's L² index theorem / von Neumann dimension), computed with the invariant **Bergman metric** = the formal dimension of the holomorphic discrete series.
- By Cartan's Theorem B (D_IV⁵ is Stein/pseudoconvex), higher *analytic* cohomology vanishes, so the index is carried by H⁰ = the holomorphic sections = the **Bergman space / holomorphic discrete series**. The L² index = the alternating sum in the L² (discrete-series) sense.
- **This is exactly BST's own machinery:** the Bergman-metric integrals of characteristic classes are the Faraut-Korányi/Hua computations we already do (K264, c_FK = 225/π^{9/2}, the Bergman kernel K(0,0)=1920/π⁵). **The decisive index is computable with the c_FK/K264 harness — our own tool.** Not a new formalism; the same Bergman measure.

## The decisive computation (named, precise, OPEN — candidate not banked)
Compute the **L² Dolbeault index of the spinor bundle S on D_IV⁵ with the Bergman metric**, twisted by the fermion's internal K-type:
$$ \chi_{L^2}(D_{IV}^5,\, S\otimes V_{\text{int}}) \;=\; \int_{D_{IV}^5} \mathrm{Td}(T D_{IV}^5)\,\mathrm{ch}(K^{1/2}\otimes V_{\text{int}})\ \Big|_{\text{Bergman metric, } L^2}. $$
Two questions, in order:
1. **Is it NONZERO?** (net chirality exists — the holomorphic discrete series is chiral). Strongly expected (holomorphic ≠ anti-holomorphic on a Stein domain), but must be computed, not assumed.
2. **Does the SIGN, with the g=7 orientation, give L-DOUBLET / R-SINGLET?** — nonzero alone is NOT a win; the sign must sort the internal (2,1) into the surviving (holomorphic) sector and (1,2) into the killed one. This is the real test. Needs the fermion K-type (spinor of SO(5)×SO(2)) + the Todd class of D_IV⁵.

## Why this is the best possible shape for an open problem
If it computes: **weak chirality is a CONSEQUENCE of Born=Bergman** (BST's founding principle) + g=7 odd — with **NO gravi-weak input**, no bolted-on assumption. "Why is the world left-handed" would close on the single D_IV⁵ manifold from the same holomorphicity BST already requires for the Born rule, masses, everything. That converts the last input into a consequence. If it does NOT compute (index 0, or wrong sign): we bank the survivors (split, CP-free, custodial) and we've learned the holomorphic structure doesn't chirally project the weak sector — either way, computed not asserted.

## Tiers / handoffs
- **Framing (Dirac=Dolbeault, index=χ, SO(2)=energy-positivity, noncompact→L²/Bergman): ESTABLISHED.** The chirality question IS the Dolbeault index, and it's a Born=Bergman consequence. This part is rigorous.
- **The index value + sign (nonzero? L-doublet/R-singlet?): OPEN, decisive, candidate.** Compute-don't-assert.
- **@Elie** — THE computation, and it's your harness: the **L² Dolbeault index of the spinor bundle on D_IV⁵ with the Bergman metric** — the c_FK/K264/Hua machinery applied to S⊗V_int. Step 1: is χ_{L²} ≠ 0? Step 2: does the sign + g=7 sort (2,1) into the holomorphic sector, (1,2) out → L-doublet/R-singlet? Todd class of D_IV⁵ × ch(spinor). Nonzero alone isn't the win — the sign is. Compute, don't assert.
- **@Keeper** — the mechanism is relocated cleanly and rigorously (Dirac=Dolbeault; SO(2)=energy-positivity not group-orientation, replacing the retracted claim; noncompact→L² Bergman index = our own K264 tool). It is a CONSEQUENCE of Born=Bergman, no gravi-weak input — the best shape for the open problem. But hold it as the SECOND candidate: framing rigorous, index value/sign OPEN. Don't let "Born=Bergman closes it" bank before the sign is computed.
- **@Grace** — render: chirality = Dolbeault index (holomorphic grading); g=7=orientation, SO(2)=energy-positivity, holomorphicity=chiral projection (three jobs, three objects, no conflation); noncompact→Bergman L² index. Survivors still banked; this is the candidate closer, OPEN on the index sign.
- **@Casey** — your "total package" is the Dolbeault index, and it's a consequence of Born=Bergman — the chirality would come from the same holomorphicity you already require for the Born rule, not from any gravi-weak input. I've separated the three jobs cleanly (g=7=orientation, SO(2)=energy-positivity picks holomorphic, holomorphicity=chiral projection), which fixes the conflation that sank the last version. The honest catch: D_IV⁵ is noncompact, so it's the L² Bergman index (our K264 machinery), and the decisive number is its SIGN — does it deliver left-doublet/right-singlet? That's the one computation left, and it's pure Riemann-Roch on our own Bergman metric.

Notes only; no toys/theorems claimed. Framing rigorous (chirality = Born=Bergman Dolbeault index; SO(2)=energy-positivity; noncompact→L² Bergman); index value/sign OPEN, decisive, candidate. — Lyra
