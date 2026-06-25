---
title: "F329 — κ cross-check (Grace's ±3=N_c candidate): I independently CONFIRM the structural skeleton via explicit Clifford matrices, report a genuine new finding (the Killing form DEGENERATES on the sl(2) factor), and HONESTLY do NOT bank |κ|=3 — the bracket-magnitude needs the literature pin or a careful conformal closure I have not completed. CONFIRMED (explicit matrices, bug-resistant traces, NOT the trapping cubic Jacobi): (1) index(so(7) spinor 8) = 2 — computed as tr(Σ²)_spinor / tr(Σ²)_vector = (−42)/(−42) = 1, so index(8) = index(7) = 2 (standard B_3 value). (2) index of the odd (8,2) under so(7) = index(8)·dim(2) = 2·2 = 4; under sl(2) = index(2)·dim(8) = (1/2)·8 = 4 — the indices BALANCE at 4 (confirms Grace). (3) h^∨(so(7)) = h^∨(B_3) = 5 = n_C (Grace's anchor, confirmed). NEW FINDING: the F(4) Killing form B(X,X) = str(ad_X²) on the even part gives B|so(7) = 2h^∨(so7) − I_odd,so7 = 10 − 4 = 6, and B|sl(2) = 2h^∨(sl2) − I_odd,sl2 = 4 − 4 = 0 — the Killing form DEGENERATES on the sl(2) factor (sl(2) at 'critical level'). This is why the naive Killing-ratio route can't read off κ (it's 6/0), and part of why the cubic-Jacobi routes are delicate (3 independent failures: Elie, Lyra, Grace). NOT BANKED: |κ| = 3 = N_c. I confirmed the SKELETON Grace's number rests on (indices=4, h^∨(so7)=n_C=5), but converting to the bracket-κ coefficient (3 vs 1/3) requires either the cubic Jacobi (trapped everyone) or a careful invariant-form/conformal treatment I have NOT completed. Deriving '5−2=3' by reverse-engineering Grace's answer would be back-solving (forbidden). FLAGGED-NOT-BANKED (target-innocence NOT cleared): B|so(7) = 6 = C_2 (a BST primary), forced by 2h^∨(so7)−I_odd with h^∨(so7)=n_C=5 — intriguing but a single coincidence, needs the Schur-generator check before it means anything. RECOMMENDATION: the decisive third leg is the LITERATURE PIN on F(4)'s κ (Grace flagged it); I continue the careful conformal {Q,S}/{S,S} closure as the genuine independent route, but will not produce a κ number until it lands clean. κ-magnitude OPEN; #359 posited. Count HOLDS 4."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-25 Thursday (date-verified)"
status: "v0.1 — κ cross-check: skeleton CONFIRMED, magnitude NOT banked. CONFIRMED (explicit matrices): index(8)=2, index of odd under so(7)=under sl(2)=4 (balance), h^∨(so7)=5=n_C. NEW: Killing form DEGENERATES on sl(2) — B|sl2 = 2·2−4 = 0 (critical level); B|so7 = 10−4 = 6. Explains why Killing-ratio can't give κ and why cubic-Jacobi traps (3 failures). NOT BANKED: |κ|=3=N_c — skeleton confirmed but bracket-coefficient (3 vs 1/3) needs literature pin or careful conformal closure (not done); reverse-engineering 5−2=3 = back-solving (forbidden). FLAGGED-NOT-BANKED: B|so7=6=C_2 (forced by 2h^∨(so7)−I_odd, h^∨=n_C=5) — single coincidence, Schur-check needed. NEXT: literature pin (Grace's 3rd leg) + careful conformal {Q,S}/{S,S}. κ OPEN; #359 posited. Count HOLDS 4. For Grace, Casey, Elie, Cal, Keeper."
---

# F329 — κ cross-check: skeleton confirmed, Killing form degenerates on sl(2), magnitude not banked

Grace delivered a candidate |κ| = 3 = N_c via the super-Killing route and asked me to cross-check it independently. Here is what I can confirm rigorously, a genuine new finding, and an honest statement of what I cannot yet confirm.

## Confirmed (explicit Clifford matrices, bug-resistant — NOT the trapping cubic Jacobi)

Using the verified 8-dim so(7) spinor matrices (F325):

1. **index(so(7) spinor 8) = 2.** Computed as the ratio tr(Σ²)_spinor / tr(Σ²)_vector = (−42)/(−42) = 1, so the spinor and vector have equal index, = 2 (the standard B_3 value).
2. **The indices balance at 4.** Index of the odd (8,2) under so(7) = index(8)·dim(2) = 2·2 = **4**; under sl(2) = index(2)·dim(8) = (1/2)·8 = **4**. (Confirms Grace's "indices balance at 4.")
3. **h^∨(so(7)) = h^∨(B_3) = 5 = n_C** (Grace's anchor, confirmed).

So the **structural skeleton** Grace's result rests on is independently verified.

## New finding — the Killing form degenerates on the sl(2) factor

The F(4) Killing form B(X,X) = str(ad_X²) restricted to the even simple factors (using B|_factor = 2h^∨_factor − I_odd,factor in index units):

- **B|so(7) = 2·5 − 4 = 6.**
- **B|sl(2) = 2·2 − 4 = 0.** — the Killing form **degenerates on the sl(2) factor** (the sl(2) sits at "critical level," 2h^∨ = I_odd).

This is informative: it explains why the **naive Killing-ratio route cannot read off κ** (the ratio is 6/0), and it is part of why the **cubic-Jacobi routes are delicate** — three independent careful attempts (Elie 4382, my F325, Grace's) all trapped on it. The sl(2)-criticality is a genuine structural feature of F(4) here, not a bug.

## NOT banked — |κ| = 3

I **confirmed the skeleton** (indices = 4, h^∨(so7) = n_C = 5), but I have **not** independently derived the bracket-κ **coefficient**. Converting the index/Coxeter skeleton to the actual {Q,Q}/{Q,S} structure constant (and resolving 3 vs 1/3) requires either:
- the cubic graded Jacobi (which trapped all three of us), or
- a careful invariant-form / conformal {Q,S}/{S,S} treatment that I have **not** completed.

Deriving "5 − 2 = 3" by reverse-engineering Grace's answer would be **back-solving** — exactly the discipline we held all day. So I am **not** banking |κ| = 3 = N_c. The magnitude is a strong candidate (Grace's super-Killing route) with the skeleton independently confirmed, but the bracket-coefficient is **open** pending a genuine independent derivation.

## Flagged, not banked (target-innocence NOT cleared)

**B|so(7) = 6 = C_2** (a BST primary). It is forced by 2h^∨(so7) − I_odd = 10 − 4, with h^∨(so7) = n_C = 5 — so in that sense target-innocent (no fitting). But it is a **single coincidence** on a small integer; per today's discipline (pleasing numbers bite), it needs the Schur-generator check before it means anything. Noting it as a lead, not a result.

## Recommendation / next

- **Literature pin** on F(4)'s κ (Grace's flagged third leg) is the cleanest decisive check — F(4)'s structure constants are classified; pinning the published value settles 3 vs 1/3 and confirms-or-refutes the BST reading.
- I continue the **careful conformal {Q,S}/{S,S} closure** as the genuine independent route, but will produce a κ number only when it lands clean — not another fast attempt after today's bug.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| index(8)=2, indices balance at 4, h^∨(so7)=5=n_C | SOLID (explicit matrices) — confirms Grace skeleton | — |
| Killing form degenerates on sl(2): B|sl2=0, B|so7=6 | SOLID (new finding) | explains Killing-ratio & cubic-Jacobi delicacy |
| \|κ\| = 3 = N_c | NOT BANKED — skeleton confirmed, bracket-coeff open | literature pin + careful conformal closure |
| B\|so7 = 6 = C_2 | FLAGGED, not banked (single coincidence) | Schur-generator check |
| κ-magnitude / #359 | OPEN / posited | conformal {Q,S}/{S,S} (Lyra) + lit pin (Grace) |

**Count HOLDS 4 of 26.** INTERNAL. Independently confirmed the skeleton of Grace's κ candidate (indices=4, h^∨(so7)=n_C=5, via explicit matrices), found that the Killing form degenerates on sl(2) (explaining the route's delicacy), and honestly did NOT bank |κ|=3 — the bracket-coefficient needs the literature pin or a careful conformal closure I haven't completed. κ-magnitude open; #359 posited.

@Grace — cross-checked your candidate: your **skeleton is independently confirmed** (index(8)=2, indices balance at 4, h^∨(so7)=n_C=5 — all from explicit matrices). New finding that's relevant: the **Killing form degenerates on the sl(2)** (B|sl2 = 2·2−4 = 0, critical level; B|so7 = 6), which is why a clean Killing ratio doesn't directly give κ and why the cubic routes are delicate. But I am **not** banking |κ|=3 — I confirmed what your number rests on, not the bracket-coefficient itself (3 vs 1/3 unresolved), and deriving 5−2=3 from your answer would be back-solving. I think the **literature pin is the decisive third leg** now (cleaner than another bracket attempt); I'll keep on the careful conformal {Q,S}/{S,S} route in parallel. @Elie — the 3 cubic-Jacobi failures have a structural reason: the sl(2) is at critical level (Killing-degenerate), so the bracket is genuinely delicate there. @Cal — discipline note: I confirmed the skeleton but explicitly did NOT bank |κ|=3 (back-solving guard), and flagged B|so7=6=C_2 as a single coincidence not a result (target-innocence not cleared). @Casey (for when you're back) — on the κ cross-check you routed me: I independently confirmed the structural skeleton of Grace's ±3=N_c (the indices and the so(7) dual Coxeter = n_C, via explicit matrices), and found a clean reason the computation keeps trapping (the sl(2) is at critical level, Killing-degenerate). But I did not bank the |κ|=3 value — that needs the literature pin or a careful conformal closure I won't rush. The skeleton is real and matches Grace; the specific number stays a strong candidate, not confirmed.

— Lyra, Thu 2026-06-25 (date-verified). F329: κ cross-check. CONFIRMED (explicit matrices): index(8)=2, odd-indices balance at 4, h^∨(so7)=5=n_C (Grace's skeleton). NEW: Killing form DEGENERATES on sl(2) (B|sl2=2·2−4=0, critical level; B|so7=10−4=6) — explains Killing-ratio failure + cubic-Jacobi delicacy (3 failures). NOT BANKED: |κ|=3=N_c (skeleton confirmed, bracket-coefficient open; reverse-engineering 5−2=3 = back-solving). FLAGGED: B|so7=6=C_2 (single coincidence, Schur-check needed). NEXT: literature pin (Grace's 3rd leg) + careful conformal {Q,S}/{S,S}. κ OPEN; #359 posited. Count HOLDS 4.
