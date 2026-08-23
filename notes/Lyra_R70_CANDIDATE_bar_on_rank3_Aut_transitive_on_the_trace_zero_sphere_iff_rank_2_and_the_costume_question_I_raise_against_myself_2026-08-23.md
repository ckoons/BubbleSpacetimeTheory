# R70 — A candidate bar on rank 3 with **no number in it** — and the costume question, which I raise against myself

**Lyra, 2026-08-23. Cal's ask: exclude rank 3 on grounds other than "2 < 3" — a physical bar a rank-3 Jordan frame cannot satisfy. Object first, no minimality anywhere. Rule 3: PARTIAL CLAIM, needs two CIs; and I do not think it closes the cell yet. Nothing pushed, nothing banked.**

## 1. THE THEOREM — both directions, no numbers
> **Aut(J) acts TRANSITIVELY on the unit sphere of J₀ = {x : tr x = 0} ⟺ rank(J) = 2.**

**Aut(J) preserves the characteristic polynomial, hence the SPECTRUM. So the spectrum is an orbit invariant.**

**(⟸) rank 2.** Every trace-zero x satisfies `x² = −det(x)·1`, so its spectrum is {λ, −λ}; **normalized, EVERY unit trace-zero element has the same spectrum {1, −1}.** No invariant separates them, and Aut = O(J₀) is transitive. Verified:
```
   Sym_2(R)   normalised trace-zero spectra over random draws:  {(-0.7071, +0.7071)}   -- ONE spectrum
   Herm_2(C)  same:                                             {(-0.7071, +0.7071)}
```
**(⟹) rank r ≥ 3.** Take a primitive idempotent e₁ and form `e₁ − (1/r)1`; its spectrum is degenerate. A generic trace-zero element's is not. Verified in Sym₃(ℝ), both unit-normalized:
```
   from a primitive idempotent :  (-0.4082, -0.4082, +0.8165)     degenerate
   generic trace-zero          :  (-0.7071,  0.0000, +0.7071)     distinct
   -> two unit trace-zero elements, two spectra -> two orbits -> NOT transitive.
```

## 2. THE PHYSICAL READING — and it is a bar, not a preference
> **At rank ≥ 3 the algebra INTRINSICALLY DISTINGUISHES commitment directions:** the spectrum of a balanced (trace-zero) commitment is an invariant no automorphism can move, so some commitment directions are permanently inequivalent to others.
> **At rank 2 it CANNOT.** All balanced commitments have one spectrum; the algebra has no means to prefer any of them.

**⟹ PREMISE: *no commitment direction is intrinsically preferred* ⟹ rank = 2. There is no "2 < 3" anywhere in it.** That is the shape Cal asked for.

## 3. ★ THE COSTUME QUESTION — I am raising it against my own result
Cal probed the complement condition and found it was **rank 2 in a third costume.** **Is this a fourth?** Logically, **yes**: I proved both directions, so the premise is *equivalent* to rank 2.

**But logical equivalence CANNOT be the costume test** — **any** successful derivation of a specific rank has a premise equivalent to its conclusion given the rest of the chain. **The test is whether the premise is motivated from OUTSIDE the thing being derived.**

**⟹ THE DISCRIMINATOR, and it is the same one that discharged the N_c = a debt:**
> **Does "no preferred commitment direction" do work anywhere ELSE in the corpus?**
> **Load-bearing elsewhere ⟹ a genuine premise, and rank 2 is derived from it.**
> **Appears only here ⟹ a costume with better public relations, and the cell is unchanged.**
**I have NOT run that sweep. Until it runs, this is a candidate, and I am labelling it one.**

## 4. ⚠ AND A CAUTION AGAINST MYSELF — this is NOT the isotropy that was struck this morning
@Keeper struck *"commitment + isotropy forces type IV"* today on the ground that **isotropy does no RANK work.** That ruling was about **isotropy of the DOMAIN** — which delivers the symmetric-space structure and constrains nothing about rank.
**This is a different statement: transitivity on the trace-zero sphere of the ALGEBRA.** They are not the same object and they must be **subscripted before either is cited**:
```
   isotropy_domain  : G acts transitively on D          -> symmetric-space structure, NO rank content
   isotropy_commit  : Aut(J) transitive on S(J_0)       -> equivalent to rank 2
```
> **Without that subscript I have resurrected a struck sentence under a new name — which is precisely the T1446 disease, and it would be the seventh same-name-different-object of the day.** Flagging it on my own result rather than waiting for someone to catch it.

## 5. WHAT THIS DOES AND DOES NOT DO
- **It does NOT close Internal A.** Rank 2 is still an input.
- **It DOES change the input's character**: from *"rank 2, chosen as the minimum"* to *"rank 2, forced by a commitment-isotropy premise whose independence is untested."* **A posit with physical content and a named test beats a bare minimality selection** — but it is not a derivation, and I will not call it one.
- **The residual is unchanged at one integer.** What moved is *what kind of thing that integer is*.

**Lyra, R70. CANDIDATE: Aut(J) transitive on the unit sphere of trace-zero elements ⟺ rank 2 — proved both directions, verified (rank-2 spectra all {−0.7071,+0.7071}; Sym₃(ℝ) gives two distinct unit trace-zero spectra hence two orbits). Physical reading: at rank ≥ 3 the algebra permanently distinguishes commitment directions; at rank 2 it cannot. So "no commitment direction is intrinsically preferred" forces rank 2, with no minimality in it. ★ COSTUME QUESTION RAISED AGAINST MYSELF: it IS logically equivalent to rank 2, but equivalence cannot be the test — the test is outside-motivation, and the discriminator is whether the premise is load-bearing elsewhere in the corpus. That sweep has NOT run, so this is a candidate. ⚠ And it is NOT the isotropy struck this morning — subscript isotropy_domain vs isotropy_commit or I have resurrected a struck sentence under a new name. Two CIs wanted. Nothing pushed.**
