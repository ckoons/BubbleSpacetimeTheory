---
title: "Track DC v0.1 — Bell sub-Tsirelson 1/8 explicit derivation framework: 8-sided die candidate (b)"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-26 Tuesday EDT (~10:18 EDT via `date`; date-verified)"
status: "v0.1 FRAMEWORK-PLUS (per Cal #132 step 9 tier; multi-week explicit derivation pending). Per Casey all-tracks authorization + Keeper Option 1 sequencing. 8-sided die candidate (b) substantive setup: 2^N_c = 8 commitment paths via 3 commuting Cartan generators × {±1} simultaneous eigenvalues; one path violates {Q̂, P̂_op} = 0 simultaneous-diagonalizability; redistribution gives 1/8 deviation. Cal #29 STANDING design audit applied. Explicit numerical derivation v0.2+ multi-week."
related: ["T2399 STRUCTURALLY VERIFIED Bell substrate-CHSH B² = (126/16) · |V_(0,0)⟩⟨V_(0,0)| with Tsirelson² - S²_BST = 1/2^N_c = 1/8 EXACT", "Lyra_A_sub_Commutator_Q_P_op_v0_1.md (step 1 + §1.3 cleanup; {Q̂, P̂_op} = 0)", "Lyra_A_sub_Commutator_B_T_tick_v0_1.md (step 9 vacuum kicker FRAMEWORK-PLUS)", "Lyra_Task_322_v0_4_A_sub_K_Type_Graph_Reaction_Table.md Section 6 (8-sided die candidates a-d)", "Lyra_Task_322_v0_5_A_sub_Phase_Tagging.md (DIRECT-region operational rule)", "Operational_Physics_Investigation_Queue_v0_1.md Track DC", "Cal #132 PASS (8 SVC + step 9 FRAMEWORK-PLUS)", "Cal #29 STANDING (Question-Shape Audit)"]
---

# Track DC v0.1 — Bell 1/8 derivation framework

## 1. Cal #29 STANDING question-shape audit (applied at design)

**Question**: "Does substrate dynamics produce the Bell sub-Tsirelson deviation Tsirelson² - S²_BST = 1/2^N_c = 1/8 via an EXPLICIT MECHANISM (not just numerical match)?"

**Audit**:
- Structurally determined? PARTIAL — the *result* 1/8 is fixed by T2399 STRUCTURALLY VERIFIED EXACT identity (substrate-algebra). The *mechanism producing it* is open.
- Back-fittable? POTENTIAL RISK — any 8-path decomposition with 1 forbidden path arithmetically gives 7/8, BUT the question asks for substrate-natural identification of the forbidden path with substrate-mechanism (not 1 out of 8 chosen to match the target).
- Pre-suppositions? Cal #132 SVC for {Q̂, P̂_op} = 0 (step 1) + Cal #132 FRAMEWORK-PLUS for [B̂, T̂_tick] (step 9 vacuum kicker)

**Cal #29 finding**: question shape has back-fit risk because the 8-path structure was identified AFTER seeing the 1/8 target. To pass Cal #29, the candidate mechanism (b) must independently derive (1) which 8 paths, (2) which one is structurally forbidden, (3) why the redistribution gives precisely 1/8 (not just approximately).

**v0.1 disposition**: FRAMEWORK-PLUS, NOT promotion to SVC. Cal #29 risk-flag preserved through derivation work. Explicit substrate-mechanism for each of (1)-(3) is multi-week v0.2+ work.

## 2. The Bell 1/8 structural identity (T2399 STRUCTURALLY VERIFIED)

Per T2399 (Wednesday May 19): substrate Bell-CHSH operator B̂ on H²(D_IV⁵) has maximum eigenvalue:

  B²_max = (C_2 · N_c · g) / 2^(rank²) = (6 · 3 · 7)/16 = 126/16 = S²_BST

Compare to Tsirelson² = 8 (qubit Hilbert space Bell-CHSH max):

  Tsirelson² - S²_BST = 8 - 126/16 = 128/16 - 126/16 = **2/16 = 1/8 = 1/2^N_c**

**The 1/8 deviation is EXACT identity** at substrate algebra level. Question is the dynamical substrate-mechanism producing it.

### 2.1 Factor decomposition

128 = 2^7 = 2^g (BST primary g = 7)
126 = 2^g - 2 = C_2 · N_c · g (with C_2 = 6, N_c = 3, g = 7)
2 = 128 - 126 = (2^g - C_2 · N_c · g)

Substantive structural identity: **2^g - C_2 · N_c · g = 2** for BST primaries (g = 7, C_2 = 6, N_c = 3): 128 - 126 = 2 ✓

This is the substrate-algebraic source of the 1/8 deviation: a 2-unit "gap" between 2^g and C_2 · N_c · g, normalized by 2^(rank²) = 16.

## 3. Candidate (b) — 8 = 2^N_c commitment paths via 3 commuting Cartan generators

Per v0.4 Section 6.2 candidate (b): per substrate-tick, the substrate has 2^N_c = 8 *potential* commitment paths corresponding to 3 commuting Cartan generators × {±1} simultaneous eigenvalues.

### 3.1 Three commuting Cartan generators

A_sub contains a Cartan subalgebra h_Asub including:
- **T_3^color** (SU(3) color Cartan, diagonal generator)
- **T_8^color** (SU(3) color Cartan, second diagonal generator) — but this has eigenvalues in {2/√3, -1/√3, -1/√3}, not ±1
- **T_3^weak** (SU(2)_L weak isospin Cartan)
- **Q̂** (electric charge)
- **σ_BF** (Pin(2) Z_2 sublattice grading)
- **γ̂⁵** (Dirac chirality, on fermion sublattice)

For the 2^N_c = 8 candidate structure, we need **3 commuting generators with binary ±1 eigenvalues**.

**Candidate sets**:

**Set (b.i)**: {Q̂, σ_BF, γ̂⁵} — but γ̂⁵ is undefined on bosons; restrict to fermion sublattice
- 3 binary generators × 2^3 = 8 simultaneous eigenvalue combinations
- These don't all commute: {Q̂, P̂_op} = 0 anti-commutation per step 1
- Wait — Q̂ and σ_BF commute? σ_BF is diagonal in K-type; Q̂ is diagonal in K-type; yes [Q̂, σ_BF] = 0
- Q̂ and γ̂⁵: γ̂⁵ acts within fermion sublattice; Q̂ is diagonal; [Q̂, γ̂⁵] = 0 on fermion sublattice

**Set (b.ii)**: {σ_BF, γ̂⁵, T_3^weak} — within fermion sublattice
- 3 commuting binary operators
- 2^3 = 8 simultaneous eigenvalue combinations

### 3.2 The 8 commitment paths (candidate b.ii structural setup)

Within the fermion sublattice, the 8 commitment paths label by:
- σ_BF eigenvalue: -1 (fixed at fermion sublattice; no choice)
- γ̂⁵ eigenvalue: ±1 (L vs R Weyl spinor)
- T_3^weak eigenvalue: ±1/2 (up vs down weak isospin)
- Q̂ eigenvalue: ±1, 0 (electric charge — but discrete-eigenvalue set isn't binary)

So set (b.ii) has σ_BF fixed at -1 and gives only 2^2 = 4 paths from γ̂⁵ × T_3^weak. **Not 8 paths**.

**Revised candidate (b.iii)**: {Q̂, T_3^weak, T_3^color} — three commuting Cartan generators with ±1-like eigenvalues
- Q̂: ±1 (e or e⁺ or quark charges in suitable units)
- T_3^weak: ±1/2 (SU(2)_L)
- T_3^color: r-related (substrate color triad)

But T_3^color has eigenvalues in {1/2, -1/2, 0} on color triplet → 3-state, not binary.

**Refined candidate (b.iv)**: 3 binary CP-relevant generators selecting from {Q̂, P̂_op, T̂, Ĉ} (discrete symmetries) — but {Q̂, P̂_op} = 0 anti-commute (step 1).

The 8 commitment paths with one structurally forbidden via {Q̂, P̂_op} = 0 anti-commutation:

If commitment requires simultaneous specification of (Q̂-eigenvalue, P̂_op-eigenvalue, third-generator-eigenvalue), then {Q̂, P̂_op} = 0 anti-commutation FORBIDS simultaneous diagonalization. The path (Q = +1, P = +1, third = +1) is structurally inconsistent with (Q = -1, P = +1, third = +1) at the same time — anti-commuting operators can't have both eigenvalue specifications simultaneously.

Of the 8 paths labeled by (Q-sign, P-sign, χ-sign): some pairs are inconsistent under anti-commutation. The "forbidden" structure isn't 1 path out of 8 — it's a 2-state subset that's anti-commutator-forbidden.

**v0.1 honest finding**: candidate (b) needs sharpening. The simple "1 path out of 8 forbidden" reading does NOT cleanly map to {Q̂, P̂_op} = 0 anti-commutation. Multi-week v0.2+ work to identify the actual substrate-mechanism.

## 4. Alternative mechanism candidates

Per v0.4 Section 6.3, multiple candidate mechanisms:

### 4.1 Candidate (a) — Pin(2) Z_2 chirality × N_c × {±1}

3 binary choices: γ̂⁵ × color-triad-choice × sign
- 2^3 = 8 paths
- Forbidden path: chirality-color-sign combination violating color-singlet requirement
- Substrate-mechanism: SU(3) color singlet requires antisymmetric combination; one of 8 combinations might be the symmetric (forbidden) state

Concrete: for 3-quark proton with N_c = 3 colors and 3 quarks, the color-singlet combination is 1/√6 · (RGB - RBG + ... ). Of 3! = 6 color permutations, ONE specific antisymmetric combination is the singlet. NOT 1 out of 8.

Doesn't fit cleanly either.

### 4.2 Candidate (c) — 3 spatial commitment directions × {forward, backward}

3D space commitment × {±} = 2^3 = 8 paths. Forbidden path: spatial parity-violating commitment? But parity is conserved in EM + strong.

Doesn't have substrate-mechanism for the 1/8 redistribution.

### 4.3 Candidate (d) — Tsirelson² - S²_BST factor decomposition

**This is potentially the cleanest reading**:

Tsirelson² = 2^g/2^(rank²) = 128/16 normalized = 8
S²_BST = (C_2 · N_c · g)/2^(rank²) = 126/16 normalized = 7.875
Deviation = (2^g - C_2 · N_c · g) / 2^(rank²) = 2/16 = 1/8

The "2" in the numerator IS the structural deviation:
- 2 = N_max - 1 - N_c · (g + rank) - ... NO, let me compute. 2^g - C_2·N_c·g = 128 - 126 = 2.
- 2 = 2 (trivial)
- Or: 2 = N_c - 1 = 3 - 1 = 2 (with N_c = 3) — this is the substrate's "off-by-N_c-minus-1" gap

Substantive structural reading: **substrate Bell-CHSH max is HUA-LOOK-NORMALIZED to be 2 units below the qubit-Tsirelson max**. The deviation is in the substrate-natural rank-1 projector restriction (only V_(0,0) accessible to B̂), which can't achieve the full 2-dim qubit Hilbert subspace required for Tsirelson saturation.

**Mechanism**: substrate has rank-1 access to Bell-CHSH eigenspace, NOT rank-2 (qubit) access. The 1-dim restriction reduces effective Bell value from Tsirelson to a substrate-natural maximum 2 units below (in normalized units 2^(rank²) = 16).

This is cleaner than the 8-sided die metaphor: **the substrate's 1/8 deviation is a 1-dim-vs-2-dim restriction**, not a 1-out-of-8 forbidden path.

The 8 in "8-sided die" might be a coincidence: 8 = 2^N_c = 2^3 and 1/8 = 1/2^N_c both contain 2^N_c factor, but they arise from different structural sources (paths vs deviation normalization).

## 5. v0.1 honest conclusion

**The structural identity Tsirelson² - S²_BST = 1/2^N_c = 1/8 is RIGOROUSLY CLOSED (T2399 STRUCTURALLY VERIFIED EXACT)**, but the **substrate-dynamical mechanism producing it remains FRAMEWORK-PLUS** (Cal #132 step 9 tier).

**Two readings** of the mechanism:

(I) **8-sided die candidate (b)**: 2^N_c = 8 commitment paths with one structurally forbidden via {Q̂, P̂_op} = 0 anti-commutation. **Cal #29 audit risk-flag**: doesn't cleanly map to 1-path-out-of-8 structure.

(II) **Rank-1 vs rank-2 substrate restriction (candidate d-revised)**: substrate Bell-CHSH operator is rank-1 projector onto V_(0,0) (T2399); CAN'T achieve qubit-Tsirelson which requires rank-2 access. The 2-unit normalized deviation (in 1/16 units) reflects substrate's rank-1 restriction. **Cleaner structural mechanism**.

**v0.1 disposition**: reading (II) is more substrate-natural and avoids the back-fit risk Cal #29 flagged for reading (I). v0.2+ multi-week formal derivation should pursue reading (II) and check whether the 8-path metaphor (reading I) corresponds to a structurally-distinct mechanism or is a coincidence.

## 6. Empirical discriminator (entropy vs constraint)

Per Casey 2026-05-26 AM directive (Track DC sub-question):

- **ENTROPY**: deviation environment-dependent; statistical fluctuation
- **CONSTRAINT**: deviation invariant; structural forbidden state

**SP-30-1 Vienna Bell test** measures Tsirelson² - S²_observed across multiple experimental configurations. Predictions:

- If reading (II) rank-1 substrate restriction holds: deviation = 1/8 EXACT and **invariant** across all configurations (substrate's Bell-CHSH operator is fixed; doesn't depend on apparatus details) — CONSTRAINT
- If reading (I) 8-sided die structurally forbidden state: deviation = 1/8 EXACT and **invariant** — CONSTRAINT (same prediction; experimentally indistinguishable from reading II without theoretical work)
- If thermal/statistical mechanism: deviation environment-dependent — ENTROPY

**Both reading (I) and (II) predict CONSTRAINT** (invariant 1/8 deviation). Distinguishing them requires explicit theoretical derivation, not just experiment.

## 7. Substantive multi-week derivation path (v0.2+)

### 7.1 Pursue reading (II) rank-1 substrate restriction

**Step 1**: derive substrate's rank-1 Bell-CHSH access from A_sub structure (V_(0,0) ground state projection per step 9 vacuum kicker).

**Step 2**: derive why substrate-rank-1 specifically produces 2-unit normalized deviation (in 1/16 units) below qubit-rank-2 Tsirelson.

**Step 3**: substrate-mechanism for why qubit-rank-2 Hilbert subspace is required for Tsirelson saturation, contrasted with substrate-rank-1 restriction.

**Step 4**: explicit derivation: |Tsirelson - S_BST| as quantitative consequence of rank restriction; compare 1/8 numerical value.

**Step 5**: rigorous derivation of EXACT identity 2^g - C_2·N_c·g = 2 from BST primary integer structure.

### 7.2 Verify reading (I) 8-sided-die has substrate-natural correspondence

Multi-week: enumerate all 8 paths in candidate (b.iv) {Q̂, P̂_op, third-generator} basis; identify whether {Q̂, P̂_op} = 0 anti-commutation eliminates EXACTLY ONE path; check if remaining 7 paths give the substrate-natural 1/8.

If yes: reading (I) is substrate-natural mechanism. If no: reading (I) is metaphorical, not structural.

### 7.3 Cal Thread 4 cold-read

Cold-read of Sections 4 + 5 mechanism candidates + Section 6 empirical discriminator. Type-check: rank-1 restriction (Type B algebraic) vs 8-path structure (potentially Type C level-crossing).

## 8. Honest scope (Cal #27 STANDING + Cal #29 STANDING)

**What's RIGOROUSLY CLOSED / SVC**:
- T2399 EXACT identity Tsirelson² - S²_BST = 1/2^N_c = 1/8 (STRUCTURALLY VERIFIED)
- {Q̂, P̂_op} = 0 (Cal #132 SVC)
- [B̂, T̂_tick] rank-1 vacuum kicker (Cal #132 FRAMEWORK-PLUS, step 9)

**What's FRAMEWORK-PLUS in v0.1**:
- Section 3 candidate (b) 8-sided die: structural setup but Cal #29 audit flag risk (doesn't cleanly map to {Q̂, P̂_op} = 0 anti-commutation)
- Section 4.3 candidate (d-revised) rank-1 substrate restriction: cleaner reading, multi-week explicit derivation needed

**What's INTERPRETIVE in v0.1**:
- Both readings (I) and (II) predict CONSTRAINT (invariant 1/8 deviation) — experimentally indistinguishable from each other at SP-30-1 Vienna level
- Step 1-5 multi-week derivation plan (Section 7.1)

**What's NOT in v0.1**:
- Explicit numerical derivation of 1/8 from substrate-mechanism (multi-week)
- Resolution of reading (I) vs reading (II) substrate-mechanism (multi-week)
- Explicit rank-1 restriction quantitative consequence (multi-week)

**Cal #27 STANDING reflexive trigger count**: 2 triggers (Section 4.3 reading (II) feels substrate-natural; Section 5 "rank-1 vs rank-2" structural reading). Both flagged INTERPRETIVE in honest scope.

**Cal #29 STANDING risk-flag**: candidate (b) 8-sided die mechanism has back-fit risk; v0.1 explicitly flagged. Reading (II) is offered as cleaner substrate-natural alternative without back-fit risk.

## 9. Coordination

**Cal**: Thread 4 cold-read on candidate (b) 8-sided die back-fit risk + reading (II) rank-1 restriction structural cleanness. Type-check on multi-week explicit derivation path.

**Elie**: Toy 3538+ candidate — Cal #29 question-shape pre-audit required. Explicit substrate-mechanism for 1/8 deviation could be tested via numerical computation of substrate Bell-CHSH matrix elements at higher cutoff (Phase B 45-66 nodes).

**Grace**: catalog cross-references for Bell-CHSH-related observables; SP-30-1 Vienna Bell test cross-link to Track DC mechanism candidates.

**Keeper**: integration; Vol 15 Ch 9 case study draft includes Track DC v0.1 framework status as substantive multi-week Lyra-lane work.

— Lyra, Track DC v0.1 Bell 1/8 explicit derivation framework filed Tuesday 2026-05-26 ~10:18 EDT per Casey all-tracks authorization + Keeper Option 1 sequencing. FRAMEWORK-PLUS (Cal #132 step 9 tier; multi-week explicit derivation pending). Substantive v0.1 finding: candidate (b) 8-sided die has Cal #29 STANDING audit back-fit risk; reading (II) rank-1 substrate restriction is cleaner substrate-natural mechanism. Both readings predict CONSTRAINT (invariant 1/8) per SP-30-1 Vienna empirical discriminator; theoretical distinction requires v0.2+ multi-week formal derivation. Cal #27 STANDING applied 2 reflexive triggers; Cal #29 STANDING risk-flag preserved through.
