# R13 pins: are the massless (ladder) unitary highest-weight representations of SU(2,2) tempered? (draft)

Grace lane, 2026-09-27 (clock 12:18 EDT). Paths are relative to this directory unless prefixed `../r12_tempered/` or `../r11/`. Every quote is from a `.txt` made by `pdftotext -layout` from a PDF saved here. Garbled displays were rendered to `png/` and transcribed in `VISUAL_TRANSCRIPTIONS.txt` (VT-1 … VT-3). No git.

## Verdict up front

**Decided, for every helicity at once: NOT tempered.** The result is carried by three numbered primary theorems and one elementary check:

1. **Bai–Hunziker, Prop. 3.2 [BH15]** (VT-1). For a unitary highest-weight module L(λ), set k(λ) = −(λ, β^∨)/c. If 0 ≤ k ≤ r−1, then AV(L(λ)) is the closure of O_k and GKdim = dim O_k.
   - For su(2,2): r = 2, c = 1, (ρ, β^∨) = 3.
   - The massless tower has (λ, β^∨) = −1 for every helicity. So k = 1, AV = closure of O_1 (dimension 3), and GK dimension 3.
   - The complex orbit of O_1 is [2,1,1], the minimal nilpotent orbit of sl(4,ℂ). Source: Bai–Hunziker–Xie–Zierau, Table 2 (VT-3).
2. **Schmid–Vilonen, Theorem 1.4.** The associated cycle equals the wave front cycle under the Kostant–Sekiguchi correspondence, and corresponding orbits lie in the same complex orbit. So the WF cycle of every massless representation is a positive multiple of one real orbit inside the complex orbit [2,1,1].
3. **B. Harris, Theorem 1.1 / Corollary 1.2.** An orbit that occurs in the WF cycle of a tempered representation has a compact Levi factor of its centralizer, modulo Z(G). Equivalently, it does not meet any proper real Levi subalgebra.
   - The real orbits in [2,1,1] ⊂ su(2,2) fail this test. The Levi factor is ≅ u(1,1), with trace-form signature (+2, −2). This is checked by `toy/harris_levi_su22.py` and agrees with the signed-Young-diagram rule in Harris Example 5.1.
   - Calibration: the holomorphic [2,2] orbit, which carries the holomorphic discrete series, passes the test (Levi ≅ su(2), negative definite).

Nothing in the chain depends on a coroot or weight normalization, beyond the canonical pairing (λ, β^∨). The |h| ≥ 4 caveat from R12 is resolved (see the closing section).

| Route in the brief | Result |
|---|---|
| A. WF/AV necessary condition for temperedness | **FOUND, PRIMARY, numbered.** Harris arXiv:1209.4123 Thm 1.1 and Cor 1.2 (a Vogan conjecture, proved). HHO Thm 1.2 (reused) gives WF = AC(orbital support) but is not needed for the verdict. |
| B. "Tempered unitary highest-weight ⇔ (limit of) holomorphic discrete series" | **Not found as a numbered statement** in any open source (same as R12). **Not needed.** |
| C. AV/GK of unitary highest-weight modules | **FOUND.** BH15 Prop. 3.2, restated by the same authors in arXiv:2409.16555 (the original in Sci. China Math. 58 (2015) is paywalled: PIN OWED on the original). The orbit chain, dimensions and complex labels are in arXiv:2402.08886 (1.1)–(1.2), (3.5) and Table 2. Scalar cross-check: Kobayashi–Ørsted II Lemma 4.4. |
| D. Direct statement "minimal/ladder representations are not tempered" | **Only unnumbered:** Salmasian's intro sentence "singular representations … form a large class of non-tempered representations". It is context, not a pin. |

---

## 0. Definitions, quoted first

**Tempered.**
- HHO `../r12_tempered/arxiv_1308.1863.txt:98-100`:
  > "The irreducible representations occurring in the direct integral decomposition of L2 (G) are called irreducible, tempered representations of G"

  and `:106-107`:
  > "we say π is weakly contained in the regular representation if supp π ⊂ Ĝtemp."
- Benoist–Kobayashi II Def. 2.1 (weak containment), and its equivalence with almost-L² and the Ξ bound via Cowling–Haagerup–Howe: quoted in `../r12_tempered/R12_TEMPERED_PINS_draft.md` Section 0 (D1–D3). This is the notion Harris uses. Harris works with irreducible admissible π (`arxiv_1209.4123.txt:19-20`) and Rossmann's orbit attached to "each irreducible, tempered representation" (`:76-77`).

**Associated variety and GK dimension.** Bai–Hunziker `arxiv_2409.16555.txt:216-226`:
> "The Gelfand–Kirillov dimension of M is defined by GKdim M = lim_{n→∞} log dim(Un(g)M0)/log n. The associated variety of M is defined by AV(M) := {X ∈ g∗ | f(X) = 0 for all f ∈ AnnS(g)(gr M)}. These two definitions are independent of the choice of M0, and dim V(M) = GKdim M (e.g., [NOT01])."

Also `arxiv_2402.08886.txt:52-58`:
> "When L(λ) is a highest weight Harish-Chandra module for GR, the associated variety is contained in (g/q)∗ ≃ p+. It is well-known that the closures of the K-orbits in p+ form a chain (1.1) {0} = O0 ⊊ O1 ⊊ · · · ⊊ Or = p+, where r is the real rank of gR … It follows that (1.2) AV(L(λ)) = Ok, for some k = 0, 1, . . . , r."

And `:699-700`, eq. (3.5):
> "Ok = K · (Xγ1 + · · · + Xγk), k = 1, 2, . . . , r, where Xγ is a root vector for γ."

**Associated cycle and wave front cycle.** Schmid–Vilonen `arxiv_math_0005305.txt:54-57`, eq. (1.1):
> "this 'associated cycle' becomes a linear combination Ass(π) = Σ aj [Op,j] (aj ∈ Z≥0) of fundamental cycles of K-orbits Op,j in N∗ ∩ p∗, all of the same dimension."

And `:66-71`, eq. (1.2):
> "WF(π) = Σ bj [OgR,j] (bj ∈ C) … We shall call WF(π) the 'wave front cycle' of π. Its support coincides with the wave front set of the distribution Θπ at the identity, as was proved by Rossmann".

**Wave front set of a unitary representation** (analytic definition). HHO `../r12_tempered/arxiv_1308.1863.txt:388-391`:
> "we define the wave front set of π … by WF(π) = ⋃_{u,v∈V} WFe(π(g)u, v)".

**Real distinguished.** Harris `arxiv_1209.4123.txt:37-40`:
> "we define a nilpotent orbit for a real reductive algebraic group to be real distinguished if it does not meet a proper Levi subalgebra. By Levi subalgebra, we mean the Levi factor of a real parabolic subalgebra."

And `:56-58`:
> "If Oν is a nilpotent orbit, then one checks that ZG(ν) is compact modulo Z(G) iff Oν is a real distinguished nilpotent orbit".

## 1. Pin H: Harris, the temperedness obstruction (route A). PRIMARY, numbered

`arxiv_1209.4123` (B. Harris, "Tempered Representations and Nilpotent Orbits", arXiv v2 2015; abs page carries no journal-ref — published venue NOT verified here). Abstract page: `arxiv_1209.4123.abs.html`.

- **Theorem 1.1**, `arxiv_1209.4123.txt:23-26`:
  > "Suppose O is an orbit contained in WF(π) for a tempered representation π, let ν ∈ O, and let L be a Levi factor of ZG(ν). Then L/Z(G) is compact."
- `:26-28`:
  > "This theorem was conjectured by David Vogan. It makes precise the widely held intuition that orbits occuring in the wave front cycles of tempered representations are necessarily large."
- **Corollary 1.2**, `:61-63`:
  > "If O ⊂ g∗ is a nilpotent coadjoint orbit occurring in the wave front cycle of a tempered representation, then O does not meet m∗ for any proper Levi subalgebra m ⊂ g."
- **Scope**, `:100-102`:
  > "We only state them in the case of real, reductive algebraic groups because we use results of [10], [11], and [12]".

  SU(2,2) and U(2,2) are real reductive algebraic groups.
- **Example 5.1 (U(2,2)), unnumbered example**, `:445-449`:
  > "Nilpotent orbits in U(2, 2) can be parametrized by signed Young diagrams of signature (2, 2) (see page 140 of [3]). A nilpotent orbit of U(2, 2) is real distinguished iff it corresponds to a signed Young diagram for which any two rows of equal length begin with the same sign."

  And `:457-463`:
  > "the nilpotent orbits corresponding to discrete series for U(2, 2) are precisely the real distinguished nilpotent orbits of U(2, 2). … That the associated variety of the representation corresponds to the wave front cycle of the representation under the Kostant-Sekiguchi correspondence is a deep result of [13]." ([13] = Schmid–Vilonen.)

## 2. Pin SV: associated cycle = wave front cycle. PRIMARY, numbered

`arxiv_math_0005305` (Schmid–Vilonen, Ann. of Math. 151 (2000) 1071–1118).
- **Scope**, `:24`: "we consider a linear, reductive Lie group GR". SU(2,2) ⊂ SL(4,ℂ) is linear.
- `:74-76`, eq. (1.3):
  > "K\(N∗ ∩ p∗) ←→ GR\iN∗R was established by Sekiguchi [Se] and Kostant (unpublished)."
- **Theorem 1.4**, `:78-79`:
  > "The associated cycle Ass(π) coincides with the wave front cycle WF(π) via the correspondence (1.3)."

  And `:81-82`:
  > "it implies that the coefficients bj of the wave front cycle are nonnegative integers."
- `:1510-1513` (Sec. 6, lead-in to Theorem 6.3):
  > "Sekiguchi [Se] and Kostant (unpublished) have described a bijective correspondence between the K-orbits in N ∩ p on one hand, and the GR-orbits in N ∩ igR on the other. Orbits that correspond to each other lie in the same G-orbit, and thus have the same dimension."

## 3. Pin BH: the AV/GK of every unitary highest-weight module (route C)

- **Bai–Hunziker Prop. 3.2 [BH15]**, restated by the same authors in `arxiv_2409.16555.txt:259-277`. The display is garbled, so see **VT-1** (rendered `png/arxiv_2409.16555_p-06.png`). Key lines:
  > "Denote k = k(λ) := −(λ, β∨)/c. Then (1) If k > r − 1, we have GKdim L(λ) = rz_{r−1} = ½ dim(G/K). (2) If 0 ≤ k ≤ r − 1, then k is a non-negative integer and GKdim L(λ) = k((ρ, β∨) − (k − 1)c) = kz_{k−1} = dim O_{k(λ)}. The associated variety of L(λ) is O_{k(λ)}."

  Tier: PRIMARY as the authors' own restatement. **PIN OWED** on the original (Bai–Hunziker, Sci. China Math. 58 (2015) 2489–2498, DOI 10.1007/s11425-014-4968-y, paywalled).
- **Setup and conventions**, `arxiv_2409.16555.txt:54-59`:
  > "Let β denote the unique maximal noncompact root of ∆+. Now choose ζ ∈ h∗ so that ζ is orthogonal to ∆(k) and (ζ, β∨)=1. … By letting the nilradical act by zero, we may consider F(λ) as a module of the parabolic subalgebra q = k + p+. Then we define: N(λ) = U(g) ⊗U(q) F(λ). Let L(λ) denote the irreducible quotient of N(λ)".
- **Constants**, Table 1 from [EHW83] (VT-2): su(p, n−p) has r = min{p, n−p}, c = 1, (ρ, β^∨) = n−1. For su(2,2): r = 2, c = 1, (ρ, β^∨) = 3.
- **Orbit data**, `arxiv_2402.08886` Table 2 (VT-3):
  > "su(p, q): dim(Ok) = k(p + q − k); label of O^C_k = [2^k, 1^{p+q−2k}]."

  For (2,2): O_1 has dimension 3 and complex label [2,1,1] (the minimal orbit of sl₄). O_2 = p⁺ has dimension 4 and label [2,2].
- **Holomorphic discrete series have AV = p⁺**, Remark 3.2 in `arxiv_2402.08886.txt:754` (VT-3):
  > "If X is an irreducible generalized Verma module … (as in … the case of holomorphic discrete series representations), then … AV(X) = O_r = p+."
- **Independent cross-check, h = 0 only.** Kobayashi–Ørsted II `../r12_tempered/arxiv_math_0111085.txt:277-284`:
  > "M0,0(p, q; C) \ {O} is the unique KC ≃ O(p, C) × O(q, C)-orbit of dimension p + q − 3. … Lemma 4.4. The associated variety Vg(ϖK^{p,q}) equals M0,0(p, q; C)."

  For (p,q) = (4,2) this gives dimension 3 = dim O_1.

## 4. The massless tower in BH coordinates (INFERENCE; instrument `toy/helicity_to_BH.py`, output `.out`)

- **Input from r11 (PINNED there).** Massless means (d; j₁, j₂) with j₁j₂ = 0 and d = j₁+j₂+1. This is Mack 1977 class (5): `../r11/R11_PINS_draft.md`.
- **Coordinates.** Use the compact Cartan of u(2,2), λ = (a₁,a₂ | b₁,b₂). The p⁺-roots are e_i − f_j, and β = e₁ − f₂. The algebra is simply laced with |root|² = 2, so β^∨ = β and (λ, β^∨) = a₁ − b₂.
- **Spins.** j₁ = (a₁−a₂)/2 and j₂ = (b₁−b₂)/2. These are fixed by dim = 2j+1 of the SU(2) factors, so there is no normalization freedom.
- **Energy.** E is the element of the center of k that acts by +1 on p⁻, which is the energy-raising part. It is unique on su(2,2): if two such elements existed, their difference would be central in k and kill p, so it would be central in the semisimple g, hence zero. This matches the physics normalization, where P_μ raises d by exactly one. So E(λ) = −(a₁+a₂−b₁−b₂)/2 = d on the lowest K-type.
- **Result.** (λ, β^∨) = −d + j₁ + j₂. For the massless tower this is **−1 for every helicity**, so k = 1, z = z₁ = 2, AV = closure of O_1, and GKdim = 3.
- **Toy check.** The toy runs h = 0, ±½, …, ±6 and gets PASS on all 25 rows.
- **Controls.**

  | Case | (λ, β^∨) | GK |
  |---|---|---|
  | trivial | 0 | 0 |
  | scalar d = 2 | −2 | 4 |
  | Mack boundary d = j₁+j₂+2 | ≤ −2 | 4 |
  | holomorphic DS | < −3 | 4 |

  So among nontrivial unitary highest-weight modules of SU(2,2), **exactly the massless tower has GK < 4**. This agrees with the scalar Wallach set {0,1} ∪ (1,∞), which was pinned in R12 (P5).

## 5. Orbit test (INFERENCE on Harris Thm 1.1; instrument `toy/harris_levi_su22.py`, output `.out`)

**Rank-one nilpotents in su(2,2).** Every rank-one nilpotent X in su(2,2) = {A : A*J + JA = 0, tr A = 0} with J = diag(1,1,−1,−1) has JX anti-Hermitian of rank 1. So JX = i t v v* with t real, v ≠ 0 and v*Jv = 0; the trace condition forces the null condition. By Witt's theorem U(2,2) is transitive on nonzero null vectors, so there are **exactly two** such real orbits, t > 0 and t < 0. The central U(1) acts trivially under Ad, so these are also the SU(2,2)-orbits. Both are in the complex orbit [2,1,1].

For each X the toy builds an sl₂-triple (X, H, Y), computes l = z(X, H, Y), and tests whether tr(AB) is negative definite on l. That is the compactness test for a Lie subalgebra of the semisimple su(2,2).

| case | Jordan type | dim l | tr(AB) signature | l compact | Harris test |
|---|---|---|---|---|---|
| min_plus (t > 0) | [2,1,1] | 4 | (+2, −2) | no | **fails** |
| min_minus (t < 0) | [2,1,1] | 4 | (+2, −2) | no | **fails** |
| hol22 (both rows same sign) | [2,2] | 3 | (0, −3) | yes (su(2)) | passes |
| mixed22 | [2,2] | 3 | (+2, −1) | no (su(1,1)) | fails |

These agree with Harris's Example 5.1 rule.
- [2,1,1] with signature (2,2) forces its two rows of length 1 to carry opposite signs, so it is not real distinguished.
- The [2,2] diagram whose rows both begin with the same sign is real distinguished. That is the orbit of the holomorphic discrete series, AV = p⁺, and it passes as it must.

*PIN OWED:* two standard facts, the signed-Young-diagram parametrization (Collingwood–McGovern Thm 9.3.3) and "Levi factor of Z_g(X) = z_g(X, H, Y)" (Collingwood–McGovern Lemma 3.7.3 / Barbasch–Vogan), are used only through the toy and Harris's example. The Witt-theorem argument above gives the orbit count without Collingwood–McGovern.

## 6. The chain, per helicity

For any massless π_h (h ∈ ½ℤ), realized on SU(2,2), a linear real reductive algebraic group. U(2,2) works equally well, since Benoist–Kobayashi II Remark 2.4(2) (pinned in R12) says temperedness is unchanged by a central U(1).

1. AV(π_h) = closure of O_1, which has dimension 3, and GKdim = 3. **[BH15 Prop 3.2 + Table 1; Section 4 arithmetic]**
2. So Ass(π_h) = a[O_1] with a ≥ 1, since the open orbit in the support has positive multiplicity. **[SV (1.1)]**
3. Therefore WF(π_h) = a[O_R], where O_R is the Sekiguchi image of O_1, a real orbit inside the complex orbit of O_1, which is [2,1,1]. **[SV Thm 1.4 + Sec. 6 sentence; BHXZ Table 2]**
4. Every real orbit in [2,1,1] ∩ su(2,2) has a noncompact Levi factor of its centralizer, u(1,1). **[Section 5 toy; Harris Ex. 5.1 rule]**
5. By Harris Theorem 1.1 (equivalently Corollary 1.2), π_h is **not tempered**. **[Harris]**

This holds for every h. The chain never uses the value of h, only k(λ) = 1.

**Consequence for R12 link 3.** This replaces the R12 INFERENCE (the Ξ-decay argument) with a chain of numbered primary theorems. The R12 verdict "not tempered, all helicities" is **confirmed**.

## 7. Negatives and context (honest)

- **Route B.** No open numbered statement of "tempered unitary highest-weight ⇔ holomorphic discrete series or a limit of them" was found. Knapp–Okamoto (JFA 1972), Knapp–Zuckerman, EHW 1983 and Knapp–Speh are paywalled. **PIN OWED**, and not needed.
- **Route D.** Salmasian, `arxiv_math_0504363.txt:59-61` (introduction, unnumbered):
  > "Representations which correspond to degenerate classes are called singular representations. They form a large class of non-tempered representations".

  Context only.
- **HHO Thm 1.2** (`../r12_tempered/arxiv_1308.1863.txt:120-122`: "If G is a real, reductive algebraic group and π is weakly contained in the regular representation of G, then SS(π) = WF(π) = AC(O-supp π)"). It is consistent with the verdict but is not used. Turning it into a verdict would need dimension facts about asymptotic cones, and the AC of an elliptic orbit can drop dimension, as the holomorphic discrete series shows.
- **Searched, no pin:**
  - arXiv:2203.14784 (holomorphic discrete series in L²(G/N, ψ))
  - 1707.02565, 2408.07951, 1909.00705, 2005.11536, 2205.05362, 1307.0606 (GK/AV of highest-weight modules; 1909.00705 Prop. 2.3 repeats BH15)
  - 0712.4375 (Neeb)
  - 2304.05663, 1212.3411 (small representations)
  - math/0210371 (He)
  - 2105.11027
  - 1610.06202
  - 1702.04841 (small orbits for Spin groups)

## Files

- **Pinned:**
  - `arxiv_1209.4123` (Harris)
  - `arxiv_math_0005305` (Schmid–Vilonen)
  - `arxiv_2409.16555` (Bai–Hunziker)
  - `arxiv_2402.08886` (Bai–Hunziker–Xie–Zierau)
  - `arxiv_math_0504363` (context only)
  - Reused from `../r12_tempered/`: `arxiv_1308.1863` (HHO) and `arxiv_math_0111085` (KO II)

  Each is saved as .pdf, .txt and .abs.html.
- **Instruments:** `toy/harris_levi_su22.py` + `.out`, and `toy/helicity_to_BH.py` + `.out`.
- **Transcriptions:** `VISUAL_TRANSCRIPTIONS.txt` (VT-1..3) and `png/`.
- **Checksums:** `SHA256SUMS.txt`.
- **PIN OWED list:**
  - BH15 original (Sci. China Math. 2015)
  - Collingwood–McGovern Thm 9.3.3 and Lemma 3.7.3 (used only via the toy and Harris's example)
  - Knapp–Okamoto / Knapp–Zuckerman / EHW originals (route B, not needed)
  - Harris published venue + numbering (not verified; abs page has no journal-ref)

## Does any pinned theorem settle link 3 for every helicity? YES/NO, via which numbered statements, and does it resolve the |h| ≥ 4 weight-normalization caveat?

**YES.** It is settled by **Harris Theorem 1.1 / Corollary 1.2** (a tempered π has only real-distinguished orbits in its wave front cycle), **Schmid–Vilonen Theorem 1.4** (WF cycle = Kostant–Sekiguchi image of the associated cycle, inside the same complex orbit), and **Bai–Hunziker Proposition 3.2** with Table 1 (AV of a unitary highest-weight module is the closure of O_{k(λ)}, where k(λ) = −(λ, β^∨)/c). **Table 2** of arXiv:2402.08886 gives the complex label [2,1,1] of O_1.

For SU(2,2) the only representation-specific input is k(λ) = 1. It holds for every massless helicity because (λ, β^∨) = −d + j₁ + j₂ = −1 (Section 4). The step "orbits in [2,1,1] are not real distinguished" is geometry of su(2,2). It is independent of the representation, and we checked it numerically for both real orbits.

**Two caveats on tier:**
- (a) BH15 is pinned through the authors' own restatement; the original is PIN OWED.
- (b) The two Collingwood–McGovern structural facts are carried by the toy and Harris's Example 5.1, not by an open numbered pin.

**It resolves the |h| ≥ 4 caveat.** The conclusion depends only on the associated variety, an intrinsic invariant: the closure of the rank-≤1 K_ℂ-orbit in p⁺, of dimension 3 < 4. The only pairing used is the canonical coroot pairing (λ, β^∨). Spin is fixed by SU(2) dimensions, and d is fixed by the unique central element of k acting by +1 on p⁻. No SU(1,1) coroot rescaling enters, and the verdict does not change with h.

As a by-product, the canonical pairing gives (λ, β^∨) = −1, so the extremal weight along β is 1 for every helicity. That is the normalization R12 step 4 used ("min w = 1"). The "half" normalization that would have flipped |h| ≥ 4 is not the coroot normalization. So the R12 Ξ-inference was also right, but it is now superseded by the numbered chain.
