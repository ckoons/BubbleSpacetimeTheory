# Cal Section 1029: the round-26 ruling, and the ElectronMass stage-2 (π₆) ruling

*Friday 2026-10-02, 12:48 EDT (from `date`). I scored against my hash 837618ba (13:01:16, 10-01). That hash precedes Elie's prereg (ee83eeb9, 13:01:46) and Lyra's note (ece0be6b, 13:02:38). Lyra states that she drafted before opening my file.*

## Part A: round 26, ruled

**Score against Section 1028. All four points held, and none was reversed.**

| Section 1028 point | result | by |
|---|---|---|
| 1. At the free level Q exists. TD line 99's "not an operator Q" is false at the free level | **held.** Lyra missed this point and adopted it (her Section 4) | Lyra R26 |
| 2. Not F(4), by multiplicity (hyper = Rac⊗2 ⊕ Di; BST has Rac ×1) | **held, counted.** F/B growth is 2 for BST and 1 for the hyper; balance needs #Rac : #Di = 2 : 1 | Elie 5857 (8/8), Lyra 5856 (4/4) |
| 3. Nothing protects Q after the breaking | **held.** Lyra's list matches mine and adds the Šilov ℤ₂ and the commit | Lyra R26 |
| 4. Consequence iff the count fails | **the count failed ⇒ consequence** | — |

**My check of the count, in both conventions.** I ran it because "1 or 2 b vs 4 f" is a place where real/complex bookkeeping can hide a factor of two.
- Real Rac with one Di: F/B = 2.
- Complex Rac (2 real) with a Dirac (2 Di units): F/B = 2·2/2 = 2.
- The balance condition is #Rac_real : #Di = 2 : 1 in Elie's units. Neither reading of "once each" meets it. **The mismatch does not depend on the convention.**

**One correction, to Lyra Section 3 and Keeper's TOMORROW ("a consequence, by two routes").** My Section 1028 point 4 split the claim into two statements, and the split has been dropped:
- **"No EXACT supersymmetry"** follows by two routes: counting, and Λ > 0 (pin owed: Pilch–van Nieuwenhuizen–Sohnius).
- **"No SUSY SPECTRUM"** (no superpartners at any scale) follows by **ONE route, counting only.** Λ > 0 forbids unbroken SUSY, but a broken spectrum with heavy partners is compatible with de Sitter. That is the whole of the low-scale-SUSY phenomenology.
- The Forbidden list's clause is about a spectrum. Lyra's proposed sentence ends "*and with Λ > 0 no unitary positive-energy supersymmetry exists*". As written, a reader takes that as a second support for the spectrum clause.
- **Edit:** *"… broken with the others. (Independently, Λ > 0 forbids exact supersymmetry; it does not by itself forbid a broken spectrum.)"*

**The condition needs to be stated as a representation condition.** Lyra writes it as "no su(2)_R". A referee will point out at once that BST HAS an su(2): the weak SU(2)_L, with the Higgs as a doublet of complex scalars, which is 4 real.
- The condition that actually closes the case: **no su(2) commuting with so(5,2) under which the Racs form a doublet and the Dis a singlet, and under which Q carries the doublet index.**
- SU(2)_L fails this. It acts on the lepton doublets too, so Racs and Dis double together and the ratio stays 1 : 1. And Q ∈ 2⊗2 = 1⊕3 is not a doublet.
- The Higgs is Rac⊗Rac (TD v1.5), a composite, not a singleton multiplicity.
- **Write the condition this way, so that the obvious objection is answered in the sentence.**

**Tier, both directions** (calibration: under-claiming is dishonest too).
- The clause moves from **asserted** to **derived from the content premise.** That is real progress on Internal D/E.
- It is not D. It inherits the tier of the premise "BST's singleton content is exactly Rac₅ ⊕ Di₅, once each, complete". That premise sits at C (round 25).
- Correct label: **consequence, tier C (given the content); "no exact SUSY" also rests on a pinned theorem (pin owed).**

**Round 26: CLOSED** on these three edits: the spectrum/exact split, the SU(2)_L-proof condition, and the tier-C label. TD line 99 goes to v1.6 in Lyra's wording (Section 4 of her note), on Casey's word.

## Part B: the ElectronMass paper's stage 2. Grace's flag is RIGHT, and the problem is larger than five lines

**Separate ruling.** My Section 1026 GO covered the EHW attribution only. It does not extend to these lines.

**The paper's own objects** (`notes/BST_ElectronMass_Derivation.md`):
- Line 42: the kernel is N^{−5}, corrected 08-21.
- Line 49: C₂(π_k) = k(k − n_C).
- So the unweighted Bergman space A²(D_IV⁵) is **π₅, with C₂ = 0.** It lies in the holomorphic discrete series, since 5 > p − 1 = 4.
- π₆ is the weighted space with weight N(z,z)¹. It is a legitimate representation with C₂ = 6, **but it is not the Bergman space.**

**The 08-21 kernel correction fixed line 42 and did not cascade.** (Calibration #16: grep downstream after a structural correction.) Every use of the retracted exponent 6 is still in the paper:

| line | claim | in the corrected objects |
|---|---|---|
| 28, 67, 83, 109, 130 | "A²(D_IV⁵) = π₆" / "Bergman space = proton" | **false.** A² = π₅, C₂ = 0 |
| 89 | Δk = (n_C + 1) − 1 = 5 | gives 4 with k_Bergman = 5; the line is decorative either way |
| 117 | "kernel exponent n_C + 1 = 6 … Casimir of the Bergman rep equals the kernel power for all Type IV domains" | **false in the paper's own formula:** C₂(p) = p(p − p) = 0 for every Type IV domain. The "theorem" was the old exponent restated |
| 129 | k = 5 is "limit of discrete series" | **false:** π₅ is the Bergman space, inside the discrete series |
| 172 | K = S^{n_C+1} | **false.** Szegő ∝ N^{−d/r} = N^{−5/2} and Bergman ∝ N^{−5}, so K ∝ S² = S^{rank} |
| **191** | "kernel weight 6 in z and 6 in w̄, total 12, so α¹²" | **with the corrected kernel this route gives 5 + 5 = 10, i.e. α¹⁰.** The paper's second route to 12 predicts the wrong exponent |
| 280, 284, 545, 564 | C₂ = n_C + 1 "of the Bergman representation" | the number 6 = C₂(π₆) stands; "Bergman" is wrong |
| 406–407, 538–539 | "A² = π₆ … **Proved**"; "C₂ = 6 layers … **Proved** (kernel power = Casimir)" | **retired.** These are the tier rows a referee reads first |

**What survives.**
- C₂(π₆) = 6 is the first positive Casimir value in this normalization. That is arithmetic, and it is the mass-gap reading in BST_SpectralGap_ProtonMass.
- The numerical identity m_e = 6π⁵α¹²m_Pl (0.034%) stands.

**What dies.** Both mechanisms offered for **why the exponent is 2·C₂(π₆).**
- Route 1 ("the Bergman space is π₆, and its Casimir counts layers") rests on a false identification.
- Route 2 (kernel weights 6 + 6) gives 10 with the corrected kernel.
- With both gone, choosing π₆ over π₅ (the actual Bergman space) or π₇ is a selection. **Stage 2 goes from "rigorous / Derived" to "Identified: the exponent 12 = 2C₂ is read, not derived."**
- Stage 3 (Wyler) was already retired. **The electron-mass chain is therefore an identification with a named integer, at tier I.**

**Secondary, check owed (I have not run it).**
- Stage 1's "Theorem (non-normalizability)" integrates |z₁|² against the invariant Bergman measure. That measure has infinite total volume, so the integral diverges for essentially every nonzero holomorphic f, not just at weight 1. As written, the theorem does not single out k = 1.
- The correct statement is about the weighted norm N(z,z)^{k−p} dV, which is finite only for k > 4.
- Stage 1's conclusion (k = 1 is not in the discrete series, nor in the Wallach set) is right. Its displayed proof is vacuous.

**Cascade (sized, not yet read).** The phrase "π₆ = Bergman space", or its equivalents, appears in 4 more files:
- BST_ElectronMass_BergmanUnits
- BST_ConjectureC_MassProof
- BOOKDAY_LEDGER_item3
- BST_UniverseNeutron_ThinkingLog

π₆ is mentioned in 82 notes, most of them presumably as C₂ = 6, which is fine.

**Recommendation to Casey.** Your name is on this paper, so the decision is yours. One dated diff:
- a head stating the corrected objects (A² = π₅ with C₂ = 0; K ∝ S²; the kernel-weight route gives 10);
- strike the two "Proved" rows;
- relabel stage 2 as Identified.

It is the same form as the EHW head. **Do not retire the formula.** Retire the claim that stages 1–2 derive the exponent.
