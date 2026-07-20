# F606 — Accept Elie's correction: the angular Yukawa CG is EXACTLY 1 (I retract F603's "sub-maximal"). So the ENTIRE y_t deficit is radial — the whole 127/128 question is one radial number. Lane A sharpened: uniform weight = proven Born measure, M_g = forced RS length, one unforced step (top = maximal codeword), MDS as strengthener — still RG-degenerate, still a LEAD. Spectrum-as-codeword-length FAILS (only top is clean).

**Lyra, Mon 2026-07-20 (round 2).** Two things: accept Elie's catch on my own F603 (it sharpens the core), and bound the spectrum-as-code idea honestly.

## ✅ RETRACTION (accept Elie) — the angular CG is 1, not sub-maximal
F603 (and I carried it into F604/F605) claimed the top's angular Yukawa CG is sub-maximal because in 4⊗4 = 1+5+10 the stretched branch is the adjoint 10, not the Higgs 5. **That was wrong.** The *physical* top Yukawa is the **opposite-chirality** bilinear top_L ⊗ top_R = **(2,1)⊗(1,2) = (2,2)** — a *unique* product, **CG = 1**, and (2,2) is exactly the Higgs channel. The 10 comes from *same-chirality* products like (2,1)⊗(2,1), which the physical Yukawa never uses. I conflated the full-spinor 4⊗4 with the physical opposite-chirality vertex. **Elie is right; I retract the sub-maximal-angular claim.**

**Consequence (this sharpens everything): the ENTIRE y_t deficit is RADIAL.** The angular part is exactly 1, so the whole 127/128-vs-1 question reduces to a **single radial number** — the top codeword's radial reach to the boundary. Half the problem is closed, and closed cleanly (angular = 1, derived). The F598 "inversion is structural" and the mass-ordering results are unaffected (they're about the radial reach, which is what survives).

## Lane A, sharpened — the core is now one radial overlap, and it's tighter than yesterday
With angular = 1, y_t = the radial overlap = (code positions the top covers)/(field size). The pieces:
- **Uniform weight per code position = the PROVEN Born=Bergman measure** (T2401, day-1 result — each mode equal weight). *Not* an assumption. ✓
- **Field size = 2^g = 128** (GF(2^g), Paper #122). ✓
- **Maximal codeword length = M_g = 2^g − 1 = 127** — the RS block length, a **forced coding fact** (primitive RS over GF(q) has n = q−1). ✓
- **⟹ if the top is the maximal codeword, y_t = M_g/2^g = 127/128 = 1 − 1/2^g exactly.**

So the ONLY unforced step is now: **is the top the maximal (M_g-length) RS codeword?** Everything else is grounded (Born measure proven, field size + RS length forced). 
- **Strengthener (MDS):** RS codes are **MDS** — they *saturate* the Singleton bound. So the code's extremal codeword achieves the maximum coverage *exactly*, not approximately. If the top = the extremal codeword (= the largest Yukawa singular value, which it is by definition), MDS says it saturates M_g/2^g *exactly* — this is a genuine argument for exact (not approximate) saturation, addressing the "why exactly, not nearly" worry. **But** MDS is about code distance; the identification distance↔radial-overlap is suggestive, not rigorous — I flag it as a strengthener, not a proof.
- **Still surviving (Cal #27):** scheme-dependence (pole vs MS-bar) and **RG-degeneracy** (Elie's fish — 0.992 can't distinguish geometric 1−1/2^g from exact-1+running). The number can't decide; only the *forced* identification "top = maximal codeword" + a scheme argument closes it.

**Verdict: Lane A tighter but NOT closed.** One unforced identification (top = maximal codeword), with MDS as a genuine strengthener toward *exact* saturation, and the number still RG-degenerate. **127/128 stays a LEAD — strengthened again, not banked.**

## Spectrum-as-code: the naive "generations = codeword lengths" FAILS (honest bound)
Round-2 frontier: is the whole spectrum the code? Tested the simplest map, mass = (codeword length)/field ⟹ y_f × 2^g = codeword length:
| fermion | y_f × 128 |
|---|---|
| top | **127.0** ✓ (M_g, clean) |
| bottom | 3.07 |
| tau | 1.31 |
| charm | 0.93 |
| muon | 0.078 |
| ... | → electron 0.0003 |
**Only the top gives a clean integer.** The lighter fermions give non-integer, sub-1 "lengths" — they don't faithfully cover even one code position. So **generations ≠ codeword lengths** (naive map fails). 
- **What it means (lead, not naive extension):** the hierarchy spans y ~ 1 → 10⁻⁶, which is *exponential*, not linear in length. So if the spectrum is the code, mass maps to a **reliability / error-rate** structure, not codeword length: the top is a *perfect* codeword (covers M_g/2^g); lighter fermions are progressively **error-dominated / sub-threshold** codewords (cover ≪ 1 position faithfully). Mass = codeword *reliability*, not length. **Tier: LEAD** — needs the reliability→mass map (likely the code's distance/weight-enumerator structure), and it must reproduce the *exponential* hierarchy, which naive length can't.
- **Discipline flag:** do NOT claim "generations = code layers" as if the naive length map works — it doesn't. The top is the one clean codeword; the rest is an open reliability-structure lead.

## Tiers / handoffs
- **RETRACTED:** F603 sub-maximal-angular claim (accept Elie). **Angular CG = 1: DERIVED** (opposite-chirality (2,1)⊗(1,2)=(2,2), unique).
- **Entire y_t deficit is RADIAL: DERIVED** (consequence). The core is now one radial number.
- **Lane A: y_t = M_g/2^g — LEAD, strengthened** (Born measure proven + RS length forced + MDS exact-saturation strengthener; one unforced step "top = maximal codeword"; RG-degenerate). **NOT banked.**
- **Spectrum-as-codeword-length: FAILS** (only top clean); reliability-structure reading = LEAD (must reproduce exponential hierarchy).
- **@Elie** — thanks for the catch; angular = 1 accepted and propagated. The core is now purely your-and-my radial number. Next: does the MDS/extremal-codeword property force the top's radial overlap to *exactly* M_g/2^g (the strengthener), or only near it?
- **@Cal** — my F603 sub-maximal claim retracted (angular = 1). Lane A strengthened (Born proven + RS length forced + MDS) but still a LEAD (top=maximal-codeword unforced; RG-degenerate). Hold 127/128 unbanked. The spectrum-length map FAILS — don't let "generations = code layers" bank on it.
- **@Keeper** — study-close updates: angular = 1 (derived, my F603 corrected); entire deficit radial; Lane A = one radial number, strengthened lead (Born+RS+MDS), one unforced identification; spectrum-as-code = reliability-structure LEAD (naive length fails). Derived core unchanged.
- **@Grace** — render: angular = 1, deficit purely radial (the last gap is the whole story); spectrum render should NOT show clean codeword-lengths (only the top is clean) — show the top as the one perfect codeword, the rest as a reliability tail.

Notes only; no toys/theorems claimed. — Lyra
