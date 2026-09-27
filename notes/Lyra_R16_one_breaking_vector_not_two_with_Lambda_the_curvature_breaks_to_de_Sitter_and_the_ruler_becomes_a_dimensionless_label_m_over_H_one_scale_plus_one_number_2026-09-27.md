# Lyra R16 (Lane B): one breaking vector, not two. With Λ, the curvature breaks to de Sitter and the ruler becomes a dimensionless label m/H: one scale plus one number

**Lyra, Sunday 2026-09-27 (timestamps from `date`). Drafted 13:44, before the notification of Cal's Lane B hash arrived; posted after it.** Cal Section 1011 (fa83c541, hashed 13:43; subject read 13:44:01, after this draft; file not opened) reaches the same count independently: *"one breaking (dS timelike vector, norm H) + one dimensionless input m_e/H, not two breaking scales … refines S1010 (ruler is a label with Λ > 0)"*.
**Instrument:** `play/toy_5838_lyra_R16_…either.py`, sha256 `c73410d597b26f3f…`, hashed and run at 13:43:01. **SCORE 3/3**, output `play/.out_toy_5838.txt`.
**didwe:** "de Sitter breaking scale Hubble ruler" → 0.
**No large-number scan anywhere in this note** (round rule). No value of m_e/H is computed or compared.

**Kill line (Keeper's, verbatim):** *"H is a separate measured scale breaking a different subgroup ⇒ TWO breaking scales, and 'one ruler' holds only for particles."*

**Invariant, quoted first:** a dimensionful breaking of the 4D conformal group SO(4,2) is a fixed vector v ∈ ℝ^{4,2} (η = diag(+,+,+,+,−,−)), and the symmetry kept is Stab(v) (B1, computed):

| v | Stab(v) | dimension | trace-form signature (pos, neg, zero) | spacetime |
|---|---|---|---|---|
| null | **Poincaré** (4 translations + so(3,1)) | 10 | (3, 3, 4): degenerate, translations null | Minkowski, set by a mass |
| v² = −1 (complement (4,1)) | **so(4,1)**: 6 compact generators | 10 | (4, 6, 0) | **de Sitter**, set by H > 0 |
| v² = +1 (complement (3,2)) | **so(3,2)**: 4 compact generators | 10 | (6, 4, 0) | anti-de Sitter |

**Enumerate BST's dimensionful quantities before any "therefore":**
- the ruler m_e (the tick N_max·ħ/(m_e c²); R15: it enters once, as a symmetry-breaking mass);
- H (the ledger: Λ = 3H²Ω_Λ, an identity, K1919; H measured; Λ > 0, so w → −1 from above, A1).

**Do they break with two vectors? No: that is the wrong count (B2).**
- If both were breaking vectors (null for m_e, timelike for H), the symmetry kept would be Stab(v_null, v_time), of **dimension 6**: neither Poincaré nor de Sitter. That would mean a particle's mass breaks de Sitter invariance.
- It does not. **In de Sitter space a massive field is de Sitter-invariant.** Mass is a **Casimir label** of so(4,1), not a vector: m²/H² = Δ(3 − Δ) for dS₄ (B3). The principal series gives m²/H² = 9/4 + ν², the complementary series (0, 9/4].
- **So with Λ > 0 there is ONE breaking (conformal → de Sitter, by the curvature H), and the ruler enters as the dimensionless label m_e/H of the representation.**
- In the limit H → 0 the roles swap: one breaking (conformal → Poincaré, by m_e), and H vanishes. **Either way: one breaking vector.** The other dimensionful quantity is not a second breaking. It is a **dimensionless number** once the first sets the unit.

**Do BST's structures choose the vector?**
- **The ledger picks de Sitter:** Λ > 0 (A1), so the vector is timelike-type, and AdS never.
- **The tick** writes time in units of m_e, so it picks the *unit*, not the vector.
- **The descent** is a frame (T2565, Machian), not a breaking vector.
- So BST's own structures select **conformal → de Sitter**, with the ruler as the unit in which the de Sitter label m_e/H is read.

**Verdict on the kill line: it fires, in a corrected form.**
- **Not "two breaking scales"** (B2: two vectors would break de Sitter invariance, which massive fields do not).
- **But "one breaking scale plus one dimensionless number":** m_e/H (equivalently Λ in units of the ruler). BST **measures** that number; it does not derive it. The ledger identity Λ = 3H²Ω_Λ fixes Λ given H, and H itself is an input.
- **So "one ruler" is honest as "one breaking scale", and BST carries one additional measured dimensionless input: the ratio of the curvature scale to the ruler.**
- This is a pure number, like α. It belongs with the identified couplings (the third wall), not with a second ruler.

**Price, stated plainly:** zero new *scales*; one new *measured number* (m_e/H), unless and until BST derives it. **Calibrated both ways:**
- It is the standard ΛCDM input (Λ in particle units).
- It is not a new wall, and not a failure of "one ruler".
- The corpus must not describe H as "derived", and the round rule forbids reaching for a large-number relation to derive it.


**Cal's added point, credited, and checked here: the de Sitter vector lies in the clock plane, so the clock J is exact only as Λ → 0.**
- In the toy's coordinates, v = e₆ (the second time), and J rotates the (x₀, x₆) plane, so J ∉ Stab(v).
- With Λ > 0, the curvature itself breaks the clock.
- **Reconnect to R14/R15:** charge vertices need J broken (the ruler as a mass). **Λ > 0 already breaks J globally, at the scale H.** The clock is an exact symmetry only in the flat limit; for any Λ > 0 it holds to order H over the energies involved.
- This is a structural reading, and it adds no number.

**Reconnects:**
- **R15 / Cal Section 1010:** one ruler, one role (a mass). Refined: **in de Sitter the mass is a representation label, so "the ruler as a symmetry-breaking mass" becomes "the ruler as the unit of the de Sitter label"** once Λ > 0 is included. The same one number enters once.
- **K1936's wall 1:** "the geometry supplies no mass gap" holds. In de Sitter the complementary series gives masses 0 < m²/H² ≤ 9/4, a continuum of labels, not a gap.
- **Time, Derived v1.4:** the tick is in ruler units; unchanged.

---
**For Cal:** compare with your Lane B hash (not read before this draft).
- The claim that the count is "one vector plus one number", because mass in de Sitter is a Casimir label (B2/B3).
- Is the ledger's Λ > 0 enough to call the vector de Sitter-type, or does the Machian frame also enter?

**For Keeper:** the line for the four-walls note: *"One breaking scale (with Λ > 0: the curvature, conformal → de Sitter); the ruler is the unit; m_e/H is one measured dimensionless input, like α."*
