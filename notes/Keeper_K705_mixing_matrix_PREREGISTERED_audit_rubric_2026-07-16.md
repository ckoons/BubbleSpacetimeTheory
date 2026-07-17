# K705 — PRE-REGISTERED audit rubric for the mixing render (bands pinned BEFORE the numbers). Verdict is mechanical when Grace's run lands. This exists to stop me rationalizing whatever the machine produces.

**Keeper | 2026-07-16 | Written while the team runs the render, BEFORE any output. Pins (a) the target-innocent inputs that must be fixed in advance, (b) the observed values + honest tier-2 tolerance bands per parameter, (c) the qualitative structure bars that a radial-only run FAILS, (d) the miss protocol. Criteria-innocence-of-conclusion (Lyra methodology). If any input below is adjusted after seeing data, the render is a FIT, not a derivation, and does not bank.**

## A. Target-innocent inputs — FIXED NOW (adjusting any of these post-hoc = FIT, auto-FAIL to bank)
These must be the values the run is fed, derived from the cited corpus, NOT tuned to the observed angles:
- **Radial moduli r_k** = the E-ladder grounds (the masses, already banked): charged-lepton map {1, 2/3, 1/2}; neutrino {1, 3/5, 3/7}; down {1, 3/4, 3/5}; up = down × refraction (N_c/rank = 3/2).
- **Directions** ê₁ / ρ̂ from **F379/F384**; cos ψ = ê₁·ρ̂ = 5/√34.
- **Phases** z_k carries ω^(k−1), ω = e^(2πi/3) (**F493/F547**). ℤ₃ from N_c=3 — NOT a free phase.
- **Neutrino locus** = Majorana/chargeless axis (**F413**), off the charged-lepton axis. This is the ONLY source of large PMNS; it is fixed by the Majorana mechanism, not chosen.
- **Refraction index** = N_c/rank = 3/2 (**F548**) for up/down.
- **Overlap integrand** = exact rank-2 FK, genus = n_C = 5 (**F547**): |⟨w_i|w_j⟩| = [N_ii N_jj]^(5/2) / |N_ij|^5.
**None of the above may move after the first render.** If a parameter misses, the response is the miss protocol (Section D), NOT retuning an input.

## B. Observed values (PDG/NuFIT 2024) — pinned so they can't drift
**CKM:**
- θ_12 (Cabibbo) = 13.04° ; sinθ_C = 0.2245 ; |V_us| = 0.2243
- θ_23 = 2.38° ; |V_cb| = 0.0405 (range 0.040–0.042)
- θ_13 = 0.20° ; |V_ub| = 0.00369
- δ_CKM ≈ 66–69° ; **J_CKM = 3.08×10⁻⁵**
**PMNS (normal ordering):**
- θ_12 = 33.4° ; sin²θ_12 = 0.307
- θ_23 ≈ 49° (octant ambiguity: 42°–49°) ; sin²θ_23 ≈ 0.45–0.57
- θ_13 = 8.6° ; sin²θ_13 = 0.022
- δ_CP ≈ 197° (poorly constrained, ~0.8–1.5π)

## C. Tolerance bands — HONEST tier-2 (this is a structural theory, 10⁻²–10⁻⁴ floor, NOT 10⁻¹⁴)
Per-parameter PASS = target-innocent input AND lands within band:
- **Angles:** within **±15% or ±3°** (whichever is larger) of observed. Tighter than that = strong; outside = the parameter misses.
- **Jarlskog:** correct SIGN and within a **factor of ~3** of observed magnitude (J is a product of sines, so a factor-few on a structural theory is the honest bar).
- **δ phases:** SIGN + rough magnitude only (the phases are the least constrained observationally; do NOT over-weight a δ hit or miss).

## D. The QUALITATIVE STRUCTURE BARS — the real discriminator (a radial-only run FAILS ALL of these)
The numbers are the second test; the STRUCTURE is the first and strongest, because the F498 failure mode gives ≈0 on all of it. Passing these qualitatively is the signal that the angular reunion worked at all:
1. **CKM is small** — all three CKM angles < 15°, hierarchy θ_12 > θ_23 > θ_13.
2. **PMNS is large** — at least two angles > 30° (θ_12, θ_23), and θ_13 **small-but-clearly-nonzero** (~8–9°, NOT zero, NOT large).
3. **J ≠ 0 in BOTH sectors** — nonzero CP, from the ℤ₃ phases (complex positions). A real result here (J=0) means the phases didn't enter → back to the radial-only failure mode.
4. **The CKM/PMNS asymmetry is sourced correctly** — small CKM from up/down at *similar* loci; large PMNS from the neutrino on its *distinct Majorana axis*. If the render gets large PMNS by tuning rather than by the Majorana locus, that is a FIT (Cal watches this).
**If bars 1–3 pass qualitatively, the reunion is confirmed even before the numbers sharpen.** That is the headline to watch for.

## E. Miss protocol — pressure-test order (NEVER retune an input first)
If a parameter misses its band with target-innocent inputs:
1. **Down E₀=3 (d=g=7) ground FIRST** — the "+2 for color" step is K703's flagged weak anchor. A CKM miss (up/down sector) points here.
2. **The neutrino Majorana locus geometry** — a PMNS miss (θ_23 octant, or θ_13 too large/small) points to how the Majorana axis is placed (F413), not to the phases.
3. **Only after 1–2 are cleared** is the machine or the integrand suspect — and Grace's F498 is VERIFIED, so that's last.
A miss that cleanly fingers the down ground is a **CONDITIONAL PASS of the framework** (the mechanism is right, one ground needs work), not a failure. "A failure named precisely is a win."

## F. Whole-matrix verdict thresholds (pre-set)
- **PASS:** qualitative bars D1–D3 all hold + ≥5 of 6 parameters within band, target-innocent inputs. → bank the mixing sector; M=UΣV† renders; the 26 close.
- **CONDITIONAL PASS:** D1–D3 hold + 3–4 of 6 within band, the misses cleanly finger the down ground or the Majorana locus placement (not the phases, not the machine). → framework confirmed, named gap.
- **FAIL:** any of D1–D3 fails qualitatively (esp. J=0 → phases didn't enter, or PMNS≈0 → back to radial-only). → the angular reunion did not actually happen; diagnose which input didn't reach the integrand before any claim.

## G. What I will NOT accept as a pass
- A large PMNS obtained by tuning a phase or direction to the data (must come from the Majorana locus F413 + ℤ₃ ω, fixed in A).
- J≠0 obtained by adding a free phase not equal to ω = e^(2πi/3).
- Any "close enough" on an angle achieved by adjusting r_k (the masses are BANKED — they cannot move to help the mixing).
- A δ_CP "hit" used to inflate confidence (δ is barely measured; it is not a load-bearing test).

— Keeper K705, 2026-07-16. Pre-registered BEFORE the render. Inputs fixed (Section A), bands pinned (C), the qualitative small-CKM/large-PMNS/J≠0 structure (D) is the real discriminator that radial-only FAILS, miss protocol pressure-tests the down ground first (E), whole-matrix thresholds pre-set (F). Verdict will be mechanical when Grace's numbers land. See [[Keeper_K704...]] (the reunion), [[Keeper_K703...]] (grounds, down = weak anchor).
