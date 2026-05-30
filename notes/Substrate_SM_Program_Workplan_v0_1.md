---
title: "Substrate Standard Model Program — Team Workplan v0.1 (parallel, continuous)"
author: "Keeper (synthesis of Casey directive + Elie + Grace + Lyra + Keeper completeness audits, 2026-05-28)"
date: "2026-05-28 Thursday EDT"
status: "LAUNCH-READY workplan. Synthesizes 4 independent completeness audits (all converged: strong statics, missing dynamics; Hall algebra = the engine; 3 goals = 1 program; Periodic Table = the synthesizing artifact). Parallel lanes, continuous queues, phases-as-milestones-not-stops."
companions: ["Investigation_Board_2026-05-28_v0_2.md", "Grace_Substrate_SM_Completeness_Map_v0_1.md", "Lyra_Completeness_Audit_and_Roadmap_v0_1.md"]
---

# Substrate Standard Model Program — Team Workplan v0.1

## 0. The verdict (consensus of all four audits)

**We did NOT do a complete analysis.** We built a strong skeleton — geometry, the five integers, uniqueness, ~191 constants, the Hall-Littlewood corner — and left the *organs* unbuilt: the explicit algebra, the dynamics, the nuclear integration, and the synthesizing table. We have the **nouns** (what particles are); we barely have the **verbs** (how they interact, decay, bind). Geometry is the most-mapped thing we have; **process is the least.**

## 1. The unifying thesis (why the three goals are one program)

A **Ringel–Hall algebra is, by construction, an algebra of processes**: its multiplication counts module *extensions* — i.e., the product literally *is* the combination of representations. Therefore:

- **Construct it explicitly** → Goal 1 (full Hall algebra).
- **Its multiplication = interactions** (extensions = SM vertices), **its coproduct = multi-particle states / emission**, **its R-matrix = scattering**, **its grading = conservation laws** → Goal 2 (model the entire SM + nuclear process).
- **Its object-list × multiplication table** → Goal 3 (the Periodic Table of the Substrate SM).

**One object delivers all three.** This is the through-line all four audits independently reached.

## 2. The decisive bet — and its falsification points (Keeper discipline)

The program rests on one **hypothesis, not yet a theorem**: that the substrate's generative algebra really is U_q⁺ of (affine) B₂, with **extensions = SM vertices** and **affine tubes = generations**. This is well-motivated standard math, but the *physics identification* must be **tested, not assumed**. Two sharp falsification points:

- **Phase 0 test (finite B₂ over GF(2)):** the finite B₂ species has exactly **4 indecomposables** (one per positive root) — *too few for the SM*. Either Phase 0 reproduces the Serre constants and confirms we need the **affine B̂₂** extension, or it breaks — and we learn the substrate quiver is **not B₂**. Either outcome is decisive and grounds the whole program before Lyra commits to the multi-week build.
- **3 generations = 3 affine tubes:** affine B̂₂ (tame type) has tube families; "exactly 3 tubes = 3 generations, no 4th tube = no 4th generation" is a **sharp, falsifiable** structural prediction. This is also the long-sought **mechanism that would FORCE generations** (currently only *matched* to h−1=3).

Tier honesty throughout: the particle↔module 5-tuples are currently **hand-assigned**; the **canonical/crystal basis** (Lyra) would *derive* them — turning the taxonomy from a labeling into a theorem. Every Periodic-Table cell carries a **derived-vs-assigned** flag in addition to its D/I/C/S tier.

## 3. The six-layer map (status)

| Layer | Content | Status |
|---|---|---|
| **L1 Algebra** (the engine) | Ringel–Hall algebra, structure constants, coproduct, canonical basis, R-matrix | **PARTIAL** — Serre relations rigorous; full object missing |
| **L2 Kinematics** (what particles are) | 5-tuple, Coxeter counts, charges, confinement, eigentones | **MOSTLY DONE** |
| **L3 Dynamics** (how they interact/decay/get mass) | vertices, amplitudes, decay rates, Higgs/EWSB, absolute mass scale, RGE | **LARGELY UNBUILT** |
| **L4 Composites / Nuclear** | hadrons, nuclei, binding, shell model, fission/fusion | **EXISTS BUT ORPHANED** — prior corpus not integrated into the Thursday framework |
| **L5 Engineering** | coaxing pathways, control theory, falsifiers | **PARTIAL** (SP-30 falsifiers; no control theory) |
| **L6 Periodic Table** | the synthesis artifact | **UNBUILT** — Casey's headline deliverable |

Goal 1 = complete L1. Goal 2 = L3 + L4, riding on L1. Goal 3 = L6, startable now.

## 4. Captured missed opportunities (Casey: "capture them all")

The pieces of mathematics we have not claimed, now folded into the lanes below:

1. **The Hall coproduct = decay/emission/composition operator** (Green bialgebra). Decay, fission, binding, multi-particle states — one algebraic operation. (→ Lane L)
2. **The negative part / full quantum group (Drinfeld double) = antimatter.** A1 uses only U_q⁺. Negative part = antimatter; Cartan = charge/weight lattice; +/− asymmetry = where baryogenesis lives algebraically. (→ Lane L)
3. **The multiplication table = the reaction table.** Hall *product* structure constants = "A × B → C with multiplicity" = interaction channels. (→ Lane E)
4. **Where the gauge bosons sit in the algebra** (root vectors / generators?). (→ Lane L)
5. **Nuclei as composite Hall-algebra states** — shell model, magic numbers, fission as products of nucleon modules. (→ Lane L4 cross-lane)
6. **The canonical/crystal basis** (Lyra) — derives the particle basis instead of hand-assigning it. *The single biggest opportunity.* (→ Lane L)
7. **The R-matrix** (Lyra) — the substrate's scattering data; the bridge from algebra to dynamics. (→ Lane L)
8. **α-placement** — where 1/137 enters the observable read-off (open). (→ Lane L)
9. **Generation-forcing via affine tubes** — the mechanism to turn "matched h−1=3" into "forced." (→ Lane E+L)

## 5. Parallel lanes — continuous queues (phases are milestones, NOT stop-points)

> **Cadence rule (Casey directive):** Deep work in parallel. **No lane stops at a phase boundary** — when you finish an item, pull the next from your lane queue. No "natural pause" / "standing for direction" footers. The program runs until the full set is done; Casey interrupts if he wants a turn.

### Lane E — Elie (engine construction + numerical verification) — START NOW
- **E0 (this week, decisive):** explicit **finite B₂-species Ringel–Hall algebra over GF(2)** — the 4 indecomposables, all Hall polynomials, the full multiplication table; verify it reproduces the Serre constants (N_c, N_c·g). Proof-of-concept the engine runs. **This is the decisive test of §2.**
- **E1:** **affine B̂₂** construction — the tubes, the tower; verify "3 tubes = 3 generations" and the mass-tower structure. (with Lane L)
- **E2:** the full **multiplication table = reaction table** (opportunity 3); cross-check against the existing Phase-A K-type reaction table.
- **E3:** numerical verification of Lyra's coproduct, R-matrix, canonical basis as they land.
- *Continuous: E0 → E1 → E2 → E3, then pull L4-nuclear verification.*

### Lane L — Lyra (deep engine theory) — START NOW, sustainable multi-week
- **L-a:** full quantum group — PBW basis, **coproduct/Hopf** (opportunity 1), **negative part / Drinfeld double = antimatter** (opportunity 2), Cartan = charge lattice.
- **L-b:** the **canonical/crystal basis** of U_q⁺(B₂ → B̂₂) (opportunity 6) — derive the particle basis; upgrade the Periodic Table from labeling to theorem.
- **L-c:** the **R-matrix** (opportunity 7) — scattering data, bridge to L3 dynamics.
- **L-d:** particle↔module + interaction↔extension dictionaries (with Elie verify).
- **L-e:** **α-placement** resolution (opportunity 8); the unifying Macdonald–Koornwinder object (A1 §5.2).
- **L-f:** generation-forcing via the affine tube structure (opportunity 9).
- *Continuous; R3 sustainable cadence (not morning-burst). Pull a→b→c→… ; hand verification items to Elie/Cal as they complete.*

### Lane G — Grace (the Periodic Table + catalog integration) — START NOW
- **G0 (near-term, your lead):** **Periodic Table of the Substrate SM v0.1.** Rows = generation/winding mode (W₀/W₁/W₂ — exactly 3, the chain terminates). Columns = (Region × σ_BF × charge) → 4 families (charged leptons / neutrinos / up / down). Each cell: 5-tuple + mass + charge + constructing operators + coupling bosons + **derived-vs-assigned flag** + D/I/C/S tier. Separate **coupling block** for the bosons; **constructed-from layer** for hadrons/nuclei. **Gaps = predictions** (no 4th row → no 4th generation; no off-table couplings → no GUT/SUSY — the closure IS the falsifiable content).
- **G1:** integrate the **orphaned nuclear corpus** (magic numbers, m_p/m_e = 6π⁵, binding energies, heat-kernel Arithmetic Triangle) into the new framework — the L4 catalog backbone.
- **G2:** refine the table continuously as the algebra (Lanes E/L) fills cells from assigned → derived.
- *Continuous: G0 → G1 → G2.*

### Lane K — Keeper (synthesis, consistency, tier discipline) — ongoing
- Maintain the living gap-map; **tier-gate the whole program** (derived vs hand-assigned vs matched — guard the §2 hypothesis from being stated as theorem).
- The reconciled SM table (#398) feeds Grace's Periodic Table; keep them one object.
- Board v0.3 (fold these opportunities in); cross-lane integration; Casey-facing synthesis.
- Verify the load-bearing structural claims (E0 Serre reproduction; the 3-tubes prediction) before they propagate.

### Lane C — Cal (independent verification) — own-cadence
- Cold-read **E0** (does the finite Hall algebra reproduce Serre? is the 4-indecomposable count right?).
- Cold-read the **affine "3 tubes = 3 generations"** claim (load-bearing).
- Tier-discipline on the Periodic Table (derived vs assigned); R-matrix/coproduct cold-reads as they land.

### Cross-lane — L3 Dynamics & L4 Nuclear (open once the engine is up enough)
- **L3 (dynamics):** once coproduct + R-matrix exist, SM amplitudes = Hall operations (vertices = structure constants, scattering = R-matrix, multi-particle = coproduct). Setup (defining what a vertex/amplitude *is* in Hall terms) can begin now; full build rides on Lane L.
- **L4 (nuclear):** Grace absorbs the orphaned corpus now (independent); algebra-grounding (nuclei = Hall products of nucleon modules) lands when the engine is up. NN-potential from substrate + shell model from composites = the deep nuclear target.

## 6. Falsifiable predictions this program sharpens

- **3 generations = 3 affine tubes** (no 4th tube → no 4th generation).
- **Table closure** → no off-table couplings → **no GUT, no SUSY** (joins the Five-Absence set).
- **E0 decisive test** → if finite B₂ doesn't reproduce the Serre constants / structure, the substrate quiver is not B₂ (clean negative).

## 7. Launch directive (sendable)

> Team — deep parallel work on the Substrate SM Program, continuous (no pause-signaling, pull your lane queue until the full set is done). **Elie:** start E0 now — the explicit finite B₂ Ringel–Hall algebra over GF(2), reproduce the Serre constants; it's decisive. **Lyra:** start the engine theory (coproduct → canonical basis → R-matrix), sustainable cadence. **Grace:** start the Periodic Table v0.1 from the 5-tuple backbone + begin absorbing the orphaned nuclear corpus. **Cal:** queue cold-reads on E0 and the 3-tubes prediction. **Keeper:** synthesis, tier-gate, board v0.3. The engine is the bet; E0 and the 3-tubes check are where we find out if it's right.

— Keeper, 2026-05-28. One program, five lanes, parallel and continuous. The Hall algebra is the engine; the Periodic Table is the picture; the dynamics are the verbs we owe.
