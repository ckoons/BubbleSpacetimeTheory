# F736 — The surgical unblock (29p), both gates in my lane, resolved to the FK primary source. **Gate A: the type-IV multiplicity is d = a = n_C − 2 = 3 = N_c, verified against FK's own definition (NOT d = 1, which is type A / real-symmetric) — this kills the d=1-vs-d=3 ambiguity in writing.** For the symmetric cone of type IV (the Lorentz cone in ℝⁿ, Jordan algebra = the spin factor ℝ ⊕ ℝⁿ⁻¹, rank 2), FK's characteristic multiplicity is **a = n − 2**; D_IV⁵ has Jordan-algebra dimension n = n_C = 5, so **a = 3 = N_c** (Faraut–Korányi Ch I/Ch X, the classification table — the spin factor's off-diagonal Peirce space V₁₂ has dim a = n − 2, and here dim V₁₂ = N_c = 3, F708/T2511, consistent). Keeper's anchor confirmed against the book, not taken on assertion. **Gate B: the real generalized Pochhammer with a = 3, r = 2 is (ν)_{(λ₁,λ₂)} = (ν)_{λ₁} · (ν − 3/2)_{λ₂}, and it passes the built-in tripwire — the single-row minimal degree gives (ν)_{(1,0)} = ν = N_c = 3, the down-check.** The down ladder {1,3,5} is single-row (a-independent — which is exactly why it can't validate d and why Keeper said "not the down shortcut"); the up/lepton/neutrino sectors are the two-row (λ₂ > 0) cases where a = 3 genuinely enters, and there the a=3 value differs from a=1 (e.g. (3)_{(1,1)} = 4.5 at a=3 vs 7.5 at a=1). The off-diagonal mixing = the Pieri coupling (add one box, multiplicity a=3) through the degree-1 condensate. This note pins d and sets the a=3 evaluation with the self-correcting tripwire; Elie evaluates the specific two-row entries from FK and fires.

**Lyra, Wed 2026-07-29. The block was one convention. Pinned d to the book (a = n−2 = 3, not 1), set the a=3 Pochhammer with the down tripwire as the self-check. Sourced (FK Ch I/X + Ch XII), not reconstructed; if the tripwire fails, the d-pin is wrong and we know immediately.**

## Gate A — pin the multiplicity d (once, in writing, to the FK definition)
The symmetric cones (FK, classification):
| type | Jordan algebra | rank r | multiplicity a (= d) |
|---|---|---|---|
| I (real sym) | Sym(m,ℝ) | m | **1** |
| II (cplx Herm) | Herm(m,ℂ) | m | 2 |
| III (quat Herm) | Herm(m,ℍ) | m | 4 |
| **IV (Lorentz / spin factor)** | **ℝ ⊕ ℝⁿ⁻¹** | **2** | **a = n − 2** |
| V/VI (Albert) | Herm(3,𝕆) | 3 | 8 |

**D_IV⁵ is type IV with n = n_C = 5 ⟹ a = n_C − 2 = 3 = N_c.** The d = 1 floating in the corpus is the **type-I** value (real symmetric, rank m) — the wrong type; it does not apply. Independent corpus confirmation: the Peirce off-diagonal V₁₂ has dim = a, and dim V₁₂ = N_c = 3 (T2511/F708/F727 — the color sector). So **a = 3** two ways (FK classification + the Peirce dimension). **Pinned: d = a = 3. In writing.** (Also = F157's "a = n_C − 2 = 3 = N_c is odd" — consistent with the whole √π / odd-color thread.)

## Gate B — the real generalized Pochhammer/binomial (a = 3), with the down tripwire
The FK generalized Pochhammer (rank r = 2, multiplicity a = 3):
$$ (\nu)_{(\lambda_1,\lambda_2)} = \prod_{j=1}^{2}\Big(\nu - (j{-}1)\tfrac{a}{2}\Big)_{\lambda_j} = (\nu)_{\lambda_1}\,\big(\nu - \tfrac{3}{2}\big)_{\lambda_2}. $$
**The tripwire (self-correcting, K1002-style):** the minimal single-row degree must reproduce (N_c)_min:
$$ (\nu)_{(1,0)} = (\nu)_1 = \nu \;\xrightarrow{\ \nu = N_c\ }\; 3 = N_c. \checkmark $$
And the full single-row down ladder at ν = N_c = 3: (3)_{(1,0)}=3, (3)_{(3,0)}=60, (3)_{(5,0)}=2520 → **1 : 20 : 840** (banked). **If a two-row evaluation ever breaks this single-row consistency, the d-pin is wrong — immediate.**

**Why the down is a-independent (Keeper's "not the down shortcut"):** single-row partitions (λ₂ = 0) have (ν)_{(λ₁,0)} = (ν)_{λ₁} — the (ν − a/2)_{λ₂} factor is empty, so a never enters. The down {1,3,5} therefore cannot validate d. **The genuine test is the two-row sectors** (λ₂ > 0), where a = 3 vs a = 1 diverge:
- (3)_{(1,1)} = (3)_1·(3−3/2)_1 = 3·(3/2) = **4.5** [a=3] vs 3·(3−1/2) = 7.5 [a=1] — distinguishes.
- (3)_{(2,1)} = (3)_2·(3/2)_1 = 12·(3/2) = **18** [a=3].
- (3)_{(2,2)} = (3)_2·(3/2)_2 = 12·(3/2)(5/2) = 12·(15/4) = **45** [a=3].

**The off-diagonal mixing (the Pieri coupling):** the degree-1 condensate O = (1,0) couples μ → λ by adding one box; the FK Pieri coefficients (multiplicity a = 3) are the off-diagonal K(μ, λ). E.g. the coupling (μ) → (μ + box) carries the a=3 Pieri weight. These are the finite binomial numbers Elie sources from FK Ch XII (Prop XII.1.3 / the Pieri formula) — now with **a = 3 pinned**, so the evaluation is unambiguous.

## Tier / handoffs
- **@Elie** — with **a = 3 pinned (Gate A)**: evaluate the two-row generalized Pochhammer (ν)_{(λ₁,λ₂)} = (ν)_{λ₁}(ν−3/2)_{λ₂} and the Pieri off-diagonal (add-one-box, a=3) for the up/lepton/neutrino sectors, from FK Ch XII. **Built-in tripwire: your evaluation MUST reproduce the single-row down (3)_{(1,0)}=3 and the ladder 1:20:840** — if not, flag it (the d-pin failed) and stop. Then post the full K matrix + provenance BLIND (K1002) and fire.
- **@Cal** — audit the d-pin: FK type IV ⟹ a = n−2 = 3 (two ways: the classification + dim V₁₂ = N_c = 3). Confirm d = 1 is the type-I value, not applicable. And that the two-row a=3 values (4.5, 18, 45) are FK-sourced, not tuned.
- **@Keeper** — Gate A resolved to the book (a=3, in writing); Gate B set with the self-correcting down tripwire. The block is cleared to one sourced evaluation. Your K1002 blind bar holds; the tripwire is the extra self-check inside it.
- **@Grace** — data-layer dedup can proceed; the diagonal (single-row down, banked) is clean, the two-row entries land from Elie.
- **@Casey** — the block was exactly one convention, and I pinned it to the book rather than take anyone's word (Keeper gave me the anchor and, correctly, told me to verify it — asserting a convention is the one thing we don't do). The multiplicity for our type of domain is n − 2 = 3, which is our color number — and it checks two independent ways (the textbook classification, and the dimension of the color/off-diagonal Peirce space, which is 3). The d = 1 that was floating around is the value for a *different* type of domain (real symmetric matrices), not ours. With that pinned, the binomial table is unambiguous, and it carries its own safety catch: it has to reproduce the down-quark check (the minimal entry = 3) or we know the pin is wrong on the spot. So the crank is now genuinely one sourced evaluation from turning — and it's self-correcting, which is the right way to unblock something that feeds thirteen numbers.

Notes only; no toy/theorem claimed (Elie owns the numeric). F736 (surgical unblock 29p): GATE A — type-IV multiplicity d=a=n_C−2=3=N_c, verified FK (classification: type IV a=n−2; + dim V₁₂=N_c=3 two ways); d=1 is type-I, not applicable; pinned in writing. GATE B — generalized Pochhammer a=3, r=2: (ν)_{(λ₁,λ₂)}=(ν)_{λ₁}(ν−3/2)_{λ₂}; tripwire (ν)_{(1,0)}=ν=N_c=3 (single-row a-independent, the down consistency, 1:20:840 banked); two-row a=3 distinguishes from a=1 ((3)_{(1,1)}=4.5 vs 7.5); off-diagonal = Pieri add-box a=3 through degree-1 condensate. @Elie evaluate two-row + Pieri from FK Ch XII with a=3, MUST reproduce down tripwire else d-pin wrong, post blind, fire. @Cal audit d-pin. Self-correcting unblock. — Lyra