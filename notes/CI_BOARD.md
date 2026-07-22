---
title: "CI Coordination Board — Monday 2026-07-20 · NEW ROW: CP phase = the commutator [H_u,H_d] (after the condensate arc closed)"
author: "Casey Koons & team (Keeper, Lyra, Elie, Grace, Cal)"
status: "WEAK-CHIRALITY: DIRAC (K822). CHARGE SECTOR DERIVED given reps + non-circular on T2521 (K828/K829). GAP(a): instanton bundle over S⁴ computed k=±1 (Lyra/Elie 4790 — the grading MECHANISM is realized). ★ BUT K831: 'k=1 → one generation' hits a vector-like obstruction (= the squeeze/K822 anticommutator; Witten-KK confirms it — cosets are real-rep/vector-like even with nonzero index). Casey reframe 'linear algebra one manifold': obstruction = K822 (ours); escape = non-orientable Z₂ (K826, ours); no KK machinery. **FRONTIER (pure D_IV⁵ linear algebra): do the Z₂-projected instanton-twisted holomorphic sections carry a COMPLEX (chiral) or REAL/pseudoreal (vector-like) rep? SU(2) doublet is pseudoreal → the CHIRALITY is carried by U(1)_Y (makes rep complex) = the DERIVED charge sector.** Parity NOT derived by k=1 — held HARD. Prompt: team_prompt_2026-07-22T."
---

# CI COORDINATION BOARD — front page (2026-07-20)

## ▶▶▶ NEW ROW — CP phase (round 10 landed; K788/K789) → derive MAXIMAL leptonic CP (`team_prompt_2026-07-20k`)
**Condensate arc CLOSED (K785/K786):** spine + angular=1 banked; the continuous-fundamental inversion (publishable); 127/128 = parameter-free conditional (→ consolidate).
**★★ CP row — round 10 DERIVED a real result (K788):** CP = the commutator **J ∝ det[H_u,H_d]**; at rank-1 (both from the one O) the matrices are the same projector → commute → **J=0 at leading order** (verified). So **CP is small BECAUSE the condensate is rank-1** — structural, not fine-tuned. J = (mixing angle)³ × phase (J_CKM=3.08e-5 ✓); the smallness is the corrections cubed, the phase is O(1).
- **★ STRUCTURAL PREDICTION (Lyra):** CKM CP ≪ PMNS CP — quark = rank-1 (suppressed), **neutrino = rank-2** (F589, m₁=0 → NOT suppressed the same way). Matches data (J_CKM tiny; δ_PMNS near-maximal).
- **✅ CP/NEUTRINO ROW CLOSED (Round 13, K792) — δ_PMNS is a FREE parameter, for TWO independent geometric reasons:** (1) rank-2 M_ν = m₂v₂v₂ᵀ + m₃v₃v₃ᵀ; δ = relative phase of the two flavor-vectors; the strata are **radial** but δ is an **angular** S¹ phase (Shilov U(1)) → radial⊥angular → geometry can't fix it. (2) **no-ν_R = Five-Absence** → no phase-carrier → δ-open ⟺ no-ν_R. Elie 4760: real strata → δ=0 (opposite of −90° hint, target-innocent, DUNE-δ≠0 kills it). **Honest DUNE story: BST predicts δ unconstrained (like SM), distinct from maximal-predicting models. Nothing tuned to −π/2 all row.**
- **✅ ROW BANKED clean:** CP small = rank-1 (J=0, verified 3×); CKM ≪ PMNS (~1000×); flavor = one overlap object. **Neutrino SIX target-innocent:** m₁=0 (from domain rank-2, survives no-seesaw), sin²θ₁₂=3/10, sin²θ₁₃=1/45, sin²θ₂₃=4/7, Majorana, 0νββ band, **no-seesaw/no-ν_R (Five-Absence)**; δ honestly free.
- **✅ THREAD 1 RESOLVED (Tue, Lyra + K793/K794) — δ_PMNS stays FREE (F618).** Reading B ("identity has no phase") is TRUE but = the **ν₁ Majorana phase** (already banked via m₁=0), NOT δ. δ = ν₂–ν₃ relative phase, both nonzero/discrete-log → present, not absent. Reading A rests on the 127/128 discreteness premise + doesn't select → free either way. A-strong ruled out. **Honest DUNE story holds; nothing tuned to −π/2.** (ν S⁴-locus at rank-1 ridge: consistent, open — needs closer analysis.)
- **▶▶ ROW 2 IN PROGRESS (Tue, K794) — QUARK+LEPTON HIERARCHY, reduced to ONE question.** Convergent (Elie 4761/4762, Lyra, Grace): rank-1 → only gen-3 massive (confirmed); one geometric λ spans all 3 sectors — up-type ~λ⁴/step, **down-type & charged-lepton both ~λ²/step.** **★ THE QUESTION: why is up-type ALONE doubly-suppressed (λ⁴ vs λ²)?**
- **⚖ ADJUDICATED (Tue R2, K795) — Lyra(ε²) vs Elie(ε¹): NO contradiction, both right.** Saturation ALONE does NOT give λ⁴ (Elie 4763, 4 ways — generic correction → ε¹). Lyra's ε² holds ONLY IF the up-type correction's **first-order kernel-block vanishes** (→ seesaw-through-top ε²/s). Both flagged the same open check. **Unified condition for up-type λ⁴: the up-type correction δM has a vanishing kernel-block in the PHYSICAL strata basis = a texture zero / selection rule.** (Repair to Lyra: ⊥O gives the trivial projector-block; need a selection rule on δM, not O.)
- **⚖ ROUND 3 — F621 RETRACTED (Lyra, honest); reduction RIGOROUS (Grace+Elie).** λ⁴ ⟺ up-type ⊥⊥-block (charm–charm direct coupling) vanishes as an INVARIANT (Elie: σ₂-power is weak-basis invariant → a Fritzsch/NNI basis-zero is cosmetic, can't fake ε²). Saturation is the proximate red herring (Grace verified); top=O + saturated-top-stability survive as banked facts.
- **★ KEEPER MATH CONTRIBUTION (K796):** the correct selection rule is **Wigner–Eckart** — block vanishes ⟺ **c_L⊗c_R\* ⊉ (1,0) vector** (O's rep), NOT "sphericity" (the singlet is ⊥ the vector; refines Grace's K745). **THE FORK:** (A) EXACT texture zero (grading selection rule → clean integer → **λ⁴ DERIVED**) vs (B) RADIAL-localization suppression (continuous → **Tier-2**, non-integer). **Evidence leans (B):** Grace's OBSERVED scatter λ^{2.0–4.3} (non-integer) + the 5D-localization mechanism BST actually uses (web) both point to continuous suppression, not a texture zero.
- **★★ REFRAME (K797, Casey's exponent question) — STOP testing "powers of λ," test the RATIOS.** The λ-exponent p=ln(ratio)/ln(λ) is a lossy log: an EXACT ratio **m_s/m_d = 20 = rank²·n_C** (Tier-1, RG-invariant) shows up as p≈2.01, camouflaged as "messy λ² Tier-2 scatter." **Exponents project discrete-code structure onto a continuous log axis → hide exact algebra.** RETRACT "scatter ⟹ Tier-2" (K796 lean) — scatter is uninformative.
- **✅ QUARK-HIERARCHY ROW CLOSED (Round 5, K799) — 3-part honest close, paper drafted.** (1) **Mechanism located:** radial localization on F86 strata; **(B)** no texture zero (generations = radial copies of one K-type → uniform Wigner–Eckart rule; Elie's exact (a,0)-criterion is the unrealized (A)-branch). (2) **Asymmetry located:** top-saturation (y_t=1, boundary) sets the anchor → falloff rate (Lyra's F621 homed). (3) **Precision — ONLY m_s/m_d = 20 = rank²·n_C survives** (0.7%, unique) + lepton ladder. **Rejected by audit:** m_b/m_s (real 51.4; forms 45/50/54 bracket → fit-trap; Grace's 45 = wrong value), m_c/m_u=588 (over-fit, m_u ±22%), m_t/m_c=137 (pole/running artifact, RGI~277).
- **Paper:** `BST_Quark_Mass_Hierarchy_As_Radial_Localization_DRAFT_2026-07-21.md` (Lyra to finalize prose+PDF). Statement: located mechanism + one exact new ratio, NOT a full-spectrum derivation — boundary marked sharply.
- **Key methodological win (reusable):** mechanism (A/B) ⊥ precision (Tier-1/2); TEST RATIOS not λ-exponents (m_s/m_d=20 hides at p≈2.01); same-sector ratios RG-invariant. (K797/K798.)
- **Banked spine +:** … CP small=rank-1 · CKM≪PMNS · no-seesaw/6-of-7-ν · δ-free · quark rank-1→gen-3-only · **m_s/m_d=rank²·n_C + quark-hierarchy=radial-localization (new)**.

### ✅ CKM MIXING ROW — high-value part DONE (K800). Landed same as masses (SAME object).
- **★ BANKED — the flavor UNIFICATION:** quark masses + CKM mixings = ONE inter-stratum overlap object (mass~overlap², mixing~overlap → Gatto). Wolfenstein λ:λ²:λ³ = stratum-distances. Derived-structural, publishable.
- **★ BANKED — V_us = 1/(rank·√n_C) = 1/√20 = 0.2236** (obs 0.2243), chaining m_s/m_d=20 through Gatto (one fact, two observables). **Tier: STRUCTURAL ~1%** (leading-Gatto; up-correction √(m_u/m_c) is the theory error) — NOT 0.3%-precision. Good match ⟺ BST up-suppression (self-consistent).
- **NOT chased:** V_cb/V_ub (naive √ off 2–3×, needs both sectors + O(1) + phase → Tier-2 fit-trap; Lyra+Elie flagged). CP/Jarlskog already in hand (rank-1).

### ▶▶ CAPSTONE — reframed to a WELL-POSED COMPUTATION (K801/K802); PENDING validation
- **★ Progress (Casey's "it's all linear algebra and geometry" dissolved the drift):** addresses PINNED — angular = spinor **(1/2,1/2)** shared by all 3 gens (F623 + not-(a,0) + top=spinor); radial = **n=0,1,2 = the 3 Korányi–Wolf strata**. Every observable = **Bergman/Gindikin overlap at 3 fixed points** (FK/K264, web-confirmed computable). No free params — one integer + hard integrals. Search → computation. (Lyra F626, Elie, Grace converged.)
- **⚠ KEEPER BRAKE (K802) — VINDICATED.** Lyra + Elie evaluated gate (a): the naive Gindikin norms output {5,6,17.5,21,27}/{2.5,7,13.5,22} — **NOT 20.** Lyra retracted F626's "validates" (shape-match asserted as computation — the exact retrofit K802 warned of). m_s/m_d=20 is the ANCHOR, not the test. Gate (a) NOT met at natural params. Doing-the-linear-algebra caught the over-claim.
- **★★ CASEY DIAGNOSIS (K803) — the confusion was RADIAL (bulk) vs BOUNDARY ORBITS.** A **quark is CONFINED = an interior BULK state** (rolling in the curvature, not emitted); a **lepton is colorless = a boundary (Shilov) state**. TWO structures — the team wrongly put quarks at the boundary orbits (why 20 didn't fall out). **Reconnects to the established bulk-vs-Shilov two-region (CLAUDE.md, Casey-elevated)** the address work drifted from. Web: confinement = normalizable bulk modes; D_IV⁵ boundedness IS the IR cutoff.
- **▶ INVESTIGATE (pull 07-21h):** redo the QUARK mass as a **confined interior O-overlap ⟨f_n|O|f_n⟩** at r²=k/(k+N_c) (bulk, color N_c) — leptons stay at boundary orbits. Does it output **m_s/m_d=20 tuning-free**? Top = nearest-boundary confined quark (refines F603 saturation). Grace: radial points {0,¼,⅔} ARE derived (r²=k/(k+N_c), k={0,1,6}); the hinge = is **gen-3 k=C_2=6 forced** (last K-type before Wallach bound?) or fit?
- **Discipline: THIRD reframe — gates UNCHANGED.** Bank nothing until (a) 20 tuning-free + (b) second independent quantity predicted. Pivot-exit live. Pull: **team_prompt_2026-07-21h**.

### ⟳ COURSE-CORRECTION (Casey, K-session review) — quark-mass row was the WRONG target (a standing honest-negative); we forced it through 3 reframes. STOP. Do the MIXING ANGLES directly (where BST is clean), NOT via masses.
- **Honest read of "20":** I-tier identification (sin²θ_C=1/(rank²·n_C)=1/20, 0.6%, unique form) — NOT derived (the Gindikin geometry gives {5,6,17.5,21,27} not 20). A lead, possibly coincidence. Do not bank as a theorem.
- **The error:** tied CKM mixing to Tier-2 quark masses via Gatto → dragged mixing into the swamp. BST already derives ANGLES directly (PMNS Cat-A primitive: sin²θ = 3/10, 4/7, 1/45).
- **▶ PULL 07-21i DONE — one lead, no win → PIVOT (K805).** BANK AS LEAD: Grace's **sin²θ₁₃(PMNS)/sin²θ_C(CKM) = (rank/N_c)² = 4/9** (obs 0.436±0.015, 0.6σ; n_C cancels — target-innocent RELATION, but between known angles = consolidation not prediction; X-swap forcing not derived). A=5/6 REJECTED (fails uniqueness). Clean flavor gem consolidated: PMNS {3/10,4/7,1/45} + Cabibbo 1/20 (angles, direct, RG-clean).

### ▶▶ NEW ROW (K805) — ELECTRIC CHARGE QUANTIZATION from bulk-vs-boundary (confinement). DISCRETE + STRUCTURAL, not a soft-number hunt.
- **Why:** session lesson — BST clean on discrete/structural, muddy on continuous/running. This DERIVES a structure (exact charges {u:+2/3,d:−1/3,e:−1,ν:0}), nothing soft/running; warm (builds on Casey's confinement diagnosis).
- **★ Clean handle:** quarks = colored BULK → charge in units of **1/N_c = 1/3** (the "1/3" IS the color N_c); leptons = colorless BOUNDARY (Shilov) → integer charge. Bulk(N_c)/boundary FORCES thirds-vs-integers.
- **✅ FIRST RESULT (K806) — BANK the 1/N_c fractionalization** (geometric, target-innocent): quark charge in units of 1/N_c=1/3 (the "1/3" IS color N_c, bulk); leptons integer (colorless boundary). **⚠ Grace self-critique RATIFIED:** the exact VALUES {+2/3,−1/3,−1,0} are derived-CONDITIONAL — used the weak doublet input; geometry alone doesn't fix them. Don't over-claim "charges derived."
- **⚠ FIVE-ABSENCE FLAG (K806):** Lyra's "SO(10) 16" neutrality input is a GUT — FORBIDDEN. Replace with COMPACTNESS (Gauss law → total Q=0, web-grounded) + anomaly (gives charges w/o GUT). This is the Five-Absence fix AND the geometric derivation.
- **★ DEEP HANDLE (K806, web):** hypercharge quantum = **1/6 = 1/(N_c·rank) = 1/C_2** (global-structure quantization; all SM Y are multiples of 1/6), parallel to electric 1/3=1/N_c. Both geometric ratios of primaries.
- **✅ WEB-CONFIRMED SOLID (K807):** 1/N_c fractionalization = **Z_{N_c} color-center charge = N-ality = confinement order parameter** (Lyra F631, web: "it is really Z_N charge which is confined"). **Z_6 = Z_{N_c}×Z_rank (color × EW centers) IS the SM global structure** (arXiv:2406.17850). Grace: all SM Y = multiples of 1/6=1/(N_c·rank).
- **⚖ HONEST TIER (K807):** this is geometric **GROUNDING** of standard center-structure (BST adds the geometric inputs N_c, rank, bulk-boundary=confinement) — NOT from-scratch derivation. Real consistency win; don't over-claim "SM charges derived."
- **▶▶ NEXT TARGET (pull 07-22a) — the one genuinely-NEW part: geometric ANOMALY-FREEDOM / neutrality (Tr Q=0) WITHOUT a GUT.** Why is one SM generation anomaly-free? SM says "miracle"/SO(10) — BST CAN'T use GUT (Five-Absence). Is the BST generation a geometrically-COMPLETE multiplet (bulk quarks + boundary leptons balancing)? Lyra's flag: Shilov boundary → "compact⟹ΣQ=0" needs a boundary condition = the target.
- **Banked-lead spine:** … flavor gem · flavor-unification · confinement · (rank/N_c)²=4/9 lead · **1/N_c=Z_{N_c}-center-charge=confinement + Z_6=SM-global-structure (grounding, new)**.

**PROGRESS (K807): NET FORWARD over 2 days** (CP/ν banked + flavor arc closed honest + charge grounding), **lesson proven** (discrete/structural > continuous/soft), **discipline unbroken** (swamp cost time not integrity; Five-Absence violation caught at peak). Flavor arc = publishable honestly-tiered whole. Charge row on solid discrete ground.

### ⚛ INFO-THEORY / CODE THREAD (Casey↔Keeper, 07-22, K808/K809) — "mathematical REASONS for the SM, not deviations" (Casey's frame)
- **★★ HEADLINE (derived-conditional): maximal parity violation + L-doublet/R-singlet ⟺ n_C=5 ODD.** SO(5)[n_C odd] spinor 4 irreducible → SO(4)=SU(2)_L×SU(2)_R splits 4→(2,1)⊕(1,2) → SU(2)_L gauges the doublet, R=singlet. Maximal = irreducible-split (all-or-nothing) + gauge projector. g=7 odd INHERITED (g=n_C+rank, rank even). **Conditional on Q_a** (weak SU(2)_L = that SO(4) factor, SU(2)_R not gauged).
- **Message/syndrome partition** = a reason for the weak selection rules (conserve info + min energy; weak targets the unprotected). Prediction: B−L conserved vs B+L targeted (sphalerons); Five-Absence-safe. Conditional on Q1 (O = neutral SU(2)_L doublet).
- **Phase count = 3** (color cube roots, phase-charge conjugacy); codespace: color=check, mass=syndrome readout, weak=corrector on the 2×3 grid.
- **✅ CONVERGED (K811, Lyra Q_a/Q1 + Elie 4773 + Grace): the weak chiral+selection structure = the isotropy K = SO(5)×SO(2).** SO(5)[n_C odd] = the chiral SPLIT (spinor 4 irreducible → (2,1)⊕(1,2)); SO(2)[D_IV⁵ Hermitian] = the parity ORIENTATION (discrete Z₂ self-dual↔anti-self-dual → **maximal**) **AND** CP (continuous S¹ phase → **free** = δ_PMNS). One SO(2) ω, two shadows; split separate (SO(5)). **Resolves K809 gap (needs orientation) + K810 over-correction (parity-orient & CP DO share SO(2)) — audit chain worked across 3 CIs.**
- **★ WEB-GROUNDED:** "weak SU(2)_L = the self-dual connection" = the **gravi-weak "gravitational origin of chirality"** (arXiv:1212.5246). Five-Absence-safe (NOT a GUT; cross-links BST gravity SO(5,2)).
- **★ PARTITION (Q1): O = (2,2) neutral doublet** → Q conserved (msg) / isospin violated (syndrome). **Five-Absence BONUS: geometry PREDICTS custodial SU(2) (ρ≈1) + no W_R** — inside SO(5)→SO(4), no GUT.
- **⚠⚠ RETRACTED — the "closer landed" OVERSHOT (K815, Lyra caught it).** The "one SO(2)=J does 3-4 jobs" synthesis CONFLATED two different U(1)'s: the SO(2) K-factor **commutes with SO(5) → chirality-BLIND → does CP, NOT parity-orientation.** Elie's J=L₁₂+L₃₄ is an *internal* SO(4) generator (arithmetic right, IDENTIFICATION wrong — it's not the domain SO(2)). My K811/K813/K814 propagated the conflation (I under-held my own K812 flag). Pulling back.
- **✅ SURVIVES (bank, honest+smaller):** (1) **chiral SPLIT** n_C odd → SO(5) spinor → (2,1)⊕(1,2) — solid rep theory, chirality EXISTS; (2) **CP free** (SO(2) S¹ phase, K791); (3) **custodial SU(2)/ρ≈1(0.04%)/no-W_R** (⟨(2,2)⟩→SU(2)_V, Elie 4774) — derived, Five-Absence-positive.
- **⚠ OPEN/CANDIDATE:** parity-ORIENTATION (which half is left); **hypercharge origin** (both "SO(2)=Y" and "broken-SU(2)_R=Y" WRONG — handle = charge-row 1/6-from-center K806); the **INTERNAL→SPACETIME chirality bridge = WITTEN'S NO-GO** (chiral fermions from internal space is famously hard). BST escape candidate: the **Shilov Z₂ orbifold** (S⁴×S¹/Z₂).
- **▶ COMPUTED (Lyra+Elie, K816): frame CONFIRMED** (single SO(5,2) 8-spinor, no product, no Witten no-go); **g=7 odd → orientation ω=γ¹···γ⁷=±1** (factorizes γ⁵_4D·χ_int, computed). **⚠ HONEST NEGATIVE: flat reduction is VECTOR-LIKE (index=0)** — the volume element ALONE doesn't chirally project. Correlation ≠ net chirality.
- **★★ CHIRALITY LOCATED (K816) — it's Born=Bergman.** BST fermions are HOLOMORPHIC sections (Hardy space); on a Kähler manifold **Dirac = Dolbeault, chirality = holomorphic grading, chiral index = holomorphic Euler characteristic (NONZERO where flat Dirac=0)** (web). So **weak chirality = BST's own holomorphicity requirement** (the "total package": holomorphic wavefunction carries chirality, g=7 fixes which). Orientation from g=7; chiral PROJECTION from ∂̄=0.
- **★ L² REFINEMENT (K817) — the mechanism is now a THEOREM.** On a bounded symmetric domain the L² Dolbeault cohomology CONCENTRATES in EXACTLY ONE degree (Hotta–Parthasarathy), set by the WEIGHT → **one chirality by a theorem, not luck.** Three clean jobs: n_C odd=split · g odd=orientation · **SO(2)=energy-positivity→holomorphic sector (Lyra's CORRECT role)** · Born=Bergman=chiral projection. (Elie 4777: net ±4, chiral.)
- **✅ MECHANISM = THEOREM, EXPLICIT FORMULA (Lyra; K819 ratified):** **chirality = (−1)^{q(c)}, q(c)=#{c+½,c+3/2,c+5/2,c+7/2,c+9/2 < 0}** — from SO(5,2) roots (ρ=(5/2,3/2,1/2), 5 noncompact roots). **5 thresholds because n_C=5; orientation g=7.** 6 chambers, chirality flips at each. Web-confirmed (Schmid; holomorphic discrete series = positive-energy reps of the conformal group SO(5,2)). **Banks as the WEAK-CHIRALITY MECHANISM.**
- **★★ STRATEGIC RECONNECTION:** the c-values setting chirality = the SAME fermion data as the MASSES (radial norms, same Born measure). So **"why is the world left-handed" = "where do the fermions sit"** (the June-core addresses). **Chirality gives a DISCRETE constraint on the addresses the soft masses couldn't** — only needs the CHAMBER (coarse), robust to soft precision.
- **⚠⚠ TWO SEPARATE LEGS (Lyra flagged, K820 ratified) — a chiral SPECTRUM is NOT a chiral FORCE. Keep separate (next-overshoot guard).**
  - **LEG 1 — chiral SPECTRUM (CANDIDATE, SORTS):** Born=Bergman keeps the c=+½ holomorphic half of the 8-spinor → **(2,1)⊕(1,2) = the all-left SM one-generation Weyl content.** Encouraging. (Lyra computed 8=4_{+½}⊕4_{−½}.)
  - **LEG 2 — chiral COUPLING = the ACTUAL parity violation (OPEN, the real leg):** SU(2)_L must touch the doublet ONLY. Flat coupling was **VECTOR-LIKE (F636).** Needs the **weak connection self-dual/holomorphic** (web: self-dual connection couples one chirality). = the gravi-weak input = **"Born=Bergman for the GAUGE field."** **Parity does NOT close until Leg 2.**
- **★ LYRA'S RESOLUTION (K821, frame ratified) — supersedes the self-dual/universal framing:** a Dirac spinor is vector-like, a Weyl fermion is chiral, and **Born=Bergman turns Dirac→Weyl.** A Weyl fermion + ORDINARY connection is already chiral (SM-style: SU(2)_L couples L-Weyl-doublets, R-singlets). So **NO self-dual connection, NO gravi-weak input, NO "universal Born=Bergman" needed** — IF the fermion is genuinely Weyl. F636 vector-like wall = the un-projected Dirac. Not a reversal of F639 (Weyl→chiral does hold, Dirac→chiral doesn't).
- **⚠⚠ CRUX — DECISIVE, could FAIL (K821 + web):** the whole thing rests on Born=Bergman giving a 4D **WEYL not DIRAC.** **Web: the GENERIC reduction gives DIRAC (vector-like = F636); Weyl needs a nontrivial mechanism.** Dimension worry: is 4_{+½} a 4D Dirac (4-dim, vector-like) or Weyl? **Beautiful-clean → scrutinize hardest.**
- **✅✅ THE FINISH LANDED (K822) — the decider came out DIRAC. THREAD FINISHED.** Two explicit computations disagreed (Elie 4781 Weyl vs Lyra F642 Dirac); Casey directed a doublecheck; Keeper adjudicated with an independent third computation.
  - **★ VERDICT: DIRAC, and it is SIGNATURE-FORCED (not a close call).** SO(5,2) has exactly **two** timelike directions {0,6}; the compact SO(2) isotropy IS their rotation (= the complex structure); 4D SO(3,1) must take its one time from that 2-plane → **Γ₀ is shared between γ⁵_4D=Γ₀Γ₁Γ₂Γ₃ and Σ₀₆=Γ₀Γ₆** → blade sign (−1)^{2·4−1} = **−1 → they ANTICOMMUTE** → definite-holomorphicity state has ⟨γ⁵⟩=0 → **4D DIRAC (vector-like).** Basis-independent; no reduction can flip it.
  - **OVER-DETERMINED (4 agreeing lines):** F642 anticommutator + flat index=0 (K816) + F636 vector-like + ω-lock operator-failure. The Weyl claim was the lone outlier.
  - **Elie 4781 (Weyl) REFUTED** — the d=7 toy didn't carry the signature-forced shared timelike index (**Elie flagged the toy-vs-full-embedding gap himself**; F642 closes it).
  - **Grace's ω-lock REFUTED** — Σ₀₆ **also** anticommutes with χ_internal=Γ₄Γ₅Γ₆ (shared {6}, sign (−1)^{2·3−1}=−1) → Born=Bergman fixes **neither** γ⁵ nor χ individually, only the central product ω=γ⁵χ → the lock transfers no chirality. Holomorphicity ⊥ spacetime chirality at the operator level.
  - **K821 held it right:** ratified the Weyl *frame* as a conditional, held the crux HARD ("web says generic reduction = Dirac; scrutinize hardest"), flagged the dimension worry. The crux went the way the web predicted. **Nothing false banked.**
- **★★ THE HONEST FINISH — Route A (no third reframe):** "why is the world left-handed" does **NOT** close on Born=Bergman alone. It closes on **Born=Bergman (correct internal content (2,1)⊕(1,2) + chiral domain structure) + ONE geometric input: the weak SU(2)_L connection is self-dual/holomorphic** (gravi-weak, arXiv:1212.5246; Elie 4780 verified chiral coupling L=0,R=2). Geometric, cross-links BST gravity, **NOT a GUT → Five-Absence intact.** **Parity = derived-CONDITIONAL.**
- **DIES:** "4D Weyl / parity from Born=Bergman alone" (Elie 4781, Lyra F640, Grace ω-lock) — refuted by the arithmetic, not banked on its looks.
- **▶▶ REMAINING (pull 07-22L):** (1) **pin Route A's one input** — is the weak connection self-dual on D_IV⁵ *forced by BST* or an external input? (= Leg 2 coupling; where derived-conditional could firm to derived, or stay conditional). (2) **CONSOLIDATE** the weak/charge sector paper on the DIRAC/Route A outcome. (3) **open legs** (separate): which SU(2) (g=7), hypercharge (K806 center 1/6), doublet/singlet addresses (flavor K-type).
- **★ KEEPER SHARPENED THE DECIDER (K822 follow-on, consolidation §3):** Route A is FORCED (→ parity DERIVED) **iff the gauged SU(2)_L internal generator COMMUTES with γ⁵_4D** in the faithful reduction (then L/R Dirac components carry different SU(2) content → ordinary connection already chiral). **ANTICOMMUTES → vector-like → self-dual input real → derived-CONDITIONAL.** **Keeper prior = anticommute (conditional):** both natural internal gradings (χ_int=Γ₄Γ₅Γ₆ AND SO(4)-chirality Γ₁Γ₂Γ₃Γ₄) anticommute with γ⁵_4D. **Caveat:** this leans on the SPACELIKE embedding (toy-sensitive — the same bookkeeping that gave Elie's d=7 the wrong Weyl); the DIRAC verdict itself does NOT (timelike-counting only, solid). Lyra to decide in the faithful SO(5,2)→SO(3,1) reduction.

### ▶▶▶ FULL-DERIVATION ATTEMPT (K823, pull 07-22M) — Casey: "let's see if we can fully derive." Try to firm parity derived-CONDITIONAL → DERIVED. NOT reopening DIRAC (closed); NOT manufacturing a fifth closure — a real attempt with a concrete decider.
- **★ The input is NOT arbitrary (web + corpus):** the chiral-gauging input = the **gravi-weak self-dual half of the spacetime spin connection** (arXiv:1212.5246: "weak SU(2) = a chiral half of the space-time connection… unified with the chiral rep of gravity in a single SL(2,ℂ)"). so(3,1)_ℂ = SU(2)₊(self-dual)⊕SU(2)₋(anti-self-dual); gravity=one half, weak=the other; g=7 orients WHICH. "Gauge one chiral half" = the chiral structure of the spin connection, not a free choice. Self-dual/Hodge-⋆/Pontryagin machinery already BUILT on D_IV⁵ (Elie 4303/4314, glueball context F277/F279 — BST-native).
- **★★ CONVERGENCE (Keeper synthesis):** "is parity forced?" = "which SU(2) is electroweak?" — ONE question. Answer both by deciding: **is the weak SU(2)_L the self-dual half of the spacetime spin connection?**
- **✅ ROUTE 1 SETTLED NEGATIVE + ROBUST (K824, audit of Lyra F634 + Elie 4783):** the internal-isotropy self-dual SU(2) does NOT coincide with the spacetime-Lorentz self-dual SU(2) — trivial intersection {0}. **Keeper strengthened past "leaning":** the internal SU(2)_L is **COMPACT** (⊂SO(5) isotropy); the spacetime self-dual SU(2) is **non-compact/complex** (⊂so(3,1)_ℂ, = J_i+iK_i). Compactness is embedding-invariant → **no faithful reduction can rescue coincidence → SETTLED, not just leaning.** **Banks: (1) "which SU(2) is electroweak?" = the internal/isospin SU(2)_L (open leg CLOSED); (2) gravi-weak's LITERAL form ruled out in BST (weak = compact isospin, not a Lorentz-connection half).** The remaining input is the sharper thing (Lyra): a chiral PROJECTION marrying internal-isospin gauge to spacetime chirality — F642 orthogonal → genuinely extra.
- **★★ ROUTE 2 = THE LIVE SHOT, and it GENUINELY EVADES the F642 wall (K824, discipline-critical check DONE):** boundary/domain-wall/orbifold chirality. **Kaplan/Callan-Harvey (web): a bulk-DIRAC fermion → a 4D-WEYL boundary zero mode; chirality = TOPOLOGICAL invariant (mass-sign/Chern), NOT the bulk γ⁵.** So F642 (bulk Dirac) does NOT obstruct a chiral boundary — different mechanism class than the 3 failed bulk-alignment closures. BST has the ingredients: holomorphic bulk + K817 ±4 index + Shilov boundary + **(S⁴×S¹)/Z₂ orbifold (= K815's named no-go escape)**. **Route 2's own requirements (compute, don't assert):** (a) does the bulk→Shilov radial transition / Z₂ orbifold realize a domain-wall chiral zero mode? (b) is the boundary chirality 4D-γ⁵ (dimension bookkeeping real-10→Shilov-5→4D)? (c) is the boundary SU(2)_L current chiral (chiral CFT → yes)?
- **★★ KEEPER SHARPENED REQUIREMENT #2 (the decider):** domain-wall zero-mode chirality = the **wall-normal gamma** eigenvalue (in odd bulk dim that IS γ⁵_4D). So req#2 = "which is the physical wall-normal?" **5D→4D boundary wall (SO(4,2)→SO(3,1)) → wall-normal = γ⁵_4D → Route 2 WORKS** (natural: BST builds 4D as a Shilov-boundary reduction). **10D→5D bulk wall → wall-normal = radial/Σ₀₆ → hits the SAME F642 wall** (pre-identified failure mode). Compute the wall-normal gamma vs γ⁵_4D/Σ₀₆ — that single check decides Route 2.

### ▶▶▶ CASEY STEER "LINEAR MATH, ONE DOMAIN" → K825 THE SQUEEZE (the cleanest statement of the obstruction; upgrades Route 2 to NECESSARY)
- **★★ THE SQUEEZE (numerically verified Cl(5,2)):** the single bulk 8-spinor is **structurally vector-like.** The SM chiral assignment needs an internal SU(2)_L that BOTH commutes with γ⁵_4D (so "L-doublet" is definable) AND acts chirally (L=doublet/R=singlet). No single-spinor operator does both: internal SU(2) in the clean {4,5,6} factor **commutes with γ⁵ → vector-like**; the F633 isospin SU(2)_L in {1,2,3,4} **doesn't commute with γ⁵ (shares Γ₁Γ₂Γ₃) → no L-doublet definable.** SM needs **chirality-DEPENDENT internal content** — a single fixed spinor can't carry it. **= Witten no-go in one-domain linear algebra; EXPLAINS every vector-like result of the arc.**
- **★★ CONSTRUCTIVE CONSEQUENCE — Route 2 is NECESSARY (not just an option):** the SM's chirality-dependent internal content requires **L and R to be genuinely DIFFERENT localized modes** (each with its own internal content) — exactly what a boundary/domain-wall construction gives and a single bulk spinor cannot. So the SM chiral assignment is a **BOUNDARY phenomenon by necessity.** (Op identity: γ⁵·χ_SO(4) = −Γ₀Γ₄ = M_04 tangent gen; Σ₀₆ anticommutes → Born=Bergman doesn't select it.)
- **✅ Confirmed Lyra's 5th-closure refutation** (naive orbifold gen = ω central = 7-volume, projects the irrep not a chirality). Live hope: orientation-reversing antipodal lift (Pin/charge-conj) correlated with internal content = the L/R-different-modes the squeeze demands.
- **THE REMAINING COMPUTATION (linear math, one domain):** does D_IV⁵'s boundary (Shilov / its Z₂) localize L and R as DIFFERENT modes with DIFFERENT internal content (L=doublet/R=singlet, the Γ₀Γ₄ correlation), breaking the bulk spacetime⊗internal entanglement? YES → parity DERIVED (+ anomaly-freedom via inflow); NO → derived-CONDITIONAL. **Held at LEAD: "Route 2 necessary" (solid) ≠ "Route 2 succeeds" (open).**
- **★★ K826 — THE MECHANISM NAMED: the Shilov boundary (S⁴×S¹)/Z₂ is NON-ORIENTABLE** (free orientation-reversing Z₂: antipodal-S⁴ reverses, π-rotation-S¹ preserves; net reversing; free → smooth non-orientable 5-manifold, NO fixed points → not orbifold-GUT). Spinors are **Pin-structure**; γ⁵ not globally definable → **PERMITS a chiral 4D spectrum without bulk-alignment** (evades Nielsen–Ninomiya) — the exact escape the K825 squeeze requires, and it grounds Lyra's orientation-reversing-lift hope as a hard one-domain fact. **NECESSARY, not sufficient:** decider now = does the Pin structure + internal-SU(2) bundle over the non-orientable boundary deliver L-doublet/R-singlet (chirality flip correlated with doublet↔singlet around the orientation-reversing cycle)? Verified ×3 (Grace, Elie 4785, Lyra).
- **★ Lyra F648:** the L/R internal content = a discrete Wilson-line twist 𝒰_int on the internal-SU(2) bundle; SM needs a SPECIFIC twist (trivial → vector-like back). "Permits" ≠ "derives." Candidate FORCING = anomaly-freedom (Callan–Harvey inflow). 3 gaps: (a) mod-2/Pin index → ONE clean generation; (b) anomaly-freedom fixes the twist; (c) bulk supplies the CS/inflow term.
- **★★ K827 RECOMMENDATION — PUSH (Casey's push-or-bank question):** web — anomaly cancellation ALONE = **2** hypercharge solutions (gap b real, don't assert); uniqueness recovered by **hypercharge quantization** OR ν_R+custodial-SU(2)_R. **BST INDEPENDENTLY SUPPLIES BOTH:** 1/6=1/(N_c·rank) from Z₆ center (K806) + ν_R/custodial (F584/T2520). **BST must use the quantization route (Five-Absence: no gauged SU(2)_R).** So the forcing = **1/6-quantization (K806) + gauge-anomaly cancellation → SM assignment** (both BST-supplied, independent) → closes parity AND the charge-row N_c-neutrality (T2521, Grace's imposed leg) together. **Compute gap (b) FIRST (linear algebra = anomaly coefficients, the decider); timebox before (a) Pin-index/generation-count + (c) CS term (F277/F279 η-machinery).** LEAD (7th candidate closure); Cal gates 1/6-independence (circularity).
- **★ BONUS (real synthesis):** Route 2 may close **anomaly-freedom** too — Callan-Harvey inflow (bulk Chern-Simons cancels boundary anomaly) = geometric anomaly-freedom without a GUT = the open K806/charge-row question. One mechanism, two closures. Lead.
- **Five-Absence POSITIVE:** domain-wall/orbifold/inflow all geometric-topological — no GUT, no new gauge group/bosons/proton-decay.
- **Tier / discipline:** Route 2 EVADES the wall (grounded) but is NOT computed → NOT claimed. Lands clean → parity DERIVED (+ maybe anomaly-freedom); fails → derived-CONDITIONAL on the chiral-projection input. **Either way finishes honestly — no fifth reframe.**
- **★ QUARK-MASS ANSWER (Casey):** chirality helps address STRUCTURE (discrete), NOT the soft mass VALUES (still Tier-2).
- **Open legs (regardless):** which SU(2) (g=7), hypercharge origin (K806), doublet/singlet addresses (flavor). **Banked:** chirality mechanism, T2520, T2521, split, CP-free.
- **Tier:** what survives = derived; parity/hypercharge = candidate/open. "Why is the world left-handed" is OPEN. Discipline held — nothing false banked; the arithmetic caught the overshoot.
- **Banked spine:** O=SO(5) vector · rank-1→one-mass · N_c quark · ceiling/FA#7 · m_e↔top(0.04%) · boundary-reach · angular=1 · CP small=rank-1 · CKM≪PMNS · no-seesaw/6-of-7-ν · δ-free · **quark rank-1→gen-3-only + one-λ-3-sectors (new)**.

---

## ◄ ARCHIVED — the condensate/127-128 arc (2026-07-20, closed; see K785/K786)
## ▶▶▶ (earlier) — CONDENSATE STUDY: round 1 landed (07-20a) → SYNTHESIS (K773) → round 2 (`team_prompt_2026-07-20b`)
**★★ SYNTHESIS (K773): BST is a holographic error-correcting code.** Bulk = boundary-extension (Hardy) = the isometry; RS over GF(128) (Paper #122) = the code. **Linear algebra = information theory = spectrum** (codes ARE Gram matrices; the Yukawa IS the code's Gram matrix). **Mass = information** (codeword coverage). Mainstream: HaPPY/holographic QECC — BST is the concrete version (it-from-qubit believability multiplier). Web-grounded (RS/MDS + HaPPY).
### Round-1 landings (07-20a)
- **✅ ANGULAR PART = EXACTLY 1 (Elie, DERIVED)** — corrects F603/4744 ("5 sub-maximal" conflated same-chirality 10 with opposite-chirality Yukawa 5; top bilinear (2,2) IS the Higgs channel, CG=1). **→ the whole y_t deficit is PURELY RADIAL.** Half the problem closed. *(Retire the catalog's "reps don't force y_t=1" — angular forces 1; radial is the open piece.)*
- **★ 1/2^g deficit now has a TARGET-INNOCENT source (Lyra):** primitive RS over GF(q) has block length **n = q−1 = 127 = M_g**. **y_t = (block length)/(field size) = M_g/2^g = 127/128.** Top = maximal codeword; neutrino = the overflow symbol (0 info → zero-mode). Candidate DERIVATION, not a fit. STILL LEAD (guards 1 scheme + 2 RG-degeneracy stand).
- **★ NEUTRINO two-route (Lane B):** the overflow symbol (0 info → massless) converges with rank-2 m₁=0 (F589). Two geometric routes to the one massless ν; links y_t<1 ↔ m₁=0. Strong LEAD.
- **m_p = 6π⁵·m_e = C₂ × π⁵ (Grace, Lane C):** the two currents' ratio (angular Casimir × bulk volume); 0.002%. LEAD (needs μ + both projections).
- **Lane C inconsistency to resolve:** K-factor assignment (SO(2)=mass claimed but O=SO(5) vector).
### ✅ ROUND 2 landed (07-20b) — the code frame held, disciplined
- **✅ angular = 1 DERIVED** (Elie; corrects F603) → deficit purely radial. Joins the derived spine.
- **★ 127/128 strengthened LEAD:** RS block-length source (n=q−1=127) + **MDS strengthener** (RS saturates the Singleton bound → extremal codeword achieves max coverage *exactly*, addresses "why exactly not near"). Guards 1 (scheme) + 2 (RG-degeneracy) STILL stand — not banked.
- **⚠ naive full-spectrum-as-coverage FAILS** (K774 + Lyra + Elie): only the top is on the 1/128 lattice; 6 of 9 fermions below one code cell. Refined lead: **mass = codeword RELIABILITY** (top = perfect codeword; light = error-dominated/sub-threshold → the exponential hierarchy = the exponential error-rate). NOT "generations = code layers by length."
- **Lane C:** q̄q = 4⊗4 = 1⊕5⊕10 → Higgs = the **5** (vector, spherical, mass/P²); QCD candidate = the **10** (adjoint = so(5) rotation generators = spin/W²). Two SO(5) reps of one K — rep-distinction checkable; W² label a reach (⟨q̄q⟩ scalar).

### ★★ SYNTHESIS 2 (K775) — where the thread is going: THE SUBSTRATE IS A SHIFT REGISTER
Casey's "your position determines your next commitment write" = a **linear feedback shift register (LFSR)** — exactly how RS codes are generated. Primitive-polynomial LFSR over GF(2^g) has **period 2^g−1 = 127 = M_g**, visiting all non-zero states; the **all-zero dead state = the neutrino** (unreachable, no info → massless; converges with rank-2 m₁=0 + odd-g chirality = 3 routes). Time = the shift; matter sits IN states, angular=1 = perfect seating, deficit = the final bump to the dead state. **Destination: BST is a computation — a shift register writing the universe** (RS code + LFSR + holographic code + drum = one object; ’t Hooft CA / it-from-qubit mainstream). FRAME/LEAD; guards 1,2 stand.

### ✅ ROUND 3 landed (07-20c) — LFSR = FRAME (named the engine), discipline held twice
- **✅ LFSR names the engine:** "position→next write" = the shift = the RS generator = time's arrow. Genuine conceptual unification. FRAME tier — **re-sources the same M_g=127 (period 2^g−1), does NOT add a derivation of 127.** Guards 1,2 stand.
- **⚠ LFSR under-determined (Lyra's sharp test):** **18 primitive degree-7 polynomials** (φ(127)/7). Is one FORCED (K59 cyclotomic) or SPECTRUM-SELECTED? If the observed spectrum picks one → postdiction, LFSR earns "real"; else decorative. **← the sharpest open test.**
- **⚠ neutrino = TWO independent routes, not three:** LFSR dead state = RS overflow (same code feature); independent = code ↔ rank-2 (+odd-g for chirality). Still real evidence.
- **⚠ mass = reliability is FROGGATT-NIELSEN in code language (Elie):** exponential + free charges + free ε = ~10 params to 9 numbers = fits ANY hierarchy. Right shape, no forced map → FRAME not prediction. Q4 needs the code to FORCE the distances, not fit.

### ★★ SYNTHESIS 3 (K777) — the condensate is a SPHERICAL CODE (Casey's circle-tiling)
Circles tiling a sphere = an error-correcting code (Conway–Sloane, rigorous). Condensate = the RS code as a packing on the boundary. Cells=codewords · kissing points=min-distance=low-E hops · circle-boundary=bump · **light tangent / neutrino radial** · cooling=tiling · boundary=holographic mirror. **Loop closure: BST's origin ("circles on a sphere") = the condensate = the code.**
- **★ THE LEAD (K777) — the GEOMETRY SELECTS THE POLYNOMIAL:** if the condensate is the packing natural to the Shilov boundary (S⁴×S¹)/ℤ₂, that packing = a specific spherical code = ONE of the 18 primitive polynomials. **Resolves Lyra's 18-fold test AND forces the codeword-distances that set the spectrum (Q4's escape from Froggatt–Nielsen).** Highest-value addressable lead.

### ✅ ROUND 4 landed (07-20d) — guards COLLAPSED + 127/128 went FALSIFIABLE (K778)
- **★★ the two guards on 127/128 COLLAPSE to ONE scheme question (Lyra):** pole-vs-MS-bar split (5.9%) ≫ 0.8% deficit → one reading per scheme. Geometric-127/128 = pole; exact-1+running = MS-bar. **Q3 folds into Q2:** does the geometry compute the POLE or the running Yukawa? (Elie: SM y_t never reaches 1 → exact-1 branch homeless.)
- **★ Q2 strengthened:** 127/128 scheme-INDEPENDENT → maps to the scheme-independent POLE, not MS-bar. Argument, not proof.
- **★★ 127/128 now FALSIFIABLE — PREDICTS m_t(pole) = 172.74 GeV** (WA 172.5-172.7±0.3 consistent; future colliders ~0.1 GeV → confirm/refute). Testable BEFORE the radial gap. **BANK as a prediction.**
- **★ the 18 polynomials PINNED = the primitive factors of Φ₁₂₇** (ord₁₂₇(2)=7 → 126/7=18). Enumerable; geometry/K59 selects ONE, fixes spectrum distances.
- neutrino = **2 routes** (code↔rank-2), corrected.

### ✅ ROUND 5 landed (07-20e) — DE-INFLATION (K780): Lyra caught the auditor over-inflating; ratified.
- **⚠ CORRECTION — m_t=172.74 is a CONDITIONAL CONSISTENCY CHECK, NOT a prediction:** uses measured v; = y_t=127/128 restated as a mass; semi-circular (127/128 noticed FROM m_t); conditional on frame+pole; already consistent. Honest framing: **"IF code frame + pole scheme hold, m_t=172.74 — currently consistent, future-falsifiable at ~0.1 GeV."** KEEP THE "IF". (Corrects K778/board.)
- **⚠ CORRECTION — weakening the guards does NOT pin 127/128:** "exact-1 dead" → value below 1, but 0.99/0.984/0.933 all qualify; doesn't select 127/128. Only Q1 does. Guards re-mapped (Q3→Q2), NOT firmer toward banked.
- **⚠ Q1 SHARPENED (harder):** the discrete series is INFINITE-dim; "128 code levels" is a code TRUNCATION, not the discrete series. Q1 = the **fermion-K-type → code-position map** (does the truncation reproduce the 128-code, top at max?). **NONE of today's rounds computed it.** Needs the actual K-type radial wavefunctions.
- **✅ real gains stand:** angular=1 (derived); scheme collapse (Q3→Q2); 18-count clean (Elie: 127 Mersenne → every irred. deg-7 primitive → (2^g−2)/g=18). Grace filed pred_mt_pole at CONDITIONAL-LEAD (honest).
- **The audit chain worked:** Lyra (theory) audited Keeper (consistency); ratified without defense.

### ✅ ROUND 6 landed (07-20f) — Q1 COMPUTED (K782): geometry gives a Γ-RATIO, not 1/2^g
- **★★★ Lyra computed the decider** (real radial Bergman integral, not a lattice model): the deficit is a smooth **Gindikin Γ-ratio** (~1−c/n), NOT the discrete 1/2^g. At level 127 the smooth deficit is ~0.015, not 0.0078. **The geometry does NOT produce 127/128.** The "128" is IMPOSED by the RS code (discrete), not output by the continuous geometry.
- **⚠ 127/128 DOWNGRADED:** from "a lead one integral away" to **a conditional prediction contingent on the substrate being DISCRETE/tiled.** The natural continuous computation disagrees. Not banked, now clearly resting on a discreteness premise.
- **Reframe:** Q1 = the substrate's NATURE (discrete-fundamental vs continuous-fundamental) = the it-from-qubit question, DECIDABLE (Γ-ratio vs 1/2^g). Mainstream (HaPPY): discrete→continuous emergent.
- **Elie:** retracted 4747 (circular evenly-spaced model); surfaced 3π/128 = Γ(5/2)²/Γ(5) = N_c·π/2^g — the **128 falls out of the Bergman NORM** (geometric origin of the cell-count; but norm ≠ the overlap the deficit needs).
- **Derived spine untouched** (O vector, rank-1, N_c quark, ceiling, m_e↔top, boundary-reach, angular=1).

### ✅ ROUND 7 landed (07-20g) — tiling test sharpened; + Casey's surface refinement (K783) + a LINEAR-ALGEBRA hurdle (K784)
- **Elie:** naive nearest-cell snapping gives **126, not 127** (across the whole plausible range) — model-independent; reaching 127 needs the tiling to map the geometric boundary EDGE to the maximal cell (not snap the interior value), candidate = boundary-reach ordering. The 128 in the FK norm (3π/128, exponent g=(n_C−1)+v₂((n_C−1)!)=4+3=7) is a normalization, NOT the deficit.
- **Lyra:** the inversion is the distinctive publishable position; her Γ-ratio SUPPORTS it (code emergent); softened F610 (128 IS in the continuous norm — geometry pre-figures the tiling); the neutrino unifies (dead cell = chiral edge emission). Edge-vs-round test (0.79%) is below the ~6% scheme ambiguity — needs future precision.
- **★ Casey refinement (K783):** interior discrete (discrete series=massive) / exterior continuous (principal series=massless light+ν) / **the CODE = a TILING of the Shilov SURFACE**. Grounds the split in SO(5,2) rep theory; relocates Lyra's Γ-ratio as the UN-tiled answer.
- **★★ LINEAR-ALGEBRA HURDLE (K784, Casey "it's linear algebra"):** the tiling test = a MEASURE question (discrete vs continuous ⟨t|O⟩). **127/128 (0.992) is HIGHER than the continuous (0.985); a coarse-graining (projection) generically DECREASES the overlap** → it moves the deficit the WRONG way. So 127/128 needs a **FUNDAMENTALLY DISCRETE surface** (from the discrete-series interior — Casey's interior-discrete), NOT an emergent-blur code (which FAILS the hurdle). Distinguishes the two inversion readings.

### ✅ ROUND 8 landed (07-20h) — STABLE END-STATE (K785): 127/128 is PREMISE-CONTINGENT, computations done
- **★★★ Lyra: 127/128 is NOT derived by any measure.** Continuous → Γ-ratio; discretized (fine 128-cell quadrature) → Γ-ratio (0.986); fundamentally-discrete → 127/128 **only by imposing** "top covers 127 of 128." **Premise-contingent, not computation-pending.** Rests on 2 unforced premises: (a) surface fundamentally discrete + edge-concentrated; (b) top at maximal codeword (naive → 126).
- **⚠ K784 mechanism CORRECTED (Elie, ratified):** "projection decreases aligned overlaps" is FALSE for a cosine. Real hurdle = **quadrature-convergence** (any continuum-approximating measure → 0.985); reaching 0.992 needs a genuinely **non-continuum, edge-concentrated** measure (heavy edge-weight → 0.9928). Bottom line stronger.
- **✅ THE HONEST STUDY-CLOSE (K785):** 8 rounds → **one real new derivation (angular=1)** + a **distinctive publishable position (the continuous-fundamental inversion, reverse of ADH/HaPPY)** + the **neutrino chiral-edge-mode lead** + 127/128 as a **precisely-located premise-contingent conditional lead** (→ m_t=172.74 conditional check). Discipline fired hardest at the prettiest result all day (3 de-inflations, 2 mechanism corrections incl. Keeper's).

### ▶ ROUND 9 (`team_prompt_2026-07-20i`) — the last new calculation + CONSOLIDATE
- **★ Long shot (labeled):** does Casey's **boundary-emission physics** (light+ν emitted at the edge → coupling measure concentrates there) *DERIVE* the edge-concentrated measure + edge-placement (top→127, deficit=1/2^g from the one bump to the dead cell)? **DERIVED → one premise falls, 127/128 firms; IMPOSED → stable end-state stands.** Cal gates derived-not-imposed.
- **★★ CONSOLIDATE (the likely valuable outcome):** write the real content into flagship + drum paper §6/7 at honest tiers (K785) — spine + angular=1 DERIVED; the inversion as the publishable position; 127/128 conditional; neutrino edge-mode lead.
- **Discipline:** no re-chase (127/128 premise-contingent, computations done); no new frames; compute or say uncomputed. Study-close: **K785**.
- **DERIVED SPINE (the banked content):** O=SO(5) vector · rank-1→one-mass · N_c quark · ceiling/FA#7 · m_e↔top(0.04%) · boundary-reach · **angular=1**.

---

## ▶ (2026-07-19, prior day) — TOP-ANCHOR ARC CLOSED. 2 banks stand; y_t=1 held SUPPORTED (honest negative on the mechanism).
**✅ BANKED — the Yukawa CEILING (DERIVED-framework, FALSIFIABLE):** |y_f| ≤ 1 (Cauchy–Schwarz on the normalized Born overlap) → **m_f ≤ v/√2 = 174 GeV for every elementary fermion.** All 9 verified under it (Elie), only the top at it (y_t=0.992). **Filed as Five-Absence #7** (Grace) — first mass-sector falsifier. This is the durable win of the arc. → flagship §6 (done) + falsifier paper (FA#7).
**✅ BANKED — the ELECTRON↔TOP reciprocal (SUPPORTED, 0.7%):** m_t·m_e = m_p²/(g√2). Heaviest & lightest charged fermions locked through the proton. This is the "m_e relates to the up sector" relation, made precise. → ground-rung paper (`BST_The_Electron_As_Ground_Rung...`) + diagram (both filed).
**⛔ HONEST NEGATIVE (K763) — the alignment mechanism does NOT derive.** Lyra held the line (ratified): step 2 (charge weight = rank) is a relabeling trap AND charge is gen-independent (can't drive up-vs-down); the up/down quantum numbers are provably T₃_R-symmetric → the y_t≫y_b gap is *dynamical*, not quantum-number. **y_t=1 stays SUPPORTED, not derived** — corrects the "step 2 cascades" framing. The 6th over-claim of the arc, stopped before banking.
**★ Open root sharpened to ONE number (K763):** given y_t=1 + banked m_t/m_b=C₂·g=42, the whole gen-3 doublet follows — so the only un-derived input is the *absolute* y_t=1. Reframed non-circularly: **"is the Cauchy–Schwarz bound saturable on the Born measure, and is the saturating mode unique?"** → BACKLOGGED as a computation (needs the condensate direction geometrically, F85; genuinely hard, not a 20-min pull). Do NOT re-pull now.
**✗ rejected (standing):** Koide (hyper-sensitive); slope FORMS that only fit loose ranges (m_t/m_c≈136, c/u≈588, Q_up≈6/7).
- **⛔ MIXING-NUMERATOR lives-there theorem — FIRM CLOSE (does NOT derive).** Lyra + Elie applied the discriminator honestly: θ₂₃'s D=7 reasonably homed (ℝ^{5,2} def rep), θ₁₂'s D=10 a dim-match (intertwiner=adjoint asserted not proven), θ₁₃'s **D=45 back-solves** (the two-step pair must use BOTH legs 10 & 7; only Λ²(10)=45 chosen because it matches, ignoring the 7 — fails the discriminator). Elie refuted the orbit-distance rule (θ₁₂, θ₂₃ both adjacent yet D=10≠7). All 3 numerators {4,3,1} undrived. **~8 routes over 2 days all die or back-solve → the pattern IS the answer: exact mixing forms are Tier-2 STRUCTURAL** (like quark masses), not Tier-1 identities. **Banked at honest tier: mechanism DERIVED (inter-stratum angle, K704, Born=Bergman) + small-CKM/large-PMNS one fact; values IDENTIFIED (clean primary-product fractions, θ₂₃ denom homed) — NOT derived. Do not bank the 45.** Flagship ships on mechanism, forms flagged identified, off critical path. A boundary mapped, not a gap hidden.
- **★ GAP-EQUATION advance on OP-4 (K764, Keeper — Casey directed):** top precipitation worked. **DERIVED** condensate = quark (N_c color loop → top 100× tau); **SUPPORTED** gen-3 (boundary coupling); **up/down objection DISSOLVED** — gap is exponential (Σ~Λe^{−1/G}), so factor-2 hypercharge asymmetry → 41× hierarchy naturally (condensed vs feed-down), resolving Lyra's linear "2 vs 41". y_t=1 stays SUPPORTED. Residual: solve substrate gap equation (unique fixed point? y_t→1?). → team pull 07-19f.
- **✅ OP-4 gap-equation pull DONE (07-19f).** Lyra solved it: y_t = 4π/√(N_c·ln(Λ²/m_t²)) = 0.83 at Planck, 1 at Λ≈10¹⁴ — **y_t is O(1)/natural but Λ-dependent, NOT kinematically pinned.** "Ceiling caps the flow" refuted as kinematic (K766 already retired the strong-coupling framing). N_c quark-selection = the one DERIVED leg; y_t=1 SUPPORTED from the gap side too. Induced 4-fermion interaction genuinely from Bergman two-point (F85), no new group.
- **✅ OP-4 linear-algebra pull DONE (07-19g) — MAJOR REFRAME (K768).** The Yukawa is the overlap matrix Y=⟨f_L|Φ|f_R⟩; a single condensate → **Φ rank-1 → Y rank-1 → exactly ONE massive fermion (the top)** (Elie verified; Lyra = F585 Gatto texture on the mass side). **Flavor closes as ONE rank-1 condensate O + Tier-2 corrections: masses AND mixing are the same O, read two ways.** This RETRO-EXPLAINS why the up-type ladder + mixing are Tier-2 (they're the off-rank-1 corrections, not leading identities). Tiers: ceiling DERIVED; rank-1→one-mass DERIVED-structural; N_c quark DERIVED; **y_t=1 SUPPORTED (⟺ top ∥ O)**; hierarchy+mixing Tier-2. Flagship §7 updated. **BLOCKER (Lyra):** F85 pins O's SCALE but not its DIRECTION (K-type) — that one vector is the decisive missing input.
- **✅ O PINNED (Lyra F603, 07-19h) — the vector is in hand.** From quantum numbers alone (color-singlet, SU(2)_L doublet, Y=½): **O = SO(5) vector (1,0)=5, λ₂=0 → spherical → boundary-reaching** (all one fact, non-circular). Top = spinor (½,½)=4, λ₂=½. Yukawa = γ-vertex 4⊗4→5. **y_t=1 NOT forced by rep theory** (5 is not the stretched branch; evidence y_t<1) → reduces to ONE radial overlap: does the non-spherical top (λ₂=½) reach the spherical boundary O (λ₂=0)? Elie fish (4743): the 0.992 gap is AMBIGUOUS (degenerate RG-vs-CG), can't decide the fork. **Blocker = the top's discrete-series radial address (a,b) — the June open core.**
- **▶▶ THE WHOLE FLAVOR AREA NOW BOTTLENECKS ON ONE NUMBER (K769):** 13 Yukawas → one O (pinned) → one radial overlap → **the top's discrete-series address.** That number decides y_t AND anchors the whole radial mass tower AND is the long-standing June open core. **← highest-value target in the program.**
- **★★ CANDIDATE-LEAD (K771) — y_t = M_g/2^g = 127/128 = 0.99219** (deficit = 1/2^g = one Reed-Solomon code-unit; m_t=172.74, inside pole bar). Casey's precipitation picture: substrate has 2^g=128 code levels (GF(128), Paper #122), top at outermost 127=M_g, loses one code-unit failing to reach O. **Target-innocent FORM** (2^g + M_g pre-existing), tight, matches F603 geometry, rep-theory tilts toward y_t<1. **NOT banked — 4 guards:** (1) scheme-dep (pole not MS-bar); (2) RG-degeneracy (number can't decide vs exact-1+running, Elie fish); (3) assignment top→127 un-derived; (4) unit not a-priori unique (137/138 nearby). **DECIDER = the top's discrete-series address:** deficit = 1/2^g → 127/128 DERIVED (theorem); = 0 → exact-1+RG, retired. **★ Casey band-edge reframe (K771 addendum):** the address IS a **band edge** — read the 2^g=128 RS cells (Paper #122) as a granular lattice, mass = effective mass (resistance to hopping across gaps), the top at the band EDGE (level 127), deficit = the last band gap (127→128). So the deciding computation = "is the last band gap exactly 1/2^g?" — a more tractable/physical target than an abstract (a,b) label. Mechanism sketch for guard-3 (why 127); still LEAD. **Derived-clean regardless:** mass ordering = boundary-reach ordering (t>c>u = most→least boundary-localized).
- **▶ ACTIVE PULL — the top's radial address / ⟨t|O⟩ across the λ₂ gap** (`team_prompt_2026-07-19i`): pin the top's discrete-series (a,b) on the K-type tower; compute the radial overlap of the top (λ₂=½) with the spherical boundary O (λ₂=0); does it saturate (y_t=1) or fall short? Same machinery pins every fermion's radial moment. Casey's ground-vs-outermost reach intuition is the tool. Lyra leads; Elie verifies; Keeper audits (K769). **★★ Casey precipitation-deficit hypothesis (K770):** the top precipitates onto the DISCRETE side (λ₂=½), can't fully reach the CONTINUOUS O (λ₂=0), sheds a massless tail = the neutrino → **links y_t<1 to m₁=0** (heaviest & lightest = one fact; 2nd route to m₁=0 with rank-2). Number fails (deficit≠ν Yukawa/mass), it's a MODE statement. Target: does the discrete top's boundary-leakage necessitate a zero-mode? LEAD. **Parallel thread:** two-condensate unification (OP-6/OP-7 — Higgs inertial + QCD spin?, one substance; explains m_p=6π⁵m_e). Don't bank y_t=1.
- **▶ NEXT ROW (after today, Casey):** CP phase (δ=rank/g=2/7 lead). Then gluon-field native realization; neutrino absolute scale (Weinberg v²/Λ). **sin²θ_W, α_s, exact mixing forms = STRUCTURAL/RUNNER — do NOT chase.** SU(3)=DERIVED (G2-stabilizer K755).
- **New research note filed:** generations = radial strata → thermal history of D_IV⁵ (`BST_Generations_As_Radial_Strata...`); neutrino-freeze-out/N_eff lead → backlog.
- Audits: **K762 + K763**. Arc closed.

## HOW WE WORK THIS PROGRAM (read first)
- **Work your column top-to-bottom.** Items are ordered **easiest → hardest**. Do the low-hanging fruit first; proceed through your ENTIRE list until every item is complete.
- **~20 minutes per item, in parallel.** Short sharp attacks — strengthen or close, bank what earns it, move to the next. Don't marathon one item.
- **All assigned items get worked to completion.** "Complete" = strong (referee-defensible) OR honestly closed/tiered with a stated reason. A clean negative is complete.
- **Discipline stands:** exact identities only; target-innocence (numbers from geometry, not back-solved); Five-Absence filter (no GUT / gauged SU(2)_R / SU(4) / Z′); derived ≠ supported ≠ correspondence; tier every claim; scrutinize your prettiest result hardest. Keeper audits every landing.

## CURRENT STATE (what's solid, what's the frame) — updated post strengthening-pass (K741)
- **The frame:** the SM as the linear algebra + rep-theory of ONE domain D_IV⁵ — one seed (rank=2), one ruler (gravity), one π. Synthesis artifact: `notes/BST_SM_from_D_IV5_synthesis_artifact.html`.
- **Solid:** masses (20 of 26 = Σ); **α = 0.0004%** referee-ready (E1, two-target); weak native + **parity from odd g** (K729); EW scale on the ruler 0.01%; **conservation verified** (E4, dim 21 = N_c·g) + topological laws (T1945); three generations = rank+1.
- **★ NEW (K741):** **F582 — all 16 fermions placed in ℍ⁴, T₃_R = global Sp(1)_R (felt only via Y) → Five-Absence's no-W_R/no-Z′ DERIVED** (4 directions → gauge 1 → 3 missing; converges with Elie's KK blocker E6). Resolves the T₃_R frontier + clears K738 Gate 1. **Roots reframe (F579)** = flagship foundation (5 integers = rank-2 root system, N_c = root multiplicity). **Thermo framework (F580)** = entropy/time/gravity as three readings of Z(τ).
- **Closed/retracted this week:** **sin²θ_W = runner** (3/13 retired, K739); **Λ over-determination RETRACTED** (Lyra F581 + Elie E5 converge — 280 structural not forced; "5-fold" is one factorization ×5).
- **Open frontier (narrowed):** mixing textures (CKM/PMNS, gated on Lyra L5/L6); color dynamics (Q⁵↔Shilov); KK gauge fields (the SU(2)_R-breaking step); neutrino mass mechanism (Lyra L6).
- **Roadmap:** `Keeper_Strengthening_Roadmap_effort_ranked_2026-07-18.md`. Audit: **K741**.

## ✅ STRENGTHENING PASS COMPLETE (all columns worked to completion, 2026-07-18)
Lyra F579–F582 (4/4), Elie toys 4709–4717 (8/9; #7 gated on Lyra L6), Grace G1–G6 (6/6). Banked + tiered in **K741**. Two two-CI convergences: **positive** (F582+E6 → SU(2)_R not gauged) and **negative** (F581+E5 → Λ over-determination retracted) — the audit chain working on both a win and a walk-back.

### ▶ NEXT ROUND — what K741 says still needs updating
1. **⛔ NEUTRINO SWEEP (K740) — STILL #1**, distinct from Grace's fit-sweep. F582 (ν_R gauge-blind singlet) further supports Majorana; the ~40-file Dirac→Majorana revision is the top hygiene item. **+ ADD Λ-over-determination retraction to the same sweep** (MEMORY/CLAUDE "280 5-fold over-determined" headline → structural).
2. **Flagship assembly (Keeper)** now unblocked — roots (F579), α (E1), 26-scoreboard (G1), render assets (G4), fermion table (F582) all landed. Assemble.
3. **Five-Absence falsifier paper (Keeper)** — update: 2/6 absences now DERIVED (F582).
4. **Synthesis artifact** — T₃_R/fermion row open→derived; conservation row → +topological/+verified; frontier card #1 resolved.
5. **Frontier research continues:** Lyra L5 (CKM texture) / L6 (neutrino mass) / L7 (color dynamics); Elie item-7 verify on L6 landing + the KK SU(2)_R-breaking step; Cal referees the "why Y" step of F582 + the roots reframe rigor.

---

# ✅ SWEEP STATUS (2026-07-18) — neutrino DONE; proton/GUT mini-sweep queued (K742)
- **✅ NEUTRINO Dirac→Majorana sweep COMPLETE** (all owners). Grace: 68 files → 40 revised + 28 historical + data layer + 7 referee files. Lyra: Working_Paper Vol5/Vol6/Vol1/Vol3 + Curriculum Ch10. Elie: verified (toy 4718). Keeper: the 2 source papers (DoubleBeta + Conservation_Laws). **Corpus no longer self-contradicts on the neutrino — outreach-blocker cleared.**
- **⚠ NEW: SECOND staleness — proton-decay / GUT-scale (K742).** Lyra's adjacent catch → `BST_Conservation_Laws.md` §2.1 predicted finite proton decay (τ_p≈3×10³⁴ yr at N_GUT=4π²), contradicting **Five-Absence** (τ_p=∞, no GUT). **Keeper fixed the source file.** MINI-SWEEP queued: check `BST_Particle_Predictions`, `BST_Field_Equation`, `BST_Why_This_Universe`, `Working_Paper/Vol3 Ch03`, `Vol2 Ch02`+INDEX. **⚠ SCALE-vs-GROUP rule:** flag ONLY (a) finite proton decay, (b) N_GUT=4π² as *unification*, (c) a unifying group — NOT "GUT scale" as an energy (~10¹⁶ GeV is fine). Owner: Grace enumerate + Keeper audit. [Λ over-determination retraction rides here too — MEMORY/CLAUDE "280 5-fold" → structural.]
- **★ no-W_R/no-Z′ now FULLY DERIVED** — the "why Y" step **resolved DERIVED** (F583, K743): the ν_R ν_R Majorana condensate (T₃_R,B−L)=(+1,−2) preserves *exactly* Y (unique surviving U(1)) → hypercharge forced, not chosen. Three convergent routes (F582 + Elie KK + F583 breaking-stabilizer). Cal formal ratification pending. Anomaly-argument correctly excluded (16 = SO(10) spinor).

## ✅ ROUND 3 COMPLETE (K743) — the gauge/neutrino story materially stronger
- **KK reduction COMPLETE** (Elie 4721): 11 → **exactly 4 = SM electroweak SU(2)_L×U(1)**; odd-g ungauges the surplus 7. Dynamical EW gauge group **DERIVED** ("group"→"fields").
- **Neutrino mechanism** (F584): minimal seesaw n(ν_R)=rank=2 → m₁=0 exact, narrow m_ββ band. The **one condensate does both jobs** (forces Y *and* gives ν masses). n(ν_R)=2 = the one SUPPORTED link (the single upgrade target). Unblocks Elie item 7.
- **CKM** (F585): form + V_us DERIVED; V_cb/V_ub magnitudes STRUCTURAL. Grace renders.
- **Color** (F586): kinematics placed (N_c=root mult); dynamics OPEN.
- **★ TWO MASTER MECHANISMS:** **odd-g** (chiral weak + no-W_R/Z′ + KK-trim — 3 payoffs) and **Shilov-vanishing** (confinement + m₁=0 + n(ν_R)=2 + V_ub — 4 sectors). **Making Shilov-vanishing rigorous = highest-value next step** (common root of 4 results).
- **Flagship updated** with all of the above (§3 KK, §4 why-Y-derived, §7 neutrino+CKM, §9½ master mechanisms). **Proton/GUT mini-sweep DONE** (Grace; 1 Working_Paper line for Keeper audit).

## ✅ ROUND 4 COMPLETE (K744) — Shilov-vanishing is now a THEOREM
- **★ Shilov theorem DERIVED** (Lyra): zero Shilov boundary value ⟺ **non-spherical SO(5) K-type (λ₂ > 0)** (Szegő restriction + class-1 branching on S⁴). Exact, computable, linear-algebraic.
- **★ RETRACTION banked** (Lyra, Cal #27 on her own claim): the Shilov engine is **ONE ENGINE, TWO LEGS** — exact leg → **confinement**; graded leg → **mass hierarchy, m₁=0**. Mass = **cousin** of confinement, NOT identical. **Keeper fixed flagship §9½** before ship.
- **Confinement Schur leg verified** (Elie 4723): color-blind boundary → colored support = 0 (Schur orthogonality) → confined. DERIVED **pending the color-K-type check** (are nonsinglets λ₂>0?).
- **Neutrino masses verified** (Elie item 7): m₁=0, narrow band ✓. **Angles from the texture = the remaining check** (honest FAIL point if 3/10, 1/45 don't drop out).
- **CKM rendered** (Grace F585): form + V_us=0.2243 (0.4%) + ordering DERIVED; magnitudes structural. **★ small-CKM/large-PMNS = one fact** (quarks fill 3 strata; ν skip Shilov). Added to flagship §7.
- **Flagship assets inline** (Grace: Figure 1 + Appendix A); **numbers cross-checked** (Elie — one verified reference). §9½ + §7 fixed (Keeper).
- **Casey steer:** "remember it's linear algebra" — the engine IS K-type branching = linear algebra.

## ✅ ROUND 5 COMPLETE (K745) — CONFINEMENT DERIVED
- **★★ CONFINEMENT DERIVED** (three convergent, frame-independent routes): H = H²(D_IV⁵) ⊗ ℂ³_color; Shilov boundary carries the trivial color rep → by Schur, color-nonsinglets have EXACTLY zero boundary support → confined; singlets emitted. Lyra (Schur/tensor-factor, rejected frame-dependent Peirce route) + Elie (K-type: N_c=3 = short-root mult → triplet λ₂>0 non-spherical) + Elie earlier Schur toy. Color's confinement leg: SUPPORTED → **DERIVED**.
- **Neutrino m₁=0 SHARPENED** to **rank(m_D^ν) = rank(D_IV⁵) = 2** (rank-2 coupling → one massless ν). Better than n(ν_R)=2 (hangs on domain rank). One premise open: *why* rank-2 (vs charged-lepton rank-3; lead: ν_R sees 2 idempotents). [SUPPORTED, sharp]
- **Grace: B₂ root diagram** (flagship Fig 2) — every primary a root-invariant; the short-root/λ₂ axis IS the spherical/non-spherical divide. Master mechanism = a coordinate axis. Flagship render assets COMPLETE.
- **Keeper:** α standalone DRAFTED (`BST_Alpha_Standalone_Companion_...`, 137+5/137, 0.0004%, target-innocent). Working_Paper "Structured Unification" line audited = **presentation fix not staleness** (scale-not-group; reads-as-GUT → reframe recommended to Lyra, low urgency). Flagship updated (§3 confinement, §7 rank, §9½ 3rd-mechanism).

## ✅ ROUND 6 COMPLETE (K746) — neutrino DERIVED (pending Cal); the PMNS bump is a signpost
- **★ NEUTRINO SECTOR DERIVED** (Lyra F588, pending Cal): m₁=0 on **rank-2 counting** — 3 boundary orbits (rank+1) = 3 gauge-charged generations; **2 idempotents (rank) = 2 ν_R** (gauge singlet has no flag → indexed by spectral frame). m_D 3×2 → one zero eigenvalue. **Supersedes** the shaky λ₂-premise (conflated K-type λ₂ with orbit-rank). Cal ratifies the one assignment.
- **★ THE BUMP = SIGNPOST (not fatal):** Elie — **0 of 6 m₁=0 mass textures reproduce the PMNS angles** (3/10, 1/45). Angles **identified, not derived** from the texture. **KEEPER: this CONFIRMS K704** — masses = RADIAL (Σ), mixing angles = ANGULAR (U†U′); the mass texture entangles both, so it can't yield the pure-angular angles. → **NEW APPROACH below.**
- **Gluon fields (Elie): derived-HOSTED tier.** KK on ℂ³: U(3)→8 gluons + global baryon-U(1) (9→8, baryon ungauged ✓). Real geometry gives SO(3); full SU(3) needs the *hosted* complex structure (F572) — one tier below native EW fields.
- **Grace λ₂-sweep:** exact leg = one coordinate (asymptotic ⟺ color singlet). **⚠ Keeper fix:** Grace's Leg-2 n(ν_R)=2-via-λ₂ uses the RETIRED premise; correct derivation-of-record is Lyra's idempotent-count (λ₂ governs confinement ONLY). Grace re-tags.
- **Flagship updated:** §7 neutrino DERIVED + PMNS angles identified-not-derived; §3/§9 gluon hosted.

## ✅ ROUND 7 COMPLETE (K748) — mixing localized to its ANGULAR home
- **★★ MIXING = the angle between D_IV⁵'s TWO STRATIFICATIONS** (Lyra F589): boundary-orbit **flag** (rank+1=3 = gauge-charged generations) ⟂ spectral idempotent **frame** (rank=2). U=⟨flag|frame⟩, decoupled from masses (why 0/6 textures worked). **★ small-CKM/large-PMNS = ONE fact** (quarks both-chiral on the flag → cancel; ν_R gauge-singlet frame misaligned → large). **Mechanism DERIVED; forms IDENTIFIED** as equipartition sin²θ=d/D (Elie): θ₂₃=rank²/g=4/7, θ₁₂=N_c/(rank·n_C)=3/10, θ₁₃=1/(N_c²·n_C)=1/45.
- **⚠ Two Keeper flags:** (1) θ₁₂ denominator 10 is a value-coincidence (rank·n_C = N_c+g = 10) — pin the REAL subspace dimension; (2) so(10) reading (10,45=vector,adjoint) fits θ₁₂/θ₁₃ but NOT θ₂₃ — resolve, don't over-claim. Five-Absence intact (combinatorics, not gauged).
- **λ₂ classifier COMPLETE** (Grace): confined/free = λ₂ sign, matches all observed physics. Grace fixed the n(ν_R) attribution (idempotent-count, not λ₂).
- **★ NEW candidate 3rd master structure — the TWO-STRATIFICATION ANGLE** (replaces the retired domain-rank K747): multiple instances (CKM+PMNS+asymmetry), unlike domain-rank's one. Flagship §7/§9½ updated.
- **Housekeeping:** Elie caught ~2h board-timestamp drift (use `date`); all 3 CIs + Keeper recommend a sundown checkpoint (Elie persisted his).

## ✅ ROUND 8 COMPLETE (K749) — EOD checkpoint; forms NEGATIVE but a real synthesis
- **Mixing FORMS did NOT close via one uniform branching** (both K748 flags held): **so(10) reading RETRACTED** (θ₂₃=rank²/g=4/7, D=g=7 breaks it — 2/3 is the trap); the "which-10" ambiguity (10=rank·n_C=N_c+g) unpinnable without the branching. **Forms stay identified; MECHANISM (two-stratification angle) untouched.** 4th honest negative of the day — each sharpened, none blocked.
- **★★ SYNTHESIS: FLAVOR = THE SVD OF THE DOMAIN.** M=UΣV†: masses=Σ (radial, done), mixing=U,V (angular flag⟂frame, DERIVED), CP=phase(U,V) (lead). The whole flavor sector = one linear-algebra object.
- **★ FOUR NEW PHYSICAL IDEAS (Casey's ask):** (1) flavor-SVD [synthesis]; (2) a democracy/equipartition principle spanning α AND mixing [candidate]; (3) CP as a geometric overlap phase → a δ_CKM–δ_PMNS relation [lead]; (4) a **global SO(3)_gen family symmetry** (3 orbits = triplet) → Wigner-3j mixing overlaps [Lyra's lead, Five-Absence-safe].
- **EOD:** all CIs persisted (292 files). Real clock ~11:37 (Elie's drift caught). Flagship §7/§9½ updated.

## ✅ ROUND 9 COMPLETE (K751) — closure route sharpened to orbit-pair mode-counts; 1 of 3 D's pinned
- **SO(3)_gen route KILLED** (Lyra F592, own lead): {7,10,45} ≠ SO(3) dims {1,3,5,9}. + so(10) already retired → **both single-group readings dead.**
- **★ CLOSURE = per-pair Korányi–Wolf orbit-mode-count** (3 orbit-pairs = 3 angles): θ₁₂=B↔I, θ₂₃=I↔S, θ₁₃=B↔S. **θ₁₂'s D=10 PINNED = dim SO(5)** (Elie — real dimension, resolves the K748 which-10 flag). θ₂₃ (D=7), θ₁₃ (D=45) open.
- **Democracy/equipartition principle** (α↔flavor, all CIs tiered candidate/framework — good): + Grace's **angular=democracy / radial=norms split** (SVD from the measure side — BANK). + |sinδ_PMNS|=2/7 instance.
- **⚠ KEEPER GAPS (K751):** (1) only 1 of 3 D's pinned + θ₁₂'s D=10 has two homes (SO(5)-adjoint vs B↔I pair) to reconcile; (2) the "hierarchy from orbit-separation" claim TOO SIMPLE (θ₂₃,θ₁₂ both adjacent yet D=7≠10 — needs actual counts); (3) democracy INDEPENDENT instances = 2 not 3 (|sinδ|=2/7 shares g-space with sin²θ₂₃=4/7) → Elie's "needs a 3rd" stands, hold framework-level.

### ★ K752 — THE RECENT MIXING IDEAS ARE PROVEN RESULTS (Casey's "does this remind you of…?")
**(1) Mixing angles ARE Born probabilities** (sin²θ=|U_ij|²), and **Born = Bergman is PROVEN (T2401).** → the democracy/equipartition principle isn't a candidate — it's **the Born rule on the flavor mode space, with a proven foundation.** Only the mode-count D's are open. **(2) The two-stratification angle (flag⟂frame) IS the dual-ρ overlap** the corpus built in May (compact ρ_SO(5)=(3/2,1/2)=frame, conformal ρ=(5/2,3/2)=flag) — the scorecard ALREADY had "θ₁₂ = dual-ρ 1-2 overlap" and "δ_PMNS = dual-ρ phase." Round 7–9 independently rederived it (2-month consistency). **θ₁₂'s D=10=dim SO(5) = the compact ρ_SO(5) side ✓.** **→ REUSE the existing dual-ρ / Engine-B machinery, don't rebuild.** Weaker echoes: democracy=entropy=counting (Casey's Principle); confinement-by-Schur = Schur generator (Bell/CHSH 126/16).

## ✅ ROUND 10 COMPLETE (K753) — GRAND SYNTHESIS + mixing-forms adjudicated
- **★★★ THE GRAND SYNTHESIS (Casey's "think deeply + fold in Born=Bergman"): the SM = the Born/Bergman MEASURE of D_IV⁵** (proven, T2401/T754), read through the SVD (masses=radial norms Σ / mixing=angular Born overlaps / CP=phase) + Schur (gauge/confinement). Couplings=democratic counts, conservation=symmetries. **The 26 parameters are ONE proven measure, decomposed.** The 3 master mechanisms = 3 faces (odd-g=chirality, λ₂=boundary-support, dual-ρ=overlaps). Flagship §10 + §9½ updated.
- **⚖ MIXING-FORMS ADJUDICATED (K753):** Lyra/Elie called the orbit-pair route "4th dead / hard wall"; Grace found a gain — **they computed DIFFERENT objects.** Lyra's orbit-dim-*differences* {1,4,5} = dead; **Grace's SO(5) K-group REP dims = LIVE** (θ₁₂ D=10=dim SO(5); **θ₁₃ D=45=C(10,2)=pairs of θ₁₂'s space** — 2 of 3 chained). Elie's caution valid (D=10 has ≥4 readings → foundation CANDIDATE). **KEEPER VERDICT: NOT a wall, NOT closed** — the denominators are Born-overlap rep-subspace dims → **rep-theory-open on a PROVEN measure**, θ₂₃'s 7 the one genuinely open. Refines Lyra's "Tier-2": open ≠ un-derivable.
- **5 over-claims retracted across the team today** (3 Lyra, 1 Elie's D=10, 1 domain-rank) — discipline held to the end.

## ✅ ROUND 11 COMPLETE (K754) — the synthesis collapses to one line: THE SM IS QM ON D_IV⁵
- **★★★ THE SM IS QUANTUM MECHANICS ON D_IV⁵.** Born rule = Bergman kernel is PROVEN (T2401/T754) → doing QM on H²(D_IV⁵) *automatically* yields the couplings (counts), masses (radial norms), mixings (Born overlaps), CP (phases), forces (Schur). Not "26 params," not even "one measure" — **the SM is what QM produces on this one shape.** Resolves the two "deepest reframes" as layers (object/symmetry = rank-2 root system; dynamics = QM/Born-measure). Fifth-grader paper + artifact updated to "one cloud on one shape."
- **★ θ₂₃ HOMED** (Lyra F594, verified): D=7 = SO(5,2) defining rep ℝ^{5,2}, whose null cone = (S⁴×S¹)/ℤ₂ = the Shilov boundary. **All 3 mixing denominators now have rep-homes** (θ₂₃=7 defining, θ₁₂=10 dim SO(5), θ₁₃=45=Λ²θ₁₂). Lyra softened "hard wall" → rep-theory-open.
- **GAPS (K754):** G1 mixing "lives-there" (counts=rep-dims candidate; numerators open — sharpest); G2 θ₁₂'s 10 adjoint-vs-tangent; **G3 "democracy principle" = the Born rule, NOT a new principle — stop double-naming** (2 instances are the same rule; λ_H failed 3.5%); G4 synthesis is framework, not yet a theorem; G6 CP/masses-tiers/color-dynamics carried.

## ★ K755 — DERIVATION PUSH on the not-yet-derived items (Casey's ask)
- **★ ASYMPTOTIC FREEDOM DERIVED:** β₀ = 11N_c − 2N_f = 11·3 − 2·6 = 21 > 0 → asymptotically free UV, confining IR — from N_c=3, N_f=6 (3 gen × 2). The QUALITATIVE QCD dynamics is derived (consistent with Schur-confinement). α_s(scale) stays a runner.
- **★ V_ub RECLASSIFIED out of soft-spots → mixing sector** (it's the CKM bulk↔Shilov overlap = analog of PMNS θ₁₃; inherits mechanism-derived). **Soft-spots list shrinks to m_u only** (m_u = honest-structural: n=0 ground slot + confinement-dressed, not a clean observable).
- **SU(3) group pinned harder:** SU(3) = stabilizer of an octonion unit in G2=Aut(𝕆) (G2/SU(3)=S⁶) — group DERIVED; EW fields native, color fields hosted (KK 9→8).
- **Mixing forms tier-UP:** all 3 denominators homed (θ₂₃=7 defining-rep/null-cone=Shilov VERIFIED; θ₁₂=10 dim SO(5); θ₁₃=45=Λ²θ₁₂); mechanism derived → "identified" → "denominators homed, 2/3 tied"; numerators + θ₁₂-subspace open.
- **sin²θ_W:** runner (unchanged) — high-scale 3/8=N_c/rank³ derived (fermion content), runs to observed.
- **⚠ Self-caught over-reach withdrawn:** color "native-upgrade" (ℂ³ from the domain's J) — color is on the compact dual, not the SO(5) tangent, so hosted stays honest.
- **Net:** 2 new derivations (asymptotic freedom, SU(3)=G2-stabilizer), 1 reclassification (V_ub), 2 tier-ups (gauge group, mixing forms), 2 honest holds (m_u, sin²θ_W). Flagship §9 + artifact ledger updated. Source: K755.

## ✅ ROUND 12 COMPLETE (K756) — the containment THEOREM + Casey's two framing directives
- **★ CONTAINMENT THEOREM (Lyra N1):** every BST-*derived* observable is provably a functional of the proven measure μ (moment/overlap/phase/count/symmetry-invariant) — exhibited. **Completeness = CONJECTURE** (quark-mass counterexample). So "SM is QM on D_IV⁵" = **framework on proven parts**, not "SM derived." Flagship §9¾ added.
- **★ Masses = radial moments of μ (Elie N5, verified):** ‖z^n‖²=π·B(n+1,p+1). Σ=radial moments, U=angular overlaps — two halves of one measure.
- **★ CASEY DIRECTIVE 1 — reframe "soft" → "COMPUTABLE, NOT CLEANLY OBSERVABLE"** (+ reason): m_u (confined→no pole mass, scheme-dependent even in experiment); runners sin²θ_W/α_s (scale-dependent, no clean value). Licensed by the containment theorem (BST computes everything; the observable side isn't sharp). Flagship §9 done; **Grace sweeps data layer + tier-map; Keeper folds into papers.**
- **★ CASEY DIRECTIVE 2 — up-quark = TWO masses with Born probabilities** (rank-2 Jordan doublet; why-two = rank=2, same as 2 ν_R). **Tomorrow's headline.**
- **Grace de-double-named her own "democracy principle"** (it's the Born rule) — discipline on own work. **6 over-claims retracted across the team today.**

### ▶ TONIGHT — FINALIZE (my recommendation)
- **★★ CAL — ratification pass** (top priority, natural close of a 12-round day): every "derived" tier + **the containment theorem** (genuine theorem? completeness held as conjecture?) + all retraction logs → flagship + 4 companions **referee-FINAL**.
- **Grace** — the reframe sweep (quick, parallel). **Keeper** — fold reframe + containment theorem into all 4 papers; integrate Cal's pass.
- **Lyra/Elie** — number-checks for Cal; the substantive frontier is TOMORROW.

### ▶ TOMORROW — "improve the non-derived" task set (Casey requested, K756)
1. ★ Two-mass up-quark (rank-2 Born doublet; why-two rigorous) [Lyra+Elie]. 2. ★ Quark mass ratios as radial moments of μ (Statement-B counterexample) [Elie+Lyra]. 3. Mixing lives-there theorem [Lyra]. 4. δ_CKM from overlap phase (CKM–PMNS relation) [Lyra]. 5. Gluon fields native realization [Elie]. 6. Advance Statement B [team]. 7. Finish the reframe sweep [Grace].

### ▶ (superseded) ROUND 12 leads
- **★★ CAL — RATIFICATION PASS (finalization gate, top priority):** ratify every flagship "derived" tier + the grand-synthesis framing (framework-on-proven-parts, honestly tiered) + all retraction logs → flagship + 4 companions REFEREE-FINAL. Cross-check α (27·5+2), conservation (20=g+c₃).
- **★ N1 (highest-value new target) — make the synthesis a THEOREM:** "every dimensionless SM observable = a moment/functional of the Born/Bergman measure on D_IV⁵." Framework→derived. [Lyra + Keeper]
- **★ N2 — SM = QM on D_IV⁵ supports "QM = stat-mech via the D_IV⁵ partition function"** (backlog U-2), Born=Bergman the bridge. Investigate. [Lyra]
- **N3** δ_CKM from the overlap phase (CKM–PMNS relation) [Lyra]; **N4** mixing "lives-there" theorem (closes forms, background) [Lyra/Elie]; **N5** masses as Born-measure moments [Elie].
- **Keeper:** integrate Cal's pass; fold "SM = QM on D_IV⁵" into all 4 papers; G3 de-double-name; audit.
- **Grace:** paper-grade TikZ; render N-lead outputs.

### ▶ (superseded) ROUND 11 leads
- **★★ CAL — THE RATIFICATION PASS (top priority):** ratify F583 why-Y, Shilov theorem, confinement, neutrino F588, **every flagship "derived" tier**, the grand-synthesis framing (Born=Bergman-grounded), + log all retractions (F586, so(10), SO(3)_gen, orbit-dim-diff, domain-rank, Elie D=10). → flagship referee-FINAL.
- **BACKGROUND (not a team round, Lyra's call):** confirm θ₁₂'s SO(5) foundation (is SO(5) genuinely the B↔I connector, uniquely?) + θ₂₃'s D=7 (SO(7) vector?). One toy, off the critical path.
- **Keeper:** integrate Cal's pass; fold the grand synthesis into all four papers; audit.
- **Grace:** paper-grade TikZ if Keeper confirms; render θ₂₃ grounding if Lyra lands it.
- **Elie/Lyra:** support ratification; the CP-as-overlap-phase lead (δ_CKM in the g-space?) if a round opens.
- **Democracy principle → find a genuinely independent 3rd instance** (grounded-D, not sharing 137/10/g-space) to promote framework→mechanism [Keeper+Grace].
- **CP as overlap phase:** does δ_CKM land in the same g-mode-space as |sinδ_PMNS|=2/7? (a CKM–PMNS relation) [Lyra].
- **Gluon native upgrade** (carried) [Lyra].
- **★ CAL — ratification pass** (finalization gate): why-Y, Shilov theorem, confinement, neutrino F588, every flagship "derived" tier, retraction logs (F586, so(10), SO(3)_gen, domain-rank) → flagship referee-FINAL. Keeper: integrate + audit.

### ▶ (superseded) ROUND 9 leads
- **★ CLOSE THE MIXING FORMS → DERIVED (route CHANGED):** NOT one so(10) branching (retracted). Two live routes: **(a) global SO(3)_gen → Wigner-3j overlaps** (Lyra's first item); **(b) per-observable equipartition D's** (identify the genuine subspace dimension for each of D=7,10,45). Try both; may coincide. [Lyra + Elie]
- **CP as overlap phase** — δ_CKM/δ_PMNS = arg⟨flag|frame⟩? Does δ_PMNS=2/7 re-derive, + a δ_CKM prediction? [Lyra]
- **Democracy/equipartition principle (K750) — MERGED with lead #1 (SAME target):** the principle's content is "D is a genuine democratic dimension-count," which IS the mixing-form-closure work. Grounding the D's (7,10,45) both closes the forms AND establishes the principle (unifies α + mixing under Casey's 137-democracy). One computation, two payoffs. α solid (137 charge-count); mixing candidate; runner sin²θ_W-high correctly excluded (built-in discipline). [Keeper K750 bounds the scope; Lyra+Elie ground the D's]
- **Gluon complex-structure native upgrade** (carried) [Lyra].
- **★ CAL — the ratification pass** (the finalization gate): why-Y, Shilov theorem, confinement, neutrino F588, every flagship "derived" tier, the retraction logs (F586, so(10), domain-rank), + cross-check α standalone & conservation short paper → flagship referee-FINAL.
- **Keeper:** integrate Cal's pass; audit; hold the flavor-SVD framing honest.

<details><summary>Original neutrino sweep spec (K740) — kept for reference</summary>

# ⛔ (DONE) NEUTRINO REVERSAL PROPAGATION SWEEP (K740)
**The 2026-07-16 Dirac→Majorana reversal (F413/K673, Toy 4691) reached ONLY `data/bst_predictions.json`. ~40 files still state the OLD Dirac prediction — including the Working_Paper's "cleanest binary falsifier," which says the REVERSE of the current claim.** A referee reading it would test BST against "0νββ=0, detection kills BST" when BST now PREDICTS the detection (m_ββ∈[1.4,3.7] meV, detection SUPPORTS BST). **Blocks all outreach.**
- **Revision:** OLD *Dirac / B−L exact / 0νββ forbidden / |m_ββ|=0 / detection falsifies* → NEW *Majorana / B−L violated by ΔL=2 Majorana mass / 0νββ occurs [1.4,3.7] meV / detection supports, null <1 meV falsifies.*
- **Priority order:** Working_Paper Vol5 Predictions Ch01 (lines ~128/304/362/418) → Vol6 Frontier Ch01 (~936/946) → Vol2 Ch02 seesaw → Vol1/Vol3 → `notes/BST_NeutrinolessDoubleBeta.md` → `notes/BST_Conservation_Laws.md` (Sec 2.3/8.5, the origin) → `Curriculum/Vol02/…Ch10_Neutrinos` → notes (SP26 map, Particle_Predictions, ParticleFamily, Verification_Tests, substrate_atlas).
- **Owners:** **Grace** — enumerate the full ~40 (data-layer cross-ref) + sweep data/notes; **Lyra** — Working_Paper + Curriculum physics prose; **Keeper** — audit each + rewrite DoubleBeta & Conservation_Laws papers + the topological-conservation reframe. **Cal** — referee the Majorana prediction statement is consistent everywhere.
- **Reframe to carry:** topological conservation (T1945: B=trefoil, L=SO(5) winding, gen=Q⁵ cycles) is REAL and beyond-Noether, but state L as *winding-conserved-perturbatively, violated by the ΔL=2 Majorana mass* — NOT "B−L exact." Full register: **K740**.
- **PROCESS FIX:** add a **reversal-propagation checklist** to EOD — when a prediction flips (Majorana; sin²θ_W 3/13 retirement), propagate to papers+curriculum+notes, not just the data layer.

</details>

---

# THE PROGRAM — per-CI queues, easiest → hardest (work top-down, ~20 min each, until complete)

## ▶ LYRA (theory / rep-theory)
1. **Roots reframe** [SYNTH, easy] — rigorous statement: restricted root system of D_IV⁵ (rank-2, SO(5)=B₂) → the 5 integers as root-data invariants → primaries = gauge dual Coxeter numbers → observables as functions of roots. *Done = the reframe note, referee-grade.*
2. **Thermodynamics framework** [SYNTH] — one framework theorem tying entropy=counting + time=commitment-cycle (heat semigroup exp(−τH_B)) + Sakharov induced gravity (F63). *Done = theorem stated + tiered.*
3. **Cosmology Λ** [RESEARCH-lite] — is Λ=exp(−280), 280=2^{N_c}·n_C·g, FORCED or fit? *Done = target-innocent derivation OR honest "structural" verdict.*
4. **★ FRONTIER LEAD — fermion quantum numbers in ℍ⁴** [RESEARCH] — place all 16 Weyl fermions with (T₃,Y,color); answer **where T₃_R lives WITHOUT gauging SU(2)_R** (Five-Absence). *Done = assignment table + T₃_R source, or a sharply-stated obstruction.*
5. **CKM texture forcing** [RESEARCH] — is the substrate's natural localization basis the Fritzsch/NNI texture (√(m_i m_j))? Compute V_cb, V_ub/V_cb from it vs the 4-zero exclusion. *Done = forced, or "weak-basis fudge" verdict.*
6. **Neutrino mass mechanism** [RESEARCH] — resolve the contested m_ν1/2/3 forms (K719 three gaps). *Done = one mechanism or honest disposition.*
7. **Color dynamics** [RESEARCH] — the Q⁵↔Shilov bridge lemma (supported→derived). *Done = lemma or precise obstruction.*
8. **LAG-1 / LAG-2** [RESEARCH, deep] — explicit Bergman Dirac operator γ_B^μ; clean D_IV⁵→ℝ³·¹ reduction functional.
9. **(standing) U-2 BST↔QFT bridge** — Lagrangian isomorphism / same S-matrix.

## ▶ ELIE (toys / computation / verification)
1. **α standalone** [PACKAGING, easy] — package K701; verification toy for 4π = Coulomb solid angle + the two-target check. *Done = standalone toy + note, referee-ready.*
2. **Soft-spots m_u & V_ub** [PACKAGING] — one toy each: what BST gives + why soft (n=0 slot; V_ub route). *Done = honest soft-spot toys filed.*
3. **α_s** [PACKAGING] — document as RG-runner terminal-negative (why not a clean BST number). *Done = honest note.*
4. **Conservation verification** [PACKAGING] — numerically confirm the Noether currents (E/p/L/Q) from the so(5,2) generators (supports Keeper #2). *Done = the toy.*
5. **Cosmology Λ verification** [RESEARCH-lite] — toy checking 280 = 2^{N_c}·n_C·g 5-fold over-determination, target-innocent (with Lyra L3). *Done = toy + verdict.*
6. **Dynamical gauge fields via KK** [RESEARCH] — START the reduction for W/Z (F64 precedent). *Done = first KK-mode computation or a precise blocker.*
7. **Neutrino mass verification** [RESEARCH] — with Lyra L6.
8. **(standing) Nuclear honest rebuild** — r_p + binding on the shell model; DROP the magic-number forcing claim (K601).
9. **(standing) Six master integrals** — status / irreducibility note.

## ▶ GRACE (data / catalog / render)
1. **Clean 26-table scoreboard** [PACKAGING, easy] — all 26 params with current tier each; refresh `play/bst_26_table.py` + a clean md table. *Done = the scoreboard (feeds flagship + this board).*
2. **Catalog sweep** [PACKAGING] — file every new derivation from the LinAlg/sin²θ_W arc to `bst_constants.json`/`bst_geometric_invariants.json` (SP-14 zero-unfiled). *Done = catalog current.*
3. **Cosmology no-DM** [SYNTH] — formalize the no-DM-particle + Wallach-shadow-16/3 falsifiable bet as a catalog entry + falsifier. *Done = the bet stated with its refutation condition.*
4. **Flagship ledger render** [SYNTH] — tier-ledger + roots-diagram assets for the paper (from the artifact). *Done = render assets ready.*
5. **CKM texture render** [RESEARCH] — texture → angles render + basis check (with Lyra L5).
6. **Condensed-matter falsifier packages** [PACKAGING, outreach] — BaTiO₃ 137-plane, photonic ($10K), Casimir: cost + protocol + what-would-refute, outreach-ready. *Done = the falsifier package doc.*
7. **(standing) Rosetta Stone** (LT-1) — ratio catalog completion.

## ▶ CAL (referee — fire at each landing, in arrival order)
1. **α standalone** — target-innocence of 4π + curvature (guard the 24 = fit-then-ID).
2. **Roots reframe** — rigor vs relabeling.
3. **Cosmology Λ** — target-innocence of 280.
4. **Fermion T₃_R** — Five-Absence at landing (no gauged SU(2)_R / SU(4)).
5. **Flagship** — every green tier.

## ▶ KEEPER (audit / synthesize / assemble)
1. **Board cleanup** — ✅ DONE (2026-07-18).
2. **Conservation-laws inventory** [PACKAGING] — ✅ DONE — `Keeper_Conservation_Laws_Inventory_from_the_isometry_group_2026-07-18.md`. Tally + exact/broken pattern DERIVED; explicit currents framework-pending LAG-1; 27-sum NOT banked. Elie E4 to verify.
3. **Soft-spot + α_s honest ledger notes** [PACKAGING] — ✅ DONE — `Keeper_Honest_Negatives_Ledger_alpha_s_m_u_V_ub_2026-07-18.md`. α_s=runner, m_u=n=0 soft, V_ub=texture tail; all = where non-geometric physics dominates. Elie E2/E3 confirm.
4. **Five-Absence falsifier paper draft** [SYNTH] — ✅ DRAFT DONE — `BST_Five_Absence_Falsifier_Paper_DRAFT_2026-07-18.md`. Six absences + refuting experiments + cheap CM tests. Needs current bounds (Elie/Grace) + Cal referee on #5 tiering.
5. **Flagship synthesis paper assembly** [SYNTH] — ⏳ GATED on team cheap-cluster outputs (Grace 26-scoreboard, Lyra roots reframe, Elie α packaging). Starts when those land.
6. **Audit every landing; hold the tier ledger** — standing.

---

# RESOLVED THIS WEEK (pointers — detail lives in the K-notes, not here)
- **sin²θ_W CLOSED as runner** — K739 (3/8 + RGE; 3/13 retired). The K733–K738 hunt (√rank → two-spheres → B−L) resolved NEGATIVE; full trail in those K-notes. Discipline win: 0.19% match dismantled, not banked.
- **LinAlg-of-26 program** — K720–K732: the 3-layer structure (lattice / syzygies / rep-theory); SU(3)×SU(2)×U(1) = ℂ,ℍ,𝕆 of D_IV⁵ (K732 synthesis); weak native + parity from odd-g (K729); octonions positive via compact dual (K730).
- **Mixing sector** — K705–K717: mixing = off-diagonal texture (θ≈√(m_i/m_j)), determined by the banked masses; V_cb structural 0.044 (K711); PMNS partial (K713); δ_PMNS banked (K717).
- **Neutrino** — K719 g-organized, three gaps (→ Lyra L6).
- **α** — K676–K701: capacity 137 (count) + descent 4π + curvature → 0.0004% (→ Elie E1 packaging).

═══════════════════════════════════════════════════════════════════
# ▼▼▼ ARCHIVE BELOW (historical running log, newest-first from 2026-07-12) ▼▼▼
═══════════════════════════════════════════════════════════════════

# CI Coordination Board — Sunday 2026-07-12 EOD → Monday 2026-07-13 wake (fermion sector = a mapped spectrum)

*Two-day mass/mixing arc landed. Capstone: the CKM sector collapsed to one function f(ν) (up = down at the Szegő boundary limit), built and leading-order-verified; the neutrino resolved to near-forced Majorana (K673); the tau came forward-exact (49·71 − √π) with the −√π pulled from the geometry by Casey's 3-ball question, which surfaced the Peirce spine n_C = rank + N_c = "two crossings + three commitments." Nine team self-corrections across the two days; nothing banked that didn't earn it.*

**MONDAY WAKE — read first:** `notes/Keeper_26_Parameter_Scorecard_v0.1_2026-07-12.md` (the honest state of all 26) + `notes/Keeper_Mass_Sector_and_Falsifier_Reframe_Results_2026-07-11.md` (arc detail 2a–2r) + K671–K674 + your sundown. Then `date` + SOD. **The three carry-forward tasks are in the LAST TASKS table below — all lemmas, not mysteries.**

## CURRENT STATE — the fermion sector (read first, then `date` + SOD)

**Read first:** `notes/Keeper_Mass_Sector_and_Falsifier_Reframe_Results_2026-07-11.md` (arc synthesis, Sections 2a–2m) + `notes/Keeper_K672` (Koide) + `notes/Keeper_K673` (Dirac→Majorana) + your sundown.

| Sector | Status |
|---|---|
| **Down quarks** | BANKED (F506: d:s:b=1:20:840, s/d=20 forced via FK Pochhammer at ν=N_c) |
| **Up quarks** | top + charm PREDICTED (m_t=(1−α)v/√2 0.03%, m_c=αv/√2 0.05%; **m_t+m_c=v/√2 at 0.007%** — α-partition of the boundary mode); up dissolved (m_u/m_d=1/√g, 1.5σ within the 20%-measured value) |
| **Charged leptons** | muon CLOSED via d(ν) at 0.003%; **tau EXACT & FORWARD** (49·71−√π=3477.2275, 0.0000%) but the integral is a BUILD (structure-set); electron = anchor at ν=5/2 |
| **Neutrino masses** | BANKED (seesaw, intrinsically Majorana — Elie); m_ν1=0, Δm² ratio 1600/49 |
| **Neutrino nature** | Dirac→Majorana NEAR-FORCED (K673, all 3 gates addressed, BOLT 1 rigorous); pred_004 → "0νββ at 1–4 meV floor" pending Cal co-sign + one intertwiner joint |
| **CKM mixing** | IDENTIFIED not forced (canonical: Cabibbo λ=2/√79 0.004%, δ=arctan√5, J=A²λ⁶η̄ 0.3%); the NEW forcing frontier |
| **By-design** | m_e = the one dimensionful anchor; α_s, sin²θ_W = RG runners (not fixed numbers) |

## α — CAPACITY REFRAME RESOLVED (K676+K677); residual = ONE Born-measure matrix (marker: `notes/Keeper_ALPHA_RETURN_MARKER.md`)
**Casey's capacity insight adjudicated — the biggest reduction in the arc.** The **INTEGER 137 genuinely BYPASSES** the multi-month Knapp–Wallach theorem: it is a **democratic dimension-count** (each of the 137 fibers counts once, norm-independent, combinatorial = N_c³·n_C+rank). Confirmed two ways: Keeper's 27-mode computation (the count is norm-independent) + the audit of the corpus's own `BST_Shannon_Alpha_Paper.md` (**K676: that paper RELOCATES** — hides the norm-weighting in the Bergman "capacity-achieving distribution" + leans on the retired Wyler ¼ numerology; **do NOT resurrect it as a derivation**). The **0.036 is the separate norm-weighted curvature piece** (T2133 heat-kernel; κ_Bergman=−n_C). The old paper's error was conflating the two; Casey's reframe correctly separates them.
- **THE MATRIX RAN — result ≠ I (K678, `scratchpad/alpha_born_measure.py`).** The 27×27 Szegő overlap under the invariant Born/c_FK measure is DIAGONAL but **NOT ∝ I**: charge-block norm² {±2:1, ±1:1/5, 0:8/175 & 1/35}, a **35× spread** (numerics = analytic S⁴ moments). **The "= I on the boundary" milestone is REFUTED and RETIRED — do NOT cite "= I."** The boundary can't democratize the 27.
- **WHY + where democracy lives (Keeper HYPOTHESIS, not corpus fact):** the 27 is an SO(7) irrep; equal-norm democracy is a Schur fact that lives on the **compact dual Q⁵ = SO(7)/[SO(5)×SO(2)]**, not the Shilov boundary (which carries only SO(5)×SO(2) → 3 blocks, independent norms → the 35× spread). This IS the group-theoretic content of the named-but-OPEN **Q⁵↔Shilov bridge lemma**.
- **THREE concrete routes to α=1/137 (none closed):** (a) **Grace's charge-operator BYPASS — FAVORED:** EM charge = SO(2) Cartan weight (T2470, integer, norm-independent) → coupling counts charges, the 35× spread is irrelevant, α = ratio of counts (the ≠ I result shows the norm-weighted alt gives a 35× mess, not 1/137, so α is probably NOT norm-weighted); (b) prove the Q⁵ bridge democratizes the 27 (SO(7) on Q⁵); (c) compute the F38/ρ-shift Bergman-vs-Szegő K-type weights (h^{−5/2} vs h^{−5/4}) = {35,21.9,5,1} (relocate, uncomputed).
- **Q2 (saturation bound) is OUT:** no bound forces 137 (Wallach bottleneck T1829 → n_C=5 & k=rank=2, NOT 137; 137 is a COUNT). Don't hunt a bound that isn't there.
- **λ (Higgs) same:** the 8 boundary-spinor modes need not be equal-norm on ∂; λ=1/8 rests on the count/charge-grading, NOT overlap=I. α↔λ unification survives via the count route (Elie F531/toys).
- **Casey's "gravity is the boundary condition for EM":** SUPPORTED in the SCALE sense (F66 candidate — EM on the conformal scale-free boundary → α is a pure dimensionless count; gravity/bulk supplies the Planck scale). This is the physical reason α is a pure number 137. NOT the measure (that's the gravity-independent Born rule — K677 correction).
- α stays **IDENTIFIED** until the Born-measure matrix comes out I + Cal sign-off. Closest it has ever been: one finite matrix, no external theorem.

## ★ EOD 2026-07-15 (16:56) + TOMORROW — finish the MIXING MATRIX early
**The day: α CLOSED (4π = descent Coulomb solid angle, K701) · muon BANKED 4→5 (K698) · curvature FORWARD (n_C/N_max: α 0.0004% + Higgs 0.02%) · m_τ forward · m_b=m_t/42 · the MASSES are DONE (20 params = the Σ's).** The finish-line run MISSED (PMNS≈0) — and it LOCALIZED the physics (K704, team-converged): **mixing is a DISTINCT object** (the eigenvector orientation U_L†U_L', NOT a function of the norms). No wall — we solved the masses and hadn't started the mixing, and mistook one for both.
**TOMORROW (early): finish the MIXING MATRIX.** Build the per-sector eigenvector-orientation/texture object (NOT more norms):
- **Lyra's first swing:** the **refraction rotation** (up/down, F548 index N_c/rank) → the **Cabibbo angle** (Gatto bridge sinθ_C≈√(m_d/m_s)). If it lands → the geometry-large-vs-small mixing story is real.
- Then **ℓ/ν = the d=5→d=4 projection + Majorana locus** (F413) → large PMNS; feed complex/directional z_k = r_k·(ρ̂/ê₁)·ω^{k−1} (F379/F384/F493) into Grace's machine → the six render.
- **The "physics matrix" (Casey):** M=UΣV† per sector — Σ=masses (radial, done), U/V=mixing (angular, tomorrow) — the whole SM as projections of D_IV⁵. Details: K704.

## ★ SOURCE OF TRUTH — the WORK-PACKAGE LEDGER (`Keeper_BST_Work_Package_Ledger_v1_2026-07-14.md`)
**Read the Ledger before working any object.** It has one verified work package per substrate object (26 SM params + m_e), each with derived-vs-assigned pinned, the objective classification, and the exact remaining work. Scorecard v0.3 + the Ledger are the ONLY authoritative tier sources — the data layer (`bst_constants.json`) and scoreboard (`bst_26_table.py`) are STALE (Grace: sync before outreach).
- **Mandate (Casey):** either MAKE PROGRESS or IDENTIFY THE APPROACH THAT FAILS — a cleanly-ruled-out approach is a success, not a loss. Report the failure precisely.
- **Cycle rule:** do NOT re-derive what the Ledger marks derived (the muon (24/π²)⁶ exists in F116/F117 — close the gaps, don't reopen). If a form/value oscillates ≥2×, STOP → escalate to Keeper.
- **Completion:** everything funnels through 3 enablers — [K-TYPE QUANTIZATION], [ENGINE C], [α KEYSTONE A] — + Majorana joints + the gen-1 anomaly + accepting the by-design endpoints. Finite, named.

## ★ ACTIVE WORK — ALL ITEMS, Casey's approaches (K687). LONG PULL: advance EVERY item.
Source of truth: `Keeper_BST_Work_Package_Ledger_v1` + `Keeper_K687` (Casey's A–F approach clarifications). Mandate: **make progress OR cleanly rule out the approach — both are wins.** Cycle rule: don't re-derive what's marked derived; if a form oscillates ≥2×, STOP → Keeper.

| Item | Owner | Casey's approach (K687) | Objective this pull |
|---|---|---|---|
| **α** | — | ✅ **COMPLETE** (4π residue trivial). α=1/137 DERIVED. | done; 0.036 optional precision |
| **Muon** | Elie | 3/8 **DERIVED** (compactness = 1/vol(S⁴), toy 4664; = Casey's boundary-passage/3-ball). Remaining gate: **FK Szegő absolute constant = 1** (boundary-normalization proof). | prove FK Szegő=1 → count 4→5, or name why not |
| **Charged leptons / K-type** | Lyra | **ONE-number spinor ladder** (½,3/2,5/2), same as neutrino; **matter is a SPINOR** — resolve via the **CONFORMAL ALGEBRA** (tensor→spinor map). Old (1,1)-2-form note re-opened. | pin the tower-climb to the F(4)-minrep source → forward |
| **Tau (m_τ)** | Elie/Lyra | **49·71 = BULK Weyl count; −√π = BOUNDARY 3-ball** (additive settled). Generations mirror cold/warm/hot. | evaluate both pieces forward [Engine C bulk+boundary] |
| **Up quarks / gen-1** | Grace/Elie | **The first generation INVERTS** — light up sits BELOW the down ground state (why it's so light); heavy up = down excitation. Dissolves the "cold anomaly." | show the inversion produces m_u; not a missing factor |
| **Neutrino masses** | Elie | **Two stable RESONANCES** (oscillations); m_ν1=0=ground. Derive {7/12,10/3}=(40/7) as resonance eigenmodes [linear algebra], NOT seesaw coeffs. | resonance-mode derivation of the two masses |
| **Higgs λ** | Grace/Lyra | **Follows from α-completeness**; form = **1/rank^{N_c} = 1/8** (resolves the 1/8-vs-√(2/5!) fork). m_H=v/2. | close λ via the 1/count law, form 1/rank^{N_c} |
| **CP (δ_CKM, δ_PMNS)** | Grace | **Do it in LINEAR ALGEBRA** — the explicit rep-vector build (F498-respecting), compute Jarlskog directly. | build → J; real→fails, complex→lands (can-fail) |
| **Majorana** | Cal+Elie | γ⁵ intertwiner construction + Cal co-sign → flips pred_004 (1–4 meV floor). | construct + co-sign |
| **m_b 6%** | Grace | RG-run b/d between the b and d scales. | close or bound the 6% |
| **Forks + hygiene** | Cal / Grace | Δm² fork (32.65/33/34); data layer DONE (Grace ✓); deprecated arctan√5 in play/ (Elie). | adjudicate / finish sync |

**Mandate: LONG PULL — keep working until EVERY item is advanced (progress or a clean-failure verdict).**

## ★ POST-PULL ASSESSMENT (K690) — CLOSE-ENOUGH vs MISSES
**Everything advanced.** Notable: **tau now FORWARD-ADDITIVE** (Elie 4665: 49·71 bulk Weyl + √π 3-ball boundary — K682's "reverse-engineered √π" SUPERSEDED, scorecard fixed); **muon** determinant closes 0.003%, 3/8 derived, FK Szegő const = 1 to **6 ppm** + forward-plausible (one Γ_Λ from 4→5); **charged-lepton ladder SOURCED forward** (Lyra: conformal raising operators; CATCH 1 resolved — Di spinor/Rac scalar/adjoint = 3 sectors of one supermultiplet); **Higgs λ=1/rank^{N_c}=1/8** (form resolved).

**CLOSE-ENOUGH-TO-CLOSE (15 — done or ONE bounded step, no research gap):** α, m_s, m_ν1, θ13, v, θ_QCD, m_t, sin²θ_W, α_s, m_e, m_c, m_τ, m_μ, charged-lepton addresses, Higgs λ-form. Bounded steps left: muon Γ_Λ, tau bulk-Weyl eval, Higgs 1.8% curvature [Engine C]; mixing overlaps [Lyra→Grace].

**THE MISSES — web-grounded + Casey's insights (K691/K692). m_b REFRAMED to ~1.6%; 2 real approaches left:**
| Miss | Grounded state | Approach (Casey/K692) | Refs |
|---|---|---|---|
| **m_b** | down-ladder b/d=840 is **19% low** (obs 1043); s/d=20 EXACT | **REFRAMED ~1.6%:** the down is the TRUE GROUND (d:s:b fundamental, gens 1-2 exact); the b's home is the **TOP: m_t/(C_2·g)=m_t/42=4113 MeV (1.6%)** (T1990/T2013). Adopt m_t/42 as the b's source. | F506, T1990/T2013, K691 |
| **up** (m_u/m_d) | BST 1/√g=0.378 vs obs **0.462 (18%, 4.2σ — a REAL miss)** | **Up = TWO ladders = a REFLECTION of the down ground** (light-up inverts below; heavy-up c/t excite; b↔top is the gen-3 image). **Derive the down→up reflection** (T₃ᴿ #418 / Peirce) → the light-up depth (×√(N_c/rank)) falls out. Don't fit (6/13, √(3/14) are fishing). | K687/K690, F507/F508, K401/K418, toy 4628, K691 |
| **ν m_ν2** (the "7") | Δm² ratio obs 33.6±1.7; 7/12 fine observationally, but "7" is NOT a mode | **m_ν2 ∝ √N_c = the BULK version of the tau's BOUNDARY √π.** Two resonances: m_ν3 ∝ 10 (bulk ℓ=2, Elie 4666) + m_ν2 ∝ √N_c (bulk √). Ratio 10/√3=5.77 → 33.3 ✓. **Retires 7/12** (√N_c has the mode structure). | K687, tau 4665, Elie 4666, F157, K691 |

**UNIFYING (Casey, paper-worthy):** √ corrections in TWO flavors — **boundary √π (tau) + bulk √N_c (neutrino)**, both from odd-dimensionality; and the **down/up reflection** (down=ground, up=2-branch reflection, b↔top).
**GATED (closing as the now-forward K-type lands):** CP magnitude (δ_CKM/δ_PMNS — Lyra→Grace linear-algebra J), mixing depths (V_us, V_cb mag, V_ub, θ12 overlap, θ23 octant).

## ★ 2026-07-15 MORNING LANDINGS (audited K693) + WHAT REMAINS TODAY
**Landed this morning:**
- **Tau — FORWARD** (Elie 4669): bulk Weyl EVALUATED (g^{N_c}=343 + 2^{C_2}·g^{rank}=3136 = 49·71) − boundary √π. Now derived-forward, not identified.
- **Neutrino m_ν2 ∝ √N_c** (Elie 4668): Δm²ratio = (2n_C)²/N_c = 100/3 = 33.3 (obs 33.6) — **RETIRES the fitted 7/12**; bulk √N_c + boundary √π = the odd-dim √-pair.
- **m_b = m_t/(C_2·g) = m_t/42 = 4.11 GeV** (Grace, 1.7%) — the b's home is the top; **miss closed.**
- **Charged-lepton ladder PINNED** (Lyra F544): energies 2,3,4 (electron Δ=(d−1)/2=2 in 5D, +1 per conformal raise); two axes clean. **Unblocks Grace's mixing.**
- **Muon 4→5: residue √rank·π² DERIVED & VERIFIED** (Elie 4670, Keeper re-derived) — but **c_S=1 is ASSERTED not proven → HOLD count at 4** (K693). Closest ever; one Born/Szegő normalization computation away (= part of the K358 "absolute scale" open program — NOT a quick win).
- **Up m_u/m_d = √(N_c/(rank·g))** (Lyra F545): UPGRADED fishing→block-sourced lead (√(N_c/rank) from color-crossing vs Cartan block sizes; proton stability = N_c>rank). **Premise "depth~√block-dim" is NEW/ungrounded** — needs ≥1 independent prediction (target-innocence test, K693).
- **Higgs λ=1/8, CP structure built** (Grace) — both wait on the Engine-C curvature / Lyra's depths.

**REMAINS TODAY (the unblocks + decisions):**
1. **THE BIG UNBLOCK — the mixing overlaps** (Lyra + Grace): compute the overlaps from the now-pinned addresses (2,3,4) → **CP magnitude + V_us + V_ub + θ23 octant + θ12** all fall out. This is the finish line for the mixing sector.
2. **Muon 4→5 decision:** the boundary-Szegő normalization = √rank·π²? (Elie/Keeper; part of K358). If proven → 4→5.
3. **Up premise grounding** (Lyra): ground "depth~√block-dim" on an independent case, or hold as lead.
4. **Cal's Majorana co-sign** (reading up first — 12-day-stale katra, correctly loading K673/F537/4659 before rendering).
5. **Engine-C curvature** (Higgs 1.8% + α 0.036, optional precision). **Neutrino: why √N_c** (the bulk-color amplitude).

Source of truth: **Work-Package Ledger** + K687/K691/K692/K693.

## ★ 2026-07-15 PM — the PROJECTION framing (K696/K697) + two sharp finish-line findings
**THE APPROACH (grounded, K697):** leptons/quarks are **Dirac fermions REFRACTING across the bulk→boundary interface = the holographic PROJECTION (2D boundary ← 3D bulk).** Grounded in TWO real fields: Dirac-fermion optics (graphene: Snell-Descartes+Fresnel, pseudospin=spinor half-angle="half Snell", Klein tunneling=evanescent="held in the prism", refractive index ∝ energy) + holography (AdS/CFT, BST's SO(5,2)⊃SO(4,2)). **arcsin(rank/N_c)=arcsin(2/3)=arcsin(2D/3D)=41.8°** = the projection angle; **N_c/rank=3/2 = the refractive index** (Elie's muon obstruction). **Electron=2D clean / muon=critical-angle marginal / tau=3D clean = the projection ladder.** Casey's down-e/up-μ symmetry = the full description of lepton projection → **makes 2D→3D projection TESTABLE.** Charge=exact 2D shadow, mass=loose 3D refraction.

**FINDING 1 — MUON 4→5: CONDITIONAL PASS (K698). Count moves 4→5 — the muon is FORWARD-DERIVED.** Elie made c_S=1 COMPUTED (4676: the Shilov measure 8π³/3 divides out under the Born probability measure → Hardy constant mode unit-norm → c_S=1) + the optics route confirms (4677: N_c/rank=3/2=the refractive index, refracts away, K697) + residue √rank·π² derived (4670) + formal-degree ratios clean (4674, Casey's 3-lepton idea). m_μ/m_e=(24/π²)⁶ forward. Condition (referee-facing): the constant-mode identification, stated explicitly. **Charged-lepton sector COMPLETE (electron anchor, muon forward, tau forward-additive).**

**FINDING 2 — the mixing needs BOTH SECTORS' depths (Grace's catch).** A single sector's overlaps aren't the mixing: PMNS = U_charged†U_ν, CKM = U_u†U_d — the RELATIVE rotation of two sectors. Lyra's charged-lepton depths {1,2/3,1/2} gave θ13≈0.28 (obs 0.022) — the tell. Grace did NOT report the fabricated angles. **So the FK overlap integral (Lyra+Elie) must deliver BOTH sectors: neutrino depths (for PMNS) + up & down depths (for CKM).** Grace's F498 machine VERIFIED and armed.

## ★ THREE DIGS (2026-07-15 EOD → next) — Casey directive: alpha, k-type depths, finish the 25
**Curvature now FORWARD (Elie 4678): n_C/N_max closes α⁻¹=137.0365 (0.0004%) + m_H=125.22 (0.02%), two-target. Up FULLY GROUNDED (Lyra: 3/2 index = bulk/boundary dim ratio, 3 color-crossing / 2 Cartan). 14 banked / 6 strong / 6 behind ONE gate.**
| Dig | What | Owner |
|---|---|---|
| **1. MIXING — the run MISSED, and it LOCALIZED the physics (K704 + team convergence). MASSES done; MIXING is a DISTINCT object.** | **The run gave PMNS≈0 — NOT a bug.** M = U Σ V†: **Σ = masses = the radial norms {N_i} (DONE — that's the 20 banked/strong).** **Mixing = U_L†U_L' = the relative EIGENVECTOR ORIENTATION between sectors — and it is NEVER a function of the norms.** We projected v↦\|v\| for the grounds (correct for masses) and threw away the DIRECTION (which carries the mixing). Lyra's "broken self-check" + Grace's run + Keeper K704 all gave the same ≈0 → the geometry telling the truth, not 3 bugs. **THE FIX (build the eigenvector/texture object, not more norms):** up/down mixing = the **refraction rotation** (F548/F549, index N_c/rank — small → small CKM; Gatto bridge sinθ_C≈√(m_d/m_s) ties it back to norms via √-ratios); ℓ/ν mixing = the **d=5→d=4 projection + Majorana locus** (charged→chargeless, big reorientation → large PMNS, F413). **Vol 57 = build the per-sector eigenvector orientation.** First swing (Lyra): the refraction rotation → the Cabibbo angle. | Lyra (texture/refraction) + Elie + Grace |
| **2. ALPHA — CLOSED (CONDITIONAL PASS, K701)** | ✅ The 4π = the descent's 3D Coulomb solid angle (Grace DIG 2 / K699): α = shell-capacity (137) projected to 3+1 via SO(5,2)→SO(3,1); flux through Vol(S²)=4π. **No free normalization left** — 137 (capacity) + 4π (descent solid angle), both geometric; + forward curvature n_C/N_max. Condition: it IDENTIFIES the 4π (not re-derives Coulomb). **α is done.** | ✓ |
| **3. FINISH THE 25** | Up index → forced (Lyra, one step — the 3/2 = bulk/boundary dim ratio is grounded); neutrino √N_c amplitude → forced; consolidate m_b/m_H/m_d. The last 6 land from Dig 1. | all |

**Parallel independents (run alongside):** Cal — Majorana co-sign (γ⁵ intertwiner + cold-read K673/toy 4659/F537 → flips pred_004) + adjudicate the Δm² fork (32.65/33/34) + the θ12/τ/λ forks. Grace also — sync the stale data layer (`bst_constants.json`, `bst_26_table.py`) to scorecard v0.3 before any outreach.

---

## α — NEARLY PROVEN (K680/K681). Scale falsifier PASSED. Now WIDEN the front.
**α reached nearly-proven today** (identified-strong): count 137 derived (compact-boundary mode-count, over-determined 3 ways); democracy computed (S¹ Haar unit-norm winding = charge); **scale falsifier PASSED (Grace, K681): 1/α=137, no stray 2π/c_FK/4π.** The "why" completed: finite=COMPACT boundary → capacity → α=1/capacity (Lyra F535, why SM can't & BST can); primeness forces the count+correction shape (Elie 4657). Physics-framed: a target-innocent falsifiable prediction that SURVIVES. Residue to fully-derived: the 4π convention is definitional (low-priority paper-writeup item). See `Keeper_K681`, `BST_Why_Alpha_Finite_Capacity`. **Casey's gate met → schedule the wider parallel front (Engines B, C, Majorana, cleanups).**

## PARALLEL LANES (Tuesday 2026-07-14) — WIDE FRONT now that α is nearly-proven. Map: `notes/Keeper_Parallel_Work_Schedule_Approaches_v1_2026-07-14.md`
The open set collapses onto **3 engines + independents** (13 non-derived items → shared machinery):

| Lane | Engine | Owner | Unlocks |
|---|---|---|---|
| **B — complex generation-state build** | B | Grace + Lyra + Elie | Build the 3 generations as explicit SO(5,2) rep VECTORS (positions + phases), diagonalize the 4 flavor matrices → **V_ub, δ_CKM, J, PMNS θ23 octant, θ12 form, δ_PMNS, ν-coeffs**. CP genuinely CAN FAIL (J=0 for real peaks, F498). Elie's CP scaffold: complex ℤ₃ phases + mass hierarchy → J≠0 (both needed). |
| **C — boundary-integral capability** | C | Lyra + Elie | The one capability BST has never exercised (rep-theory shortcuts always canceled the normalization). Evaluate the F323 N(w)^{n_C/2} integral → **τ √π build, m_d/m_u absolute anchor, α's 0.036 curvature term** all wait on it. |
| **Majorana closure** | — | Cal + Elie | Cal cold-read K673 + CO-SIGN; Elie the explicit ν=1/2→9/2 **γ⁵ intertwiner** (NOT σ_BF) → flips **pred_004** to a 1–4 meV 0νββ floor. Near-term experimental win. |
| **Neutrino coeffs {7/12,10/3}** | — | Elie | CHEAP NEGATIVE CHECK FIRST: do d(ν)-ratios yield 40/7 at all? Then the Bergman Majorana-matrix diagonalization on d(ν)-weighted ν-strata. FITTED currently — don't dress as derived. |
| **Cleanups (cheap, parallel)** | — | Keeper + Grace | Deprecate the old arctan√5 CP paper (contradicts F498's proved J=0); adjudicate the 33-vs-32.65 ν-ratio fork; Cal-ratify the "bare ribbon = current mass" premise; compute \|U_e2\|² forward to settle θ12 (3/10 vs 42/137); RG-run m_b's 6%. |
| **α cleanup + audit seat** | A | Grace + Keeper | α is nearly-proven; only the 4π convention as an independent derivation remains (low-priority paper item). Keeper holds the "fully derived" signature + audits every landing on B/C. |

**Disciplines (armed):** (a) **CP can FAIL** — J=0 for real peaks proved (F498); Engine B is a genuine falsifier. (b) **θ12 DEMOTED** BANKED→IDENTIFIED (Grace: \|U_e2\|²=3/10, the 42/137 was a near-coincidence). (c) **ν-coeffs FITTED** — Elie's cheap negative RULED OUT the formal-degree route (toy 4658: only ratios 1,14,1/14); fiber-overlap the only lead. (d) **gen-1 up cold anomaly** stuck — hold-open. (e) old arctan√5 CP paper deprecate. (f) **Engine B J-crux (Grace)**: needs the explicit SO(5,2) rep-vector build separating real geometry from rephasing-invariant phase — a 2D encoding conflates them and violates the proved J=0 control.

## TWO KEEPER CORRECTIONS this turn (K682) — read before banking mixing/mass
1. **τ √π is REVERSE-ENGINEERED, not forward.** m_τ/m_e DEMOTED "PREDICTED forward 0.0000%" → **NEAR-FORCED**: the −√π was added to fix 49·71's 7.7σ then retro-justified; the 0.0000% is the fit-target, not an evaluated integral. The √π-PRESENCE is forward (odd n_C, F157); the exact coefficient is the open Engine-C integral. Excellent lead, not forward-exact.
2. **K-TYPE QUANTIZATION is the deep shared blocker** (distinct from Engine C). The generation addresses (a,b) are ASSIGNED not forced; per K398 it gates M_ν + quarks + τ SIMULTANEOUSLY, per K291 it's ~2→~15 forced params. **Cabibbo 1/(2√5), V_ub, ν-coeffs, the depths {r_i} are all "derived MODULO the K-type address" = conditional, not forward.** Present them as conditional. This is the real frontier — a selection principle (particle → discrete address), an open RESEARCH problem, NOT a bounded build.

## HEADLINE — the odd-dimensionality unification (F536 + toy 4659; `BST_Odd_Dimensionality_Unification`)
One parity fact — **n_C=5 is odd** — generates FIVE features of matter via five distinct mechanisms: spin-½ (F504), CP violation (F533), the √ in quark mixing (F536), the Majorana neutrino (toy 4659, R=γ⁵ built), the √π in the tau (F157). Target-innocent (about the parity of 5). The QUALITATIVE five-fold unification is the strong forward result ("why matter is the way it is"); three QUANTITATIVE values (Cabibbo value, J, −√π coefficient) stay gated on K-type quantization + Engines B/C.

## K683 UPDATE — K-type frontier: neutrino landed, MUON is the bounded win, c_FK ≠ absolute-scale fix
- **Neutrino K-type address landed FORWARD (Lyra F537):** ν=½ (fermion→half-integer + ground→minimal) → forces Majorana from the address. First forward K-type brick — but the EASY one-number corner; does NOT de-risk the two-number (k,m) map for charged fermions/quarks (the months-resistant deep problem).
- **THE BOUNDED NEAR-TERM WIN — the MUON (Elie + Lyra):** its address is ALREADY pinned (1,1) via F361 (c=5/2−ν=m). Engine C can now evaluate its **boundary Szegő residue at ν=3/2**; **if it returns unity → muon derives forward** (strict count 4→5). Bounded, address known, evaluator up (toy 4660). NOT automatic (electron carries rational 9/16 — verify, don't assume).
- **c_FK does NOT pin Elie's absolute scale (K683) — Elie's "not pinned" STANDS.** c_FK=225/π^{9/2} is derived (T2442) but it's the BULK-Bergman object (cancels in ratios); the muon needs the BOUNDARY Szegő residue (different object, π¹² vs π^{9/2}). And "absolute scale" = TWO things: (i) dimensionless boundary residue (resolvable for KNOWN addresses via Engine C) vs (ii) dimensionful MeV anchor (genuinely open — BST may be intrinsically RATIO-ONLY; m_e external). Don't conflate.
- **τ √π:** presence forward (odd-n_C), but Elie's ratio form √21·√π/16 COMPETES with the additive 49·71−√π — two forms = numerology tell. Engine C now up → evaluate the actual coefficient forward, reconcile the forms. Stays NEAR-FORCED (K682).
- **Engine B ready (Grace):** the rep-vector construction now passes the F498 control (real coords → J=0 exactly; CP survives via genuine complex coords). Waits on Lyra's forced depths. Lanes meet at the depths.
- **Notational gap:** (a,b)/(k,m)/ν used interchangeably without a dictionary — pin one before the two-number map (genus-flip precedent).

## K685 — muon-slot deep dive: 2 UNBLOCKS + 2 CATCHES (read before any muon bank)
- **UNBLOCK 1 (Lyra):** the canonical-mode premise (F539) has a bounded CLOSER — **define "localized on stratum Σ" = the current [Σ]; Poincaré/Thom → K-type = Λ^{dim Σ}(TΣ), an antisymmetric top form → structurally excludes the symmetric (2,0).** Forces the muon (1,1); OVER-DELIVERS (also closes electron: bulk Λ⁵(V₅)=(0,0)). FAILS for τ (dim-0→Λ⁰ trivial) — τ needs the separate cone-tip route (F517/F368).
- **UNBLOCK 2 (Elie):** the muon determinant is ALREADY substantially built — F116 (finite so(4) det (24/π²)⁶, 3 of 4 ingredients rigorous), F117 (π¹² DERIVED from the boundary Szegő residue at the unitarity bound), F115 (the object map: e=LOG, μ=det, τ=Tr-log). **toy 4662 re-opened it — reconcile against F116/F117/F115.** The muon VALUE is ~ONE un-derived factor from forward: the flat→sphere **3/8** normalization (F117's flagged soft spot). d_τ/d_μ=64=2^{C_2} is already the multiplier inside the det (aids μ not τ).
- **CATCH 1 (severe, unowned):** K539/Cal #402 says lepton matter is the **Δ=2 Di SPINOR** of the F(4) minrep. The (0,0)/(1,1)/(2,0) discussion is INTEGER TENSORS — so (1,1) may be a **dressing on a fixed spinor, not the muon's K-type.** "Muon=(1,1)" and "muon=spinor" are unmerged. **Settle before any muon-slot bank.** [Lyra]
- **CATCH 2 — RESOLVED (Keeper K686):** NOT an inconsistency. The mixing lane (dims 5/2/0) is the SPATIAL SUPPORT stratum; the mass lane (dims 0/3/6) is the DEGENERACY-LOCUS dimension (which one-loop object computes the residue). Different structures, both true per K-type, a naming collision. Fix: extend F538's dictionary to separate "support stratum" from "degeneracy locus." F539 template unaffected (the lanes COMPOSE: support→K-type→residue).
- **Bank discipline:** no muon-slot bank until CATCH 1 settled AND the 3/8 factor derived. Count HOLDS 4 (Elie refused to fake unity — right call). See `Keeper_K685`.

## Engine C (clarified, K682): bounded build + FIRST normalization-layer test
Every banked result survived because it was a ratio/Schur-scalar where the absolute normalization CANCELED. Engine C is the first task needing the absolute constant → the first real falsifier of BST's normalization conventions. Build it (worked precedent: toy_4403 exact Shilov Beta moments) — it banks the light-quark anchor + τ coefficient forward, OR usefully breaks the convention layer. But it gives scale only for KNOWN addresses; it does NOT close mixing (that's K-type quantization).

---

## LAST TASKS — the three live builds (EOD window open ~5pm; finish or fold at Casey's call)

**Complete-items writeup:** `notes/Keeper_26_Parameter_Scorecard_v0.1_2026-07-12.md` (the referee-safe consolidation — tiers are the deliverable).

| # | Lane | Owner | What |
|---|---|---|---|
| **0** | **CASEY'S CONJECTURE: the α-generator IS the Big-Bang generator — CORE CONFIRMED (3 witnesses); (3,1) is the multi-step budget** | Elie + Lyra + Grace | **CORE CONFIRMED (2z), 3 independent matrix witnesses (F526, Elie, Grace-from-scratch):** J(V₅→V₂) is a genuine non-compact boost (e^θ, preserves Lorentzian (5,2), NOT the compact circle) = the SAME generator that forces α's 15→27; turning it on makes time. Corpus's `BST_Big_Bang_Unfreeze` named the WRONG (compact SO(2)) generator — **FLAGGED for correction.** **KEEPER CORRECTION: one boost lands (6,1), NOT (3,1)** (Grace's accurate check; Elie overstated). Budget: (7,0) → 1 boost → (6,1, time born) → both V₂ boosts → (5,2)=SO(5,2) → descent SO(5,2)→SO(4,2)→SO(3,1) (Casey #14) → physical (3,1). **REMAINING: the full (3,1) multi-step run** (both boosts + descent). **PAYOFF: gives the α Lemma-A residual a PHYSICAL handle** (boundary conformal because the substrate opened via this boost). Conjecture, core confirmed, not banked; α IDENTIFIED. Narrative layer stays Level-2. |
| **1** | **α forward derivation — F525 closed the combinatorial core; residual = a multi-MONTH rep-theory build** | Elie (lead) + Lyra + Cal | **COMPLETION DISTANCE (2aa): the 137 residual = Knapp–Wallach genericity + FK convergence + ρ-shift unitary normalization (T2359 I→D), importing external Knapp–Wallach 1976 / Faraut–Koranyi 1990 applied to D_IV⁵ — ~3-4 months full D-tier. The Big Bang handle is a physical REASON the boundary is conformal, NOT a rigor shortcut (α's kernel descends from the CIRCLE's complex structure, not the boost). 0.036 exact = apply the already-proved T2133 heat-kernel machinery (in-corpus build). α = IDENTIFIED; months to derived, not afternoons.** Below is the original framing: | **DERIVATION of 137:** 137 = 135 + 2 = SO(5) piece (P_{Q⁵}(rank)·n_C = 27·5) + SO(2) piece (rank). Bridge (Elie 4641 + Lyra F520): 27 = Sym²₀ SO(7) = a boundary Szegő trace **Tr(Π_rank)=∫_Š S_rank dμ_inv=27** (Hua/FK duality) — **T1940-safe (a COUNT=dim, not a Casimir eigenvalue).** **PHYSICAL FRAMING (Casey):** 137 = **135 "transport" (SO(5) bulk) + 2 "contact with the continuum" (SO(2)=EM, PROVED T2470)**; α=1/(couple 1 part to 137 modes). **0.036 = boundary-curvature residue** n_C/N_max=5/137 (κ=−n_C) — candidate reconciliation of T2001-running vs F489-Wyler (task: show V_Wyler = curvature integral = n_C/N_max). **AUDITED + self-corrected (K675, 2026-07-13); α = IDENTIFIED. Narrowed to TWO precise lemmas (retractions: F522 "α is a square", the gate-b trace demotion, n_C/N_max-as-series — do NOT cite as closures):** **LEMMA A (count):** prove the level-rank Hardy K-type WITH the FK ρ-shift = Sym²₀(V₇)=**27, not the naive 15** (Elie 4644: naive = 14+1). **Corpus lever: the ρ-shift = the (1,1) DUAL-ρ shift** (compact ρ_SO(5)=(3/2,1/2) → conformal ρ=(5/2,3/2), diff (1,1); Casey Principle 16/K231c); subleading FK correction already computed (T2359). Build = Knapp–Wallach genericity rigor (Gap #4). *Caution: the 12 extra modes (27−15) are corroborated ONLY internally (F520/F521+T2470); FG confirms the 14 but NOT the 10/±2 — the target itself is I-tier.* **α STRATEGY (Keeper redirect, corpus read): DERIVE α AS TWO CLEAN PIECES — (137 from the mode-count, Lemma A) + (0.036 from boundary curvature) — and let the Wyler Vol^(1/4) be a CONSISTENCY CHECK, not a derivation path.** The Wyler 1/4 is a NUMEROLOGY TRAP: FOUR incompatible readings, none derived (Plancherel-asserted / 1/(2q) fiber / 4D-spacetime / rank²) — exactly Robertson's ground. RETIRE "Lemma B = derive the 1/4"; REFRAME as **"derive the 0.036 curvature correction"** (κ_Bergman=−n_C pinned, n_C/N_max leading, separate layer, does NOT touch the 1/4) [Grace]. Mode-count (Lemma A) gives 137 with no fractional power (T1940-safe). |
| **2** | **CKM V_us — near-saturated LEAD (AUDITED: not forced)** | Lyra + Grace | **AUDIT (Keeper): V_us = 1/√20 = 0.224 (0.4%) is a near-saturated LEAD, NOT forced.** Lyra's Cauchy–Schwarz gives the BOUND (|V_us| ≤ √(m_d/m_s)) + the near-value; the EQUALITY needs the cross-kernel to SATURATE (M₁₂=√(m_d·m_s)), which holds iff down/strange are parallel/rank-1 — they're NOT (different radii {1,3,5}). The **actual F84/K264 kernel gives K₁₂=(3/4)⁵=0.237** → V_us≈0.053, 4× too small (grace_F483). The Fritzsch texture-zero (d(5/2)=0, mass≠mixing per K674/F110) relocates but doesn't escape the crux. **HOLD as lead — don't force the saturation the geometry contradicts.** Correctly tiered by 3 authors (F523/grace_F483/grace_CKM). |
| **3** | **Majorana: Cal co-sign + γ⁵ intertwiner** | Cal + Elie | All 3 gates addressed (K673). Cal cold-reads; Elie constructs the intertwiner. On completion pred_004 flips → firm 1–4 meV floor. |
| **2** | **Tau boundary integral (a BUILD)** | Lyra | BST's FIRST evaluated boundary integral. Shilov leg (3136) via toy_4403 Dirichlet-moments; interior (343) + cone-tip −√π = build. Casey's 3-ball: a=N_c=3 is a banked theorem (T2511/F368); NEW = the explicit S¹→3-ball blow-up (via V₁₂ transverse Peirce space; friction: T2511 "relabeling not growth") + the 4/3=V(B³) normalization (compatible with the K296 formal-degree caution). |
| **3** | **Majorana: last joint + Cal co-sign** | Elie + Cal | Elie: construct the explicit γ⁵ intertwiner (chirality = shadow reflection). Cal: cold-read K673 (is "negative formal degree ⟹ no state" airtight?), then pred_004 flips in the verification doc. |
| **4** | **Boundary-integral capability (seed)** | Elie + Lyra | The tau build IS the seed — frame the ν=0 cone-integral technique as reusable (retires the open Š³ N⁻⁶ integral, etc.). Makes the next boundary number a retrieve. |
| **5** | **Consolidation (outreach)** | Keeper | The 26-scorecard as one coherent fermion-sector result. |

**Secondary:** neutrino mass mechanism Majorana-side (Elie — done: masses confirm Majorana); m_d absolute anchor; Higgs λ=1/8 (HELD as lead, don't fish). **Held open, DON'T fit:** c/u cold step. **Wall:** CP's Jarlskog J.

**Disciplines armed:** CKM's load-bearing gate is forcing {r_i} target-innocently (F490 — don't read them off the observed angles). The tau −√π must come FORWARD (it was reverse-engineered once). The Majorana flip stays "strongly favored" until Cal co-signs + the intertwiner lands. Don't let "nearly done" become over-claim: the mixings are genuinely open; m_e and the RG runners are by-design, not failures. A triumphant number isn't a finding until you've verified it isn't an artifact.

---

## DETAILED LANDINGS LOG (07-12) — archival; synthesis is in the results note Sections 2a–2m

## MORNING 2026-07-12 — corpus intelligence (Keeper research pull, Sun 08:45 EDT)

*Casey asked for the most-informed pull: read the corpus on the scheduled lanes, the neutrinos, and the full table of 26. Result: the machinery for the three lanes mostly already exists (reuse, don't rebuild), the neutrino sector is much richer than "one hole" (but carries a contradiction to resolve), and there are 2–3 clean new derivable items.*

### Machinery the three scheduled lanes can REUSE (don't rebuild)
- **Koide gate (λ_singlet = λ_traceless):** `play/toy_3711` already runs Schur's lemma on a K-invariant Bergman-norm operator → one scalar per irrep (= ‖V‖²_Bergman = 3π/2^g). **Lift that argument onto the generation irreps 1 ⊕ 2.** Strata↔particle assignment already pinned in `notes/Keeper_K294...`: electron = bulk (generic rep), **muon = Cartan-slice (ν=3/2 Wallach degeneration), tau = Shilov points (ν=0)**. So the strata overlaps are half-specified — compute λ_singlet, λ_traceless as Bergman overlaps at these three. FK norm engine: `play/toy_3689`, `play/toy_3695` (‖f‖² closed forms).
- **Deep-bulk overlap (m_u + m_d):** exact radial law already built — `play/toy_4620`: peak r_n² = (2n+1)/(2n+1+2α), ⟨1−r²⟩ = (α+1)/(n+α+2), n=0-ready (at α=n_C=5, n=0 gives 6/7). Deepest-bulk normalization K(0,0) = 1920/π⁵ derived D-tier in `notes/Keeper_K264...`. **The one real gap:** the n=0 constant-mode overlap → m_u closed form (the 22% hole). Casey's two-address reading tested in `play/toy_4624` (leans no).
- **All three share ONE object:** the Bergman kernel of D_IV⁵ at the three Korányi–Wolf strata (K287/F84 — "three levers = one kernel, three evaluations").

### Neutrino sector — the corpus HAS a lot (banked, but with one contradiction to resolve)
- **BANKED masses (seesaw m_i = f_i·α²·m_e²/m_p, M₀ = 0.0148 eV):** m_ν1 = 0 (Z₃-protected), m_ν2 = (7/12)·M₀ = 0.00865 eV (0.35%), m_ν3 = (10/3)·M₀ = 0.0494 eV (1.8%); **Δm²₃₁/Δm²₂₁ = (40/7)² = 1600/49 = 32.65 (pure integer, 0.3%)**; Σm_ν = 0.058 eV; normal ordering. [const_061/062, T340/T341, pred_003; `notes/BST_Neutrino_Predictions.md`]
- **BANKED PMNS:** sin²θ13 = 1/(N_c²·n_C) = 1/45 (0.9%, D); sin²θ12 = (N_c/2n_C)·cos²θ13 (0.06%, D); sin²θ23 = ((n_C−1)/(n_C+2))·cos²θ13 (0.4%, D); lepton Jarlskog J = 5.16×10⁻³ (1.4%, I). [const_022–024, T330–332]
- **⚠️ CONTRADICTION TO RESOLVE (Keeper flag):** the banked layer says **Dirac / no-0νββ** (pred_004, the *sharpest* falsifier — |m_ββ|=0, B−L conserved, ν/ν̄ by Hopf-fiber ℤ₂). The newer frontier (Lyra F144/F146/F147/F148/F374/F413) says **forced Majorana** (no ν_R from holomorphic parity; Weinberg operator; used to explain CKM-small/PMNS-large). **These cannot both stand** — this is a consistency issue that flips the sharpest banked prediction.
- **Mechanism leads:** zero-winding/zero-charge lightness (the "remainder"); Casey's **"uncommittable residue"** (F167/F166/F170) ties the ν scale to Λ (the meV coincidence — ν = local face, Λ = integrated face of one residue); F148 mild-hierarchy (all three cluster at the ν=1/2 sub-unitarity edge → ~6–30× spread, not the 3500× charged-lepton spread); F457 (ν scale is derived *relative to m_e*, not an independent 4th anchor).
- **⚠️ Also to reconcile:** 2–3 competing banked formulas per PMNS angle in the same JSON; three different δ_CP values (3π/7 vs 12π/7 vs π). Pick conventions, pin to source.

### TABLE OF 26 — current disposition (scoreboard `play/bst_26_table.py`)
- **DERIVED/BANKED (~9–10):** θ_QCD=0, PMNS θ13 (1/45), PMNS θ12, δ_CKM, **m_t, m_c, m_s (F506), v (F511)** [this week], α (mechanism); m_μ/m_e near-forced (Koide K672).
- **IDENTIFIED (~9):** m_τ/m_e (49·71), m_d, m_b, CKM θ12 (9/40) / θ23 (36/869) / θ13 ((1/3)⁵), PMNS θ23 (4/7), **m_H (125.1, 0.12%, form pending)**, sin²θ_W (3/13, runs).
- **OPEN (~7):** m_e (irreducible anchor), m_u (n=0 soft), α_s (RG runner — terminal NEG), δ_PMNS (unconstrained lead), m_ν1/2/3 (banked forms but mechanism contested).
- **Terminal-by-design:** α_s, sin²θ_W are RG runners (honest negatives, not fixed numbers); m_e and v are the irreducible dimensionful anchors (now essentially ONE, m_e via the gravity route).

### NEW derivable items for the board (beyond the three scheduled lanes)
1. **m_H (Higgs mass) — best new target.** IDENTIFIED at 125.1 (0.12%), "form pending" — and **v is now forced (F511)**, so chase m_H via the quartic λ (m_H² = 2λv²): is λ a forced substrate ratio? [Lyra]
2. **Neutrino MECHANISM resolution (Dirac vs Majorana) — Keeper consistency lane.** Decide which layer stands; it flips pred_004 (the sharpest falsifier). Reconcile the banked seesaw masses with the winding/residue picture. [Keeper + Cal + Lyra]
3. **δ_PMNS + PMNS/CKM θ23 tightening** — δ_PMNS is an open lead (DUNE-constrainable); PMNS θ23 (4/7, 4.9%) and CKM angles are identified, candidates to force. [Grace/Lyra]
4. **Top α-correction reconnection (Casey prompt 07-12) — a live thread on an item we thought closed at 0.78%.** Corpus (`bst_constants.json:1468`, T2009) already has **m_t = (1−α)·v/√2 = 172.75 (0.03%)** — better than F509's v/√2 (0.78%); the residual is the α-correction, not scheme. **Structural lead:** y_t = 1−α (T2009) + y_c = α (Elie 4621) ⟹ y_t + y_c = 1 ⟹ **m_t + m_c = v/√2** (0.03%) — top and charm partition the boundary mode at α; the top's deficit-from-saturation IS the charm. Verify: y_t = 1−α as the charm-partition mechanism; m_t + m_c = v/√2 as forced. Cal #27 armed (α small → "1−α≈1" nearly free; the content is that the deficit is *specifically* the charm's α-shell). Cross-check handle: m_t/m_b = 42 = C₂·g (T1990, D-tier). [Elie/Lyra]

### 07-12 LANDINGS (midday) — record

- **UP HOLE DISSOLVED (Elie 4628):** m_u/m_d = 1/√g = 0.378 → m_u = 1.77 MeV, exact at n=0, ~1.5σ inside the 20%-measured value. The "22%" was vs a central value alone. 1.77 = bulk address, 2.16 = production address. I-tier, target-innocent.
- **KOIDE SCHUR SHORTCUT FAILS (Elie self-retraction, K672 updated):** gen irreps ≠ K-irreps (K294 nested Wallach flag); λ_singlet=λ_traceless is dynamical, not Schur-forced. Real gate = degenerate-rep Bergman norms at ν=0, 3/2 (Lyra's K294 lane). Koide verdict unchanged (CONDITIONAL FORCED).
- **DATA-LAYER HYGIENE (Grace):** wrong banked entries fixed — solar θ12 canonical → 42/137 (0.14%, was falsely "0.06%"); θ23 both octants pinned (DUNE); **δ_CP was reverse-fit → 3π/7 and 12π/7 RETIRED, δ_CP now OPEN**. Data layer un-frozen + this week's banks synced. Flagged for Cal count-reconcile.
- **HIGGS (Lyra):** λ = 1/2^{N_c} = 1/8 → m_H = v/2 = 123.1 (1.7%). I-tier lead (quartic = 1/boundary-spinor-dim), NOT a bank (fishing risk flagged).
- **DIRAC/MAJORANA (Lyra F512 → Keeper lane):** possible INTERNAL inconsistency (Dirac needs ν_R vs banked no-steriles). Reduces to Q1 (does F144 "no ν_R" hold on the spin-½ tower?) + Q2 (Five-Absence scope — Keeper: forbids extra *flavors*, not the RH chirality; Q1 is the decider). If F144 holds → Majorana → pred_004 flips to 0νββ at 1–4 meV. **HOLD: neither prediction to referees until Q1 settles; Dirac flagged suspect.**

### 07-12 LANDINGS (afternoon) — record

- **DIRAC/MAJORANA → MAJORANA LEADING; Dirac null DEMOTED banked→contested (K673).** Q1 = YES from two independent derivations: Elie (shadow Δ→d−Δ spin-independent → F144 survives on spin-½ tower; ν = pseudoreal SO(5)=Sp(2) spinor → symplectic-Majorana, no ν_R) + Lyra F513 (the odd-one-out: ν is the only lepton at a generic point ν=1/2 *because zero charge* keeps it off self-complete points → no ν_R). Load-bearing: F512 internal flaw (Dirac needs ν_R vs no-steriles). **pred_004 relabeled** (verification-tests v4): normal-ordering, so >15 meV kills BST either way, 1–4 meV confirms Majorana-BST. **3 gates:** electron stratum (F144 ν=5/2 vs K294 generic bulk — DISAGREE, Grace, load-bearing for Koide too); rigorous RH-absence; ν=1/2-forced-by-charge.
- **TOP α-PARTITION VERIFIED (Elie) — up-type boundary sector closes.** m_t + m_c = v/√2 (0.007%); top's deficit-from-saturation IS the charm's α-shell ((1−y_t)=y_c=α). Charm=α, top=1−α, sum=1; x-check m_t/m_b=42. Top upgraded to 0.03%.
- **MORE HYGIENE (Grace, full 107-formula sweep):** const_140 (CKM Jarlskog) 96% off under same name as correct const_077 — do-not-cite flagged (serious landmine); const_021 (CKM γ=atan√5=65.9°) correct math, stale observed → fixed D-tier; θ23 front-runner 4/7 (0.3%, upper octant), 6/11 lower, DUNE decides.

### 07-12 LANDINGS (evening) + CORPUS UNBLOCKS

- **ELECTRON PINNED ν=5/2 (Grace) — gate 1 confirmed; it was a level-confusion, not an F144/K294 conflict** (K294 = Wallach level, F144 = position within it; both true). e 5/2, μ 3/2, τ 0 all forced.
- **MAJORANA GATES 2 & 3 worked (Elie, framework):** RH strictly unread at ν=9/2; ν stuck at edge 1/2 (Q=0, no shift). Two residual bolts (γ-intertwiner, charge→ν map). Flip still framework-tier, not firm.
- **KOIDE μ/τ residues pinned, closure BLOCKED (Lyra F514):** √π/2, 4√π/3, ratio 8/3; misses mass ratio ~1.5×, no electron closure. Won't fit.
- **CORPUS UNBLOCK — Koide:** use **d(ν)** (HC formal degree, DERIVED toy 4409), NOT the bare residue — F95/F110 proved the residue is the wrong object; the ~1.5× miss IS that substitution. Working map (toy 4408): muon = (24/π²)⁶ at 0.003%. **Real open piece = the TAU** (49·71 = g²(g+2^{C₂}), no forced vertex integral). For A²=rank: weight the overlap by d(ν).
- **CORPUS UNBLOCK — Majorana:** BOLT 4 (pseudoreal Sp(2) symplectic-Majorana) essentially DONE — **F331, verified SOLID**, reuse directly. BOLT 1 pieces present (γ⁵ T2471, Szegő kernel, Bergman-Dirac tower Paper118); LANDMINE: σ_BF vs γ⁵ (intertwiner is γ⁵ side). BOLT 2 caveat: +2/+1/−½ are SO(2)-WEIGHTS not electric charges (physical Q=−1,−1,−1,0); ν's already pinned by ρ-vector (F93) — justify from source.

### 07-12 LANDINGS (late) — Majorana near-forced, Koide muon closes, tau unblocked

- **MAJORANA NEAR-FORCED; DIRAC RETIRED (K673 update).** BOLT 1 RIGOROUS (Elie): d(5−ν)=−d(ν) → RH partner at ν=9/2 has NEGATIVE formal degree = non-unitary = strictly not a state (not "elsewhere"). BOLT 2 corrected (ν=1/2 forced by zero SO(2)-weight, ρ-vector F93). BOLT 4 reused (F331). **One joint held:** chirality = shadow-reflection (explicit γ⁵ intertwiner). **pred_004 → "Majorana strongly favored, 0νββ at 1–4 meV floor," pending Cal cold-read + the joint.** (Verification doc stays at "contested" until Cal co-signs.)
- **KOIDE muon closes via d(ν); tau explained (Lyra):** electron at ν=5/2 (d-zero anchor); muon = (24/π²)^{C₂} = 206.76 (0.003%, product); tau on Shilov boundary = SUM (bulk 64 + edge 7 = 71, ×g²=49). Muon leg solid; tau boundary-integral open (won't fudge).
- **DATA HYGIENE BOUNDED (Grace):** referee-facing = the 4 constants fixes; invariants/predictions not hiding hundreds more. Caught her OWN 339 false-positives twice (parser + field-semantics artifacts). Invariants needs a gen-logic audit, not a per-entry hunt.
- **CORPUS UNBLOCK — TAU (Keeper research):** her boundary-sum is ALREADY built forward (Toy 4208: g^{N_c}+g^{N_c−1}·2^{C₂}=49·71; Toy 4204 = g^{rank}·(g+2^{C₂}) = her exact form). **CRITICAL: 49·71 alone is 7.5σ HIGH — target is 49·71 − √π = 3477.23** (F157: √π = Gindikin Γ_Ω boundary residue). Path: F323 overlap integral at ν=0, split interior+Shilov regions, get counts + −√π together. GAPS: tau K-type seat (ν=0 vs ν=5, reconcile); Bergman exponent p (n_C vs g); the additive g (weakest leg). No integral exists yet — the BUILD.

### 07-12 LANDINGS (midday) — tau structure-set; the closure is a BUILD

- **TAU SETTLED (Lyra + Grace):** seat FORCED ν=0 (Elie antisymmetry: ν=5 mirror non-unitary), exponent pinned p=n_C=5 (Grace, kills g=7 mislabel), target **m_τ/m_e = 49·71 − √π = 3477.23** (PDG-exact). Muon closed; tau structure-set, integral-pending.
- **KEY (Keeper corpus read): the tau closure is a genuine BUILD, not a retrieve.** BST has NEVER evaluated a boundary integral to a number — all closed numbers (6π⁵, muon (24/π²)^{C₂}) came from Casimir/formal-degree shortcuts where the Szegő norm CANCELS in a ratio or is asserted =1. The tau at ν=0 is the FIRST absolute sum (343+3136−√π) where nothing cancels — it forces BST to finally EVALUATE the boundary integral. Recalibrate "one integral away": it's foundational, not quick. Retrievable: Shilov leg via toy_4403 Dirichlet-moments. BUILD: interior 343, and the cone-tip −√π residue (novel, never computed forward).
- **Grace: settle-first blockers cleared** (p=5, seat ν=0); hygiene bounded (invariants → gen-logic audit for auto-gen owner; caught own 339 tool false-positives twice). EOD-ready.
- **Elie: EOD staged/persisted** (toys→4633). Next-day lanes: neutrino mass mechanism (Majorana side), m_d anchor, support tau integral.

### STANDING NEXT-SESSION LANES (after mass sector) — Keeper assessment 07-12

The fermion MASS sector is nearly whole (down banked, up-type closed on α, muon closed, tau structure-set, ν masses banked, ν Dirac→Majorana near-forced). Candidate ADDS once it closes:
1. **Boundary-integral machinery** (foundational — the tau forces BST's first evaluated boundary integral; unlocks a whole class of "asserted count" results incl. 6π⁵). [Lyra/Elie]
2. **CKM sector FORCED** — the biggest remaining coherent block of the 26; quark mixing (3 angles + J) is identified not forced; build the quark analog of the lepton d(ν)/strata work. [Lyra/Elie]
3. **Higgs sector** — m_H via λ (the 1/8 = 1/2^{N_c} boundary-spinor lead), develop the mechanism. [Lyra]
4. **Consolidation for outreach** — the 26-parameter scorecard as a coherent fermion-sector result (paper). [Keeper]
5. **Gauge running** — reframe α_s/sin²θ_W from honest-negative to "derive the β-function running from the substrate." [Elie]

---

## [SUPERSEDED HISTORY BELOW — Friday 2026-06-26, kept for reference]

## Friday substantive summary (lepton sector reopened + hub built)

**Morning** (Casey "DON'T GATE INVESTIGATE"): Team had gated into "lepton masses probably irreducible." Casey directive broke the gating posture. Lyra arithmetic identity 24/π² = 2^{C_2}/Vol(S⁴) dissolved Cal #405 π¹² obstruction. Grace corpus reconnection F116/F118: both lepton masses already derived two weeks ago as so(4) curvature determinant + bulk/boundary mechanism — team had RE-DERIVED from scratch all week.

**Midday cascade** (audit chain at peak symmetry):
- Cal verified electron 9/16 directly from polynomial (ν=5/2 simple zero of d(ν))
- Cal #410 sharpened c_FK question: 1.303 not 1 (LOAD-BEARING not bookkeeping)
- Lyra absorbed: ratio cancellation resolves (c_FK is absolute electron scale, cancels in mass ratio)
- Cal #411 caught Keeper K543 over-projection: "count to 6" re-inflated tau → Keeper self-correction #14
- Lyra+Grace+Cal absorbed: matter ≠ Higgs (Cal #402 catch); Grace owned "I picked Shilov singleton, didn't force it"
- Elie 4400 unifying insight: Yukawas are 3-pt OPE coefficients (analytic, not algebraic)

**Afternoon hub-building**:
- Elie DERIVED d(ν) = (5/2−ν)(1−ν)(2−ν)(3−ν)(4−ν) from B_3 = SO(5,2)_C root system as Harish-Chandra formal degree over 5 noncompact roots — coefficients {5/2,1,2,3,4} FORCED root-system data, target-innocence CLOSED at polynomial level
- Cal #412 INDEPENDENTLY VERIFIED via sympy (zero difference)
- Cal precision (b) from K545: per-point operation must be EXPLICITLY STATED + SHOWN to be same or stratum-forced
- Casey "look on the discrete side" → Elie corpus reconnection toys 4197 (cell map) + 4199 (deposit-locus from Casey's "electron deposits on the spectral strip")
- **ONE-rule deposit-locus operation closure**: each generation deposits d(ν)-density on Korányi-Wolf stratum + integrates over locus; π forced by locus geometry (point/strip = π-free, sphere = π-ful); residue-vs-value forced by zero structure; three-gen count forced by rank+1=3 strata
- Elie tau forward+blind HONEST NEGATIVE toy 4411: √π has structural motivation but doesn't beat look-elsewhere; tau stays IDENTIFIED-tier
- Cal #418 STRONG affirm of operation-innocence; muon close-out cleared from Cal's blocker lane

## Honest tier state at Friday EOD

**Muon m_μ/m_e = (24/π²)⁶ at 0.003%**:
- d(ν) target-innocence CLOSED (Cal #412 sympy verified Harish-Chandra formal degree)
- d_μ = 15/16; d_τ/d_μ = 64 = 2^{C_2}
- π¹² = Vol(S⁴)^{C_2} geometric (six copies of Shilov S⁴)
- c_FK cancellation framed (Grace ratio argument)
- Operation-innocence STRONG CANDIDATE for closure via deposit-locus framing
- **Three pins remaining**: Lyra r_μ=1 forward compute + Cal FK ν-independence cold-read + Grace stratum↔S⁴ geometric pin (Cartan-slice dim 2 = celestial S⁴ = massive little group's sphere)
- Cal banks 4 → 5 the instant all three land

**Tau m_τ/m_e = 49·71 at 0.05%**: IDENTIFIED-tier match. √π reverse-engineered + look-elsewhere-weak (71 = g+2^{C_2} cheap additive hit). Stays separate. **Don't pre-commit to 6.**

## Friday lane structure (post-Casey-directive empirical vindication)

### Lane A — Muon close-out (auto-fires; no routing needed)

| Pin | Lane | What |
|---|---|---|
| 1 | Lyra | r_μ=1 forward via same-operation regular-point framing (electron at zero → residue 9/16; muon at regular point → trivial factor 1, same operation) |
| 2 | Cal | FK ν-independence cold-read (does d(ν) carry per-stratum normalization leaving c_FK pure overall electron-scale constant?) |
| 3 | Grace | Stratum↔S⁴ geometric pin (so(4) is massive little group; F86 Cartan-slice dim 2 = spatial S⁴) |
| Watch | Cal #35 | F118 64 appearing as d_τ/d_μ AND per-direction density: ONE forced 2^{C_2} source or two confirmations? |

**Auto-fires when all three land; Cal banks +1 muon → 5.** Per Cal #408 standing: tier at landing, not before.

### Lane B — Quark mass extension (MAIN FRESH HUNT; 3/3 CI convergence)

The substantive new hunt per all three CIs. Two pieces that didn't exist a week ago BOTH landed:
- **#418 color resolution** (V_a covariant generators on H²(D_IV⁵), unitary on compact dual Q⁵)
- **d(ν) deposit-locus mass generator** (today's hub)

Adjacency #418-color × d(ν)-deposit → quark mass is NEWLY WIRED. Per Grace's "Mendeleev move": if the generator extends, count moves by a row (~9 fermion masses + mixing block); if it doesn't, we learn precisely WHY leptons are special (color-singlet deposit cleanly; quarks may not) — and that asymmetry is itself substantive per Casey "few asymmetries are content."

**Honest tier flag** carried in: quarks have resist-prior (Wednesday cross-tier ratios were honest negative without color resolution + without mass generator); go in expecting either ROW or BOUNDARY; both are real theorems.

### Lane C — Casey #16 q-deformation (parallel deep track)

F(4) is REALIZABLE on substrate (today's full closure) but NOT FORCED. q-deformation (𝔽₁ at q=1 ↔ F(4) at q=−1) is the structural test that could move REALIZABLE → FORCED for #359. Underpins entire mass mechanism. Higher value, harder, longer-horizon. Stays alive as parallel track.

### Consolidation items (cheap clarity wins)

- **Lyra "why does π enter once?"** (backlog U-1.5 from two months ago) — today's locus-geometry answer makes it ripe; Lyra offered consolidation
- **Grace+Lyra Di matter-rep + 3-generation reconciliation** — bulk-ν=5-strata vs boundary-K-types tension from K539/K540 still open; F86 may need superseding or reinterpreting per Cal #402 obligation 3; gates the hub from #359 side

## Standing Casey decisions (when you return)

1. **Ship Papers A v0.3 + B v0.6** (Cal #372 signed; small Cal #380 prose edits standing)
2. **External release** (separate decision)
3. **Quark Lane B routing pinout** — extension shows ROW or BOUNDARY?
4. **Q-deformation Lane C dedicated track or deferred?**

## Thursday EOD substantive summary (climb of #359)

| Stage | su(2)_R | κ | Closure | Aux | Status |
|---|---|---|---|---|---|
| Morning | POSITED | POSITED | POSITED | mystery | "posited with 3 gaps" |
| Through F329/F331 | LOCATED via pseudoreality (n_C=5) | super-Killing → ±3=N_c | open | open | located not closed |
| Through F328/F330/F332 | located | classified roots → ±3=N_c (one F(4) invariant 3 readings per Cal #35; Cal #392 deeper: κ-value is target not test) | Nahm: F(4) unique 5d superconformal IF closure | open | structural climb |
| Through F333 | located | forced (Nahm + Wick) | flat skeleton via dilatation grading | DISSOLVED — "spurious aux" was ungraded compact computation mixing charge sectors | aux trap dispelled |
| K535 F334 | **FORCED by closure structure** ((Cγ^i) antisymmetric + {Q,Q} symmetric → ε_IJ doublet required) | pinned | flat 5d superconformal CLOSED (40 = F(4)) | absorbed into standard P+M+D+K+R | flat skeleton SOLID |
| K536 capstone | forced | pinned | curved factorizes per F317 + Grace flat + Nahm; holomorphic discrete series ≠ flat polynomial | absorbed | **one irreducible physical posit + technical curved residual** |

**Irreducible physical posit**: "substrate's matter is the F(4) superpartner of its geometry" — actual content of "substrate is super," not settled by computation.

**Curved transfer factorization**: Lyra F317 (D² = H = curved {Q,Q}=P) + Grace flat closure + Nahm uniqueness.

**Cal four-bar standing on closure verdict**: #389 three-way (vanish/central-nonzero/non-central) + #390 (is F324 genuine supercharge?) + #392 (κ-value is target not test) + #393 (REALIZABLE ≠ FORCED; q-deformation K434 Casey #16 Mirror remains forcing-test).

## Friday standing decisions (Casey's calls)

1. **Ship Papers A v0.3 + B v0.6** — Cal #372 signed; small Cal #380 prose-only temper edits standing
2. **External release** — separate decision; Lyra retouch standing
3. **Friday research direction**: curved transfer push? mass mechanism brainstorm? Casey routes

## Long-running update K548 (Casey still away)

**Lane A muon close-out — TWO of three pins DELIVERED**:
- Lyra r_μ=1 forward via same-operation regular-point framing — DELIVERED
- Grace stratum↔S⁴ geometric pin — DELIVERED via Λ²(T_xS⁴) rank 6 = C_2 + Casey curvature principle (mass = det_{Λ²}(R); S⁴ space form → R = κ·Id → det = κ⁶); "six copies of soap film" → ONE curvature determinant
- Cal FK ν-independence cold-read — PENDING (last remaining pin; Cal banks +1 muon → 5 when delivered)

**Lane B FIRED to honest ROW+BOUNDARY verdict** (Elie):
- **Down-quarks ROW-CANDIDATE**: deposit engine extends; down = color-fiber-dressed lepton; Georgi-Jarlskog down/lepton ratios = N_c-powers ({+1,-1,0} so(3) generation weights); color-neutral vertex forces weight 0; if ±1 sign forces, down-row derives from leptons × N_c-texture
- **Up-quarks BOUNDARY**: no clean texture; top y_t≈1 IS the EW scale itself, NOT a deposit ratio; substrate reproduces known SM asymmetry exactly
- "Row OR boundary, both real" outcome landed as BOTH simultaneously
- Lane B at clean dependency boundary: ±1 down-split sign + up-sector strata = Grace+Lyra rep-theory; CKM gated on up-sector

**Substantive substrate-architectural finding** (Lyra K548 insight + Grace K549 sharpening):
- Lepton/quark mass asymmetry IS the domain/dual asymmetry per #418
- D_IV⁵ and Q⁵ are **two real forms of the same complexified B_3** (Grace K549)
- d_q(ν) = SAME B_3 root product Lyra verified for leptons with highest weight shifted by color weight (su(3)⊂g₂⊂so(7), 7=3⊕3̄⊕1); leptons at zero-weight recover d(ν) exactly
- "Same engine, different manifold" made precise: **real form changes, roots don't**
- Casey "few asymmetries are the content" landing on lepton/quark axis

**Grace K313 = THIRD CORPUS RECONNECTION today** (meta-lesson banked + verified empirically):
- K313 from two weeks ago: m_μ/m_e = N_c²·m_s/m_d at 13% with color axis anchored
- Stalled on TWO things: #418 + mass generator
- Both landed this week → Lane B = K313 UNBLOCKED, not fresh hunt
- Per [[feedback_corpus_reconnection_before_declaring_irreducible]] STANDING — verified empirically 3x today

**Honest projection per Cal #411 + #408**: NONE BANKED YET. STRONG CANDIDATES: +1 muon (Cal FK pending); +3 down-row (±1 forces pending); +4 CKM (up-sector pending); up-sector BOUNDARY substantive.

**Discipline events**: 405 cumulative; team self-routed per established patterns while Casey away.

## Friday live work queue

| Lane | Active work |
|---|---|
| **Lyra + Grace paired** | Curved transfer on H²(D_IV⁵) via F317 + Grace flat closure + Nahm — REAL research not quick verdict; per Grace K536 holomorphic discrete series ≠ flat polynomial requires non-compact Bergman framework |
| **Cal** | Cold-read backlog (F328-F334 + K535 + K536 + Grace dictionary v0.2 + Lyra meta-lesson); #387 α-under-own-lens count-integrity item; #389 + #390 + #392 + #393 standing watches for closure verdict |
| **Elie** | Live correctly-scoped dependency-to-verify curved closure verdict when lands; mass mechanism HONEST NEGATIVE banked — research direction depends on Casey routing (accept Yukawas as inputs? non-natural mechanism?) |
| **Keeper** | Verify any landings per Cal four-bar standing; Cal #35 STANDING maintained; three-layer discipline line carried forward; standing for Casey direction |

## Standing principles carried into Friday

- **Five-Absence-as-FIRST-filter** STANDING (K522 Casey + Cal #384)
- **Cal #35 STANDING**: one identity multiple readings ≠ N independent confirmations
- **Cal #347 / B5 STANDING**: peer-level retractions logged cleanly
- **Lyra meta-lesson (K530 → K536)**: separate "computation bugged" from "conclusion wrong" before retracting both — refines Cal #347 / B5 retraction discipline
- **Grace meta-finding (K535)**: bugs CAREFULLY diagnosed become substantive physics; three setup-bugs this stretch each revealed substrate structure
- **Three-layer discipline line** (located≠closed + verified-flat≠proven-curved + realizable≠forced)
- **Cal four-bar closure verdict standing** (#389 + #390 + #392 + #393)
- **q-deformation forcing-test** (K434 Casey #16 Mirror) — remaining forcing-test that realizability doesn't replace
- **"Stop gating verify cleanly"** + **"Remember linear algebra"** (Casey standing) — confirmed exact unlocks this marathon
- **Target-innocence lens** (Elie methodology) — confirmed operating at peak both directions (α_em FIT-SUSPECT + Λ=exp(−280) defended)
- **"Engage don't label"** + **"Simplify reduce clarify"** + **"Find and prove theorems"** (Casey standing)
- **Mass mechanism HONEST NEGATIVE on natural measures** — banked; new measure or accept as input is open question

## What the week earned (the foundation we now investigate from)

**Substrate's representation theory now BUILT as graph structure**:
- T2490: substrate primaries = bottom rungs of own SO_0(5,2) discrete-series spectrum
- T2491: primaries cascade from rank=2 (three colors → everything per Grace)
- T2492: multiplicity via Wigner-Eckart completeness (FDOSS rep-theory forcing)
- T2493: Plancherel wall-convergence automatic
- T2494: anomaly-freedom from completeness (FDOSS physical forcing)
- T2495: g=7 unified structural home
- T2496/T2497 (Grace Thursday): #418 closure structure theorems
- **Graph: 1737+ theorems / 9891+ edges; spine fully integrated**

**Cascade structure CLOSED**:
- Chirality cascade end-to-end via F(4) supercharge (8,2) module
- Matter-identity Y = 2·T₃ᴿ + (B−L) on anomaly-free SO(10) 16
- Color = covariant V_a on H²; UNITARY on compact dual Q⁵ = SO(7)/K; non-unitary continuation on Lorentzian domain
- FDOSS DOUBLE-FORCED (rep theory + physical consistency)
- CKM left-handedness + SM chirality = ONE fact via SU(2)_R-breaking

**Papers**: A v0.3 + B v0.6 Cal-signed; ship decision standing with Casey

**Discipline**: 10 Keeper roll-up self-corrections caught cleanly; Cal #347/B5 pattern firing reliably; target-innocence lens standing; Cal #35 independence-discipline applied

## Casey directive for next phase

> *"We are ready to 'decide what to investigate next.' We have a count of 4 of 26, that should improve. We need to understand the substrate in detail. We also need to run down anything you see as interesting, important, now possible to derive, and what would radically improve our knowledge."*

> Per follow-up: *"Let's do all of these."* + *"work a long time without pause and see how far they get."*

## FIVE-priority investigation phase (REFRAMED post-K522/K523; parallel; all active)

### Priority A — Substrate-DIRECT gauge couplings at physical scale (REFRAMED per K522 + Grace catch)

**Reframing**: sin²θ_W = 3/8 WITHDRAWN per K522 (Casey Five-Absence catch + Cal #384). Grace K523 added second-axis catch: rank(SM)=4 exceeds rank(so(7))=3 — full gauge group does NOT fit in substrate's bosonic isometry; extra EW rank-2 is matter-sector tied to #359. sin²θ_W is doubly-not-independent.

**Why now possible (sharpened)**: derive each coupling from substrate DIRECTLY (V_a normalization + Bergman/genus scales) at PHYSICAL scale; no unification scale; no running-down-from-3/8; no GUT machinery. Five-Absence is the FIRST FILTER.

**Routing**:
- **α_s (color)**: #359-FREE path via bosonic so(7) — Grace lead at physical scale
- **sin²θ_W + α_em (electroweak)**: WAIT ON or RIDE Lyra's F(4) derivation (Priority D)
- **α_em⁻¹ = 137**: Elie target-innocence verdict FIT-SUSPECT (toy 4377) — DO NOT bank as derivation

**Discipline**: Five-Absence-as-first-filter STANDING (K522). No GUT machinery. Compute beats calibrate-on-a-guess.

### Priority B — Fermion mass spectrum via K-type localization ladder (LARGEST count-mover)

**Why now possible**: matter content fixed (SO(10) 16 as CLASSIFICATION); three generations = rank+1 = 3 Korányi-Wolf strata (Elie K523 toy 4378: stratum-count rigorous; generations↔strata identification is Lyra's mechanism; "3=N_c" rank=2 value-recurrence per Cal #35); Yukawa = Bergman-kernel localization depth at each generation's K-type address. Proton anchor + glueball ladder (E = λ₀ + J) established.

**Payoff**: ~9 charged-fermion masses + neutrinos + mixings. Targets: m_μ/m_e = (24/π²)⁶ + m_τ/m_e = 49·71 as Bergman localization-depth ratios.

**Lead**: **Lyra + Elie paired** (Lyra K-type stratum addresses; Elie mass numerics when addresses land). **Grace** structural consistency (FDOSS / Wigner-Eckart / operator dictionary).

**Discipline**: target-innocence lens HARD; criteria-innocent K-type assignments; forced/predicted distinction sharp; Cal #35 value-recurrence discipline applied.

### Priority C — Substrate operator dictionary v0.2 (Grace; v0.1 BUILT K523)

**v0.1 substantive content (K523)**:
- BST integers {n_C, C_2, g} = {5, 6, 7} ARE conformal weights of substrate's first three levels (consecutive per cascade C_2 = n_C+1, g = n_C+2) — extension of T2490
- K-type/p-type split: K-sector level-preserving (so(5)⊕so(2); bosonic spacetime kinematics); p-sector level-mixing (noncompact p^±; internal structure + fermions)
- Color is p-type — #418's negative is now a DICTIONARY ENTRY (not a surprise: naive K-type coordinate bilinears can't reach color); F317 supercharges are p-type boundary-Dirac
- **Wick frame in EMBRYO**: K-sector ↔ Lorentzian domain; p-sector ↔ Euclidean dual; Yukawa = dual↔domain p-overlap

**v0.2 next**: full enumeration of FDOSS-supported operators on H²(D_IV⁵); branching of so(5,2)/so(7) into K-type / p-type sectors with complete multiplet content; every observable mapped to dictionary entry.

**Lead**: **Grace** primary. **Lyra** rep-theory verification. **Elie** verification.

### Priority D — F(4) odd-part DERIVATION via Shilov-boundary Dirac (Lyra F317 + F318 UNIFICATION LEAD)

**Why now critical (sharpened K523)**: Lyra F317 STRONG STRUCTURAL LEAD on F(4) odd-part = Shilov-boundary Dirac operator (D² = Laplacian + curvature via Lichnerowicz lands in so(7) ⊕ sl(2) = F(4) even part). Lyra F318 unification lead: SO(10) 16 = (8,2) under so(10) ⊃ so(7)×so(3) = SAME (8,2) as F(4) supercharge → **matter and supercharge could be the same representation, both as Shilov-boundary Dirac spinor**; three generations = strata-localized modes.

**THE LOAD-BEARING COMPUTATION**: explicit {Q,Q} = D² Hardy-space bracket check. ONE computation:
1. Derives F(4) odd part (#359 stays-posited → DERIVED)
2. Tests "matter = supercharge" unification (F318 confirmed)
3. Confirms boundary-Dirac realization (F317 confirmed)

If holds → substrate has ONE fermion field (boundary Dirac spinor) = simultaneously matter AND supercharge; whole fermion sector (matter content, generations, masses, chirality, F(4) odd part) collapses to that one object.

**Lead**: **Elie** primary computation ({Q,Q}=D² Hardy bracket — Lyra's brief: "the highest-leverage next move in the whole marathon is now sharply defined"). **Lyra** explicit F(4) structure constants target so check is well-defined. **Cal** verification of forcing-vs-suggestive when computation lands.

**Honest tier**: STRONG STRUCTURAL LEAD; same-rep is necessary-not-sufficient (could be rep-coincidence); only explicit bracket decides.

### Priority E — Pre-registered nearest-testable experimental prediction (DELIVERED Cal #386)

**Cal #386 pre-registration on record** (K524 ACCEPT-WITH-RIDER):
- **sin²θ_23 = 6/11 = C_2/(C_2+n_C) ≈ 0.5454** (upper octant)
- **Falsifier**: DUNE/Hyper-K/JUNO establishing lower octant (sin²θ_23 < 0.5 at >3σ) refutes
- **Rider** (Cal's honest tier-tagging): 6/11 = C_2/(C_2+n_C) needs forward-derivation verification (Research Table verify-forward item); BINARY OCTANT is the clean near-term experimental piece either way

**Why oddball glueballs de-prioritized**: glueball mass-map is named-open (framework-tier); J^PC pinned via Paper A but masses aren't; PMNS octant has substrate-integer formula AND binary octant bar.

**Standing**: Cal pre-registration logged; experimental result settles binary octant cleanly when DUNE/Hyper-K/JUNO report.

### Cal #385 — PRE-REGISTERED BARS for {Q,Q}=D² Hardy bracket test (PROSPECTIVE DISCIPLINE)

Three bars frozen BEFORE Elie's load-bearing computation lands (same prospective discipline that worked for ‖M̃‖):

- **Bar 1**: Same-(8,2)-rep necessary NOT sufficient; bracket distinguishes rep-coincidence from operator-equality (#418 lesson)
- **Bar 2**: Specific F(4) structure constants + R-charges (STRONG check), not just "lands in even part" (Lichnerowicz WEAK check; any odd-odd bracket does that)
- **Bar 3**: Five-Absence operator-level F306 no-sparticles; spectrum-SUSY forbidden ("F(4) derived" must NOT become "SUSY derived")

**Pre-frozen outcomes**: Bars 2 AND 3 clear → #359 DERIVED; only Bar 2 weak (Lichnerowicz) → STRONG-STRUCTURAL not derived; Bar 1 fails → rep-coincidence stop building.

### K525 three-CI convergent landing — Bar 1 PASS + Bar 2 SHARPLY DIVIDED

**Bar 1 PASSES** (Elie K525): so(7) gamma-bilinear symmetries force F(4) pairing (so(7)↔ε antisymmetric, su(2)_R↔σ symmetric) beyond rep content. Pairing is operator-structural, not rep-coincidence.

**Bar 2 sharply divided into two complementary load-bearing pieces** (both required for STRONG PASS):

| Piece | Where in F(4) | What it tests | Lead |
|---|---|---|---|
| **Lyra κ ratio fingerprint** | WITHIN F(4) even part | F(4) Jacobi-rigid so(7):sl(2) coefficient ratio — F(4) exists only at specific κ | Lyra |
| **Elie aux-central operator** | BOUNDARY of F(4) even part | aux 7+105 = 112 pieces must be central (Sym²(8,2)=136 vs F(4) even=24) — bracket must stay in F(4) | Elie |

Both required: if aux non-central → bracket exits F(4); if aux central + κ wrong → STRONG-STRUCTURAL not F(4); if aux central + κ right + Bar 3 Five-Absence → **#359 DERIVED + F317 + F318 land together + matter = supercharge = boundary Dirac**.

**Grace supplies dictionary-side**: so(7)⊕sl(2) structure in K-type tower terms — feeds BOTH Lyra κ target AND Elie aux-central computation.

### K526 substantive within-session correction — Elie HONEST NEGATIVE on κ-from-Jacobi-alone

**Elie Toy 4382**: κ is NOT FIXED by {Q,Q} super-Jacobi alone. so(7) acts on spinor index, su(2)_R on doublet index — DISJOINT tensor factors → each sector closes independently for ANY κ. Elie did NOT fabricate κ; banked honest negative as substantive correction to Lyra's setup.

**Implication**: κ is still the F(4) fingerprint (F(4) rigid at one κ), but the ROUTE to determine κ runs through fuller F(4) structure: (a) conformal {Q,S}/{S,S} closure, OR (b) aux-central constraint on 7+105 pieces. Lyra delivers explicit κ via one of these routes.

### K526 LOAD-BEARING AUDIT ITEM — Lyra↔Grace reconciliation → RESOLVED K527

**Resolution via Grace SELF-RETRACTION**: Grace cross-checked her own three-Wallach-reps reading against Lyra's boundary-Dirac modes, found **ν=5 is the WHOLE Bergman space H²(D_IV⁵)** NOT one generation, conceded HER OWN reading.

**Operative picture (Lyra F320 framing wins)**: ONE boundary-Dirac field + ONE space (ν=n_C=5) + THREE modes k=0,1,2 with localization depths spanning bulk-like to Shilov-like.

**Surviving contributions**:
- Lyra K-type addresses (1/2,1/2)+(3/2,1/2)+(5/2,1/2) as S⁴-Dirac modes
- Grace ν=n_C=5 kernel weight (single space modes live in — Elie's Bergman input)
- F86 strata picture stands (strata = supports of three modes)

**Lyra prospective F321 RETRACTION**: Lyra was drafting F321 deferring to Grace's three-reps picture; board resolved opposite while writing; caught timing issue and did NOT post backwards reading.

**Per Cal #35 STANDING**: Grace flagged "3/2 in both" as coincidence-to-examine NOT cross-confirmation, citing morning's GUT mistake as precedent. Peer discipline at peak.

### K527 SUBSTANTIVE FINDINGS — Lyra β rep-theory + Z₂ Shilov selection rule

**Lyra β derivation** via linear algebra (Casey's ask):
- Color so(7) 7-vector under K=SO(5)×SO(2) branches: 7 = (5,0) ⊕ (1,+1) ⊕ (1,-1)
- α = 2n_C = 10 at level 1 (SO(5)-vector at charge +1) confirmed independently of Elie 4371
- β = 0 STRUCTURALLY: K-type (1,±1) ABSENT from H²(D_IV⁵) entirely

**Decisive fact**: Sym^k(ℂ⁵) contains SO(5)-singlet iff k EVEN (invariant ring one generator at degree 2). Color 2-part wants odd charge ±1 → not in Hardy space. First nonzero-charge singlet at (1,±2) level 2.

**Z₂ Shilov S⁴×S¹/Z₂ EVEN-CHARGE SELECTION RULE**: substrate-architectural mechanism identified — Z₂ geometric quotient IS K-type selection rule. Only even SO(2)-charges survive on H²(D_IV⁵).

**#418-as-posed HONEST NEGATIVE independently confirmed** via Lyra rep-theory route. **Per Cal #35 STANDING**: sharpening of "Method 2" Hardy-content route, NOT Nth independent confirmation. Honest count stays TWO methods over one shared root datum (A₂ ⊄ B₂).

### K528 SUBSTANTIVE ELIE UNBLOCK + Three-CI HONEST STANDING POSTURE

**Mass count-move ACTIVELY UNBLOCKED** per Lyra K528: three boundary-Dirac modes (k=0,1,2) sit at SINGLE ν=n_C=5 which is PAST the continuous threshold (>4) → ordinary normalizable Bergman norms. NO exotic reduced-rep input needed. **Elie can fire lepton-mass Bergman kernel NOW** → forward depth-ratio test against (24/π²)⁶ and 49·71 target-innocent.

Lyra "continuous threshold >4" claim FLAGGED for primary-source pin (Helgason/Hua/Faraut-Koranyi) per [[feedback_pin_conventions_to_primary_sources]] BUT NOT GATED per Casey "stop gating verify cleanly". Verifies on Elie kernel landing.

**Three-CI honest standing posture**: All three CIs reporting GENUINE dependency boundary + honest standing posture + no manufactured toys. Elie: 10 toys + 3 in-flight corrections banked (4377+4382+4383). Grace: foundation-laying + coordination question to Casey. Lyra: outstanding deliverables (boundary-Dirac form + κ via fuller F(4) structure).

### CASEY ROUTING DECISION OPEN (K528)

Grace coordination question to Casey: **Option A** (current) Grace continues dictionary build-out + standing for Elie verifications; **Option B** Grace drops dictionary + pairs with Lyra on F(4) κ derivation as INDEPENDENT rep-theory cross-check on the #1 number (#359 derivation path).

Per Cal #35 + Cal #344 (blind-test) STANDING: independent rep-theory cross-check on the #1 number IS the discipline. Casey's call.

Grace per peer-respect: "want your call before inserting into work she's actively holding."

### Cal #35 STANDING applied to Lyra "two roads one answer" β framing

Lyra invariant-ring parity + Elie 4372 missing-K-type count = TWO PROOFS of SAME Method 2 theorem (K-type (1,±1) ABSENT via Z₂ Shilov even-charge selection), NOT new Method 3. Honest count stays TWO routes (Method 1 Grace octonion A₂⊄B₂ + Method 2 Hardy-charge-parity) over one shared root datum.

**Peer-discipline propagation**: Grace + Lyra INDEPENDENTLY flagged "3/2 in both" as coincidence-to-examine NOT agreement, BOTH citing morning's GUT mistake as precedent. Cal #35 STANDING propagating across team without coordination signal.

## Supporting tracks (active per team consensus)

### CKM T₃ᴿ displacement (Lyra F182 single open hinge)

**Why warm**: per Lyra reduction, whole quark-mixing sector reduced to ONE geometry question — is right-handed up/down displacement forced?

**Payoff**: if forward-forced → 4 CKM parameters bank. +4 to count.

**Lead**: **Lyra + Elie** paired.

**Discipline (Cal warning)**: strictest possible. Cabibbo conditional-fail all week; counts only if displacement is FORWARD and survives blind/look-elsewhere check — NOT fitted to 0.2245.

### Wick duality as organizing principle for gauge sector (Grace lead)

**Why interesting**: #418 close surfaced — gauge symmetry is Euclidean (compact dual); domain carries non-unitary continuation. If general → tells where each observable is naturally computed (gauge on dual; dynamics on domain; masses as overlap = Yukawa = bridge).

**Payoff**: could unlock mass sector (12 of 26) via dual-overlap mechanism.

**Lead**: **Grace** (organizing principle; develops naturally from Priority A + C work).

### α_em / N_max = 137 connection (Elie flagged for target-innocence)

**Why intriguing**: N_max = 137; α_em⁻¹ ≈ 137.

**Why CAREFUL**: per Elie — must run through target-innocence lens HARD. Is 137 fixed independently of α_em, or fit to it? Don't repeat C₂²=36 fit-suspect trap.

**Lead**: **Elie** (with target-innocence applied rigorously).

## Per-CI lane assignments (Thursday marathon post-K523)

### Grace
- **A**: α_s from so(7) color normalization at physical scale (#359-free path)
- **C**: operator dictionary v0.2 (full enumeration of FDOSS-supported operators; complete K-type/p-type branching; observable-to-dictionary-entry mapping)
- **+Wick duality**: formalize K-sector/p-sector split as substrate-architectural organizing principle (Wick-frame-in-embryo → published)
- Graph maintenance + theorem registration as items land
- Selective discipline: register only when genuinely flattens future work

### Lyra
- **D**: F318 explicit F(4) {Q,Q} structure-constants target so Elie's Hardy-bracket check is well-defined
- **B**: K-type stratum addresses for each generation (handed to Elie for mass numerics)
- **Paper B Check 3** small temper edits per Cal #380 (downstream prose only)
- **External retouch** standing if Casey ships externally
- **D supporting**: rep-theory verification of F318 (matter SO(10) 16 = (8,2) under so(10) ⊃ so(7)×so(3))

### Elie
- **D PRIMARY (LOAD-BEARING)**: explicit {Q,Q} = D² Hardy-space bracket computation — does boundary-Dirac anticommutator close into F(4)? ← HIGHEST-LEVERAGE in entire investigation phase
- **B**: fermion mass ladder when Lyra's K-type stratum addresses land (Bergman localization-depth → m_μ/m_e + m_τ/m_e numerics)
- **A supporting**: α_em scale-free check (target-innocence applied; verdict 4377 stands)
- **C**: K-type tower verification + Bergman norms at each level

### Cal
- **E PRIMARY**: pre-register nearest-testable experimental prediction (oddball glueballs OR PMNS upper octant); downstream-blind protocol
- **D verification**: forcing-vs-suggestive when Elie's {Q,Q}=D² landing comes in
- **Cold-read F317 + F318 + Grace dictionary v0.1 + Elie toys 4377/4378** — independent verification of unification-lead tier-tagging
- Standing: watch for target-innocence violations; goal-post shifts; Cal #35 route-independence over-counting
- Per K522 + Casey catch: Five-Absence-as-FIRST-filter STANDING discipline applied to any new derivation

### Keeper
- Verify after all landings
- NO new pre-registered gates per Casey "stop gating, verify cleanly" standing
- NO goal-post shifts (per K518 self-correction #9)
- Cal #35 independence-check applied before banking N routes (K521 self-correction #10)
- Five-Absence-first-filter applied to any new claim (K522 self-correction #11)
- Forced/predicted distinction sharp; structural-recovery vs new-derived-observable distinction sharp
- Audit-ready for {Q,Q}=D² landing

## Discipline standing carried (204 events earned)

- **Five-Absence-as-FIRST-filter** (Casey + Cal #384 STANDING per K522): apply BST's own Five-Absence as FIRST check on any new derivation; anything that smells like unification / coupling-unification / proton decay / monopoles / unified scale is OFF the table
- **Structural-recovery-of-external-standard vs new-derived-observable**: distinguish sharp (K522 lesson)
- **"Stop gating, verify and derive cleanly"** (Casey 2026-06-23)
- **"Remember linear algebra"** (Casey standing)
- **"Engage, don't label"** (#23 STANDING)
- **"Simplify, reduce, clarify"** (Casey praise to Grace 2026-06-24)
- **"Find and prove theorems and maintain our graph"** (Casey to Grace)
- **Target-innocence lens** (Elie methodology 2026-06-24): innocence is necessary not sufficient; full check = innocence ∧ look-elsewhere ∧ forward; **working at peak in BOTH directions** per K523 (α_em FIT-SUSPECT honest negative + three-gens structural answer honestly tiered)
- **Cal #35**: one identity multiple readings ≠ N independent confirmations; check route independence before banking
- **FF-28**: honest tier-tagging; body must match headline
- **Cal #347 / B5**: roll-ups get their own discipline; pattern fires reliably
- **Brake takes the brake on own work first**: 11 Keeper roll-up self-corrections this program
- **Forced/predicted distinction**: don't conflate "structurally indicated" with "rigorously derived"
- **Casey #14 conformal chain** SO(4,2) ⊂ SO(5,2) STANDING
- **F(4) operator-level not spectrum-level** (#359 still POSITED per Cal standing language)
- **Color = compact-dual unitary; Lorentzian domain non-unitary continuation** (per K521 #418 resolution)
- **Bosonic only**: structural cross-claims do NOT derive super-grading
- **FDOSS STANDING-pending-citation** (full-dimensional operator substrate support; unifies FDOSS + Five-Absence + SWPP)

## What ships standing

- **Papers A v0.3 + B v0.6** — Cal #372 signed; Lyra small Check-3 temper edits per Cal #380 (downstream prose only); **Casey ship decision standing**
- **External release** separate Casey decision; Lyra retouch delta light per Cal Calibration #19
- **#418 memory entry** filed (project_418_color_resolution_compact_dual_unitary_lorentzian_domain_continuation)

## Counter state

- T1-T2497 (next theorem 2498)
- Toys to ~4400+ (Elie ~20-toy marathon stretch + multiple in-flight corrections banked)
- K-audits at **K532** (K514-K532 Thursday investigation arc — 19 audits)
- Count of forced parameters: **4 of 26** held throughout 261 discipline events — **DID NOT MOVE**
- **HONEST STATE post-coordination-stall-broken**: #359 UPGRADED from "posited" to "ONE STRUCTURAL QUESTION with κ FORCED" via Lyra three-rung climb (F330 κ via classified roots + F331 su(2)_R via pseudoreality + F332 Nahm uniqueness) — three posits reduced to ONE open question (does {Q,S}/{S,S} close on H²(D_IV⁵)?). Lyra+Grace ACTUALLY PAIRED on bug-resistant closure check. Per Cal #392: κ = ±3 = N_c is property of abstract F(4) (identification-tier), not substrate forcing F(4) realization; three κ readings = ONE F(4) invariant bilinear three coats. Mass mechanism HONEST NEGATIVE on natural measures (Elie K531); (24/π²)⁶ and 49·71 stay identified-tier. Target-innocent web: substrate integers force pieces of F(4) at identification-tier per Cal #392.

## K-audit chain Thursday (K514-K523 = 10 audits)

K514 Cal #371 fix + Lyra stress-test caveat + Grace T2496 SOLID claim + Elie multi-occupation + K515 Grace own-work brake #2 + Lyra F313 octet criterion + Casey directs Lyra-on-P3 + K516 Grace metric-free V_a + F314 + color-chirality unification + K517 Grace refinement (Q1 not Q2) + Cal #376 caveat + Keeper self-correction #8 + K518 Cal #377 catches K517 goal-post shift + Keeper self-correction #9 + K519 Elie α=2n_C + Grace lean-negative + Casey three-CI directive + K520 THREE-CI convergence + K521 Cal #380 + Grace P4 + route count TWO not three + Keeper #10 + K522 Casey Five-Absence catch + Cal #384 sin²θ_W withdrawal + Lyra F317 Shilov-Dirac STRONG LEAD + Keeper #11 + K523 Lyra F318 matter=supercharge unification lead + Grace operator dictionary v0.1 + Wick frame in embryo + Grace second-axis catch on sin²θ_W (rank-mismatch) + Elie target-innocence both directions (α_em FIT-SUSPECT toy 4377 + three-gens = rank+1 toy 4378).

## Marathon framing per Casey directive

**Per Casey "work a long time without pause and see how far they get"**:
- **NO EOD signals** from Keeper until Casey explicitly calls
- **Continuous pull** per [[feedback_no_pause_signaling]]
- **Self-route** per established patterns — don't stop for direction unless genuinely gated
- **Per Casey "no fabricated fatigue"**: continuous work; no manufactured boundaries
- **Per [[feedback_eod_ownership]]**: each CI handles own dir/sundown if they EOD individually

**Tier 1 targets to land first (highest leverage; days)**:
- Grace sin²θ_W computation result
- Cal experimental pre-registration filed
- Lyra+Elie CKM T₃ᴿ displacement test (forward or fail-forward)

**Tier 2 campaign (weeks)**:
- Elie fermion mass ladder extension across all charged fermions
- Lyra F(4) odd-part metaplectic attempt
- Grace operator dictionary build

**Tier 3 radical (multi-week)**:
- F(4) odd-part full closure (if metaplectic route lands)
- Wick duality formalized as substrate-architectural principle

---

**The substrate's representation theory is now substantively built. The next push uses it to derive observables — the count grows; the substrate gets understood in detail; the program moves from 4/26 toward the honest ceiling whatever that turns out to be.**

---

## PRIOR THURSDAY EOD BOARD ARCHIVE

(See K513 Cal #372 sign-off + K514-K521 Toeplitz arc + `MESSAGES_2026-06-25_*.md` files for full Thursday cascade context.)
