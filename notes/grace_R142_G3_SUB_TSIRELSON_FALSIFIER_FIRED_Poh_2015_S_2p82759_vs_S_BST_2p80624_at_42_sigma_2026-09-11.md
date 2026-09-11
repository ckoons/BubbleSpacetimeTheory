# Round 142 G3 — the SCMP / SP-30-5 "sub-Tsirelson 1/8" falsifier: **FIRED**, and it fired in October 2015

**Grace, 2026-09-11 (Friday) 12:48 EDT.** Keeper's flag (Round 142 G3): registry line ~10603 (T2469) carries "SCMP predicts sub-Tsirelson deviation 1/2^N_c = 1/8 = 0.125 in Bell experiments … if measured deviation < 0.125 reliably, SCMP refuted at Layer 1." It is in Vol 14, Vol 15 and the Curriculum README's principles list; it is in neither the rubric nor the 08-26 one-pager. Ruling asked: fired / not fired / not decidable, source pinned. **Ruling: FIRED.** Numbers first.

## 1. The claim, as the registry states it (three sites, one prediction)

| site | sentence | observable |
|---|---|---|
| T2397 SP-30 table (registry :7117) | S_BST = (N_c/rank)·√(g/rank) = 2.806 vs Tsirelson 2.828 (0.79% deviation) — "SHARPEST — direct vs QM" | max CHSH value S |
| T2399 (registry :7191–7240) | S_BST² = (2^g − rank)/2^{rank²} = 126/16 = 7.875; Tsirelson² − S_BST² = 1/2^{N_c} = 1/8 EXACTLY; "(b5) BOUNDED: S_BST < Tsirelson STRICTLY" | S² |
| T2469 SCMP falsifier (registry :10603) | "if measured deviation < 0.125 reliably, SCMP refuted at Layer 1" | S² deficit |

Calibration #17 (registry :8818, :8910; Lyra on Elie S22/S23, 2026-05-20) re-read 126/16 as a "trace-level capacity" of a substrate operator, NOT a max eigenvalue — and then wrote, in the same entry: **"Bell experiment prediction validity: REMAINS VALID via trace-level / integrated-capacity interpretation … Either trace-form OR yet-unknown operator-form gives the same DEVIATION."** So the corpus's own words kept the observable claim alive after the reframing. There is no reading of the registry under which the 1/8 deviation was withdrawn from the laboratory. The falsifier is live as written, and it is decidable.

## 2. The primary, pinned (fetched today, not from memory)

**Poh, Joshi, Ceré, Cabello, Kurtsiefer, "Approaching Tsirelson's bound in a photon pair experiment," Phys. Rev. Lett. 115, 180408 (2015); arXiv:1506.01865.** Abstract, verbatim: "a value **2.82759 ± 0.00051** is observed" … "the smallest distance with respect to Tsirelson's bound ever reported, namely, **0.00084 ± 0.00051**." The experiment was BUILT to test a sub-Tsirelson prediction — Grinbaum's proposed bound 2.82537 — and rejects it at 4.3σ.

## 3. The arithmetic (python, this session)

| quantity | value |
|---|---|
| Tsirelson 2√2 | 2.828427 |
| S_BST = √(126/16) | 2.806243 |
| BST's predicted deficit in S | 0.022184 |
| Poh 2015 measured S | 2.82759 ± 0.00051 |
| S_meas − S_BST | **0.02135 = 41.9σ** |
| S²_meas | 7.9953 ± 0.0029 |
| S²_meas − 126/16 | 0.1203 ± 0.0029 — the predicted deficit 0.125 is excluded at **41.7σ** |
| Grinbaum's 2.82537 (rejected 4.3σ by the same data) | BST's bound sits **7.3×** further below Tsirelson than Grinbaum's |

The row's own trigger — "measured deviation < 0.125 reliably" — is met with a measured deviation of 0.0047 ± 0.0029 in S² (= 0.00084 ± 0.00051 in S): forty-one standard deviations inside the refutation region.

## 4. The two objections, answered before they are raised

**(a) "Poh 2015 is not loophole-free."** True, and irrelevant here. Keeper's flag said loophole-free values sit at the bound to four digits — that is not so; the loophole-free CHSH experiments (Hensen 2015, Rosenfeld 2017, Li 2018, Storz 2023) report S far below 2√2 because their detection efficiency and state fidelity are lower; they were designed to close loopholes against LOCAL REALISM, not to approach the quantum maximum. The four-digit value is Poh's fair-sampling photon experiment. The fair-sampling assumption is a loophole against local-hidden-variable models, which can exploit the detection post-selection. It is NOT a loophole against a claimed sub-quantum ceiling: the detected pair ensemble is a quantum state (local filtering of a quantum state is a quantum state), and BST's (b5) "S < Tsirelson STRICTLY" was stated for the substrate's quantum correlations as such, with no ensemble exempted. A theory whose ceiling is 2.806 for every state cannot have a post-selected sub-ensemble at 2.8276 ± 0.0005. The loophole does not open a door for this claim; the direction of the loophole is wrong.

**(b) "Calibration #17 moved the claim to a trace-level capacity that no CHSH experiment measures."** Then the falsifier was never a falsifier, and the sentence "REMAINS VALID at observable level" was false when written. Either way the observable-level sentence dies: fired if the observable claim stood, vacuous if it did not. I rule it FIRED, because the registry kept the observable claim on the record for four months, in three rows, as "the sharpest falsifier in the program," and a falsifier the program called its sharpest does not get to become unfalsifiable at the moment the number arrives. The trace identity Tr(B²) = 126/16 (Elie toy 3186, Bergman projection) SURVIVES as a statement about an operator on H²(D_IV⁵); it makes no laboratory claim and is not what fired.

## 5. What fired / what died / what survived (Section E ceremony, K1826 form)

- **What fired:** the sub-Tsirelson deviation 1/2^{N_c} = 1/8 in S² (S_max = 2.806), SP-30-5 / T2399 / T2469 Layer-1 — against Poh et al. 2015, S = 2.82759 ± 0.00051, 41.9σ. Not a near miss; the entire class of sub-Tsirelson ceilings below ~2.8265 is dead by that one measurement, and BST's was the deepest of them.
- **What DIED:** S_BST = 2.806 as a prediction; "sharpest falsifier in the program" (T2397 :7122); SP-30-5's 6–12-month falsifier window (it had closed a decade before it was written — the prediction was registered 2026-05-19, the measurement is from 2015); Paper #123 / #125's Bell anchor; Elie toy 3115's Bell-apparatus proposal and the outreach letter `Letter_Bell_Substrate_CHSH_Draft.md` (the experiment they propose was done, at higher precision than proposed, and refutes the proposal's number); T2469's Layer-1 operational content; Vol 14 Ch 6's thesis and Vol 5 Ch 8's "BST sub-Tsirelson 1/8 falsifier" as a standing item.
- **What SURVIVED:** the integer identity 2^g/2^{rank²} − (2^g − rank)/2^{rank²} = rank/2^{rank²} (arithmetic; it never said anything until it was attached to S); the trace-class statement Tr(B²) = 126/16 on H²(D_IV⁵) (operator fact, no laboratory claim); T2469's Layer-2 (metaphysical) claim, already DEFAULT-DENY EXTERNAL per Cal #48/#49 and now with no Layer-1 leg under it; the operator-zoo membership of the substrate-CHSH operator (T2419 etc. cite it as an operator, not as a prediction). **The Tsirelson bound itself is untouched: BST's Hardy-space QM (T751–T757, T2630) recovers standard QM, whose bound is 2√2 — the fired number was a substrate-coding reading laid over QM, not a consequence of the geometry.**
- **Certification:** ruling Grace 2026-09-11 (Keeper's flag, "yours to rule"); Keeper's certification of the Section E row pending; Cal's C3 falsifier cross-check will meet it today.

## 6. The lesson, in one line for the K-lessons index
**A falsifier that names an experiment must be checked against the literature the day it is registered, not the day someone quotes it.** SP-30-5 was registered 2026-05-19 with a "6–12 month" window; the refuting measurement was ten years old (PRL, October 2015) and its arXiv number is 1506.01865. The corpus fails at seams — here the seam between "we predict" and "has anyone looked."

## 7. Consumer list (sentences that quote SCMP / SP-30-5 / 126/16 / 1/8 as STANDING) — swept by grep, counted, NOT edited by me (K1892: legacy chapters are corrected in place by their owner, dated)

| file | hits | what it says |
|---|---|---|
| Curriculum/Vol05_Quantum_Mechanics/Curriculum_Vol5_Ch8_Bell_CHSH_Quantum_Correlations_v0_1.md | 21 | the chapter IS the prediction |
| Curriculum/Vol14_Information_Theory/Curriculum_Vol14_Ch6_Bell_SubTsirelson_Info_v0_1.md | 12 | the chapter IS the prediction |
| Curriculum/Vol05_Quantum_Mechanics/Curriculum_Vol5_Ch12_Pedagogical_Bridge_Synthesis_v0_1.md | 9 | synthesis quotes |
| Curriculum/Vol05_Quantum_Mechanics/Curriculum_Vol5_Architectural_Scaffold_v0_1.md | 7 | scaffold |
| Curriculum/Vol05_Quantum_Mechanics/Curriculum_Vol5_Ch11_POVMs_Quantum_Information_v0_1.md | 6 | SCMP framework cites |
| Curriculum/Vol14_Information_Theory/Curriculum_Vol14_Architectural_Scaffold_v0_1.md | 5 | scaffold |
| Curriculum/Vol05_Quantum_Mechanics/INDEX.md | 5 | :38 "BST sub-Tsirelson 1/8 falsifier" (row 8) |
| Curriculum/Vol00_Substrate_Foundation/Curriculum_Vol0_Ch7_The_Operator_Zoo_v0_1.md | 4 | operator-zoo (survives as operator; prediction sentence dies) |
| Curriculum/KEEPER_REFINEMENT_NOTES.md | 4 | notes |
| Curriculum/Vol15_Methodology/Curriculum_Vol15_Ch8a_Casey_Named_Principles_Cal_META_Discipline_v0_1.md | 3 | :28 "SCMP (May 22) — Bell sub-Tsirelson 1/8 falsifier"; :80 "8 STANDING" (SCMP is one of the eight) |
| Curriculum/Vol14_Information_Theory/INDEX.md | 3 | :39 Ch 6 row "Bell |S|² = 126/16 < 2√2"; :59 |
| Curriculum/Vol14_Information_Theory/Curriculum_Vol14_Ch4_Nyquist_Koons_Tick_v0_1.md | 3 | |
| Curriculum/Vol02_Particle_Physics/BST_Vol2_Ch12_Experimental_Program_v0_1_narrative.md | 3 | experimental program lists the Bell test |
| Curriculum/Vol01_QFT_from_D_IV5/BST_Curriculum_Vol1_QFT_from_DIV5_v0_1_outline.md | 3 | |
| Curriculum/Vol00_Substrate_Foundation/Curriculum_Vol0_Ch3_Substrate_Operating_System_v0_1.md | 3 | |
| Curriculum/README.md | 1 | :39 Vol 14 row "Bell sub-Tsirelson" (front door — Keeper's, today) |
| 14 further files at 1–2 hits each (Vol0 Ch7, Vol1 Ch6, Vol3/Vol4/Vol15 scaffolds, Vol9 ×2, Vol11 Ch12, Vol14 Ch1/Ch5/Ch8/Ch11, Vol5 Ch7/Ch10, Vol15 Ch8b/INDEX) | 1–2 | cites |
| Guide/INDEX.md | 2 | version-history lines only (v38/v39) — history, not a standing claim; no edit |
| notes/*.md outside board/log/registry | 124 files | mostly dated artifacts; the ones that matter are Elie's Bell letter draft and Paper #123/#125 outlines — dated 05-19/05-20, now carry a fired prediction |

**Registry edits made today (dated, in the text):** T2397's SP-30-5 line (:7122), T2399's section head (:7191), T2469's falsifier line (:10603) — each gets one dated FIRED bracket pointing at this note and the pin. Graph statuses on T2399 and T2469 updated (identity kept "proved"; prediction marked fired). Falsifier register → v0.5 with row E4. Nothing in Curriculum/ or Guide/ edited by me.

— Grace. Source pinned: arXiv:1506.01865 / PRL 115, 180408 (2015), abstract fetched 2026-09-11 12:48.
