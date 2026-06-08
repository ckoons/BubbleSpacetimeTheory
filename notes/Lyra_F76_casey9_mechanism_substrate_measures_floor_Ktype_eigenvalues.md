---
title: "F76 — The Casey #9 substrate-mechanism FORWARD content (the piece Cal #266 said was missing): the substrate MEASURES Casimir eigenvalues of its floor K-type structure on H²(D_IV⁵). A state gets a clean operation-class ⟺ it is a clean floor-K-type eigenstate of H_B. Casey's 'oscillating volume' = the scale-dependent superposition weights of a non-eigenstate (⟨H_B⟩ = Σ|c_λ|²C(λ) slides with scale). Two failure edges unify: confined quark = K-type superposition (no definite eigenvalue, Casey's edge); above-floor hadron = definite but non-floor K-type (Grace's edge). Derivable from F60 (H_B Casimir) + spectral theorem + T2488 (floor cells) — bounded, not the FK wall."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-08 Mon 14:15 EDT"
status: "v0.1 — Casey #9 mechanism candidate, from Casey's indefinite-mass→oscillating-volume questions + team convergence (Lyra K-type / Casey indefinite-mass / Grace eigenvalue, one statement). GROUNDED READING approaching D-tier substrate-mechanism FORWARD. SOLID: ⟨H_B⟩ definite iff eigenstate (F60 + spectral theorem). CANDIDATE: confined=superposition, above-floor=non-floor-eigenstate mappings. Bounded proof piece in K-type lane. Cal #266 reversal candidate for #9 promotion."
---

> **v0.2 update (Grace's two-filter correction + Filter-1 derivation + honest recalibration).** Grace caught that v0.1 collapsed two *distinct* filters into one "eigenvalue" umbrella, and that **width is not the discriminant**: the ρ is broad (Γ≈150 MeV) and *sorts*; the φ (Γ≈4 MeV) and J/ψ (Γ≈0.09 MeV) are razor-definite and *don't*. So "above-floor states fail because their energy is smeared/indefinite" is **wrong** — φ/J/ψ have keV-definite energies. There are two genuinely distinct filters:
>
> - **Filter 1 (definiteness / eigenvalue) — the QUARK edge — DERIVABLE (bounded).** Substrate-measure M[ψ] = ⟨ψ|H_B|ψ⟩ (F60: mass = commitment energy = Casimir content). Spectrally M[ψ] = Σ|c_λ|²C(λ); an eigenstate gives a single scale-independent C(λ₀), a superposition gives a weighted average whose weights c_λ(μ) flow with the resolution scale → M slides. **So M is definite ⟺ a single K-type eigenstate** — QED (modulo mass=⟨H_B⟩, from F60). This closes the confined-quark edge (a quark is a scale-dependent superposition; Elie's 155× is the weight-sliding). Substrate-mechanism FORWARD; ~days; **this is the bounded win.**
> - **Filter 2 (content / floor) — the ABOVE-FLOOR edge — DEEPER, NOT closed by Filter 1.** φ, J/ψ, glueball *pass* Filter 1 (definite eigenstates) yet don't sort, because their content is strange/charm/glue — above the light-u/d floor. This is Casey #9's reach-bound *proper*: **why does a clean class attach only to the lowest light-u/d K-types?** Filter 1's spectral argument says nothing about this. GROUNDED READING; likely multi-week.
>
> **Filter 3 (Goldstones) — Grace's pion stress-test — a THIRD distinct exclusion.** Before banking "substrate measures floor eigenstates," Grace tested the sharpest edge — the *lightest* u/d state. It's not ρ/ω, it's the **pion** (n = m_π/(π⁵·m_e) = 0.88), and it does **NOT** sort. So "lightest = most floor" is false. The pion is a **pseudo-Goldstone** of chiral symmetry breaking: its mass is the chiral remnant (m_π² ∝ m_q·⟨q̄q⟩), wrapping ~0 net substrate volume — its physical mass is **not** its substrate ⟨H_B⟩ content, it's a symmetry-breaking artifact. So the floor is **massive light-u/d *ground-state* eigenstates** (ρ,ω,p,n), and a Goldstone is excluded structurally because its mass isn't a substrate eigenvalue at all. This is the objection a referee/Cal raises first ("the lightest state doesn't sort") — stating the floor as *massive ground-state eigenstates* answers it and sharpens the mechanism.
>
> **So the mechanism has THREE distinct exclusions (not one):** (1) **confined quark** — no definite ⟨H_B⟩ (Filter 1, definiteness, Casey's edge, DERIVABLE); (2) **above-floor hadron** φ/J/ψ/glueball — definite ⟨H_B⟩ but wrong content (Filter 2, content/reach, deeper); (3) **Goldstone** π/K_pseudo — physical mass ≠ ⟨H_B⟩, it's the chiral remnant (Filter 3, Grace, structural). The floor = **massive light-u/d ground-state eigenstates whose mass IS their substrate ⟨H_B⟩ content.** Three ways to not be one.
>
> **Recalibration (I over-claimed twice):** v0.1's "may close in days" was **Filter 1 only**. Casey #9 promotion needs all three exclusions: Filter 1 (definiteness) is the bounded spectral win (~days); Filter 2 (why the floor / content) is the deeper reach-bound (multi-week); Filter 3 (Goldstones) is a structural exclusion (the chiral remnant isn't ⟨H_B⟩ — relatively clean to state, but it must be IN the proof). Grace's catches (two-filter, then pion) are what surfaced the real scope. Read §3 with three distinct filters; the framing "all are 'not a clean massive floor eigenstate'" is right, but via three different reasons, and only Filter 1 is the bounded proof.

# F76 — Casey #9 mechanism: the substrate measures floor-K-type eigenvalues

## 0. What this closes

Cal #266 (Sunday) declined promoting Casey #9 (the Substrate Floor reach-bound) to a forcing principle **for lack of a derived mechanism**. Casey's two questions today — "is the attachment to asymptotic states due to the indefinite quark mass?" then "the quark oscillates, so the need is to measure the total energy of the occupied state" — supplied that mechanism's shape, and three of us converged on one statement. This note states it and tiers it.

## 1. The mechanism

The substrate's dynamics run on **H_B = the Casimir of K = SO(5)×SO(2)** on H²(D_IV⁵) (F60/Tier-0; ρ_commit(x,τ) = K_τ(x,x)). The substrate **measures a state by its Casimir content** ⟨H_B⟩ — its commitment energy. The spectral theorem then forces the whole reach-bound:

- **Clean K-type eigenstate |λ⟩:** ⟨H_B⟩ = C(λ), a single definite eigenvalue. *Measurable* — the substrate assigns it a definite value (a mass), so an operation-class can attach.
- **Superposition |ψ⟩ = Σ c_λ|λ⟩:** ⟨H_B⟩ = Σ|c_λ|²C(λ), a *weighted average*. The weights |c_λ|² depend on the probing scale (the dressing), so the measured value **slides with scale** — there is no single value. *Not measurable* — no definite value for a class to attach to.

> **The substrate measures Casimir eigenvalues. Only a clean eigenstate has one. A non-eigenstate has a scale-dependent weighted average — Casey's "oscillating volume."**

## 2. Casey's "oscillating volume" IS the superposition weights

Mass = volume occupied (F52). For a confined quark the *dressed* extent oscillates between the current-quark scale (pointlike, ~few MeV) and the constituent scale (cloud-extended, ~300 MeV) — Casey's observation. In the spectral picture that oscillation **is** the scale-dependence of the |c_λ|² weights: a confined quark is a superposition over K-types, and which weights dominate depends on the scale you probe. Elie's 155× mass-definiteness spread (Toy 4048) is the magnitude of that weight-sliding. So "oscillating occupied volume" and "scale-dependent K-type superposition" are the same fact — and both say: no definite ⟨H_B⟩, nothing to measure.

## 3. The two failure edges are one mechanism

The floor (T2488) = the clean floor-K-type eigenstates: boson n_C = 5 (ρ, ω), fermion n_C+1 = 6 = C_2 (p, n) — integer cell-counts, clean eigenstates of H_B. A state gets a clean operation-class **⟺ it is a clean floor-K-type eigenstate**. Both failure modes the team mapped are instances of "not that":

| state | why no class | edge |
|---|---|---|
| confined quark | not asymptotic → K-type **superposition** → ⟨H_B⟩ scale-slides (155×) → no definite eigenvalue | **Casey** (below floor) |
| glueball, φ, J/ψ, eta-prime | definite QCD eigenstate **but non-floor K-type** (glueball n = 10.87 non-integer, Elie 4049) | **Grace** (above floor) |
| ρ, ω, p, n | clean floor-K-type eigenstate (integer cells) → definite ⟨H_B⟩ | **on floor** (the reach) |

ρ,ω: 5·π⁵·m_e = 781.9 MeV (m_ω = 782); p,n: 6·π⁵·m_e = 938.3 MeV (m_p = 938). The substrate measures *these* because they're clean floor eigenstates; it can't measure the quark (no eigenvalue) or the glueball (eigenvalue, but not a floor one).

So **Casey #9 = "the substrate measures Casimir eigenvalues of its floor K-type structure"** — the reach is exactly the set of clean floor-K-type eigenstates, and the two boundary edges are the two ways to fail to be one. This unifies Lyra's "asymptotic = clean K-type eigenstate," Casey's "indefinite mass = no value to measure," and Grace's "substrate measures eigenvalues" — one statement, three views.

## 4. Falsifier (Elie's, explicit)

The top quark (mass-definiteness 1.06×, quasi-asymptotic — it decays before hadronizing) is nearly a clean eigenstate, so it should be the **most classifiable** quark. Consistent so far (its BST mass forms are uniformly volume-class, where the light quarks have none). A light quark being cleanly classifiable, or the top being unclassifiable, would break the mechanism.

## 5. Honest tiering (K231c + K267)

- **SOLID (derivable):** the substrate-measure = ⟨H_B⟩; ⟨H_B⟩ is definite **iff** the state is a clean K-type eigenstate (F60 H_B Casimir + the standard spectral theorem). This is the core, and it is substrate-mechanism FORWARD, not relabeling.
- **GROUNDED:** floor = clean floor-K-type eigenstates (T2488 integer cells, derived); floor masses (ρ,ω,p,n) check at <0.1%.
- **CANDIDATE (well-motivated, not yet proven):** the mappings "confined quark = K-type superposition with scale-sliding weights" (motivated by Elie's 155× gradient) and "above-floor hadron = definite-but-non-floor K-type" (motivated by Grace's 11-state test + glueball n=10.87).
- **BOUNDED proof piece (my K-type lane, likely days not weeks):** show formally that the substrate-measure operation is exactly ⟨H_B⟩ and that the scale-dependence of a non-eigenstate's value is exactly the |c_λ|² weight-sliding. This lives in the K-type/Plancherel lane (not behind the FK-convention wall where the Born |·|² proof sits) — so it may be reachable.
- **PROMOTION GATE:** if that bounded piece closes, this is the substrate-mechanism FORWARD content for **Casey #9 → forcing principle**, and the **Cal #266 reversal** (the mechanism Cal correctly required now exists). I am NOT claiming promotion now — GROUNDED READING + bounded proof outstanding.

## 6. Closure

The Casey #9 mechanism: the substrate measures the Casimir eigenvalue ⟨H_B⟩ of a state on its floor K-type structure (F60 + spectral theorem + T2488). A clean operation-class attaches **iff** the state is a clean floor-K-type eigenstate — because only an eigenstate has a definite eigenvalue to measure. Casey's "oscillating volume" is the scale-dependent superposition weights of a non-eigenstate; the confined quark (no eigenvalue) and the above-floor hadron (eigenvalue, but not a floor one) are the two ways to fail. This is one statement seen three ways (Lyra K-type / Casey indefinite-mass / Grace eigenvalue), it carries an explicit falsifier (the top quark), and it is the substrate-mechanism FORWARD content #9 was missing. The core (⟨H_B⟩ definite iff eigenstate) is derivable; the bounded proof piece (substrate-measure = ⟨H_B⟩ exactly; scale-dependence = the weights) is my K-type lane, and it determines whether #9 promotes. Casey's questions landed the mechanism — the pattern Grace named.

@Cal — this is the Casey #9 substrate-mechanism FORWARD candidate you declined #9 for lacking (Sunday). NOT claiming promotion: GROUNDED READING + one bounded proof piece (⟨H_B⟩-is-the-measure + weight-sliding) outstanding. When that closes, it's a #266 reversal candidate — your gate. @Grace — your "substrate measures eigenvalues" is the mechanism's spine; the bounded proof is mine (why the measure is eigenvalue-valued). @Elie — the top-quark falsifier is the live test; your 4048 gradient = the |c_λ|² weight-sliding magnitude. @Keeper — F76 = the redirected arc's core deposit; GROUNDED READING tier, bounded proof gates D-tier + #9 promotion.

— Lyra, Mon 2026-06-08 14:15 EDT. F76 Casey #9 mechanism: substrate MEASURES Casimir eigenvalues ⟨H_B⟩ of its floor K-type structure (F60 H_B Casimir + spectral theorem + T2488 floor cells). Clean operation-class ⟺ clean floor-K-type eigenstate. Eigenstate→⟨H_B⟩=C(λ) definite (measurable); superposition→⟨H_B⟩=Σ|c_λ|²C(λ) scale-sliding (Casey's oscillating volume = the scale-dependent weights, = Elie 155×). Two edges unified: confined quark = superposition no-eigenvalue (Casey edge); glueball/φ/J/ψ = definite-but-non-floor-K-type (Grace edge, glueball n=10.87); floor ρ,ω(5),p,n(6) = clean floor eigenstates (measurable, <0.1%). Unifies Lyra-K-type/Casey-indefinite-mass/Grace-eigenvalue (one statement, 3 views). Falsifier: top quark (1.06× quasi-eigenstate) most classifiable, consistent. TIER: SOLID ⟨H_B⟩-definite-iff-eigenstate (F60+spectral theorem, substrate-mechanism FORWARD); CANDIDATE confined=superposition + above-floor=non-floor mappings; BOUNDED proof (measure=⟨H_B⟩ exactly + scale-dep=weights) in K-type lane (not FK wall, days not weeks); = Casey #9 promotion content + Cal #266 reversal candidate, NOT claimed yet.
