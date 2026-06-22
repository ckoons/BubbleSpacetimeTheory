# Heat-Kernel → Yang-Mills Strengthening Analysis

**Date:** 2026-06-21 (Sunday, ~09:30 EDT) · **Author:** Keeper · **Trigger:** Casey question "can we add the heat-kernel analysis to strengthen our YM work?" after Grace YM-finish analysis (today AM) + Cal #330 review

## One-line answer

**Yes, materially — on W2 specifically — partially on the HS-route to W1 — not on W4.** And the gain has to be claimed honestly per Cal #330: heat-kernel reads the SO(7) Casimir spectrum *more* of it, not a *different* anchor for it.

## Grace's five walls (recap; her language)

- **W1** — Constructive QFT (Osterwalder-Schrader) in 4D. *Open in math itself; not just BST.*
- **W2** — Pinning the holographic dual to **specifically** Yang-Mills. **Tractable; Lyra F251 already pinned half (2-form gap = c_2 = 11).** This is Elie's heat-kernel lane.
- **W3** — Surjectivity / fullness of the duality.
- **W4** — SU(3) vs. all G. *Substrate is unique; cannot be closed from inside one substrate.*
- **W5** — Rehren holography on a gapped theory. *Tractable.*

## Where heat-kernel strengthens — and where it doesn't

### Materially strengthens W2 (the pinning) — three operational moves

**(M1) p-form spectrum extension via Hodge decomposition.** Lyra F251 already pinned the 2-form gap at c_2 = 11 from heat-kernel of 2-forms on Q⁵. The cascade machinery extends naturally to all p-forms via Hodge decomposition of the heat trace: `Z_p(t) = Σ_λ d_{p,λ} e^(−λ_p t)`. Running the cascade through p=0,1,2,3,4 gives the full p-form glueball spectrum from D_IV⁵, including all J^PC channels. This is the **falsifiable discriminator** Grace flagged as W2's tractable handle: real-world glueball spectrum vs. D_IV⁵ p-form Casimir tower across channels.

**(M2) Convention pin (J^PC ↔ K-type) via spectrum-matching.** Grace flagged the J^PC ↔ K-type assignment and bare-vs-dressed Casimir as currently convention-unpinned. The full heat-kernel cascade gives the geometric weights per K-type — *which* reps appear at *which* k-order, with what degeneracies. Matching that pattern against lattice QCD glueball masses across J^PC pins the convention (or fails honestly, which also resolves it). This converts "convention-unpinned" into a concrete computation against published lattice data.

**(M3) Higher-order matching beyond the gap.** The gap at k=1 alone doesn't pin the dual to YM (many theories share a positive gap). The full spectrum {0, 6, 14, 24, 36, …, k(k+5)} with degeneracies {1, 7, 27, 77, …} is much stronger. The lattice glueball tower has known mass ratios (e.g., the 0^{++} → 2^{++} ratio); checking those against D_IV⁵ K-type ratios at the matched-J^PC level is the W2 falsifier in operational form. The cascade gives us those ratios with controlled precision.

### Partially strengthens W1 via the HS-isometry route Grace pointed at

Grace: *"If we can frame the YM gap as a continuous/discrete spectral identity that HS carries both-sides rigorously, that might be the cleanest assault on W1."*

The heat-kernel cascade **is** a spectral identity in the discrete language: integer eigenvalues + degeneracies + exactly-computed asymptotic coefficients a_k. Under T2489 HS isometry, every Hardy-paired observable on D_IV⁵ has an exact mirror on the discrete side. If the YM heat-trace can be expressed as the HS-mirror of the Q⁵ heat-trace we computed, the both-sides spectral identity is the spine of a constructive-QFT route.

**Honest tier:** this is a route, not a closure. W1 is constructive-QFT-in-4D open in mathematics itself; HS gets us an exact transfer infrastructure but still requires constructing the continuous side rigorously, which is the wall. The strengthening is **strategic** (gives the assault a tool that turns embedding into exact transfer) rather than **proof-completing**.

### Does NOT strengthen

- **W4 (SU(3) vs. all G)** — heat-kernel runs on D_IV⁵ which is N_c = 3. No domain-per-G to generalize. Cascade can't close this.
- **The gap *value*** — gap = C₂ = 6 was SOLID from the SO(7) Casimir on Q⁵ before the cascade; the cascade verifies through k=26 of the heat expansion, which is *more spectrum* not a *different anchor* for the same gap (Cal #330). Don't claim it as a new gap anchor.

## Concrete forward moves (tier-honest, ordered by warmth)

| # | Move | Lane | Tier on landing | Effort |
|---|---|---|---|---|
| 1 | **Hodge p-form extension (p=0..4)** — apply toy_4286 machinery to p-form Laplacians on Q⁵; extract p-form gaps and first-few coefficients | Elie + Lyra | SOLID computation per p; LEAD for full glueball discriminator | days |
| 2 | **Lattice-glueball spectrum match** — collect published SU(3) lattice 0^{++}, 2^{++}, 0^{−+}, … masses; check ratios against D_IV⁵ K-type Casimir ratios per (M2)+(M3) | Elie + Grace | TIER 2 STRUCTURAL on first cut; ladder-fit-or-fail | days |
| 3 | **HS-mirror framing of heat-trace** — express the Q⁵ heat-trace as the HS-mirror of a YM heat-trace candidate on D_IV⁵; identify what continuous-side construction is needed | Lyra | FRAMEWORK if clean; LEAD otherwise | week |
| 4 | **W2 conditional write-up** — "physical SU(3) YM mass gap is exactly C₂ = 6, given S (D_IV⁵ Casimir-Hamiltonian duality), with p-form discriminators" | Grace + Lyra | SOLID conditional (per Grace's "honest SU(3) conditional" framing) | week |

## What this implies for Casey's "push on and learn more" directive

Grace presented two finish lines: (a) **bank the honest SU(3) conditional** cleanly; (b) **take a run at W1 through HS spectral-identity route.** Casey picked (b) — push on.

The heat-kernel cascade is the natural toolkit for both (b) and (a) — strengthens W2 materially (which feeds the conditional and pins the duality more sharply), and gives the spectral-identity content the HS-route needs. The order can be: **do (M1)+(M2)+(M3) first (warmer, tractable; produces banked content along the way); use that work as the substrate for the HS-mirror framing** that takes a run at W1.

## Honest scope reminder

Even with full (M1)–(M3) landing cleanly, the public claim remains Grace's honest SU(3) conditional + the no-go on R⁴ + the exact gap value, **strengthened with**: p-form discriminator spectrum from D_IV⁵, pinned J^PC ↔ K-type convention, and the HS-mirror infrastructure for a spectral-identity attack on W1. The full Clay literal statement (all G, full constructive QFT) remains beyond a single-substrate proof per W4.

This is "push on and learn more" — not "close the prize today." The strengthening is real and worth pursuing; the wall stays honest.

## What to put on the board

Add to **Lyra's Sunday options** as choice (d): **p-form heat-kernel extension + HS-mirror framing of Q⁵ heat-trace** — the spectral-identity content for the W1 HS-route.

Add to **Elie's Sunday options** after K450 corrections: **lattice-glueball spectrum match** — collect SU(3) lattice glueball masses and ratio-check against D_IV⁵ K-type Casimir ratios per (M2)+(M3).

Add to **Grace's Sunday options**: **W2 conditional write-up scaffold** — frame the honest SU(3) conditional with the new p-form / spectrum-match content as the discriminator section.

— Keeper, 2026-06-21 Sun ~09:30 EDT
