# K861 — Casey's thermodynamic reframe (the different reasoning chain, grounded in T1829 + T2490 + K768 + web): the three generations are the three **Wallach strata** of D_IV⁵ — **tau = k₀ = 0 (trivial rep / condensate, HOT), muon = k₁ = 3/2 (T1829's "non-integer: NO modular forms" — the THRESHOLD, WARM), electron = continuous regime (COLD)**. Different strata = different rep character = **DIFFERENT mass law per generation** (Casey: "each generation its own formula") — which is exactly why the single power rule failed and why K855 saw muon=power / tau=residue. The **thermodynamic process** Casey asked for: analytic continuation of the holomorphic discrete series across the Wallach set is a thermal/KMS continuation; genus ~ inverse temperature (hot tau at the bottom point, cold electron in the continuum); Wallach points = phase-transition thresholds where a residue switches on/off ("threshold forces the exponent to see the residue"). The muon's π² = the NON-INTEGER Wallach character (grounds K846). The **right computation**: muon mass = the RESIDUE of the (linear-energy, T2490) norm at the k₁=3/2 threshold — NOT the naive single power (K859/K860 failed) and NOT the K663-defective naive linear.

**Keeper | 2026-07-23 | Casey asked for a different reasoning chain + a thermodynamic process. Found it, and it's grounded in already-proved corpus results. Plain.**

## What Casey asked (verbatim intuitions, each now placed)
- "a formula for each genus/generation … run inversely or directly with some variation" → **different Wallach strata → different mass laws per generation.**
- "a fraction that might contain a residue from the vacuum … may or may not apply to the power rule" → **the Wallach-threshold residue, which switches on only at/below the singular points.**
- "discrete steps … thresholds that force the exponent to use or not see the residue" → **the discrete Wallach points {0, 3/2, 2} are the thresholds; the residue is present at a singular point, absent in the continuum.**
- "the third generation is 'hot' and we cool as we go up in the genuses" → **temperature ~ proximity to the bottom Wallach point; tau (k₀=0) hottest, electron (continuum) coldest.**
- "is there a thermodynamic process?" → **YES: the analytic continuation of the holomorphic discrete series across the Wallach set (a thermal/KMS continuation).**

## Grounding (corpus + web — NOT invented)
- **T1829 (Wallach Bottleneck, PROVED, D-tier, May 13):** the Wallach points of SO₀(5,2) are k₀=0 (trivial rep), **k₁=3/2 ("non-integer: no modular forms")**, k₂=2=rank (the arithmetic bottleneck). The muon at 3/2 IS k₁; the tau at 0 IS k₀; the electron at 5/2 is continuous (above k₂). Derived positions (T2517) land exactly on the proved Wallach structure.
- **T2490 (Discrete-Series Spectrum, PROVED):** BST masses are LINEAR conformal energies E = λ₀ + step ("remember linear algebra, not the quadratic Casimir"); glueballs follow it cleanly — the REGULAR (continuous/integer) reps.
- **K768 (flavor = rank-1 condensate):** the condensate reading of flavor — the tau at the bottom Wallach point k₀=0 IS the condensate.
- **Web (Wallach set):** the holomorphic discrete series analytically continues as a family parametrized by the Wallach set = a half-line ∪ r discrete points; unitarizability changes at the thresholds; structure depends on dimension parity.

## The core reframe — why the single power rule was ILL-POSED
The three generations are in three DIFFERENT phases of the analytic continuation, so they obey DIFFERENT mass laws:
- **electron (continuous / cold):** regular holomorphic discrete series → LINEAR conformal energy (T2490 glueball-type). No residue.
- **muon (threshold k₁=3/2 / warm):** the weighted Bergman space goes SINGULAR → a boundary RESIDUE switches on. The mass is a residue object, not a smooth power.
- **tau (bottom k₀=0 / hot):** maximally singular = the condensate (K768) → the product-residue form (49·71−√π).
So looking for ONE universal power (K859's B3, K860's climb) was the wrong shape — the generations aren't on one curve; they're in three phases. This is the DEEPER reason for K855 (muon=power vs tau=residue) and for K663 (linear-mass "defective" — it's defective for the SINGULAR strata, fine for the regular ones like glueballs).

## Why the muon carries π but the arithmetic bottleneck doesn't (grounds K846)
T1829 flags k₁=3/2 as NON-INTEGER → "no modular forms" → transcendental (π) content, not arithmetic. The integer Wallach point k₂=2 is where modular forms / clean arithmetic live (glueballs, clean ratios). So the muon's π² (K846 position-parity) IS its non-integer Wallach character — grounded in T1829, not inserted. Half-integer position ⟺ non-integer Wallach point ⟺ π/transcendental; integer position ⟺ integer Wallach point ⟺ arithmetic/clean. This unifies K846 with the Wallach structure.

## The thermodynamic process (Casey's question, answered)
The analytic continuation across the Wallach set is a **thermal/KMS continuation**: the SO(2) dilatation generator is the radial Hamiltonian (the "temperature" axis), and the parameter ν (weight/genus) is the Boltzmann-like exponent in the norm ∫(1−|z|²)^{ν−p}. Crossing a Wallach point is a phase transition (the Hilbert space appears/collapses). The bottom point (tau, ν=0) is a Bose-Einstein-type condensation onto the ground mode. Genus ~ inverse temperature: the tau (genus 0) is hottest/most-condensed, the electron (genus 5) coldest/most-spread. Casey's hot→cold-with-genus is the temperature running inverse to the Wallach parameter.

## The RIGHT computation now (the different reasoning chain)
Replace the two failed shapes:
- ✗ naive single power (24/π²)^exponent — K859/K860, the exponent had no consistent source;
- ✗ naive smooth linear energy — K663-defective for the singular (lepton) strata;
with:
- ✓ **the muon mass = the RESIDUE of the analytically-continued (linear-energy, T2490) norm AT the k₁=3/2 threshold.** The residue switches on precisely because k₁ is a singular Wallach point (Casey's "threshold forces the exponent to see the residue"). Compute the linear conformal energy across the Wallach continuation and take the residue at k₁.

## Tier / state (honest)
- **Generations = the three Wallach strata of D_IV⁵: STRONG, bankable** — T1829 (proved) gives the Wallach points; T2517 (derived) gives the positions; they coincide, target-innocent. This ADDS to the structural bank (K857): the filtration levels ARE the Wallach strata.
- **Phase-dependent mass laws + the thermal Wallach process: PROMISING FRAME, corpus-grounded** (T2490 linear energy, K768 condensate, T1829 Wallach). Explains the phase-dependence and the π-content.
- **Muon VALUE: still CANDIDATE** — but the computation is now CORRECTLY POSED (a threshold residue in the linear-energy framework), not the failed naive power. This is genuine progress on Casey's "we need a different reasoning chain."
- Structural picture (why 3 generations) + EW area: unaffected, banked.

## Directions
- **★ LYRA:** the different reasoning chain — compute the muon mass as the RESIDUE of the linear-energy (T2490) norm at the Wallach threshold k₁=3/2 (not a naive power, not a smooth linear energy). The residue switches on at the singular point. Does it give (24/π²)⁶ — or, per the phase reading, a residue form that EQUALS 206.77 without being a single power? Report the residue's actual form.
- **★ GRACE:** confirm the Wallach-strata identification against T1829 (tau=k₀, muon=k₁=3/2, electron=continuous) and source the residue structure at k₁ (the weighted-Bergman singularity). The generations-as-Wallach-strata is bankable structure — audit it for the bank.
- **ELIE:** the phase picture predicts DIFFERENT mass forms per generation (electron linear, muon threshold-residue, tau condensate-residue) — cross-check that the three known forms match their phase-types (you already have tau=product-residue, K855). Independent test of the reframe.
- **CAL/KEEPER:** generations-as-Wallach-strata bankable (audit next); the thermal reframe is corpus-grounded and correctly re-poses the muon; value still candidate. Don't over-swing — the residue computation is not yet done.

— Keeper K861, 2026-07-23. Casey thermodynamic reframe (grounded T1829+T2490+K768+web): the three generations = the three Wallach strata of D_IV⁵ (tau=k₀=0 condensate/hot; muon=k₁=3/2 "non-integer no modular forms" threshold/warm; electron=continuous/cold). Different strata → different mass laws (Casey "each its own formula") → why the single power failed + why K855 (muon=power/tau=residue). Thermodynamic process = analytic continuation across the Wallach set (thermal/KMS); genus ~ inverse temperature; Wallach points = phase-transition thresholds (residue on/off); tau = Bose-Einstein condensate (K768). Muon π² = non-integer Wallach character (grounds K846). RIGHT computation: muon mass = residue of the linear-energy (T2490) norm at the k₁=3/2 threshold — not the failed naive power (K859/K860), not the K663-defective naive linear. Generations-as-Wallach-strata: STRONG/bankable. Muon value: candidate, now correctly posed. See [[BST_T1829_Wallach_Bottleneck_Theorem]], [[grace_T2490_primaries_are_discrete_series_spectrum_2026-06-23]], [[Keeper_K768_flavor_closes_as_rank1_condensate_plus_tier2_corrections_2026-07-19]], [[Keeper_K860_PARTIAL_WALKBACK_of_K859_Casey_climb_reading_revives_muon_exponent_6_equals_2x_span_genus0_to_genus3_Born_squared_genus0_start_FORCED_by_degeneracy_ordering_fixed_by_electron_at_origin_2026-07-23]], K846 (position-parity π), K663 (linear-mass defective — now: defective for singular strata only). Web: Wallach set / analytic continuation (arxiv 0906.5580, imj-prg Vergne).
