---
title: "Paper B v0.3 — D_IV⁵ substrate uniqueness. Absorbs Cal #332 cold-read: the criteria-innocence claim is tiered DOWN from 'maximally airtight' to 'sharpened toward innocence; airtightness pending three checks.' The FF-28 fix is applied head-on — the abstract and net now match the honest body (no 'maximal innocence' anywhere). Deltas from v0.2 (BST_PaperB_substrate_uniqueness_Cartan_elimination_v0.2_revision.md); the spine (rank=2, m_s=3 → dim ∧ color) carries over UNCHANGED — only the innocence *claim about* the spine is re-tiered, plus the three open checks are stated as explicit conditions."
author: "Lyra (Claude Opus 4.8) — Casey Koons, PI; Grace (Cartan + N_c=3 invariant + W3 + c-function checks), Elie (Toy 4290/4292), Cal (#331/#332 anti-circularity standard)"
date: "2026-06-21 Sunday"
status: "v0.3 DRAFT — absorbs Cal #332. The selection SPINE is solid (rank=2, m_s=3 ⟹ dim_C=5 ∧ N_c=3). The INNOCENCE of that spine (its non-circularity) is CLAIMED, NOT PROVED, and rests on three open checks — chiefly Check 1, the dimension-independence of the m_s≥3 lower bound (an open Harish-Chandra c-function computation, routed to Grace). Abstract tiered down accordingly. For Cal re-read + Grace c-function work."
---

# Paper B v0.3 — revision deltas (innocence tiered to "pending")

This revises v0.2. **The mathematical spine is unchanged**: among irreducible Hermitian symmetric domains, the prior root-system criteria (rank = 2, short-root multiplicity m_s = 3) force both dim_C = 5 and N_c = 3, with m_s = 3 itself bracketed by R3 (≥3) and R5 (≤3). What changes in v0.3 is the **claim about that spine's innocence** — its freedom from circularity — which Cal's #332 cold-read showed is not yet established. We tier it down honestly and state the open checks as explicit conditions.

## Δ0 — The FF-28 fix (why this revision exists)

v0.2's body honestly tagged the n-scan "computed-not-verified" (Δ5) and flagged the dimension-link, but its abstract/net escalated to "**maximal** criteria-innocence." That is the recurring headline-vs-body leak (K450/K330 pattern): the summary was written as a separate act from the body and overstated it. v0.3 makes the abstract, the net, and the body say the **same** thing. **There is no "maximal innocence" claim anywhere in v0.3.**

## Δ1 — The innocence claim, re-tiered (replaces v0.2's Δ1 headline)

**v0.2 claimed:** "(rank=2, m_s=3) forces dim AND color, *neither named in the criteria* — maximal criteria-innocence."

**v0.3 claims:** "(rank=2, m_s=3) forces dim_C=5 and N_c=3 — a genuine and elegant reduction. Whether this is *criteria-innocent* (non-circular) depends on three checks, of which the first is decisive and currently open. Pending those, the honest reading is **'sharpened toward innocence; airtightness pending Checks 1–3.'**"

The spine is the theorem a referee checks; its innocence is the property that makes the theorem *load-bearing for the "G is derived" strategy*. We separate the two cleanly: the first is solid, the second is pending.

## Δ2 — Check 1 (DECISIVE, OPEN): does m_s ≥ 3 derive without presupposing the dimension?

R3's lower bound (m_s ≥ 3) was justified in v0.2 (Δ3) via the c-function vanishing to order ≥ 6, "so that ⌊n_C/2⌋ = 2 seminorms converge." **⌊n_C/2⌋ = 2 presupposes n_C ∈ {4,5}** — the dimension being derived. If the convergence requirement genuinely counts ⌊n_C/2⌋ seminorms, R3 mentions the dimension and the anti-circularity fails.

**The candidate dimension-free form, and the exact test that decides it.** The natural innocent reading is that the seminorm count is the **rank** (R1, prior), not ⌊n_C/2⌋. The test is sharp because the two quantities behave oppositely across the family:

- rank = 2 for **every** n in type IV (the Lie ball is rank 2 for all n ≥ 3);
- ⌊n_C/2⌋ = 2 **only** at n_C ∈ {4,5}.

They **coincide at n=5 and nowhere else** — the fingerprint of a quantity that looks prior but reads the answer. So the n=5 case cannot settle it; it is settled only by computing the order of vanishing of the Plancherel density |c(λ)|⁻² at the short-root wall on a rank-2 type-IV domain, and showing rank-2 trace-formula limit-interchange forces order ≥ 6 (⟹ m_s ≥ 3) with n_C entering *only* through m_s = n−2, not through a seminorm count. **This is an open Harish-Chandra c-function computation (routed to Grace).** We do not assert the exponent.

**The fallback honest claim if Check 1 cannot be made dimension-free** (Keeper K456's framing): R3 then "jointly determines m_s ≥ 3 *and* n_C ≈ 5 from a single convergence requirement." That is **still a uniqueness theorem** — D_IV⁵ is still the unique domain meeting the criteria — but the criteria then *do* reference the dimension, so the marketing claim "G is derived from conditions that never mention dimension or color" weakens to "G and dimension are co-derived from one spectral requirement." The strategy survives either way; only the strength of the innocence claim moves.

## Δ3 — Check 2 (OPEN): is the upper bound also dimension-clean?

R3 ∧ R5 bracket m_s = 3 from both sides. The lower bound is Check 1. The **upper bound** (R5: Selberg degree d_F ≤ 2 ⟹ m_s ≤ 3) needs the same scrutiny: **d_F must be shown to track m_s (or the count of Gamma factors in the completed spectral zeta), not the dimension.** If d_F = dim (a naive Weyl-law reading), then "d_F ≤ 2" bounds the *dimension* directly — a different circularity, and an inconsistent one (dim_C = 5 would give d_F > 2). Pinning the degree-formula's actual dependence is required. Routed to Grace (same c-function/spectral-zeta lane as Check 1).

## Δ4 — Check 3 (SUBSTANTIAL, OPEN): N_c = m_s = 3 — derivation or coincidence?

The structural link must be more than two integers that happen to be 3 (Cal's #286 small-integer-coincidence concern). What's needed: **the SU(3)_color generators are realized on the short-root multiplicity space of D_IV⁵** — i.e. "N_c = short-root multiplicity" is a *representation* statement, not an arithmetic match. We have h^∨(SU(3)) = N_c via the dual Coxeter number (Elie engine §7), and K449 link 2 (SO(10)/Pati-Salam, B−L) is SOLID *at the classification level*. The remaining gap: show the K449 embedding makes **color act on the (n−2)-dimensional short-root space**. Until then, the honest statement is "N_c = 3 *matches* the short-root multiplicity; structural identification pending the embedding." Routed to the K449 embedding audit.

## Δ5 — Check 4 (MINOR, mechanical): verify the innocent n-scan

Toy 4290 (6/6) verified the **spine** (rank ∧ dim ⟹ D_IV⁵); Toy 4292 verified the **a = 3 selector**. **Neither verifies the R1 ∧ R3 ∧ R5 n-scan** — the very computation that constitutes the criteria-innocence proof (the thing that makes v0.2/v0.3 "innocent"). A mechanical Elie toy (the n-scan: for each n, evaluate tube/m_s≥3/d_F≤2 and confirm n=5 is the unique pass) closes this in ~30 min. Honestly flagged, not yet run.

## Δ6 — Carried over unchanged from v0.2

The spine (Δ1/Δ2 of v0.2), the R3-generic-spectral citation (Δ3), the R2/R4 independent-invariants no-double-lock (Δ4), and the W3 net-compatibility grounding via BGL (Δ6) all carry over. The over-determination (§5 of v0.1: integer-web 21 = N_c·g; Strong-Uniqueness legs) stays at its existing tier as corroboration, not proof.

## Net (revision status)

| item | v0.2 | v0.3 |
|---|---|---|
| selection spine (rank=2, m_s=3 ⟹ dim=5 ∧ N_c=3) | solid | **solid (unchanged)** |
| innocence of the spine | "maximal criteria-innocence" | **"sharpened toward innocence; airtightness pending Checks 1–3"** |
| Check 1: m_s≥3 dimension-free | (the overstated part) | **OPEN — decisive; c-function computation → Grace** |
| Check 2: d_F tracks m_s not dim | unexamined | **OPEN → Grace** |
| Check 3: N_c=m_s structural | "third independent selector" | **OPEN — structural link pending K449 embedding** |
| Check 4: innocent n-scan | tagged computed-not-verified | **explicit: 4290/4292 don't cover it; 30-min Elie toy** |
| abstract vs body | abstract overstated (FF-28) | **abstract = body; no "maximal innocence" anywhere** |

**Count HOLDS 4 of 26.** SU(3) scope. v0.3 is the honest interim state: the spine stands; its innocence is claimed-not-proved and reduces to three named checks, the first being a specific open spectral computation. When Grace's c-function result lands, Check 1 resolves to either dimension-free (innocence airtight → v0.4 restores the strong claim) or co-derived (the K456 fallback → v0.4 states the weaker-but-honest claim). INTERNAL.

@Cal — #332 absorbed in full: the abstract is trimmed to "sharpened toward innocence; airtightness pending Checks 1–3" (your exact directive); all four checks stated as explicit conditions, decisive-first; the FF-28 headline-vs-body leak fixed (no "maximal innocence" anywhere in v0.3). Your #331 anti-circularity standard is the paper's gate, written in. @Grace — Checks 1 and 2 are the load-bearing c-function questions and they're yours; v0.4's innocence claim is whatever your computation says it is (airtight if dimension-free; the co-derivation fallback if not). @Keeper — K456 fallback framing ("R3 jointly determines m_s≥3 and n_C≈5") is written in as the explicit Check-1-fails branch (Δ2); the theorem survives either branch, only the innocence strength moves. @Elie — Check 4 is the 30-min n-scan toy (R1∧R3∧R5 → n=5 unique); 4290/4292 don't cover it, as you'd expect.

— Lyra, Sun 2026-06-21 (date-verified). Paper B v0.3: innocence tiered DOWN per Cal #332. Spine unchanged (rank=2, m_s=3 ⟹ dim=5 ∧ N_c=3, solid). Innocence CLAIMED-NOT-PROVED → "sharpened toward innocence; pending Checks 1–3." Check 1 (decisive, OPEN): m_s≥3 lower bound WORDED via ⌊n_C/2⌋=2 references dimension; candidate fix (count=rank, prior) dimension-free in structure (rank=2 ∀n; ⌊n_C/2⌋=2 only at n=5 — coincide at answer) but needs the c-function order computation (→Grace); K456 fallback = "m_s and n_C co-derived" if it can't be made dimension-free (theorem survives, claim weakens). Check 2 (OPEN): d_F must track m_s not dim (→Grace). Check 3 (OPEN): N_c=m_s structural via K449 embedding not 3=3. Check 4 (minor): n-scan unverified, 30-min Elie toy. FF-28 fixed: abstract=body, no "maximal innocence." Count HOLDS 4.
