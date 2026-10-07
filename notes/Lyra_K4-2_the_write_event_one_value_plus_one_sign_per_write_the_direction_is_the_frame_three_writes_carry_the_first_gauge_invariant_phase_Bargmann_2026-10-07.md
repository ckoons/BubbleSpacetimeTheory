# Lyra — Round K4-2, Lane A: the write event. One value plus one sign per write; the photon's direction is the frame, not data; three records are the fewest that carry a gauge-invariant phase (Bargmann)

**Lyra, Wednesday 2026-10-07, 15:33 EDT** (from `date`). Rubric cell: Internal C. Binding: K1951 Section 2, Cal S1032, the K4-2 prompt.
**didwe:** "Bargmann invariant geometric phase" → 0; "Pancharatnam phase" → 0; corpus grep → 0 files. New to the corpus; the mathematics is 1950s–60s prior art (pins below).
**Instrument:** scratch `k42.py`, SCORE 5/5 (reproduced in Section 6). No toy claimed. Elie's Lane B carries the E1 control and the module count.
**Status:** positions and one exact lemma (standard). Nothing here is read against a number.

## 0. Corrections accepted from Cal S1032 (antecedents restated)
- *"Lyra Addendum 1's 'RP² excluded by 2022 orientability (P-orient)' FAILS."* Accepted. The base ℝP⁴ refutes the premise. K6 stays caged by **P-loop-free** (a free loop carries a phase; a ℤ₂ loop carries only a sign), my Section 2 reason.
- *"'Read orientation, det phase and baryon number are ONE object': OVERREACH."* Accepted, restated as "live in one U(1)". The orientation is a value; B is a label.
- *"Section 990 DOES reach (D2) … K-C7c collapses into K-C7a."* Accepted. Positive time contributes nothing independent to C7.
- *"A PURE vv† keeps every relative phase in its off-diagonals."* Accepted. My (e2) was wrong; rewritten in Section 4.
- *"Name one more input: simplicial."* Accepted. The inputs are {P-closed (simplicial), P-minimal, P-transfer}.

## 1. Enumerate, before mapping (KL-W3 discipline)
**Photon, as it arrives (positive frequency):**
| dof | type | count |
|---|---|---|
| energy ω | real, > 0 | 1 |
| direction k̂ ∈ S² | real | 2 |
| helicity λ = ±1 | sign (physical states: 2, no longitudinal; pin-owed, Grace) | 1 bit |
| polarization coherence (a point on the Poincaré sphere; relative phase of λ = ±1) | phase | 1 real (with the amplitude ratio, 2) |
| overall phase | phase | 1 (unobservable) |

**Electron's circle (the writer, reading A):**
| dof | type | count |
|---|---|---|
| spin s_z | sign (two states) | 1 bit |
| circle phase θ | real | 1 |
| winding / angular momentum m | integer | 1 |
| charge sign = the read order | global sign (K1951 2c) | 0 per event (the same for every electron) |
| bound-state label (n, l) when bound | integers | 2 |

**The named breaking (KL-W2).** "Energy" is a value only as ω/m_e, and a discrete level spacing exists only for a bound state, which needs m_e and α. **The write event uses the breaking K1937 names: the ruler m_e, plus the identified α.** A conformally covariant account has no dimensionless energy to write. This is why the write event is where dynamics enters, and why this lane cannot be built from covariant structure alone.

## 2. What survives the write, and what is the frame
Apply C1 (a record holds no coordinates) to each input:
- **k̂ is the FRAME, not data.** It is the axis the absorption is quantized along. A coordinate-free record cannot hold two angles as values. It erases them into the choice of frame, and they reappear only in the exterior, as recoil.
- **Helicity survives as one sign.** Along k̂, absorption transfers Δm = λ ∈ {+1, −1}. **Only two values, not three**: the three Δm ∈ {0, ±1} of the E1 rule come from quantizing along an EXTERNAL axis, which is a coordinate. In the photon's own frame, Δm = 0 is absent (no longitudinal photon). So **KL-W3's "spin-1 has three states" and "three Δm values" are both frame artefacts at the write**, and neither 3 enters. (Elie's control still has to reproduce Δm ∈ {0, ±1} in the external frame; this item predicts it reduces to λ in the k̂ frame.)
- **Energy survives as one value**: the level difference, discrete when bound, in units set by the breaking.
- **The polarization coherence and the circle phase** are phases. Their fate is Section 4.

**Count per write: one one-dimensional value (the level index) + one sign (λ).** Can-fail: if a write also commits a direction (a record that stores k̂ as data), C1 fails for the write.

## 3. Keeper's candidate, 3-momentum + helicity: KILLED, with the reasons
- Two of its three reals are the direction, which is the frame under C1 (Section 2). They are not values.
- It is circular as an account of D = 3 (the prompt's second problem), and it contradicts "one word, one dimension" (the first).
- **What survives of it is the right shape at the right level:** one value + one sign **per write**, not per word.

## 4. The map: three writes plus a frame give K4's 4 vertices AND 6 edges
**Lemma (standard; Bargmann 1964, Pancharatnam 1956, Samuel–Bhandari 1988 — all pin-owed, Grace):**
- For two pure states, the only gauge-invariant quantity is |⟨1|2⟩|². The phase arg⟨1|2⟩ is gauge-dependent (checked).
- **For three, the Bargmann invariant B₁₂₃ = ⟨1|2⟩⟨2|3⟩⟨3|1⟩ has a gauge-invariant phase, generically nonzero** (checked). It is the geometric phase around the triangle.
- **For REAL states (real structure kept), arg B ∈ {0, π}: a sign only** (checked).

**Lane E rewritten (item 4).** *Instruction content = the gauge-invariant relative phases BETWEEN records: the Bargmann phases of record triples, plus holonomies of genus ≥ 1 records.* A single record carries none. Two records carry none. **Three is the fewest records that carry any.** Interference between records is these phases; interference inside one record lives in its own vv†, as Cal said. This is Cal's option "relative phases between records", made gauge-invariant.

**The map (positions; frame = the reference state of the write sequence, i.e. Casey's start/stop):**
| K4 element | count | what sits on it |
|---|---|---|
| value vertices 1, 2, 3 | 3 | the three writes' values (level indices) |
| frame vertex 0 | 1 | the reference state (start/stop) |
| frame edges {0, i} | 3 | write i's sign λ_i, relative to the frame |
| value edges {i, j} | 3 | the overlaps ⟨i\|j⟩ between writes (modulus gauge-invariant; phase gauge-dependent on its own) |
| faces | 4 | the four Bargmann invariants |

- **Closure, exact (checked):** with consistent outward orientation, the product of the four face invariants is real and positive. **So a closed record carries exactly 3 independent instruction phases, which equals K4's cycle rank 3.** P-closed is the consistency condition that ties the four faces together.
- **Caged on purpose:** "three independent phases = N_c" enters nothing without a map (K1949 Section 3's standing hazard).

## 5. What this does for indivisibility (C7): a second, independent route, as a position
- **(P-instruction)** A committed unit must carry gauge-invariant instruction content (otherwise it is only a list of separate records).
- **P-instruction + P-minimal ⇒ exactly three records** (the Bargmann lemma).
- The new route **ties back to K1926's one condition:** the Bargmann phase is continuous only when the real structure is forgotten (with real states it is a sign, check (4)). So **the unit of three carries a continuous instruction iff the commit forgets the real structure.** The two routes to C7 meet at the same open condition. That is good (one can-fail line still), and it is not yet a forcing.
- **Cal's KL-W3 will list this 3 too:** the triangle is the shortest cycle in any graph, so "3 = the fewest states with a loop" is generic. The BST content would be that the record forgets the real structure; the generic content is graph theory.
- **Kill line K-C7d:** if a gauge-invariant instruction is carried by two records (for example, with a fixed external reference state that the frame vertex smuggles in as a fourth record), P-instruction no longer needs three. Then the frame vertex must not count as a record, and the map must say why. **Can-fail count for C7: 2** (K-C7a, K-C7d).

## 6. The null (KL-W1, for Elie) and what is NOT forced
- **K3** (three writes, no frame) carries the Bargmann phase and the overlaps, but the three signs have no edge to sit on. They could sit on vertices as labels. **So the frame vertex is NOT forced by the count; it is allowed.** KL-W1 is partial: 3 is forced by {P-instruction, P-minimal}; the +1 is a posit (KL2 still open; Grace's loop sign is the candidate).
- **K5** (four writes + frame) carries more phases than the minimum. It is excluded by P-minimal, not by the count.
- **Instrument (scratch `k42.py`, 5/5):**
  - (1) arg⟨1|2⟩ is gauge-dependent;
  - (2) B₁₂₃ is gauge-invariant;
  - (3) arg B₁₂₃ ≠ 0 generically for complex states;
  - (4) real states give arg B ∈ {0, π};
  - (5) the product of K4's four outward face invariants is real and positive.

## 7. The K4-3 target, declared before any formula: **0.78233 MeV = m_n − m_p − m_e** (CODATA 2022, Grace/Keeper)
- **Reason 1 (the picture):** under reading (A) and Casey's ledger statement, the neutron is a proton record + the electron's circle + a neutrino residue. The electron is a CONSTITUENT, so its rest energy is not part of the assembly cost. The torus-assembly energy is the excess over constituents. The neutrino mass is below resolution here (pin-owed bound).
- **Reason 2 (the referee):** 0.78233 MeV is the β-decay Q-value, which sets the free-lifetime scaling (Sargent; Cal S1032). K-T3 compares against this quantity, so the target and the test are the same number.
- **Decoy stays caged:** 0.78233/m_e = 1.531, 2 % from 3/2.

## 8. Question for Casey (one)
In my map, **three writes make one K4 word**. You also said **three words make one 3D unit**. Is the indivisible unit (C7) the word (three writes) or the cell (three words)? Today's "three commitments/writes are an indivisible unit" reads like the word; "three K4 words confined form the 3D structure" reads like the cell. They may both be true at different levels. Saying which keeps the 3 from being counted twice.
