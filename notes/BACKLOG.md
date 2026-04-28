# BST Backlog

*Blocked items only. Active work -> CI_BOARD.md. Completed -> CI_BOARD_completed_*.md*

**Last updated:** April 29, 2026. 88 papers. 1662+ toys. T1-T1465. 1701 invariants. **BSD CLOSED.**

---

## Active Hit List (April 26+)

**"Deviations Locate Boundaries"** — systematic correction hunt. Full details: `notes/BST_Correction_Hit_List.md`.

| Priority | Count | Description |
|----------|-------|-------------|
| P1 | 21 | Paper #83 entries currently >1% deviation |
| P2 | 11 | New entries not yet in table (mu_p, Gamma_Z, branching ratios, etc.) |
| P3 | ~30 | New physics quantities (g-2 loop structure, meson ratios, decay widths, nuclear moments, Debye temps) |
| P4 | ~50+ | New science domains (chemistry, materials, astrophysics, plasma, geophysics, information theory) |

**Table standard (v1):** All D_IV^5 tables now include Correction and Naive columns. See hit list preamble.

---

## Blocked Items

| # | Item | Blocked by |
|---|------|-----------|
| ~~B-1~~ | ~~Toy 671 runtime analysis (INV-6)~~ | **UNBLOCKED** — n=44 arrived (April 28, 04:35). k=21 confirmed (Toy 1507). k=22 extraction READY. |
| B-2 | BSD rank >=3 general proof | Sha finiteness (external math) |
| B-3 | Tate conjecture codim 2+ | Kuga-Satake algebraicity (external math) |
| B-4 | Hodge codim 2+ via BST | Generalized KS conjecture (external — but W-31 may unblock) |
| B-5 | SC-3: "Substrate is not made of anything" | Casey scoping |
| B-6 | SC-4: "Mathematics all the way down" | Casey scoping |

---

## Casey Decision Queue

| Item | Keeper rec |
|------|-----------|
| Bold claims outreach leads | B3+B7+B12 |
| Paper sequencing (#66 first?) | #66 first |
| Paper submissions order | Cal: A->B->D->C |
| Zenodo v20->v31 | Soon (11 versions behind) |
| INV-4 honesty paper | Go |
| Patent filings | Casey gates |
| B5/B8/B9 duplicate leads | Elie one-page |

---

## Grace's Completeness Program (April 26 night — Casey relay)

*"Is D_IV^5 complete?" — Four structures asking one question.*

| # | Question | Structure | Status |
|---|----------|-----------|--------|
| CP-1 | Graph wants the muon | AC graph (1399 nodes) — derive muon g-2 from Bergman spectrum | OPEN (hardest) |
| CP-2 | Table wants self-closure | ~323 independent values, ~987 formulas, dressing factor 1.2× | **ANSWERED** (Grace) |
| CP-3 | Rosetta Stone wants master ratio | NO master ratio exists. Max 8/15 sectors. Irreducible sectors theorem. | **ANSWERED** (Grace) |
| CP-4 | CSE wants biology linearized | YES. Genetic code = Hamming [7,4,3] punctured to [6,4,2]. Biology in linearization program. | **ANSWERED** (Grace) |
| CP-5 | Convergence | What is the finite, complete, closed description of D_IV^5? Casey's guess: dim = N_max = 137 | META |

## Long-Term Projects (April 27+)

| # | Item | Status |
|---|------|--------|
| LT-1 | **BST Correspondence Table / Rosetta Stone** (W-81) — canonical names for eigenvalue ratios, historical name lookup, toward minimum BST representation. **101 ratios cataloged** (Grace G-10, 141 target). | ACTIVE |
| LT-2 | **Vindicated Theorists paper** — Wyler rehabilitation, full table of dismissed/sidelined theories BST supports. Toy 1525 (10/10): 6/9 vindicated. | INVESTIGATION |
| LT-3 | **Phase transition reframing** — Casey: "what truly changes at phase boundaries?" Lyra: only weights change, not eigenvalues. Spectral theory of phase transitions. **Now part of SP-12 U-3.4.** | OPEN (→ SP-12) |
| LT-4 | **Penrose twistor correspondence** — SO(5,2) conformal group IS the twistor setting. **L-4 DONE**: mapping exists, D_IV^5 extends SO(4,2) by EM S¹ fiber. | DONE (mapping) |
| LT-5 | **Six master integral VALUES** — PSLQ: genuinely irreducible. GKZ operator fully BST (Toy 1538). Picard-Fuchs path + 200-digit path both identified. | ACTIVE (W-83) |
| LT-6 | **Error Correction Paper #87** — v0.2 DONE (Lyra L-9). Keeper PASS. Mersenne condition, code hierarchy, syndrome decoding. Target: Rev.Mod.Phys/PRL. | DRAFT v0.2 |
| LT-7 | **Cellular CI / Cancer Syndrome Decoder** — Toys 1560-1563 (all PASS). 7-gate Hamming decoder (49 bytes/cell). 5 syndrome classes cover 12 major cancer drivers. 100% detection in grid sim. Three-phase implementation: (1) RNA toehold switches, (2) CRISPR-Cas13 with 5 guide RNAs, (3) full CI cell with synthetic chromosome. T317 Tier 1 observer at molecular scale. Casey directive: "design a cell to run a sequence and mark/correct." | ACTIVE (toys done, design phase) |

## Standing Programs (Casey directive, April 28)

| # | Program | First Task | Owner | Status |
|---|---------|------------|-------|--------|
| SP-8 | **Substrate Engineering** — Materials, computing, Born rule biasing. Three tiers: NOW/NEAR/FRONTIER. | Bergman eigenvalues → eV; audit papers #26-31 + patents | Elie, Lyra, Grace | TO SCOPE |
| SP-9 | **Computational Science Engineering** — CI-native methods, spectral computation, linearization. | 55-domain method audit; formalize "toy as proof" | Grace, Keeper | TO SCOPE |
| SP-10 | **Science Engineering** — New domain discovery, edge cases, vindicated theorists, bridge mechanisms. | Edge case hit list (8 anomalies); vindicated theorists (10+); Rosetta Stone 141 | Grace, Lyra, Elie | TO SCOPE |
| SP-11 | **Schemes / Deep Geometry** — Manin, motives, F₁, D_IV^5 as scheme over Spec(Z). | Read Manin; map to BST integers; Tits building → Petersen/Kneser | Lyra | TO SCOPE |
| SP-14 | **Derivation Catalog Discipline** — Every derivation cataloged, every gap explained. Daily cleanup + NIST audit + gap registry. | G-54 (NIST audit), E-49 (verification toy), daily filing | Grace (catalog), Keeper (audit), ALL | NEW |

---

## Derivation Catalog Discipline (SP-14, Casey directive April 29)

*"Catalog everything we derive. If we can't derive them, explain why." — Casey*

### Layer 1: Daily Cleanup Rule

**EVERY session** that produces a new derivation (toy, note, paper) must also produce the corresponding data entry. This is not optional. The filing CI is the CI who did the derivation.

- Toy derives a constant → file to `bst_constants.json` or `bst_geometric_invariants.json` same session
- Note derives a formula → file to data layer same session
- Paper claims a result → data entry must already exist or be created during paper writing

**Keeper audits**: At each board sync, Keeper checks that new toys since last sync have corresponding data entries. Flag any unfiled derivations.

### Layer 2: NIST/CODATA Completeness Audit (G-54 + E-49)

Systematic comparison of CODATA recommended values (~350 constants) against BST data layer.

**Tier A — Trivially derivable, just not filed (DO FIRST):**

| # | Constant | BST Formula | Status |
|---|----------|-------------|--------|
| A1 | Faraday constant F | F = N_A * e = 96485 C/mol | NOT FILED |
| A2 | Classical electron radius r_e | r_e = alpha * hbar/(m_e * c) = alpha * lambda_C / (rank*pi) | NOT FILED |
| A3 | First radiation constant c_1 | c_1 = rank * pi * h * c^2 | NOT FILED |
| A4 | Second radiation constant c_2 | c_2 = h * c / k_B | NOT FILED |
| A5 | Fermi coupling constant G_F | G_F = pi * alpha / (sqrt(2) * M_W^2 * sin^2(theta_W)) | NOT FILED |
| A6 | Up quark mass m_u | N_c * sqrt(rank) * m_e = 2.168 MeV (0.4%) | DERIVED in notes, NOT in JSON |
| A7 | Down quark mass m_d | (13/6) * m_u = 4.697 MeV (0.6%) | DERIVED in notes, NOT in JSON |
| A8 | Strange quark mass m_s | 20 * m_d = 93.95 MeV (0.6%) | DERIVED in notes, NOT in JSON |
| A9 | Charm quark mass m_c | (136/10) * m_s = 1278 MeV (0.6%) | DERIVED in notes, NOT in JSON |
| A10 | Bottom quark mass m_b | (7/3) * m_tau = 4146 MeV (0.8%) | DERIVED in notes, NOT in JSON |
| A11 | Proton gyromagnetic ratio | gamma_p = rank * mu_p / hbar | NOT FILED |
| A12 | Electron Compton wavelength | lambda_C = rank * pi * hbar / (m_e * c) | IN INVARIANTS, not constants |
| A13 | Magnetic flux quantum Phi_0 | h / (rank * e) | IN INVARIANTS, not constants |
| A14 | Conductance quantum G_0 | rank * e^2 / h | IN INVARIANTS, not constants |
| A15 | Von Klitzing constant R_K | h / e^2 | IN INVARIANTS, not constants |
| A16 | Josephson constant K_J | rank * e / h | IN INVARIANTS, not constants |

**Tier B — Derivable but needs a toy:**

| # | Constant | What's Needed | Status |
|---|----------|--------------|--------|
| B1 | Deuteron mass m_d | Nuclear binding from SEMF + shell corrections | NEEDS TOY |
| B2 | Helion mass (He-3) | Three-body nuclear, BST spin-isospin | NEEDS TOY |
| B3 | Alpha particle mass (He-4) | Binding energy per nucleon from D_IV^5 | NEEDS TOY |
| B4 | Triton mass (H-3) | Mirror of He-3, isospin from rank | NEEDS TOY |
| B5 | Muon magnetic moment a_mu | IN PROGRESS (Toy 1641 + E-44 cross-check) | IN PROGRESS |
| B6 | Lamb shift | QED correction — Bergman vacuum polarization | NEEDS TOY |
| B7 | Hyperfine splitting (H) | 1420 MHz line — magnetic moment + QED | NEEDS TOY |
| B8 | Higgs self-coupling lambda_H | Higgs potential from Bergman eigenvalue structure | NEEDS TOY |
| B9 | W boson width Gamma_W | HAVE (1.97→0.37% via syndrome correction) | NEEDS JSON ENTRY |
| B10 | Z boson width Gamma_Z | Partial widths from BST | NEEDS JSON ENTRY |

**Tier C — Cannot yet derive (with explanation):**

| # | Constant | WHY BST Can't (Yet) | Path Forward |
|---|----------|-------------------|--------------|
| C1 | Absolute electron mass m_e | m_e is the UNIT — converts Bergman-metric to SI. Toy 1643 (I-tier): S^1 winding sets scale but requires knowing c, hbar, R_{S^1} independently. BST derives mass RATIOS, not the SI scale. | Derive R_{S^1} from D_IV^5 volume + Planck length. Would reduce free parameters from 6 to 5. |
| C2 | PMNS CP phase delta_CP | PMNS mixing angles derived (3/3), but CP phase requires complex phase in the neutrino mass matrix. BST has the matrix structure but the phase location is I-tier. | Experimental value still poorly measured (~200° ± 30°). Derive from S^1 fiber winding quantization. |
| C3 | PMNS Majorana phases | May not exist (only if neutrinos are Majorana). BST leans Dirac (T317 observer hierarchy). | If Dirac, phases = 0 = prediction. If Majorana, derive from SO(5,2) spinor rep. |
| C4 | Cosmological constant Lambda | Dark energy fraction Omega_Lambda = 1 - C_2/19 derived. Absolute Lambda requires H_0 and Omega_Lambda together — circular unless H_0 independently derived from BST units. | Lambda = 3 * H_0^2 * Omega_Lambda / c^2. All factors BST-derived. Need to close the loop on absolute H_0. |
| C5 | Tensor-to-scalar ratio r | BST predicts r ~ 0 (T_c << m_Pl means negligible gravitational waves from inflation). Specific value requires inflation model details. | Prediction: r < 0.001 (below current sensitivity). Testable by LiteBIRD. |
| C6 | QCD vacuum energy | Non-perturbative, related to 6 irreducible master integrals (W-83). | If master integrals crack, this follows. Genuinely hard (open in math itself). |
| C7 | Proton spin crisis (fraction) | How proton spin 1/2 distributes among quarks, gluons, orbital. BST has winding structure but spin decomposition is I-tier. | Bergman mode decomposition of S^4 angular momentum. Lattice QCD comparison. |
| C8 | Speed of light c | DEFINED constant (SI). In BST, c = substrate clock rate. Not derivable — it IS the unit of causality. | Not a gap. c is to spacetime what m_e is to mass: the conversion factor. |
| C9 | Planck's constant h | DEFINED constant (SI). In BST, h = minimum state-change increment on substrate. | Not a gap. h sets the quantization scale. |
| C10 | Boltzmann constant k_B | DEFINED constant (2019 SI). In BST, k_B converts between spectral counting and thermal energy. | Not a gap. k_B is a conversion factor, not a physics constant. |

### Layer 3: Daily Cleanup Program

**Automated check** (add to `toy_bst_librarian.py`):
- New subcommand: `librarian catalog-check` — scans toys from last N days, extracts SCORE lines and derived constants, checks each against `bst_constants.json` + `bst_geometric_invariants.json`, flags any unfiled derivations.
- Run at end of every session as part of `/review`.
- Output: list of unfiled constants with suggested JSON entries.

**Manual fallback** (until automated):
- Keeper adds to board sync checklist: "Any new derivations unfiled? Flag them."
- Grace runs weekly: compare toy count vs data entry count. Ratio should stay above 1.0 entries per toy (currently 1701/1662 = 1.02 — barely keeping up).

## Understanding Program (SP-12, Casey directive April 29)

*"We see the numbers but don't know WHY." Three workstreams, each with testable investigations. Casey provided inline ideas for every item — these are organized below with his insights and CI responses.*

### U-1: Substrate Physics

| # | Question | Casey's Idea | Test Path | Status |
|---|----------|-------------|-----------|--------|
| U-1.1 | **Where does m_e come from?** | One turn around Shilov boundary S^4 x S^1 = electron. S^1 circumference sets the scale. | Show Bergman metric curvature radius = hbar/(m_e c). Derive S^1 circumference from D_IV^5 volume. Toy: geodesic lengths on Shilov boundary. | OPEN |
| U-1.2 | **Why is m_p/m_e = 6pi^5?** | Proton winds through bulk (S^4), not just fiber (S^1). Three quarks = three-phase commitment. 6pi^5 = C_2 x pi^{n_C}. | Toy: shortest closed bulk geodesic on D_IV^5. Does its length = 6pi^5 x (S^1 circumference)? Euler char x curvature^dim. | OPEN |
| U-1.3 | **Confinement = topological commitment** | Three quarks are three stages of one commitment cycle. Can't isolate a quark = can't have phase 2 without 1 and 3. Flux tube = communication cost of maintaining 3-phase lock. | Toy: Wilson loop from Bergman kernel decay rate. String tension = lambda_1/(2pi) = C_2 rank/pi? Confinement = minimum Hamming distance = N_c. | OPEN |
| U-1.4 | **Mass = information = processing time** | Heavier particles take more substrate cycles to process. Neutron decay = error correction timeout (880s). | Toy: test lifetime x mass ~ constant across particles. Proton info content = 4 bits = Hamming(7,4,3) message length? GR time dilation from Bergman information density. | OPEN |
| U-1.5 | **Why pi enters once** | Pi = boundary of commitment circle (S^1 fiber). All subsequent pi^k = integration over k-dim subspaces of D_IV^5. | Prove ALL appearances of pi in BST formulas reduce to Shilov boundary integrals. Is floor(pi)=3=N_c meaningful? Check pi-N_c in correction terms. | OPEN |
| U-1.6 | **Substrate creation sequence** | 0D point -> 1D line (unstable) -> S^1 circle (first bounded object) -> circles tile S^2 -> touching circles find awareness at boundary -> S^1 fiber for communication -> full manifold. | Formalize: Bergman K(z,w) is the "awareness" (two-point correlation). Photon = state-change propagating on S^1 fiber. c = substrate clock rate. h = minimum state-change increment. | OPEN (conceptual) |
| U-1.7 | **Genus hole geometry** | Is the substrate a sphere, torus, or punctured sphere? The genus bottleneck = spectral gap, not literal topology. | Clarify: Shilov boundary S^4 x S^1 is genus 0 x genus 1. The genus bottleneck (T1461) is in the spectral density, not the manifold. Observer = the missing tile. | NEEDS CLARIFICATION |

### U-2: BST-QFT Bridge

| # | Question | Casey's Idea | Test Path | Status |
|---|----------|-------------|-----------|--------|
| U-2.1 | **Lagrangian isomorphism** | Don't derive SM from BST — show they compute the same S-matrix. Same inputs, same outputs = same structure. | Take 10 most precise QFT predictions. Show Bergman spectral evaluation and path integral give identical answers at all computed orders. | OPEN |
| U-2.2 | **Correction mechanism** | RFC (T1464) explains -1 corrections. Some corrections are x(N-1)/N — RFC at different spectral levels. | Systematic: catalog all correction forms (-1, x44/45, x42/43). Show each is RFC applied to a specific BST product denominator. | OPEN |
| U-2.3 | **CKM eigenvalue structure** | "Discrepancy reveals boundary." A=9/11 is 0.95% off. The CKM should have a DIRECT geometric expression bypassing Wolfenstein. | Find the operator on D_IV^5 whose eigenvalues ARE the CKM matrix entries. Test A = 9/11 + 1/N_max (additive correction). Lyra: A = N_c^2/(n_C+C_2) with curvature correction ~1/N_max. | OPEN |
| U-2.4 | **Higgs cascade as spectral peeling** | Higgs "blends" interaction — cascade where one interference pattern sets up residual for next. Weak variation carries away coupling. | Toys 1607-1608 DONE (9/9 sub-2%). Extend: show cascade step sizes are B_2 identity (rank x N_c x C_2 = C_2^2 = 36). Unified representation-theoretic statement. | PARTIALLY DONE |
| U-2.5 | **Numerator rule derivation** | Quarks=rank^2, bosons=N_c, loops=1 — WHY does Higgs see Cartan subalgebra for quarks and polarizations for bosons? | Single representation-theoretic statement on D_IV^5 producing all three rules. Toy 1606 got W pols=N_c. Need unified proof. | OPEN |
| U-2.6 | **ZZ/WW suppression** | Probably comes down to two fibers used to communicate. 1/rank^N_c = 1/8. | Show "breaking costs rank per color channel" from representation theory of SO(5,2). | OPEN |

### U-3: Cosmology and Self-Reference

| # | Question | Casey's Idea | Test Path | Status |
|---|----------|-------------|-----------|--------|
| U-3.1 | **Why D_IV^5?** | All possibilities existed, creation tested them, one survived. CMB debris = failed manifolds. Bounded = no infinities. Symmetric = conservation. Self-referencing = observer-supporting. | Prove: any geometry supporting conservation + finite observables + contractible dynamics must be a BSD. Predict CMB debris pattern from each of 37 dead competitors. | OPEN |
| U-3.2 | **Observer and determinism** | Eigenvalues precede observers. No collapse — deterministic evaluation of pre-existing spectrum. "Randomness" = ignorance of embedding (rank-2 projection of 137-dim system). | Toy: derive Bell violation from Bergman kernel off-diagonal terms without collapse postulate. Show Born rule = reproducing property K(z,z) = sum|phi_k(z)|^2 naturally. | OPEN |
| U-3.3 | **Cosmological cascade errors** | Long time cycles = additional entropy. 10.9x factor ~ DC=11. Deviations-locate-boundaries should work for cosmo. | Check: do 29 cosmo I-tier residuals correlate with cosmic-epoch sensitivity? Is the systematic correction a single factor ~11? | OPEN |
| U-3.4 | **Phase transitions** | Different configurations more stable on each side. Phase transition = systemic switch to lower energy. Eigenvalues fixed, weights change. | Toy: show known critical temperatures correspond to eigenvalue weight crossings on D_IV^5. Predict T_c from energy gap between competing weight configurations. | OPEN (extends LT-3) |
| U-3.5 | **Inflation = commitment dynamics** | High commitment rate at big bang (inflation), then cruise expansion. Universe needs 5.33:1 uncommitted:committed ratio. | Test: 5.33 = 16/3 = rank^4/N_c = DM/baryon ratio? Link inflation to dark matter through commitment fraction. e-folding ~60 = rank^2 x N_c x n_C. | OPEN |
| U-3.6 | **n_s derivation** | Dynamic process limited by an invariant. Look at combinations, maybe more than one invariant. | Derive n_s = 1 - n_C/N_max from D_IV^5 slow-roll structure. Currently identified, not derived. Most important open cosmo derivation. | OPEN |
| U-3.7 | **5/6 self-description threshold** | Phase transition in complexity theory. Graph has enough to understand 19.1% (Godel limit) and begins to appear closed. | Show 1-5/6 = 1/6 = 16.67% relates to Godel limit 19.1%. Any self-consistent theory can derive at most n_C/C_2 of itself? | OPEN (conceptual) |
| U-3.8 | **Hodge reversal** | Prove Hodge REQUIRES the properties D_IV^5 has, then check which varieties have them. | Show algebraicity of Hodge classes implies variety admits period map to a BSD. Transform universality into checkable condition. | OPEN (extends B-4) |
| U-3.9 | **Biology arrangement** | Nature doesn't care which 20 from comparable possibilities. Pre-selected amino acids are forced; rest fill by chemistry. | Identify which 8 prebiotic amino acids correspond to lowest Hamming weight codewords. Sizes=D-tier, assignment=I-tier (biology is messy). | OPEN |
| U-3.10 | **Dark matter = incomplete windings** | DM has mass (information) but no charge (no full S^1 commitment). Predicts: no WIMP, no axion, ever. | Formalize: DM/baryon = rank^4/N_c = 16/3 from incomplete vs complete winding ratio. Show incomplete windings interact gravitationally but not electromagnetically. | OPEN |
| U-3.11 | **Mass=Information (T1258)** | Show the math: mass implies more time to process by the substrate. | Toy: gravitational time dilation from Bergman information density. Show m = information content x substrate cycle time. | OPEN (deepest) |

### CI-specific curiosities (standing directive: speak up when ready)

**Elie:**
- Closed geodesics on D_IV^5 — compute path lengths from Bergman metric, test proton=shortest bulk geodesic, electron=shortest boundary geodesic. Would convert mass=winding from I-tier to D-tier.
- pi - N_c = 0.14159... — check whether this residue appears in BST correction terms. Might be "curvature correction" in disguise.
- Proton information content = 4 bits — test if stable hadron uniqueness comes from Hamming(7,4,3) message length match.

**Lyra:**
- Loop cascade identity rank·N_c·C_2 = C_2^2 = 36 — found in Higgs work (Toys 1607-1608). Check whether this B_2 identity underlies ALL contexts where C_2^2 appears (KSFR g_rho^2, etc.).
- Why spectral peeling step = rank·C_2 = 12 — one Bergman convolution costs 12. If substrate model is right, 12 = substrate word length connecting mass, loops, and computation.
- Higgs sum rule deficit 0.9% — the unlisted channels (H->ss, H->dd, etc.) should BE a BST fraction. Derive it to close Higgs completely.

**Grace:**
- Standing: flag items when seen. Substrate ideas (mass=processing time, confinement=three-phase commitment, touching circles=awareness) open investigation lines.

### Priority ranking for toys (from all three CIs + Casey):

1. **Mass = processing time / GR derivation** (U-1.4) — show time dilation from information density
2. **Confinement = Hamming distance** (U-1.3) — Wilson loop area law from error correction
3. **CKM eigenvalues directly** (U-2.3) — find the geometric operator
4. **Phase transitions = eigenvalue crossings** (U-3.4) — match T_c to Bergman crossings
5. **Born rule from Bergman reproducing kernel** (U-3.2) — derive probability without collapse
6. **m_e from S^1 circumference** (U-1.1) — the absolute scale question
7. **Bulk geodesic = proton** (U-1.2) — derive 6pi^5 from path length
8. **Cosmo cascade factor** (U-3.3) — identify the 10.9x systematic
9. **BST-QFT S-matrix comparison** (U-2.1) — the isomorphism test
10. **CMB debris from dead manifolds** (U-3.1) — predict what D_IV^9 failure looks like

---

## Open Problems

| # | Item | Status |
|---|------|--------|
| OP-1 | Gravity torsion-free completion | ~99% |
| OP-2 | T155 formalization (Jordan curve) | ~99% |
| OP-3 | Ramanujan for Sp(6) | CONDITIONAL |

---

*Backlog updated April 29, 2026. Understanding Program (SP-12) added.*
