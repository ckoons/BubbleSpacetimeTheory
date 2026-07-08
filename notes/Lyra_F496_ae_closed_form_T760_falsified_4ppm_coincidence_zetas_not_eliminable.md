---
title: "F496 — QED radiative-structure exploration (my fresh lane): I TESTED my own earlier 'proved' closed-form claim T760 [a_e = (α/2π)(1−(2α/π)²)^{2n_C·g}, allegedly zeta-free] against the measured electron anomaly and it is FALSIFIED as exact — it matches only to ~4 ppm while a_e is measured to ~10⁻¹², and structurally it sets the 2-loop coefficient C₂ = 0 (the closed form has only EVEN powers of α/π inside, so it CANNOT produce the genuine linear-in-(α/π) 2-loop term, which carries ζ(3) and ln2); the ~4-ppm agreement is a numerical COINCIDENCE at α=1/137 (the closed form's C₃ = −2·2n_C·g = −140 cubic term mimics the true 2-loop shift because 140·(α/π) = 0.325 ≈ |C₂| = 0.328, off 1%). So the ZETAS ARE NOT ELIMINABLE: a_e genuinely needs the standard QED loop structure (ζ(3)+ln2 live in the true C₂), and the 'zeta-free observable / Observable Closure' reading (T719/T760) is form-cheap for a_e. ALSO FALSIFIED: the zeta-ladder TRUNCATION claim ('QED structurally finite at 3 transcendentals ζ(3),ζ(5),ζ(7) because only 3 odd BST primes') — higher loops bring ζ(9), ζ(11), ... (standard weight growth); the odd-zeta ORDERING (ζ(3)@2-loop, ζ(5)@3-loop, ζ(7)@4-loop = ζ(2L−1) at loop L) is STANDARD Feynman-period weight-counting, and {3,5,7} = {N_c,n_C,g} is a small-odd-number coincidence for the first three, NOT a prediction (the ladder does not stop at 7). HONEST SELF-CORRECTION: T760 is my own prior 'proved' theorem; the precision test retracts it. WHAT SURVIVES (untested by me, flag for separate check): the DENOMINATOR-separation pattern (T1481: the rational-part denominators of the low-loop coefficients are BST monomials in {rank,N_c,n_C}) is a distinct descriptive claim about the rational parts — I did not test it here; it may be a real feature or numerology, separate from the (falsified) zeta-free-closed-form claim. WHAT THIS DOES NOT TOUCH: α itself is RULED (the coupling = the input); this is about the LOOP structure (which is standard QED given α, NOT a BST closed form). NET (honest, per Casey's 'report positive or negative'): the fresh QED-radiative lane yields a NEGATIVE — BST does NOT derive a zeta-free closed form for a_e; the loop structure is standard QED. The genuine BST content in QED is α (RULED), full stop; the perturbative zeta/RFC 'patterns' are either standard weight-counting relabeled with small BST integers (zeta ladder) or untested (denominator monomials). For Keeper (adjudicate the RETRACTION of T760 + the Observable-Closure-for-a_e claim T719: the zeta-free closed form is a 4-ppm coincidence, C₂=0, falsified at 10⁻¹² measured precision; the zeta-ladder truncation-at-3 is also falsified; the odd-zeta ordering is standard weight-counting), Grace (T760 was your flag → Keeper verdict; the closed form doesn't survive the precision test — the zetas are real), Elie (the target-richness of the QED series is exactly why the fish-detector fires here; the closed form was a coincidental fit), Casey (honest negative: BST's QED content is α, RULED; the loop structure is standard QED, not a BST closed form; the 'zeta ladder at BST primes' is a small-number coincidence), Cal."
author: "Lyra (Claude Opus 4.8)"
date: "2026-07-08 Wednesday (date-verified)"
status: "v0.1 — QED-radiative fresh lane, HONEST NEGATIVE. Tested my own T760 closed form a_e=(α/2π)(1−(2α/π)²)^{2n_C·g} vs measured a_e: matches only ~4 ppm (a_e known to ~1e-12) → FALSIFIED as exact. Structural: the closed form has only EVEN powers of α/π inside → C₂=0 → MISSES the real linear 2-loop term (which carries ζ(3)+ln2); its C₃=−140 cubic COINCIDENTALLY mimics the true 2-loop shift at α=1/137 (140·α/π=0.325≈|C₂|=0.328). So zetas NOT eliminable; Observable-Closure-for-a_e (T719/T760) form-cheap. Zeta-ladder TRUNCATION ('finite at 3 transcendentals') also falsified — higher loops → ζ(9),ζ(11); the ζ(2L−1) ordering is standard weight-counting, {3,5,7}=BST is a small-number coincidence. SELF-CORRECTION (T760 is mine). Untested: T1481 denominator-monomials (separate). Doesn't touch α (RULED). BST's QED content = α, full stop; loop structure = standard QED. No bank; a retraction."
---

# F496 — the a_e closed form (T760) is a 4-ppm coincidence; the zetas are not eliminable

Fresh lane (Casey): the QED radiative structure — the zeta ladder, a_e, the RFC pattern. The corpus already has a *testable* claim, my own T760: **a_e = (α/2π)(1−(2α/π)²)^{2n_C·g}, zeta-free.** So I tested it. It doesn't survive.

## The test

| | value |
|---|---|
| measured a_e | 1.15965218059 × 10⁻³ (known to ~10⁻¹²) |
| T760 closed form (exponent 2n_C·g = 70) | 1.15965645 × 10⁻³ |
| difference | +4.3 × 10⁻⁹ = **+3.7 ppm** |

a_e is one of the most precisely known numbers in physics (~10⁻¹²). A form that matches to **~4 ppm** is off by **~10⁴–10⁶ times** the measurement. **Falsified as exact.**

## Why — the structural reason (not just the number)

The closed form (1−(2α/π)²)^{70} has **only even powers of α/π inside**, so its correction to Schwinger starts at (α/π)²·(α/2π) = (α/π)³. Expanding:
- **T760:** C₁ = 1/2, **C₂ = 0**, C₃ = −2·(2n_C·g) = **−140**, …
- **Known QED:** C₁ = 1/2, C₂ = **−0.32848**, C₃ = **+1.18123**, …

**T760 sets the entire 2-loop coefficient C₂ to zero** — but the real C₂ = −0.328 is where **ζ(3) and ln2 live.** The closed form *cannot* produce it (no odd power of α/π available). The 4-ppm agreement is a **coincidence at α = 1/137**: the cubic −140(α/π)³ mimics the true quadratic C₂(α/π)² because 140·(α/π) = 0.325 ≈ |C₂| = 0.328 (1% off). At any other α, or at the measured precision, it fails.

**⟹ The zetas are not eliminable.** a_e genuinely requires the standard QED loop structure; ζ(3) is *in* the observable (in C₂), not a "perturbative artifact." The Observable-Closure-for-a_e reading (T719/T760) is form-cheap.

## Also falsified: the zeta-ladder *truncation*

The corpus claim "QED is structurally finite at three transcendentals ζ(3), ζ(5), ζ(7) because there are only three odd BST primes" is false: higher-loop QED brings **ζ(9), ζ(11), …** (transcendental weight keeps growing ~2/loop). What's real is only the *ordering* — the leading new odd zeta at loop L is ζ(2L−1) (ζ(3)@2, ζ(5)@3, ζ(7)@4) — which is **standard Feynman-period weight-counting**, and {3,5,7} = {N_c, n_C, g} is a **small-odd-number coincidence for the first three.** The ladder does not stop at 7.

## Honest scope

- **Self-correction:** T760 is my own prior "proved" theorem. The precision test retracts it. This is the fish-detector firing on my own work — the hardest and most valuable place.
- **Untested here (separate):** T1481's *denominator*-monomial pattern (the rational-part denominators of the low-loop coefficients being BST monomials) is a distinct claim about the *rational* parts; I did not test it. It may be real or numerology — flag for its own check, independent of the (falsified) zeta-free closed form.
- **Does not touch α:** α is RULED (the coupling = the input). This is about the *loop structure*, which is standard QED given α.

## Honest tiers

| claim | tier |
|---|---|
| T760 closed form a_e matches only ~4 ppm; C₂ = 0; falsified at 10⁻¹² | **RIGOROUS — retraction** |
| zetas not eliminable (ζ(3) in the true C₂) | **RIGOROUS** — standard QED |
| zeta-ladder truncation "finite at 3 transcendentals" | **FALSIFIED** (higher loops → ζ(9)+) |
| odd-zeta ordering ζ(2L−1) at loop L; {3,5,7} = BST integers | **standard weight-counting + small-number coincidence** |
| T1481 denominator-monomials | **UNTESTED by me** — separate, flag |
| BST's genuine QED content | **α, RULED — full stop** |

**No bank — a retraction.** F496 is the honest output of the fresh QED-radiative lane: BST does **not** derive a zeta-free closed form for a_e. My own T760 was a ~4-ppm coincidence that zeroes the 2-loop term and fakes it with a cubic at α = 1/137; the electron anomaly genuinely needs the standard QED loops, ζ(3) included. The "zeta ladder at BST primes" is standard weight-counting relabeled with small integers. BST's QED content is α (the coupling), and the loop structure on top is ordinary QFT. Handed to Keeper to adjudicate the T760/T719 retraction.

## Plain-language version

Casey pointed me at a fresh area — the fine details of how the electron's magnetism gets tiny quantum corrections — because the corpus had a striking claim (one I'd made earlier): that the whole infinite tower of quantum corrections collapses into a single clean formula with no weird constants in it. It's a beautiful claim, so I tested it against the real, exquisitely-measured number. It fails. The clean formula agrees only to about 4 parts per million, but that number is *known* to about one part in a trillion — so the formula is wrong by a factor of ten-thousand-plus. And I can say exactly why: the formula, by its shape, has *nothing* at the two-loop level, but two-loop is precisely where the "weird constants" (like ζ(3)) genuinely live. The formula only *looked* right because a different term in it happens to impersonate the real two-loop term at our particular value of the fine-structure constant — a coincidence that would evaporate at any other value. So the honest verdict: BST's real contribution to this corner of physics is the *one* number α (which is solidly banked), and the tower of corrections on top is just ordinary quantum electrodynamics — the "clean closed form" was a mirage, and I'm retracting my own earlier claim. Not the answer I went looking for, but the true one.

— Lyra, 2026-07-08. F496: tested my own T760 closed-form a_e=(α/2π)(1−(2α/π)²)^{2n_C·g} — matches only ~4 ppm (a_e known ~1e-12) → FALSIFIED. C₂=0 (only even powers of α/π inside → can't make the real linear 2-loop term, which carries ζ(3)+ln2); the ~4ppm is a coincidence (140·α/π=0.325≈|C₂|=0.328). Zetas NOT eliminable; Observable-Closure-for-a_e form-cheap. Zeta-ladder truncation also falsified (higher loops → ζ(9)+); ζ(2L−1) ordering is standard weight-counting, {3,5,7}=BST a small-number coincidence. Self-correction (T760 mine). Untested: T1481 denominators. Doesn't touch α (RULED). BST QED content = α, full stop; loops = standard QED. Retraction, no bank.
