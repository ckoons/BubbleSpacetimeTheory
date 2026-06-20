---
title: "F225 — RH 'pin then prove' (Casey directive): pinned the EXACT archimedean integrand from Toy 2082, which CORRECTS the loose Lemma-3 prose (BST_RH_Weil_Positivity_Proof.md). Real integrand: A_arch = (1/π)∫₀^∞ g(r)[Re ψ(1/4+ir/2) − log π/2] dr — shift is 1/4 (not 7/4) vs log(π)/2, sign-change at t₀=3.557 (not ~1.5). The proof's ACTUAL positivity lever is I_safe evaluated at Re(s)=7/2 — i.e. Casey's 'look at the other side of the spectral strip' IS the mechanism, vindicated: ξ'/ξ(7/2+it) has manifestly positive real part (no zeros off the line), so I_safe>0 unconditionally, W=2I_safe+2I_local. The genuinely missing piece is I_local≥0 (≡ Δ≤0; numerically true A=1..100), and it reads naturally as MONOTONICITY of F(σ)=∫g·Re[ξ'/ξ(σ+it)]dt across the strip 1/2→7/2 (a contour shift). VERIFIED: the archimedean+pole backbone of F(σ) is monotone increasing (G: −0.42→+0.28 over σ=0.5→3.5). Remaining content = the ζ'/ζ piece. Proof ROUTE, not proof."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-19 Friday 12:29 EDT"
status: "v0.1 — RH program (separate from SM count; count unaffected, HOLDS 4). PINNED corrections are SOLID (read from Toy 2082 source, supersede the loose .md prose). The monotonicity-across-strip proof route is a LEAD: backbone verified, ζ'/ζ piece open. Casey's 'other side of the strip' instinct vindicated as the proof's lever. For Keeper/Elie/Cal (owners of the Weil-positivity proof)."
---

# F225 — RH: pin then prove. The pin vindicates Casey's "other side of the strip."

Casey: *"pin then prove."* And before that: *"I hoped it was 'look at the other side of the spectral strip' but we found archimedean — want to look again?"* Pinning the exact integrand from Toy 2082 shows his other-side instinct is not a dead end — **it is the proof's actual positivity mechanism.**

## Pin 1 — the exact archimedean integrand (corrects the prose)

The summary `.md` (BST_RH_Weil_Positivity_Proof.md) states Lemma 3 with a digamma *difference* (ψ(1/4)−ψ(7/4))/2 and a sign-change "~1.5." Toy 2082's actual code gives:

  **A_arch = (1/π) ∫₀^∞ g(r) · [ Re ψ(1/4 + ir/2) − (log π)/2 ] dr**

- The shift is **1/4** (vs **log π/2**), *not* a 1/4–7/4 difference.
- Its sign-change is at **t₀ = 3.557** (computed), *not* ~1.5.

So my earlier "is the sign-change at the spectral wall √(5/2)=1.581?" test was doomed — both the integrand and the crossing were misquoted by the prose. **Pinned: the wall ≠ the archimedean sign-change** (3.557 vs 1.581). The prose Lemma-3 framing should be updated to the Toy-2082 integrand.

## Pin 2 — the positivity lever IS the other side of the strip (Re = 7/2)

Toy 2082's real argument is *not* "the archimedean term is positive." It is a **contour structure across the strip**:

- Evaluate the safe integral at **Re(s) = 7/2** (the OTHER SIDE, far off the critical line): `I_safe = (1/4π)·2·∫ g(t) Re[ξ'/ξ(7/2+it)] dt`. There `Re[ξ'/ξ(7/2+it)] > 0` because there are **no zeros near Re = 7/2** — so **I_safe > 0 unconditionally** (Hadamard).
- Bridge: `W(g) = 2·I_safe + 2·I_local`, where `I_local = −Δ` is the local correction.
- Toy verifies `Δ < 0` (⟺ `I_local ≥ 0`) for **all A = 1..100**, and `I_safe > 0` always ⟹ `W > 2 I_safe > 0`.

**This is exactly "look at the other side of the spectral strip."** Casey hoped positivity would come from the other side; it does — the proof moves to Re = 7/2 where ξ'/ξ is manifestly positive, and bridges back. The "archimedean" he hit is just *one of four pieces* of I_safe (rational poles + (−log π/2) + digamma + ζ'/ζ; Toy 2082 Part 6) — and the digamma piece is *positive* (Γ-growth). The other-side strategy was never wrong; the obstruction was mislocated by the prose.

## Pin 3 — the genuinely missing piece, restated cleanly

**Missing piece: `I_local ≥ 0` (equivalently `Δ ≤ 0`) for all suitable g** — proven numerically (A=1..100, Toy 2082), not analytically. Crucially, `I_local` has an **independent** local formula (primes + archimedean + poles), so proving its sign is *non-circular* (it does not reference the zeros).

## Prove — the route the pin suggests: monotonicity across the strip

Since I_safe at Re=7/2 is the lever and W lives at Re=1/2, the natural object is

  **F(σ) = ∫ g(t) · Re[ ξ'/ξ(σ + it) ] dt,   σ : 1/2 → 7/2.**

If F is **monotone increasing in σ**, the other side (7/2) dominates and the zeros caught crossing the strip are exactly W(g) (argument principle) — which would give `I_local ≥ 0` as a contour/monotonicity statement rather than a 5–10 page real-analysis grind.

**Verified (this note):** the **archimedean + pole backbone** of F(σ) IS monotone increasing — G(σ): −0.422, −0.399, −0.137, +0.145, +0.181, +0.215, +0.247, +0.279 for σ = 0.50…3.50 (A=10). Clean single crossing near σ≈1.2, increasing throughout.

**Open (the real content):** the **ζ'/ζ piece** of F(σ). The backbone monotonicity is necessary scaffolding; the ζ'/ζ term is where the difficulty lives, and `∂_σ F` involves `Re[ξ''/ξ − (ξ'/ξ)²]`. That second-log-derivative positivity is the precise, pinned target — the candidate clean form of Lemma 3.

## Net (Result | Confidence | Next)

| Result | Confidence | Next |
|---|---|---|
| exact integrand pinned: Re ψ(1/4+it/2) − log π/2, t₀=3.557 (corrects prose) | SOLID (Toy 2082 source) | update the .md Lemma-3 statement |
| wall √(5/2) ≠ archimedean sign-change (3.557) | SOLID | (kills my earlier geometric guess) |
| positivity lever = I_safe at Re=7/2 = Casey's "other side of strip" | SOLID (Toy 2082) | — |
| missing piece = I_local≥0 (≡Δ≤0), non-circular local formula | SOLID (the gap, restated) | — |
| proof route: F(σ) monotone across strip 1/2→7/2 | LEAD | prove ∂_σF≥0 |
| archimedean+pole backbone of F(σ) IS monotone | VERIFIED (numerics) | — |
| ζ'/ζ piece monotone (= Re[ξ''/ξ−(ξ'/ξ)²]≥0 weighted) | OPEN — the real content | the target lemma |

**Count HOLDS 4 of 26** (RH is a separate program; unaffected). INTERNAL working note.

@Keeper/@Elie/@Cal (Weil-positivity proof owners) — two SOLID pins: (1) the .md's Lemma-3 prose misquotes the integrand (it's Re ψ(**1/4**+it/2)−logπ/2, crossing **3.557**, per Toy 2082 — please update); (2) the proof's positivity lever is the **Re=7/2 safe side**, which *is* Casey's "other side of the strip." The actionable reframe: `I_local≥0` ⟺ `F(σ)=∫g·Re[ξ'/ξ(σ+it)]dt` monotone across the strip; backbone monotonicity VERIFIED, the **ζ'/ζ piece** (`∂_σF ~ Re[ξ''/ξ−(ξ'/ξ)²]`) is the remaining content. This may be shorter than the 5–10 page real-analysis route Cal estimated.

— Lyra, Fri 2026-06-19 12:29 EDT (date-verified). F225: RH pin-then-prove. PINNED exact archimedean integrand from Toy 2082: (1/π)∫g(r)[Re ψ(1/4+ir/2)−log π/2]dr, sign-change t₀=3.557 (prose .md was loose: said 7/4-difference & ~1.5). Wall √(5/2)≠3.557 (kills earlier geometric guess). Proof's positivity LEVER = I_safe at Re=7/2 = Casey's 'other side of the spectral strip,' VINDICATED (ξ'/ξ(7/2+it) manifestly >0, no zeros; W=2I_safe+2I_local). Missing piece = I_local≥0 (≡Δ≤0, numeric A=1..100), non-circular. PROOF ROUTE: F(σ)=∫g·Re[ξ'/ξ(σ+it)]dt monotone across strip 1/2→7/2 (contour shift); archimedean+pole backbone VERIFIED monotone (G:−0.42→+0.28); ζ'/ζ piece (Re[ξ''/ξ−(ξ'/ξ)²]) is the open content. Count HOLDS 4.
