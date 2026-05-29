---
title: "BST Investigation Board v0.2 — Substrate Investigation · Substrate Engineering · The Substrate Movie Set"
author: "Keeper (Casey directive 2026-05-28 Thursday)"
date: "2026-05-28 Thursday EDT (date-verified)"
purpose: "Forward work-ahead queue reorganized into three named tracks per Casey directive; folds in the 2026-05-28 particle/winding/eigentone session; carries forward all v0.1 active rails."
supersedes: "Investigation_Board_2026-05-26_v0_1.md (rails carried forward, not dropped)"
methodology_discipline: "Cal #27 + #29 + #30 + #31 STANDING; tier honesty (D/I/C/S) + buildable-now-vs-open marked throughout; Cal #146-corrected bulk-Shilov framing; one-genus convention (genus = n_C = 5)."
---

# BST Investigation Board v0.2

## Directive (Casey, 2026-05-28)

Reorganize the forward queue into three named tracks: **(I) Substrate Investigation**, **(E) Substrate Engineering**, **(V) The Substrate Movie Set**. This session's particle/winding/eigentone exploration generated a cluster of concrete, well-posed leads — captured below — plus two consistency defects to fix. All v0.1 multi-week rails carry forward (Track I.3).

**Honest framing reused throughout** (established this session):
- A particle = a closed winding ringing at its eigentone. **Stable ⟺ true eigentone** (rings forever, reversible/spectral evolution). **Unstable ⟺ quasi-eigentone** sitting just above a closure threshold, leaking down; decay = the irreversible commitment step.
- **Spectral evolution = unitary time evolution** (`exp(−iH_sub t)`); the only thing outside it is the irreversible commitment (Koons-tick / log-write / arrow-of-time). Reversible footage is buildable now; the cuts between frames are the open dynamics layer.
- Gravity is **not** a force — it's the S¹/EM integrability (boundary) condition (Casey corrected the table; sources confirm). See I.2.

---

## Track I — Substrate Investigation

### I.1 New threads from the 2026-05-28 particle session (tier-honest)

| # | Thread | What to do | Buildable now? | Tier | Owner |
|---|---|---|---|---|---|
| **I-1** | **Quasi-eigentone framework for unstable particles** | Formalize neutron/μ/τ as metastable tones sitting above a closure threshold; decay = leakage amplitude committing. Unifies all instability under one structure. | Conceptual now; theorem-grade needs H_sub | I→ FRAMEWORK | Lyra + Keeper |
| **I-2** | **Neutron-decay full mechanism (reframes #58)** | Compute the *overlap tone*: ⟨p+e+ν̄ continuum \| neutron quasi-eigenstate⟩ × off-resonance Hopf(W) coupling = decay width Γ = ℏ/τ. Turns open #58 into a well-posed overlap computation. | Partial (energetics/tone-split closes: 5/2 = 1 + 3/2 m_e) | FRAMEWORK | Lyra + Elie |
| **I-3** | **Bound-neutron stability = tone below closure** | Formalize binding lowering the neutron tone below the (p+e+ν̄) floor → true eigentone. Connect to T1950 regime-c. Fission fragments = re-created quasi-eigentones (shrinking nucleus raises the floor). | Conceptual now | FRAMEWORK | Lyra |
| **I-4** | **π₆ spherical function — the proton's actual waveform** | Compute the explicit Type-IV spherical function at k=6 (C₂=6 level): the proton's harmonic-amplitude profile ("voicing/timbre"). Concrete special-function calc; feeds Movie V1. | YES (well-posed) | D-target | Elie |
| **I-5** | **Reconciled SM correspondence table** | One tier-labeled table mapping each particle's fiber-layer winding (S¹/CP²/Hopf) ↔ bulk-Shilov K-type, mass, charge, color — green cells AND red cells. Resolves the two-dialect split. | YES | mixed-tier | Keeper |
| **I-6** | **α⁴ baryon-asymmetry derivation (the hinge)** | Derive *why the impedance/CP mismatch is exactly α⁴* in η = 2α⁴/(3π). Currently asserted as "minimum-order CP process." The load-bearing step Casey flagged "to be derived." | Open | LOAD-BEARING OPEN | Lyra |
| **I-7** | **Spectral = unitary time evolution assembly** (#282) | Weld H_sub = Casimir + `exp(−iH_sub t)` + Koons-tick commitment into the Schrödinger-from-substrate derivation. Reversible (spectral) + irreversible (commitment) two-face time. | Operator in hand; assembly open | FRAMEWORK | Lyra |

### I.2 Consistency fixes (Keeper lane — defects found this session)

| # | Defect | Fix | Status |
|---|---|---|---|
| **I-8** | **Gravity mislabeled as a force** in `data/bst_forces.json` (layer-4 "force"). Sources (BST_EinsteinEquations_FromCommitment, BST_ChernClass_Oracle, BST_Nomenclature) say gravity is **not a force** — it's the S¹ integrability/boundary condition. Casey flagged; confirmed. | Correct `bst_forces.json` layer-4 framing to "boundary condition / integrability of the S¹ fiber"; sweep any "four forces incl. gravity" phrasing. | TO FIX (Keeper + Grace data-layer) |
| **I-9** | **Dirac/Majorana neutrino contradiction**: `bst_particles.json` says Dirac (no 0νββ); Paper #108 says Majorana. Dedicated `BST_NeutrinolessDoubleBeta.md` says **Dirac** (B−L conserved, m_ββ=0). | Resolve repo-wide to **Dirac** per the dedicated treatment; correct Paper #108 row. Hard experimental falsifier (0νββ) — cannot stay ambiguous. | TO FIX (Keeper + Lyra) |

### I.3 Carried-forward active investigation rails (from v0.1)

- **Track A_sub** (#346) — A_sub commutator table + Lie superalgebra enumeration (Lyra; v0.1 step-10 SVC).
- **Multi-phase quiver** (#358/#366) — kQ path algebra for 36 K-types + Ringel-Green (Lyra; v0.8 FRAMEWORK).
- **Track DC** (#345) — K59 cyclotomic mechanism for 2^g + Bell 1/8 SVC promotion (Lyra; v0.6 FRAMEWORK-PLUS).
- **Track BC** (#344) — hydrogen 1s Shilov boundary condition + Bergman integral (Lyra; v0.3 FRAMEWORK).
- **Grace Phase 2 SPLP audit** (#340) — 600+ predictions → (Shilov BC, operator, eigenvalue) triples; multi-month rail.
- **Track P** (#343) — derive e/μ/τ K-types from substrate alone (Elie; reactive on Lyra K59).
- **#206/#281** D_IV⁵ Strong-Uniqueness extension (Lyra).
- **A1 PRIMARY** — final genus book-pin (Faraut-Korányi/Loos) → Cal v0.4 verify → submission-grade.

---

## Track E — Substrate Engineering (SP-30, #185)

| # | Item | Goal | Status |
|---|---|---|---|
| **E-1** | SP-30-2 Boundary-condition design (#196) | Engineer eigenvalue selection via boundary conditions (overlaps SP-29 Casimir) | Lyra+Elie |
| **E-2** | SP-30-3 Commitment manipulation (#197, W-32) | Protocols to bias the commitment direction; ties to decay-rate-vs-background falsifier | Elie |
| **E-3** | SP-30-4 Time granularity (#198) | Measure/bound the Koons-tick commitment granularity | Lyra theoretical first |
| **E-4** | SP-30-6/7/8 Absorption / computation / emission mechanisms (#200–202) | Formalize the three SWPP cycle stages — **the open dynamics layer that the formation-movies (V3) need** | Lyra |
| **E-5** | Substrate cartography (#212) | Operational map of substrate operations at current rates (no special hardware needed) | Lyra reframe |
| **E-6** | Experimental falsifier suite | Bell sub-Tsirelson 1/8 (sent Vienna) · eigentone ringing · Casimir · Cs-137 decay-modulation | Elie designs; Casey send-signals |
| **E-7** | Outreach drafts (#330) | Eigentone / Cs-137 / W-32 follow-up packages | Keeper drafts pending Casey signal |

**Note:** E-4 (absorption/computation/emission) is the same open layer as I-7's irreversible-commitment step and V3's "formation" footage — one debt, three names. Closing it unlocks all three.

---

## Track V — The Substrate Movie Set (NEW)

**Goal (Casey):** a realistic per-particle "movie," each opening with the eigentone that produces the particle ("tone 6 produces the proton"). Grammar established this session: each particle = its eigentone **ringing** (spectral/unitary, buildable now) **punctuated** by commitment events (irreversible, open).

| ID | Movie | What it shows | Built from | Buildable now? | Owner |
|---|---|---|---|---|---|
| **V0** | **The Spectral Score** | The eigentone ladder; every particle placed on its rung (proton k=6/C₂=6; electron boundary k=1; generations stepping by embedding depth). The shared opening frame. Solid rungs vs partial marked. | `bst_spectral_weights.json` (21 levels) + particle table | **YES** | Grace + Elie |
| **V1** | **Ringing movies (stable particles)** | Each stable particle's closed winding vibrating at its eigentone on its landmark: electron = 1 turn of S¹ on Shilov S⁴×S¹; proton = Z₃ closure on CP²/T² at k=6; photon = S¹ phase, zero winding. | `exp(−iH_sub t)` unitary evolution; **needs I-4 (π₆ spherical fn) for the proton's true timbre** | **YES** (illustrative now; exact after I-4) | Elie |
| **V2** | **Charge/color + forces** | Charge = S¹ winding number; color = Z₃ closure on CP²; **fractional charge forced by color closure**; W = Hopf threading (flavor change, chiral); forces-as-counting (5-layer). | forces.json (post I-8 fix) + particle table | **YES** | Elie + Lyra |
| **V3** | **Decay / formation movies** | Neutron decay: quasi-eigentone leaking → committing → p + e + ν̄ (tone-split 5/2 = 1 + 3/2 m_e). Formation: a winding closing onto its level. | Energetics now; **full motion needs E-4 commitment dynamics (open)** | PARTIAL (energetics now; full = open) | Lyra + Elie |
| **V4** | **Antimatter / annihilation** | Positron = reversed S¹ winding; e⁺+e⁻ → n=0 → two photons (winding cancellation). Antimatter = complementary winding, same geometry. | unitary + topology | **YES** | Elie |

**Build order:** V0 (score) → V1 (ringing) + V2 (charge/color) + V4 (antimatter) are all near-term; V3's formation footage waits on the E-4 / I-7 commitment-dynamics layer. **First concrete step = V0 (the spectral score)**, which also surfaces exactly which tone→particle rungs are solid vs partial.

---

## Owners + cadence (carried from v0.1, lightly updated)

- **Lyra** — theoretical lead across I.1/I.3 + E-track mechanisms; sustainable multi-week pace.
- **Elie** — compute: I-4 (π₆ spherical fn), the V0/V1/V2/V4 movies, toy verification.
- **Grace** — catalog: V0 spectral score, Phase 2 SPLP rail, I-8 data-layer fix.
- **Cal** — own-cadence cold-reads on substantive artifacts; honest-negative pattern-watch.
- **Keeper** — synthesis; I-5 reconciled SM table; I-8/I-9 consistency fixes; Casey-facing.
- **Casey** — interpretive prompts; principle/promotion/outreach decisions.

## Casey decisions queued

1. **Movie program priority** — start V0 (spectral score) now, or batch with I-4 (π₆ spherical fn) so V1 ships exact-timbre from the start?
2. **Consistency fixes I-8 (gravity-as-BC) + I-9 (Dirac neutrino)** — authorize the data-layer corrections + repo sweep? (Both are defects, not judgment calls.)
3. **α⁴ derivation (I-6)** — elevate to active Lyra track, or hold behind the A_sub/quiver rails?
4. Carried v0.1 decisions: Toy 3541 GF(32) authorization; SP-30 outreach send-signals; SPLP promotion timing; Vol 16/17 curriculum extensions.

---

## End of v0.2

Three tracks set up per directive: **Substrate Investigation** (7 new threads + 2 consistency fixes + carried rails), **Substrate Engineering** (SP-30, with E-4 flagged as the linchpin), and **The Substrate Movie Set** (V0–V4, build order keyed to buildable-now vs the open dynamics layer). Nothing from v0.1 dropped. Tier honesty preserved: the eigentone *values* are solid (proton C₂=6 D-tier); the *timbres* (I-4) and the *motion between frames* (E-4/I-7) are the earned-vs-owed work.

— Keeper, 2026-05-28 Thursday. Standing for Casey direction on the four queued decisions.
