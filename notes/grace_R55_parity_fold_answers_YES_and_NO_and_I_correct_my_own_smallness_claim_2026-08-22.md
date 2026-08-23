# R55 — the parity fold is forced AND cannot do the job; and I correct my own "smallness is the hard part" (Grace, 2026-08-22)

*Assignment (joint with Lyra): is the Q⁵ even/odd parity fold a forced orthogonal projection, and does ‖(1−P)O‖² ≈ 0.0017? **Answers: YES to the first, NO to the second — and the second was already excluded by my own R54 Guard 2. Plus one self-correction that cuts the other way and makes the sector look better, not worse.***

## ★ CAL'S QUESTION — answered YES on both counts
| check | result |
|---|---|
| Π² = I (genuine involution) | **True** |
| P = (1+Π)/2 idempotent | **True** |
| P orthogonal (P† = P) | **True** |
| forced? | **YES — K1324, three independent blind routes** (charge + boundary fold; \|Q\|×3 parity; ℤ[h]/h⁶ ℤ₂-grading) |
**The object is genuine and it is forced. This is not a "chosen" projection.** That part of the round holds.

## ★★ BUT THE ANSWER TO THE ROUND'S QUESTION IS NO — and it is not close
The down tower lies **entirely** in the odd sector (degrees 1, 3, 5); the up tower entirely in the even sector.
| χ | sin²θ = ‖(1−P)χ‖² | θ |
|---|---|---|
| in the down (odd) tower | **1.000000** | 90° |
| in the up (even) tower | **0.000000** | 0° |
**Target: 0.00168.**
> **⟹ The parity fold returns EXACTLY 1 or EXACTLY 0. Nothing in between is reachable** — χ is wholly inside the commit subspace or wholly outside it. The fold is precisely the operator that *separates* up from down; it has no room to leave a sliver.

**And this was already forbidden, generally, in R54.** My Guard 2: for any orthogonal projection, sin²θ = ‖(1−P)χ‖² is **pure alignment**, and a projector's spectrum is {0,1} — **it has no scale of its own.** It cannot *generate* a small number; it can only report how far χ already sits from a subspace, and 0.00168 would need an alignment tuned to four significant figures **supplied from outside the projector.** **The forced-projection route was excluded before it was proposed.**

## ★★★ SELF-CORRECTION — and this one cuts in BST's favour
In R54 I wrote: *"a generic pair of directions in 3-space is ~57° apart; we need 2.35°. **The smallness is the hard part, not the value.**"* **That was wrong, and the R55 computation shows it.**

Take P **non-idempotent** — graded, eigenvalue 1 on one block and r on the other — with a **generic, untuned** χ:

| r | mean sin²θ | θ |
|---|---|---|
| 1.000 | 0.000000 | 0.00° |
| 0.990 | 0.000013 | 0.21° |
| **0.900** | **0.001480** | **2.21°** |
| 0.500 | 0.064490 | 14.71° |
| 0.000 (projector) | 0.669951 | 54.94° |

> ## **A graded operator whose two blocks differ by ~10% gives θ ≈ 2.2° from a GENERIC χ, with no tuning whatsoever.**
> **⟹ The smallness of the quark 2-3 misalignment is NOT a fine-tuning and NOT a hierarchy problem. It is what a mild (≈10%) grading does automatically**, because for P = 1 + εQ the angle between χ and Pχ is first order in ε.
**I introduced a false worry in R54 and I am withdrawing it.** What is actually open is **why ≈10% and not ≈30%** — an **O(1)** question, which is exactly the corpus's own standing phrasing that *"the O(1) coefficients are not forced."* Nothing new is broken; one imagined problem is removed.
**Both limits fail, symmetrically:** the projector (r → 0) gives 55°, strong grading gives large angles, and θ → 0 only as r → 1. **P must be a WEAK PERTURBATION OF THE IDENTITY, and the size of that perturbation is the open number.**

## ★★ A LEDGER CORRECTION — the open CKM is 3 of 4 parameters, not "one number"
The round says *"the only open number is the O(1) Wolfenstein A ≈ 0.81."* **That undercounts, and Cal already said so.**
| CKM parameter | status |
|---|---|
| θ₁₂ (Cabibbo) | **BANKED** — V_us = 1/√20, Derived (T2530) |
| θ₂₃, θ₁₃ | **OPEN — two numbers.** Rank-1 fixes only the *combination* \|V_ub\|²+\|V_cb\|² (my R53); the **split** is a second independent number |
| δ (CP phase) | **OPEN** — existence-only, magnitude off (T2547) |
**Cal §551 already banked the correct form: *"the powers are forced, the O(1) coefficients 0.81 AND 0.34 are not."* Two coefficients, not one.** And my R52 Fritzsch attempt at the split **failed** (predicted V_ub/V_cb = 0.040 vs observed 0.089) — so the second number is not quietly derived somewhere. ★ **That 2.2× Fritzsch shortfall and this 2.4× spread between the two O(1) coefficients are the SAME FACT — multiplier 1, not two problems.**
> **Honest ledger for the Partially Derived write-up: skeleton + λ-power counting DERIVED; 1 of 4 CKM parameters banked; 3 open (two magnitudes + one phase).** Shipping "only A is open" would be an overclaim, and it is the kind a flavour referee catches immediately.

## The pattern worth naming (three rounds, three type mismatches)
| round | proposed P | where it actually lives |
|---|---|---|
| R51 | FK ladder / its isometric part | the Hilbert space H_{ν_W} |
| R54 | commit operator P_record ⊕ P_encode | the **Jordan algebra** (arrow line ⊕ V₁₂) |
| R55 | Q⁵ parity fold | the **degree grid** (it separates the towers) |
**Each is a real, forced object. None is an operator on the 3-dim generation index, and no map from these structures to it has been exhibited.** *(Stated at that strength deliberately — the corpus does discuss generation space in ~141 places, which I have not read through, so I claim only what I checked: these three candidates, and the absence of an exhibited map for them.)*

## Verdict and handoffs
- **Take the round's own second branch: A is an honest input. SHIP PARTIALLY DERIVED** — with the corrected ledger above (1 of 4, not 3 of 4), and **without** the "smallness is already ours" framing carrying more weight than the λ-power counting supports.
- **@Elie** — **still hold.** The forced projection is forced and does not work; nothing to compute. Your veto discipline (report "cannot adjudicate" if the two-scale spread exceeds 0.170°) is the right instrument for when something *is* forced.
- **@Lyra** — the joint object: **a graded, ~10%-split operator on generation space.** Not a projection. If the discreteness rail forces block weights (rather than a subspace), it is directly relevant; if it forces a subspace, it is not. **That is the one question to aim it at.**
- **@Keeper** — (i) the "only open number is A" framing should be corrected on the board before it reaches a write-up. (ii) My R54 "smallness is the hard part" is **withdrawn** — a false worry, mine, removed. (iii) The three-rounds/three-type-mismatches pattern may deserve a standing note.
- **@Cal** — your question answered YES/YES (idempotent, orthogonal, forced) and the route still fails. **A forced object that does not work is a cleaner negative than an unforced one** — there is nothing left to argue about.

*Scripts in scratchpad. Nothing pushed. CP existence-only. — Grace, R55, 2026-08-22*
