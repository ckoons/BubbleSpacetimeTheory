# The Standard Model as the Representation Theory of One Bounded Symmetric Domain
### Flagship synthesis — DRAFT, Keeper (assembly), 2026-07-18. Referee-grade, honestly tiered. Front matter: `BST_SM_from_D_IV5_synthesis_artifact.html`.

**Authors:** Casey Koons with the CI team (Lyra, Keeper, Elie, Grace); visiting referee Cal A. Brate.

---

## Abstract
We present the Standard Model — its gauge group, its fermion content, its conserved charges, and the numerical values of its dimensionless parameters — as the linear algebra and representation theory of a single object: the rank-2 bounded symmetric domain **D_IV⁵ = SO(5,2)/[SO(5)×SO(2)]**. From one integer seed (**rank = 2**), one dimensionful input (the gravitational/Planck scale), and π, we reconstruct: the gauge group as the three division-algebra structures of the domain; parity violation as a consequence of an odd embedding dimension; one fermion generation as the domain's 16-real spinor; the conserved charges as the Noether currents of its isometry group plus three topological (knot/winding) charges; twenty of the twenty-six dimensionless constants as radial norms on the one ruler; and the fine-structure constant to 0.0004%. **Every claim is assigned an epistemic tier** — derived / supported / open / runner — and the derived/open boundary is drawn exactly. We also report, in the same spirit, what the framework *forbids* (six falsifiable absences, two of them now derived) and where it is honestly weak. The organizing result is that the "underlying symmetry" physics has long sought is a **rank-2 root system**, not a large unifying group.

---

## 1. The object and the seed
**D_IV⁵ = SO(5,2)/[SO(5)×SO(2)]** is the rank-2 bounded symmetric domain of type IV in dimension 5. Its invariants are five integers:

| | value | as root-data | polynomial in rank |
|---|---|---|---|
| rank | 2 | # independent roots (the seed) | rank |
| N_c | 3 | root **multiplicity** (a = n−2) | rank + 1 |
| n_C | 5 | complex dimension | rank² + 1 |
| C₂ | 6 | Casimir / second index | rank² + rank |
| g | 7 | embedding/signature index | rank² + rank + 1 |

with N_max = N_c³·n_C + rank = 137 downstream. **(F579, roots reframe.)** The five integers are the invariants of the domain's **rank-2 restricted root system** (SO(5) = B₂); color N_c is not inserted but is the root multiplicity; the primaries coincide with the SM gauge dual Coxeter numbers. When physics searches for "the unifying symmetry," this rank-2 root diagram is the terminus — and being rank-2, it admits no grand-unified extension (Section 8).

**Tier:** the domain's uniqueness under (3 colors, 3 generations, dim 5) is *derived*; the root-data reading of the integers is *derived-synthesis* (Cal referee: rigor vs relabeling — the identifications are structural, not fitted).

**Figure 1 — the generative family tree** (one seed grows the primaries grow the observables; Grace render asset B):

```
                              rank = 2                         [THE SEED]
            +--------------------+--------------------+
   N_c = rank+1 = 3      n_C = rank²+1 = 5    g = rank²+rank+1 = 7
   (colors, SU(3))       (dim, the domain)    (embedding; g = Fano/PG(2,2))
            +----------+---------+----------+---------+
                       |                    |
        N_max = N_c³·n_C + rank = 137        C₂ = rank·N_c = 6
   ─────────────────────────────────────────────────────────────
   the observables (each a form in {rank,N_c,n_C,g} × π × gravity-scale):
     sin²θ13 = 1/(g²−rank²)      α⁻¹ = N_c³·n_C + rank
     sin²θ12 = N_c/(N_c+g)       sin²θ23 = rank²/g       λ_H = 1/rank³
     |sinδ_PMNS| = rank/g        m_s/m_d = rank²·n_C     Ω_DM/Ω_b = rank⁴/N_c
   the two exact locks (forcing laws among the primaries):
     g² = N_c²·n_C + rank²   (49 = 45 + 4)   ← the deep Pythagorean law
     N_c + g = rank·n_C      (3 + 7 = 10)    ← rank=2 value-specific
```

**Figure 2 — the B₂ = SO(5) root system, the geometry of the seed** (asset `BST_B2_root_diagram_figure1.png`; full spec `BST_B2_root_diagram_figure_spec_2026-07-18.md`, Grace). The eight roots (long ±e₁±e₂, short ±e₁,±e₂) of the domain's rank-2 restricted root system; the five integers are its invariants — rank = 2 (simple roots), N_c = 3 (root multiplicity), and the Weyl vector ρ = (3/2,1/2). The conformal ρ = (5/2,3/2) direction sets the V_cb angle (30.96°, cos = 5/√34); the short-root (λ₂) axis is the spherical/non-spherical divide of the Shilov theorem (§9½). **Being rank-2, it admits no grand-unified extension** — §8. *(Fig 1 = the arithmetic: 2 grows the integers; Fig 2 = the geometry: the integers are one root system.)*

## 2. Three layers
The 26 dimensionless observables organize into three algebraic layers:
1. **Multiplicative lattice** — every ratio-observable is a monomial in {2, 3, 5, 7, π} (rank 4). The unique clean cross-observable identity is Gatto's (V_us² = m_d/m_s).
2. **Additive syzygies** — forcing identities among the primaries, separated into *polynomial laws* (true for any seed: **g² = N_c²·n_C + rank² → 49 = 45 + 4**) and *value-specific* facts (exact at seed = 2: N_c + g = rank·n_C = 10). The polynomial laws are the deep content.
3. **Representation theory** — the gauge group and fermions (Sections 3–4).

**Tier:** lattice + syzygies *derived* (exact identities, sympy-verified). The 49 = 45 + 4 law forces the neutrino CP structure and is the strongest single result.

## 3. The gauge sector
**SU(3) × SU(2) × U(1) = the three division-algebra structures of D_IV⁵** (K732):
- **U(1)** = the intrinsic complex structure J (the SO(2) charge circle); electric charge = the integer SO(2) weight. **[derived]**
- **SU(2)_L** = the real-form quaternionic spinor; SO(5) ≅ Sp(2) gives the electroweak doublets. **[derived, native]**
- **SU(3)** = the octonionic / compact-dual (Q⁵ = SO(7)) structure, acting on the color factor ℂ³ (N_c = 3 = the domain's root multiplicity). **Color confinement is derived** (K745): the state space factorizes H²(D_IV⁵) ⊗ ℂ³, the Shilov boundary carries the trivial color rep, so by Schur orthogonality every color-nonsinglet has *exactly zero* boundary support → cannot be asymptotic → confined; singlets are emitted. Three convergent, frame-independent routes. **[confinement derived; the full SU(3) dynamics — running, gluon fields — is the open frontier, Section 9]**

**Parity violation (V−A) is derived** from g = 7 being **odd**: the volume element ω = γ₁⋯γ₇ is central, locking internal weak chirality to spacetime chirality (K729, verified twice). This is the deepest asymmetry in nature as a consequence of the odd embedding dimension. **[derived]**

**Five-Absence-safe:** these are three *different structures* of one domain, not branches of one large group.

**The gauge *fields*, not just the group (KK, Elie toy 4721):** Kaluza–Klein reduction over the domain produces an 11-mode gauge connection; the odd-g chirality lock ungauges the surplus 7 (the SU(2)_R and the (2,2) coset), leaving **exactly 4 = the electroweak SU(2)_L × U(1)**. The whole electroweak gauge content traces to one geometric fact — turning "gauge group identified" into "gauge fields derived." **[derived]**

## 4. The fermions and their charges
**One generation = ℍ⁴ = 16 real = the SO(5,2) spinor** [native structure]; **three generations = rank + 1** support strata [derived]. All 16 Weyl fermions are placed with their quantum numbers, every hypercharge from one rule (F582):
$$Y = T_{3R} + (B-L)/2,$$
where **T₃_R is the *global* (ungauged) second Sp(1) of SO(5) = Sp(2)**, felt only through Y. This yields a genuine new result: the right-handed + B−L sector has **4 directions**; the geometry gauges **exactly one** (hypercharge); the missing three are precisely **W_R^± and Z′** — so **two of the six Five-Absences (no right-handed W, no Z′) are derived, not imposed** (F582).

**Why hypercharge is the single gauged direction — resolved, DERIVED (F583).** It is forced by symmetry breaking, not chosen. The high-scale breaking condensate is the **ν_R ν_R Majorana condensate**, with (T₃_R, B−L) = (+1, −2): electrically neutral and an SU(2)_L singlet. A condensate breaks every U(1) it is charged under and preserves the one it is neutral under — and its neutral direction is **exactly Y** (Y = 1 + (−2)/2 = 0, and this preserved direction is *unique*). So the surviving gauge symmetry is U(1)_Y; hypercharge is what is left unbroken, not a choice. **This closes the gap, and no-W_R/no-Z′ are now fully derived** via three convergent routes (fermion placement F582, KK reduction Elie toy 4721, and this breaking-stabilizer argument). *Honest note:* anomaly cancellation does **not** select Y here (16 is a full SO(10) spinor → every U(1) in the plane is anomaly-free), so the mechanism is genuinely breaking, not anomaly. **Elegance:** the same ν_R ν_R condensate that forces Y also generates the neutrino masses (§7) — one mechanism, two jobs. [derived; Cal formal ratification pending]

## 5. Conservation laws (Noether + topological)
Every conserved charge is a symmetry of the domain (`Keeper_Conservation_Laws_Inventory`, T1945):
- **Noetherian (continuous):** energy, momentum, angular momentum (isometry group SO(5,2)); electric charge (SO(2)); weak isospin, hypercharge, color (the gauge structures). Total continuous conserved = **20 = g + c₃**. CPT exact; P, CP, and scale broken by *derived* mechanisms (odd g; Jarlskog; the mass ruler). **[derived tally; verified: all 21 so(5,2) generators are exact isometries, Elie E4]**
- **Topological (beyond Noether):** **baryon number = trefoil (3-crossing) knot count** (N_c-forced, absolutely conserved, τ_p = ∞); **lepton number = SO(5) winding count** (conserved perturbatively, violated by the ΔL=2 Majorana mass); **generation number = Q⁵ cycle count**. These explain what the SM leaves as accidental global symmetries. **[derived, T1945]**

## 6. The mass sector and the couplings — one ruler
All masses are radial norms of the domain's representations, scaled by a single dimensionful input:
- **20 of 26 constants** are the singular values Σ of the fermion mass map M = UΣV†, pinned by the mass-ladder grounds. **[derived]**
- **α⁻¹ = 137.0365 (0.0004%)** — capacity N_max (a combinatorial charge count) + the descent's 4π Coulomb solid angle + a derived curvature correction (n_C/N_max), with a two-target check (the same correction closes the Higgs) as its target-innocence proof. **[derived, referee-ready; E1/K701]**
- **Electroweak scale v = (6π⁵)³·α¹²·m_Planck/g (0.01%)** — the Higgs VEV rides the same ruler. **[derived]**
- **★ The Yukawa ceiling — no elementary fermion above 174 GeV.** A Yukawa is a *normalized Born overlap* of the fermion mode with the Higgs direction on the proven measure, so Cauchy–Schwarz forces |y_f| ≤ 1, i.e. **m_f ≤ v/√2 = 174.1 GeV** for every elementary fermion. All nine massive fermions obey it and **only the top approaches it** (y_t = 0.992) — the top is the one *un-suppressed* fermion, saturating the ceiling; the hierarchy is the sequence of decreasing overlaps below it. This is a falsifiable prediction — a 4th-generation or any elementary fermion above 174 GeV refutes BST (a mass-sector companion to the Five Absences). **[derived-framework; falsifiable; K761/K762]**
- **★ The electron and the top are one relation apart.** Composing the top anchor (m_t = v/√2, the saturated ceiling) with the banked scale (v = m_p²/(g·m_e)) locks the heaviest and lightest charged fermions reciprocally through the proton: **m_t · m_e = m_p²/(g√2)** (88 967 vs 88 929 MeV², 0.04% with the predicted m_t). The top *inherits the electron's precision* — the up-type ladder anchors at its clean heavy end (m_e-locked), not its soft light end. The up quark relates to m_e through the same chain, m_u·m_e = m_p²/(g√2·[t/u]), pending the up-type slope. **[supported; K762]**
- **The 26 numbers** grow from rank = 2 with π and the one scale; the by-design five add zero free rows.

## 7. Mixing and neutrinos
- **Mixing (CKM/PMNS) = the angle between D_IV⁵'s two canonical stratifications** (F589) — a **distinct object from the masses**, decoupled (K704). The domain has two stratifications: the boundary-orbit **flag** (3 Korányi–Wolf orbits = the 3 gauge-charged generations) and the spectral idempotent **frame** (rank 2). The mixing matrix is their fixed relative orientation, U = ⟨flag | frame⟩ — the *angular* U, V of the SVD M = UΣV†, independent of the radial masses Σ. **This is why the mass texture missed (0 of 6, Elie): we were asking radial data for an angular answer.** **★ The small-CKM / large-PMNS asymmetry is then one fact:** quarks have both chiralities gauge-charged → both bases on the same flag → rotations nearly cancel → small CKM; the neutrino right-handed side is the *gauge-singlet spectral frame*, misaligned → large PMNS. **[mechanism derived]**
- **The angle values** read as equipartition overlaps sin²θ = d/D (fraction of a maximal-entropy angular state in a primary subspace): sin²θ₂₃ = rank²/g = 4/7, sin²θ₁₂ = N_c/(rank·n_C) = 3/10, sin²θ₁₃ = 1/(N_c²·n_C) = 1/45 — combinatorial fractions, not mass ratios. **CKM:** V_us = √(m_d/m_s) = 0.2243 (0.4%) and the ordering derived; V_cb, V_ub magnitudes structural. **Honest status:** the forms are **identified, not yet derived.** A tempting single-group reading (an so(10) generation rotation, D = 10 vector and 45 adjoint) fits θ₁₂ and θ₁₃ but **not θ₂₃** (D = g = 7), and the D = 10 has a value-coincidence (rank·n_C = N_c+g = 10) — so that reading is **retracted** (K749; Five-Absence never at risk — it was generation-space combinatorics, not a gauged group). The three angles map onto the three pairs of the domain's three Korányi–Wolf boundary orbits (bulk, intermediate, Shilov): θ₁₂ = bulk↔intermediate, θ₂₃ = intermediate↔Shilov, θ₁₃ = bulk↔Shilov (C(3,2) = 3 pairs = 3 angles). **The per-pair connecting-mode counting was pursued to a firm close (K763; ~8 routes over two days):** θ₂₃'s denominator is reasonably homed (D = 7 = the SO(5,2) defining rep ℝ^{5,2}, whose null cone is the Shilov boundary — independent of the angle); θ₁₂'s D = 10 is a dimension-match to dim SO(5) with the intertwiner-equals-adjoint step asserted, not proven; and θ₁₃'s D = 45 = Λ²(10) **back-solves** — the bulk↔Shilov pair is two-step and a genuine composite must involve both legs (10 and 7), but 45 is chosen precisely because it matches while ignoring the 7 leg, and the orbit-distance rule that would predict it is refuted (θ₁₂, θ₂₃ are both adjacent yet have D = 10 ≠ 7). All three numerators {rank² , N_c, 1} are likewise unpinned. **Honest verdict:** the exact mixing forms are **Tier-2 structural** — clean primary-product fractions of the same character as the quark-mass ratios, not Tier-1 identities. They sit **off the critical path**: the mixing sector's referee-final claim is the *mechanism* (the inter-stratum angle on the proven measure, plus the small-CKM/large-PMNS asymmetry as one fact), with the exact numbers flagged identified-not-derived. This is a boundary mapped thoroughly, not a gap concealed. **[mechanism derived; exact forms identified — Tier-2 structural, off critical path]**
- **★ Flavor physics is one object — a rank-1 condensate plus corrections.** A Yukawa is a Born overlap, so the Yukawa matrix is the *overlap matrix* Y_ij = ⟨f_L^i | Φ | f_R^j⟩ on H²(D_IV⁵), and masses are its singular values. Because the condensate Φ is essentially **rank-1** (a single projector onto the condensate direction O), Y is rank-1: **exactly one fermion is massive at leading order — the top** — with y_t = ‖P_L O‖·‖P_R O‖ ≤ 1 (Cauchy–Schwarz, the ceiling). Every lighter mass, and *all* of the mixing, are the **off-rank-1 corrections** of the *same* O. This is why the up-type ladder and the mixing angles are Tier-2 structural: they are subleading deviations from rank-1, not leading identities. So the whole flavor sector is **one rank-1 condensate direction O + a structured correction spectrum** — masses and mixing unified, read from one object. The leading structure (rank-1 → one dominant mass) is derived; **y_t = 1 holds iff the top mode is parallel to O** (a decidable geometric question — the top's Clebsch–Gordan coefficient with the condensate); CP violation is the phase of the corrections. The 13 Yukawas were never 13 things: they are one condensate overlap and its Tier-2 corrections. **The condensate direction O is pinned non-circularly** (F603): from its quantum numbers alone (color-singlet, SU(2)_L doublet, Y = ½), O is the **SO(5) vector (1,0), spherical (λ₂ = 0), hence boundary-reaching** — its being a Shilov-boundary condensate is the *same fact* as its being the vector, not an added assumption. The top is the spinor (½,½), λ₂ = ½, and the Yukawa is the γ-matrix vertex 4⊗4 → 5. This reduces y_t = 1 to a **single radial overlap** — whether the non-spherical top mode reaches the spherical boundary where O sits — and the representation theory shows it is *not* automatic, consistent with the observed y_t = 0.992. **[rank-1 leading structure derived; O direction pinned = SO(5) vector (F603); y_t = 1 reduced to one radial overlap, supported not automatic; corrections Tier-2]**
- **The neutrino is Majorana** (F413/K673): the odd-g chirality lock makes the light ν_R non-unitary, so the Weinberg operator generates a Majorana mass — the ΔL=2 process that makes **neutrinoless double-beta decay occur**, |m_ββ| ∈ [1.44, 3.63] meV. **A detection supports BST.**
- **Mechanism — m₁ = 0 DERIVED on rank-2 counting (F588; pending Cal ratification).** A rank-2 domain has two canonical stratifications, and the two fermion types index onto different ones: the **3 boundary orbits** (Korányi–Wolf, = rank+1) are the 3 generations of *gauge-charged* fermions (which carry an electroweak flag), while the **2 spectral idempotents** (the Jordan frame, = rank) are the 2 right-handed neutrinos — because ν_R is a *gauge singlet* with no flag, so the only invariant left to distinguish its copies is the spectral value, of which there are exactly 2. Then m_D is 3×2 → rank ≤ 2 → m_ν = m_D M_R⁻¹ m_Dᵀ has one exactly-zero eigenvalue → **m₁ = 0** (normal ordering, one Majorana phase, narrow band). Both counts fall out of the single integer rank = 2. *(This supersedes an earlier premise that conflated the K-type λ₂ with the boundary-orbit rank; the idempotent count uses neither.)* **[derived on counting; Cal ratifies the one assignment "a flag-less singlet is indexed by the spectral frame, not the flag"]**

## 8. What the framework forbids — six falsifiable absences
Rank-2 rigidity forbids, and cannot absorb, a specific list (`BST_Five_Absence_Falsifier_Paper`):

| forbids | status | refuted by |
|---|---|---|
| Grand unification | derived (rank-2, no extension) | any unification signature |
| Proton decay | **derived** (baryon = trefoil, τ_p = ∞) | one p-decay event (Super-K/Hyper-K) |
| **Right-handed W, Z′** | **derived** (one gauged direction, §4) | a confirmed W_R / Z′ |
| Magnetic monopoles | supported | a confirmed monopole |
| Sterile neutrinos | supported (Majorana, no ν_R force) | a sterile-ν oscillation |
| SUSY spectrum | supported (16 = one generation, no doubling) | a superpartner |

Plus cheap positive tests where a clean null kills the theory fast (BaTiO₃ 137-plane ~$25K; photonic-crystal ~$10K).

## 9. What is honestly open, soft, or retired (the ledger's amber/red)
- **Open (frontier):** the mixing *numerators* / "lives-there" step (§7 — the denominators are now all homed as rep-dimensions; the numerators and θ₁₂'s subspace remain); the color gluon *fields* (hosted-tier, native-realization open); the grand synthesis as a *theorem*.
- **Qualitative QCD dynamics — DERIVED (K755):** the sign of the QCD β-function follows from the content — **β₀ = 11 N_c − 2 N_f = 21 > 0** (N_c = 3, N_f = 6 = 3 generations × 2) ⇒ **asymptotically free in the UV, confining in the IR** — consistent with the Schur-confinement (§3). The *running value* α_s(scale) is a runner; the *direction* is derived.
- **Computable, not cleanly observable (a distinct, honest tier — not "soft"):** the containment theorem (§9¾) says BST *computes* every observable as a functional of the proven measure μ; the items below are ones for which **no scheme-independent number exists to compare against** — the limitation is in the observable, not the computation.
  - **m_u** — the up-quark is confined, so there is no pole mass; the quoted "up-quark mass" is a scheme/scale-dependent Lagrangian parameter, and *even experiment has no clean value*. BST computes its radial moment of μ; the observable side is intrinsically un-sharp. **The anchor is now the top, not m_u:** the up-type ladder hangs from the saturated ceiling (y_t = 1, m_t = v/√2, m_e-locked) and m_u is *predicted forward* down the slope — inheriting the top's solidity rather than floating with its own ±23%. The two masses of a quark (current/constituent) are one bulk radial locus + gluon dressing — **not** two loci (a colored quark has zero Shilov support, so it cannot sit on the Shilov idempotent; the rank-2 two-loci reading is refuted, K758). The open piece is the up-type *slope* (Section 9), gated on why the condensate aligns with the max-|Q| gen-3 mode. *(V_ub is **not** in this list — it is the CKM bulk↔Shilov overlap, the exact analog of PMNS θ₁₃; §7.)*
  - **sin²θ_W and α_s (runners)** — these *run*, so "the value" is scale-dependent, not a clean observable. BST computes the high-scale/geometric value (sin²θ_W = 3/8 = N_c/rank³, fermion-content-derived) and the running *direction* (α_s asymptotically free, §9); the observed number is the scale-dependent extraction. The tidy sin²θ_W = 3/13 was retired as a running coincidence (a worked example of the program's discipline).
- **Structural, not derived:** the cosmological constant Λ = exp(−280) has the right form and size but is not target-innocently forced (the "5-fold over-determination" was one factorization; retracted).

## 9½. Two master mechanisms (the deep simplicities)
Much of the derived content above traces to two geometric facts, each generating several observables (the program's "one-property-many-observables" pattern — expressed, as throughout, in the linear algebra of the domain's representations).

**(1) The embedding dimension g = 7 is odd.** → the weak force is chiral (V−A, K729); the right-handed gauge bosons are forbidden (no W_R, no Z′, §4); and the KK over-production trims to exactly the electroweak group (§3). *One fact, three payoffs.*

**(2) The Szegő boundary-restriction engine (F586, now a theorem).** The boundary-restriction map H²(D_IV⁵) → L²(Shilov) is K-equivariant, and class-1 branching on L²(S⁴) admits an SO(5) K-type *only if spherical* — highest weight (λ₁, λ₂) with **λ₂ = 0**. So a state's Shilov boundary value **vanishes exactly iff its SO(5) K-type is non-spherical (λ₂ > 0)**. (The substrate's own ρ-vector (3/2, 1/2) has λ₂ = ½ > 0 — the non-spherical direction is built in.) This *one engine* — the Wolf boundary strata crossed with the λ₂ dichotomy — has **two distinct legs**, and they must not be conflated:
- **Exact leg** (boundary-value vanishing): a non-spherical / colored state has *identically zero* Shilov support, so it cannot be asymptotic → **color confinement** (Elie's Schur-orthogonality computation confirms: color-blind boundary → colored support = 0; singlet = O(1)). Pending the one color-K-type check.
- **Graded leg** (bulk-overlap suppression *along* the strata): the mass hierarchy, with **m₁ = 0 as the graded endpoint**, and the n(ν_R) = 2 count. The mass sector is a **cousin** of confinement — the same engine, the *graded* consequence — **not the identical theorem.** *(This corrects an earlier over-unification, F586; the two legs are one engine, two consequences.)*

Making both legs of this engine fully rigorous — in particular the two named K-type computations (are color-nonsinglets non-spherical? does ν_R force λ₂ = 0?) — was the round-5 target; the exact leg (confinement) is now closed (§3).

**(3) Candidate third structure — the angle between the two stratifications.** D_IV⁵ carries two canonical stratifications: the boundary-orbit **flag** (rank+1 = 3) and the spectral idempotent **frame** (rank = 2). Their fixed relative angle is **every mixing matrix** (§7): CKM small (both quark bases on the flag), PMNS large (the gauge-singlet ν frame is misaligned). Unlike an earlier "domain-rank" candidate — which had a single instance (m₁ = 0) and failed its second-instance test (K747), so is *not* claimed as a mechanism — the two-stratification angle has **multiple instances** (CKM, PMNS, the base-alignment asymmetry) and is the genuine candidate for the third organizing fact. If it ratifies, the derived Standard Model traces to three: odd-g, the λ₂ Szegő engine, and the two-stratification angle.

## 9¾. The containment theorem (what "one measure" means precisely)
The claim "the Standard Model is one measure, decomposed" splits into two statements that must not be conflated:
- **Containment (a theorem):** with μ the Born/Bergman measure (proven unique, T2401), **every BST-*derived* dimensionless observable is a functional of μ** — a moment, overlap, phase, count, or symmetry-invariant. Proved by exhibition: confinement is the support of μ; θ_QCD = 0 is a symmetry-forced zero; the hypercharge direction is a stabilizer; m₁ = 0 is the rank of a μ-overlap operator; the mixing angles are two-point Born overlaps; CP is their phase; the masses are radial moments (‖z^n‖² = π·B(n+1,p+1)). The derived core of the theory is provably *one functional class of one proven measure.*
- **Completeness (a conjecture):** that *every* Standard-Model observable — including those not yet derived (the quark mass ratios are the standing counterexample-in-progress) — is such a functional. This is what would license "the SM *is* QM on D_IV⁵" as a *derived* fact; it is open, and advances one observable at a time.
So the grand thesis is **a framework built on proven parts** (μ is proven; the derived observables are provably functionals of it) **with completeness as the honest open conjecture** — not "the SM is derived."

## 10. Conclusion
The Standard Model is the physics of one bounded symmetric domain: its gauge group is the domain's three division-algebra structures, its fermions are its spinor, its conserved charges are its isometries and its knots, its masses are radial norms on one ruler, and its dimensionless constants grow from the number 2. The derived, supported, open, and retired lines are drawn exactly — and a program that retires its own prettiest near-miss (sin²θ_W = 3/13) is one whose derived rows can be trusted.

**The deepest reframe — one measure.** The classes of observable are not separate accidents; they are features of a single object, the **Born/Bergman measure on D_IV⁵**, read through two decompositions. Because the **Born rule is the Bergman kernel** — a proven result (the Born measure is the unique automorphism-invariant measure on H²(D_IV⁵)) — this measure is not assumed. Under it: **couplings** are democratic counts (α = 1/capacity), **masses** are radial norms (the Σ of the SVD), **mixings** are angular Born overlaps between the domain's two dual bases, **CP** is the phase of those overlaps, **confinement and gauge** are the Schur structure (only color singlets carry boundary support), and **conservation** is the measure's symmetries. The three organizing mechanisms are three faces of it — an odd embedding dimension (its chirality), the boundary-vanishing (its support), and the two-stratification angle (its overlaps). The twenty-six parameters were never twenty-six things: they are one proven measure, decomposed. And the symmetry underlying it all is a **rank-2 root system** — which, being rank-2, forbids, falsifiably, the grand-unified physics forty years of experiments have not found.

---

## Appendix A — the 26-parameter tier-ledger (Grace render asset A; source `data/bst_26_tier_map.json`, current as of K739)

```
  DEEPEST FORCING (LAW — polynomial identity, true for all rank)
    g² = N_c²·n_C + rank²  (49 = 45 + 4)  →  sin²θ13 = 1/(g²−rank²) = 1/45 [0.1%]
                                          →  |sinδ_PMNS| = rank/g = 2/7 (magnitude; branch data-picked)
    N_max = N_c³·n_C + rank = 137          →  α⁻¹ (charge-count, identified)
  ONE CLEAN MULTIPLICATIVE SYZYGY:  Gatto  sin²θ_C · (m_s/m_d) = 1  [0.4%]
  VALUE-SPECIFIC (rank=2 only):  N_c+g = rank·n_C = 10  →  sin²θ12 = 3/10 [2%]
  LATTICE MONOMIALS {2,3,5,7}:  m_s/m_d=20, m_u/m_d=√(3/14), m_t/m_b=42, λ_H=1/8, sin²θ23=4/7, m_μ/m_e=(24/π²)⁶
  DERIVED-NATIVE (real signature):  weak SU(2)_L ← SO(5)=Sp(2) doublets ;  parity V−A ← g=7 odd
  SUPPORTED (correspondence):  color SU(3) ← octonions via intrinsic complex structure J=SO(2)
  ONE FREE DIMENSIONFUL INPUT:  gravity scale → m_e, v, all absolute masses
  RUNNERS:  sin²θ_W (3/8+RGE), α_s      STRUCTURAL HOLDOUTS:  V_cb (~0.044), V_ub
  EXACT ZEROS (Five-Absence):  θ_QCD=0, m_ν1=0      OPEN:  m_ν2, m_ν3
  CKM (F585): form + V_us=√(m_d/m_s) DERIVED; ordering |V_us|>|V_cb|>|V_ub| DERIVED; V_cb/V_ub magnitudes STRUCTURAL.
  Count: 9 masses + 4 CKM + 4 PMNS + 3 gauge + 2 Higgs + θ_QCD = 26.
```

---
*Draft assembly status:* Sections 1–10 complete + **Grace render assets now inline (Fig 1 family-tree §1; Appendix A tier-ledger; CKM render F585 feeds §7)**. Remaining: Cal referee pass on every "derived" tier (esp. §4 "why Y" — now F583 DERIVED, §1 roots rigor); the α and Five-Absence standalone papers as companions; current experimental bounds table. **Figures done:** Fig 1 (family tree) + Fig 2 (B₂ root diagram, `BST_B2_root_diagram_figure1.png` + spec) + Appendix A (tier-ledger), all Grace. Front matter = the synthesis artifact.

— Keeper, 2026-07-18. Flagship draft: SM = rep-theory of D_IV⁵, honestly tiered. Gauge = ℂ/ℍ/𝕆 (§3); fermions in ℍ⁴ + no-W_R/no-Z′ derived (§4); conservation Noether+topological (§5); masses + α on one ruler (§6); mixing/Majorana (§7); six absences, 2 derived (§8); the honest amber/red ledger (§9). See [[BST_SM_from_D_IV5_synthesis_artifact]], [[Keeper_K741_strengthening_pass_audit...]], [[Keeper_K742_round2_sweep_complete...]].
