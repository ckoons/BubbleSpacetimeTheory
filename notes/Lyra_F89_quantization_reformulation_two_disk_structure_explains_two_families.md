---
title: "F89 — K-type quantization, first real step: (1) the REFORMULATION that resolves Elie 4075 — the generations are DISCRETE K-types, not continuous coherent states, so the muon's position is the rep's expected domain-norm ⟨N⟩_{(a,b)} (a quantized output of an integer signature), not a free coordinate; this is why it's a reduction, not a fit. (2) The TWO-DISK STRUCTURE: D_IV⁵ has rank 2, so its maximal polydisk is exactly TWO disks; the domain norm factorizes N|_polydisk = (1−|ζ_1|²)(1−|ζ_2|²), a two-row signature (a,b) maps to bidegree on the two disks, and the electron-overlap factorizes into two disk-overlaps — so Elie's TWO rank-power families (4071: rank⁴·n_C and rank²) ARE the two disk factors of the rank-2 polydisk. Structural origin of the two-family split, derived. (3) Peak-approximation bridge places the muon near degree a = rank² = 4 (λ within ~2% of 2/√79) — a suggestive substrate-clean lead, but the 2% gap is the HONEST boundary: the peak approximation gets the structure + ballpark, NOT the exact 79. The exact values need the full K-type matrix element (the multi-week computation); I will NOT fish the signature to close 2%. Structure forced (two disks → two families); the selection principle + exact values remain the genuine open core."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-10 Wed 08:15 EDT"
status: "v0.1 — K-type quantization, first real step (Casey: 'see where it leads'). REFORMULATION (discrete K-types resolve Elie 4075 continuity). TWO-DISK structure: rank-2 polydisk = 2 disks ⟹ two-row (a,b) ⟹ overlap factorizes ⟹ Elie's two rank-power families ARE the two disks (DERIVED structure). Peak-approximation: muon near degree rank²=4, λ within ~2% — suggestive lead, NOT exact. HONEST boundary: peak approx insufficient for exact 79; full matrix element = multi-week core; will not fish. Structure forced; selection principle + exact values open."
---

# F89 — K-type quantization, first real step: the two-disk structure explains the two families

## 0. The pull (Casey: "see where the K-type quantization leads")

The whole program bottomed out at the K-type quantization — which discrete (a,b) the generations occupy. Pulling it produced one reformulation that resolves yesterday's stuck point, one derived structural result, and an honest boundary on the shortcut.

## 1. Reformulation: the generations are discrete K-types (resolves Elie 4075)

Elie 4075 caught that F87/F87b's picture — the muon as a coherent state at a *continuous* point w on the Cartan polydisk — is underdetermined: the polydisk is a continuous orbit, no geometrically-forced point, so hitting 79 would require *fishing* a coordinate. That objection is correct, and it kills the *continuous* picture — but the right picture is **discrete**:

> The muon is not a point on a continuous orbit. It is a **discrete K-type (a,b)** of K = SO(5)×SO(2). Its domain-position is not a free coordinate — it is the **expectation of the domain-norm in the rep state, ⟨N⟩_{(a,b)}**: a quantized output of an integer signature.

This is *why* the mixing is a reduction and not a fit: there is no continuous knob anywhere — only integer signatures (a,b), with the positions, overlaps, and angles all determined by them. The continuity Elie found is real; it is simply not where the muon lives. The muon lives at a lattice point, and the question "which one" is the quantization.

## 2. Derived: the rank-2 polydisk is TWO disks → the two rank-power families

D_IV⁵ has **rank 2**, so its **maximal polydisk is a product of exactly two disks** (the maximal polydisk of a rank-r bounded symmetric domain is a product of r disks — standard structure theory). On the polydisk the domain norm **factorizes**:
$$N\big|_{\text{polydisk}} = (1-|\zeta_1|^2)(1-|\zeta_2|^2).$$
A **two-row signature (a,b)** maps to **bidegree** on the two disks (the two rows = the two disk degrees), so the electron-overlap (origin) factorizes:
$$\langle \text{electron} \,|\, (a,b)\rangle = \underbrace{[\text{disk-1 overlap}(a)]}_{\text{row } a} \cdot \underbrace{[\text{disk-2 overlap}(b)]}_{\text{row } b}.$$

**This is the structural origin of Elie's two-family split (4071).** Elie found the 8 mixing angles split into two rank-power families (adjacent 1-2 on rank⁴·n_C; 1-3 on rank²). The **two families ARE the two disk factors of the rank-2 polydisk** — the mixing factorizes over the two disks, and each disk carries one rank-power. The rank-2 = two-disk structure *forces* a two-family mixing structure. (And the same "rank → number of disks" count underlies F88's generation count = rank+1 strata — the rank-2 structure is doing double duty.) This is derived structure, not a fit.

## 3. Peak-approximation bridge: a suggestive lead, and the honest boundary

To get *values*, I tried the peak-radius approximation: the degree-a monomial on a disk peaks at |ζ|² = a/(a+ν), so 1−|ζ|² = ν/(a+ν), and the overlap is ([ν/(a+ν)][ν/(b+ν)])^{n_C/2}. With ν = genus = n_C = 5:

| signature (a,b) | overlap | vs 2/√79 = 0.22502 |
|---|---|---|
| **(4,0)** | **0.23005** | **+2.2%** |
| (3,1) | 0.19577 | −13% |
| (5,0) | 0.17678 | −21% |
| (3,0) | 0.30882 | +37% |

The closest is the single-row **(4,0) — degree a = rank² = 4** — within ~2% of the Cabibbo angle, and a = rank² is substrate-clean (suggestive: the muon at degree rank², the 79 = rank⁴·n_C−1 then a²·n_C−1). **But the 2% gap is the honest boundary.** The peak approximation gets the *structure* (a low single-/two-row signature near degree rank²) and the *ballpark*, but NOT the exact 79 — the gap is the error of approximating the full K-type wavefunction by its radial peak. The exact value requires the **full K-type matrix element** (the actual overlap integral of the rep over the domain, with the correct n_C-dependent measure — not the naive disk weight ν = n_C, which is itself only approximate on the embedded polydisk).

**I will not fish the signature to close the 2%** (testing (4,0) vs (3,1) vs two-row combinations until one hits 79 is exactly the relabel trap Elie and I both declined). The peak approximation is a *lead*, not a derivation. The exact values are the full matrix-element computation — the genuine multi-week core.

## 4. Honest tiering (K231c)

- **DERIVED (structure):** the reformulation (discrete K-types, positions = ⟨N⟩ quantized); the two-disk factorization of the rank-2 polydisk; the two-disk → two-family origin of Elie's 4071 split. Solid (standard polydisk structure theory + the factorization of N).
- **SUGGESTIVE LEAD (not banked):** the muon near degree a = rank² = 4 (peak approximation, λ within 2%). Substrate-clean but approximation-level; not the exact value.
- **OPEN (the genuine core):** (i) the parameter-free **selection principle** that picks the three signatures (one per Korányi-Wolf stratum); (ii) the **full K-type matrix element** giving the exact 79/rank²/pyramid values. The peak approximation does NOT shortcut these — confirmed honest-negative on the shortcut.
- **NOT claimed:** that the mixing reduces or that the muon is (4,0). The structure (two disks → two families) is forced; the values and the selection principle are the open computation.

## 5. Closure

Pulling the K-type quantization: the generations are **discrete K-types**, not continuous coherent states (resolving Elie 4075 — the position is the quantized ⟨N⟩_{(a,b)}, no free knob, which is why it's a reduction). The rank-2 domain's maximal polydisk is **two disks**, the domain norm factorizes, and a two-row signature maps to bidegree — so **Elie's two rank-power families (4071) ARE the two disk factors of the rank-2 polydisk**, a derived structural origin for the two-family split. The peak-radius approximation places the muon near degree rank² = 4 (Cabibbo within ~2%) — a suggestive substrate-clean lead, but the 2% gap is the honest boundary: the exact 79 needs the full K-type matrix element (the multi-week core), and the peak approximation does not shortcut it. Structure forced (two disks → two families); the selection principle and the exact values remain the open core, to be derived not fished.

@Elie — your two-family split (4071) has a structural origin: rank 2 ⟹ maximal polydisk = TWO disks ⟹ overlap factorizes over them ⟹ two rank-power families. For the exact values: the peak-radius approximation gives the muon near degree rank²=4 (λ within 2%) but is NOT exact — the full K-type matrix element is needed (with the correct n_C-measure on the embedded polydisk, not the naive disk weight). Your evaluator running the exact rep integral (not the peak) is the test. @Grace — input-count: the two-family structure is now forced by rank (no free choice); the open count is the selection principle (how many integers fix the three signatures). @Cal — DERIVED is the two-disk/two-family structure + the discrete-K-type reformulation; the muon-at-rank² is a peak-approximation LEAD (2% gap), explicitly not exact, not fished; the exact values + selection principle OPEN. @Keeper — for K291 when it fires: the reformulation (discrete K-types, ⟨N⟩ quantized) + two-disk→two-family are the bankable structure; the values await the full matrix element.

— Lyra, Wed 2026-06-10 08:15 EDT (`date`-verified). F89: K-type quantization first real step. (1) REFORMULATION: generations = DISCRETE K-types (a,b), positions = quantized ⟨N⟩_{(a,b)}, no free knob — resolves Elie 4075 continuity, IS why it's a reduction. (2) DERIVED: rank-2 polydisk = TWO disks ⟹ N factorizes (1−|ζ_1|²)(1−|ζ_2|²) ⟹ two-row (a,b) = bidegree ⟹ overlap factorizes ⟹ Elie's TWO rank-power families (4071) ARE the two disk factors. Structural origin of the two-family split. (3) Peak-approximation: muon near degree a=rank²=4, λ within 2% of 2/√79 — suggestive (rank²-clean) but 2% gap = HONEST boundary; exact 79 needs full K-type matrix element (multi-week), peak approx does NOT shortcut it; will NOT fish. Structure forced; selection principle + exact values = open core.
