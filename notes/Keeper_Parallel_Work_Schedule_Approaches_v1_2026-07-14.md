# Parallel Work Schedule — best approach + alternatives for every non-derived item (deep-dive informed)

**Keeper | 2026-07-14 | Five parallel corpus deep dives (α/Keystone-A, CKM, PMNS, neutrino, light quarks). For every non-derived parameter: the recommended approach, ranked alternatives, and what's been tried. Structural finding: the ~13 non-derived items collapse onto THREE shared engines + a few independents. Schedule these in parallel AFTER α reaches derived/nearly-proven.**

## The structural finding — 13 items, 3 shared engines
Most non-derived items are not independent problems; they are readouts of three unbuilt computations:
- **ENGINE A — the gauge-coupling normalization integral** → α + Higgs λ + V_us mechanism.
- **ENGINE B — the explicit complex generation-state build** → CKM (V_ub, δ, J) + PMNS (θ23, θ12, δ) + neutrino coefficients {7/12,10/3}. **Enormous leverage — one build, ~7 parameters.**
- **ENGINE C — boundary-integral evaluation capability** → the tau √π build + m_d/m_u absolute anchor + α's 0.036 curvature term. **A foundational capability BST has never actually exercised (rep-theory shortcuts always canceled the Szegő normalization; here it doesn't).**
- **Independents:** Majorana closure (γ⁵ intertwiner + Cal co-sign); m_b 6% (RG-running); a few cleanups.

---

## ENGINE A — α + Higgs λ + V_us (do FIRST, per Casey)
**BEST APPROACH: the explicit KK gauge-kinetic integral over the S¹ fiber.** Reduce ∫F²√-g over the S¹-bundle / 137-channel structure of D_IV⁵ and show the dynamical coefficient of F² is *exactly* (1/4)·137 with NO stray factor (no 2π, no internal-Vol, no ½). Needs the explicit fiber metric. **This is the genuine falsifier and the ONE computation that proves "unity" rather than assuming it — NOT started.** Land it → α DERIVED, Higgs λ=1/8 and V_us ride along; miss it → all three leads fall (real falsifier).
- **Critical clarification (deep dive):** do NOT expect the gravity-KK / heat-kernel machinery (F63/F64/F101) to deliver this — that machinery computes the *running* gauge coupling (a₂ heat-kernel coefficient, universal 11/3, 2/3 factors), a DIFFERENT object than the 1/count normalization. The template for a *derived* normalization is c_FK=225/π^{9/2} (T2442, the one normalization actually proven in-corpus, Born-invariance-forced).
- **Two sub-steps (K679):** (a) show the kinetic term sees exactly count 137 = 27·n_C+rank (not "the S¹ capacity" asserted by hand in BST_Maxwell.md:91-95); (b) prefactor = unity.
- **ALTERNATIVES (ranked):** (1) charge-count route (T2470 proved: EM charge = SO(2) integer weight → norm-independent → 1/137) — FAVORED, but reaches unity *definitionally* (ratio of dimensions), which is why α stays IDENTIFIED not DERIVED; (2) ρ-shift realization (route 3, K679) — compute the FK/Bergman-vs-Szegő K-type weights, check = {35,21.9,5,1}, converges with charge-count on 1/137, UNCOMPUTED; (3) Q⁵↔Shilov bridge (SO(7) Schur democracy on the compact dual — Keeper hypothesis, open); (4) heat-kernel a₂ — WRONG OBJECT (running).
- **TRIED/FAILED:** Wyler ¼ (retired numerology); Shannon-capacity paper (K676 RELOCATE — don't resurrect); "27×27=I" milestone (ran, ≠ I); plain-measure norm-weighting (refuted); saturation bound (no bound forces 137, K677).
- **"Nearly proven" status:** the COUNT (137) is there (F525 one-matrix + T1939 + T2470); the UNITY PREFACTOR is the S¹-fiber integral, not started. **Reachable to "nearly proven" = do that integral.**

## ENGINE B — the complex generation-state build (CKM + PMNS + ν-coefficients)
**BEST APPROACH: construct the 3 generation states as explicit SO(5,2) rep VECTORS (not assigned radii), read peak positions AND phases, form the F84/K264 Bergman overlap matrix per sector (down/up/lepton/ν), diagonalize once.** Eigenvalues → masses; eigenvectors → U_u,U_d,U_ν → CKM + PMNS + Jarlskog J. **This single build decides ~7 parameters + all the mixing + whether CP survives.** GENUINELY CAN-FAIL: real peaks → J=0 identically (F498 PROVED); CP needs complex peaks, which the natural radial model does NOT give.
- **State (deep dive):** the generations are currently ASSIGNED as REAL radii {0, 0.5, 0.82} on the ν-ladder {5/2,3/2,0} — so as built, BST predicts J=0 (no CP). The complex build (F493 ℤ₃ phases z_k=r_k ω^{k-1}) is PROPOSED but the phases are motivated-not-forced and it's NOT executed. gen-1 at r=0 IS forced 3 ways (target-innocent).
- **Readouts once built:** V_ub (the apex = 0.414 residual of the U_u†U_d cancellation); δ_CKM + J; PMNS θ23 octant (does |U_μ3|² land ≷ ½); θ12 form (does |U_e2|²=3/10 forward → settles 3/10 vs 42/137); δ_PMNS (the phases); AND feed the ν-coefficient diagonalization.
- **ALTERNATIVES for CP (ranked by target-innocence):** (1) non-collinearity/triangle-area (F491) — most innocent, magnitude-silent; (2) SO(2) time-circle localization (K585) — strong "why CP needs time," near-maximal sinδ≈0.90, but exact δ un-bankable (two forms fish); (3) ℤ₃ cube-roots (F493) — hinges on unproven "generations carry ℤ₃ triality." (4) **DO NOT trust the old arctan√5 / J=A²λ⁶η̄ paper** (BST_CKM_CPPhase_Derivation.md) — reverse-fit, CONTRADICTS the current frontier's proved J=0-for-real-peaks. **Cleanup: mark that paper deprecated.**
- **NEAR-TERM SUB-WIN (independent of the full build):** close the Fritzsch cross-kernel for V_us — derive M₁₂=√(m_d·m_s) forward (0.4%). Blocker: reconcile F381 (down at d(ν) strata → d(5/2)=0 massless) vs F506 (down at FK ν=N_c → nonzero) first.
- **TRIED/FAILED:** Wolfenstein-power reading (rejected); naive degree→radius {1,3,5} (over-mixes 3.4×, toy 4635); single-sector overlap≈I (wrong object); 2/√79 Cabibbo (Cal #318 demoted); bunched prescription B (ruled out by electron-at-origin).

## ENGINE C — boundary-integral evaluation capability (tau √π + m_d/m_u anchor + α 0.036)
**BEST APPROACH: build the capability to evaluate a Szegő/Bergman boundary integral to an actual number** (the F323 integrand N(w)^{n_C/2} against the invariant measure; ‖z^n‖²=π·B(n+1,α+1), α=n_C). BST has NEVER done this — every closed result used rep-theory shortcuts where the normalization canceled; at n=0,1 (light-quark anchors) and for the tau cone-tip it does NOT cancel. **Foundational, bounded, in-corpus — a build, not a wall.** One capability unlocks: (i) m_d absolute anchor + m_u value (same integral at n=0,1); (ii) the tau √π cone-tip forward; (iii) α's 0.036 curvature term (T2133 heat-kernel).
- **ALTERNATIVES:** none — this is a capability, not a choice. It's the prerequisite for the absolute-scale layer.

## INDEPENDENT — Majorana closure (near-term experimental win)
**BEST APPROACH: two deliverables.** (1) **The explicit ν=1/2→9/2 γ⁵ intertwiner** — an operator I: V_{ν=1/2}→V_{ν=9/2} that IS the γ⁵ chirality map (NOT σ_BF spin-statistics — the flagged landmine), showing the RH shadow partner has negative formal degree ⇒ non-unitary ⇒ no ν_R. Bounded rep-theory computation on top of T2471 (global γ⁵, structurally-verified) + Paper-118 (Bergman-Dirac tower). (2) **Cal's cold-read co-sign** (governance — flipping a banked falsifier's sign). → flips pred_004 to a 1–4 meV 0νββ floor.
- Independent of the mass coefficients (orthogonal problems).

## INDEPENDENT — neutrino coefficients {7/12, 10/3}
**BEST APPROACH: a Bergman-kernel Majorana mass-matrix diagonalization on d(ν)-weighted ν-strata** (the machinery that closed muon/tau at 0.003%/0.0000%). Check if the eigenvalue ratio = 40/7 with m₁=0. **Gated behind forcing the ν localizations** (same F490 bar as CKM — so this rides ENGINE B). **CHEAP NEGATIVE CHECK FIRST:** test whether d(ν)-ratios yield 7/12, 10/3, or 40/7 at all (d(1/2)=+105/8 already computed); if none fall out, the ν masses do NOT live on the charged-lepton machinery — a strong result either way.
- **Honest state:** {7/12,10/3} are FITTED (team says so). 7/12 has THREE incompatible "derivations" (numerology flag). **CLEANUP: adjudicate the fork** — T1972 (Δm² ratio = c₂·N_c = 33) vs T1260 ((40/7)²=32.65); two banked/theorem-level claims for one observable. Cheap source-pin, do first.

## INDEPENDENT — light-quark cleanups
- **m_b 6% miss (840 vs ~890):** ratio 840 IS forced (single-row Q⁵ topology); the 6% is a scale/RG problem (geometric scale vs m_b scale). RG-run the down ratio. Tractable.
- **gen-1 up cold anomaly (c/u=588≠137):** genuinely STUCK — no forced mechanism; over-determined 3 ways (1/√g, 19·31, N_c(rank·g)² — numerology). Principled route = Grace's position-dependent τ-gradient / two-anchor thermal ordering (why gen-1 is cold), tied to matter stability — SCAFFOLDED, UNRUN, and the simple single-τ law already fails. Hold-open-don't-fit.
- **PREMISE FLAG (load-bearing):** the whole down sector rests on "bare ribbon = current (not constituent) mass" — Casey-endorsed, NOT Cal-ratified. If it fails, F506 reverts to a structural miss. **Cleanup: Cal ratify the current-mass reframe.**

---

## RECOMMENDED PARALLEL SCHEDULE (after α reaches derived/nearly-proven via Engine A)
| Lane | Engine | Owner(s) | Unlocks |
|---|---|---|---|
| 1 | **A — gauge-normalization integral** (FIRST) | Grace | α + λ + V_us |
| 2 | **B — complex generation-state build** | Grace + Lyra + Elie | V_ub, δ_CKM, J, θ23, θ12, δ_PMNS, {7/12,10/3} |
| 3 | **C — boundary-integral capability** | Lyra + Elie | tau √π, m_d/m_u anchor, α 0.036 |
| 4 | **Majorana closure** (γ⁵ intertwiner + co-sign) | Elie + Cal | pred_004 |
| 5 | **Cleanups** (parallel, cheap) | Keeper + Grace | deprecate arctan√5 CP paper; adjudicate 33-vs-32.65; Cal-ratify current-mass premise; compute |U_e2|² forward for θ12; RG-run m_b |

**Discipline armed:** θ12 over-claimed (BANKED papers over DERIVED-vs-SELECTED — compute |U_e2|² forward); ν-coeffs FITTED (don't dress); CP CAN FAIL (J=0 for real peaks, proved); the old arctan√5 paper contradicts the frontier; Engine A is a falsifier not just a closer. Cal #27 hardest on Engines A & B.

— Keeper, 2026-07-14. Deep-dive approach menu. 13 non-derived items → 3 engines (A gauge-norm → α/λ/V_us; B generation-build → all mixing + ν-coeffs; C boundary-integral → absolute scale) + Majorana + cleanups. α first (Engine A = the S¹-fiber ∫F² integral), then schedule 2–5 in parallel.
