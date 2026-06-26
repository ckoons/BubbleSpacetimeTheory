---
title: "Lane B setup (Grace, geometric/rep-theory input for Elie's engine + Lyra's Di rep) — the quark extension is K313 UNBLOCKED, not a fresh hunt. Two weeks ago K313 had: m_μ/m_e = N_c²·m_s/m_d at 13% (Georgi-Jarlskog form RECOVERED, color axis anchored), down/lep = 1/N_c² color-pinned, up-type GJ-anomalous (the 2.84 under-constrained), three fork-free sector numbers {up/lep, down/lep, up/down}={2.84, 0.097, 29.4}. It was bottlenecked on TWO things: (1) #418 color resolution, (2) the absence of a mass generator. BOTH landed this week — #418 resolved (V_a covariant, T2496), and d(ν)×deposit-locus = the mass generator. So Lane B = K313 with its bottleneck removed. GEOMETRIC EXTENSION of my Lane A pin: lepton measurement little group SO(4) (exponent 6, color-singlet) → quark little group SO(4) × color-fiber (a=N_c, F92); the mass-determinant picks up the color fiber → N_c² in the sector ratio (matches K313's anchored down/lep). DOWN sector + leptons = clean color rule = ROW candidate. UP sector = GJ-anomalous, steeper, needs hypercharge/isospin = BOUNDARY candidate (per 'few asymmetries are the content', the up/down 29.4 asymmetry IS the content). FIVE-ABSENCE FLAG (my own sin²θ_W lesson): the GJ FORM (N_c² factors) is allowed as substrate color-counting (color fiber a=N_c, F92); the GJ GUT MECHANISM (SU(5)/SO(10) unification scale) is FORBIDDEN — derive N_c² from the color fiber in the little group, NEVER from a unification group. F95 SNEAKY-TRAP discipline (mine, K313) carried forward: if a formal-degree value lands near 2π=6.283, refuse the pull to call it 2π — close-but-not-equal is success, exactly-2π is a red flag."
author: "Grace"
date: "2026-06-26 Friday"
status: "Lane B geometric/rep-theory setup, handed to Elie (engine) + Lyra (Di/hypercharge rep). NOT a result — the setup that says where to fire and how to tier. Count HOLDS 4/26. Honest resist-prior carried: down sector ROW candidate, up sector BOUNDARY candidate, both real theorems."
---

# Lane B setup — the quark extension is K313 unblocked

Casey's "don't resist the obvious; find it in the corpus, don't re-derive" applies hard here. **The quark
extension is not a fresh hunt from zero — it is K313 with its bottleneck removed.** Two weeks ago the team
got most of the way and stalled on exactly the two things that landed this week.

## 1. What K313 already had (June 11) — don't re-derive this

- **Georgi-Jarlskog FORM recovered:** `m_μ/m_e = N_c²·(m_s/m_d)` → 207 vs 180, **~13% (inside the ~15% RG
  window).** The color axis of the sector rule is **anchored**, not fished.
- **`S_down/S_lep = 1/N_c²`** — the bulk-color fiber `a = N_c` (F92) shows up **squared** in the sector ratio.
- **Three fork-free sector numbers** (electron BF point ν=5/2 is common-mode, cancels): `{up/lep, down/lep,
  up/down} = {2.84, 0.097, 29.4}` — test the **color+charge sector only**.
- **Up-type is GJ-anomalous:** steeper hierarchy; GJ's clean `N_c` factors pin only the lepton–down relation;
  the up-type `2.84` was genuinely under-constrained.
- **The whole thing rode on #418** (four-CI convergence: the color/hypercharge chiral content).

## 2. The two bottlenecks both landed THIS week

1. **#418 color resolution** — color su(3) closes on H²(D_IV⁵) via the covariant `V_a` generators (T2496),
   unitary on the compact dual Q⁵. The color half K313 was waiting on is **in hand**.
2. **The mass generator** — `d(ν) × deposit-locus` (today's hub). K313 had no engine to turn the sector
   ratios into masses; now it does.

So Lane B = **run the deposit-locus engine on the color-extended little group, with the K313 color rule as
the structural anchor.**

## 3. The geometric extension (my Lane A pin → quarks)

My Lane A result: the lepton mass is the **curvature determinant over the measurement little group** —
`det_{Λ²(T_xS⁴)}(R)`, exponent `6 = dim so(4)`, color-singlet. The quark differs by **one thing**: it carries
color, so its measurement little group is **not `SO(4)` alone**:
```
lepton little group:  SO(4)                         → det over Λ²(T_xS⁴),  exponent 6
quark  little group:  SO(4) × (color fiber, a=N_c)  → det picks up the color fiber
```
The color fiber `a = N_c` (F92) entering the **determinant** is exactly why it shows up **squared** in the
sector ratio (`down/lep = N_c²`, K313). The geometry and the K313 phenomenology agree: **the N_c² is the
color fiber's contribution to the mass-determinant.** This is the diagonal-vs-off-diagonal question made
concrete:
- **DOWN + leptons:** color fiber contributes cleanly → `down/lep = N_c²` → **ROW candidate.** If the engine
  reproduces the down-quark ladder (m_s/m_d, m_b/m_s) from the color-extended determinant, masses move.
- **UP:** GJ-anomalous, steeper → the color fiber alone doesn't pin it; needs the full hypercharge/isospin
  content of the Di rep → **BOUNDARY candidate.** Per "few asymmetries are the content," the **up/down 29.4**
  is the substantive object, not a failure.

## 4. Concrete fire instructions

**Elie (engine):** run the deposit-locus integrator (the 4402/4403 machinery) with the color-extended little
group `SO(4) × (a=N_c fiber)` for the down sector first (cleanest, anchored). Report the color-trace
structure, the π-powers, and the rational coefficients **separately** (Cal #408: investigation unbounded,
banking disciplined). Target: does `det` over `Λ²(T S⁴) ⊗ (color fiber)` reproduce `down/lep = N_c²` and then
the down-quark ladder? Up sector second, expecting anomaly.

**Lyra (Di/hypercharge rep):** the down/up split is the **hypercharge/isospin content of the Di Δ=2 spinor**
(Cal #402: matter = Di, not Rac). The color half is anchored (a=N_c); the **open half is hypercharge** — which
member of the Di multiplet each quark is, and why up is steeper. This is also the matter-rep + 3-generation
reconciliation (the consolidation item) — same rep, so do them together.

## 5. Discipline carried forward (both mine)

- **FIVE-ABSENCE (my sin²θ_W lesson):** the Georgi-Jarlskog **form** is allowed *only* as substrate
  color-counting (color fiber `a=N_c`, F92). The Georgi-Jarlskog **GUT mechanism** (SU(5)/SO(10) unification
  scale, X/Y bosons) is **forbidden** by Five-Absence. Derive `N_c²` from the color fiber in the little group;
  **never** from a unification group. If the down ladder only closes by importing a GUT relation, that's a
  forbidden value, not a win — same trap I fell into with 3/8.
- **F95 SNEAKY-TRAP (mine, K313):** if any formal-degree value lands near `2π = 6.283`, **refuse** the pull to
  call it 2π. Close-but-not-equal is what success looks like; exactly-2π would be a red flag (means the
  measure didn't cancel). Values come from rep-theory formal degrees, not proximity coincidence.
- **Target-innocence both directions (Elie's lens):** the color fiber `a=N_c` and the exponent structure must
  be substrate-structural and innocent of the observed quark masses. If the only way to hit `m_s/m_d` is to
  tune the fiber, it's FIT-suspect, not derived.
- **Resist-prior honest:** quarks were an honest negative before #418 + the generator. Both exist now, so the
  question is genuinely re-opened — but go in expecting EITHER the down-row OR the up-boundary, both real.

— Grace, 2026-06-26 Friday. Lane B = K313 unblocked. Color half anchored (down/lep=N_c²); the curvature
determinant extends to SO(4)×color-fiber; down=ROW candidate, up=BOUNDARY candidate; Five-Absence + F95 +
target-innocence carried. Handed to Elie (engine) + Lyra (Di/hypercharge). Count HOLDS 4/26.
