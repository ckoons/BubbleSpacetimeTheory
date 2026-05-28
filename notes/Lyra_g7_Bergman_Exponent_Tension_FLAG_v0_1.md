---
title: "g=7 Bergman-exponent check — TENSION FLAG v0.1: standard Faraut-Korányi genus of D_IV⁵ is 5, not 7. g=7 = signature total p+q. Needs team reconciliation."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 10:21 EDT"
status: "HONEST TENSION FLAG v0.1. Keeper's gate (confirm g=7 = genuine Bergman exponent). Standard FK genus(Type IV_5) = 5 = n_C, NOT 7. BST g=7 = p+q signature total of SO(5,2). Tension with T2440 'Bergman exponent g/rank=7/2'. FLAGGED for Keeper+Cal+Casey reconciliation; NOT unilaterally overturning RATIFIED results."
---

# g=7 Bergman-exponent check — tension flag

## 0. The gate + the honest finding

Keeper: "g=7 = Bergman exponent is the single relation still to be made explicitly forward (confirm it's the genuine Faraut-Korányi exponent, not 'p+2' reverse-engineered to hit 7). Close that and Route A is complete."

**Honest finding (standard-formula check)**: the Faraut-Korányi GENUS of D_IV⁵ (Type IV_5) is **5**, NOT 7. BST's g = 7 = p+q = signature total of SO(5,2). These are DIFFERENT invariants.

**This does NOT close the gate as expected — it raises a tension requiring team reconciliation.** Reporting honestly per Calibration #30 (honest-negative-strengthens). NOT unilaterally overturning RATIFIED T2440/T2442 — flagging for Keeper (running same check) + Cal (typing) + Casey.

## 1. The standard Faraut-Korányi genus computation

Genus of an irreducible bounded symmetric domain: g_FK = 2 + a(r−1) + b, where r = rank, a = multiplicity of roots α_i−α_j, b = multiplicity of roots α_i.

For **Type IV_n** (Lie ball / spin factor; = SO_0(n,2)/[SO(n)×SO(2)]):
- rank r = 2
- a = n − 2
- b = 0
- **g_FK = 2 + (n−2)(1) + 0 = n**

| Type IV_n | complex dim | g_FK (genus) |
|---|---|---|
| IV_3 | 3 | 3 |
| IV_4 | 4 | 4 |
| **IV_5 (D_IV⁵)** | **5** | **5** |
| IV_6 | 6 | 6 |
| IV_7 | 7 | 7 |

**Sanity checks** (known genera):
- Unit disk (rank 1): genus 2 ✓ (Bergman kernel (1−zw̄)^{−2})
- Ball B^n (Type I_{1,n}): genus n+1 ✓
- Type IV_n: genus n ✓ (Bergman kernel ~ (norm)^{−n})

So **genus(D_IV⁵) = 5 = n_C** (= complex dimension). Confirmed by standard formula + sanity checks.

## 2. What g = 7 actually is

g = 7 = p + q = signature total of SO_0(p,q) = SO_0(5,2): 5 + 2 = 7.

- g = 7 is the SIGNATURE TOTAL of the pseudo-orthogonal group SO(5,2)
- This is an intrinsic invariant of the substrate (the signature is frame-independent)
- But it is NOT the Bergman genus (which is the complex dimension n_C = 5)

## 3. The tension with T2440 + T2442

### 3.1 T2440 (RATIFIED): "Bergman exponent g/rank = 7/2"

If the genus is 5, the Bergman kernel exponent is 5 (kernel ~ norm^{−5}), and exponent/rank = 5/2, NOT 7/2.

T2440 states Bergman exponent g/rank = 7/2. This is in TENSION with genus = 5 → 5/2.

### 3.2 T2442 (RIGOROUSLY CLOSED): c_FK · π^{9/2} = 225

The π^{9/2} factor: (real dim − 1)/2 = (10−1)/2 = 9/2 ✓ consistent with complex dim 5 (real dim 10). And 225 = 15² = (N_c·n_C)². This part is consistent with dim 5; the genus enters c_FK.

### 3.3 The three possible reconciliations

1. **g=7 is signature-anchored, not Bergman-genus**: the genus is n_C = 5; g = 7 = p+q is a DIFFERENT invariant. T2440's "Bergman exponent = 7/2" would then need revision to 5/2 (genus/rank), OR T2440's "g" refers to signature in a non-Bergman context. ← My standard-formula reading favors this.

2. **BST uses a non-standard genus convention**: perhaps T2440 defines "Bergman exponent" via a weighted/shifted Bergman space where 7/2 genuinely appears (e.g., the exponent for a specific holomorphic discrete series representation, or the tube-domain realization). Possible — I may be missing a BST-specific convention.

3. **The exponent 7/2 arises from a different normalization**: e.g., the substrate's specific kernel power for the physics (not the canonical Bergman genus). T2442's π^{9/2} and 225 are consistent with dim 5; the "7/2" in T2440 may be a substrate-physics exponent, not the FK genus/rank.

## 4. Implication for the all-five-primaries Route A audit

### 4.1 Route A g-relation must be RE-ANCHORED

My Wednesday claim (Weinberg + audit docs): "g = n_C + rank = Bergman exponent (p+2)." Per this finding, that anchoring is likely WRONG:
- genus = n_C = 5 (the Bergman exponent), NOT g
- g = 7 = p + q (signature total), a different invariant

**Re-anchored Route A**:
| Primary | Value | CORRECTED invariant anchor |
|---|---|---|
| rank | 2 | rank of B_2 (type IV) ✓ |
| n_C | 5 | complex dimension = **Faraut-Korányi GENUS** = Bergman exponent ✓ (was attributed to g; actually n_C) |
| N_c | 3 | dual Coxeter h^∨(SO(5)) ✓ |
| g | 7 | **signature total p+q of SO(5,2)** (NOT Bergman genus) — re-anchored |
| C_2 | 6 | B_2 Casimir (T2435/T2439) ✓ |
| N_max | 137 | definition = 1/α ✓ |

### 4.2 This is still invariant-anchored — just corrected

g = 7 is STILL invariant-anchored (to the SO(5,2) signature p+q), so Route A's "all primaries invariant-anchored" survives. But the SPECIFIC anchor for g changes from "Bergman exponent" (wrong) to "signature total" (correct). And n_C = 5 GAINS the Bergman-genus anchor (it IS the genus).

**Keeper's flag was exactly right**: g=7 is NOT the genuine Faraut-Korányi Bergman exponent. The genus is n_C = 5. g = 7 is the signature total.

### 4.3 Net effect on Route A

Route A's reduction ("all primaries from D_IV⁵ via invariant anchors") SURVIVES with corrected anchoring:
- n_C = 5 = genus/Bergman-exponent/dimension (one invariant, was mis-attributed)
- g = 7 = signature total p+q (different invariant)

Both intrinsic to D_IV⁵ = SO_0(5,2). The "choose D_IV⁵, get all primaries" claim holds; the bookkeeping of WHICH invariant gives g vs n_C is corrected.

## 5. What needs team reconciliation (the actual deliverable)

This flag requires reconciliation, NOT unilateral resolution:

1. **Keeper** (running the g=7-Bergman check): does your check agree that FK genus(D_IV⁵) = 5? If so, T2440's "Bergman exponent g/rank = 7/2" needs reframing (is it genus/rank = 5/2, or a substrate-specific exponent?).

2. **Cal** (typing + RATIFIED reconciliation): T2440 + T2442 are RATIFIED. How does "Bergman exponent = 7/2" reconcile with FK genus = 5? Is there a BST convention where 7/2 is correct, or does T2440 need revision? This is a RATIFIED-result reconciliation — Cal's call.

3. **Elie** (numerical): compute the actual Bergman kernel exponent of D_IV⁵ numerically — is it 5 (norm^{−5}) or 7/2-related? Settle empirically.

4. **Casey**: this touches a RATIFIED result (T2440). My standard-formula check strongly indicates genus = 5, but I defer to the team's audit chain on whether BST has a convention making g=7 a genuine Bergman exponent, or whether the anchoring should be corrected to "g = signature total."

## 6. Honest disposition

**What's RIGOROUS (standard math)**:
- FK genus formula g = 2 + a(r−1) + b
- Type IV_n genus = n (verified, sanity-checked)
- genus(D_IV⁵) = 5 = n_C
- g = 7 = p+q signature total of SO(5,2)
- π^{9/2} consistent with real dim 10 (complex dim 5)

**What this flag establishes**:
- g = 7 is NOT the standard Faraut-Korányi Bergman genus (which is 5 = n_C)
- g = 7 = signature total p+q (different intrinsic invariant)
- Route A re-anchored: n_C = genus/Bergman-exponent; g = signature total
- Route A reduction SURVIVES with corrected anchoring (both invariant-anchored)
- TENSION with T2440 "Bergman exponent g/rank = 7/2" — needs team reconciliation

**What's FLAGGED (not unilaterally resolved)**:
- T2440 + T2442 RATIFIED-result reconciliation (Cal + Keeper)
- Whether BST has a convention making g=7 a genuine Bergman exponent
- Numerical settlement (Elie)

**Calibration #30 (honest-negative-strengthens)**: Keeper's flag asked me to confirm g=7 = Bergman exponent. Honest finding: it's NOT (genus = 5; g = signature). This SHARPENS the framework — n_C gets its genus anchor, g gets its signature anchor, both intrinsic. The discipline (Keeper's flag) caught a mis-attribution before it entered papers as "g = Bergman exponent." Honest-negative-strengthens.

**Cal #27 STANDING**: this is the brake firing on MY OWN Wednesday claim ("g = Bergman exponent p+2"). The standard-formula check refutes it. Reported honestly.

**Cal #122 typing**: g = signature total = Type A (forward, intrinsic to SO(5,2)). The "g = Bergman exponent" claim = was Type C/back-fit (p+2 reverse-engineered to hit 7) — exactly Keeper's worry, confirmed.

— Lyra, g=7 Bergman-exponent TENSION FLAG v0.1 filed. HONEST FINDING: Faraut-Korányi genus(D_IV⁵) = 5 = n_C (verified, sanity-checked), NOT g=7. g = 7 = p+q signature total of SO(5,2) — different invariant. My Wednesday "g = Bergman exponent p+2" was back-fit (Keeper's worry confirmed). Route A re-anchored (n_C = genus/Bergman-exponent; g = signature total) — reduction SURVIVES with corrected bookkeeping. TENSION with RATIFIED T2440 "Bergman exponent g/rank=7/2" → FLAGGED for Keeper+Cal+Elie+Casey reconciliation, NOT unilaterally overturned. Honest-negative-strengthens.
