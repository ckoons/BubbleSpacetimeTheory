---
title: "Keeper routing note — Vol 16 OUTLINE v0.1 §1.5 staleness fix per Cal flag. The 'three genera' framing in the outline doc is stale relative to the Thursday 2026-05-28 convention convergence. Distinct from Vol 16 Ch 1 §3 v0.1 (which Keeper tier-gated and which DOES carry the corrected convention). Single specific edit + propagation routed to Lyra."
author: "Keeper"
date: "2026-05-30 Saturday late-morning"
status: "ROUTING NOTE — single staleness fix; Lyra absorption recommended in Vol 16 OUTLINE v0.2."
---

# Vol 16 OUTLINE §1.5 staleness fix routing

## 0. What Cal flagged

Cal (Saturday morning batch, Cal #163-#173 range): "Vol 16 Outline v0.1 — STALENESS FLAG — §1.5 'three genera' framing stale vs Thursday one-genus convention; v0.2 absorption needed."

## 1. Confirmation + specifics

File: `notes/Lyra_Vol_16_A_sub_Curriculum_Outline_v0_1.md` (filed 2026-05-28, BEFORE the Thursday 2026-05-28 PM genus-convention convergence).

**Current §1.5 (lines 28-35, stale)**:

> ## 1.5 Volume-wide STANDING convention — the three genera of D_IV⁵ (state in Chapter 1; referee-proofing)
> Per Keeper standing action item (2026-05-28): D_IV⁵ has THREE distinct dimension/genus invariants that MUST be stated explicitly and never conflated...
> - **Hua genus = n_C = 5** = complex dimension...
> - **Faraut-Korányi genus = C_2 = 6** = FK genus invariant = quadratic Casimir
> - **Embedding/signature dimension = g = 7** = p+q of SO_0(5,2) — explicitly NOT a genus
> ...
> (Open item flowing into the curriculum: kernel singularity exponent 7/2 vs Hua 5/2 — Keeper+Elie recheck; Chapter 3 to use resolved value.)

**The Thursday 2026-05-28 PM convergence corrected this** (per CLAUDE.md Thursday narrative + Lyra A1 v0.5 + Strong-Uniqueness v1.1 C2 correction + my Vol 16 Ch 1 §3 v0.1 tier-gate):

- **GENUS = n_C = 5** = complex dimension of D_IV⁵ = Bergman kernel singularity exponent = Hua kernel exponent. **FK and Hua AGREE on Type IV per Faraut-Korányi 1994**: both = n_C = 5.
- **C_2 = 6 = quadratic Casimir of B₂ — NOT a genus** (this was the mislabel that cost the recheck cycle).
- **g = 7 = embedding/signature dimension = p+q of SO_0(5,2) — NOT a genus**.
- Bergman/kernel singularity exponent per rank = n_C/rank = **5/2 = ρ_1**, NOT 7/2.

## 2. Recommended fix for Vol 16 OUTLINE v0.2 §1.5

Replace the stale "three genera" framing with the corrected one-genus + Casimir + embedding framing:

> ## 1.5 Volume-wide STANDING convention — one genus + Casimir + embedding (state in Chapter 1; referee-proofing)
> Per Thursday 2026-05-28 convergence (Elie Toy 3596 four ways + Keeper multiplicity + Lyra A1 v0.5 + Strong-Uniqueness v1.1 C2 correction): D_IV⁵ has THREE distinct dimension invariants that MUST be stated by value+role (Cal #32 STANDING) and never relabeled:
> - **GENUS = n_C = 5** = complex dimension of D_IV⁵ = Bergman kernel singularity exponent = Hua kernel exponent. Per Faraut-Korányi 1994 on Type IV, FK and Hua agree at n_C = 5. Per rank: 5/2 = ρ_1 of B₂.
> - **CASIMIR = C_2 = 6** = quadratic Casimir of B₂ — NOT a genus.
> - **EMBEDDING / SIGNATURE = g = 7** = p+q of SO_0(5,2) — NOT a genus.
>
> Every chapter that invokes a "Bergman exponent," "genus," or "dimension" must specify which. This single convention statement prevents the prior conflation (which cost a recheck cycle Thursday morning) permanently. The Bergman/kernel singularity exponent is n_C/rank = 5/2 = ρ_1 (NOT 7/2, which was the g-as-genus mislabel).

**Also remove or update the "Open item flowing into the curriculum: kernel singularity exponent 7/2 vs Hua 5/2 — Keeper+Elie recheck; Chapter 3 to use resolved value." line** — the recheck happened Thursday and is closed (5/2 = ρ_1 wins). Replace with: "Resolved Thursday 2026-05-28: kernel singularity exponent per rank = 5/2 = ρ_1 (n_C/rank); 7/2 was the g-as-genus mislabel and is retired."

## 3. Propagation check

The corrected convention is already absorbed in:
- ✓ Lyra Vol 16 Ch 1 §3 v0.1 (10:01 Saturday) — opening "Convention update" Section 0 (Keeper tier-gated as PEDAGOGICAL PASS earlier).
- ✓ Lyra A1 v0.5 / v0.4 Final Disposition.
- ✓ Lyra Strong-Uniqueness v1.1 C2 correction.
- ✓ CLAUDE.md Thursday narrative.
- ✓ Honest-State Ledger v0.2/v0.3/v0.4.

**Stale only in**: Vol 16 OUTLINE v0.1 §1.5 (this fix). One file, one section, ~10 line rewrite.

## 4. Calibration #34 self-check

The fix itself is Calibration #34 STANDING discipline: the OUTLINE doc headline + Section 1.5 used "three genera" framing prominently. A reader of the outline would walk away with the stale convention; the recent Ch 1 §3 v0.1 update would not propagate to that reader. **Headline-cap-conditionality requires propagation across documents that share standing conventions.**

This is also a small instance of the broader staleness-propagation issue Cal flagged at 4th instance of headline-cap-conditionality (Engine v0.3 §3): when a load-bearing convention changes, all docs invoking it need synchronized update. Vol 16 OUTLINE v0.1 § 1.5 is one such site.

## 5. Routed handback

- **Lyra**: Vol 16 OUTLINE v0.2 absorbs §1.5 staleness fix per recommended wording above; trivial mechanical edit (~5 min). Confirm propagation across other Vol 16 outline locations (lines 28-35 are the substantive site; spot-check for "FK genus" or "three genera" elsewhere).
- **Cal**: flag closed pending Lyra v0.2 filing.
- **Keeper**: no further audit needed; pedagogical staleness, not substantive structural issue.

## 6. Cross-references

- Vol 16 Ch 1 §3 v0.1 (Saturday 10:01) — corrected convention already in place.
- Lyra Strong-Uniqueness v1.1 §2 (C2 corrected to 5/2 = ρ_1).
- CLAUDE.md Thursday 2026-05-28 narrative (genus convergence).
- Keeper Vol 16 Ch 1 §3 v0.1 tier-gate doc — pedagogical PASS with N1+N2 sharpening notes.

— Keeper. Brief routing note; Vol 16 OUTLINE v0.1 §1.5 staleness confirmed; recommended fix wording provided; Lyra absorption trivial (~5 min); Cal #34 STANDING discipline noted as cross-doc propagation issue.
