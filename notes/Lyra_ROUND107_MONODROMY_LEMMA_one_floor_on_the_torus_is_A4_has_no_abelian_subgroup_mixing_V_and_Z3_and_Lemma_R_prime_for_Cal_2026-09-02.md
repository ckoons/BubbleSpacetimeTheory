# ROUND 107 — THE MONODROMY LEMMA: Lemma R′, the One-Floor Lemma on the torus, and where one floor fails
**Lyra. Stamp (rendered by `date` as a separate action): 2026-09-02 Wednesday 16:34 EDT.** Conserved Knowledge Theory (Casey's
name). DISCUSSION tier; nothing registered; Cal referees; frames pinned as in my 13:10 file (oriented closed surface,
Heawood sign z_t, ℤ₃ = ⟨A⟩ ⊂ GL(2,2) the rotation a→b→c→a, V = GF(2)², A₄ = V ⋊ ⟨A⟩ acting freely on colorings).

## 0. Line one
Every Heawood-closed record r on a closed orientable triangulated surface S carries ONE object: a flat A₄-torsor
(its local completions), hence a monodromy Φ_r: π₁(S) → A₄, defined up to conjugacy. Realized ⟺ Φ_r = 1. The
transport holonomy θ is Φ_r mod V; the "V-holonomy" is Φ_r on ker θ. The derived cover of Φ_r realizes r with
|im Φ_r| sheets, and |im Φ_r| ∈ {1, 2, 3, 4, 12} because those are the subgroup orders of A₄ — so NEVER 6.
**On the torus π₁ is abelian, im Φ_r is an abelian subgroup of A₄, and A₄ has no abelian subgroup containing both a
3-cycle and a nontrivial element of V. So a transport orphan has im Φ_r = ℤ₃ exactly, its 3-sheet θ-cover kills
Φ_r outright, and the V-obstruction cannot survive floor 1. That is the One-Floor Lemma, and it is torus-specific.**
On genus ≥ 2, im Φ_r = A₄ is not excluded; there one floor is predicted to FAIL (3 sheets, then 4, twelve in all).

## 1. The torsor (the object that was measured today)
Fix a face t₀ with edge e₀ and vertex v₀. A LOCAL COMPLETION of r near t₀ is a pair (label on e₀ ∈ {a,b,c}, color
at v₀ ∈ V): 3 × 4 = 12 choices, and each propagates uniquely across faces (the sign fixes the cyclic order of labels;
colors follow f(w) = f(u) + ℓ(uw)). A₄ = V ⋊ ⟨A⟩ acts on the 12 local completions freely and transitively (rotate the
label by A^j, translate the color by t ∈ V), so the local completions form an A₄-TORSOR; Lemma R (ii) is the
statement that A₄ is exactly the sign-stabilizer in S₄, so this is the largest group that can act. Propagation along a
path transports the torsor; around a closed loop γ it returns an element Φ_r(γ) ∈ A₄ (well defined up to conjugacy by
the base choice). Vertex loops give Φ = 1 by Heawood closure (the label part is c(v) mod 3 = 0 and the color part is
a face-sum a+b+c = 0), so Φ_r factors through π₁(S).

**Reading the pieces.** The ℤ₃-component Φ_r mod V is the transport holonomy θ (labels see only the rotation). If
θ = 0 then Φ_r ⊆ V is abelian and equals the label-cocycle class [ℓ] ∈ H¹(S;V) of 13:10 (the translation part is
Σℓ along the loop). If θ ≠ 0 there is no global labeling, and "the V-holonomy" is only defined on ker θ — which is
π₁ of the θ-cover — as Φ_r restricted there. That is what Grace's fattened-walk instrument computes.

## 2. Lemma R′ (for Cal; the clean statement, with the H₁ = 0 question answered)
**Lemma R′.** Let S be a closed orientable triangulated surface and r a Heawood-closed record.
(i) r is realized by a proper 4-coloring ⟺ Φ_r = 1. When realized, the completions are exactly the 12 flat sections,
one A₄-orbit: ONE completion per realized record mod A₄, on every S.
(ii) N_realized ≤ N_{θ=0} ≤ N_closed, with N_{θ=0} = #{r : Φ_r ⊆ V} and N_realized = #{r : Φ_r = 1}. If H₁(S) = 0
both are equalities (π₁ trivial forces Φ_r = 1 for every closed r: Heawood's theorem for the sphere).
*Proof of (i).* A coloring is a flat global section of the torsor; a flat section of a torsor with FREE structure-group
action exists iff every Φ_r(γ) fixes it iff Φ_r = 1; the sections then form one orbit of the 12-element fiber. ∎
**Where H₁ = 0 enters and where it does not.** The direction "realized ⟹ determined up to A₄" uses only the torsor
(12 local completions, free action, unique propagation). It never uses H₁ = 0. The sphere hypothesis in Lemma R
is used ONLY for the converse — every closed record is realized — via H₁ = 0 ⟹ π₁ = 1 ⟹ Φ_r = 1. That answers
Cal's referee question as I understand it: NO, not in that direction. The "iff H₁ = 0" in the wake prompt's R′
wording is half proved: H₁ = 0 ⟹ equality is proved; "equality ⟹ H₁ = 0" is MEASURED on every torus tested
(orphans always present) and I do not claim it in general — a torus triangulation with every closed record
realized would need Φ_r = 1 for all closed r, which I cannot exclude on paper today.

## 3. The Monodromy Lemma (derived)
**(a) The floor.** The derived (regular, unbranched) cover S̃_Φ → S with group im Φ_r is the MINIMAL cover realizing r:
on it Φ_r pulls back to 1 (construction), and any cover S′ → S realizing r has p_*π₁(S′) ⊆ ker Φ_r, so S′ factors
through S̃_Φ. Sheets = |im Φ_r|. Subgroups of A₄ have orders 1, 2, 3, 4, 12 (no subgroup of order 6: A₄ has no
element of order 6 and no index-2 subgroup). So the number of sheets of the floor is in {1, 2, 3, 4, 12}. **Never 6:
derived, not measured.**
**(b) Stage-wise floors.** Floor 1 := derived cover of θ (3 sheets if θ ≠ 0, else nothing). On it the residual
monodromy is Φ_r|ker θ ⊆ V. Floor 2 := derived cover of that (2 or 4 sheets). Total sheets = |im Φ_r|; the tower has
height ≤ 2 on every closed orientable surface, height 2 ⟺ im Φ_r = A₄.
**(c) One-Floor Lemma (torus).** π₁(T²) = ℤ² is abelian, so im Φ_r is an abelian subgroup of A₄: one of 1, ℤ₂, V, ℤ₃
(A₄'s abelian subgroups; ℤ₃ × ℤ₂ = ℤ₆ does not embed). Hence: θ ≠ 0 ⟹ im Φ_r = ℤ₃ ⟹ Φ_r|ker θ = 1 ⟹ realized on
the 3-sheet θ-cover with NO surviving V-obstruction; θ = 0 ⟹ im Φ_r ⊆ V ⟹ realized on the 2- or 4-sheet V-cover.
Every torus orphan has exactly one nontrivial floor; sheets ∈ {2, 3, 4}; never 6, never 12. ∎
**Grace's half in these coordinates.** A loop γ with θ(γ) = A^j, j ≠ 0, lifts 3:1; its lift's translation part is
t + A^j t + A^{2j} t = (1 + A + A²) t = 0 because A has minimal polynomial x² + x + 1 over GF(2). That is the
abelian-image argument read on one generator. **The owed half** — a loop δ ∈ ker θ (lifting 1:1) has zero V-holonomy —
is the commutator: on the torus [γ, δ] = 1, so Φ(γ)Φ(δ) = Φ(δ)Φ(γ); with Φ(γ) = (t, A^j) a 3-cycle and Φ(δ) = (s, 1)
a translation, commutation reads A^j s = s, i.e. s is fixed by A^j ≠ 1, and the only fixed vector of a 3-cycle on V is 0.
So s = 0. **The mechanism is "a rotation and a translation of V never commute unless the translation is zero."** That
is why 906/906 transport orphans needed no second floor, and why a transport-clean record CAN be cocycle-obstructed
(no rotation present to force the translation to zero) — both halves of Grace's table from one sentence.
**(d) The decision cost, identified (Grace 14:51 asked for the map).** The two "12"s are one object. The
structure group of the local-completion torsor is A₄ (Lemma R (ii)); Φ_r on the free generator of a fixed-width
torus family ranges over A₄; when the short generator's holonomy is trivial (the dominant sector, measured 5628) the
long generator's value is a free element of A₄, and N_closed/N_realized → |A₄| = 12 says that value is asymptotically
EQUIDISTRIBUTED over A₄ — an equidistribution statement (a null: "no further constraint on the record"), measured
to be exact, not derived here. The split log₂ 3 + log₂ 4 is |A₄| = |ℤ₃|·|V| through the extension. log₂(sheets)
was never a candidate once (a) is read: sheets = |im Φ|, and on a fixed-width family im Φ on ONE generator is
cyclic, of order 1, 2, or 3 — its log is not the cost of deciding among 12 values.

## 4. Pre-registered, can-fail
- **P1 (torus, derived):** no orphan on any torus triangulation needs a second floor; sheets ∈ {2,3,4}. Kill: one
  record on a torus with a surviving V-obstruction after its 3-sheet θ-cover, or a 6- or 12-sheet minimal cover.
  (Grace's 906/906 and 5629/5630 are the measurement; the derivation says it cannot fail.)
- **P2 (genus ≥ 2, prediction, not derived):** there exist Heawood-closed records with im Φ_r = A₄, needing a 3-sheet
  floor and then a 4-sheet floor (12 in all). Witness shape: a genus-2 triangulation and a record whose transport
  holonomy on two generators are two DIFFERENT 3-cycles of A₄ (two 3-cycles generate A₄) — equivalently, two
  loops with θ ≠ 0 on each whose commutator has nonzero V-holonomy. Kill of P2: every closed record on every genus-2
  triangulation tested has abelian image. I do not know a construction today; existence is Grace's instrument's
  question if Casey wants it, and the honest registered scope until then is "torus: one floor; general: ≤ two floors,
  sheets ∈ {1,2,3,4,12}."
- **P3 (structural, derived):** |im Φ_r| ∈ {1,2,3,4,12} on every closed orientable surface; 6 never appears.
- **Positive controls for any instrument computing Φ_r:** the sphere (Φ = 1 on every closed record); a realized torus
  record (Φ = 1); a transport orphan (Φ a 3-cycle; its cube trivial); a cocycle orphan (Φ ∈ V, order 2).

## 5. What is derived and what is not (for Keeper's ledger)
Derived: the torsor; R′(i); H₁ = 0 ⟹ R′ equalities; the floor is the derived cover of Φ_r; sheet orders {1,2,3,4,12};
One-Floor on the torus with its mechanism; the identification of the cost constant with |A₄|. Measured only:
orphans exist on every torus tested; equidistribution of Φ on the free generator; 906/906. Not claimed: "equality
⟹ H₁ = 0"; P2's existence. Naming: none here beyond Casey's.
— Lyra
