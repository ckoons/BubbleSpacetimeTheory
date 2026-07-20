# K774 — Working Target 4 + Lane B: the code frame TIGHTENS the ceiling (the top mass, not 174), but a quantization check shows "mass = coverage = n/q" is TOP-ONLY. The light fermions are off-lattice corrections — Target 1 (full spectrum as RS code) is not the naive version.

**Keeper | 2026-07-20 | Lead working the ceiling-as-capacity (Target 4) and the neutrino overflow (Lane B) while the team runs 07-20b. One pretty result, one disciplining check. `code_ceiling_quantization.py`.**

---

## Target 4a — the code frame gives a TIGHTER ceiling (conditional, LEAD)
Two levels of ceiling:
- **C-S (kinematic):** y ≤ 1 → m ≤ v/√2 = **174.1 GeV.** DERIVED (FA#7).
- **CODE (if y = coverage = n/q, and the maximal primitive RS block length is n = q−1):** y ≤ **(q−1)/q = 127/128** → m ≤ **172.7 GeV.** And 172.7 GeV **is the top mass.**

So under the code frame, FA#7 *tightens*: not "no fermion above 174" but **"no fermion above the top"** — because the top saturates the *maximal RS coverage* (q−1)/q, and nothing can cover more of a q-symbol field than q−1 positions. This is an information-theoretic sharpening of the falsifier. **Tier: conditional on the code frame = LEAD** (guards 1, 2 of 127/128 still stand; this doesn't clear them, it re-expresses the same lead as a tighter ceiling).

## Target 4b — the DISCIPLINE CHECK (this is the valuable part): coverage is TOP-ONLY
The code frame makes a *second*, testable prediction: if y = coverage = n/q, then **every y is an integer multiple of 1/q = 1/128.** Checked all 9 fermions (y·128):
- **top: 127.01 — an integer (127).** ✓
- bottom 3.07, tau 1.31, charm 0.93, muon 0.078, ... — **all non-integer, none on the lattice.**

**Verdict: only the top lands on the code lattice.** So **"mass = coverage = n/q" is a LEADING-order (top-only) statement.** The light fermions are **off-lattice corrections** — which is exactly consistent with the rank-1 picture (the top is the leading codeword; everyone else is a Tier-2 off-rank-1 correction), and it is *not* consistent with a naive "all fermions are RS codewords with y = n/q."

**Consequence for Target 1 (full spectrum as the RS Ladder):** do NOT pursue "y_f = n_f/q for every fermion" — it fails for everything but the top. The full spectrum being the RS *Ladder* must be a subtler structure (the corrections to the leading codeword — the code's error/redundancy structure, or a different code variable), not naive coverage. This is a guardrail for the team's Target 1, saving a dead route (the naive one) before it's chased.

## Lane B — the neutrino overflow as a zero-mode (structural, LEAD)
The overflow symbol (the one field position the top's codeword does NOT cover) has, by construction, **zero overlap with the coverage** — so a mode living there has **zero Yukawa → massless.** That is the neutrino-as-zero-mode. Whether it **coincides with the rank-2 zero eigenvalue** (F589's m₁ = 0 = the kernel of the measure-overlap operator) is the open identification: both are "the mode orthogonal to the condensate coverage," so they *plausibly* coincide (two routes to one massless ν), but the explicit identification (overflow position = rank-2 kernel) is the step to prove. **Tier: LEAD** — the structural argument is clean; the two-route convergence needs the explicit identification.

## Honest net
- **Sharpening (lead):** the code ceiling is the top mass — FA#7 tightens to "nothing above the top," conditional on the code frame.
- **Guardrail (the useful bit):** the naive "mass = coverage" is top-only; the light fermions are off-lattice, so Target 1's full-spectrum-as-code must be subtler than coverage. Saves a dead route.
- **Lane B:** overflow → zero-mode is clean; = rank-2 kernel is the open identification.
- **Unchanged:** 127/128 stays LEAD (guards 1, 2); angular = 1 stays derived; the code frame stays a FRAME.

— Keeper K774, 2026-07-20. Code ceiling y ≤ (q−1)/q = 127/128 → m ≤ 172.7 = the top mass (tightens FA#7 to "nothing above the top", conditional/LEAD). Quantization check: only the top is on the 1/q lattice (127); light fermions off-lattice → "mass = coverage = n/q" is TOP-ONLY, guardrail for Target 1 (full spectrum needs a subtler code structure, not naive coverage). Lane B: overflow → zero-mode (clean) = rank-2 kernel (open identification). See [[Keeper_K773_BST_is_a_holographic_RS_error_correcting_code_synthesis_2026-07-20]].
