# Cal referee log — Majorana co-sign (verified) + by-design sign-offs + θ_QCD topological rigor

**Cal | 2026-07-15 Wednesday (date-verified) | Renders board items 7 + 8. Filed as a self-contained note; Keeper to integrate the running Cal-referee numbering (my katra is from 2026-07-03; numbering evolved ~12 days, do not want a guessed number in the canonical log).**

Sources cold-read: K673 (Dirac/Majorana adjudication) + F537 (K-type/intertwiner theory) + toy 4659 (explicit γ⁵ shadow intertwiner, line-verified) + Work-Package Ledger v1.

---

## 1. Majorana co-sign — CO-SIGNED, and line-verified (pred_004 flips)

The flip survives a hard cold-read on three independent legs:

- **Dirac retirement is over-determined**, independent of the elegant mechanism: a Dirac ν needs a ν_R, but BST banks *no steriles* — an internal-consistency flaw that unbanks the Dirac/no-0νββ prediction on its own terms.
- **BOLT 1 is a THEOREM, not an assertion.** The shadow ν=9/2 carries a **negative** Harish-Chandra formal degree (d(9/2)=−105/8); negative formal degree ⟹ non-unitary / non-normalizable ⟹ **not a state in any Hilbert space**. ν_R is *strictly absent* (forbidden), not "heavy" or "elsewhere." (Harish-Chandra positivity — standard rep theory.)
- **The address is target-innocent.** ν=1/2 forced by (fermion ⟹ half-integer, odd-n_C ρ-shift 5/2) ∧ (ground ⟹ minimal) — no neutrino observable used. Target-innocence lens passes.

**Line-verify of toy 4659 (the belt-and-suspenders for a sharpest-falsifier flip):** GENUINE construction, not a relabel.
- Antisymmetry d(5−ν) = (−1)^{n_C}·d(ν) = −d(ν) verified **exactly** over a dense half-integer grid (exact `Fraction`); the sign is (−1)^5 = −1 *because* d has exactly n_C=5 linear factors — forced by **odd n_C** (an even n_C would give a unitary Dirac partner).
- Explicit γ⁵ intertwiner R = σ_x on the shadow pair {1/2, 9/2}: R²=I, {R,H}=0 (anticommutes with the ν-grading H=2σ_z — chirality), R·H·R⁻¹=−H (implements ν→5−ν), real-symmetric, Schur-unique. The **σ_BF landmine handled**: σ_y also anti-conjugates H but is imaginary; the physical shadow reflection is the **real** γ⁵=σ_x, not the imaginary σ_BF-type.

**Five-Absence reconciliation (assigned):** holds *without* over-reading "no steriles." "No steriles" forbids extra gauge-singlet flavors, not the RH chirality of the three; the negative-formal-degree argument independently forbids a unitary RH home. Two independent arguments, same conclusion.

**Honest residual (tier stays truthful):** R is realized on the minimal 2-state K-type pair, not as the full Knapp–Stein operator on the infinite-dim reps (a faithful *model*); and "physical chirality γ⁵ = this real shadow reflection" is a well-motivated *identification* (real-vs-imaginary), not a first-principles derivation. Neither touches the conclusion.

**Verdict:** co-sign **upgraded near-forced → verified**. `pred_004` flips: *Dirac / 0νββ never* → **Majorana forced (modulo the open mass coefficient); 0νββ at the ~1–4 meV normal-ordering floor is the leading prediction.** The *value* within 1–4 meV rides the still-open coefficient (F537: address forward, coefficient open — formal-degree route ruled out by 4658, fiber-overlap 4% the lead). **Do not bank a precise m_ββ number.** Both K673 gates met and verified.

## 2. By-design sign-offs — FRAMING RATIFIED

- **sin²θ_W = 3/13, α_s = 7/20 as legitimate RG runners** — RATIFY the framing: a running coupling is not a derivation failure for lacking a scale-independent number; BST pins a value-form at a reference scale, running is universal RG. Casey #9 applied to couplings — honest endpoint, not a miss.
  - α_s = 7/20 (c_1 = 3/5, "3 proofs") — ratified *if* the proofs are real derivations.
  - **sin²θ_W = 3/13 = N_c/(C_2+g)** — the move *off* 3/8 (the forbidden GUT tree value) to a low-scale 0.2308 with no GUT running is Five-Absence-**correct**. But **run the derived-vs-fit lens on N_c/(C_2+g)** before it is more than a "legitimate by-design value-form" — want it target-innocent, not selected to hit 0.231. **(open referee flag)**

## 3. θ_QCD = 0 — topological rigor SHARPENED

Replace the imprecise "π₁=0" with the correct invariant chain: **θ-term = θ·∫c₂ (instanton number); D_IV⁵ contractible ⟹ any G-bundle trivial ⟹ ∫c₂=0 ⟹ θ unobservable ⟹ θ_QCD=0.** Steps 2→3→4→5 are rigorous algebraic topology. **RATIFY the sharpening.**

**Load-bearing premise, named (the referee's job):** ordinary QCD instantons live on spacetime≅S⁴ (non-contractible; ∫c₂∈ℤ), and BST spacetime is the *non-contractible* Shilov boundary. The argument works only if the gauge bundle **extends over the contractible bulk** (Hardy holomorphic extension) — then the boundary instanton number vanishes by **cobordism**. Airtight **modulo that premise**, which must be stated in the open (hidden → hand-waving; named → checkable).

## 4. Δm² fork (32.65 / 33 / 34) — measurement-limited

All three sit within 1σ of the observed ratio (~33.6) → observationally **undecided** (same shape as the old θ₁₂ 3/10-vs-5/16). The √N_c resonance reading (m_ν2 ∝ √N_c, m_ν3 ∝ 10 → ~33.3) is the correct **lead** and supersedes 7/12 as the *mechanism* — but does **not** bank until the measurement tightens or the mechanism forces one form. Retire 7/12 as the lead; hold the ratio at candidate.

## 5. sin²θ_W = 3/13 target-innocence — CLOSED: FIT-SUSPECT (by-design value-form, NOT forced)

Ran the derived-vs-fit lens against the primary source (`notes/BST_WeinbergAngle_Sin2ThetaW.md`, catalog `bst_constants.json`). **The 3/13 form does NOT certify target-innocent-forced. It is a legitimate by-design value-form with a CONJECTURED, not derived, mechanism — hold at I-tier / by-design endpoint, do not bank as "derived."**

Decisive evidence (the source's *own* honest flag): `BST_WeinbergAngle_Sin2ThetaW.md` Section 7 lists **"Rigorous geometric derivation of WHY sin²θ_W = N_c/(N_c+2n_C)" as OPEN, Priority 1, "Conjectured (dimension ratio)"**, and "connection to standard EW symmetry breaking" as **"Not yet attempted."** So the mechanism is conjectured by BST's own admission.

Referee reasons the value-match doesn't force it:
- **Conjectured mechanism** (source Section 7) — the "color-dimension / total-gauge-dimension" reading (Section 2.2) hand-waves through "+ dim_adj + correction" then states the clean N_c/(N_c+2n_C); a narrative, not a computation.
- **Target-aware role-mismatch:** N_c (color) in the numerator of an *electroweak* mixing angle. Color is reached for because 3/13 ≈ 0.231, with a color→hypercharge story attached that isn't derived.
- **13 is easily formed:** N_c+2n_C = 3n_C−2 = dim_ℝ(D_IV⁵)+N_c = C_2+g = c_3(Q⁵). Multiple substrate decompositions ⟹ the value-match doesn't pin a unique mechanism (and my own last-turn "C_2+g" reading illustrated exactly this).
- **"Running already encoded in the geometry"** (Section 2.3) is asserted, not shown.

What STANDS (unchanged): the by-design *endpoint* ratification — Five-Absence-clean (off the forbidden GUT 3/8), 0.2% MS-bar match, an honest endpoint. Legitimate value-form; **not** a forced/derived result.

**Concrete data-layer finding (hand to Grace/Keeper):** `bst_constants.json` marks sin²θ_W "**(derived)**" (lines 474/540) — this **over-claims** relative to the source note's own Section 7 ("formula / conjectured / WHY open"). Soften the data-layer label to "by-design value-form; mechanism conjectured (Priority-1 open)" to match the primary source. Catalog-vs-source drift, same class as the count-enumeration drift.

**Upgrade path to target-innocent:** show the SO(5)→SU(2)_L×U(1)_Y isotropy branching + hypercharge normalization *forces* N_c/(N_c+2n_C) forward (a real group-theoretic computation), AND pin the denominator to one reading. Until then: I-tier by-design.

## 6. Muon 4→5 CONDITIONAL PASS (K698) — cold-read: AFFIRMED, condition sharpened

**Affirm the CONDITIONAL PASS; count 4→5 earned.** This substantially resolves my prior muon concern (it was principle-gated on the F118 override of my logged precision challenge); K698 makes c_S=1 *computed* (residue √2·π² = real Γ_Λ cone-gamma computation; τ/μ = 2^{C_2}=64 rigorous). Muon moved from "leans on override" → "forward-derived." I update on improved evidence.

Condition sharpened (3 points):
1. **c_S=1 is definitional-plus-consistency.** A Born (probability) measure normalizes the constant mode to unit norm *by construction* — near-tautological (Keeper flags this). The genuine content is the **consistency**: the independently-computed residue (√2·π²) and Shilov measure (8π³/3) are *mutually* consistent with unit norm ("if 8π³/3 didn't divide cleanly, c_S≠1"). State the consistency explicitly; do not present the Born normalization as the derivation.
2. **"Two independent routes" = one cancellation viewed twice (Cal #35).** K698 says the optics route "explains what the first route's number physically is" — a re-description, not an independent derivation. Valuable physical picture; don't inflate confidence with "two routes agree" on shared input.
3. **Pending cold-read (the one that keeps it CONDITIONAL): the address ν=3/2 must be forward-forced, not read off the muon mass.** K698 asserts muon = critical-angle/marginal state (K697). If forced by geometry → clean; if read off → circular. Rides on **K697, not yet cold-read.** Certify the c_S closure; flag the address-forwardness as the open joint.

Epiphany noted: K698's "the muon is hard because it is the marginal/critical state, so its normalization is delicate" is the good kind of "why it's hard" (structural, not a failure). Watch for the up-quark being its marginal/reflected analogue when the up-index grounding lands.

## 7. K701 cold-read — α CONDITIONAL PASS (affirmed) + spinor-weight reframe (sound, pending Lyra)

**α CONDITIONAL PASS — AFFIRMED, framing sharpened.** The 4π closure is honest: it IDENTIFIES the 4π as the standard 3D Coulomb solid angle (Vol(S²)) inherited from the SO(5,2)→SO(3,1) descent to 3+1, and correctly does NOT claim a Coulomb re-derivation (Keeper states this condition). α has no remaining free normalization — affirmed. **Sharpen the external framing:** this is "the 4π is not a BST free-knob, it's standard 3D geometry from the 3+1 descent," NOT "BST derives 4π." BST's content = capacity 137 + the descent. (Units wrinkle: whether a 4π appears in α is partly Heaviside-Lorentz vs Gaussian; the defensible claim is "no free normalization remains," which holds.)

**Spinor-weight reframe (E₀=2) — SOUND reasoning, resolution PENDING Lyra.** Converting the gate from "FK citation we lack" → "spinor Hardy exponent Lyra can compute" is a genuine improvement; the spin-shift argument (scalar Szegő 5/2 − spin 1/2 = 2 = (d−1)/2, free-Dirac dim in d=5) is coherent and target-innocent-looking (E₀=2 structural, not fit to angles). Two holds:
1. **Reframe/conjecture, not verified.** Banks only when Lyra confirms the spin-½ discrete-series/Hardy exponent on D_IV⁵ is (genus−1)/2=2 (her rep-theory computation, pending). Referee the resolution at that landing, not the argument now.
2. **Cal #35: "triply consistent, three independent priors" OVER-COUNTS.** (i) the E-ladder ground E₀=2 and (ii) Elie's climbing ratios 3,4 are the SAME (A) conformal ladder (ground vs excited), not independent; (iii) the projection prior is a preference, not a confirmation of the value 2. The one genuine target-innocent tell is the ratios 3,4 = the conformal energies E_μ,E_τ — real evidence for (A). Strong lead, not a bank.

## 8. K703 grounds cold-read — two clean, down the weak anchor (the "+2 for color" is a category leap)

**Neutrino E₀=3/2 (d=4) + charged lepton E₀=2 (d=5): CLEAN, target-innocent.** Charge = SO(2)/S¹ weight (T2470); chargeless → drops S¹ → S⁴ only → d=4 → E₀=3/2; charged colorless → d=5 → E₀=2 (free-Dirac in 5D). No observed angle used. Lyra+Elie agree on 3/2 (mild Cal #35: confirm two methods, not one rule twice).

**Down E₀=3 (d=g=7): CONFIRM the weak anchor — the "+2 for color" is a CATEGORY LEAP.** d = 4(S⁴) + 1(charge) + 2(color): the +1 for charge is a *real spatial dimension* (the S¹); the +2 for color treats an *internal color-fiber* contribution as 2 additional *effective spacetime* dimensions in the Hardy exponent — that internal↔boundary-dim equivalence is the asserted leap. Tell: +2 = N_c−1 = rank SU(3) lands d *exactly* on g = 2N_c+1 = 7 → either genuine over-determination or reverse-engineered so d=g (→E₀=3→small CKM). Depends on whether "+2=N_c−1" is color-counting *independent of CKM* or CKM-informed. Correctly flagged CONDITIONAL; the right one to pressure-test.

**Methodology RIGHT:** sign grounds off as *leads* for Grace's verified F498 (the arbiter); bank on the run (does small-CKM+large-PMNS fall out?), not the derivation; drop Lyra's broken self-check (a bug, not evidence). Structure-forcing.

**My caveat for the run — asymmetric confirmation:** a match robustly confirms the lepton+neutrino sectors (clean grounds → real prediction) but confirms the down only as strongly as "+2=N_c−1" is target-innocent (if CKM-informed, a matching CKM is partly circular). Want the +2 provenance explicit at the landing, not just the angle match. A miss fingers the down (agreed).

## 9. The mixing run landed ≈0 — DIAGNOSIS AFFIRMED: norms carry no mixing (masses done; mixing is a distinct, unbuilt object)

Grace's run + Lyra's F552 both gave θ₁₂ ≈ 0 for all inputs. **This is CORRECT, not a bug — a theorem.** M = U Σ V†: masses = singular values (Σ = radial norms {N_i}); mixing = relative rotation of left singular vectors (V_CKM = U_L^{u†}U_L^{d}). Eigenvalues ⊥ eigenvectors — norm-only grounds carry ZERO mixing info; shared left-rotation → identity mixing → ≈0 is the correct prediction. **Two genuinely independent constructions converging on ≈0 = structural fact, not two bugs** (the opposite of shared-input; independence *strengthens* it). Lyra's retraction of "broken self-check" (she wanted large angles) = honest own. Grace refusing to fabricate a render = the right call.

**Honest accounting:** masses STAND (14 banked + 6 identified = all Σ's, genuine eigenvalue predictions). But the **mixing finish MOVED — it was mis-scoped**, not one-run-from-done; the six mixing params were behind an object never built. State as honest correction, not pure progress. (A wrong render would hide where the physics lives; a clean ≈0 points at it.)

**Recovery = well-posed promising LEAD, banks nothing yet:** carry the full vector; refraction (up↔down) + d=5→d=4 projection (ℓ↔ν) as candidate eigenvector rotations; qualitative large-PMNS/small-CKM story physically sensible; GST bridge (sin θ_C ≈ √(m_d/m_s)) a real anchor + target-innocence check. Banks only when refraction → Cabibbo lands *forward* + large/small holds *quantitatively*.

**THE crux I referee hardest (Cal #27):** recovery is real ONLY IF the directional/angular data is geometrically FORCED (upstream of the radial projection), NOT supplied/fit to observed angles. Forced → genuine relocation; invented → BST has an honest mixing GAP, not a hidden object. The refraction→Cabibbo test tells them apart. Same bar: orientations forced, not fit.

## 10. (2026-07-16) Angular-input target-innocence check (mixing render) — inputs CLEAR the bar; magnitudes stay gated

Assigned discipline check on the mixing render's angular inputs (F379/F384 directions, F493 phase, F413 Majorana locus). **Target-innocent to a high standard — not a fit-dressed lane. Trending relocation, not gap** (yesterday's crux: directions largely FORCED).

- **ℤ₃ phase (F493) — EXEMPLARY.** ω=e^(2πi/3) forced by N_c=3 (center Z(SU(3))=ℤ₃). CP EXISTENCE forward + gate-independent (complex cube roots N_c≥3 → Im(triple)≠0 generic). **J MAGNITUDE explicitly NOT forward** (phase varied −128/−173/+79° across radii → δ not forced, only existence). No reverse-read. Assumption (generations carry ℤ₃, motivated 3=N_c) named. Model of the discipline.
- **cos ψ = 5/√34 = n_C/√(n_C²+N_c²) (F379/F384) — primaries-only form, ONE residual.** τ-direction=ρ̂ a THEOREM (ν_τ=0 ⟹ τ-address=ρ). Residual: μ-direction=ê₁ (dilation axis) — natural but data-confirmed (Leg 2 selected ρ-dir because it fits V_cb 0.2%). Derived-modulo-one-input; not fishing (old "6/7" fear → primaries-only form); the joint to nail.
- **Large-PMNS/small-CKM (F413) — target-innocent, rides on my Majorana co-sign.** Dirac↔Dirac→small CKM; Dirac↔Majorana→large PMNS. Falls out of the verified-forward Majorana result, not fit.

**Armed flags for Grace's render (Cal #27):** (1) **Bank EXISTENCE/STRUCTURE; HOLD MAGNITUDES** — F493 gates J on radii → J≈3e-5 rides on the done-masses + misalignment, NOT the phase; bank "CP exists from N_c=3", not a J number; same for θ_C≈13° (only if it falls out of cos ψ without re-tuning u_μ). (2) **u_μ=ê₁ residual** — the CKM joint to close. (3) **Five-Absence:** neutrino locus = Z₂/Shilov Majorana sector, NO ν_R sneaking in; no GUT-scale structure to force an angle.

---

**Net:** Majorana co-signed+verified; by-design ratified; θ_QCD sharpened+premise-flagged; Δm² measurement-limited; **sin²θ_W 3/13 CLOSED (fit-suspect).** **Muon 4→5 CONDITIONAL PASS affirmed** (address = pending K697). **α 4π-closure affirmed.** **Spinor E₀=2 = sound lead.** **K703 grounds: 2 clean, down weak anchor.** **Mixing run ≈0 DIAGNOSIS AFFIRMED (theorem; masses stand, mixing relocated).** **Angular inputs (7-16) CLEAR target-innocence — ℤ₃ phase EXEMPLARY, cos ψ primaries-only + u_μ=ê₁ residual, PMNS-large from verified Majorana; bank structure/existence, HOLD magnitudes; prettiness gets no discount.** Next cold-read: Grace's render. Keeper to integrate numbering into `referee_objections_log.md`.

— Cal, 2026-07-15 / -16.

## 11. (2026-07-16 PM) Circularity trace CLOSED + texture watch armed

**Circularity trace CLOSED — clean.** F506's m_s/m_d=20 derived forward: ν=N_c=3 (Wallach threshold) + degrees {1,3,5} (Elie BLIND-LOCKED, T1929) + FK Pochhammer → ladder {(3)₁,(3)₃,(3)₅}={3,60,2520} → s/d=60/3=20=(ν+1)(ν+2) exact at ν=N_c (obs 19.9, 0.5%). **ZERO reference to Cabibbo/V_us/θ_C** (grep empty; derivation purely mass-ladder). So the Gatto identity θ_C=√(m_d/m_s)=√(1/20) is NON-CIRCULAR — masses independent, Cabibbo falls out forward. Reinforced by: {1,3,5} blind-lock (T1929; the one supporting claim to verify for max rigor), honest down-sector-specific scoping (no universal-law over-claim), F502/F503 "miss" = target-selection error not a moved number (20 stable). **Identity closes.**

**Texture watch ARMED (Cal #27 hardest).** Fritzsch/Gatto texture is always basis-attainable (NNI proves nothing) → "derived" ≡ natural basis gives the texture WITHOUT a fitted weak-basis rotation. Three cold-reads for Grace's render:
1. **Natural basis, not fitted rotation** — texture must emerge in the substrate localization/K-type basis; a rotation-to-texture-basis certifies nothing.
2. **Magnitudes + zeros DERIVED** — off-diagonals come out √(mᵢmⱼ) from the overlap geometry; zeros geometrically forced, not imposed.
3. **Viable vs excluded (falsification check)** — BST must land the VIABLE 4-zero (or modified), NOT the EXCLUDED 6-zero Fritzsch. If it forces the excluded 6-zero → clean FALSIFICATION, called plainly (Five-Absence for textures). 

Standing to cold-read Grace's texture render.

— Cal, 2026-07-16.

## 12. (2026-07-16 PM) rank-1 Yukawa mechanism + target-innocence watch on 36/869 + corrections

**Rank-1 dissolves the basis worry — AFFIRMED (credit K709).** M_ij=O_i O_j rank-1 → |M_ij|=√(M_ii M_jj) identically every basis = THEOREM (not fitted basis choice). Gatto texture forced by rank-1; my earlier natural-basis-vs-fitted-rotation concern genuinely resolved. Right kind of resolution (theorem, not narrative).

**36/869 = C₂²/(11·79) — FIT-SUSPECT (specific).** 36=C₂², 11=c_2 substrate-natural; but **79 = rank⁴·n_C − 1 = 80−1 carries a corpus-flagged FIT −1** (the "+1/−1 anomaly," not-principle-grade; same rich-vocab 79 as the retired sinθ_C=2/√79). So V_cb=36/869 rests on a denominator with a documented fit factor — not merely "asserted (K708 gap)" but actively fit-suspect. **Do NOT bank V_cb on 36/869 until 79's −1 is derived.**

**Degeneracy-lifting corrections = the whole target-innocence burden.** Pure rank-1 degenerate (V_cb undefined); down-texture excluded 1.9× (K708). V_cb comes wholly from corrected up+down structure → must be DERIVED, not tuned — and NOT tuned to hit the fit-suspect 36/869 (fitting one fit with another). Forward + lands ≈0.041 = real; aims at 36/869 = circular.

**Honest tier (affirm Lyra):** pure rank-1 → one massive generation → Gatto angles are LEADING-ORDER (natural tier), corrections named — NOT zero-correction exact.

**F506 circularity: closed** (§11 — m_s/m_d=20 forward, no Cabibbo back-fit; Gatto identity non-circular). Standing to cold-read Grace's render: V_cb forward-or-fit, viable-4-zero-vs-excluded-6-zero called plainly, magnitudes derived-not-tuned.

— Cal, 2026-07-16.

## 13. (2026-07-16 eve) F506 closed (unlocks V_us) + 23-block radii = fit-masquerade; refraction is the only forward route

**Job 1 — F506 circularity CLOSED** (confirmed §11): m_s/m_d=20 forward (ν=N_c=3 + blind-locked {1,3,5} + FK Pochhammer), zero Cabibbo reference → θ_C=√(m_d/m_s) non-circular identity → **V_us forward; V_us + rank-1 mechanism cleared for CONDITIONAL PASS on my end.**

**Job 2 — 23-block radii (0.508/0.821) = the fit-masquerade spot. Two tells:**
1. **Not the mass-ratios** — in rank-1/Gatto the radii ARE the masses (done). V_cb needs SEPARATE radii → not a consequence of the banked masses.
2. **Candidate forms are post-hoc form-search that don't even land clean** — r₃≈√C₂/N_c=0.8165 vs fitted 0.821 (0.5% off); r₂≈1/2=0.5 vs 0.508 (1.6% off). Fitting substrate-shaped forms NEAR fitted radii = fit dressed as derivation; the "near not exact" is the tell (a real derivation lands the radius).

**Do NOT bank V_cb on form-searched radii.** ENDORSE the only target-innocent route: derive V_cb from the up↔down **refraction difference (3/2=N_c/rank)** pulling below the rank-1 floor to 0.041, masses the only radial input. Lands → banks; else clean can-fail (real limit, report don't dress).

**36/869 — OUT unless 79 sourced.** 36=C₂², 11=c_2 fine; **79=rank⁴·n_C−1=80−1 carries a corpus-flagged fit −1** (not-principle-grade +1/−1 anomaly; same 79 as retired sinθ_C=2/√79) — NOT sourced. Per wake bar ("11 and 79 must be sourced or out") → 36/869 OUT. Refraction route must NOT be tuned to reproduce it (fitting a fit with a fit).

**Bar to bank V_cb:** forward from refraction, radii fall out EXACTLY from masses (not near-form fit), viable 4-zero, NOT via 36/869. Short of that = clean can-fail (honest result).

— Cal, 2026-07-16.

## 14. (2026-07-16 late) CKM resolved right (K711) + projection-radius √(2/3) innocence: VALUE innocent, amplitude-FORM structural-pending-theorem

**Context:** K711 rejected sub-percent fits (0.041, 36/869) per §13; V_cb → structural 0.044 via projection-truncation (top refracts past boundary y_t=1; radius √(2/3)). Discipline landed correctly.

**Job 1 — F506 CLOSED** (reconfirm §11/§13): m_s/m_d=20 forward, no Cabibbo → V_us forward. No new work.

**Job 2 — √(2/3) target-innocence: SPLIT.**
- Arithmetic: √(2/3)=√(C₂/(C₂+N_c))=√C₂/N_c=√(rank/N_c)=0.8165; all one number since 2/3=rank/N_c=C₂/N_c²=C₂/(C₂+N_c).
- **VALUE 2/3 = INNOCENT (inherited, not fit):** 2/3=rank/N_c=1/(refraction index N_c/rank); the refraction index + critical angle sinθ_c=2/3 (arcsin=41.8°) were FIXED IN THE MUON SECTOR (K698) with ZERO CKM input. radius²=2/3=sinθ_c reads a pre-existing substrate quantity. Four substrate routes → SAME simplest ratio (not four rich numbers near 0.821) = robust, opposite of the 79 rich-vocab problem.
- **Amplitude FORM "radius²=2/3" = STRUCTURAL-PENDING-THEOREM (sets tier ceiling):** why radius=√(2/3) rather than fraction=1−cosθ_c=0.255 (transmitted solid angle) or sin²θ_c=4/9 (projected-disk area)? Asserting radius²=2/3 because 2/3 is the innocent critical sine = form-match at the amplitude step until the hemisphere geometry FORCES transmitted-fraction=sinθ_c. = Lyra's upgrade lead (derive from S⁴×S¹/ℤ₂ + refraction boundary).

**VERDICT: V_cb tier ceiling = STRUCTURAL, honestly** — derivation structural AND data structural (5% incl/excl puzzle; sub-percent was chasing absent precision). Rises to DERIVED iff Lyra's theorem forces transmitted-fraction=sinθ_c=rank/N_c (why 2/3, not 0.255/4/9).

**RECOMMENDATION:** state radius²=rank/N_c=sinθ_c (inherited from muon), NOT C₂/(C₂+N_c) — same number, but the sum-denominator form dresses it as a tunable part/whole; rank/N_c is cleaner and ties to the already-innocent critical angle.

— Cal, 2026-07-16 late.

## 15. (2026-07-16 midday) PMNS: F506 CLOSED (job 2) + PRE-REGISTERED μ-τ target-innocence bar (job 1)

**Job 2 — F506 trace: CLOSED** (§11/§13/§14). m_s/m_d=20 forward, no Cabibbo → V_us forward. No new work.

**Job 1 — μ-τ (2-3) exchange symmetry: PRE-REGISTER the bar BEFORE Lyra answers (so it can't be reverse-engineered from θ₂₃≈45°).**

State of play: **F413 establishes large-vs-small (Dirac-Majorana misalignment) — target-innocent — but NOT the specific 2-3 symmetry.** The μ-τ symmetry is a NEW, still-OPEN rep-theory question (K713), not established. Bar:

1. **Must be an EXACT geometric involution of the chargeless d=4 locus** — a specific ℤ₂ isometry swapping the gen-2/gen-3 support-strata addresses, DERIVED from removing SO(2)/the charge circle (d=5→d=4), with NO input from the observed angle. The lore "μ-τ symmetry → θ₂₃=45°, θ₁₃=0" is the CONSEQUENCE, not evidence FOR the symmetry; the evidence must be the involution itself (which coordinate dropped, why 2↔3 and NOT 1↔2). = the tribimaximal trap (K712 #1): do NOT posit maximal mixing and add θ₁₃ as an epicycle.

2. **RED FLAG (falsifiable, can fail):** F86's inverted pyramid puts gens 2,3 at DIFFERENT-dimension strata (gen-2 = Cartan slice dim=rank; gen-3 = Shilov boundary). So it is NOT obvious they differ only by the dropped S¹ coordinate. Lyra must SHOW the chargeless reduction makes the 2-3 addresses exchange-symmetric — a nontrivial claim that could genuinely fail. (GOOD news: F86 already makes gen-1 DISTINCT (origin), so a residual 2-3 symmetry after dropping S¹ is geometrically motivated IF gens 2,3 collapse — but it must be exhibited, not assumed.)

3. **Symmetry ALONE under-produces (verified):** exact μ-τ → sin²θ₂₃=1/2 (45°), θ₁₃=0. Banked forms are sin²θ₂₃=4/7 (48.4°), sin²θ₁₃=1/45 — NOT maximal, NOT zero. So the deliverable is involution + DERIVED breaking. The breaking (1/2→4/7 = +1/14 = +1/(rank·g); 0→1/45) must be sourced from the SAME locus geometry, target-innocent — NOT two independent tunings, and 1/(rank·g) is rich-vocab-vulnerable (must be derived, not matched).

4. **DISCRIMINATOR + bonus falsifiable prediction:** genuine μ-τ-breaking CORRELATES θ₁₃ with (θ₂₃−45°) through ONE breaking parameter. If Lyra's derivation yields both from ONE substrate quantity → strong target-innocent (a Schur generator, Cal #35/#36). If two independent knobs → weak/fit-suspect. Either way it yields a **falsifiable structural prediction: the θ₂₃ octant/deviation ↔ θ₁₃-magnitude correlation** (DUNE/HyperK-testable), which BST should own regardless of tier.

**VERDICT: μ-τ is PROMISING but UNPROVEN.** Bar set. Do NOT let "μ-τ→maximal" lore OR the near-45° data substitute for the geometric involution. PASS iff (1) exact involution derived from the SO(2)-drop + (3) breaking from one named substrate quantity giving 4/7 and 1/45 with (4) the θ₁₃↔θ₂₃ correlation. Anything reached from an imposed 2-3 ansatz = tribimaximal trap = FAIL.

— Cal, 2026-07-16 midday.

## 16. (2026-07-16) Referee F558 at the seam — the 4 conditions on the μ-τ involution. Cond 2 NOT cleared (the pin); cond 1/4 substantially met; cond 3 relocated.

**F558 (Lyra) derives the SOURCE of μ-τ, not the ansatz — real progress, honestly tiered (grounded-lead, nothing banked). Ruling per condition:**

- **COND 1 (exact involution from SO(2)-drop, NOT the tribimaximal trap): SUBSTANTIALLY MET.** The Shilov ℤ₂ (the /ℤ₂ of S⁴×S¹/ℤ₂) is target-innocent — part of D_IV⁵'s definition, predates PMNS. Deriving "chargeless → drop S¹ → residual ℤ₂ survives" instead of imposing μ-τ clears the trap in spirit. FURTHER anchored: "fix gen-1, swap 2↔3" aligns with the INDEPENDENTLY-banked fact that gen-1 is the massless ℤ₃-protected ground (m_ν1=0) — so "fix the distinct one, swap the excited pair" is natural, NOT chosen to hit 45°. Creditable structural win.

- **COND 2 (ℤ₂ DEMONSTRABLY swaps 2↔3 on the generation addresses): NOT CLEARED — THE PIN.** Category gap: the ℤ₂ acts on the boundary SPACE (S⁴×S¹); the μ-τ exchange must act on the generation INDEX (the F86 support-strata / K-type addresses). The induced action is ASSERTED, not derived. Collides with the §15 red flag: F86 puts gen-2 at the Cartan slice, gen-3 at the Shilov boundary — DIFFERENT-dimension strata, so a boundary involution does not obviously transpose them. **The pin (concrete, falsifiable):** exhibit the three neutrino generation K-type/weight addresses on the chargeless d=4 locus, and show the /ℤ₂ generator acts on the SO(5) weight labels as exactly the transposition (23) with gen-1 on the fixed axis. If gen-2,gen-3 weights are ℤ₂-conjugate (mirror pair) and gen-1 is on the axis → clears. If not → mechanism boundary found (forms stay banked). Lyra flags this herself ("to pin"); HONEST. Do NOT let "μ-τ → 45°" (standard, verified: eigenvector (0,1,−1)/√2 exact) substitute for this.

- **COND 3 (breaking SINGLE-sourced from one substrate quantity): PARTIALLY MET — and the fit-risk RELOCATES.** One knob not two: the θ₁₃↔θ₂₃ correlation is the one-parameter signature and checks at same-order (sin²θ₂₃−½ = 1/14 vs ½ sin θ₁₃; **4.2% off exact** → single-sourcing SUPPORTED at structural tier, not proven). SHARP POINT: the mechanism moves the fit-risk OFF 4/7 (no longer a fundamental form — 4/7 = ½ + 1/14, and note 4/7 = rank²/g = (n_C−1)/(n_C+2), two readings = rich-vocab, now moot) ONTO the breaking magnitude **1/14 = 1/(rank·g)**, which becomes the single load-bearing number and is rich-vocab-vulnerable. It must be DERIVED from the "small S¹ remnant in the Weinberg operator," not matched to θ₁₃. Currently ε is fixed by sin θ₁₃ (a match), not forward. Open.

- **COND 4 (θ₁₃↔(θ₂₃−45°) correlation as a falsifiable prediction): MET.** One-breaking predicts UPPER octant θ₂₃≈49° correlated to the observed θ₁₃ — a real, DUNE/HyperK-testable octant prediction. Strongest, most target-innocent part; BST should own it regardless of whether cond 2 fully pins.

- **θ12 scale-independence: DERIVED-GIVEN-μ-τ (real progress).** Under μ-τ, θ12 is a 1-2-block RATIO → decouples from Σ → works with m_ν1=0 hierarchical (Σ~0.058, DESI-ok); dissolves Grace's quasi-degeneracy artifact (a genuine internal-consistency threat) WITHOUT the no-degeneracy line. Inherits cond-2 contingency; specific 3/10 = N_c/(rank·n_C) still open (Lyra flags).

**BANK RULING (for Keeper/K712):** Do NOT bank θ23/θ13 mechanism yet — cond 2 is a grounded-lead, not cleared. The SOURCE is target-innocent (not the trap) and the octant correlation (cond 4) is bankable AS A PREDICTION. Bank θ23+θ13 as derived-mechanism ONLY when (i) the ℤ₂→(23) action on the generation addresses is exhibited (reconciled with F86 strata) AND (ii) the breaking magnitude 1/(rank·g) is derived from the S¹-remnant. Until then: banked-forms + strong target-innocent lead. This is PASS-track, not yet PASS.

— Cal, 2026-07-16.

## 17. (2026-07-16) The knife on Casey's neutrino-oscillator hypothesis: currently a RELABEL, right kind, one-knob test settles it. DEVELOP not discard.

**Verify:** sin²θ13/sin²θ12 = (1/45)/(3/10) = 2/27 = rank/N_c³ ✓ (and N_max = N_c³·n_C + rank = 137, same integers). m_ν3/m_ν2 = √(100/3) = 5.77 = genuinely anharmonic (harmonic n=2/n=1 = 2.0) ✓.

**Q1 — derivation or relabel? RELABEL (doc admits "2/27 is a MATCH").** The oscillator earns a real QUALITATIVE win over F558: θ13 = Δn=2 gives θ13 an INTRINSIC home (small, nonzero, doesn't touch θ12, correlated with θ23) — fixes F558's charged-lepton-contamination failure. BUT the MAGNITUDE 2/27 is forced by nothing: harmonic ⟨0|x|2⟩ = 0 EXACTLY; Δn=2 opens only via anharmonic coupling λ, and Δn=2/Δn=1 is a FUNCTION of λ + the choice of coupling operator, NOT a universal oscillator constant. "It's an oscillator" does not predict 2/27.

**Q2 — force vs tune = reduces to Q3 (one knob vs two).** Forces 2/27 IFF: (i) ONE anharmonicity, (ii) fixed independently by the banked masses (5.77), (iii) via a coupling operator fixed target-innocently (S⁴ Casimir, not chosen), (iv) COMPUTES to 2/27. Zero of four shown.

**Q3 — smuggling? TWO knob-risks.** (1) "position-degenerate → maximal θ23" IS the μ-τ/ℤ₂ claim re-worded → inherits UNPINNED §16 cond-2; AND it CONFLICTS with F86 (F86: gens 2,3 at DIFFERENT strata Cartan-vs-Shilov; oscillator: SAME shell diff frequency) — must reconcile, not assume. (2) λ → 2/27 map hides an operator-choice knob (Morse vs quartic vs Casimir give different Δn=2 laws) unless the coupling operator is the substrate's own, fixed independently.

**THE ONE TEST (bar to bank θ13 derived):** Fix the S⁴ Casimir/Laplacian spectrum target-innocently → read the two frequencies (→ masses, must give 5.77) AND the ground→2nd-mode overlap (→ θ13/θ12, must give 2/27) from the SAME operator, NO tuning. Same operator → both → ONE knob → strong/bankable. Re-tune needed → two knobs → unification oversold (discard unification; qualitative θ13-home may survive). DISCARD trigger: fixed-operator gives θ13/θ12 ≠ 2/27, or mode-count ≠ ground+2.

**CONVERGENCE (constructive):** Lyra's Step 1 (mode-count on S⁴: massless ground + exactly 2 modes, position-degenerate/frequency-split) is the SAME derivation that pins §16 cond-2 — the two degenerate-position modes ARE the ℤ₂-conjugate pair. One computation grounds BOTH the oscillator AND the μ-τ ℤ₂. Efficient; pursue it.

**VERDICT: DEVELOP, don't shoot.** Right kind of hypothesis (attacks θ13, target-innocent-SHAPED via bare rank/N_c³, falsifiable: θ13 = θ12·2/27 correlated with θ23-octant, no charged-lepton contamination). But currently a RELABEL — does NOT bank until the one-knob computation FORCES 2/27 from the operator that also gives 5.77. Not yet a derivation; a well-posed, falsifiable path to one.

— Cal, 2026-07-16.

## 18. (2026-07-17 Fri) Projection Theory — target-innocence knife, segment by segment. Segments 0-2 + face derive/inherit clean; the EDGE (√(3/4), θ13) is the one fit-risk. HOLD on the blind sweep.

**Segment target-innocence scorecard:**
- **n = N_c/rank = 3/2** (refractive index), **arcsin(2/3)=41.8°** (projection angle): target-innocent, INHERITED from the muon critical angle (K697/F548), predate mixing. ✓ clean.
- **Fresnel √ (amplitude=√intensity → mixing=√mass-ratio):** NOT a new knob — the √ is already EXACT in rank-1 Yukawa (|M_ij|=√(M_ii·M_jj), banked). Fresnel is a target-innocent RE-READING of an exact feature, adds no freedom. ✓
- **Face √(2/3) (V_cb):** §14 — VALUE innocent (2/3=rank/N_c=sinθ_c from muon), amplitude-FORM pending Lyra's hemisphere theorem (which segment-3 now attempts). Consistent.
- **V_cb evanescent truncation (up→r=1=y_t=1):** derives clean; self-consistency √(2/3)·√(3/2)=1 EXACT; y_t=1 predates CKM. ✓
- **masses-radial→invariant→precision / mixings-angular→sheared→structural:** framework reading, coherent, NO new knob; but it's an EXPLANATION not a derivation — its falsifiable content IS the universality sweep.

**THE FIRE — EDGE √(3/4) + θ13 = 3/35×√(3/4):**
- Verified: 3/35×√(3/4)=0.074231 vs 2/27=0.074074 → **0.2% INEXACT (not an identity).** And 3/35 = the UNIQUE nearest bare ratio (q≤40) to (2/27)/√(3/4)=0.08553 → **back-solve signature** (answer÷curvature → nearest simple form). Replacing the EXACT bare-integer 2/27=rank/N_c³ (§17) with an inexact curvature-dressed product is BACKWARDS on target-innocence. **DO NOT bank on the 0.2% match.**
- Two honest mitigations (the knife defends real structure too): (1) composition **√(3/4)·√(2/3)=√(1/2) EXACT** → the factors are the √((d−1)/d) descent LADDER (3→2, 4→3), NOT independent fitted numbers; (2) 3/35=N_c/(n_C·g) has an INDEPENDENT identity (S⁴ ⟨x⁴⟩ = Δn=2 second-harmonic). IF forward-derived, not back-solved.

**BANK BAR for θ13 (three, NONE using 2/27):** (a) 3/35 derived FORWARD as the S⁴ ⟨x⁴⟩ boundary value, computed WITHOUT reference to 2/27 [if read as (2/27)/√(3/4) → REJECT]; (b) √(3/4) derived as the 4→3 edge curvature from κ_Bergman=−n_C, independent of θ13; (c) **universality sweep run BLIND** — √(3/4) confirmed on OTHER chargeless observables, θ13 EXCLUDED from its own evidence.

**CIRCULARITY WARNING (the load-bearing discipline):** θ13's 0.2% match CANNOT validate the edge factor — √(3/4) was INTRODUCED to explain θ13. It earns its keep only on observables that did NOT motivate it. If θ13 is the ONLY place √(3/4) appears → one-observable curvature fit = fishing, θ13 stays structural, and exact 2/27=rank/N_c³ remains the honest form.

**RICH-VOCAB SLIDE flag:** pin whether √(3/4)'s "3,4" are DIMENSIONS (4→3 descent rung) or BST INTEGERS (N_c, rank²) — they coincide only because N_c=3, rank²=4. Derive from ONE; do not slide between the two readings to make √(3/4) look doubly-motivated.

**VERDICT:** Projection theory is coherent and MOSTLY target-innocent — segments 0-2 + face derive or inherit clean, and the descent-ladder composition (√(1/2)) is a genuine exact consistency. The EDGE (√(3/4), θ13) is the SINGLE fit-risk and is currently a one-observable, 0.2%-inexact, back-solve-shaped curvature match. HOLD — gated entirely on (a) forward 3/35 + (b) κ_Bergman edge derivation + (c) the BLIND universality sweep. Prefer exact 2/27=rank/N_c³ until the edge factor earns the decomposition on OTHER observables. The sweep is the right make-or-break test; it must exclude θ13 from its own evidence.

— Cal, 2026-07-17.

## 19. (2026-07-17 Fri) μ-τ sum-rule route for θ13/θ23/δ — referee the CORRELATION not the value. The whole target-innocent content = whether cosδ is DERIVED.

**Edge-projection CLOSED NEGATIVE (recorded):** Grace's sweep + §18 knife ruled out the universal shear; edge-wrap = backsolve; θ13 reverts to clean 1/45 = rank/N_c³. Projection theory's derived segments (n=3/2, arcsin(2/3), Fresnel-√, V_cb evanescent) kept as narrative; universal-shear claim dropped. Correct discipline.

**The sum rule cos2θ23 ≈ sinθ13·cosδ (hep-ph/0601118) is STANDARD** — holds in ANY μ-τ-breaking model, target-innocent. Using it is NOT a fit.

**★ THE SHARP POINT (referee the correlation, not the value):** cosδ = cos2θ23/sinθ13 = the RATIO of the θ23-deviation to θ13. So the sum rule is one equation in three measured quantities; the entire target-innocent content is **whether that ratio (= cosδ = δ) is DERIVED from the geometry:**
- ONE ε fixes cosδ geometrically → δ PREDICTED → θ13/θ23/δ close from one source → BANKS (structural).
- cosδ left free (two independent ε) → δ NOT predicted → the "correlation" is EMPTY, two knobs → FAIL.
**⟹ the DERIVED δ (equivalently cosδ) is BOTH the payoff AND the proof. The deliverable that banks is δ, NEVER θ13's 0.1% match to 1/45** (that's the answer; §18 circularity discipline; the pull is right).

**ε must be derived FORWARD from the chargeless-locus geometry (the imperfect ℤ₂ residual), NOT set to reproduce θ13=1/45** — that would just relocate the edge-wrap backsolve into ε. REJECT if ε is read off from θ13.

**Consistency VERIFIED (single-ε viable):** |cos2θ23|/sinθ13 = (1/7)/(1/√45) = 0.958 < 1 → a valid δ EXISTS → predicts cosδ ≈ −0.958 → **δ ≈ 163° or 197° (DUNE-testable).** Report as the falsifiable output; don't claim the value (Grace renders, DUNE decides). Had the ratio exceeded 1, no δ → sum rule would FAIL; it doesn't.

**C1 branch CONFIRMED (target-innocent):** BST is NORMAL hierarchy (m_ν1=0 banked, ℤ₃-protected → no quasi-degeneracy) + UPPER octant (sin²θ23=4/7=0.571>1/2 → θ23=48.4°). Both independent of the sum rule.

**Cautions:** (1) |cos2θ23|=1/7=1/g is an EXACT consequence of banked 4/7 — a consistency signature, NOT independent evidence (don't cite as a separate win). (2) PIN the sum-rule coefficient to hep-ph/0601118's derivation — a tuned coefficient shifts the predicted δ = a hidden knob. (3) rich-vocab flag stands: pin whether ε's integers are dimensions or {N_c, rank²}, derive from one.

**VERDICT:** the sum-rule route is the RIGHT structure — target-innocent, one-parameter, correlated, δ-PREDICTING — a real improvement over both the edge-wrap (backsolve, §18) and the oscillator (2/27 unforced, §17). Banks θ13+θ23 at STRUCTURAL tier IFF (a) ε derived forward from the chargeless locus, (b) cosδ/δ derived from the geometry (not free), (c) the θ23↔θ13↔δ closure holds from that one ε. Evidence = the derived δ, never θ13's 1/45.

— Cal, 2026-07-17.

## 20. (2026-07-17 Fri) Referee ε (F563/K717). Correlation + δ-prediction SOUND; "closes to DERIVED" NOT yet earned (2 DOF fit, 1 predicted); 197° branch currently DATA-picked.

**F563 discipline is clean:** F562 √(3/4) backsolve RETRACTED, Grace's negative accepted, correlation-not-value framing correct, ε honestly tiered grounded-lead / nothing banked. Credit.

**Correlation IS one-source & target-innocent (confirm):** ε = ONE complex number = 2 real DOF (|ε|, arg ε). Re(ε) = |ε|cos(arg ε) is NOT independent → the sum rule cos2θ23 = sinθ13·cosδ is AUTOMATIC, not a third knob. So "three faces of one imperfection" is structurally right, and the octant is fixed (cos2θ23 = −1/7 < 0 → UPPER, target-innocent from banked 4/7).

**★ DOF SHARPENING (the catch): a complex ε has TWO DOF, and both are currently FIT.** |ε| ← θ13 (1/√45), and Lyra inputs cos2θ23 = −1/7 (θ23) → 2 DOF absorbed by θ13 & θ23; only **δ is the genuine sum-rule prediction.** So the sector is right now **STRUCTURAL (two independently-banked forms 4/7, 1/45) + ONE forward prediction (δ) + the correlation — NOT yet DERIVED.** "θ23/θ13/δ upgrade to DERIVED from ε" requires ε's TWO DOF to BOTH derive from geometry (ZERO fit DOF → three forward checks). That has not happened; ε is grounded-lead.

**BAR for ε → DERIVED (pre-registered, none using measured angles):** (i) |ε| derived forward from the imperfect-ℤ₂ residual → gives sinθ13 = 1/√45; (ii) arg(ε) derived forward INCLUDING quadrant → gives δ; then (iii) θ23-tilt = Re(ε) via the sum rule is the over-determination check. Both DOF derive → 3 forward predictions, sector closes DERIVED. Only existence posited + magnitudes fit → structural + 1 prediction.

**★ BRANCH FLAG (the pull's explicit ask — "derivation picks the branch, not the data"):** cosδ = −N_c√n_C/g = −3√5/7 is BRANCH-AMBIGUOUS → δ = 163.4° OR 196.6°. The banked cosδ form does NOT select 197°. F563 picks 197° because it "matches T2K/NOvA ~195–200°" — that is DATA-picking the branch. Target-innocent status: δ banks at the |cosδ| level (both branches); **selecting 197° over 163° requires sign(Im ε) = sign(sinδ) = sign(J_PMNS) DERIVED from the geometry, NOT chosen to match the measurement.** Octant (Re ε sign) is target-innocent; CP-branch (Im ε sign) is INDEPENDENT and currently data-dependent. Close it by deriving arg(ε)'s quadrant.

**Cautions:** the "self-consistency |ε| = (1/g)/|cosδ| = 1/√45" is TRUE BY CONSTRUCTION (sum rule rearranged), NOT independent corroboration — same as |cos2θ23|=1/g being 4/7 re-expressed. The one genuine target-innocent output is cosδ (and it's branch-ambiguous).

**VERDICT:** correlation = DERIVED-mechanism (standard μ-τ, target-innocent) ✓; δ = forward PREDICTION banks at |cosδ| level ✓; **but the sector does NOT close to DERIVED until ε's magnitude AND phase both derive from the chargeless locus (zero fit DOF), and the 197° branch is selected by sign(Im ε) from geometry, not by T2K/NOvA.** Referee stays on ε's two derivations and the branch sign — never on 1/45.

— Cal, 2026-07-17.

## 21. (2026-07-17 Fri) g-organization (K719): the two identities CONFIRMED target-innocent (strong sense); δ CONDITIONAL + a SIGN CATCH on sinδ=rank/g.

**Job 1 — the two primary identities: CONFIRMED exact + target-innocent in the STRONG sense.**
- g² = N_c²·n_C + rank² → 49 = 45 + 4 ✓; N_c + g = rank·n_C → 10 = 10 ✓.
- Both reference ONLY the fixed integers {rank, N_c, n_C, g} — NO neutrino observable. You cannot retrofit an identity among fixed integers (49 either equals 45+4 or not; it does). So they are innocent by construction, NOT reverse-engineered from the angles. The Schur-generator reading (g organizes four observables via two exact relations) is legitimate target-innocent STRUCTURE and banks as such.
- HONEST framing note (Cal #27, peak-elegance): "four shadows of ONE integer g" is a legitimate RE-CENTERING enabled by the identities, not g being uniquely privileged — sin²θ13 = 1/(N_c²·n_C) is rewritten as 1/(g²−rank²) via the identity. The IDENTITIES are the content, not g's primacy. State it that way.
- CAVEAT: target-innocent identity ≠ δ derived. The identity fixes the MAGNITUDES |sinδ|=rank/g, |cosδ|=N_c√n_C/g GIVEN the two banked angle forms; it does not by itself derive δ.

**Job 2 — δ derived-not-chosen: AFFIRM the conditional downgrade + a SIGN CATCH.**
- AFFIRM K717→conditional: Grace's catch (generic 2-3 breaking → δ=0; sum rule needs a specific class — column-preservation / charged-lepton-1-2) is exactly the §20 DOF/one-source concern made concrete. δ=197° is CONDITIONAL on BST's imperfect-ℤ₂ being a sum-rule-realizing class. Correct; not oversold.
- ★ SIGN CATCH (new): g²=45+4 fixes sin²δ = rank²/g², i.e. |sinδ| = 2/7 — the MAGNITUDE ONLY. The SIGN of sinδ IS the branch (= sign Im ε = sign J_PMNS). Verified: δ=196.6°("197")→sinδ=−2/7→J<0; δ=163.4°→sinδ=+2/7→J>0. So **"sinδ = rank/g = +2/7" as WRITTEN is the 163° branch (J>0), which CONTRADICTS the claimed 197° (which needs sinδ=−2/7).** The Pythagorean identity does NOT pin the branch. Pin sign(Im ε) from the S⁴ geometry BEFORE writing sinδ=+2/7 — as written it selects the wrong branch. (Octant is separately fixed by cos2θ23<0 → upper, target-innocent; CP-branch is independent.)

**VERDICT:** g-organization banks as target-innocent STRUCTURE ✓ (two exact fixed-integer identities, not retrofitted). δ's MAGNITUDE forms bank. δ as a SIGNED angle (197°) is (a) CONDITIONAL on the breaking class (affirm Grace) and (b) BRANCH-UNPINNED (sign catch — and the written +2/7 is inconsistent with 197°). Do NOT report δ=197° as "derived" until BOTH the sum-rule-realizing class AND sign(Im ε) land from geometry. Referee stays on the breaking-class realization + the sinδ sign, never on 1/45.

— Cal, 2026-07-17.

## 22. (2026-07-17 Fri) Exact-only gate on the Consolidated 26-linear-algebra doc: syzygy classification CONFIRMED; enumeration discipline sharpened; octonion/gauge tier over-promotion flagged.

**SYZYGY GATE (Layer 2) — classification CONFIRMED correct, discipline sharpened.**
- g² = N_c²·n_C + rank²: verified genuine POLYNOMIAL LAW (holds for ALL rank under the recipe N_c=r+1, n_C=r²+1, g=r²+r+1). ✓ deep.
- N_c + g = rank·n_C: verified VALUE-SPECIFIC (r³−r²−r−2 = (r−2)(r²+r+1), only real root r=2). ✓
- SHARPEN for the exhaustive enumeration (workstream B): small integers {2,3,5,7} are MASSIVELY over-related — most exact identities are value-specific coincidences (e.g., N_c²=n_C+rank²: 9=5+4 looks Pythagorean but is value-specific, roots r∈{0,2} only). So **exact-identity COUNT is NOT evidence of structure** — that would be fishing dressed as a lattice. Only (a) the GENERATIVE RECIPE (one generator rank=2) and (b) genuine POLYNOMIAL LAWS carry structural weight. Value-specific exact identities are the DEFAULT (expected), and count ONLY when load-bearing in a derivation. Also: polynomial>value-specific is a DEPTH/generality ranking, NOT a target-innocence ranking (both are target-innocent among fixed integers).

**DERIVED-vs-CORRESPONDENCE LINE (Layer 3, octonion/gauge) — the doc is mostly honest (names 3 open frontiers, tiers SM-link as correspondence) BUT the consolidated tier line (line 26) OVER-PROMOTES three items to DERIVED:**
1. **"𝕆 = BST's spinor" — derived for the COMPACT form SO(7)/complex B₃, NOT for BST's ACTUAL group.** BST's group is the NON-compact real form SO(5,2); the octonion/G₂/Spin(7) spinor lives in the compact SO(7). These are different real forms of B₃. Whether the octonionic spinor survives to SO(5,2) IS the doc's own OPEN frontier #1 (real-form/chirality). So the honest tier is "derived for B₃/SO(7); real-form selection to SO(5,2) OPEN" — not flatly DERIVED. The dim-8 match is real; the real form is the gap.
2. **"one gen = ℂ⊗𝕆 = rank⁴" is the Furey/Dixon CORRESPONDENCE, not a BST derivation** — the doc lists it under BOTH "DERIVED" and "correspondence + external anchor." Internal inconsistency; it belongs in correspondence. "=rank⁴=16" is integer-matching on top.
3. **The "primaries = PG counts over F₂" grounding rests on "rank=2 = F₂"** — itself an identification (2=2), NOT yet a derivation. IF rank=2 genuinely carries F₂-projective structure (derived), then g=Fano=Im(𝕆)=7 is STRUCTURAL (same object, not coincidence) and the whole labeling earns "correspondence+." IF "rank=2=F₂" is just 2=2, the PG/octonion labeling is INTEGER-MATCHING (the weakest tier the discipline itself flags). This is the LOAD-BEARING derived-vs-correspondence question of Layer 3 — name it as the gate, don't bank it as DERIVED.

**INTEGER-MATCHING FLAG:** "BST integers label the ladder EXACTLY" (Im ℍ=3=N_c, Im 𝕆=7=g, dims 2/4/8=rank^{1,2,3}) is structural ONLY IF "rank=2=F₂ + primaries=PG counts" is derived; otherwise it is the weakest tier (integers coincide with fixed division-algebra facts). Do NOT let "label exactly" upgrade a coincidence.

**VERDICT:** Layer 1 (lattice reduction) + Layer 2 (recipe + the ONE polynomial law verified) are sound and honestly tiered. Layer 3's DERIVED column should be demoted on the three items above to: 𝕆=spinor [derived for SO(7), real-form OPEN]; ℂ⊗𝕆=gen [CORRESPONDENCE]; PG-over-F₂ [gated on deriving rank=2=F₂]. The genuinely BST-DERIVED core of Layer 3 is narrower than the tier line states — and the whole octonion story hinges on the single question "does D_IV⁵ (real form SO(5,2)) select the octonionic construction," which is exactly frontier #1. Keep that question the headline of Layer 3, not a footnote to a "DERIVED" bank.

— Cal, 2026-07-17.

## 23. (2026-07-17 Fri) Layer 2 COMPLETE — polynomial-law enumeration + the g-organization is TIERED (2 deep, 2 shallow). Branch-flag/retraction accepted (noted).

**Accepted upstream:** my §20/§21 branch flag landed — δ=197° reverts to data-picked, J<0 = data input not prediction; and F567 chirality→CP over-reach retracted cleanly. Discipline held both ways.

**COMPLETENESS (the honest answer to "exhaustive enumeration"):** the polynomial-law layer is COMPLETELY generated by the recipe — ONE generator (rank) + 4 defining laws (N_c=rank+1, n_C=rank²+1, g=rank²+rank+1, C_2=rank²+rank). Every other polynomial law is a CONSEQUENCE, and consequences are unbounded (one-variable ring ℤ[rank]) → **their COUNT is NOT evidence (§22).** Verified consequence-spine (all hold ∀rank):
- **C_2 = rank·N_c** (Casimir = rank×color) ✓
- **g = C_2 + 1 = n_C + rank** ✓
- **N_c² = n_C + 2·rank** ✓
- **(g−rank)(g+rank) = N_c²·n_C** ✓ — the load-bearing CP-magnitude law.

**VALUE-SPECIFIC (verified, hold only near r=2):** N_c+g=rank·n_C (r=2 only); g=2rank²−1 (r∈{−1,2}); N_c²=n_C+rank² (r∈{0,2}).

**DISCIPLINE ILLUSTRATION (same number, two tiers):** 9=5+4 reads as **N_c²=n_C+2·rank (POLYNOMIAL LAW)** OR **N_c²=n_C+rank² (VALUE-SPECIFIC)** — because rank²=2·rank only at r=2. The polynomial-law reading is the true structure; the rank² reading is its value-specific shadow. Prefer the law reading; don't cite the shadow as if deep.

**★ THE REFINEMENT (headline — refines §21's "g-organization"): the g-organized neutrino sector is TIERED, NOT uniformly deep.**
- **θ13 + δ-magnitude** (sin²θ13=1/(N_c²n_C); |sinδ|=rank/g, |cosδ|=N_c√n_C/g): ride the **POLYNOMIAL LAW** (g−rank)(g+rank)=N_c²n_C — DEEP, robust ∀rank.
- **θ23-tilt** (cos2θ23=−1/g): rides **g=2rank²−1** — VALUE-SPECIFIC (r∈{−1,2}), load-bearing → counts, but shallow.
- **θ12** (sin²θ12=N_c/(N_c+g)=3/10): rides **N_c+g=rank·n_C** — VALUE-SPECIFIC (r=2 only), load-bearing → counts, but shallow.
So "four shadows of one integer g" is honest but **2-DEEP (law) + 2-SHALLOW (value-specific)**, not uniformly deep. State the g-organization at that split tier — the CP magnitude is the deep result; θ23-tilt and θ12 are load-bearing value-coincidences at rank=2.

**GATE for value-specific (standing):** a value-specific identity counts ONLY when load-bearing (used in a derivation). N_c+g=rank·n_C and g=2rank²−1 qualify (θ12, θ23-tilt). A value-specific identity that rides nothing is numerology — excluded.

**VERDICT:** Layer 2 is COMPLETE and honestly tiered: polynomial-law spine = the recipe (1 generator, closed); the ONE load-bearing polynomial law is the CP magnitude (g−rank)(g+rank)=N_c²n_C; the g-organization splits 2-deep/2-shallow. Count-of-identities remains a non-metric.

— Cal, 2026-07-17.

## 24. (2026-07-17 Fri) §22 frontier ANSWERED (SO(5,2) spinor = quaternionic, octonions hosted). Tier line on the NEW quaternion/weak lane.

**§22's load-bearing question SETTLED — with a computed reason.** Cl⁰(5,2) ≅ Cl(5,1), (p−q) mod 8 = 4 → ℍ(4): the SO(5,2) spinor is QUATERNIONIC, NOT octonionic (verified two ways: charge-conjugation on (5,2) gammas + Clifford/Bott classification; octonions need Cl(5,2)⊗ℂ = Cl(7,ℂ), reachable only by complexifying away the two minus signs). So the octonion→SM spine is **HOSTED, proven-not-a-derivation** — exactly the boundary I flagged in §22, now closed with a theorem, not a table. Clean discipline outcome (Lyra built it, didn't cite it).

**AFFIRM the pivot's strength claim:** the ℍ-structure is NATIVE — forced by the actual (5,2) signature — unlike 𝕆 which needed complexification. So the quaternion lane CAN genuinely reach "derived" where the color/octonion lane structurally could not. This is a real improvement and the right lane. ✓

**TIER LINE TO HOLD (the knife): "native quaternionic structure" ≠ "derived SU(2)_L weak force."** Three sub-claims bundled in "ℍ = the weak sector," each a structures-match trap:
- **(a) THE DEEPEST TRAP — is the Sp(1)=SU(2) of the ℍ-structure the GAUGE SU(2)_L, or the generic SU(2) that EVERY quaternionic space carries?** dim_ℂ ℍ=2 and Sp(1)=SU(2) are BST-INDEPENDENT facts — every ℍ-space has an Sp(1). That an SU(2) is PRESENT is NOT that the WEAK GAUGE group is derived. Needs: the SU(2) acts as a GAUGE symmetry on the right fermion content, not merely as ℍ-automorphisms.
- **(b) is the ℍ left/right non-commutativity the weak V−A chirality?** ℍ non-commutativity gives a genuine left/right asymmetry — suggestive for V−A — but "derived" needs WHICH handedness couples + right-handed fermions = SU(2)-singlets, from the geometry, not just "ℍ has a handedness."
- **(c) do the fermion DOUBLETS (actual reps (ν,e)_L …) come from the spinor decomposition**, or just "ℍ is 2-dim over ℂ so doublets exist"? Needs the real rep content.

**BAR for DERIVED (higher than octonion could reach):** (a)+(b)+(c) from the SO(5,2) geometry. All three → genuine native derivation of the weak sector (a real, strong result). Only "ℍ carries an SU(2) + a handedness" → structures-match masquerade: native STRUCTURE, but SU(2)_L identification still hosted/asserted.

**Cautions:** (1) rank=2 = h^∨(SU(2)_L) is INTEGER-MATCHING (2=2), weakest tier — suggestive, not derivation. (2) BOUNDARY: native = WEAK ONLY. Color/octonion stays HOSTED (Lyra just proved it). Do NOT let the quaternion win bleed into re-claiming color natively via ℍ⊂𝕆 — that smuggles the hosted color piece back as native; it isn't. (3) Five-Absence OK: SU(2)_L is the observed weak group, not a GUT — safe.

**VERDICT:** octonion frontier CLOSED (hosted, computed). Quaternion/weak lane OPEN and genuinely native — the real derivation opportunity, and structurally able to reach "derived" where color couldn't. I referee it on (a)+(b)+(c) — the gauge-action, the chirality-selection, and the doublet reps — never on "ℍ has an SU(2)" or rank=2=h^∨. Native structure is the floor; derived weak force is earned only by the three.

— Cal, 2026-07-17.

## 25. (2026-07-17 Fri) Referee F570/F571 (native weak sector). Chirality-lock VERIFIED (elegant, derived); hold the line on single-gauging + real-form/signature + a ν_R Five-Absence check.

**VERIFIED CORRECT (credit fully):**
- **F570 group theory:** Spin(5)≅Sp(2)=USp(4) (both dim 10, standard exceptional iso, quaternionic) ⊃ Spin(4)=SU(2)_L×SU(2)_R; the 4-spinor = (2,1)_L⊕(1,2)_R. Standard, target-innocent Lie theory. The electroweak DOUBLET structure genuinely falls out of the geometry — my §24 checklist item (c) is MET.
- **F571 chirality-lock:** VERIFIED by explicit Cl(7) construction — ω=γ₁…γ₇=−i·𝟙 is CENTRAL (odd d=7); ω=γ₅^ST·χ^int exactly; γ₅^ST²=+1, χ^int²=−1, [γ₅^ST,χ^int]=0; eig(χ)=±i, eig(γ₅^ST)=±1. Since ω is a SCALAR, on any χ^int-eigenstate γ₅^ST is FIXED → a weak doublet has DEFINITE spacetime chirality. **The lock is genuine, elegant, target-innocent (g=7 fixed long ago). "A weak-SU(2) doublet is necessarily single-handed, FORCED by g=7 odd" = DERIVED.** Strongest native SM-derivation in the corpus; I agree the weak sector (not color) is BST's real derivation lane.

**TIER LINE TO HOLD (residuals, precise):**
1. **"Weak force VIOLATES PARITY" ≠ the chirality-lock alone.** The lock says gauging EITHER SU(2) gives a chiral coupling; it does NOT say only ONE is gauged. Full parity violation = "only one SU(2) is gauged, not both" = the DYNAMICAL-GAUGING residual (Lyra correctly holds it open). Lock makes chirality automatic PER doublet; it does not select single-gauging. So: chiral-NESS DERIVED; "weak force violates parity" still needs the single-gauging step. Don't merge them.
2. **L-vs-R absolute = convention: AGREE** (defensible — IF the two SU(2)s are mirror-symmetric and one is gauged; like the sign of charge). Correct physics, not a hidden gap.
3. **REAL-FORM / SIGNATURE check (the sharp technical one):** the lock is verified in COMPLEXIFIED Cl(7,ℂ) — real-form-independent, a genuine PLUS over the octonions (no real-form choice needed for the lock). BUT identifying the internal-3 with the COMPACT weak SU(2)_L is NOT free: (5,2) − (3,1)_spacetime = (2,1)_internal = NON-compact SO(2,1), not compact SO(3)=SU(2). So F571's "internal-3 = weak SU(2)" must be reconciled with F570's "weak SU(2) ⊂ compact SO(5)" and the SO(3,1) signature. The lock survives; the weak-SU(2) IDENTIFICATION needs the compact real form pinned. Don't let "verified in Cl(7,ℂ)" paper over which real SU(2) it is.
4. **FIVE-ABSENCE check (flag):** (1,2)_R contains a right-handed neutrino ν_R. Does the native doublet structure require a PROPAGATING ν_R — the forbidden sterile neutrino — or is it the non-sterile Majorana partner (consistent with BST's Majorana/no-sterile)? Must be checked; the elegant (1,2)_R must not smuggle in a forbidden ν_R.

**VERDICT:** F570 doublets + F571 chirality-lock = DERIVED and verified — the real native SM-derivation, genuinely stronger than the hosted octonions (and the lock is real-form-INDEPENDENT, unlike the octonion story). Residuals, honestly: (1) single-gauging (dynamical) for full parity violation; (2) compact-real-form identification of the internal SU(2) [signature (2,1) vs compact SO(3)]; (3) the ν_R Five-Absence consistency. "BST derives the electroweak doublet+chirality structure natively" is defensible and strong; "derives the weak force dynamically / full parity violation" is the residual. Bank the first two rows; hold the third.

— Cal, 2026-07-17.

## 26. (2026-07-17 Fri) FOR THE RECORD: odd-g parity IS target-innocent. + Pre-registered native-vs-matching bar on sin²θ_W (3 traps).

**ODD-g PARITY TARGET-INNOCENCE — CONFIRMED for the record:** g=7 was fixed as a substrate primary in the original five-integer set (2022), long before any parity/weak-sector work. The chirality lock (§25, verified in Cl(7)) uses ONLY g=7's ODDNESS — zero reference to the observed parity violation. So "the weak force is chiral because g=7 is odd" is target-innocent, AND falsifiable (even substrate → chiralities float free → no forced parity violation). Genuinely new physics stated geometrically. Affirmed.

**sin²θ_W = N_c/(N_c²+rank²) = 3/13 — pre-registered bar (native-vs-matching). THREE traps:**
1. **FORM-MATCH:** 3/13 = N_c/(N_c²+rank²), with 13 = N_c²+rank² an anchor — a recognizable form. Banks native ONLY IF it is a COMPUTED embedding normalization: the Dynkin/trace-index ratio Tr(T_{SU(2)_L}²)/Tr(T_{U(1)_Y}²) for SU(2)_L=Sp(1)⊂SO(5) and U(1)_Y=SO(2) inside SO(5,2), computed target-innocently and EMERGING as 3/13 — NOT "3/13 recognized, then a normalization fitted to it." The computation must be innocent of the observed 0.231.
2. **★ FIVE-ABSENCE / GUT-REASONING (fire hardest — the 3/8 lesson):** "an embedding FIXES sin²θ_W" is itself GUT-LIKE reasoning — in the SM, sin²θ_W is a FREE parameter (SU(2)_L, U(1)_Y independent couplings); ONLY unification fixes it. sin²θ_W=3/8 is the forbidden SU(5) GUT value. BST's 3/13 is non-GUT (good), BUT the MECHANISM must be verified to NOT smuggle coupling-unification (common gauge coupling at a scale → proton decay / all-three-couplings unify). Allowed IFF it is a pure geometric normalization of two factors inside SO(5,2)/SO(5) WITHOUT unifying SU(3) (color is hosted/separate) and WITHOUT GUT gauge bosons. Fine line — run it through Five-Absence explicitly.
3. **SCALE/RUNNING honesty (the 'runner' issue):** sin²θ_W RUNS. 3/13=0.2308 sits at the M_Z MS-bar value (0.19%), NOT a bare/high-scale value; on-shell is 0.2229 (3.5% off). An embedding gives a value at the GEOMETRIC scale that must RUN to M_Z. If 3/13 is claimed "at the natural scale" but compared to the M_Z number WITHOUT running, that's a scale-mismatch fudge. The derivation must state the scale of 3/13 and compare to the measurement AT that scale (or run honestly).

**STANDING FLAG:** I previously tiered sin²θ_W=3/13 FIT-SUSPECT (earlier log §5: source's own Section 7 says "conjectured/WHY open"; catalog "derived" over-claims). The embedding computation is exactly what COULD overturn that — but the bar is: target-innocent Dynkin-index computation (trap 1) + Five-Absence-clean non-GUT mechanism (trap 2) + honest scale-matching (trap 3). Clear all three → runner→forced-native. Any one fails → stays runner/fit-suspect.

**Native tier AFFIRMED (for balance):** the weak sector IS native (from the (5,2) signature) and CAN reach "derived" where color couldn't — doublets (F570) + parity (F571) are verified-derived (§25). sin²θ_W is the right next test because the embedding is a definite computation; I referee it on the three traps, never on the 0.19% match.

— Cal, 2026-07-17.

## 27. (2026-07-17 Fri EOD) sin²θ_W embedding = HONEST NEGATIVE (naive → forbidden GUT 3/8); octonion "intrinsic-J" refinement = fair upgrade, hosted-line SURVIVES.

**sin²θ_W — §26 trap 2 FIRED, honest negative (credit Lyra F572):** the naive SU(2)_L/U(1)_Y embedding in SO(5,2) gives sin²θ_W = **3/8 = the forbidden SU(5)/SO(10) GUT value**, NOT 3/13. So the embedding-DERIVATION of 3/13 FAILED — exactly the GUT-reasoning trap I pre-registered. Ruling:
- **3/13 is NOT derived.** It survives only as a corpus-banked FORM/SIGNATURE (sin²θ_W = N_c/(N_c²+rank²) carries the color number N_c) — suggestive of Casey's dual-face weak-color coupling, but an OBSERVATION, not a derivation. Tier: **runner / signature, NOT forced.**
- **Cal #27 (peak-elegance):** "the weak mixing angle knows about color" is a genuinely interesting observation and the dual-face motivation is a nice story — but the ONE attempt to derive it gave the forbidden value. Do NOT let the 0.19% form-match + the elegant motivation read as "derived." K731's "robust signature" = robust FORM, not banked derivation.
- **RECURRENCE flag:** tan²θ_W = 3/10 = N_c/(rank·n_C) = **sin²θ12 (PMNS)** — same value-specific identity N_c+g=rank·n_C (§23, rank=2-only, shallow). Two unrelated observables share 3/10: note it, but same-source-test-or-rich-vocab (don't over-read; 3/10 is an accessible form).
- **DUAL-FACE avenue (open, HIGH fit-risk):** the escape from 3/8 to 3/13 via the compact-dual Q⁵ face must be a PRINCIPLED computed normalization that gives 3/13 for a reason INDEPENDENT of avoiding the forbidden 3/8 and hitting the corpus form. Bar (unchanged §26): computed dual-face Dynkin normalization → 3/13, Five-Absence-clean (no coupling-unification/proton-decay), scale-honest (3/13 sits at M_Z, not bare). Escape-hatch risk is HIGH precisely because the straightforward computation already gave the forbidden value.

**Octonion "intrinsic complex structure" refinement (Lyra F572-A) — FAIR upgrade, but the hosted line SURVIVES:** D_IV⁵ is Hermitian symmetric → intrinsically complex (the SO(2) charge circle IS the canonical J), so the complexification SO(5,2)→SO(7,ℂ) reaching the octonions uses the domain's OWN complex structure — **canonical, not the "complexify away the minus signs" cheat I/F569 framed.** Fair; credit Casey+Lyra. BUT: it is still a COMPLEXIFICATION. The physical spinor over the REAL (5,2) form is QUATERNIONIC (§24, verified); the octonions live in the complexified spinor. So:
- **Upgrade:** octonions from "artificially hosted (cheat)" → "CANONICALLY hosted (natural complexification via intrinsic J)." Real improvement.
- **Line survives:** WEAK sits at the REAL Lorentzian level (quaternionic, no complexification); COLOR needs the (canonical) complexification. So color remains ONE LEVEL less native than weak. "Canonically reachable by complexifying" ≠ "the real physical structure IS octonionic." g=7=Im(𝕆)=Fano is structural AT the complexified level (fair upgrade to §22), not at the real Lorentzian level.
- Net: weak = NATIVE (real form, derived §25); color = CANONICALLY-HOSTED (upgraded, but hosted). The two-tier distinction is intact and now more precisely drawn.

**EOD STATE (referee ledger, robust vs open):**
- ROBUST/DERIVED-native: EW doublets (F570), parity-from-odd-g (F571, verified §25), the g-organized neutrino magnitudes (§21/23, δ-mag + θ13 on the polynomial law).
- CANONICALLY-HOSTED: octonion/color spine (F572 upgrade).
- HONEST NEGATIVES today: sin²θ_W naive embedding → 3/8; projection universality sweep; chirality→CP bridge. All three killed cleanly — discipline working.
- OPEN (closure avenues + bars): dual-face sin²θ_W [3 traps §26]; dynamical gauging W/Z; real-form reconcile F570-vs-F571 SU(2); ν_R Five-Absence; hypercharge U(1)_Y; 3 generations; gravity-scale reducibility.

— Cal, 2026-07-17 EOD.

## 28. (2026-07-17 Fri) sin²θ_W reduced to k (no-manufacture line); three-door synthesis tiers CONFIRMED with precision.

**sin²θ_W = N_c/(N_c + k·n_C) — the reduction to one integer k is GENUINE PROGRESS, but k=rank is DATA-SELECTED-then-relabeled (hold no-manufacture):**
- k=1 → 3/8 (forbidden GUT); k=rank=2 → 3/13 (BST); k=3 → 1/6. Verified.
- **k=2 is the UNIQUE integer giving ~0.231 (the observed value)** → k=2 is DATA-SELECTED; "k=rank" is the relabeling of the data-required value. This is the razor: the whole Weinberg angle now hangs on one integer, and that integer is currently fixed by the answer, not the geometry.
- **PRINCIPLED part (fair to BST):** BST is NOT a GUT — U(1)_Y = SO(2) is a SEPARATE factor (the complex structure J), not inside a simple group with SU(2)_L. So k need NOT be 1, and Five-Absence REQUIRES k≠1 (k=1 is the forbidden GUT). So "k≠1" is genuinely principled. But k could be anything ≠1; **k=rank SPECIFICALLY must fall out of the computed SO(2) charge-circle Dynkin/index normalization (the g'² normalization relative to SU(2)_L), for a reason innocent of 3/13.** If computed → sin²θ_W derived (a real NON-GUT geometric prediction, and Casey's weak-color coupling confirmed). If k=rank asserted/relabeled → still a runner.
- SCALE note: softer than a GUT here — BST has no high-scale unification, so 3/13 need not run 14 orders; the geometric scale may ~be the EW scale. Still state the scale of the k=rank prediction.
- BAR (final): computed SO(2) normalization → k=rank, Five-Absence-clean (separate factor, no coupling-unification), scale-honest. The reduction to k is the win; the computation of k=rank is the pending target-innocent step.

**THREE-DOOR SYNTHESIS (K732): SU(3)×SU(2)×U(1) = 𝕆×ℍ×ℂ — CONFIRM the tiers, with precision:**
- **ℂ → U(1) [DERIVED at group level; normalization OPEN]:** SO(2) = the complex structure J = a U(1). Group solid. BUT the U(1) is hypercharge-like (U(1)_Y), and U(1)_em = T_3+Y/2 needs EW mixing; and its NORMALIZATION (k=rank) is exactly the open sin²θ_W question. So "ℂ→U(1) derived" = the GROUP; the hypercharge normalization is NOT yet derived. Don't let "U(1) EM derived" gloss the normalization gap.
- **ℍ → SU(2)_L [DERIVED native]:** verified §24/§25 — real-form quaternionic spinor, doublets (F570), parity (F571). Fair for the STRUCTURE; dynamical gauging (W bosons) + real-form reconcile (F570-vs-F571) + ν_R still open.
- **𝕆 → SU(3) [SUPPORTED-not-derived]:** §27 — canonically-hosted via intrinsic complex structure (upgrade from cheat), but color needs the complexification; NOT native like weak. "Supported-not-derived" = CORRECT tier. Confirmed.
- **★ derived-vs-correspondence on the WHOLE synthesis (Cal #27):** "SU(3)×SU(2)×U(1) = 𝕆×ℍ×ℂ" is elegant and correctly tiered, BUT the "division-algebras → SM gauge group" LINK is the EXTERNAL Furey/Dixon/Baez correspondence (§22/§24), NOT BST-derived. **BST's genuine novelty = a SINGLE geometric home (D_IV⁵) for the three algebras + NATIVE EM/weak (real-form ℂ/ℍ).** Don't let "= 𝕆×ℍ×ℂ" read as "BST derives the SM gauge group" — it derives EM+weak natively and provides a canonical home for the (externally-corresponded) color.

**CONFIRM (Casey's ask):** three-door tiers = EM derived(group)/normalization-open, weak derived-native, **color supported-not-derived** ✓. The synthesis is real and defensible at these tiers; the algebra→group link is external correspondence, BST's contribution is the shared domain + native EM/weak.

— Cal, 2026-07-17.

## 29. (2026-07-17 Fri) sin²θ_W √rank mechanism — NOT gating (per Casey); pre-registered LANDING bar + a discriminator lane for the computation.

**Protocol:** Casey's steer = investigate, don't pre-gate; referee at the landing. Followed. This is NOT a verdict — the boundary computation hasn't landed. Recording the shape + the bar + a lane so the ruling is mechanical when Lyra posts.

**SHAPE (honest, now):** √rank on Y ⟺ rank in Y² ⟺ k=rank (§28, consistent). The √rank MECHANISM (a normalization factor + a geometric story) is a BETTER shape than a raw form-match — but "Lyra solved for √rank" means she found the factor that turns 3/8 into 3/13, i.e. it was SOLVED-FOR-GIVEN-THE-TARGET. "Solved not fit" understates that: solving for the factor that hits 3/13 IS the fit; what would SAVE it is the INDEPENDENT boundary computation producing √rank. So the "two rulers → √2" is currently a MOTIVATING STORY, not yet a computation.

**★ DISCRIMINATOR LANE (hand to the investigation, not a gate):** the "two rulers on the rank-2 boundary → norm over 2 directions = √2 = √rank" story has a gap. The domain's TWO NATURAL rulers are the ρ-vector components (n_C/rank, N_c/rank) = (5/2, 3/2) — and their norm is **|ρ| = √34/2 ≈ 2.92, NOT √2 = 1.41.** (√34 is itself a BST quantity — cos ψ=5/√34, m₃/m₂.) So the naive 2-direction norm gives √34/2, not √rank. **WHICH two EQUAL rulers give √2?** The ρ-components are unequal → √34/2. The computation must identify the equal-weighted pair that yields √rank, or √2 comes from a different structure. This is the load-bearing discriminator — flagging it now as a lane helps Lyra, doesn't gate her.

**PRE-REGISTERED LANDING BAR (guide at landing):** √rank banks (sin²θ_W runner→derived) IFF —
1. **Direction:** √rank EMERGES from the RMS/projection + ρ-vector + FK/Shilov computation → 3/13 falls out. NOT "solve for the factor giving 3/13." The direction of the computation is the tell.
2. **Two-rulers is a genuine geometric count** (why exactly 2 equal rulers → √2, resolving the √34/2 discriminator), not a story fitted to √2.
3. **Five-Absence clean** (non-GUT, separate SO(2) factor, no coupling-unification).
4. **Scale-honest** (state the scale; milder than GUT since no high-scale unification).

If (1)–(4) → derived, and I'll say so plainly (a real non-GUT prediction + Casey's weak-color coupling confirmed). If √rank stays solved-for-target with a story → still a runner. **Ruling deferred to the landing, per Casey.**

— Cal, 2026-07-17.

## 30. (2026-07-17 Fri) sin²θ_W two-isomorphic-circles candidate — NOT gating; §29 flag engaged; the whole result is ONE binary (one circle vs two).

**Protocol:** referee at landing, per Casey. Not a verdict.

**§29 flag ENGAGED (good-faith):** my §29 concern (the domain's two natural rulers = ρ-components (5/2,3/2) → √34/2, NOT √2) got a direct response: the resolution is NOT the ρ-vector but TWO ISOMORPHIC SO(2) circles (equal BY isomorphism, not the unequal ρ). That's a real answer to the "which two EQUAL rulers" discriminator. Credit.

**Fermion-trace numbers VERIFIED:** sin²θ_W = Tr(T₃²)/(Tr(T₃²)+c²·Tr(Y²)) with Tr(T₃²)=2, Tr(Y²)=10/3. c²=1→3/8 (GUT); c²=|Y|²=rank=2→3/13 (BST). Arithmetic sound; the only question is c².

**★ THE WHOLE RESULT IS ONE BINARY (the crux to verify FIRST):** c² = |Y|² = 1 (ONE hypercharge circle → 3/8 GUT) vs 2 (TWO independent circles → 3/13 BST). The (1,1)-over-two-circles gives |Y|²=1²+1²=2 ONLY IF there are TWO GENUINELY INDEPENDENT SO(2)'s (a 2-torus). **But Keeper's own candidate says D_IV⁵ and Q⁵ SHARE the isotropy SO(5)×SO(2) — which has only ONE SO(2) → literally reads as c²=1 → 3/8.** So the load-bearing question (= Keeper's flagged honest seam): **are the charge-circle and color-circle TWO INDEPENDENT U(1)'s (2-torus → (1,1) → |Y|²=2), or the SAME shared SO(2) (→ |Y|²=1 → GUT 3/8)? That binary IS sin²θ_W.** Verify this BEFORE the (1,1)-forcing — if it's one shared circle, the whole thing collapses to the forbidden value.

**LANE — honest labeling (dimensions-vs-integers slide, §22 pattern):** if |Y|²=2 comes from "# dual faces = 2," note that a bounded symmetric domain has exactly ONE compact dual → "domain+dual = 2" ALWAYS, independent of rank. So the 2 most naturally reads as "# faces (always 2)," NOT "rank" (2 here, coincidental). State it as "two faces," not "rank" — and note this SHARPENS falsifiability: the mechanism predicts sin²θ_W=N_c/(N_c+2n_C) fixed, not rank-varying. (Also GOOD for target-innocence: "always 2" is non-tunable.)

**LANDING BAR (refined, §29+this):** derived IFF — (1) TWO genuinely-independent circles shown (resolve the shared-SO(2) crux, NOT one circle double-counted); (2) Y FORCED to be the (1,1) diagonal — threads both AND equally (isomorphism → equal), not assumed; (3) the 2 labeled honestly (faces, non-tunable) — target-innocent (counts faces, not 3/13); (4) Five-Absence clean (Cartan-dual, non-GUT); (5) scale-honest. Rule at landing.

**Keeper's honest seam noted + endorsed:** his "the color circle sits somewhere I haven't placed it" IS the one-vs-two-circle crux above. Tiered correctly as candidate, not result. That's the right disposition; the crux is the thing to nail first.

— Cal, 2026-07-17.

## 31. (2026-07-17 Fri) Referee Elie's SECOND seam (toy 4707 Part-2): VALID — the marquee's chain has a broken middle step. Two formulas, two numbers.

**Elie's catch (separate from Keeper's geometric retraction) is CORRECT and important.** The marquee "prove Killing-norm²(Y)=rank → c²=rank → sin²θ_W=3/13" conflates TWO different objects both labeled "rank":
- **(1) PURE-GAUGE / Killing:** sin²θ_W = ‖T₃‖²/(‖T₃‖²+‖Y‖²) = 1/(1+rank) = **1/3** (0.333). Proving ‖Y‖²(Killing)=rank lands HERE — Lyra's own catch ("3/13 is NOT a pure-gauge Killing number; that's 1/3"), now Elie-corroborated. Does NOT match obs 0.231.
- **(2) FERMION-TRACE:** sin²θ_W = Tr(T₃²)/(Tr(T₃²)+c²Tr(Y²)) = 2/(2+c²·10/3). c²=1 → **3/8** (GUT); c²=rank → **3/13** (matches obs).
- Both invoke "rank" but feed DIFFERENT formulas → 1/3 vs 3/13. **Physical sin²θ_W (obs 0.231) = 3/13 = FERMION-TRACE.** So proving the literal Killing statement lands on 1/3, NOT the target.

**RULING: the marquee as stated is PROVABLE-BUT-INSUFFICIENT.** Lyra could succeed at "‖Y‖²=rank" and correctly get 1/3, missing 3/13. The real closure is TWO arrows: (i) ‖Y‖²=rank from the geometry, AND (ii) why the PHYSICAL sin²θ_W is the fermion-trace object with c²=rank (→3/13), not the pure-gauge Killing ratio (→1/3).

**★ SHARPENING (connects to §26/§28): Arrow (ii) IS the Five-Absence/GUT trap I've flagged three times.** The fermion-trace formula's c²=1 baseline = the GUT 3/8; it's the SU(5)-style Tr(T₃²)/Tr(Q²) calculation. So justifying c²=rank in the TRACE must NOT import GUT unification (Five-Absence). The geometry naturally gives the Killing norm (→1/3, pure-gauge); the physical number needs the trace normalization (→3/13), which is the GUT-adjacent, high-risk arrow. The two "rank"s differ precisely BECAUSE BST isn't a GUT (pure-gauge and fermion-trace Weinberg angles coincide only for GUT-complete content). So Arrow (ii) is the load-bearing one, and it's the same trap.

**RECOMMENDATION: fold Elie's restatement into the prompt BEFORE relay.** Agree with Elie's lean — cheaper to fix the target than chase the wrong one. Restate the marquee as the two arrows so Lyra doesn't spend Vol 60 forcing ‖Y‖²=rank and land on 1/3. (Prompt is Keeper's file — my role is the ruling; Keeper/Casey fold it in.)

**Net EW-sector state after both seams:** the GEOMETRIC identification (which two circles) is retracted/open (Keeper §30 crux); the FORMULA selection (Killing 1/3 vs trace 3/13) is a SECOND open arrow (Elie, this section) = the Five-Absence/GUT trap. sin²θ_W stays reduced-to-lead; TWO independent things must land, not one. Both are honest open, correctly scoped. The number (3/13) is untouched; what's open is BOTH which-geometry AND which-formula.

— Cal, 2026-07-17.

## 32. (2026-07-17 Fri) Referee Lyra's B−L re-posing of sin²θ_W: genuine advance (resolves Elie's seam in principle) + THREE load-bearing pieces, one a correctness gap.

**GENUINE ADVANCE — credit:** Lyra re-posed sin²θ_W = 1/(2 + ¼‖B−L‖²) using PHYSICAL gauge couplings (g ∝ 1/‖generator‖), NOT the GUT/fermion-trace formula — so it resolves Elie's §31 seam IN PRINCIPLE (no GUT smuggled). And it reduces sin²θ_W to ONE physically-meaningful quantity ‖B−L‖² — better than the abstract c². **"Color enters via B−L" is a REAL structural fact:** a quark's baryon number = 1/N_c because N_c quarks make a baryon, so N_c is genuinely IN B−L geometrically — Casey's weak-color coupling has a real home now (supersedes the √rank/two-spheres heuristic). Honest that ‖B−L‖² is uncomputed. Real step up: fog → formula-ambiguity → one meaningful number with color's fingerprint.

**THREE load-bearing pieces at the landing (not just ‖B−L‖²):**
1. **‖B−L‖² = 28/3 is the REVERSE-ENGINEERED TARGET (uncomputed).** 28/3 → 3/13, 8/3 → 3/8 (verified). So the number that gives the answer is known; the geometric COMPUTATION of ‖B−L‖² is the open piece (Lyra honest). Target-innocence pending: it must COMPUTE to 28/3, not be set to it.
2. **The denominator CONSTANT "2" is ALSO load-bearing.** At ‖B−L‖²=28/3: const=2 → 3/13, but const=1 → 3/10. So the weak-sector normalization (the "2") must be derived alongside ‖B−L‖² — verify the WHOLE formula, not just the B−L norm.
3. **★ CORRECTNESS GAP: Q = J₁₂ + (B−L)/2 FAILS for right-handed fermions.** Verified: u_R → 1/6 (physical 2/3), e_R → −1/2 (physical −1), d_R → 1/6 (physical −1/3). The formula is the LEFT-handed-only charge; the universal charge needs T₃_R: Q = T₃_L + T₃_R + (B−L)/2, i.e. hypercharge Y = 2·T₃_R + (B−L), NOT just (B−L). **So ‖B−L‖² may NOT be the whole U(1) normalization — the T₃_R (SU(2)_R) piece is dropped.** Connects to §25 (the (1,2)_R / SU(2)_R / ν_R sector, still open). Either J₁₂ secretly = T₃_L+T₃_R (clarify), or the reduction to ‖B−L‖² alone is incomplete. Verify the charge assignment is universally correct before banking the B−L reduction.

**Elie's seam:** Lyra CLAIMS resolved (physical couplings). Elie raised it — Elie should VERIFY no GUT formula smuggled in the g∝1/‖generator‖ derivation. Plus Five-Absence + scale gates (Lyra notes scale) still apply.

**VERDICT:** the B−L re-posing is a real advance in interpretability and correctly avoids the GUT-formula trap in principle — the marquee is now "compute ‖B−L‖²" instead of "force a formula," which is sharper and target-innocent-shaped. BUT the derivation is pending AND has TWO extra load-bearing pieces beyond ‖B−L‖² (the constant "2"; the right-handed charge/T₃_R correctness). Referee at the landing of the ‖B−L‖² computation — and specifically check the right-handed charges, because if T₃_R must enter, ‖B−L‖² isn't the whole story. sin²θ_W stays reduced-to-lead.

— Cal, 2026-07-17.
