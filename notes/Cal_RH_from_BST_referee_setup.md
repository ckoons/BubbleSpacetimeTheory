---
title: "RH from BST — a referee's setup: what exists, where the gaps are, and the only viable path"
author: "Cal A. Brate (visiting referee)"
date: "2026-06-15 Monday 12:33 EDT"
status: "Referee scoping per Casey's request (a setup of what might work for RH from BST). NOT a proof; a map of obligations vs. what BST has. Honest tier throughout."
---

# RH from BST — referee setup

Casey asked for a setup of what might actually work for Riemann from BST. This is the cold-eyed map: what BST genuinely has, where each attempt breaks, the universal obstacle, and the only path with a chance — plus whether BST has any real edge on it.

## 1. What BST genuinely has (real — credit)

**A correct realization.** ζ(s) appears as the constant term of an Eisenstein series on SO_0(5,2); the Harish-Chandra / Gindikin-Karpelevič c-function (the scattering matrix of the Bergman Laplacian on Γ\D_IV⁵) carries ζ, and the Riemann zeros are the zeros of that c-function. This is standard automorphic theory, and D_IV⁵ = SO(5,2)/[SO(5)×SO(2)] is a genuine rank-2 instance. This is NOT numerology — it is a real vehicle, and it is the legitimate reason BST can even be in the RH conversation. The c-function's arithmetic factors are ξ(2s), ξ(2s−2), ξ(2s−4) (theta-lift). Some partial spectral results (temperedness of the SO(5,2) automorphic spectrum; wall projection) appear genuine.

## 2. The two attack routes, and where each breaks

### Route A — self-adjointness / Maass-Selberg / "rank-2 overdetermination" (theta-lift, BST_RH_AC_Proof, L13)
The distinctive BST claim: the B₂ root system's three exponents (1:3:5) "overdetermine" the zeros — "three rulers that don't share common factors," so the only location consistent with all three is Re(s)=1/2; rank 1 is insufficient, rank 2 forces the line.

**This does not work, and the reason is the same independence failure flagged all session (Cal #35).** The "three exponent constraints" are not three independent functions — they are the SAME ζ at three SHIFTED arguments: the c-function carries ξ(2s), ξ(2s−2), ξ(2s−4). A single ζ-zero ρ therefore produces c-function zeros at three spectral points (s = ρ/2, ρ/2+1, ρ/2+2) — one zero replicated at three offsets, NOT three independent measurements of where ρ is. Measuring with three copies of the *same* ruler at three offsets pins the length no better than one ruler. So the "rank-2 overdetermination" is illusory.

Stripped of the illusory overdetermination, Route A reduces to the canonical non-sequitur: c(s)c(−s)=1 (unitarity on the axis = the functional equation) forces the zeros to be **reflection-symmetric about the line, NOT on it.** Self-adjointness makes the continuous spectrum real and the on-axis Plancherel density non-negative — both automatic, and both silent about where the off-axis c-function zeros sit. A zero at ρ off the line paired with a pole at its reflection is perfectly consistent with unitarity on the line. This is exactly why the Eisenstein/Selberg spectral theory — fully developed for 60 years — does not prove RH. Route A is that theory with an illusory overdetermination bolted on.

### Route B — Weil positivity via the Arthur trace formula (BST_RH_Weil_Positivity_Proof)
The legitimate strategy: prove W(g) = Σ_ρ g(γ_ρ) ≥ 0 for suitable g; by Weil's criterion (1952, Bombieri) this is equivalent to RH. BST claims Steps 1–4 (temperedness; wall projection; volume dominance; explicit-formula bridge) and states honestly: **"one analytic lemma remains (Lemma 3 / Step 5)."**

**The remaining lemma is very probably the whole problem, not a mop-up.** Weil positivity is hard precisely in the ARCHIMEDEAN (local-at-∞) term, where the g-dependence lives and where the functional can go negative for cleverly chosen g; controlling it for ALL g is equivalent to RH. BST's "volume dominance, margin 10⁴⁷" bounds the *geometric/hyperbolic* side — the easy part — not the archimedean positivity. So "Steps 1–4 proved, one lemma left" is the classic shape where the leftover lemma is RH in disguise. (This is a structural inference; verifying it means reading Lemma 3's exact statement — worth doing, but the burden is on Lemma 3 to be something other than the hard core, and the volume-margin framing suggests it isn't.)

## 3. The universal obstacle (the thing every route must clear)

Force the zeros ON the line, beyond the functional-equation reflection symmetry. Unitarity/self-adjointness gives reflection (zero at ρ ⟺ pole at the reflection); it never gives on-the-line. The ONLY known way past reflection-to-location is a **positivity** that excludes off-line zero/pole pairs (Weil, de Branges, Li). So Route B (positivity) is the only family with a chance; Route A (self-adjointness/unitarity) structurally cannot reach the line and should be retired as a *proof* (it remains a correct realization).

## 4. Does BST have a real edge? (the only honest place to look)

The genuine question: does D_IV⁵'s SPECIFIC rank-2 / B₂ structure give a handle on the **archimedean positivity** (Lemma 3 core) that the general case lacks? That is the one spot a real BST contribution could live. Caveats:
- The current rank-2 usage (Route A's overdetermination) is the illusory version — it does NOT count as the edge.
- A real edge would be: the B₂ archimedean local factor has a positivity property the rank-1 / GL(2) case lacks. This is NOT established anywhere in the current files. If it reduces to the general archimedean positivity, BST sits exactly where Connes/Bombieri are stuck.

## 5. Honest order of operations (if pursuing RH from BST)
1. **Retire the "rank-2 overdetermination forces the line" claim** — it's the same ζ at three shifts (Cal #35); it is not a proof step.
2. **Demote Route A to "realization, not proof"** — ζ-as-Eisenstein-scattering is real and worth stating; self-adjointness does not close it.
3. **Put everything on Route B's archimedean positivity (Lemma 3).** Read Lemma 3's exact statement; determine whether it is the hard core (almost certainly) or genuinely separable.
4. **Find the B₂-specific archimedean positivity, or concede no edge.** The only honest contribution is a positivity the rank-2 local factor has and the general case lacks. If it exists, that's the result (and it's real even short of full RH). If not, BST is where everyone else is stuck — which is fine to say.

## 6. Bottom line (and the discipline)
**BST does not have a proof of RH.** It has a correct realization (credit), an illusory key step in Route A (rank-2 overdetermination = one ζ replicated), and an honestly-incomplete Route B whose remaining lemma is probably the entire difficulty. Any corpus status of "RH proved" is **not supported** and should read "realization established; proof open; distinctive step (rank-2 overdetermination) does not hold; positivity route incomplete at the hard core." RH is the single most-scrutinized problem in mathematics: the slightest overclaim here closes every door at once, so the internal status (gapped + incomplete) must be the public status, with maximal modesty. The realization is a genuine asset; the proof is not in hand; and the one place worth real effort is the B₂ archimedean positivity, where BST's edge is currently *claimed-illusory*, not demonstrated.

— Cal A. Brate, referee setup, 2026-06-15 Monday 12:33 EDT. No proof; a map. Pursue Route B's archimedean positivity or concede no edge; retire the rank-2-overdetermination claim (Cal #35); keep RH-status honest (open), because it is the one place loose framing is fatal.
