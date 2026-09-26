# Lyra R5 (round 5): the real structure is time reversal; J is central, so the SO(4) lead dies; H² is built from hydrogen shells but contains no hydrogen; Ω_Λ carries a colourless 19

**Lyra, Saturday 2026-09-26, 10:45 EDT (from `date`).** Inputs: K1926 Sections 1–4 and Addenda 1–5, the round-5 prompt, Casey's 19:42 scope ruling, Cal Section 988, T2138, T1966, T192, T193, T305, and F242.
**Instrument:** `play/toy_5800_lyra_round5_time_reversal_is_the_real_structure_J_central_in_K_hydrogen_shells_in_H2.py`, sha256 `42bf640d106c41e2…`. The hash was taken before the run, and the predictions P1–P7 are in the docstring. **SCORE 6/7.** The miss is mine and it is disclosed: I predicted F242's element would commute with 3/6 su(2)± generators, and it commutes with 4/6. It is itself one of the su(2)₊ generators, and I forgot that it commutes with itself. The substance of P3 holds. Output: `play/.out_toy_5800.txt`.
**didwe:** "real form Silov" 0; "time reversal antiunitary" 0; "Szego Silov" 0; "19 hexagonal" 0; "SO(4,2) hydrogen" → K1878 STOP (energies; this note reads structure only, per Casey 19:42); "self-dual complex structure" → **F242** (06-20, VERIFY_FAIL). Item 2 retires part of F242.

---

## 1. Why would a commit forget the real structure? The real structure is time reversal.

**Kill line (written first):** if the record must support a comparison of a state with its own time-reverse (T acting on records), the record keeps tr(ρρᵀ), and colour on records is SO(3), not SU(3).

**Direction:** the real structure on V₁ is not a new object. It is the V₁ piece of the one antilinear map that reverses the arrow.
- The standard conjugation σ(v) = v̄ on V = ℂ⁵ is an antilinear triple automorphism. It sends the time-line tripotent e = (x₀ + iy₀)/2 to ē, which reverses the arrow (Cal Section 988: down vs up = e vs ē = J's orientation). It preserves V₁ = ℂ³, and on V₁ it is exactly the real structure K1926 R2 uses (toy P1).
- **tr(ρρᵀ) = |⟨σv, v⟩|²:** the one q-trace a record keeps is the overlap of a state with its image under σ (P1, numerically exact).
- **In Casey's phase-space picture (Addendum 3)** this is standard: complex conjugation in the position representation is Wigner's time reversal T (x ↦ x, p ↦ −p). The unitaries commuting with it are the real ones, O(3) (toy P2: commutant dimension 3 of 9).

**So K1926's condition reads: the record's symmetry is SU(3) iff time reversal is not an operation on records.** Records have SU(3) symmetry iff the record cannot be compared with its arrow-reversed image. The act has a direction, and so does the record.

**Reconnect:** this is the corpus's positive-time ontology ("CPT-mirror impossible; arrow dynamical, not geometric") applied to records. It is also Cal Section 988's finding that conjugation swaps e ↔ ē. Nothing new is posited. The σ that would carry the real structure is the arrow reversal, and the arrow is not reversible.

**Tier: IDENTIFIED (mechanism candidate), not derived.** The step "a one-way commit ⇒ T is not a record operation ⇒ tr(ρρ̄) is not recorded" is a physical reading. The algebra (σ = the arrow reversal; tr(ρρᵀ) = its overlap; commutant = O(3)) is exact.
**Can fail:** (a) any recorded T-odd/T-even comparison in the colour sector. QCD's T-invariance (θ ≈ 0) is a statement about dynamics, not about records, so that needs care; Cal should rule whether strong-CP bears on this. (b) Coleman–Mandula, Section 6.

## 2. Handedness: the SO(4) lead dies because J is central in K. F242 is retired in part.

**Kill line (written first):** if the geometry's J commutes with both SU(2) factors of every SO(4) the geometry supplies, J picks no hand there.

**Result (toy P3, exact):** K = SO(5) × SO(2), and J = 1 ⊗ j on p = ℝ⁵ ⊗ ℝ² is the SO(2) factor. It **commutes with every element of so(5) ⊗ 1**, so in particular with SO(4) = the stabilizer of a real unit vector, and with **both** su(2) factors: max |[J, so(4)]| = 0.0. **The lead as stated dies.**

**F242's error, named:** F242 (06-20) identified "the shared SO(2) = the conformal Hamiltonian = J" (correct) and then computed with J = J₁₂ + J₃₄ ∈ so(4) (a different object: an element of SO(5)'s algebra). K's centre is not in so(4). The reduction SO(4) → U(2) in F242 is correct linear algebra about J₁₂ + J₃₄, but that element is not the geometry's J. **Retire F242's rows 3–5 ("J reduces SO(4) → U(2)", "weak = J-selected su(2)", "why-left = self-duality class of J").** Keep rows 1–2: the embedding, and the fact that J's sign is energy, not chirality. The retirement needs Keeper's dated head on F242.

**What survives (toy P4):** the only ℝ⁴ on which J acts as a complex structure *and* the geometry distinguishes it is ℝ⁴ = (e-plane) ⊗ ℝ². There, J is self-dual and the e-plane rotation is anti-self-dual. But K realizes only the Cartan u(1) × u(1) there; neither SU(2) is in K. Both orientations involved (e vs ē, and J's sign) are the arrow, so this ℝ⁴'s orientation is arrow × arrow, which is fixed and gives no parity content.

**The wall, stated sharply (open):** in Lorentzian signature a hand is an identification of QM's i with ±⋆, the Hodge star on Λ²ℝ^{3,1} (⋆² = −1 there, so ⋆ is a complex structure on bivectors; (½,0) vs (0,½) is which sign i takes). **BST picks a hand iff the descent identifies J with ⋆ (or −⋆) on the bivectors of its ℝ^{3,1}.** That needs the descent's frame (T2565: the frame needs a matter/observer input), so the hand is at most as forced as the frame. `didwe` has no hit on this form. It is the next place to look.

## 3. One circle: 16 is not a count on one S¹, and one circle predicts Δ ≠ 0

**Kill line (written first):** if the energy of a winding state is its clock charge (the SO(2) weight), complete and incomplete windings differ in energy, so Δ ≠ 0 and 16/3 would depend on temperature.

- **16 on one circle:** one S¹ with its Pin(2) double cover supplies one ℤ₂ sheet label (rank¹ = 2). rank⁴ = 16 needs four independent sheet labels. One circle cannot count to 16. **Wall:** 16 is counted somewhere other than the circle, and T1966/T2138 do not say where. One candidate exists, dimension-matched only: the half-spin module of Cl(p), p = ℝ¹⁰, is 16-dimensional. It is named here with menu risk and not claimed.
- **Δ on one circle:** H²'s SO(2) weights are exactly the clock charges (5/2 + ℤ≥0). If complete and incomplete windings live on the same circle and energy is the clock charge, a fractional winding carries less charge, so Δ > 0. **One circle therefore predicts the opposite of Δ = 0.** Δ = 0 needs the energy to be per mode rather than per unit of winding charge. That is the question Cal Section 988's "u(1) collides with the clock" already raised. This reading of one circle does not rescue 16/3's temperature independence.
- **Dark mode, reworded per Casey (K1925 addendum 2):** "the dark sector is energy held in windings that did not close. Such a winding writes no value into matter, so it couples only through gravity. 16/3 is the ratio of that energy to the baryons' energy, per baryon. No particle claim is made either way; m_p/3 is the energy per unclosed unit only if Δ = 0."

## 4. Atomic shells (Casey 19:42 scope: structure only, never the energies). H² is built from hydrogen shells, and hydrogen's representation is not in it.

**Kill line (written first):** if the SO(2)-weights of H²(D_IV⁵) and of the SO(4,2) ladder representation do not overlap, then Hom(ladder, H²|SO(4,2)) = 0.

**(a) Every SO(4)-type in H² is a hydrogen shell (toy P5, exact for j < 40).** Take SO(4) = the stabilizer of a real vector in SO(5). This is Fock's SO(4), and the corpus's SO(5,2) ⊃ SO(4,2) ⊃ SO(4). Degree-j harmonics on ℂ⁵ (the SO(5)-type (j,0)) restrict to SO(4) as ⊕_{i=0..j} (i/2, i/2), with dimensions (i+1)² = n²:
**dim (j,0)_{SO(5)} = Σ_{n=1}^{j+1} n²** (for example, 30 = 1 + 4 + 9 + 16).
**No SO(4)-type (a,b) with a ≠ b ever occurs.** Seen by SO(4), the polynomial content of BST's Hilbert space consists entirely of hydrogen's shells: n² states for each n, with no other SO(4)-types. This is Casey's "recapitulating", made exact.

**(b) Hydrogen's representation itself does not appear (toy P6).** The hydrogen bound spectrum is the SO(4,2) ladder representation: the minimal Wallach point ν = 1 of D_IV⁴, each shell once, with **the principal quantum number n equal to the weight of the compact SO(2) generator** (Barut–Kleinert's Γ₀; Grace pins). That SO(2) is K's centre, **BST's clock**, and it is shared by SO(4,2) ⊂ SO(5,2). H² lives at clock weights 5/2 + ℤ≥0. The ladder lives at 1 + ℤ≥0. The two sets are **disjoint: multiplicity 0.** There are two independent obstructions:
- **floor:** 5/2 > 1;
- **lattice:** half-integer vs integer, which is n_C odd (Cal Section 954's cover).
The restriction H²|SO(4,2) = ⊕_{k≥0} H_{5/2+k}(D_IV⁴) (holomorphic-type pair, normal Taylor expansion). Grace should pin this to Kobayashi's multiplicity-free branching or Jakobsen–Vergne. Each summand carries every shell (j/2, j/2), but with the tower q^m (weights 5/2 + k + j + 2m), not once.
**Verdict among Casey's three words:** "recapitulating" (shell structure identical), not "containing" (hydrogen's rep is absent). "Isomorphic" is ruled out by the clock offset. **Structure-only lemma: in both, the principal quantum number is the clock reading, and BST's clock starts at 5/2 where hydrogen's starts at 1.** Spin: 2n² = n² ⊗ ℂ²; the geometry supplies the n², and the ℂ² is the spin wall (unchanged).

## 5. Which route does each 19 use? One of them is colourless.

`didwe "19 hexagonal"` → 0. The catalogue (`data/bst_constants.json`) has **five** 19-formulas, not three. Keeper's first look searched for a bare 19 and missed T192 and T193, whose code reads `13.0/19.0`.

| quantity | formula | 19 as | coloured quantity? |
|---|---|---|---|
| Ω_Λ (T192) | 13/19 | N_c² + 2n_C | **no: the vacuum** |
| Ω_m (T193) | 6/19 | N_c² + 2n_C | mixed (DM + baryons) |
| Ω_b (T198c) | 18/361 = (6/19)(3/19) | N_c² + 2n_C, and 16 + 3 in 3/19 | yes (baryons) |
| \|V_ud\|² (T305) | 19/20 = 1 − 1/(4n_C) | 4n_C − 1 | quarks, but the weak current is colour-blind |
| m_d (T2032) | 13·19/28 m_e | N_c³ − rank³ | yes |

**Routes actually used:** none of the five uses the hex-shell route. N_c² + 2n_C (cosmology), 16 + 3 (3/19 only), 4n_C − 1 (CKM) and 27 − 8 (m_d) are four different expressions. Only one of them, 3/19 = N_c/(rank⁴ + N_c), has a structural reason: it is a count ratio.
**Casey's pre-registered prediction ("19 only in coloured quantities") meets Ω_Λ = 13/19.** Cal must rule on the word. If "coloured quantity" means a quantity involving coloured matter, Ω_Λ **falsifies** the prediction. If it means "the formula contains N_c", the test is **empty**, since almost every formula does. Either way the prediction does not survive as stated. What survives is narrower: **the 16 + 3 route appears only in 3/19, a baryon count.**

## 6. The Heisenberg hypothesis (Addendum 3), with its Coleman–Mandula line

**Hypothesis H-col:** V₁ = ℂ³ is the phase space of three dimensions (h = g + iω). The act writes in a Lagrangian half (position; real structure present; SO(3)). The record keeps ω and forgets which half was position; by Section 1, it forgets T. Colour's SU(3) is then the symmetry of the record's phase space, U(3) ∩ Sp(6, ℝ) with the centre removed.
**Coleman–Mandula line:** an internal symmetry must commute with the live Poincaré group. H-col passes only if the record's phase space is not the live (spacetime) phase space. On the act/record split, it is not: the act's position half is spacetime's, and the record's SU(3) moves between halves of a *recorded* ℂ³. **Kill:** if any record-level SU(3) generator acts on live momenta, H-col is dead by the theorem.
**Reconnect:** `Lyra_Heisenberg_Conjugacy_Justification_for_dH_dm.md` (06-01) used Heisenberg conjugacy through K-type Casimirs (mass ↔ momentum). H-col is the same ω seen one level down, on V₁ instead of on the K-types. The 09-15 resolution-limit marker (`Lyra_R152_IDEA_Section_D_…2026-09-15.md`) says the record space is bounded and scale-fixed. H-col adds that the bounded record keeps ω and not the split, so the record's uncertainty is structural (no preferred half), not accumulated. That is the marker's "non-accumulating" clause with a mechanism. **Tier: hypothesis (C). The geometry gives the structure; ħ is not derived.**

## 7. Pauli, relocated to records

**Kill line (written first):** if a record of several written directions is an ordered list, or a multiset, and not a subspace, exclusion does not follow.
- **Statement:** if a record of k written directions is the oriented subspace they span (its Plücker image v₁∧…∧v_k), then a direction cannot be recorded twice (v∧v = 0, toy P7) and the record is antisymmetric. A *complete* record of all three directions is Λ³ℂ³ = ε, which is one-dimensional. That is exactly the colour singlet ε_{abc} of a baryon. **SU(3), not U(3), is the group preserving h and ε** (P7: the centre's phase moves ε). So "special" in SU(3) means "a complete record keeps its orientation", and the ℤ₃ centre acts trivially on it, which is baryon number mod 3 (K1700b).
  - **~~Clause citing K1700b~~ STRUCK (Keeper 2026-09-26 on Cal Section 990 (7)):** K1700b retracts "the centre is B mod 3". Triality t = 3B mod 3 ≡ 0 on every colour singlet; the centre acts trivially on ε because ε is a singlet (t = 0). The rest of the item stands at IDENTIFIED.
- **Walls:** (i) *why* a record is a subspace rather than a list is a reading of "record", not derived. (ii) This is exclusion for records; Pauli for particles needs the row Cal Section 954 flagged as missing ("no row relates record space to particle space"). (iii) Spin-½ is unchanged. **Tier: IDENTIFIED.**

## 8. Exotics: the two kill lines (Casey, K1925 addenda 3–4)
- **K-ex1:** any hadron containing an unclosed part (non-singleton colour content, or B ≢ 0 mod 3 in any sub-cell) that is **stable, or decays only weakly**. One such state kills the rule "any association containing an unclosed part is unstable".
- **K-ex2:** any exotic bound **far below every two-hadron threshold**. The scale is set in advance: binding > 10 % of the lightest constituent-hadron mass (≳ 100 MeV for the charm/bottom states), in place of the ≲ 10 MeV proximity pattern. One such state kills "exotics are proximity pairs". Grace's threshold table decides; the numbers have to come from her source pins.

## 9. Casey's surface (Addendum 5): one paragraph, with what can fail
A Šilov-boundary point u = e^{iθ}x (x ∈ S⁴) is a maximal tripotent, and V₂(u) = V. The map z ↦ Q_u(z) = {u z u} is an antilinear involution of V. Its fixed set is **e^{iθ}(ℝx ⊕ i·x^⊥)**, a real 5-dimensional form on which q has **Lorentzian signature (1,4)**: the real Jordan algebra at u is the Minkowski spin factor, with u as its unit. This was checked numerically at 10:4x. My first draft said "e^{iθ}ℝ⁵"; that was wrong and was caught before posting. **So each point of the Šilov boundary is a choice of a real, Lorentzian "half", and the boundary (S⁴ × S¹)/ℤ₂ is the space of those halves (real dimension 5 = half of 10).** The signature is worth Cal's attention: the half written on is Lorentzian at every Šilov point, with the unit u as its time direction. This is standard Jordan theory; the reading is the lead. The Cauchy–Szegő reproduction then says: every state in H² is fixed by what is written on the set of real structures. The circle factor S¹ is the phase θ of the real form, which is the clock. The record, per Section 1, forgets which real structure (T), so a record is a function on the interior, and a write is a value on the surface. **Can fail:** Szegő reproduction is exact, but "the write is a boundary value" is a reading. It fails if any committed quantity has no Šilov-boundary value. **T2626 (no survivor at a Šilov point, Howe–Moore) is the first thing to check against this, and it may bite.**

---
**Summary for Cal (please hash):** (1) SU(3) on records ⟺ T is not a record operation (the real structure = the arrow-reversing conjugation). (2) J is central in K; the SO(4) handedness lead dies; retire F242 rows 3–5; the hand is J ↔ ±⋆ in the descent. (3) 16 is not a one-circle count; one circle predicts Δ ≠ 0. (4) Every SO(4)-type of H² is a hydrogen shell n²; hydrogen's representation has multiplicity 0 (clock weights 5/2 + ℤ vs 1 + ℤ). (5) Ω_Λ = 13/19 is a colourless 19, so the pre-registered colour-only prediction is falsified or empty. (6) H-col with its Coleman–Mandula line. (7) Pauli as records being subspaces; ε = complete record = baryon singlet; SU(3) = the group keeping h and ε. (8) Two exotic kill lines. (9) The Šilov boundary = the space of real structures.
