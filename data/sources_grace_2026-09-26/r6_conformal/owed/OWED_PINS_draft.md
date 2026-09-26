# OWED PINS (draft) — r6_conformal / owed

Written 2026-09-26 11:57 EDT. Every pin below is a verbatim quote from a file in this
directory, cited as `file:line`. Text is pdftotext `-layout` output, so sub/superscripts
and fraction bars are displaced onto neighbouring lines; the quotes keep that layout and a
cleaned reading is given beside each one. Nothing here was pinned from a search snippet.
Web search was used only to FIND candidate arXiv ids. Every id was then downloaded and its
title checked in the saved `.abs.html`.

Tags: **PINNED** = verbatim in a saved primary. **INFERENCE** = my step from pinned text,
with the step shown. **PIN OWED** = paywalled, and only Crossref metadata is saved.

---

## 0. ID correction (verify-the-id)

- **arXiv:math/0607004 is NOT the requested paper.** Its saved abs page title reads
  `[math/0607004] Propagation of multiplicity-freeness property for holomorphic vector bundles`
  (`kobayashi_math0607004_propagation.abs.html`). Its jref is Progr. Math. 306 (2013) 113–140.
  I kept it anyway, because it is ref. [49] of the target paper and is cited there for the
  proof of Theorem 8.10 (see 1.4). grep of its text finds no so(n,2)/SO(n,2) statement.
- **The correct id is arXiv:math/0607002.** Its abs title reads
  `[math/0607002] Multiplicity-free theorems of the restrictions of unitary highest weight modules with respect to reductive symmetric pairs`,
  and its jref is `RIMS-1549 -- Progr. Math., 255 (2007), pages 45-109`
  (`kobayashi_math0607002.abs.html`).
- Crossref (`crossref_kobayashi_progrmath255_doi.json`): DOI 10.1007/978-0-8176-4646-2_3,
  container "Progress in Mathematics / Representation Theory and Automorphic Forms",
  pages 45-109, publisher Birkhäuser Boston, ISBN 9780817645052. The `issued` date is null.
  **Year discrepancy:** the arXiv jref says 2007 and the brief says 2008. Neither is pinned
  from the publisher. Cite the pages and DOI and leave the year as "2007 (arXiv jref) / 2008 (brief)".

---

## 1. Kobayashi, Progr. Math. 255, 45–109 (arXiv:math/0607002)

Files: `kobayashi_math0607002.{pdf,txt,abs.html}`

### 1.1 Conventions (quoted before any formula)

- Hermitian type and the characteristic element Z:
  `kobayashi_math0607002.txt:196` — "su(p, q) , sp(n, R) , so(m, 2) (m 6= 2) , e6(−14) , e7(−25) ." (so(m,2) with m ≠ 2)
  `:211-214` — "gC := g ⊗ C = kC ⊕ p+ ⊕ p− ... is the eigenspace decomposition of ad(Z) with eigenvalues 0, −1 and − −1," (i.e. 0, √−1, −√−1)
- Highest weight module / scalar type / holomorphic discrete series (Definition 1.3):
  `:229-237` — "We say (π, H) is a unitary highest weight representation of G if H_K^{p+} ≠ {0}. Then, π is of scalar type (or of scalar minimal K-type) if H_K^{p+} is one dimensional; π is a (relative) holomorphic discrete series representation for G if the matrix coefficient g 7→ (π(g)u, v) is square integrable on G modulo its center for any u, v ∈ H."
- Parametrisation: the parameter is a highest weight µ ∈ √−1 t*, not a scalar λ.
  `:2360-2364` — "If µ is the highest weight of V^{p+} , we write V as π^g_µ ... (π^g_µ)^{p+} ≃ π^k_µ . (8.1.3)"
  `:2448-2451` — "πµg is of scalar type, namely, (πµg)p+ is one dimensional, if and only if ⟨µ, α⟩ = 0 for any α ∈ ∆(k, t) . (8.3.1)"
  `:2453-2456` — "Furthermore, the representation πµG is a (relative) holomorphic discrete series representation of G if and only if ⟨µ + ρg , α⟩ < 0 for any α ∈ ∆(p+ , t) . (8.3.2)"
- The strongly orthogonal roots ν_j used in the sum, and their number l:
  `:2424-2432` gives the choice of ν_1, …, ν_l in ∆(p+^{−τ}, t^τ), and
  `:2442-2444` reads "Likewise, in light of (8.2.2) for the Hermitian symmetric space Gτθ/Gτθ ∩ K = Gτθ/Gτ,θ , we have l = R-rank gτθ ."

### 1.2 Theorem 8.3 — PINNED verbatim, with its hypotheses

`kobayashi_math0607002.txt:2462-2476`:
> Theorem 8.3. Let G be a non-compact simple Lie group of Hermitian type.
> Assume that µ ∈ √−1 t∗ satisfies (8.3.1) and (8.3.2). Let τ be an involutive
> automorphism of G of holomorphic type, H = Gτ0 (the identity component of
> Gτ ), and {ν1 , . . . , νl } be the set of strongly orthogonal roots in ∆(p−τ+, tτ) as
> in Subsection 8.2. Then, πµG decomposes discretely into a multiplicity-free sum
> of irreducible H-modules:
>     πµG |H ≃ Σ⊕_{a1≥···≥al≥0, a1,...,al∈N} π^H_{µ|tτ − Σ_{j=1}^{l} aj νj}   (discrete Hilbert sum). (8.3.3)

Section 8 scope statement, `:2298-2301`: "This section discusses an explicit irreducible
decomposition formula of the restriction π|H where the triple (π, G, H) satisfies the
following two conditions: 1) π is a holomorphic discrete series representation of scalar type (Definition 1.3)."

The proof also uses the discrete-series hypothesis, `:2866-2869`: "Since πµG is a (relative)
holomorphic discrete series representation of G, all irreducible summands in the
right-hand side must be (relative) holomorphic discrete series representations of H by Fact 5.1 (1)."

### 1.3 KEY QUESTION — what range of λ?

**Answer (PINNED): Theorem 8.3 is stated only for the holomorphic discrete series.** Its hypothesis
is (8.3.2) (`:2456`), and Section 8 is scoped to "a holomorphic discrete series representation of
scalar type" (`:2300`). The theorem does **not** cover the continuous Wallach range below the
discrete-series threshold.

What the threshold is for SO(2,n) with scalar parameter λ:
- **PINNED in a second Kobayashi primary** (Kobayashi–Pevzner, arXiv:1301.2111, Section 6, which works on the Lie ball):
  `kobayashi_pevzner_1301.2111.txt:3445-3448` — "Remark 6.4. If λ ∈ R and λ > n − 1, then H2 (X, Lλ ) ∶= O(X, Lλ ) ∩ L2 (X, Lλ ) is a non-zero Hilbert space on which G̃ acts unitarily and irreducibly, giving a holomorphic discrete series representation of G̃ modulo the center."
  Their λ convention, `:3361-3366`: "For λ ∈ Z we define a character of c(k) by tHo ↦ λt, and lift it to a character Cλ of K. ... the representation of G on O(X, Lλ ) is identified with the multiplier representation πλ ≡ πλG of the same group on O(X) given by (6.4) F (z) ↦ (πλ (g)F )(z) = J(g −1 , z)−λ F (g −1 ⋅ z)". For any λ ∈ C they pass to the universal cover G̃ (`:3376-3378`). The Lie ball is X (`:3351-3353`) and "G′ = SOo (n − 1, 2) acts on the subsymmetric domain Y ∶= X ∩ {zn = 0}" (`:3356-3357`).
- Remark 6.4 is a sufficiency statement ("If λ > n−1"). The claim that the scalar holomorphic
  discrete series is **exactly** λ > n−1 = p−1 is standard but is **not pinned here**. It agrees with
  `arxiv_2205.06786.txt:256-259`, where the weight (…)^{λ−n} dv "is finite on D^IV_n precisely for λ > n − 1".
  → **INFERENCE (not pinned as iff):** for n = 5, Theorem 8.3 covers λ > 4 only. It does **not** cover
  3/2 < λ ≤ 4, and in particular it does **not** cover the Hardy point λ = 5/2.

**Specialisation of (8.3.3) to (so(2,n), so(2,n−1)) — INFERENCE, with the steps shown:**
- (a) The pair is of holomorphic type. Table 3.4.1 row `kobayashi_math0607002.txt:1073` reads
  "so(2, n)   so(2, p) + so(n − p)"; take p = n−1.
- (b) l = R-rank g^{τθ} (`:2442-2444`). Kobayashi–Pevzner Table 2.1 (`kobayashi_pevzner_1301.2111.txt:2519-2528`) lists
  "so(n, 2)  so(n − 1, 2)  so(n − 1) ⊕ so(1, 2)" under "Split rank one irreducible symmetric pairs of holomorphic type".
  So l = 1.
- (c) Therefore (8.3.3) becomes π_µ|_H ≃ ⊕_{a≥0} π^H_{µ|tτ − a ν1}. Identifying −ν1 with a unit step in the
  scalar parameter gives π_λ| ≃ ⊕_{ℓ≥0} π_{λ+ℓ}. This identification is not in the source. It is
  consistent with Kobayashi–Pevzner Theorem 6.1(iii), `:3392-3397`: Hom ≠ 0 ⇔ "ν − λ ∈ N", for O(X,Lλ) → O(Y,Lν).
- (d) The sign convention differs between the two papers. Kobayashi 2007 uses ⟨µ+ρ, α⟩ < 0 (`:2456`).
  Kobayashi–Pevzner use "(4.5) ⟨λ − ρg , α⟩ > 0" (`kobayashi_pevzner_1301.2111.txt:2913`) with ind(−λ).
  Do not mix the two without pinning the map.

### 1.4 What covers the full unitary highest-weight range (below the discrete series)

- **Theorem 8.10 — PINNED.** It is abstract only: it gives no explicit formula and its proof is not given in the paper.
  `kobayashi_math0607002.txt:2947-2957`:
  > Theorem 8.10. If (g, h) = (u(p, q), u(1)+u(p−1, q)) or (so(n, 2), so(n−1, 2)),
  > then any irreducible unitary highest weight representation of G decomposes
  > discretely into a multiplicity-free sum of irreducible unitary highest weight
  > representations of H.
  > In contrast to Theorem A, the distinguishing feature of Theorem 8.10 is
  > that π is not necessarily of scalar type but an arbitrary unitary highest weight
  > module. ... We do not give the proof here that uses the vector bundle version of Theorem 2.2 (see [49]).
  > Instead, we give an explicit decomposition formula for holomorphic discrete
  > series π. The proof of Theorem 8.10 for the case (G, H) = (SO0 (n, 2), SO0 (n−1, 2)) can be also found in Jakobsen and Vergne [31, Corollary 3.1].
- Fact 5.1(1), `:1350-1360`: for τ of holomorphic type, "If π is an irreducible unitary highest weight
  representation of G, then π is (H ∩K)-admissible. ... The restriction π|H splits into a discrete Hilbert sum of irreducible unitary highest weight representations of H ... where the multiplicity mπ (µ) is finite for every µ."
- Theorem B(2) + Theorem A, `:286-314`: C(π) = 1 (multiplicity-free) "if π is of scalar type". This holds for any
  irreducible unitary highest weight π (no discrete-series hypothesis) when the pair is of holomorphic type.
- **Consequence (PINNED + INFERENCE):** At λ = 5/2 on SO(2,5)~ ↓ SO(2,4)~, the source gives discreteness and
  multiplicity-freeness (Theorem A/B, Fact 5.1, Theorem 8.10). The **explicit** summand list ⊕_{ℓ≥0} π_{λ+ℓ} is
  **not** stated in math/0607002 for non-discrete-series λ.
- Explicit full-range source = Jakobsen–Vergne, J. Funct. Anal. 34 (1979) 29–53, Cor. 3.1.
  **PIN OWED** (paywalled). Metadata is in `crossref_jakobsen_vergne_1979.json`: DOI 10.1016/0022-1236(79)90023-5,
  "Restrictions and expansions of holomorphic representations", JFA 34, 29-53, issued 1979-10.
  SECONDARY statement of its content: `kobayashi_math0607002.txt:2956-2957` (quoted above).
- Algebraic-level side note: Kobayashi–Pevzner Theorem 6.1 (`kobayashi_pevzner_1301.2111.txt:3392-3397`) holds for
  **all λ, ν ∈ C**: "Suppose λ, ν ∈ C. ... (i) HomG̃′ (O(X, Lλ ), O(Y, Lν )) ≠ {0}. (ii) dimC ... = 1. (iii) ν − λ ∈ N."
  This covers every λ, including 5/2, but it classifies symmetry-breaking operators between holomorphic section
  spaces. It is not a unitary Hilbert-sum decomposition. The unitary upgrade (Remark 6.4, `:3445-3452`) is stated only for λ > n − 1.

---

## 2. Wallach set, genus, Hardy and Bergman points, Szegő kernel for the Lie ball

### 2.1 Faraut–Korányi — PIN OWED (paywalled)

- Book: `crossref_faraut_koranyi_1994_ch13.json`. "Function Spaces On Symmetric Domains Of Tube Type", in
  "Analysis on Symmetric Cones", Oxford University Press, pp. 260-289, DOI 10.1093/oso/9780198534778.003.0013,
  ISBN 9780198534778 / 9781383025507, authors Jacques Faraut, Adam Korányi. **PIN OWED.**
- Paper: `crossref_faraut_koranyi_1990.json`. DOI 10.1016/0022-1236(90)90119-6, "Function spaces and reproducing
  kernels on bounded symmetric domains", JFA 88, 64-89, issued 1990-01. An open copy was tried via the
  ScienceDirect PDF URL and returned HTML only (deleted). **PIN OWED.**
- The content below is pinned from open secondary primaries (arXiv papers that state it).

### 2.2 General formulas — PINNED from Ding, arXiv:2206.05739

Files: `arxiv_2206.05739.{pdf,txt,abs.html}`. Title: "The biholomorphic invariance of essential
normality on bounded symmetric domains". Ding cites Upmeier [29] (Toeplitz operators and index theory, OT 81, 1996)
and Faraut–Korányi for these facts.

**Conventions:**
- The genus is defined through the Bergman kernel, `arxiv_2206.05739.txt:215-220` — "there exists a unique generic polynomial ∆(z, w) in z, w̄ and a numerical invariant N satisfying the property that the Bergman kernel of Ω is given by K_N(z, w) = ∆(z, w)^{−N} , (2.1) where the numerical invariant N is also called the genus of domain Ω, and the generic polynomial ∆(z, w) is also called Jordan triple determinant such that ∆(0, 0) = 1."
  (Kernel normalisation: ∆(0,0) = 1, and λ is the exponent in ∆^{−λ}.)
- n is the complex dimension, via the dimension count, `:274-282` — "r is the rank of Ω and a, b are two numerical invariants (nonnegative integers) associated with the joint Peirce decomposition ... such that the dimension count n = r + (a/2) r(r − 1) + br (2.3) holds and the genus N is given by N := 2 + a(r − 1) + b."
- The Wallach set is defined by positivity, `:304-307` — "The Wallach set WΩ with respect to Ω is defined to be the set consists of all λ ∈ C satisfying (λ)_m ≥ 0 for all integer partitions m ≥ 0, which is exactly the set of value λ such that ∆(z, w)^{−λ} is a positive kernel."
  Here (λ)_m = Π_j (λ − (j−1)a/2)_{m_j} (`:294-299`, eq. (2.4)).

**Formulas:**
- Wallach set, `:308-310` — "The Wallach set WΩ admits the following decomposition WΩ = WΩ,d ∪ WΩ,c where WΩ,d = {λ = (j − 1) a/2 , j = 1, · · · , r} and WΩ,c = {λ > (r − 1) a/2 }."
- Genus: p ≡ N = 2 + a(r−1) + b (`:282`), the same as (r−1)a + b + 2.
- Bergman and weighted Bergman, `:321-322` — "The weighted Bergman space A2 (dvγ ) coincides with H²_{N+γ}(Ω), γ > −1". So Bergman ↔ λ = N (γ = 0), consistent with (2.1).
- Hardy, `:322-324` — "and the classical Hardy space H 2 (Ω) defined in [29, Definition 2.8.4] coincides with H²_{n/r}(Ω)." (layout: "H 2n (Ω)" with "r" on line 324 = subscript n/r).
- Szegő, `:400-402` — "The Szegö kernel of Ω is given by S(z, ξ) = ∆(z, w)^{−n/r} , (z, w) ∈ Ω × S." (layout: "n" on 401 over "r" on 402).
- Weighted Bergman threshold, `:966-968` — "When λ > N − 1, it is trivial to equip the weighted Bergman spaces Hλ2 (Ω) with module actions ... since those inner products are induced by the integration with suitable probability measures."

### 2.3 Type IV invariants — PINNED from Quiroga-Barranco & Seng, arXiv:2205.06786

Files: `arxiv_2205.06786.{pdf,txt,abs.html}`. Title: "Commuting Toeplitz operators on Cartan domains of type IV and moment maps".

- Domain and dimension, `arxiv_2205.06786.txt:175-179` — "We will denote by D^IV_n the n-dimensional Cartan domain of type IV, which is given by D^IV_n = {z ∈ C^n | |z|^2 < 1, 2|z|^2 < 1 + |z^⊤ z|^2 }". At `:187-188`: "for every n ≥ 3, the bounded symmetric domain D^IV_n is irreducible".
- Group, `:216-217` — "D^IV_n ≃ SO0 (n, 2)/SO(n) × SO(2)".
- **Invariants**, `:223-225` — "In the notation of [25], the domain D^IV_n has genus n, rank 2 and characteristic multiplicities a = n − 2 and b = 0. In particular, the vanishing of the last value implies that D^IV_n is a bounded domain with a tube-type unbounded realization." ([25] = Upmeier 1996, `:1977-1978`.)
- Bergman kernel, `:248-252` — "K(z, w) = (1 − 2z^⊤ w̄ + (z^⊤ z)(w^⊤ w)‾)^{−n}". This is the genus exponent n with h(z,w) = 1 − 2z·w̄ + (z·z)(w·w)‾. (Bars are lost in the layout text; this reading is INFERENCE from the Bergman definition.)
- Weighted Bergman range, `:256-259` — "(1 − 2|z|^2 + |z^⊤ z|^2 )^{λ−n} dv(z) which is finite on D^IV_n precisely for λ > n − 1."

### 2.4 General-n formulas for type IV_n — INFERENCE (substituting 2.3 into 2.2)

With r = 2, a = n−2, b = 0, d = n:
- dimension check: 2 + (n−2)/2·2·1 + 0 = n ✓
- genus: 2 + (n−2)(1) + 0 = n ✓ (agrees with 2.3, pinned)
- Wallach: {0, (n−2)/2} ∪ ((n−2)/2, ∞)
- Hardy: ν = n/2
- Bergman: ν = n
- Szegő: h(z,w)^{−n/2}
- weighted Bergman / holomorphic discrete series: λ > n−1

### 2.5 Evaluation for IV_5 (r = 2, a = 3, b = 0, d = 5) — INFERENCE

No saved source states n = 5 itself. This is arithmetic substitution into pinned formulas.
- dimension: 2 + (3/2)(2)(1) + 0 = 5 ✓
- genus p = 2 + 3·1 + 0 = **5**
- Wallach set = {0, 3/2} ∪ (3/2, ∞)
- Hardy point ν = n/r = **5/2**. It lies in the continuous part, since 5/2 > 3/2.
- Bergman point ν = p = **5**
- Szegő kernel = h(z,w)^{−5/2}, with h(z,w) = 1 − 2z·w̄ + (z·z)(w·w)‾
- weighted Bergman / holomorphic discrete series: λ > 4

Link to item 1 (INFERENCE):
- The Hardy point 5/2 lies in (3/2, 4]. That is inside the continuous Wallach range but below the
  discrete-series threshold 4.
- So Kobayashi Theorem 8.3 does not reach λ = 5/2.
- Theorem 8.10 and Fact 5.1 (discrete and multiplicity-free) do reach it.
- The explicit ⊕_{ℓ≥0} π_{5/2+ℓ} rests on Jakobsen–Vergne Cor. 3.1. That pin is **OWED**.

**Convention caution (INFERENCE):** equating Kobayashi–Pevzner's λ (J^{−λ} multiplier, HDS for λ > n−1) with
Ding's λ (∆^{−λ} kernel, Bergman at λ = N = n, weighted Bergman for λ > N−1) is consistent at the discrete-series
threshold. It is not proven equal by a quoted map in these files. Pin the map (e.g. J(g,z)^2 ∝ Jacobian^{2/n}, or
the reproducing-kernel form of H²(X,Lλ)) before using the same λ across the two sources.

---

## 3. Owed list

1. Jakobsen–Vergne 1979, JFA 34:29–53, Cor. 3.1. This is the explicit branching SO0(n,2) ↓ SO0(n−1,2) for arbitrary unitary highest weight modules. PIN OWED (paywalled). Secondary: Kobayashi math/0607002 lines 2956-2957.
2. Faraut–Korányi 1990 JFA 88:64–89 and FK 1994 Ch. XIII. PIN OWED. Content pinned via Ding 2206.05739 and Quiroga-Barranco–Seng 2205.06786.
3. An "iff" statement that scalar HDS for SO(2,n)~ ⇔ λ > n−1. Remark 6.4 gives "if" only. The L²-finiteness iff (2205.06786:256-259) is for the measure, not for the discrete-series notion.
4. The publication year of Progr. Math. 255 (2007 per arXiv jref vs 2008 per brief). Crossref `issued` is null.
