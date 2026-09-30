---
node_type: k_audit
id: K1946
title: "Round 25 closed: ONE MODULE (Cal Section 1026 hashed; Lyra 5854 in full SO(5) characters; Elie 5855 an exact character identity to depth 5): Rac⊗Di's lowest piece is L(spinor, 7/2) with multiplicity one, which is K1653's electron K-type. K1653's dichotomy dissolves for fermions. The premise stays unforced (tier C), and it is the fermion FAMILY's module, not the electron's (Cal Section 1027). Round 26 follows what the decomposition exposed: Rac⊗Di carries CONSERVED spin-(s + ½) currents, the first a conserved spin-3/2 current, i.e. a supercurrent. BST's singletons have the field content of a free 5D hypermultiplet (Δ = 3/2 scalars, a Δ = 2 fermion), whose free theory is F(4)-superconformal (Nahm: the 5D superconformal algebra is F(4); corpus K434). BST's Forbidden list includes 'a SUSY spectrum'. Is the spin-3/2 current broken with the higher spins, or does a BST structure keep it?"
date: 2026-09-30
author: Keeper
rubric_cell: "Internal — mechanism open (a free-level symmetry and its fate); External — the Forbidden list's SUSY clause checked against BST's own structure"
---

# K1946 — Round 25 closed; round 26: the spin-3/2 current

## Part 1 — Round 25 rulings (Cal Sections 1026–1027; Lyra R25 6bfcaa76, toy 5854 4/4; Elie 5855 5/5, d000f037; Grace a7ea3e81, register v0.41)
1. **One module:** Rac⊗Di = L(spinor, 7/2) ⊕ (conserved spin-(s + ½) pieces at 3 + s for s ≥ 3/2, i.e. at 7/2 + (s − ½)). It is a half-integer Flato–Fronsdal (Lyra; Elie exact to depth 5).
   - The lowest piece has multiplicity one and K-type V_(1/2,1/2) = K1653's electron slot.
   - Controls: Rac⊗Rac reproduces 5822; Di⊗Di has no half-integer-spin piece.
   - Treating every piece as unconserved breaks the identity, so the conservation above spin ½ is real (Elie).
   - The spin-½ piece sits above the spinor endpoint 2, so it is an ordinary irreducible module, not a current.
2. **The premise stays unforced** (Cal; Lyra): representation theory cannot tell "posit L(spinor, 7/2)" from "build it as Rac⊗Di". So **ν = 7/2 is derived given the two-singleton premise (tier C).** The premise now has one reading instead of two.
3. **Wording (Cal Section 1027):** it is the fermion FAMILY's module (the electron, muon, neutrino and quarks sit there; species labels live beyond). K1653's re-key must say "the fermions' module", not "the electron is …".
4. **Lyra's F680 correction head** (f8db8cf9) matches the EHW fix. She also flags a second issue: F680's "bulk Bergman k = 6" is a Casimir parameter, not a point on ν = k/2, where Bergman sits at ν = 5.
5. **Casey's queue:**
   - GO or no on the ElectronMass/Ribbon correction (Cal recommends GO);
   - Cal's Time, Derived Section 7 re-word (v1.6);
   - the Zenodo upload.

## Part 2 — Round 26: the conserved spin-3/2 current
**What the decomposition exposed:** at the free level, Rac⊗Di carries a conserved spin-3/2 current (the s = 3/2 piece). In field theory a conserved spin-3/2 current is a **supercurrent**.

**Known structure (Keeper; pins owed to Grace from numbered sources):**
- **Nahm (1978):** superconformal algebras exist only for d ≤ 6, and **in d = 5 the superconformal algebra is F(4)** (bosonic part so(5,2) ⊕ su(2)). The corpus already has it: **K434 (06-20) "F(4) is basic classical exceptional, the 5D superconformal"**, and K443 (Coleman–Mandula on F(4)).
- **The free 5D hypermultiplet:** scalars at Δ = 3/2 and a symplectic-Majorana fermion at Δ = 2, which are **exactly BST's two singletons (Rac₅, Di₅)**, up to multiplicities and the su(2)_R labels. Its free theory is F(4)-superconformal. **The pin owed:** the hypermultiplet as an F(4) supersingleton (Günaydin et al.; Fernando–Günaydin is already in the corpus for the Rac).
- **BST's Forbidden list:** *"any confirmed detection kills the framework: … a SUSY spectrum."*

**The question:** at the free level, BST's singleton content carries a conserved supercurrent. **Is it broken, like the higher-spin currents (round 10: any interaction breaks s > 2, and spares s = 1 and 2 by locality and global symmetry), or does a BST structure keep it exact?**
- The breaking pattern of round 10 extended to half-integer spin: an interacting theory with a stress tensor keeps only the stress tensor and the global-symmetry currents. **A spin-3/2 current survives only if the theory is supersymmetric.**
- Candidate protectors, enumerated before preferring any: the clock sign Z_t (does it pair Rac and Di?); the ℤ₂ structure of the Šilov boundary; the one breaking scale (a tensor spurion, so SUSY-neutral? or not?); the commit.
- **Kill line, written first:** if a BST structure keeps the spin-3/2 current exactly conserved after the breaking, BST predicts superconformal / supersymmetric structure, which **contradicts its own Forbidden list.** One of the two must go, and it gets said plainly.
- **Calibrate the other way:** if nothing keeps it, the statement is "BST's singletons form a free supermultiplet whose supersymmetry is broken with the higher spins": structure, consistent with the Forbidden list, and **a precise reason BST predicts no SUSY spectrum** rather than a bare posit. That would upgrade a Forbidden-list item from an assertion to a consequence.
- **Menu risk:** "hypermultiplet" matches field content (Δs and spins). Whether the multiplicities and the su(2)_R structure match is part of the check. **Do not claim the match before counting.**

## Part 3 — Lanes
- **Cal (first, hashed):**
  - Is the conserved spin-3/2 piece a supercurrent in the field-theory sense (does its charge anticommute into the stress tensor's charges)?
  - Does any BST structure keep it after the breaking?
  - Is the Forbidden list's SUSY clause then a consequence or a posit?
- **Lyra:**
  - the singleton content against the F(4) supersingleton (multiplicities; su(2)_R); reconnect K434, K443, F235 (the "substrate superalgebra F(4) candidate");
  - the protector enumeration; kill line first.
- **Elie (hash first):**
  - (i) verify the conserved spin-3/2 piece of Rac⊗Di and its weight (3 + 3/2 = 9/2) with a character identity;
  - (ii) count the free hypermultiplet's content against Rac₅ ⊕ Di₅ (dimensions of the K-types, multiplicities).
  - Control: the free scalar, where there is no spin-3/2.
- **Grace:**
  - pin Nahm 1978 (the d = 5 superconformal algebra is F(4)) and the free hypermultiplet's F(4) representation from numbered sources;
  - K1653's re-key per Cal Section 1027 ("the fermions' module");
  - the EHW original when your agent lands.
- **Keeper:** fold; Casey's three items.
