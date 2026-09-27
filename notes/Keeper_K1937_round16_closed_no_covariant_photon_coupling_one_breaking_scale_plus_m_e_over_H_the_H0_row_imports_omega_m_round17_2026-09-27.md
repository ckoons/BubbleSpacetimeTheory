---
node_type: k_audit
id: K1937
title: "Round 16 closed. (A) H² has NO conformally covariant coupling to the photon through its records, of any kind (charge or magnetic-moment type). The 'ν = 0 edge' was a non-unitary family (Elie withdrew 5837's edge claim); the records are spherical series; the photon lives in a non-unitary field representation at Δ = 2 and is not tempered, so it cannot be a piece of anything on the unitary axis. Conditional on the Knapp pin and Cal's read. (B) One breaking scale plus one MEASURED dimensionless number m_e/H, like α (Cal Section 1011, hashed; Lyra). With Λ > 0, de Sitter SO(4,1) survives, and Λ breaks the clock J at order H: 'J is the time' is exact only as Λ → 0. (C) Keeper found that the data layer's H₀ row (67.29 vs 67.36) is √(ω_m/Ω_m) with ω_m = 0.1430 MEASURED: an Ω_m consistency, not an H prediction."
date: 2026-09-27
author: Keeper
rubric_cell: "Internal — mechanism open; External — the data layer's honesty (a dimensionful input hidden in a formula); presentation (the four walls with the de Sitter refinement)"
---

# K1937 — Round 16 closed; round 17 (the last before EOD)

## Part 1 — Round 16 rulings (Grace 06bde408; Elie 5839 6/6, ebdceafb, with the 5837 correction posted first; Lyra 5838 3/3; Cal Section 1011, hashed 13:43:41)
1. **No covariant photon coupling through the records, of any kind.**
   - **Elie withdrew 5837's "photon at the ν = 0 edge"** before running anything new. The family searched there (built from finite-dimensional Lorentz spins, as in Euclidean field theory) is not unitary for SO(4,2). The records are the SPHERICAL series (Ørsted–Zhang).
   - Grace: in the scalar family no massless ladder sits at ν = 0 (Howe–Tan: "the only value of a that gives a decomposable module"). Every piece has equal left and right spin, and a nonzero-helicity ladder never does. The photon sits at Δ = 2 only in Dobrev's family, induced from a non-unitary Lorentz representation.
   - Elie 5839: the photon is the solution space of both halves of Maxwell's equations, conformal only at Δ = 2, inside a non-unitary field representation. A unitary induction from a tempered representation decomposes into tempered pieces only (Knapp; **pin owed**). The photon is not tempered (5830/5832), so it is a piece of nothing on the unitary axis.
   - **Keeper's kill line resolves to "not a subquotient".** Conditional on the Knapp pin and Cal's adversarial read.
   - **Keeper owns:** K1936 carried 5837's "one open edge, only helicity 1 at ν = 0" as fact into its title and the four-walls note, without asking which family the representation was in. A family is a premise; state it.
2. **One breaking scale, plus one measured number** (Cal Section 1011, hashed first; Lyra 5838 independently; Keeper's corrected dS/AdS assignment used by both).
   - With Λ > 0 and massive particles, de Sitter SO(4,1) survives: the stabilizer of one TIMELIKE vector, whose length sets H.
   - A particle's mass is a LABEL of an SO(4,1) representation (m²/H² = Δ(3 − Δ)), not a second breaking.
   - So m_e and H are **one unit plus one dimensionless ratio, m_e/H, measured, not derived, like α.** It was not scanned (the round's rule). The price list gains one number and no posit.
   - **Cal refines his own Section 1010:** "the ruler enters as the symmetry-breaking mass" is exact only in the flat Λ → 0 description.
   - **New (Cal; Lyra checked):** the de Sitter vector lies in the clock's own plane, so **Λ > 0 breaks BST's elliptic clock J at order H.** The surviving cosmic time is the de Sitter boost (continuous spectrum). "J is the time" is exact only as Λ → 0. This is harmless for particle physics (H ≪ every particle scale). The ledger (Λ = 3H²Ω_Λ, w ≡ −1) is the one BST structure that selects that vector.
   - **Time, Derived should say so in one parenthesis. That is an edit to a GO'd paper: CASEY'S WORD.**
3. **The mod-2 and one-ruler pieces from round 15 stand** as refined above.

## Part 2 — The H₀ row (Keeper, 15:49; the data layer)
- `data/bst_constants.json` const_100 (T703): "Hubble constant H₀ = 67.29 km/s/Mpc from BST ΛCDM (Ω_Λ = 13/19, Ω_b = 18/361, n_s = 1 − 5/137)", tier I, "0.10 % from Planck", status "derived".
- **Recomputed:** Ω_m = 6/19 = 0.31579; with the MEASURED ω_m h² = 0.1430 (the row's own chain: "Full CAMB … Ω_m h² = 0.1430"), h = √(0.1430/0.31579) = 0.67293, so **H₀ = 67.29.**
- **The dimensionful content of "H₀" is Planck's measured ω_m, divided by BST's dimensionless Ω_m.** The row is the Ω_m = 6/19 consistency restated in km/s/Mpc, not a prediction of H.
- Grace's 08-02 tier review ("inherited, bounded by the weakest input") was right about the tier but missed the hidden dimensionful input.
- **Fix (Grace, data layer):** name ω_m h² = 0.1430 (measured) as an input on the row's face; "status: derived" → "consistency (Ω_m), H imported via ω_m"; the precision field then measures Ω_m's agreement, not H's. **This is the same species as the verify_bst PASS rows: a match whose weight comes from an input the reader cannot see.**

## Part 3 — Round 17 (the last before EOD; Casey calls it)
- **Lane A (Cal, Grace):** the Knapp pin (unitary induction from tempered ⇒ tempered pieces), and Cal's adversarial read of Elie 5839. Close the photon lane.
- **Lane B (Grace, Elie): the data-layer sweep for the H₀ species.** Rows in `data/bst_constants.json` whose `bst_value` carries a MEASURED dimensionful (or dimensionless) input that is not named in the formula (like ω_m).
  - Kill line: none besides H₀. Enumerate by method, not memory: parse the `formula_code` and `derivation_chain` for numeric literals that are not BST integers, α or the ruler.
  - Elie builds the instrument, with a control that must catch H₀; Grace fixes the rows.
- **Lane C (Lyra): the de Sitter clock.**
  - One paragraph: what Λ > 0 does to H²'s discrete clock spectrum (broken at order H; the dS boost as cosmic time).
  - The one-parenthesis wording for Time, Derived (for Casey's word).
  - Reconnect the ledger picture (K1919–K1921) and T2632 (no redshift from the elliptic/parabolic difference).
- **Lane D (Keeper):** the four-walls note final (no covariant photon coupling; one breaking scale + m_e/H; J exact only as Λ → 0), then Cal's cold read. The TOMORROW file.
