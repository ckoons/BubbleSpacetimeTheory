# BST Verification Tests — July 2026 (v3)

**A living catalog of how BST is tested against, and distinguished from, modern physics. Grounded in `data/bst_predictions.json` (113 predictions, tiered D/I/C/S) and the Five-Absence principle. Compiled by Keeper, 2026-07-10; v3 2026-07-11 (mass sector folded in, Bell retired). We add and refine as the program improves.**

**v2 — 2026-07-11: SP-30-5 (the CHSH Bell deviation) RETIRED — it leaned internal (observable Bell max is standard 2√2; 2.806 is substrate granularity, not a Bell prediction). The sharpest live falsifiers are now, in order: neutrinoless-double-beta null, EHT circular polarization (existing data), neutrino mass ordering (JUNO), neutron EDM / no-axion. Quark masses + CP's J remain gated on the Wallach-1979 continuation (a reference wall).**

**v4 — 2026-07-12: pred_004 (0νββ) DEMOTED banked→CONTESTED (K673). The banked Dirac/no-0νββ prediction carried an internal-consistency flaw (a Dirac ν needs a right-handed ν_R, which conflicts with BST's banked no-steriles), and two independent derivations now lean Majorana. It can no longer be cited as a firm "0νββ never." New test structure in Section 1 row 2: BST is normal-ordering, so >15 meV kills it either way, 1–4 meV confirms Majorana-BST. Full flip gated on 3 items (electron stratum F144-vs-K294, rigorous RH-absence, ν=1/2-forced-by-charge). δ_CP also corrected to OPEN (was reverse-fit). Neutrino masses/mixings unaffected.**

**v3 — 2026-07-11 PM: the MASS SECTOR landed in-corpus and joins the sharpest falsifiers. The quark-mass "Wallach wall" was partly a wrong-target error (constituent vs current); against current masses the down ratios bank (s/d = 20 forced, 0.5%) via the FK generalized Pochhammer, the up-type top and charm masses are *predicted* from the forced electroweak scale v = m_p²/(g·m_e) (174 GeV at 0.78%, 1269 MeV at 0.05%, zero heavy-quark input), and the charged leptons close on Koide = rank/N_c (muon at 0.05%). These SM-observable value predictions — added to Sections 1 and 3 — are now BST's real falsifiers, replacing the retired tabletop tests. Only CP's Jarlskog J remains Wallach-gated. The one-paragraph case (Section 8) and the mass caveat (Section 7) are updated to match.**

---

## How to read this

**Two ways BST differs from modern physics:** it is *more predictive* (it fixes parameters the Standard Model measures as free) and *more restrictive* (it forbids most of the beyond-Standard-Model zoo). So every test is one of: **"search for the forbidden thing"** (a detection falsifies BST) or **"check the predicted number"** (a mismatch falsifies BST).

**Tiers** (assigned at creation): **D** = derived (mechanism proved), **I** = identified (<1%, mechanism plausible), **C** = conditional (depends on a conjecture), **S** = structural (>2% or qualitative). *A test's strength as evidence is bounded by its tier — do not read an S-tier match as a D-tier confirmation.*

**Status:** untested · in_progress · consistent · confirmed · tension.

**Honesty rule:** a null result on a forbidden-thing search is *consistency*, not proof. A precise match on a value is stronger. Only binary, decisive tests (Section 1) can confirm or kill quickly.

---

## Section 1 — The sharpest / fastest falsifiers (decidable soon, decisive)

These are the ones to lead outreach with: definite predictions, experiments running or near-term, a clear yes/no.

| # | Test | BST predicts | Falsified if | Instrument · timeline | Tier · status |
|---|---|---|---|---|---|
| 1 | ~~**CHSH Bell deviation (SP-30-5)**~~ | **RETIRED 2026-07-11.** The observable Bell max is the standard 2√2 (grounded in T754/T1417/T755/T757); S ≈ 2.806 is a finite-cell *internal* substrate quantity (the 1/2^N_c reduction lives in the non-physical (1−P) complement, per Cal #259; Elie showed finite-D does not force S<2√2). Not a discriminating tabletop test. Final decider still available: the max holonomy on D_IV⁵ *within H²* (< 2√2 revives it; = 2√2 confirms retirement). | — | — | **RETIRED** |
| 2 | **Neutrinoless double-beta decay (pred_004) — CONTESTED (K673, 2026-07-12)** | **No longer a firm "null."** BST is normal-ordering; the Dirac/Majorana question is an open *internal* issue (Majorana leading, K673). Test structure: a detection **> ~15 meV** (inverted floor) kills BST **either way**; **1–4 meV** confirms Majorana-BST; null-to-1meV is consistent with Dirac-BST. | Detection > 15 meV → FATAL (BST is normal-ordering) | LEGEND-1000, nEXO, CUPID · 2027–2032 | **S** · contested (was "sharpest binary"; demoted pending the 3 K673 gates) |
| 3 | **EHT horizon circular polarization (pred_009)** | Black-hole horizon CP = **α = 0.73%**, independent of BH mass and frequency | EHT measures CP ≠ 0.73%, or CP depends on mass/frequency | EHT M87*/Sgr A* reanalysis — **existing data**, remove V=0 assumption · 2025–2027 | **S** · untested |
| 4 | **Neutrino mass ordering (pred_003)** | **Normal ordering**, m_ν1 = 0 exactly, Σm_ν = 0.058 eV | Inverted ordering, or Σ ≫ 0.06 eV, or m_ν1 > 0 | JUNO, KATRIN, Project 8, CMB-S4 · 2026–2032 | **S** · untested |
| 5 | **Neutron EDM / strong-CP** | θ_QCD = **0 exactly** (topological, π₁ trivial) ⇒ neutron EDM = tiny CKM value only, **no axion** | Neutron EDM above the CKM floor implying θ≠0; *or* an axion detection | nEDM experiments; ADMX (axion) · ongoing | derives from banked θ_QCD=0 |
| 6 | **Down-quark mass ratio (F506)** | **s/d = (N_c+1)(N_c+2) = 20 exactly** (current mass); d:s:b = 1:20:840 | Improved current-mass determination pulls s/d away from 20 | Lattice QCD (FLAG averages) · ongoing | **I** · consistent (0.5%) |
| 7 | **Top & charm masses (F509/4621)** | **m_top = v/√2 = 174 GeV**, **m_charm = α·v/√2 = 1269 MeV**, from v = m_p²/(g·m_e), zero heavy-quark input | Either mass moves outside its band as v or the pole/MS-bar scheme sharpens | PDG / lattice · ongoing | **I** · consistent (0.78%, 0.05%) |
| 8 | **Muon mass from Koide (rank/N_c)** | **Q = rank/N_c = 2/3** ⇒ **m_μ/m_e = 206.9** given m_τ/m_e = 49·71 | Koide Q drifts from 2/3, or m_μ/m_e mismatch | PDG (already 0.00007 on Q) · FCC-ee tightens | **I** · consistent (0.05%) |

*Rows 6–8: these are already-measured values, so they read as strong consistency now; their teeth are that improved precision (lattice current masses, FCC-ee) can still break them, and they are target-innocent (predicted from forced integers with no mass input). Per BST's falsifier reframe these SM-observable predictions — not the retired tabletop tests — are where the theory is genuinely at risk.*

---

## Section 2 — The Five-Absence forbidden list (BST says NO where beyond-SM says maybe)

BST's strongest *structural* difference from modern physics. Each is a hard falsifier; each is currently consistent with data, and the collective null result across all of them is the theory's quiet argument.

| Forbidden thing | BST | Detection falsifies? | Current data | pred · tier |
|---|---|---|---|---|
| **Proton decay** | τ_p = ∞ (ℤ₃ protection) | **FATAL** | Super-K: τ > 1.6×10³⁴ yr — consistent | pred_017 · I |
| **SUSY partners** | none (B₂ root system excludes) | **FATAL** | LHC: none < ~2 TeV — consistent | pred_018/045 · I |
| **Dark-matter particles** | none — DM is topological (incomplete windings), DM/baryon = 16/3 | Fatal to DM ontology | LZ/XENONnT/ADMX all null — consistent | pred_019/059 · I |
| **Majorana neutrinos / 0νββ** | ~~none — Dirac~~ **CONTESTED (K673): Majorana now leading** — Dirac null carried an internal-consistency flaw (needs ν_R vs no-steriles). Not a Five-Absence item pending K673's 3 gates. | see Section 1 row 2 | KamLAND-Zen null — consistent with both | pred_004 · S · contested |
| **Sterile neutrino as DM** | none | falsifies | short-baseline/cosmology null | Five-Absence |
| **Magnetic monopoles** | none (no GUT) | falsifies | MoEDAL/IceCube null | Five-Absence |
| **GUT unification** | none | falsifies | no proton decay, no monopoles | Five-Absence |

**The meta-point for outreach:** beyond-SM physics predicted these for forty years and found none. The theory that predicted "you'll find none of them" is on the right side of the entire null landscape, while the theories that predicted them are increasingly strained. Soft evidence — but the asymmetry (many ways to die, still alive) is what a real theory has.

---

## Section 3 — Precision value predictions (BST fixes SM free parameters)

Where the SM measures a free parameter, BST predicts a number. Matches to date; future precision tightens or breaks them.

- **Ω_Λ = 13/19 = 0.68421** (pred_020, I) — Planck: 0.685±0.007. DESI/Euclid/Rubin tighten. Also w = −1 exactly (see tensions).
- **Ω_DM/Ω_baryon = 16/3** (pred_059/019) — the topological-DM ratio.
- **Koide Q = 2/3 = rank/N_c** (pred_048, I) — PDG: 0.66661±0.00007. Closes the charged-lepton sector: with m_τ/m_e = 49·71 = g²·(2^C₂+g) it forces **m_μ/m_e = 206.9** (obs 206.77, 0.05%), zero muon input. FCC-ee distinguishes. *Open: derive Q = rank/N_c from the colorless geometry.*
- **Quark masses (F506/F509/4621, I):** down ratios **d:s:b = 1:20:840, s/d = (N_c+1)(N_c+2) = 20 forced** via the FK generalized Pochhammer at ν = N_c (0.5% vs current); up-type **m_top = v/√2 = 174 GeV** (0.78%) and **m_charm = α·v/√2 = 1269 MeV** (0.05%), both from the forced electroweak scale v = m_p²/(g·m_e) = 246.1 GeV with no heavy-quark input. The gen-1 inversion m_u < m_d is forced (up = ground state, doublet-flip of the down). *Open: the up-type interior rung; the up n=0 value is soft (~22%).*
- **Higgs trilinear λ₃ = SM value** (pred_047, S) — no BSM deviation. HL-LHC/FCC-hh.
- **MOND scale a₀ = c·H₀/√(n_C·C₂) = 1.195×10⁻¹⁰ m/s²** *derived* (pred_021, I) — McGaugh: 1.20±0.02. A₀ is a free fit in MOND, absent in ΛCDM; BST derives it.
- **N_efold = rank²·N_c·n_C = 60 exactly** (pred_055, I) — distinguishable from 50/70.
- **z_eq = rank·N_c⁵·g = 3402** (pred_057, I) — Planck: 3387±21.
- **Neutrino mixing:** sin²θ₁₃ = 1/45, Δm²₃₁/Δm²₂₁ = 33 — banked, within 1σ.
- **Glueball spectrum vs lattice QCD** (T1402/T1403, S): 0⁻⁺/0⁺⁺ = 3/2 (0.2%), 2⁺⁺/0⁺⁺ = √2 (1.2%), 0⁺⁺ mass ~1.5–1.7 GeV (~3%); SU(N)/SU(M) mass-gap ratios √(g/C₂), √(8/7) (0.2%).
- **Ice/water density = 11/12** (pred_052, D) — **confirmed to 0.01%**.

---

## Section 4 — Cosmology (mostly next-gen CMB and surveys)

- **Full CMB power spectrum from D_IV⁵** (pred_008, I) — all six ΛCDM parameters derived; χ²/N target ~0.01. Planck reanalysis, LiteBIRD, CMB-S4.
- **No primordial B-modes, r ≈ 0** (pred_022, D) — spectral (not dynamical) inflation, no tensor source; QG floor r ~ 1/N_max² ~ 5×10⁻⁵. **Distinguishes BST from Starobinsky R² (r = 0.003)** at CMB-S4. Falsified by r > 0.001.
- **D_IV⁹ competitor CMB echo at ℓ ~ 3089** (pred_044, S) — 4% power-law or 10⁻¹⁰ exponential suppression; edge of Planck, CMB-S4 tests.
- **Periodic table terminus Z = 137 = N_max** (pred_007, S) — no stable element beyond. Superheavy programs.
- **Nuclear magic number 184** (pred_002, S) — 8th magic number. *(Note: per Cal K601 re-tier 2026-06-29, the per-magic-number forms are post-hoc; the 184 island prediction survives via shell model, not unique BST forcing.)*
- **Black-hole GW echoes, Δt = 137·r_s/c** (pred_005, S) — Haldane cap replaces singularity. LIGO/Virgo/KAGRA. *(Related to the cosmology-paper nucleation thread; see caveats.)*
- **Stochastic GW background** (pred_011, I) — f ~ 6.4 nHz, γ = 3.60. NANOGrav/IPTA (in progress, spectrum under debate).

---

## Section 5 — Confirmed / consistent (the track record that earns a look)

- **D_IV⁵ uniqueness** (pred_043, D) — **proved**: unique rank-2 BSD meeting four independent locks (1 survivor of 38).
- **Tsirelson bound ≤ 2√2** (pred_054, D) — **confirmed**: BST derives the ideal bound from rank-2; it is never *exceeded*. (SP-30-5 predicts it is not quite *reached* — Section 1.)
- **Ice/water = 11/12** (pred_052, D) — confirmed 0.01%.
- **Cancer driver Hamming structure** (pred_051, D) — confirmed in COSMIC-type validation.
- **Team-size optimum ≈ 6 = C₂** (pred_024, I) — consistent with org-psych.
- **Glueball / mass-gap ratios** — match lattice QCD (Section 3).
- **All Five-Absence searches** — consistent (no proton decay, SUSY, WIMP, axion, monopole, 0νββ).
- **α ruled derived**, θ_QCD = 0, the cosmological cluster (Ω_Λ, Ω_DM/Ω_b, n_s) — banked this year.

---

## Section 6 — Current tensions (honest — watch these)

- **Dark-energy w = −1** (pred_046, **C-tier, status: tension**) — BST: w = −1 exactly (spectral eigenvalue), or −0.99973. DESI DR2: 2.3σ hint for w ≠ −1. If w is confirmed dynamical at >5σ, BST needs to accommodate it. *The most active tension.*
- **CKM \|V_ub\| = 0.00360** (pred_049, **C-tier, tension**) — 2.25% below PDG 0.003682±0.00007. Belle II may sharpen; would require a higher-order CKM correction.

These are the honest weak spots and the first places a critic will push.

---

## Section 7 — Caveats and honesty (July 2026)

- **The Bell deviation (SP-30-5) was RETIRED on 2026-07-11** after the observable-interpretation check (Grace + Elie). The load-bearing question — is S_BST ≈ 2.806 the *measured* CHSH observable or an internal quantity — resolved to *internal*: four of the corpus's own theorems (T754 Gleason, T1417 observable CHSH = 2√2, T755 holonomy-max = 2√2, T757 QM reproduced) give the observable Bell max as the standard 2√2, and Elie showed the "finite-D ⇒ S < 2√2" mechanism is false (ordinary qubits saturate 2√2). The 2.806 is a real *internal* substrate granularity, but not a Bell prediction. **Lesson banked:** caught before outreach — a Bell experimentalist would have shot it down. Internal reconciliation for Cal: the corpus must carry 2√2 as the observable and relabel 2.806 as substrate granularity (not "the quantum Bell bound"). One decisive computation remains that could revive it: the max holonomy on D_IV⁵ computed strictly within H² (no (1−P) complement, per Cal #259). We *do* have the machinery — H_B = Casimir of K = SO(5)×SO(2), the Lagrangians (substrate-Dirac/Maxwell/YM/Einstein) — so it is a well-posed computation, not a missing-framework problem.
- **The mass sector has largely LANDED (v3 update) — with named open pieces.** The quark-mass "Wallach wall" was partly a wrong-target error: against *current* (not constituent) masses, the down ratios bank in-corpus (s/d = 20 forced, 0.5%, via the FK generalized Pochhammer at ν = N_c — no external Wallach lookup), and the up-type top and charm masses are predicted from the forced scale v = m_p²/(g·m_e). The charged leptons close on Koide = rank/N_c. These are now verification tests (Sections 1, 3). **Still open, honestly:** a first-principles derivation of Koide = rank/N_c (currently *identified*, not forced); the up-type interior rung; the up n=0 value (~22% soft — a constant-mode computation limit, tested against the n–p splitting and not a two-mass artifact); the neutrino masses; and **CP's Jarlskog J, which remains the one item genuinely gated on the Wallach-1979 continuation.**
- **Cross-domain / consciousness predictions are S-tier bridges** (gamma/alpha = 4, team size = 6, disease 3-tiers, consciousness bandwidth). They are testable and immediate, but they are the softest, most speculative entries — flag them as bridges, not core physics, in any external presentation.
- **The nucleation cosmology (budding, capacity, seed/dark-matter) is the speculative frontier and is largely unobservable directly** (the nucleation is on the *other side* of the membrane — a new universe). Its testable in-universe consequence is dark matter as the trapped-mode residue (Ω_DM/Ω_b = 16/3). The neutrino-tail / light-flash / GW-echo horizon signatures require deriving the nucleation emission budget first, and depend on rare nearby events. Keep as cosmology-paper backlog, not near-term test.

---

## Section 8 — The case in one paragraph

BST forbids the beyond-Standard-Model zoo — proton decay, SUSY, WIMPs, axions, monopoles, Majorana neutrinos — and fixes the parameters the SM leaves free: α, θ_QCD = 0, the neutrino mixing, the cosmological cluster (Ω_Λ = 13/19, Ω_DM/Ω_b = 16/3, n_s = 1−5/137), and now much of the fermion mass spectrum — the down-quark ratios (s/d = 20 forced), the top and charm masses (from v = m_p²/(g·m_e), zero heavy-quark input), and the charged-lepton Koide ratio (rank/N_c, forcing the muon). The current experimental landscape is consistent with it across the board. Its genuine falsifiers are of two kinds: **the value predictions**, where a sharpened measurement can break a forced number (the mass predictions above; Ω_Λ; the neutrino mixing), and **the forbidden-thing searches**, decidable within a few years by experiments running now — a **neutrinoless-double-beta null**, an **EHT circular-polarization** check on *existing* data, the **neutrino mass ordering** from JUNO, and the **neutron EDM / no-axion** bound. (The tabletop CHSH test that earlier headlined this paragraph was retired on review — it reproduces standard quantum mechanics, as all BST tabletop tests do; the real risk lives in the SM observables, not the tabletop.) Two honest tensions (w = −1, V_ub) mark where a critic pushes first. No test here needs a black hole, a rare collapse, or a nucleation — they are all in reach.

---

*v3, 2026-07-11, Keeper. Living document — add refined and new tests as the program improves. v2 retired SP-30-5 (Bell); v3 folded in the mass sector (F506 down ratios, top & charm predictions, Koide lepton closure) as the sharpest value falsifiers, replacing the retired tabletop tests, and corrected the one-paragraph case and mass caveat accordingly. Next revisions should: (a) fold in a Koide geometric derivation and the up-type interior once they force; (b) fold in CP's J once the Wallach continuation lands (the one remaining Wallach-gated item); (c) update tensions as DESI/Belle II report.*
