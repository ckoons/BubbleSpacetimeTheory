---
title: "F260 — probe of bulk-color v0.6/v0.7 (Casey 'probe 0.6'), read from the actual files (not memory). FINDING: v0.6's count + Cartan-Weyl organization (8 = 3 T_a + 3 T_a^† + 2 K-Cartan) is sound as a COUNT; but v0.7's FRAMING — 'substrate so(5) → effective A_2 = su(3) by suppressing the B_2 long-extended root α_1+2α_2' — is OBSTRUCTED by F258 and must be dropped. THREE probe results: (1) The 'B_2 → A_2 by deleting the long root' story works FORMALLY at the root-combinatorics level (deleting α_1+2α_2 makes [E_{α_2},E_{α_1+α_2}]=0, matching A_2's vanishing), BUT it is NOT a subalgebra map: so(5) is SIMPLE (no ideal to quotient), and F258 proves su(3) ⊄ so(5) rigorously (no faithful real rep ≤ 5). So 'suppression' cannot be an so(5) reduction; it MUST be an honest operator statement on H². (2) RECONCILED with F258/F259: the Toeplitz operators live on the infinite-dim Hardy space H², where an su(3) operator algebra CAN exist even though su(3) ⊄ so(5) — so v0.6/v0.7's operator layer is COMPATIBLE; only v0.7's 'so(5)-reduction' LANGUAGE is wrong. The correct home is F259's INTERNAL su(3) ⊂ g_2 ⊂ so(7)_C, commuting with so(5,2). (3) LEAD: v0.7's Channel-1 Toeplitz symbol |z|^g uses g = 7; F259 identifies 7 = the G_2 fundamental (7 = 3⊕3̄⊕1 under su(3)). So the 'g = 7' doing the suppression may be the G_2-fundamental dimension (the color-singlet '1' direction stabilized), NOT the SO(5,2) embedding dimension — a possible mechanism-identification worth testing. NET: v0.6/v0.7 stays CANDIDATE; the path to rigorous = (i) DROP the so(5)-reduction framing (F258-obstructed), (ii) prove the Toeplitz operators close as su(3) on H² (v0.6 sec-2, still open, Elie's never-run multi-week target), (iii) show the su(3) is INTERNAL (commutes with so(5,2)) via the F259 g_2-stabilizer origin. The g=7/rank=2 falsifiers (F-bulk-1/2) remain good and remain UN-run."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-21 Sunday 12:42 EDT"
status: "v0.1 — probe of bulk-color v0.6/v0.7 against F258/F259. v0.6 count/organization SOUND. v0.7 'so(5)→A_2 reduction' FRAMING OBSTRUCTED (F258: su(3)⊄so(5); so(5) simple). RECONCILE: Toeplitz su(3) on H² is compatible (operator algebra, not subalgebra); correct home = F259 internal g_2-stabilizer su(3) commuting with so(5,2). LEAD: g=7 in Channel-1 symbol may be the G_2-fundamental dim (7=3⊕3̄⊕1), not the embedding dim. Path to rigorous: drop reduction framing + prove operator closure (open) + show internality. Falsifiers un-run. Count HOLDS 4, SU(3) scope. For Casey, Grace, Elie, Cal, Keeper."
---

# F260 — Probing bulk-color v0.6/v0.7: the operator layer is sound, the so(5)-reduction framing is obstructed

Casey: "probe 0.6." Read v0.6 (Structural Closure Check) and v0.7 (Mechanism Deepening) from the files. The honest result: the **count and Cartan-Weyl organization survive**, the **"reduce so(5) to su(3)" framing does not** (F258 kills it), and reconciling the two points the program to F259's internal-g_2 picture.

## What v0.6/v0.7 actually claim

- **v0.6:** the SU(3) octet is 8 = 3 T_a (SO(3)-vector Toeplitz raising) + 3 T_a^† (lowering) + 2 K-Cartan, structurally aligned with su(3)'s 6 root vectors + 2 Cartan. Closure (the actual su(3) commutators) flagged OPEN, multi-week.
- **v0.7:** the mechanism is "substrate so(5) (B_2) → effective A_2 = su(3)" by **suppressing the long-extended root α_1+2α_2** via a Hardy Toeplitz operator T_{|z|^g} (Channel 1, g=7) plus a Cartan rescaling by rank=2 (Channel 2). Falsifiers F-bulk-1 (only g=7 works) and F-bulk-2 (only rank=2 works) set; Elie verification multi-week.

## Probe result 1 — the "B_2 → A_2 by deleting the long root" is formally suggestive but NOT a subalgebra map

At the **root-combinatorics** level the story is tidy: B_2 has roots {±α_1, ±α_2, ±(α_1+α_2), ±(α_1+2α_2)}, and the obstruction to su(3) is the structure constant [E_{α_2}, E_{α_1+α_2}] = ±2 E_{α_1+2α_2} ≠ 0. **Delete α_1+2α_2** and this bracket vanishes — exactly matching A_2, where [E_{β_2}, E_{β_1+β_2}] = 0 (since β_1+2β_2 is not an A_2 root). So formally, "kill the long-extended root" turns B_2 Chevalley relations into A_2 Chevalley relations.

**But this is not a Lie-algebra operation.** so(5) is **simple** — there is no ideal to quotient by, so you cannot "set E_{α_1+2α_2} = 0" and stay a homomorphism (Jacobi fails). And F258 settles it rigorously: **su(3) ⊄ so(5)** (su(3)'s smallest faithful real rep is 6-dimensional; the so(5) vector 5 cannot carry a faithful su(3) action). **So there is no su(3) subalgebra of so(5) to land on by any "suppression."** The B_2→A_2 deletion is a mnemonic for the *target* structure, not a derivation of it.

## Probe result 2 — reconciled: the Toeplitz operators live on H², where this is fine

The rescue is that v0.6/v0.7's su(3) is built from **Toeplitz operators on the infinite-dimensional Hardy space H²**, not from elements of so(5). An su(3) **operator algebra** on H² is **not** constrained by "su(3) ⊄ so(5)" — that obstruction is about finite-dimensional subalgebras / geometric isometries, not about operator algebras on an infinite-dimensional function space. So **the operator layer is compatible with F258**; what is wrong is only v0.7's **language** ("so(5) → A_2 reduction"), which imports the impossible subalgebra picture. The correct home for the resulting su(3) is **F259's internal su(3) ⊂ g_2 ⊂ so(7)_C = so(5,2)_C**, acting on H² and **commuting with the geometric so(5,2)** (internal, as a gauge symmetry must be) — not a piece of the so(5) inside K.

**Concretely, the reframe:** keep v0.6's {T_a, T_a^†, K-Cartan} octet and the closure question; **discard** v0.7's "suppress the so(5) long root to reduce B_2→A_2"; **replace** it with "the Toeplitz octet realizes the internal su(3) ⊂ g_2 (the G_2-stabilizer of the color singlet) on H²." The closure question (v0.6 sec 2) is then: do the Toeplitz commutators reproduce the su(3) ⊂ g_2 structure constants? — same open computation, correct framing.

## Probe result 3 — a LEAD on the g = 7 (flagged, not claimed)

v0.7's Channel 1 uses the Toeplitz symbol |z|^g with **g = 7 = the SO(5,2) embedding dimension**. But F259 gives 7 a *second* meaning: **7 = the G_2 fundamental** (7 = 3 ⊕ 3̄ ⊕ 1 under su(3), with the **1** = the color singlet whose G_2-stabilizer is su(3)). So the "g = 7" doing the suppression in Channel 1 may actually be the **G_2-fundamental dimension** — the operator picking out the color-singlet direction in the 7 — rather than the embedding dimension. If so, F-bulk-1 ("only g=7 works") would pass *for a structural reason* (it's the G_2 fundamental), not as a tuned exponent. This is a **lead**: it connects v0.7's empirically-motivated g=7 to F259's G_2 mechanism. I have not shown the Toeplitz symbol |z|^7 implements the G_2-singlet projection; that's the test.

## What this does to the tier

v0.6/v0.7 stays **CANDIDATE** (as it always was — closure was openly flagged multi-week). The probe **sharpens the path to rigorous** and removes a dead branch:

1. **DROP** the "so(5) → A_2 reduction" framing (F258-obstructed; not a subalgebra map).
2. **PROVE** the Toeplitz octet {T_a, T_a^†, K-Cartan} closes as su(3) on H² (v0.6 sec 2 — the load-bearing open computation; Elie's multi-week target, **never run** — the toys v0.7 routed to (3661+) went to other work).
3. **SHOW** the su(3) is **internal** (commutes with so(5,2)), via the F259 g_2-stabilizer origin — this is the new structural anchor the old program lacked.
4. The **g=7 / rank=2 falsifiers** (F-bulk-1, F-bulk-2) remain good tests and remain **un-run**; probe-result-3 gives F-bulk-1 a candidate structural reason (G_2 fundamental).

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| v0.6 octet count + Cartan-Weyl organization (8 = 3+3+2) | SOUND (count) | — |
| v0.7 "so(5) → A_2 by deleting the long root" as a subalgebra map | OBSTRUCTED (F258; so(5) simple) | DROP framing |
| Toeplitz su(3) on H² compatible with F258 (operator algebra, not subalgebra) | SOLID (reconciliation) | reframe to internal |
| correct home = internal su(3) ⊂ g_2 ⊂ so(7)_C, commuting with so(5,2) | SOLID (F259) | — |
| Toeplitz octet closes as su(3) on H² | OPEN (v0.6 sec 2, never run) | Elie multi-week, correctly framed |
| g=7 = G_2 fundamental doing the Channel-1 projection | LEAD (unproven) | test |z|^7 = G_2-singlet projection |

**Count HOLDS 4 of 26.** SU(3) scope. The probe keeps v0.6/v0.7 at CANDIDATE, removes the F258-obstructed reduction framing, reconciles the operator construction with today's findings, and re-anchors it on F259's internal g_2-stabilizer su(3). The single load-bearing open computation (does the Toeplitz octet close as su(3)?) is unchanged and still un-run. INTERNAL.

@Casey — probed v0.6/v0.7 from the files. The good news: the operator construction (8 Toeplitz generators) is fine and compatible with today's no-geometric-color finding. The correction: v0.7's story that you "shrink so(5) down to su(3) by deleting a root" can't be right — so(5) is simple and (F258) just doesn't contain su(3); that "reduction" was a mnemonic for the answer, not a derivation. The right picture is the one F259 found: the su(3) is *internal*, living in g_2 inside the complexified geometry, realized by operators on the Hardy space that commute with spacetime. And a genuine lead fell out: the "g = 7" that v0.7 uses to do the suppression is probably the G_2 fundamental's dimension (7 = 3⊕3̄⊕1), not the embedding dimension — which would explain *why* 7 and not 5 or 6. The one computation that actually decides bulk-color — do the eight Toeplitz operators close into su(3)? — was flagged open in 2026-05 and was never run. That's the real #418 frontier. @Elie — the closure computation (v0.6 sec 2) is the load-bearing one and the framing is now corrected (internal g_2-stabilizer su(3) on H², not so(5) reduction); when you're free of the p-form build this is the genuine color target. @Grace — does the corpus carry a G_2 / octonionic / 3-form structure on the g=7 object? That's what probe-result-3 needs. @Cal/@Keeper — no new claim banked; SOLID parts are the F258 reconciliation; the g=7=G_2-fundamental is a flagged LEAD.

— Lyra, Sun 2026-06-21 12:42 EDT (date-verified). F260: probe bulk-color v0.6/v0.7 (from files). v0.6 octet count SOUND. v0.7 "so(5)→A_2 by deleting B_2 long root" OBSTRUCTED — formally turns B_2 Chevalley into A_2 ([E_{α_2},E_{α_1+α_2}]→0) but is NOT a subalgebra map (so(5) simple; F258: su(3)⊄so(5)). RECONCILED: Toeplitz su(3) on infinite-dim H² is compatible (operator algebra ≠ subalgebra); correct home = F259 internal su(3)⊂g_2⊂so(7)_C commuting with so(5,2); DROP the reduction framing. LEAD: Channel-1 g=7 symbol may be the G_2-fundamental dim (7=3⊕3̄⊕1, singlet projection), not embedding dim — would explain F-bulk-1. Path to rigorous: drop framing + prove Toeplitz closure as su(3) on H² (open, never run) + show internality via g_2-stabilizer. Count HOLDS 4.
