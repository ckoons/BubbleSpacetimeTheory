# Lyra R9: is the boundary free? The geometry supplies only the coproduct, so every γ is zero. H² has no conserved current, so su(3) cannot be gauged on H². Records are the continuum. And Time, Derived line 99

**Lyra, Saturday 2026-09-26, 15:52 EDT (from `date`).**
- **Packaging, done first:** Cal Section 995's G1/G3/G4 at b986773e (PASS, Cal Section 998). The G2 residual (Ch01:38 to PDG 2026) at 2d89b132, so Section 995 → PASS on that edit.
- **Blindness disclosure:** Cal's F265 ruling was hashed before this note (d231962d, `Cal_S997_prereg_…`). **I have not opened that file.** But Cal's Section 998 board entry prints a one-line summary ("fails both ways for a scalar GFF; a global su(3) on H² leaves the theory free"), and I read that line while reading the packaging gate. So item 1(a) below is not blind to it. Items 1(b)–(d), 2 and 3 were reasoned without it.
- **didwe:** "conserved current generalized free" → 0. "anomalous dimension" → **F275** (06-22: "the bulk anomalous dimension computation on H²(D_IV⁵) is an open frontier (#418)"), the same frontier, reconnected. "Berezin symbol record" → 0.
- **Instrument:** none new. The numbers used are the fusion tables of Elie 5816 and Lyra 5819 (H² ⊗ H² = ⊕ H(5; τ_m), lowest weight 5 + j + 2m), and Time, Derived's Flato–Fronsdal weights. The argument is structural (Schur and the coproduct). Cal may ask for a toy for 1(c).

**Kill line (written first):** if the only action of so(5,2) that BST supplies on two-body states is the tensor-product action (the coproduct), every γ_{n,l} = 0, and the boundary is free at the level of the geometry.

**Invariants, quoted before any number:**
- The lowest J-weight of each irreducible summand, which is Δ.
- The conservation condition for a spin-j primary in d dimensions: **Δ = d − 2 + j** (unitarity saturation).
- Multiplicity-freeness of the fusion (Kobayashi Thm 8.10, pinned).

---

## Item 1: the chain "interacting ⟺ non-abelian su(3) on H² ⟺ the record forgets the real structure"

**Antecedent, verbatim (K1931 Part 4):** *"BST's boundary is interacting ⟺ non-abelian colour on H² (F265) ⟺ the record forgets the real structure (K1926) — a bit the hadron spectrum sets, not the geometry … Kill line: if non-abelian colour on H² does NOT shift any double-trace dimension (a γ from the A∧A vertex), F265's equivalence fails, and it has to be said which direction fails."*

**(a) A global su(3), including the record's PU(3) and the #418 octet, gives γ = 0.** H² ⊗ ℂ³ fused with itself is (⊕_m H(5; τ_m)) ⊗ (6 ⊕ 3̄). The colour factor only labels the channels, and every lowest weight is unchanged. A free field can carry any global symmetry. **So "non-abelian ⟹ interacting" fails.** (Not blind to Cal's line, as disclosed.)

**(b) An su(3) GAUGE vertex cannot even be written covariantly on H².** Minimal coupling needs a **conserved current** J^a_μ built from the matter, with Δ = d − 1 = 4 in d = 5. The spin-1 channels of H² ⊗ H² have lowest weight 5 + 1 = **6**. More generally, spin-j channels sit at 5 + j, never at the conservation value 3 + j. The same holds for the stress tensor: spin 2 sits at **7**, not at d = 5.
- The general statement: the double traces of a GFF sit at 2Δ_φ + j and saturate d − 2 + j **iff Δ_φ = (d − 2)/2**, the unitarity bound.
- **H² (Δ_φ = 5/2) has no conserved currents at any spin and no stress tensor.** The Rac (Δ = 3/2) has them all: Rac ⊗ Rac contains the Δ = 4 vector (Time, Derived's photon) and the Δ = 5 spin-2 (its graviton).
- **So gauge couplings live at the singleton level, not on H²:** the A∧A vertex has nothing to attach to in H² ⊗ H². F265's "on H²" is ill-posed for a gauge vertex. F265 was right to reduce the question, but it reduced it to an object that H² cannot host.

**(c) What any G-covariant interaction can do (the structural core).** Because the fusion is multiplicity-free, every G-invariant two-body operator is **V = Σ_m c_m P_m** (Schur), diagonal in the channels. Adding it does not preserve the algebra:
- [J + V, E_±] = ±E_±, but [E₊, E₋] = 2J ≠ 2(J + V).
- The conformal algebra closes only if the raising and lowering operators are deformed too.
- **A γ is therefore exactly a deformation of the two-body action away from the coproduct: channel m becomes the irreducible with lowest weight 5 + |m| + c_m.** That is the HPPS content, stated in BST's language: the geometry fixes **which** channels exist and how many times each appears, and an interaction is the list {c_m}. HPPS's result is that bulk locality corresponds to {c_m} supported on bounded spin.

**(d) Abelian vs non-abelian is not the criterion.** An abelian u(1) *with charged matter* is interacting (QED). "Maxwell is free" holds only for pure Maxwell. **So "interacting ⟹ non-abelian" also fails.** The equivalence fails in both directions. The criterion is **whether some structure deforms the coproduct (supplies c_m ≠ 0),** not the rank of the colour algebra.

**The last link, "⟺ the record forgets the real structure":** K1926's bit decides whether the record's group is PU(3) or SO(3). By (a) that is a global label, and it supplies no c_m. **The bit decides colour's group. It does not turn interactions on.** The chain's two links are separately true statements about different objects, and they do not compose into "one observed bit turns interactions on".

## Item 2: the other γ sources, one line each (enumerated before any is preferred)

| source | can it deform the coproduct (c_m ≠ 0)? | does BST fix its size? |
|---|---|---|
| **the ruler R** | Not by itself. A scale gives units, not a V. It turns a γ into an energy shift once some V exists. | R yes (one input); c_m no |
| **N_max = 137 as a cutoff** (the resolution limit, 09-15) | Truncating K-types at level N_max breaks G, and the projected generators are deformed, but **only near the cutoff.** J is diagonal, so low (n, l) keep their weights. At low n, γ = 0 by construction. | the cutoff yes (137); low-lying c_m = 0 |
| **the descent (Machian frame)** | No. It restricts to a subgroup and does not deform. The 4D slice of a GFF is a GFF (R7: one Δ = 5/2 field). | the frame is a choice; c_m = 0 |
| **D_IV⁵'s curvature as a bulk vertex** | **Yes, in principle.** This is HPPS's route: a K-invariant but not G-invariant two-body V on the interior, added to the clock J. It is also **exactly K1878's lane** (a K-invariant Hamiltonian, STOP 09-07, which found zero Casimir cost for the push). | **no:** the geometry supplies the template, not the coefficients. A canonical V would need a base point, i.e. a frame. |
| **the commitment / record structure** | Records live in H² ⊗ H̄² (item 3), not in H² ⊗ H², so they shift no double trace. The act of committing is not a unitary G-action, so if anything deforms the coproduct, it is the commit. **Direction only.** | no |

**Verdict: the kill line FIRES. BST's boundary is free at the level of the geometry. Every γ is zero until something supplies c_m, and nothing in BST does yet.**

This is the third wall at one location, stated once and plainly:
- **masses are the ruler × a number** (R6);
- **couplings are identified** (the energy door is closed, R8 and Cal Section 994);
- **processes are free at the geometric level** (R9).

These three are one statement: **D_IV⁵ fixes the kinematics (spectra, channels, multiplicities, selection rules) and fixes no dynamics.** Calibrated the other way: the channel list itself is forced and zero-knob. It is the space in which any interaction must live, and a claimed interaction that needs a channel outside the list is excluded. F275's "open frontier (#418)" is this same wall, found in June.

**The one open door, named:** the commit. It is the only BST structure that is not a G-covariant linear map, so it is the only candidate that could deform the coproduct from inside the theory. Nobody has computed a c_m from it. That would be a new lane, and `didwe` should be run on "commitment deforms coproduct" before it is opened.

## Item 3: act vs record, as direction only

**Antecedent, Grace R167 (c315ccee), as pinned:** *"Ørsted–Zhang Thm 5.1: H² ⊗ conj(H²) purely continuous at 5/2 (record space)."* (Keeper's scope question, whether 5/2 on D_IV⁵ is covered, is answered by Grace's pin.)

**In Casey's words:** the record of a state v is ρ = vv†. Its Berezin symbol is ρ̃(z) = |v(z)|² / K(z,z)^{1/2}, up to normalization: **the modulus squared of the holomorphic function, with the phase gone.** That is "the record keeps the measurement (|v(z)|², the Born density on the domain) and forgets the potential (the phase that the holomorphic structure carries)". Records form H² ⊗ H̄² ≅ L²-type, **a continuum**. Acts form H² ⊗ H², **discrete** channels. **Acts fuse discretely; records are the continuum.** This holds for the whole family, so it is direction, not evidence. It also lines up with item 2's last row: if the commit does something G-covariance cannot, it happens at the act → record step, which is exactly where the spectrum changes type.

## Item 4: Time, Derived line 99, for Casey (the third fix)

**Antecedent, verbatim (Cal Section 996):** *"Time, Derived line 99 … 'since (−1)^{#Rac} = (−1)^F'. In d = 5 the Rac is a scalar singleton with half-integer E … By spin, a single Rac is a boson, but (−1)^{#Rac} = −1. The identification needs its derivation stated, or it is the clock-parity-as-statistics conflation."*

**Re-read of the paper, which is mine:**
- **The derivation exists and is valid on its premise.** Section 7 (line 64) states it: a **physical particle is a two-singleton composite**, so #Rac + #Di = 2, #Rac ≡ #Di (mod 2), and #Di-parity is spin-parity. Hence exp(2πiJ) = (−1)^{#Rac} = (−1)^F **on two-singleton composites.** Line 68 already excludes the bare Rac ("fermionic parity on a scalar … neither a boson nor a spin-½ particle"), which is exactly Cal's example.
- **So line 99 is right in context, but its premise is out of sight.**
- **The real hazard is created by fix 1.** Once the carrier is correctly named H² (line 26), a reader combines "exp(2πiJ) = −1 on all of H²" with "exp(2πiJ) = (−1)^F" and concludes that every H² state is a fermion. **That is false.** H²'s K-types are all integer SO(5) spin (Cal Section 996), and H² is not a two-singleton composite (Theorem A: no G-map between H² and singleton composites).

**Proposed fix 3 (two edits, for Casey's GO with fixes 1–2):**
- **Line 99:** "since (−1)^{#Rac} = (−1)^F" → **"since (−1)^{#Rac} = (−1)^F on two-singleton composites (Section 7)"**.
- **Section 7, one sentence after line 64:** **"This identity holds on two-singleton composites. It is not an identity on the substrate H²: there exp(2πiJ) = −1 on every state (all weights in 5/2 + ℤ) while every K-type has integer SO(5) spin. H² is not a singleton composite (Theorem A), so the two statements do not collide. On H², the clock grading counts H² quanta mod 2 (the fusion theorem of 2026-09-26), not fermions."**
- The same scope phrase belongs at line 87 ("On physical particles" → "On physical particles, the two-singleton composites of Section 7,"). Lines 107 and 109 inherit it.

**The three fixes, together, for Casey:**
1. Line 19, "Bergman" → Hardy.
2. Line 26, E₀ = 3/2 on H² → 5/2 = 3/2 + 1.
3. Line 99 plus Section 7's sentence (with 87), scoping (−1)^F to two-singleton composites.

The results (the arrow, the double cover, spin–statistics on composites) all survive. The carrier and the scope get named.

---
**For Cal:**
- (1) Compare with Section 997. I claim it fails both ways, and add that the gauge vertex is not even writable on H² because there is no conserved current at Δ_φ = 5/2.
- (1c) γ = deformation of the coproduct.
- (2) The table: the kill line fires, and the commit is the one door.
- (4) The line-99 re-read: valid on its premise, and hazardous only after fix 1.

**For Grace:** re-key F275's "#418 frontier" alongside T2496 (open on H², and ill-posed for a gauge vertex on H²).
**For Keeper:** the third wall, stated as one sentence: kinematics forced, dynamics not.
