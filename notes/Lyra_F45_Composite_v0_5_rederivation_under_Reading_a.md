---
title: "F45 — Composite v0.5 (m_μ/m_e = 207) re-derived under Reading (a): the additive 'bulk+boundary' is retired (double-count); replaced by a CANDIDATE H²-internal Peter-Weyl K-type sum 207 = [(N_c·n_C)²·g + N_c⁴]/2^{N_c}, normalized by ONE Hardy factor. Candidate, not forced; K-type assignment is the open core (joint Elie)."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-06 Saturday 13:25 EDT"
status: "v0.1 PRIMARY — load-bearing F44 consequence. Retires bulk+boundary additivity; proposes H²-internal heat-trace-like decomposition; honest open core + Tier-2-STRUCTURAL fallback"
supersedes: "Composite v0.5 additive interpretation (F9/F32/Ch9) — the FORM 207 stands, the bulk+boundary READING is retired"
---

# F45 — Composite v0.5 under Reading (a)

## 0. The problem (my own F44 flag)

Composite v0.5 wrote m_μ/m_e = 207 = Term 1 (bulk, 1575/8) **+** Term 2 (edge, 81/8). Under the F44 reading decision (everything physical in H²; bulk/boundary = two *realizations* of the same space), "bulk + boundary" of the same data **double-counts** — the additive form as written cannot stand. This note re-derives, or retires, the result honestly.

## 1. What additivity is *allowed* under Reading (a)

Reading (a) does not forbid additivity — it forbids adding two *realizations of the same object*. Within H², distinct **K-types are orthogonal** (Peter–Weyl), so a sum of distinct-K-type matrix contributions is a legitimate additive decomposition of a single H² trace:

$$\mathrm{Tr}_{H^2}\big(\mathcal{O}\big) = \sum_{\lambda}\, c_\lambda\,\langle V_\lambda\mid \mathcal{O}\mid V_\lambda\rangle,\qquad V_\lambda \perp V_{\lambda'}.$$

So the rescue path is: read 207 as an **H²-internal sum over orthogonal K-types**, not as bulk + boundary.

## 2. A Reading-(a)-consistent candidate decomposition

$$\boxed{\;m_\mu/m_e \;=\; 207 \;=\; \frac{(N_c\,n_C)^2\,g \;+\; N_c^4}{2^{N_c}} \;=\; \frac{a_0\,g + N_c^4}{2^{N_c}}\;}$$

where $a_0 = (N_c n_C)^2 = 225$ is the **leading heat-trace coefficient** of D_IV⁵ (Sunday Toy 3661; also $c_{FK}\pi^{9/2}=225$). Check: $(225\cdot7 + 81)/8 = 1656/8 = 207$. ✓ The two original terms map exactly: Term 1 $=a_0 g/2^{N_c}=1575/8$, Term 2 $=N_c^4/2^{N_c}=81/8$.

**Why this is Reading-(a)-consistent (the key structural change):**
- The overall $1/2^{N_c}$ is a **single Hardy normalization** of the H² trace — one factor, not a second additive region. No double-count.
- The numerator $a_0 g + N_c^4$ is a sum of **distinct K-type contributions** within H²: $a_0$ is the leading (vacuum/Weyl, V_(0,0)-anchored) coefficient; $N_c^4$ is a sub-leading correction from a higher K-type. Peter–Weyl orthogonality makes the "+" legitimate **inside H²** — exactly what Reading (a) requires.

So the *form* 207 stands; the *reading* changes from "bulk realization + boundary realization" (illegal double-count) to "leading + sub-leading orthogonal K-type contributions to one H² trace, normalized once" (legal).

## 3. Connection to the surviving work (R(k), Ch 8)

This reframing **routes the muon ratio through the heat trace** — which is exactly the surviving F41/R(k) structure:
- $a_0 = 225$ is the leading heat-trace coefficient; the heat-trace coefficient *ratios* are Elie's $R(k) = C(k,2)/\kappa_{\mathrm{Bergman}}$ (κ_Bergman = −n_C).
- So under Reading (a), m_μ/m_e becomes a **truncated H² heat-trace** governed by the same Bergman-curvature structure that survived F43. The muon mass and the heat-trace cascade would then share the H² spectral geometry — a *legitimate* shared structure (same trace, same κ_Bergman), not the withdrawn bulk⊕Shilov operator-sharing.

This is the honest replacement for the retired "P unifies muon + Λ": the unifier, if any, is the **H² heat trace / Bergman curvature**, not the bulk/boundary projection.

## 4. The open core (joint with Elie's PRIMARY K-type scan)

Three things must close before this is more than a candidate:

1. **K-type assignment.** Identify the *specific* orthogonal H² K-types whose contributions are $a_0 g$ and $N_c^4$. $a_0=225$ is the leading coefficient (clean); $N_c^4=81$ is **not** obviously a standard heat-trace coefficient (a_1 = −1875, not 81), so the K-type giving $N_c^4$ is genuinely open. → **Elie's computational K-type candidate scan** is the tool; coordinate via this file.
2. **Truncation.** Why exactly two terms ($a_0 g + N_c^4$)? The higher heat-trace contributions must be shown to vanish, cancel, or be absorbed into these two. Otherwise 207 is a truncation artifact.
3. **Term-1 multiplicity (Casey #5 flag).** Term 1 = 1575/8 has *two* readings — $n_C\cdot(5/2)_3$ (V_(3/2,1/2) Pochhammer) **and** $a_0 g/2^{N_c}$ (leading heat-trace × g). These are different objects that coincide numerically. Reading (a) + the heat-trace route favors the $a_0 g$ reading, but this multiplicity must be resolved, not hidden (Cal #242).

## 5. Honest fallback

If Elie's scan finds **no** clean orthogonal-K-type structure producing $a_0 g + N_c^4$ (in particular, no K-type giving $N_c^4$), then the additive decomposition does **not** survive Reading (a) in any form, and the honest disposition is: **retire Composite v0.5's additive derivation; m_μ/m_e = 207 reverts to a Tier-2 STRUCTURAL identification** (it matches at 0.112%, the Two-Tier floor) **with the mechanism OPEN** — likely the (24/π²)^{C_2} = T190 form (which is a single-object form, not additive, hence Reading-(a)-safe) as the leading candidate mechanism instead. I flag T190 as the fallback because it does not invoke an additive split at all.

## 6. Honest status

- **Retired:** the "bulk + boundary" additive reading of Composite v0.5 (double-counts under Reading (a)).
- **Candidate (Reading-(a)-consistent):** 207 = [a_0·g + N_c⁴]/2^{N_c} as a single H² heat-trace, normalized once, decomposed into orthogonal K-type contributions; routes the muon through Bergman-curvature/R(k) (the surviving structure).
- **Open core:** identify the K-types (esp. N_c⁴'s); justify the two-term truncation; resolve the Term-1 multiplicity. Joint with Elie.
- **Fallback:** if no clean K-type structure, retire to Tier-2 STRUCTURAL with T190 (24/π²)^{C_2} single-object form as the open mechanism.
- **Tier:** F45 v0.1 candidate re-derivation under Reading (a); additive bulk+boundary RETIRED; H²-heat-trace candidate FRAMEWORK; multi-week per Cal #189 joint Elie.

## 7. Closure

Under Reading (a), Composite v0.5's "bulk + boundary" additivity is retired (double-count). The form 207 survives as a *candidate* H²-internal sum, 207 = [(N_c·n_C)²·g + N_c⁴]/2^{N_c}, legitimately additive via Peter–Weyl K-type orthogonality and normalized by a single Hardy factor — and this routes the muon ratio through the H² heat trace and Bergman curvature (κ_Bergman = −n_C), the structure that survived F43. The honest replacement for the withdrawn "P unifies muon + Λ" is "the H² heat trace / Bergman curvature is the shared structure, if any." Open core: the K-type assignment (Elie's scan), the truncation, and the Term-1 multiplicity. Fallback: Tier-2 STRUCTURAL via T190 if no clean K-type structure. The number was never in doubt; the mechanism is now honestly posed inside H².

@Elie — PRIMARY coordination: I need your K-type candidate scan to test whether distinct orthogonal H² K-types yield $a_0 g$ and $N_c^4$ contributions (esp. which K-type gives 81 = N_c⁴, since it is not a standard heat-trace coefficient). That decides candidate-vs-fallback. @Keeper — this routes through Ch 8 (Bergman curvature) and the R(k) theorem candidate; the muon-heat-trace connection is the substrate-curvature framing.

— Lyra, Sat 2026-06-06 13:25 EDT. F45 v0.1: Composite v0.5 re-derived under Reading (a). Bulk+boundary additive split RETIRED (double-counts two realizations of one H² object). Candidate replacement: 207 = [(N_c·n_C)²·g + N_c⁴]/2^{N_c} = [a_0·g + N_c⁴]/2^{N_c} (a_0=225 leading heat-trace coeff), read as ONE H² trace normalized by a single 2^{N_c}, decomposed into orthogonal K-type contributions (Peter-Weyl additivity — legal under Reading a, unlike bulk+boundary). Routes muon ratio through H² heat trace + Bergman curvature κ_B=−n_C → legitimately shares structure with Elie's R(k)=C(k,2)/κ_B (the surviving F41 work), replacing the withdrawn bulk⊕Shilov "P unifies muon+Λ." Open core: identify K-types (esp. which gives N_c⁴=81, NOT a standard heat-trace coeff), justify 2-term truncation, resolve Term-1 dual reading (n_C·(5/2)_3 vs a_0·g, Casey #5). Joint Elie K-type scan decides candidate vs fallback. Fallback: retire to Tier-2 STRUCTURAL via T190 (24/π²)^{C_2} single-object form (Reading-(a)-safe, non-additive). Multi-week per Cal #189.
