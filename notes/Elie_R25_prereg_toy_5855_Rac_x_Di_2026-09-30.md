# Elie — round 25 PREREG, toy 5855: Rac⊗Di of SO(5,2) by K-type counting — 2026-09-30 11:01 EDT, before any code
Antecedent (K1945 Part 2, verbatim): "compute Rac⊗Di's lowest summand by K-type counting. Control: the scalar Rac⊗Rac (Flato–Fronsdal, 5822). Negative control: Di⊗Di." Cal's kill: "a multiplicity or K-type mismatch between the two" (K1653's substrate-Dirac mode, V_(1/2,1/2), vs Rac⊗Di's lowest piece).
Groups, families and sources: Rac₅ (λ = 3/2, K-types H_m(ℂ⁵) at 3/2 + m; 5822); Di₅ (spinor singleton, SO(5) (m+½, ½) at 2 + m; 5846, pin owed; its endpoint status CONFIRMED by 5853). K = SO(5)×SO(2) characters; SO(5) weights by Freudenthal (5792).
Checks:
(1) the LOWEST K-type of χ(Rac)χ(Di): weight 3/2 + 2 = 7/2, SO(5) type (½, ½) (the spinor), multiplicity 1: exactly K1653's electron K-type.
(2) the full decomposition as a character identity to depth 5: χ(Rac)χ(Di) = [s = ½ module at 7/2, generic: t^{7/2} χ_{(½,½)}·S] + Σ_{s ≥ 3/2} [conserved spin-s module at 3 + s: t^{3+s} χ_{(s,½)} S − t^{4+s} χ_{(s−1,½)} S] (the 5D half-integer Flato–Fronsdal pattern; HYPOTHESIS tested, not assumed). NEGATIVE: generic characters for every s FAIL the identity.
(3) CONTROL: Rac⊗Rac reproduces 5822's identity (scalar at 3 + conserved currents at 3 + s).
(4) NEGATIVE CONTROL: Di⊗Di contains NO K-type with half-integer spin (in particular not (½,½)): its lowest K-types are at weight 4, with SO(5) content (½,½)⊗(½,½) = (1,1) ⊕ (1,0) ⊕ (0,0).
DIRECTION: (1)–(4) hold. Rac⊗Di's lowest summand is a single spinor module at 7/2 with lowest K-type (½, ½), multiplicity one, and it is NOT at a conservation bound (7/2 > 2, the spinor unitarity endpoint from 5853), so it is a generic (irreducible generalized-Verma) module. This matches K1653's K-type; the module identification is Cal's to rule.
KILL: the lowest K-type ≠ (½,½) at 7/2, multiplicity ≠ 1, or (2) fails with the stated characters.
