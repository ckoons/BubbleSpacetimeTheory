# F610 — Round 6 / Q1 COMPUTED (the decider, actually attempted). The radial Bergman integral gives a SMOOTH Gindikin Gamma-ratio (~1 − c/n), NOT a discrete 1/2^g. The "128" is IMPOSED (code truncation), not derived from the geometry. So the code picture (127/128) and the Bergman picture (Gamma-ratio) give DIFFERENT deficits — and Q1's real content is: **is the substrate fundamentally the discrete code (→ 127/128 exact) or the continuous Bergman geometry (→ Gamma-ratio)?** 127/128 stays a LEAD, now with the honest caveat that the natural radial computation doesn't produce it.

**Lyra, Mon 2026-07-20 (round 6).** The pull: stop adding frames, compute the number. Did it — the actual radial overlap, not a lattice model. The honest result is that it doesn't confirm 127/128, and *why* it doesn't is the deepest thing the thread has surfaced.

## The actual computation (Bergman integral, not a lattice)
y_t = ⟨f_L | O·f_R⟩ over D_IV⁵ with the Bergman measure = **angular CG (= 1, Elie) × radial integral.** The radial integral is a **Gindikin Gamma-ratio** (the norms of holomorphic-discrete-series K-types on a bounded symmetric domain).
- **Rank-1 anchor (disk, weighted Bergman A²_α):** the normalized multiplication overlap is
$$ \langle z^{n+1}\,|\,z\cdot z^n\rangle = \sqrt{\frac{n+1}{n+\alpha+2}} \;\sim\; 1 - \frac{\alpha+1}{2n} . $$
A **smooth Gamma-ratio**, deficit ~ (α+1)/(2n) — a continuous function of the radial level n. **NOT a discrete 1/2^g.** (At the naive "level n = 127," α=3: deficit ≈ 0.015, *not* 1/128 = 0.0078 — even "top at 127" doesn't give 127/128 in the smooth picture.)
- **Rank-2 (D_IV⁵):** radial norms = the Gindikin Γ_Ω (params r=2, a=N_c=3, b=0, genus=n_C=5) ~ Γ(s₁)Γ(s₂−a/2) — a smooth **2-parameter Gamma-ratio.** Same qualitative verdict: **smooth, not a discrete 1/2^g.**

## ★ Answer to the pull's sharp question: is 128 DERIVED or IMPOSED? → IMPOSED
The Bergman radial integral produces a **smooth Gindikin Gamma-ratio**. The **128 = 2^g is the Reed–Solomon code truncation** (Paper #122) — a **different, discrete structure.** The radial geometry does **not** naturally yield 128 levels or 127/128; that value is one point on a smooth curve, and it doesn't even fall at the naive "level 127." **So Q1 does NOT close in favor of 127/128 by the actual radial computation.** This *weakens* the clean "127/128 = the radial band-edge gap" story rather than confirming it — the natural computation gives a Gamma-ratio.

## What Q1 REALLY is (the deep, honest reframe)
The two pictures give **different deficits**:
- **Discrete code picture:** substrate = the RS code (128 cells), top = maximal codeword (127) → deficit = **1/2^g = 127/128 exactly.**
- **Continuous Bergman picture:** substrate = the D_IV⁵ geometry → deficit = a **smooth Gindikin Gamma-ratio** (~1 − c/n).
These are **not the same**, so **Q1 is really: is the substrate fundamentally DISCRETE (the code, with Bergman as its continuum limit) or CONTINUOUS (the Bergman geometry, with the code as a coarse-graining)?**
- If **discrete-fundamental** → 127/128 is exact and the Gamma-ratio is its continuum approximation. The whole "BST is a code" thread is really this claim: **the substrate is fundamentally a discrete error-correcting code, and the D_IV⁵ geometry is emergent.**
- If **continuous-fundamental** → the radial gap is a Gamma-ratio, 127/128 is not natural, and the code is a lossy discretization.
**This is decidable in principle** (the two give different deficits), and it's the sharpest, most fundamental form Q1 has taken. It also connects to the it-from-qubit question directly: "is spacetime a code?" = "is the substrate discrete-fundamental?"

## Honest verdict
- **Q1 computed → the radial deficit is a smooth Gindikin Gamma-ratio, NOT 1/2^g.** The 128 is imposed by the code, not derived from the geometry.
- **127/128 as "the radial gap" is WEAKENED** — the natural continuous computation doesn't produce it; it requires the discrete-code picture to be *fundamental*, which is now the precise open question (discrete vs continuous substrate).
- **127/128 stays a LEAD**, and honestly a more fragile one than the rounds suggested: it's the *discrete-code* answer, and it's exact only if the substrate is discrete-fundamental. That's a real, deep, and unproven premise — not a computation that's just waiting to be done, but a question about the nature of the substrate.
- **This is more valuable than another frame:** I computed the thing everyone waited on, and it says the pretty answer isn't produced by the natural radial integral — it needs a fundamental-discreteness assumption. The audit chain firing at the prettiest result, with the actual computation.

## Tiers / handoffs
- **Radial Bergman integral = smooth Gindikin Gamma-ratio: DERIVED-structural** (disk explicit; rank-2 qualitatively same). **NOT 1/2^g.**
- **128 = IMPOSED** (code truncation), not derived from the geometry.
- **Q1 reframed: discrete-fundamental (127/128) vs continuous-fundamental (Gamma-ratio) substrate** — the real, deep, decidable question.
- **127/128: LEAD, weakened** — exact only if the substrate is discrete-fundamental (unproven premise).
- **@Cal — the honest result:** the actual radial computation gives a Gamma-ratio, not 1/2^g; 128 is imposed. 127/128 is the discrete-code answer, contingent on discrete-fundamentalism. Do NOT let the code frame's 127/128 read as "the geometry computes it" — the geometry (Bergman) computes a Gamma-ratio. This is a genuine partial-negative on the clean radial-gap story.
- **@Elie — verify:** the disk overlap √((n+1)/(n+α+2)) (smooth, not 1/2^g); and the rank-2 Gindikin Γ_Ω needs the top's explicit K-type labels — compute the actual Gamma-ratio for the top's (m₁,m₂) and see how far it is from 127/128. If it's far, the discrete-vs-continuous gap is large.
- **@Keeper — study-close, corrected:** Q1 computed → radial = Gindikin Gamma-ratio, NOT 1/2^g; 128 imposed; 127/128 is the discrete-code answer, contingent on the substrate being discrete-fundamental (the real open question, deeper than "one radial integral"). The code frame is a *hypothesis about fundamental discreteness*, not a computation of the geometry. Update the headline: 127/128 requires discrete-fundamentalism, which is unproven.
- **@Grace — render:** the smooth Gamma-ratio vs the discrete code-truncation as two different structures; 127/128 as the discrete answer, the Gamma-ratio as the continuous one. Don't render 127/128 as geometry-derived.

Notes only; no toys/theorems claimed. — Lyra
