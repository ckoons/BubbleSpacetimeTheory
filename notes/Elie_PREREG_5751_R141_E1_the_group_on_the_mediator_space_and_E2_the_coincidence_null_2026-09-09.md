# PRE-REGISTRATION — Toy 5751, Round 141 (E1, E2). Hashed before the run. **This is the round's can-fail and it decides C2.**

**Elie, 2026-09-09 (Wednesday) 12:47 EDT (shell-copied).**

## Setup, stated so the computation is checkable
Spin-factor triple on V = ℂ⁵: {x,y,z} = (x|y)z + (z|y)x − (x·z)ȳ, with (x|y) = Σx_i conj(y_i) and x·z = Σ x_i z_i. Minimal tripotent **e = (u + iv)/2** with u, v ∈ ℝ⁵ orthonormal (this normalisation gives {e,e,e} = e). K = SO(5) × SO(2) acts by z ↦ e^{iθ}gz.

## E1 — the obstruction, made exact
- **A1 (control):** the Peirce operator D(e,e)x = {e,e,x} has eigenvalues **1, 1/2, 0 with dimensions 1, 3, 1**, so V₁₂ ≅ ℂ³ = span_ℂ{e₃,e₄,e₅}. Verified numerically, and the family gives 1, n−2, 1.
- **A2 (can fail):** the isotropy **Stab_K(e) has Lie-algebra dimension 4** and is **SO(2)_diag × SO(3)**, where the SO(2) is {(rotation by −θ on span{u,v}, θ)} and SO(3) acts on span{e₃,e₄,e₅}. Computed as the null space of (A, t) ↦ Ae + ite on so(5) ⊕ so(2), not asserted.
- **A3 (can fail — the round's line):** the image of that isotropy in GL(V₁₂) is **{e^{iθ}h : h ∈ SO(3)} = U(1)·SO(3), of dimension 4. SU(3) has dimension 8, so SU(3) DOES NOT EMBED.** And the argument extends past the compact isotropy: any compact subgroup of the full structure-group stabiliser is conjugate into its maximal compact, which is this same dimension-4 group, **so SU(3) does not embed in the stabiliser of a minimal tripotent in either the compact or the full structure group.**
- **A4:** the inclusion that does exist runs the wrong way for a derivation: **SO(3) ⊂ SU(3)** by the standard vector embedding, dimension 3 inside 8. The geometry supplies a proper subgroup of colour, not colour.
- **A5 (the endomorphism question T2551 raised):** the bare algebra depends entirely on which structure you forget. **End_ℂ(V₁₂) = M₃(ℂ)** (forgets the group), **End_ℝ of the real 3-space = M₃(ℝ)** (forgets the complex structure too), and **End_ℝ(V₁₂) as a real 6-space = M₆(ℝ)**. The object that respects the geometry is the **commutant of the isotropy, which by Schur is ℂ** (the vector rep of SO(3) complexified is irreducible), or M₂(ℝ) if the phase is dropped. **So the correct object is ℂ, not M₃ of anything, and the only route to SU(3) is End_ℂ(ℂ³) = M₃(ℂ) — available for ANY three-dimensional complex space, which is exactly the slip T2567 withdrew.**
- **Hashed verdict: the obstruction is real and it is a dimension count, 8 against 4. "Colour = the mediator space" is not merely unexhibited; it is ruled out by the group the geometry supplies.**

## E2 — the coincidence null, **menu named before counting**
**Menu (fixed now):** for every irreducible bounded symmetric domain with dim_ℂ ≤ 30, the six root-data integers **{rank r, multiplicity a, multiplicity b, genus p, dim_ℂ, dim V₁₂ = a + b}**. Target: the measured integer **3**.
- **A6 (can fail):** **at least 20 domains carry some menu invariant equal to 3**, so "a domain has an invariant equal to 3" is cheap; whereas **the specific invariant a = 3 is a singleton**. The look-elsewhere factor is therefore the menu size, six per domain, and the selector's strength depends entirely on whether the invariant was named before the target. I report the counts; **whether the naming was prior is a history question, not mine to rule** — the corpus's own record is that the identification was withdrawn three times and re-registered.
- **A7:** the same count for the other small measured integers {2, 4, 6, 8} so the round can see the whole table rather than one row.

Score X/7; A2, A3, A6 can fail.
