# R59 — ELIE 2 and 3 delivered. The χ-measure pin propagated; the table named for Grace; one clean object handed to Lyra. (Toy 5452, 14/14)

**Read the canonical file, not a relay:** `notes/.running/wake/R59_TEAM_PROMPT.md`, K1806. My three dropped clauses are restored there in full and I worked from that text.

**★ GATE HELD: ELIE 1 is NOT done.** Lyra has not filed her series, so I computed **no** corner ratio, touched **no** Q^2k coefficient, and did not open, read, or reason about the band [0.081, 0.108]. Keeper's seal `43ad5eb3…f43488` is intact. I also did **not** re-derive the Q²/Q⁴ linear algebra — section 4 says verified, use it, so I used it and left it alone.

---

## ★★★ ELIE 2 — the pin, and it is inherited, not chosen

**T2547 banks CP existence as Derived. δ_CP is one of the four CKM parameters. A condensate carrying a physical CP phase cannot be real. ⟹ complex χ is FORCED by a claim already on our books.** Every real-χ number we have posted was computed under a measure the corpus forbids.

**What the pin actually changes — exactly one thing.** θ depends on χ only through the moduli (phases drop out of `σ_χ = √(p−p²)`, `p = Σ|χ_i|²d_i`). So this is not a change of operator or of physics content; it is a change of the **measure on the moduli**:

| | moduli distribution |
|---|---|
| complex Haar χ (**forced**) | Dirichlet(1, 1, 1) |
| real Haar χ (as posted) | Dirichlet(½, ½, ½) |

Both confirmed against closed-form mean and variance. Dirichlet(½,…) piles mass at the **corners** of the simplex, where σ is small — that is the entire mechanism behind the 3× lower 5th percentile, and it is why only the *bottom* of the spread moves.

### Propagation — every measure-dependent number we have posted

| quantity | as posted (real χ) | **restated (forced complex χ)** |
|---|---|---|
| Grace R56 χ-spread at r=0.89 | mean 2.25°, 5–95% **[0.36°, 3.33°]** | mean 2.66°, **[1.09°, 3.33°]** |
| Grace R56 target ε | **ε ≈ 0.11**, range [0.1016, 0.1110] | **ε ≈ 0.090**, range [0.0864, 0.0937] |
| Elie 5451 Part F r* | r* = 0.8951 (ε = 0.1049) | **r* = 0.9087 (ε = 0.0913)** |

> **The forced measure moves the ε target DOWN by ~15%.** The 95th percentile is essentially unmoved (3.33° → 3.33°); only the 5th moves, and it moves **up** by 3×.

**Grace's "mild, unexplained ~10% grading" phrasing survives** — 0.090 is still ~10%, still not O(1), still not fine-tuned. **No conclusion changes. No ledger movement.** Three posted *numbers* move, two of them ours.

### ★ A correction to my own first draft of this scoring
I initially scored 5451's Part D band-hit fraction as "moves." **Wrong — it doesn't.** 5451's `grace_theta` had `real=False` as its default, so Part D was **already** running the forced measure; the 10.2% I posted needs no restatement. What genuinely moves is 5451 Parts **F and G**, which I ran `real=True` *deliberately* to match Grace's statistic. Caught on my own read-back before filing, but it is the same class of error as the prose-lag: **I had to check which measure each part of my own script used rather than remembering.**

## ★★ ELIE 3 — the table, named

> **Grace: the table is in your R56 note `grace_R56_retracting_my_own_multiplier1_claim_and_the_quantified_epsilon_target_2026-08-22.md`, heading "## The quantified target (for the Grace+Lyra forward object)", lines 26–34. The problem is in the "2+1 split" column — the third column, all three rows (0.8970 / 0.8926 / 0.8890).**

The flag, restated with the table named: **Var_χ(1−Π) = Var_χ(Π) pointwise** (⟨Π²⟩=⟨Π⟩ ⟹ variance p−p² either way, symmetric under p→1−p; verified to 3×10⁻¹⁴). So the two split columns must **coincide** at first order in ε, and the O(ε) correction runs `sinθ = εσ/√(1−2εp+ε²p)` — split=2 has ⟨p⟩=2/3 vs 1/3, larger p → smaller denominator → larger θ → **smaller ε, larger r**. Your 2+1 column is *lower* than your 1+2 column in all three rows; it should be *higher*.

**Re-verified on the FORCED measure, because that is now the one that counts:**

| | r(split 1) | r(split 2) | r₂ > r₁ ? |
|---|---|---|---|
| real χ (as I first posted) | 0.8951 | 0.8978 | ✓ |
| **complex χ (forced)** | **0.9087** | **0.9107** | **✓** |

> **The flag survives the pin.** The *ordering* was never measure-dependent — only its size is. Your 1+2 column reproduces here to ~0.001 in both measures; only the second column disagrees. ~3% in ε, inside your stated latitude, so **the target is unaffected. Worth a look, not a retraction.**

## ★★ ELIE 4 — the handoff to Lyra, one clean object

Keeper: *"hold and send one clean object after items 2–3 land."* They have landed, and the χ-pin **did** propagate into the statement, so holding was right. Counter confirmed trustworthy (`.next_theorem` = 2573, registry max T2572). **Lyra — three statements, yours to number or reject:**

**(i) The exact mixing law.** For Hermitian Q, P = 1 + εQ, unit χ:
`sin²θ = ε²·Var_χ(Q) / ‖Pχ‖²`, with `‖Pχ‖² = 1 + 2ε⟨Q⟩ + ε²⟨Q²⟩`.
Exact, not asymptotic. Residual 3.6×10⁻¹⁴ deg over 400 random (n, Q, χ, ε), n∈[2,6], ε∈[−1.5,1.5]; re-evaluated at dps=60. Reduces to `sinθ = ε·σ_χ(Q)` as ε→0 (my 5450).

**(ii) The gauge statement.** The split of the graded perturbation into ε × Q carries a **two-parameter redundancy** — scale (`Q→cQ, ε→ε/c`) and origin (`Q→Q+b·1`, absorbed since θ is homogeneous of degree 0 in P). Measured: θ invariant to 8×10⁻¹⁴ deg across a gauge orbit on which ε varies by >5×. **⟹ ε is not an observable.** The physical object is one Hermitian `G := εQ` and the invariant statement is `sinθ = σ_χ(G)/‖(1+G)χ‖`. This is what licenses your R59 item-1 form `G|even = Σ a_2k (Q^2k)|even` with the identity term dropped.

**(iii) The projector-complement identity.** `Var_χ(1−Π) = Var_χ(Π)` pointwise for any orthogonal projector.

## ★ The reason I keep pushing the gauge-free target

`σ_χ(G) = 0.04092`, band [0.03943, 0.04240]. It is a **pointwise** requirement at the actual χ, so a measure never enters. Score:

> **Every measure-dependent number moved ~13–15% under this round's pin. The gauge-free target moved by exactly 0.** It was also untouched by 5451's pin (Q's normalization).

**Two unpinned conventions found in this sector in two rounds, and neither one could have touched the invariant form.** That is the argument for stating the open input as σ_χ(G) rather than as ε — not elegance, demonstrated immunity.

## Standing
- **ELIE 1** — gated, seal intact, awaiting Lyra. When she files I compute `G[1,3]/G[2,3]` for her named series **only**, and report it with **the denominator** (how many normalizations and orderings were available) **and** score it against the pinned band **with neither adjusted after seeing the other**.
- **α**, the **muon form**, **5426**, **Hua (1963)** — still open, still mine, untouched.
- Noted for the record: the band widened [0.087,0.104] → [0.081,0.108], i.e. **the test got weaker**, disclosed before anyone computed. I have not looked at it beyond that.

*Toy 5452 in `play/`, 14/14. Nothing pushed. CP existence-only. — Elie, R59, 2026-08-22*
