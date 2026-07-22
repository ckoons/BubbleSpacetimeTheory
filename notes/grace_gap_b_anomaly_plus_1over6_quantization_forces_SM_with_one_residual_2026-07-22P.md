# Gap (b): anomaly + 1/6-quantization → the SM, with one honest residual (the fundamental-charge reading)

*Grace | 2026-07-22 | Casey's PUSH on the anomaly-freedom forcing. Gap (b) is the cheap decider (finite linear algebra) and it's my lane (the 1/6 quantization is my charge-row result, K806/T2521). I computed it target-innocently, and it does NOT cleanly land — there's a genuine third anomaly-free direction. The 1/6 quantization resolves it, but only via a specific reading I've pinned for Cal's circularity gate. Held LEAD, honest residual named.*

## The computation (target-innocent scan of all integer Y_i in units of 1/6)
LH Weyl content Q=(3,2), u^c=(3̄,1), d^c=(3̄,1), L=(1,2), e^c=(1,1); impose all four anomalies (SU(3)²U(1), SU(2)²U(1), grav²U(1), U(1)³). **Three primitive anomaly-free directions:**
| dir | n = (Q,u,d,L,e) | Y | meaning |
|---|---|---|---|
| **D1** | (1,−4,2,−3,6) | (1/6,−2/3,1/3,−1/2,1) | **the SM** |
| **D2** | (1,2,−4,−3,6) | (1/6,1/3,−2/3,−1/2,1) | SM with u^c↔d^c (trivial relabel — same physics) |
| **D3** | (0,1,−1,0,0) | (0,1/6,−1/6,0,0) | **quark-only U(1), leptons NEUTRAL — NOT the SM** |

## ★ The honest result — anomaly cancellation alone is NOT unique (D3 is the ambiguity)
**Anomaly cancellation by itself does not force the SM** — D3 is a genuine extra anomaly-free U(1) (only the right-handed quarks charged, oppositely). *This is exactly the "2-fold hypercharge ambiguity" the web/K827 named*, made concrete. So I do **not** get to say "gap (b) lands cleanly." It doesn't — not from anomalies alone.

## What the 1/6 quantization does (and it's real work, not scale-fixing)
- **1/6-quantization alone doesn't kill D3** — D3 is *already* in units of 1/6.
- **What kills D3:** the Z₆ center forcing the SU(2) doublet Q_L to carry the **fundamental unit Y_Q = 1/6** (the minimal nonzero center charge). D3 has Y_Q = 0, so **Y_Q = 1/6 excludes D3** → only D1/D2 survive = the SM (mod the trivial u/d relabel). Verified: {Y_Q=1/6 + anomalies} → the SM uniquely.
- So the 1/6-from-the-center does **more than fix the scale** — it *excludes the quark-only branch*, which is what makes the SM unique.

## The residual (for Cal's circularity gate — I flag it, don't paper it)
The whole thing turns on **one sub-question:** does the Z₆ center force **Y_Q = 1/6 specifically** (i.e. Q_L is the *fundamental rep* of the [SU(2)×U(1)]/Z₆ quotient, carrying the minimal center charge), or only the weaker "all Y in units of 1/6"?
- **Fundamental-rep reading → Y_Q=1/6 → excludes D3 → SM forced.** ✓
- **Weaker unit-only reading → D3 survives (it's 1/6-quantized) → SM not forced.** ✗
**So gap (b) reduces to: is Q_L the fundamental rep of the center quotient?** Plausible (it's the natural reading of the Z₆ = Z_{N_c}×Z_rank structure — the doublet+triplet fundamental carries the minimal charge), but **must be pinned, not assumed.** That is the honest frontier of gap (b).
**Circularity check (Cal):** anomalies contribute the *direction structure* (D1/D2/D3); the center contributes *Y_Q = fundamental*. These are **independent inputs** — the center reading is a geometric fact (K806), not derived from the anomaly argument. So it's **not circular** — but the 1/6 is doing load-bearing work (excluding D3), so its independence and the fundamental-rep reading must both hold.

## Honest tier
- **LEAD.** Gap (b) is the cheap decider and it **conditionally lands:** anomaly + (Z₆ forces Y_Q=1/6) → SM. But it has the residual — the fundamental-rep reading — which is *not* established, just plausible.
- **Even a partial result is a real result** (Lyra's framing): if Q_L turns out to be the fundamental rep, gap (b) is closed and the forcing is on; if it's only unit-quantization, the SM is anomaly-*consistent* but not uniquely forced (D3 survives) → the mechanism is grounded but parity stays derived-conditional.
- **Compute-don't-assert.** I did NOT let "anomaly forces the SM" bank — it doesn't (D3). The clean statement is the conditional one.
- **Order of attack confirmed (Lyra's plan):** gap (b) was the cheap one — done, with a precise residual. Only if the fundamental-rep reading holds do the harder gaps (Pin/mod-2 index → one generation; bulk Chern–Simons for inflow) get spent on. DIRAC + Route 1 closed; FA-positive.

## Net
- **Computed gap (b) target-innocently:** anomaly cancellation gives **3** directions (SM, u/d-relabel, quark-only D3) → **NOT unique alone** (the web's 2-fold ambiguity = D3, concrete).
- **★ The 1/6 quantization resolves it — but only via "Q_L carries the fundamental Z₆ charge Y_Q=1/6," which excludes D3** (not mere unit-quantization, which D3 already satisfies). Verified: Y_Q=1/6 + anomalies → SM uniquely.
- **The residual (the honest frontier):** is Q_L the fundamental rep of the [SU(2)×U(1)]/Z₆ quotient? Plausible, unproven — that one sub-question is now gap (b). Not circular (anomalies vs center = independent).
- **Held LEAD;** the two-for-one (parity + charge-row neutrality) is live *if* the fundamental-rep reading holds.

---

## ★ RESIDUAL RESOLVED (K828) — the center CORRELATION kills D3 (gap b CLOSED)
My residual was "does the Z₆ center force Y_Q=1/6 specifically?" **Resolved, and rigorously.** The Z₆ center doesn't just quantize Y in units of 1/6 — it **correlates** Y with the (color, isospin) reps:
$$6Y \equiv 4\cdot(\text{color triality}) + 3\cdot(\text{doublet-ness}) \pmod 6$$
I verified it holds for all five SM fields (Q_L→1, u^c→2, d^c→2, L_L→3, e^c→0). **D3's Q_L is a color-triplet doublet (triality 1, doublet 1) → requires 6Y≡1, but D3 has 6Y_Q=0 → D3 VIOLATES the correlation → excluded by group theory** (not the weaker "require a charged generation" postulate). This is the rigorous form of my fundamental-rep flag — Keeper adjudicated to it (K828). **Gap (b) CLOSED:** anomaly forces the ratios + the center correlation excludes D3 and fixes the scale → the SM hypercharges DERIVED **given the reps.** Not circular (anomalies = ratios; center correlation = K806 geometry, independent).

**The two-for-one delivered:** those linear anomaly conditions ARE my N_c-weighted neutrality (T2521) that I *imposed* — now DERIVED via Callan–Harvey inflow → the exact charges {+2/3,−1/3,−1,0} firm derived-conditional → **DERIVED (given reps).** I firmed the T2521 registry entry accordingly.

**Scope held hard:** gap (b) forces the hypercharges GIVEN the reps (Q_L a color-triplet doublet, etc.). It does NOT derive the **rep content** — which fields are doublets/singlets (the Wilson-line twist) — that's **gap (a), open** (Lyra's boundary Pin computation). So: **charge sector firmed to derived; parity's rep-content forcing is the open frontier.**

— Grace, 2026-07-22P (K828: residual resolved, gap b closed). Gap (b) computed target-innocently (my lane, the 1/6 is K806/T2521): anomaly cancellation gives 3 primitive directions — D1=SM, D2=SM(u↔d relabel), D3=(0,1,−1,0,0) quark-only-U(1)-leptons-neutral — so anomalies ALONE do NOT force the SM (D3 = the web's 2-fold ambiguity, concrete). RESOLUTION: 1/6-quantization alone doesn't kill D3 (already 1/6-quantized); what kills D3 is the Z₆ center forcing Y_Q=1/6 = the doublet carries the FUNDAMENTAL unit (D3 has Y_Q=0, excluded) → SM uniquely (mod u/d). RESIDUAL (gap-b's honest frontier, for Cal): does Z₆ force Y_Q=1/6 (fundamental-rep charge) or only 'Y in units of 1/6'? fundamental→SM forced; unit-only→D3 survives, not forced. NOT circular (anomalies=direction, center=fundamental charge, independent K806). TIER LEAD, conditional-lands; even partial=real (anomaly-consistent vs forced). Order confirmed: gap(b) cheap-done w/ residual; harder gaps (Pin mod-2 index, bulk CS) only if fundamental-rep holds. DIRAC+Route-1 closed; FA-positive; two-for-one live if reading holds.
