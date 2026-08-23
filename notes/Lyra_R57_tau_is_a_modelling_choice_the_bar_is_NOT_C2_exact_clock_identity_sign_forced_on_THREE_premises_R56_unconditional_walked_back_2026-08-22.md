# R57 — τ: Cal's prior question answered, the bar corrected, the clock bound derived — and my R56 "UNCONDITIONAL" walked back

**Lyra, Sat 2026-08-22, restart round 57. Reconnected to primaries first (F778, §4751 frozen, my own R56) before deriving. Nothing pushed.**

## 0. Cal's prior question, answered plainly first

> **Is τ = ln a forced, or a modelling choice?**

**A modelling choice. It is not forced.** τ = ln a ⟺ κ = H exactly at all times (κ ≡ dτ/dt = the commit rate), i.e. the substrate tick rate tracks the Hubble rate identically. That is a dynamical coincidence, not a definition. F778 names the map as the open edge ("the τ↔a coupling map … must be computed from the geometry"); §4751's C7 lists κ as one of three unpinned knobs (F779, "the one unproved edge"). **Cal is right that a convention cannot fail.**

**The escape is not to force τ = ln a — it is to prove the inequality over the whole admissible clock class.** That converts a convention into a theorem that *can* fail (exhibit an admissible clock violating it and the sign prediction dies). Below I do that, and it costs three explicit premises.

## 1. The bar is NOT C₂. My R56 statement was wrong.

From F778/§4751, exactly (no approximation):
```
w + 1 = (1/3)·r(τ)·τ' ,   r ≡ −dlnρ_Λ/dτ = ⟨λ⟩_τ ,   ' ≡ d/d ln a
d(w+1)/dln a = (1/3)[ −Var_τ(λ)·τ'² + r·τ'' ]        (since dr/dτ = −Var)
⟹  w_a > 0  ⟺  τ'' < B(τ)·τ'² ,   B(τ) ≡ Var_τ(λ)/⟨λ⟩_τ = ⟨λ²⟩/⟨λ⟩ − ⟨λ⟩
```
**B is a function, not the constant C₂.** Over the *pre-registered* knob space (τ_now ∈ [0.10,0.30]; the three §4751 c_k profiles; c₀ scanned):

| | B |
|---|---|
| B_min | **0.93** (single-mode, c₀=0.1, τ=0.10) |
| B_max | **17.3** (equipartition, c₀=100, τ=0.10) |
| fraction of scan with B < 6 | **54%** |

C₂ = 6 = λ₁ is the **τ→∞ asymptote** of B, reached from below in the two-mode (c₀ + λ₁) limit — not the bar. My R56 line *"the bar is 6 = C₂ = the leading bleed rate"* is a **decorative clause bolted to an asymptote**: the number is defensible as a limit, the stated reason ("= the leading bleed rate", as if that *were* the threshold) is not. Proving "τ'' < C₂τ'²" would have been **the wrong inequality** — necessary-looking, not sufficient, over half the scan.

Also confirmed: with **c₀ = 0** (no non-bleeding zero mode), B → 0 and *any* τ'' > 0 flips the sign. **c₀ > 0 is load-bearing** and was not flagged as such.

## 2. What actually rescues the bar: data, not geometry

Small B requires the λ-distribution to be near-degenerate, which forces r ≈ λ₁ large, which forces |w+1| = (1/3)rτ' large — **already excluded by the measured w₀ ≈ −1.** Imposing the measured deviation as a cut (τ'=1 normalisation):

| cut on \|w+1\| | surviving B_min |
|---|---|
| ≤ 0.30 | 5.12 |
| ≤ 0.20 | **5.43** |
| ≤ 0.10 | 5.71 |
| ≤ 0.02 | 5.94 |

Monotone, → 6 as the cut tightens. **So the honest statement is: C₂ = 6 is the bar in the limit |w+1| → 0; at the measured deviation the bar is ≈ 5.4.** (Mechanism verified by direct scan; the B↔r anticorrelation that drives it is corr = −0.51 — real but only moderate, so the exclusion is *scanned*, not proved analytically.)

**This is a stronger result than the original claim, and it costs a measured input:** the bar's floor rides w₀, which is data. The sign is therefore **not forced by geometry alone.**

## 3. The clock bound — exact identity, then the theorem

Writing T ≡ 1/κ (tick period in cosmic time), v ≡ H·T (tick period in Hubble times), s ≡ d ln T/d ln a:

> **τ''/τ'² = v · [ (3/2)(1+w_tot) − s ]**   — **exact.**

Verified numerically against finite differences on ΛCDM, 4/4 cases to <10⁻⁶, including:
- **proper/local clock** (s=0, v≈10⁻⁶⁰) → τ''/τ'² ≈ 10⁻⁶⁰
- **horizon clock** (s = (3/2)(1+w_tot), v=1) → **exactly 0. This *is* τ = ln a.**
- **v=1, s=0** → 0.465 — **this reproduces the "Koons-tick ≈ 0.5" of my R56 note**, which was |Ḣ|/H² and is now identified: it is the constant-tick-period clock at Hubble normalisation.

**T2573 (candidate) — the clock bound.** Under
- **C1** (sub-Hubble tick): v = HT ≤ 1 — the substrate commits at least once per Hubble time;
- **C2** (non-accelerating commit rate): s ≥ 0 — the tick period does not *shorten* as the universe expands;
- **C3** (NEC, matter+Λ era): (3/2)(1+w_tot) ≤ 3/2;

then **τ''/τ'² ≤ 3/2**, against a data-allowed bar **B ≥ 5.4** ⟹ **τ'' < Bτ'² with ≥ 3.6× margin ⟹ w_a > 0.** ∎

**C2 is the open link, and I will not paper it.** The support is Margolus–Levitin (κ ≤ 2E/πℏ) with E non-increasing under NEC + ρ ≥ 0 in expanding FRW ⟹ **κ_max** non-increasing. That bounds the *ceiling*, not κ itself; a clock running below its ceiling could still accelerate. Closing C2 needs either (i) commitment saturates its energy bound (BST-natural: commitment is not throttled), or (ii) a direct geometric derivation of κ.

**What a violation would require, for the record (so C2 can fail):** at v=1, reaching B≈5.4 needs s ≈ −4.9, i.e. the fundamental tick period shrinking ~140× per e-fold, sustained. Finite rate + positive energy do **not** exclude that by exhaustion — the available log-range (≈138 e-folds down to a Planck tick) affords ~28 e-folds of such contraction. **So Casey's framing — "finite Koons-tick rate + positive energy" — does not by itself close the theorem.** What closes it is C2's *direction* (κ non-increasing), which is a stronger and different statement than finiteness.

## 4. Walk-back, owned

My R56 concluded: *"the falsifier is UNCONDITIONAL as a sign test."* **That over-claimed.** Corrected:

> **The sign w_a > 0 is forced GIVEN (i) the measured w₀ ≈ −1 (which sets the bar floor B ≥ 5.4), (ii) c₀ > 0, and (iii) C1–C3 on the clock, of which C2 is a held premise.** Per the standing rule that a held premise caps the chain, the sign ships **conditional**, not unconditional.

**The FLOOR this walk-back sets** (it is not a demotion to nothing): the sign is forced for *every* clock without positive-power commit-rate scaling, and both natural clocks sit 3.6×–10⁶⁰× below the bar. The falsifier still **can fail** (DESI excluding w_a ≥ 0 at ≥3σ), so it remains a live test — it is its *unconditionality* that was oversold, not its content.

## 5. Consequences for §4751 (frozen — companion note, no edit)

The frozen file says the sign is *"forced by complete monotonicity"* **and** *"robust in 8/9 scan cases"* — Cal's flagged internal tension. This work resolves it:

> **Complete monotonicity (c_k ≥ 0) forces only the SPECTRAL half** (the −Var·τ'² term). It cannot force the total sign, because the coupling term r·τ'' is independent of it. **"Forced" and "8/9" are statements about different halves** — the first about the spectral term, the second a scan over clock maps and knobs. Both are true; neither is the whole sign.

That is a better reconciliation than "it's 8/9, robust-not-forced," and it is **consistent with** (I have not verified the identity of) the 9th case being a low-B corner. **@Cal — this belongs in the §4751 companion note, alongside the sign/amplitude correction you already ordered. No edit to the frozen file; the hash stands.**

**Inherited caveat, not opened here:** my analysis is the *local* derivative −dw/dln a|_{a=1}; the DESI w_a is a **CPL fit** over a range. Those signs can differ for non-linear w(a) (K1144's CPL-artifact thread). The pre-registration compares to a CPL posterior, so this is live.

## Handoffs
- **@Elie** — please reproduce independently: (a) B(τ) = Var/⟨λ⟩ over the §4751 knob space, is B_min ≈ 0.93 and does the |w+1| cut lift it to ≈5.4? (b) the exact identity τ''/τ'² = v[(3/2)(1+w_tot) − s]. **Report your numbers before reading mine.**
- **@Keeper** — for the curation pass: (i) "the bar is C₂ = 6" must not propagate as the threshold; (ii) the sign ships **conditional on C1–C3 + measured w₀ + c₀>0**, not unconditional; (iii) **separate finding**: Cal §352 (K1283) cites **T5230** as a theorem for the "simple SO(5,2) ruler" half of my simple-vs-product gate — **T5230 is not a registered theorem** (registry tops out at T2572; the only 5230 object is `play/toy_5230_AUG13_gate_not_cleared...`). Dead citation on a PD-tier gate. I have *not* shown the simple-ruler claim is absent under another number.
- **@Grace** — the "T-prefix" is overloaded between theorems and toys throughout the running notes (T2849–T2953 are toys). Subscript or re-prefix.
- **@Casey** — plain version below.

## Plain version
We had a prediction: dark energy is slowly settling *down* toward a constant value, not swinging past it. Whether that's right turns on a race between two things — how fast the substrate's "background hum" fades, and how fast the substrate's clock speeds up relative to the expanding universe. We'd said the finish line for that race sits at the number 6, and that no real clock could ever get there. **Two corrections.** First, the finish line isn't 6 — it moves, anywhere from 1 to 17 depending on settings we hadn't pinned. What pulls it back near 6 isn't the geometry, it's the *measurement* that dark energy is already very close to constant: that measurement rules out exactly the settings where the finish line would be low. Second, I found the exact formula for how fast the clock is running, checked it four ways, and it needs three assumptions — one of which I can't yet prove (that the substrate's clock doesn't *speed up* as the universe expands). So the prediction stands and can still be proven wrong by data, which is what we want — but I oversold it last round when I called it unconditional. It's conditional, the conditions are written down, and the margin is comfortable: about 3.6× on the worst natural clock.

— Lyra, R57. Counter unmoved (2573; T2573 is a *candidate*, not registered). Nothing pushed; CP existence-only.
