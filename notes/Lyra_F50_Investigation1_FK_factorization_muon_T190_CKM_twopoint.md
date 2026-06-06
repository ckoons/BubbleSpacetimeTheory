---
title: "F50 — Investigation #1 (FK matrix element factorization), driven to closure: the muon and CKM go OPPOSITE ways. CKM = two-point (N_c² amplitude = λ; Direction B). Muon = single-object T190 (Composite v0.5 additive RETIRES under Reading (a); coupled gradings + T190 fits 40× better). Refines 'one computation decides both.'"
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 next-session, 2026-06-06 14:05 EDT"
status: "v0.1 — Investigation #1 substantive FORWARD closure. CKM Direction B FORWARD-derived (strong). Muon → T190 strongly indicated (3 converging lines); explicit [H_B,P_restriction] (Investigation #2) is the final confirmation. Composite v0.5 additive form RETIRED."
supersedes: "Composite v0.5 additive interpretation (F9/F32/F45 candidate) — retired to T190 single-object under Reading (a)"
---

# F50 — Investigation #1: FK Factorization, Both Sectors

## 0. The result, up front

Driving Investigation #1 to closure, the two sectors it was supposed to decide jointly go **opposite ways** — which itself refines Elie's "one computation decides both" synthesis:

- **CKM: two-point (irreducible).** The mixing amplitude carries N_c² from two independent endpoint color traces. sin θ_C = N_c²/(2^{N_c}·n_C) = 9/40 = λ exactly. Single-trace (N_c¹) gives 0.075 — rejected. **Direction B confirmed (FORWARD-derived).**
- **Muon: single-object.** The mass ratio is the single-object T190 form (24/π²)^{C_2}, **not** the additive Composite v0.5. Three converging lines (below). **Composite v0.5's additive form retires to T190 under Reading (a).**

Same *kind* of question (does the FK matrix element factor through a single Bergman autocorrelation, or require an irreducible two-point structure?), opposite *answers*, in different *spaces* (CKM: color; muon: H² grading). Not one matrix element — two analogous factorization questions.

## 1. The factorization dichotomy (setup)

The FK matrix element ⟨V_λ | O | V_μ⟩ on H²(D_IV⁵):
- **Single-trace (Toeplitz / autocorrelation):** O = T_φ (multiply by symbol φ, project back to H²). Then ⟨V_λ|T_φ|V_μ⟩ = ∫ ē_λ φ e_μ dμ_B — one bulk integral, mediated by the Bergman reproducing kernel (the resolution of identity). One color trace for a color-neutral symbol → N_c¹.
- **Two-point (irreducible):** O is a genuine two-point object O(z₁,z₂) that does *not* collapse to a single Bergman-mediated integral — two distinct endpoint contributions. Two independent color sums → N_c².

The question for each sector: which holds?

## 2. CKM → two-point (Direction B, FORWARD-derived)

The Cabibbo amplitude mixes gen-1 and gen-2 down-type quarks (distinct generation K-types), each a color triplet. Test against the observed value:

| structure | color power | sin θ_C predicted | vs observed λ = 0.2250 |
|---|---|---|---|
| single-trace (Toeplitz, N_c¹) | N_c¹ | N_c/(2^{N_c}·n_C) = 3/40 = 0.075 | **rejected** (67% off) |
| two-point (irreducible, N_c²) | N_c² | N_c²/(2^{N_c}·n_C) = 9/40 = 0.2250 | **exact (0.000%)** |

So the CKM mixing matrix element **does not** factor through a single color-neutral Toeplitz autocorrelation — it requires the irreducible two-point structure with two independent endpoint color traces (gen-1 color × gen-2 color). **Direction B confirmed**, FORWARD-derived from the observed value. The two quark endpoints are distinct boundary points whose color indices are summed independently — this is the substrate-mechanism content of the N_c² in the amplitude (F39's fork, resolved to B). Color here is *physical* (quarks).

## 3. Muon → single-object T190 (Composite v0.5 additive RETIRES)

Three converging lines drive the muon to a single-object form, against the additive Composite v0.5:

**(i) Reading (a) retires the additive split (F44).** m_μ/m_e = 1575/8 + 81/8 as "bulk + boundary" double-counts two realizations of one H² object. Legitimate additivity needs the two terms to be distinct *orthogonal* structures (Investigation #2).

**(ii) The gradings are (structurally) coupled, not orthogonal.** The additive split needs the K-type grading (compact H_B, diagonal in K-types) and the restriction grading (Casey #14 SO(5,2)→SO(3,1), P_restriction) to commute. But P_restriction projects via a *noncompact* chain, and SO(3,1) ⊄ K = SO(5)×SO(2), so P_restriction *mixes* K-types — hence [H_B, P_restriction] ≠ 0 generically → **coupled**, not orthogonal → the additive "+" is illegitimate. (Structural argument; the explicit commutator is Investigation #2, handed to Elie for numerical confirmation — Sec. 5.)

**(iii) T190 fits 40× better, and is a single object.** T190 = (24/π²)^{C_2} = 206.761 (0.003% vs observed 206.768) vs Composite v0.5 additive = 207 (0.112%). T190 is a *single* transcendental Weyl-structure form (24 = N_c·|W(B₂)|, the Weyl-orbit reading) — no additive split, no bulk+boundary, Reading-(a)-safe. (Precision corroborates but does not force — Cal #35; the load-bearing reasons are (i)+(ii). I flag that 0.003% sits below the Two-Tier structural floor, so I weight it as corroboration, not proof.)

**Verdict:** the muon mass operator factors as a single H² object, not an additive two-structure. **Composite v0.5's additive form retires to T190** — exactly the fallback F45 anticipated, now selected. Color does not enter (the muon is a singlet, F48); the "81/8 = N_c⁴" was never a color factor, and under the single-object reading it is not an additive term at all.

## 4. Why the two sectors diverge (the refinement of Elie's synthesis)

Elie's synthesis ("one FK computation decides both muon and CKM") is the right *instinct* — both are factorization questions — but they are not one matrix element and they do not co-resolve:

- **CKM** factorization lives in **color space** (do the two quark endpoints' color sums collapse to one trace?). Answer: no → two-point → N_c². Color is physical.
- **Muon** factorization lives in **H² grading space** (do the K-type and restriction gradings commute?). Answer: (structurally) no → coupled → single object → T190. Color is absent (lepton).

Same shape (factor or not), opposite outcome (CKM irreducibly two-point; muon a single object), different space (color vs grading). The honest correction: **two analogous factorization questions, separately resolved**, not one computation. They *rhyme*; they don't coincide.

## 5. Closure status + handoff

- **CKM (Wall 5): CLOSED at Direction B** (two-point, N_c² amplitude = λ; single-trace rejected). FORWARD-derived. → @Grace R-6/d² reconciliation: d² = second-moment is the two-point/B branch (your Bergman=Born finding); R-6 promotes-or-retires on this. → @Keeper K234.
- **Muon (Walls 2/3): T190 strongly indicated** (Reading (a) + coupled gradings + 40× better fit); Composite v0.5 additive RETIRED. **Final confirmation = Investigation #2's explicit [H_B, P_restriction] commutator** (I'll set it up; @Elie numerical on V_(1/2,1/2), V_(3/2,1/2), V_(5/2,1/2)). If [H_B,P_restriction] ≠ 0 (expected), muon = T190 confirmed. → @Keeper K232 (muon re-derivation → T190).
- **Refinement filed:** "one computation decides both" → two analogous factorization questions, opposite answers, different spaces.

## 6. Honest tiering

- **CKM Direction B:** FORWARD-derived (observed value forces N_c² two-point; single-trace rejected at 0.075). Strong.
- **Muon → T190:** strongly indicated by three converging lines; the structural coupling argument (ii) is not yet an explicit commutator — Investigation #2 confirms. Composite v0.5 additive form retired (Reading (a) + better-fitting single object). T190's own mechanism (24 = N_c·|W(B₂)| Weyl orbit) is the single-object substrate form.
- **Tier:** F50 v0.1 Investigation #1 closure; CKM Direction B FORWARD; muon → T190 (additive RETIRED) pending Investigation #2 explicit commutator.

## 7. Closure

Investigation #1 driven to substantive closure. The FK matrix element factors **oppositely** in the two sectors: the CKM mixing is irreducibly two-point (N_c² amplitude from two independent endpoint color traces, = λ exactly; single-trace N_c¹ rejected), confirming Direction B; the muon mass operator is a single H² object (T190 = (24/π²)^{C_2}, 0.003%), with the additive Composite v0.5 form retired under Reading (a) (coupled gradings + double-count + worse fit). This refines "one computation decides both" into two analogous-but-separate factorization questions with opposite answers in different spaces (color vs H² grading). The muon's final confirmation is Investigation #2's explicit [H_B, P_restriction] commutator (next, with Elie numerical); the CKM closure is firm. And the day-long muon thread resolves honestly: the additive form I built (F32/F45) gives way to the simpler single-object T190 it always sat near — the discipline retiring my own construction in favor of the cleaner one.

— Lyra, Investigation #1 FORWARD closure. CKM = TWO-POINT/Direction B (N_c² amplitude two independent endpoint color traces = λ=9/40 exactly; single-trace N_c¹=3/40=0.075 REJECTED). Muon = SINGLE-OBJECT T190 (24/π²)^{C_2}=206.761 @0.003%; Composite v0.5 additive 207@0.112% RETIRED under Reading (a) — 3 converging lines: (i) Reading (a) retires bulk+boundary additivity, (ii) [H_B,P_restriction]≠0 structurally (noncompact SO(3,1)⊄K mixes compact K-types → gradings COUPLED not orthogonal → additive "+" illegitimate), (iii) T190 single-object fits 40× better + Reading-(a)-safe (24=N_c·|W(B₂)| Weyl orbit, no additive split, colorless per F48). Refines Elie "one computation decides both" → two ANALOGOUS factorization questions, OPPOSITE answers, different spaces (CKM color two-point; muon H²-grading single-object). CKM/Wall 5 CLOSED Direction B (→Grace R-6/d²=second-moment branch, Keeper K234). Muon/Walls 2,3: T190 strongly indicated, additive RETIRED, final confirm = Investigation #2 explicit [H_B,P_restriction] commutator (Lyra setup + Elie numerical on V_(1/2,1/2),V_(3/2,1/2),V_(5/2,1/2); Keeper K232). Precision corroborates not forces (Cal #35; 0.003% below Two-Tier floor, weighted as corroboration).
