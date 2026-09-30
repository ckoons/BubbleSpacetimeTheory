# R24 pins: the Wallach set of the spinor family of so(2,5). Does anything sit at 7/2? (draft)

Grace lane, 2026-09-30 (clock 10:33 EDT at start of writing). Paths are relative to this directory unless prefixed. Every quote comes from a `.txt` made by `pdftotext -layout` from a PDF saved here. Garbled displays were rendered to `png/` and transcribed in `VISUAL_TRANSCRIPTIONS.txt` (VT-1 to VT-6). The retained instrument is `toy/r24_spinor_line_so25.py`, with its output in `toy/r24_spinor_line_so25.out`. No git.

## Verdict up front

**In the FK scale (E0 = the SO(2) weight, which equals ν on the scalar line), the spinor family of so(2,5) is unitary exactly for E0 ≥ 2.**

- It has one discrete point, E0 = 2 (the Di). That point is at once:
  - the first reduction point,
  - the last unitary reduction point,
  - the end of the continuous part.
- The continuous part is E0 > 2. There, the generalized Verma module N(λ) is irreducible and unitary.
- Holomorphic discrete series: E0 > 9/2. The limit of holomorphic discrete series is at E0 = 9/2 (z = 0).

**Nothing natural sits at 7/2.**
- E0 = 7/2 is an interior point of the continuous part. N(λ) is irreducible there: the instrument gives a Dirac margin of +3 > 0.
- The only arithmetic route to 7/2 found: 7/2 = Di + c = 2 + 3/2. This is where a first reduction point would sit if the spinor line copied the scalar pattern (a = b − c).
- The pinned criterion says instead that a = b on the spinor line (Section 4).

| Point (spinor family, so(2,5)) | EHW z = (λ+ρ, β∨) | FK-scale E0 = −λ1 | is it 7/2? |
|---|---|---|---|
| continuous part | z < 5/2 | E0 > 2 | contains 7/2 as an interior point |
| first reduction point a(λ0) | 5/2 | 2 | no |
| last unitary (discrete) point b(λ0) | 5/2 | 2 | no |
| Di singleton | 5/2 | 2 | no |
| limit of holomorphic discrete series | 0 | 9/2 | no |
| holomorphic discrete series | z < 0 | E0 > 9/2 | no |
| "Hardy-type" point for the spinor bundle | — | NOT DEFINED in any pinned source | — |
| (for comparison) scalar line, same scale | Wallach {4, 5/2} ∪ (−∞, 5/2) | ν ∈ {0, 3/2} ∪ (3/2, ∞); HDS ν > 4 | no |

**Corpus claim, item 3.** The corpus says "square-integrable for k ≥ k_min = 3 (EHW 1983)". This is **not supported**, as follows.
- EHW's normalization, as restated in the open sources: holomorphic discrete series ⟺ z < 0 ⟺ ν > 4.
- That agrees with the already-pinned Kobayashi–Pevzner and Quiroga-Barranco–Seng statement λ > n − 1 = 4.
- In the doubled scale k = 2ν, "3" is the first Wallach point ν = 3/2. It is the last discrete point of the scalar Wallach set (the minimal/Rac representation, GK dimension 5). It is not an L² threshold.
- In the doubled scale the L² threshold is k > 8.
- No normalization found makes 3 a square-integrability threshold for n = 5 (Section 5).

---

## 0. Parametrizations, stated first

### 0.1 Bai–Hunziker (BH), arXiv:2409.16555 v1 (identical to `../../sources_grace_2026-09-27/r13/arxiv_2409.16555.txt`; `cmp` passes)

**Setup**, `arxiv_2409.16555.txt:54-64`:
> "Let β denote the unique maximal noncompact root of ∆+ . Now choose ζ ∈ h∗ so that ζ is orthogonal to ∆(k) and (ζ, β ∨ )=1. … Then we can write λ = λ0 + zζ, with λ0 ∈ h∗ such that (λ0 + ρ, β)=0, and z = (λ + ρ, β ∨ ) ∈ R."

- **Constants**: Table 1 (`:241-251`, "from [EHW83]"), row so(2, 2n−1): r = 2, c = n − 3/2, (ρ, β∨) = 2n − 2.
- **For so(2,5)** (n = 3): r = 2, c = 3/2, (ρ, β∨) = 4.

**Discrete points**, `:73`, eq. (1.1):
> "zk = (ρ, β ∨ ) + uk = (ρ, β ∨ ) − kc"

For so(2,5): z0 = 4 and z1 = 5/2.

### 0.2 Pandžić–Prlić–Souček–Tuček I (PPST1), arXiv:2209.15324 v1: coordinates

**Section 3.5**, `arxiv_2209.15324.txt:1291-1301`:
> "The basic Schmid k-submodules of S(p− ) have lowest weights −s1 or −s2 , where s1 = (1, 1, 0, . . . 0), s2 = (2, 0, 0, . . . 0). Moreover, all irreducible k-submodules of S(p− ) have lowest weights −sa,b , where sa,b = (2b + a, a, 0, . . . 0). The highest weight (g, K)-modules have highest weights of the form λ = (λ1 , . . . , λn ), where λ2 ≥ λ3 ≥ · · · λn ≥ 0, λi − λj ∈ Z and 2λi ∈ N0 … In this case ρ = (n − 1/2, n − 3/2, . . . , 1/2)."

For so(2,5): ρ = (5/2, 3/2, 1/2), with ε1 = the SO(2) (central) direction.

### 0.3 PPST2, arXiv:2305.15892 v2: the EHW line and the first reduction point

**The line**, `:221-226` (VT-6):
> "The shape of the [EHW] classification is given by certain lines in t∗ of the form (1.10) λ = λ0 + zζ, z ∈ R. Here ζ ∈ t∗ is orthogonal to ∆k and normalized so that 2⟨ζ,β⟩/⟨β,β⟩ = 1 … For a fixed λ, λ0 is defined as the point on the line λ + zζ, z ∈ R, such that ⟨λ0 + ρ, β⟩ = 0."

**Direction of unitarity**, `:227-229`:
> "It is known from the work of Harish-Chandra that if λ is on the line (1.10), for sufficiently negative z the module N (λ) is the (g, K)-module of a holomorphic disrete series representation."

**First reduction point**, `:231-236`:
> "Let a be the smallest real number such that N (λ0 + aζ) is reducible. The corresponding λ is called the first reduction point. It follows by continuity that the Shapovalov forms on N (λ0 + zζ), z < a, are all positive definite and hence these modules are unitary. … Hence L(λ0 + aζ) is also unitary. [EHW] use this argument to prove unitarity of N (λ0 + zζ), z < a, and also of L(λ0 + aζ). See [EHW, Proposition 3.1]."

**Continuous and discrete parts**, `:242-245`:
> "The irreducible unitary modules N (λ0 + zζ), z < a, form the continuous part of the set of the unitary points on the line (1.10). In addition, there is a finite number of discrete unitary points on the line. One of these discrete points (possibly the only one) is obtained for z = a."

### 0.4 Translation to coordinates (INFERENCE, elementary)

In the B3 coordinates of 0.2, with the noncompact simple root α1 = ε1 − ε2:
- β = ε1 + ε2 and |β|² = 2, so β∨ = β.
- ζ = ε1: it is orthogonal to the compact roots ε2 ± ε3, ε2, ε3, and (ε1, β∨) = 1.

Hence, for λ = (λ1, λ2, λ3):

  z = (λ + ρ, β∨) = λ1 + λ2 + 4.

The two lines are:
- **Scalar line**, λ = (−ν, 0, 0): z = 4 − ν.
- **Spinor line**, λ = (−E0, 1/2, 1/2): z = 9/2 − E0.

This matches BH's own spinor point. BH `:524` gives "λ = ωn − (n − 1/2)ζ (unitary reduction point)". With ω3 = (1/2, 1/2, 1/2) that is λ = (−2, 1/2, 1/2), so z = 5/2 = z1.

### 0.5 Calibration to the FK scale (the brief's normalization)

The brief gives the FK facts for the Lie ball of dimension 5: Wallach set {0, 3/2} ∪ (3/2, ∞), Hardy space at 5/2, genus 5, holomorphic discrete series for ν > 4. Scalar FK facts were pinned before, in `../../sources_grace_2026-09-26/r6_conformal/owed/OWED_PINS_draft.md` Sec. 2.3, from Quiroga-Barranco–Seng 2205.06786 and Kobayashi–Pevzner Remark 6.4.

The map ν = −λ1 = (ρ, β∨) − z is fixed by two points and checked on a third:
- **Trivial representation.** z0 = 4 gives ν = 0. BH `:517-519` (so(2,2n−1), AV = O0): "It follows that λ = 0 (trivial representation)."
- **First Wallach representation.** z1 = 5/2 gives ν = 3/2. BH `:523`: "λ = −(n − 3/2)ζ (1st Wallach representation)". Also r13 `arxiv_1909.00705.txt:1624`: "λ = −kcζ + ρ = (−k(n − 3/2) + (n − 1/2), n − 3/2, . . . , 1/2)".
- **Check.** z < 0 ⟺ ν > 4, which is the pinned L² range "λ > n − 1" (Kobayashi–Pevzner Remark 6.4, `../../sources_grace_2026-09-26/r6_conformal/owed/kobayashi_pevzner_1301.2111.txt:3445-3448`). The r6 pins show that the KP λ is the FK ν for the scalar line.

**The spinor family's central parameter.** The lowest K-type is spinor ⊗ (character of the SO(2) centre with weight −E0). The natural central parameter is E0 = −λ1, the eigenvalue of the central generator on the lowest K-type. It reduces to ν on the scalar line. This is the "E0" of the corpus clock convention and of Angelopoulos–Laoues (Section 3).

An alternative, "ν′" = −(λ, β∨) = E0 − 1/2, keeps the scalar formula z = 4 − ν′. Both scales are given below so that no convention slips in unstated.

---

## 1. Pin A: the shape of the EHW unitarity set on any line. PRIMARY restatement, numbered

EHW 1983 is paywalled.

**Metadata** (`crossref_ehw1983.json`, Crossref API):
- T. J. Enright, R. Howe, N. Wallach, "A Classification of Unitary Highest Weight Modules".
- In *Representation Theory of Reductive Groups* (Park City 1982), Progr. Math. 40, Birkhäuser Boston 1983, pp. 97–143.
- DOI 10.1007/978-1-4684-6730-7_7; ISBN 9780817631352 / 9781468467307.
- **Status: PIN OWED on the original. SECONDARY restatements below.**

**Bai–Erickson–Hunziker–Jiang (BEHJ), arXiv:2512.08199 v1, Section 2.5.**

`arxiv_2512.08199.txt:460-466`:
> "Define Z(λ0 ) := {z ∈ R | L(λ0 + zζ) is unitarizable}. By Enright–Howe–Wallach [19, Thm. 2.4], the set Z(λ0 ) is given by the diagram shown in Figure 1."

Figure 1 (VT-1): a solid ray from −∞ ending at a(λ0), then equally spaced dots at spacing c up to b(λ0).

`:472-475`:
> "Here, a(λ0 ) is the so-called first unitary reduction point and b(λ0 ) is the last unitary reduction point. … The set Z(λ0 ) includes the ray ending at a(λ0 ), as well as certain reduction points between a(λ0 ) and b(λ0 ) that are spaced at an interval of length c, whose value (from [19]) can be found in Table 2."

Table 2 (VT-2): so(2, 2n−1) has r = 2, c = n − 3/2, h∨ = 2n − 1.

**Theorem 2.24** (VT-2; `:503-507`, citing Bai–Hunziker Forum Math. [3, Thm. 3.2]): "The last unitary reduction point b(λ0) is given by b(λ0) = h∨_{Q(λ0)} − 1 + (r_{R(λ0)} − r_{Q(λ0)})/2".

**Definition of Q and R**, `:492-500`, verbatim:
> "Let Φc (λ0 ) = {α ∈ Φ(k)|(λ0 , α) = 0}. Consider the root subsystem Ψ1 of Φ, which is generated by ±β and Φc (λ0 ). Let Q(λ0 ) be the simple component of Ψ1 which contains −β. If Φ has two root lengths and there exist short roots α′ ∈ Φ(k) that are not orthogonal to Q(λ0 ) and satisfy (λ0 , α′∨ ) = 1, then let Ψ2 be the root system generated by ±β, Φc (λ0 ), and all such α. Let R(λ0 ) be the simple component of Ψ2 which contains −β. If Φ has only one root length or no such α exists, then we let R(λ0 ) = Q(λ0 ). … For a root system Φ, we write h∨Φ = (ρ, β∨) + 1 to denote the dual Coxeter number of Φ".

Note on [3]: BEHJ's reference [3] is "Z. Bai and M. Hunziker. A characterization of unitarity of some highest weight Harish-Chandra modules. Forum …" (`:1519`), which is arXiv:2409.16555. **Thm. 3.2 is not in the arXiv v1 on disk.** The published Forum version is the one numbered; PIN OWED on that number. The formula is quoted here from BEHJ.

---

## 2. Pin B: the spinor line of so(2, 2n−1). PRIMARY, numbered (PPST1 Lemma 3.86 + Thm 3.92 + PPST2 Cor. 2.5)

**Lemma 3.86** (VT-3; `arxiv_2209.15324.txt:1311-1316`): "The basic Dirac inequality for s = s1 is given by … λ1 ≤ 1 − n for λ = (λ1, 1/2, . . . , 1/2)". The proof, `:1325-1331`, says (λ − s1)+ = λ − ε1, and:
> "Plugging γ = ε1 into (3.84) we obtain 2(λ1 + n − 1/2) ≤ 1 which gives (3.88) λ1 ≤ 1 − n."

This is the **necessary** condition, `:1301-1303`:
> "The basic necessary condition for unitarity is, as before, the Dirac inequality (3.83) ‖(λ − s1)+ + ρ‖2 ≥ ‖λ + ρ‖2."

**Theorem 3.92**, `:1367-1369`:
> "Let λ be as in case 2 or as in case 3 and let (3.87) holds. Then the Dirac inequality (3.84) holds for any Schmid module s."

The proof, `:1373-1374`: "with strict inequality if (3.87) is strict."

**From the Dirac inequality to irreducibility, unitarity and non-unitarity.** PPST2 **Corollary 2.5**, proved there for any Hermitian symmetric pair, `arxiv_2305.15892.txt:356-366`, `:374-379`:
> "(1) Let s0 be a Schmid module such that the strict Dirac inequality (1.6) … holds for any Schmid module s of strictly lower level than s0 , and such that ‖(λ − s0 )+ + ρ‖2 < ‖λ + ρ‖2 . Then L(λ) is not unitary. (2) If (2.6) holds for all Schmid modules s, then N (λ) is irreducible and unitary." … "Unitarity of N (λ) follows from the strict Dirac inequality (2.7) by [EHW, Proposition 3.9]."

Also Remark 2.8, `:380-389`: when N(λ0 + zζ) is irreducible and unitary for z < a and L is not unitary just above a, "N (λ0 + aζ) can not be irreducible, so λ0 + aζ is the first reduction point".

PPST1 Lemma 2.1 (its proof: "we leave it for [PPST2]", `:193-194`) is PPST2 Corollary 2.3 (`arxiv_2305.15892.txt:322-329`), with the same statement, now proved. So the chain behind Thm 3.92 is closed in the open literature.

**Scope caveat.** PPST2 says (`:40-42`) that so(2,n) "will be treated in our forthcoming paper [PPSST]". What is used here is general: Cor. 2.5, Cor. 2.3 (both proved for any Hermitian pair), and PPST1's so(2,2n−1) computation (Section 3.5). The so(2,n) discrete-part construction is not needed for this line, because its discrete part is a single point, pinned independently by BH (Pin C).

---

## 3. Pin C: the Di is the unitary point z1 on the spinor line. PRIMARY, numbered (BH Thm 1.1 + Section 5.2)

**BH Theorem 1.1**, `arxiv_2409.16555.txt:78-79`:
> "Let λ ∈ Λ+ (k) and suppose AV(L(λ)) = Ok with 0 ≤ k ≤ r − 1. Then L(λ) is unitarizable if and only if (λ + ρ, β ∨ ) = zk ."

**BH Section 5.2** (so(2, 2n−1)), `:520-524`:
> "Suppose AV(L(λ)) = O1 and z(λ) = z1 = n − 1/2. … In the first case, it follows that λ = −(n − 3/2)ζ (1st Wallach representation). In the second case, we have λ = ωn − (n − 1/2)ζ (unitary reduction point)."

**Angelopoulos–Laoues**, arXiv:hep-th/9806100 (Rev. Math. Phys. 10 (1998)), **Theorem 2.4** (VT-5b; `:1113-1119`):
> "Every infinite-dimensional irreducible massless representation of so(2, n), for n ≥ 3, integrable to Ḡn , is a weight representation d^{n,ε}_{(−(s+n/2−1), s⃗)} … The eigenspace of εH0 corresponding to the eigenvalue (s + n/2 − 1 + k), k ∈ N, is an irreducible so(n)-module corresponding to the representation D(s⃗+(k, 0, . . . , 0))."

Proposition 2.4 (`:1121-1123`): these are "integrable to unitary representations of Ḡn". And `:1107-1110`: "s = 0 or 1/2 when n is odd".

For n = 5 and s = 1/2 this gives lowest energy E0 = 1/2 + 5/2 − 1 = **2**. In PPST/BH coordinates that is λ = (−2, 1/2, 1/2) = ω3 − (5/2)ζ, exactly BH's "unitary reduction point" at z1 = 5/2.

- **Di singleton**: E0 = 2, which is z = 5/2 (BH z1).
- In the ν′ scale: ν′ = 3/2. This is the same z, and the same ν′, as the scalar first Wallach point (Rac, E0 = 3/2).

**Physics cross-check** (level-one necessary condition only). Minwalla, arXiv:hep-th/9712074, eq. (2.48) (VT-4; `:437`): "ǫ0 ≥ 2 (h1 = h2 = 1/2)" for d = 5. General d, (2.56) (`:464`): "ǫ0 ≥ (d − 1)/2 (spinor)". On saturation, `:471-474`: "this operator obeys [P/ , ψ] = 0, i.e., the Dirac equation."

Minwalla says sufficiency was checked only in d = 3, 4 (`:506-509`). For d = 5 the sufficiency comes from Pin B.

---

## 4. Deliverable: the spinor-family unitarity set in the FK scale (INFERENCE = applying Pins A–C; arithmetic shown)

### 4.1 Last unitary reduction point b(λ0), from BEHJ Thm 2.24 (INFERENCE)

Take λ0 = ω3 − 5ζ = (−9/2, 1/2, 1/2). Check: (λ0 + ρ, β∨) = −9/2 + 1/2 + 4 = 0 ✓.

**Root system Q.**
- Φc(λ0) = compact roots orthogonal to λ0 = {±(ε2 − ε3)}. (ε2 + ε3, ε2 and ε3 all pair to 1/2 or 1.)
- Ψ1 = ⟨±(ε1+ε2), ±(ε2−ε3)⟩ = {±(ε1+ε2), ±(ε1+ε3), ±(ε2−ε3)}. This is **A2** (6 roots, one length).
- So Q = A2, the root system of su(1,2). BEHJ Table 2 row su(p, n−p) with n = 3 gives h∨_Q = 3 and r_Q = min{1,2} = 1.

**Root system R.**
- The short compact roots with (λ0, α′∨) = 1 that are not orthogonal to Q are ε2 and ε3, since (λ0, 2ε2) = (λ0, 2ε3) = 1.
- Ψ2 is then all of **B3**, so R = so(2,5)'s own root system and r_R = 2.

**Result.** b(λ0) = 3 − 1 + (2 − 1)/2 = **5/2**, which is E0 = 9/2 − 5/2 = **2**.

The instrument computes Q and R by reflection closure and prints |Q| = 6 (single length) and |R| = 18 for the spinor line.

**Calibration on the scalar line** (λ0 = −4ζ):
- Φc = all compact roots, so Q = R = B3, with h∨ = 2n − 1 = 5.
- b = 5 − 1 + 0 = 4, i.e. ν = 0, the trivial representation ✓ (BH `:519`). The instrument prints |Q| = |R| = 18.

### 4.2 First reduction point a(λ0) and the continuous part (INFERENCE)

**Necessity.** PPST1 (3.88) with n = 3 gives λ1 ≤ −2, i.e. **E0 ≥ 2** (z ≤ 5/2). So no point with E0 < 2 is unitary.
- More precisely, PPST2 Cor. 2.5(1) applies with s0 = s1, which has level 1; the only lower level is λ itself.
- This rules out isolated unitary points below the Di.

**Sufficiency.** For λ1 < −2, (3.87) holds strictly, so Thm 3.92 gives the strict Dirac inequality for all Schmid modules. PPST2 Cor. 2.5(2) then gives **N(λ) irreducible and unitary for all E0 > 2** (z < 5/2).

**At E0 = 2.** N(λ) is reducible: L has AV = O1 ≠ p+, while N(λ) = S(p−) ⊗ Fλ has full associated variety. L(λ) is unitary (Pin C, and also PPST2 Lemma 1.11 by continuity).

**Therefore:**
- a(λ0) = the smallest z with N reducible = **5/2**, and b(λ0) = **5/2** (Section 4.1).
- Z(λ0) = (−∞, 5/2]: a ray with **no** discrete points beyond its end.
- In the FK scale: **E0 ∈ [2, ∞)**. In the ν′ scale: ν′ ∈ [3/2, ∞).

**Instrument** (`toy/r24_spinor_line_so25.out`). It gives min over s_{a,b} (a, b < 12) of ‖(λ−s)+ + ρ‖² − ‖λ+ρ‖². On the spinor line:

| E0 | 1 | 3/2 | 2 | 5/2 | 3 | 7/2 | 4 | 9/2 | 5 |
|---|---|---|---|---|---|---|---|---|---|
| margin | −2 | −1 | 0 | +1 | +2 | **+3** | +4 | +5 | +6 |

- The margin is positive exactly for E0 > 2 and zero at the Di.
- Scalar calibration: margin 0 at ν = 3/2, positive for ν > 3/2, negative at ν = 1. This matches PPST1 Thm 3.89 ("λ1 < 3/2 − n").

### 4.3 Holomorphic discrete series threshold (INFERENCE from the Harish-Chandra condition as restated)

**Statement of the condition.** Dobrev, arXiv:0712.4375 (r13), `:497-499`:
> "According to the results of Harish-Chandra the holomorphic discrete series happen when the numbers mα are negative integers for the M2 -non-compact roots"

and `:500-502`, "limits … when some of the M2 -non-compact numbers mα become zero".

**Direction check against EHW's z.** Dobrev `:765-769`, so(4,2): "(z = 0 by [4]) … limits of discrete series" and "(z < 0 by [4]) … holomorphic discrete series". Together with PPST2 `:227-229`, the direction is set: discrete series lie at z → −∞.

**For the spinor line**, λ + ρ = (5/2 − E0, 2, 1). The pairings with the coroots of the noncompact positive roots {ε1 ± ε2, ε1 ± ε3, ε1} are maximized by ε1 + ε2, which gives 9/2 − E0 (instrument: HC max = 1, 1/2, 0, −1/2 at E0 = 7/2, 4, 9/2, 5).

- **Holomorphic discrete series** (on the universal cover, for real E0): **E0 > 9/2** (z < 0). This is "scalar threshold 4, shifted by the spin 1/2".
- **Limit of holomorphic discrete series**: E0 = 9/2.
- **Scalar check**: ν > 4 ✓. This is the pinned KP / QBS λ > n − 1.

### 4.4 Is 7/2 among the natural points?

| Candidate | E0 (FK scale) | ν′ = E0 − 1/2 | = 7/2? |
|---|---|---|---|
| first reduction point a | 2 | 3/2 | no |
| last discrete point b | 2 | 3/2 | no |
| start of continuous part | 2 (open: E0 > 2) | 3/2 | no |
| holomorphic discrete series threshold | 9/2 (strict) | 4 | no |
| limit of discrete series | 9/2 | 4 | no |
| Di singleton | 2 | 3/2 | no |
| "Di shifted by spin" | 2 ± 1/2 = 5/2 or 3/2 | — | no |
| Hardy-type point for the spinor bundle | **NOT DEFINED** in any pinned source. By analogy (INFERENCE only) with the scalar Hardy point z = 3/2, it would be E0 = 3; with the spin-independent d/2 axis, E0 = 5/2. | — | no (either way) |
| Di + c = b + c | **7/2** | 3 | **yes, but it is not a point of the Wallach set.** It is interior to the continuous part: N(λ) is irreducible there (margin +3), z = 1. |

**Where 7/2 could have come from.** The scalar pattern on so(2,5) is b = a + c: Wallach 3/2 plus c = 3/2 gives ν = 0 in reverse. Copying that onto the spinor line with the Di taken as the last point b would put a "first reduction point" at E0 = 2 + 3/2 = 7/2. The pinned criterion refutes this: on the spinor line a = b.

**Related secondary conflict (so(2,3), not adjudicated here).** Dobrev 0712.4375 `:540-548` states, for so(3,2), that the spin-1/2 FRP is E0 = 3/2, with the Di "isolated … below — by 1/2-spacing". That is exactly this "Di + c" pattern.

It conflicts with:
- Minwalla (2.43): "ǫ0 ≥ 1 (j = 1/2)", stated as necessary and sufficient in d = 3 at `:506-509`.
- PPST1 (3.88) with n = 2, which gives λ1 ≤ −1, i.e. E0 ≥ 1.

The same pattern-error on so(2,5) would produce exactly 7/2. Treat any 7/2 claim traced to Dobrev-style FRP bookkeeping as **suspect**.

---

## 5. Corpus claim check: "square-integrable for k ≥ k_min = (n_C − 1)/2 + 1 = 3 (EHW 1983)"

Corpus locations: `notes/BST_ElectronMass_Derivation.md:24,400,534`, and `notes/Paper_DIV5_Ribbon_Holonomy_v0.1_2026-07-09.md:106` ("ν = N_c = 3 (the Wallach threshold k_min)").

1. **EHW's normalization, as restated.** Holomorphic discrete series ⟺ z < 0 (Dobrev `:765-769`; PPST2 `:227-229`). With z = 4 − ν this is **ν > 4**. It agrees with KP Remark 6.4 / QBS `:256-259` ("finite on D^IV_n precisely for λ > n − 1").
2. **EHW's own "k".** BH Prop. 3.2 (r13 `arxiv_2409.16555.txt:258-275`) defines "k = k(λ) := −(λ, β∨)/c" and r13 `arxiv_1909.00705.txt:153-154` gives the Wallach set "Ws = {−kcξ | k ∈ Z and 0 ≤ k ≤ r − 1}", so k ∈ {0, 1} for so(2,5).
   - For the scalar line, k = ν/c = 2ν/3.
   - The first Wallach point is k = 1 (ν = 3/2). The L² threshold is k > 8/3.
   - Neither is 3. At k = 3 (ν = 9/2) the representation is already in the holomorphic discrete series.
3. **Doubled scale k = 2ν** (weight-k kernels). The Wallach set becomes {0, 3} ∪ (3, ∞), Hardy is at 5, and the L² threshold is k > 8.
   - Here k = 3 is the **first Wallach point** (ν = 3/2, the last discrete point). It is not a square-integrability threshold.
   - The corpus formula (n_C − 1)/2 + 1 = 3 equals 2 · (n_C − 2)/2 = 3 only because n_C = 5. The general doubled-scale Wallach point is n − 2, and the general L² threshold is 2(n − 1).
4. **Verdict.** No pinned normalization makes 3 the square-integrability threshold for n = 5.
   - "k_min = 3" is **correct as the doubled-scale first Wallach point**, i.e. the end of the continuous part (ν = 3/2).
   - The labels "square-integrable" and "EHW 1983" are **wrong or unsupported** as attached.
   - The r6 pins already recorded this (OWED Sec. 2.3). This round adds EHW's own z-normalization to that record.
   - Edit owed in the corpus, not made here.

---

## 6. Owed / not found

- **EHW 1983 Thm 2.4 and Prop. 3.1 / 3.9**: PIN OWED (paywalled). Metadata is pinned. The open restatements are BEHJ Section 2.5 + Fig. 1 + Thm 2.24, and PPST2 Section 1 + Cor. 2.5.
- **Jakobsen, "Hermitian symmetric spaces and their unitary highest weight modules"**, J. Funct. Anal. 52 (1983), no. 3, 385–412 (`crossref_jakobsen1983.json`; DOI 10.1016/0022-1236(83)90076-9): PIN OWED.
  - Open secondary for its role: BH `:41-42`: "The full classification was independently completed in [EHW83] and [Jak83]". PPST1 `:73` says the same ("In [EHW] (and independently in [J])").
  - No open restatement of Jakobsen's own parametrization was found.
- **Bai–Hunziker Forum Math. Thm 3.2** (the b(λ0) formula): PIN OWED on the published numbering. Quoted via BEHJ Thm 2.24.
- **An explicit EHW formula for a(λ0)** (first reduction point) in an open source: **not found**. a(λ0) = 5/2 for the spinor line is derived from PPST1 + PPST2 Cor. 2.5 (Section 4.2), not quoted.
- **The Hardy space of the spinor bundle on the Lie ball**: no source in hand defines it. Not pinned.
- Enright–Hunziker, Rep. Theory 8 (2004) 15–51 (DOI 10.1090/s1088-4165-04-00215-8; AMS open journal): identified but not downloaded. It covers exceptional groups only, so it is not needed for so(2,5).
- Davidson–Enright–Stanke (Mem. AMS 1991): not open; not needed.

## Files

- **PDFs, texts and abstract pages**: arxiv_2512.08199 (BEHJ), arxiv_2209.15324 (PPST1), arxiv_2305.15892 (PPST2), arxiv_2405.18766 (Erickson–Hunziker; context only, not quoted), arxiv_2409.16555 (BH, a copy of r13), arxiv_hep-th_9712074 (Minwalla), arxiv_hep-th_9806100 (Angelopoulos–Laoues).
- **Crossref records**: crossref_ehw1983.json, crossref_jakobsen1983.json.
- **Renders**: png/ (8 renders) and VISUAL_TRANSCRIPTIONS.txt.
- **Instrument**: toy/r24_spinor_line_so25.py, with output in toy/r24_spinor_line_so25.out.
- **Reused, not copied**: `../../sources_grace_2026-09-27/r13/arxiv_0712.4375.txt` (Dobrev), `../../sources_grace_2026-09-27/r13/arxiv_1909.00705.txt`, and `../../sources_grace_2026-09-26/r6_conformal/owed/` (KP, QBS).
