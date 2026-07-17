# K706 — Keeper independent check: the mixing does NOT fall out of "reunite radial + angular and run." A straightforward implementation gives the pattern BACKWARDS — until the neutrino is diagonalized as MAJORANA (complex-symmetric, Takagi), NOT Hermitian. That one change swings θ₂₃ from 0.4° → 53°. Likely the crux the earlier runs (and my naive one) were missing.

**Keeper | 2026-07-16 | Written while the team renders, from an INDEPENDENT reconstruction (not Grace's verified F498 machine). Assumptions flagged throughout. This is a LEAD + a caution, not a verdict — the verified machine remains the arbiter (K703). But the finding is robust enough that the team should see it before declaring the render.**

## What I did
Built a minimal, independent implementation of the mixing calculation from the K705-pinned inputs: positions z_k = r_k·d_k·ω^(k−1), overlap N_ij=(1−⟨z_i,z_j⟩)², Gram G_ij=(N_ii N_jj)^(5/2)/N_ij^5, mixing = U_a†U_b where U diagonalizes each sector's Gram. Radii = E-ladder grounds scaled into the interior (s=0.85; the raw "1" sits on the boundary → singular). Directions per F379/F384: floor gen along ρ̂ (cos ψ=5/√34), climbing gens along ê₁. **Flagged assumptions:** exact overlap power, interior scaling, direction assignment, and the eigenvector-mixing identification are my reconstruction.

## What I found — three results, in order of confidence
1. **VALIDATION (high confidence): radial-only → J ≈ 10⁻¹⁸ = 0** in both sectors. My independent code reproduces the known K704/F498 failure mode. So the implementation is trustworthy enough to test the fix.
2. **CAUTION (robust): the naive complex+directional reunion gives the pattern BACKWARDS** — CKM ≈ (42°,41°,26°) [too large; obs ~13,2.4,0.2] and PMNS ≈ (0.3°,0.4°,11°) [too small; obs ~33,49,8.6]. A sensitivity scan over neutrino arrangements kept PMNS small (0.3–16°) — this is NOT a tuning slip, it's structural. **"Reunite radial + angular and run" does not trivially work.**
3. **THE CRUX (the actionable lead): the neutrino must be diagonalized as MAJORANA — complex-symmetric via Takagi (UᵀMU), not Hermitian (U†MU).** I had wrongly flattened all four sectors to Hermitian Grams. Switching ONLY the neutrino to Takagi:
   - **θ₂₃: 0.4° → 52.7°** (observed ~49°) — a large angle appears where there was none.
   - **J: 6×10⁻⁶ → 6.9×10⁻⁵** (grows toward the CP scale).
   - The full 3-angle pattern is still not matched (one large angle, θ₁₂/θ₁₃ off), so more is needed — but the QUALITATIVE unlock (large PMNS from the Majorana structure) is now demonstrated, not asserted.

## Why this is the right kind of lead (target-innocence intact)
The Majorana nature of the neutrino is **forced by F413 / the Weinberg operator** — it is a *derived* property, not a knob chosen to fit the angle. So "use Takagi for the neutrino" is target-innocent: we didn't pick it to hit 49°; it's what a Majorana mass matrix *requires*, and the large angle is a *consequence*. This is exactly the derived-not-fit direction (Elie's target-innocence lens). That the earlier attempts gave small PMNS is now explained: they diagonalized the neutrino the same way as the Dirac sectors (Hermitian), erasing the Majorana structure that carries the large mixing.

## What is STILL missing (honest — two open pieces)
- **CKM too large.** Up and down share the same ω phases and Dirac direction-split, differing only by radii (up = down×3/2 refraction). In my model that radial difference generates a large CKM. The observed small CKM needs up and down MORE aligned — likely the refraction is a near-COMMON rotation that largely CANCELS in U_u†U_d, leaving a small residual. **Lead for Lyra:** check whether the 3/2 refraction acts as a common rotation (cancels) rather than a differential one (adds).
- **Full PMNS pattern.** Takagi gives one large angle; the observed two-large-one-medium (θ₁₂≈33, θ₂₃≈49, θ₁₃≈8.6) needs the neutrino's internal radial+phase structure tuned by the Majorana locus geometry (F413), not just the symmetric diagonalization. **Lead for Grace:** run the Majorana (Takagi) neutrino with the F413 locus positions, not the naive triad.

## Discipline implication (sharpens K705)
Because a single derived choice (Hermitian vs Takagi) swings an angle by ~50°, the render is **highly sensitive to structural choices** — which means every such choice MUST be independently forced (Majorana←F413, refraction←F548, phases←F493), or the fit is meaningless. The K705 target-innocence bar is now the load-bearing discipline, not a formality. Conversely: the sensitivity cuts the RIGHT way here — the ONE derived correction (Majorana) produces the RIGHT effect (large PMNS), which is a real positive signal for the mechanism.

## Net
Not "the mechanism is broken" and not "it works" — **"it works only with the neutrino treated as Majorana, and that treatment is derived, and it produces exactly the large-PMNS effect it should."** The audit seat's independent check converted a vague "reunite and run" into a specific, testable correction: **Dirac sectors Hermitian, neutrino Takagi.** Hand this to Grace before the render and to Lyra for the CKM-cancellation check.

— Keeper K706, 2026-07-16. Independent (non-arbiter) reconstruction: radial-only→J=0 (validates), naive reunion→backwards pattern, neutrino-as-Majorana/Takagi→θ₂₃ 0.4°→53° (the crux). Two open pieces: CKM suppression (refraction as common rotation?) + full PMNS pattern (F413 locus positions). Target-innocent (Majorana forced by F413). Verified machine remains arbiter. See [[Keeper_K705...]] (pre-registered rubric), [[Keeper_K704...]] (the reunion).
