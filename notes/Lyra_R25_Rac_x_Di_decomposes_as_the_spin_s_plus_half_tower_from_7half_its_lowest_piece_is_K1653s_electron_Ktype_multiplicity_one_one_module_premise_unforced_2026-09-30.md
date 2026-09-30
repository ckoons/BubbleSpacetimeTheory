# Lyra R25: Rac⊗Di decomposes as the spin-(s + ½) tower from 7/2. Its lowest piece is K1653's electron K-type, with multiplicity one: one module, and the premise is still unforced

**Lyra, Wednesday 2026-09-30, 11:03 EDT (from `date`).**
**Instrument:** `play/toy_5854_lyra_R25_…mult_1.py`, sha256 `152892ad9afb8610…`, hashed and run at 11:01:00. **SCORE 4/4**, output `play/.out_toy_5854.txt`. **Full SO(5) characters** (Weyl character formula at five random torus points, four levels above the bottom), not dimensions.
**Order:** Cal hashed Section 1026 at 11:00. I read its subject at 11:01:07, **after my toy ran**; the file is not opened. We agree (below).
**Also done:** F680's dated correction head (f8db8cf9): k_min = 3 is the first Wallach point, not the EHW L² threshold. A second F680 inconsistency (its "k = 6 bulk Bergman") is flagged.

**Group, family, action (stated first):**
- K = SO(5) × SO(2); SO(5) = B₂ with highest weights (x, y), x ≥ y ≥ 0.
- **Rac** K-types: (a, 0) at clock 3/2 + a. **Di** K-types: (a + ½, ½) at clock 2 + a (spinor harmonics on S⁴; E₀ pinned by K956).
- p⁺ = the SO(5) vector (1,0). Generalized Verma V(λ; τ) = τ ⊗ Sym(p⁺).
- A conserved spin-j piece is V minus its divergence submodule.

**Kill line (Keeper's, restated):** *"a multiplicity or K-type mismatch between the two"* (K1653's substrate-Dirac mode vs Rac⊗Di's lowest piece).

---

## 1. The decomposition (C2, exact to four levels in full characters)

> **Rac ⊗ Di = H(7/2; (½,½)) ⊕ ⊕_{s ≥ 1} [ spin-(s + ½) conserved at 7/2 + s ]**, where the s ≥ 1 pieces are V(7/2 + s; (s + ½, ½)) minus V(9/2 + s; (s − ½, ½)).

- **Control C1:** the scalar Flato–Fronsdal identity Rac⊗Rac = V(3; 0) ⊕ Σ_s [spin s conserved at 3 + s] holds in full SO(5) characters.
- **Negative control C4:** dropping the divergence subtraction fails.
- **The lowest piece is H(7/2; (½,½)):** the SO(5) spinor **4**, at clock 7/2. **At clock 7/2, the spinor (½,½) occurs with multiplicity exactly 1 in Rac⊗Di** (C3: the bottom level is χ_(0,0)·χ_(½,½)).
- **7/2 is an interior point** of the spinor family (unitary from 2; discrete series above 9/2; K1945). **H(7/2; (½,½)) is the full generalized Verma module,** with no reduction there, while every s ≥ 1 piece sits at its conservation bound. That is the fermionic Flato–Fronsdal pattern: one massive-type spin-½ piece at the bottom, then conserved spinor-tensors.

## 2. Against K1653's electron

**K1653, verbatim:** *"the electron is the K-type V_(1/2,1/2)^{(0)}"*.
- **K-type: match.** (½, ½) is the SO(5) spinor 4, the lowest K-type of the lowest summand.
- **Level: match.** The superscript (0) is the bottom level. The spinor recurs at higher levels inside H(7/2; ·) (e.g. (1,0) ⊗ (½,½) ∋ (½,½) at 9/2), but the level-0 copy is unique.
- **Multiplicity: match** (1).
- **The one correction to K1653's wording:** "on H²(D_IV⁵)" is wrong for it (Cal Section 1018 P2). **Its home is H(7/2; (½,½)), the lowest summand of Rac⊗Di.**
- **Kill line: does not fire.** There is no K-type or multiplicity mismatch.

## 3. What this closes, and what it does not

- **Closes (Cal Section 1026, by its subject, and this note independently): one module.** K1653's substrate-Dirac mode and Time, Derived's Rac⊗Di fermion are **the same object**: the lowest summand H(7/2; (½,½)). **The singleton-vs-constituent dichotomy K1653 flagged dissolves for fermions.** It is one module, read two ways.
- **Does not close: the premise.** That the *physical* electron *is* this module (rather than, say, a mode of some other spinor-family member) is still Time, Derived's premise. Nothing in D_IV⁵ forces the fermion to be a two-singleton composite. **ν = 7/2 stays DERIVED GIVEN THE PREMISE (tier C).** What this round adds is that the premise now has **one** reading, not two.
- **For Time, Derived's parenthesis "(Section 7's premise; open per K1653)":** the "open per K1653" half can be re-worded as **"one module, per K1653 and Rac⊗Di (R25)"**, and **"a premise"** stays. That would be a v1.6 matter on Casey's word, not proposed today.

---
**For Cal:** Sections 1–3; the tier stays C (agreed with Section 1026's "one premise no").
**For Keeper:**
- K1653 re-key: "the electron is the lowest K-type of H(7/2; (½,½)) ⊂ Rac⊗Di (R25), not a mode of H²".
- F680's second flag (k = 6) goes to whoever owns the electron-mass paper's k-ladder.
**For Casey:** your two paper edits (K1945 item 4) are unaffected. F680's correction is in my own note only.
