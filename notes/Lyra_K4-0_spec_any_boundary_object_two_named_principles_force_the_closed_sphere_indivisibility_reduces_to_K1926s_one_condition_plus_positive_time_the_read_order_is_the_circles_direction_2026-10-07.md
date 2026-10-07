# Lyra — Round K4-0 spec (with K4-1 Lane A items 1–7): what ANY boundary object must do; two named principles force the closed sphere; indivisibility reduces to K1926's one condition plus positive time; the read order is the circle's direction

**Lyra, Wednesday 2026-10-07, 14:34 EDT.** Rubric cell: Internal C. Binding: K1950 Sections 3, 4, 9, 10; K1949 Addenda 1–8.
**didwe:** "indivisible commitment boundary record" → 0; "projective plane six vertex triangulation" → 0; "baryon number determinant phase" → 0.
**Instrument:** scratch `k40.py` (reproduced in Section 9, five checks, all exact). No toy claimed; Elie's Lane B carries the domain-level checks.
**Tier of this note:** positions and conditions. Nothing here is a result about physics. Each item states what is forced, by what, and what kills it.

Casey's frame (Addendum 8), used for every item: **geometry → information principles (named, written before use) → boundary/continuum.**

---

## 1. The spec, before the object is named
Any object O that carries information across the two-sided Šilov boundary ∂_S D_IV⁵ = (S⁴ × S¹)/ℤ₂ must have:

| Slot | Requirement |
|---|---|
| **Inputs** | an interior amplitude v ∈ H²(D_IV⁵) (positive frequency on the one circle); an incoming photon (helicity ±1). |
| **Output** | a committed record ρ = vv† (bilinear, bosonic); its exterior field = the record's Poisson/Szegő extension. |
| **Reverse** | the reading direction: boundary data → interior by the reproducing (Szegő) kernel. The reverse must exist and must NOT undo the commit. Reading reconstructs ρ's content, not v's discarded phases. |
| **Erased at the crossing** | (e1) the overall phase of v; (e2) the relative phases that ρ = vv† forgets (the instruction content, Section 8); (e3) the real structure on V₁ if K1926's condition holds (which complex directions were position); (e4) the orientation sign of an odd reordering (it squares away in ρ). |
| **Conserved** | (c1) every U(1) charge carried by v: the ρ of a charge eigenstate commutes with the charge, so the label survives the square; (c2) the record count (Landauer: each commit paid at T_dS, the ledger picture); (c3) the deck class: which sheet of the cover the record was written on, as a ℤ₂ label. |

**What O must do that the kernel does NOT (KL4's floor):** discretize, commit irreversibly (e2 is lost for good), and carry the conserved labels (c1–c3) out to the exterior. A K4 projection that only reproduces kernel output fails the spec by definition.

---

## 2. Item 1: the information principles, written before use
- **(P-closed)** A committed record has no dangling dependence. Every edge borders exactly two faces, and the record is a closed triangulated 2-manifold (a cycle: ∂ = 0).
  - *Information reading:* an edge with one face is a constraint written on one side only, which is a pending commitment. That is the ledger picture's "open half" (09-22). Committed ⟺ closed.
- **(P-minimal)** A committed record uses the fewest vertices of any record satisfying (P-closed).

**What they force (exact; Heawood bound n ≥ ⌈(7 + √(49 − 24χ))/2⌉, attained except for the Klein bottle; attainment theorem pin-owed: Ringel–Youngs / Jungerman–Ringel):**

| Surface | χ | min vertices | 1-skeleton |
|---|---|---|---|
| S² | 2 | **4** | **K4** |
| RP² | 1 | 6 | K6 |
| T² | 0 | 7 | K7 |
| Klein bottle | 0 | 8 (Heawood says 7; Franklin exception, pin-owed) | not complete |

- **(P-closed) + (P-minimal), minimised over ALL closed surfaces, gives S² with 4 vertices, i.e. K4.**
  - Genus 0 is forced, not assumed. The sphere is the global minimum.
  - Coordinate-freeness (C1) comes out as a consequence: the minimal record's 1-skeleton is complete.
  - **Tier: D_IV⁵ + {P-closed, P-minimal}.** The geometry contributes nothing yet; this is purely the information layer (K1950 Section 9a's third bin).
- **What they leave free:** every non-minimal closed record. Casey's torus (assembly instructions) is closed but NOT minimal, so a torus record needs a **third principle, written now so it is not invented later:**
  - **(P-loop)** an instruction record must carry a non-contractible loop, so that a holonomy phase can live on it (H¹(S²) = 0, H¹(T²) = ℤ²; Addendum 6).
  - (P-closed) + (P-loop) + (P-minimal, among orientable records with H¹ ≠ 0) gives T² with 7 vertices, i.e. K7.
- **CAGED, new (my addition):** the boundary is NON-orientable (K1950 Section 4b). If a record may be non-orientable, the minimal record with a loop is **RP² on 6 vertices, 1-skeleton K6**, and 6 = C₂. Same cage as K7/g:
  - the 6 enters nothing without a map from the deck ℤ₂ to a non-orientable record;
  - (P-loop) is stated for ORIENTABLE records on purpose, and that choice is itself named as a posit;
  - RP²'s H¹(·; ℤ) is ℤ₂-torsion only, so it carries a sign, not a phase, and cannot hold a U(1) instruction. That is a reason for orientability, not proof of it.

**Kill line for item 1:** if the record surface is not a closed 2-manifold (for instance, if commitment writes a 1-complex or a 3-cell directly), (P-closed) is the wrong principle and K4 returns to "chosen."

---

## 3. Item 2: indivisibility (C7) as a condition, with its dependencies and kill line
**The condition.** A commit is allowed only on combinations of writes that are invariant under the record's symmetry group G_rec. If:
- (D1) writes transform as the 3 of a group whose centre ℤ₃ acts faithfully (SU(3); triality);
- (D2) **writes are one-way**: the writer has no 3̄. This is the positive-time ontology, with the commit direction = positive frequency on the circle (09-25 R3; project_bst_pure_positive_time_ontology);
- (D3) only G_rec-invariants commit (the ledger stores only what every frame agrees on);

then n writes commit only if n ≡ 0 mod 3. The smallest case n = 3 is unique: Λ³ℂ³ is one-dimensional (ε_abc). One or two writes carry triality ω or ω² and cannot commit. **C7 is then a selection rule.**

**The dependency I missed in the first pass, stated against my own antecedent.** My antecedent: *"Suppose each write is a vector v in V₁ = ℂ³, transforming as the 3 of the record's SU(3)."* Correction:
- K1926 puts the ACT at the real level (SO(3), real structure present). The 3 of SO(3) is real (3 ≅ 3̄) and its centre is trivial.
- At that level two writes already make an invariant (δ_ab v^a w^b), so **indivisibility is NOT forced at the act level.**
- It is forced only if the commit is taken at the level where the real structure has been forgotten. That is exactly K1926's open condition.

**So C7 and colour SU(3) hang on the SAME unforced condition:** *a commit forgets V₁'s real structure.* That condition plus (D2) plus (D3) gives both. That is economical: one can-fail line instead of two. But it means C7 is **not yet forced**, and K4-3 still cannot be credited for the factor three through it (K1950 Section 3 stands).

**Consistency check (retrodiction, not evidence):** (D2) says no committed (permanent) record contains a 3̄. Mesons (3 ⊗ 3̄) are singlets, so (D2) must treat them as acts, not records. Every meson is unstable; the only stable hadron is a baryon. The SM explains proton stability by baryon-number conservation, so this is consistency only (Cal's genericity).

**Kill lines (can-fail count 3, of which 2 are live today):**
- K-C7a: a reason the commit forgets the real structure is not found → C7 stays Casey's posit (live);
- K-C7b: a stable record with net zero triality from 3 ⊗ 3̄ is exhibited → (D2) dies (checked against stable hadrons: none, so not live);
- K-C7c: Cal's Section 990 counterexample class (spin-1 polarization records) is shown to apply to (D2) as well as to "one-way ⇒ PU(3)" → the positive-time route to (D2) dies (live; Cal to rule).

---

## 4. Item 3: which S₃ embedding. **Bare, in U(3).** What puts the token level outside SU(3) is the det phase, and the det phase is the one circle.
Antecedent (Keeper K1950 Section 9c): *"signed permutations … preserve ε_abc for ALL six, so no orientation is selected; bare permutations (in U(3), not SU(3)) preserve ε only for A₃."* **Agreed. My first pass used both embeddings.** Recomputed (Section 9): bare det = sgn(σ); signed det = +1 for all six.

**The choice and its reason:**
- U(3) = (SU(3) × U(1))/ℤ₃. The ℤ₃ quotient **identifies SU(3)'s triality centre with the cube roots of the U(1) phase.** On Λ³ℂ³ the U(1) acts by e^{3iφ}, so a phase of π/3 per write emulates an odd permutation (checked).
- A write carries the circle's positive-frequency phase (input slot, Section 1). So the write group is U(3), not SU(3), and **the token level sits in U(3) because each write carries one unit of the circle's charge.**
- In standard physics the det U(1) on Λ³ of quark triplets is baryon number, with B(ε_abc qqq) = 1. Position: **the read orientation, the det phase and baryon number are one object.** The record is orientation-sensitive iff it carries the det charge; a baryon record carries it, a meson record does not.

**The real gain, for Cal (KL3).** The read order, taken as the circle's direction, **descends to the physical boundary.** The deck map (x, θ) ↦ (−x, θ + π) has degree −1 on S⁴ (that is what makes the quotient non-orientable) but is a rotation on S¹. The circle's direction is preserved, and θ ↦ 2θ is a well-defined map to a circle with a global direction. So:
- the **total** orientation of the boundary does not exist globally (K1950 Section 4b/c, correct);
- the **circle's direction** does exist globally. Casey's "the read order always views the dimension in the same order" holds on the physical boundary itself, not only on the cover, **if the read order is the circle's direction and not S⁴'s orientation**;
- this **disagrees with K1950 Section 4c's "the read order flips around every orientation-reversing loop."** That holds for an S⁴-orientation read order, not for a circle-direction one. Cal rules which object the read order is;
- antimatter: C reverses J (positive ↔ negative frequency), which reverses the circle's direction and therefore the read order. KL3(c)'s demand is met by C directly, **without** needing the deck map to be C. Position, map owed (J ↦ −J as C on the det charge is standard; J as the circle's generator is 09-25 R3).

**Kill line:** if the read order must be S⁴'s orientation (for instance, because the three values live on S⁴ directions), the circle route is wrong and K1950 Section 4c's flip stands.

---

## 5. Item 4: which level commits
**The selection rule acts on amplitudes; the store keeps ρ.**
- Orientation (the det SIGN) is visible only on v and squares away in ρ (e4). So the A₃ selection is enforced **at write time**, as part of the act.
- The det CHARGE survives in ρ as a superselection label (c1). So **the record cannot tell an even from an odd reordering, but it knows it carries baryon number.**
- This coheres with KL3(b): right-handed records exist and are read; what is handed is the coupling (the act), not the stored record. The grammar lives in the act. Records are grammatically neutral and carry the charge.

---

## 6. Item 5: where the electron's 2-surface lives
**Not in 3-space.** A Dirac-type charged surface is about 10⁷ times larger than the measured bound on the electron's size (Grace; pin in hand). The spec therefore requires the record surface to live in the **internal geometry**, not in spacetime: the electron's exterior size is the size of its field and coupling, which is a different object.

**Candidate, conditional on Elie's Lane B1:** a closed S² in the compact dual of the rank-two sub-geometry, Q² ≅ S² × S² (pin-owed: Helgason or Faraut–Korányi, Grace). If it holds:
- (P-closed) is met geometrically (a round, closed S²);
- the torus side sits on the sub-geometry's Šilov boundary T²;
- **but it is generic to every D_IV^n with n ≥ 2 (allowed, not forced by 5)**, unless Elie's null finds otherwise.

**Kill line:** if D_IV² ⊂ D_IV⁵ does not place a closed S² where a record can sit (Elie B1 fails), the surface has no named home, and step 2 of Casey's chain stays a picture.

---

## 7. Item 6: T958. **Reading (A).**
**The electron is the circle and WRITES onto a 2-surface it does not have.**
- **Coherent with item 3:** the writer carries the circle's phase (the det U(1) per write); the record is the closed sphere (item 1).
- **Coherent with Dirac:** Dirac's sphere is the RECORD's shape, not the electron's body. That also removes Grace's 10⁷ problem from the electron itself.
- **Coherent with Casey:** "the bones the electron deposits absorbed information into."
- **Coherent with Addendum 7:** the loop (S¹) is in the neutron and none in the proton (T958, both April and today); the electron brings the loop.
- **Caveat:** T958 is an April "PROVED — structural" label with no audit (Addendum 7). Picture adopted; nothing cited as proved.

**Kill line:** if the electron must itself carry two dimensions of the record (for instance, if its spin-½ must be the S² of item 6 rather than the writer's phase), (A) fails, and (B) "T958's electron assignment is wrong" becomes the reading.

**Open for Casey (one question):** in (A), the writer is one-dimensional and the record two-dimensional. Is "1D information encoded on 2D surfaces" (Addendum 8) exactly this, with the electron's circle as the 1D information and the record sphere as the 2D surface?

---

## 8. Item 7: the wave-function definition (Lane E)
**ψ = v ∈ H²(D_IV⁵)**, with two contents:
- **record content** ρ = vv†: what commitment writes. The Born square is the record's bilinearity (T1239's picture; tier unaudited, re-tier before citing);
- **instruction content**: the relative phases ρ forgets (e2), plus, for a record with H¹ ≠ 0 (torus, under P-loop), the holonomies around its two loops.

**Interference** is instructions combining before the write.

**Commitments the definition makes, so referees can hit them:**
- **ψ-ontic.** v is the physical state of the process, not knowledge of a hidden discrete state. PBR excludes ψ-epistemic models under preparation independence (pin-owed, Grace). This definition does not need the exclusion: the instructions are real.
- **Nonlocal by construction.** D_IV⁵ is one shared ledger, so Bell's theorem is met by nonlocality, not superdeterminism (pin-owed).
- **Uncertainty is a property of v, not of the instrument.** K1926's symplectic form ω on V₁ makes position and momentum conjugate halves of one phase space. Preparation uncertainty is then the Fourier relation within v. "Resolution limit" (09-15) must be shown to reproduce exactly that, which is Elie's discriminator toy (Lane B3).
- **Prior art to read before any novelty claim (Grace):** Bohm–Hiley "active information" (nearest to "assembly instructions"); 't Hooft's cellular automaton; Spekkens' toy model (which is ψ-epistemic, and so is the contrast case).

---

## 9. Which of Casey's six steps the spec forces, and which it allows
| Step | Status |
|---|---|
| 1. A photon carries information | **allowed** (standard; input slot) |
| 2. A 2D charged electron captures it | **rewritten under (A):** the electron is the 1D writer; the 2D surface is the record's, in the internal geometry (Section 6) |
| 3. K4 words (3 values + frame) | **K4 forced by D_IV⁵ + {P-closed, P-minimal}**; the frame vertex is allowed (KL2 open; Grace's loop sign is the candidate) |
| 4. Three words indivisible | **reduced** to K1926's one condition + positive time (D2) + invariance (D3); not forced |
| 5. D_IV⁵ = the shared ledger | **allowed**, and **required** by the ψ-ontic definition (Bell) |
| 6. Nucleons archive; torus records | **allowed**; the torus needs (P-loop), stated now; K7/g and K6/C₂ caged |

**Count:** 1 forced by named principles (3); 1 reduced to an existing open condition (4); 4 allowed or rewritten.

**Instrument (scratch `k40.py`, exact):**
- (i) Heawood minima: S²: 4, RP²: 6, T²: 7, each with a complete 1-skeleton (E = 3(n − χ) = n(n−1)/2);
- (ii) bare det = sgn(σ) over all six permutations; signed det = +1 (Keeper's control reproduced);
- (iii) a phase of π/3 per write equals −1 on Λ³;
- (iv) the deck map has degree −1 on S⁴ and +1 on S¹.

## 10. For Cal (rule each)
1. (P-closed) and (P-minimal) as inputs: admissible information principles, or smuggled K4?
2. C7 reduced to K1926's condition: is the reduction exact, and does Section 990 reach (D2)?
3. Bare embedding plus det = circle charge = baryon number: position or overreach?
4. **The read order as the circle's direction descends globally; this contradicts K1950 Section 4c.** Rule which object the read order is.
5. Amplitude-level selection, record-level charge.
6. The surface in Q²'s S², pending Elie B1.
7. T958 reading (A).
8. ψ-ontic plus nonlocal ledger.
9. **The new cage:** RP² = K6, 6 = C₂.
