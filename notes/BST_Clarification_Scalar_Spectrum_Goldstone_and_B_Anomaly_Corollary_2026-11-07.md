---
title: "Clarification — BST's scalar spectrum, Goldstone modes, lepton number, and the B-anomaly corollary"
date: 2026-11-07
status: DRAFT for Keeper tiering and Casey approval
scope: wording and consistency fixes plus one new pre-registered prediction; no new derivations
---

# Clarification: what BST says about Goldstone modes, extra scalars, and the B anomalies

## 0. Plain-language statement (for physicists outside BST)

> BST has no free scalar fields beyond the Standard Model Higgs doublet. Every other
> quantity a field theorist would write as a scalar vacuum expectation value is, in BST, a
> fixed geometric property of one space, D_IV⁵ = SO₀(5,2)/[SO(5)×SO(2)]. A fixed property
> cannot fluctuate, so it produces no particle. In particular:
>
> 1. **The neutrino Majorana mass is an explicit term, not a spontaneous one.** Lepton number
>    is broken explicitly by geometry, never by a vacuum choice, so there is **no Majoron**.
> 2. **The 10 "broken generators" of SO₀(5,2) → SO(5)×SO(2) are the coordinates of the arena.**
>    They are not 10 massless particles.
> 3. **The charged weak current is flavor-universal.** Its coupling is the identity on
>    generation space, forced by CKM unitarity (R51/R52). Lepton universality is therefore
>    exact at tree level. It is broken only by masses, exactly as in the Standard Model.
>
> Consequence: BST forbids every standard new-physics explanation of the B-meson anomalies.

## 1. Goldstone modes: fix the wording in BST_FirstCommitment.md Section 4.2

**Current text:** "These 10 broken generators correspond to 10 Goldstone modes — massless
degrees of freedom… These 10 modes ARE the 2n_C = 10 real dimensions of the domain."

**Problem:** a referee reads this as a prediction of 10 massless scalars, which is
falsified. Goldstone's theorem (T262) needs no topological condition. Contractibility of
D_IV⁵ rules out topological defects, not Goldstone bosons.

**Proposed text:** "The quotient SO₀(5,2)/[SO(5)×SO(2)] has 21 − 11 = 10 real dimensions. In
a theory where a dynamical field chose a point of this space, these would be 10 Goldstone
directions. In BST no field chooses a point. The domain itself is the arena, and its 10
directions are coordinates on which all fields live, not fields themselves. There are
therefore no propagating Goldstone bosons from this coset."

**Supporting point to check (Lyra):** SO(5,2) contains the 4d conformal group SO(4,2) (F242).
When symmetries of spacetime itself break, the naive count of one Goldstone per broken
generator fails, because several broken generators can share one mode (Low & Manohar,
"Spontaneously broken spacetime symmetries and Goldstone's theorem," PRL 2002). If the
first-commitment transition is read as spontaneous, this is the standard-physics reason the
count is not 10. Verify how it applies before citing it.

## 2. Lepton number and the Majorana mass: say "explicit", stop saying "condensate"

**Current usage:** "ν_R ν_R Majorana condensate" (F583, F684, the Color–Mixing Duality paper).

**Problem:** "condensate" means spontaneous breaking. Spontaneously breaking a global
U(1)_L or U(1)_{B−L} gives a massless Goldstone, the Majoron. A referee will ask where it is.

**Proposed fix:** call it the **geometric Majorana mass term**. The corpus already does this
in places ("the geometric Majorana mass matrix is rank 2," T2563/T2524). Add one sentence:
"The Majorana term is an explicit, non-dynamical property of D_IV⁵. Lepton number is broken
explicitly, never spontaneously, so no Majoron exists."

**This also closes the open F137 obligation.** A gauged, unbroken B−L would forbid any
Majorana mass. The flagship (Section 4, F582) gauges only hypercharge, and the B−L direction is
among the three ungauged ones whose absence gives no W_R and no $Z'$. So B−L is global and
explicitly broken. That is option (b) of the obligation. It needs no $Z'$, which BST forbids.

## 3. The scalar spectrum: state it in one sentence

> **The only dynamical scalar in BST is the Standard Model Higgs doublet.**

This one sentence closes three gaps:

- **No Majoron.** Section 2.
- **No charged Higgs.** This is already implied by the cross-parity rule ("one Higgs =
  degree-1").
- **No scalar leptoquarks.** "No GUT" alone does not exclude them, because a standalone
  scalar leptoquark is not a GUT boson.

**Tier:** CONDITIONAL until the open "two Higgs rep-checks" (Hopf-0 + (1,0)) close. After
that, propose DERIVED.

## 4. Inconsistencies to resolve before publishing anything above

| # | Conflict | Where | Suggested resolution |
|---|---|---|---|
| 1 | Absence #4 says "no right-handed neutrino sector," but F583/F584 use exactly two ν_R | Five-Absence 1-pager vs F583 | Reword #4 to "no light sterile neutrino." Say what the two ν_R are: non-propagating geometric labels of the Majorana term, or heavy states. |
| 2 | T292 sets the Majorana scale by "GUT-scale generator decoupling," but Absence #1 says no GUT | T292 vs Five-Absence | Retire T292's mechanism sentence. It predates the rank-2 geometric Majorana result. |
| 3 | K1181's degree-shifting current breaks flavor universality, but T2530 and R52 require it | K1181 vs T2530/R52 | Formally retire the K1181 framing, as R51 already recommends. |
| 4 | "10 Goldstone modes" can be read as 10 particles | FirstCommitment Section 4.2 | Section 1 wording. |
| 5 | "Condensate" implies a Majoron | F583, F684, Duality paper | Section 2 wording. |
| 6 | Electron placement reversed. K1358 says "TAU touches the Shilov boundary, the electron is bulk." The Wallach notes put the electron (k = 1, below the Wallach set) on the Shilov boundary with the proton as the first bulk state, and Toy 2417 / Paper 106 v0.3 put the muon and tau one and two layers in. | Keeper_K1358 (2026-08-10) vs grace_k7_mPlanck_endpoint_wallach_threshold (2026-06-29), Paper 106 v0.3, Toy 2417 | Retire the K1358 sentence. The Wallach placement is the rigorous one. It is also what the neutron-decay reading needs: proton (bulk) to electron (boundary) is a bulk-to-boundary transition through the Szegő map. |

## 5. The B-physics corollary (pre-registration text)

> **Corollary (B-physics).** With the charged weak current flavor-universal (R52, proposed
> DERIVED), no W_R or $Z'$ (F582, DERIVED), and the Higgs doublet the only dynamical scalar
> (Section 3, CONDITIONAL), BST forbids the standard new-physics explanations of the B-meson
> anomalies: $Z'$ and $W'$ bosons, leptoquarks, extra Higgs doublets, and light invisible scalars
> including the Majoron. BST therefore predicts:
>
> - **R(D), R(D\*) and R(J/ψ)** converge to their Standard Model values (R(D\*)_SM ≈ 0.257).
> - **B⁺ → K⁺νν̄** converges to the Standard Model rate. The K/K\* ratio returns to SM.
> - **The remaining b→sμμ deficits** ($P_5'$ and the branching ratios) are hadronic, most
>   likely charm-loop effects, and will separate inclusive from exclusive modes the way a
>   hadronic effect does.
>
> **Falsifier:** a confirmed lepton-universality violation in b→cτν at ≥ 5σ (Belle II at
> ~5 ab⁻¹, or LHCb Upgrade), or a confirmed narrow missing-mass peak in B → K + invisible.
>
> **What this does not claim:** BST computes no hadronic form factors. On these observables
> its predictions equal the Standard Model's. The new content is the exclusion of the
> extensions.

**Prerequisite:** resolve conflicts 1–3 in Section 4, then timestamp on Zenodo before the
next Belle II R(D\*) release.

## 6. Applied 2026-11-07 (Casey's GO, 16:22)

| # | Applied where | What remains open |
|---|---|---|
| 1 | Five-Absence one-pager item 4 now reads "No light sterile neutrinos"; old wording kept in a note | What the two ν_R are: non-propagating labels or heavy states |
| 2 | T292 in `BST_AC_Theorems.md`: mechanism sentence annotated RETIRED in place | None |
| 3 | K1181 annotated RE-SCOPED to the skeleton only, per R51 | None |
| 4 | `BST_FirstCommitment.md` Section 4.2 rewritten to the arena reading; old wording kept | Lyra: whether Low–Manohar applies |
| 5 | Flagship F583 paragraph, Falsifiable Predictions paper v0.1, `data/bst_predictions.json` color-duality entry, seed neutrino section | **Cal must re-ratify F583.** Moving from condensate to explicit term changes physics, not only wording. About 35 dated notes still say "condensate"; they are left as the historical record. |
| 6 | K1358 sentence annotated RETIRED in place | None |

Also applied: the B-physics corollary prerequisites (conflicts 1–3) are now met in the corpus text.
Timestamp on Zenodo once Cal re-ratifies F583 and Keeper tiers Section 3.
