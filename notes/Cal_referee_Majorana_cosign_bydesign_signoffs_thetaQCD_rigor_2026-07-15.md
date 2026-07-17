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
