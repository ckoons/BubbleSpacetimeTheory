---
title: "F452 — the F451 identification is now FORCED (a theorem): the color su(3) fundamental 3 is a MAXIMAL ISOTROPIC subspace of the so(7) vector ℂ⁷, so the SO(7) Dirac spinor (BST's 2^{N_c}=8 Clifford sector) IS Λ*(color-3) = the color Fock space — and its grades match QCD color EXACTLY. Proof: under su(3)⊂g₂⊂so(7), ℂ⁷ = 1+3+3̄ (F449); the SO(7) quadratic form Q is su(3)-invariant and there is NO invariant 3⊗3 form (3⊗3 = 6+3̄, no singlet), so Q(3,3)=0 — the color-3 is isotropic, dim 3 = ⌊7/2⌋ = maximal. The standard spinor construction gives Spin(7) spinor = Λ*(maximal isotropic ℂ³) = Λ*(color-3). Grades: Λ⁰=1 vacuum, Λ¹=3 QUARK, Λ²=3̄ DIQUARK (antisymmetric qq = 3̄ in QCD — MATCHES), Λ³=1 BARYON (singlet ε=det). Cross-check: 8-spinor under g₂ = 7+1 → under su(3) = 1+1+3+3̄ = Λ*(ℂ³). MATCH, FORCED. This upgrades F451: the color Fock space = the SO(7) spinor sector is a THEOREM, not an identification; Pauli exclusion (v∧v=0) and the color/spin unification are forced by D_IV⁵'s so(7) with the color-3 as its isotropic subspace. Answers the F451 load-bearing check (Grace's lane). No bank (unification/theorem-of-existing-structure, not a new observable); count 8. For Casey, Grace, Keeper, Elie, Cal."
author: "Lyra (Claude Opus 4.8)"
date: "2026-07-02 Mid-Year Day (date-verified)"
status: "v0.1 — F451 identification UPGRADED TO THEOREM. color-3 = maximal isotropic subspace of so(7) vector ℂ⁷ (Q(3,3)=0 since 3⊗3=6+3̄ has no singlet; dim 3=⌊7/2⌋ maximal). Spin(7) spinor = Λ*(isotropic ℂ³) = Λ*(color-3) = 2^{N_c}=8 Clifford sector. Grades match QCD: Λ⁰ vacuum, Λ¹=3 quark, Λ²=3̄ DIQUARK (QCD-correct), Λ³=1 baryon. Cross-check via g₂: 8→7+1→1+1+3+3̄ = Λ*(ℂ³). FORCED. Color Fock = SO(7) spinor is a THEOREM; Pauli + color/spin unification forced by D_IV⁵. No bank, count 8. For Casey/Grace/Keeper/Elie/Cal."
---

# F452 — color Fock space = SO(7) spinor is a theorem (the color-3 is the isotropic subspace, grades match QCD)

## ⚠ NOVELTY CORRECTION (Keeper flag K642 + literature check, 2026-07-02) — this theorem is CORRECT but KNOWN; the "new for nuclear physics" framing is WITHDRAWN

Keeper flagged that I should check the literature before "new" hardens. I did (WebSearch), and he was right. The structure below — color su(3) as the exterior algebra of a maximal isotropic ℂ³ in so(7)/G₂, with the 8-spinor grading {1, 3, 3̄, 1} = {vacuum, quark, diquark, baryon} — is **the established Günaydin–Gürsey octonionic quark model (1973)** and its active modern descendants (Furey; Dixon; Lasenby's geometric-algebra SU(3); Stoica's Cℓ(6)/Cℓ(7) SM algebra; the "algebraic Standard Model" program). The literature explicitly states "the extension from SU(3) to Spin(7) extends the three colours and three anticolours to 7 charges" — exactly the ℂ⁷ = 1+3+3̄ decomposition. So:

- The **math is a genuine theorem and it is correct** — but it is a *known* theorem, not a discovery. BST **re-derives / embeds** it, it does not find it.
- **"New for nuclear physics" is WRONG** and withdrawn. This is a ~50-year-old *particle*-physics algebraic structure; it is not new, and it is not nuclear.
- **What is genuinely BST-specific (modest, and to be stated carefully, not as "new physics"):** the octonionic color algebra here is the spinor of **so(5,2) ≅ so(7), the isometry algebra of the *spacetime* domain D_IV⁵** — so in BST the *same* so(7) that carries color also carries the conformal spacetime chain (so(3,1)⊂so(4,2)⊂so(5,2)). The algebraic-SM literature (Furey et al.) typically treats the Clifford/octonion algebra as an *internal* space separate from spacetime; BST ties it to the spacetime geometry. That embedding is the only candidate-novel element, and even it has echoes (Cℓ(7) geometric-SM approaches) — so it is a **connection to a respected literature, not a claim of priority.**
- **Correct disposition:** F451/F452 are a **consistency WIN, not a discovery** — BST's D_IV⁵ Clifford sector independently reproduces the established Günaydin–Gürsey color structure (including the QCD-correct diquark = 3̄). That is real evidence BST's color sector is right, and a citation bridge to a 50-year program. It is **understanding, not a bank, and not new** (count 8, unchanged). Cite Günaydin–Gürsey 1973 and the modern algebraic-SM program in any writeup; never present the exterior-algebra color structure as original.

The technical content below stands (it is correct); read it as "BST reproduces this known structure," not "BST discovers it."

---

F451 identified the substrate's 2^{N_c}=8 Clifford sector with the color Fock space Λ*(color-3), pending one check (Grace's lane): is the color ℂ³ really the maximal isotropic subspace of so(7) whose exterior algebra builds the spinor? I ran it. **It is — and the result is forced (and, per the correction above, it is the known Günaydin–Gürsey structure).**

## The proof (it's short and clean)

The so(7) vector is ℂ⁷ with a quadratic form Q. Under su(3) ⊂ g₂ ⊂ so(7),

  ℂ⁷ = 1 ⊕ 3 ⊕ 3̄   (F449).

Q is su(3)-invariant, so it can only pair su(3)-dual pieces. The invariant bilinears on 1⊕3⊕3̄ are 1⊗1 and 3⊗3̄ — and crucially **there is no invariant 3⊗3 form** (3⊗3 = 6 ⊕ 3̄ contains no singlet). Therefore **Q(3,3) = 0: the color-3 is isotropic.** Its dimension is 3 = ⌊7/2⌋ = the maximal isotropic dimension in ℂ⁷. So the **color-3 is a maximal isotropic subspace of so(7).**

The standard construction of the Spin(7) Dirac spinor is Λ*(W) for W a maximal isotropic subspace. Taking W = the color-3:

  **SO(7) spinor 8 = Λ*(color-3),** with grades under su(3)_color:

| grade | rep | state | QCD check |
|---|---|---|---|
| Λ⁰ | **1** | vacuum | — |
| Λ¹ | **3** | quark | color triplet ✓ |
| Λ² | **3̄** | diquark | antisymmetric qq = **3̄** in QCD ✓ (this is a real, nontrivial match) |
| Λ³ | **1** | baryon | color singlet ε = det ✓ |

**Cross-check (independent route):** the 8-spinor of SO(7) under g₂ is 7 ⊕ 1; then 7 → 1+3+3̄ and 1 → 1 under su(3), giving 8 → 1 + 1 + 3 + 3̄. And Λ*(ℂ³) = 1(Λ⁰) + 3(Λ¹) + 3̄(Λ²) + 1(Λ³) = 1 + 1 + 3 + 3̄. **They match.** Forced.

## What this upgrades

F451 was "strong identification, checkable." F452 makes it a **theorem**: BST's 2^{N_c} = 8 Clifford/spinor sector (H_Clifford, F369) **is** the color Fock space Λ*(color-3), because the color-3 is the maximal isotropic subspace of the so(7) that D_IV⁵'s isometry algebra so(5,2) ≅ so(7) carries. Consequences, now forced:

- **Pauli exclusion is geometric and forced:** v∧v = 0 on the odd generators of this spinor/exterior algebra — exclusion is the nilpotency of the color Fock creation operators, which *are* the substrate's spinor structure. Not a statistical axiom; a theorem of the substrate geometry.
- **Color and spin are unified:** the *same* 8-dimensional so(7) spinor is the color Fock space (grade = quark number) and the Dirac/Clifford spin sector. D_IV⁵ forces color and spin to share one exterior algebra.
- **The QCD diquark = 3̄ falls out** (Λ² of the color-3) — a nontrivial, correct QCD fact reproduced with zero input, which is real evidence the identification is right and not a dimension-coincidence.

## Honest tier

| claim | tier |
|---|---|
| color-3 is a maximal isotropic subspace of so(7) (Q(3,3)=0) | **SOLID** (rep theory; 3⊗3 has no singlet) |
| SO(7) spinor = Λ*(color-3) = color Fock space; grades = {vacuum, 3, 3̄, 1} match QCD | **THEOREM** (standard spinor construction + the isotropy fact) |
| ⟹ Pauli exclusion + color/spin unification forced by D_IV⁵ | **forced given** su(3)⊂g₂⊂so(7) (corpus, K551/F449) |
| new observable / bank | **none** — this is a theorem about existing structure (the 2^{N_c}=8 sector), a unification, not a new number |

**No bank; count 8.** F452 forces F451: the alternative to Pauli (exclusion = exterior-algebra nilpotency, color Fock = the spinor sector) is not just consistent — it is a theorem of D_IV⁵, and it reproduces the QCD color grading (quark 3, diquark 3̄, baryon 1) exactly.

— Lyra, 2026-07-02. F452: color-3 = maximal isotropic subspace of so(7) (Q(3,3)=0, dim 3=⌊7/2⌋). Spin(7) spinor = Λ*(color-3) = 2^{N_c}=8 Clifford sector = color Fock space. Grades {1,3,3̄,1} = {vacuum, quark, diquark-3̄, baryon} match QCD (incl. diquark=3̄). Cross-checked via g₂ (8→7+1→1+1+3+3̄). FORCED. F451 identification is now a THEOREM; Pauli + color/spin unification forced by D_IV⁵. No bank, count 8.
