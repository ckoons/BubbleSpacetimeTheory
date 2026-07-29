---
node_type: k_audit
id: K1006
title: The off-diagonal overlaps are the JACK generalized-binomial coefficients at α = 2/d = 2/3 — a standard target-innocent computation, NOT a mystical FK-book lookup that requires the physical text. Method identified + diagonal Pochhammer verified (reproduces Lyra's 4.5/7.5 and the down ladder). BUT: my quick 2-variable Jack implementation FAILED its own α=1 sanity check (returned monomials, not Jack polynomials), so the off-diagonal numbers are a real computation Elie must implement + VALIDATE against known limits — not guess. This is the discipline vindicating itself at the input level.
date: 2026-07-29
author: Keeper
verdict: Reframe the block — it's Jack(α=2/3), computable by standard algorithm, not "wait for the FK book." Diagonal verified. Off-diagonal needs a validated implementation (Elie) checked against 4 gates. Keeper does NOT supply the value-bearing off-diagonal numbers — a naive attempt already produced wrong ones, which is exactly why they must be sourced+validated, not asserted.
---

# K1006 — The off-diagonal is Jack(α=2/3): computable, not a book lookup

Casey: "Elie needs MORE help." The real stall isn't a missing number — it's that the team has been framing the off-diagonal as "wait for the physical FK Ch XII text." **It isn't a book lookup. It's a standard, target-innocent computation.** Here is the reframe, what's verified, and — honestly — where my own quick attempt failed, which is the useful part.

## ★★ THE REFRAME — the off-diagonal is Jack(α=2/3)
The spherical polynomials on D_IV⁵ (rank 2, multiplicity d=3, K1005) are **Jack polynomials at parameter α = 2/d = 2/3.** The FK generalized-binomial coefficients $\binom{\lambda}{\mu}$ are the **Jack generalized binomial coefficients** (Okounkov–Olshanski, "Shifted Jack polynomials, binomial formula") — a computable combinatorial object, OR equivalently the direct FK-measure overlap integrals ⟨ψ_λ | O | ψ_μ⟩ of the explicit spherical polynomials. **Either route is pure geometry — no observable enters, and no physical book is required to evaluate it.** This dissolves the "one FK lookup" stall: it's "run the α=2/3 Jack algorithm," not "find the book."

## ★ VERIFIED (solid)
- **d = 3 → α = 2/3** (K1005).
- **Diagonal Pochhammer** (needs no Jack machinery — closed form): (ν)_{(λ₁,λ₂)} = (ν)_{λ₁}(ν−3/2)_{λ₂} at ν=N_c=3 gives the down ladder **{3,60,2520} = 1:20:840, m_s/m_d=20**, and the two-row **(3)_{(1,1)} = 4.5** (Lyra's a=3 number; a=1 would give 7.5). Confirmed both.

## ★★ HONEST CAVEAT — my quick off-diagonal impl was WRONG (and that's the point)
I tried to compute the off-diagonal binomials directly to hand Elie the numbers. **My naive 2-variable Jack solver failed its own α=1 sanity check:** it returned P_(2,0)=x²+y² and P_(3,0)=x³+y³ — the bare monomials — when the textbook α=1 answer is the Schur/complete-homogeneous P_(2,0)=x²+xy+y², P_(3,0)=x³+x²y+xy²+y³ (the cross terms are missing). So **the off-diagonal binomial numbers that implementation produced are invalid, and I am not filing them.**
- **This is the blind-bar discipline working at the INPUT level.** A plausible-looking computation of the one load-bearing input gave wrong numbers. That is precisely why **Keeper must not be the origin of the value-bearing off-diagonal numbers**, and why they must be produced by a validated implementation and checked — not asserted from memory or a quick script.

## ★ THE VALIDATION PROTOCOL (the 4 gates Elie's implementation must pass before the numbers are trusted)
Any off-diagonal evaluation (Jack-binomial or direct-integral) must reproduce, IN THE CODE, all four before its numbers feed the engines:
1. **α=1 limit → Schur:** single-row P_{(n)}^{(1)} = complete homogeneous h_n (x²+xy+y², x³+x²y+xy²+y³, …). [my naive attempt FAILED here — the canary.]
2. **α=2 limit → zonal** (the d=1 real-symmetric case) — a second independent limit.
3. **Diagonal → (ν)_{(λ₁,λ₂)} = (ν)_{λ₁}(ν−3/2)_{λ₂}** at ν=3 (the verified Pochhammer: {3,60,2520}, (1,1)=4.5).
4. **Down single-row tripwire → (N_c)_min = 3** (K1004/K1005).
Only after 1–4 pass is the two-row off-diagonal table trustworthy.

## ★ TWO INDEPENDENT ROUTES (cross-check, don't rebuild)
- **Route A — Jack binomials:** implement Jack(α=2/3) generalized binomial coefficients (Okounkov–Olshanski). Validate on gates 1–4.
- **Route B — direct overlap integrals:** ⟨ψ_λ|O|ψ_μ⟩ against the FK measure, from the explicit spherical polynomials + the degree-1 (2,2) condensate. **The corpus already has matrix-element machinery — toy_3677/3724/3741/3891/3919 (Mehler/Pochhammer), toy_4004 (Bergman matrix element).** Reconnect and build on the validated ones (don't greenfield the integrator).
- Routes A and B must agree — that agreement is a fifth, strong check.

## ★ Handoff
- **★ ELIE — implement Route A and/or B, pass gates 1–4 in-code (α=1 Schur is the canary that caught my error), cross-check A vs B, THEN evaluate the two-row lepton/neutrino/up off-diagonals and fire.** Build on toy_4004 etc.; validate before trusting.
- **★ LYRA — the Jack(α=2/3) identification against aif.2069 / FK Ch XII: confirm the spherical polynomials are Jack at α=2/d and that the FK binomial = the Jack binomial** (this is the one book-check that remains, and it's a *statement* to confirm, not a table to transcribe).
- **★ CAL — audit that the implementation passes gates 1–4 target-innocently.**
- **★ KEEPER — I do NOT supply the off-diagonal values** (my attempt was wrong); I supply the method, the gates, and the ruling. Bar stands (K1002/K1003).

## Honest state
The "help" that landed is a reframe plus a caution, both real: the off-diagonal is Jack(α=2/3) — computable now, no physical book needed — and getting it right is error-prone enough that I got it wrong on the first pass, caught by the α=1 canary. So the unblock is a *validated* computation, not a lookup and not a guess: Elie implements against four known-answer gates, cross-checks two routes, Lyra confirms the one identification against the source, and the down tripwire fires if d is wrong. That is the honest path from here to the whole spectrum, and it's fully within the committed bar.

— K1006, Keeper, 2026-07-29. Off-diagonal = Jack(α=2/d=2/3) binomials (or direct FK overlap integrals) — computable, target-innocent, NOT a book lookup. Diagonal verified (down ladder + (1,1)=4.5). My naive Jack impl FAILED the α=1 Schur check → off-diagonal numbers must be a VALIDATED implementation (gates: α=1 Schur, α=2 zonal, diagonal Pochhammer, down tripwire), two routes cross-checked, built on toy_4004. Keeper supplies method+gates, not values. See [[Keeper_K1005_GATE_A_RESOLVED_independent_verification_d_equals_3_genus_5_rho_5half_3half_the_d1_route_is_D_IV3_not_D_IV5_and_conflates_g7_with_the_genus_reproduces_down_ladder_2026-07-29]], [[Keeper_K1004_unblock_Elie_the_off_diagonal_numbers_genuinely_dont_exist_its_a_real_FK_evaluation_two_gates_d_convention_and_N_c_min_shortcut_is_unproven_beyond_down_single_row_2026-07-29]], Okounkov–Olshanski shifted Jack, aif.2069.
