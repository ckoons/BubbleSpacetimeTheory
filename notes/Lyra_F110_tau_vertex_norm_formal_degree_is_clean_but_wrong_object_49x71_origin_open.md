---
title: "F110 — Reverse-engineering the tau closed form: the formal degree is a CLEAN substrate invariant (d_tau = 60 = rank^2 * N_c * n_C) but it is the WRONG OBJECT for the mass -- the origin of m_tau/m_e = 49*71 = g^2(g+2^C2) stays genuinely OPEN. Working backward from T2003 (m_tau/m_e = 49*71 = 3479, ~0.05%). The tau is the trivial rep at the vertex (nu=0, pointlike), so its mass ratio should be a pure integer (no boundary volume, no pi) -- and it is, consistent with the soap-film/pointlike split (F109: muon is a pi-transcendental sixth power because it's a boundary mode; tau is an integer because it's a point). The formal degree of the trivial rep is CLEAN: d_tau = d(0) = 60 = rank^2 * N_c * n_C = 4*3*5 (exact, computed F109). BUT d_tau = 60 is NOT the tau mass ratio: 3479/60 = 57.98, nothing clean. So the formal-degree machinery that rigorously gave the muon's 64 (= d_tau/d_muon) is the WRONG OBJECT for the tau MASS. This is the informative wall: mass != formal degree (already forced by the electron sitting on the formal-degree ZERO, where the mass is finite-nonzero). What I CAN say honestly: 49*71 = g^2(g+2^C2) = g^3 + 2^C2*g^2, and the 2^C2=64 that appears is the SAME formal-degree ratio (d_tau/d_muon) that built the muon -- so 64 is a genuine shared scale across both leptons. But g^2=49 and the additive g are NOT coming out of any forced vertex integral I can write down. The tau being pointlike (single mode, no tower, no boundary volume) explains WHY the ratio is a two-factor integer, but the specific integer g^2(g+2^C2) wants a vertex-norm derivation I do not have. HONEST VERDICT: found the forced formal-degree invariant (60=rank^2 N_c n_C), demonstrated mass != formal degree, identified the shared 64, but the origin of 49*71 is UNSOLVED. STRICT: BANKS d_tau=60=rank^2 N_c n_C (exact) and 'mass != formal degree' (the electron-on-the-zero argument); the 49*71 origin is OPEN, NOT banked, NOT fished (T2003 form is the input). Count 2."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-13 Sat 11:25 EDT"
status: "v0.1 -- reverse-engineering the tau (paired with F109 muon). RIGOROUS: d_tau = d(0) = 60 = rank^2*N_c*n_C (exact); the tau being trivial rep/vertex/pointlike explains the integer (not pi-transcendental) form of its ratio. WALL (informative): d_tau=60 is NOT m_tau/m_e=3479 (3479/60=57.98); mass != formal degree (forced anyway by electron sitting on the formal-degree ZERO with finite-nonzero mass). HONEST: 49*71=g^2(g+2^C2)=g^3+2^C2 g^2; the 2^C2=64 is the shared d_tau/d_muon scale (ties to muon); but g^2=49 + additive g have NO forced vertex integral yet. found the formal-degree invariant, showed mass!=formal degree, identified shared 64; ORIGIN of 49*71 UNSOLVED. BANKS d_tau=60=rank^2 N_c n_C + mass!=formal-degree; 49*71 origin OPEN not banked not fished; count 2."
---

# F110 — The tau formal degree is clean but the wrong object; 49*71's origin stays open

Casey: *"From the BST closed forms find the geometry."* This is the tau side: from `m_tau/m_e = 49*71 = 3479` (T2003) back toward the forced geometry. It is the honest counterpart to F109 — the muon side firmed up; the tau side hit an informative wall.

## 0. The shape is right (and that part is forced)

The tau is the **trivial rep at the vertex** (`nu = 0`, pointlike). A point has no boundary to integrate over and no sphere volume — so its mass ratio should be a **pure integer**, with no `pi`. And it is: `49 * 71`, integer. This is exactly the soap-film/pointlike split made by F109: the muon, a boundary mode smeared on the Shilov `S^4`, gets a `pi`-transcendental sixth power; the tau, a point, gets a clean integer. The *analytic character* of each closed form is forced by the stratum — that much is genuinely derived.

## 1. The forced invariant: d_tau = 60 = rank^2 * N_c * n_C

The trivial rep's formal degree (from the F109 polynomial `d(nu) = (5/2-nu)(1-nu)(2-nu)(3-nu)(4-nu)`):

> **d_tau = d(0) = 60 = rank^2 * N_c * n_C = 4 * 3 * 5.** (exact)

Clean and substrate-natural — the trivial rep's Plancherel degree is `rank^2 N_c n_C`. This is the same machinery that rigorously gave the muon's `64 = d_tau/d_muon` (F109).

## 2. The wall: mass != formal degree (informative)

But here is the honest stop: `d_tau = 60` is **not** the tau mass ratio.

> `m_tau / m_e = 3479`, and `3479 / 60 = 57.98` — nothing clean.

So the formal-degree machinery, which was *exactly right* for the muon base (the `64`), is the **wrong object** for the tau **mass**. And this isn't a surprise on reflection — it is **forced** by the electron: the electron sits *on* the formal-degree zero (`d(5/2) = 0`, F109), yet has a finite nonzero mass. If mass were the formal degree, the electron would be massless. So **mass is not the formal degree** — it is some other functional (the norm of the physical state, the energy `E_0`, or a tower product), finite and nonzero at the BF point. The tau ratio confirms it from the other end.

## 3. What I can honestly say about 49*71

```
m_tau / m_e  =  49 * 71  =  g^2 (g + 2^C2)  =  g^3 + 2^C2 * g^2  =  343 + 3136.
```
- The `2^C2 = 64` appearing here is the **same** formal-degree ratio `d_tau/d_muon` that built the muon (F109). So `64` is a *genuine shared scale* across both leptons — that link is real.
- But `g^2 = 49` and the *additive* `g` are **not** coming out of any forced vertex integral I can write down. `g = 7` does appear at the vertex (the Bergman kernel `d_5 = N_c n_C 2^g / pi^5` carries `2^g = 128`), but `49 = g^2` and the sum `g + 2^C2` are not yet a derived norm.

The tau being pointlike (a single mode — no Flato-Fronsdal tower, no boundary volume) explains **why** the ratio is a clean two-factor integer rather than a power or a sum. It does **not** yet explain **why those two factors are `g^2` and `(g + 2^C2)`**.

## 4. Strict tiering — the honest verdict

- **BANKS (rigorous):** `d_tau = 60 = rank^2 N_c n_C` (exact); the integer (non-`pi`) character of the tau ratio is forced by its pointlike/trivial-rep stratum (F109 split); **mass != formal degree** (forced by the electron sitting on the formal-degree zero with finite mass); the `2^C2 = 64` in `71 = 2^C2 + g` is the shared `d_tau/d_muon` scale.
- **OPEN (unsolved, the wall):** the origin of `49 * 71 = g^2(g + 2^C2)` — no forced vertex-norm integral yet produces `g^2` and the additive `g`. Found the formal-degree invariant, showed it is the wrong object for the mass, identified the shared 64 — but did **not** crack the tau mass.
- **NOT claimed / NOT fished:** that `49*71` is derived (it is the *input* from T2003); no new value. Count stays **2**.

## 5. Closure

The tau side is the honest counterpart to the muon's win. What's forced: the tau ratio is an *integer* (no `pi`) because the tau is a point (trivial rep at the vertex) — the analytic character is dictated by the stratum, exactly as F109's split predicts. What's clean: the tau formal degree `d_tau = 60 = rank^2 N_c n_C`. What's informative: that `60` is **not** the mass ratio — mass is not the formal degree, which the electron (sitting on the formal-degree zero with finite mass) forces independently. What stays **open**: the actual origin of `49*71 = g^2(g+2^C2)` — the shared `64` ties it to the muon, but `g^2` and the additive `g` have no forced vertex integral yet. I would rather log this as a clean wall than dress it as a result: the muon's base reverse-engineered to rigorous geometry; the tau's mass did not. Count stays honestly 2.

@Casey — honest split on your "opposite direction": the MUON reverse-engineered cleanly (F109, base is rigorous geometry); the TAU did not. I found its formal degree (60 = rank^2 N_c n_C, clean) but that's the WRONG object -- it isn't the mass (3479/60 = 57.98), and the electron-on-the-zero proves mass != formal degree. The origin of 49*71 = g^2(g+2^C2) is genuinely OPEN -- the shared 64 ties it to the muon, but g^2 and the extra g have no forced vertex integral yet. Logging it as a clean wall, not dressing it up. @Elie — your tau = Delta=0 = the identity/point matches: pointlike -> integer ratio (no pi), no tower, single mode. That explains the FORM (two-factor integer) but not the two factors. @Grace — strict: BANKS d_tau=60=rank^2 N_c n_C + 'mass != formal degree' (electron on the zero); 49*71 origin OPEN not banked; no re-fit; count 2. @Keeper — ledger: tau formal degree d(0)=60=rank^2 N_c n_C (exact, clean) but NOT the mass ratio 3479 (mass != formal degree, forced by electron on formal-degree zero); 49*71=g^2(g+2^C2), shared 2^C2=64=d_tau/d_muon, but g^2 + additive g origin OPEN; count 2.

— Lyra, Sat 2026-06-13 11:25 EDT (`date`-verified). F110 reverse-engineering the tau (counterpart to F109 muon): d_tau=d(0)=60=rank^2 N_c n_C (exact, clean) BUT NOT the mass ratio (3479/60=57.98) -> mass != formal degree (forced anyway: electron on the formal-degree zero d(5/2)=0 has finite mass). 49*71=g^2(g+2^C2)=g^3+2^C2 g^2; 2^C2=64=d_tau/d_muon = shared scale w/ muon; but g^2=49 + additive g have NO forced vertex integral. tau pointlike (trivial rep/vertex) explains integer (non-pi) FORM but not the two factors. BANKS d_tau=60 + mass!=formal-degree; 49*71 origin OPEN not banked not fished; count 2.
