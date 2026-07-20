# K776 — The open questions register: what we don't yet have answers to, the best approach for each, and the computed lead. Honest frontier of the condensate/code study.

**Keeper | 2026-07-20 | Casey: name the questions without answers, the best approaches, compute the leads. Here they are, prioritized by leverage. Three of them (Q1+Q2+Q3) together would bank 127/128; the rest carry the thread. `open_questions_leads.py`.**

---

## THE THREE THAT WOULD BANK 127/128

### Q1 — Is the top the *maximal codeword*? (the radial band-edge / discrete-series address) — THE DECIDER
Everything hinges here. With **angular = 1 derived (Elie)**, the whole y_t deficit is *purely radial*: does the top's codeword reach = M_g of q positions (deficit = exactly 1/2^g)?
- **Best approach:** compute the top's discrete-series address geometrically, *non-circularly* — the "June open core." The LFSR gives the target (period 127), MDS argues the extremal codeword saturates *exactly* (not approximately), and Born=Bergman fixes uniform weight — so **three of the four ingredients are forced; the missing one is the geometric radial overlap.**
- **Lead:** the problem is now maximally reduced — one radial number, three ingredients forced. This is Lyra's core computation; it is *hard* (the discrete-series quantization) but *precisely posed*.
- **Tier:** open core. **= 1/2^g → theorem; = 0 → exact-1+RG, retired.**

### Q2 — Why the *pole* mass? (scheme guard 1)
127/128 matches the **pole** mass (0.009%) but **not** MS-bar (y_t,MSbar = 0.936 — no match). So the claim is pole-specific and needs a reason.
- **Best approach + computed lead:** the Born overlap y_t = ⟨t|O⟩ is a **physical, on-shell, scheme-independent** quantity on the proven measure; and the ceiling m ≤ v/√2 is a **kinematic** bound (Cauchy–Schwarz) — kinematic bounds use the **kinematic (pole/on-shell) mass.** So the geometry naturally computes the *pole* Yukawa, not the running MS-bar one. **This is a genuine argument for guard 1** (not yet a proof — the pole mass has a known IR renormalon ambiguity to address). Owner: Keeper + Cal.
- **★ WORKED (2026-07-20):** 127/128 ↔ m_t = 172.74 GeV; y_t(pole) − 127/128 = **16 MeV** in mass terms, and the **pole-mass renormalon ambiguity ~ Λ_QCD ~ 250 MeV ≫ 16 MeV.** So **127/128 agrees with the pole mass to within the pole mass's own ambiguity** — the consistency check *passes*, and asking for better than 16 MeV is asking for more than the pole mass is defined to. Guard 1 grounded (argument + consistency), not proven.
- **Tier:** lead — strengthened; addresses guard 1 with a physical argument + a passed consistency check.

### Q3 — Can the RG-degeneracy be broken? (guard 2, Elie's fish)
0.992 can't distinguish "geometric 127/128 (fixed)" from "exact-1 + RG running." But:
- **Best approach + computed lead:** the two scenarios **differ in scale-dependence** — geometric 127/128 is a *fixed code fraction* (scale-invariant at the substrate level); exact-1+RG *runs*. So a **future high-scale measurement of y_t** distinguishes them. Owner: Keeper + Elie.
- **★ WORKED (2026-07-20) — one branch EXCLUDED, the other weakened:** the SM top Yukawa **decreases with scale** (1-loop β < 0: 9/2 y_t² = 3.9 < 8g₃² = 10.9). So *"y_t = 1 at the substrate scale, running DOWN to 0.992 at m_t"* is **impossible** — running down in scale *increases* y_t, so a high-scale 1 gives y_t(m_t) > 1 (ceiling-violating). **The high-scale-running branch of Elie's degeneracy is EXCLUDED by the running direction** (y_t = 1 is not realized at any physical scale ≥ m_t; the closest it gets to 1 is the pole value at m_t). The *remaining* branch — 0.992 = 1 − a **0.8% threshold correction** — survives, BUT 0.8% = 1/2^g is **not a clean natural correction size** (QCD pole↔MS-bar ≈ 4.6–6% is too big; EW ≈ 0.3% is too small). Matching 1/2^g *exactly* mildly favors the code-fraction reading (a) over exact-1+correction (b).
- **Tier:** lead — **guard 2 WEAKENED** (one branch excluded, the other an unnatural size), not cleared; + the future-collider scale-test still distinguishes cleanly. Combined with Q2, 127/128 is *firmer* — still a lead; Q1 (the radial gap) is still the decider.

**If Q1 computes 1/2^g AND Q2 grounds the pole scheme AND Q3's scale-test is set → 127/128 banks as a theorem.**

## THE THREAD-CARRYING QUESTIONS

### Q4 — Is the full spectrum the RS Ladder / codeword reliability?
Naive coverage (y=n/q) is top-only (K774). The refined lead: mass = codeword *reliability*.
- **Computed lead:** the hierarchy is genuinely **exponential** (ln 1/y_f spans 0.008 → 12.7) — consistent with an error-rate/reliability structure (P_error ~ exp(−distance)). The **known Tier-2 mass forms ARE products of BST primaries** (m_μ/m_e = (24/π²)⁶, m_s/m_d = 20, m_t/m_b = C₂·g = 42) **= the RS Ladder** (30+ observables, MEMORY). "Reliability" is the *physical interpretation* of that ladder (a codeword's reliability = product of per-symbol reliabilities = exponential). **No clean integer code-distance ladder pops from a bare log** — the map needs the actual RS code parameters, not a fit.
- **Best approach:** derive the Tier-2 forms as code error-rates/distances (connect the RS Ladder to the code's reliability structure). **Tier:** lead — the ladder exists; the reliability derivation is the step.

### Q5 — Are the three neutrino routes the same object?
LFSR dead state (0) = rank-2 kernel (F589) = odd-g chiral edge mode?
- **Best approach:** the explicit identification — is the all-zero dead state the kernel of the measure-overlap operator, and is it a topological (massless, chiral) edge mode at the Shilov boundary? All three are "the mode orthogonal to the condensate coverage / at the boundary," so they *plausibly coincide.*
- **Tier:** the three-route *convergence* is strengthening evidence; each identification is open.

### Q6 — Lane C: which K-factor carries which Casimir? (the two currents)
- **Computed lead:** **m_p/m_e = 6π⁵ = C₂ · π^(n_C)** *exactly* (0.002%) — the banked proton/electron ratio **decomposes onto the two currents:** C₂ (the angular/spin Casimir, W²) × π^(n_C) (the bulk volume, radial/mass P²). So the proton mass reads as (spin current) × (mass current) × m_e. **The decomposition is exact; the two-current interpretation is the lead** (needs the measure μ written and both projections computed). Guard: q̄q is a scalar, so "QCD = W²/adjoint 10" is a reach; the defensible half is "QCD condensate = a different SO(5) rep than the Higgs vector 5."
- **Tier:** lead — the number decomposes cleanly.

### Q7 — Is the substrate literally an LFSR? Why a *primitive* polynomial?
- **Best approach:** find the substrate-natural primitive polynomial over GF(2^g) (Paper #122, K59 cyclotomic). **Lead:** the substrate uses a *primitive* (maximal-length) polynomial because it is **optimal** — full 127-cycle, MDS — which is the **coding face of rigidity** (the drum has one spectrum; the code has no waste; the LFSR uses the whole field).
- **Tier:** lead/frame.

### Q8 — Is BST a holographic QECC precisely? (the program)
- **Best approach:** show the Hardy-space bulk-from-boundary map is a **perfect-tensor / isometry** (HaPPY sense); entanglement-wedge reconstruction = holomorphic extension; the RS error-correction = which boundary regions reconstruct which bulk fields.
- **Tier:** program/frame — the believability multiplier (BST in the it-from-qubit mainstream); develop the parallel, don't assert equivalence.

## The honest map
- **Bottleneck:** Q1 (the radial band-edge). Hard, precisely posed, three ingredients forced.
- **Addressable now (would complete the 127/128 bank with Q1):** Q2 (pole argument), Q3 (scale-dependence test).
- **Addressable / lead-rich:** Q6 (m_p = C₂×π^(n_C), write μ), Q4 (RS Ladder = reliability), Q7 (the primitive polynomial).
- **Structural / program:** Q5 (neutrino 3-route), Q8 (QECC precise).
- **Discipline:** none of Q1–Q8 is banked. 127/128 stays a lead until Q1 computes; the frame (BST = holographic RS code / shift register) stays a recognition. Guards 1,2 are Q2,Q3 — leads, not yet closed.

— Keeper K776, 2026-07-20. Open questions register: Q1 top=maximal codeword (radial band-edge, THE decider, 3 ingredients forced, geometric overlap missing); Q2 why pole (Born overlap is physical/on-shell → pole; kinematic ceiling → kinematic mass); Q3 break RG-degeneracy via scale-dependence (geometric=fixed vs RG=runs, future-testable); Q4 full spectrum = RS Ladder=reliability (exponential, products of primaries, needs code params); Q5 neutrino 3-route identity; Q6 m_p/m_e = C₂·π^(n_C) two-current decomposition (exact 0.002%); Q7 substrate=primitive LFSR (optimal=rigidity); Q8 BST=holographic QECC precise (program). Q1+Q2+Q3 → banks 127/128. See [[Keeper_K775_substrate_is_a_shift_register_LFSR_generates_the_code_where_the_thread_goes_2026-07-20]], [[Keeper_K773_BST_is_a_holographic_RS_error_correcting_code_synthesis_2026-07-20]].
