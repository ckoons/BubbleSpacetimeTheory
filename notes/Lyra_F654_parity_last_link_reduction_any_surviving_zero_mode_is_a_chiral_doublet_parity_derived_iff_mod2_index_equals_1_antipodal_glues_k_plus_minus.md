# F654 — Parity last-link, the projection/reduction (my piece of Item 1). Plain statement: **parity is derived ⟺ the mod-2 index of the Z₂-projected, k=1-instanton Dirac operator = 1.** Reason: the instanton bundle is the **isospin SU(2)_L** bundle, so *any* zero mode it produces is an **isospin doublet** — and by the center correlation (6Y ≡ 4t+3d), an isospin doublet has **Y ≠ 0** → the rep (2,Y) is **complex → chiral**. So there is no "sterile Y=0" escape: a surviving mode is *necessarily* a chiral doublet. The only question is **survival** — does a zero mode survive the Z₂ projection (mod-2 index 1) or not (0). The Z₂ structure to feed the index: the antipodal on S⁴ is orientation-reversing, so it **swaps the internal S⁺↔S⁻ (k=+1 ↔ k=−1)** AND flips the spacetime chirality — the surviving mode is the combination invariant under *both* flips. That combined (Pin-equivariant) survival is the mod-2 index — Elie's harness. No theater: the reduction is done; the number is one ℤ₂ computation.

**Lyra, Thu 2026-07-23. Item 1, projection/reduction. Reduced to one bit; handed the bit to Elie.**

## The reduction (plain)
1. **The instanton is the isospin SU(2)_L bundle** over S⁴=SO(5)/SO(4) (k=±1, F652). The Dirac operator coupled to it has its zero modes in the **fundamental (doublet)** — that is what the index k counts. **So every zero mode carries isospin (t=1).**
2. **Center correlation** (charge sector, F650): 6Y ≡ 4t + 3d (mod 6). For an isospin doublet (t=1): color-singlet (d=0) → 6Y≡3 → **Y≡1/2**; color-triplet (d=1) → 6Y≡7≡1 → **Y≡1/6**. Either way **Y ≠ 0.**
3. **Y ≠ 0 ⟹ (2,Y) is complex** (conj(2,Y)=(2,−Y)≠(2,Y)) **⟹ chiral.**
4. **Therefore: any surviving zero mode is a chiral doublet. There is no Y=0 sterile outcome from this bundle.** The doublet-carries-isospin fact + the center correlation remove the "vector-like/sterile" branch *at the level of the reps* — provided a mode survives.

**⟹ Parity derived ⟺ (mod-2 index of the Z₂-projected k=1-instanton Dirac operator) = 1.** One bit.

## The Z₂ structure (what the index computation must carry)
The boundary is the mapping torus (S⁴×S¹)/Z₂, Z₂: (x,ζ)→(−x,−ζ) (non-orientable, K826). On the zero mode ψ₀ (internal S⁺, one spacetime chirality, constant on S¹):
- **Antipodal on S⁴ is orientation-reversing** ⟹ it maps the internal **S⁺ → S⁻** (swaps the two S⁴ spinor bundles = swaps k=+1 ↔ k=−1) **and** flips the **spacetime chirality**.
- **S¹ reflection** ζ→−ζ acts on the constant (n=0) mode.
So the naive "index=1 ⟹ a mode survives" is **NOT** automatic: the antipodal glues the k=+1 and k=−1 sectors and flips spacetime chirality simultaneously. **The surviving mode is the diagonal invariant under (internal swap) × (spacetime flip) × (S¹ reflection).** Whether that diagonal is nonempty = the **mod-2 index** on the mapping torus. That is the one ℤ₂ number.

## Readout (state it plainly)
- **mod-2 index = 1** → one chiral doublet survives → Y≠0 (center correlation) → complex → **parity DERIVED, and locked to the charge sector** (the same U(1)_Y).
- **mod-2 index = 0** → no survivor → **vector-like → parity derived-conditional.**
No third outcome. No "sterile Y=0" branch (the instanton only makes doublets, and doublets aren't sterile). **The eleventh-closure test is exactly this one bit — computed, not asserted.**

## Handoffs (no theater)
- **@Elie** — the one bit: **mod-2 index of the Z₂-projected, k=1-instanton Dirac operator on (S⁴×S¹)/Z₂.** Carry the structure: antipodal swaps internal S⁺↔S⁻ (k=±1) AND flips spacetime chirality; survivor = the diagonal invariant. Your harness. Report **0 or 1** + the surviving rep. My reduction: any survivor is a doublet (I've closed the rep side — it's a chiral doublet, Y≠0, not sterile), so you only need the survival bit.
- **@Grace** — the Y readout is pre-closed by the reduction: any surviving mode is an isospin doublet → Y≠0 (6Y≡3 singlet / ≡1 triplet, mod 6) → complex/chiral. So "read off Y" = "confirm the survivor carries isospin," which it must (it's the instanton doublet). Nothing sterile to worry about.
- **@Keeper** — Item 1 reduced to one bit: parity derived ⟺ mod-2 index=1. The rep side is closed (any survivor is a chiral doublet, Y≠0, via the instanton-is-isospin + center-correlation — no sterile escape). The only open thing is survival (the Pin-equivariant mod-2 index on the mapping torus, with the antipodal gluing k=±1 + flipping spacetime chirality). Elie's number decides it. Held at the eleventh closure until the bit is in.
- **@Casey** — plainly: the last question is one yes/no bit. The instanton makes *isospin doublets* — and a doublet is forced to carry nonzero hypercharge by the same center rule that closed the charge sector, so it's automatically a *complex, chiral* rep. There's no way to get a boring sterile fermion out of this bundle. So the entire parity question is: **does a zero mode survive the boundary's Z₂ or not?** — the mod-2 index, 0 or 1. If 1, parity is derived and it's the same U(1)_Y that closed charge; if 0, it's vector-like. The one subtlety that keeps it honest: the boundary's flip swaps the k=+1 instanton with k=−1 *and* flips spacetime chirality at once, so survival is a real ℤ₂ computation, not a given. Elie runs that number. I've closed everything around it — the survivor's identity is pinned; only its existence is open.

Notes only; no toys/theorems claimed. Parity derived ⟺ mod-2 index=1; any survivor is a chiral doublet (Y≠0, no sterile branch); the bit = the Pin-equivariant mod-2 index (antipodal glues k=±1 + flips spacetime chirality) = Elie's harness. — Lyra
