# R15 PINS (draft): invariant trilinear forms on D⁺ × D⁻ × π₃ for SL(2,ℝ), the rank-one control for SO(4,2)

Compiled 2026-09-27 by Claude (subagent for Grace). Every pin is a verbatim quote from a file in this directory, cited as file:line. Where the text layer garbles a formula, the page was rendered to `png/` and read by eye. Those readings are in `VISUAL_TRANSCRIPTIONS.txt`, block ids in [brackets]. Text marked **READING** is my own inference from the pinned quotes; it is not a quotation. Nothing here was taken from an abstract or a search snippet.

## 0. Files

| file | what it is | access |
|---|---|---|
| repka_1979_cjm31.{pdf,txt} | Repka, Canad. J. Math. 31 (1979) 836–844, DOI 10.4153/CJM-1979-079-9 | copied from ../../sources_grace_2026-09-26/r8_tensor/ |
| crossref_10.4153_cjm-1979-079-9.json | Crossref record for the above | copied from r8 |
| crossref_10.2307_2373909.json | Crossref record: Repka, "Tensor Products of Unitary Representations of SL 2 (R)", Amer. J. Math. 100(4) p.747, JSTOR | **PIN OWED** (paywalled, full text not on disk) |
| gk_2002_math0109201.{pdf,txt} | Groenevelt–Koelink, "Meixner functions and polynomials related to Lie algebra representations", J. Phys. A 35 (2002) 65–85, arXiv:math/0109201 | open |
| gkr_2003_math0302251.{pdf,txt} | Groenevelt–Koelink–Rosengren, "Continuous Hahn functions as Clebsch-Gordan coefficients", arXiv:math/0302251 | open |
| kitaev_2017_1711.08169.{pdf,txt} | Kitaev, "Notes on SL(2,ℝ)~ representations", arXiv:1711.08169 (cites Repka 1978 as [9]) | open |
| br_2004_math0305351.{pdf,txt} | Bernstein–Reznikov, "Estimates of automorphic functions", Moscow Math. J. 4 (2004), arXiv:math/0305351 | open |
| br_1999_math9907202.{pdf,txt} | Bernstein–Reznikov, Annals 150 (1999) 329–352, arXiv:math/9907202 | open (no trilinear-uniqueness statement; see 2c) |
| loke_2001_pjm197.{pdf,txt} | H. Y. Loke, "Trilinear forms of gl₂", Pacific J. Math. 197 (2001) 119–144, from msp.org (open) | open |
| crossref_10.2140_pjm.2001.197.119.json, crossref_search_loke.json | Crossref record for Loke | |
| deitmar_2005_math0503379.{pdf,txt} | Deitmar, "Invariant triple products", arXiv:math/0503379 | open (principal series only; context) |

---

## 1. CONVENTIONS, quoted first

**Repka 1979 (CJM).** SL(2) labels by the SO(2) weight:
> "Following Lang ([8]), for n ≧ 2 (resp. n ≦ −2) we let Tn denote the discrete series representation with lowest (resp. highest) weight n (corresponding to the character χn). The weights of Tn are n, n + 2, n + 4, . . . (resp. n, n − 2, n − 4, . . . ), each occurring with multiplicity one." (repka_1979_cjm31.txt:306-309 and 318; letter-spaced OCR, de-spaced here)

In general G₀, π_Λ is the unitary Hilbert-space representation, labelled by its highest weight Λ subject to condition (2), "(Λ + ρ)(H_γ) < 0, for all γ ∈ Σ₊" (txt:43). The tensor product is the Hilbert tensor product.

**Groenevelt–Koelink(–Rosengren).** The label is k = half the lowest |H|-eigenvalue. Representations are \*-representations of 𝔰𝔲(1,1) on finite linear combinations of basis vectors.
> "The positive discrete series representations πk+ are representations labelled by k > 0. … πk+ (H) en = 2(k + n) en , … πk+ (Ω) en = k(1 − k) en ." (gkr_2003_math0302251.txt:690-700; [GKR12a])
> "The negative discrete series representations πk− are labelled by k > 0. … πk−(H) en = − 2(k + n) en" (gkr:703-707; [GKR12b])
> "The principal series representations π ρ,ε are labelled by ε ∈ [0, 1) and ρ ≥ 0, where (ρ, ε) ≠ (0, 1/2)." (gkr:717)
> "For (ρ, ε) = (0, 1/2) the representation π^{0,1/2} splits into a direct sum of a positive and a negative discrete series representation: π^{0,1/2} = π⁺_{1/2} ⊕ π⁻_{1/2}." (gkr:735-737; [GKR12c])

**READING (dictionary):** Repka's T_m equals GK's π⁺_{m/2}. In both, the weights of H are m, m+2, …. The limit of discrete series (Repka m = 1) is k = 1/2.

**Kitaev.** Representations of the universal cover G̃. The label is λ, the Casimir is q = λ(1−λ), and the basis vectors |m⟩ have "m ∈ µ+Z" (kitaev:152-161). The discrete series are:
> "Discrete series Dλ+ , Dλ− : λ > 0, µ = ±λ, m = λ, λ + 1, λ + 2, . . . or m = −λ, −λ − 1, −λ − 2, . . ." (kitaev:176-180)
> "These formulas can be specialized to the irreps of G ≅ PSL(2, R), which are characterized by µ = 0. In particular, the discrete series representations are Dn± with n = 1, 2, . . ." (kitaev:859-860)

**READING:** Kitaev's λ is the same as GK's k, so Repka weight = 2λ.

**Bernstein–Reznikov 2004.** G = PGL₂(ℝ), not SL₂, and smooth vectors:
> "For reasons explained bellow we would like to work with the group G of all motions of H; this group is isomorphic to P GL2 (R). Hence throughout the paper we denote G = P GL2 (R)." (br_2004:213-214)
> "Usually it is more convenient to work with the space V = L∞ of smooth vectors in L." (br_2004:244)

The explicit model covers the class-one (generalized) principal series only:
> "For every complex number λ consider the space Vλ of smooth even homogeneous functions on R2 \ 0 of homogeneous degree λ − 1 … The representation (πλ , Vλ ) is called representation of the generalized principal series." (br_2004:296-301)

**Loke 2001.** Works in the algebraic category of (𝔤,K)-modules for GL₂. The discrete series d_s contains both signs of weight:
> "Throughout this paper all representations of GL2 (C) or GL2 (R) are infinitesimal representations unless otherwise stated." (loke:202-203)
> "If s ≥ 1 and s − ϵ is an odd integer, then π contains a unique irreducible submodule ds spanned by {wn : |n| ≥ s + 1}. It is a self dual representation. When s ≥ 1 it is called a discrete series representation. The quotient π/ds is an irreducible finite dimensional representation." (loke:239-242; ϵ dropped by the text layer, see [LK7] note)
> "If s = 0 and ϵ = 1, π = d0 is called a limit of discrete series." (loke:247)

**READING:** restricted to SL₂, Loke's d_s is D⁺_{s+1} ⊕ D⁻_{s+1} in Repka weights. So GL₂ statements cover the sign-patterns only jointly.

**Weight constraint (any category).** Loke Section 2.4:
> "The action of H gives (n1 + n2 + n3 )φ(w¹n1 ⊗ w²n2 ⊗ w³n3 ) = 0." (loke:256-257; [LK7a])

---

## 2. Pins

### 2a. Repka 1979, Theorem 2 (holomorphic ⊗ antiholomorphic)
> "THEOREM 2. If Λ, −Λ′ satisfy (1) and (2) of § 2, and L (resp. L′) is an irreducible representation of K0 with highest weight Λ (resp. lowest weight Λ′), then, as representations of G0, π_Λ ⊗ π_Λ′ ≈ Ind_{K0}^{G0} L ⊗ L′." (repka_1979_cjm31.txt:288-292)
> "Proof. By Schur's Lemma and Proposition 4.1, the tensor product is unitarily equivalent to the action of G0 on ℋ_{L⊗L′}~, and this representation is isomorphic to ℋ_{L⊗L′}, for which the action of G0 by right translation is indeed Ind_{K0}^{G0} L ⊗ L′." (txt:293-296)

**Hypotheses.** G₀ is non-compact simple, and its non-compact positive roots are totally positive (so K₀ has non-trivial centre) (txt:28-33). Conditions (1)+(2) mean both factors are genuine holomorphic, resp. antiholomorphic, discrete series. Limits and analytic continuations are not covered.

**The SL(2,ℝ) specialisation, discrete versus continuous content** (printed p.842; [RP7a]):
> "T_m ⊗ T_{−n} ≈ Ind_{K₀}^{G₀} χ_m ⊗ χ_{−n} = Ind_{K₀}^{G₀} χ_{m−n}." (txt:325-327, garbled; [RP7a])
> "This induced representation is easily decomposed using Frobenius Reciprocity; it contains one copy of the direct integral of the principal series representations of the appropriate parity (the same as the parity of m − n), and (at most) finitely many discrete series representations, namely those which contain the weight m − n. Each such component occurs with multiplicity one. See [9] for details, and for the connection with holomorphic functions on the upper half-plane. It is also proved there that the same results (i.e. same formulae) carry over to the "limits of discrete series" or "mock discrete series," i.e. when n and/or m is allowed to equal 1." (txt:329-337; [RP7c])

**Answer to the question asked.** Yes. Ind_{K₀}^{G₀}χ_{m−n} contains discrete series summands exactly when some discrete series contains the K-type m−n. For m ≠ n there are finitely many such summands, all of sign sgn(m−n). For m = n the weight is 0, and no discrete series contains weight 0 (Repka's T_k has |k| ≥ 2), so the content is purely continuous. **READING:** that last step is my application of the quoted rule, not a separate quote.

### 2b. The Repka 1978 (Amer. J. Math.) statement, via open restatements
- Primary: Crossref `crossref_10.2307_2373909.json` gives Repka, Amer. J. Math. 100(4) (1978), from p.747, JSTOR. **PIN OWED**: the full text is not on disk.
- SECONDARY 1. Groenevelt–Koelink 2002, **Theorem 2.2** (gk_2002_math0109201.txt:289-310; [GK6a]):
  > "Theorem 2.2. For k1 ≤ k2 the decomposition of the tensor product of positive and negative discrete series representations of su(1, 1) is π⁺_{k₁} ⊗ π⁻_{k₂} ≅ ∫₀^∞⊕ π^{ρ,ε} dρ, [k₁ − k₂ ≥ −1/2, k₁ + k₂ ≥ 1/2]; … ⊕ π^{λ,ε}, [k₁ + k₂ < 1/2]; ≅ ∫₀^∞⊕ π^{ρ,ε} dρ ⊕ ⨁_{j∈ℤ≥0, k₂−k₁−1/2−j>0} π⁻_{k₂−k₁−j}, [k₁ − k₂ < −1/2], where ε = k1 − k2 + L, L is the unique integer such that ε ∈ [0, 1) and λ = −k1 − k2."

  With the sign identified: "From this we recognize the action of Ω in a discrete series representation πk2 −k1 −j . From the action of H, we find that this is a negative discrete series representation." (gk:284-285)
- The same theorem is restated as Theorem 4.1 in GKR 2003: "The decomposition of the tensor product of a positive and a negative discrete series representation of su(1, 1) is determined in full generality in [10, Thm.2.2]." (gkr:761-786; [GKR13a])
- SECONDARY 2. Kitaev, **eq. (140)**. He cites Repka: "For the group SL(2, R), this task was accomplished by Repka [8, 9]." (kitaev:1377), where [9] is "J. Repka, "Tensor products of unitary representations of SL2 (R)", Am. J. Math. 100 (4), 747–774 (1978)." (kitaev:1714-1715)
  > "D⁺_{λ₁} ⊗ D⁻_{λ₂} ≅ ∫₀^∞ C^ν_{1/4+s²} ds ⊕ ⨁_{λ=|ν|−p>1/2, p=0,1,2,...} D^{sgn ν}_λ ⊕ (C^ν_{λ(1−λ)} for λ = λ₁ + λ₂ < 1/2)" (140), with ν = λ₁ − λ₂ (kitaev:1541-1548, 1558; [KT25a])

  Kitaev also points at a numbered result inside Repka 1978: "One could use some functional analysis to characterize the relation between the Hilbert spaces D⁺_{λ₁} ⊗ D⁻_{λ₂} and H^ν_H, cf. Proposition 7.2 in [9]." (kitaev:1538-1540)
- **READING (translation to Repka weights, m = 2k₁, n = 2k₂).** D⁺_m ⊗ D⁻_n = (principal series of parity m−n, continuous) ⊕ ⨁ D^{sgn(m−n)}_{|m−n|−2j}, over j ≥ 0 with |m−n|−2j > 1. For the linear group this means |m−n|−2j ≥ 2, i.e. exactly the discrete series containing weight m−n, in agreement with 2a. The limit of discrete series (weight 1, k = 1/2) is **not** a discrete summand. It sits inside the principal series at (ρ,ε) = (0,1/2) (gkr:735), a single point of the continuous spectrum. The complementary-series term occurs only on the universal cover (k₁+k₂ < 1/2), never for SL(2,ℝ) itself (gk:447-449: "For the group SU (1, 1) there is no complementary series representation in the decomposition of the tensor product, since then k1 , k2 ∈ 1/2 N.").
- The user's guess "D_m⁺ ⊗ D_n⁻ ⊃ D⁺_{m−n−2j}" is correct in Repka weights when m > n. In GK half-weights the offset is j, not 2j.

### 2c. Bernstein–Reznikov: dimension ≤ 1, and the Oksak model
BR 2004 **Section 2.4.2** (the statement is headed "Theorem." with no number; it sits in numbered subsection 2.4.2):
> "2.4.2. Uniqueness of triple products. The central fact about invariant trilinear functionals is the following uniqueness result: Theorem. Let (πj , Vj ), j = 1, 2, 3 , be three irreducible smooth admissible representations of G. Then dim HomG (V1 ⊗ V2 ⊗ V3 , C) ≤ 1." (br_2004_math0305351.txt:356-359) [G = PGL₂(ℝ)]
> "Remark. The uniqueness statement was proven by Oksak in [O] for the group SL(2, C) and the proof could be adopted for P GL2 (R) as well (see also [Mo] and [Lo]). For the p-adic GL(2) more refined results were obtained by Prasad (see [P]). He also proved the uniqueness when at least one representation is a discrete series representation of GL2 (R). There is no uniqueness of trilinear functionals for representations of SL2 (R) (the space is two-dimensional). This is the reason why we prefer to work with P GL2 (R). For SL2 (R) one has the following uniqueness statement instead. Let (π, V ) and (σ, W ) be two irreducible smooth pre-unitary representations of SL2 (R) of class one. Then the space of SL2 (R)-invariant trilinear functionals on V ⊗ V ⊗ W which are symmetric in the first two variables is one-dimensional." (br_2004:360-370)

Explicit model, **Section 5.1, eqs. (17)–(19)**, for the class-one principal series V_λ:
> "Kλ1 ,λ2 ,λ3 (s1 , s2 , s3 ) = |ω(s2, s3 )|^{(α−1)/2} |ω(s1 , s3 )|^{(β−1)/2} |ω(s1, s2 )|^{(γ−1)/2} … where α = λ1 − λ2 − λ3 , β = −λ1 + λ2 − λ3 , γ = −λ1 − λ2 + λ3 ." (17) (br_2004:641-642)
> "(1) K is invariant with respect to the diagonal action of SL2 (R). (2) K is homogeneous of degree −1 − λj in each variable sj ." (br_2004:644-645)
> "lmod(f1 ⊗ f2 ⊗ f3 ) = (2π)^{−3} ∭ f1 (x)f2 (y)f3 (z)Kλ1 ,λ2 ,λ3 (x, y, z)dxdydz" (19) (br_2004:668-671)
> "Remark. The integral defining the trilinear functional is often divergent and the functional should be defined using regularization of this integral. … Fortunately in the case of unitary representations all integrals converge absolutely" (br_2004:674-678)

The Oksak reference is "[O] A. Oksak, Trilinear Lorenz invariant forms. Comm. Math. Phys. 29 (1973), 189–217." (br_2004:989). Oksak's own paper is **not on disk**: PIN OWED/SECONDARY via BR.

**Scope limits:**
- BR 2004 does not treat discrete series: "There are other spaces in this decomposition which correspond to discrete series representations. Since they are not related to Maass forms we will not study them in more detail." (br_2004:285-287)
- BR 1999 (Annals) contains no dimension statement for trilinear functionals. grep "unique" hits only a seminorm claim (br_1999:584, 870). Its method uses invariant Hermitian forms, not trilinear uniqueness.

The same model kernel, for the universal cover and allowing discrete series, is Kitaev **eq. (128)** ([KT23a]), with the dimension count in the surrounding prose:
> "In general, this system of equations has multiple linearly independent solutions. But we are considering only those values of λj , mj that correspond to unitary irreps. With this restriction, the linear relations in the allowed region of (m1 , m2 , m3 ) are nondegenerate and can be turned into recurrences, which are solved beginning with just two Fourier coefficients. Thus, the solution space is at most two-dimensional." (kitaev:1419-1423)
> "…This can only happen if a discrete series representation is involved. But if, say, U^{µ1}_{λ1} = D⁺_{λ1}, then the generating form (124) is holomorphic in z1 = e^{iϕ1} for |z1| < 1. In this case, the regularization is achieved by analytic continuation. Since both cyclic orders are just limiting cases of z1 being inside the circle, the intertwiner space is one-dimensional." (kitaev:1433-1439)

This is prose in a set of notes, not a numbered theorem. Treat it as SECONDARY support.

### 2d. Loke 2001 (open, msp.org): the classification with discrete series is Prasad's Theorem 1.1
> "Theorem 1.1. Suppose F = R and π1 is a discrete series representation or a limit of discrete series representation. Then π1 ⊗ π2 ⊗ π3 exhibits a (g, K)-invariant form if and only if ϵ(σ1 ⊗ σ2 ⊗ σ3 ) = 1. In this case the invariant form is unique up to scalars." (loke_2001_pjm197.txt:69-72; [LK3b]) (attributed: "The following result is due to Prasad [Pa1]", loke:68)
> "(ii) ϵ(σ1 ⊗σ2 ⊗σ3 ) = 1 if at least one of the representations πi is a principal series representation. (iii) ϵ(σ1 ⊗ σ2 ⊗ σ3 ) = −1 if and only if π1 , π2 and π3 are discrete series representations and π1′ ⊗ π2′ ⊗ π3′ has a non-zero H∗ -invariant form." (loke:59-67; [LK3a])
> "If πi is a discrete series, we denote πi′ to be the irreducible finite dimensional representation of H∗ with the same infinitesimal character and central character as πi." (loke:45-47)

Principal-series completion:
> "Theorem 1.2. … π1 , π2 and π3 are (g, K)-modules belonging to the principal series … (1) If F = R, then πi is either irreducible or reducible of type I. … (3) The product of central characters of the three representations is trivial. … π1 ⊗ π2 ⊗ π3 exhibits a (g, K)-invariant form and it is unique up to scalars." (loke:79-88; [LK3c])
> "2.8. The proof can be modified to find gl2 (R)-invariants for πi irreducible. In this case (1) is not necessary and we can show that the space of such invariants has dimension two." (loke:385-387)

The second quote is the (𝔤, K₀)-level statement, i.e. without ω: dimension two. This agrees with BR's "two-dimensional" for SL₂.

**Loke's own paper states no separate (D⁺, D⁻, π₃) or (D⁺, D⁺, π₃) condition.** GL₂(ℝ) discrete series are D⁺ ⊕ D⁻ jointly (Section 1 conventions). The SL₂ sign-pattern answers below are READINGS obtained by combining 2d with 2a/2b and the weight constraint.

**READING: the triple-discrete case in weights.** For GL₂, d_s ↔ π′ = the finite-dimensional representation of ℍ\* (Loke: "we identify its subset of non-zero elements H∗ with U2", loke:44-45) of dimension s, i.e. SU(2) spin (s−1)/2. An SU(2)-invariant exists on the triple iff the spins satisfy the triangle inequality and integrality. So ϵ = −1 ⟺ triangle holds, and a GL₂ trilinear form on d_{s₁}⊗d_{s₂}⊗d_{s₃} exists iff the triangle **fails**: one s_i − 1 exceeds the sum of the other two. In Repka weights k_i = s_i + 1, and with parity, this is k_big = k₁ + k₂ + 2j, j ≥ 0. This matches Repka Theorem 1 (T_m ⊗ T_n = ⊕ T_{m+n+2k}; repka txt:317-321 [RP7b]; Kitaev (129) [KT24a]). The s ↔ dim π′ step is from Loke's "π/d_s is an irreducible finite dimensional representation" (loke:241-242) together with "same infinitesimal character". The ℍ\*-to-SU(2) triangle rule is standard. Neither of those two steps is quoted here, so this remains a READING.

---

## 3. TABLE: SL(2,ℝ), invariant trilinear form on π₁ × π₂ × π₃

π₁ = D⁺_m (lowest weight m ≥ 2), π₂ = D⁻_n (highest weight −n, n ≥ 2), in Repka weights (T_m, T_{−n}). The contragredient of D^±_k is D^∓_k. A form on π₁×π₂×π₃ is the same as π₃^∨ ↪ π₁⊗π₂ (discretely, or at the (𝔤,K)/smooth level). The "L²" column asks whether π₃^∨ is a discrete Hilbert summand; the "(𝔤,K)/smooth" column asks whether a form exists at all.

| (π₁, π₂, π₃) type | invariant trilinear form exists? | conditions | source file:line |
|---|---|---|---|
| (D⁺_m, D⁻_n, D⁺_k) | **Yes, iff** n − m − k ∈ 2ℤ≥0 (so needs n > m). L²: D⁻_k is a discrete summand of D⁺_m⊗D⁻_n. Unique. | k ≡ n−m (mod 2), 2 ≤ k ≤ n − m. GK units: k/2 = k₂ − k₁ − j > 1/2 | gk_2002:289-310 [GK6a]; kitaev:1541-1548 [KT25a]; repka:329-334 ("those which contain the weight m − n"). (𝔤,K)-level iff: READING from repka:317-321 [RP7b] (T_m⊗T_k ⊇ T_n ⟺ n = m+k+2j) + loke:69-72 (uniqueness) |
| (D⁺_m, D⁻_n, D⁻_k) | **Yes, iff** m − n − k ∈ 2ℤ≥0 (needs m > n). Mirror of the row above. | k ≡ m−n (mod 2), 2 ≤ k ≤ m − n | same as above, with the roles swapped (Kitaev D^{sgn ν}, ν = λ₁−λ₂) |
| (D⁺_m, D⁻_n, D^±_k), m = n | **No** (discrete). Both signs of π₃ fail the conditions above. | weight m−n = 0 lies in no discrete series | repka:329-334; gk_2002:289-296 (first case k₁−k₂ ≥ −1/2 has no discrete part) |
| (D⁺_m, D⁻_n, limit D^±_1) | L²: **No** discrete summand (the limit is inside π^{0,1/2}, measure zero). (𝔤,K): READING yes iff the weight rule holds with k = 1 (n − m − 1 ∈ 2ℤ≥0), via Repka's extension to limits, which is SECONDARY to [9] | parity odd | gkr:735-737 [GKR12c]; gk:308 (strict >1/2); repka:335-337 [RP7c] (limits, cited to [9]); loke:69-72 (limit allowed in π₁) |
| (D⁺_m, D⁻_n, principal series π^{ρ,ε}) | **Yes** at the smooth/distribution level, for every principal series of matching parity. It is **not** an L² discrete coupling: it appears in the continuous spectrum. Unique (Kitaev: one-dimensional when a D⁺ is involved). | ε ≡ parity of m−n (central character) | repka:329-331 ("one copy of the direct integral of the principal series … parity of m − n"); gk_2002:289-296; kitaev:1433-1439; GL₂ level: loke:59-60 (ϵ=1 if any PS) + 69-72 |
| (D⁺_m, D⁻_n, complementary series) | Only on the universal cover, when k₁+k₂ < 1/2 (Repka weights m+n < 1). **Never** for SL(2,ℝ) | — | gk_2002:293-296, 447-449; kitaev (140) |
| (D⁺_m, D⁺_n, D⁻_k) | **Yes, iff** k = m + n + 2j, j ≥ 0 ("weights add"). Unique | parity k ≡ m+n | repka:317-321 [RP7b] (Theorem 1, SL₂ case); kitaev:1442-1446 (129) [KT24a]; GL₂ form: loke:59-72 (ϵ=1 ⟺ triangle fails), READING |
| (D⁺_m, D⁺_n, D⁺_k) | **No** | all weights positive; H-invariance forces weight sum 0 | loke:256-257 [LK7a] |
| (D⁺_m, D⁺_n, irreducible PS) | **No** (READING). The (𝔤,K) tensor product is ⊕ lowest-weight modules (Repka Thm 1), and an irreducible PS has no lowest-weight vector | — | repka Theorem 1 (r8 VT R3b; txt:117-130) + loke:230-236 (PS basis w_n for all n of one parity) — **READING, not pinned** |
| (π₁,π₂,π₃) all class-one PGL₂ | ≤ 1-dim (PGL₂); SL₂: 2-dim; model kernel (17)/(19) | smooth vectors | br_2004:356-370; br_2004:641-678; loke:385-387 |

**Rank-one answer to the control question.** A holomorphic D⁺_m and an antiholomorphic D⁻_n couple invariantly to a discrete (lowest- or highest-weight) third module **only if their weights differ**. The third module is then any discrete series whose contragredient contains the K-type m − n. These are finitely many, all of sign sgn(m−n), with |weight| ≤ |m−n| and matching parity. At equal weight (m = n) only the principal series couples. The limit of discrete series (Repka weight 1) is never an L² summand. At the (𝔤,K) level it does couple when |m−n| is odd and ≥ 1; this rests on Repka's limit extension, which is SECONDARY. Uniqueness is always one-dimensional once a discrete series is present (Prasad via Loke Thm 1.1; Kitaev).

---

## 4. Higher rank (item 3): no numbered trilinear-form statement found

- No source on disk or found here states a numbered theorem on invariant trilinear forms on (holomorphic DS) × (antiholomorphic DS) × (unitary highest-weight / ladder module) for SU(2,2), SO(4,2) or general Hermitian G. **Nothing to pin. Search incomplete**: Kobayashi's symmetry-breaking papers were not opened with this target in mind. arXiv:math/0607004 (Kobayashi, propagation of multiplicity-freeness) was checked, has no such statement, and was not kept.
- Deitmar (deitmar_2005_math0503379.txt:18-26, Thm 2.1 at :206-211) covers only **principal series** and uniqueness "only if G is locally a product of hyperbolic groups". It says nothing on discrete or highest-weight modules.
- What *is* pinned for higher rank:
  - **Repka Theorem 2** (2a) holds for any simple Hermitian G₀, including SU(2,2), provided both factors are genuine (condition (2)) holomorphic or antiholomorphic discrete series: π_Λ ⊗ π_Λ′ ≈ Ind_{K₀}^{G₀} L⊗L′ = L²(G₀/K₀, L⊗L′).
  - **Ørsted–Zhang 1997, Theorem 5.1** (pinned in r8): "Let ν > (p−1)/2 … π_ν ⊗ π̄_ν ≅ ∫^⊕_{𝔞*/W} H(λ) dλ" (../../sources_grace_2026-09-26/r8_tensor/VISUAL_TRANSCRIPTIONS.txt:59-62, [OZ17b]; SU(2,2) genus p = 4 per [OZ1c] line 47-49). For scalar equal weights this is purely continuous, spherical principal series only, with no discrete summands. It is the higher-rank analogue of the m = n row.
- **READING (unpinned, standard Harish-Chandra):** the discrete spectrum of L²(G₀/K₀, τ) ⊂ L²(G₀)⊗V_τ consists of discrete series only. A massless spin-1 ladder module of SO(4,2)/SU(2,2) is a unitary highest-weight module *below* the discrete-series range (not satisfying Repka's condition (2)). So it cannot occur as a discrete L² summand of hol-DS ⊗ antihol-DS, whatever the weights. Whether a smooth/distribution-level invariant trilinear form exists (the analogue of the "(𝔤,K)" column and of the limit-of-DS row) is **not settled by any pinned source**. It is PIN OWED.

## 5. Owed

1. Repka, Amer. J. Math. 100 (1978) 747–774: primary text (JSTOR). The exact statement and Proposition 7.2 are PIN OWED. The restatements are GK 2002 Thm 2.2 and Kitaev (140).
2. Oksak, Comm. Math. Phys. 29 (1973) 189–217: PIN OWED (only cited via BR 2004:360, 989).
3. Prasad, Compositio 75 (1990) 1–46, source of Loke Thm 1.1: SECONDARY via Loke.
4. A numbered higher-rank statement (item 3): none found.
