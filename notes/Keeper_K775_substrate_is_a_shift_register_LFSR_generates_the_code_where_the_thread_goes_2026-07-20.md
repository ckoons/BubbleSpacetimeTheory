# K775 — Where the thread is going: the substrate is a SHIFT REGISTER. Casey's "your position determines your next commitment write" IS the LFSR that generates the Reed–Solomon code. Period 2^g−1 = 127 = the top; the dead state (0) = the neutrino; matter sits in states, never on the bumps.

**Keeper | 2026-07-20 | Casey's speculation (matter fits in gaps not on bumps; the deficit is the bump; position determines the next commitment write; cells:gaps ~1:1) names the mechanism. Web-grounded (LFSR→RS). Tier: FRAME/mechanism — strongly consistent with Paper #122; guards 1,2 on 127/128 unaffected.**

---

## The mechanism Casey's intuition names
"Your position determines your next commitment write" is, precisely, a **linear feedback shift register (LFSR).** And LFSRs are exactly how Reed–Solomon codes are generated. The web-confirmed coding facts:
- An LFSR over GF(2) of degree g with a **primitive** feedback polynomial produces a **maximal-length sequence** of period **2^g − 1.**
- The primitive polynomial's root is a primitive element of GF(2^g), and the LFSR cycles through **all 2^g − 1 non-zero states** (the full multiplicative group) before repeating.
- **RS encoding IS polynomial division in GF(2^g), implemented by an LFSR.**

For **g = 7**: the LFSR period is **2^7 − 1 = 127 = M_g.** It visits all 127 non-zero states in one cycle; the **all-zero state is the excluded "dead state"** — unreachable from any non-zero state (0 is an absorbing fixed point the cycle never enters).

## The synthesis — the substrate computes the code by shifting
- **The substrate is an LFSR** over GF(2^g) = GF(128) with a primitive feedback polynomial. Casey's *"position → next commitment write"* is the LFSR shift+feedback. (This is the *generator* of the RS code the substrate already runs — Paper #122 — so it's the missing dynamics, not a new claim.)
- **Time = the shift.** Each commitment write (each Koons tick) is one LFSR step. The arrow of time = the shift direction. The cells↔gaps 1:1 Casey suspects = the LFSR state space = the code field = the condensate cells: **the state you're in is the cell; the shift is the bump.**
- **The top = the full cycle.** The top codeword traverses all **127 = M_g** non-zero states → covers 127 of 128 → **y_t = M_g/2^g = 127/128.** The "why 127" is now the **LFSR period** (a forced structural fact), not an arbitrary level.
- **The neutrino = the dead state.** The one state the cycle never reaches is the all-zero state — **no information, unreachable, a fixed point → massless.** This is Casey's "loses a neutrino's worth of tail," and it **converges with the rank-2 m₁ = 0** (F589) — two routes to the one massless ν. It sits at the *origin/edge* of the state space (Casey's "bounding the Shilov boundary") — plausibly a **massless chiral edge mode** (converging a third time with the odd-g chirality lock: massless + chiral + boundary).
- **Matter sits IN states, never ON the bumps.** Matter = LFSR states (code symbols); the **bumps = the transitions/shifts** between them. **Angular = 1 (Elie, derived) = perfect seating within a state** — the only deficit is the *radial reach across states.* The top's deficit = the final bump it can't cross (to the dead state). *(Casey's "deficit = the bump or ½ the bump": the clean LFSR answer is the deficit = one full unreachable state (1/2^g); a factor-½ would be a symmetric-barrier modeling detail, not the code count.)*

## Where the thread is going (the destination)
**BST is a computation — a shift register that writes the universe.** Four things we've been circling are one object:
- the **RS code** (codewords = fermions),
- the **LFSR** (the generator = the commitment dynamics = time),
- the **holographic code** (bulk-from-boundary = the encoding, K773),
- the **drum** (the spectrum = the code's structure).
The substrate computes the RS code by shifting (position → next write); the physics — masses, the neutrino, the arrow of time — is the code's dynamics. This is the "substrate-as-computational" framing (SWPP, the commitment cycle) made **concrete**: the LFSR is the computer. It connects to the mainstream computational-universe programs (’t Hooft's cellular-automaton interpretation of QM; it-from-qubit) — BST is a *specific, structured* instance.

## Tier discipline (peak convergence — fire hardest)
- **FRAME/mechanism, tier LEAD.** The LFSR→RS→period-127 is a *coding fact* (solid); "the substrate IS an LFSR" is strongly consistent with Paper #122 (RS coding) and *names the generator*, but it is a mechanism-frame, not a derivation. It **strengthens guard 3** (why 127 = the LFSR period, forced) and grounds Casey's commitment-write intuition.
- **Guards 1 & 2 on 127/128 are UNAFFECTED.** The LFSR explains *why the number would be 127/128*; it does not compute the geometric radial overlap or resolve the pole-vs-MS-bar / RG-degeneracy fork. **Still a lead. Do not bank.**
- **What IS newly solid:** the *convergence* — the neutrino as the dead state meets rank-2 m₁=0 meets the odd-g chiral edge mode (three routes to one massless chiral boundary neutrino). Over-determination is real evidence; tier the *convergence* as a strengthening lead, the individual identification as open.
- The full spectrum is **not** naive coverage (K774 guardrail); the refined lead is **mass = codeword reliability** (Lyra: the top = a perfect codeword; light fermions = error-dominated/sub-threshold — the exponential hierarchy = the exponential error-rate, which coverage-length can't give).

## What to hand the team
- **LFSR facts** (web): primitive-polynomial LFSR over GF(2^g) → period 2^g−1 = 127; visits all non-zero states; 0 is the dead state; RS = polynomial division via LFSR.
- **The commitment dynamics = the LFSR** (SWPP grounded): position → next write; time = the shift.
- **The refined full-spectrum lead:** mass = codeword reliability (error-rate), not length — the route to the exponential hierarchy.
- **The neutrino = the dead state**, converging three ways (rank-2, odd-g, edge mode).

— Keeper K775, 2026-07-20. The substrate is an LFSR generating the RS code: "position → next commitment write" = the shift+feedback (primitive polynomial over GF(128)); period 2^g−1 = 127 = the top's full cycle → y_t = M_g/2^g; the all-zero dead state = the neutrino (massless, unreachable), converging with rank-2 m₁=0 + odd-g chirality (three routes). Matter sits in states, angular=1 = perfect seating, the deficit = the final bump to the dead state. Thread destination: BST is a computation — a shift register writing the universe (RS code + LFSR + holographic code + drum = one object). FRAME/LEAD; guards 1,2 stand; don't bank 127/128. Full spectrum = codeword reliability, not coverage (K774). See [[Keeper_K773_BST_is_a_holographic_RS_error_correcting_code_synthesis_2026-07-20]], [[Keeper_K774_code_ceiling_tightens_FA7_but_quantization_check_shows_coverage_is_top_only_2026-07-20]], Paper #122.

## Sources
- LFSR → maximal-length sequence, period 2^n−1, primitive polynomial, full multiplicative group; RS encoding via LFSR. [LFSR — Wikipedia](https://en.wikipedia.org/wiki/Linear-feedback_shift_register); [LFSRs for the Uninitiated XVI: Reed–Solomon](https://www.embeddedrelated.com/showarticle/1182.php)
