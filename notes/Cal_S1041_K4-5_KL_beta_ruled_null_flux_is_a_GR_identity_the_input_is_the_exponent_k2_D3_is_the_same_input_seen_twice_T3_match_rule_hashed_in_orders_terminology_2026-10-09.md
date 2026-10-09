# Cal Section 1041 — K4-5: KL-β ruled (the null flux is a GR identity; the INPUT is the exponent k = 2, and "D = 3 forced" is that input seen twice); T3's match rule hashed in orders before Elie computes; terminology ruled

**Written 2026-10-09 14:56 EDT (from `date`).** Read: the K4-5 prompt, Lyra's K4-4 rewrite (0c814419), K1956 (+ Section 8 via the prompt), Elie 5874. **Not read: K1919 Section 7's number, any census input, any N_req.** No instrument needed for Section 1 (one line of algebra, checked against Lyra's sympy output); none run.

## 1. KL-β ruled: the null flux is a GR identity, not an input — but it does not set β. The exponent does.
Write the law as N ∝ N_H^k. Then s_N = k·d ln N_H/dx = k[3(1 − f) + Ω_r] at w = −1 (Lyra's instrument line; 5874 R1–R2). Match to Elie's parametrization 6(1 − f) + βΩ_r: the matter term gives **k = 2**, and then **β = k = 2 with nothing left to choose.** So:
- **The null-flux identification is a GR identity** (d ln N_H/dx = −2Ḣ/H² = 3Σ(1 + w_i)Ω_i; a horizon is a null surface; Jacobson's dQ = T_ab k^a k^b is the lineage). It is not a choice made with the answer in view; the timelike form was never a candidate for a null surface. **KL-β: PASS on the identification.** Keeper's reading (K1956 Section 1) is right: consistency with GR, K1919 class.
- **But β is set by k, and k = 2 is the law's one input.** Where did k = 2 come from? From the filling law's design: ρ_DE = E·N/V_H ∝ H⁴N is constant iff N ∝ H⁻⁴ ∝ N_H². "N ∝ N_H²" is the sentence "ρ_DE is constant" rewritten; K1922's ε = 2 was chosen on 09-25 to make the matter era give exactly that. **The exponent was fixed with the answer (a constant ρ_DE) in view, before today.** That is not a knob (there is no continuous parameter) and it is not a fine-tuning; it is a construction. KL-β's void clause does not fire (β was not chosen after the run), and the honest tier is Keeper's: **Λ by identity.** The sentence "zero-knob SHAPE from one identification" (Lyra Section 4) overstates: the shape is zero-knob GIVEN k = 2, and k = 2 is the shape.
- **"Constant iff D = 3" is the same input seen twice.** With general k, ρ_DE ∝ H^{1 − k(D−1) + D} is constant iff k = (D + 1)/(D − 1); k = 2 ⟺ D = 3. Elie 5778 found exactly this on 09-25 (per-write exponent (D + 1)/2). So "D = 3 forced by the exponent count" means "the exponent chosen for D = 3 is consistent with D = 3." A consistency between two integers that were both on the table; not a derivation of D. **Caged: "the ledger derives three dimensions."**
- **The pair reading ("a commit relates two boundary cells; N_H² is the pair capacity; N = c·N_H²") is Condition A one level up:** N_H² is a capacity of ADDRESSES (pairs); "the committed count is a constant fraction c of the pair capacity at every epoch" is the assertion that makes w ≡ −1, and nothing in the law says why the committed fraction of pairs is constant in time. It is a candidate mechanism at most, pending (i) Casey's two-ended answer and (ii) a charging rule (P1 charges one bit per commit; a pair is one commit, fine; but why does the count track the square?). **Ruling: mechanism at tier C — REFUSED as written; identity at the K1919 tier — GRANTED; the pair reading — candidate, two things owed.**
- **KL-β2 (the source's composition): answered and accepted.** Source = the null flux (N ∝ N_H²); census = the normalization c. No mixed source. Elie's run proceeds under this word.

## 2. T3's match rule, hashed before the census is computed
**Definitions, fixed:**
- **N_req**: the count that makes ρ_DE = Ω_Λ ρ_crit today under the law's own E_commit = ℏH₀ ln 2/(2π) and V_H = (4π/3)(c/H₀)³. It is an identity on the record (K1919 Section 7); **I have not read it and do not here.** Elie evaluates it from the formula, as an instrument line, AFTER N_census is on disk.
- **N_census**: the number of absorptions of real photons by bound electrons, over cosmic history, inside today's comoving Hubble volume (the cumulative comoving count A times V_H(a = 1), as 5869 defines W), **stellar interiors excluded** (Casey's Q2; Lyra's census table). One absorption = one bound–bound or bound–free transition of a bound electron caused by a real photon (E1, M1 hyperfine, band/solid transitions all count once each). Thomson/Rayleigh/Compton scattering do not count. Recombination capture does not count (an emission). Re-emission followed by a later absorption elsewhere counts the later absorption again (χ ≡ 1); the dust infrared cycle is a fork (counted once per stellar photon vs recursively), printed as such.
- **Forks (printed with the can-fail count):** χ ≡ 1 (primary, the computable proxy) and χ = 1 − f_local (proxy, beside); relic-photon classes (21-cm, Lyman) and starlight/EBL classes separately and summed; dust once vs recursive. No η_γ (one K4 per absorption, KL-W1 closed). Elie prints the span of N_census across forks before anything else.
- **Control first:** x_e ≡ 1 (no bound electrons) ⇒ N_census = 0.

**Order:** N_census (every fork) on disk with its hash → then N_req from the formula → then the ratio. Not the other way.

**The rule, in orders:**
- **MATCH (credit):** |log₁₀(N_census/N_req)| ≤ 1 for the primary fork (χ ≡ 1, all classes summed, dust once). Within a factor ten. The census's own fork spread will be of order one decade or more; a match tighter than the instrument's spread is not claimable, and a match looser than one decade is "same kind of number", not a match.
- **REPORT, no credit:** 1 < |log₁₀| ≤ 3 — the two counts are the same KIND of number; the pincer does not fire but the normalization is not reproduced.
- **MISS:** |log₁₀| > 3 — the pincer fires: either (i) a commit is not one per atomic absorption (Casey's substrate-level rate, the March premise), or (ii) c is set by the de Sitter end and the census is the carrier. **Which horn is not decided by the number; it is decided by Casey's "two-ended or one-ended" answer and by the half-angle test, both still open.**
- **Null for the credit band:** the a-priori span between a photon budget and a horizon-area count is many decades; Elie prints the span between the smallest fork and N_req when both are on disk, and the chance of a ±1-decade landing is 2/(that span). I do not write the span from memory.
- **Caged on sight:** N_req ≈ any BST integer or power; N_census/N_req ≈ any clean ratio; a second census class added after the ratio is read (void).

## 3. Terminology, ruled (one sentence each)
- **"One K4 per absorption"** is the COMPOSITION: the substrate constructs one K4 from each non-null absorption, with no cross-atom triples; the count N is the number of such K4s.
- **"Census-sourced"** is a GROWTH LAW in which d ln N/dx is set by the absorption history (5869 H2, 5874 R9); the law no longer uses it for growth, only for the normalization c; "N = W gives w ≠ −1" (R9) is a statement about that retired growth law, not about the composition.

## 4. Target 2: unattempted stands (K1954 Section 10).

## 5. Carried
- The half-angle test (Elie, now; P7 stands: ratio 2, "same 3" survives only as a spinorial claim).
- Lyra's R-sector paragraph, the two-ended/one-ended forms, the Coleman–Mandula sentence; the scope-annotation rewording (owners' edit; I read).
- Casey's three: two-ended?; S4; "exterior".

— Cal, 2026-10-09.
