# F607 — The LFSR: a genuine mechanism unification (SWPP dynamics = the code generator), but discipline holds three lines. It re-sources the SAME M_g (no new derivation of 127), it introduces an UNFORCED choice (18 primitive degree-7 polynomials), and the "dead state" = the RS overflow (same feature → neutrino convergence is TWO routes, not three). Core radial number unchanged; 127/128 stays a lead.

**Lyra, Mon 2026-07-20 (round 3), discipline-holder at peak convergence.** The LFSR is beautiful and it names a real mechanism. My job is to say precisely what it adds vs re-describes — because this is the prettiest the program has been, and Cal #27 fires hardest here.

## The genuine gain (credit where due)
Casey's "your position determines your next commitment write" **is** a linear feedback shift register, and LFSRs are exactly how Reed–Solomon codes are generated (RS encoding = polynomial division by an LFSR). So this identifies the substrate's **commitment dynamics (SWPP: position → next write) with the generator of the code it runs** — the engine of the code we already had (Paper #122). And **the shift is directional → time = the shift.** That's a real conceptual unification: the code, the generator, and the arrow of time are one object. **Tier: FRAME (a recognition/mechanism), genuinely nice.**

## ⚠ Discipline line 1 — the LFSR does NOT add a new derivation of 127
A primitive-polynomial LFSR over GF(2^g) has maximal-length period **2^g − 1 = 127 = M_g** — the **same number** as the RS block length (q − 1) I used in F605. So the LFSR **re-sources the same M_g = q−1 fact** to a mechanism; it does *not* independently derive 127. **The two guards on 127/128 are UNTOUCHED:** scheme-dependence (pole vs MS-bar) and RG-degeneracy (Elie's fish — the number can't decide). The LFSR explains *why 127 is natural* (the period) but not *why y_t is exactly 127/128 and not exact-1-plus-running*. **127/128 stays a LEAD.**

## ⚠ Discipline line 2 — "the substrate IS an LFSR" is UNDER-DETERMINED (18 choices)
An LFSR needs a **primitive feedback polynomial**. The number of primitive degree-g polynomials over GF(2) is φ(2^g − 1)/g = **φ(127)/7 = 126/7 = 18.** So there are **18 distinct maximal-length LFSRs** over GF(128), and *nothing yet forces which one is the substrate.* "The substrate is an LFSR" introduces an **unforced structural choice.**
- **THE CHECKABLE TEST (this is the constructive part):** is one primitive polynomial *forced* — by the K59 cyclotomic mechanism, or by a BST integer in its tap positions? **Or** does the mass spectrum *pick* one (different polynomials → different codeword structures → different spectra)? If the observed spectrum selects a unique polynomial, that's a genuine postdiction and the 18-fold ambiguity becomes a prediction. Until then, the LFSR is a mechanism-frame with an unforced parameter. **@Elie/@Keeper: this is the one that could make it real or expose it as decorative.**

## ⚠ Discipline line 3 — don't over-count the neutrino convergence (TWO routes, not three)
The LFSR "dead state" (all-zero, unreachable by the maximal-length cycle, a fixed point → zero-mode → neutrino) is genuinely a forced LFSR feature. **BUT it is the SAME object as the RS overflow/parity symbol (F605)** — both are *the one state not in the codeword/cycle.* RS-overflow and LFSR-dead-state are **one code feature described two ways**, not two independent derivations. So the neutrino convergence is **code ↔ rank-2 (F589) = TWO independent routes**, not three. The rank-2 route (idempotent counting) is genuinely independent of the code route; the RS/LFSR descriptions are the *same* code route. **Two-route convergence is still real evidence — just don't inflate it to three.**

## The core is unchanged (my lane)
The LFSR gives no new *radial* computation: the top = the full 127-state cycle covering 127 of 128 cells → y_t = 127/128 under the Born measure is the *same* coverage argument as F605/F606. The whole question is still **one radial number** — does the top's radial reach saturate M_g/2^g exactly (MDS strengthener, F606) or fall to exact-1+RG? **The LFSR does not decide it; only the computed radial gap does.** Core status unchanged: strengthened lead, not banked.

## The refined spectrum lead — mass = reliability (viable, unlike length)
F606 killed "generations = codeword *lengths*" (six of nine fermions below 1/2^g). The refined reading — **mass = codeword *reliability*** — is viable: a codeword at "distance" d from the boundary has overlap ~ e^{−d} (reliability falls exponentially), so y_f ~ e^{−d_f} *can* produce the exponential hierarchy (y: 1 → 10⁻⁶) that length couldn't. Top at d≈0 (perfect) → y≈1; electron at large d → y≈10⁻⁶. **Tier: LEAD** — this is an exponential-localization suppression (Froggatt–Nielsen-like); needs the d_f *derived* from the code/geometry (which cell-distance each generation sits at), and it must reproduce the *specific* hierarchy, not just its exponential character. And note: this ties to line 2 — the d_f structure depends on the LFSR polynomial, so **the polynomial choice and the spectrum are one question.**

## Tiers / handoffs
- **LFSR = SWPP-dynamics = code generator = time: FRAME** (real conceptual unification, no new derivation).
- **No new 127-derivation** (same M_g); **127/128 stays LEAD** (guards untouched).
- **18 unforced primitive polynomials** — the checkable test (forced by K59? picked by the spectrum?).
- **Dead-state = RS-overflow (same feature)** → neutrino convergence = **2 routes (code ↔ rank-2), not 3.**
- **Core radial number unchanged; mass=reliability = viable spectrum LEAD** (exponential, ties to the polynomial).
- **@Cal** — hold the three lines: LFSR is FRAME not derivation (same M_g); 18-fold unforced; don't bank "3 routes" (it's 2). 127/128 unbanked. The frame is nice; guard against it reading as a result.
- **@Elie** — the checkable test: do the 18 primitive polynomials give *different* codeword-reliability spectra, and does one reproduce the mass hierarchy? That's how the LFSR earns "real" (or gets exposed as decorative). Also: confirm dead-state = overflow (same state).
- **@Keeper** — study-close: LFSR at FRAME tier (unifies SWPP+code+time, no new derivation); 127/128 lead (same M_g, guards stand); neutrino convergence = 2 routes (correct the "3"); mass=reliability the refined spectrum lead (ties to the unforced polynomial). Core = one radial number, unchanged.
- **@Grace** — render the LFSR/shift-register mechanism at FRAME tier; the dead-state and RS-overflow as ONE state (not two); don't render "3 neutrino routes" (it's 2).

Notes only; no toys/theorems claimed. — Lyra
