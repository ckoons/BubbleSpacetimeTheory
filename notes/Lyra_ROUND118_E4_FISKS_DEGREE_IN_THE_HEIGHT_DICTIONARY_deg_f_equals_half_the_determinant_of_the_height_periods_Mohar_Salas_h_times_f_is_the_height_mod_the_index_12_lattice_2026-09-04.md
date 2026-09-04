# Round 118 E4 — FISK'S DEGREE IN THE HEIGHT DICTIONARY: it IS a function of the height lift's global datum
**Lyra. Friday 2026-09-04, 09:03 EDT (from `date`, rendered 09:03:17). Existence before derivation; written BEFORE E5 runs. Source pinned from the paper, not memory: Mohar–Salas, arXiv:0901.1010 / J. Phys. A 42 (2009) 225204, Section 3.1 eq. (3.1)–(3.2), Proposition 3.2 (Fisk), Theorem 3.4, Corollary 3.5. Fisk's own text (Adv. Math. 24 (1977)) is Cal's pin; nothing below needs more of Fisk than Mohar–Salas quote.**

## 0. The spaces, named first
- **Col₄(T)**: proper 4-colourings f of the triangulation T of a closed oriented surface (Mohar–Salas: "a nondegenerate simplicial map f: T → ∂Δ³", eq. 3.1). Fisk's degree deg: Col₄(T) → ℤ, "deg(f) = p − n" for any one target triangle t, p/n = faces mapping to t orientation-preserved/reversed (eq. 3.2), independent of t.
- **The height** h: V(T) → ℤ² (Eulerian T; on T with odd vertices, on the branched double cover Σ), h ≡ f mod 2 under V = GF(2)² = ℤ²/2ℤ². Its **global datum** is the period class [ω] ∈ H¹(T; ℤ²) = (H¹(T;ℤ))², i.e. the pair of integer classes ([ω_x], [ω_y]); on a torus with generators γ₁, γ₂ this is the two period vectors P₁ = P(γ₁), P₂ = P(γ₂) ∈ ℤ².
- **The charge** φ = (x + y) mod 3 of h: a 3-colouring of T when T is Eulerian and [c] = 0 (Paper 2, 3.3 = Fisk's criterion). Λ₀ = {x + y ≡ 0 (3)} ⊂ ℤ² the charge kernel (index 3).
- **The Heawood/Fisk face sign** ε_F ∈ {±1}: the cyclic order of the three labels a, b, c around F (= Fisk's orientation sign of f on F, up to one global sign; both are A₄-invariant and flip under a transposition of colours — checked on the face (0,b,c) under (0 a)).

## 1. Lemma (the face sign is the orientation of the height image).
On a face F with height sign σ_F (the chessboard of T2603) the image triangle has edge vectors σ_F L(ℓ) in label order. Negation of the plane preserves orientation, so the orientation o_F of h on F is ε_F **for both σ_F = ±1**: o_F = ε_F. (This is why the chessboard is invisible to Fisk's degree and why T2603's colouring-independence and Fisk's colouring-dependence coexist: σ is the triangulation's, ε is the colouring's.) Hence
  **deg(f) = ¼ Σ_F ε_F = ¼ Σ_F o_F = ½ · (signed area of the height image, faces of area ½).**
Sphere: a single-valued map into ℝ² has zero signed area ⟹ deg = 0 for every 4-colouring of an Eulerian sphere triangulation (Fisk's positive control, re-derived).

## 2. Theorem (Mohar–Salas's h × f is the height mod an index-12 lattice).
Let T be Eulerian and 3-colourable (their hypothesis), so h exists on T with periods in 2ℤ² (Paper 2, 1.3) and the charge φ is a 3-colouring, so the periods lie in Λ₀. Put **L₁₂ := 2ℤ² ∩ Λ₀** (index 4 · 3 = 12 in ℤ²). Then h descends to h̄: T → ℝ²/L₁₂, and (h̄ mod 2, h̄ mod Λ₀) = (f, φ) is Mohar–Salas's map h × f: T → Δ² × ∂Δ³ = T(6,2,2) — the torus ℝ²/L₁₂ triangulated by the 24 lattice triangles (12 vertices, 6-regular), exactly their Figure 1. Their projection g to ∂Δ³ has degree 6 = 3 (forget the charge: ℝ²/L₁₂ → ℝ²/2ℤ², three sheets) × 2 (the colour torus ℝ²/2ℤ² → ∂Δ³: each colour triple is carried by two lattice triangles, both positively oriented). So their Proposition 3.2, deg(f) = 6 deg(h × f), reads
  **deg(f) = 6 · deg(h̄ : T → ℝ²/L₁₂).**
On a torus the degree of a map to a torus is the determinant of the induced map on H₁, so
  **deg(f) = 6 · det(P₁, P₂)/12 = det(P₁, P₂)/2.**
On genus g with a symplectic basis (a_i, b_i): deg(f) = ½ Σ_i det(P(a_i), P(b_i)) = ½ ⟨[ω_x] ∪ [ω_y], [T]⟩. **Fisk's degree is the cup-square of the height's period class, halved.** It is a function of the global datum, quadratic, and nothing else enters.
Consistency (three checks, all pass): periods even ⟹ det ∈ 4ℤ ⟹ deg even (Tutte, their Lemma 3.1); periods in Λ₀ ⟹ det ∈ 12ℤ ⟹ deg ∈ 6ℤ (their Prop. 3.2); their Kempe invariant deg mod 12 is **det(P₁,P₂)/12 mod 2 = det(Q₁,Q₂)/3 mod 2 with P_i = 2Q_i, Q_i ∈ Λ₀ — the parity of the charge-neutral period area.**
Checkpoint for Cal (named, not assumed): the chessboard sign on T exists iff the dual of T is bipartite; on every lattice torus T(3L,3M) it is the up/down colouring and exists; for a general Eulerian surface triangulation the obstruction is a ℤ₂ class, to be read off the page before E5 leaves lattice tori.

## 3. What this settles for E5, before the run
- **E5(ii) is a THEOREM, not a measurement:** deg mod 12 is a function of the height datum, by the formula. The run checks the instrument.
- **E5(i) is OPEN and the formula constrains it:** a Kempe change re-labels the boundary edges of the Kempe region (ℓ → ℓ + a on edges from ∂R into R), so the period vectors CAN change; if they change, they change by δ with det(P + δ) − det(P) ∈ 24ℤ (Theorem 3.4). I make no prediction on (i); "the datum is invariant" and "the datum moves inside a det-mod-24 coset" are both open, and (i) = NO is not a kill of the dictionary — it is the statement that the conserved charge of WSK is the QUADRATIC invariant of the record, not the record.
- **E5(iii):** #Kempe classes ≥ #distinct values of det(P₁,P₂)/12 mod 2 (two on T(3L,3M) by Mohar–Salas's existence result for deg ≡ 6); #distinct height data ≥ #classes iff (i) = YES.

## 4. Hashed for Elie/Grace on T(9,9) (three lines, before any enumeration; toy number from the claim file)
H1. For every 4-colouring f of T(9,9): deg(f) = s · det(P₁, P₂)/2 with ONE global sign s ∈ {±1} fixed by the orientation conventions (Fisk's on ∂Δ³, ours on T). Exact, colouring by colouring. Kill: any colouring off by other than the global sign.
H2. det(P₁, P₂) ∈ 12ℤ for every colouring (periods in L₁₂). Kill: one colouring with det ∉ 12ℤ (then either the height is not single-valued on T(9,9), i.e. the chessboard or the 3-colourability failed, or the instrument reads periods in the wrong basis).
H3. Two Kempe classes at least, separated by det/12 mod 2; the class containing the 3-colourings has det ≡ 0 mod 24 (Mohar–Salas Cor. 3.5 + Theorem 3.4). Kill: a Kempe path (BFS) joining det/12 odd to det/12 even.
Positive control: an Eulerian sphere triangulation (the octahedron): every colouring has P = 0 and deg = 0; one Kempe class (Fisk 1973).

## 5. On the tower (T2613) and the cover case
For T with odd vertices and [c] = 0 (confined), the pulled-back colouring on Σ has degree 2 deg(f), the height descends to Σ → ℝ²/L₁₂, and deg(f) = 3 deg(h̄_Σ) = ¼ Σ_i det(P(a_i), P(b_i)) over a symplectic basis of H₁(Σ). For [c] ≠ 0 the height does not descend mod Λ₀ and Fisk's factorization through Δ² is unavailable — which is Mohar–Salas's own hypothesis (3-colourable) seen from the tower: the charge floor is where the mod-12 invariant is born. Not asserted beyond this sentence.

— Lyra
