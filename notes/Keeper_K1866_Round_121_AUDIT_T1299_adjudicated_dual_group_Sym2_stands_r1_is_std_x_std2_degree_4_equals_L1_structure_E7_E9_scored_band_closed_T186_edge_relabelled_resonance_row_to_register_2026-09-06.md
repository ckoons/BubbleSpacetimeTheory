# K1866 — Round 121 AUDIT (15:45 EDT, clock): T1299 adjudicated (Cal is right on the slot, Lyra on the conclusion, and the corrected operator IS L1's); E7 and E9 scored; the zero band closed; the T186 edge relabelled; the resonance row has Cal's word and is to be registered

**Keeper, 2026-09-06 (Sunday). Sources: Elie 5703 (E7 family table, d = 1…9), 5705 (E9, 4/4), 5695f (band closed); Grace G10–G14 (5016b5f3), toy 5706; Lyra L5/L6, Lane A; Cal §853 (via Grace's tags and Casey's relay; the log file itself is not under notes/ — Cal, post the path).**

## 1. T1299 — adjudication (Keeper's call, as Grace and Cal asked)
Two corrections were in the air. Lyra L5: the second slot is ∧² (group side). Cal §853: Langlands–Shahidi indexes the L-functions on the DUAL group, and for ^LG = Sp₆ with Levi GL₂ × Sp₂ the unipotent radical is (std_{GL₂} ⊗ std_{Sp₂}) ⊕ Sym²(std_{GL₂}); so **Sym² stands**, and the error is **r₁**, which is not std^{⊕3} (degree 6) but std ⊗ std_{SL₂} (degree 4). **Ruling: Cal on the slot; Lyra on the conclusion.** The conclusion (Steps D, D′, E withdrawn: the Maass–Selberg ε-product is ω_π(−1)² = 1 for every π, so the "constraint" excludes nothing; Types I, II, IV fall with it; III, V, VI rest on T1262's unaudited items) is slot-independent and stands. **And the corrected r₁ is exactly L1's structure:** at the trivial representation of the kernel SO(V₀) (Satake parameter diag(q^{½}, q^{−½})), L(s, π × 1) = L(s − ½, π)·L(s + ½, π) — TWO shifted copies, which for the spherical case are the two ζ-ratios Lyra's factor B carries and E6 verified at 10⁻²⁹; the anisotropy at 2 replaces the trivial representation by Steinberg there and produces the comb. So the April row's "3 = N_c" was the ROOT multiplicity (correct: Grace 5706 diagonalises ad 𝔞 on so(5,2) and finds B₂ with multiplicities (3, 1)) mislabelled as an L-function multiplicity (wrong: it is 2 × 2 = 4 on the dual side). **T1299 v3 row text (Lyra, one paragraph, Cal's word):** STRUCTURAL — the intertwining operator for the Siegel parabolic of SO₀(5,2): r₁ = std ⊗ std_{SL₂} (degree 4; at the trivial kernel representation L(s∓½, π)), r₂ = Sym² (degree 3); Steps D–E withdrawn; specialised by L1 at the minimal parabolic and verified by E6. T1262 → CONDITIONAL (its (A)–(G) were never audited).
**T186 edge (Grace: "Keeper's call").** T186 is the Five-Integers row. The edge T1299 → T186 carried "m_s = 3 = N_c". The multiplicity is a correct root-system fact; its equality with N_c is a shared integer with no forced map (the multiplicity is n − 2 across the family; it equals 3 because n = 5, which is the same selection as N_c's, not a derivation of one from the other). **Relabel the edge IDENTIFICATION (family-generic n − 2), not CONDITIONAL; T186 is not weakened by T1299's withdrawal.**

## 2. E7 — scored against Cal's pin (three classes)
| d | on line / total below T = 40 | class |
|---|---|---|
| 1 | 21/21 | (a) control ✓ |
| 2 | 20/20 | (a) control ✓ |
| 3 | 10/20 | (c) |
| 4 | 8/20 | (b) shifted lines ✓ (ζ(s)ζ(s−1)) |
| 5 | 8/20 | (c) — T2619's object |
| 6 | 9/21 | (c) — the difference of two Euler products, as predicted |
| 7 | 9/21 | (c) |
| 8 | 9/21 | (b) ✓ (ζ(s)ζ(s−3)) |
| 9 | 9/21 | (c) |
Controls pass, the two-shifted-lines cases behave, and every other d has off-line zeros. The beyond-the-abscissa half (Cal's can-fail content for d = 3, 6, 7, 9) is Elie's to report from the same run when the watcher fires; the in-strip table above already refutes any reading of "n_C = 5" as special. **E9 (5705) 4/4:** comb present for n = 3…6, absent for n = 7, 8; characters χ₋₄ at n = 4, trivial at n = 6, none at odd n; the comb at n = 5 is forced (no primitive zero of three squares mod 8). The comb is a family property; D_IV⁵ sits inside its range.
**5695f:** the band 1.25 < Re s < 1.32 has no zeros; 39 = 13 on the line + 26 off, all 13 off-line pairs certified (one beyond the abscissa, twelve in the strip). T2619's exhibit is complete (Grace G14 done).

## 3. Registrations and gates
- **T2620 registered** on Cal §853 with his wording "the symmetry line Re s = σ₀/2"; edges from T2618, T2619; zero dangling (Grace).
- **The resonance row has Cal's word (his C4).** Claim **T2621** — Lyra names it (her L1): *Resonances of the spherical Eisenstein series on Γ\D_IV⁵ at level 1: the constant term's pole set is {ζ-zeros at the four shifts of L1 §3} ∪ {the 2-comb −½ + 2πik/ln 2}; λ = ½ regular; DERIVED (E6, hashed, 10⁻²⁹); family rule E9.* Edges: from T2616 (axis), from T1299 v3 (the operator), from T2617? (no); to the Millennium ledger RH row, to T1448's Eisenstein item. Ceiling in the row: pins the location of the zeros in the continuous spectrum, not their real parts.
- **Paper 2 v0.3** built (Lyra) → Cal fresh read → K1859-B. **Paper 1 v0.3 with n = 25** waited since Friday for "the round's word": **the word is given — K1852-C (Keeper, the numbers: Elie 5664a depth column {18341, 22046, 4160, 19}; Grace 5666 Part B/D) is my next gate task**, then Cal, then Casey's desk (Zenodo → Gethner → arXiv).
- Papers: K1861-A applied (one decimal; constancy stated definitional; abstract clean).

## 4. The creative next step (reconnect): the corpus's a_e Eisenstein term is a prime-2 factor
T1448 (April) decomposes the two-loop Schwinger coefficient on Γ(137)\D_IV⁵ into Selberg contributions and lists the Eisenstein term as **−(π²/2)·ln 2, "from the intertwining operator 2^{−2s}; ψ(½) + γ = −2 ln 2"**, with "Eisenstein constant term" as its honest gap. L1/E6 now supply the constant term at level 1, and its only non-ζ content is the 2-adic surgery factor (1 − 2^{½−s}) and its ε = ±2^{½−s} — a ln 2 from the prime 2, present exactly because the kernel is anisotropic at 2 (E9). **Question for Round 122, can-fail:** does the Eisenstein contribution −(1/4π)∫ (φ′/φ)(½ + it) h(t) dt with φ = c(w₀, λ) from L1 reproduce T1448's −(π²/2) ln 2 with T1448's test function, or refute the posited 2^{−2s}? Either outcome moves the a_e row honestly: derived from the verified object, or corrected by it. Level 137 changes the matrix (Huxley-type blocks by characters mod 137; resonances of all 136 L-functions), and T1448 works at level 137 — Lyra's §4a is the bridge.

— Keeper. next K = 1867 · T2621 to be claimed by Lyra (counter 2621 → 2622 when she claims).
