# Lyra R17 (Lane C): the de Sitter clock. Λ breaks J; the surviving time is a boost; the ladder stays as kinematics, not dynamics. A Time, Derived parenthesis for Casey

**Lyra, Sunday 2026-09-27, 15:53 EDT (from `date`).** Inputs: Cal Section 1011, Lyra R16 (ebfe50d1), K1937.
**Instrument:** `play/toy_5841_lyra_R17_…noncompact.py`, sha256 `c9a79411dd36d588…`, hashed and run at 15:52:12. **SCORE 3/3**, output `play/.out_toy_5841.txt`. C1's zero projection is immediate in this basis; it is a check, not a discovery.
**didwe:** "de Sitter clock J broken" → 0.

**Family statements, per the new rule, before using any representation:**
- **H²:** the unitary scalar highest-weight module of SO₀(5,2) at the Hardy point λ = 5/2 (analytic-continuation range, below the holomorphic discrete series λ > 4).
- **Its 4D pieces H_{5/2+k}(D_IV⁴):** unitary scalar highest-weight modules of SO₀(4,2). k = 0 is below the discrete series; k ≥ 1 are holomorphic discrete series.
- **De Sitter representations:** the unitary principal and complementary series of SO₀(4,1).

**Kill line (written first):** if Λ > 0 left J inside the surviving symmetry, the discrete clock would stay exact. It does not (C1): J rotates the two-time plane and moves the de Sitter vector e₅.

## The paragraph

**With Λ > 0, the curvature fixes a timelike vector in the clock's own plane (Cal Section 1011), and the symmetry that survives is de Sitter SO(4,1).**
- **J is not in it** (C1). SO(4,1)'s compact part is SO(4), spatial rotations only, and every generator that moves the remaining time direction is a **boost**: non-compact, hyperbolic, with continuous spectrum on unitary representations (C2, C3).
- **So the conserved "time" of a Λ > 0 world is a de Sitter boost** (the static-patch Killing time), **not the elliptic clock.** BST's time generator J is exact only in the limit Λ → 0.

**What happens to H²'s discrete clock spectrum 5/2 + ℤ≥0:**
- **As kinematics it is untouched:** J's spectrum on H² is a property of the representation, and H² does not change.
- **As dynamics it is no longer conserved:** J no longer commutes with the evolution. Its eigenvalues are approximate quantum numbers, good to order **H/E** (E the energy of the process; no value of H/E is computed here, per yesterday's no-scan rule).
- **How H²'s 4D pieces decompose under SO(4,1) is NOT computed here.**
  - The naive map "Δ → m²/H² = Δ(3 − Δ)" gives 5/4 at Δ = 5/2 (complementary series) but a **negative** value for Δ ≥ 7/2 (k ≥ 1). It therefore cannot be the general rule for these families, and it is **not assumed.**
  - The restriction of these SO(4,2) highest-weight modules to SO(4,1) is a branching problem; **pin owed** (Grace: a numbered source for highest-weight modules of SO(4,2) restricted to SO(4,1)).

**Why this is harmless for particles:**
- R15 (Cal Section 1010): the clock's ladder in units ħc/R is a frame statement, and physical masses enter only through the ruler.
- R16: with Λ > 0 the ruler becomes the de Sitter label m_e/H.
- So nothing BST says about particle spectra rests on J being exactly conserved. What changes is the *reading* of the clock: an exact generator becomes an approximate one, at order H/E, which is negligible at every particle-physics energy.
- **The arrow survives** as what it is in Time, Derived: the **positivity of J's spectrum on H²** is kinematic, so it is unchanged. What becomes approximate is "J generates the flow".

**What it connects:**
- R14/R15 found that charge vertices need J broken (the ruler as a mass). **Λ > 0 breaks J everywhere, weakly, at scale H.** So the exact clock symmetry that forbade single-H² vertices (R14) is itself exact only as Λ → 0.
- **The odd-H² prohibition** (Cal Section 1009; K1935 amendment) therefore holds exactly in the Λ → 0 limit, and to order H/E otherwise.
- **The mod-2 H² superselection label** (R15 Lane C) likewise.

## Time, Derived: the proposed parenthesis (FOR CASEY'S WORD; not applied)

**Where:** v1.4, Section 2, immediately after the sentence that names the generator ("The generator is the **conformal Hamiltonian** J … with a **half-integer spectrum**."). v1.4 is frozen, so on Casey's GO this lands as **v1.5**, and Cal gates it.

**Text:**
> *(J is the generator of the flow exactly in the limit Λ → 0. With Λ > 0 the cosmological curvature fixes a timelike vector in J's own plane, so the surviving symmetry is de Sitter SO(4,1) and the conserved time is a de Sitter boost. J then generates the flow to order H/E, where E is the energy of the process. J's spectrum on H², and with it the arrow's positivity, is a property of the representation and is unchanged.)*

**Calibrated both ways:**
- It concedes one thing honestly: "J is the time" becomes a Λ → 0 statement.
- It keeps what the paper derives: the arrow as spectrum positivity, and the double cover.
- It adds no number.

---
**For Cal (adversarial):**
- Is "the arrow's positivity is kinematic, unchanged" right? Or does the paper's arrow argument need J to be the *conserved* generator (Section 3: "exp(−τJ) is a contraction semigroup … the flow runs one way")?
- If the latter, the parenthesis must say that the arrow, too, holds to order H/E.

**For Grace:** the SO(4,2) → SO(4,1) branching of highest-weight modules (numbered source). It replaces the naive Δ(3 − Δ) map, which fails for Δ ≥ 7/2.
**For Casey:** the parenthesis above, yes or no.
