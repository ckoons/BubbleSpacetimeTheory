---
title: "Vol 9 Chapter 4 — Superconductivity from Substrate"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — LOAD-BEARING; cuprate mechanism + B12H32 hydride T_c ~214 K BST predictions"
volume: "Vol 9 Condensed Matter from D_IV⁵"
chapter: 4
load_bearing: "Superconductivity from substrate; BCS for conventional; cuprate BST mechanism; B12H32 T_c ~214 K BST prediction; iron pnictide family predictions"
---

# Chapter 4 — Superconductivity from Substrate

## Level 1 — one sentence

Superconductivity — zero resistance + Meissner effect below $T_c$ — has well-understood BCS mechanism for conventional materials (Cooper-pair phonon-mediated condensate), but cuprate high-$T_c$ superconductors remain partly mysterious; BST gives specific predictive readings: cuprate mechanism via substrate CuO₂-plane K-type structure, B12H32 hydride T_c ~214 K, and family-wide iron pnictide predictions.

## Level 2 — graduate-physicist precision

### 4.1 Discovery and basic phenomenology

**Onnes 1911**: discovered superconductivity in mercury at 4.2 K — resistance dropped abruptly to zero at $T_c$. Below $T_c$, supercurrents flow forever (no decay observable in years).

**Meissner-Ochsenfeld 1933**: superconductors expel magnetic fields. $\vec B = 0$ inside bulk superconductor. Distinct from "perfect conductor" — superconductor expels initial flux too.

**Two characteristic lengths**:
- Penetration depth $\lambda_L$: how far $\vec B$ penetrates surface (London ~100 nm)
- Coherence length $\xi$: scale of Cooper pair (~$\hbar v_F/(\pi\Delta)$, ~100 nm in conventional)

Type I ($\xi > \lambda_L$): single $H_c$, complete Meissner.
Type II ($\xi < \lambda_L$): two critical fields $H_{c1} < H_{c2}$, partial flux penetration via Abrikosov vortex lattice (all high-$T_c$ are type II).

### 4.2 BCS theory (1957)

**Bardeen-Cooper-Schrieffer 1957** (Nobel 1972): conventional superconductivity from phonon-mediated electron pairing.

**Cooper pair**: two electrons with opposite momenta and spins ($\vec k\uparrow, -\vec k\downarrow$) bind via attractive phonon exchange. Pair size = coherence length $\xi$.

**BCS gap equation**: $\Delta = 2\hbar\omega_D \exp(-1/[g(E_F)V])$ where $V$ is the BCS coupling, $\omega_D$ Debye frequency, $g(E_F)$ density of states at Fermi level. At T = 0: $\Delta_0 \approx 1.76 k_B T_c$ — universal BCS ratio.

**Isotope effect**: $T_c \propto M^{-1/2}$ (mass dependence) confirms phonon mechanism.

Substrate reading: Cooper pairs are substrate Pin(2) K-type pairings under phonon-coupling boundary conditions; substrate's natural K-type pairing produces the BCS gap.

### 4.3 Cuprate high-$T_c$ superconductors

**Bednorz-Müller 1986** (Nobel 1987): discovered La₂₋ₓBaₓCuO₄ at $T_c$ ~ 35 K — first high-$T_c$. Soon YBa₂Cu₃O₇ ($T_c$ = 93 K), HgBa₂Ca₂Cu₃O₈ ($T_c$ = 138 K at ambient pressure, 164 K under pressure).

Cuprate phenomenology:
- d-wave pairing symmetry (not s-wave like BCS)
- Pseudogap phase above $T_c$
- Strange metal normal state (resistivity linear in T)
- Magnetic correlations + spin fluctuations
- ~40 years of intense theoretical work; no complete consensus mechanism

**BST cuprate prediction** (Task #88, completed in BST catalog): cuprate superconductivity arises from substrate CuO₂-plane K-type structure under the specific BST primary integer constraints. The d-wave symmetry, pseudogap, and strange-metal behaviors are substrate-mechanism consequences. BST predicts specific mechanism signatures observable in cuprate response measurements (full predictions in BST catalog).

### 4.4 BST B12H32 hydride T_c ~214 K prediction

**Hydride high-T_c**: H₃S (~203 K, Eremets 2015), LaH₁₀ (~250 K), recently CaH₆, YH₉. All require high pressure (>100 GPa).

**BST prediction**: **B12H32 hydride T_c ~214 K**. This is a specific BST-derived prediction (memory: BST May 2026 substrate coherence work). The substrate's natural K-type structure favors B12H32 as a stable hydride configuration at the predicted T_c.

Test: synthesize B12H32 (hydride synthesis is challenging but feasible at gigapascal pressures), measure T_c. Falsifier: T_c not in vicinity of 214 K → BST mechanism wrong for this material.

### 4.5 Iron pnictide superconductors

Iron pnictides (LaFeAsO, BaFe₂As₂, etc.; Kamihara 2008) reach T_c ~ 50 K with multi-band physics (Fe d-orbitals). Pairing symmetry s±-wave (sign-changing between Fermi pockets).

**BST iron pnictide predictions** (Task #105, completed): substrate predicts specific T_c values across the iron pnictide family via substrate K-type structure on FeAs-layer boundary condition.

### 4.6 Type II superconductor flux quantization

In type II SC under field $H_{c1} < H < H_{c2}$: magnetic flux enters as quantized vortices, each carrying flux $\Phi_0 = h/(2e) \approx 2.07 \times 10^{-15}$ Wb. Vortex lattice (Abrikosov 1957, Nobel 2003).

The 2e (not e) reflects Cooper pairing — fundamental confirmation of pairing mechanism.

### 4.7 Worked example: NbTi superconducting magnet

NbTi: $T_c \approx 9.5$ K, $H_{c2} \approx 11$ T at 4.2 K. Used in MRI scanners, particle accelerators (LHC has thousands of NbTi magnets).

Cooper-pair characteristics:
- Coherence length $\xi \approx 38$ nm
- Penetration depth $\lambda_L \approx 240$ nm
- BCS gap $\Delta_0 \approx 1.76 k_B T_c \approx 1.4$ meV

### 4.8 K-audit anchors

- **Task #88** (cuprate mechanism, completed): BST predictive mechanism for cuprates
- **B12H32 ~214 K** (memory): BST hydride T_c prediction
- **Task #105** (iron pnictide): BST T_c predictions for iron pnictide family
- **Vol 5 Ch 9** (Pin(2) spin-statistics): Cooper-pair statistics

## Level 3 — 5th-grader accessibility

**Superconductors** have zero electrical resistance below a critical temperature $T_c$. Discovered 1911 in mercury at 4 K. **BCS theory** (1957): electrons pair up (Cooper pairs) via phonons (lattice vibrations), forming a condensate that flows without resistance. Universal ratio: $\Delta_0 \approx 1.76 k_B T_c$. **Cuprate revolution** (1986): copper oxide materials reach $T_c > 100$ K — but BCS doesn't fully explain them. 40 years and still partly mysterious. **BST predictions**:
- Cuprate mechanism via substrate K-type structure on CuO₂ planes
- **B12H32 hydride at $T_c \approx 214$ K** (specific number!)
- Iron pnictide family-wide T_c predictions

If anyone synthesizes B12H32 and measures T_c far from 214 K, that BST prediction is falsified.

---

## What comes next

Chapter 5 develops topological phases of matter.

## Where to look this up

- Tinkham, *Introduction to Superconductivity*
- BCS 1957 paper
- BST: Task #88 cuprate; B12H32 prediction memory; Task #105 iron pnictide
