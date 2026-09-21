# Lyra — ITEM 7, my half: where does 6π⁵ live? Enumeration of the three mechanism sentences from their own inputs; T187's sketch RETIRED; the chapter's a₁ is a NAME; the June reading written as an operator statement is a RELABELING with one unbanked step; the residual's order stated as naturalness, not derived. READINGS, NOT RULINGS — Cal hashes the input list.
**Lyra, 2026-09-21 (Monday), 09:09 EDT (clock). On Casey's hand-out of K1915 Sections 2–3 and Elie's 5770 (the three sentences evaluated from their inputs: none computes 6π⁵). Numbers from the corpus; the measured ratio was read by K1915 before this note and is quoted only in Section 5.**

## 1. The inputs of every mechanism sentence (Cal: this is the list to hash)

| sentence | site | inputs named by the sentence | inputs actually banked | what the arithmetic gives |
|---|---|---|---|---|
| S1 "ratio of Bergman zero-mode densities K_Q⁵(0,0)/K_Q³(0,0) … from the volume ratio" | T187 proof sketch, `notes/BST_AC_Theorems.md:6592–6596` | Vol(D_IV⁵) = π⁵/1920; Vol(D_IV³) = π³/24 | Hua: Vol(D_IV^n) = π^n/(2^(n−1) n!) — both banked (T2403: K(0,0) = 1920/π⁵) | π²/80 = 0.1234 or 80/π² = 8.106. A density is 1/volume and carries π^(−n); a ratio of two densities carries π^(−2). **No reading of S1 produces π^(+5).** |
| S2 "a₁(D_IV⁵) = C₂·π^(n_C) = 6π⁵, the Seeley–DeWitt coefficient of exp(−tΔ_B)" | Vol 2 Ch 6 :35, :43–45, :61–67 | Δ_B the Bergman Laplacian; Faraut–Korányi | the corpus's own heat-trace for that operator (K204, toy 3661, 2026-05-31): a₀ = (N_c n_C)² = 225 = c_FK π^(9/2); **a₁ = −N_c n_C⁴ = −1875** | a₁/a₀ = −1875/225 = **−25/3 = R/6 with R = −p·dim_ℝ = −5·10 = −50** — the textbook Seeley–DeWitt a₁ = (1/6)∫R for the scalar Laplacian of the Bergman metric normalised Ric = −p·g, p = genus = 5 (toy 3661's own normalisation). So toy 3661's a₁ IS the coefficient of the operator the chapter names, and it is negative and rational. **The chapter's "a₁ = 6π⁵" is not the coefficient of any operator; it is the target with the letter a₁ written beside it.** |
| S3 "(n_C+1) cells × π^(n_C) bulk volume" | T2487 + T2488 (2026-06-07) | n_C + 1 = 6 = C₂ (cell count, T2488, anchored on T185's Z₂ bit); π^(n_C) = the π-exponent of Vol(B^(2n_C)) = π⁵/5! (T2487) | both factors banked; the step "π-exponent" strips the rational part | 6 × [π⁵ with 1/120 (ball) or 1/1920 (Lie ball) discarded]. See Section 3. |

Elie's 5770 evaluates each from its inputs and gets the same three results; nothing here depends on the measured ratio.

## 2. S1 — what π²/80 would have to mean, or retire

For S1 to mean 6π⁵ the "density ratio" would have to be Vol(D_IV⁵)·(6·1920)/1 — i.e. the numerator's density inverted into a volume and multiplied by 11,520, a rational that no banked object supplies. There is no such reading. Densities of holomorphic zero-modes on the compact duals Q⁵, Q³ (dim H⁰(Q^n, O(1))/Vol(Q^n) = 7·60/π⁵ and 5·3/π³) give 28/π², also π^(−2). **Reading: RETIRE T187's proof sketch.** The theorem row's identification survives at the 26-table's word (region-matched, K1673); its "Proved (depth 1)" label rests on this sketch and should be re-labelled by Keeper. This retires a sentence I wrote.

## 3. S3 written as linear algebra on D_IV⁵ — and what it is

Casey's standing order: element, eigenvalue or grading of one operator on H²(D_IV⁵). Written out:

- **What 6 is.** 6 = n_C + 1 = g − 1 is (a) the quadratic Casimir of the vector representation **7** of SO(7) = SO(g), which is (b) the first Laplace eigenvalue λ₁ of the compact dual Q⁵ = SO(7)/SO(5)×SO(2), and (c) the number of Schubert cells of Q⁵ = its Euler characteristic χ(Q⁵) (n odd ⟹ χ = n + 1). **Why (a)–(c) are equal:** each counts the g − 1 = 6 directions transverse to one fixed vector of ℂ⁷ — the Casimir of the vector of SO(N) is Σ_(j≠1) 1 = N − 1; the Bruhat cells of the quadric in ℙ^(N−1), N odd, are one per even dimension, N − 1 of them. That is the Grand Identity (T190) with its reason. **Where it lives: on the compact dual, as an eigenvalue of the SO(7) Casimir.** It is NOT an eigenvalue of any operator on H²(D_IV⁵) that I can name — on H² the Casimir of so(5,2) on the ν = 5/2 Hardy space is ν(ν − n) = −25/4, rational, and the SO(5) Casimir on the first K-type is 4. The chapter's "C₂ = 6 the lowest non-trivial Casimir eigenvalue of the substrate" is the compact dual's number.
- **What π⁵ is.** π⁵ is the transcendental part of 1/K(0,0): K_(D_IV⁵)(0,0) = 1920/π⁵ (T2403), i.e. Vol(D_IV⁵) = π⁵/1920 — an **element** (the reproducing kernel evaluated at the origin), banked. Equivalently Vol(B¹⁰) = π⁵/120 with a different rational. The rational is not optional: it is |W(D₅)| = 2⁴·5! = 1920 for the Lie ball (an identity, Vol(D_IV^n) = π^n/|W(D_n)|; noted, not used — the group here is B-type).
- **The product.** 6π⁵ = 6 · 1920 · Vol(D_IV⁵) = 11,520/K(0,0) = 6!·Vol(B¹⁰). To make 6π⁵ an operator quantity one needs an operator whose trace or eigenvalue is a volume times exactly 6·1920 (or a ball volume times 6!). S3 supplies the 6 (compact dual) and the π⁵ (kernel at the origin) and **strips the 1920 by hand**. That strip is the one unbanked step, and it is the whole content.
- **Why it is not a mass ratio.** Nothing in S3 assigns a dimension to either factor: 6 is dimensionless, Vol is a volume in the Bergman coordinates, and m_e enters only as the ruler (26-table row 1, input). A ratio of two masses needs two operators, one per particle, on the same space; S3 has one integer and one volume. The chapter's "proton = full-theory mass gap λ₁, electron = elementary radiator" names the two but writes no operator for the electron.

**Verdict on S3: a relabeling.** Both factors are banked objects; the product is not the element, eigenvalue or grading of any operator on H²(D_IV⁵) or on the compact dual; the rational 1920 (or 120) is discarded without a mechanism. Casey asked that this be said plainly if it is so: it is so. 6π⁵ stays IDENTIFIED (5768: SPECIAL at 1 in 19, K1815 — the number survived its null, the mechanism did not appear). No survivor computes 6π⁵ from banked objects with the ratio unread.

## 4. What would be a mechanism (the door, named, not opened)

An operator on H²(D_IV⁵) whose lowest eigenvalue or trace is 11,520·Vol(D_IV⁵) — e.g. a weighted trace over the six cells of the compact dual of the kernel at the origin with a weight the Z₂ bit fixes at 1920 per cell. I have no such operator; the 1920 = 2⁴·5! is the count that a mechanism must produce, and until one does, "six cells times one bulk volume each" is bookkeeping.

## 5. The residual as an order — stated as what it is

CODATA 2022: m_p/m_e = 1836.152673426(32). 6π⁵ = 1836.118109. Relative residual +1.882 × 10⁻⁵ (K1915). Casey asked which power of α (or 1/N_max) the first correction carries, and why, before anyone computes a coefficient. **Honest answer: no surviving mechanism exists (Sections 2–3), so no order is derivable today; the only statement available is naturalness, which reads the residual and is therefore not a derivation:** the claim "first correction at order α^k" is the claim c_k = residual/α^k = O(1); c₁ = 2.6 × 10⁻³, c₂ = 0.35, c₃ = 48 — only k = 2 is O(1). I record α² (= 1/N_max² in the program's reading) as the SELECTED order with that reason and no other, and I flag that c₂ = 0.353 is 6 % from 1/N_c, which at the measurement's 1.7 × 10⁻¹¹ precision is a 10⁵σ exclusion of α²/N_c as the exact correction: **the bait Keeper named is already dead as an exact term.** Nothing here is sealed; there is nothing for Elie to compute blind until a mechanism supplies a next term.

## 6. Applied to the chapter (Casey's two edits, done)

Vol 2 Ch 6: Lenz 1951 credited beside the formula; "below one in ten thousand" replaced by 5768's one in nineteen with the toy and rule named. No other line touched; the head-note regime (Keeper 09-19) stands.

— Lyra. Readings for Cal's hash and Keeper's read; nothing gated by me.
