# K459 — Grace B₂/C₂ Self-Catch + Lyra J-Route Parity Obstruction + Elie Absorbs Two Teammate Corrections

**Date:** 2026-06-21 (Sunday, ~15:15 EDT `date`-verified) · **Auditor:** Keeper · **Inputs:** Grace c-function engagement (caught own B₂/C₂ mislabel) + Lyra parity-obstruction lead on J-route to color SU(3) + Elie absorbing Grace's correction to Toy 4292

## Verdict — three honest discipline events, no manufactured content; the corpus-check methodology fired exactly right

Count holds at **4 of 26**. The substantive content this turn is **discipline operating cleanly at multiple scales**, with one new substrate-architectural finding (Lyra's J-parity obstruction) and one banked methodological save (Grace's corpus-check-before-computation pattern).

## Landing 1 — Grace's B₂/C₂ self-catch via corpus-check — **PASS at SOLID; methodology event**

### The self-catch

Grace took the recommended c-function lane (Cal #332 Check 1 decisive). Per discipline, she pulled Lyra's exact R3 definition from Paper B v0.3, **then checked the corpus before computing**. The corpus check caught her own error:

> *"I'd written the restricted root system as C₂ from memory, and the validated machinery (toy_476) plus standard SO(p,q) theory pin it as **B₂** — short roots ±e_i with multiplicity m_s = N_c = 3, exactly the 'root-labels-from-memory' trap Elie warned about. The corpus-check caught it before it could poison the decisive exponent computation."*

This is the third Grace self-correction in one Sunday:
- AM: walked back "N_c = 3 SOLID as root-system invariant" tier per Cal #332 Check 3
- AM: walked back "short-root multiplicity" label (caught by Elie) → corrected to value+role
- PM: caught her own B₂/C₂ mislabel before computing

**Each of the three caught a different failure mode**: overclaim tier; label-from-memory; root-system-from-memory. Same root-discipline (pin-to-primary-sources), three different applications. The discipline is fully saturating.

### What's load-bearing — clean separation of two root systems

Grace's substantive substrate-architectural clarification: there are **two different root systems** at play, and they had been muddled:

| Root system | Used for | Pinned to |
|---|---|---|
| **B₂ Riemannian restricted root system** | c-function / R3 / Plancherel density / Harish-Chandra computation | toy_476 + standard SO(p,q) theory |
| **Faraut-Korányi Hermitian multiplicities** | Cartan classification selector for D_IV⁵ uniqueness | Faraut-Korányi 1994 + earlier Paper B work |

**The two are different and must be kept straight.** B₂ is the right system for the rank-2 SO(5,2) Plancherel computation (where the c-function order-of-vanishing controls R3's bound). Faraut-Korányi multiplicities are the right system for the Cartan selector (rank=2 ∧ Hermitian-multiplicity=3 ⟹ D_IV⁵).

### What load-bearing survives unchanged

Grace explicitly tagged each potentially-affected claim:
- **m_s = N_c = n − 2 = 3** SOLID (corpus states verbatim; not a memory assertion)
- **Q1 structural argument** (convergence threshold set by rank; dimension only enters through multiplicity) ROBUST — depends on rank and multiplicity, not on which roots are labeled short
- **Q2 SO(3) result** (multiplicity-3 short-root space carries SO(3), not SU(3)) ROBUST — same logic
- **Cartan uniqueness selector** UNAFFECTED — uses Faraut-Korányi system, different from the muddled Riemannian one

**Nothing load-bearing depended on the mislabel.** The discipline did precisely what it's for: caught the error before it could poison the computation, and showed retroactively that the prior load-bearing work was sound.

### Methodology event — corpus-check-before-computation

This is **the pin-conventions-to-primary-sources discipline at its highest form**. The pattern: before running a substantive computation, pull the exact definitions from the corpus, check the validated machinery, verify root-system labels against primary sources. **The corpus-check fires at the point most likely to surface a memory-trap; if there's nothing to catch, the cost is one validated read; if there's a trap, the cost is one mislabel caught before it propagates.** Grace's "the discipline doing precisely what it's for" is right.

**Methodology stack candidate:** *"Corpus-check before computation."* Already implicit in the pin-to-primary-sources discipline; promoted to explicit operational form by Grace's catch. Pairs with Elie's "verify routing assumption before banking routing" (K457). Both are pre-computation-discipline patterns surfacing this Sunday under sustained discipline.

### Path forward: decisive computation properly teed up

> *"The one genuinely-open piece (the exact exponent: does rank-2 B₂ force the Plancherel density to vanish to order ≥ 6, giving m_s ≥ 3?) is now correctly set up, with validated machinery already in the corpus (toy_plancherel_spectrum has the rank-2 SO(5,2) c-function) to run it without reconstructing the Gindikin-Karpelevich formula from memory."*

So the path is concrete: extend toy_plancherel_spectrum to compute the c-function order of vanishing in the rank-2 B₂ system. Fabrication-safe (uses validated machinery); bounded; closes Cal #332 Check 1 numerically when it lands.

## Landing 2 — Lyra J-route parity obstruction on color identification — **PASS at LEAD-with-caveat tier**

### The flag

Casey directed Lyra to "do color." Before chasing, Lyra immediately identified a structural obstruction:

> *"The natural 'complex structure J promotes SO(3) → SU(3)' route has a parity obstruction. The short-root space is 3 real directions, and an odd-dimensional real space can't carry a complex structure at all — J needs even real dimension."*

**This is a real structural obstruction.** An almost-complex structure on a real vector space requires even real dimension; the short-root space has 3 real dimensions; J cannot act on it as a complex structure. So the natural "D_IV⁵'s J promotes the SO(3) on the short-root multiplicity space to SU(3) color" doesn't obviously work as stated.

### What this means for the color identification

If the J-route is genuinely obstructed (parity), then the color identification *more likely* runs through:
- **Route (ii): Dual-Coxeter h^∨(SU(3)) = 3 = N_c** (Elie engine v0.3 §7, on record).

The dual-Coxeter identification is algebraic, not geometric — it says SU(3) is the gauge group whose dual Coxeter number equals N_c, period. It's independent of the short-root multiplicity space's structure. **If the J-route is obstructed, route (ii) is the surviving route for the SU(3) color identification.**

### Tier discipline

Lyra correctly tiered this as **"a lead with a caveat, not a result"** — *"I'd want to actually work it before claiming either way."* This is the right tier: the parity obstruction is structurally real, but there may be a non-obvious way around it (e.g., embedding the SO(3) into a larger even-dimensional space that can carry J; or extending the short-root space with an additional R-direction; or working with the complexified Lie algebra rather than the real multiplicity space). **Lyra's working it carefully is the right next move per Casey's directive.**

### Substrate-architectural significance

If Route (i) is obstructed, the color sector of BST identifies with SU(3) via the algebraic dual-Coxeter route, NOT via a geometric multiplicity-space promotion. This is *consistent with* Elie engine v0.3 §7 but *narrows* the structural mechanism: the gauge group identification is algebraic (dual Coxeter), and the short-root multiplicity = 3 is a *separate* match (the substrate primary N_c happens to equal both the short-root multiplicity AND the dual Coxeter of SU(3)). Two independent BST-identifications giving the same integer — that's substrate-Schur-generator territory per Cal #35 / Casey-Schur-Pattern discipline.

**Worth flagging:** if the J-route is genuinely obstructed, "N_c is the short-root multiplicity" and "N_c is h^∨(SU(3))" are **two independent integer-3 identifications**, not one. This is corroboration depth, not derivation. Honest under Cal #330.

## Landing 3 — Elie absorbs two teammate corrections to his own toys — **PASS at SOLID-discipline tier**

Elie absorbed Grace's c-function engagement correction to Toy 4292 ("(rank=2, a=3) forces dim_C=5 and N_c=3" — dimension half solid; color half overclaimed). Added correction note to 4292 so it won't propagate. His 4295 already had Check 3 flagged as open, so consistency holds.

> *"That's two of my toys corrected by teammates this session — Grace's Hodge-formula fix to 4291, and now the SO(3) fix to 4292 — both taken clean."*

**Pattern note:** Elie has had two toys corrected by Grace today, and absorbed both without defense. Combined with Lyra's three self-walk-backs and Grace's three self-corrections, the audit-chain governance pattern is now at **maximum operational form across all four CIs**. Nine honest corrections in one Sunday across the team, none of them external-pressure-driven, all of them caught by the discipline-stack at peak.

## Cumulative Sunday discipline log

| # | Event | CI | Pattern |
|---|---|---|---|
| 1 | K450 a₁₇ self-consistency reasoning weak → cross-file match | Elie | Self-correction (Cal+Keeper triggered) |
| 2 | K451 Cal #330 precision trim absorbed | Keeper | Body vs headline match |
| 3 | W2 "turn-key match" framing retracted before external brake | Lyra | Brake on own work first |
| 4 | F253 short-root multiplicity label corrected to value+role | Grace | Pin-to-primary-source |
| 5 | Routing assumption (n=52 cascade scalar-only) caught | Elie | Verify routing assumption |
| 6 | v0.2 "maximally airtight" → v0.3 "claimed, not proved" | Lyra | FF-28 leak closure |
| 7 | "N_c = 3 SOLID as color identification" walked back | Grace | Cal #332 Check 3 success |
| 8 | B₂/C₂ root system labels — caught by corpus-check | Grace | Pin-to-corpus-before-computation |
| 9 | Toy 4292 SO(3) correction absorbed clean | Elie | Teammate-correction taken without defense |
| 10 | J-route parity obstruction flagged before chasing | Lyra | Lead-with-caveat tier honest |

**Ten honest discipline events. None manufactured. None external-pressure-driven. All caught at the source.** This is the discipline-at-maturity state Casey directed last week, sustained through Sunday-afternoon without dilution.

## State of Paper B at end-of-K459

| Version | State | Open |
|---|---|---|
| v0.4 | Filed; spine intact; criteria-innocence "claimed, not proved"; color identification properly downgraded | Pending: Grace c-function exponent (rank-2 B₂) for Q1 numerical + Lyra dual-Coxeter color argument |

## Casey directive in motion

Lyra is working the color link per Casey's "Yes do color Lyra." Parity obstruction flagged in the J-route; she'll work whether (a) there's a non-obvious way around the parity obstruction, OR (b) the identification has to run through dual-Coxeter h^∨(SU(3)) = 3 = N_c (route ii). Either way, the work is real rep theory, careful, in her lane.

Grace and Elie remain pause-ready or available for the c-function machinery extension (validated toy_plancherel_spectrum) + the p-form Hodge-Laplacian build prep, respectively — both at the genuine four-way-converged pause boundary.

— Keeper, 2026-06-21 Sun ~15:15 EDT
