# Grace — Lead #85: pinning the electroweak generators in SO(5)×SO(2) (2026-08-07)

**Sequenced task (K1271): Grace + Lyra pin WHICH SO(5)×SO(2) generators are the electroweak ones BEFORE Elie/Keeper compute g′²/g² blind (Elie's gate: you can't compute a norm ratio without the generators). This is the SETUP — a candidate embedding + where the factor-2 must live — NOT the norm computation. Honestly a lead; Lyra's rep-theory confirms/corrects the embedding.**

## The target (settled, K1269/Cal)
Force **g′²/g² = N_c/(2n_C) = 3/10**, which is exactly **half** the GUT normalization N_c/n_C = 3/5. The whole gate is **one factor of 2**, and Casey's mechanism is the candidate: the "2" = the complex→real projection of the substrate.

## Candidate generator assignment (structural — my piece)
K = SO(5) × SO(2), dim 10 + 1 = 11. Electroweak SU(2)_L × U(1)_Y = dim 3+1.
- **SO(5) ⊃ SO(4)** (equal rank 2), and **SO(4) ≅ (SU(2)_L × SU(2)_R)/Z₂.** So the two SU(2)s live inside SO(4) ⊂ SO(5).
- **SU(2)_L** = one SU(2) factor of SO(4). Its three generators sit in the SO(5) Killing form with a definite length ⟨T_L, T_L⟩.
- **U(1)_Y = T_3R + (B−L)/2** (the standard hypercharge decomposition): **T_3R** from the *other* SU(2)_R ⊂ SO(4) ⊂ SO(5); **(B−L)** from the **SO(2) factor** — the compact isotropy axis that carries the complex structure (this is the SO(2) I exhibited in Row 2 as the time-circle / and that carries the Bekenstein 1/4).

## Where the factor-2 must live (the hypothesis to test, NOT claimed)
Couplings normalize inversely to generator length: g² ∝ 1/⟨T_L,T_L⟩, g′² ∝ 1/⟨Y,Y⟩, so **g′²/g² = ⟨T_L,T_L⟩/⟨Y,Y⟩**, and the target needs **⟨Y,Y⟩/⟨T_L,T_L⟩ = 2n_C/N_c = 10/3.**
- With Y = T_3R + (B−L)/2 and T_3R sharing SO(4)'s norm with T_L, the T_3R piece contributes an O(1) (GUT-like) part → the **GUT ratio N_c/n_C = 3/5** comes from the SO(4) (real) sector alone.
- The extra **factor of 2** (3/5 → 3/10) must come from the **(B−L) piece living on the SO(2)** — the complex-structure axis. If the SO(2) axis enters the *real-form* Killing norm with the complex→real doubling (⟨B−L, B−L⟩ picks up a factor 2 because SO(2) is the complex direction projected to real), then ⟨Y,Y⟩ doubles → g′²/g² halves → **3/5 → 3/10.** That is Casey's projection = the doubling, made concrete as a norm on the SO(2) axis.

## Honest status + what's owed
- **Setup only.** I've pinned the *candidate* generators (SU(2)_L ⊂ SO(4); Y = T_3R + (B−L)/2 with B−L on the SO(2)) and localized the factor-2 to the SO(2)-axis norm. I have **not** computed ⟨Y,Y⟩/⟨T_L,T_L⟩ — that's the blind Elie/Keeper step.
- **Lyra's confirmation needed:** (1) that SU(2)_L is genuinely the SO(4) factor and not a twisted combination; (2) the exact B−L generator and whether it lies purely on the SO(2) or mixes; (3) the precise complex→real normalization convention for the SO(2) axis (this IS the factor-2 — pin it to the source, don't assert).
- **Guard (peak-convergence):** the factor-2-from-projection is *elegant*, which is the danger signal — it must fall out of the norm computation **un-tuned and blind**, not be inserted because it's the number we need. If it forces, 3/13 earns Derived through Casey's mechanism; if the SO(2) axis doesn't carry the doubling, the mechanism was a heuristic and we say so.

## Cross-link
Ties Row-2 (SO(2)=time/complex-structure), Bekenstein-1/4 (SO(2) center), and now Weinberg (SO(2)=B−L/projection axis) — three physical roles for the one SO(2). If the norm computation lands, that convergence is real; until then, one object, three candidate roles. Nothing pushed.

## UPDATE 2026-08-07 — my component-flag QUANTIFIED (resolves toward Elie; sharpens the test)
Keeper flagged the tension: does the factor-2 double the WHOLE substrate leg (Elie) or just the (B−L)-on-SO(2) component (my earlier worry)? Worked out with generator norms (a = ⟨T_L,T_L⟩=⟨T_3R,T_3R⟩ SO(4) sector; b = ⟨B−L,B−L⟩ SO(2), fixed by the GUT anchor g′²/g²=3/5 ⇒ b=8a/3):

| reading | g′²/g² | sin²θ_W | |
|---|---|---|---|
| GUT (no doubling) | 3/5 | **3/8 = 0.375** | the normalization BST rejects |
| **WHOLE doubles (Elie)** | 3/10 | **3/13 = 0.2308** | ✓ BST value |
| COMPONENT doubles (my flag) | 3/7 | **3/10 = 0.30** | ✗ misses ~30% |

**Resolution:** the two readings give DIFFERENT, falsifiable predictions. Only WHOLE-substrate doubling gives 3/13; component-only gives 0.30 (a miss). So my component-flag, worked out, **resolves toward Elie's reading** — the honest object is the whole-substrate dimension count (n_C complex → 2n_C real), not a per-generator decomposition. I'm not clinging to the flag; the arithmetic points the other way. **But the flag earns its keep:** it turns the ×2 into a SHARP test with a concrete falsifiable alternative — the blind norm computation must yield WHOLE-doubling (→3/13); if it comes out component-only (→0.30), the mechanism is falsified. Either outcome is decisive. This is the stricter test Keeper wanted, now with numbers.
