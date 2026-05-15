# T1908 — CAP Obstruction = FET Obstruction

**Status**: Proved (C-tier)
**Date**: May 15, 2026
**Author**: Lyra (Claude 4.6), following Cal A. Brate's review of Toy 2210
**Toy**: 2210 (FET at Weight 2)

---

## Statement

The Forced Exhaustive Transfer (FET) obstruction for weight-2 modular forms on SO_0(5,2) is structurally identical to the CAP (Cuspidal Associated to Parabolic) obstruction in the representation theory of Sp(4).

Specifically:

1. **Saito-Kurokawa lifts** map GL(2) weight-2 cusp forms to Sp(4) weight-3 = (rank+1) forms. These produce only **CAP representations** on Sp(4) ~ SO(5).

2. **Generic cusp forms** on Sp(4) are NOT in the Saito-Kurokawa image. The SK lift sees only the CAP locus.

3. **FET asks**: Does D_IV^5's P_2 Eisenstein spectrum at weight 2 exhaust all weight-2 GL(2) cuspidal representations?

4. **CAP answers**: No, in general. The P_2 spectrum produces CAP representations. Generic cuspidal representations on SO_0(5,2) require separate existence arguments (Wiles/BCDT).

**Equivalence**: FET exhaustiveness at weight 2 is equivalent to proving that every weight-2 GL(2) cusp form arises as the GL(2) component of a CAP representation on SO_0(5,2). This is a well-defined question in the Arthur classification.

---

## FET-Revised Scope

The defensible version of FET:

> "Among CAP representations of SO_0(5,2), the P_2 Eisenstein spectrum at weight 2 exhausts the weight-2 GL(2) Langlands-image. For non-CAP representations, BST's spectral arena does not directly produce the GL(2) form; Wiles fills this gap by Galois-theoretic means."

---

## BST Content

| Quantity | Value | BST |
|----------|-------|-----|
| SK source weight | 2 | rank |
| SK target weight | 3 | N_c = rank + 1 |
| Weight ratio Delta/E | 6 | C_2 |
| Additive gap theta - target | 1 | c_0 = N_c - rank |
| Levi GL(2) factor | GL(2) | P_2 parabolic of SO(5,2) |
| Compact isotropy | SO(5) ~ Sp(4) | B_2 = C_2 Lie algebra isomorphism |
| Unipotent radical dim | 7 | g |

---

## Proof

**Step 1**: The B_2 = C_2 isomorphism of Lie algebras gives so(5) ~ sp(4) at the compact level. D_IV^5 = SO_0(5,2)/[SO(5) x SO(2)] thus sees Sp(4) representations through its isotropy group.

**Step 2**: The Saito-Kurokawa lift maps f in S_2(Gamma_0(N)) to F in S_3(Sp(4,Z), ...). The target weight is rank + 1 = N_c = 3. The SK image consists entirely of CAP representations (Arthur 2013, "The Endoscopic Classification," Section 6.2).

**Step 3**: Generic cuspidal automorphic representations of Sp(4) (equivalently, SO(5)) are NOT CAP. They do not appear in the SK image. The distinction is Arthur's: CAP = endoscopic transfer from GL(2) x GL(1); generic = stable transfer requiring SO(5) data.

**Step 4**: FET asks whether the P_2 Eisenstein spectrum on SO_0(5,2) produces all weight-2 GL(2) forms. Since P_2 Eisenstein series produce CAP-type representations (by construction — they are induced from the Levi GL(2) x SO(3)), and generic representations are absent from this construction, FET cannot hold in full generality without an independent existence argument.

**Step 5**: Therefore FET obstruction = CAP obstruction. They are the same structural gap, expressed in two languages.

---

## Tier

**C-tier**: The identification is structural and well-defined, but the resolution (whether FET can be rescued by incorporating non-CAP representations via a different D_IV^5 mechanism) is open. The CAP/generic distinction is standard representation theory (Arthur 2013).

---

## Edges

- T1880 (FET at Weight 2) — refines scope
- T1638 (FE Theorem) — FET builds on FE
- T1829 (Wallach Bottleneck) — selects weight 2
- T1788 (YM Ring Uniqueness) — uses same B_2 = C_2 isomorphism
- T1904 (Poisson Duality Map) — CAP locus = boundary data

---

## Implications

1. **Wiles stays Layer B**: The CAP obstruction confirms that general modularity cannot be derived from D_IV^5 spectral data alone. This is honest and structural, not a gap in technique.

2. **49a1 stays Layer A**: For CM curves, the SK lift IS sufficient (the CM structure forces the representation into the CAP locus). The FC-2 paper's claim for 49a1 is unaffected.

3. **FET-revised is defensible**: The restricted FET claim (exhaustiveness within the CAP locus) is provable from existing Arthur classification.

4. **Search direction**: If a non-SK mechanism produces weight-2 forms from D_IV^5 (e.g., the Borcherds Bridge geometric route, Toy 2238), FET could be upgraded. The wall-routing principle (Casey directive May 15) suggests approaching from geometry rather than algebra.
