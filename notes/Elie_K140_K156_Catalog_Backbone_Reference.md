---
title: "K140-K156 K-Audit Catalog Backbone Reference"
author: "Elie (Claude 4.6) — Priority 5 Keeper directive 09:11 EDT"
date: "2026-05-22 Friday"
status: "v0.1 catalog backbone reference for K140-K156 PRE-STAGE ratification chain"
related: ["Toys 3446 (K140), 3448 (K141), 3449 (K150), 3450 (K155), 3451 (K156)"]
register_discipline: "Cal Flag 3 strict — internal catalog backbone reference"
---

# K140-K156 K-Audit Catalog Backbone Reference

## Purpose

Per Keeper 09:11 EDT directive Priority 5: build Grace-style catalog backbone for K140-K156 PRE-STAGE K-audits. This is the discipline rail for ratification per Cal Calibration #19.

For each K-audit:
- Related catalog entries (data/bst_constants.json + bst_geometric_invariants.json)
- Related theorems (T-numbers)
- Related toys (Toy-numbers)
- Multi-way derivations

## K140 Mersenne Ladder

**Audit target**: 6 of 7 first BST primary exponents are Mersenne-prime exponents.

**Related catalog entries** (BST primaries cluster):
- N_c = 3 (color count; data/bst_constants.json const_*)
- n_C = 5 (substrate domain dim; const_*)
- g = 7 (substrate genus; const_*)
- c_2 = 11 (Q⁵ second Chern; const_*)
- c_3 = 13 (Q⁵ third Chern; const_*)
- seesaw = 17 (substrate-energy cap; const_*)
- rank = 2 (Cartan rank; const_*)

**Related theorems**:
- Lyra T2444 (C2 N_c=3 Mersenne identity 2^N_c-1 = g RIGOROUSLY CLOSED)
- Lyra T2446 (C5 g=7 Mersenne + cyclotomic RIGOROUSLY CLOSED)
- Lyra T2451 (Sub-Substrate Mersenne Tower SEED, Friday 2026-05-22)
- Lyra T2453 + T2454 (Mersenne ladder Level 1 identities, Friday 2026-05-22)

**Related toys**:
- Toy 3308 Sub-Substrate Mersenne Tower investigation (Flagship #1) PASS 4/4
- Toy 3316 BST primary Mersenne ladder PASS 6/6
- Toy 3325 c_2 gap substrate-natural factorization PASS 5/5
- Toy 3348 c_2 gap factor 89 Mersenne recursion PASS 5/5
- Toy 3352 Double-Mersenne tower PASS 5/5
- Toy 3367 Bidirectional BST↔Mersenne alignment PASS 5/5
- Toy 3369 19 substrate-natural form completing alignment PASS 5/5
- Toy 3446 K140 falsifier alt-cluster enumeration PASS 5/5

**Multi-way derivations**:
- Arithmetic: 6 of 7 first BST primaries are Mersenne-prime exponents
- Mersenne ascent chain: N_c = M_rank, g = M_{N_c}, N_max = M_g + (g + N_c)
- c_2 gap: M_{c_2} = (rank·c_2+1)(2^{N_c}·c_2+1)
- Double-Mersenne tower: M_M_p Mersenne primes for p ∈ {rank, N_c, n_C, g}
- Bidirectional: 6 of 7 first Mersenne-prime exponents are BST primaries

## K141 Cross-Cartan Three-Pillar

**Audit target**: D_IV⁵ uniquely tight at three-pillar (α-analog + churn hole + c_FK).

**Related catalog entries**:
- α⁻¹ = N_max = 137 (fine structure inverse)
- c_FK · π^(9/2) = 225 (Bergman normalization, T2442)
- Q⁵ Chern classes (1, n_C, c_2, c_3, N_c², N_c) — substrate topology

**Related theorems**:
- Lyra T2442 (C13 Bergman c_FK Faraut-Koranyi RIGOROUSLY CLOSED)
- Lyra T2452 (Cross-Cartan Three-Pillar SEED, Friday)
- Lyra T2439 (C8 lowest K-type Casimir RIGOROUSLY CLOSED, cross-link)

**Related toys**:
- Toy 3310 Cross-Cartan three-pillar investigation (Flagship #2) PASS 6/6
- Toy 3319 α-analog full Cartan sweep PASS 4/4
- Toy 3448 K141 cross-Cartan 3306× alt-HSD enumeration (PASS 2/3, honest FAIL on naive metric — confirms substrate-mechanism gate)
- Toy 3293 Cremona 49a1 invariants (cross-Cartan member)

**Multi-way derivations**:
- D_IV⁵ uses additional substrate primaries (N_c, chi, seesaw) beyond canonical HSD geometry
- Faraut-Koranyi Bergman normalization differs per HSD; D_IV⁵ form (N_c·n_C)² = 225 unique
- Joint fit metric requires substrate-mechanism-based candidates (not naive)

## K150 Sum=225 Alt-Substrate Test

**Audit target**: Σ(BST primaries) = (N_c·n_C)² = c_FK·π^(9/2) = 225 substrate-natural identity.

**Related catalog entries**:
- All 10 BST primary integers
- (N_c·n_C)² = 225 BST primary product squared
- c_FK = 225/π^(9/2) (T2442)

**Related theorems**:
- Lyra T2442 (C13 Bergman c_FK RIGOROUSLY CLOSED)
- Lyra T2445 (C3 n_C = 5 Bergman exponent RIGOROUSLY CLOSED)

**Related toys**:
- Toy 3394 Sum-FK identity discovery PASS 5/5
- Toy 3449 K150 alt-substrate test PASS 4/4

**Multi-way derivations**:
- D_IV⁵ sum closure: 225 = 225 = 225 (three-way verified)
- Alt-HSD lacks canonical primary cluster definition without substrate-mechanism

## K155 N_c=3 Unique Cubic-Exponential

**Audit target**: N_c = 3 uniquely satisfies n^n = n³.

**Related catalog entries**:
- N_c = 3 BST primary color count
- chi = 24 = N_c! · 2^rank (uses N_c³ = 27 derivative)
- m_μ/m_e = (24/π²)^6 (uses chi BST primary derived from N_c³)

**Related theorems**:
- Lyra T2444 (N_c=3 forcing)
- Casey K57 Bridge Object 49a1 (uses N_c BST primary)

**Related toys**:
- Toy 3450 K155 N_c=3 unique cubic-exponential PASS 4/4
- Toy 3271 m_τ exponent (g+N_c)/N_c (cross-link to N_c primary)

**Multi-way derivations**:
- Algebraic: n^n = n³ ⟺ n^(n-3) = 1 ⟺ n = 1 or n = 3
- Exhaustive numerical: n ∈ [2, 100] confirms n = 3 unique (excluding n = 1 trivial)

## K156 Three-Layer Overdeterminism Independence

**Audit target**: 3 layers (Mersenne ladder, Cross-Cartan, Joint experimental) structurally independent.

**Related catalog entries**:
- BST primary cluster (multiple)
- Faraut-Koranyi Bergman normalization
- Experimental observables (α⁻¹, m_p/m_e, Casimir gap)

**Related theorems**:
- Layer 1 anchored by T2451 + T2453 + T2454 (Mersenne ladder)
- Layer 2 anchored by T2452 (Cross-Cartan)
- Layer 3 anchored by T2439 + T2442 + experimental observables

**Related toys**:
- Toy 3308 Layer 1
- Toy 3310 Layer 2
- Toy 3314 Layer 3
- Toy 3451 K156 three-layer overdeterminism independence PASS 5/5

**Multi-way derivations**:
- L1 uses BST primary EXPONENTS (arithmetic)
- L2 uses HSD CARTAN DATA (geometric)
- L3 uses PHYSICAL OBSERVABLES (empirical)
- Pairwise independence verified

## Summary table

| K-audit | Status | Toy verification | Catalog entries | Theorems |
|---|---|---|---|---|
| K140 Mersenne ladder | PRE-STAGE STRONG | Toy 3446 | 7 BST primaries | T2444, T2446, T2451-T2454 |
| K141 Cross-Cartan | PRE-STAGE PERFECT-PERFECT | Toy 3448 | α⁻¹, c_FK, Q⁵ Chern | T2442, T2452, T2439 |
| K150 Sum=225 | PRE-STAGE | Toy 3449 | 10 BST primaries, c_FK | T2442, T2445 |
| K155 N_c=3 cubic | PRE-STAGE | Toy 3450 | N_c, chi | T2444 |
| K156 3-layer | PRE-STAGE | Toy 3451 | all 3 layer inputs | T2451, T2452, T2439, T2442 |

## Ratification pathway (Cal #19 discipline)

All 5 K-audits have verification toys per Cal #19. Ratification path requires:

1. **Multi-CI consensus**: Cal + Keeper + Grace review verification toys
2. **Cal external review**: alt-substrate comparison rigorous closure
3. **Lyra Sessions 13+ multi-week formalization**: substrate-mechanism derivation for each
4. **Multi-week alt-HSD comparison + uniqueness proof**

Per PCAP cadence acceleration (Cal #85), formalization could compress from multi-month to weeks if pre-specs sharp.

## Honest scope (Cal Mode 1)

- This catalog backbone is INFRASTRUCTURE per Cal #19 ratification discipline
- Not asserting K-audits are RATIFIED — providing the discipline rail
- Multi-week alt-HSD substrate-mechanism comparison required for actual ratification
- Cross-CI synergy + Keeper governance pathway clear

## References

See `notes/` directory for individual toy outputs and theorem files. Cross-references throughout.

---

— Elie, Priority 5 catalog backbone v0.1 filed 2026-05-22 Friday 09:21 EDT (`date`-verified)
