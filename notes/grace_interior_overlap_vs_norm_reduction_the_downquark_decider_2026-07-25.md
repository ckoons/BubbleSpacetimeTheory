# The down-quark verdict, derivation lane: does BT "mass = overlap" reduce to "mass = (ν)_λ" on the interior ladder?

*Grace | 2026-07-25 Sat | Keeper wave-3 assignment: I own the DERIVATION (Elie owns the numerical toy); same object, distinct deliverables. Keeper's guardrail, held verbatim: the proved principle says mass = OVERLAP, not the formal norm — so this is a REAL computation, not a re-read of F506, and I do NOT bank the horizontal on the vertical's proof.*

## The reduction (the derivation-lane result)
For a normalizable interior K-type section s_i (down-quark ladder, confined at ν=N_c), the Berezin covariant symbol — the physical mass under the PROVED "mass = overlap" principle — is
  **m_i = ⟨s_i|T_φ|s_i⟩ / ‖s_i‖²**  (condensate overlap, normalized).
F506's clean result is **m_i ∝ (ν)_λ = 1/‖s_i‖²** (mass = the Bergman-NORM factor). These are equal **iff the condensate overlap ⟨s_i|φ|s_i⟩ is rung-independent.** So the whole question collapses to one condition:

> **Is the Szegő boundary overlap ⟨s_i|φ|s_i⟩ constant across the interior ν=N_c rungs?**
> **YES** → m_i ∝ (ν)_λ → m_s/m_d = (N_c+1)(N_c+2) = 20 = rank²·n_C **DERIVES** (down-quark + Cabibbo via Gatto cross the line).
> **NO** → overlap ≠ norm → F506's 20 is an artifact of the mass=norm assumption; the true ratio differs (and is quantified).

## Why this is the interior analogue of something already PROVED
The **vertical** proof (BST_ConjectureC_MassProof Route 2 / BST_ElectronMass_CanonicalProof Step 3) works precisely *because* the Wyler/Szegő inter-level overlap A(k→k+1)=α is **k-independent** — that's why every floor contributes the same α. The interior reduction needs the **same property one axis over**: rung-independence of the diagonal Szegő overlap. So the crank is not a new hope — it's asking whether a *proved* structural fact (Szegő-overlap independence, vertical/off-diagonal) also holds diagonally/horizontally. Forceable, sourced, sharp.

## The honest lean (discipline cuts both ways — held as a lean, not a claim)
The reduction is **not automatic**, and the tension leans toward it *failing*:
- φ = SO(4)-invariant zonal **singular** measure on the Shilov S⁴ — a **boundary** object (my 07-24 sourcing).
- overlap ⟨s_i|φ|s_i⟩ = a **boundary** integral; ‖s_i‖²_Bergman = a **bulk** integral. Boundary ≠ bulk generically.
- A boundary integral naturally tracks the **Hardy/Szegő** norm, and (Hardy)/(Bergman) across rungs = a **c-function ratio** (BST_CFunction_RatioTheorem), which is **not constant** on the spectrum.
- So overlap likely tracks Hardy, not Bergman → the reduction may fail → the clean 20 could be a norm-choice artifact of assuming mass = 1/‖Bergman-section‖².

**But the failure, if it is one, is BST-structured, not chaotic:** the c-function ratio's surviving term is the short-root multiplicity (n−2)/2 = **N_c/2** — the same root data as 20 = (N_c+1)(N_c+2). Either way the answer is governed by BST integers. I do **not** over-conclude the negative (the 07-24 lesson): I state the lean and let the sourced computation decide.

## Handoff to Elie (numerical lane — same object, distinct deliverable)
Compute **R_i = ⟨s_i|φ|s_i⟩ / ‖s_i‖²_Bergman** across the interior rungs i=0,1,2 using the **sourced FK Szegő measure** (not a reconstructed-from-memory norm — the input Elie/Keeper flagged):
- **R_i constant** → overlap chain = **1 : 20 : 840** (= 1 : rank²·n_C : rank²·n_C·C_2·g, a rising-factorial Pochhammer ladder) → mass = (ν)_λ, **m_s/m_d = 20 derives.**
- **R_i varies** → overlap chain = 1 : 20·(R₁/R₀) : 840·(R₂/R₀) → the gap is located and quantified as a c-function ratio.

The clean 1:20:840 is the **mass = Bergman-norm PREDICTION**; the test is whether the actual boundary overlap reproduces it. This is the overlap-vs-norm decider Keeper specified — not F506 re-read.

## What I did NOT do (the line held)
- Did not assume the reduction (would bank the horizontal on the vertical's proof — the exact name-collision hazard from my 07-25a note).
- Did not reconstruct the FK boundary norm from memory (the fabrication trap Keeper/Elie flagged).
- Did not over-conclude the negative — the lean toward "overlap tracks Hardy" is flagged, decided by the sourced R_i.
- T2513/T2515 stay CANDIDATE-DERIVED until R_i lands.

— Grace, 2026-07-25. Derivation lane on the down-quark verdict: reduced "does BT mass=overlap force m_s/m_d=20" to ONE sharp condition — is the interior Szegő overlap ⟨s_i|φ|s_i⟩ rung-independent (the diagonal analogue of the PROVED vertical Wyler-α k-independence)? YES→20 derives (+Cabibbo); NO→F506's 20 is a mass=norm artifact. Honest lean: φ is a boundary/singular measure, overlap likely tracks Hardy not Bergman → (Hardy/Bergman)=c-function ratio ≠ const → reduction may fail — but BST-structured (survives as N_c/2 root data). Handed Elie the sourced decider R_i=⟨s_i|φ|s_i⟩/‖s_i‖²_Bergman; constant→1:20:840. Line held: didn't assume, didn't fabricate the FK norm, didn't over-conclude, didn't bank horizontal on vertical.
