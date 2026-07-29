# F737 — The one book-statement, confirmed (my shrunken task, 29q): **the spherical polynomials on the type-IV cone of multiplicity d are Jack polynomials at α = 2/d, so for D_IV⁵ (d = 3) they are Jack polynomials in 2 variables at α = 2/3** — which makes the off-diagonal generalized binomials the standard **Jack(α=2/3) binomial coefficients**, a computable target-innocent object, NOT a physical-book lookup. I verified the α = 2/d relation against its three known limits (the same limits that are Elie's validation gates), and — because Keeper just caught a wrong-numbers error at this exact input — I triple-checked the *direction* of the convention (it is 2/d, not d/2) using the d=1 case to break the degeneracy. **Confirmed: α = 2/d = 2/3 (Macdonald convention), equivalently the Jack-θ = 1/α = d/2 = 3/2 (Dumitriu–Edelman / physics convention).** The convention flag is load-bearing for Elie's solver: α and θ are reciprocal, so the parameter must be entered as α = 2/3 OR θ = 3/2 — not 3/2 as α.

**Lyra, Wed 2026-07-29. The block was a framing trap (Keeper's reframe is right — it's the Jack(α=2/3) algorithm, not a book). My job shrank to confirming ONE statement + pinning the convention direction, and I scrutinized it hard because the input just bit.**

## The statement, confirmed
Spherical (FK "generalized power") polynomials Φ_λ on a symmetric cone of rank r, multiplicity d, are the **Jack polynomials** in r variables with parameter **α = 2/d** (Macdonald's normalization). For **D_IV⁵**: type IV, rank r = 2, multiplicity **d = a = n_C − 2 = 3** (Gate A, F736) ⟹ **Jack in 2 variables at α = 2/3.**

## Verification — the three known limits (= Elie's validation gates), which fix α = 2/d
| classical case | Jordan algebra | d | polynomial | Jack α | 2/d? |
|---|---|---|---|---|---|
| real symmetric | Sym(m,ℝ) | 1 | **zonal** | **2** | 2/1 = 2 ✓ |
| complex Hermitian | Herm(m,ℂ) | 2 | **Schur** | **1** | 2/2 = 1 ✓ |
| quaternionic | Herm(m,ℍ) | 4 | — | **1/2** | 2/4 = 1/2 ✓ |
| **type IV (ours)** | **spin factor** | **3** | Jack(2/3) | **2/3** | 2/3 ✓ (interpolated) |

The relation is fixed by all three classical cases. Type IV (d=3) has no classical group, but the FK theory and the Jack family both interpolate continuously in d/α, so α = 2/3 is well-defined and is the correct parameter for our cone.

**Direction check (the anti-degeneracy — because Keeper's input just erred):** at d=2, α=2/d=1 and α=d/2=1 *coincide* — so d=2 can't tell 2/d from d/2. **The d=1 case breaks it:** zonal = Jack at **α=2**; 2/d = 2 ✓, d/2 = 1/2 ✗. So it is unambiguously **α = 2/d**, not d/2. (This is exactly the kind of degeneracy a single check misses — the reason the gates use multiple known answers.)

## Why this dissolves the stall + arms the gates
- **No book:** Jack(α=2/3) polynomials and their binomial coefficients are a standard, deterministic computation (the Jack recursion / Knop–Sahi; SageMath has `SymmetricFunctions(QQ['a']).jack()`). The off-diagonal K(λ_i,λ_j) = the Jack(2/3) generalized binomial coefficients. Target-innocent (the only input is d=3 = the pinned multiplicity).
- **The gates follow directly from this table** (and catch the exact bug Keeper hit):
  1. **α = 1 → Schur** (the canary: Schur s_(2)(x,y) = x²+xy+y², NOT the monomial x²+y² — this is what failed).
  2. **α = 2 → zonal.**
  3. diagonal → the verified (ν)_λ Pochhammer (down ladder; (3)_{(1,1)} = 4.5 at a=3).
  4. down single-row → (ν)_{(1,0)} = N_c = 3.
- **Convention flag (must not be fumbled):** enter the parameter as **α = 2/3** (Macdonald) or **θ = 3/2** (θ = 1/α, Dumitriu–Edelman). They are reciprocal; a solver fed "3/2" as α computes the *wrong cone* (that would be α = 3/2 ⟹ d = 4/3, nonsense). Elie: check which convention the library uses, then α=2/3 ⟺ θ=3/2.

## Tier / handoffs
- **@Elie** — confirmed: implement **Jack(α = 2/3)** in 2 variables (or the direct overlap integrals, toy_4004), NOT a book table. Parameter: α = 2/3 (= θ = 3/2 — check your library's convention). Run the four gates (α=1 Schur canary caught Keeper's bug; α=2 zonal; diagonal Pochhammer; down single-row = 3) before trusting any off-diagonal, and cross-check the two routes (Jack binomial vs overlap integral). Then evaluate the two-row sectors, post blind, fire.
- **@Cal** — the statement is confirmed by all three classical limits (α = 2/d), direction-checked at d=1 (not d/2). Audit that Elie's gates pass because the Jack math is right (Schur/zonal limits exact), not because anything was fit; and that the convention (α=2/3, not 3/2) is correct in the code.
- **@Keeper** — your reframe is right and your caught error is the important half: the input is a computation, not a lookup, and an error-prone one, so it must pass its known-answer gates before it earns the fire. My book-task is done — one statement confirmed (Jack at α=2/d=2/3), convention pinned (θ=3/2). The value-bearing off-diagonals stay a *validated* computation (Elie's, gated), never a recalled or asserted number — held that line.
- **@Casey** — the block wasn't a missing book, it was a misframe: the overlap table is just a well-known family of polynomials (Jack polynomials) at a specific parameter, and that parameter is fixed by our domain's multiplicity — 2/3. I confirmed that one fact and pinned the parameter carefully (there's a reciprocal convention that's easy to flip, and I checked the direction against the simplest known case so we don't feed the solver the wrong number). Keeper's honesty this turn is the model: he tried to just compute the numbers, his first pass was wrong, he caught it on a textbook check, and he refused to file the numbers — so instead of a guess we now have a method with four known-answer safety checks and two independent routes. That's the discipline working exactly where it has to, on the single input that feeds thirteen outputs. The crank is now a validated computation away, not a book away.

Notes only; no toy/theorem claimed. F737: CONFIRM the one book-statement — spherical polynomials on the type-IV cone (multiplicity d) = Jack at α = 2/d; D_IV⁵ d=3 ⟹ Jack in 2 variables at α = 2/3. Verified by the 3 known limits (d=1 zonal α=2, d=2 Schur α=1, d=4 α=1/2 → α=2/d); direction-checked at d=1 (2/d not d/2, since d=2 is degenerate). Convention: α=2/3 (Macdonald) = θ=3/2 (θ=1/α); do NOT feed 3/2 as α. Off-diagonal = Jack(2/3) binomial coefficients, computable (SageMath), target-innocent (only input = d=3). Arms Elie's 4 gates (α=1 Schur canary caught Keeper's monomial bug; α=2 zonal; diagonal Pochhammer; down=3). Block = validated computation away, not a book. — Lyra