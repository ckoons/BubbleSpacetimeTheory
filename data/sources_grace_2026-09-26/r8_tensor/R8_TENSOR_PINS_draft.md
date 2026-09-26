# R8 — Tensor products H_λ ⊗ H_μ of scalar holomorphic modules: primary-source pins (DRAFT)

Compiled 2026-09-26 ~15:00 EDT by a Claude subagent for Grace. Every pin below is a verbatim quote from a file on disk, cited as file:line (text layer) or as a VISUAL_TRANSCRIPTIONS block id (formula read by eye from a rendered page; PNG saved alongside). Lines marked **READING** are my own arithmetic or inference and are not pins.

Directory: `data/sources_grace_2026-09-26/r8_tensor/` (new files) plus the existing `../r6_conformal/` (JV 1979, Nakahama 2603.21472, Kobayashi–Pevzner 1812.09733; not modified).

Target case: G = SO_0(2,5) (or its covering), D = Lie ball of type IV_5, scalar modules H_λ with λ = μ = 5/2.

---

## 0. Files and access status

| Source | File(s) | Status |
|---|---|---|
| J. Repka, Can. J. Math. 31 (1979) 836–844 | `repka_1979_cjm31.pdf` (9 pp, Cambridge Core open PDF), `.txt`, `repka_p{1,3,7}-*.png` | **PINNED from primary.** DOI per Crossref is **10.4153/CJM-1979-079-9**. The brief's "…-079-0" is wrong. See `crossref_10.4153_cjm-1979-079-9.json`. |
| B. Ørsted & G. Zhang, Can. J. Math. 49 (1997) 1224–1241, DOI 10.4153/CJM-1997-060-5 | `orsted_zhang_1997_cjm49.pdf` (18 pp, open), `.txt` (font-garbled), `oz_p-{01,17}.png` | **PINNED from primary** (visual). Found through the Crossref search for Repka, not in the brief. It is directly relevant because it is the analytic-continuation paper. |
| Jakobsen & Vergne, JFA 34 (1979) 29–53 | `../r6_conformal/jakobsen_vergne_1979.{pdf,txt}`, `jv_p-{07,24}.png` | PINNED (primary) |
| Nakahama, arXiv:2603.21472v2 | `../r6_conformal/arxiv_2603.21472.{pdf,txt}`, `nak_p-{07,08,16,17,30}.png` | PINNED (primary) |
| Kobayashi–Pevzner, arXiv:1812.09733 (Ann. Inst. Fourier 70 (2020)) | `../r6_conformal/arxiv_1812.09733.{pdf,txt}`, `kp_p-{07,09,12}.png` | PINNED (primary, arXiv version) |
| T. Kobayashi, "Multiplicity-free theorems … reductive symmetric pairs", Progr. Math. 255 (2008) 45–109, Thm 8.4 / Lemma 8.9 | not on disk | **PIN OWED / SECONDARY**: quoted only as Nakahama restates it (Section 3 below). |

---

## 1. Repka 1979 — "Tensor products of holomorphic discrete series representations"

### 1a. Conventions (quote first)

- Group: "Let g0 be a non-compact simple real Lie algebra." [`repka_1979_cjm31.txt:27`]. The Cartan subalgebra lies in 𝔨₀, and the non-compact positive roots are assumed "totally positive, in the terminology of Harish-Chandra" [txt:31-33; VT R1c].
- Weight conditions (VT R1b; txt:41-43):
  > "Suppose Λ ∈ 𝔥* satisfies: (1) Λ(H_α) is a nonnegative integer, for all α ∈ Σ, α ∉ Σ₊ (2) (Λ + ρ)(H_γ) < 0, for all γ ∈ Σ₊."

  Here Σ₊ = the non-compact positive roots and 2ρ = the sum of all positive roots [txt:30, 34].
- Representations: vector-valued in general. "Suppose too that L is an irreducible representation of K0 on a Hilbert space V, which has highest weight Λ. Then … Harish-Chandra constructs a (unique) unitary irreducible representation of G0 … This representation … will be denoted π_Λ, and called a holomorphic discrete series representation." [txt:44, 56-60]
- The normalization is by highest weight Λ with Harish-Chandra's condition (2). **Only the holomorphic discrete series proper** is covered. The paper has no parameter λ that is continued analytically.

### 1b. Main theorem (holomorphic ⊗ holomorphic) — VT R3b; txt:117-130

> "THEOREM 1. π_Λ ⊗ π_Λ′ is a direct sum of representations of the form π_Λ″, with finite multiplicities. The Λ″ which occur are all of the form Λ″ = Λᵢ″ − (m₁γ₁ + ... + m_qγ_q), where Λᵢ″ (0 ≦ i ≦ s) is a weight of L ⊗ L′, and mᵢ are nonnegative integers. The multiplicity M_Λ″, of π_Λ″ is given by the inductive formula M_Λ″ = n″(Λ″) − Σ_{λ≠Λ″} M_λ n_λ(Λ″)."
>
> "In particular, π_{Λ+Λ′} occurs with multiplicity one."

The decomposition is discrete, with finite multiplicities, and is fixed by weight counting. The proof uses Garland–Lepowsky Lemma 4.4 plus unitarity [txt:132-140].

### 1c. Holomorphic ⊗ antiholomorphic — txt:288-292

> "THEOREM 2. If Λ, −Λ′ satisfy (1) and (2) of § 2, and L (resp. L′) is an irreducible representation of K0 with highest weight Λ (resp. lowest weight Λ′), then, as representations of G0, π_Λ ⊗ π_Λ′ ≈ Ind_{K0}^{G0} L ⊗ L′."

### 1d. SL(2,ℝ) example: the rank-one formula (VT R7a, R7c; txt:317-321, 334-337)

> "So if m, n ≧ 2, the weights of T_m ⊗ T_n are m + n, m + n + 2, ..., m + n + 2k, ..., where m + n + 2k occurs with multiplicity k + 1. Consequently, by Theorem 1, T_m ⊗ T_n ≈ T_{m+n} ⊕ T_{m+n+2} ⊕ T_{m+n+4} ⊕ ... = ⊕_{k=0}^∞ T_{m+n+2k}"
>
> "It is also proved there [= ref. 9, Repka, Amer. J. Math. 100 (1978)] that the same results (i.e. same formulae) carry over to the "limits of discrete series" or "mock discrete series," i.e. when n and/or m is allowed to equal 1."

- Convention: "T_n denote the discrete series representation with lowest (resp. highest) weight n" for n ≥ 2 (resp. n ≤ −2) [txt:306-307]. The integer n is the SO(2) weight, i.e. the modular weight.
- The limit case (m or n = 1) is **stated here as proved in ref. [9]**, which is not on disk. That makes it SECONDARY.
- Non-integer (covering-group) parameters are not treated.

### 1e. Higher rank — no closed form (txt:355-360, 392-396)

> [Sp(2,ℝ)] "Other representations π_{Λ+Λ′−kα−jγ} also occur (e.g. π_{Λ+Λ′−α−γ} occurs with multiplicity 2) but it gets increasingly messy to calculate the multiplicities."
>
> "The decomposition of tensor products of holomorphic discrete series representations will follow easily from an analysis of irreducible representations of K0 — their weights and the decomposition of their tensor products. On the other hand, it is also clear that these calculations quickly become fairly involved."

**Repka verdict.** Repka covers general simple Hermitian G0 with vector-valued π_Λ. The only hypothesis is Harish-Chandra's discrete-series condition (2). There is no explicit SO(2,n) or type-IV example; the worked examples are SL(2,ℝ) and Sp(2,ℝ). Limits and analytic continuation are not covered, except the SL(2) limit m, n = 1, which is only cited to [9]. **READING:** for scalar type IV_5, condition (2) corresponds to λ > n − 1 = 4, so Repka does not reach λ = 5/2. This translation of (2) into the λ parameter is mine and is not pinned from a type-IV source. Nakahama's threshold 2n/r − 1 (Section 3a) gives the same number.

---

## 2. Jakobsen–Vergne 1979 — "Restrictions and expansions of holomorphic representations"

### 2a. Conventions and hypotheses (quote first)

- Setting: 𝔤 semisimple with 𝔨 having nontrivial center (Hermitian symmetric) [`../r6_conformal/jakobsen_vergne_1979.txt:209-212`]. "Let G_c be the simply connected Lie group with Lie algebra g_c, and let K_c, G, and K be the connected subgroups corresponding to …" [txt:231-232].
- The modules are vector-valued: τ is "a finite-dimensional irreducible unitary representation of K in V_τ" [txt:250], and H(τ) ⊂ 𝒪(G, K, V_τ).
- The two sets I and P (VT JV7a; txt:311-316):
  > "I = { τ ∈ K̂ | 𝒰(𝔤^ℂ) ⊗_{𝒰(𝔨^ℂ⊕𝔭⁺)} V_τ is irreducible }, and P = { τ ∈ K̂ | W(τ) is unitarisable }."  (2.15)

  I is the set where the generalized Verma module is irreducible. P is the unitarizable set, i.e. the full unitary highest-weight range, **not only discrete series**. "Finally we observe that the set P is not known apart from some special cases [8, 10, 13]." [VT JV7c; txt:328-330]

### 2b. Corollary 2.6 (general G) — r6 VT block [J] J3-J4; txt:457-460

> "COROLLARY 2.6. Let G be as before, and let τᵢ ∈ I ∩ P for i = 1, 2. Then H(τ₁) ⊗ H(τ₂) = ⊕_{n=0}^{∞} H(τ₁ ⊗ τ₂ ⊗ Sⁿ(p⁻))."
>
> "Proof. Imbed G in G × G by the diagonal map and apply Proposition 2.5 with G = G × G and G1 = G. (Comment: τ1 ⊗ τ2 ∈ I ∩ P ⊂ Ĝ×G.)" [txt:461-462]

Proposition 2.5 also says: "Furthermore, the modules on the right-hand side are all finite sums of H(μᵢ)'s where μᵢ ∈ I₁ ∩ P₁ ⊂ K̂₁" [r6 VT J1-J2; txt:425-426]. So each H(τ₁ ⊗ τ₂ ⊗ Sⁿ(p⁻)) means the finite sum over the K-irreducibles in τ₁ ⊗ τ₂ ⊗ Sⁿ(p⁻).

### 2c. Scalar case for O(2, n+1): where λ = 5/2 enters (r6 VT block [L] L8; txt:606-608)

> "If α ≥ (n − 1)/2, it is known that α ∈ P and if α > (n − 1)/2, α ∈ I ∩ P. We denote in this case the representation of G_{n+1} in the space H(α; n + 1) of holomorphic functions on Ω⁺_{n+1} by T(α; n + 1)."

Conventions for α, quoted before use:
- "(T_α(g)f)(v̄) = j(g⁻¹, v̄)^{−α} f(g⁻¹v̄) (3.12) for α ∈ ℤ." [r6 VT L1-L2; txt:584-585]
- The kernel is built from "R(z, z′) = q′(v(z), v(z̄′)) = −½(z − z̄′)²" (3.13) and "the function z → K(z, i)^{−α}" [r6 VT L3-L6; txt:592, 603].
- The group is "0(2, n + 1) … G_{n+1} its connected component … K_{n+1} … isomorphic to SO(2) × SO(n + 1)" [txt:482-485 region, r6 VT K3-K5].

**READING (not a pin):**
- SO(2,5) is JV's O(2, n+1) with n + 1 = 5, i.e. n = 4. The threshold (n − 1)/2 is then 3/2, so α = 5/2 > 3/2 and JV's statement gives α = 5/2 ∈ I ∩ P.
- JV's α is the exponent of the rank-2 quadratic kernel R^{−α}. On the tube this is the Faraut–Korányi generic-norm exponent, so α = the brief's λ (the Wallach continuous threshold is (N−2)/2 = 3/2 for N = 5). This identification is mine.
- **Caveat 1:** JV define T_α in (3.12) "for α ∈ ℤ". The general Section 2 set-up (G ⊂ G_c simply connected) allows half-integral central characters, but JV never write α = 5/2 explicitly. Using α = 5/2 therefore needs the covering group. The "α > (n−1)/2 ⇒ α ∈ I ∩ P" sentence is a citation ("it is known") and not proved in JV.

**Given that reading**, Corollary 2.6 yields the discrete Hilbert decomposition H(5/2) ⊗ H(5/2) = ⊕_{n≥0} H(χ_{5/2}⊗χ_{5/2}⊗Sⁿ(p⁻)).
- **Caveat 2:** that the K-types χ_5 ⊗ V_k lie in I₁ ∩ P₁ is asserted by Prop. 2.5 itself ("finite sums of H(μᵢ)'s where μᵢ ∈ I₁ ∩ P₁").

### 2d. What JV do NOT write

- **No explicit decomposition of Sⁿ(p⁻) for type IV.** No formula "H_λ ⊗ H_μ = ⊕_{a,b} H(λ+μ+…)" appears for SO(2,n). The phrases "p⁻ ≅ ℂⁿ" and "Sⁿ(ℂⁿ) = ⊕ harmonic pieces" come from the brief and are not in JV. Section 3's O(2,n+1) analysis is about **restriction** O(2,n+1) ↓ O(2,n) (Corollary 3.1, Prop. 3.2, 3.3; r6 VT K17-K18, M2-M6), not tensor products.
- **The "O(4,2) detailed case" is Section 4, "EXAMPLE: TENSOR PRODUCTS OF ANALYTIC CONTINUATIONS OF THE HOLOMORPHIC DISCRETE SERIES FOR SU(2,2)"** [txt:698-699]. Its explicit result concerns **mass-zero limit points** T₁(n,−1), T₂(m,−1), not scalar H_λ at generic λ (VT JV24a; txt:1078-1096):
  > "PROPOSITION 4.9. T₁(n, −1) ⊗ T₁(m, −1) = ⊕_{q=0}^{min(n,m)} T₁(n + m − 2q, q) ⊕ ⊕_{r=1}^{∞} T₃(n + m + r, r, r + 2); … T₁(n, −1) ⊗ T₂(m, −1) = ⊕_{r=1}^{∞} T(n + r, m + r, m + r + 2)."

  Here "(T₁(n, α)(g)f)(z) = τ_n(cz + d)⁻¹ det(cz + d)^{−(α+2)} f(g⁻¹z)" with "α, β ∈ ℤ, and n, m ≥ 0. For α > −1 and β > −1 the representations … are unitary, irreducible, and strongly supported by C⁺" [txt:947-953].

---

## 3. Nakahama, arXiv:2603.21472v2 — "Holographic operators for the tensor products of the spaces of holomorphic functions on Hermitian symmetric spaces of tube type"

### 3a. Conventions (quote first)

- Groups: "D ≃ G/K = Sp(r,ℝ)/U(r), SU(r,r)/S(U(r)×U(r)), SO*(4r)/U(2r), SO0(2,n)/SO(2)×SO(n) and E7(−25)/U(1)×E6, realized as bounded symmetric domains in complex simple Jordan algebras p⁺ = Sym(r,ℂ), M(r,ℂ), Alt(2r,ℂ), ℂⁿ, and Herm(3,𝕆)^ℂ respectively." [`../r6_conformal/arxiv_2603.21472.txt:106-109`]. **Type IV (SO_0(2,n), p⁺ = ℂⁿ) is included explicitly.** The group acting is the universal cover G̃ [txt:378-384].
- "rank p⁺ = r, dim p⁺ = n = r + (d/2)r(r − 1)" [txt:194]. **READING:** for SO_0(2,5), r = 2, n = 5, d = 3.
- Scalar normalization: "𝒪(D, χ^{−µ}) =: 𝒪_µ(D)" [VT N7b]. The inner product is ∫_D f₁ f̄₂ h(x,x̄)^{µ−2n/r} dx, with C_µ = π^{−n} Π_j Γ(µ − (d/2)(j−1)) / Γ(µ − n/r − (d/2)(j−1)) [VT N7c]. The discrete-series condition is "λ_r > 2n/r − 1" [VT N7a]. **READING:** for type IV_5, 2n/r − 1 = 4 and n/r − 1 = 3/2.
- Tube type is assumed throughout; type IV is tube type.

### 3b. Decomposition used (Kobayashi's theorem as restated) — VT N8c; txt:485-493

> "Theorem 2.2 (Kobayashi, [16, Theorem 8.4]). Suppose λ, µ > 2n/r − 1. Then ℋ_λ(D) ⊗̂ ℋ_µ(D) is decomposed under G̃ as ℋ_λ(D) ⊗̂ ℋ_µ(D) ≃ Σ^⊕_{k∈ℤ^r_{++}} ℋ_{λ+µ}(D, V^∨_{kγ})."

Here "ℤ^r_{++} := {k = (k₁,...,k_r) ∈ ℤ^r | k₁ ≥ ··· ≥ k_r ≥ 0}" and "𝒫(𝔭⁺) ≃ ⊕_{k∈ℤ^r_{++}} V^∨_{kγ} … (2.3) (see [9, Theorem XI.2.4])" [VT N8b]. Also "When k = (l,...,l), we have 𝒪_λ(D, V^∨_{kγ}) ≃ 𝒪_{λ+2l}(D)" [VT N16b; txt:991].

- **READING for SO_0(2,5):** r = 2, so H_λ ⊗̂ H_μ ≃ ⊕_{k₁≥k₂≥0} H_{λ+μ}(D, V^∨_{(k₁,k₂)}). The scalar summands are exactly k = (l,l), giving H_{λ+μ+2l}. The other summands are vector-valued.
- Hypothesis λ, μ > 2n/r − 1 = 4. **This does not cover λ = μ = 5/2.** The original is Kobayashi, Progr. Math. 255 (2008): PIN OWED.

### 3c. Main theorems — hypotheses and the holographic operator

- Theorem 4.1 [txt:909-942] is for general σ, τ with "m ∈ ℤ such that Re λ_r + m > n/r − 1, Re µ_r + m > n/r − 1". The target is O(D×D) or O((D×D)^×) depending on 2m ≥ λ₁ + μ₁ − λ_r − μ_r.
- Scalar specialization (VT N16a; txt:973-988):
  > "Corollary 4.3. Let λ, µ ∈ ℂ, k ∈ ℤ^r_{++}, Re λ, Re µ > −k_r + n/r − 1. … Then the map ℱ^{λ,µ}_{k↑}: 𝒪_{λ+µ}(D, V^∨_{kγ}) → 𝒪_λ(D) ⊗̂ 𝒪_µ(D), (ℱ^{λ,µ}_{k↑} f)(x,y) := det(x−y)^{−λ−µ+n/r} ∫_{C(x,y)} det(w−y)^{λ−n/r} det(x−w)^{µ−n/r} × K_k(((w−y)⁻¹ + (x−w)⁻¹)⁻¹) f(w) dw intertwines the G̃-action."
- Corollary 4.4 (k = (l,…,l)) [txt:1000-1008]:
  > "Let λ, µ ∈ ℂ, l ∈ ℤ≥0, Re λ, Re µ > −l + n/r − 1. Then the map ℱ^{λ,µ}_{l↑}: 𝒪_{λ+µ+2l}(D) → 𝒪_λ(D) ⊗̂ 𝒪_µ(D), (ℱ^{λ,µ}_{l↑} f)(x,y) := det(x−y)^{−λ−µ−l+n/r} ∫_{C(x,y)} f(w) det(w−y)^{λ+l−n/r} det(x−w)^{µ+l−n/r} dw intertwines the G̃-action."

  C(x,y) is a totally real submanifold (Section 3, eq. (3.4)).
- Normalization, Theorem 5.1 (VT N30a; txt:2014-2034): "(ℱ^{λ,µ}_{k↑} v)(x,y) = B_r(λ,µ,k) K_k(x−y) v" under the same hypothesis Re λ, Re µ > −k_r + n/r − 1.
- Hilbert-space comparison, Corollary 5.2 (VT N30b; txt:2072-2082): requires "λ, µ ∈ ℝ, … λ, µ > 2n/r − 1".

**READING:** for SO_0(2,5), n/r − 1 = 3/2. So Corollary 4.3, Corollary 4.4 and Theorem 5.1 **do** hold at λ = μ = 5/2 for every k ∈ ℤ²_{++}, since 5/2 > −k₂ + 3/2. They hold as statements about G̃-intertwiners between the full spaces 𝒪(D), not as a unitary Hilbert decomposition. The unitary statements (Theorem 2.2, Corollary 5.2) need λ, μ > 4.

### 3d. Explicit SO(2,n) example?

**None.** The only worked example is "Example 4.5. Let p⁺ = Sym(r,ℂ), G = Sp(r,ℝ)" [txt:1011]. A grep for SO / ℂⁿ / Lorentz finds SO_0(2,n) only in the list of groups (txt:107) and in the description of Kobayashi–Pevzner's (SO_0(2,n), SO_0(2,n−1)) restriction case (txt:133). No type-IV tensor-product formula is written out.

---

## 4. Kobayashi–Pevzner, arXiv:1812.09733 — rank-one template (SL(2,ℝ)~ × SL(2,ℝ)~ ⊃ SL(2,ℝ)~)

### 4a. Conventions (quote first) — VT KP7a-c; txt:268-309

> "For λ ∈ ℤ we define a representation π_λ of SL(2,ℝ) on 𝒪(Π) by π_λ(g)f(z) = (cz + d)^{−λ} f((az+b)/(cz+d)) for g⁻¹ = (a b; c d). Viewed as a representation of the universal covering group SL(2,ℝ)~, the representation π_λ is well-defined for all λ ∈ ℂ."
>
> "For λ > 1 the weighted Bergman space ℋ²(Π)_λ := (𝒪 ∩ L²)(Π, y^{λ−2}dxdy) is nonzero … reproducing kernel K_λ(z,w) = ((λ−1)/4π)((z−w̄)/2i)^{−λ}"
>
> "π_λ (λ = 2, 3, ···) is referred to as a holomorphic discrete series representations of SL(2,ℝ), and π_λ (λ > 1) as a relative holomorphic discrete series representation of the covering group SL(2,ℝ)~."

λ is the modular weight: the kernel exponent, the same as Repka's T_n with n = λ. The Hardy space is λ = 1, the boundary of λ > 1.

### 4b. The decomposition — VT KP12a; txt:527-531

> "…discrete series representations π_λ′ and π_λ″ that decomposes into a multiplicity-free direct Hilbert sum of irreducible unitary representations when λ′, λ″ > 1 [22, 23]: (2.8) π_λ′ ⊗̂ π_λ″ ≃ Σ^⊕_{ℓ∈ℕ} π_{λ′+λ″+2ℓ}."

KP cite this; they do not prove it. [23] is Repka CJM 1979 and [22] is Molchanov 1980 [txt:2713-2716].

### 4c. Holographic operator and its hypotheses — VT KP9a-c; txt:369-409

> "Definition 2.1 … ℓ := ½(λ‴ − λ′ − λ″). Assume that (2.5) Re(λ′ + ℓ) > 0, Re(λ″ + ℓ) > 0, and ℓ ∈ ℕ. … (2.6) (Ψ^{λ‴}_{λ′,λ″} g)(ζ₁,ζ₂) := (ζ₁ − ζ₂)^ℓ / (2^{λ′+λ″+2ℓ−1} ℓ!) × ∫_{−1}^{1} g(((ζ₂ − ζ₁)v + (ζ₁ + ζ₂))/2)(1 − v)^{λ′+ℓ−1}(1 + v)^{λ″+ℓ−1} dv."
>
> "Theorem 2.2 … (1) The map Ψ^{λ‴}_{λ′,λ″}: 𝒪(Π) → 𝒪(Π × Π) intertwines the action of SL(2,ℝ)~ from π_λ‴ to the tensor product representation π_λ′ ⊗̂ π_λ″. (2) Moreover, if both λ′ and λ″ are real and greater than 1, then the linear map Ψ^{λ‴}_{λ′,λ″} induces an isometric embedding (up to rescaling) of the weighted Bergman space: ℋ²(Π)_λ‴ → ℋ²(Π × Π)_{(λ′,λ″)}."

The Parseval–Plancherel theorem (Theorem 2.7) and the projection formula (Corollary 2.8) are stated for "λ′, λ″ > 1" [txt:470, 538].

**Template structure (pinned):**
- The intertwiner exists for complex λ′, λ″ subject to (2.5).
- The unitary, multiplicity-free Hilbert decomposition is stated for λ′, λ″ > 1.
- Nakahama's Corollary 4.3/4.4 is the tube-type generalization, with the (2.5)-type condition becoming Re λ > −k_r + n/r − 1 [Nakahama txt:21, 105-111, 140-144]. For r = 1, n = 1 this is Re λ > −l, the same as KP's (2.5) in Nakahama's Theorem 1.2 restatement, "Re λ, Re µ > −l" [Nakahama txt:83].

---

## 5. Adjacent find (not requested): Ørsted–Zhang 1997, holomorphic ⊗ ANTI-holomorphic, analytic continuation

Conventions (VT OZ17a): "p = a(r − 1) + 2 + b be the genus … We let π_ν be the analytic continuation of holomorphic discrete series of a general bounded symmetric domain as defined in [FK]." For SU(2,2): "genus p = 4 … for ν ∈ {0,1} ∪ (1,∞) we still get a unitary representation … Wallach set" (VT OZ1c).

> "THEOREM 5.1. Let ν > (p−1)/2 and H(λ) be the principal series representation of G with parameter λ ∈ 𝔞*. We have the following decomposition formula for the tensor product π_ν ⊗ π̄_ν: π_ν ⊗ π̄_ν ≅ ∫^⊕_{𝔞*/W} H(λ) dλ" (VT OZ17b; txt:1045-1048)

They add: "It would be interesting to find out the decomposition of π_ν ⊗ π̄_ν for other (unitary) values of ν." (VT OZ17c)

**READING:** for type IV_5, a = 3, b = 0, r = 2, so p = 5 and (p−1)/2 = 2. Since ν = 5/2 > 2, Theorem 5.1 applies to H_{5/2} ⊗ \overline{H_{5/2}}: purely continuous spectrum and no discrete part. The ν normalization is FK's, the same as λ above; I did not cross-check this against a type-IV-specific source. This is the **conjugate** product, a different problem from H_λ ⊗ H_μ.

---

## 6. What is and is not pinned for λ = μ = 5/2 on SO(2,5)

**Pinned from primary text:**
- The discrete form H_λ ⊗̂ H_μ ≃ ⊕_{k∈ℤ^r_{++}} H_{λ+μ}(D, V^∨_{kγ}), which for r = 2 is k₁ ≥ k₂ ≥ 0 with scalar summands H_{λ+μ+2l} at k = (l,l). It is pinned only for λ, μ > 2n/r − 1 = 4, via Nakahama's restatement of Kobayashi 2008. Kobayashi's own text is PIN OWED.
- Repka 1979 covers only Harish-Chandra's holomorphic discrete series (condition (2)). It gives no type-IV formula and no analytic continuation.
- Nakahama's holographic intertwiners (Cor. 4.3, 4.4) and their normalization (Thm 5.1) are pinned with hypothesis Re λ, Re μ > −k_r + n/r − 1. For type IV_5 this reads > −k₂ + 3/2, which **includes 5/2**. They are intertwiners on the full holomorphic-function spaces 𝒪(D), not a proof of a unitary Hilbert decomposition.
- JV Corollary 2.6 gives the discrete Hilbert decomposition H(τ₁) ⊗ H(τ₂) = ⊕ₙ H(τ₁ ⊗ τ₂ ⊗ Sⁿ(p⁻)) for τᵢ ∈ I ∩ P. JV state for O(2,n+1) scalar modules that α > (n−1)/2 ⇒ α ∈ I ∩ P.

**Not pinned; my reading only:**
- **The one bridge that covers our point is not pinned as a single sentence.** With N = n+1 = 5, the JV bound is α > 3/2. So λ = 5/2 ∈ I ∩ P, and Corollary 2.6 would give H_{5/2} ⊗ H_{5/2} = ⊕_{k₁≥k₂≥0} H(χ_5 ⊗ V_k), discrete and unitary. Taking this as established requires four things:
  - my index translation;
  - identifying JV's α with the brief's λ;
  - the covering-group extension, since JV's (3.12) is written "for α ∈ ℤ";
  - accepting JV's "it is known" citation for the I ∩ P membership.
- The explicit K-type content of Sⁿ(p⁻) for type IV, "harmonic pieces" giving (k₁,k₂), is not written in any pinned source. The general form is Nakahama (2.3), citing FK Thm XI.2.4.
- Whether 5/2 is literally "the Hardy point" of the Lie ball is the brief's statement, not checked here.
- Multiplicity-one of each k and completeness of the Hilbert sum at λ = 5/2 are not stated for λ ≤ 4 by any pinned source except through the JV route above.
- **Pins owed** if this is to be closed from primary text:
  - Kobayashi 2008, Progr. Math. 255, Thm 8.4 and its exact λ range. It may be stated for the full unitary range; unverified.
  - A primary statement of the discrete hol ⊗ hol decomposition throughout the continuous Wallach range. Candidates: Peng–Zhang, or Kobayashi's multiplicity-free theorem for the pair (G×G, diag G). Neither is on disk.

---

## 7. New files in this directory

Checksums are in SHA256SUMS.txt.
- `repka_1979_cjm31.pdf`, `repka_1979_cjm31.txt`
- `orsted_zhang_1997_cjm49.pdf`, `orsted_zhang_1997_cjm49.txt`
- `crossref_10.4153_cjm-1979-079-9.json`, `crossref_10.4153_cjm-1997-060-5.json`, `crossref_search_repka.json`
- `VISUAL_TRANSCRIPTIONS.txt`
- PNGs: `repka_p1-1.png`, `repka_p3-3.png`, `repka_p7-7.png`, `oz_p-01.png`, `oz_p-17.png`, `jv_p-07.png`, `jv_p-24.png`, `nak_p-07.png`, `nak_p-08.png`, `nak_p-16.png`, `nak_p-17.png`, `nak_p-30.png`, `kp_p-07.png`, `kp_p-09.png`, `kp_p-12.png`
