# K1258 — Forcing-Pincer Innocence Audit: the shared circularity failure mode, and the two discriminators that decide it

**Auditor:** Keeper. **Date:** 2026-08-07. **Object:** Paper B (Cartan-elimination forcing of D_IV⁵), the K1255 two-bound pincer on the short-root multiplicity. **Question posed:** is the pincer *target-innocent* (two genuine independent constraints squeezing m_s = 3), or *circular* (one or both bounds secretly presuppose the answer)?

**Verdict:** the pincer stays **CONDITIONAL — not yet a forcing.** Both jaws share one failure mode, and I can name the exact discriminator for each. I cannot resolve either from the armchair (each needs one representation-theory computation), but I have reduced "is the forcing real?" to two sharp, computable yes/no questions. That reduction is the deliverable.

---

## The pincer, stated exactly (with the BSD invariants pinned)

An irreducible bounded symmetric domain is fixed by (r, a, b): r = rank, a = multiplicity of the "off-diagonal" restricted roots, b = multiplicity of the "short" roots. For the **type IV_n domain** (D_IV^n, the Lie ball):
- r = 2, **a = n − 2**, b = 0 (tube type), dim_C = r + a·r(r−1)/2 + b·r = **n**, genus p = (r−1)a + b + 2 = **n**.

For D_IV⁵: **r = 2, a = 3, b = 0, dim = 5, genus = 5.** So the corpus's "m_s = 3 = N_c" is exactly the off-diagonal multiplicity **a = 3**, and "dim_C = m_s + rank = 5", "genus = n_C = 5" all check. (Source-consistent with CLAUDE.md: genus = n_C = 5, N_c = m_s = 3, dim = 5. I am using a for what the corpus calls m_s.)

Paper B's forcing: **(r = 2) ∧ (a = 3) ∧ (tube type) ⟹ D_IV⁵**, and the two jaws pin a:
- **R3 (lower jaw):** convergence ⟹ a ≥ 3 ⟺ (at r=2) n ≥ 5.
- **R5 (upper jaw):** Selberg d_F ≤ 2 ⟹ a ≤ 3 ⟺ (at r=2) n ≤ 5.

Squeeze ⟹ a = 3 ⟹ n = 5.

---

## The shared failure mode: a pincer is innocent iff neither jaw is machined to the target

Reduce it to counting (AC(0)). Each jaw is an inequality "the multiplicity a must be ≥ (or ≤) 3 for quantity Q to [converge / have degree ≤ 2]." That inequality is a **genuine external constraint** only if Q is fixed *before* a is known. It is a **tautology** if Q is itself a function of a — because then "Q converges / Q has degree ≤ 2" is just an algebraic restatement of "a = the value that makes it so," and the jaw has been machined to land on the target.

**One-line audit rule (standing, this lane): a pincer forces its target only if neither jaw's controlling quantity depends on the target.** Both jaws here are *at risk under exactly this test*, and each risk is concrete:

### R3 discriminator — is the convergence exponent a-dependent?

R3 asks: how large must a be for the domain's canonical integral to converge at r = 2? The controlling quantity is the **exponent s** in ∫_D N(z,z)^{-s} (equivalently, where the Gindikin Γ-factor / Wallach continuum begins). The continuous Wallach threshold at r = 2 is **(r−1)a/2 = a/2**, and convergence of ∫N^{-s} needs s past a rank-and-a-dependent line.

- **CIRCULAR case:** if the exponent plugged in is the **genus** s = p = (r−1)a + 2 (i.e. the *Bergman* kernel), convergence is automatic — the Bergman integral ALWAYS converges, that is what makes it Bergman — so "R3" says nothing about a. The bound would be vacuous, dressed as a constraint.
- **INNOCENT case:** if the exponent is an **a-independent physical scale** — the Szegő/Hardy exponent s = 1, or the commitment operator's fixed heat-semigroup parameter e^{−τH_B} whose trace-convergence threshold is set by rank and the *physical* τ (not by a) — then "converges at r = 2 only if a ≥ 3" is a real lower bound.

**Discriminator (Grace, one computation): write the exact convergence threshold for the substrate's actual controlling integral, and read off whether its exponent is a function of a. If yes → R3 circular. If no (fixed physical exponent) → R3 innocent, and check the threshold genuinely lands at a ≥ 3.** The Plancherel/Wallach density is the object; the question is purely "does the exponent carry an a in it?"

### R5 discriminator — is d_F a multiplicity-degree, or just the rank in disguise?

R5 asks: d_F ≤ 2 ⟹ a ≤ 3. The controlling quantity is **d_F**, the "Selberg / fundamental degree." Two readings, and they are NOT the same audit:

- **CIRCULAR case:** if d_F is the **fundamental degree = the rank r** (the degree of the generic minimal polynomial of the Jordan algebra, = r for all these domains), then "d_F ≤ 2" ⟺ "r ≤ 2" — a constraint on RANK, not on a. Combined with the *already-assumed* r = 2, it says nothing new about a; the "⟺ n ≤ 5" step would be smuggling (fixing r = 2, then re-reading a rank fact as a multiplicity bound).
- **INNOCENT case:** if d_F is genuinely a **multiplicity-sensitive degree** — e.g. the degree of the b-function / a count of relative invariants that *grows with a* — then "d_F ≤ 2" is a real upper bound on a at fixed r.

**Discriminator (Lyra, one definition + one check): pin d_F to its primary-source definition (which "Selberg degree"?), then compute its a-dependence at r = 2. If d_F = r (rank) → R5 circular. If d_F grows with a → R5 innocent, and check it caps at a ≤ 3.**

---

## Why this is the right place to be careful (and why it is CONDITIONAL, not FAIL)

This is the deepest-question lane — "is D_IV⁵ forced?" — and it is exactly the lane where the peak-convergence temptation (K1256) is strongest: a clean two-line pincer landing on n = 5 *feels* like the pithy paragraph Casey predicted a hundred years out. The tell is not the feeling; it is whether the jaws were machined. Right now I cannot certify they weren't, so:

- **NOT a forcing yet.** Paper B remains CONDITIONAL PASS (K453 tier holds). It may NOT be cited as "D_IV⁵ is forced" externally.
- **NOT refuted.** Neither jaw is *shown* circular — both are *at risk* pending the discriminator. If both come back innocent, this is a genuine forcing and a major promotion (routes to Casey + Cal per the D-tier governance chain).
- The honest current statement: **"D_IV⁵ is the unique tube-type rank-2 bounded symmetric domain with off-diagonal multiplicity 3; whether (rank 2, multiplicity 3) is itself *forced by physics* reduces to two computable innocence checks (R3 convergence-exponent a-dependence; R5 Selberg-degree rank-vs-multiplicity), both open."**

That last sentence is publishable *as a forcing skeleton with two named open gates* — which is more honest and more useful than either "forced" (overclaim) or silence.

---

## Routing

- **@Grace** — R3: write the substrate's actual controlling convergence integral and read the a-dependence of its exponent. Deliverable: "R3 exponent is [genus p(a) → circular] / [fixed physical s → innocent, threshold at a ≥ __]."
- **@Lyra** — R5: pin "Selberg d_F" to its primary-source definition, compute its a-dependence at r = 2. Deliverable: "d_F = [rank r → circular] / [multiplicity-growing → innocent, cap at a ≤ __]." Pin the definition to the book once (standing rule) before computing.
- **@Keeper** — re-audit both deliverables against the one-line rule (neither jaw's Q depends on a); if both innocent, draft the promotion note for Casey/Cal; if either circular, the pincer is downgraded to "uniqueness within the type-IV family" and the forcing of (r=2, a=3) stays open.

— Keeper, K1258, 2026-08-07. Forcing pincer stays CONDITIONAL (not a forcing). Both jaws share one failure mode: a bound forces the target only if its controlling quantity is target-independent. R3 innocent iff the convergence exponent is a-independent (circular if it's the genus/Bergman, which always converges); R5 innocent iff Selberg d_F grows with multiplicity (circular if d_F = rank in disguise). Two computable discriminators routed to Grace (R3) and Lyra (R5). Publishable now only as a forcing skeleton with two named open gates. Both innocent → genuine forcing, routes to Casey+Cal.
