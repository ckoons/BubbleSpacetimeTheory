# R17 pins: unitary parabolic induction preserves temperedness, and the induced rep splits into finitely many tempered irreducibles (draft)

Grace lane, 2026-09-27. All paths are relative to `data/sources_grace_2026-09-27/`. Quotes come from `.txt` files made with `pdftotext -layout` from saved PDFs. Where the text layer garbles Ind_H^G super/subscripts or ⊕ signs, the page was rendered into `r17/png/` and transcribed in `r17/VISUAL_TRANSCRIPTIONS.txt` (VT-A … VT-I). No git.

## Verdict up front

| Claim | Status |
|---|---|
| (T) σ tempered for M, ν real ⇒ Ind_{MAN}^G(σ ⊗ e^{iν} ⊗ 1) is tempered for G | **PINNED PRIMARY, fully general (any locally compact G, any closed P = LU with U amenable).** It is three numbered statements composed: BK II Remark 2.4(2), then BK II Lemma 4.3, then BK II Lemma 2.3 (≡ BHV Thm F.3.5 + Ex. E.1.8(i) + Thm E.2.4). A second, independent pin is CCH Remark 4.1 + Prop. 4.2. |
| (F1) σ **square-integrable** (discrete series) ⇒ Ind_P^G(σ ⊗ φ) is a finite direct sum of irreducibles, each tempered | **PINNED PRIMARY-VIA-CITATION + one-line INFERENCE.** CCH Thm 6.6 (= Harish-Chandra [HC76] Thm 38.1; proof cited to [Kna86] Thm 14.31) with Def. 6.4: the commutant is a *finite-dimensional* C*-algebra. The step from a finite-dimensional commutant to a finite direct sum of irreducibles is standard operator algebra and is **not** pinned to a numbered statement. Temperedness of each summand follows from (T) + BHV Rem. F.1.2(iii),(iv). |
| (F2) σ an arbitrary **tempered irreducible** of M (including limits of discrete series) ⇒ same finite decomposition | **INFERENCE** from CCH Thm 5.16 (applied to L) + BHV Thm E.2.4 + Prop. E.2.2 + (F1). **One gap is PIN OWED:** that P_L·N is a parabolic subgroup of G whose Langlands factors are those of P_L (standard; Knapp 1986 Ch. VII, paywalled). |
| Knapp–Zuckerman converse: every irreducible tempered rep is a constituent of such an induced rep | **PINNED, SECONDARY-quoting-numbered:** HSY Theorem 2.2 ("Every tempered representation of G is basic"), which HSY attribute to KZ Annals 116, Corollary 8.8. **PIN OWED** on the KZ original (JSTOR, paywalled). |
| Knapp 1986 Prop. 7.x / Thm 14.2 / Thm 14.31 | **PIN OWED.** Paywalled (De Gruyter/PUP). Crossref metadata saved. Not opened, so no numbering is asserted from Knapp itself. |

**Bottom line.** The temperedness half is pinned in full generality, with no finiteness or linearity hypotheses. The finiteness half is pinned for square-integrable σ in the CCH class of groups (real points of a connected reductive algebraic group; see the hypothesis check in Section 4). For general tempered σ it is an inference with one standard structural fact owed.

---

## 0. Definitions (quoted before any statement)

### 0.1 "Tempered"

- **D1, weak containment. This is the definition used for (T).** BK II = Benoist–Kobayashi, *Tempered homogeneous spaces II*, arXiv:1706.10131. `r12_tempered/arxiv_1706.10131.txt:425-428`, Definition 2.1 (VT-A):
  > "The unitary representation π is said to be tempered or G-tempered if π is weakly contained in the regular representation λG of G in L2 (G) i.e. if every matrix coefficient of π is a uniform limit on every compact subset of G of a sequence of sums of matrix coefficients of λG ."

  The setting is `:420-424`: "Let G be a locally compact group and π be a unitary representation of G in a Hilbert space Hπ … The notion of tempered representation is due to Harish-Chandra."
- **Weak containment.** BHV = Bekka–de la Harpe–Valette, *Kazhdan's Property (T)*, authors' preprint of 23 Feb 2007 (numbering match against CUP 2008 is **PIN OWED**, as in R12). `r12_tempered/bhv_KazhdanTotal.txt:17758-17768`, Definition F.1.1:
  > "We say that π is weakly contained in ρ if every function of positive type associated to π can be approximated, uniformly on compact subsets of G, by finite sums of functions of positive type associated to ρ."

  Remark F.1.2, `:17793-17796`:
  > "(iii) If π is contained in ρ, then π ≺ ρ." … "(iv) For unitary representations π, ρ, and σ of G, weak containments π ≺ ρ and ρ ≺ σ imply π ≺ σ."
- **D2, L^{2+ε}. Used by the Knapp–Zuckerman-side sources.** HSY = Hochs–Song–Yu, arXiv:1705.02088, `r12_tempered/arxiv_1705.02088.txt:401-402`:
  > "A unitary irreducible representation π ∈ Ĝ is tempered if all of its K-finite matrix coefficients belong to L2+ ε (G) for all ε > 0."
- **D-CCH, the reduced dual.** CCH = Clare–Crisp–Higson, *Parabolic induction and restriction via C\*-algebras and Hilbert C\*-modules*, arXiv:1409.8654, `r17/arxiv_1409.8654.txt:46-49`:
  > "… a real reductive group, for which the irreducible representations in the reduced dual are precisely Harish-Chandra's irreducible tempered representations; see for example [CHH88]."

**Match check.** D1 ⇔ D2 on irreducibles is Cowling–Haagerup–Howe (connected semisimple, finite center). It is pinned in R12 as BK II Prop. 2.6: SECONDARY, with the CHH original PIN OWED (`r12_tempered/R12_TEMPERED_PINS_draft.md`, Section 0). The reduced dual (D-CCH) is by definition the set of irreducibles weakly contained in λ_G (BHV Appendix F), so D-CCH = D1 on irreducibles. The Levi factor M is reductive and possibly disconnected. For M, D1 is the definition in force for (T), and it needs no hypothesis on M. D2 enters only through HSY/KZ, on HSY's class (Section 4).

### 0.2 The induction: unitary, normalized

- **General unitary induction (the one in (T)).** BK II `r12_tempered/arxiv_1706.10131.txt:364-388`, Section 2.1.2:
  > "More generally, for any unitary representation π of H, one defines the (unitarily) induced representation Π := IndG H (π) in the following way. … The space of the representation Π is the space HΠ := L2 (G/H; Hπ ) of Hπ -valued L2 -functions on G/H and the action of G is given, for g in G, ψ in HΠ , x in G/H, by (Π(g)ψ)(x) = c(g −1 , x)1/2 π(σ(g, g −1x))ψ(g −1 x), where c is again the Radon–Nikodym cocycle (2.1)."

  The factor c^{1/2} is what makes the induced representation unitary. For H = P = MAN it is exactly the ρ-shift of normalized parabolic induction. BHV's own calibration shows this, Example E.1.8(iii) (VT-D, `bhv_KazhdanTotal.txt:17402-17422`): for SL₂(R), Ind_P^G of the unitary character χ_t^±(a) = ε^±(a)|a|^{it} is the principal series acting by |−cω+a|^{−1−it}. The "−1" is the ρ-shift, supplied automatically by the quasi-invariant measure. So **BHV/BK II "Ind" = normalized (unitary) parabolic induction.** No extra e^{ρ} is to be inserted.
- **Parabolic induction as used for P = MAN.** CCH `r17/arxiv_1409.8654.txt:536-540`:
  > "Apart from being a subgroup of P = L ⋉ N, the Levi factor L = P/N is also a quotient. So if τ : L → U(H) is a unitary representation of L, then we can consider τ as a representation of P too, and so form the unitarily induced representation IndG P τ : G −→ U(IndP H)."

  Langlands decomposition, `:760-769`:
  > "P = (MP × AP ) ⋉ NP = MP AP NP , where: (a) NP = N. (b) MP AP = L. (c) AP is the group of positive-deﬁnite matrices in the center of L. … every tempered irreducible representation of L is a product σ ⊗ ϕ of a tempered irreducible representation σ of MP with a unitary character ϕ of AP."
- **HSY's normalization and parameter convention.** `r12_tempered/arxiv_1705.02088.txt:463`:
  > "(Here and in the rest of this paper, Ind denotes normalised induction.)"

  Basic representations, `:596-607` (VT-I):
  > "Let ν ∈ ia∗ . A basic representation of G is a representation of the form IndG P (πM … ⊗ eν ⊗ 1N ), where 1N is the trivial representation of N."

  **Convention collision, pinned:** HSY write e^{ν} with ν ∈ i**a**\*. The task writes e^{iν} with ν ∈ **a**\* real. These are the same set of unitary characters of A, with ν_HSY = iν_task. CCH write φ ∈ Â, a unitary character of A. All three describe the same object.

---

## 1. (T) Induction preserves temperedness: the weak-containment route

**Pin T1. PRIMARY, numbered.** BK II Lemma 2.3, `r12_tempered/arxiv_1706.10131.txt:434-441` (VT-A):
> "Lemma 2.3. Let G be a locally compact group, H be a closed subgroup of G and π be a unitary representation of H. If π is H-tempered then the induced representation IndG H (π) is G-tempered."
> "Proof. Since the H-representation π is weakly contained in the regular representation λH of H, the G-representation IndG H (π) is weakly contained in the regular representation λG = IndG H (λH ), and hence is G-tempered."

It is introduced at `:433` by "This notion is also preserved by induction."

**Pin T1′. PRIMARY, numbered. The BHV ingredients of T1, independently.**
- BHV Theorem F.3.5, `r12_tempered/bhv_KazhdanTotal.txt:18373-18376` (VT-C):
  > "Theorem F.3.5 (Continuity of induction) Let H be a closed subgroup of the locally compact group G. Let σ and τ be unitary representations of H such that σ ≺ τ. Then IndG H σ ≺ IndG H τ."
- BHV Example E.1.8(i), `:17395-17397` (VT-D):
  > "If H = {e} and σ = 1H , then IndG H σ is the left regular representation λG of G."
- BHV Theorem E.2.4, `:17479-17483` (VT-E):
  > "Theorem E.2.4 (Induction by stages) Let H and K be closed subgroups of G with K ⊂ H, and let τ be a unitary representation of K. Then IndG H (IndH K τ ) is equivalent to IndG K τ."

  With K = {e}: Ind_H^G λ_H = Ind_H^G Ind_{e}^H 1 = Ind_{e}^G 1 = λ_G. This is BK II's "λG = IndG H (λH )".

**Pin T2. PRIMARY, numbered. The inducing rep σ ⊗ e^{iν} ⊗ 1 is P-tempered.**
- BK II Remark 2.4(2), `r12_tempered/arxiv_1706.10131.txt:445-451` (VT-A):
  > "When G is a product of two closed subgroups G = SZ with Z central, a unitary representation π of G is G-tempered if and only if it is S-tempered."

  Apply this to L = MA, with S = M and Z = A. A is central in L (CCH `:764`, "(c) AP is the group of positive-deﬁnite matrices in the center of L"). The restriction (σ ⊗ e^{iν})|_M is σ, because M ∩ A = {e} (CCH `:760`, M_P × A_P). So **σ M-tempered ⇒ σ ⊗ e^{iν} L-tempered.**
- BK II Lemma 4.3, `r12_tempered/arxiv_1706.10131.txt:832-840` (VT-B):
  > "Lemma 4.3. Let P = LU be a real algebraic group which is a semidirect product of a reductive subgroup L and its unipotent radical U. Let π0 be a unitary representation of P which is L-tempered and trivial on U. Then the representation π0 is also P -tempered."

  Take π₀ = σ ⊗ e^{iν} ⊗ 1_N and U = N. Then **σ ⊗ e^{iν} ⊗ 1 is P-tempered.**
- The only structural input in the proof of Lemma 4.3 is "Since U is amenable" (`:838`). For N: BHV Corollary G.2.3, `bhv_KazhdanTotal.txt:19167-19168`:
  > "Every compact extension of a soluble topological group is amenable."

  N is nilpotent, hence soluble. Hulanicki–Reiter, BHV Theorem G.3.2, `:19347-19351`:
  > "(i) G is amenable; (ii) 1G ≺ λG ; (iii) π ≺ λG for every unitary representation π of G."

  These are "equivalent".

**Composition (T). Pinned links, INFERENCE only in chaining them.** σ ≺ λ_M ⇒ (Rem. 2.4(2)) σ⊗e^{iν} ≺ λ_L ⇒ (Lemma 4.3) σ⊗e^{iν}⊗1 ≺ λ_P ⇒ (Lemma 2.3, H = P closed) **Ind_{MAN}^G(σ ⊗ e^{iν} ⊗ 1) ≺ λ_G, i.e. tempered (D1).** BK II itself runs exactly this chain in its own proof, at `:1087-1093`: "Proposition 3.8 and Remark 2.4 tell us that the representation … π0 is L-tempered by (2.4). Therefore, by Lemma 4.3, the representation π0 … Lemma 2.3 implies that this representation Π0 is G-tempered." It also states the P-tempered → G-tempered step in the intro at `:254-256`: "If we knew that π were a P -tempered representation it would be easy to conclude, using Lemma 2.3, that the representation Π = IndG P π is G-tempered."

- **Hypotheses used:** G locally compact; P closed; A central in L; N amenable. **No** irreducibility of σ, **no** finite center, and **no** linearity are needed.
- The one hypothesis to watch is BK II's "real algebraic" in Lemma 4.3. The proof quoted above uses only that U is a closed normal amenable subgroup acting trivially. So the lemma applies to P = MAN in SO₀(2,5) or its covers as written.

**Pin T3. PRIMARY, numbered. An independent C\*-route.** CCH Remark 4.1 (end), `r17/arxiv_1409.8654.txt:640-643` (VT-F):
> "But the representation of C ∗ (G) on Cr∗ (G/N)ψ is easily checked to be weakly contained in L2 (G/N), and the representation of C ∗ (G) on this Hilbert space factors through Cr∗ (G) because N is amenable."

CCH Proposition 4.2, `:646-650` (VT-F):
> "4.2 Proposition. (See [Cla13, Corollary 1].) Let τ be a tempered unitary representation of L on a Hilbert space H. The parabolically induced representation IndG P τ is unitarily equivalent to the representation of G on the Hilbert space Cr∗ (G/N) ⊗Cr∗ (L) H."

Together: Ind_P^G τ is a representation of C_r\*(G), i.e. weakly contained in λ_G, i.e. tempered. This holds on CCH's class of groups (Section 4).

**Corroboration (unnumbered, not a pin).** Afgoustidis, arXiv:1510.02650, `r17/arxiv_1510.02650.txt:407-410`: after M(δ) = Ind_{MχAχNχ}^G(V_{Mχ}(µ) ⊗ e^{iχ} ⊗ 1), eq. (3.1):
> "This is a tempered representation."

BK II intro bullet, `r12_tempered/arxiv_1706.10131.txt:112-113`:
> "Tempered representations are closed under induction, restriction, tensor product, and direct integral of unitary representations."

---

## 2. (F1) Finitely many constituents: square-integrable σ

**Pin F1a. PRIMARY statement, quoting Harish-Chandra.** CCH Theorem 6.6, `r17/arxiv_1409.8654.txt:1206-1210` (VT-H):
> "6.6 Theorem. [HC76, Theorem 38.1] Let σ be an irreducible square-integrable unitary representation representation of M, and let ϕ be a unitary character of A. The finite-dimensional C ∗ -algebra I(σ, ϕ) is the full commutant of the parabolically induced representation IndGP (σ ⊗ ϕ)."
> "Proof. See [KS80, Corollary 9.8] and [Kna86, Theorem 14.31]."

The doubled word "representation representation" is in the source. The theorem is introduced at `:1204` with "The following result is known as Harish-Chandra's Completeness Theorem."

**Pin F1b. Why I(σ, φ) is finite-dimensional.** CCH Definition 6.4, `:1175-1179` (VT-G):
> "We denote by I(σ, ϕ) the ﬁnite-dimensional C ∗ -algebra of operators on the Hilbert space of the principal series representation IndG P (σ ⊗ ϕ) generated by the Knapp-Stein intertwiners Uw,ϕ associated with the elements of the ﬁnite group Wσ,ϕ ."

The finiteness of W, `:1132-1133`: "W = NK (L)/K ∩ L = NG (L)/L. It is a finite group; see [Kna86, Chap. V]."

**Inference F1 (one line, not pinned to a numbered statement).** A unitary representation whose commutant is a finite-dimensional C\*-algebra is a finite orthogonal direct sum of irreducibles. The reason: write 1 = Σ p_i over a maximal family of orthogonal minimal projections in the commutant; there are at most dim I(σ,φ) of them, and each range is irreducible because p_i·(commutant)·p_i = ℂp_i. Each summand is a subrepresentation of a tempered representation (T), so it is tempered by BHV Rem. F.1.2(iii) followed by F.1.2(iv).

**Knapp's own numbering (PIN OWED).** CCH cite "[Kna86, Theorem 14.31]" for the proof. Crossref places Knapp's Chapter XIV "Irreducible Tempered Representations" at pp. 515–625 (`r17/crossref_10.1515_9781400883974-017.json`). The task's suggested "Prop 7.14 / Theorem 14.2" was **not** verified: the book was not opened. "Theorem 14.2" matches the numbering of Knapp–Zuckerman II (see Section 3), not the book as far as we can check.

## 3. (F2) General tempered σ of M, and the Knapp–Zuckerman converse

**Pin F2a. PRIMARY, numbered, cited to Langlands/Trombi.** CCH Theorem 5.16, `r17/arxiv_1409.8654.txt:1064-1066`:
> "5.16 Theorem. (See [Lan89, Lemma 4.10] or [Tro77].) Every tempered irreducible representation of G may be realized as a subrepresentation of a principal series representation."

"Principal series" is defined at `:772-780` as Ind_P^G(σ ⊗ φ) with σ square-integrable of M_P.

**Pin F2b. BHV Proposition E.2.2 (induction commutes with ⊕).** `r12_tempered/bhv_KazhdanTotal.txt:17455-17457` (VT-E):
> "Let (σi , Ki )i be a family of unitary representations of H. Then IndG H (⊕i σi ) is equivalent to ⊕i IndG H σi."

**Inference F2.**
1. Apply F2a to the reductive group L. Then σ⊗e^{iν} ⊂ Ind_{P_L}^L(σ′ ⊗ φ′), with σ′ square-integrable on M′ ⊂ L.
2. Write the principal series as σ⊗e^{iν} ⊕ (complement). By E.2.2 and E.2.4, Ind_P^G(σ⊗e^{iν}⊗1) is a subrepresentation of Ind_{P_L N}^G(σ′ ⊗ φ′ ⊗ 1).
3. If P′ := P_L N is a parabolic subgroup of G with Langlands factors M′A′N′ (**PIN OWED**: standard, Knapp 1986 Ch. VII/V, paywalled), then (F1) says the big representation is a finite sum of irreducible tempered representations.
4. A subrepresentation of a finite direct sum of irreducibles is again a finite direct sum: its commutant is a corner p·I·p of a finite-dimensional algebra.

Limits of discrete series are covered, because they are irreducible tempered. HSY Theorem 2.1, `r12_tempered/arxiv_1705.02088.txt:507-518`: "The following result is Theorem 1.1 in [23]. … the representation π^G_{λ,R+,χ} is • nonzero if and only if … • irreducible and tempered in that case."

**Pin KZ. The converse direction (every irreducible tempered rep is a constituent). SECONDARY-quoting-numbered.** HSY Theorem 2.2, `r12_tempered/arxiv_1705.02088.txt:609-618` (VT-I):
> "Theorem 2.2 (Knapp–Zuckerman). Every tempered representation of G is basic."
> "This is Corollary 8.8 in [23]. In Theorem 14.2 in [24], Knapp and Zuckerman complete the classification of tempered representations by showing which basic representations are irreducible and tempered. (These are the ones with nondegenerate data and trivial R-groups; see Sections 8 and 12 in [24] for details on these conditions)."

"Basic" means Ind_P^G(limit-of-d.s. ⊗ e^ν ⊗ 1_N) with P cuspidal, `:596-607`. [23] and [24] are KZ Annals 116 (1982) 389–455 and 457–501 (`:2988-2995`).

Originals: **PIN OWED** (JSTOR, paywalled).
- `r17/crossref_10.2307_2007066.json`: KZ I, Ann. of Math. 116 (1982), p. 389.
- `r17/crossref_10.2307_2007019.json`: KZ II, p. 457.
- `r17/crossref_10.2307_2007089.json`: typesetter's correction, 119 (1984), p. 639.

The open-access PNAS announcement (Knapp–Zuckerman, PNAS 73 (1976) 2178–2180, DOI 10.1073/pnas.73.7.2178, PMCID PMC430485; `r17/crossref_10.1073_pnas.73.7.2178.json`) was **not retrieved**: PMC and Europe PMC served captcha/"Just a moment" pages to curl. **PIN OWED (open, needs a browser fetch).**

## 4. Hypothesis check for the BST target (G = SO₀(2,5), or its covers)

- **(T) is unconditional.** BK II Lemma 2.3 and Remark 2.4 are stated for locally compact G. Lemma 4.3's proof uses only that N is amenable. So SO₀(2,5), Spin(2,5) and the universal cover are all covered, with D1 as the definition.
- **CCH class** (`r17/arxiv_1409.8654.txt:476-479`):
  > "we shall let G ⊆ GL(n, R) be a self-adjoint group which is also the group of real points of a connected (and necessarily reductive) algebraic group deﬁned over R. For brevity, we shall simply say that G is a real reductive group."

  SO₀(2,5) is the identity component of SO(2,5)(ℝ), not all of the real points. SO(2,5)(ℝ) is in the class. Passing between them uses BK II Remark 2.2 (finite index preserves temperedness, `:430-432`) and Mackey restriction to a finite-index subgroup, which preserves finiteness of the decomposition. That restriction step is **INFERENCE, not pinned**. Non-linear covers are **outside** CCH's class, so (F1) and (F2) are **not pinned** for them.
- **HSY class** (`r12_tempered/arxiv_1705.02088.txt:389-392`): "G will denote a connected, linear, real reductive Lie group with compact centre ZG . (This is the class of groups for which tempered representations were classified in [23, 24, 25].)" SO₀(2,5) qualifies.

## 5. Files

- `r17/arxiv_1409.8654.{pdf,txt,abs.html}`: Clare–Crisp–Higson (new).
- `r17/arxiv_1510.02650.{pdf,txt,abs.html}`: Afgoustidis (new, corroboration only).
- Reused from R12, not copied: `r12_tempered/arxiv_1706.10131.*` (BK II), `r12_tempered/bhv_KazhdanTotal.*`, `r12_tempered/arxiv_1705.02088.*` (HSY), `r12_tempered/R12_TEMPERED_PINS_draft.md`.
- `r17/crossref_*.json`: KZ I/II/correction, KZ PNAS 1976, Knapp 1986 (DOI 10.1515/9781400883974, ISBN 9781400883974, PUP), and chapters VII (pp. 167–202), VIII (203–280) and XIV (515–625). `crossref_search_KZ.json` is the raw search.
- `r17/png/` contains 9 rendered pages. `r17/VISUAL_TRANSCRIPTIONS.txt` holds VT-A…VT-I.
- `r17/SHA256SUMS.txt`
