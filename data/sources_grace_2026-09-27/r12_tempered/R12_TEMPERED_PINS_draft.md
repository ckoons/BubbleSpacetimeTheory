# R12 pins: temperedness chain L²(SO₀(2,5)/K) → restriction to SO₀(2,4) → massless ladder reps (draft)

Grace lane, 2026-09-27. All paths are relative to this directory. Every quote is copied from a `.txt` produced by `pdftotext -layout` from a saved PDF. Where formulas were garbled, the page was rendered to `png/` and transcribed in `VISUAL_TRANSCRIPTIONS.txt` (VT-A … VT-F). No git.

## Verdict up front

| Link | Status |
|---|---|
| (1) L²(G/K) is tempered | **PINNED PRIMARY**, two independent routes: the Plancherel decomposition (Helgason, restated as eq. (28) and Theorem 3 in arXiv:2606.20290), and Benoist–Kobayashi II Prop. 3.1(2) with H = K, H′ = {e} |
| (2) Tempered for G ⇒ restriction to a closed H is tempered for H | **PINNED PRIMARY**. It is two numbered statements composed by transitivity: BHV Prop. F.3.4, then Prop. F.1.10, then Remark F.1.2(iv). Only "H closed" is needed; no unimodularity. BK II (line 112) also states it, but as an unnumbered intro bullet |
| (3) The massless ladder reps of SU(2,2) are not tempered, per helicity | **INFERENCE, all helicities.** The inference is built only from pinned PRIMARY lemmas plus a checked numeric ρ. **No primary source was found that states it directly.** For Δ = 1 it is supported by the singular infinitesimal character (Kobayashi–Ørsted, PRIMARY), but that alone does not decide temperedness |
| SL(2,R) calibration: the limits D₀^± (= "D₁^±") are tempered | **PINNED PRIMARY** (Hochs–Song–Yu Thm 2.1, quoting Knapp–Zuckerman Thm 1.1, and Sec. 3.7) |

**Consequence for the chain (INFERENCE):** by BK I Remark 2.6, only a μ-null set of non-tempered representations can occur in the direct integral of L²(SO₀(2,5)/K)|_H. So no massless ladder rep of any helicity occurs as a discrete summand, or on a set of positive measure, in the restriction of L²(G/K) to H.

---

## 0. Definitions of "tempered". Quote first, then match them.

Three definitions are in play. They agree in our setting (connected semisimple, finite center) by Cowling–Haagerup–Howe.

- **D1 (weak containment; the one we use).** BK II `arxiv_1706.10131.txt:425-428`, Definition 2.1:
  > "The unitary representation π is said to be tempered or G-tempered if π is weakly contained in the regular representation λG of G in L2 (G) i.e. if every matrix coefficient of π is a uniform limit on every compact subset of G of a sequence of sums of matrix coefficients of λG ."

  The same wording is in BK I `arxiv_1211.1203.txt:127-130`, Definition 2.3 ("The following definition is due to Harish-Chandra").
  Weak containment is defined in BHV `bhv_KazhdanTotal.txt:17758-17768`, Definition F.1.1:
  > "We say that π is weakly contained in ρ if every function of positive type associated to π can be approximated, uniformly on compact subsets of G, by finite sums of functions of positive type associated to ρ."
- **D2 (L^{2+ε}).** Hochs–Song–Yu `arxiv_1705.02088.txt:401-402`:
  > "A unitary irreducible representation π ∈ Ĝ is tempered if all of its K-finite matrix coefficients belong to L2+ ε (G) for all ε > 0."

  BK II Definition 2.5 ("almost L²") is the version for representations that need not be irreducible (VT-A).
- **D3 (Harish-Chandra Ξ bound).** BK II `arxiv_1706.10131.txt:471-478`, Proposition 2.6 (Cowling, Haagerup and Howe [8]). Transcribed in VT-A:
  > "Let G be a connected semisimple Lie group with finite center and π be a unitary representation of G. The following are equivalent: (i) the representation π is tempered, (ii) the representation π is almost L2, (iii) for every K-finite vectors v, w in Hπ, for every g in G, one has |⟨π(g)v, w⟩| ≤ Ξ(g)‖v‖‖w‖(dim⟨Kv⟩)^{1/2}(dim⟨Kw⟩)^{1/2}."

  Ξ is defined at `:463-467`, eq. (2.5): Ξ(g) = ⟨π₀(g)v₀, v₀⟩, with π₀ = Ind_{P_min}(1).
  The original is Cowling–Haagerup–Howe, J. reine angew. Math. 387 (1988) 97–110, DOI 10.1515/crll.1988.387.97 (`crossref_10.1515_crll.1988.387.97_CHH.json`). It is paywalled: **PIN OWED on the original. SECONDARY via BK II**, which cites "[8, Thms. 1, 2 and Cor.]".

**Match check.** D1 ⇔ D3 requires finite center. SU(2,2) (center Z₄), SO₀(2,4) and SO₀(2,5) all satisfy this. For U(2,2) = SU(2,2)·(central U(1)), use BK II Remark 2.4(2), `:445-451`:
> "When G is a product of two closed subgroups G = SZ with Z central, a unitary representation π of G is G-tempered if and only if it is S-tempered."

For finite covers, BK II Remark 2.2, `:430-432`, says temperedness is stable under passage to a finite-index subgroup. The **universal cover** of SU(2,2) has infinite center, so the Ξ criterion does not apply there as stated. We work on SU(2,2), where all the ladder reps (Δ = |h|+1, h ∈ ½Z) live (standard; see the caveat in Section 3).

## 1. L²(G/K) is tempered (Harish-Chandra Plancherel)

**Pin 1a. PRIMARY, open, numbered.** Ferreira–Hilgert–Mourão–Nunes, arXiv:2606.20290 (`arxiv_2606.20290.abs.html` title: "Fourier-Helgason transform as infinite geodesic time limit in geometric quantization").
- `arxiv_2606.20290.txt:65-68` (intro, eq. (1)):
  > "The Fourier–Helgason (FH) transform for a noncompact symmetric space G/K corresponds to the direct integral decomposition of the unitary representation of G on square integrable functions on G/K into irreducible principal series representations"
- `:1026-1037`, eq. (28). The formula is transcribed in VT-C:
  > L²(X, dx) = ∫_{a*₊} H_λ dλ/|c(λ)|², "where c is the Harish-Chandra c–function, with H_λ being given by the image of the Poisson transform defined on L²(B, db)".
- `:1051-1057`, Theorem 3 (Helgason):
  > "The FH transform is a unitary isomorphism and its inverse is given by … (31)". The source is cited there as Helgason [Hel08] Ch. III, Sec. 1.

Helgason's book itself is paywalled: **PIN OWED on Helgason. The pin above is PRIMARY for the statement as used.** H_λ is the spherical principal series Ind_{MAN}(1 ⊗ e^{iλ} ⊗ 1), realized on L²(B) with B = K/M.

**Pin 1b. PRIMARY. Temperedness follows directly, with no Plancherel needed.** BK II `arxiv_1706.10131.txt:610-617`, Proposition 3.1:
> "Let G be a semisimple Lie group with finitely many components such that the identity component Ge has finite center and H′ ⊂ H two closed subgroups of G. 1) If L2 (G/H) is G-tempered then L2 (G/H′) is G-tempered. 2) The converse is true when H′ is normal in H and H/H′ is amenable (for instance finite, compact, or abelian)."

Take H = K and H′ = {e}. Then L²(G/{e}) = L²(G) is tempered by D1, trivially, and K/{e} = K is compact. So L²(G/K) is tempered.

Cross-check: BK I Thm 4.1(a), `arxiv_1211.1203.txt:425-427` ("L2 (G/H) is tempered ⇐⇒ ρh (Y) ≤ ρq (Y) for any Y ∈ a", where a is a maximal split abelian subspace of **h**). For H = K we have a = 0, so the criterion holds trivially.

**Pin 1c. PRIMARY (direct integrals).** BK I `arxiv_1211.1203.txt:148-152`, Remark 2.6:
> "When a unitary representation π of G is a direct integral π = ∫⊕ πλ dµ(λ) of irreducible unitary representations πλ, the representation π is tempered if and only if the representations πλ are tempered for µ-almost every parameter λ."

## 2. Restriction of a tempered representation to a closed subgroup is tempered

Source: Bekka–de la Harpe–Valette, *Kazhdan's Property (T)*, the authors' open preprint dated February 23, 2007 (`bhv_KazhdanTotal.txt:1-3`), hosted at perso.univ-rennes1.fr/bachir.bekka/KazhdanTotal.pdf. The published CUP 2008 numbering was not checked against it: **numbering-match PIN OWED.**

- **Prop. F.3.4**, `bhv_KazhdanTotal.txt:18368-18370`:
  > "Let H be a closed subgroup of the topological group G, and let π and ρ be unitary representations of G such that π ≺ ρ. Then π|H ≺ ρ|H ."
- **Prop. F.1.10**, `:18018-18019`:
  > "Let G be a locally compact group, and let H be a closed subgroup of G. Then λG |H ≺ λH ."

  Remark F.1.11 (`:18064-18065`) adds the converse: "λG|H and λH are actually weakly equivalent".
- **Remark F.1.2(iv)**, `:17795-17796` (transitivity):
  > "For unitary representations π, ρ, and σ of G, weak containments π ≺ ρ and ρ ≺ σ imply π ≺ σ."

**Composition.** π ≺ λ_G ⇒ π|_H ≺ λ_G|_H (F.3.4) ≺ λ_H (F.1.10) ⇒ π|_H ≺ λ_H (F.1.2(iv)). That is, π|_H is H-tempered in the sense of D1.
- **Hypotheses:** G is locally compact and H is **closed**. No unimodularity is assumed.
- SO₀(2,4) ⊂ SO₀(2,5) is closed. So is Spin(2,4) = SU(2,2) ⊂ Spin(2,5).
- BK II also states this, unnumbered, at `arxiv_1706.10131.txt:112`: "Tempered representations are closed under induction, restriction, tensor product, and direct integral of unitary representations." Induction is also numbered there: Lemma 2.3, `:434-442`.

## 3. Massless (ladder) representations of SU(2,2), per helicity

### 3a. What was searched and not found (honest negatives)

**No open source was found that states "the ladder/massless representations of SU(2,2) are (not) tempered" or "… are (not) limits of holomorphic discrete series".** Searched and saved:
- Kobayashi–Ørsted I–III (`arxiv_math_0111083/5/6.txt`): grep "tempered" gives 0 hits in the representation-theoretic sense.
- Benoist–Kobayashi I–II.
- Kobayashi's Varna lecture 1212.6871.
- Kobayashi–Mano 0712.1769; Hilgert–Kobayashi–Möllers 1009.4549; Kobayashi 1001.0224; Kobayashi math/0607002.
- 2604.20566, 2305.15892 (EHW-type classification papers): no "tempered".
- 2206.07407; Möllers 1205.5171; Neeb–Ørsted math/0006075.
- From r11: Fernando–Günaydin 0908.3624, Gazeau–Pejhan–Todorov 2601.18433, Todorov 1905.13009.

The "general criterion: a unitary highest weight module is tempered iff it is a (limit of) holomorphic discrete series" was **not found as a numbered statement** in any open source. Knapp–Zuckerman (Ann. Math. 1982), Wallach (Trans. AMS 251, 1979), EHW 1983 and Knapp–Speh (JFA 1982, the unitary dual of SU(2,2)) are paywalled: **PIN OWED on all four.**

**Two naming traps** (quotes from r11/cand):
- `../r11/cand/arxiv_0908.3624.txt:302-304`:
  > "These are simply the doubleton representations of SU (2, 2). They were referred to as ladder (or most degenerate discrete series) unitary representations by Mack and Todorov"

  "Most degenerate discrete series" is physics naming. It is **not** Harish-Chandra's discrete series, and must not be read as "tempered".
- `../r11/cand/arxiv_2601.18433.txt:1325-1327`:
  > "the physically relevant discrete series UIRs are precisely the symmetric cases Π±p=s,q=s … that lie at the lower limit of the discrete series"

  These are discrete series of the **de Sitter group Sp(2,2) (Spin(1,4))**, the restriction target. They are not of SU(2,2). "Lower limit of the discrete series" there says **nothing** about SU(2,2) temperedness.

### 3b. Pinned ingredients (PRIMARY) used by the inference

- **P1** (Ξ criterion): BK II Prop. 2.6(iii), quoted in Section 0 (VT-A).
- **P2** (upper bound on Ξ): BK II `arxiv_1706.10131.txt:727-729`, in the proof of Prop. 3.7, unnumbered display citing Knapp Prop 7.15 (VT-B):
  > "Ξ(e^Y) ≤ M0 (1 + ‖Y‖)^d e^{−ρg(Y)/2} for all Y in a"

  Here ρ_g(Y)/2 = the usual ρ(Y), because BK define ρ_V(Y) = Trace_{V+}(dτ(Y)) at `arxiv_1211.1203.txt:236`, eq. (3.1). **The display is in a proof, not a numbered statement.** The numbered original is Knapp, *Representation Theory of Semisimple Groups*, Prop. 7.15, which is paywalled: **PIN OWED.**
- **P3** (limits of DS are tempered): Hochs–Song–Yu `arxiv_1705.02088.txt:509-529`, Theorem 2.1 = Knapp–Zuckerman Thm 1.1 (VT-D): "nonzero if and only if (λ, α) ≠ 0 for all simple … compact roots α; irreducible and tempered in that case. … The limits of discrete series representations are the nonzero representations occurring in the above theorem."
- **P4** (every tempered rep is basic): `arxiv_1705.02088.txt:609-610`, Theorem 2.2 (Knapp–Zuckerman):
  > "Every tempered representation of G is basic." ("This is Corollary 8.8 in [23].")
- **P5** (scalar Wallach set; the Δ = 1 ladder is the first nonzero discrete Wallach point, realized on the rank-1 orbit, i.e. the light cone): Möllers `arxiv_1205.5171.txt:213-219, 253-256` (VT-F):
  > "W = {0, d/2, …, (r−1)d/2} ∪ ((r−1)d/2, ∞)"

  For SU(2,2): r = 2, d = 2, so W = {0, 1} ∪ (1, ∞).
  > "Rossi–Vergne [49] showed that the scalar type unitary highest weight representation corresponding to the Wallach point λ ∈ W can be realized on a space of L2-functions on the orbit Ok for λ = k d/2 …"
- **P6** (infinitesimal character of the O(p,q) minimal/ladder rep): Kobayashi–Ørsted I `arxiv_math_0111083.txt:784-800`, Theorem 3.6.1(2),(4) (VT-E):
  > "In the Harish-Chandra parametrization, the Z(g)-infinitesimal character of ϖp,q is given by (1, (p+q)/2 − 2, (p+q)/2 − 3, …, 1, 0)."

  Item 4 gives irreducibility and unitarity for p+q even with (p,q) ≠ (2,2). For (4,2) this is (1, 1, 0): **singular**. Note the scope from `:77`: "minimal representations if p + q ≥ 8 (i.e. the annihilator is the Joseph ideal)". For p+q = 6, ϖ^{4,2} is the ladder rep, but KO do not call it "minimal" in the Joseph-ideal sense.
- **Input from r11** (lowest K-type): massless ⇔ (d; j₁, j₂) with j₁j₂ = 0 and d = j₁+j₂+1. This is Mack 1977 class (5), pinned in `../r11/R11_PINS_draft.md` lines 43, 64, 91. So the lowest K-type of helicity h is (|h|, 0) or (0, |h|), with Δ = |h|+1.

### 3c. The inference (INFERENCE; instrument `toy/rho_su22_check.py`, output `toy/rho_su22_check.out`)

1. Let γ₁, γ₂ be the two strongly orthogonal noncompact roots of su(2,2), and S = SU(1,1)_{γ₁} × SU(1,1)_{γ₂}. Then A = {a_t = exp(t₁X_{γ₁} + t₂X_{γ₂})} ⊂ S.
2. **ρ on a.** The numeric instrument gives ρ(a_t) = 3t₁ + t₂ for t₁ ≥ t₂ ≥ 0, in the same normalization in which SU(1,1) has ρ(t) = t. Output: `SU(2,2) … t=(1,0) rho=3.0; (1,1) 4.0; (2,1) 7.0; SU(1,1) rho=1`. This matches restricted roots ±2t_j (mult 1) and ±t₁±t₂ (mult d = 2). By P2, Ξ(a_{(t,0)}) ≤ M₀(1+t)^d e^{−3t}.
3. **Coefficient along a_t.** A weight vector v of the lowest K-type of a unitary highest weight module is killed by p₋, so it is an S-extremal vector with SU(1,1)-weights (w₁, w₂). The S-module it generates is D_{w₁} ⊠ D_{w₂}. By the elementary SU(1,1) computation (g = [[a, b], [b̄, ā]], a = cosh t, acting on the constant function), |⟨π(a_t)v, v⟩| = (cosh t₁)^{−w₁}(cosh t₂)^{−w₂}. *(PIN OWED for a printed source of this formula.)*
4. **Weights for helicity h.** The lowest K-type is Sym^{2|h|}(C²) of one SU(2) (spin |h|) with Δ = |h|+1. Its weight vectors carry (w₁, w₂) = (Δ + j₃, Δ − j₃), with j₃ ∈ {−|h|, …, |h|}. So w₁ + w₂ = 2Δ, and **min w = Δ − |h| = 1 for every helicity.** (Derived from the U(2,2) Fock-model K-types, highest weight (−½,−½ | 2|h|+½, ½). This is our arithmetic, not a pin.)
5. **Violation of P1.** Take v with w₁ = 1 and g = a_{(t,0)}. Then |⟨π(g)v, v⟩| = (cosh t)^{−1} ≥ e^{−t}. But the (iii) bound is ≤ C(1+t)^d e^{−3t}, which fails for large t. **So the ladder rep is not tempered, for every helicity h.**
6. **Internal calibration.** The same computation for scalar type λ gives "tempered ⇔ λ ≥ 3 = p−1 (genus p = 4)". Here λ > 3 is exactly the scalar holomorphic discrete series and λ = 3 the limit. On SU(1,1) it gives "tempered ⇔ λ ≥ 1", with D_1 = the limit of DS, tempered (agrees with P3/Section 4). Both reproduce known endpoints. The massless tower sits at "Δ-weight 1 in one direction", far below 3.

### 3d. Per-helicity table

| helicity | Δ | lowest K-type (j₁, j₂) | tempered for SU(2,2)? | source file:line | tier |
|---|---|---|---|---|---|
| 0 (scalar, ladder / "minimal") | 1 | (0, 0) | **No.** Coefficient (cosh t₁ cosh t₂)^{−1} vs Ξ ≲ e^{−(3t₁+t₂)}. Also singular inf. char. (1, 1, 0) (P6) | 3c; P1 `arxiv_1706.10131.txt:471-478`; P2 `:729`; P5 `arxiv_1205.5171.txt:216,253-256`; P6 `arxiv_math_0111083.txt:796-797` | INFERENCE (on PRIMARY lemmas); singularity PRIMARY |
| ±½ (Weyl) | 3/2 | (½, 0) / (0, ½) | **No.** min w = 1 (weights (2,1), (1,2)) | 3c + r11 Mack class (5) | INFERENCE |
| ±1 (Maxwell) | 2 | (1, 0) / (0, 1) | **No.** min w = 1 (weights (3,1), (2,2), (1,3)) | 3c | INFERENCE |
| ±s, general | s+1 | (s, 0) / (0, s) | **No.** min w = 1 for all s | 3c | INFERENCE |

**Referee caveats on 3c:**
- (i) The step-4 weight list depends on the coroot normalization H_γ. It was cross-checked two ways: the scalar case gives w = (1, 1), i.e. Wallach λ = 1 (P5), and w₁ + w₂ = 2Δ reproduces Δ = |h|+1. If one used the "half" normalization instead, min w would be |h|/2 + 1. That still gives < 3 for |h| ≤ 3, but would flip at |h| ≥ 4. So the high-helicity rows rest on the step-4 normalization. **The toy checks ρ, not the weights.** A weight-level toy is owed before this becomes a row.
- (ii) Half-integer helicities are representations of SU(2,2) = Spin(2,4), not of SO₀(2,4) (−1 acts by (−1)^{2h}). The chain must then be run in Spin(2,4) ⊂ Spin(2,5). Section 2 is unaffected.
- (iii) Step 3's use of P1 needs only one K-finite vector. That is legitimate: P1 quantifies over all K-finite v, w.

## 4. SL(2,R) calibration: limits of discrete series are tempered

- `arxiv_1705.02088.txt:1150-1153` (Sec. 3.7):
  > "This group G has three kinds of tempered representations: the (holomorphic and antiholomorphic) discrete series, the limits of the discrete series, and the (spherical and nonspherical) unitary principal series."

  At `:1195`: "For the limits of the discrete series D0± …".
  General statement: P3 (Thm 2.1, "irreducible and tempered"). **PRIMARY** (numbered via the quoted KZ Thm 1.1; the SL2 sentence itself is unnumbered).
- Realization: Tensor-classification paper, `arxiv_2104.01475.txt:491-493` (Sec. 3.2.3, unnumbered bullet, (g,K)-module level):
  > "I0,1 = D0+ ⊕D0− decomposes into the holomorphic and anti-holomorphic limits of discrete series representations"
- Independent route (PRIMARY lemmas plus inference): BHV Example E.1.8(iii), `bhv_KazhdanTotal.txt:17398-17421`, defines π^±_{it} = Ind_P χ^±_t. BK II Lemma 2.3 says induction from P, which is amenable (BK II Remark 2.4(1)), is tempered. So π^−_0 is tempered, and its subrepresentations D₀^± are tempered by BHV Remark F.1.2(iii)+(iv).
- **Notation.** "D₁^±" in the brief = D₀^± here: lowest K-type ±1, Harish-Chandra parameter 0.

## Files

- **Pinned:** `arxiv_1211.1203`, `arxiv_1706.10131`, `bhv_KazhdanTotal`, `arxiv_2606.20290`, `arxiv_1705.02088`, `arxiv_2104.01475`, `arxiv_1205.5171`, `arxiv_math_0111083` (all as .pdf + .txt, with .abs.html for arXiv), and `crossref_10.1515_crll.1988.387.97_CHH.json`.
- **Searched, no pin:** `arxiv_math_0111085/6`, `arxiv_1212.6871`, `arxiv_0712.1769`, `arxiv_1001.0224`, `arxiv_1009.4549`, `arxiv_2603.11036`, `arxiv_2505.22607`, `arxiv_2604.20566`, `arxiv_2305.15892`, `arxiv_2206.07407`, `arxiv_math_0607002`, `arxiv_math_0111172`, `arxiv_math_0006075`, `arxiv_math_9908031`, `arxiv_2210.13146`, `arxiv_2409.09036`, `arxiv_0707.0874`, `arxiv_1308.1863`.
- **Other:** `VISUAL_TRANSCRIPTIONS.txt`, `png/`, `toy/rho_su22_check.py` (+ `.out`), `SHA256SUMS.txt`.

**PIN OWED list:**
- Helgason (GGA/GASS, Ch. III)
- Cowling–Haagerup–Howe 1988 (original)
- Knapp Prop. 7.15 (Ξ bound)
- Knapp–Zuckerman 1982 Thm 1.1 / Cor. 8.8 (originals)
- BHV CUP numbering match
- A printed source for the SU(1,1) coefficient (cosh t)^{−w}
- A primary statement of (non-)temperedness of the SU(2,2) ladder reps: Knapp–Speh 1982 JFA or EHW 1983 are the likeliest
