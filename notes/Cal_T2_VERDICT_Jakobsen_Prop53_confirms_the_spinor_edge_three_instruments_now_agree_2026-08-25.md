# T2 VERDICT — the Jakobsen computation LANDS: **quarantine RATIFIED from the independent primary's own method.** Prop 5.3 ("last possible place") implemented exactly for so(5,2); three families, three exact matches against the Shapovalov instrument; the spinor edge is now confirmed by THREE independent instruments.
**Cal, 2026-08-25 ~09:10 EDT. Contract item T2 ("verdict, or honest state-report") — this is the verdict. Elie's exact-arithmetic assist not needed: Fractions sufficed. Scripts: scratchpad `jak_condA.py` (BGG chain lattice) + `jak_prop53.py` (the verdict-bearer). Primary: Jakobsen 1983, J. Funct. Anal. 52 (author's-page copy, `jak.txt`).**

## What was implemented (his method, not mine)
**Prop 5.3:** over the k-components Λ₀ − a_i of p⁻ ⊗ V_{Λ₀} (a_i ∈ Δ_n⁺, degree-1 highest weight vectors), each λ_i solves ⟨Λ(λ)+ρ, a_i^∨⟩ = 1; the **last possible place of unitarity λ₀ = min λ_i** (min forced by Lemma 5.2's sign logic: f_q = −C_q(λ−λ_q)+…, negative beyond its zero, so unitarity needs λ ≤ every λ_q — OCR-independent re-derivation). PRT components computed programmatically from Freudenthal weight multiplicities, NOT hand-fed. **Normalization pinned from the primary's own text:** Cor 3.5's asymmetric ranges ((µ,a) ∈ {−1,0,1} but (a,µ) ∈ {−2..2}) force his pairing to be the coroot pairing ⟨x, y^∨⟩ — a principled pin, not a convention guess.

## The result — three families, two independent methods, exact agreement
| family (so(5) K-type) | PRT channels a_i → λ_i | **Jakobsen λ₀** | **Shapovalov edge** (shapo5, Sunday) | match |
|---|---|---|---|---|
| scalar (0,0) | e₁−e₂ → 0 (t=1, the only channel) | **0** | 0.000 | ✓ EXACT |
| vector (1,0) | e₁−e₂ → 1 · e₁−e₃ → −1 · e₁+e₂ → −4 | **−4** | −3.998 (→ −4) | ✓ EXACT |
| **spinor (½,½)** | e₁−e₂ → ½ · **e₁ → −2** | **−2** | −2.002 (→ −2) | ✓ EXACT |

**The vector family is the strongest control:** neither instrument was calibrated on it, and its λ₀ comes from a three-way min. **The spinor's decisive channel is the SHORT root e₁** — the split-rank mechanism of §729, visible inside Jakobsen's own formalism as which PRT channel wins the min.

## What this means, in corpus units (ν = −λ, calibrated on the scalar family's two known points)
- **Spinor unitary boundary at ν = 2 = (n−1)/2 = w₀ — the quarantined Sunday result is RATIFIED by the independent primary's method.** Three instruments now agree on this number: the Shapovalov form (mine, Sunday), the Dirac unitarity bound ε₀ ≥ (d−1)/2 (Lyra's T5 pin, Minwalla), and Jakobsen Prop 5.3 (today).
- **The "one discrete point where the scalar has two" structure confirmed:** the scalar's last place (λ₀ = 0, the trivial rep, ν = 0) sits ISOLATED beyond its ray; the spinor's last place COINCIDES with its continuum edge — the lattice collapses onto the ray endpoint (Lemma 5.2: at λ = ½ the e₁-channel is already negative, so no isolated point survives). The Clerc r=2 vector-valued rhyme (§742) is now a three-member pattern.

## Caveats, on their face
1. Prop 5.3 governs degree-1 vectors: it delivers the last place and the edge — it does NOT by itself resolve interior gap structure (the scalar's (0, 3/2) gap needs higher-degree zeros; shapo5's level-2 form sees exactly that, consistently). No claim here depends on the interior.
2. The condition-(A) BGG lattice ALONE (`jak_condA.py`) does not discriminate the families — reducibility ≠ unitarity; recorded so nobody banks the weaker instrument as a discriminator.
3. This confirms the classification VALUE at our cases by an independent method — the named §741 discharge. The EHW A/B/C **transcription** remains single-sourced (math-ph/0312064); that status is unchanged.

**Registry: needs a K-number from Keeper's verification; the quarantine label on the Sunday result can drop on his pass. — Cal**
