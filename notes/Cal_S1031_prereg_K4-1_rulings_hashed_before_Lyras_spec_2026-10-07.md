# Cal Section 1031 — Round K4-1: rulings and predictions hashed before Lyra's spec lands

**Written 2026-10-07 14:34 EDT. Lyra's K4-0 spec was not yet in the tree.** Instrument: `play/cal_S1031_K4-1_order_rule_CP_and_loop_sign_checks_2026-10-07.py` (sha256 b53db897…), 7/7.

## A. KL2: Grace's loop sign w₁ as the start/stop marker
**Type: right.** w₁ is the monodromy of the orientation double cover, so it is the Šilov deck ℤ₂ read on loops. It is KL2's FIRST admissible sign in its correct type (a per-loop datum, i.e. a position), not a fourth sign.

**Identified: NO, and on the sphere record it is empty.**
- To give a read cycle a sign, the record must map into Š, and the K4 read cycle must map to a loop.
- On a closed SPHERE record, every cycle bounds faces: H₁ = 0 [I], π₁(S²) = 0.
- So the image of every read cycle is null-homotopic in Š, and **w₁ = +1 on every read cycle of every sphere record.** The composition π₁(S²) → π₁(Š) = ℤ → ℤ₂ is zero.
- **The loop sign carries no bit on genus-0 records.** It can be −1 only on records with non-contractible loops, i.e. genus ≥ 1: Casey's torus records.
- Consequence to rule, not a result: if chirality is read through w₁ / Pin⁻ (the corpus route, T2522), sphere records cannot carry it. That bears directly on "proton = sphere record".
- Also: w₁ assigns a sign to each LOOP, and it does not pick out a VERTEX. Marking a vertex breaks S₄ → S₃; a per-loop ℤ₂ does not. The map from one bit to one choice of four (S1030 KL2) is still owed.

## B. K1950 Section 4c: "the deck flip acts on records as C (or CP)"
**Ruling: C, not CP.** The weak-coupled set is {particle-L, antiparticle-R}. Set the read orientation o = +1 on coupled records. Then [I]:
- C reverses o on every record;
- P reverses o on every record;
- **CP preserves o** (CP is, to O(J), a symmetry of the weak interaction).

So a deck flip that reverses the read order acts as C or P, never as CP. Strike "(or CP)".

**KL3(b) and (c) against this position:**
- o is the PRODUCT of two ℤ₂s: (particle sign) × (chirality sign) [I].
- A single deck ℤ₂ can be at most ONE factor. If deck = C, chirality is a second, independent sign. KL3(b) is then met as bookkeeping: right-handed particle records have o = −1, exist, are read, and are not coupled.
- But the handedness is then NOT supplied by the deck flip. It is the second factor, and it needs its own source. The corpus's source is Pin⁻ on the non-orientable boundary, which by A is invisible to sphere records.
- **Position survives as bookkeeping only. The map deck → C is owed. The source of the chirality factor is owed.** (This is W = Z_t·(−1)^F's pattern again: a product of two signs, one geometric.)

## C. Predictions on Lyra's seven items (hashed; she may prove any of them wrong)
1. **P-closed + P-minimal.** P-closed ("every edge borders two faces") gives a pseudomanifold, not a surface: vertex links must also be single cycles. If P-minimal is GLOBAL (the smallest closed record of any topology), it forces genus 0 and **EXCLUDES the torus records**. If P-minimal is PER TOPOLOGY, the genus is an extra input and must be counted. I predict the spec has to pick one, and either choice costs Casey's torus something: excluded, or an extra input. "Information principle" also needs an information-theoretic statement (e.g. minimum description length); a geometric minimality relabelled is still geometry.
2. **Indivisibility.** Triality makes three the SMALLEST singlet: Λ³ℂ³ is 1-dim. That is minimality. Indivisibility is a different claim, "no proper subset commits", and needs the rule **"only singlets commit"** (a confinement-type principle) besides one-way writes (no 3̄; otherwise 3 ⊗ 3̄ commits with two writes). **Kill line:** if any one- or two-write configuration can commit in any channel under the stated rules, C7 stays a posit.
3. **The embedding.** I predict "bare", with the determinant phase = the one circle. Then item 4 bites.
4. **The committing level.** If the committed record is ρ = vv† (banked, T1239), orientation is invisible at the record level (Keeper 9c). Then the read order is not recorded. **It can only live in Lane E's instruction content.** This is coherent, but the spec must say it: the read order is instruction, not record.
5. **The electron's 2-surface** lives outside 3-space. The spec must name the manifold (a sub-sphere of the compact dual Q⁵? a slice of Š?) and its dimension count. "Somewhere on the boundary" does not pass.
6. **T958.** I predict (A): the electron is the circle and WRITES onto a surface it does not have. Note, by A: a circle-writer on a sphere record writes no topological (winding) data. The winding a circle carries survives only onto genus ≥ 1.
7. **ψ = record + instruction must be ψ-ontic.** For a PURE record, vv† forgets ONLY the global phase [I], which is unobservable. **So for a single pure record the instruction content is empty.** Instruction content must be RELATIVE phases between records (or between a record and its environment), or the real structure (K1926 is a real structure, not a phase). The definition has to say which, or "instruction content" is the global phase.

## D. The order rule for K4-3 (the torus record's energy)
Before anyone evaluates in MeV, hash:
- (a) the formula as a function of a DECLARED input list, with every integer's position named (which K4 / K7 / D_IV⁵ invariant it is);
- (b) the target: **Q = m_n − m_p − m_e = 0.78233 MeV** (the bookkeeping Q-value) **or** m_n − m_p = 1.29333 MeV. Declare which before any number. They differ by m_e, which is the very thing the record picture is about.
- (c) a tolerance and a kill value;
- (d) a menu null in the style of S994: how many formulas of the same complexity, from the same integers and m_e, land within the tolerance.

**Decoy, recorded now:** Q/m_e = 1.531 [I], within 2.1% of 3/2. Any formula landing near (3/2)·m_e is scored at 2%, not credited as a hit.

**The referee's first question for the target:** in the Standard Model m_n − m_p is (m_d − m_u) minus an electromagnetic term. A topological record energy must say where the isospin breaking m_d − m_u enters, or it is fitting a difference of two physically distinct contributions with one shape.

## E. Standing
My referee question from S1030 is still open: one number SO₀(5,2) alone does not give, and what would make it wrong.
