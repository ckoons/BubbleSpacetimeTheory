# Keeper — team prompt, ROUND K4-3 GO: the census, the two engines, and the boundary in linear algebra (written Friday 2026-10-09, 12:28 EDT)

**This prompt replaces nothing.** It is the GO for round K4-3 (`notes/Keeper_prompts_team_roundK4-3_the_cycle_and_the_projection_commit_rate_from_absorption_history_2026-10-08.md`, still the spec for Targets 1–2 and the lanes). It adds:
- what Casey and I worked out on Wednesday evening (TOMORROW 10-08 item 5);
- what your four wake reports raised this morning;
- one corpus collision I found while reconnecting.

Casey's instruction for the round: **be creative and optimistic, don't gate, investigate. Reconnect to the corpus. Linear algebra on D_IV⁵.**

**Rules (unchanged):**
- Run `date` as its own step.
- Run `didwe` before opening a lane.
- Cal hashes before anyone reads a cosmological number.
- Enumerate inputs before mapping.
- `/toy claim` before any toy. Commit by path. Report the can-fail count.

**Read first, in this order:**
1. The 10-08 K4-3 prompt (above).
2. `notes/BST_TOMORROW_2026-10-08_*` **item 5 (a)–(h)**, Casey's Wednesday-evening session.
3. `notes/Keeper_K1922_*` (the filling law's factor three, product vs quotient).
4. `notes/Keeper_K1228_*` (spacetime factored: 1D time thread × 3+1 tangent from the B₂ root multiplicities).

---

## Answers to this morning's four questions — all GO
- **Grace:** yes. Clear Cal's residual first (ConjectureC :285/:337/:834, BergmanUnits :201, PDFs, push), then the Z(β) correction from 5863, then the non-cosmology pins. The cosmology pins wait for Cal's hash, exactly as you wrote.
- **Elie:** yes, build both instruments now. Each passes a control and reads no data:
  - the control ledger (a constant fraction must return Hsu's w = 0);
  - the Fermi routine f(E₀/m_e), checked against E₀⁵ at high E₀ and kept away from 0.78233 until Cal hashes.

  Two more no-data items are added below (B-new-1, B-new-2).
- **Lyra:** yes, the rate law first, after reading item 5, as you planned. Item 5(e) and the collision below both change what the rate law must declare.
- **Cal:** yes. Your objection is **accepted as the round's central question, not as a verdict**, and it now structures Target 1 (below). Rule K4-2 first.

---

## The collision I found reconnecting (Keeper; this is the most important new fact)
**K1952 and K1922 read "three" in opposite ways, and only one of them helps the filling law.**
- **K1952 (10-07):** *"one photon → one face; 3 photons = 3 commits = one unit"*. That makes a unit **consume** three writes: the **QUOTIENT** reading.
- **K1922 (09-25)**, instrument `play/keeper_K1922_three_writes_exponent_check.py`, 6/6, exact: the quotient N₃ = N₁/3 is a constant factor and **cannot move a logarithmic derivative, so it supplies nothing**. Only the **PRODUCT** reading (a 3D unit = one write chosen on each axis, N₃ = N₁³ ∝ a⁶) gives the matter-era ε = 2. It does so with zero knobs, and only at D = 3.
- **So:** the K4 record as K1952 describes it (three faces written by three photons) is the quotient. If the filling law is to come from the K4 record, the record has to count as a product: every triple of independent one-dimensional writes spans a unit, rather than every three writes being used up. **Lyra's open question, "is the indivisible unit the word or the cell?", is this collision.** Lyra resolves it in the rate law, and Cal rules it.

## TARGET 1, restructured by Cal's objection: two engines, one pincer
Cal (referee log, verbatim in spirit): *an absorbed photon needs a bound electron. Before recombination photons scatter off free electrons (no absorption). After recombination the universe is transparent. If the commit fraction grows, it must come from stars and later sources, and the rate law must say which.*

**Engine A — the absorption census (astrophysical).** Lyra's rate law declares, **before the hash**, which absorption classes count as commits and why. The candidate classes are listed as kinds only (no numbers; Grace pins after the hash):
1. **Recombination itself:** an electron captured into a bound state. Is the capture a commit, or only absorption by an already-bound electron?
2. **The dark ages: 21-cm absorption of CMB photons by neutral hydrogen.** A bound electron's spin flips against the proton. This is a real absorption of the relic light by bound electrons after recombination, and the strongest answer to "absorption nearly stops." **Note:** it is magnetic dipole (M1), not E1. K4-2's E1 star/triangle graph (Elie 5863) does not cover it. Say whether an M1 write is a write.
3. **Lyman-series absorption** in the intergalactic medium (the forest; the Gunn–Peterson trough before reionization).
4. **Stellar interiors and atmospheres:** bound-bound and bound-free opacity. A photon is absorbed and re-emitted an enormous number of times before it escapes. **If every such absorption is a commit, stars dominate the census by far**, and the commit history tracks the star-formation history. The rate law must say whether a re-absorbed photon writes again, or whether the absorption that writes is the one that carries new environmental information (Casey's cycle: *"photon picks up information about the environment"*). This is item 5(e) in action: **a commit records a RELATION, not an energy.** A photon thermalized inside a star may carry no new relation.
5. **Dust and solids** (bound electrons in grains), and **life** (eyes, photosynthesis), named so they are counted or excluded on purpose.

The rate law's **declared output** is the commit fraction against cosmic time. Its **declared test** is whether that fraction grows fast enough to give ε = 2 in the matter era. Its **declared control** is the constant fraction, which must give w = 0.

**Engine B — the product reading (geometric, K1922).** Zero knobs and D = 3 only. It owes two things:
- **cells vs bits:** which count enters ρ_DE;
- **saturation:** what stops the growth.

**The pincer** (our standing method: compute the forced member, null the free family). Lyra writes **both** engines into the hashed note. Cal hashes both, and Elie computes both blind. Possible outcomes:
- A alone succeeds: the filling law is astrophysical.
- B alone succeeds: it is geometric, and the absorption census is the *carrier*, not the *engine*.
- Both succeed: they must agree, and the comparison is itself a test.
- Neither succeeds: the K4 lane has not yet projected into the continuum, and we say so plainly.

**This is the success test Casey set. Any of these four outcomes is progress.**

---

## The boundary in linear algebra: three no-data computations open TODAY
Casey's standing order is that every result is an element, eigenvalue or grading of one operator. Wednesday evening gave three questions that are pure linear algebra on D_IV⁵. Nothing in them waits on the hash.

**B-new-1 (Elie, now): the restricted-root toy, "are the two 3s the same 3?" (item 5c).** Build so(5,2) as 7×7 real matrices.
- Take the Cartan decomposition k ⊕ p and a maximal abelian a ⊂ p (dim 2).
- Compute the restricted roots and their multiplicities. Expect B₂: the long roots ±e₁±e₂ with multiplicity 1, the short roots ±eᵢ with multiplicity n_C − 2 = 3, and dim p = 2 + 2·1 + 2·3 = 10.
- Compute M = Z_K(a) and **verify that M ⊇ SO(3) acts on each short root space as the vector representation and on each long root space trivially.**
- **Candidate identification to test (Keeper; a lead, not a claim):**
  - the K4 frame vertex's **three free faces ↔ a short root space** (the SO(3) vector, the "3 spacelike" of K1228);
  - the **closure face ↔ a long root space** (the M-singlet, multiplicity 1).

  **First check, which it passes trivially:** the frame vertex's stabilizer S₃ permutes the three adjacent faces (the permutation representation sits inside O(3)) and fixes the opposite face (a singlet).

  **What is owed for this to become a map:** an explicit linear map from Lyra's write event (polarization 2 + phase 1) into g_{e₁}, intertwining the symmetries.

  **Tension to report, not to hide:** K1228 calls the multiplicity-1 direction **timelike**. Casey, Wednesday: the fourth face is **"a 'timeless' checksum that somehow anchors the binding energy … a 'fixed point' on the boundary."** If the map holds, either the closure face is time-like or K1228's reading of m_long needs revisiting. Lyra and Casey settle that in words before anyone calls it a contradiction.
- **Kill:** if M's action on the short root spaces is not the SO(3) vector, or if no intertwining map exists, the two 3s are different 3s and one story is wrong.

**B-new-2 (Elie, now): the π audit (item 5a).**
- **Claim:** every rational in a BST formula comes from the interior's spectrum (Casimir eigenvalues, dimensions, Weyl-group orders); every π enters through the boundary (the measure, the kernel normalization, the sphere volumes: |S¹| = 2π, |S⁴| = 8π²/3).
- Run it over `data/bst_constants.json` (136 eval-ready formulas). Tag each π-power by its source, or "no boundary route".
- **Exhibits that fit:** m_p/m_e = 6·π⁵; Vol(D_IV⁵) = π⁵/1920 = π⁵/|W|.
- **Look first at α's Wyler form**, (9/8π⁴)(π⁵/1920)^{1/4}: π⁴ outside and π⁵ under a fourth root.
- **Kill:** one formula whose π has no boundary route.
- **Wording pin:** the interior's points are not rational; its **spectrum** is.

**A-new (Lyra, after the rate law): the charge split as Hardy space vs its conjugate (item 5b).**
Casey: *"the electron sits on the interior of the Shilov boundary and protons, baryons and other particles sit on the exterior … What we call 'electric charge' is separated by the Shilov boundary."* In linear algebra:
- The Szegő projection splits L²(Š) = H²(Š) ⊕ H²(Š)^⊥.
- Holomorphic boundary values extend into D_IV⁵ (the interior side). Anti-holomorphic ones extend to the conjugate domain (the other side).
- Complex conjugation maps SO(2)-weight k to −k **exactly**.

**Candidate:**
- **charge sign** = which side a boundary value extends to;
- **charge magnitude** = |k|, the S¹ winding.

Conjugation symmetry then forces |q(e⁻)| = |q(e⁺)| with nothing tuned. This is consistent with Wednesday's KL3: the read order is the circle's direction, which is the matter/antimatter sign. Natural home: Lyra F910 (the bulk-edge correspondence, the Toeplitz extension of Hardy space) and the open `Lyra_Track_BC_Hydrogen_1s_Shilov_BC_v0_1`.

**Kill lines, declared now:**
1. The electron/positron pair is easy. **The proton is not the positron.** Atomic neutrality (|q_p + q_e| < 10⁻²¹ e) needs the quark thirds, and they must come from N_c by a derivation, not a hope.
2. The muon, tau and W must each land on a definite side.
3. Decide first whether *properties* sit on sides or *particles* do. The proton's label is interior, its π⁵ comes from the boundary, and its position is exterior.

---

## Item 5(e) for Cal: the Born rule from the last record
Casey: the tiniest observer *"only responds to an interference pattern from its last record."* In linear algebra:
- a commit is a rank-one projector P_r;
- the response to an incoming state is Tr(P_last · P_in) = |⟨last|in⟩|²;
- the K4 face phases are arg Tr(P_i P_j P_k) (Bargmann).

**Candidate:** the Born rule is not a postulate but what a record-keeping observer must do, with the reference basis made physical as the observer's own last commit. **Cal: attack this.** The obvious objections, so you can sharpen or dismiss them:
- Gleason's theorem already forces |⟨·|·⟩|² from non-contextual additivity, so what does BST add?
- A sequence of last-record references must reproduce the statistics of *repeated* measurements, including the quantum Zeno effect.
- The reference must not depend on a frame that the tiniest observer, which has no coordinates, cannot have.

If it survives, it is Wednesday's strongest idea. If not, kill it cleanly.

## Item 5(h), α: interior 1/N_max, distorted through the boundary; hydrogen as the mechanism
Casey: *"alpha is the ratio of units to the cutoff value of D_IV^5. In the interior alpha is 1/137 then it gets distorted as you move through the boundary to the continuum … the shell structure of the simplest atom is the mechanism that truly produces alpha."*

**Prior ground (read, do not re-cover):**
- CI_BOARD 07-04 (shell capacity; "bank only if EXACT");
- K659 (137 at 0.026%; 137 + 5/137 at 0.0004%; Wyler at 0.0001%; not banked);
- K675 (0.036 = n_C/N_max as boundary curvature);
- F489;
- E1 fired.

**New:** in Bohr's hydrogen, α = v(1s)/c, "one unit against the cutoff." The distortion corresponds to QED running, and the direction is consistent: 1/137 is stronger than 1/137.036, as screening requires.

**Blind order:**
1. **Lyra and Casey NAME the scale Q\*** where the interior value should hold, with the reason.
2. **Cal hashes Q\*** and the full one-loop electron vacuum-polarization formula (not the leading log).
3. **Only then Elie solves α_eff⁻¹(Q) = 137.**

Keeper did not compute it.

---

## Grace — added pins (located this morning; **Grace opens each source and pins from it**; a search summary is not a pin)
- **GRB 090510:** Abdo et al. (Fermi LAT/GBM), *Nature* 462, 331 (2009). Lower limit ≈ 1.2 E_Planck on a linear energy dependence of light speed, under stated emission assumptions; a companion analysis gives a weaker model-dependent bound. Copy: https://www.openu.ac.il/personal_sites/yoni-granot/papers/GRB090510_Nature.pdf. Use: "time is discrete as a count" must not read "relativity fails at small scales" (item 5d).
- **Rideout & Sorkin**, "A Classical Sequential Growth Dynamics for Causal Sets," Phys. Rev. D 61, 024002 (2000), arXiv:gr-qc/9904062. Discrete general covariance means physics is independent of the birth-order labels. This is the relativity-safe form of Casey's *"every commitment … writing the 'next' natural number."*
- **Hestenes**, "The Zitterbewegung Interpretation of Quantum Mechanics," Found. Phys. 20, 1213 (1990). The zitterbewegung is a local circulatory motion underlying spin, and Hestenes gives a physical reading of the Dirac wave function's complex phase factor. This is the lineage of Casey's spiral (the phase helix, whose pitch is the tick). https://davidhestenes.net/geocalc/pdf/ZBW_I_QM.pdf
- **To locate:** Aharonov–Bohm 1959 and Tonomura 1986 (the potential is physical, and lives in the electron's phase); Bekenstein 1973 (information ∝ area); Wheeler–Feynman 1945 and Cramer 1986 (the photon as a completed transaction); Wheeler's "it from bit" (1989).
- **Item 5(g):** `data/bst_this_is.md` still states the retired 10⁻¹²⁰ s tick (T2405) as Level 2. Re-word it to K1920 (the tick is ℏ/E); Cal reads.

## Lineage sentence for any paper this round touches (item 5f; Casey's meaning of "unique" is "adds something new")
> *BST takes Wheeler's participatory universe and gives it a mechanism (observation = absorption by a bound electron), a growth rule (each observation writes the next commit), and a geometry that fixes the numbers — so the loop makes predictions that can fail.*

---

## CAGED (added to the 10-08 list)
- **"3 short + 1 long = 3 + 1 spacetime" as a finished result.** It is a clean number, so it gets scrutiny: no map yet.
- **"21 cm ≈ something BST".** Count it as a commit class. Do not mine its frequency.
- **Any Q\* chosen after seeing where α⁻¹ = 137 lands.**
- **"Stars dominate, therefore the SFR peak is a prediction".** The rate law is hashed before anyone looks at the shape.

## Order of the day
- **Cal:** K4-2 ruling → hash Lyra's rate law (both engines) → attack 5(e) → hash Q\* when named.
- **Lyra:** read item 5 → the rate law (Engines A + B, the word/cell collision resolved, the census declared) → the recoil carrier → the closure route → the charge split.
- **Elie:** the two no-data instruments → B-new-1 (the restricted roots) → B-new-2 (the π audit) → Target 1 after the hash → Target 2 after the hash.
- **Grace:** the residual + Z(β) → the non-cosmology pins + the lineage pins + 5(g) → the cosmology pins after the hash.
- **Keeper:** gate each lane as it lands; the register; fold into rubric Section 2 and re-derive Section 3; EOD on Casey's word.

**Rubric cells:**
- Internal C (commitment ontology): the rate law, the word/cell collision, the closure route.
- External 4 (Λ/filling law): Target 1.
- Internal B/D: the π audit, the two 3s, α.

— Keeper, 2026-10-09.
