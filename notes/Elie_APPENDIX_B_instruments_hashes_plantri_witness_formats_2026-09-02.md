---
title: "APPENDIX B (draft v0.1) — Instruments, hashes, plantri version, witness formats. For the census paper. Every number in the paper traces to a script in play/, a run record in TOY_LOG.md, and a hash printed before the count."
author: "Elie"
date: "2026-09-02, Wednesday (clock-verified 12:46 EDT, stamp copied from a separate render)"
status: "DRAFT v0.1 for Lyra's v0.1 assembly; Cal's referee read tomorrow. Nothing here says proof; nothing mentions 25 vertices."
---

# B.1 Graph generation
- **plantri** (B. McKay & G. Brinkmann), version 5.8, built from source at `play/tools/plantri58/plantri`
  (tarball plantri58; the binary prints its usage banner with `-h`; the exact flag set used is stated per population below). Triangulations of the sphere as rotation systems (ASCII `-a`).
- Populations: (i) all triangulations n = 6…11 (`plantri n`: 2, 5, 14, 50, 233, 1,249); (ii) **5-connected
  triangulations n = 12…24** (`plantri -c5 n`: 1, 0, 1, 1, 3, 4, 12, 23, 71, 187, 627, 1,970, 6,833) — the frame
  in which a minimal counterexample lives (internally 6-connected ⟹ 5-connected); (iii) Florek's G_n
  (n-antiprism + two apexes) n = 5…12, constructed in code; (iv) named out-of-frame graphs: Fritsch (G5),
  Errera (Sage edge dict; ≡ the antiprism-stack "T3" — one object, two names, found 09-02), Kittell (Sage),
  Poussin (Sage constructor rules), and the corpus's flip families (family_B_right(k, off)) and stacked
  triangulations (P3).
- Faces come from the rotation system (u, nbr[i], nbr[i+1]) where plantri is the source; from
  `faces_from_adj_triangulation` for the named graphs (checked 3n−6 edges, Euler).

# B.2 Colorings and the stuck predicate
- All proper 4-colorings of T−v are enumerated by backtracking **modulo the 24 colour permutations**
  (canonical form: colours relabelled by first appearance along the sorted vertex order); Kempe swaps commute
  with relabelling, τ and insertability are invariant. Counts in the paper are mod-S₄ counts unless marked raw.
- **Stuck:** τ_v(c) = 6 (Definition 5: every pair (a,b) operationally tangled — no single (a,b)-swap seeded at a
  link vertex frees a or b at v) and not directly freeable. **Gate phase:** a colour absent at v, or τ_v ≤ 5.
- Roles (canonical context, One-Context Lemma): the two r-copies B₁, B₂ flanking the middle n_sM; singletons
  n_si, n_sj. The instrument's B₁/B₂ labels follow cyclic order from n_sM; where a statement needs the copy
  adjacent to a named singleton, the paper says so ("adjacency-pinned") — two conventions exist in the run
  records and every count states which.

# B.3 The alphabet and legality
- Context-moves: (role, {role's colour, x}), 15 of them; words = ordered pairs with distinct pairs, 186;
  93 mirror orbits (B₁↔B₂, s_i↔s_j). A word acts as the four-stage commutator m₁m₂m₁m₂.
- **Legality:** a stage is legal iff its seed carries a pair colour at that stage; a word is applied only if
  all four stages are legal. (The laboratory primitive `apply_move` is a silent no-op on an illegal stage;
  every count from toy 5587 on tags legality explicitly — counts before 5587 are superseded.)
- Kittell's eight chains, far-copy seed rule (Cal §821): α=(s_M,s_i)@n_sM, β=(s_M,s_j)@n_sM, γ=(r,s_j)@B₁,
  δ=(r,s_i)@B₂, ε=(s_i,s_j)@n_si, ζ=(r,s_i)@B₁, η=(r,s_j)@B₂, θ=(r,s_M)@n_sM.

# B.4 The instruments (script → what it measures → record)
| toy | measures | record |
|---|---|---|
| 5596 | in-frame existence + Kempe classes of T−v (union-find over canonical forms) | 374,658 stuck n ≤ 22; 0 classes without an insertable member |
| 5600 | direct one-word exit by the 3-word set then the family | per-n record hashes (n=22 bba11de8, 23 4325b0e8, 24 94ecad02) |
| 5601 | gate exit / word-depth BFS / single-swap null on the no-direct set | depth ≤ 2 everywhere; witnesses saved |
| 5602 | in-frame one-word hitting set (exact) | 1·2·8·4·6·9·14·21 for n = 14…22 |
| 5605/5606 | first/second-word anatomy; Kittell switch BFS | second word = bridge; switch distance ≤ 3 |
| 5608 | middle-first vs bridge-first two-word programs | bridge→middle 373,447/374,658 |
| 5611/5615/5616 | cut C = X₃∩X₄; containment; leaf table; Δ-flip; Z-tagging | H_cut dead; M3 signature; flip 69% |
| 5613 | eight-chain intersection type | 40 bit-types; locked mixed at every refinement |
| 5619/5620 | trajectory type (Cal §823 bits); far-chain bits on bridge-fails | mixed; 1,121/1,211 |
| 5622 | Kempe's two plain swaps; the 90's exit sets | 2/349 insert; hitting set 4/3 |
| 5624 | unrestricted plain-swap Kempe depth | (this afternoon) |

# B.5 Hashes and witness formats
- Witness files (JSON lists; each row: n, plantri -c5 index (0-based, in plantri's output order for that n),
  v, the coloring as a tuple in sorted vertex order (canonical mod S₄), legal-image count, single-swap gate
  count, exit kind): sha256 prefixes
  - 7a5ed073ec0f3428  .in_frame_26_two_word_locked.json
  - 13581405fe80c3c4  .in_frame_23_two_word_locked_n22.json
  - 734fc7930248b710  .in_frame_44_two_word_locked_n23.json
  - e5522680bd3202e6  .in_frame_256_two_word_locked_n24.json
  - bebde99d70dfbdfb  .nine_hard.json
  - 6a88a8d181f3bc0d  .the90_exit_sets.json
  - 7c930cb265c5788b  .tranche2_family_exclusion.json
  - 84ae31ca39ffe927  .tranche2b_family_exclusion.json
- Per-run record hashes are printed by each toy BEFORE its aggregate lines (blind discipline); TOY_LOG.md
  carries the score and one-line summary per toy; the running notes carry the k/N with the can-fail count.
- Regenerability: every population is regenerated from plantri + the seeds in the scripts; harvested sets
  (tranches, D-flip) regenerate bit-identically from fixed seeds (5574/5579 verified).

# B.6 Nulls that travel with the counts
Single-swap null (any seed, any pair, one swap → gate): 1,846/1,855 out of frame; 42/334, 258/827, 573/1,579,
3,682/10,488 on the in-frame no-direct sets. Generic Δ-NO base rate ≈ 99.7% at n = 22. Depth-three
expectation under the measured lock rates: below one witness in the census (Cal §823).

— Elie
