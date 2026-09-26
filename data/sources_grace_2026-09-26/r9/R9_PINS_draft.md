# R9 pins (draft): HPPS contact-term spin truncation, φ⁴ γ(n,0), GFF double-trace spectrum, Labriet 2004.14012 scope

Grace, 2026-09-26 15:53 EDT (from `date`). DRAFT. Nothing here has been committed.

Directory: `data/sources_grace_2026-09-26/r9/`. Every PDF was fetched from arxiv.org/pdf/<id> and converted with `pdftotext -layout`. Line numbers `file.txt:N` point into that text. Formulas the text layer garbles were read off rendered pages (`png/`) and are written out in `VISUAL_TRANSCRIPTIONS.txt` as entries [V1]–[V12]. Check instrument: `check_r9_gamma.py`, output in `check_r9_gamma.out`.

---

## Conventions (quoted before any formula)

**HPPS (arXiv:0907.0151):**
- **d is the boundary CFT spacetime dimension. The bulk is AdS_{d+1}.** "Let us consider Euclidean AdSd+1 defined by the hyperboloid" (`0907.0151.txt:1218`), "embedded in (d + 2)-dimensional Minkowski spacetime" (`:1243`). "Our analysis was limited to CFTs in d = 2 and in d = 4." (`:2002`)
- **Δ** is the dimension of the single scalar O: "the only low dimension single-trace operator is a scalar O of dimension ∆" (PDF p11, [png/HPPS_p11]). The paper assumes a Z₂ symmetry O → −O. "We normalize O to be 1/N times a trace of adjoint variables, so that the two-point function and disconnected four-point function are of order N⁰" (`:456`).
- **n and l** index the double-trace primaries (3.3) `O_{n,l} ≡ O ∂↔_{µ1}…∂↔_{µl}(∂↔_ν ∂↔^ν)^n O − traces` (`:451`). "This has spin l and dimension ∆n,l = 2∆+2n+l+O(1/N²)." (`:453`)
- **γ normalisation**, eq (3.9) (`:540`): `∆(n,l) = 2∆ + 2n + l + (1/N²) γ₁(n,l) + …`, and eq (4.4) sets `γ(n,l) = γ₁(n,l)`. So γ is the coefficient of 1/N². The overall size of any contact solution (γ(0,0), or the coupling in Sec. 5) is left free. (5.5): "the bulk to boundary propagator … (−2P·X)^{−∆}, up to a normalization constant that will not be important for us".
- **p(n,l)** "is the square of the OPE coefficient", (`:495`), with blocks normalised as in (3.5)–(3.7) [V1]. Each block goes as (zz̄)^{E/2} at leading order.
- **"2k derivatives"** means the bulk quartic vertex has 2k derivatives (Fig. 2 caption, `:691`, and the text under (6.3)).

**Fitzpatrick–Kaplan (arXiv:1112.4845):** "the spacetime dimension in the CFT is 2h" (under eq (42), [V9]). So h = d/2, with d the boundary dimension. Spin is written ℓ, which the text layer renders as "`".

---

## 1a. HPPS: bulk quartic contact with bounded spin/derivatives ↔ CFT solutions with truncated spin

**Setup and statement (Sec. 4.1, printed pp. 12–13):**
- `0907.0151.txt:587`: "A λφ4 bulk interaction, or any quartic interaction with additional derivatives, will provide a solution (a trilinear interaction is forbidden by the Z2 symmetry)."
- `:606–609`: "As we will show in Sec. 5, an interaction with 2k derivatives in the bulk corresponds to perturbations p1(n,l), γ1(n,l) growing as n^{2k+const.} in the CFT. Thus we could count the number of solutions whose large-n behavior is bounded by a given power, and compare with the number of interactions with the corresponding number of derivatives."
- `:611–621` **(the truncation statement)**: "In fact it will be simpler to look at the spins of the intermediate states. The interaction φ4 destroys and creates only two-particle states of spin 0, and so the corresponding p1(n,l), γ1(n,l) are nonzero only for l = 0. The interaction φ2φ;µνφ;µν creates and destroys two-particle states of spin 0 or 2, as does φ2φ;µνσφ;µνσ (note that the spin must be even, by Bose symmetry). Thus, we will count bulk interactions according to the maximum spin that they can couple to, and similarly will count CFT solutions by the maximum value of l for which the perturbation is nonzero."
- `:624–637` (bulk count): "… Thus the operator couples to maximum spin 2a. In all, there are a + 1 interactions of maximum spin 2a. These have 2k derivatives, for k = 2a, 2a + 1, . . . , 3a. The total number of interactions with spin at most L is then Σ_{a=0}^{L/2}(a + 1) = (L + 2)(L + 4)/8."
- Fig. 2 caption (`:691–693`): "Quartic interactions of spin l = 2a and with 2k derivatives. There are 1 + a interactions of even spin l = 2a, with the number of derivatives given by k = 2a, 2a+1, . . . , 3a. The total number of interactions with spin at most L is (L + 2)(L + 4)/8."

**Where the truncation enters the equations (Sec. 4.2, d = 2):**
- `:718–719`: "we introduce at this point the restriction explained in the previous subsection, that l is bounded above by some given L, in order to exclude additional ln(1 − z) behavior. In Sec. 7 we will see that this is not actually necessary."
- The truncated crossing equations are **(4.5), (4.7) and (4.11)**, each summed over `l = 0 … L, l even`. (4.11) (`:789`, [png/HPPS_p17]): `Σ_{l=0,even}^{L} γ(p,l)J(p+l,q) + Σ_{l=2,even}^{L} γ(p−l,l)J(p−l,q) = (p ↔ q)`.
- Upper bound (`:855–859`, Fig. 3 at `:849–852`): "number of free parameters is Σ_{p=0}^{L/2}(L/2 + 1 − p) = (L + 2)(L + 4)/8 … Thus there are at most (L + 2)(L + 4)/8 solutions to the crossing condition with maximum spin L."
- **Match (`:861–865`):** "This is the same as our count of interactions in Sec. 4.1: our upper and lower bounds agree. We can conclude that the total number of solutions of the crossing relations is exactly equal to the number of bulk interactions, and our conjecture is true for interactions restricted to bounded L."
- d = 4 (Sec. 4.4, `:1113–1114`, (4.32)): "As the counting is the same as in two-dimensions, we again have that there are at most (L + 2)(L + 4)/8 solutions to the crossing relation with maximum spin L."
- Abstract (`:32–36`) and intro (`:66–67`): "For solutions whose intermediate spins are bounded above we show by a counting argument that our conjecture holds. We obtain some explicit solutions in d = 2 and d = 4."

**Explicit bulk check (Sec. 5.1):**
- `:1285–1287`: "A quartic interaction with only 2 derivatives does not generate a new four-point function … The first new contribution comes from an interaction vertex with 4 derivatives, (∇φ)²(∇φ)²." For (5.12): "The expansion only contains partial waves with spin 0 and 2" (`:1317`). The same holds for the 6-derivative vertex (5.15) (`:1349–1350`). `:1355–1356`: "solutions to the CFT constraints are in one-to-one correspondence to local bulk interactions, in agreement with our conjecture."

**Precision note on "L derivatives vs 2k derivatives".** HPPS never say "at most L derivatives ⇒ γ only for l ≤ L". They index by **maximum spin L** (L even). A spin-L interaction has 2k derivatives with k ∈ {L, …, 3L/2}, where L = 2a and k = 2a…3a. The minimum-derivative interaction at spin L has 2L derivatives (`:905–906`: "the result (4.16) corresponds to bulk interactions of spin L and with 2L derivatives, i.e. the leftmost box in each row in Fig. 2"). **The correct statement:** a quartic contact vertex with 2k derivatives produces γ(n,l) ≠ 0 only for even l ≤ L_max(k), and L_max ≤ k. The paper states this as maximum spin 2a ↔ k ∈ [2a, 3a] (`:633–635`). φ⁴ (k = 0) gives l = 0 only. Scope: the counting is proved in **d = 2 and d = 4 only**. Sec. 7 argues, but does not prove, that the unbounded-L solutions are convergent sums of bounded ones (`:864`).

---

## 1b. HPPS: φ⁴ (no-derivative contact) anomalous dimension γ(n,0)

**What HPPS give explicitly:**
- **d = 2, eq (4.13)** (`:804`, [V3]): `γ(p,0) = γ(0,0) J(0,p)/J(p,0) = γ(0,0) (2∆−1)/(2∆+2p−1)`. "Thus there is at most one solution for γ(n,0) when L = 0, determined up to the overall normalization γ(0,0)" (`:807–808`). "Thus there is exactly one solution with L = 0" (`:819`).
- **d = 4, eq (4.34)** (`:1133–1135`, [V6]): "The relation is solved by `γ(p,0) = (2∆+p−3)(p+1)(∆+p−1)(2∆−1) / [(∆−1)(2∆+2p−3)(2∆+2p−1)] · γ(0,0)`". Footnote 17 adds: "the case ∆ = 1 in d = 4 is special".
- These are identified with φ⁴ at `:1282–1283`: "In both d = 2 and d = 4 we recover the unique solution with L = 0 found in the previous section, Eqs. (4.13) and (4.34) respectively." This refers to the D-function (5.7), `(zz̄)^∆ A1 ∝ D̄_{∆∆∆∆}(u,v)`.
- **General d, only as the product p₀γ at maximal spin, eq (5.44)** (`:1571`, [V7], Sec. 5.2 "Regge limit"), for the vertex φ²(∇²)^kφ² with even k and k = L (`:1413`, `:1528`):
  `p0(n,L)γ(n,L) = π^{d/2} 2^{2L} Γ(2∆+2n+L−1) Γ²(2∆+n+L−d/2) Γ⁴(∆+n+L) / [Γ⁴(∆) Γ²(1+n) Γ(2∆+2n+L−d/2) Γ(2∆+2n+2L) Γ(2∆+2n+2L−1)]`.
  L = k = 0 is φ⁴. HPPS then divide by p₀ **only for d = 2 ((5.45) via (4.2)) and d = 4 ((5.46) via (4.29))**. They give no general-d p₀(n,l), so **no general-d γ(n,0) formula appears in HPPS.**
- **Answer to the question:** the explicit γ(n,0) is given for d = 2 and d = 4 only. General d appears only as p₀γ in (5.44).

**Combination (NOT a pin; flagged as derived).** Divide (5.44) at L = 0 by the general-d p₀(n,0) = [1+(−1)⁰]·(c̄_{n,0})² from FK (42) with Δ₁ = Δ₂ = Δ, calC = 1, h = d/2. This gives a general-d γ(n,0). `check_r9_gamma.py` tests the combination:
- d = 2: (4.2) = 2·FK(42) exactly, and (5.44)/(4.2) = (5.45) exactly. Matches the shape of (4.13) (ratio 1 to 1e-20, Δ ∈ {1.7, 2.5, 3.3}, n = 0..4).
- d = 4: the n-shape matches (4.34) exactly.
- n-shape at Δ = 5/2, γ(n,0)/γ(0,0) for n = 0..4:
  - d = 5: 1, 2.604, 5.234, 8.832, 13.393
  - d = 4: 1, 5/3, 7/3, 3, 11/3, which equals (4.34)
  - d = 2: 1, 2/3, 1/2, 2/5, 1/3, which equals (4.13)

  This is a derived combination of two sources. Its overall normalisation is arbitrary (coupling), as it is in HPPS.

**⚠ Normalisation flag in HPPS d = 4 (factor 2). Not a ruling. Check before using absolute d = 4 values.** (4.29) as printed ([V5]) gives p₀(0,0) = 4. But (3.10) + (4.1) require p₀(0,0) = 2: the leading term of (zz̄)^Δ A₀ is 2(zz̄)^Δ, and the l = 0 block (3.7) → (zz̄)^{E/2}. The d = 2 formula (4.2) gives 2, and 2·FK(42) at h = 2 gives 2. Consistent with this, (5.46) = (5.44)/[(4.29)/2] and not (5.44)/(4.29) (`check_r9_gamma.out`, the "vs (5.46)=0.5" column). So either (4.29) carries an extra factor 2 as printed, or I have a transcription slip. The PNG was re-read and the transcription looks correct. The n-dependence (shapes) is unaffected.

---

## 2. Generalized-free-field double-trace spectrum Δ = 2Δ_φ + 2n + l; even l for identical scalars

**Best numbered-equation pin: HPPS itself.**
- (3.3) + sentence (`0907.0151.txt:451–453`, [png/HPPS_p11]): `O_{n,l} ≡ O∂↔_{µ1}…∂↔_{µl}(∂↔_ν∂↔^ν)^n O − traces` (3.3). "This has spin l and dimension ∆n,l = 2∆+2n+l+O(1/N²)."
- (3.9) (`:540`): `∆(n,l) = 2∆ + 2n + l + (1/N²)γ₁(n,l) + …`
- **Even l, identical operators** (`:525–526`): "The crossing condition implies that l must be even (from interchanging the vertex operators at z and 0 or at 1 and ∞ via a conformal transformation), and also that A(z,z̄) = A(1 − z, 1 − z̄) (3.8)". The sums in (3.10), (3.11) and (4.3) run over "l=0, even". The explicit numbered form of this is (4.2) `p0(n,l) = [1 + (−1)^l] C_n C_{n+l}` ([V2]), and likewise (4.29), [V5]. Both vanish for odd l. The Bose-symmetry remark is at `:615` ("note that the spin must be even, by Bose symmetry").

**Fitzpatrick–Kaplan 1112.4845 (general d):**
- `1112.4845.txt:378–379` (Sec. 2.1, printed p. 8 / PDF p9): "Given two single-trace primary scalar operators O1 and O2, one can form double-trace primaries [O1 O2]n,ℓ which will have dimension ∆1 + ∆2 + 2n + ℓ and spin ℓ." This sentence has no equation number; its examples are eqs (13)–(14).
- `:308–309`, attached to **eq (11)**: "γ(n,ℓ) is the anomalous dimension of the double trace operator [O1 O2]n,ℓ of dimension ∆1 + ∆2 + 2n + ℓ + γ(n,ℓ)".
- **Eq (43)** ([V9], PDF p14): general-d MFT OPE coefficients (c̄¹²_{n,ℓ})², carrying a factor (−1)^ℓ. FK: "This result matches that of [22] in the cases they considered, namely that of 2-dimensional and 4-dimensional CFTs with ∆1 = ∆2 normalized without the factor of C∆1C∆2" (`:677–678`). [22] is HPPS.
- **FK does NOT state "only even ℓ for identical operators".** A grep for even/odd/identical (`1112.4845.txt`) turns up no such sentence. The even-ℓ pin comes from HPPS (3.8)/(4.2).
- 1111.6972 (Analyticity paper) was fetched. It has double-trace poles at ∆1 + ∆2 + 2m (`1111.6972.txt:297`) but no ℓ-spectrum sentence worth pinning.

**Review:** Poland–Rychkov–Vichi 1805.04405, PDF p25 ([V12]), footnote 81, **not a numbered equation**: "The OPE φ × φ contains only operators of the schematic form φ(∂²)ⁿ∂^ℓφ, which have spin ℓ and dimension 2∆φ + 2n + ℓ." The same page's main text reads "Explicit conformal block decompositions of MFT 4pt functions containing scalars were obtained by Heemskerk et al. (2009) for d = 2, 4 and by Fitzpatrick and Kaplan (2012) in general d." (`1805.04405.txt:1871–1875`, left column). PRV has no even-ℓ sentence here. Simmons-Duffin TASI 1602.07982 was fetched and grepped, and has no MFT spectrum statement found by grep (only "even spin blocks are invariant under x1 ↔ x2", `1602.07982.txt:2159`), so it was not pinned.

---

## 3. arXiv:2004.14012: verified title, author, scope

- **Title/author** (arXiv abs meta, `2004.14012.abs.html`; PDF p1): "Holographic transform for tensor product of holomorphic discrete series", **Quentin Labriet** (single author, Reims). Published as DOI 10.1142/S0129167X20500901 (Int. J. Math.). arXiv class math.CA, v2 of 25 Aug 2020.
- **Group:** the universal cover of SL₂(ℝ) only. This is the "diagonal case" (G, G′) = (SL₂~ × SL₂~, SL₂~). Abstract (`2004.14012.txt:10–12`): "We study holographic operators associated with Rankin-Cohen brackets which are symmetry breaking operators for the restriction of tensor products of holomorphic discrete series of the universal covering of SL2(R)." Sec. 2 (`:97–98`): "two different models for the holomorphic discrete series representations of the universal covering group of the Lie group SL2(R)".
- **λ range, verbatim hypothesis (C1)** (`:93`, [V10]): "λ′, λ′′, λ′′′ > 1 such that l := ½(λ′′′ − λ′ − λ′′) ∈ N." Reason given (`:113`): "It is known that H²_λ(Π) = {0} for λ ≤ 1, so we suppose that λ > 1." (`:140`): the representation "lifts to a unitary and irreducible representation of the universal covering group SL2(R) for λ > 1".
- **Main theorem, Theorem 1.1** (`:52`, [V10]): "Suppose λ′, λ′′, λ′′′ > 1 such that l = ½(λ′′′ − λ′ − λ′′) ∈ N. Let w1, w2 ∈ Π, and g ∈ H²_{λ′′′}(Π). Then we have: (RC^{λ′′′}_{λ′,λ′′})* g(w1,w2) = C(λ′,λ′′) ∫_Π g(z) K^{λ′′′}_{λ′,λ′′}(z,w1,w2) dµ(z) (1.1)", with K = (w2−w1)^l ((w1−z̄)/2i)^{−(λ′+l)} ((w2−z̄)/2i)^{−(λ′′+l)}, dµ = y^{λ′′′−2}dxdy, and C = (λ′−1)_{l+1}(λ′′−1)_{l+1}/(2^{2l+4}π² l!). Theorem 2.1 (`:206`) restates it under (C1). The second result is Fact 4.3, the Jacobi-polynomial interpretation.
- **SO(2,n) / type IV:** the paper has **no theorem for SO₀(2,n)**. The conformal case appears only as the setting of [KP20] (`:23–36`): "(G, G′) = (SO0(2,n), SO0(2,n − 1)) referred to as the conformal case … leads to the construction of a relative reproducing kernel in the conformal case (see Thm 3.10 in [KP20])". Plus one unproved remark (`:68–70`): the second proof "is new and can also be used in the conformal case". [KP20] = T. Kobayashi, M. Pevzner, "Inversion of Rankin-Cohen operators via holographic transform", Ann. Inst. Fourier 2020 (`:913–914`). That paper is **not fetched or pinned here**.
- **Does it cover SO(2,5) at λ = 5/2 below the holomorphic discrete series (λ > 4)? No.**
  1. The group is SL₂(ℝ)~, not SO(2,n).
  2. Its only λ-hypothesis is λ > 1, the SL₂ weighted-Bergman nonvanishing threshold.
  3. (C1) further requires l = ½(λ′′′ − λ′ − λ′′) ∈ ℕ, i.e. discrete, integer-spaced tensor-product components.
  4. Nothing on analytic continuation in λ. The only analytic continuation (`:522`) is in the variables w₁, w₂, z.

  The type-IV threshold "λ > n − 1 = 4 for n = 5" is **not stated in this source**. It needs its own pin, e.g. from Faraut–Korányi or from KP20 itself.

---

## Files (all in r9/)
- **Sources:** 0907.0151.pdf/.txt, 1112.4845.pdf/.txt, 1111.6972.pdf/.txt, 1805.04405.pdf/.txt, 1602.07982.pdf/.txt, 2004.14012.pdf/.txt, 2004.14012.abs.html
- **Renders:** png/ (HPPS p11, 12, 15, 17, 18, 22, 23, 24, 32, 33; FK p7, 9, 14; Labriet p2, 3; PRV p25)
- **Transcriptions:** VISUAL_TRANSCRIPTIONS.txt [V1]–[V12]
- **Instrument:** check_r9_gamma.py → check_r9_gamma.out
- **Checksums:** SHA256SUMS.txt
