---
title: "F423 — PRIMARY 1 (the why-α, F66 bulk-boundary propagator): the why-α splits CLEANLY into a derivable COUNT and an open MAGNITUDE, and the existing corpus 'proof' (BST_ElectronMass_Derivation Section 7.2) is an IDENTIFICATION with Wyler's formula, not a derivation from the propagator. (A) The honest read of Section 7.2: line 351 sets the per-level transition amplitude |⟨π_{k+1}|T̂|π_k⟩|² = (N_c²/8π⁴)(Vol D_IV^{n_C}/Vol B^{2n_C})^{1/2} = α² — but that RHS is LITERALLY Wyler's α-formula (N_c²=9, the same volume ratio that defines α, line 404). So the per-layer α² is ASSERTED ≡ Wyler-Robertson, NOT computed from the bulk-boundary propagator. This is the corpus's own 'motivated not proved' line 411. (B) What the propagator DOES derive — the COUNT: the bulk-boundary (Hardy→Bergman) transition operator on the Shilov boundary S⁴×S¹ that steps Bergman level k→k+1 is multiplication by e^{iθ} (one S¹/EM quantum); the S¹ integral (1/2π)∫e^{−i(k+1)θ}e^{imθ}e^{ikθ}dθ = δ_{m,1} ENFORCES exactly one EM quantum per level-step (machine-verified: m=1→1, all other m→0). ⟹ the NUMBER of α-factors = the number of Bergman levels from the boundary electron (k=1) to the first bulk state above the Wallach gap (k=C₂+1=7) = C₂=6 steps, ×2 for the holo×antiholo Bergman norm = 2C₂=12. The COUNT (=exponent structure) is a clean S¹-charge-ladder selection rule. (C) What it does NOT derive — the MAGNITUDE: that each S¹ quantum's amplitude = α (not 4πα, not α/N_c) reduces to the S⁴ adjacent-level Bergman ground-state overlap = Wyler volume ratio. THIS is the genuine open Berezin-Toeplitz normalization — well-defined, NOT fakeable in one step, and it is EXACTLY Grace's statement that 'the kernel N(z,w)^{−p} carries no α': the kernel power carries the COUNT, the α-MAGNITUDE lives in the S⁴ overlap normalization, not the kernel power. (D) Count consequence: m_e=R STAYS (C). This does NOT move the count to 10 — it SHARPENS the gap to a single named integral (the S⁴ adjacent-level overlap = Wyler ratio) and hands Elie's Sakharov side the precise target. Honest forward progress, NO faked count move. Five-Absence: passes (no forbidden structure). Count 9/26."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-29 Monday (date-verified)"
status: "v0.1 — PRIMARY 1 why-α count-vs-magnitude split. Section 7.2 per-layer α² is IDENTIFICATION with Wyler (RHS = Wyler's own formula), not derivation. Propagator DERIVES the COUNT (S¹ charge-ladder selection rule: e^{iθ} steps k→k+1, S¹ integral = δ_{m,1}, exactly one EM quantum per Bergman level → C₂ steps boundary→bulk ×2 holo/antiholo = 2C₂=12). Propagator does NOT derive the MAGNITUDE (each quantum=α reduces to S⁴ adjacent-level overlap = Wyler volume ratio = the open Berezin-Toeplitz normalization = Grace's 'kernel carries no α'). m_e=R STAYS (C); gap sharpened to one named integral for Elie. No faked count move. Count 9/26."
---

# F423 — The why-α splits into COUNT (derived) and MAGNITUDE (open); the corpus "proof" is an identification, not a derivation

**PRIMARY 1, Keeper K609 / the 3-CI exp-12 collaboration.** Worked the F66 bulk-boundary (Hardy→Bergman) propagator against Elie's concrete BLIND target ("does the propagator give α per coset-direction, *derived* not *assigned*?"). The honest answer separates into three parts.

## (A) The existing corpus "proof" is an identification with Wyler, not a derivation

`BST_ElectronMass_Derivation.md` Section 7.2 (line 351) sets the inter-level transition amplitude

  |⟨π_{k+1}|T̂|π_k⟩|² = (N_c²/8π⁴)·(Vol D_IV^{n_C}/Vol B^{2n_C})^{1/2} = α².

But that right-hand side **is Wyler's α-formula** (N_c²=9 = the "9" in α=(9/8π⁴)(π⁵/1920)^{1/4}, line 404; same volume ratio). So Section 7.2 **asserts** the per-layer amplitude ≡ Wyler's α via the "Wyler-Robertson correspondence" — it does **not compute** the amplitude from the bulk-boundary propagator and find α. This is precisely the corpus's own honest flag (line 411: "Each Bergman layer contributes α² — **Motivated**, needs rigorous Berezin-Toeplitz analysis"). The (C) tier on m_e=R is correct and this is why.

## (B) What the propagator DOES derive — the COUNT (the exponent structure)

The bulk-boundary propagator's S¹ structure gives the **number** of α-factors cleanly. On the Shilov boundary Š = S⁴×S¹, the level-k Bergman ground state carries S¹ (= SO(2) = EM/U(1)) charge e^{ikθ}. The operator stepping k→k+1 is multiplication by e^{imθ}; the S¹ matrix element is

  (1/2π)∫₀^{2π} e^{−i(k+1)θ}·e^{imθ}·e^{ikθ} dθ = δ_{m,1}   (machine-verified: m=1→1, m∈{0,2,−1}→0).

So **each Bergman level-step requires exactly one S¹/EM quantum** — a selection rule, not a choice. The electron sits at the boundary k=1; the first bulk state above the Wallach gap is k = C₂+1 = 7; the ladder is

  k=1 →(1 EM quantum)→ 2 → 3 → 4 → 5 → 6 → 7,   **C₂ = 6 steps**.

The Bergman *norm* is |f|² (holomorphic × anti-holomorphic), doubling the count to **2C₂ = 12**. So the **exponent 12 is the S¹-charge-ladder count** — derived from the propagator, target-innocent, and it disambiguates the F416 "5 forms" pile in favour of 2C₂ (the ladder mechanism *selects* this reading over R(S⁴) etc.).

## (C) What it does NOT derive — the MAGNITUDE (each quantum = α)

That each S¹ quantum's amplitude equals **α specifically** (not 4πα, not α/N_c, not e) is the surviving open piece. After the S¹ integral fixes the selection rule, the amplitude reduces to the **S⁴ adjacent-level Bergman ground-state overlap**:

  ⟨π_{k+1}|T̂|π_k⟩ = ∫_{S⁴} Ȳ_{k+1}(s) Y_k(s) dμ_{S⁴}   (the S¹ part is already 1).

The claim is that this overlap = the Wyler volume ratio (Vol D_IV⁵ / Vol B¹⁰)-type quantity → α. This is a **single, well-defined integral** — the Berezin-Toeplitz normalization of the S⁴ part — and it is genuinely **not derivable in one step**. Crucially, this is **exactly Grace's statement** that "the kernel N(z,w)^{−p} carries no α": the kernel *power* carries the COUNT (part B); the α-**magnitude** lives in the S⁴ overlap normalization, which the kernel power does not contain. The geometry literally cannot fake the magnitude — confirming Grace's delimitation from the propagator side.

## (D) Count consequence — honest, no faked move

**m_e=R stays (C).** This finding does **not** move the count 9→10. What it does:
- **Confirms** the (C) tier is correct (the per-layer α is an identification with Wyler, not a derivation).
- **Derives** the COUNT half (the exponent 2C₂=12 is the S¹-ladder selection rule — this part *is* now mechanism-backed, partially answering F416's disambiguation).
- **Sharpens** the open MAGNITUDE half to a single named integral: the **S⁴ adjacent-level Bergman overlap = Wyler volume ratio**. This is the precise, well-posed target for Elie's Sakharov/heat-kernel side and Grace's geometry side.

The count moves only if (C) closes — i.e. if the S⁴ overlap is *computed* to equal the Wyler ratio (making m_e/m_P a from-scratch prediction independent of any measured input, since α itself is the Wyler output). That computation is the genuine multi-step rigor; I will not compress it into a claim to move a number (Keeper K609 / F417 (C)-trap). Five-Absence: passes. **Count 9/26.**

*Discipline: this is the count-vs-magnitude factorization of the why-α — the kind of "engage, don't label" Casey asked for. It replaces "why-α is multi-week" with "the COUNT is the S¹ selection rule (done); the MAGNITUDE is one named overlap integral (open)." The boundary is now a sharp integral, not a fog.*
