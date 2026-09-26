# R10 pins (draft) — Flato–Fronsdal and its d-dimensional form; Maldacena–Zhiboedov / Alba–Diab higher-spin rigidity; slightly-broken anomalous dimensions

Grace, 2026-09-26 (`date`: Sat Sep 26 16:20 EDT 2026). All files are in this directory. Text layers come from `pdftotext -layout`; `file.txt:N` means line N of that text file. Where the text layer garbles a formula, the formula was read off a rendered page, and the reading is in `VISUAL_TRANSCRIPTIONS.txt` (V-numbers) with the PNG under `png/`. Pins come from numbered equations and body text only. The one abstract quoted is labelled as an abstract.

Sources on disk:

| file | paper |
|---|---|
| `crossref_FF_BF00400170.json` | Crossref metadata only: Flato & Fronsdal, "One massless particle equals two Dirac singletons", Lett. Math. Phys. 2 (1978) 421–426. **Text not obtained, so no pin is taken from it.** |
| `1410.7668.pdf/.txt` | Basile, Bekaert, Boulanger, "Flato–Fronsdal theorem for higher-order singletons" (JHEP 11 (2014) 131) |
| `hep-th_0404124.pdf/.txt` | Vasiliev, "Higher Spin Superalgebras in any Dimension and their Representations" |
| `hep-th_0508031.pdf/.txt` | Dolan, "Character formulae and partition functions in higher dimensional conformal field theory" |
| `1112.1016.pdf/.txt` | Maldacena & Zhiboedov, "Constraining conformal field theories with a higher spin symmetry" (arXiv v1) |
| `1510.02535.pdf/.txt` | Alba & Diab, "... higher spin symmetry in d > 3 dimensions" (arXiv v1) |
| `1307.8092.pdf/.txt` | Alba & Diab, "... in d = 4" (arXiv v2; superseded by 1510.02535, per 1510.02535 abstract) |
| `1204.3882.pdf/.txt` | Maldacena & Zhiboedov, "... slightly broken higher spin symmetry" (arXiv v1) |
| `1601.01310.pdf/.txt` | Giombi & Kirilin, "Anomalous dimensions in CFT with weakly broken higher spin symmetry" = JHEP 11 (2016) 068 |
| `crossref_JHEP11_2016_068.json`, `inspire_GK.json` | DOI to paper to arXiv mapping for item 5 |

Item 5 identification: Crossref gives DOI 10.1007/JHEP11(2016)068 as "Anomalous dimensions in CFT with weakly broken higher spin symmetry" by Giombi and Kirilin. INSPIRE maps that DOI to arXiv:1601.01310, and the arXiv PDF title page matches (`1601.01310.txt:6-13`). The Springer PDF URL returned HTML rather than the paper, so the pins use the arXiv v2 text. A guessed arXiv ID, 1609.09651, turned out to be an unrelated pendulum paper; it was discarded and nothing is pinned from it.

---

## 1. Flato–Fronsdal and the generalized theorem

### 1.0 Flato–Fronsdal 1978 itself
- The Crossref record (`crossref_FF_BF00400170.json`) confirms title, authors, Lett. Math. Phys. vol. 2, pp. 421–426, 1978.
- The text was not obtained, so there is **no verbatim pin from the original**.
- Secondary identification of its Rac and Di: Dolan footnote 4 (V6, `hep-th_0508031.txt:883-887`): "In the nomenclature of [6], the representations D^{(3)}_{[1;1/2]} and D^{(3)}_{[1/2;0]} correspond to the 'Di' and 'Rac' singleton representations, respectively." Here [6] = Flato–Fronsdal (`hep-th_0508031.txt:2441`). So Rac = (Δ = 1/2, spin 0) and Di = (Δ = 1, spin 1/2) of so(3,2).

### 1.1 Basile–Bekaert–Boulanger (arXiv:1410.7668)

**Conventions, quoted before any formula.**
- `1410.7668.txt:175-181`: "The rank of the orthogonal subalgebra so(d) ⊂ so(2, d) is denoted by r ... we will be only interested in so(2, d) representations with highest-weight Λ = (−∆, ~s), where ∆ is, in AdS_{d+1}/CFT_d language, the scaling dimension of the corresponding primary operator or the minimal energy of the corresponding bulk field".
  - So **d = boundary (CFT) spacetime dimension**, the bulk is AdS_{d+1}, and the algebra is written **so(2, d)**.
- `1410.7668.txt:192-193`: "We denote by V(∆, ~s) (resp. D(∆, ~s)) the generalised indecomposable (resp. irreducible) Verma module associated with the highest-weight Λ = (−∆, ~s)."
- Rac normalisation (V1, `1410.7668.txt:350-355`): "we call Di (resp. Rac) ℓ-lineton the irreducible so(2, d) module ... based on the lowest-energy states |(d+1)/2 − ℓ, 1/2⟩ (resp. the state |d/2 − ℓ, 0⟩). Indeed, for ℓ = 1 and d = 3 they correspond to the Di (resp. Rac) singleton of Dirac [1]."
  - So **Rac = D(d/2 − 1, 0)** and **Di = D((d−1)/2, 1/2)** (the ℓ = 1 case).
- Unitarity (V2, `1410.7668.txt:525-527`): the ℓ-linetons are unitary "only in the case ℓ = 1".

**The theorem.** BBB Sec. 4 contains one unnumbered "Theorem". Its displayed equations are numbered (4.24)–(4.27). See V2 and `1410.7668.txt:539-590`.

> "Theorem. The tensor product of two ℓ-linetons, scalar and spinor, decomposes as:
> (4.24) D(d/2 − ℓ, 0) ⊗ D(d/2 − ℓ, 0) ≅ ⊕_{k=1}^{ℓ} ⊕_{s=0}^{∞} D(s + d − 2k, s, 0),
> (4.25) D((d+1)/2 − ℓ, 1/2) ⊗ D(d/2 − ℓ, 0) ≅ ⊕_{t=1}^{2ℓ−1} ⊕_{s=1/2,3/2,...} D(s + d − t − 1, s, 1/2).
> In the cases d = 2r + 1, we have (4.26) D((d+1)/2 − ℓ, 1/2) ⊗ D((d+1)/2 − ℓ, 1/2) ≅ ⊕_{t=2−2ℓ}^{2ℓ−2} D(d − 1 − t, 0) ⊕ ⊕_{s=1}^{∞} ⊕_{m=0}^{r−1} D(s + d − 2ℓ, s, 1^m) ⊕ ⊕_{t=1}^{2ℓ−2} ⊕_{s=1}^{∞} ⊕_{m=0}^{r−1} 2D(s + d − t − 1, s, 1^m)"

Remark (`1410.7668.txt:644-652`): "the symbols ⊕ appearing in the theorem should be understood in the weak sense, i.e. either direct or semi-direct sums". This matters only for non-unitary ℓ > 1. At ℓ = 1 all modules are unitary (V2).

**Specialisation to so(2,5), d = 5, ℓ = 1.** This is my arithmetic on the quoted formulas, not a sentence in the paper.
- Rac = D(3/2, 0) and Di = D(2, 1/2).
- (4.24), where k = 1 only: **Rac ⊗ Rac = ⊕_{s≥0} D(s + 3, s)**. This matches the requested D(d−2+s, s) = D(3+s, s).
- (4.25), where t = 1 only: **Di ⊗ Rac = ⊕_{s=1/2,3/2,...} D(s + 3, s, 1/2)**.
- (4.26), with ℓ = 1 and r = 2:
  - The first sum is t = 0 only, giving D(4, 0).
  - The second sum gives D(s + 3, s, 1^m) for s ≥ 1 and m = 0, 1.
  - The third sum is empty, because its upper limit is 2ℓ − 2 = 0.
  - So **Di ⊗ Di = D(4,0) ⊕ ⊕_{s≥1} [D(s+3, s) ⊕ D(s+3, s, 1)]**.
- Cross-check: this agrees with Dolan (4.33) at r = 2 (below).

### 1.2 Vasiliev (hep-th/0404124), Sec. 8 "Generalized Flato-Fronsdal theorem"

**Conventions (a different d; note this).**
- `hep-th_0404124.txt:161-170`: "In this paper we will be mainly interested in the AdS_d case of g = o(d − 1, 2). The generators T^{AB} of o(M, 2) ... We will use the mostly minus convention with η^{00} = η^{M+1 M+1} = 1 and η^{ab} = −δ^{ab} ... The AdS_{M+1} energy operator is E = iT^{M+1 0}."
  - Here **d = bulk AdS dimension, M = d − 1 = boundary dimension**, and the algebra is written **o(M, 2)**, with the two timelike directions last.
  - **BBB's d = Vasiliev's M.**
- Singletons (`hep-th_0404124.txt:298-302`): "Type II is the case of boundary conformal fields which we will call singletons ... In this case, o(M, 2) acts as conformal group in M dimensions."
- Rac weight (V3, `hep-th_0404124.txt:1756-1759`): "(6.38) E_0^+ = (1/2)M − 1. This is the correct value for the conformal scalar in M dimensions".

**Statement** (V4, `hep-th_0404124.txt:1990-2011`):

> "Using (6.41) one finds that the lowest energies are (8.7) E_0 = s + M − 2, where s is a degree of the polynomial ψ_0(ā). Therefore (8.8) |Rac⟩ ⊗ |Rac⟩ = Σ_{s=0}^{∞} ⊕H(s + M − 2, s, 0, 0 ...). According to (1.7), the right hand side of this formula describes for M > 2 the direct sum of all totally symmetric massless spin s representations of the AdS_{M+1} algebra o(M, 2). As a result, the tensor product of the massless scalar representation of the conformal group in d − 1 dimensions with d > 3 is shown to contain all integer spin totally symmetric massless states in AdS_d, that extends the result of Flato and Fronsdal [1] to any dimension."

Di ⊗ Rac, eq. (8.9) (`hep-th_0404124.txt:2065-2077`): "|Di⟩^± ⊗ |Rac⟩ = Σ_{s=1/2,3/2...} ⊕H(s + M − 2, s, 1/2, 1/2, ...)^±". Di ⊗ Di is eq. (8.14) (`:2112-2139`).

Caveat pinned from the same section (`hep-th_0404124.txt:2016-2018`): "The spin zero field in the AdS_d HS multiplet has energy d − 3 which is different from the energy of conformal scalar (1/2)d − 1 beyond the case of d = 4." In this sentence d is the bulk dimension.

**At M = 5**, that is o(5,2) = so(5,2), AdS_6, d_Vasiliev = 6: (8.8) gives ⊕_s H(s + 3, s), identical to BBB (4.24) at d_BBB = 5.

### 1.3 Dolan (hep-th/0508031)

**Conventions.**
- `hep-th_0508031.txt:112-116`: "Starting from the Lie algebra for SO(d, 2), ... g_AB = diag.(1, ..., 1, −1, −1) ... for a, b = 1, ..., d".
  - So **d = boundary spacetime dimension** and the algebra is written **SO(d, 2)**.
- Free scalar (Rac) (V5, `hep-th_0508031.txt:672-676`): "For the free scalar case, for which Λ = (−r + 1/2, 0, ..., 0) is the highest SO(2r+3) weight ... (3.33)". This is d = 2r + 1 and Δ = r − 1/2 = d/2 − 1.
- `hep-th_0508031.txt:893-894`: "Free fields have conformal dimension ℓ + (1/2)d − 1".

**Statement, odd d = 2r + 1** (V7, `hep-th_0508031.txt:1307-1322`):

> "(4.34) D^{(2r+1)}_{[r;1/2]} D^{(2r+1)}_{[r−1/2;0]} = Σ_{q=0}^{∞} D^{(2r+1)}_{[2r+q−1/2; q+1/2, 1/2, ..., 1/2]}, along with (4.35) D^{(2r+1)}_{[r−1/2;0]} D^{(2r+1)}_{[r−1/2;0]} = Σ_{q=0}^{∞} D^{(2r+1)}_{[2r+q−1; q,0,...,0]}, which generalise similar formulae obtained in [6] to odd dimensions."

Di ⊗ Di (odd d) is (4.33). The even-d analogues are (4.24) and (4.26); Dolan says (4.26) "matches Vasiliev's result" (`:1195-1228`).

**At d = 5 (r = 2):** (4.35) gives D[3/2;0] ⊗ D[3/2;0] = ⊕_q D[3 + q; q]. Three independent sources give the same result: BBB, Vasiliev and Dolan.

---

## 2. Maldacena–Zhiboedov, arXiv:1112.1016 (J. Phys. A 46 (2013) 214011)

**Convention.** The CFT dimension is the spacetime dimension. Assumption (d) reads "three spacetime dimensions".

**The theorem**, verbatim from the body, Sec. 1 (`1112.1016.txt:91-110`; PNG `png/1112.1016_p3-03.png`). There is no numbered theorem; the paper states it as an assumptions and conclusions list:

> "Let us clearly state the assumptions and the conclusions.
> Assumptions :
> a) The theory is conformal and it obeys all the usual CFT axioms/properties, such as the operator product expansion, existence of a stress tensor, cluster decomposition, a finite number of primaries with dimensions less than some number, etc.
> a') The two point function of the stress tensor is finite.
> b) The theory is unitary.
> c) The theory contains a conserved current j_s of spin higher than two s > 2.
> d) We are in three spacetime dimensions.
> e) The theory contains unique conserved current of spin two which is the stress tensor.
> The theorem, or conclusion :
> There is an infinite number of even spin conserved currents that appear in the operator product expansion of two stress tensor. All correlation function of these currents have two possible structures. One is identical to that obtained in a theory of N free bosons, with currents built as O(N) invariant bilinears of the free bosons. The other is identical to those of a theory of N free fermions, again with currents given by O(N) invariant bilinears in the fermions."

Commentary from the same passage:
- On a′ (`:109-110`): "We spelled out a′) explicitly, to rule out theories with an infinite number of degrees of freedom, as in the N = ∞ limit of O(N) vector models".
- On d (`:120-122`): "Assumption d) should hopefully be replaced by d ≥ 3. Some of the methods in this paper have a simple extension to higher dimensions, and it should be straightforward to extend the arguments to all dimensions d ≥ 3."
- On e (`:126-133`): "The assumption of a unique stress tensor can also be relaxed, at the expense of making the conclusions a bit more complicated to state. It is really a technical assumption that simplifies the analysis. In fact, we actually generalize the discussion to the case that we have exactly two spin two conserved currents. ... We expect something similar for a larger number of spin two currents, but we did not prove it."
- On scope of the conclusion (`:135-148`): "we did not prove the existence of a free field operator φ, in the CFT"; "We are not making any statement regarding other possible odd spin conserved currents, or spin two currents that do not appear the operator product of two stress tensors."

---

## 3. Alba–Diab, arXiv:1510.02535 (JHEP 03 (2016) 044), with companion 1307.8092

**Convention.** d is the CFT spacetime dimension ("in d > 3 dimensions"). There is **no numbered theorem** (a grep for "theorem" finds only the Coleman–Mandula mentions and Wick's theorem). The statement is given in the Introduction and restated in Sec. 6.

**Statement, body text, Introduction** (`1510.02535.txt:88-96`):

> "In this paper, we will prove an analogue of the Coleman-Mandula theorem for generic conformal field theories in all dimensions greater than three. We will show that in any conformal field theory that (a) satisfies the unitary bound for operator dimensions, (b) satisfies the cluster decomposition axiom, (c) contains a symmetric conserved current of spin larger than 2, and (d) has a unique stress tensor in d > 3 dimensions, all correlation functions of symmetric currents of the theory are equal to the correlation functions of one of the following three theories - either the theory of n free bosons (for some integer n), a theory of n free fermions, or a theory of n free (d−2)/2-forms."

**Restatement, Sec. 6** (`1510.02535.txt:1459-1465`): "we have shown that in a unitary conformal field theory in d > 3 dimensions with a unique stress tensor and a symmetric conserved current of spin higher than 2, the three-point function of the stress tensor must coincide with ... free bosons, ... free fermions, or ... free (d−2)/2-forms. This implies that all the correlation functions of symmetric currents of the theory coincide with the those in the corresponding free field theory."

**Unique stress tensor** (`1510.02535.txt:1477-1486`): "We stress that our classification into the bosonic, fermionic, and tensor free field theories depends somewhat sharply on our assumption that a unique stress tensor exists. Other free field theories with higher spin symmetry exist in d > 3 dimensions, such as a theory of free gravitons. This theory, however, does not have a stress tensor ... our result also holds in the case of two stress tensors. We do not comment on the possibility of more than two stress tensors."

**d = 5 caveats, pinned directly:**
- Introduction (`1510.02535.txt:98-110`): "Note that in odd dimensions, the free (d−2)/2-form does not exist, and the status of our result is somewhat complicated. ... For every odd dimension d ≥ 7, we know that an infinite tower of higher-spin currents must be present [13], but in d = 5, it may be the case that there are not infinitely many higher spin currents. Assuming that the solution exists and there are an infinite number of higher spin currents, we show that the correlation functions ... may be understood as the analytic continuation of the correlation functions of the currents of the even-dimensional free (d−2)/2-form theory to odd dimensions."
- Sec. 2 (`:399-404`): the infinite-tower result "was proven in a different way in [13] for all dimensions other than d = 4 and d = 5, wherein they showed that there is a unique higher-spin algebra in d ≠ 4, 5". Here [13] = Boulanger–Ponomarev–Skvortsov–Taronna.
- Tensor-case paragraph (`:541-547`): "In d = 5, our technique shows that if there is a solution for the Ward identity in the tensor lightcone limit, then it is unique. We do not prove, however, that there is an infinite tower of higher spin currents or that there is exactly one current of every spin. ... Henceforth, we assume that our theory does indeed contain the infinite tower of higher-spin currents necessary for our analysis."
- Sec. 6 (`:1505-1507`): "In d = 5, it is not known if all the higher-spin currents must be present. Assuming they are present, our results also flow through in d = 5."
- Unitarity is essential (App. F, `:1992-2022`): the free Maxwell field in d > 4 "is a conformal field theory with higher spin symmetry, but it is non-unitary in dimension d > 4", and its ⟨TTT⟩ is a superposition of all three structures, eq. (F.3). "This demonstrates that unitarity is a necessary assumption for our result".

**Companion 1307.8092** (d = 4 only). Title "... in d = 4". Abstract, labelled as abstract (`1307.8092.txt:17-23`): "unitary conformal field theories with a unique stress tensor and at least one higher-spin conserved current in four dimensions ... one of three free field theories: the free boson, the free fermion, and the free vector field." It does not cover d = 5. 1510.02535 "supersedes the previous paper by the authors [1]" (abstract, V12), where [1] = 1307.8092 (`1510.02535.txt:2035`).

---

## 4. Maldacena–Zhiboedov, slightly broken, arXiv:1204.3882

**Convention.** d = 3 CFT, dual to AdS4 (Vasiliev and Chern–Simons-matter theories).

**Assumptions** (body, `1204.3882.txt:102-128`), in brief:
- "a CFT with a unique stress tensor and has a large parameter Ñ"
- an approximate Fock space of single-trace and multi-trace operators
- "It has a single spin two conserved current. In addition, it has a sequence of approximately conserved currents J_s, with s = 4, 6, 8, ···. These currents are approximately conserved, so that their twist differs from one by a small amount of order 1/Ñ
  **(1.1) τ_s = ∆_s − s = 1 + O(1/Ñ).**"
- "In addition, we have one single trace scalar operator."
- "the higher spin symmetry can be broken only by double trace operators via effects of order 1/Ñ".

**Anomalous-dimension pattern**, App. A (V8, `1204.3882.txt:1571-1586`):

> "(A.4) τ_4 − 1 = (32/(21π²)) (1/Ñ) λ̃²/(1 + λ̃²). This formula should be applied to O(N) theory. For general group and arbitrary spin s we expect the following formula to be true (A.5) τ_s − 1 = a_s (1/Ñ) λ̃²/(1 + λ̃²) + b_s (1/Ñ) λ̃²/(1 + λ̃²)², where a_s and b_s are some fixed numbers. ... we have used the formula for the anomalous dimensions for the critical O(N) theory given in eqn. (2.20) of [35]. Thus, we fixed the overall coefficient in (A.4) so that the λ̃ → ∞ limit matches [35]. This also fixes a_s = (16/(3π²)) (s−2)/(2s−1)."

Status notes:
- (A.5) is stated as "we expect", so it is **not proved**.
- The normalisation of a_s is imported from the critical O(N) result [35].
- (5.6) (`:1192-1195`) repeats (A.4) in the body.

**Higher-d remark** (Sec. 5.6, `1204.3882.txt:1394-1413`): "the unitarity bound for the scalar operators is (d−2)/2. And, thus, if we restrict our attention to unitary theories, the equation (5.13) can be only valid in d ≤ 6 ... the scenario that we considered in d = 3 is impossible to realize in d = 4. In d = 5 it seems possible to realize the scenario via the UV fixed point of a −(φ·φ)² theory. This is a sick theory because the potential is negative, but one would probably not see the problem in 1/N perturbation theory. In d = 6 we do not know whether there is any example."

---

## 5. Giombi–Kirilin, JHEP 11 (2016) 068 = arXiv:1601.01310

**Conventions.**
- d is the CFT spacetime dimension (`1601.01310.txt:51-52`: "The spectrum of a d-dimensional conformal field theory ... a representation R of SO(d)").
- (1.1) ∆_s ≥ d − 2 + s (`:60`).
- (1.5) ∆_s = d − 2 + s + γ_s (`:97`).
- `:158-161`: in large-N vector models "∂·J_s = (1/√N) Σ JJ (1.7). This implies that the anomalous dimensions are γ_s ∼ O(1/N)".

**Large-N critical O(N), general d, singlet currents** (V9, `1601.01310.txt:966`):

> (4.16) γ_s = 2γ_φ · [1/((d/2 + s − 2)(d/2 + s − 1))] · [(s − 1)(d + s − 2) − Γ(d+1)Γ(s+1)/(2(d−1)Γ(d+s−3))]

Non-singlet (4.13): γ_{s(ij)} = 2γ_φ (s−1)(d+s−2)/((d/2+s−2)(d/2+s−1)).

**Large-s, general d** (V10, `1601.01310.txt:971-986`):

> (4.17) γ_s = 2γ_φ − 2γ_φ (Γ(d+1)/(2(d−1))) (1/s^{d−2}) − 2γ_φ (d(d−2)/4)(1/s²) + ...
> "We see a tower of higher spin currents (1/s^{d−2}) in the singlet channel, as well as the σ (1/s²) in both the singlet and the traceless parts."

So in the large-N O(N) model in general d, **γ_s does not grow like log s**. It tends to the constant 2γ_φ, with power-law corrections 1/s^{d−2} and 1/s². At d = 5 the tower term is 1/s³. That last step is my substitution; the paper does not state it.

**Where log s appears.** It appears only (a) at d = 2 + ε and (b) at subleading order at Wilson–Fisher.
- NLSM, d = 2 + ε (V11, `1601.01310.txt:1454-1466`): "(6.17) γ_s = (ε²/(N − 2)) (1/s − 1/2 + H_{s−2}) where H_k = Σ_{n=1}^{k} 1/n is the harmonic number ... In the large spin limit, we see the logarithmic behavior (since H_k ∼ log(k) at large k) (6.18) γ_s = (ε²/(N − 2)) (log(s) + γ − 1/2 − 1/(2s) + O(1/s²))."
  - (6.19) shows that this log is the d → 2 limit of the 1/s^{d−2} term in (4.17): "(6.19) γ_s = ε/N − (ε/N)(Γ(3+ε)/(2(1+ε)))(1/s^ε) + ... = (ε²/N) log(s) + ...".
- Wilson–Fisher, d = 4 − ε (`1601.01310.txt:1527-1532`): "(7.4) γ_s = 2γ_φ − (N + 2)(12π²λ² + (N + 8)λ³(log(s) − γ − 5/2))/(256π⁶ s²) + O(1/s³). We see that a logarithmic term arises at subleading order in the coupling constant". Here the log multiplies 1/s², so γ_s still tends to 2γ_φ.

(`1601.01310.txt:1015-1016`: the cubic models in d = 6 − ε "provide a 'UV completion' of the large N UV fixed points of the O(N) model in d > 4". This is relevant to the d = 5 use of (4.16) and (4.17).)

---

## 6. Does the MZ/AD theorem apply at d = 5, and is its unique-stress-tensor hypothesis stated as such?

- **Maldacena–Zhiboedov (1112.1016): no, not at d = 5.**
  - Hypothesis (d) is literally "We are in three spacetime dimensions" (`1112.1016.txt:99`).
  - The authors only hope it "should hopefully be replaced by d ≥ 3" (`:120`).
  - The unique stress tensor is stated as hypothesis (e): "The theory contains unique conserved current of spin two which is the stress tensor" (`:100`).
  - The authors call it "really a technical assumption" and prove a two-stress-tensor extension (`:126-133`).
- **Alba–Diab (1510.02535): only conditionally at d = 5.**
  - The result is stated for "d > 3", which formally includes 5.
  - For d = 5 the paper says explicitly that the infinite tower of higher-spin currents is **not proved**. The d ≥ 7 tower comes from Boulanger–Ponomarev–Skvortsov–Taronna, which excludes d = 4, 5. The paper **assumes** the tower (`:104-110`, `:541-547`, `:1505-1507`).
  - The third (tensor) structure, the (d−2)/2-form, "does not exist" as a free field in odd d. Even if a solution exists (then it is unique), its realisation is unknown.
  - So at d = 5 the pinned content is: free boson or free fermion, or an unrealised tensor structure, **conditional on the infinite tower being present**.
- **Unique stress tensor in AD:** stated as hypothesis (d), "has a unique stress tensor in d > 3 dimensions" (`1510.02535.txt:92`). Sec. 6 says the classification "depends somewhat sharply" on it, and that it extends to two stress tensors (`:1477-1486`).
- **Unitarity:** also a hypothesis in AD (a) and MZ (b). AD App. F shows it is necessary: the non-unitary d > 4 Maxwell field violates the conclusion.
- **Alba–Diab 1307.8092:** d = 4 only; it does not cover d = 5.

## 7. Convention crosswalk (for the so(5,2) / D_IV^5 reader)

| source | "d" means | algebra written | Rac lowest weight | at the case so(5,2) |
|---|---|---|---|---|
| BBB 1410.7668 | boundary CFT dim (bulk AdS_{d+1}) | so(2,d) | D(d/2 − 1, 0) | d = 5; Rac = D(3/2,0); Rac⊗Rac = ⊕D(s+3,s) |
| Vasiliev hep-th/0404124 | **bulk** AdS_d dim; M = d−1 = boundary | o(M,2) = o(d−1,2), mostly-minus, timelike last | E_0 = M/2 − 1 (6.38) | M = 5, d_V = 6; ⊕H(s+3,s) (8.8) |
| Dolan hep-th/0508031 | boundary CFT dim | SO(d,2), g = diag(1..1,−1,−1) | [r − 1/2; 0], d = 2r+1 | r = 2; ⊕D[3+q;q] (4.35) |
| MZ / AD / GK | CFT spacetime dim | (conformal group of the d-dim CFT) | n/a | d = 5 |

- so(2,d) and so(d,2) are the same real Lie algebra, with the timelike pair written first or last.
- **Vasiliev's d is one larger than everyone else's.** His "d > 3" means boundary dimension > 2.

## Not pinned / owed
- The Flato–Fronsdal 1978 original text is paywalled; only metadata is on disk. The Rac/Di identification comes via Dolan footnote 4.
- The Vasiliev PLB paper "Nonlinear equations for symmetric massless higher spin fields in (A)dS(d)" (hep-th/0304049) was not fetched. hep-th/0404124 Sec. 8 is the d-dimensional FF statement.
- The JHEP published version of Giombi–Kirilin was not obtained (the Springer URL returned HTML). The arXiv v2 is pinned. Equation numbers between arXiv and JHEP have not been cross-checked.
