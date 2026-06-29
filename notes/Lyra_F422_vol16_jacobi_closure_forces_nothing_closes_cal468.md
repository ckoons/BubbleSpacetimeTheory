---
title: "F422 — Vol-16 Jacobi/closure check (Cal #468/#472): the bracket structure of the substrate operator algebra A forces NOTHING new. Machine-verified. (1) Jacobi is AUTOMATIC: because [Ĥ,D̂]=0 (the two mass operators are co-diagonal), the Jacobi term [V̂,[Ĥ,D̂]] vanishes identically, so [Ĥ,[D̂,V̂]]=[D̂,[Ĥ,V̂]] holds for ANY V̂ — no constraint. (2) Closure: {Ĥ,D̂,V̂} with generic off-diagonal V̂ generates the full gl(3) on H_gen (dim 9), BUT every DIAGONAL operator the closure produces lies in span{I,Ĥ,D̂,Ĥ²} — no new diagonal invariant is forced outside the already-banked spectrum {5/2,3/2,0}. (3) The structure constants are exactly the spectral gaps {ν_e−ν_μ, ν_e−ν_τ, ν_μ−ν_τ} = {1, 5/2, 3/2} = {(n_C−N_c)/rank, n_C/rank, N_c/rank}, all functions of the banked spectrum — [Ĥ,V̂]_ij/V̂_ij = ν_i−ν_j as Vol-16 already stated. ⟹ The linear-algebra representation is a FAITHFUL CONSOLIDATING reformulation: closing A under brackets generates no hidden prediction and no new number. Closes the Cal #468 bar COMPLETELY (Cal #472 condition met: Jacobi/commutator structure forces nothing). Banks as consolidating spine. No new claim, no count move. Count 9/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-29 Monday (date-verified)"
status: "v1.0 — Cal #468/#472 closure. Jacobi automatic ([Ĥ,D̂]=0). Generated Lie algebra = gl(3); diagonal sector closes in span{I,Ĥ,D̂,Ĥ²}; structure constants = spectral gaps {1,5/2,3/2}={(n_C−N_c)/rank, n_C/rank, N_c/rank}. Forces nothing new ⟹ faithful consolidating reformulation. Closes Cal #468 bar. No count move. Count 9/26."
---

# F422 — The Vol-16 operator algebra closes under brackets and forces NOTHING new (Cal #468/#472)

**The bar (Cal #468, condition Cal #472):** the Vol-16 linear-algebra representation banks as consolidating spine *iff* the commutator/Jacobi structure of A forces no new relation among the integers — i.e., closing A under brackets must generate no hidden prediction. Tested, machine-verified (sympy, exact rationals).

## Setup

Generation sector H_gen, basis (e, μ, τ):
- **Ĥ** = diag(5/2, 3/2, 0) — conformal weights = generations (Wallach points).
- **D̂** = diag(5, 2, 0) — Korányi-Wolf fiber dims = support strata.
- **V̂** = generic antisymmetric off-diagonal generator (CKM = exp V̂); entries a,b,c left **symbolic** so the test reads what closure forces, not a fitted angle.

## Three results

**(1) Jacobi is automatic.** [Ĥ,[D̂,V̂]] + [D̂,[V̂,Ĥ]] + [V̂,[Ĥ,D̂]] = 0 identically. The mechanism is that **[Ĥ,D̂]=0** — the two mass operators are simultaneously diagonal (that eigenbasis *is* the mass eigenbasis), so the third term vanishes and Jacobi collapses to [Ĥ,[D̂,V̂]]=[D̂,[Ĥ,V̂]], which holds for any V̂ because both sides multiply entry ij by the same scalar (ν_i−ν_j)(d_i−d_j). **No constraint is imposed.**

**(2) Closure generates no new diagonal invariant.** {Ĥ, D̂, V̂} with generic V̂ generates the full gl(3) on H_gen (dim 9, expected — generic off-diagonal + diagonal span everything). The count-relevant fact: **every diagonal operator produced by the closure lies in span{I, Ĥ, D̂, Ĥ²}** (verified: rank unchanged when each generated diagonal is appended). No new diagonal invariant — i.e., no new conserved spectral quantity — is forced outside the already-banked spectrum {5/2, 3/2, 0}.

**(3) The structure constants are the spectral gaps — already banked.** [Ĥ,V̂]_ij / V̂_ij = ν_i − ν_j, giving the three gaps

  {ν_e−ν_μ, ν_e−ν_τ, ν_μ−ν_τ} = {1, 5/2, 3/2} = {(n_C−N_c)/rank, n_C/rank, N_c/rank}.

All three are functions of the banked spectrum — exactly the [Ĥ,V̂]_23/V̂_23 = ρ₂ = N_c/2 fact Vol-16 already stated, now exhibited for all three pairs. No new number appears.

## Conclusion

Closing A under brackets generates **no hidden prediction and no new integer relation**. The Vol-16 linear-algebra representation is therefore a **faithful consolidating reformulation** of the established results, not a disguised new claim. This is precisely the Cal #472 condition ("Jacobi/commutator structure forces nothing"), so it **closes the Cal #468 bar completely** and banks as consolidating spine. No new claim, no count move. **Count 9/26.**

*Discipline note: this is a NEGATIVE-in-the-good-sense result — it confirms the reformulation hides no prediction. It does not move the count and was not pursued to move it (the only live count-mover remains the exp-12 blind why-α propagator, PRIMARY 1).*
