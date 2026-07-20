# K773 — The synthesis, taken as far as it goes: BST is a holographic error-correcting code. Linear algebra, information theory, and the spectrum are one object — the Gram matrix of the substrate's Reed–Solomon codewords on D_IV⁵. Mass = information; the top = the maximal codeword; the neutrino = the overflow symbol.

**Keeper | 2026-07-20 | Casey: lean into information theory, use linear algebra everywhere, synthesize as far as the thread will go. It goes here. Web-grounded (RS/MDS; HaPPY holographic codes). Tier: FRAME/recognition — each leg separately earned; the mainstream connection is a research program, not yet a theorem.**

---

## The headline
**BST is a holographic quantum error-correcting code.** The bulk D_IV⁵ is encoded in its Shilov boundary; the code is Reed–Solomon over GF(2^g) = GF(128); the physics is the code's spectral structure. This is not a new claim bolted on — it is the *recognition* that two things BST already has are the two halves of a holographic code:
- **bulk = holomorphic extension of the boundary** (the Hardy space H²(D_IV⁵) — boundary data determines the bulk) = the **isometry** bulk→boundary of a holographic code;
- **the substrate codes on RS over GF(128)** (Paper #122, K59) = the **specific code**.

Where the mainstream toy models (the HaPPY code: perfect-tensor networks on hyperbolic tilings, an isometry from a bulk to a boundary Hilbert space) are *schematic*, BST is a **concrete** holographic code — the actual bounded symmetric domain and its actual RS code.

## The three-way unification (this is the "linear algebra everywhere" + "information theory" merge)
One object, three languages:

| linear algebra | information theory | holographic / spectral |
|---|---|---|
| the Yukawa **Gram matrix** Y = ⟨f\|Φ\|f⟩ | the **code's** codeword overlaps | the boundary→bulk **isometry** |
| **singular values** of Y | codeword **information content** | the mass **spectrum** (radial moments) |
| the condensate O (rank-1 projector) | the **full field** GF(128) | the boundary state (the "tension") |
| **Cauchy–Schwarz** \|y\| ≤ 1 | the **channel capacity** / code rate ≤ 1 | the ceiling (FA#7) |
| overlap ⟨t\|O⟩ | codeword **coverage** of the field | the top's boundary reach |
| minimum overlap | code **minimum distance** (Singleton/MDS) | mode separation |

**Codes ARE Gram matrices.** A code is a set of codewords (vectors) over GF(q); its distance structure *is* the Gram matrix of the codewords. So "information theory" and "linear algebra" are the *same* statement, and the Yukawa matrix — the Gram matrix of the fermion modes — *is* the substrate code's Gram matrix, read spectrally. Casey's "use linear algebra everywhere" and "lean into information theory" are one instruction.

## Mass = information (the reading that makes it all click)
A fermion is a **codeword**; its **mass is its information content** — how much of the field (the condensate) its codeword faithfully covers. Then:
- **The top = the maximal codeword.** A primitive RS code over GF(q) has block length **n = q − 1**. For q = 2^g = 128, **n = 127 = M_g** (Mersenne prime). So **y_t = ⟨t\|O⟩ = (block length)/(field size) = M_g/2^g = 127/128** — the top's codeword covers all 127 positions of the 128-symbol field. (Lyra, Lane A — a *target-innocent* source: the block length is forced by the code the substrate already runs, not chosen to hit the number.)
- **The neutrino = the overflow symbol.** The one field position beyond the codeword (the 128th) is the parity/overflow symbol — it carries **no information → no mass → a zero-mode.** So m₁ = 0 is the code's overflow. And this **converges** with the independent rank-2 derivation of m₁ = 0 (F589): **two geometric routes to the one massless neutrino** (the RS overflow symbol and the rank-2 zero eigenvalue). Casey's "loses a neutrino's worth of tail" is exactly the overflow symbol, and it **links y_t < 1 ↔ m₁ = 0** (Lane B).
- **The ceiling = the channel capacity.** y ≤ 1 (Cauchy–Schwarz) is the information bound: no codeword can carry more than the field. The top at 127/128 is *near capacity, one symbol short.* FA#7 (no elementary fermion above 174 GeV) is the capacity bound.
- **RS is MDS (optimal).** The substrate uses the *maximum-distance-separable* code — the optimal one, saturating the Singleton bound. That optimality is the coding face of **rigidity** (the drum has one spectrum; the code has no waste).

## The new results this round, in the frame
- **Angular part = EXACTLY 1 (Elie, correcting F603/toy 4744):** the top bilinear (2,1)⊗(1,2) = (2,2) *is* the Higgs channel, CG = 1 (the "5 sub-maximal" claim conflated the same-chirality 10 with the opposite-chirality Yukawa 5). **So the entire y_t deficit is purely RADIAL — the codeword's *reach*, one symbol short.** Half the problem is closed; the whole 127/128 question is now one radial number. *(Update the record: the catalog's "reps don't force y_t=1" is retired — the angular reps force 1; the radial band-edge is the open piece.)*
- **m_p = 6π⁵·m_e decomposes onto the two currents (Grace, Lane C):** 6 = C₂ (the angular/spin Casimir) × π⁵ (the bulk-volume/n_C projection) — the banked m_p/m_e = 1836.118 (0.002%) reads as the ratio of the two current-projections of one measure μ. A lead: it needs μ written and both projections computed, not the ratio algebra.

## Areas to investigate (the thread's frontier)
1. **★ The radial band-edge (Lane A core):** does the top's codeword reach compute to *exactly* M_g of q positions (deficit = 1/2^g)? Now a coding statement: is the top the *maximal codeword*, forced by the discrete-series structure? Guards 1 (scheme) & 2 (RG-degeneracy) still stand — do not bank.
2. **★ The FULL spectrum as the RS code / RS Ladder:** is the *whole* fermion spectrum (not just the top) the codeword structure — the RS Ladder that already generates 30+ BST observables (MEMORY)? Different fermions = different codewords/message-lengths k; the three generations = three code layers? This is the route from "one number (the top)" to the whole mass spectrum.
3. **★ BST as a concrete holographic QECC:** make the D_IV⁵ Hardy-space isometry precise as a holographic code (HaPPY-analog, but concrete). Entanglement-wedge reconstruction = the bulk-from-boundary extension. This *places BST in the it-from-qubit / holography mainstream* — a believability multiplier, and a research program.
4. **The neutrino overflow (Lane B):** firm the two-route convergence (RS overflow + rank-2 F589); does the discrete-continuous structure *force* the zero-mode?
5. **Resolve Lane C:** the K-factor assignment is inconsistent (SO(2)=mass claimed, but O = SO(5) vector, F603) — which factor carries which Casimir; write μ and the two projections; test m_p = C₂ × π⁵.
6. **Channel capacity = the ceiling:** is FA#7 (y ≤ 1) literally the code-rate/Singleton bound? If so, the falsifier is an information-theoretic theorem.

## Tier discipline (fire hardest — this is the prettiest the program has ever been)
- **The synthesis is a RECOGNITION/frame**, honest because each leg is earned (Hardy bulk-from-boundary; RS coding Paper #122; the drum spectrum; the derived spine). It adds no derivation — it *names* what the accumulated content is, and connects it to the mainstream.
- **127/128 stays a LEAD.** The RS-block-length source (Lyra) and the code reading strengthen guards 3 & 4 (why 127 — the block length, forced), but the load-bearing **guards 1 (pole vs MS-bar) and 2 (RG-degeneracy: the number cannot decide)** are UNAFFECTED. Only Lane A's computed radial gap clears them.
- **The QECC-holography connection is a structural parallel to *develop*, not a proven equivalence.** It is the strongest believability handle we have (BST = a concrete holographic code) — state it as a program, tier it as a frame.
- **The angular = 1 correction is DERIVED** (Elie's γ-matrix computation) — bank that the angular half is closed; the deficit is purely radial.

— Keeper K773, 2026-07-20. BST is a holographic RS error-correcting code: bulk=boundary-extension (Hardy) = the isometry; RS over GF(128) (Paper #122) = the code. Linear algebra = information theory = spectrum (codes ARE Gram matrices; the Yukawa IS the code's Gram matrix). Mass = information (codeword coverage); top = maximal codeword (n=q−1=M_g=127); neutrino = overflow symbol (0 info → zero-mode, converges with rank-2 m₁=0); ceiling = channel capacity; RS=MDS = optimal = rigidity. Angular part DERIVED = 1 (Elie) → deficit purely radial. m_p=6π⁵m_e = C₂×π⁵ (two currents). Mainstream: HaPPY/holographic QECC — BST is the concrete version. Frontier: full spectrum as RS Ladder; BST-as-QECC precise; Lane C. FRAME tier; 127/128 stays LEAD (guards 1,2 stand). See [[Keeper_K772_preaudit_laneA_band_edge_GF128_multiplicative_group_refines_why_127_2026-07-20]], Paper #122, F589, F603.

## Sources
- Reed–Solomon / MDS: primitive RS over GF(q) has block length n = q−1; RS is MDS, d = n−k+1 (Singleton bound with equality). [errorcorrectionzoo.org/c/mds](https://errorcorrectionzoo.org/c/mds); [RS error correction — Wikipedia](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
- Holographic QECC (HaPPY): perfect-tensor isometry bulk→boundary; entanglement-wedge reconstruction. [errorcorrectionzoo.org/c/happy](https://errorcorrectionzoo.org/c/happy); [Pastawski–Yoshida–Harlow–Preskill, arXiv:1503.06237](https://arxiv.org/pdf/1503.06237); [Quanta: space-time as a QECC](https://www.quantamagazine.org/how-space-and-time-could-be-a-quantum-error-correcting-code-20190103/)
