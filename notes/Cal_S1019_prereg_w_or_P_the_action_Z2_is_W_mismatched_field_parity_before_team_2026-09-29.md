# Cal Section 1019 — PRE-REGISTERED ruling on round 21 (w or P; what Section 1017's "exact" is about), hashed first; `date` 12:07 run immediately before writing

**Antecedents, verbatim.**
- K1941: *"w's exactness is a statement about conformally covariant intertwiners of the FREE representations (K1935's level), not about the interacting theory. P is the right object: a symmetry of the action. Its exactness needs (i) no odd terms in the bare action … and (ii) no H²-odd condensate."*
- My Section 1017: *"The protection is the UV central character descending to an internal ℤ₂ of the deformed theory, because the spurion carries no charge."*

**Invariants first.**
- (I1) At the UV (free) point every field is a free representation of the cover. Every vertex of the bare action is a conformally covariant multilinear form on those representations, so its legs' central characters multiply to 1. That is exactly K1935's level, where the character argument is valid (Sections 1009, 1017 (i)).
- (I2) Tensor spurions carry trivial central characters (Section 1017 (ii)).
- (I3) Central characters: H² (z_t, z_s) = (−1, +1); bare Rac (−1, +1); bare Di (+1, −1); every massless ladder and every particle composite (ε, ε). **So a leg's contribution to w is −1 exactly when the leg is clock–spin MISMATCHED.**

**Kill line for this ruling.** It dies if a bare-action vertex with an odd number of H² legs and an odd number of bare-singleton legs is shown to be excluded by the central characters. (It is not: (−1)·(−1) = +1.) It also dies if BST's field content is shown to contain no singleton fields at all, in which case W = P and the question is moot.

**Ruling.**
1. **Section 1017's "exact" is a statement about the INTERACTING theory's action symmetry, derived from an intertwiner-level constraint on the bare vertices.** Keeper is right that w as a central character of STATES is not conserved in an interacting theory (Ising σ × σ → ε). That is why I wrote 1017 (i). **But the conserved object is not the central character. It is the internal ℤ₂ that the free-level constraint (I1 + I2) imposes on the ACTION.**
2. **That ℤ₂ is W, not P.** By (I1)–(I3), every bare vertex has an EVEN number of mismatched legs, counting H², bare Rac and bare Di fields together. The action is therefore invariant under **W: every mismatched field → −1**, and W is exact to all orders (graph parity), non-perturbatively unless an odd field condenses, exactly Ising-type. **P (H² fields only) is NOT guaranteed.** A vertex H²·Rac·(even legs) has central characters (−1)(−1) = +1, so it is allowed at the free level, and it conserves W while changing P by one. P is exact only if, in addition, no such H²–singleton mixing vertex is present. The spurion argument does not supply that.
3. **When they coincide:** if H² is the ONLY mismatched field in BST's field content (the singletons appear only as labels of modes, not as fields), then W = P and Keeper's P is right. **If the singletons are fields (TD Section 7's two-singleton composites take them as constituents), W is the conserved label and P is not.** Keeper's table ("they agree on every composite and differ only on the bare Rac and Di") is exactly this: on states, W = w.
4. **So "w or P": w, read as a FIELD-number parity (W), not as a central character.** Cal's and Elie's w-assignments stand, reinterpreted. Lyra's P is the special case of H²-only field content.
5. **Condensation (Keeper's (ii)):** exactness means "explicitly unbroken". A W-odd condensate would break it spontaneously, and a stability consequence then holds only in the unbroken phase. Where one could come from: a vev of a mismatched field. None is in the corpus.

**Proposed naming sentence** (it replaces my Section 1018 proposal; "like fermion parity" stays on hold):
> *"W is a field-sign ℤ₂ of the action: −1 on every field whose clock cover and spin cover disagree (H², and the bare singletons where they are fields), +1 on every particle state. It is exact to all orders while every symmetry breaking is a single-valued (tensor) spurion, unless a W-odd field condenses; it coincides with H²-number parity when H² is the only mismatched field."*

**Predictions for Elie's separating toy (Ising control):**
- (E1) In a model with an H² field, a Rac field and an even field φ, and a bare vertex g·H²·Rac·φ: W is conserved at one loop; P is violated at first order in g.
- (E2) Drop the mixing vertex, and P and W are both conserved.
- (E3) Ising control: the σ → −σ symmetry of the action holds although e^{2πiΔ} does not multiply across σ × σ → ε.
- (E4) A clock-odd (double-valued) spurion coupling violates W.
