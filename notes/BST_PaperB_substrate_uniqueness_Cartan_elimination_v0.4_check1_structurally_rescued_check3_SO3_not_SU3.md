---
title: "Paper B v0.4 — D_IV⁵ substrate uniqueness. Absorbs Grace's two cold-read findings (Q1, Q2) on Cal #332's decisive checks. CHECK 1 STRUCTURALLY RESCUED: the m_s≥3 convergence bound is set by the RANK (integration dimension = 2 for all type-IV domains), with the dimension entering ONLY through the multiplicity variable a = n−2 — so '⌊n_C/2⌋=2' was a mis-statement of 'f(rank)=2'; the 2 is the rank, genuinely dimension-free; the circularity dissolves structurally; only the NUMERICAL threshold (rank-2 ⟹ a≥3) remains as a Harish-Chandra computation (not a circularity). CHECK 3 CORRECTED (Grace self-walkback): the short-root multiplicity space carries SO(3) = M = SO(n−2), NOT SU(3) — the 3 directions transform as the SO(3) vector; so N_c=3 matches the DIMENSION (3=3) but the natural group is SO(3); the color identification SU(3) is a SEPARATE pending argument (complex structure SO(3)→SU(3), or the dual-Coxeter route h^∨(SU(3))=N_c). CRUCIAL: the uniqueness SPINE is UNTOUCHED — it only ever needed the multiplicity VALUE a=3 to select D_IV⁵, never the color reading; the central theorem survives, the secondary 'this 3 is color' claim downgrades to pending. Net: a CLEANER paper — dimension-innocence structurally recovered (Check 1), color-identification correctly separated out as downstream-pending (Check 3). Deltas from v0.3."
author: "Lyra (Claude Opus 4.8) — Casey Koons, PI; Grace (c-function rank-argument Q1 + SO(3) centralizer correction Q2), Elie (Toy 4290/4292/4295 full n-scan), Cal (#331/#332 anti-circularity standard)"
date: "2026-06-21 Sunday"
status: "v0.4 DRAFT — absorbs Grace Q1 (Check 1 structurally rescued; numerical threshold pending) + Q2 (Check 3 corrected: SO(3) not SU(3); spine survives). SPINE solid (multiplicity a=3 selects D_IV⁵ uniquely). DIMENSION-innocence structurally recovered, one Harish-Chandra value pending. COLOR-identification (a=3 IS SU(3)) downgraded to separate pending claim. Elie 4295 closes the n-scan verification (Check 4). For Cal re-read + the two pending computations (Grace c-function value; SO(3)→SU(3) link)."
---

# Paper B v0.4 — revision deltas (Check 1 rescued, Check 3 corrected)

This revises v0.3. Grace took Cal #332's two substantive checks to their fabrication-safe limits and returned a result on each — one an upgrade, one a self-correction. Both improve the paper. The uniqueness **spine is unchanged and intact**; what moves is the disposition of the two innocence checks.

## Δ1 — Check 1 (decisive) is STRUCTURALLY RESCUED (Grace Q1)

**v0.3 had this OPEN and decisive:** R3's lower bound m_s ≥ 3 was justified via "⌊n_C/2⌋ = 2 seminorms," and ⌊n_C/2⌋ presupposes the dimension.

**Grace's finding:** the spectral-convergence threshold is set by the **rank** — the rank is the *integration dimension* of the spherical transform (the maximal flat), and it is **2 for every type-IV domain, for all n**. The dimension n enters the analysis **only** through the multiplicity variable a = n − 2 (the thing being bounded). So:

  "⌊n_C/2⌋ = 2" was a **mis-statement** of "**f(rank) = 2**."

The "2" is the rank (R1, a prior criterion), **genuinely dimension-free**. The two expressions coincided at n = 5 (rank 2 = ⌊5/2⌋) — which is precisely why the slip hid (exactly the "coincide at the answer and nowhere else" fingerprint v0.3/F257 flagged). **The circularity dissolves structurally: the criteria are innocent of the dimension.**

**What remains (narrowed, and NOT a circularity):** the *numerical* fact that rank-2 trace-formula convergence requires multiplicity **≥ 3 exactly** is a genuine Harish-Chandra c-function computation (the order of vanishing of |c(λ)|⁻² at the short-root wall on a rank-2 domain). Grace will not assert the value from memory. So Check 1 moves from **"OPEN — possible circularity"** to **"structural innocence recovered; one numerical threshold value pending a clean spectral computation."** That is a large upgrade: the worry was *circularity*; what's left is an honest *unproved-but-not-circular* numerical bound.

## Δ2 — Check 3 (substantial) is CORRECTED: SO(3), not SU(3) (Grace Q2, self-walkback)

**v0.3 had:** "N_c = 3 matches the short-root multiplicity; structural identification pending the K449 embedding."

**Grace's finding (correcting her own earlier "N_c = 3 is solid, not an external color assignment"):** the short-root multiplicity space carries **SO(3)**, not SU(3). The centralizer of the maximal flat is M = SO(n−2) = SO(3); the n−2 = 3 short-root directions transform as the **SO(3) vector**. So:

- **N_c = 3 = a matches the DIMENSION** (3 = 3, the count of short-root directions) — and *this* is what selects D_IV⁵ uniquely;
- but the **natural group** on that space is **SO(3)**, not color SU(3).

Cal's #286 small-integer-coincidence concern was therefore **real**: "a = 3 IS the color group SU(3)" is a **separate, pending argument**, not established by the multiplicity match. The two live routes (neither asserted here): (i) the complex structure J promoting SO(3) → SU(3) on the J-complexified short-root space; (ii) the independent dual-Coxeter route h^∨(SU(3)) = N_c (Elie engine §7). Until one closes, the honest claim is: **"a = 3 selects D_IV⁵; identifying that 3 with color SU(3) is downstream and pending."**

## Δ3 — Why the spine survives both (the load-bearing point)

The uniqueness theorem **only ever needed the multiplicity VALUE a = 3** — that (rank = 2, a = 3) selects D_IV⁵ uniquely across the classification (Elie 4290 spine + 4292 a=3 selector + 4295 full R1∧R3∧R5 n-scan). It **never needed** the color identification. So:

- **Check 1 rescue** strengthens the theorem's *innocence of dimension* (the criteria don't smuggle n).
- **Check 3 correction** removes a claim the theorem never relied on (color = the multiplicity), relocating it to a clearly-marked downstream pending item.

The central result is therefore **cleaner** in v0.4 than in v0.2: dimension-innocence is structurally recovered, and the color claim — the part most exposed to "small-integer coincidence" — is honestly separated out rather than bundled into the spine.

## Δ4 — Check 4 (n-scan verification) now CLOSED (Elie 4295)

Toy 4295 runs the R1 ∧ R3 ∧ R5 n-scan (for each n: tube ∧ a≥3 ∧ d_F≤2 → n=5 unique pass), completing the criteria-innocence scan that 4290 (spine) and 4292 (a=3 selector) did not cover. **Verifying the scan confirms the arithmetic of the elimination — it does not by itself establish innocence** (that's Checks 1–3). Honest status: the scan is now verified; innocence rests on Δ1 (structurally recovered, one value pending) + Δ2 (color separated, pending).

## Δ5 — Check 2 (Selberg upper bound) status

Unchanged from v0.3: R5 (d_F ≤ 2 ⟹ a ≤ 3) needs d_F shown to track the multiplicity, not the dimension. This pairs with Grace's Q1 lane (same c-function/spectral-zeta structure) and is pending the same computation family. The two-sided bracket on a = 3 is then: lower bound rank-set (Δ1), upper bound multiplicity-set (this Δ) — both dimension-free in form, both with one numerical value pending.

## Net (revision status)

| item | v0.3 | v0.4 |
|---|---|---|
| selection spine (rank=2, a=3 ⟹ dim=5) | solid | **solid (unchanged); n-scan now verified (Elie 4295)** |
| Check 1: dimension-circularity | OPEN, decisive | **STRUCTURALLY RESCUED (bound is f(rank), dimension-free); numerical a≥3 value pending Harish-Chandra (Grace)** |
| Check 2: Selberg d_F tracks a not dim | OPEN | OPEN (same c-function lane) |
| Check 3: N_c=3 IS color SU(3) | "pending K449 embedding" | **CORRECTED: multiplicity space carries SO(3) not SU(3); a=3 matches the dimension; color identification SEPARATE + pending (J→SU(3) or dual-Coxeter)** |
| Check 4: innocent n-scan | unverified, 30-min toy | **CLOSED (Elie 4295)** |
| dimension-innocence of the criteria | claimed-not-proved | **structurally recovered (Δ1); honest** |
| color claim (a=3 = SU(3)) | bundled in spine | **separated out as downstream-pending (Δ2)** |

**Count HOLDS 4 of 26.** SU(3) scope. v0.4 is sharper than v0.2 ever was: dimension-innocence structurally recovered, color-identification honestly separated. Two computations remain — the rank-2⟹a≥3 threshold value (Grace c-function) and the SO(3)→SU(3) link (J-complexification or dual-Coxeter). Neither is a circularity; both are bounded, fabrication-safe, flagged-not-faked. INTERNAL.

@Grace — both your findings absorbed: Q1 is Δ1 (Check 1 structurally rescued — the "2" is the rank, dimension-free; only the numerical ≥3 threshold pending your c-function); Q2 is Δ2 (Check 3 corrected — SO(3) = M = SO(n−2) carries the 3 directions as a vector; color SU(3) separated out as pending). Your self-walkback made the paper cleaner: the spine never needed color, so removing the overclaim costs nothing and the central theorem is now more defensible. @Cal — #332 fully absorbed across v0.3→v0.4: Check 1 no longer a circularity (structurally dissolved), Check 3 your #286 concern confirmed and corrected, Check 4 closed (Elie 4295). The remaining items are honest unproved-numerical / unproved-structural, not circular. @Elie — 4295 closes Check 4; thank you. @Keeper — K456's "co-derived" fallback is now superseded for the better: Check 1 isn't "m_s and n_C co-derived," it's "the bound is rank-set and dimension-free in form, with one numerical value pending" — strictly stronger than the fallback.

— Lyra, Sun 2026-06-21 (date-verified). Paper B v0.4: absorbs Grace Q1+Q2. CHECK 1 STRUCTURALLY RESCUED — convergence threshold = f(rank), rank=2 ∀ type-IV n, dimension enters only via a=n−2; "⌊n_C/2⌋=2" was a mis-statement of "f(rank)=2"; circularity dissolves; only numerical rank-2⟹a≥3 threshold pending (Harish-Chandra, Grace). CHECK 3 CORRECTED (Grace self-walkback) — short-root multiplicity space carries SO(3)=M=SO(n−2) as vector, NOT SU(3); a=3 matches dimension (3=3, the selector) but color identification is SEPARATE + pending (J→SU(3) or dual-Coxeter). SPINE UNTOUCHED (only needs a=3 value, never color). CHECK 4 CLOSED (Elie 4295 n-scan). Net: cleaner paper — dimension-innocence structurally recovered, color-claim separated as downstream-pending. Count HOLDS 4.
