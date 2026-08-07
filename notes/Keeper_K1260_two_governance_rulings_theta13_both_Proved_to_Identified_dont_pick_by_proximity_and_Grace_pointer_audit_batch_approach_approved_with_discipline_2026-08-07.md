# K1260 — Two governance rulings: θ₁₃ (both Proved → Identified, don't pick by proximity) + Grace's pointer-audit batch approach (approved, with discipline). Both route to Casey.

**Keeper, 2026-08-07.** Two decisions the sweep forced. I recommend; Casey rules (tier changes and bulk corrections both route to him).

## 1. θ₁₃ (task #83) — recommend: BOTH forms Proved → Identified; do NOT pick by data-proximity.

**Facts (Grace + Cal, verified):** the corpus banks two "Proved" forms for the reactor angle — sin²θ₁₃ = 1/45 = 1/(N_c²·n_C) = 0.02222, and sin²θ₁₃ = 3/137 = N_c/N_max = 0.02190. Measured ≈ 0.02203. Cal *enumerated* (not asserted): only these two simple BST forms land within 1σ, so the data genuinely **cannot** choose between them (both ≈ 0.3σ). Neither is mechanism-forced: 1/45's factorization is unpinned; 3/137 is a third form with no derivation shown.

**Recommendation:**
- **Neither banks as Proved.** Two "Proved" labels on one observable with *different values* is a contradiction the registry must not carry. Demote both to **Identified** (< 1% match, mechanism plausible but unproven) pending a forcing.
- **Do NOT resolve it by which sits closer to the measured value.** That is target-chasing — exactly the discipline we tightened this week (target-innocence; the geometry must *force* the form, not the data select it). Picking 3/137 because it's marginally closer, or 1/45 because it's "cleaner," both fail the same test. The tie is broken by a *mechanism*, or it stays a two-candidate Identified.
- This is a demotion **from an over-claim** (Proved that was never earned), not a reduction of a real result — closer to a correction. But it's a tier change, so Casey's ruling.
- **Not a running-coincidence panic** (unlike sin²θ_W): neutrino angles run little, so both forms are legitimately near the interior value; the defect is "two Proved forms," not "run-down shadow." Lower severity than the sin²θ_W retirement.
- Does **not** block QM-10/10 externals (θ₁₃ isn't in the flagship).

## 2. Grace's pointer-integrity audit — approve the batch approach, with three disciplines.

**What Grace found (verified against TWO independent sources, graph + registry):** only **29 of 197** constants have a `theorem_id` pointing at the right theorem. Root cause is benign but pervasive — at some reorganization the low theorem numbers (T176–T400) were reassigned to foundational-math theorems and the physics-constant theorems were re-registered into the T1900–T2000 range, but the constants' pointer column was never migrated. So the *correct* backing for almost every physics constant is a high-numbered theorem with a near-identical name (top quark → T2009, proton charge radius → T1992, CMB spectral index → T1962). **Formulas, values, and tiers are intact — only the traceability is broken.** But traceability is exactly the machinery that should have caught "sin²θ_W = 3/13, Proved" and didn't (the link pointed at Lagrange's Theorem). So it is **load-bearing for the externals block**, even though it is not a physics error.

**Recommendation — approve, gated by three disciplines** (Grace already proposed the shape; I'm ratifying it and adding the audit gate):
1. **Auto-name-matching is a CANDIDATE GENERATOR ONLY, never an applier.** Grace's own catch: the matcher wants to point electron g−2 at the proton anomalous moment, proton lifetime at the tau lifetime. A bulk rewrite would trade *stale-but-visible* errors for *silent wrong* ones — strictly worse. Every applied link is human-eyeballed.
2. **Every applied link verified against BOTH sources** (graph + registry markdown must agree on the target theorem's identity). Grace is already doing this; make it the standing rule.
3. **Keeper spot-audits each batch before it counts as clean.** I independently re-verify a sample of each batch against graph+registry. The externals block lifts only when the swept registry+ledger is Keeper-clean.

**Phasing (Grace's plan, endorsed):** the **19 exact-name matches** first (verified target name ≈ constant name, both sources agree — lowest risk) → then the ~**75 near-match candidates** in reviewed batches → then **orphans / no-matches investigated individually**. Grace may start applying the 19 the moment Casey approves; I spot-audit that first batch against both sources before it's banked clean.

This is the systemic fix. A retirement only *stays* retired if the link that should surface it points at the right node. That the full audit turned up 168 stale pointers vindicates running it — this is the rot we suspected, now measured.

— Keeper, K1260, 2026-08-07. Recommend to Casey: (1) θ₁₃ both Proved-forms → Identified, tie broken by mechanism NOT data-proximity (target-innocence); not a running-coincidence, doesn't block externals. (2) Approve Grace's pointer-audit batch approach — 29/197 pointers correct, root cause = un-migrated column after a T-number reorg, physics intact but traceability broken (load-bearing for the block); disciplines: auto-match is candidate-only, verify against both sources, Keeper spot-audits each batch; 19 exact matches first, ~75 candidates in batches, orphans individually.
