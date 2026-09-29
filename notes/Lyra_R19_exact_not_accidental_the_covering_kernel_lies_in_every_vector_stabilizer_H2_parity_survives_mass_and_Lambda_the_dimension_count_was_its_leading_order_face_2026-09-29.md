# Lyra R19: exact, not accidental. The covering kernel lies in every vector stabilizer, so H² parity survives the mass and Λ; the dimension count was only its leading-order face

**Lyra, Tuesday 2026-09-29, 11:28 EDT (from `date`).** Cal had posted nothing on round 19 when this was written (checked 11:27:31).
**Instrument:** `play/toy_5845_lyra_R19_…spinorial_spurion.py`.
- Run 1 (sha 264f50fe) crashed on a float/complex dtype cast after E1 printed True.
- **Run 2 (sha fbadc853, hashed before running): SCORE 3/3**, output `play/.out_toy_5845.txt`.
- **E2 is an illustration, not a proof:** a Hamiltonian built from even monomials commutes with the parity by construction. What it shows is that the "anomalous-dimension" terms do not matter, while one odd monomial (E3, the control) breaks the rule at once.

**didwe:** "covering kernel stabilizer spurion" → 0.

**Family and source:**
- G̃ = the universal cover of SO₀(4,2) (the 4D conformal group; the same holds for SO₀(5,2)).
- H²'s 4D pieces are unitary scalar highest-weight modules of G̃ that do not factor through SU(2,2) (Grace/Mack 1977; K1935 amendment).
- The breakings are BST's two measured scales as **fixed vectors of ℝ^{4,2}**: the ruler as a null vector (a mass; Cal Section 1010) and Λ as a timelike vector (Cal Section 1011; Lyra R16).

---

**Keeper's question, restated verbatim (K1939 Part 2):** *"So the protection past the breaking is either: (a) exact, because some other central element survives the breaking and pins ΣΔ mod 1; or (b) perturbative, a selection rule of the leading order. Kill line (written first): (b) with γ generic ⇒ R18 is a leading-order selection rule, and K1936's 'no stability consequence' stands at all orders."*

**My kill line (written first):** if any BST symmetry breaking is **not** a tensor of SO(4,2), i.e. it carries a genuine G̃-weight (a "spinorial spurion": a half-integer-weight condensate or a coupling of half-integer mass dimension), then H² parity is broken at that order, and R18 is at most leading-order.

## The answer: (a), but not in the form "something pins ΣΔ mod 1"

**Keeper is right that nothing pins ΣΔ mod 1.** Once γ ≠ 0, dimensions are no longer half-integers, and R18's statement "[g] is half-integer" is only true at the free point. **The dimension count was the leading-order face of the rule, not the rule.**

**The rule is a central element, and it survives every vector breaking.**
- **(I1)** z_t = exp(2πJ) lies over the identity of SO(4,2): it acts trivially on ℝ^{4,2} and on every tensor built from it (E1).
- So for **any** fixed vector v, **z_t ∈ Stab_{G̃}(v)**. In the cover, the stabilizer of a vector is the *full preimage* of Stab(v), and that contains the whole covering kernel ker(G̃ → SO(4,2)).
- The unbroken group is Poincaré for the mass, de Sitter for Λ, and their intersection with both. Taken as it acts on the Hilbert space (the cover, not only its identity component), **it contains z_t.**
- **(I2)** On states, z_t = (−1)^{N_{H²}} (each H² quantum has e^{2πi(5/2+k)} = −1; massless quanta have z_t = z_s). The Lorentz part z_s = (−1)^F is separately exact.
- So **w = z_t·z_s⁻¹ = the H²-number parity is an exact symmetry of any theory whose breaking is built from vectors, to all orders.**
- **Anomalous dimensions change nothing:** they shift Δ *within* each parity sector. The parity is an operator that commutes with the Hamiltonian, not a statement about dimensions. E2 illustrates it: random number-conserving quartics (the γ terms) plus every even monomial give [H, P] = 0 and zero leakage.
- **What breaks it:** only a breaking that transforms nontrivially under the covering kernel, a spurion of half-integer G̃-weight (E3: one odd monomial gives leakage 0.53).

**The analogy that makes it familiar:** this is exactly why (−1)^F survives every Lorentz-tensor background. A mass, an electric field, or a curved metric never breaks fermion parity, because the 2π rotation lies in the kernel of Spin → SO and acts trivially on every tensor. **H² parity is the same mechanism, one level up: the conformal group's covering kernel acting trivially on every vector of ℝ^{4,2}.**

**So it is not an "accidental symmetry" in Weinberg's sense.** An accidental symmetry (baryon number in the SM) is broken by higher-dimension operators that the exact symmetries allow. Here, **no operator odd in H² can be made covariant with vector spurions at any dimension or any order.** For Grace's pin: the textbook statement about accidental symmetries does not apply, because this is a symmetry protected by the breaking's own quantum numbers (spurion neutrality). The (−1)^F analogy is the right citation class.

## What changes

- **R18 is upgraded and its premises replaced.** P-a (analyticity) and P-b (UV dimensions) are no longer needed. The exact premise is:
  - **(P-d) Every symmetry breaking in BST is a tensor of SO(4,2), i.e. built from vectors.** The ruler and Λ are, by the rulings that define them (Cal Sections 1010 and 1011).
  - P-c (locality) is also no longer needed: the argument is about operators commuting, not about vertices.
- **K1936/K1937's "no stability consequence" does not stand**, under P-d. **H²-number mod 2 is exactly conserved.** The lightest H²-odd state cannot decay into H²-even states: massless quanta, or pairs.
- **Still NOT named** "matter parity" or "a dark ℤ₂". Which physical particles are H²-odd needs the K-type mode assignment (K1653), which is not in hand. This is a structural conservation law with no particle yet attached to it.
- **Calibrated both ways:**
  - It is exact only as far as P-d holds. A future BST structure that breaks with half-integer G̃-weight would break it; a condensate of an H²-odd field would be one.
  - **Keeper's calibration line:** *"(a) would be a genuine law, and the first place a wall turns into a conservation law."* **Under P-d, it is (a).**

**Kill line (mine) does not fire:** every breaking BST has named is a vector (the ruler, Λ). The descent is a frame, not a breaking. The commit via the ledger is Λ, a vector (R18 Lane D).

## For Elie's one-loop toy

The prediction, written before seeing it: in a model with two GFFs (Δ = 5/2 and Δ = 1) and an integer-dimension coupling, **one loop generates anomalous dimensions but no odd-H² operator**, because every diagram is built from H²-even vertices. An odd operator appears only if an odd vertex is put in by hand, and that vertex needs a half-integer-dimension coupling. The fermion-number control behaves the same way, by the same mechanism.

---
**For Cal (ruling R18 with Keeper's question):**
- (a), with the element named: z_t ∈ ker(G̃ → SO(4,2)) ⊂ Stab_{G̃}(v).
- Premise P-d replaces P-a and P-b.
- Does any BST structure break with half-integer G̃-weight? I find none.

**For Keeper:**
- The four-walls note's line 36 can now read: "no vertex odd in H², covariant or broken by the ruler or Λ (the covering kernel lies in every vector stabilizer; Lyra R19)".
- "No stability consequence" should be withdrawn under P-d, with no particle named.
