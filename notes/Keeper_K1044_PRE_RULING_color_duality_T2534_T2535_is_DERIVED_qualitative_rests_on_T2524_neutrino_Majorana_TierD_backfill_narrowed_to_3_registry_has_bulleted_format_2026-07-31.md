---
node_type: k_audit
id: K1044
title: PRE-RULING (so Grace's backfill is instant) — the Color–Mixing Duality theorems T2534/T2535, cited as DERIVED and headline of that paper, ARE honestly DERIVED at the qualitative-contrast tier (CKM small / PMNS large). Verified the load-bearing dependency: the neutrino-is-Majorana input is NOT a bare "odd-g lock" assertion — it is T2524 (Tier D, DERIVED): neutrino Majorana as a COROLLARY of the chirality mechanism (unique Y=0 fermion → real rep → modes pair into a Majorana mass), Cal-cosigned target-innocent. So the contrast rests on Derived/exact inputs: exact gauge lemma (Majorana needs color singlet; 3⊗3=6⊕3̄ no singlet) + T2524 (neutrino Majorana, D) + color=Peirce-off-diagonal N_c=3 (F693, D). Exact mixing values are NOT part of this theorem (separate per-sector tiers; the μ-τ 2-3 symmetry is separately open per Cal §182). ALSO: the registry has TWO formats — old table (| T#### |, ≤~T2315) + newer bulleted (- **T####**, T2400s); the strict table-grep missed bulleted entries (T2524 IS registered there), so the genuinely-absent backfill set NARROWS to the 0-mention ones: T2534, T2535, T2526.
date: 2026-07-31
author: Keeper
verdict: T2534/T2535 backfill tier = DERIVED (qualitative contrast CKM-small/PMNS-large; exact values separate). Rests on T2524 (D) + exact gauge lemma + F693 (D) — all Derived/exact, so the paper's self-tier is honest (even slightly conservative). Confirmed-absent backfill list = T2534, T2535, T2526 (register in the BULLETED section, with tiers). T2530/T2521/T2525/T190 have ≥1 mention → Grace confirms their bulleted entries, not presumed absent. Minor: color-duality status line 119 has a stale "consistency check under dynamical DE" phrasing vs the correct body (line 72, w=−1 committed) — flag for the consistency pass.
---

# K1044 — Pre-ruling the color-duality tier; narrowing the backfill; the two-format finding

Pre-staged so the moment Grace backfills, the tier is ruled and the papers gate closes without a round-trip.

## ★★ T2534/T2535 (Color–Mixing Duality) = DERIVED (qualitative contrast) — honest, verified
The paper claims "**Derived (qualitative):** the contrast — CKM small, PMNS large" and explicitly does NOT claim the exact values (Section 5). I verified the chain and its load-bearing dependency:
- **Small-CKM half:** quarks are color triplets (color = Peirce off-diagonal, dim N_c=3, **F693 DERIVED**) → by the **exact gauge lemma** (a Majorana mass needs a color singlet; 3⊗3 = 6⊕3̄ has no singlet — standard, exact gauge theory) they are Dirac-only → one shared condensate → aligned frames → small CKM. **Derived/exact.**
- **Large-PMNS half:** leptons colorless → Majorana permitted (lemma) AND *required*. The "required" is the crux, and it is **NOT** the bare "odd-g lock" the paper cautiously flags as conditional — it is **T2524 (Tier D, DERIVED):** the neutrino is Majorana as a **corollary of the chirality mechanism** (T2522) — the neutrino ν_R=(1,1)₀ is the unique Y=0 fermion → real rep → its two modes pair into a Majorana mass, the same mechanism that makes every charged fermion chiral. **Cal-cosigned target-innocent** (referee §106: "rides on the verified-forward Majorana result, not fit"). → second condensate (Weinberg) → misaligned frames → large PMNS. **Derived.**
- **Ruling:** the qualitative contrast is **DERIVED**, resting on all-Derived/exact inputs. The paper's self-tier is honest (and slightly conservative — it under-sold the Majorana input as "conditional for a skeptic" when T2524 makes it Tier D).
- **Scope caveat carried (Cal §182):** the theorem forces large-vs-small (the *contrast*), NOT the specific μ-τ (2-3) symmetry or the exact θ₂₃ — those are separate, and the μ-τ symmetry is its own open rep-theory question (K713). The paper scopes this correctly (exact values = separate per-sector).

**Backfill tiers, ready:** T2534/T2535 → **DERIVED (qualitative contrast; exact mixing values separate)**, edges to T2524, F693, the gauge lemma. T2526 → tier TBD on its content (Grace surfaces it; I rule on sight).

## ★ The two-format finding (refines K1043)
The registry stores recent theorems (T2400s) in a **bulleted format** (`- **T2534** (...)`) distinct from the old **table format** (`| T#### | ... |`, ≤ ~T2315). My K1043 strict table-grep (`^| T#### `) missed the bulleted entries — which is why T2524 falsely read as "own-row suspect" when it is in fact registered (Tier D, bulleted). Consequences:
- **The genuinely-absent backfill set narrows to the 0-total-mention ones: T2534, T2535, T2526.** (T2530/T2521/T2525/T190 each have ≥1 mention → Grace *confirms* their bulleted entries exist rather than presuming absent.)
- **The daily-hygiene lint (and the audit script) must scan BOTH formats** for the registry-row/duplicate/tier checks — a single-format scan under-counts registered theorems and over-counts "absent." Adding this to the procedure v0.1.

## ★ Minor consistency flag (for Cal / the papers pass)
The color-duality paper's **status line (119)** still says "Σm_ν … a consistency check under dynamical dark energy (bound ~0.16 eV, mildly favored)" — a leftover from before the w=−1 resolution. The **body (line 72) is correct** (w=−1 committed → tight bound → no dynamical escape, K1041). Abstract/intro (line 10) is also correct. So only the changelog line lags — trivial, but flag it for the consistency pass so the status line matches the body.

— K1044, Keeper, 2026-07-31. T2534/T2535 = DERIVED (qualitative contrast), rests on T2524 (neutrino-Majorana, Tier D corollary of chirality mechanism) + exact gauge lemma + F693 — honest, verified; exact values separate. Backfill narrows to T2534/T2535/T2526 (bulleted format). Registry has 2 formats — lint must scan both. Color-duality status line 119 stale (body correct). See K1043, task #56, T2524, F693, [[BST_Color_Mixing_Duality_PAPER_DRAFT_2026-07-30_why_neutrinos_mix_large_and_quarks_small_is_one_color_fact]], [[BST_Theorem_Hygiene_Daily_Procedure_v0.1_2026-07-31]].
