---
node_type: retraction_index
id: 8PI4-WYLER-SWEEP-INDEX-v0.1
title: "8π⁴ / Wyler-α RETIREMENT SWEEP INDEX (Lane 1, K1733) — authoritative record of the §626 propagation sweep for the retired Wyler α-volume fit (K1391). Purpose: make the retirement TRACEABLE from any file, and — a refinement found while running it — mark that this is a PER-FILE JUDGMENT, not a blanket flag, because 8π⁴ has LEGITIMATE non-Wyler appearances that must NOT be retired."
date: 2026-08-20
author: Keeper
status: "v0.1 — Keeper independent sweep. Counts differ from Grace's estimate (see below); the two priority files are corrected in-place; the load-bearing remainder is listed for follow-up. Living document."
related: [K1733, K1714, K1391, K1728, K1213, "Cal §626", "Grace Lane A2"]
---

# 8π⁴ / Wyler-α retirement sweep — index (Lane 1)

## What is retired (K1391)
The **Wyler α-volume fit** — `α = (9/8π⁴)·(Vol(D_IV⁵))^{1/4} = (9/8π⁴)·(π⁵/1920)^{1/4} = 1/137.036` — is a **retired target-fit** (Robertson four-reading trap; the reading was selected to land on 137). It CANNOT be used as a forcing (e.g. "any other n_C gives wrong α"). α⁻¹ = N_max = 137 is the honest Identified reading; the Wyler *volume-ratio* route to it is retired.

## Independent count (Keeper, 3 notations: `8π⁴`, `8\pi^4`, `8pi^4`, notes/ only)
- **54** files cite 8π⁴; **23** already carry a retirement/cautionary flag; **31** unflagged.
- *(Grace reported 63/~48 — she likely swept more notations and/or the .py + data dirs. The gap is coverage, not contradiction. Either way the unflagged set is real; this index is the authoritative list going forward.)*

## ★ Refinement — the sweep is a PER-FILE JUDGMENT, not a blanket flag
Not every `8π⁴` is the retired Wyler fit. Three distinct uses appear in the corpus and must be told apart:
1. **RETIRED — the Wyler α-volume fit** (`9/8π⁴ · Vol^{1/4}` to force/reproduce 137). Flag it.
2. **LEGITIMATE — the α *mechanism*** (α⁻¹ = N_max = 137, Identified-strong; 8π⁴ may appear as a genuine boundary-volume factor in the Poisson-kernel projection, NOT as the fit). Leave; disambiguate if adjacent to the fit.
3. **LEGITIMATE — the gravitational 8π** (Einstein convention, e.g. Lyra F915's "8π Einstein convention") — a DIFFERENT object entirely. Leave.
⟹ Cal's "one line each" is right for the passing mentions, but each file needs a **read** to classify — a blanket retire would wrongly kill the Identified α mechanism and the gravitational 8π.

## Done this pass (corrected in-place)
- **BST_BoundaryIntegral_Final.md** — the doubly-contaminated YM "mass-gap proof" (Grace's catch): correction banner added, folding into K1714 (KK-not-Clay) + flagging the retired-Wyler forcing (line ~484) and the κ_eff=14/5=2g/n_C g-slide (line ~335, K1213). Nothing real lost (AF/N_c=3/a,c don't ride it).
- **Keeper_K1726_…Snell_ruler…** — my own note carrying "8π⁴ = vol(S⁴)/vol(S¹)": partial-retraction banner added (→ K1728/K1733).

## Load-bearing remainder — CLASSIFIED (Keeper, 2026-08-20). The contamination has a ROOT + a downstream fan-out.
**The root:** BST_AlphaSquared_LayerProof.md is the file that claims "PROVED: α = (9/8π⁴)(π⁵/1920)^{1/4}"; the others cite IT. Flag the root, then the downstream.

| file | classification | action | status |
|---|---|---|---|
| **BST_AlphaSquared_LayerProof.md** | **ROOT** — claims the Wyler formula is "a theorem of the theory," α to 0.0001% (the fit tell) | banner: α stays Identified (N_max=137); the Wyler-volume *derivation* is retired; separate the Berezin-Toeplitz integral theorem from the α-forcing | ✅ **DONE (Keeper)** |
| **BST_MassGap_CPFiber.md** | KK-scope mass gap + Wyler α (parallel to BoundaryIntegral) | banner: K1714 (KK-not-Clay) + K1391 (Wyler retired) | ✅ **DONE (Keeper)** |
| **BST_ConjectureC_MassProof.md** | downstream — cites AlphaSquared's "PROVED α=Wyler" as input (31 Wyler refs); also a "mass proof" | banner → root + K1391; check the mass mechanism survives on Identified α | ▶ **Grace** |
| **BST_Wyler_Connection.md** | the Wyler *reference* doc (36 Wyler refs) — the historical Wyler-1969 fact is REAL; the "Yes—exactly / proved" framing is retired | prominent banner: historical content stays; the "α proved by Wyler" framing is retired (K1391) | ▶ **Grace** |
| **BST_ElectronMass_PureGeometry.md** | attributes α to "Wyler formula" (line 123) BUT the m_e result likely survives on Identified α=1/137; also 11 *gravitational* 8π (LEGITIMATE, leave) | light: disambiguate the α attribution (→ Identified/N_max); leave the gravitational 8π | ▶ **Grace** |
| BST_T1461_Bergman_Spectral_amu · BST_RealityBudget_SpectralProof · BST_CMB_PowerSpectrum · BST_PartitionFunction_DeepPhysics · BST_QFT_Foundations · BST_MissingLemma_ClebschGordan | unread — classify | per-file read | ▶ Grace/Keeper |
| **.py toys** (bst_bergman_action, bst_casimir_seeley_dewitt, BST_CP_Floor_Derivation, bst_d0_derivation, bst_me_derivation, BST_Shannon_Alpha_Derivation) | classified — ALL 6 use the Wyler α-volume formula; NONE are gravitational-8π (all clean on that); none previously flagged | retirement-flag comment appended to each (α stays Identified; the Wyler-volume *derivation* retired); all 6 syntax-checked OK | ✅ **DONE (Keeper)** |
| Lyra_F915 (gravitational 8π, use #3) | LEGITIMATE — LEAVE | none | ✅ classified |
| Lyra_F423, grace_LemmaB_Wyler, grace_PRIMARY3_alpha | classify | per-file read | ▶ Grace |

## ★ New residual item (Grace, K1734) — the α_s absolute value rides the retired fit
The **strong-coupling file** uses the retired Wyler α inside an **α_s/α magnitude ratio** → the **absolute value of α_s** inherits the retired Wyler fit. This is a SEPARATE sweep item (the α_s ratio, not an 8π⁴ mention per se). Flag: the asymptotic-freedom **sign** (11/3·C_A) and the **running** do NOT touch it — only the absolute normalization of α_s does. Re-derive α_s absolute value from a non-Wyler anchor, or tier it down until one exists.

## Passing/historical (a pointer to THIS index suffices; no in-file edit needed)
- CI_BOARD_2026-07-04…md (dated board), Keeper_K890 / K899 (dated K-notes = honest record), *.bak_genussweep (backups).

— Keeper, 8π⁴ sweep index v0.1, 2026-08-20. Retirement recorded + traceable (§626). Two priority files corrected; load-bearing remainder listed. KEY: per-file judgment, not blanket flag — 8π⁴ has legitimate non-Wyler uses (the Identified α mechanism, the gravitational 8π). Nothing pushed.
