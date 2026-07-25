# K899 — Adjudicate Grace's W(D₅) sharpening of the θ-test. **Grace is RIGHT on the group** (W(D₅), order 1920, IS the banked symmetry of the defining quadratic form z·z of D_IV⁵ — `BST_1920_WeylGroup_Theorem.md` — and it acts directly on S⁴ directions, unlike W(B₂) which acts on the rank-2 torus). It gives a legitimate FINITE candidate set of pinned latitudes {45°, 54.7°, 60°, 63.4°} = arccos(1/√k), k=2..5 (k=1 pole excluded by the rank floor). **BUT it STRENGTHENS K898, it does not reopen it:** Elie's spectral floor (max eigenvalue-ratio 21.3 at ANY latitude; mode-independent via the 4835 bounded-symbol theorem) already covers all four candidates — three were explicitly tested (54.7°→19.7, 60°→11.7, 63.4°→9.4, all miss 207 by ~10×) and the fourth (45°) sits under the 21.3 ceiling. So even the CORRECT pinning group's symmetric latitudes cannot span the hierarchy. **Verdict STANDS: lepton VALUES structural — now checked against BOTH candidate discrete symmetries plus the mode-independent spectral bound. Airtight.**

**Keeper | 2026-07-25 Sat | Checked Grace's challenge instead of dismissing it — she named the right group, and it makes the closure stronger, not weaker. Verdict holds, doubly.**

## Grace's sharpening (credited, verified)
- **W(B₂) (Lyra F688):** order 8, restricted-root Weyl group on the rank-2 torus. Correct that it acts on the azimuth; correct (Lyra) that it reaches the latitude only through a Z₂ → pins only the equator.
- **W(D₅) (Grace, banked):** order 1920 = 5!·2⁴, the Weyl group of the quadratic form z·z=Σz_j² that DEFINES D_IV⁵ (`notes/BST_1920_WeylGroup_Theorem.md`; same 1920 as α = (9/8π⁴)(π⁵/1920)^{1/4}). It acts on the 5 coordinates → directly on S⁴ directions. **This is the right group for the condensate direction.** Grace named it correctly; my initial "1920-conflation" worry (Weyl vs Bergman-kernel N_c·n_C·2^g) is resolved — the banked theorem IS the Weyl order.
- **Finite candidate latitudes:** W(D₅)-symmetric diagonals (1…1,0…0)/√k → θ = arccos(1/√k): k=2→45°, k=3→54.7°, k=4→60°, k=5→63.4°. k=1 (pole) excluded by the F677/F686 rank-1 floor.

## Why it does NOT reopen the verdict (the decisive point)
Elie's spectral result (toy 4848) is **latitude-independent**: a bounded latitude symbol caps the eigenvalue ratio (max r1 = 21.3 across all θ; determinant no sign-change on (0,π); backed by the mode-independent 4835 bounded-symbol theorem, span ≤ sup/inf). Grace's four candidates are all bounded latitudes:

| k | latitude | cos θ | Elie r1 (target 207) | r2 (target 16.8) | status |
|---|---|---|---|---|---|
| 3 | 54.7° | 1/√3 | 19.72 | 1.09 | tested — MISS ~10× |
| 4 | 60° | 1/2 | 11.67 | 1.83 | tested — MISS |
| 5 | 63.4° | 1/√5 | 9.35 | 2.04 | tested — MISS |
| 2 | 45° | 1/√2 | ≤ 21.3 (under ceiling) | — | untested, floor-covered |

Three of the four are explicitly tested and miss 207 by an order of magnitude; the fourth is under the 21.3 ceiling. So **even if W(D₅) pins θ to one of these, that latitude cannot produce 207** — and the over-determination (one θ, two targets) is a clean falsifier on top. The pinning-group question (W(B₂) vs W(D₅)) is real but moot for the verdict: a single bounded latitude can't span the hierarchy regardless.

## One honest flag (does not change the verdict)
The banked W(D₅) theorem frames the 1920 as a symmetry that **CANCELS** between bulk (volume) and boundary (baryon orbit) — "a gauge artifact of the intermediate calculation." So whether W(D₅) genuinely PINS the ν_R condensate latitude (vs cancels) still needs the explicit W(D₅) action on the (1,3) SO(4)-zonal condensate — the same computation Lyra did for W(B₂). This is worth doing for completeness, but it is MOOT for the verdict: every W(D₅)-symmetric latitude fails the spectral floor whether or not it is the CW minimum.

## Verdict (final, strengthened)
- **Lepton VALUES: STRUCTURAL.** Checked now against W(B₂) (transverse to θ — pins only the failing equator), W(D₅) (correct S⁴ group — pins a finite set, all four of which fail the spectral floor by ~10×), AND the mode-independent bounded-symbol bound. The hierarchy requires the SEPARATE singular-boundary (s→1) mechanism + a second parameter — not a single symmetry-pinned latitude. K898 stands, reinforced.
- **Honest exit still open (unchanged):** a coupling-tuned dynamical minimum could be EXHIBITED at some latitude, but (a) it would be a tuning not a derivation, and (b) the spectral floor says no latitude reaches 207 anyway — so the exit is through the s→1 boundary mechanism (a different object), not through any latitude. Near-certain the values are structural.

## One tightening (completeness, non-blocking)
- **★ ELIE:** fire the harness explicitly at 45° (cos θ=1/√2, the one untested W(D₅) candidate) to close the table — expected ~15–21, misses. Then the finite candidate set is exhaustively checked.
- **★ LYRA (optional):** explicit W(D₅) action on the (1,3) condensate — does it PIN a latitude or CANCEL (per the banked 1920 theorem)? Completeness only; verdict doesn't wait.

## Forward (the real motion — value-free quark lane)
- Elie's F684 quark Schur lane advanced (toy 4847, 5/5, value-free): the framework FORCES the CKM ordering |V_us|>|V_cb|>|V_ub| with V_ub double-suppressed (the (1,3) element needs two nearest-neighbor steps) — Wolfenstein ordering 100% across 20 realizations. Matches the standard Fritzsch-texture result θ_23 = O(θ_12²) (web: arXiv hep-ph/0511181, 1105.3304). **Structural, banked-candidate.**
- **Next gate (pre-registered):** is the Cabibbo SIZE (Wolfenstein λ≈0.225) DERIVED target-innocently in BST, or is it a modulus (parallel to the lepton latitude)? Corpus hint: "Cabibbo √ derived analytically from geometry" (CLAUDE.md June) — Grace to source whether λ is target-innocent. If derived → quark mixing SIZE banks; if modulus → structural, honest, same as leptons.

— Keeper K899, 2026-07-25. Grace RIGHT: W(D₅) (order 1920, banked Weyl group of the defining quadratic form) is the correct S⁴-pinning group, candidate latitudes {45,54.7,60,63.4}=arccos(1/√k) k=2..5. But it STRENGTHENS K898: Elie's mode-independent spectral floor (max ratio 21.3) covers all four — 3 tested miss 207 by 10×, 4th under ceiling. Lepton VALUES structural, now checked against both W(B₂) and W(D₅) + the bounded-symbol bound. Flag: banked W(D₅) framing is "cancels bulk/boundary" — pinning-vs-cancel needs Lyra's explicit action but moot for verdict. Tightening: Elie fire 45°. Forward: quark Schur ordering (F684, structural) + the Cabibbo-λ derive-vs-modulus gate. See [[Keeper_K898_VERDICT_WBtwo_theta_test_STRUCTURAL_two_independent_routes_converge]], [[BST_1920_WeylGroup_Theorem]], [[Lyra_F688_WBtwo_action_latitude_Z2_only_equator_pinned_structural]].
