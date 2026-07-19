# K757 — Verification spec for the two-mass candidate: does every quark's current/constituent (undressed/dressed) mass split = the two rank-2 Jordan idempotents (c₁ = bulk = current, c₂ = Shilov = constituent)? The MAKE-OR-BREAK test: the geometry must produce a **universal ADDITIVE dressing ~ m_p/N_c** (constituent ≈ current + 330 MeV), NOT a multiplicative ratio. A ratio → the candidate FAILS.

**Keeper | 2026-07-19 | Casey directive: have the team verify the two-mass candidate. Adjudication + the falsifiable test the team works against.**

## What's SOLID (not under test)
- **Every quark has two masses — standard, measured physics:** current (undressed, bare Lagrangian) mass and constituent (dressed, QCD-cloud) mass. up: 2.2 → 336 MeV; down: 4.7 → 336; s: 95 → 486; c: 1270 → 1500; b: 4200 → 4700. Proton ≈ 3 × 336 ≈ 940 MeV. **This is consistent with our understanding — it is not the thing under test.**
- The up-quark "soft spot" **is** this split: the current value is tiny/scheme-dependent, the constituent is ~99% dressing → no single clean observable ("computable, not cleanly observable," yesterday).

## THE CANDIDATE under test (BST hypothesis, NOT yet derived)
The two masses = the **two rank-2 Jordan idempotents** of the domain:
- **c₁ = bulk/interior idempotent → the current (undressed, bare) mass** = the bare radial moment of the Born/Bergman measure.
- **c₂ = Shilov/boundary idempotent → the constituent (dressed, confined) mass** — ties directly to the *proven* confinement = Schur/Shilov result (K745): the Shilov idempotent is the boundary/emission structure.
If it holds, **one geometric fact (rank = 2) explains the current/constituent split of *every* quark** — and that split is a genuine standard-physics puzzle (why constituent ≈ current + a near-universal ~330 MeV).

## ★ THE MAKE-OR-BREAK TEST (the discriminator — this is what the team verifies)
Nature relates current → constituent by a **universal ADDITIVE offset**, not a ratio:
| quark | current | constituent | offset |
|---|---|---|---|
| up | 2.2 | 336 | **+334** |
| down | 4.7 | 336 | **+331** |
| strange | 95 | 486 | +391 |
- Two idempotent eigenvalues are two numbers — they *can* be additive — **but only if the Shilov idempotent (c₂) contributes a roughly-universal +Λ ≈ 330 MeV.** Encouraging BST-scale candidate: **Λ ≈ m_p/N_c ≈ 313 MeV** (the proton mass shared among N_c quarks).
- **PASS:** the geometry produces c₂ = c₁ + Λ_Shilov with Λ_Shilov a *derived* universal additive scale (~m_p/N_c), matching the table. → the candidate is real; unifies with confinement.
- **FAIL:** the idempotent structure predicts c₂ = ratio·c₁ (multiplicative). → fails the additive table; retire the geometric reading.
- **A clean FAIL is a complete result.** Try to verify AND to falsify.

## ⚠ KEEPER PRE-AUDIT (two refinements before anyone runs it)
**(1) The "Λ ≈ m_p/N_c" match is NEARLY CIRCULAR — do not count it as a pass.** The proton *is* ~3 constituent quarks (m_p ≈ N_c·constituent), so m_p/N_c ≈ constituent ≈ (current + Λ) ≈ Λ for light quarks. Verified: dressing(up) = 334, dressing(down) = 331, m_p/N_c = 313 — but that agreement is tautological (Λ = constituent − current ≈ constituent ≈ m_p/N_c *by construction*). **Using m_p to predict Λ is circular** (m_p is built from the constituent masses). Cal must reject "Λ ≈ m_p/N_c ✓" as target-aware.
- **The TIGHTENED, target-innocent test:** derive **Λ_Shilov from the boundary geometry ALONE** — the Bergman/Szegő kernel evaluated at the Shilov boundary, or the domain's confinement/emission energy scale — **WITHOUT using m_p or any constituent mass as input.** If that independent geometric quantity lands ~330 MeV → **real PASS.** If Λ can only be gotten by feeding in m_p → circular, **not a derivation.**

**(2) The additive structure points to a SPECIFIC reading (the one likely to pass).** Two *independent* idempotent eigenvalues are generically NOT additive (they could relate any way). Additivity requires **not** two separate eigenvalues but **one mode: current = the bulk radial moment, constituent = current + a FIXED Shilov boundary-dressing energy Λ** — additive precisely because the boundary energy is a *fixed, mode-independent scale* (the confinement scale). So the version to test is "bulk energy + boundary dressing," not "two spectral eigenvalues." If the geometry instead ties the two masses multiplicatively → FAIL. This also sharpens Lyra's rep-theory task: is the second mass a separate eigenvalue (→ likely fails additive) or a fixed boundary-energy shift of the first (→ can pass)?

## THE SUB-TASKS (per CI)
1. **Lyra (rep-theory):** does the quark mass operator on the rank-2 domain genuinely have **two idempotent eigenvalues** (the Peirce c₁, c₂)? Identify which is bulk (current) and which is Shilov (constituent). Is the two-slot structure forced, or is "two masses = two idempotents" a relabeling? [the load-bearing derivation]
2. **★ Elie (the decisive computation):** compute the **Shilov idempotent's contribution Λ_Shilov**. Is it (a) **additive and universal** (~m_p/N_c ≈ 313 MeV — PASS) or (b) **multiplicative/a ratio** (FAIL)? Verify c₂ = c₁ + Λ against all six quarks' current/constituent values. This is the make-or-break toy.
3. **Grace (data + render):** assemble the current/constituent table (all 6 quarks) with the BST-scale candidates (m_p/N_c, Λ_QCD); render the two-idempotent/bulk-vs-Shilov picture; catalog on landing.
4. **Cal (referee):** **target-innocence** — is Λ_Shilov *derived* from the geometry, or *matched* to the observed ~330? (The 330 ≈ m_p/N_c must come from the Shilov idempotent, not be fit.) The additive-vs-ratio outcome is the honest discriminator — guard against forcing additivity.
5. **Keeper (audit):** hold the tier (CANDIDATE until the additive-universal dressing genuinely comes out); the confinement = Schur/Shilov tie-in; catch coincidence traps (Λ ≈ m_p/N_c is only meaningful if *derived*).

## Discipline
This is a candidate with a *sharp, falsifiable* test — the ideal shape. Retire the earlier "two masses with Born *probabilities*" framing (probabilistic alternatives); the correct physics is **current/constituent — both present** (bare + dressed), the two spectral slots. Don't bank the geometric reading unless the additive-universal dressing is *derived*. A clean negative (predicts a ratio) is complete and valuable.

— Keeper K757, 2026-07-19. Two-mass candidate: current/constituent = two rank-2 idempotents (c₁ bulk/current, c₂ Shilov/constituent). SOLID: every quark has two masses (standard). CANDIDATE: the geometric reading. TEST: does c₂ = c₁ + universal Λ_Shilov ~ m_p/N_c (additive, PASS) or a ratio (FAIL)? Elie's decisive toy. Retire the "Born probabilities" framing → current/constituent both-present. See [[Keeper_K755_derivation_push...]] (m_u soft), [[Keeper_K745_round5_audit...]] (confinement=Schur/Shilov).
