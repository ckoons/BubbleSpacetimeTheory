---
title: "K40: T841 P(3) Erratum-Upgrade — c_2 vs C_2 Conflation Sweep"
author: "Keeper"
date: "2026-05-15"
audit_id: K40
verdict: ERRATUM (isolated; corrected identity is STRONGER than original claim)
overall_confidence: 95%
scope: "Toy 2255 finding (Elie): T841's P(3) = g·C_2 = 42 is wrong; correct identity is P(3) = g·c_2 = 77"
related: ["K38_Alpha137_Derivation_Chain_Audit.md", "BST_AC_Theorem_Registry.md (T841 entry)", "toy_2255_hilbert_Q5.py", "toy_910_exp_half_gap_closure.py"]
---

# K40: T841 P(3) Erratum-Upgrade

## Verdict: **ERRATUM, ISOLATED, UPGRADE**

T841's registry entry contains a single arithmetic error: `P(3) = g·C_2 = 42`. The correct identity is `P(3) = g·c_2 = 77`, where c_2 = 11 = rank·n_C + 1 is the second Chern class integer (distinct from C_2 = 6, the second Casimir / scalar Laplacian gap). The corrected identity uses **four** BST integers (g, rank, n_C, +1 unit) rather than two — this is a **strengthening**, not a weakening.

Contamination scope: isolated to T841's registry summary. **The Q⁵ Hilbert polynomial formula in Toy 910 line 255 is correct** — it just was not extended to test P(3) in its 8/8 PASS list. Other "42 = g·C_2" appearances in the corpus are in legitimately different contexts (θ-correspondence, eigenvalue product, mass formulas) where 42 = 7×6 is correct arithmetic for that identity.

## Origin

From Toy 2255 (Elie, 2026-05-15, 38/40):
- P(Q⁵, 1) = 7 = g ✓ (T841 claim correct)
- P(Q⁵, 2) = 27 = N_c³ ✓ (T841 claim correct, K38 load-bearing leg confirmed)
- P(Q⁵, 3) = 77 ≠ 42 (T841 claim wrong)

Elie's identification of the correct factorization:
$$P(Q^5, 3) = 77 = g \cdot c_2 = 7 \cdot 11 = 7 \cdot (\text{rank} \cdot n_C + 1)$$

where **c_2 = 11 is the second Chern class integer of Q⁵**, not C_2 = 6 (the second Casimir / scalar Laplacian gap on D_IV^5).

## c_2 vs C_2 — the disambiguation

These are two distinct BST integers that have shared the same notation in older docs:

| Symbol | Value | Meaning | Where |
|--------|-------|---------|-------|
| **c_2** | 11 | Second Chern class of Q⁵ = rank·n_C + 1 = 2-form Laplacian gap = dim K | T1484, T1788, T1790, T1791, T1794, T1726 |
| **C_2** | 6 | Second Casimir invariant = scalar Laplacian gap = χ(Q⁵) | T186, all BST core docs |

The distinction is **already correctly established** in newer theorems (T1484 Thirteen Theorem explicitly references "c_2·c_3 = 11·13 = 143 = N_max + C_2"; T1788 YM Ring Uniqueness writes "adjoint gap c_2/C_2 = 11/6"; T1790 Weitzenböck 2-Form Gap states "2-form Laplacian gap on Q⁵ is c_2 = 11, the second Chern class"; T1791 confirms "universal identity c_2 = dim K holds for all quadrics"; T1794 distinguishes "adjoint gap c_2 = 11 exceeds scalar gap C_2 = 6").

T841 (registered earlier — predates the c_2/C_2 disambiguation) used the symbol C_2 throughout its registry summary line, including a place where it should have written c_2. The arithmetic mistake was the inevitable consequence.

## Sweep results

### Confirmed-error files (need fix)

| File | Line | Current | Correct |
|------|------|---------|---------|
| `notes/BST_AC_Theorem_Registry.md` | 893 | `P(3)=g·C_2` | `P(3)=g·c_2 = 7·11 = 77` |

That is the entire confirmed-error scope. ONE entry in ONE file.

### Verified-correct files (no fix needed)

| File | Use of "42 = g·C_2" | Why correct |
|------|---------------------|-------------|
| `BST_22_Uniqueness_Conditions.md:61` | Condition 7 spectral product `d_1·λ_1 = g·(n+1) = 42` | This is the eigenvalue-multiplicity × eigenvalue product on Q⁵ (NOT the Hilbert polynomial value). Substituting n=5 gives 7×6 = 42. Correct identity for THIS quantity. |
| `BST_22_Uniqueness_Conditions.md:229` | Condition with `C_2 × g = 42 only at n=5` | Same product, level-rank duality framing. Correct arithmetic for the SO(7)₂ × Sp(6)₂ central charge product. |
| `notes/.running/grace_gf_product_theorem.md:36` | `42 = g · C_2 = 7 · 6. Matter-mode count.` | Number-theoretic "matter mode" decomposition. Arithmetic 42 = 7×6 is correct. |
| `play/toy_1318_arthur_packets_enumeration.py:237` | `theta_dim = g * C_2  # = 42` | θ-correspondence dimension of Sp(6) representation. Standard. Not Hilbert poly. |
| `play/toy_1857_dark_matter_wallach_shadow.py:164` | `m_DM = g * C_2 * m_e * π⁵ = 42 · π⁵ · m_e` | Mass formula using g·C_2 as a numerical coefficient. Different physical context. |
| `MESSAGES_2026-05-03:437` | "Hilbert-to-eigenvalue ratio P(1)/λ_1 = g/C_2" | This is P(1)=g over λ_1=C_2. P(1) = 7 (Q⁵ Hilbert) over C_2 = 6 (Casimir). Both readings consistent with Toy 2255. |

### Ambiguous (flagged for Lyra clarification)

`BST_22_Uniqueness_Conditions.md:61` includes the phrase: *"The value 42 is the dimension of the θ-correspondence representation of Sp(6) **and the Hilbert series evaluation P(1)**..."*

The "Hilbert series evaluation P(1)" sub-clause is ambiguous: if it refers to the Q⁵ Hilbert polynomial, **it is wrong** (P(Q⁵, 1) = 7, not 42, per Toy 2255). If it refers to a different Hilbert series (e.g., the Sp(6) θ-correspondence Hilbert series, which IS dimension 42 at the relevant degree), it is correct.

**Recommendation**: Lyra clarify the sub-clause to specify *which* Hilbert series, OR strike it as conflated wording. Severity: MINOR.

## Why this is an UPGRADE, not just a fix

T841 claimed: P(3) = g · C_2 = 7 · 6 = 42, using **two BST integers**.

Corrected identity: **P(3) = g · c_2 = g · (rank · n_C + 1) = 7 · (2·5 + 1) = 7 · 11 = 77**, using **four BST integers** plus a unit (g, rank, n_C, +1).

The corrected form binds more of the BST integer cascade into a single Hilbert polynomial value. It is also consistent with the structural pattern Lyra identified post-Toy 2255:

- **c_2 = rank · n_C + 1 = 11** (second Chern integer, the "+1" is genus correction at low degree)
- **N_max = N_c³ · n_C + rank = 137** (spectral cap, the "+rank" is genus correction at the maximal K-type level)

Same Hilbert-polynomial structure: coefficient × n_C + genus correction. This is the basis for Lyra's reframed A2 search — instead of looking for a single +rank derivation, look for the **family of shifts c_k = [coefficient_k]·n_C + [genus_correction_k]** that the Bergman kernel exponent on D_IV^5 generates, and read off rank at level k = N_c³.

The erratum is therefore not just an arithmetic fix — it surfaces a STRUCTURAL PATTERN that Lyra now has as a probe for A2.

## Actions

| # | Action | Owner | Status |
|---|--------|-------|--------|
| K40-1 | Fix T841 registry entry line 893: change `P(3)=g·C_2` to `P(3)=g·c_2` (= 77) | Keeper | THIS SESSION |
| K40-2 | Annotate T841 entry with K40 erratum reference | Keeper | THIS SESSION |
| K40-3 | Flag `BST_22_Uniqueness_Conditions.md:61` sub-clause for Lyra clarification | Lyra (when next on docs) | QUEUED |
| K40-4 | Tag Hilbert polynomial entries in `data/bst_geometric_invariants.json` with K40 reference (Hilbert_Q5_P3 should note T841 erratum) | Grace | DONE (per RUN_LIST T1.8) |
| K40-5 | Add c_2 vs C_2 disambiguation note to onboarding docs (CLAUDE.md or `bst_seed.md`) | Keeper or Grace | OPTIONAL |

## Implication for K38

K40 does NOT downgrade K38. The chain N_c³ leg rests on P(Q⁵, 2) = 27, verified by Toy 2255 independently of any T841 claim. K38 retains its A1-PASS upgrade.

K40 strengthens K38 indirectly: the c_2 = rank·n_C + 1 structural pattern is exactly the kind of "genus correction at a forced level" that Lyra needs to derive for the +rank step of K38 (A2). If A2 succeeds along that line, the K40 erratum will have surfaced the very mechanism that closes K38 external D-tier.

## Bottom line

T841 had a single arithmetic error inherited from pre-disambiguation c_2/C_2 notation. The correct identity is **stronger** than the original claim. Contamination is **isolated** to one registry entry. The fix produces a structural pattern that points the way to closing A2.

Erratum filed. K38 stands. Lyra's A2 has a new probe.

— Keeper, K40, 2026-05-15
