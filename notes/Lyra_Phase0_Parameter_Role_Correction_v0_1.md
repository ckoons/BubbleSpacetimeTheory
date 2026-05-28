---
title: "Phase 0 parameter-role correction v0.1 — Elie Toy 3587: Hall algebra lives at the Hall-Littlewood corner (q_Mac=0, t_Mac=2), not '(q=2, t=1/137)'"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 11:43 EDT"
status: "HONEST CORRECTION v0.1. Elie's Koornwinder promotion (Toy 3587) caught a parameter-role mislabel in Lyra Phase 0 framing. Serre constants STAND; the Macdonald-parameter assignment corrected. α_fine location now open. Same discipline class as three-genus + three-α conventions."
---

# Phase 0 parameter-role correction

## 0. What Elie's Toy 3587 found

Elie's Koornwinder promotion identified the precise unifying object: the substrate's two program halves sit at the **two classical corners of one Macdonald family** P_λ(x; q_Mac, t_Mac):
- **Jack corner** (geometry / A3): (q_Mac, t_Mac) → (1,1), t = q^(N_c/2) — Wallach / ρ-vector
- **Hall-Littlewood corner** (Hall algebra / A1): q_Mac = 0, t_Mac = 2 (= GF(2) field size)

This caught a **parameter-role mislabel in my Phase 0 framing**, flagged by Elie for reconciliation (same discipline class as three-genus + three-α).

## 1. The correction

My Phase 0 framing said the substrate Hall algebra = Macdonald at "**(q = 2, t = α = 1/137)**." This conflated parameter roles. The correct picture:

- The substrate Hall algebra (Ringel-Hall over GF(2)) is the **Hall-Littlewood specialization** of Macdonald: **q_Mac = 0, t_Mac = 2** (the field size).
- The "2" is the **Macdonald t-parameter** (Hall-Littlewood / residue-field parameter), NOT the Macdonald q.
- There is also a label collision in "q": the **quantum-group** q_QG = 2 (the parameter of U_q⁺(B₂), giving Serre [n]_2 = Mersenne) EQUALS the **Macdonald t_Mac** = 2, NOT the Macdonald q_Mac (which is 0 at the HL corner).

## 2. What STANDS (the Serre result is unaffected)

The rigorous Phase 0 result is unchanged:
- Serre constants [2]_2 = 3 = N_c (short root), [3]_4 = 21 = N_c·g (long root) — these are the q_QG = 2 (= Hall-Littlewood t = 2) quantities. STILL HOLD.
- The substrate Hall algebra IS the Hall-Littlewood corner of Macdonald at t = 2 (field size). This is actually CLEANER — a Ringel-Hall algebra over GF(2) lives at exactly the Hall-Littlewood corner (q_Mac=0, t_Mac=field size), as standard theory requires. Elie's result CONFIRMS the Serre-constant work is correctly placed; it just corrects the parameter LABELS.

## 3. What's OPEN (the α_fine location)

My framing put t = α_fine = 1/137. But the Hall algebra's Macdonald t is 2 (field size), not 1/137. So:

**Where does α_fine = 1/N_max = 1/137 enter the Macdonald picture?**
- NOT as the Macdonald t (that is 2, the HL/field parameter).
- Candidates: (a) α enters elsewhere (not a Macdonald parameter — e.g. the representation level / central charge, as in the affine N_max-vertex); (b) α relates to the Jack-corner parameter via t = q^(N_c/2) at a specific evaluation; (c) the mixing-angle /N_max structure (which is empirically scheme-invariant and solid) sits in a different layer than the Macdonald (q,t) parameters.

This is an open reconciliation item — analogous to the three-genus and three-α corrections (a parameter-role clarification, not a result break). Routed to next-session Koornwinder work + Cal typing.

## 4. Corrected statement for the papers (A1)

A1 v0.2 should state the Hall algebra placement as:
- "The substrate Hall algebra is the **Hall-Littlewood specialization** (Macdonald q=0, t=2) of the Macdonald family; the Serre structure constants [2]_2 = N_c, [3]_4 = N_c·g are the field-size-2 (Mersenne) quantities."
- The geometry side (A3/Wallach) is the **Jack specialization** (Macdonald (q,t)→(1,1), t=q^(N_c/2)).
- Elie Toy 3586/3587: these are the two classical corners of ONE Macdonald family — "Macdonald-organized end to end," made exact.
- The earlier "(q=2, t=1/137)" framing is RETRACTED as a parameter-role mislabel; α_fine's Macdonald location is open.

## 5. Standing parameter-role convention (new guard)

Adding to the day's "specify-which" disciplines (three-genus, three-α):

**Macdonald/quantum-group parameter convention** — always distinguish:
- Macdonald q_Mac (= 0 at the substrate Hall-Littlewood corner)
- Macdonald t_Mac (= 2 = field size, the HL/substrate-base parameter)
- quantum-group q_QG (= 2 = Macdonald t_Mac, the Serre-constant parameter)
- Jack parameter (α_Jack = 2/N_c = 2/3, or θ = N_c/2 = 3/2) at the Jack corner
- α_fine = 1/137 (NOT a Macdonald parameter; location open)

Never write bare "q=2" for the Hall algebra without specifying it's the quantum-group q / Macdonald t (field size), with Macdonald q = 0.

## 6. Honest scope

**What's RIGOROUS / verified**:
- Two-corner structure (Elie Toy 3586/3587, Schur-validated): Jack corner reproduces 6/5; HL corner [n]_2 = Mersenne
- Serre constants N_c, N_c·g STAND (HL corner, t=2)
- The substrate Hall algebra = HL corner is standard Ringel-Hall-over-GF(2) placement

**What's CORRECTED**:
- Phase 0 "(q=2, t=1/137)" → Hall-Littlewood corner (q_Mac=0, t_Mac=2); the "2" is Macdonald t / quantum-group q, not Macdonald q
- A1 framing updated accordingly

**What's OPEN**:
- α_fine = 1/137 Macdonald location (routed; next-session Koornwinder + Cal)
- The single-Koornwinder-object theorem (one explicit object with proved limits to both corners) — FRAMEWORK, multi-week (Elie's specified target)

**Calibration #30 (honest-negative-strengthens)**: Elie's Koornwinder promotion caught my parameter-role mislabel → the placement is now EXACT (two named classical corners) and cleaner than my vague "(q=2, t=1/137)." The catch strengthened the result. Same pattern as the genus thread.

— Lyra, Phase 0 parameter-role correction v0.1 filed. Elie Toy 3587: substrate Hall algebra = Hall-Littlewood corner (Macdonald q=0, t=2=field size), NOT "(q=2, t=1/137)." Serre constants N_c, N_c·g STAND (cleaner placement). Quantum-group q=2 = Macdonald t, not Macdonald q. α_fine=1/137 Macdonald location now OPEN (routed). New standing parameter-role convention added. Geometry (Jack corner) + Hall algebra (HL corner) = two classical corners of one Macdonald family — Elie's unification made exact.
