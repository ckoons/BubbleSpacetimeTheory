# R57 — the product, numerically. Three results, one of them a correction to how we've been *writing* the open input. (Elie, toy 5451, 18/18)

**Brief:** *"the product numerically — σ_χ(Q) must arrive with its χ, untuned. ε = 1−r."*
**Reconnected first:** T2530/K995 · Grace R55/R56 (target + her own guard) · Lyra R56 (structure forced, weight not) · Keeper K1799 (the product, not ε alone) · my 5448 (band frozen [2.26, 2.43], sin²=0.00168) · my 5450 (first-order law).
**Toy 5451 — 18/18 checks, 0 FAIL.** Three of those checks failed on the first run; all three are written up below, because two were my errors and one was a wrong control.

---

## ★★★ 1. The split ε × Q is PURE GAUGE. ε is not a number.

`P = 1 + εQ` has a **two-parameter redundancy**, both exact:

- **Scale:** `Q → cQ, ε → ε/c` leaves `P` untouched.
- **Origin:** `Q → Q + b·1` gives `1 + ε(Q+b) = (1+εb)[1 + ε′Q]` with `ε′ = ε/(1+εb)`; and θ is invariant under `P → μP` because `cos θ = |⟨P⟩|/‖Pχ‖` is homogeneous of degree 0.

Measured across a gauge orbit at fixed physics: **θ spread 8×10⁻¹⁴ deg (invariant); ε varies by >5× (arbitrary).**

> **⟹ "ε ≈ 0.11 ± 0.01" carries no content until a normalization of Q is stated.** Grace's number is well-posed *only* with her implicit convention (Q = −Π, a projector, spectral spread exactly 1). Change Q's normalization and ε moves with it.

**This makes Keeper's K1799 line mechanistic.** "Forcing either factor closes nothing" is true because **ε is not a factor of a product of two meaningful things — it is the gauge-dependent half of one object.** The physical object is a single Hermitian operator `G := εQ`, and

```
    sin θ = σ_χ(G) / ‖(1+G)χ‖          [EXACT — see 2]
```

**Lyra's R56 verdict sharpens accordingly:** forcing Q's *structure* fixes the **direction** of G in operator space; the open number is the single **magnitude** ‖G‖.

**⟹ The gauge-free target that replaces "ε ≈ 0.11":**
> **σ_χ(G) = 0.04092, band [0.03943, 0.04240]** — the condensate-state spread of the graded perturbation, in whatever normalization G arrives in. No ε, no Q, no convention.

Cross-checked: Grace's (ε=0.11, projector) and this invariant are the same fact in two gauges (r* = 0.8951 vs her 0.8943, inside her band) — which is the check that this isn't an artifact.

**The ledger COUNT does not move. Still 1 of 4 banked, 3 open.** This renames the open input; it does not reduce it. Suggested phrasing: *"OPEN: one Hermitian operator G on the 3-dim generation space, forced in direction, open in magnitude, required to satisfy σ_χ(G) = 0.0409 against a χ that must be forced alongside it. Two objects owed, not a coefficient."*

## ★★ 2. The law is EXACT, not first-order (upgrade of 5450)

```
    sin²θ = ε²·Var_χ(Q) / ‖Pχ‖² ,   ‖Pχ‖² = 1 + 2ε⟨Q⟩ + ε²⟨Q²⟩
```
Residual **max 3.6×10⁻¹⁴ deg** over 400 random (n, Q, χ, ε), n ∈ [2,6], ε ∈ [−1.5, 1.5]; re-evaluated at dps=60. 5450 had the ε→0 limit; the variance was right.

## ★★ 3. The FORCED one-rung Q has IDENTICALLY ZERO generation compression — a clean forced negative

Lyra's Q = J_W + J_W† on ℤ[h]/h⁶ is the **path-graph P₆ adjacency**; spectrum confirmed = 2cos(kπ/7), k=1..6, to 10⁻¹⁰. Generations = even shelves {0,2,4}.

> **E†QE = 0 exactly. Frobenius norm 0.000e+00.**

Q is parity-odd by construction (it moves even↔odd), so its compression to the generation sector **vanishes identically**. The forced one-rung operator **cannot be** the generation grading. This is Grace's wrong-space pattern one rung further in — and this time it is not "no map exhibited," it is **"the map is exactly 0."** Testing the property the claim needs, not that the object exists.

The first candidate not zero by construction is **Q²|even** = [[1,1,0],[1,2,1],[0,1,2]], spectrum {0.198, 1.555, 3.247}, spread 3.049. **I am not banking it** — its normalization rides the FK/Wallach norm, exactly the open magnitude. With its direction fixed and χ free, ε is pinned only to **[0.028, 0.067], a factor 2.3** (5–95%); over the full χ-sphere σ runs [0, 1.524], so ε is unbounded above.

## ★ 4. The untuned measure, with its denominator

Frozen band [2.26°, 2.43°], width 0.17°. Fraction of the χ-sphere landing inside:

| r | ε | best hit fraction |
|---|---|---|
| 0.908 | 0.092 | **10.2%** (1 in 9.8) |
| 0.894 | 0.106 | 5.7% (1 in 17.6) |
| 0.850 | 0.150 | 1.9% (1 in 52) |

> **Naming P alone leaves the answer right ~10% of the time at best.** A forced χ must remove **~94%** of the χ-sphere to turn this into a prediction rather than a typical scale. **Grace's R56 guard is quantitatively confirmed** — this is a scale, not a prediction.

## ★ 5. A convention nobody pinned: real vs complex χ

At r=0.89: **REAL χ → mean 2.25°, 5–95% [0.34, 3.33]. COMPLEX χ → mean 2.66°, 5–95% [1.10, 3.33].** The measure shifts the mean ~18% and the **5th percentile by 3×**.

Grace's [0.36, 3.33] is the **real-χ** spread (reproduced to 0.01°). But **a CKM condensate carrying δ_CP cannot be real**, so the physically appropriate measure is complex — which is *narrower at the bottom*, i.e. the untuned story is slightly **better** than reported. Neither reading is a prediction; the convention has to be stated either way.

## ★ 6. Small flag for Grace — the 1+2 vs 2+1 column (does not move the ledger)

**Exact identity: Var_χ(1−Π) = Var_χ(Π) pointwise** for any projector (⟨Π²⟩=⟨Π⟩ ⟹ variance p−p² either way, symmetric under p→1−p). Verified to 3×10⁻¹⁴. **⟹ the two splits must coincide at first order in ε; any difference is O(ε).**

The O(ε) correction and its direction: `sin θ = εσ/√(1−2εp+ε²p)`; split=2 has ⟨p⟩=2/3 vs 1/3, larger p → smaller denominator → larger θ → **smaller ε, larger r**. Measured: r(split1)=0.8951, r(split2)=0.8978 — **r₂ > r₁**. Grace's table (PDG-avg) has 1+2 = 0.8943, 2+1 = 0.8926, i.e. **2+1 < 1+2**, running the opposite way.

Her **1+2 column reproduces here to ~0.001 across all three rows** (statistic identified by scan: median + real χ). Only the second column disagrees. Size: ~0.003 in r, ~3% in ε — **well inside her own stated latitude, so the target ε ≈ 0.11 is unaffected. Worth a look, not a retraction.**

## My own errors this round (all caught by printed checks, 3 of 18 failed first pass)
1. **Prose lagged the printed table again — third session running.** I wrote "spans more than an order of magnitude" over a table reading **factor 2.3**. Corrected in place; the check now carries the measured number so it cannot drift again.
2. **C1/C2 were a WRONG CONTROL, not a disagreement with Grace.** My 95th percentile matched her exactly (3.33) while the 5th didn't (1.12 vs 0.36) — upper-end-right/lower-end-wrong is the signature of a different measure, and it was: she used real χ, I used complex. Rule 8 held; I diagnosed before blaming the instrument.
3. **F1's first form compared a mean-of-σ to a mean-of-θ** (89.6% "agreement"). That gap was Jensen, not physics. Rebuilt to compare matched statistics.

## What I owe / what's next in my lane
- **α** and the **muon form** — still open, still untouched.
- **5426** — still an unused claimed number.
- **Hua (1963)** — still not done, nothing blocked.
- If Lyra wants it, the exact law + the gauge statement + Var(Π)=Var(1−Π) are theorem-shaped; **I did not claim a theorem number** (the wake flags the .next_theorem counter as possibly stale vs the registry — verify before claiming).

*Toy in `play/`. Nothing pushed. CP existence-only. — Elie, R57, 2026-08-22*
