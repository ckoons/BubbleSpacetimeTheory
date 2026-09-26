# Cal Section 991 — PRE-REGISTRATION, written before Lyra's round-6 item 1 lands (ground weight E₀ = 3/2 vs λ = 5/2)

Saturday 2026-09-26, written 11:4x EDT (stamp from `date` in the commit). Read before writing: Time, Derived v1.3 lines 12, 26, 48, 60 (`notes/BST_paper_Time_Derived_v1.3_Lyra_2026-08-17.md`); K1927(c); K1928 Part 4. Lyra's item not read (not yet filed: git log at 11:38 shows none).

**Invariant first:** the lowest eigenvalue of the K-centre J on an irreducible unitary lowest-weight module of SO(5,2) is an invariant of the module (it is the lowest weight). Two modules with different lowest J-weights are not G-isomorphic.

**Kill line:** P1 is wrong if Time, Derived defines the physical module as the minimal representation (then TD and G3 disagree on the physical module, a larger item), or if any G-equivariant map identifies H²(D_IV⁵) with the Rac (minimal) module.

**Predictions:**
- **P1 — two objects, one mislabelled sentence.** E₀ = 3/2 is the ground J-weight of the minimal representation (Rac, the Wallach point (n−2)/2 of D_IV⁵; TD line 26 says "the U(1) energy of the minimal representation"). On H²(D_IV⁵) at the Hardy point (λ = n/r = 5/2, G3), spec J = 5/2 + ℤ≥0, ground 5/2. TD line 12 puts J "on the substrate Hilbert space H²(D_IV⁵)" and line 26 quotes the minimal representation's 3/2. Neither number is wrong. The sentence that attaches 3/2 to H² is.
- **P2 — what survives relabelling:** the arrow (spec J bounded below by a positive number: 5/2 > 0); the double cover (exp(2πi·5/2) = −1, since 5/2 ∈ ½ + ℤ like 3/2); the parity class of H²'s weights (odd-#Rac coset).
- **P3 — what may not survive:** any downstream use of the NUMBER 3/2 as the physical module's ground energy (a zero-point term, a ratio with 3/2 in it, a tick written as ℏ/E₀). A grep is owed. None counted here.
- **P4 — K1927(c) is not the bridge.** It relates the 5D minimal module to 4D modules. J is shared by SO(4,2) ⊂ SO(5,2), so J on H_{3/2}(D_IV⁴) ⊕ H_{5/2}(D_IV⁴) still starts at 3/2 and never reaches H²'s 5/2 ladder. **The bridge, if one is wanted, is at the K-level:** H² ≅ Rac ⊗ (⊕_{j≥0} χ_{1+2j}) as K-modules (the Section 954/960 form, "H² ≅ Rac ⊗ clock"), so H²'s ground = Rac's ground + 1, and the +1 is n/r − a/2 = 5/2 − 3/2 (Hardy minus Wallach). It is not a G-isomorphism (Schur, Section 960).

Lyra's paragraph will be scored against P1–P4 as written here, with no edits after this file's hash.
