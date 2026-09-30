# R25 pins: the Enright–Howe–Wallach (1983) normalization, and so(2,5) in it (draft)

Grace lane, 2026-09-30 (clock 11:08 EDT when writing began). Paths are relative to this directory unless they start with `../`. Every quote is verbatim from a `.txt` made by `pdftotext -layout` from a PDF saved on disk, cited as file:line. Where the text layer garbles a display, the page was rendered to `png/` and transcribed in `VISUAL_TRANSCRIPTIONS.txt` (VT-n). The retained instrument is `toy/r25_ehw_so25_normalizations.py`, with its output in `toy/r25_ehw_so25_normalizations.out`. No git.

Relation to R24: `../r24/R24_WALLACH_PINS_draft.md` already pinned the scalar and spinor lines of so(2,5) from the secondary sources. R25 (a) made the hard attempt on the original, which failed and is logged in Section 1; (b) adds one new primary restatement that covers so(2,2n−1) explicitly, PPST3 = arXiv:2412.06317; (c) pins EHW's own letters A(λ0) and "z < 0" through Dobrev; and (d) re-examines the "k ≥ 3" claim across every scale, including the lattice question, which R24 did not treat.

---

## Verdict up front

1. **The original EHW 1983 could not be reached as a file.** Every route failed; the log is in Section 1. **All EHW pins below are SECONDARY**: open restatements that name EHW (Thm 2.4, Prop. 3.1, Prop. 3.9, Section 5, Table). The EHW page numbers inside the original are **PIN OWED**.
2. **EHW's normalization, as restated (four independent open sources agree):**
   - β is the maximal (noncompact) root.
   - ζ is orthogonal to Δ(k) and normalized by (ζ, β∨) = 1.
   - λ = λ0 + zζ, with (λ0 + ρ, β∨) = 0, so **z = (λ + ρ, β∨)**.
   - The unitarity set on a line is Z(λ0) = (−∞, A(λ0)] ∪ {A(λ0) + c, A(λ0) + 2c, …, B(λ0)}. The notation A(λ0) = first reduction point is EHW's own letter, as quoted by Dobrev; BEHJ write a(λ0) and b(λ0).
   - Holomorphic discrete series ⟺ z < 0. Limits of holomorphic discrete series are at z = 0.
3. **so(2,5)** (the row so(2, 2n−1) with n = 3):
   - r = 2, c = 3/2, (ρ, β∨) = 4, h∨ = 5.
   - Scalar line λ = (−ν, 0, 0) gives z = 4 − ν.
   - Wallach points z ∈ {4, 5/2}, continuous part z < 5/2, i.e. ν ∈ {0} ∪ [3/2, ∞).
   - Hardy space at z = 3/2 (ν = 5/2). Genus 5 = h∨ = (ρ, β∨) + 1.
   - Holomorphic discrete series z < 0 ⟺ ν > 4.
4. **"Square-integrable for k ≥ (n_C − 1)/2 + 1 = 3":**
   - **No scale puts the L² threshold at 3.** The thresholds are:
     - z < 0 (EHW z);
     - ν > 4 (FK ν);
     - k > 8/3 (the BH scale k = ν/c);
     - k > 5/2 (the shifted scale k = ν − 3/2, i.e. distance below the first reduction point);
     - k > 8 (the doubled scale k = 2ν).
   - **Calibration in the other direction.** On the lattice ν ∈ ½ℤ, the first L² point ν = 9/2 has k = 3 in two scales: k = ν − 3/2 and k = ν/c. So "k ≥ 3 ⟹ square-integrable" is a TRUE sufficient statement on that lattice. On that lattice it is even sharp.
   - **In the shifted scale this is general.** k = (n_C + 1)/2 = (n_C − 1)/2 + 1 for every n_C (toy output). The formula in the corpus is exactly "the first half-integral L² point, measured from the Wallach point".
   - **Three limits on that reading:**
     - (i) It is a lattice statement, not a threshold. On the universal cover, ν > 4 is L², i.e. k > 5/2, so 5/2 < k < 3 is also L².
     - (ii) On the linear group SO_0(2,5) (ν ∈ ℤ), the first L² point is ν = 5, i.e. k = 7/2.
     - (iii) The ½ℤ scalar lattice is not Spin(2,5), because B3 weights are all-integer or all-half-integer. It is a double cover along the central SO(2).
   - **The corpus's own reading is "3 = the Wallach threshold k_min", i.e. the doubled scale, 2 × 3/2** (R24 `:277`). There 3 is the unitarity (Wallach) point, **not** an L² threshold. Under that reading the claim is **false**.
   - **Where 3 is literally EHW's L² start: so(4,2), not so(5,2).** Dobrev's EHW-based formula "k = A(λ0) + 1, …" gives HDS from k = 3 for so(4,2) (A = 2), and from k = 7/2 for so(5,2) (A = 5/2, INFERENCE).

---

## 1. Attempt log for the original (step 1). All routes failed

| Route | What was done | Result | File kept |
|---|---|---|---|
| Internet Archive | advancedsearch full-text for "unitary highest weight modules"; also for "Enright Howe Wallach" and the proceedings volume | 10 hits, all arXiv mirrors. The Park City volume is not there | `ia_search.json` |
| Wallach UCSD page | fetched `mathweb.ucsd.edu/~nwallach/` (curl -k: the server's certificate chain is incomplete), plus `preprints.html` and `old_preprints.html` | No EHW 1983. The file named `EHW.pdf` is **Enright–Hunziker–Wallach, "A Pieri rule for Hermitian symmetric pairs"** (2 pp.), a different paper. Old-preprint list: 1972–1999 items only; "analytic continuation of the discrete series II" (TAMS 1979) is listed there without a link | `wallach_home.html`, `wallach_preprints.html`, `wallach_old_preprints.html`, `wallach_EHW_pieri.pdf/.txt` |
| Springer | `link.springer.com/content/pdf/10.1007/978-1-4684-6730-7_7.pdf` | HTTP 200, but an HTML "Client Challenge" page, not a PDF. Paywalled | — |
| Unpaywall / Semantic Scholar | DOI 10.1007/978-1-4684-6730-7_7 | `is_oa: False`, `oa_status: closed`; S2 openAccessPdf status CLOSED | (API output shown in session) |
| Crossref | metadata | Progr. Math. 40 pp. 97–143; the Crossref link is Springer "similarity-checking" only | `../r24/crossref_ehw1983.json` |
| Howe (Yale), CiteSeerX | web search for an EHW PDF on .edu or citeseer | no hit; the search result names only Springer | — |
| Enright–Hunziker, Represent. Theory 8 (2004) 15–51 | DOI 10.1090/S1088-4165-04-00215-8, PDF URLs from Crossref (3 variants), plus browser headers and --http1.1 | **HTTP 403 bot challenge** on every ams.org URL; issue page 403 too. Wayback: 404 or 429. Unpaywall/S2: closed | `crossref_EH_exceptional.json`, `ams_ert_issue_403_challenge.html` |
| Enright–Hunziker, J. Algebra 2004 (DOI 10.1016/S0021-8693(03)00159-5) | Unpaywall says bronze OA at ScienceDirect; tried `/pdf`, `/pdfft`, the Elsevier API and CORE (outputs/81960103) | ScienceDirect 403; Elsevier API 400; CORE download 403. Not on arXiv (arXiv API au:Enright AND au:Hunziker returns 0) | `crossref_EH_determinantal.json`, `arxiv_api_enright_hunziker.xml` |

**Status: EHW 1983 original, PIN OWED. Enright–Hunziker 2004 (both), PIN OWED.** A human with a browser or institutional access is the path. The AMS ERT paper is free to read in a browser; only the automated fetch is blocked.

---

## 2. The normalization: EHW's line, ζ, z (step 2)

### 2.1 Bai–Hunziker (BH), arXiv:2409.16555 v1, printed p. 2 (VT-9)

`../r24/arxiv_2409.16555.txt:54-64`:
> "Let β denote the unique maximal noncompact root of ∆+ . Now choose ζ ∈ h∗ so that ζ is orthogonal to ∆(k) and (ζ, β ∨ )=1. … From [EHW83], L(λ) is a highest weight Harish-Chandra module if and only if λ ∈ Λ+ (k) … Then we can write λ = λ0 + zζ, with λ0 ∈ h∗ such that (λ0 + ρ, β)=0, and z = (λ + ρ, β ∨ ) ∈ R."

`:72-73`, eq. (1.1):
> "zk = (ρ, β ∨ ) + uk = (ρ, β ∨ ) − kc, for 0 ≤ k ≤ r. Here c is a real number associated with the Hermitian type Lie group GR , see Table 1."

### 2.2 Bai–Erickson–Hunziker–Jiang (BEHJ), arXiv:2512.08199 v1, Section 2.5, printed p. 9 (VT-4). **This source names EHW Thm 2.4**

`../r24/arxiv_2512.08199.txt:457-466`:
> "2.5. Unitary highest weight modules. Let L(λ) be a highest weight Harish-Chandra module. Let β be the unique maximal root in Φ+ . Choose ζ ∈ h∗ such that ζ is orthogonal to Φ(k) and satisfies (ζ, β ∨ ) = 1. Let ρ denote half the sum of positive roots in Φ+ . We may write λ = λ0 + zζ, where λ0 ∈ h∗ satisfies (λ0 + ρ, β ∨ ) = 0, and z = (λ + ρ, β ∨ ) ∈ R. Now we suppose that λ = λ0 + zζ ∈ h∗ is Φ+ (k)-dominant integral. Define Z(λ0 ) := {z ∈ R | L(λ0 + zζ) is unitarizable}. By Enright–Howe–Wallach [19, Thm. 2.4], the set Z(λ0 ) is given by the diagram shown in Figure 1."

`:472-474` and `:489-490` (the text continues after Figure 1 and Table 2):
> "Here, a(λ0 ) is the so-called first unitary reduction point and b(λ0 ) is the last unitary reduction point. Both of these reduction points depend on certain root systems associated with λ0 ; see [19] or [2]. The set Z(λ0 ) includes the ray ending at a(λ0 ), as well as certain reduction points between … a(λ0 ) and b(λ0 ) that are spaced at an interval of length c, whose value (from [19]) can be found in Table 2."

- Figure 1 (VT-4) shows Z(λ0) = (−∞, a(λ0)] ∪ {a + c, a + 2c, …, b}.
- Split rank, `:509-511`: "From Enright–Howe–Wallach [19, §5] or Enright–Joseph [22, §1.4], the split rank r of the root system Φ of gR is equal to the number of strongly orthogonal positive noncompact roots in Φ(p+ )".
- Dual Coxeter number, `:503-504`: "h∨Φ = (ρ, β∨) + 1".
- The last point b(λ0) is BEHJ Thm 2.24, citing [3, Thm 3.2], `:505-508`. It is not an EHW statement.

### 2.3 PPST2, arXiv:2305.15892 v2, printed p. 5 (VT-8). **This source names EHW Prop. 3.1**

`../r24/arxiv_2305.15892.txt:221-226`:
> "The shape of the [EHW] classification is given by certain lines in t∗ of the form (1.10) λ = λ0 + zζ, z ∈ R. Here ζ ∈ t∗ is orthogonal to ∆k and normalized so that 2⟨ζ,β⟩/⟨β,β⟩ = 1, where β as before denotes the unique maximal noncompact root of ∆+g . For a fixed λ, λ0 is defined as the point on the line λ + zζ, z ∈ R, such that ⟨λ0 + ρ, β⟩ = 0."

`:231-237`:
> "Let a be the smallest real number such that N (λ0 + aζ) is reducible. The corresponding λ is called the first reduction point. It follows by continuity that the Shapovalov forms on N (λ0 + zζ), z < a, are all positive definite and hence these modules are unitary. … [EHW] use this argument to prove unitarity of N (λ0 + zζ), z < a, and also of L(λ0 + aζ). See [EHW, Proposition 3.1]. To identify the point a they use Jantzen's criterion for irreducibility of generalized Verma modules."

### 2.4 Dobrev, arXiv:0712.4375 v5 (file in `../../sources_grace_2026-09-27/r13/`). EHW's own letters A(λ0) and the sign of z

Printed p. 4 (VT-6), `arxiv_0712.4375.txt:158-161`:
> "The unitary lowest weight generalized Verma modules are infinitesimally equivalent to holomorphic discrete series when d = d0 + kc0 , k = A(λ0 ) + 1, 2, . . ., c0 , A(λ0 ) ∈ IN , [4]. The GVMs with d = d0 + c0 A(λ0 ) are infinitesimally equivalent to the so-called limits of discrete series [4]."

- Here [4] = EHW (`:1144`).
- Footnote 6 (`:169-173`): "EHW [4] work with highest weight modules, thus, their ranges are limited from above, while we work with lowest weight modules …"
- The map to EHW's z, `:712-714`: "the unitarity parameter z of [4] is related to ours as: z = −d + d0 + A(λ0 )."

Printed p. 17 (VT-7), so(4,2) with j1 = j2 = 0, `:754-769`:
> "these cases correspond to c0 = 1 (see above). and A(λ0 ) = 2 in the terminology of [4] (the FRP is z = A(λ0 ) = 2). The point next to the FRP (z = 1 by [4]) … The next point with d = d00 + 2 = 3 + j1 + j2 , (z = 0 by [4]), fits the ERs … which contain limits of discrete series … Finally, the cases with integer d ≥ d00 + 3 = 4 + j1 + j2 (z < 0 by [4]) are realized by the ERs χ+pνn which contain the holomorphic discrete series".

What this pins (SECONDARY, attributed to EHW by name):
- EHW call the first reduction point **A(λ0)**, and it is a value of z.
- **z = 0 is the limit of holomorphic discrete series, and z < 0 is the holomorphic discrete series.**
- Cross-check with EHW's table (INFERENCE): so(2,4) = so(2, 2n−2) with n = 3 has (ρ, β∨) = 3 and c = 1. The scalar line gives z = 3 − d, so A = z1 = 2 at d = 1, z = 0 at d = 3, and z < 0 for d ≥ 4. This matches Dobrev line by line.

**Caveat on Dobrev's formula (VT-6).** It asserts c0, A(λ0) ∈ ℕ, and Dobrev's c0 is his own step. For so(4,2), c0 = 1 = EHW c. For so(2,5), A(λ0) = 5/2 is not an integer, so the formula as printed does not cover it. Dobrev treats n = 1, 3, 4 only (`:35`, `:102`).

### 2.5 The constants table "from [EHW83]"

BH Table 1 (printed p. 5, VT-3; `../r24/arxiv_2409.16555.txt:241-251`) and BEHJ Table 2 (printed p. 10, VT-5; `../r24/arxiv_2512.08199.txt:475-490`):

| g_R | r | c | (ρ, β∨) (BH) | h∨ (BEHJ) |
|---|---|---|---|---|
| su(p, n−p) | min{p, n−p} | 1 | n − 1 | n |
| sp(n, R) | n | 1/2 | n | n + 1 |
| so*(2n) | [n/2] | 2 | 2n − 3 | 2n − 2 |
| **so(2, 2n−1)** | **2** | **n − 3/2** | **2n − 2** | **2n − 1** |
| so(2, 2n−2) | 2 | n − 2 | 2n − 3 | 2n − 2 |
| e6(−14) | 2 | 3 | 11 | 12 |
| e7(−25) | 3 | 4 | 17 | 18 |

The two tables agree column by column, with h∨ = (ρ, β∨) + 1.

### 2.6 NEW this round: PPST3, arXiv:2412.06317 v2 (saved here). The explicit so(2, 2n−1) classification

Abstract, `arxiv_2412.06317.txt:14-17`:
> "In this paper, we complete the classification of the unitary highest weight modules for the remaining cases; i.e., universal covers of the Lie groups SOe (2, n), E6(−14) and E7(−25) ."

The EHW criterion, `:91-93`:
> "Proposition 1.3. [EHW, Proposition 3.9.] With the notation as above, L(λ) is unitary if and only if the inequality (1.2) holds strictly for any K-type µ ≠ λ of L(λ)."

(1.2) is "‖µ + ρ‖ ≥ ‖λ + ρ‖" (`:87-89`).

Section 3, printed p. 4 (VT-2), `:171-186`:
> "3. Classification for so(2, 2n − 1), n ≥ 2. In this case g is so(2n+1, C) and k is so(2n−1, C) plus a one-dimensional center. … the positive noncompact roots are {ǫ1 ± ǫj | 2 ≤ j ≤ n} ∪ {ǫ1 } So the half sum of all positive roots is ρ = (n − 1/2, n − 3/2, . . . , 1/2) … Integrality with respect to k amounts to λi − λj ∈ Z and and 2λi ∈ N for all 2 ≤ i, j ≤ n. The highest (noncompact) root is β = ǫ1 + ǫ2 ."

Theorem 3.5, printed p. 5 (VT-1), `:205-208`:
> "Theorem 3.5. Non-scalar modules are unitarizabile if and only if (3.4) holds. If the inequality is satisfied strictly, the modules are irreducible Verma modules. In the scalar case, unitarizable highest weight modules are the trivial module, the Wallach module (3/2−n, 0, . . . , 0) and irreducible Verma modules (λ1 , 0, . . . , 0), λ1 < 3/2−n."

- (3.4), spinor row: "λ1 ≤ 1 − n for λ = (λ1 , 1/2, . . . , 1/2)" (`:199`).
- Section 7.2 restatement, `:941-943`: "(λ1 , 0, . . . , 0), λ1 = 0 or λ1 ≤ 3/2 − n".
- λ1 is unconstrained by k-integrality (only i, j ≥ 2 appear). The group is the universal cover (`:23`: "Let G denote the universal cover of one of the Lie groups SOe (2, n), …"), so ν = −λ1 is real.

---

## 3. so(2,5) in EHW's normalization, and the FK translation (step 3)

The instrument `toy/r25_ehw_so25_normalizations.py` uses exact fractions and reproduces the table row from coordinates.

**Constants:**
- ρ = (5/2, 3/2, 1/2).
- β = ε1 + ε2 and |β|² = 2, so β∨ = β.
- ζ = ε1 (checked orthogonal to the four compact positive roots; (ζ, β∨) = 1).
- **(ρ, β∨) = 4, c = 3/2, r = 2, h∨ = 5, dim p+ = 5.** This matches the so(2, 2n−1) row with n = 3.

**Scalar line** λ = (−ν, 0, 0): **z = 4 − ν.**

**Anchors of the map ν = (ρ, β∨) − z = −λ1:**
- PPST3 Thm 3.5 with n = 3: Wallach module λ1 = −3/2, i.e. ν = 3/2 and z = 5/2 = z1.
- Trivial module: ν = 0 and z = 4 = z0.

**FK side** (already pinned in `../../sources_grace_2026-09-26/r6_conformal/owed/`):
- Quiroga-Barranco–Seng `arxiv_2205.06786.txt:223-224`: "the domain DIVn has genus n, rank 2 and characteristic multiplicities a = n − 2 and b = 0". For n = 5 that is genus 5 = h∨ = (ρ, β∨) + 1.
- Same file, `:256-258`: "(1 − 2|z|2 + |z ⊤ z|2 )λ−n dv(z) which is finite on DIVn precisely for λ > n − 1". This is the L² range, ν > 4.
- Ding `arxiv_2206.05739.txt:310`: "WΩ,d = {λ = (j − 1) a2 , j = 1, · · · , r} and WΩ,c = {λ > (r − 1) a2 }". Read as a/2; for a = 3, r = 2 this gives {0, 3/2} ∪ (3/2, ∞).
- Ding, same file, `:322-323`: "the classical Hardy space H 2 (Ω) … coincides with H 2n (Ω)". Read as H²_{n/r}; the Hardy space is at ν = 5/2.

**Consistency:** c = a/2 in every row (a = 2, 1, 4, n−2, 6, 8). The EHW spacing c is the FK half-multiplicity, so the discrete Wallach points (j−1)a/2 correspond to z_j = (ρ, β∨) − jc (INFERENCE from the two pinned tables).

| Point (scalar, so(2,5)) | EHW z = (λ+ρ, β∨) | FK ν = 4 − z | BH k = ν/c | shifted k = ν − 3/2 | doubled k = 2ν |
|---|---|---|---|---|---|
| trivial (z0, discrete) | 4 | 0 | 0 | −3/2 | 0 |
| (gap, non-unitary; e.g. ν = 1) | 3 | 1 | 2/3 | −1/2 | 2 |
| first reduction point A(λ0) = last discrete Wallach point (z1) | 5/2 | 3/2 | 1 | 0 | 3 |
| Hardy space | 3/2 | 5/2 | 5/3 | 1 | 5 |
| limit of HDS | 0 | 4 | 8/3 | 5/2 | 8 |
| HDS (L²) | z < 0 | ν > 4 | k > 8/3 | k > 5/2 | k > 8 |
| first L², ν ∈ ½ℤ | −1/2 | 9/2 | **3** | **3** | 9 |
| first L², ν ∈ ℤ (SO_0(2,5)) | −1 | 5 | 10/3 | 7/2 | 10 |

Harish-Chandra's condition, computed directly in the instrument, agrees with the z < 0 column: (λ + ρ, α) < 0 for all five α ∈ Δ(p+).

**Where EHW's scalar discrete points sit:** z ∈ {4, 5/2}, spacing c = 3/2, with B(λ0) = 4 and A(λ0) = 5/2. This is Z(λ0) = (−∞, 5/2] ∪ {4}.

---

## 4. "Square-integrable for k ≥ (n_C − 1)/2 + 1 = 3": does any EHW normalization give it?

1. **As a threshold, no.** In every scale above, the L² boundary is strict and not at 3: z < 0, ν > 4, k > 8/3, k > 5/2, k > 8. In EHW's own variable, L² starts at z < 0, and 3 is not a value of z where anything changes. z = 3 is the non-unitary gap point ν = 1.
2. **As the first lattice point, yes in two scales on one lattice.** On ν ∈ ½ℤ, the first L² point ν = 9/2 has k = 3 both for k = ν − 3/2 and for k = ν/c.
   - The shifted scale generalizes: k = (n_C + 1)/2 = (n_C − 1)/2 + 1 for every n_C (toy table, n_C = 3…9).
   - The BH-scale match is a coincidence at n_C = 5: (2n_C − 1)/(n_C − 2) = 3 only there.
   - So "square-integrable for k ≥ (n_C − 1)/2 + 1" is **true, but only as a statement about half-integral ν, measured from the Wallach point.**
3. **Limits of that reading:**
   - On the universal cover, the one PPST3 classifies with ν real, 5/2 < k < 3 is also L².
   - On SO_0(2,5), ν ∈ ℤ, the first L² point is k = 7/2.
   - The ½ℤ scalar lattice is not Spin(2,5), since (ν, 0, 0) with ν ∈ ½ + ℤ is not a B3 weight. It needs a cover along the central SO(2).
   - "(EHW 1983)" is not an attribution EHW support for any "k ≥ 3": EHW's statement is z < 0.
4. **The corpus's actual usage** (R24 `:277`: "ν = N_c = 3 (the Wallach threshold k_min)") is the doubled scale. There k = 3 is ν = 3/2, the first reduction point. **Under that reading "square-integrable for k ≥ 3" is false.** k = 3 is the end of the unitary continuous range, a GK-dimension-5 non-L² module, and L² needs k > 8.
5. **so(4,2) versus so(5,2).** Dobrev's EHW-based counting d = d0 + k c0 with k ≥ A(λ0) + 1 (VT-6) gives HDS from **k = 3** for **so(4,2)** (A = 2, c0 = 1; pinned at VT-7: HDS from d = 4 = d0 + 3). For so(5,2), the same counting (INFERENCE: A = 5/2, c0 = 1 on the integer-d lattice) starts at k = 7/2. A "k ≥ 3" carried over from so(4,2) conformal-group literature would be an n = 4 value.

**Bottom line for the ledger:**
- "k_min = 3 is the L² threshold (EHW)": **not supported by any EHW normalization.**
- "k ≥ 3 ⟹ L²": true in the shifted and BH scales **on the half-integral lattice only**. Such a claim must name the scale and the lattice, and cite EHW as "z < 0", not "k ≥ 3".

---

## 5. Owed

- EHW 1983 original: the Thm 2.4 statement, the definition of A(λ0), B(λ0) and c, and the page numbers. PIN OWED (paywalled; bot-blocked).
- Enright–Hunziker, Represent. Theory 8 (2004), Section 2 statement of EHW and its constants table. PIN OWED (AMS 403 for automated fetch; free in a browser).
- Enright–Hunziker, J. Algebra 2004. PIN OWED (bronze OA at ScienceDirect; 403 for automated fetch).
- The Hardy point in EHW's own variable (z = 3/2) is INFERENCE via the FK map. No EHW-normalized source names the Hardy space.
