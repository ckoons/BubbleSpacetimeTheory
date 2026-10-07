# Cal Section 1030 — Round K4-0: four kill lines, hashed before anyone computes

**Written 2026-10-07 13:39 EDT. No teammate output on K4-0 had been read when this was written** (Lyra, Grace and Elie were woken at 13:33). Instrument: `play/cal_S1030_K4_kill_line_facts_before_anyone_computes_2026-10-07.py` (sha256 fd06f802…), SCORE 12/12, plain Python. Every structural fact below that the instrument checks is marked [I]. Facts not checked are marked pin-owed.

Keeper's four lines stand as written in the prompt. This file sharpens each one so it can fire mechanically, and adds what a referee would ask first.

## KL1 — Why 4: forced or chosen
**Fires (round says "chosen, tier S/C") unless one of the following holds.**
- **R1 (planarity) needs THREE loads, not one.**
  - (a) "Coordinate-free" must mean DIAMETER 1. Transitivity alone does not give a complete graph: cycles and the cube are vertex- and edge-transitive.
  - (b) The surface must be 2-dimensional.
  - (c) **The surface must be the SPHERE.** The cap is a genus statement, not a dimension statement. By Heawood/Ringel–Youngs (citation pin-owed; formula run [I]) the largest complete graph is K4 on genus 0, K7 on genus 1 and K8 on genus 2.
- **Coupling to the torus posit (the cage cannot be held one-sidedly).** If R1 is the forcing route and Casey's torus records are admitted, the SAME theorem forces K7 on the torus. The round must then either:
  - accept both (the 7 as a graph count is forced; its identification with g remains a separate map, still caged), or
  - forbid R1 on the torus and say why the complete-graph premise holds only on the sphere.

  Using R1 for the 4 while caging the 7 is not allowed.
- **R2 (the minimal closed surface)** forces 4 only in the SIMPLICIAL category. In CW complexes or multigraphs, a sphere closes with 2 vertices (a digon). So R2's loads are: simplicial, closed, genus 0, minimal. Each one needs a source in D_IV⁵.
- **The group search (Elie's lane; my predictions, hashed so they can be wrong):**
  - P1 [I]: the restricted Weyl group W(B₂) has order 8 and no element of order 3. By Lagrange it contains no S₃, A₄ or S₄. This search returns empty.
  - P2 [I]: the compact isotropy K = SO(5) × SO(2) contains S₄, S₅ AND S₆ faithfully. **"Found an S₄ in K" is void, and the K5 null fails there by construction.** Only DISTINGUISHED finite groups count: Weyl groups, component groups, the deck ℤ₂, N(T)/T, stabilisers of canonical point sets. Lane C should list theirs before searching.
  - P3 [I]: the one canonical S₄ is inside the complex Weyl group W(B₃) of so(7,ℂ), which has order 48. It is the cube's group; S₄ acts on the 4 body diagonals, which are the antipodal pairs of so(7)'s spin weights. S₅ is excluded by Lagrange.
  - **P4 [I]: this S₄ is not n = 5-specific.** For D_IV⁴, so(6) = D₃ and W(D₃) ≅ S₄ exactly. D_IV⁶ contains it too. A forcing must fail on D_IV⁴ and D_IV⁶.
  - **Null correction:** K3 cannot serve as a null for an S₄ search, because S₃ ⊂ S₄ always. The null is K5 together with the n-scan.
- **My prediction:** KL1 FIRES. 4 is chosen, unless the electron's 2D-ness and genus 0 are both forced (Lyra/Grace).

## KL2 — The frame vertex: one named sign
**First, a position-vs-value split the addenda leave open.**
- Addendum 2 calls the fourth vertex "one parity bit". That is a VALUE: one bit of information.
- Addendum 3 calls it "start/stop". That is a POSITION: a delimiter carrying no value.

These are different objects. The round must pick one.

**Fires (stays a posit) unless all four of the following hold:**
1. The choice of position or value is stated.
2. If it is a value, the round says whether the bit is a FUNCTION of the three values (a checksum, so no new information and the word carries 3, not 3 + 1) or INDEPENDENT (then it is a sign).
3. Exactly ONE of the Šilov deck ℤ₂, Z_t or (−1)^F is named BEFORE any fit is checked (W = Z_t·(−1)^F counts as a pair, not as a fourth option).
4. A map sends the frame's action to the sign's action.

**The structural mismatch to answer:** a sign is a ℤ₂ and leaves S₄ unbroken, while marking a vertex breaks S₄ → S₃ (a choice among 4). "The sign IS the vertex" needs the map that turns one bit into one choice-of-four.

## KL3 — The grammar: read order = the weak handedness
**Fires (stays a picture) unless the map satisfies all four checks.**
- **(a) The corpus's own chirality source.** T2522 and T1949 derive the weak handedness from the Šilov boundary being **NON-orientable** (Pin⁻); I recomputed the orientation sign of the deck map [I]. A non-orientable boundary carries NO global orientation. "One fixed read order everywhere", read as a global orientation of written triangles, cannot be inherited from this boundary. The map must go through the Pin⁻ structure, or say why the corpus's chirality derivation is replaced.
- **(b) Right-handed fermions exist.** e_R, u_R and d_R are weak singlets that are present in matter. Physics does not write every record left-handed; it COUPLES only the left-handed ones. The map must say what a right-handed record is: a word read in the other order that the grammar ignores, or something else.
- **(c) C and CP.** The weak interaction violates P and C maximally and conserves CP nearly. A bare orientation is P-odd only. The map must make antimatter read the opposite orientation. Otherwise it predicts left-handed antineutrinos, which is wrong.
- **(d) Which S₃.** S₄ carries two different S₃ structures, isomorphic as groups but not the same object [I]: the vertex stabiliser (a subgroup, not normal) and the quotient S₄/V₄, which acts on the 3 perfect matchings. Orienting "the triangle" is S₃ → ℤ₃ on the stabiliser. Any reading of the matchings as axes uses the quotient. Name which.

## KL4 — Casey's test: projection, not relabel
**Relabel criterion.** Suppose the K4 projection factors as Szegő ∘ φ, where φ sends records to boundary data. Then on the image of φ it gives what the kernel gives. Progress must come from what the kernel lacks: discreteness, commitment (non-unitarity) or the reverse direction. And it must show up in an output number or law.

**The filling law has a circularity trap; this is the most important line of the four.**
- K1922's factor three came from Casey's "three writes" PRODUCT reading. Its load-bearing debt was cells-versus-bits.
- C7 (the indivisible triple) was entered in Addendum 1 **as the answer to that debt**.
- So if K4-3 "projects" the filling law's factor three through C7, the posit is returning its own input. That is calibration #18, "hunt-if-P".

**K4-3 is credited ONLY for one of these:**
- **(i)** Indivisibility forced by something other than C7: Lyra's lane, e.g. K1926.
- **(ii)** The per-write exponent 2 (area count a² per axis, K1922 Section 4 / Elie 5778) derived from the record structure.
- **(iii)** K1922's owed SATURATION clause supplied by the K4 structure, with the ceiling written before any w-direction is printed.

Reproducing ε = 2 from C7 + the product reading is a relabel of K1922.

## The position-vs-value bar for the whole lane (the can-fail count)
- K4 has at least seven invariants equal to 3 [I]: cycle rank, Hamiltonian cycles, perfect matchings, degree, face size, faces at a vertex, and |S₄/V₄|. Some of these are the same fact (n − 1).
- So **"a 3 appears" has prior ≈ 1 and can-fail count 0.** Any identification of a K4 "3" with N_c, with D = 3 or with "three words" must name WHICH invariant (the position) and give the map.
- The same applies to 4 (vertices, faces) and 6 (edges, directed Hamiltonian cycles).

## Referee's first question (outside voice, written before reading the team)
*"You have a finite graph and a symmetric space. Name one number this picture predicts that the representation theory of SO₀(5,2) does not already give, and say what would make it wrong."* KL4 is this question. If it has no answer by K4-3, the lane is a vocabulary, not a mechanism.
