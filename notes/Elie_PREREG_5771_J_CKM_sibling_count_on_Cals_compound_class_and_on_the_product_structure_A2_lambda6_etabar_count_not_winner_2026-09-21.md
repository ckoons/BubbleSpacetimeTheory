# Elie PREREG — Toy 5771: J_CKM = √2/50000 sibling count, (I) on Cal's compound class (K1809-B / Cal §705), (II) on the product structure A²λ⁶η̄ (Keeper round-2 item 8: "J is a function of four rows, its count is the product structure"). Written 2026-09-21 09:02 EDT, before the run. Cal hashes; Cal may AMEND the class's exponent range at the hash (his instrument was scratchpad; see §1). Report the count, not the winner (Lecture 7:68).

## 0. Target, pinned
J = 3.12 (+0.13 / −0.12) × 10⁻⁵, PDG 2024 CKM review, the sentence after eq. (12.26) (notes/sources_R144/rpp2024-rev-ckm-matrix.txt line 734). Published form (T-line / K1809 table): J = √rank/(rank⁴·n_C⁵) = √2/50000 = 2.828427e−5 — 9.35 % below T, z = −2.4σ on the lower error. Wolfenstein rows, same source, eq. (12.26) lines 680–682: λ = 0.22501 ± 0.00068; A = 0.826 (+0.016/−0.015); ρ̄ = 0.1591 ± 0.0094; η̄ = 0.3523 (+0.0073/−0.0071). Also reported as (a′): K1809's band 2.77 ± 0.11 e−5, the one Cal counted on (41 in band, chance 35.7).

## 1. Instrument I — Cal's compound class, rebuilt from his text
Numerator ∈ {1, a, √a, a·b}; denominator c^d · e^f; a, b, c, e ∈ V = {rank 2, N_c 3, n_C 5, C_2 6, g 7, N_max 137}; **d, f ∈ {0,…,5}** — the smallest range that contains the published form's own denominator 2⁴·5⁵ (must-catch C0). Distinct values at relative 1e-12; |P| printed. **Calibration done before this text, stated:** no exponent range reproduces Cal's 5,458 (0..4 gives 4,994, 0..5 gives 7,196, with the a·b / c≠e variants swept); his script (jsweep.py) was session scratchpad and is not on disk. The pool-size reproduction is therefore a control that will MISS by convention unless Cal names his range at the hash; the RANK-type statistics (count vs chance) are what carry over, as K1813 held for 5457.
Bands: (a) the PDG 2024 1σ band [3.00, 3.25]e−5 (asymmetric errors used as printed); (a′) K1809's 2.77 ± 0.11; **(b) the row's own tolerance, 9.35 % relative radius around T — the verdict convention**, as 5755/5769. Rule (5769's): PASS iff N(b) = 1; FAIL ⟹ IDENTIFIED (K1809: retire) iff N(b) ≥ 2. Density control as 5755: chance = (pool values within ×2 of T) × ln(hi/lo)/(2 ln 2); "surprising" iff N > chance + 2√chance, reported not ruling.

## 2. Instrument II — the product structure
J_W = A²·λ⁶·η̄ at Wolfenstein leading order — the corpus's own form is exactly (4/5)²·(1/√20)⁶·(1/(2√2)) = √2/50000, so this is the order at which the claim was written. Row sibling sets from the 5755 menu (products/ratios of ≤ 3 of V, with and without √, |P| = 3,531): S_λ = pool values inside λ's 1σ band; S_A inside A's; S_η̄ inside η̄'s. Count N_tri = #{(l, a, e) ∈ S_λ × S_A × S_η̄ : a²l⁶e ∈ J's band}, for bands (a) and (b); |S_λ|, |S_A|, |S_η̄| printed. Must-catch check C1 (stated as a prediction, since I can read the pins now): the corpus's triple (1/√20, 4/5, 1/(2√2)) — 1/√20 = 0.22361 is −2.1σ from λ's PDG 2024 value and 4/5 is −1.7σ from A's, so the corpus's J form is a product of three forms two of which are OUTSIDE their rows' 1σ bands today; its J lands 2.4σ low for that reason. Saturation line: N_loose = #{triples from the whole pool with l ∈ [λ/2, 2λ], a ∈ [A/2, 2A], e ∈ [η̄/2, 2η̄] : a²l⁶e ∈ J's (a) band} — how many BST-integer triples make J at all.

## 3. Predictions
- P1 (control): C0 — √2/(2⁴·5⁵) is in pool I.
- P2 (control, reproduction by convention): on (a′) N ∈ [25, 60] (Cal: 41 on his pool).
- P3 (can fail): N(b) ≥ 2 ⟹ FAIL ⟹ IDENTIFIED. I expect tens.
- P4 (can fail): N(a) ≥ 2 at the PDG 2024 1σ band.
- P5 (control): nothing surprising under the density control (Cal: J saturated).
- P6 (can fail, product structure): the corpus's triple is NOT in S_λ × S_A × S_η̄ (λ and A out of band).
- P7 (can fail): N_tri(a) ≥ 1 — at least one all-in-band triple makes J in band.
- Output lines: "J: N(b) = k of |P|; N(a) = …; rule FAIL/PASS; word IDENTIFIED/stays"; "product: |S_λ|·|S_A|·|S_η̄| = …, N_tri(a) = …, N_tri(b) = …, N_loose = …". **No form in any J band is printed; the lists go to play/.record_5771.json only** (report the count, not the winner).
