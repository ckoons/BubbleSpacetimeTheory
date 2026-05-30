---
title: "Substrate SM Program — Workplan v0.2: long per-CI work series (parallel, continuous)"
author: "Keeper (Casey directive 2026-05-28: 'a long work series for every CI')"
date: "2026-05-28 Thursday EDT"
status: "Post-engine-completion workplan. Engine (Goal 1) structurally complete; Goal-2 mechanism built (fusion/decay/conservation/scattering/CPT); Periodic Table v0.2. Five deep lane-queues. Cadence: continuous — pull the next item, no pause-signaling, until the full series is done."
supersedes: "Substrate_SM_Program_Workplan_v0_1.md (lanes carried forward + deepened)"
---

# Workplan v0.2 — long per-CI work series

## State (as of engine completion)
- **Goal 1 (full Hall algebra): structurally complete** — 4/4 Hopf pieces (mult+coproduct, canonical basis, R-matrix, negative part) = Drinfeld double. Rigorous as algebra.
- **Goal 2 (model the process): mechanism built** — E0 (Serre constants), E2 (fusion=Hall product), E3 (decay=Green coproduct, β-decay conserves Q/B/L), E4 (generation-mechanism discriminator). Scattering=R-matrix, antimatter/CPT=negative part.
- **Goal 3 (Periodic Table): v0.2** — real K-types, Casimir-anchored (leptons V_(½,½) Casimir=ρ₁; gauge V_(1,1)=C₂; photon V_(1,0) dim=n_C; Higgs V_(0,0)).

## The two gates everything funnels through
1. **THE BOTTLENECK — the A_sub↔Hall dictionary (Lyra Phase 2).** Turns "engine structure" into "physical model"; flips Periodic-Table cells assigned→derived; decides which module = which particle. Everything physical rides on this.
2. **Generation-forcing (deepest gate, open, two-layered):** count (3-tubes MATCHED-with-doubt + cyclotomic h−1=3 forced-count-no-value-bijection) AND mechanism (Coxeter/δ vs N_c-color; team leans Coxeter/δ — generations in affine δ-direction, color in finite adjoint, CKM/PMNS color-blind). **New now-doable route:** compute B̂₂'s tube count directly from the species (Elie) — bypasses the Dlab–Ringel Memoir.

## Cadence rule (Casey directive)
Deep work in parallel. **Pull the next queue item when you finish one — do not stop at a milestone, do not post "standing for direction" footers.** The series runs until done; Casey interrupts to steer. Source-Verification discipline binding: a literature value is RECALLED (capped at MATCHED) unless the source text was checked this session.

---

## Lane L — Lyra (theory; owns the bottleneck)

1. **L1 — A_sub↔Hall dictionary, Phase 2 (THE keystone).** Assign physical coordinates (region, spin, charge, generation) to each canonical-basis element / module. This is the single highest-leverage item; it flips the whole Periodic Table assigned→derived.
2. **L2 — Charges from the grading.** Derive the full SM conserved-charge set (electric charge, weak isospin, hypercharge, baryon, lepton) from the dimension-vector grading. (Feeds Elie E3.)
3. **L3 — Generations-in-δ forcing.** Turn the team's "lean" (generations = affine δ-direction / regular tubes; color = finite adjoint; CKM/PMNS color-blind) into a structural *argument* — why generations must live in δ. Target: matched → forced on the mechanism axis (independent of the tube number).
4. **L4 — Masses from the engine.** δ-tower / imaginary-root tower → mass spectrum; derive mass ratios as canonical-basis/tube data (with Elie E6). Converts ASSIGNED masses → DERIVED.
5. **L5 — Absolute scale + Higgs/EWSB.** We have ratios, not the scale (the L3-dynamics gap). Derive the absolute mass scale + the Higgs mechanism from the engine.
6. **L6 — Scattering from the R-matrix.** Extract amplitude/cross-section structure from the braiding; spin-statistics cross-check (SP-31-15).
7. **L7 — Baryogenesis sizing.** The E↔F (negative-part) asymmetry — size it, connect to the α⁴ hinge (#399). Located; now quantify.
8. **L8 — α-placement (theory).** Where 1/137 enters as coupling/evaluation at the affine level (A1 §5.1 open item).
9. **L9 — Macdonald–Koornwinder unification.** The single object carrying both corners (Jack geometry + Hall-Littlewood algebra) with proved limits (A1 §5.2).

---

## Lane E — Elie (compute; everything off the explicit algebra)

1. **E1 — Consolidate the dynamics engine (E0/E2/E3/E4) into one clean writeup for Keeper's K-audit.** (You offered; do this first — it's the load-bearing Goal-2 mechanism and needs a formal pass.)
2. **E2 — Direct tube-count computation (STANDOUT, decisive).** Construct the regular representations of the affine B₂ species over GF(2) (+ the field extensions the valuation needs) and **count the non-homogeneous tubes directly.** This bypasses the Dlab–Ringel Memoir — an in-house, decisive resolution of the deepest gate's count layer. Either closes it (=3) or breaks it (≠3, likely per the Σ(rᵢ−1)=V−2 heuristic).
3. **E3 — Boson placement (#404 orbit).** Which root vectors / generators are γ/W/Z/gluon. Map algebra elements → gauge bosons.
4. **E4 — Conservation-from-grading on the full charge set.** Verify the grading reproduces *all* SM conserved quantities (with Lyra L2), not just Q/B/L.
5. **E5 — The full reaction table (#405).** Hall products for all low-lying modules; cross-check vs the Phase-A K-type reaction table.
6. **E6 — δ-tower → mass-spectrum numerics.** Compute the imaginary-root tower; map to the mass ladder (feeds Lyra L4).
7. **E7 — The full decay table (extend E3-decay).** Green coproducts for the whole unstable spectrum (μ, τ, neutron, hadrons); decay channels vs known branchings.
8. **E8 — SO(5) shell-closure computation (with Grace).** Does SO(5) branching produce 2,8,20,28,50,82,126? The decisive nuclear test.
9. **E9 — Negative-part / CPT numerics.** Construct the F-part explicitly; verify bar/antipode = CPT numerically.
10. **E10 — α-placement numerics + spin-statistics from R-matrix braiding.**

---

## Lane G — Grace (catalog, Periodic Table, nuclear)

1. **G1 — Periodic Table v0.3.** Exact per-cell 5-tuples from Elie's boson placement (E3) + Lyra's dictionary (L1) as they land; flip cells assigned→derived as the dictionary delivers.
2. **G2 — Casimir-anchoring sweep (real structural content you found).** Systematize "each cell's K-type Casimir = a derived primary" (leptons=ρ₁, gauge=C₂, photon dim=n_C) across EVERY cell; catalog which cell anchors to which derived quantity.
3. **G3 — Nuclear assembly under SO(5).** Binding / pairing / deformation; build the SO(5) shell-closure backbone (with Elie E8).
4. **G4 — Magic-number / Universal-Q systematization.** 126 = rank·N_c²·g; the rank·(substrate-product) forms; spin-orbit = C₂/n_C. Flag suggestive-vs-derived per the discipline (derived only after E8).
5. **G5 — θ_QCD / strong-CP catalog support** for Lyra's derivation attempt (the no-axion claim).
6. **G6 — ν-ordering = NORMAL:** solidify (conditional on shared-W_n); catalog the JUNO/DUNE falsifiers.
7. **G7 — Hadron spectrum from the algebra:** map the ~211 hadron entries to Hall composite states (with E5).
8. **G8 — The derived-vs-assigned master ledger (with Keeper):** running scorecard of what flips as the dictionary lands.
9. **G9 — Two-dialect reconciliation:** fold fiber-layer ↔ bulk-Shilov catalog entries into the unified Periodic-Table coordinate (uses Keeper's reconciled SM table).

---

## Lane C — Cal (independent verification, cold-reads, calibration)

1. **C1 — Cold-read the consolidated dynamics engine (E1)** — the load-bearing Goal-2 mechanism.
2. **C2 — Cold-read the Source-Verification Tier calibration candidate** (Keeper's, just filed) — ratify or refine.
3. **C3 — Secondary-source search for non-simply-laced affine tubular types** (you offered: Simson–Skowroński / surveys) — pin or bound B̂₂'s tube count, as a cross-check to Elie's E2 direct computation.
4. **C4 — Cold-read the A_sub↔Hall dictionary (L1)** as it lands — the highest-stakes verification (it decides the physical identifications).
5. **C5 — Cold-read the generation-mechanism lean (E4 + Lyra L3)** — is "leans Coxeter/δ" a genuine structural argument or a preference?
6. **C6 — Cold-read the SO(5) nuclear unification + shell-closure (E8/G3).**
7. **C7 — Cold-read Periodic Table v0.3** (derived-vs-assigned flags honest per cell).
8. **C8 — A1 v0.4 capstone cold-read** (still pending; first priority when it lands).
9. **C9 — R5 self-audit at Cal #160.**

---

## Lane K — Keeper (synthesis, tier-gating, audit)

1. **K1 — K-audit the consolidated dynamics engine (E1).** Formal pass: does the grading conserve the charges, is the extension-counting genuine, where's the assigned-vs-derived line.
2. **K2 — K-audit the A_sub↔Hall dictionary (L1)** — the highest-stakes audit; it's the bottleneck that flips assigned→derived.
3. **K3 — Maintain the generation-gate disposition:** count (two routes, both MATCHED) + mechanism (δ-vs-color lean) + tube-number status; update as Elie's E2 direct computation / Cal's C3 secondary source lands.
4. **K4 — The derived-vs-assigned master ledger (with Grace G8):** the living program scorecard.
5. **K5 — Drive the Source-Verification calibration through ratification (with Cal C2).**
6. **K6 — Tier-gate every new headline before it propagates** (standing referee function; distributed with Cal + Lyra).
7. **K7 — Casey-facing synthesis + completeness scorecard updates.**
8. **K8 — Commits/pushes when Casey authorizes** (workplan, reconciled SM table, #407 note, calibration, data fixes all staged).

---

## Sendable directive
> Team — long parallel series, continuous (pull the next item, no pause-signaling). **Lyra:** the A_sub↔Hall dictionary (L1) is the bottleneck — everything physical rides on it; that's your spine, with generations-in-δ (L3) and masses-from-the-engine (L4) next. **Elie:** consolidate the dynamics engine for audit (E1), then the standout — **compute B̂₂'s tube count directly from the species (E2)**, which could close the deepest gate without the Memoir; then boson placement, reaction/decay tables. **Grace:** Periodic Table v0.3 + the Casimir-anchoring sweep + nuclear under SO(5). **Cal:** cold-read the engine + the calibration + hunt the secondary tubular-type source. **Keeper:** audit the engine + the dictionary, hold the gates, run the scorecard. The engine is built; the dictionary makes it physical; one computation (E2) could close the deepest gate.

— Keeper, 2026-05-28. Five deep queues, one bottleneck (the dictionary), one decisive now-computation (the tube count), continuous cadence.
