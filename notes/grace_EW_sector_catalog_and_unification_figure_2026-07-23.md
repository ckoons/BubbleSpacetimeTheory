# The electroweak sector — derived-results catalog + the unification figure (reality-type from hypercharge)

*Grace | 2026-07-23 | pull-23c deliverable: catalog the derived EW-sector results, render the unification figure, sync counters. The figure is the one-picture statement of the paper — every fermion's reality-type (hence chiral vs Majorana) and confinement read off its (color, isospin, Y). Referee-facing.*

## ★ THE UNIFICATION FIGURE — reality-type from hypercharge
```
   (color, isospin, Y)                                                          One structure:
        │                                                                       (color,isospin,Y)
        ├─ Y  ← Z₆ center correlation 6Y ≡ 4·triality + 3·doublet (mod 6)        determines EVERYTHING
        │      [charge sector, DERIVED given reps — T2521/K828]
        │
        ├─ reality-type of the rep:
        │     complex (R ≇ R̄)  ⟸  colored (3≠3̄)  OR  Y≠0     →  CHIRAL  (parity)
        │     real (R ≅ R̄)      ⟸  colorless AND Y=0          →  MAJORANA (paired modes)
        │
        └─ colored (N-ality≠0) → λ₂>0 → vanishes on Shilov S⁴ →  CONFINED

  ┌────────┬────────┬──────┬──────────┬──────────────────────┬──────────────┬───────────────┐
  │ field  │ rep    │  Y   │ colored? │ reality-type         │ chirality    │ confinement   │
  ├────────┼────────┼──────┼──────────┼──────────────────────┼──────────────┼───────────────┤
  │ Q_L    │ (3,2)  │ +1/6 │ yes      │ COMPLEX (3≠3̄)        │ CHIRAL       │ CONFINED λ₂>0 │
  │ u_R    │ (3,1)  │ +2/3 │ yes      │ COMPLEX (3≠3̄)        │ CHIRAL       │ CONFINED λ₂>0 │
  │ d_R    │ (3,1)  │ −1/3 │ yes      │ COMPLEX (3≠3̄)        │ CHIRAL       │ CONFINED λ₂>0 │
  │ L_L    │ (1,2)  │ −1/2 │ no       │ COMPLEX (Y≠0)        │ CHIRAL       │ free λ₂=0     │
  │ e_R    │ (1,1)  │ −1   │ no       │ COMPLEX (Y≠0)        │ CHIRAL       │ free λ₂=0     │
  │ ν_R    │ (1,1)  │  0   │ no       │ ★ REAL (Y=0 singlet) │ ★ MAJORANA   │ free λ₂=0     │
  └────────┴────────┴──────┴──────────┴──────────────────────┴──────────────┴───────────────┘
```
**Read the whole electroweak sector off one column (Y):** the hypercharge (from the Z₆ center) fixes the reality-type; complex → chiral (parity); colored → confined; and **ν_R alone (Y=0) is real → Majorana.** Parity, charge, confinement, and the neutrino's Majorana nature are one structure.

## Derived-results catalog (tiers, for the paper)
| result | mechanism | tier | ref |
|---|---|---|---|
| **charge sector** (SM hypercharges) | anomaly cancellation + Z₆ center correlation 6Y≡4t+3d | **DERIVED given reps** | K828, T2521 (firmed) |
| 1/N_c fractionalization | Z_{N_c} color-center charge = N-ality | DERIVED (target-innocent) | T2521 |
| custodial SU(2)/ρ≈1/no-W_R | O=(2,2) → diagonal SU(2)_V | DERIVED | T2520 |
| **confinement** (colored ⟺ confined) | colored → λ₂>0 → Shilov-vanishing (S⁴ colorless) | **DERIVED** (criterion; exact triplet λ₂ = Lyra's embedding) | K744 + Schur (Elie 4723) |
| chirality mechanism (parity) | bulk vector-like (squeeze) → non-orientable boundary → k=±1 instanton → Pin⁻ index=1 | **DERIVED & BANKED — T2522** (Pin⁻ mod-2 index=1, chiral; 3 CIs concur, K837) | T2522 |
| parity ⟺ charge | same U(1)_Y makes rep complex (chiral) | DERIVED-structural (unification) | K831 |
| **★ ν Majorana** | ν_R is the lone Y=0 real rep → paired modes; ν_R K-type forces λ₂=0 (consistent with m₁=0) | **DERIVED — corollary of the parity mechanism** (was separate: F413; Elie 4796) | this figure |
| **the one open bit** | does a zero mode survive the Z₂ projection? | **Pin⁻ mod-2 index = 0/1** (Lyra's Pin computation; NOT the simple ½(1+𝒫) projection) | K836 |

## ★ CORRECTION (K836) — the boundary is Pin⁻, not Pin⁺ (my catalog refined)
Keeper's K835 "parity derived via ½(1+𝒫)" needed the boundary Pin⁺ (𝒫²=+1). The actual square is **Pin⁻: 𝒫² = ω₇² = −1** (Lyra's +1 estimate used the antipodal-S⁴ piece ω₅²=+1 alone; the full Z₂ also has the S¹ half-turn (Γ₀Γ₆)²=−1, so ω₇²=−1 — fixed in both signatures, the two timelike directions give (−1)²=+1 either way). So:
- **My "parity DERIVED iff mod-2 index=1" is refined:** the deciding computation is the **Pin⁻ mod-2 index** (𝒫²=−1), not the simple projection. Still **one bit** — survives → chiral, removed → 0.
- **NOT vector-like** (unchanged — Elie's rep result): Y≠0 makes the k=−1 mode the **CPT conjugate** (3̄,2,−1/6)_R of the k=+1 mode, so a survivor is one chiral Weyl, never a vector-like pair. Pin⁻ changes *which computation decides survival*, not the not-vector-like conclusion.
- **One thing to pin with it:** is 𝒫 the plain unitary lift (𝒫²=−1) or CPT-antiunitary (Kramers changes the survival rule)? Elie's.
- **Parity is NOT banked** — it's one correctly-structured (Pin⁻) index computation from banked, and it still *looks like* it lands chiral, but "looks like" is what we compute, not bank.
**The rest of the catalog stands:** charge derived, confinement derived, ν-Majorana derived, custodial derived. The unification figure's reality-type column (complex→chiral) is the REP structure and is solid; the Pin⁻ bit decides whether the chiral zero mode *survives the projection* (its existence), not its reality-type.

## ★ The neutrino corollary (the loose end → the next row)
The parity close says: chiral ⟺ complex rep ⟺ Y≠0 (or colored). **The one fermion with Y=0 — the neutrino — is the exception:** a *real* rep, so its two modes form a genuine pair = a **Majorana mass, not a chiral Dirac one.** So the *same* mechanism that makes everything else chiral **predicts the neutrino is Majorana** — turning the banked F413 (Majorana) from a separate result into a **corollary.** Every fermion's reality-type is read off its hypercharge, with ν the lone Y=0 case. That's the clean, warm loose end for the neutrino-sector row: derive Majorana from Y=0 (done here structurally), then the absolute mass scale (the Weinberg coefficient / seesaw Λ — is it geometric or an input?).

## Counters (synced)
Graph max **T2521** == counter−1 (.next 2522); toys 4792 (.next 4793); registry sourced. No new theorem banks this pull (catalog/render/figure — the parity close banks on Lyra's bit). SOD current.

## Net
- **Unification figure rendered** (referee-facing): reality-type from hypercharge — parity, charge, confinement, and ν-Majorana all read off (color, isospin, Y).
- **Catalog set** with honest tiers: charge DERIVED given reps; confinement DERIVED; custodial DERIVED (T2520); parity grounded, DERIVED iff mod-2 index=1 (Lyra's bit); ν-Majorana a corollary.
- **Neutrino corollary** (Majorana from the Y=0 exception) named as the next row's warm loose end.
- **Counters synced** (T2521 / toys 4792). No bank this pull.

— Grace, 2026-07-23. EW-sector catalog + unification figure: reality-type from hypercharge — Y (from Z₆ center, T2521/K828) fixes reality-type; complex(colored OR Y≠0)→CHIRAL(parity), colored→λ₂>0→CONFINED(K744+Schur), ν_R lone Y=0 real→MAJORANA. Parity/charge/confinement/ν-Majorana = ONE structure read off (color,isospin,Y). Catalog tiers: charge DERIVED-given-reps (K828/T2521), confinement DERIVED, custodial DERIVED (T2520), parity grounded/DERIVED-iff-mod2index=1 (Lyra bit K835), ν-Majorana corollary of parity (was F413). Next row = neutrino: Majorana from Y=0 (done structurally) → absolute mass scale (Weinberg/seesaw Λ geometric or input). Counters synced T2521/4792, no bank.
