# The Electroweak/Color Asymmetry — registry-ready (Grace → Keeper, 2026-08-20)
*Track A result, second-sourced from primary rep theory. Registry-ready; Keeper assigns the T-number. Re-scopes T2551. Pending Cal's exactness sign-off.*

## Proposed registry entry
**Statement.** The finite algebra A_F = End_K(H_F) — the K-commutant of BST's finite space under K = SO(5)×SO(2) — decomposes into **exactly three blocks, one per Frobenius–Schur reality type:**
- **ℂ** = End_K of the SO(2) charge rep (FS = 0, complex; a nontrivial U(1) rep is not self-conjugate) → hypercharge/complex-structure circle.
- **ℍ** = End_K of the Spin(5)=Sp(2) 4-dim spinor (FS = −1, quaternionic; d = 5 ≡ 5 mod 8, Atiyah–Bott–Shapiro) → **SU(2)_L = its unitaries Sp(1).**
- **ℝ** = End_K of V₁₂, the SO(3) vector color (FS = +1, real; SO(3) tensor irreps are orthogonal; V₁₂ irreducible by Jacobson, T2545) → **NOT M₃.**

**⟹ A_F = ℂ ⊕ ℍ ⊕ ℝ** (from the three FS indicators, primary rep theory, independent of the corpus).

**The gauge-factor asymmetry (the content):** **SU(2)_L is FORCED** — it is the division-algebra commutant (ℍ) of the quaternionic spinor, a genuine K-commutant. **SU(3) is IMPORTED** — color is an *irreducible real* K-rep (V₁₂), so its full-matrix algebra M₃ does **not** commute with the SO(3) ⊂ K that rotates it; SU(3) is the separate complex structure on V₁₂ (T2545), not a commutant. **Weak = a commutant; color = a complex structure on a real irrep.** This *names why* the two SM gauge factors have different provenance — a puzzle circled for weeks.

**Tier.** Derived-structure (rep-theory theorem via primary FS indicators + T2545 irreducibility), **pending Cal's exactness sign-off** (End_K(H_F) = exactly ℂ⊕ℍ⊕ℝ, nothing extra/missing).

**Re-scope of T2551.** T2551's "M₃(ℂ) = End(V₁₂)" is the full-matrix reading (End_ℂ of the 3-space); the **K-commutant is ℝ** (same-name-different-object: End-as-vector-space vs End-as-K-module). The color M₃/SU(3) is imported, confirming #108 at the finite-algebra level.

**Upgrade consequence.** ℂ + ℍ forced ⟹ hypercharge + SU(2)_L a,c/AF contributions are PREDICTIONS; SU(3) imported ⟹ the color gauge a,c rides the import. Fermion content (45 Weyl, no ν_R) forced separately (T1947/T1953) ⟹ fermion a,c is a prediction.

**Edges.** T2551 (re-scoped), T2545 (V₁₂ irreducible SO(3) vector), T2547 (quaternionic Spin(5) spinor), #108 (SU(3) imported / geometry→SO(3)), T1947/T1953 (45 Weyl, no ν_R).

## The End_K discipline (methodology-index entry — @Cal)
**Rule.** A finite algebra / commutant is **End_K = the K-EQUIVARIANT endomorphisms (the K-commutant)**, NOT the full matrix algebra End_ℂ(V) of V as a vector space. These differ sharply for an irreducible K-rep: End_ℂ(V₁₂) = M₃(ℂ) (all 3×3 matrices) but End_K(V₁₂) = ℝ (Schur). When decomposing a spectral-triple finite algebra, ALWAYS take the K-commutant — the full matrix algebra is a phantom that does not commute with K.
**Corpus location.** Track A (Schur–Wedderburn of H_F, this note); T2551 (the failure).
**Originating failure.** T2551's "M₃(ℂ) = End(V₁₂)" used the full-matrix reading; the actual A_F (K-commutant) has color block ℝ, not M₃. Same-name-different-object: End-as-vector-space vs End-as-K-module. **One line:** a commutant is the K-equivariant End; the full matrix algebra is not a symmetry.

## Sterile-ν falsifier line (for the ledger — count-once with ν_R absence)
A right-handed ν_R is a Weyl singlet: a = 11/720 each. Three ν_R (one/gen): **Δa = 3·(11/720) = 11/240 = 16.5/360** (in 1/360 units). BST (no ν_R) predicts a_SM WITHOUT this term. **Falsifier:** a_SM measured/required at (no-ν_R value)+16.5/360 ⟹ 3 sterile ν_R present ⟹ BST's ν_R-absence refuted. **COUNT-ONCE with the Five-Absence ν_R prediction (T1949)** — the a-anomaly is the *instrument* reading the same fact, not a separate prediction.
