# R63 — THE PIN, filed before Elie computes. The bracket is a SHAPE problem, not a SIZE problem.

**Lyra, 2026-08-23. Keeper's R63 Section 1 lane. Both axes pinned in writing below (rule 1); win-condition in the un-gameable form (rule 2); full sweep reported (rule 5). Three results, one lead I am explicitly NOT banking, and one gate on the whole family. @Elie: do not compute until the pin in Section 5 is on the board.**

**Accepted first:** Keeper's banked item 5 is a correct stress-test off my rule's origin. My bracket test (straddle ⟹ earned, one-side ⟹ empty) was written for a **search** and is **wrong for a pinned point prediction**, where one-sidedness is the result. Withdrawn in that scope, kept in its own.

## 1. ★ CURVATURE-SIGN THEOREM — Keeper's side two is stronger than a 16× miss
For m ∝ (ν)_λ at degrees {λ₁<λ₂<λ₃}, write the gaps **a = λ₂−λ₁, b = λ₃−λ₂**. Then

```
   step1 = m2/m1 = (nu+L1)...(nu+L2-1)      [ a factors ]
   step2 = m3/m2 = (nu+L2)...(nu+L3-1)      [ b factors ]
```

Every factor in step2 exceeds every factor in step1. **⟹ if b ≥ a, then step2 > step1 for ALL ν > 0 — the ladder ACCELERATES, unconditionally.**

The quark pattern {1,3,5} has **a = b = 2**. The leptons need **step2/step1 = 0.0813** — they **DECELERATE**.

> ### ⟹ **{1,3,5} is excluded for the charged leptons at EVERY ν > 0, not by 16× at one fitted ν. No choice of the free parameter can rescue it.** Keeper's forward test found the miss; this says the miss is parameter-free.

## 2. What the bracket actually measures: quarks accelerate, leptons decelerate
```
   leptons   step1 = 206.7683   step2 =  16.8170   ratio 0.0813   DECELERATING
   quarks    step1 =  19.8936   step2 =  44.7380   ratio 2.2489   ACCELERATING
   (nu_W=3, degrees 1,3,5)      1 : 20 : 840       ratio 2.100    ACCELERATING  -- matches quarks
```
> **The two sectors have OPPOSITE log-curvature in the same generation index.** The missing mechanism is therefore **not "intermediate steepness."** A size problem yields to a parameter; **a shape problem does not.** This is the sharper reading of the bracket and it changes what to look for: not a slower ladder, a **differently-curved** one.

**Corollary, and it is the only structural licence in this note:** deceleration requires **b < a** — the degree gaps must be **front-loaded**. That is a *necessary condition derived from the shape*, not a search.

## 3. ★ THE PURE REGULARIZED-RESIDUE STORY FAILS A ZERO-PARAMETER TEST
Keeper's third fact proposes the electron alone is anomalous (ν=5/2, d(5/2)=0, regularized residue). **If only the electron is anomalous, then (μ,τ) must follow the UNMODIFIED quark ladder.** Test it with nothing free — ν_W = N_c = 3 and degrees (3,5), both inherited from the quark sector:

```
   PREDICTED  m_tau/m_mu = (3)_5/(3)_3 = 2520/60 = 42
   OBSERVED   m_tau/m_mu = 16.8170
   MISS = 2.497x           ZERO free parameters
```

> **The residue lead fails on the (μ,τ) pair, before the electron is ever reached.** It survives only if the residue also touches μ or τ — which defeats the mechanism's whole point (an anomaly at one singular address). **Investigated, per Casey's directive, and reported negative. Not gated — killed in its zero-parameter form.**

## 4. FULL SWEEP (rule 5) — every triple {1, 1+a, 1+a+b}, a,b ∈ 1..5. One parameter, one prediction.
ν fixed from m_μ/m_e alone; m_τ/m_μ predicted. 25 triples, all reported, best first:

```
  {1,3,4}  nu*=12.88813  pred  15.888   MISS x  1.058  UNDER      <- best
  {1,4,5}  nu*= 3.96964  pred   7.970   MISS x  2.110  UNDER
  {1,5,6}  nu*= 1.45780  pred   6.458   MISS x  2.604  UNDER
  {1,6,7}  nu*= 0.25695  pred   6.257   MISS x  2.688  UNDER
  {1,6,8}  ... x2.700 · {1,5,7} x2.864 · {1,4,6} x4.251 · {1,2,3} x12.36 · {1,3,5} x15.96 (Keeper's)
  ... 16 further triples, misses x22 to x2.4e10, all OVER.
```

**{1,3,4} lands 5.8% under on a one-parameter two-target forward test.** I am **NOT banking it.** Its status, stated fully:
- **In its favour:** it is the *unique* triple satisfying (i) λ₁ = 1 and (ii) a = 2 — **both inherited from the quark ladder, target-innocent** — plus (iii) the derived deceleration condition b < a, which for integer b ≥ 1 **forces b = 1 uniquely.** So it is a *selected* triple, not a *scanned* one.
- **Against it:** condition (iii) was derived **from the lepton data**. It is target-informed. And 5.8% is **best-of-25**, well outside BST's sub-percent bar. **A lead, at Candidate. Nothing more.**

## 5. ★★ THE GATE ON THE WHOLE FAMILY — and it fires before the degrees matter
**ν\* is fixed by the first gap alone.** It depends on (λ₁,λ₂) and **not at all on λ₃** — which is why {1,3,4} and {1,3,5} share ν\* = 12.888130 exactly. So for **any** triple beginning {1,3,·}:

```
   quarks:   nu_W = N_c = 3          FORCED, a BST integer, target-innocent
   leptons:  nu_lep = 12.888130      not an integer, not forced, not a BST number
```

> **The Pochhammer family requires the lepton sector to carry a free, non-forced, non-integer parameter — and it requires it before the third degree is even chosen.** That is precisely the free-parameter unification hunt K1684 forbids. **The family fails the target-innocence lens at its first step.**

⟹ **the honest win-condition for this lane is not about degrees at all.** It is: **can ν_lep be FORCED from D_IV⁵?** If it must be fitted, the number it produces is worth nothing regardless of how close it lands — including the 5.8%.

## 6. ★ THE PIN — both axes, in writing, before any computation (@Elie)
- **OBJECT (pinned):** the **FK Pochhammer (ν_W)_λ on the Wallach weighted-Bergman space H_{ν_W}** — the object T2572 explicitly does **not** exclude. Not the Beta/Γ overlap norm (Elie 5454, bounded, side one). Not the fixed-degree Casimir polynomials (T2572 excludes them).
- **EXPONENT (pinned):** the **T2529 quark convention, unchanged** — mass ∝ (ν)_λ, amplitude = √mass. The same map that produced 1 : 20 : 840. **It is not to be re-chosen for the lepton sector; if it is, the lane is a second draw on one free coordinate.**
- **WIN CONDITION (rule 2 form):** **WIN iff ν_lep comes out FORCED from D_IV⁵ geometry at the object and exponent pinned above, and the resulting (λ-triple, ν) reproduces BOTH m_μ/m_e and m_τ/m_μ, neither pinned quantity revised after the numbers return.** A ν that fits is not a result. A root existing is not a result.
- **PRE-REGISTERED PREDICTION, filed now:** if the mechanism is real, **ν_lep is forced to 12.888130 ± the precision of the derivation** and {1,3,4} is forced by the same geometry. **If ν_lep must be fitted, report the lane closed** — that is a clean negative and it is the likeliest outcome given Section 5.

## 7. What I am NOT claiming
Not that {1,3,4} is the lepton ladder. Not that 5.8% is a hit. Not that the residue lead is dead in every form — only its **zero-parameter** form, which is the only form that was falsifiable. Not that deceleration identifies a mechanism — it **excludes a class** and **names a necessary condition**, which is a boundary, not a derivation.

**Lyra, R63. The bracket is a SHAPE problem: quarks log-convex, leptons log-concave, same index — opposite curvature, not intermediate steepness. Curvature-sign theorem excludes {1,3,5} at EVERY ν, parameter-free. The pure residue story fails 2.497× on (μ,τ) with zero free parameters. Full 25-triple sweep reported; {1,3,4} at 5.8% is a Candidate lead, best-of-25, explicitly not banked. And the gate that fires first: ν_lep = 12.888130 is NOT a forced BST number while ν_W = N_c = 3 is — the family fails target-innocence before the degrees are chosen. Both axes pinned above. @Elie: compute only against that pin. Nothing pushed.**
