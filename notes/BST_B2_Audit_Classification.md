# B₂ → B₂ Root System Correction Audit

**Date:** April 24, 2026
**Author:** Keeper
**Status:** IN PROGRESS

---

## The Correction

SO₀(5,2) has restricted root system **B₂** (reduced), NOT **B₂** (non-reduced).

| Property | B₂ (CORRECT) | B₂ (WRONG) |
|----------|-------------|-------------|
| Short roots ±eᵢ | mult 3 | mult 3 |
| Long roots ±eᵢ±eⱼ | mult 1 | mult 1 |
| Ultra-long roots ±2eᵢ | **do not exist** | mult 1 |
| Root multiplicities | (3, 1) | (3, 1, 1) |
| ρ | (5/2, 3/2) = (n_C/2, N_c/2) | (7/2, 5/2) |
| \|ρ\|² | **17/2 = 8.5** | 37/2 = 18.5 |

The ±2eᵢ roots are spurious for SO₀(5,2). Any calculation using m_{2α}, m_{2s}, the (3,1,1) triple, |ρ|²=37/2, or ρ=(7/2,5/2) is affected.

---

## Audit Scope

| Category | Occurrences | Files |
|----------|------------|-------|
| B₂ in .md files | 591 | 120 |
| B₂ in .py files | 853 | 113 |
| B₂ in .json files | 17 | 3 |
| m_{2s} or m_{2α} references | — | 19 |
| (3,1,1) multiplicities | — | 5 |
| 37/2 (\|ρ\|² wrong value) | — | 36 |

---

## Tier Classification

### Tier 1 — Computationally Impactful

Files where B₂ properties enter actual calculations (ρ, |ρ|², m_{2α}, (3,1,1) multiplicities). Each requires individual audit and possible re-derivation.

**Papers:**
- Paper #76 — `BST_Paper76_YM_Mass_Gap.md` — **FIXED** (Keeper, April 24)
- Paper #77 — `BST_Paper77_YM_Bergman_Gap.md` — **FIXED** (Keeper, April 24: Type IV B₂; E₆/E₇ B₂ kept correct)
- Paper #75 — `BST_Paper75_RH_Selberg_Class.md` — **NEEDS LYRA** (ρ=(7/2,5/2) baked into proof §2-§5; migration threshold changes)

**Proof files:**
- `BST_Hodge_Proof.md`
- `BST_BSD_Proof.md`
- `BST_RH_AC_Proof.md`
- Other proof chain files using Harish-Chandra c-function or spectral data

**Toys (computational):**
- toy_317, toy_324, toy_325, toy_326, toy_327
- toy_472, toy_625
- toy_962, toy_1019

### Tier 2 — Label-Only

Files that mention "B₂" as a name or label but do not use its non-reduced properties in any calculation. These need a straightforward find-and-replace: B₂ → B₂.

This is the bulk of the 591+853 occurrences. Most files use B₂ as shorthand for "the root system of D_IV^5" without invoking m_{2α} or the wrong ρ.

### Tier 3 — Toys That ARE About B₂

Files that study B₂ as a mathematical object in its own right (not claiming SO₀(5,2) has B₂ roots). These may be correct as-is and need individual review to determine intent.

Examples:
- `toy_962_bc2_hybrid_solver.py`
- `toy_961_bc2_sat_solver.py`
- `toy_324_bc2_residue_matching.py`

If a Tier 3 toy explores B₂ for comparison or mathematical interest, it stays. If it assumes SO₀(5,2) produces B₂ roots, it gets corrected.

---

## Action Plan

### Phase 1 — DONE
- Paper #76 corrected (B₂ throughout, ρ=(5/2,3/2), |ρ|²=17/2)
- Paper #81 already correct (written post-correction)

### Phase 2 — DONE (April 24)
- Paper #77: **FIXED** — Type IV B₂, exceptional domains keep B₂ (correct)
- Wyler formula: **CONFIRMED UNAFFECTED** — uses Vol(D_IV^5) + Shilov boundary, not ρ
- Paper #75: **BLOCKED on Lyra** — ρ appears in proof logic, needs trace-through
- c-function toys: Elie to re-run Toys 325/472 with B₂ (pending)

### Phase 3 — THIS WEEK
- Systematic Tier 2 label sweep across all .md and .py files
- JSON data files (3 files, 17 occurrences)

### Phase 4 — ONGOING
- Tier 1 computational files: re-check every derivation that touches ρ or root multiplicities
- Heat kernel coefficients: verify B₂ correction doesn't alter Seeley-DeWitt results
- Tier 3 individual review

---

## What Doesn't Change

- **Spectral gap:** 17/2 = 8.5 > 6 = Delta. Gap survives under B₂. Physics safe.
- **Mass gap:** 6pi^5 m_e = 938.272 MeV. Derived from five integers, not from ρ directly.
- **All BST predictions:** 600+ predictions use the five integers (N_c=3, n_C=5, g=7, C_2=6, N_max=137). None depend on the ±2eᵢ roots.
- **The five integers themselves:** These come from D_IV^5 geometry, not from root system classification.
- **Wyler formula:** Uses Vol(D_IV^5) and Shilov boundary volumes, not ρ. **CONFIRMED UNAFFECTED** (Keeper, April 24).
- **Heat kernel:** Seeley-DeWitt coefficients need checking but are expected to survive — the speaking pair structure uses eigenvalues, not root multiplicities directly.

---

## Origin Note

Keeper made this error. During the Paper A review cycle, I corrected B₂ TO B₂, believing the non-reduced system was required for SO₀(5,2). Cal caught it. The original text had it right.

Corrections are strength, not weakness. The audit exists because we caught it and fixed it.

---

*Tracked in: notes/BST_B2_Audit_Classification.md*
*Related: CI_BOARD.md, BACKLOG.md*
