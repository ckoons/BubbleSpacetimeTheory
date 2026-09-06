# Grace — PRE-REGISTRATION, toy 5697 (written and hashed BEFORE the run; clock-verified 2026-09-06 10:0x EDT)

**Question (Keeper handoff G1, Casey's word):** does the cone-zeta r*(N) of ℤ^{1,4} (K1862-A: Σ over chamber vectors of norm N of 1/|W_x|) count positive-definite quaternary lattices by determinant (K1862-C's identification), when the count is made from an independent instrument and from Nipp's external table?

## The object, restated in my own terms
For x primitive in M = ℤ^{1,4} with Q(x) = N > 0, L := x^⊥ is a positive-definite (after sign) quaternary lattice with INTEGER Gram matrix and det L = N, and M is a unimodular overlattice of L ⊕ ⟨−N⟩ of index N. Conversely an L of det N with cyclic discriminant group D(L) = L*/L ≅ ℤ/N (automatic for squarefree N) embeds this way iff there is an anti-isometry φ: (D(L), b_L) → (D(⟨−N⟩), b) of the discriminant BILINEAR forms; the overlattice is then unimodular of signature (1,4), hence odd, hence ≅ ℤ^{1,4} (no even unimodular lattice exists in signature (1,4)).

Write c_L ∈ (ℤ/N)^× for the constant with b_L(a,a) = c_L/N on a generator a (equivalently c_L = adj(G)_{jj} mod N for any j whose column of adj(G) generates D(L)). Then φ(a) = u·a' is an anti-isometry iff u² ≡ c_L (mod N).

## Pre-registered predictions (can fail)
Let ω_odd(N) = number of distinct ODD primes dividing N, and r*_prim(N) = the chamber sum restricted to primitive x (for squarefree N every x is primitive, so r*_prim = r*).

**P1 (mass identity, the test of the identification).** For every squarefree N:
  r*(N) = 2^{ω_odd(N)} · Σ_{L} 1/|O(L)|,
the sum over isometry classes of positive-definite quaternary lattices L with integer Gram matrix, det L = N, and c_L a square mod N ("admissible"). Kill: any squarefree N ≤ 108 where the two sides differ. (Derivation: orbit–stabilizer on the groupoid of triples (L, x, φ); |Φ_L| = #{u mod N : u² ≡ c_L} = 2^{ω_odd(N)} when nonempty; the ±1 of O(⟨−N⟩) is absorbed by x ↔ −x.)

**P2 (per-class refinement).** For each admissible class L of det N (N squarefree): Σ_{chamber x with x^⊥ ≅ L} 1/|W_x| = 2^{ω_odd(N)}/|O(L)|. Every admissible class appears as some x^⊥; no non-admissible class does.

**P3 (external pin).** Nipp's table (F = (2f_ii diag, f_ij off), d = det F, G = |O(L)| with −1 counted): odd L of Gram-det N sits at Nipp d = 16N with all f_ij (i<j) even; even L of Gram-det N sits at d = N (as Q/2). My own |O(L)| from exhaustive isometry search equals Nipp's G on every such row; my class list for each N equals Nipp's (filtered) row list, class for class.

**P4 (reproduction of K1862-A, not blind — Elie 5693 is the blind one).** My r*(N) for N = 1..12 equals Keeper's printed 1/384, 1/96, 1/48, 3/128, 7/240, 1/16, 1/12, 5/96, 25/384, 7/48, 7/48, 5/48; orbit counts 1,1,1,2,2,2,2,3,3,2,2,4; and my stabilizer orders from Coxeter-type recognition equal a BFS closure of the reflection matrices on every chamber vector N ≤ 40.

## What a failure means
P1 fails at some N while P3 holds → the identification "cone-zeta counts quaternary lattices by determinant" is wrong or the admissibility condition is wrong (then report which classes are missing/extra: that is the correction). P3 fails → my isometry counter or Nipp parsing is wrong; fix the instrument before reading P1. P4 fails → my chamber/stabilizer code disagrees with Keeper's; stop and reconcile before anything else.

## Scope
Squarefree N ≤ 108 (Nipp's d ≤ 1732 covers odd L to N = 108). Non-squarefree N deferred (imprimitive x and non-cyclic D(L)). Instrument: play/toy_5697_*.py (Python, exact rationals; isometries by exhaustive short-vector backtracking; no PARI on this machine).

— Grace
