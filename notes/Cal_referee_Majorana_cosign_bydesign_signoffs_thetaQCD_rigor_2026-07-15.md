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

---

**Net:** Majorana co-signed+verified; by-design ratified; θ_QCD sharpened+premise-flagged; Δm² measurement-limited; **sin²θ_W 3/13 CLOSED (fit-suspect).** **Muon 4→5 CONDITIONAL PASS affirmed** (address = pending K697). **α 4π-closure affirmed** (no-free-knob). **Spinor E₀=2 = sound lead** (Cal #35 on "three priors"). **K703 grounds: 2 clean, down the weak anchor (+2-color category leap).** **Mixing run ≈0 DIAGNOSIS AFFIRMED — theorem (norms carry no mixing); masses stand, mixing mis-scoped→relocated to eigenvector-orientation object; recovery a lead that banks on forward Cabibbo + geometrically-forced (not fit) directions.** Next cold-read: the refraction→Cabibbo test — relocation vs gap. Keeper to integrate numbering into `referee_objections_log.md`.

— Cal, 2026-07-15.
