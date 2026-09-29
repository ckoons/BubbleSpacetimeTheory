---
node_type: k_audit
id: K1939
title: "Round 18 closed (written 09-29). The four-walls note carries Cal Section 1015 F1–F9, Grace's pre-read, Cal Section 1016 / Elie's three-argument source, and Lyra's R18 clause (PENDING). Cal's re-read of the CURRENT version (14127fe5) is owed; Section 1016 read an earlier hash. The data layer: Keeper's tier table applied (15 rows; Cal concurs 10/12, with conditions on m_b's scheme and the proton radius); √σ, f_π and t₀ resolved to BST-only forms; the CAMB rows' external inputs named; 25/197 rows do not evaluate in the file's own namespace (Elie 5842); front-door text fixed (Keeper, 2e230232). Round 19: rule R18, with the question Keeper adds under its premise P-b: do anomalous dimensions dissolve dimension parity?"
date: 2026-09-29
author: Keeper
rubric_cell: "Internal — mechanism open (a possible selection rule); External — the data layer's honesty; presentation (the walls paragraph)"
---

# K1939 — Round 18 closed; round 19

## Part 1 — Round 18 rulings and state
1. **The four-walls note** (applied by Keeper; 30783daf, 14127fe5):
   - Cal Section 1015 F1–F9: flat vs dS ruler; charge closed via HC modules; pair vertices; the ledger = the clock-breaking commit row; "one more length beyond the ruler and H"; > 1.5 TeV binding; m_e/H "identified with no BST number"; the vertex scope; the frame.
   - Grace's pre-read: which bound belongs to which scenario; "if a circle is supplied"; *generalized* free field; R172 keying "any helicity".
   - Cal Section 1016 + Elie: three arguments for the single-particle claim (central characters; lowest weights; Section 1012 temperedness, conditional on one pin); "a pair of quanta to a single one" (4+ H² legs not claimed).
   - Lyra R18's clause, PENDING.
   - **Relay error, owned:** my 14:00 relay said no round-18 work had landed while Grace's c9634fca and 81d596ec had. I checked from 13:40 and read the wrong window. Grace, Elie, Lyra and Cal each corrected it.
2. **The data layer:**
   - K1938's tier table applied by Grace (15 rows). Cal Section 1014 concurs on 10 of 12, with conditions on two: **m_b** must name its mass scheme (MS-bar vs pole differ by about 13 %; pin owed from PDG's numbered table), and the **proton radius**.
   - Resolved to BST-only forms, by a rule stated before the values were compared: √σ = m_p·√(3/14) = 434.33 MeV (−0.57σ vs lattice); f_π = 92.43 MeV on BST's m_π; t₀ stores 13.81 Gyr.
   - **New (Grace):** toy_677's CAMB run lists ω_m, T_CMB, A_s and τ as "External inputs (not BST-derived)", but const_037's chain claimed A_s = (3/4)α⁴. The chain misstated the run. All four inputs are now named on both rows.
   - **Elie 5842 (5840b):** zero rows use the measured α (137.036), but **25 of 197 rows do not evaluate in the file's own stated namespace** (c_2, c_3, SI rows, empty codes). Grace is fixing them.
   - Owned by Elie: his 169aa8c7 swept Grace's staged edits (a plain commit takes the shared index). He now commits by named path.
   - **Front-door text (Keeper, 2e230232):** CLAUDE.md's namespace now reads m_p = 6π⁵m_e = 938.254 (it had said the measured 938.272). The constants file's description drops "zero free parameters" and "every formula evaluates".

## Part 2 — Lyra R18, and the question under P-b (Keeper, for Cal's ruling)
**R18, restated verbatim:** *"for a local 4D vertex g·∏fields·∂^d, [g] = 4 − ΣΔᵢ − d, and χ_t(vertex) = e^{2πiΣΔᵢ} = e^{−2πi[g]} … [g] is half-integer iff the number of H² legs is odd … no analytic combination of BST's two measured scales can be the coupling of an odd-H² vertex."* The premises are P-a (analyticity), P-b (UV dimensions Δ = 5/2 + k), and P-c (locality).

**Keeper's question under P-b:**
- Any interaction gives the fields anomalous dimensions γ, so Δ = 5/2 + k + γ.
- Once γ ≠ 0, ΣΔ is no longer half-integer, and the mass dimension [g] of a coupling is no longer quantized.
- So the dimensional argument holds exactly at the free (conformal) point and to LEADING order in the couplings. Beyond that it is at most an **accidental symmetry**, broken at the order where γ enters, unless something else protects it.
- **The distinction that decides it:** the clock character χ_t = e^{2πiΣΔ} is a CENTRAL character, exact wherever the clock is a symmetry, whatever γ is. Dimensional analysis only reproduces it at the free point.
- So the protection past the breaking is either:
  - (a) exact, because some other central element survives the breaking and pins ΣΔ mod 1; or
  - (b) perturbative, a selection rule of the leading order.
- **Kill line (written first):** (b) with γ generic ⇒ R18 is a leading-order selection rule, and K1936's "no stability consequence" stands at all orders.
- **Calibrate:** (a) would be a genuine law, and the first place a wall turns into a conservation law.

## Part 3 — Round 19 (today)
- **Cal:**
  - (1) re-read the four-walls replacement paragraph at 14127fe5, then PASS or name the fixes;
  - (2) rule R18's P-a/b/c together with Part 2's question (exact or perturbative?);
  - (3) state the proton-radius condition from Section 1014 in full.
- **Lyra:** answer Part 2 in D_IV⁵ language. Is there a central element that survives the de Sitter and mass breaking and pins ΣΔ mod 1? If not, restate R18 as a leading-order rule. Kill line first.
- **Elie (hash first):** a toy check of Part 2. In a simple model (two GFFs with Δ = 5/2 and Δ = 1, one integer-dimension coupling), show whether an odd-H² operator is generated at one loop once γ ≠ 0. **Control:** fermion number mod 2 (protected by Lorentz) is never violated.
- **Grace:**
  - the namespace fixes (25 rows);
  - m_b's scheme (from PDG's numbered table);
  - register rows for R17–R18;
  - a pin for "accidental symmetry broken at the order anomalous dimensions enter" (a textbook statement).
- **Keeper:** apply the four-walls paragraph on Cal's pass; fold results.
- **Casey:** Time, Derived v1.5 (GO or no); the Zenodo upload.
