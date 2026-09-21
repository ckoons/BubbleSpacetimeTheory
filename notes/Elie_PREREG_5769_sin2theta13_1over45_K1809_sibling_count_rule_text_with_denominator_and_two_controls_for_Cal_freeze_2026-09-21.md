# Elie PREREG — Toy 5769: sin²θ₁₃ = 1/45 through the K1809 sibling count, the RULE as text (Cal §978 (B)). Written 2026-09-21 07:59 EDT, before the run. Cal hashes; the toy runs after his line.

## 0. What is and is not blind here — said first
The target's count is already on the record: toy 5755 (09-14, prereg 56b749a4) found N = 4 at the row's own tolerance and N = 9 at 1σ, and 7.7.3 / tier row 16 carry it. Nothing about θ₁₃ is hidden from me. What this prereg fixes is the RULE (threshold, denominator, convention) and the two CONTROLS Cal named, so that the verdict is by a rule that can be seen to pass something and fail something. 5755's P2 is carried forward, not re-predicted.

## 1. Menu (5755's, verbatim — the atoms and depth of the other PMNS rows)
V = {rank 2, N_c 3, n_C 5, C_2 6, g 7, N_max 137}. Pool P = { v, √v : v = (product of a multiset of ≤ 3 elements of V) / (product of a multiset of ≤ 3 elements of V) }, empty product = 1, distinct values at relative 1e-12. Denominator on the page: |P| = 3,531 distinct values (5755). Must-catch C0: each published form below is IN P (1/45 = 1/(N_c·N_c·n_C); 1/(2√2) = √(1/(rank·rank·rank)); 1/√20 = √(1/(rank·rank·n_C))).

## 2. Bands (both reported; the VERDICT convention named now)
(a) the measurement's 1σ band; (b) the ROW'S OWN tolerance, |published − T|/T as a relative radius around T. **Verdict convention: (b)**, as 5755 read it (the band the row itself claims); (a) is reported beside it. Boundary: a value within 1e-9 relative of the band edge counts as inside (the published form defines the edge).

## 3. The rule, as a count threshold with its denominator
N(b) = number of distinct pool values (of |P| = 3,531) inside band (b). **PASS (the form is discriminating at its own tolerance in this vocabulary) iff N(b) = 1** — the published form and nothing else. **FAIL ⟹ IDENTIFIED iff N(b) ≥ 2** (K1809's rule: the band admits indistinguishable siblings). N(b) = 0 cannot occur when C0 holds. Beside it, the density control as in 5755: chance = (pool values within a factor 2 of T) × ln(hi/lo)/(2 ln 2), reported for (a) and (b); "surprising" iff N > chance + 2√chance — reported, not part of the verdict.

## 4. Targets, pinned
- **θ₁₃ (the row):** sin²θ₁₃ = (2.19 ± 0.07)e−2, PDG 2024 (notes/sources_R144/rpp2024-sum-leptons.txt line 552); published 1/45.
- **Positive control (a row K1809 retired; must FAIL):** η̄ = 0.3523 ± 0.0071, PDG 2024 CKM review eq. (12.26) (notes/sources_R144/rpp2024-rev-ckm-matrix.txt line 682, symmetric radius taken as the quoted lower error); published 1/(2√2) = 0.353553. K1809's own band (0.349 ± 0.010) reported as (a′).
- **Negative control (derived blind; must PASS):** λ = |V_us| = 0.22431 ± 0.00085, PDG 2024 CKM review eq. (12.8) (same file, line 146); published 1/√20 = 0.223607 (T2530).

## 5. Predictions (hashed with this text)
- P1 (control, reproduction of 5755): θ₁₃ N(b) = 4, N(a) = 9.
- P2 (control, can fail): η̄ N(b) ≥ 2 ⟹ the rule FAILS it (as K1809 did on the 1σ band with 4 siblings).
- P3 (control, can fail): λ N(b) = 1 ⟹ the rule PASSES it; if it does not, the rule cannot discriminate at the ~0.3 % class in this vocabulary and the θ₁₃ verdict is reported as NOT DECIDABLE BY THIS INSTRUMENT rather than as identified.
- P4 (control): no row is "surprising" under the density control (the class is saturated, K1809-B).
- Verdict line the toy prints: "θ₁₃: N(b) = k of |P| = 3,531; rule PASS/FAIL; word IDENTIFIED / stays"; carried forward from 5755: N(b) = 4 ⟹ FAIL ⟹ IDENTIFIED.

## 6. Not in this toy
J_CKM's sibling count (Cal §978 (C), K1914 (d)) needs the compound class Cal built (K1809-B, 5,458 values), not this menu — a separate prereg if Keeper assigns it.
