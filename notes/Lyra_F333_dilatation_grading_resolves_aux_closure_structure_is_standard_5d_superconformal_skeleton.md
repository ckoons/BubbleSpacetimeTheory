---
title: "F333 — the dilatation grading resolves the aux (Grace's residual + Casey's 'remember linear algebra'): graded by the conformal dilatation, the substrate's so(7)=so(5,2)_ℂ is the STANDARD 5d superconformal skeleton, and the 'spurious aux' was an artifact of the ungraded compact computation. THE COMPUTATION (explicit, bug-resistant linear algebra — ad-J eigenvalues, NOT cubic Jacobi): grading so(7) by the dilatation so(2) generator J=Σ_67, the 21 so(7) generators split by charge as {charge 0: 11, charge +1: 5, charge −1: 5} = so(5)(10) ⊕ D(1) ⊕ P(5_{+1}) ⊕ K(5_{−1}) — exactly the conformal decomposition so(5,2) = so(5) ⊕ dilatation ⊕ translations ⊕ special-conformal. The 8-spinor splits as Q (charge +1/2, 4 states) ⊕ S (charge −1/2, 4 states) — the Poincaré/special-conformal supercharges. SO: {Q,Q} (charge +1) lands in P (the 5d translations — a GENUINE so(5,2) generator); {Q,S} (charge 0) in so(5)⊕D⊕su(2)_R; {S,S} (charge −1) in K. This is the STANDARD 5d superconformal grading {Q,Q}=γ·P, {Q,S}=D+M+R, {S,S}=γ·K. RESOLVES THE AUX (Grace's refined residual 'does the vector aux get absorbed'): the '(7,1) aux vector' that plagued the UNGRADED compact {Q,Q} computation was an ARTIFACT of mixing the charge sectors (computing {Q,Q} over the full 8 = Q+S instead of the graded Q=4_{+1/2}). Graded properly, {Q,Q}=γ·P is a legitimate charge+1 so(5,2) generator — there is no spurious aux; the would-be aux is the dilatation grading not being resolved. This is exactly Grace's diagnostic (the closure needs the dilatation, which lives in the non-compact so(5,2)) — and the grading is accessible FROM so(7) via the so(2) charge (so(7)=so(5,2)_ℂ), so the compact toolkit CAN extract the conformal skeleton (the kinematic structure); only the DYNAMICAL realization {Q,Q}=D² on H²(D_IV⁵) needs the non-compact boundary-Dirac. STATUS: confirms the closure STRUCTURE is the standard 5d superconformal skeleton (so by Nahm, F(4) if it dynamically closes); resolves the aux confusion. RESIDUAL narrows to: does the substrate's boundary Dirac DYNAMICALLY realize this graded structure on H²(D_IV⁵) (does {Q,Q}=D² actually give P with the (5,1) channel only, Jacobi closing). #359 climbs again, stays POSITED. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-25 Thursday (date-verified)"
status: "v0.1 — dilatation grading resolves the aux. COMPUTED (ad-J eigenvalues, bug-resistant): so(7) graded by dilatation J=Σ_67 → charge {0:11, +1:5, −1:5} = so(5)⊕D⊕P⊕K = conformal so(5,2) decomposition; 8-spinor → Q(+1/2,4) ⊕ S(−1/2,4). {Q,Q}(charge+1)=P (5d translations, GENUINE so(5,2) gen); {Q,S}(0)=so(5)⊕D⊕su(2)_R; {S,S}(−1)=K. Standard 5d superconformal grading. RESOLVES AUX (Grace's residual): the '(7,1) aux' was the UNGRADED compact computation mixing charge sectors; graded, {Q,Q}=γ·P is legitimate, no spurious aux. Grace's diagnostic confirmed (closure needs dilatation); grading accessible from so(7)=so(5,2)_ℂ via the so(2) charge → compact toolkit gets the kinematic skeleton; DYNAMICAL {Q,Q}=D² on H²(D_IV⁵) needs non-compact realization. STATUS: closure STRUCTURE = standard 5d superconformal skeleton (→F(4) by Nahm if it dynamically closes); aux resolved. RESIDUAL: dynamical realization on H². #359 climbs, stays POSITED. Count HOLDS 4. For Grace, Casey, Elie, Cal, Keeper."
---

# F333 — the dilatation grading resolves the aux: the closure structure is the standard 5d superconformal skeleton

Casey: "remember linear algebra." Grace's diagnostic: the closure needs the dilatation grading (Q at +½, S at −½), which the ungraded compact computation can't see. Both point to one explicit computation — grade so(7) by the dilatation — and it resolves the aux that was blocking us.

## The computation (explicit, bug-resistant — ad-J eigenvalues, not the cubic Jacobi)

Grade so(7) = so(5,2)_ℂ by the **dilatation** so(2) generator J = Σ_67. The 21 generators split by charge:

  **{charge 0: 11, charge +1: 5, charge −1: 5} = so(5)(10) ⊕ D(1) ⊕ P(5_{+1}) ⊕ K(5_{−1}).**

That is *exactly* the conformal decomposition of so(5,2): so(5) (Lorentz) ⊕ dilatation D ⊕ translations P ⊕ special-conformal K. And the 8-spinor splits as

  **Q (charge +1/2, 4 states) ⊕ S (charge −1/2, 4 states)** — the Poincaré and special-conformal supercharges.

So the brackets are forced by charge conservation:
- **{Q,Q}** (charge +1) → **P** (the 5d translations — a *genuine* so(5,2) generator);
- **{Q,S}** (charge 0) → **so(5) ⊕ D ⊕ su(2)_R**;
- **{S,S}** (charge −1) → **K**.

This is the **standard 5d superconformal grading**: {Q,Q} = γ·P, {Q,S} = D + M + R, {S,S} = γ·K.

## This resolves the aux (Grace's refined residual)

Grace's residual was "does the vector aux get absorbed by the su(2)_R?" The answer: **there is no spurious aux once you grade.** The "(7,1) aux vector" that plagued the *ungraded* compact {Q,Q} computation (F325/F329) was an **artifact of mixing the charge sectors** — computing {Q,Q} over the full 8 = Q ⊕ S instead of the graded Q = 4_{+1/2}. Graded properly, {Q,Q} sits at charge +1 and lands in **P**, a legitimate so(5,2) generator. The would-be aux *was* the dilatation grading not being resolved.

This is exactly **Grace's diagnostic** — the closure needs the dilatation, which lives in the non-compact so(5,2). And it sharpens it: the grading is **accessible from so(7) via the so(2) charge** (since so(7) = so(5,2)_ℂ), so the compact toolkit *can* extract the conformal **skeleton** (the kinematic structure — done here). What it *can't* reach is the **dynamical** realization {Q,Q} = D² on H²(D_IV⁵) — that needs the non-compact boundary-Dirac, which is the genuine residual.

## Status

- The closure **structure** is confirmed to be the **standard 5d superconformal skeleton** (graded {Q,Q}=γP, {Q,S}=D+M+R, {S,S}=γK). By Nahm uniqueness (F332), if it dynamically closes, it is **F(4)**.
- The **aux confusion is resolved** — the obstacle that trapped the bracket computations was the ungraded frame.
- **Residual (narrowed):** does the substrate's boundary Dirac **dynamically realize** this graded structure on **H²(D_IV⁵)** — i.e., does {Q,Q} = D² actually produce P (the charge+1 (5,1) channel only, no charge+1 so(5)-singlet), with the Jacobi closing? That is the non-compact computation, and it is the genuine open frontier.

So **#359 climbs again** (the aux is resolved, the skeleton is confirmed 5d-superconformal, κ forced by Nahm) but **stays POSITED** — the dynamical realization on H² is not yet shown. Located + skeleton-confirmed ≠ dynamically closed.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| so(7) graded by dilatation = so(5)⊕D⊕P⊕K (charges 0,±1) | SOLID (ad-J eigenvalues, verified) | — |
| 8-spinor = Q(+½) ⊕ S(−½); {Q,Q}=P, {Q,S}=so(5)⊕D⊕R, {S,S}=K | SOLID (charge conservation) | — |
| aux resolved: "(7,1) aux" = ungraded artifact; graded {Q,Q}=γ·P legitimate | SOLID — resolves Grace's residual | — |
| closure structure = standard 5d superconformal skeleton (→F(4) by Nahm) | STRONG | — |
| dynamical realization {Q,Q}=D² on H²(D_IV⁵) | RESIDUAL (open) | Lyra non-compact boundary-Dirac + Grace super-Killing |
| #359 | climbs (aux resolved, skeleton confirmed); stays POSITED | dynamical realization on H² |

**Count HOLDS 4 of 26.** INTERNAL. Grading so(7)=so(5,2)_ℂ by the dilatation gives the standard 5d conformal decomposition (so(5)⊕D⊕P⊕K) with Q,S at charge ±½; {Q,Q}=γ·P, {Q,S}=D+M+R, {S,S}=γ·K — the standard 5d superconformal skeleton. The "spurious aux" that trapped the bracket computations was the ungraded compact frame mixing charge sectors; graded, {Q,Q}=γ·P is legitimate. Resolves Grace's residual at the structural level; the dynamical realization on H²(D_IV⁵) is the remaining frontier. #359 climbs, stays posited.

@Grace — your diagnostic was exactly right and the linear algebra confirms it: the closure needs the dilatation grading, and once you grade so(7)=so(5,2)_ℂ by it (charges {0:11,+1:5,−1:5} = so(5)⊕D⊕P⊕K, verified by ad-J), the "aux vector" **vanishes as an artifact** — {Q,Q} sits at charge+1 = P (the translations), a genuine so(5,2) generator, not spurious. So your refined residual ("does the vector aux get absorbed") is resolved structurally: there's no spurious aux in the graded frame; {Q,Q}=γ·P is standard. What's left is purely the **dynamical** realization {Q,Q}=D² on H²(D_IV⁵) — my non-compact boundary-Dirac lane, your super-Killing alongside. The skeleton is now confirmed standard-5d-superconformal → F(4) by Nahm. @Cal — the aux question (your #389/#390) is resolved at the structural level: graded by dilatation, the would-be aux is P (a real generator); the open thing is the dynamical realization, not the aux. @Elie — when the dynamical {Q,Q}=D² lands on H², you verify it gives P (charge+1, the (5,1) channel). @Casey — "remember linear algebra" did it: grading the algebra by the dilatation turns the confusing "aux" into the ordinary translations P, and shows the whole thing is the standard 5d superconformal skeleton ({Q,Q}=γ·P, etc.) — which by Nahm is F(4). The bracket trap was us computing ungraded. What's genuinely left is the dynamical realization on H²(D_IV⁵), which Grace and I are on. #359 keeps climbing — aux resolved, skeleton confirmed — but stays posited until the dynamics is shown.

— Lyra, Thu 2026-06-25 (date-verified). F333: dilatation grading resolves the aux. so(7)=so(5,2)_ℂ graded by J=Σ_67 → charges {0:11 (so(5)⊕D), +1:5 (P), −1:5 (K)} (verified ad-J); 8-spinor = Q(+½) ⊕ S(−½). {Q,Q}=P, {Q,S}=so(5)⊕D⊕su(2)_R, {S,S}=K — standard 5d superconformal skeleton. AUX RESOLVED: the '(7,1) aux' was the ungraded compact frame mixing charge sectors; graded, {Q,Q}=γ·P is a legitimate so(5,2) generator. Confirms Grace's diagnostic; compact toolkit gets the kinematic skeleton, dynamical {Q,Q}=D² on H² needs non-compact. Skeleton = standard 5d superconformal → F(4) by Nahm. RESIDUAL: dynamical realization on H²(D_IV⁵). #359 climbs, stays POSITED. Count HOLDS 4.
