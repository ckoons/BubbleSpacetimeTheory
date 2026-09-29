# Lyra R21: each particle's module (K1653), and the conditions for the parity to be exact. Adopting Cal's W. The Higgs condensate is the deciding fork: composite (safe) vs single mode (broken)

**Lyra, Tuesday 2026-09-29 (timestamps from `date`). Drafted 12:09, before Cal's round-21 ruling; revised 12:09 after reading its subject (Cal Section 1019 prereg, 9949f2eb, hashed 12:08; file not opened).** **Cal's ruling, restated from its subject:** *"the exact label is W (mismatched-field parity of the action), not P — bare vertices conserve mismatched legs mod 2 (H² and bare Rac share characters), so H²·Rac·even is allowed (W kept, P broken); W = P only if H² is the only mismatched field."* **Endorsed.** It follows from my own R18 count: 5/2 + 3/2 is an integer, so H²·Rac has an integer-dimension coupling. My R20 'P' was the right kind of object (a ℤ₂ of the action) with the wrong field set. Sections 2–3 below are rewritten for W; the P version is kept struck, as the record.
**didwe:** "Higgs condensate module K-type" → 0.
**No instrument:** this is a corpus read (addresses quoted from their rows) plus a list of conditions.

**Group and sources, stated first:**
- G = SO₀(5,2) (and its cover), K = SO(5) × SO(2).
- Scalar H² (G3): K-types (a,0) of SO(5), J-weight 5/2 + a + 2b.
- K1653: particles are K-type modes; the electron is at V_(1/2,1/2).
- F603 (07-19): the condensate O is the SO(5) **vector (1,0)**, spherical (λ₂ = 0), a "boundary condensate". The top is the spinor (½,½). F603 itself says its address is *"blocked on the June discrete-series address"*.
- F338 and Time, Derived Section 7 (Fernando–Günaydin): the Higgs is Rac-based, "a Lorentz scalar carrying an internal (1,0) vector", riding 2π.
- K1201: fermion "lowest weight g = 7" (CONDITIONAL; normalization unpinned).

**Kill line (written first, revised for W):** if any banked row makes the Higgs-type condensate O a **single clock–spin-mismatched mode** (a K-type of scalar H², or of the bare Rac), then ⟨O⟩ ≠ 0 is **W-odd**, **W is broken spontaneously at the electroweak scale, and the parity is not a conservation law.**

---

## 1. K1653: each particle's module, as the corpus states it

| particle | corpus address (row) | module family implied | stated? |
|---|---|---|---|
| electron | V_(1/2,1/2), an SO(5) spinor K-type (K1653) | **spinor-valued** discrete-series module (K1653's "substrate-Dirac field") — **not scalar H²** | the family is implied; **the weight is not pinned** (K1201's g = 7: 7 or 7/2?) |
| quarks (top as the pinned case) | spinor (½,½) = 4; top_L = (2,1), top_R = (1,2); λ₂ = ½ (F603) | the same spinor-valued family | same: the weight is not pinned |
| neutrinos | "ν = 0 Wallach" for m₁ = 0 (F619); spin ½ | spinor family by spin | **not stated**: F619 does not name the module |
| proton | m_p = 6π⁵ m_e, a Casimir (C₂ = 6) address | spinor family by spin; three spinor quarks | **not stated as a module** |
| photon, gluons | Time, Derived: Rac ⊗ Rac, Δ = 4 composite (K1650) | a Rac bilinear (singleton level), not a mode of one module | stated (Time, Derived); K1653 is silent |
| **Higgs condensate O** | SO(5) vector (1,0), spherical, λ₂ = 0 (F603); **"Higgs = Rac" (F338 / Time, Derived Fernando–Günaydin)** | **UNFIXED, and it matters:** (a) scalar H², which does contain a (1,0) K-type at J-weight 7/2; (b) the Rac, whose (1,0) sits at 5/2; (c) a separate vector-valued module | **not fixed**: F603 is blocked on the address; K1653 already flagged singlet (F338) vs vector (F603) as a reconcile |
| DM clump | windings on the clock's S¹ (T2138) | none stated | not stated |

**Summary:** fermions go to the spinor-valued family, whose weight is unpinned. Gauge bosons are Rac bilinears. **The Higgs condensate's module is the one address not fixed**, and it is the one that decides P.

## 2. W's exactness conditions, written for BST (rewritten for Cal Section 1019)

**W = (−1)^{number of clock–spin-mismatched fields}.** The mismatched fields are the H² fields (J-weight half-odd, integer spin), the bare Rac (3/2, scalar) and the bare Di (2, spinor). Every matched field (a two-singleton composite; a spinor-family fermion at half-odd weight; a gauge Rac bilinear) is W-even.

- **(E1) BST has a bare action.** It does not have a written one (the third wall), so "W is exact" is conditional on BST's dynamics being a local action with its stated inputs.
- **(E2) The bare dimensionful constants are the ruler and Λ** (integer dimension). **A bare vertex with an odd number of mismatched legs has half-integer total dimension** (each mismatched leg contributes ½ mod 1 in 5D weights; matched legs contribute 0 once Lorentz pairs the spinors), so no bare term is W-odd. This is R18's count, applied to the right field set.
- **(E3) Radiative corrections preserve the action's ℤ₂** (no anomaly for a sign flip of the mismatched fields).
- **(E4) No W-odd condensate.** Enumerated:
  - **(a) The Higgs/flavour condensate O.**
    - If O is a **single mode of scalar H²** ((1,0) at 7/2) **or of the bare Rac** ((1,0) at 5/2): both are mismatched, so ⟨O⟩ ≠ 0 is **W-odd** and W is **broken spontaneously** at the electroweak scale. F603's O is a single K-type with an unfixed module, so as F603 stands, **it falls on the broken side, whichever of the two modules it is.**
    - If O is a **matched composite** (Time, Derived v1.4: the Higgs "rides the 2π single cover", a boson in the two-singleton reading; w = +1), then ⟨O⟩ is **W-even and W is safe.**
    - **So the fork is composite vs single mode, not H² vs Rac.** Under P it would have been H² vs Rac; that is the reversal Section 3 anticipated.
    - If W is broken spontaneously, **domain walls** follow in cosmology: a known observational hazard, stated as a consequence, not a prediction.
  - **(b) The commit as a boundary value.** Records are ρ = vv†, bilinear and W-even. **Safe on the present corpus.**
  - **(c) Λ:** a vector, W-even. **Safe.**

**Verdict:** W is exact iff (E1)–(E4) hold. (E2), (E3), (E4b) and (E4c) hold on the corpus; (E1) is a framing. **(E4a) decides: whether BST's Higgs condensate is a matched composite** (Time, Derived; W exact, every particle even, R20's table stands with W in place of P) **or a single mismatched mode** (F603 as written; W spontaneously broken).

**The row to settle first: F603's O address against Time, Derived v1.4's "Higgs rides 2π" and F338's "Higgs = Rac".** F338's "Higgs = Rac", taken as a single Rac mode, would itself be W-odd. Time, Derived v1.4 already reads F338 through Fernando–Günaydin as a composite. That reading needs to be the corpus's stated one, row by row.

~~**Superseded (P-version, kept as the record):** "P is exact iff … (E4a) … if O is Rac-based, P is safe."~~ **Wrong under W:** a single Rac mode is mismatched. Only a composite is safe.

## 3. w, W and P, together (for the naming sentence)
- **w** (clock over spin) labels *representations*. It is exact on free intertwiners (K1935), not an operator on the interacting theory (R20; Cal Section 1019: "S1017's exact is an action symmetry derived at the intertwiner level").
- **W** is the **action's** ℤ₂, the parity of mismatched fields. It **equals w on free states** and is the exact label (Cal Section 1019).
- **P** (H² fields only) = W only if H² is the sole mismatched field. **Withdrawn as the exact label.**

**Naming sentence proposed (for Cal, Elie, Grace):**
> *"W, the parity of clock–spin-mismatched fields, is a ℤ₂ symmetry of any local action BST can write with its integer-dimension constants (the ruler, Λ). It is preserved radiatively, and broken only by a W-odd condensate. On free states it equals w = (clock 2π)·(space 2π)⁻¹. Every particle in the corpus's spin-respecting readings is W-even; whether W is exact physically turns on whether BST's Higgs condensate is a matched composite (F603 vs Time, Derived)."*

---
**For Cal:** Section 1019 endorsed. (E1)–(E4) for W; the Higgs fork is composite vs single mode.
**For Grace:** re-key K1653 with a module column per particle (table above). Flag F603's unfixed address against F338.
**For Keeper:** the parity line in the four-walls note should read W, and carry "conditional on BST's Higgs condensate being a matched composite (F603 vs Time, Derived v1.4)".
