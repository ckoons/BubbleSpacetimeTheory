# Lyra R24: the fermion weight 7/2 is the Rac⊗Di ground weight. It is derived given Time, Derived's composite reading; no single-module point sits there

**Lyra, Wednesday 2026-09-30, 10:27 EDT (from `date`).**
- **v1.5 first:** Time, Derived v1.5 applied on Casey's GO (34e58617). Cal Section 1025: PASS.
- **Instrument:** `play/toy_5852_lyra_R24_…ground_7half.py`, sha256 `2127ad1af65a5b15…`, hashed and run at 10:26:47. **SCORE 5/5**, output `play/.out_toy_5852.txt`.
- **Order:** Cal's prediction (Section 1024) was hashed at 10:25. I read its subject at 10:26:54, **after my toy ran.** The toy's docstring (the predictions N3/N4/N5) was written blind to it, and the two agree independently (see below). I have not opened Cal's file.
- **didwe:** "spinor Wallach fermion weight 7/2" → F513 (07-12; the spinor-tower lift of the neutrino's shadow partner; CONDITIONAL). Related family, not this question; reconnected below.

**Group, family, action (stated first):**
- G = SO₀(5,2), 𝔤_ℂ = so(7,ℂ) = B₃, compact Cartan (e₁ = the clock, e₂, e₃ = SO(5)).
- Holomorphic positive noncompact roots p⁺ = {e₁ ± e₂, e₁ ± e₃, e₁}; ρ = (5/2, 3/2, 1/2).
- Spinor-valued highest-weight modules: lowest K-type the SO(5) spinor (½, ½) at clock weight λ.
- Harish-Chandra's discrete-series criterion: ⟨Λ + ρ, β⟩ < 0 for all β ∈ p⁺, with Λ = (−λ, μ).
- The singletons are pinned by K956: E₀(Rac) = 3/2, E₀(Di) = 2.

**Kill line (Keeper's, restated):** *"no natural spinor point at 7/2 means it's an identified input."*

---

## 1. The natural points of the spinor-valued family, and whether 7/2 is one

| point | scalar family (control) | spinor family | status |
|---|---|---|---|
| unitarity / first reduction | Wallach 3/2 (Rac) | **2 (Di)** (standard; K956) | known |
| Hardy-type (boundary values) | 5/2 | 3 (by the shift-by-½ analogy; **not derived here**) | analogy |
| holomorphic discrete-series edge | **4** (N1: computed, the control, = p − 1) | **9/2** (N2: computed exactly from the B₃ root data) | computed |
| Bergman-type | 5 (genus) | 11/2 (analogy) | analogy |

**7/2 is not among them** (N3). **No single-module natural point of the spinor family sits at 7/2.** Cal Section 1024 adds, and I agree (it is arithmetic): the points 2 and 3 are integer-weight spinors, so clock–spin **mismatched (W-odd)**. The discrete-series edge 9/2 and the Bergman analogue 11/2 are matched, but neither is 7/2.

## 2. Where 7/2 does sit: the ground weight of Time, Derived's fermion

- Time, Derived Section 7 reads a fermion as the **two-singleton composite Rac⊗Di**. Its lowest K-type is (trivial) ⊗ (spinor) = **the SO(5) spinor**, and its lowest clock weight is **E₀(Rac) + E₀(Di) = 3/2 + 2 = 7/2** (N4).
- z_t(7/2) = −1 = z_s(spinor), so it is **matched and W-even**, as the fermions must be (R20, K1944).
- **So ν = 7/2 is the ground weight of the lowest spinor summand of Rac⊗Di.** The weight that the Šilov placement *identified* (R23) is the weight that Time, Derived's composite reading *predicts*.
- **This reconciles K1653 with Time, Derived for fermions:** K1653's "substrate-Dirac" mode is a mode of the spinor-valued module H(7/2; spinor), the lowest summand of Rac⊗Di. The mode picture and the composite picture are one module here, not rival readings.

**Verdict on the kill line: it does not fire as stated, and it does not clear unconditionally.**
- **ν = 7/2 is DERIVED given Time, Derived's premise that the fermion is the Rac⊗Di composite.** That premise is in the paper, and v1.5 now marks it "(a premise; open per K1653)".
- It is **not** a natural point of the spinor family on its own (Section 1), so **without that premise it is an identified input.**
- **Tier: C (conditional on the composite premise); I without it.** Consistent with Cal's IDENTIFIED (Section 1023) plus the new route.
- **Two checks point the same way:** the Šilov-placed Yukawa fit (R23, IDENTIFIED) and the composite ground weight (this note, conditional-derived). They are independent routes to one number. **The remaining caveat from Cal Section 1023 stands:** the finite-t Yukawa match assumes the spinor K-matrix factor equals 1.

## 3. The g/2 coincidence: flagged, not used

2·(7/2) = 2E₀(Rac) + 2E₀(Di) = (n − 2) + (n − 1) = 2n − 3. BST's g = n + rank = n + 2. **They agree only at n = 5** (N5). K1201's "g = 7" and the composite's 2ν = 7 are thus two different expressions that coincide at BST's dimension. That is a menu risk (Cal Section 1024 flags it too). **It is not used as support**, and K1201 should not be re-worded as "ν = g/2 derived".

## 4. Reconnect: F513
F513 (07-12) lifted the neutrino's shadow-partner argument from the scalar ladder to the spin-½ tower (Wallach degeneration, the self-shadow centre). It is the same spinor family, a different question (Majorana vs Dirac). **If fermions sit at 7/2 in the composite reading, F513's spinor-tower points should be re-checked against 7/2**: flag for Grace; not done here.

---
**For Cal:** Section 1 (the computed 9/2 edge; 2 and 3 W-odd, agreed); Section 2 (derived given the composite premise; tier C); Section 3 (the flag agreed).
**For Grace:**
- K1201 re-key: "ν = 7/2: identified by the Šilov placement (R23); derived given Time, Derived's Rac⊗Di premise (R24); **not** 'g/2 derived'".
- F513 re-check flag.
**For Keeper:** the round-24 kill line does not fire; the result is conditional-derived (tier C).
