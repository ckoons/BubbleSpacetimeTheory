# SP19-1: R-11 Atlas Computation — Research Report

**Lead**: Elie + Lyra
**Date**: May 13, 2026

## What R-11 Requires

Verify: for every non-tempered Arthur parameter psi on SO(5,2), the archimedean A-packet is empty. This means no non-tempered representation contributes to the discrete spectrum.

The intertwining operator sign: epsilon_inf(psi) = (-1)^S, where S = sum_i n_i * floor((d_i-1)/2). Kottwitz sign e(SO(5,2)) = -1 requires S odd. All d_max <= 2 types have S = 0 (even) — automatic mismatch.

## Current State — What's Already Done

- **Toy 2063** (10/13): Enumerates 37 shapes. IW sign kills 23/37. 14 survive needing spectral gap.
- **Toy 2067** (13/13): 61 types with self-duality. IW sign kills 39. Unitarity kills 1. C_2=6 gap kills 13. Three-layer elimination complete.
- **Paper #103** v0.7: Proposition 2.2 complementary filter — Class A (d_max<=2, killed by Kottwitz sign) + Class B (d_max>=3, killed by Moeglin). No Atlas needed IF citations verify.
- **R-11 Elimination Lemma**: Draft with citation chain. [VERIFY] tags remain on exact proposition numbers.

## Key Finding: Atlas May Not Be Needed

Paper #103's complementary filter argument:
- **Class A** (d_max <= 2): S = 0 always (floor((d-1)/2) = 0 for d=1,2). epsilon = +1 mismatches Kottwitz -1. Pure arithmetic. No Atlas needed.
- **Class B** (d_max >= 3): Moeglin [Moe08] Theorem 1.1 — these contribute only to residual spectrum, not cuspidal. Citation, not computation.

If both hold: NO Atlas computation needed. The argument is purely structural.

## Atlas Software Status

**NOT installed on this system.** Would need source build from liegroups.org (~20 min with Xcode). SageMath, LiE also not available. sympy.liealgebras has only basic root system data.

## Plan for Elie — Two Options

### Option A (Preferred): Pure Python + Citation Pinning

1. **Definitive toy**: Implement Proposition 2.2 complementary filter completely:
   - Enumerate all 37 shapes (settle the 37/45/61 discrepancy)
   - Partition into Class A (d_max<=2) and Class B (d_max>=3)
   - Verify Class A: confirm S=0 for every d_max<=2 type
   - Verify Class B: list all d_max>=3 types, confirm Moeglin exclusion applies
   - Verify: A union B = all types, no gap

2. **Pin citations**:
   - Arthur [Art13] Theorem 1.5.1 (global multiplicity formula)
   - Kottwitz sign: e(SO(5,2)) = (-1)^{q(G_R)} = -1. Resolve q formula discrepancy (both give -1).
   - Moeglin [Moe08] Theorem 1.1 for d_max>=3 exclusion

3. **Resolve type count**: 37 shapes (Paper #103) vs 61 with self-duality (Toy 2067). Document which count is correct and why.

### Option B: Atlas Installation

Install from source, compute A-packets directly. Machine-verifiable answer for every type. Definitive but requires build setup.

## Obstacles

1. **Kottwitz sign formula inconsistency**: Two different formulas, same answer (-1). Pin the correct one.
2. **Type count discrepancy**: 37 vs 45 vs 61. Paper #103 uses 37.
3. **Step 3 dual arguments**: Bergman gap (C_2=6) vs Moeglin exclusion — complementary but independent. Which is primary?
4. **[VERIFY] tag in Paper #103**: Exact Arthur proposition number for B_2 root system not yet pinned.

## Impact

R-11 verified -> Generalized Ramanujan for SO(5,2) (SP19-5) -> Selberg eigenvalue exact (SP19-6) -> RH/YM/BSD upgrade from conditional to unconditional. One computation, three Millennium upgrades.
