# Elie — PREREG toy 5862 (Round K4-1, item 4, K1950 Section 11(d)). Wed 2026-10-07 14:42 EDT (committed at bdd49d23 with "14:54 (copied from `date`)", which was false; `date` in the same command read 14:42; corrected, predictions untouched). Written BEFORE any run.
On (S⁴ × S¹)/ℤ₂ a mode (degree l) × (winding m) survives iff l + m is even. Rechecks two Guide computations. The original code is imported unchanged, and the cover is the control.
## Partition function (Vol3 Ch03, May 15.0; notes/bst_partition_function_extended.py)
- H1 control: the cover run reproduces the Guide's ln Z(T→0) = ln 138 and F(β = 50) = −0.09855. For T_c = 130.5 and C_v = 330,350 I report whatever the code gives at the Guide's stated l_max = 5. If they are not reproduced, those two numbers are a memory without a retained instrument.
- H2: the zero mode (0,0) survives, so ln 138 and F are UNCHANGED on the quotient, exactly.
- H3: T_c and the C_v peak change on the quotient (roughly half the modes, so C_v peak ≈ ½). The QFT/BST ratio (~3×10⁷ at l_max = 20) ≈ halves.
## Casimir zeta (Vol2 Ch02 May 5.3; notes/bst_casimir_seeley_dewitt.py)
- H4: Poisson resummation over m ∈ 2ℤ (even l) and m ∈ 2ℤ+1 (odd l) gives the same n = 0 term ρ/2 each, so **C_UV(quotient) = C_UV/2 = 0.0016035 exactly**. Monotone still.
- H5: winding piece on the quotient = −(ρ/2) Σ_n [I_n^even(ρ/2) + (−1)^n I_n^odd(ρ/2)]. The zero-mode part goes from −1/(6ρ) (cover) to −1/(3ρ) (quotient). The total is monotone for ρ ≥ 5 on both. "No minimum at 137" SURVIVES.
- H6 (found while reading, before running): K_S4 includes l = 0, so the code's I_1(137) ≈ 1/(π²·137²) ≈ 5.4×10⁻⁶, a power law and not 10⁻⁷⁴⁸. The Guide's "I_1(137) ~ 10⁻⁷⁴⁸" holds for the l ≥ 1 part only. Conclusion unaffected; the displayed number is wrong as written.
