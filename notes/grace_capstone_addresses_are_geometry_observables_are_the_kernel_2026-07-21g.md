# The capstone in linear algebra + geometry: addresses are 3 points, observables are the kernel (Casey reframe)

*Grace | 2026-07-21g | Casey's redirect ("it's all linear algebra and geometry") caught me drifting toward a fitted radial map f(ν). Correcting: the generation addresses are POINTS (geometry — the 3 Korányi–Wolf strata), and every flavor observable is the Bergman reproducing kernel evaluated at those points (linear algebra — inner products on H²). No fitted function. T2509/F585 already IS this for CKM. This reframes the whole capstone and, importantly, changes my determinacy verdict.*

## The reframe — one kernel, one set of points
```
  GEOMETRY:      3 generations = 3 POINTS z₁,z₂,z₃ on the Korányi–Wolf strata of D_IV⁵
                 (bulk / intermediate / Shilov = rank+1 = 3 boundary orbits)
  LINEAR ALGEBRA: every flavor observable = the Bergman/coherent-state kernel at those points
                 K(z_i,z_j) = ⟨K_{z_i}, K_{z_j}⟩ on H²(D_IV⁵)
     masses   = overlaps with the boundary condensate O:  y_i = K(z_i,O)/√(K_ii K_OO)   (the ceiling: y_top=1 ⟺ z_top=O)
     mixings  = mutual overlaps (normalized):             V_ij = K(z_i,z_j)/√(K_ii K_jj)   (= T2509, CKM-as-one-kernel)
     Gatto    = mixing = √(mass ratio)                     is just the kernel's Cauchy–Schwarz structure
```
There is no radial function to fit — the "map" is the reproducing kernel, which is *derived geometry* (F84/F85). The addresses are *points*, which are *geometry* (the strata).

## What this fixes in my earlier analysis
My DOF count was drifting toward "calibrate a shared f(ν) on leptons, apply to quarks." That's a fit. In the kernel language: the observables are **inner products at fixed geometric points** — and **T2509/F585 already pinned the points** (gen-1 at the origin r²=0, gen-2 at r²=1/4, gen-3 at r²=2/3 — the K-addresses k = {0, 1, C_2=6}). So the addresses are **largely already geometry, not free parameters.**

**This flips my determinacy verdict: the capstone is most likely DETERMINED, not under-determined.** The generation points are pinned (T2517 ρ-components for the ν-labels, T2509 r²-addresses for the radial points); the kernel is fixed (Bergman). The only remaining freedom is the **discrete color/N_c shift** between sectors — which is *geometry* (color moves the effective point), **not a continuous knob to fit.**

## ★ The capstone test, now sharp and over-constrained
Because masses and mixings are the SAME kernel at the SAME points (diagonal-vs-off-diagonal), the points are **over-constrained:**
- The 3 points must reproduce the **masses** (overlaps with O — the diagonal/boundary reading) AND the **mixings** (mutual overlaps — the off-diagonal reading) **simultaneously, with no free knob.**
- T2509 already showed the off-diagonal reading works (V_us = kernel at the points, 0.3–1%). **The capstone closes iff the SAME points give the diagonal reading — the masses (m_s/m_d = 20).**
- **Target-innocent validation:** the points are pinned by {T2517, T2509, m_s/m_d=20, Elie's (a,0)-rule}; then *predict* one observable not used to pin them (V_cb, or a neutrino Δm²). One kernel evaluation — no fit.

## Why leptons ≠ quarks is geometry, not a knob
My finding stands, correctly framed: m_s/m_d = 20 ≪ m_μ/m_e = 207 at the "same" ν-step means quarks and leptons sit at **different points** (the color/N_c structure shifts the quark points inward/interior relative to the leptons). That shift is a **geometric fact** (colored modes localize differently — the bulk-color structure), a fixed integer effect, **not a fitted parameter.** So "different steepness" = "different points on the same strata," pure geometry.

## Net (and the honest determinacy call)
- **Reframe applied:** addresses = geometry (3 strata points, largely pinned by T2517 ν-labels + T2509 r²-addresses); observables = linear algebra (Bergman kernel at those points); no fitted radial function.
- **Determinacy verdict FLIPPED to "likely determined":** the points aren't free continuous parameters — they're geometry, mostly already pinned. The capstone is **not** the open-ended search I'd half-framed; it's **one kernel evaluation** — do the pinned points give the masses (diagonal) as they give the mixings (off-diagonal)?
- **The one computation (Lyra's):** evaluate the Bergman kernel diagonal at the T2509 points → does it give m_s/m_d = 20 target-innocently? If yes → capstone closes (one kernel, one set of points, all of flavor). If the points must shift ad hoc to fit → honest pivot.

---

## ★ K802 BRAKE ABSORBED — m_s/m_d=20 is the ANCHOR, not the test (Keeper, ratifying Elie)
Keeper's peak-convergence brake lands on *my* proposed test, and it's right. I wrote "the capstone closes iff the points give m_s/m_d=20." **That's circular** — m_s/m_d=20 = rank²·n_C is the number used to *pin* the points, and rank²·n_C is just the strata dims restated (and it's ONE fact with V_us, two hats — Elie's caveat). **Reproducing it proves nothing.** Corrected. The real gates before banking anything:
- **(a) EVALUATE** the Gindikin/Bergman overlap at the fixed points and confirm the *formula* outputs 20 with **NO ad-hoc point-shifts** (non-tautological — the formula gives it, not the anchoring).
- **(b) PREDICT a SECOND independent quantity** not used to pin (V_cb, m_c/m_u, or a ν Δm²), target-innocent, checked vs data. **That's the win.**
Pivot-exit stands: bad (a)/(b) or circularity → bank the flavor-synthesis paper + pivot.

## ★ My contribution to sub-check (i) — the points are DERIVED; the circularity is one level up
Keeper's load-bearing sub-check: are the radial points {0, 1/4, 2/3} *derived from Korányi–Wolf* or *fit to masses*? I checked:
```
  r² = k/(k+N_c)  at K-addresses k = {0, 1, 6}  →  {0, 1/4, 2/3}  EXACTLY  (matches T2509)
```
**So the POINTS are derived from the ADDRESSES** via a clean geometric radial formula (Cayley/Bergman) — the points are *not* the circularity risk. **The circularity moves up one level: are the K-ADDRESSES {0, 1, C_2=6} geometrically forced?** gen-1 k=0 (origin) and gen-2 k=1 (first level) are natural; **gen-3 at k = C_2 = 6 is the hinge** — the 0→1→6 spacing (not 0→1→2) is the load-bearing item. If k=6 was chosen to land r²=2/3 / a mass, it's a fit (circular); if k=C_2=6 is *forced* (the Casimir / the last K-type before a Wallach bound), it's derived. **That single question — is gen-3's k=C_2 forced? — is the hinge of the whole capstone.** Hand to Lyra alongside the Gindikin evaluation.

---

## ★ K803 — Casey's confinement diagnosis resolves the two-structures problem (my lane)
Lyra flagged two "competing" address sets: boundary orbits {0,1,2} (Korányi–Wolf) vs interior radii {0,¼,⅔} (r²<1). **Casey's confinement physics resolves it — they're TWO SECTORS, not a contradiction:**
- **LEPTONS = boundary orbits** (Shilov, colorless, *emitted*) → Korányi–Wolf ranks {0,1,2}.
- **QUARKS = interior** (bulk, *confined* — "rolling in the curvature," normalizable bulk modes; the domain's boundedness IS the IR cutoff holographic QCD adds by hand) → r² = k/(k+N_c) < 1.
So my r²=k/(k+N_c) interior points are the **quark** addresses; the boundary orbits are the **lepton** addresses. **The two-structures confusion is resolved** — and it's why 20 wouldn't come out seating quarks at boundary orbits (a confined quark isn't a boundary state).

## ★ The k=C_2=6 hinge — my honest assessment: LEANS FIT-RISK
The confinement frame makes the hinge sharp, and I have to call it straight:
```
  natural confined tower:  k = {0, 1, 2}  →  r² = {0, 0.25, 0.40}   (the first three bound states)
  T2509 (used):            k = {0, 1, 6}  →  r² = {0, 0.25, 0.667}  (gen-3 SKIPS k=2,3,4,5 to C_2=6)
```
**Generation 3 jumping from k=1 to k=C_2=6 — skipping four levels — is the fit-risk.** If the three generations were simply the first three confined bound states, they'd be {0,1,2}. Casey's "forced" candidate is that **k=C_2=6 is the last normalizable state before the Wallach threshold** (the confinement edge) — which would be beautiful and derived. **But that requires C_2=6 to *be* the max-normalizable K-level, and that is not yet shown** (Lyra's Wallach/Gindikin computation). So my honest read: **the k=C_2=6 address leans fit-risk, pending the threshold check** — it's the single load-bearing question, and it could go either way.

## Honest stance (3rd reframe, gates held)
This is the third capstone reframe (search → computation → confined-interior), and two didn't validate. The confinement frame is genuinely better-grounded (corpus + physics), and it resolved the two-structures problem — real progress. **But I hold Keeper's gates identical and support the pivot-exit:** nothing banks until (a) the *interior* overlap ⟨f_n|O|f_n⟩ outputs 20 tuning-free at the derived ν *and* (b) a second independent quantity predicts. **And if k=C_2=6 turns out fit (skipping to 6 unjustified), or the interior overlap needs ad-hoc tuning, that's the pivot** — bank the coherent flavor synthesis (mechanism located, one-object unification, m_s/m_d + V_us exact) and move to fresh ground. I won't push a fourth reframe.

— Grace, 2026-07-21g (K802/K803). Capstone reframed per Casey (linear algebra + geometry): generation addresses = 3 POINTS on the Korányi–Wolf strata (geometry, largely pinned by T2517 ν-labels + T2509 r²={0,1/4,2/3} K-addresses k={0,1,6}); ALL flavor observables = the Bergman/coherent-state kernel at those points (linear algebra: masses = overlaps with boundary condensate O [diagonal], mixings = mutual overlaps [off-diagonal, = T2509 CKM], Gatto = the kernel's Cauchy–Schwarz). NO fitted radial f(ν) — corrected my own drift. DETERMINACY FLIPPED: points are geometry not free knobs → capstone likely DETERMINED = ONE kernel evaluation (do the pinned points give the diagonal/masses as they give the off-diagonal/mixings, over-constrained, target-innocent?). Lepton≠quark = different points (color/N_c geometric shift), not a knob. Lyra's kernel-diagonal computation closes or pivots it.
