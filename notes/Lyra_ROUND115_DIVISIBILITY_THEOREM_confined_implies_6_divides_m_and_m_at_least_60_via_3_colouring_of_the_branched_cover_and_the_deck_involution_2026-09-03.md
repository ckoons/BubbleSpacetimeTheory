# ROUND 115 §2 — THE DIVISIBILITY THEOREM: confined ⟹ 6 | m and m ≥ 60 (derived, hashed before Elie's C₁₀₂…C₁₂₀ run)
**Lyra. Stamp (from `date`): 2026-09-03 Thursday 14:43 EDT.** Conserved Knowledge Theory. For Cal's referee read; nothing registered by me.

## 1. Confinement is 3-colourability of the cover (a fourth formulation of T2603)
Let Σ be the branched double cover of the triangulation T (branched at the k odd vertices) with its face-sign 2-colouring σ̃ (T2603).
The charge cocycle is c(u→w) = σ̃(left face of u→w) ∈ {±1} ⊂ ℤ₃. **[c] = 0 ⟺ Σ is 3-colourable as a triangulation.** Proof. If c = δφ then φ:
V(Σ) → ℤ₃ changes by ±1 across every edge, so it is a proper 3-colouring. Conversely a proper 3-colouring φ of the triangulation Σ gives
each face a cyclic orientation of its residues, hence a sign σ′(t) ∈ {±1}; along a shared edge the two faces traverse it oppositely, so
σ′ alternates across every edge; Σ's dual is connected and bipartite, so σ′ = ±σ̃, i.e. δφ = ±c, and [c] = 0. ∎
(For the sphere with no dislocations this is Heawood's "Eulerian ⟺ 3-colourable"; here Σ is always Eulerian — all degrees even —
and the obstruction to 3-colourability is exactly the class [c] ∈ H¹(Σ;ℤ₃).)

## 2. The deck involution puts every dislocation in ONE colour class
Let ι be the deck involution of Σ → T. It is orientation-preserving and swaps sheets, so σ̃∘ι = −σ̃ and ι*c = −c. If δφ = c, then
δ(φ∘ι) = −c, so ψ := −φ∘ι also satisfies δψ = c, and ψ − φ is a cocycle with zero coboundary, i.e. a constant on connected Σ:
**−φ(ιx) = φ(x) + κ** for some κ ∈ ℤ₃. At a branch point x = ιx this reads 2φ(x) = −κ, i.e. **φ(x) = κ** (2⁻¹ = 2 in ℤ₃). So all k
dislocations carry the same colour κ. For a hexagon vertex v with lifts (v,+), (v,−) = ι(v,+): φ(v,−) = −φ(v,+) − κ, so the two lifts
are either BOTH coloured κ (when φ(v,+) = κ) or coloured κ+1 and κ+2 (one each). ∎

## 3. The face count on the dislocation class
In a proper 3-colouring of a triangulation every face has exactly one vertex of each colour, so for each colour class C,
Σ_{v ∈ C} deg_Σ(v) = F(Σ). For a fullerene dual (m faces downstairs, 12 vertices of degree 5, h = m/2 − 10 of degree 6): F(Σ) = 2m;
a dislocation has deg_Σ = 10 (two laps of its 5-link); a hexagon lift has deg_Σ = 6. With all twelve dislocations in class κ and e_κ
hexagon lifts there: **120 + 6 e_κ = 2m, i.e. 60 + 3 e_κ = m.** Hence:
- **m ≡ 0 (mod 3), and since m is even, 6 | m.**
- **m ≥ 60**, with equality iff e_κ = 0 (C₆₀: the dislocation class is exactly the twelve branch points).
- e_κ is even (hexagon lifts enter class κ in ι-pairs, §2), so the number of hexagon vertices of T whose BOTH lifts are dislocation-coloured
  is **N_κ = (m − 60)/6** — a second, sharper count: C₆₀: 0 · C₇₂: 2 · C₇₈: 3 · C₈₄: 4 · C₉₀: 5 · C₉₆: 6 · C₁₀₂: 7 · C₁₀₈: 8 · C₁₁₄: 9 · C₁₂₀: 10.
- The other two classes have m/3 hexagon lifts each (3 e_i = m for i ≠ κ), consistent: (m − 60)/3 + 2m/3 = m − 20 = 2h ✓.
**General form (any triangulation with dislocation set D):** confined ⟹ Σ_{v∈D} 2·deg(v) + 6·(hexagon-type lifts in the class) = 2F, so
Σ_{v ∈ D} deg(v) ≡ F (mod 3) is NECESSARY for confinement. For fullerene duals: 60 ≡ m.

## 4. Theorem (Divisibility), and what it explains
**For a fullerene dual: confined ⟹ 6 | m and m ≥ 60; and in any 3-colouring of Σ the twelve dislocations share one colour and exactly
(m − 60)/6 hexagon vertices have both lifts in that colour.** Derived; necessary, NOT sufficient (C₆₆ has no IPR isomer; C₇₈ #0, #2–#4,
most of C₈₄, C₉₀, C₉₆ are unconfined with 6 | m). It explains, without a colouring: (i) why NO fullerene dual below C₆₀ is confined
(Elie 5651, sealed census 8500f714: 0 of 3,958 isomers below C₆₀ confined, and exactly 1 of 1,812 at C₆₀ — the icosahedral isomer; CORRECTED 2026-09-04 09:0x per Cal §842 R1: the earlier "5,770 isomers C₂₀…C₅₈, all height 2" mislabelled the population, which is C₂₀…C₆₀ inclusive and contains one height-1 isomer) — m < 60 is impossible; (ii) Elie's 14/14 with 6 | m and 0/940 at 6 ∤ m; (iii) the
gaps: confined isomers can live only at m ∈ {60, 66, 72, 78, 84, 90, 96, 102, …}, and 66 has no IPR isomer at all. Casey's
composite-and-gaps reading has its lattice: the admissible m are the multiples of 6 from 60 on.

## 5. Pre-registered for Elie's run (C₁₀₂ … C₁₂₀, all IPR isomers), hashed
1. **Zero confined isomers at m ∈ {104, 106, 110, 112, 116, 118}** (a theorem's zero; a single one kills §2 or §3 — a derivation failure,
   not a data failure).
2. Confined isomers, if any, only at m ∈ {102, 108, 114, 120}; I do NOT predict which of these carry one, nor how many.
3. On every confined isomer (the 14 known and any new): all twelve dislocations in one colour class of the cover's 3-colouring, and
   exactly (m − 60)/6 hexagon vertices with both lifts in that class (C₆₀: 0; C₇₂: 2; C₇₈ #1: 3; C₈₄ #19, #22: 4; C₉₀ #30, #36, #37: 5;
   C₉₆ ×6: 6). Elie has φ whenever [c] = 0 (his exactness BFS returns it); the count is one line.
4. Positive control on the theorem's mechanism: on an UNCONFINED isomer there is no φ, and the count is undefined — report "no φ", not 0.
Kill of the theorem: any confined isomer with 6 ∤ m, or any confined isomer whose 3-colouring puts two dislocations in different classes.

## 6. What is not claimed
Sufficiency (no second invariant offered); anything about non-fullerene triangulations beyond §3's general congruence; the 1/π; anything
for m > 120 except the theorem itself, which is for all m.
— Lyra
