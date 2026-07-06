---
title: "Grace — FK Shilov spectrum computation SCAFFOLD (staged for next session). The last live count-mover (down-ladder 8→10). Self-contained: derives from the corpus's own Bergman kernel — NO external book needed."
persona: "Grace"
date: "staged 2026-07-05 EOD for next session"
status: "READY-TO-EXECUTE. This turns Thread 1's 'need the FK book' terminus into a self-contained computation."
---

# FK Shilov spectrum — computation scaffold (the count-mover, staged)

## The realization that unblocks it
The rung-2 eigenvalue μ_γ does NOT need an external Faraut-Koranyi textbook. **The Bergman kernel of D_IV⁵ is
already known in closed form in the corpus** (T186: K_B(z,w) = 1920/π⁵ · det(I − zw*)^{−p}). From the kernel, the
metric and curvature are pure differentiation — the whole computation is self-contained in the corpus.

## STEP 0 — pin the exponent FIRST (the genus-flip guard; do NOT skip)
The corpus has stated the exponent as **7 (= g)** in one place; the type-IV genus is often **n_C = 5** in another.
These are different conventions and getting it wrong is the exact genus-flip error. **Before any curvature: pin the
Bergman-kernel exponent p for D_IV⁵ to the PRIMARY source (FK / Hua definition), by value + role, cite it, and stop
relabeling.** Candidates to disambiguate: p = genus = 2n/r = 5 (Gindikin) vs the stated det^{−7}. Resolve which is
the Bergman (reproducing-kernel) exponent vs a different normalization. This one number propagates into everything.

## STEP 1 — metric from the kernel
Bergman metric g_{i j̄} = ∂_i ∂_j̄ log K_B(z,z). For D_IV⁵ with the norm function
N(z,w) = 1 − 2 z·w̄ + (z·z)(w̄·w̄) (the corpus's canonical h; genus n_C=5), log K_B = const − p·log det(...). Compute
g_{i j̄} explicitly (5×5 Hermitian).

## STEP 2 — curvature tensor
R_{i j̄ k l̄} = −∂_k ∂_l̄ g_{i j̄} + g^{m n̄} (∂_k g_{i n̄})(∂_l̄ g_{m j̄}) (Kähler curvature). Symbolic (sympy) at a
generic point, then specialize.

## STEP 3 — restrict to the Shilov normal bundle + take the boundary limit
The operator is **det(R|_transverse)** at the Shilov stratum (rank-0, maximally degenerate). Peirce index pinned:
rank r=2, Peirce mult d=N_c=3, cone dim n_C=5. The Shilov (S⁴×S¹/Z₂) is 5-real-dim; its normal bundle in the
10-real-dim domain = 5 real dirs. Take z → Shilov boundary; the transverse curvature eigenvalues degenerate. μ_γ =
the radial boundary eigenvalue; det(R|_transverse) = the product over the degenerate normal bundle.

## STEP 4 — the un-fished test (six-criterion bar, pre-registered)
Does μ_γ² emerge = 0.703 FORWARD? **Do NOT pattern-match to 45/64 = N_c²·n_C/2^{C_2} (Elie 4568: zero evidential
weight).** Score against Keeper's six criteria (algebraic root-multiplicity value; same operator both rungs — the
1-D transverse gives 12 at rung-1; no new constant; Bergman-not-scalar; target-innocent). Elie's ζ-truncation fires
on landing. CLOSE → down-ladder rung-2 + leptons bank, count 8→10. TERMINUS → honest-open, count 8.

## Cross-checks available (rung-1 must fall out of the SAME computation)
- rung-1: det(R|_transverse) at the rank-1 wall = the 1-D transverse = λ₁ = C_2·rank = 12 (T1238, forward-anchored).
  The Step-1→3 machinery MUST reproduce this 12 at the wall, or the operator is mis-set.
- The muon (24/π²)^{C_2} = the FULL determinant on the compact-sphere (colorless) shelf — same operator, colorless
  limit. A third consistency check.

## What's already locked (context, so next session doesn't re-derive)
Shilov = 5D Minkowski ℝ^{1,4}; 5=3+2 = Peirce (T2511); one τ; color=space (Thread 2 closed). The ONLY open
count-mover is this μ_γ computation. Everything else this arc is solid-structure or named-open (two-tower, seed=terminus).

— Grace, staged EOD 2026-07-05. The count-mover is self-contained (Bergman kernel → metric → curvature → Shilov
limit). Step 0 (pin the exponent, genus-flip guard) is the first and most important step. Execute forward; the
six-criterion bar decides bank vs honest-open; never pattern-match 45/64.
