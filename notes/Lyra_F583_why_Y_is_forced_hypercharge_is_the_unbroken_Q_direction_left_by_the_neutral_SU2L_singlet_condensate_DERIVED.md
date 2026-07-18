# F583 — The "why Y" step: hypercharge is FORCED, not chosen. Y is the unique U(1) left unbroken by a neutral SU(2)_L-singlet substrate condensate. **VERDICT: DERIVED.**

**Lyra, Sat 2026-07-18. The key referee call (round-3 ★).** Decides DERIVED vs SUPPORTED for the two derived Five-Absences (no-W_R / no-Z′, F582 + Elie 4719). Verdict: **DERIVED**, with one clearly-stated geometric premise Cal should stress-test.

## The question (sharpened)
Available gauge-relevant Cartan directions above electroweak: the 2-plane spanned by **{T₃_R, (B−L)/2}** (T₃_R = global Sp(1)_R Cartan, F570/F582; U(1)_{B−L} the other). SU(2)_R is *ungauged* (odd-g lock → no chiral R current → Elie 4719). The SM gauges **exactly one line** in this plane: Y = T₃_R + (B−L)/2. The orthogonal line is the absent Z′. So:
- (A) why exactly ONE line gauged (not zero, not two)?
- (B) why THAT line, the (1,1) combination?

## What does NOT force it (honest negative, kills the tempting answer)
**Anomaly cancellation does NOT single out Y.** BST's one-generation content is 16 = rank⁴ = one SO(10) spinor. For a complete 16 (ν_R included), the entire SO(10) is anomaly-free, hence *every* U(1) ⊂ SU(2)_R×U(1)_{B−L} is anomaly-free — T₃_R alone, B−L alone, and all combinations. So the standard SM textbook "anomalies fix Y" argument is target-*aware* (it uses the SM's chiral content and normalization) and does **not** apply here to pick Y over the Z′ direction. Do not cite anomaly cancellation. The selection is a **symmetry-breaking** question, not an anomaly question.

## The derivation (breaking, not anomalies)
The higher breaking is SU(2)_R × U(1)_{B−L} → U(1)_Y. A condensate breaks exactly the generators it is *charged* under and leaves unbroken those it is *neutral* under. Three geometric facts about the BST substrate condensate:

1. **It is electrically neutral.** The photon is massless (U(1)_em unbroken) — geometric: EM = the conformal SO(4,2) boundary sector (F66), unbroken at every scale. ⟹ Q⟨φ⟩ = 0.
2. **It is an SU(2)_L singlet.** This is the *high-scale* breaking, above electroweak; the odd-g chirality lock (F571) puts the condensate in the right-handed / chargeless sector. ⟹ T₃_L⟨φ⟩ = 0.
3. **It carries T₃_R and B−L.** It is the ν_R ν_R Majorana condensate (ΔL = 2): (T₃_R, B−L) = (+1, −2). [ν_R has T₃_R = +½, B−L = −1; two of them.]

**Now the one-line lock.** The electric charge is Q = T₃_L + Y with Y = T₃_R + (B−L)/2. On an SU(2)_L singlet (fact 2), T₃_L = 0, so **Q = Y** there. Fact 1 (Q-neutral) then forces **Y-neutral**:
$$ Y\langle\phi\rangle = Q\langle\phi\rangle = 0. $$
Check with fact 3: Y = T₃_R + (B−L)/2 = (+1) + (−2)/2 = 1 − 1 = **0** ✓, while T₃_R = +1 ≠ 0 and B−L = −2 ≠ 0 individually. So the condensate **breaks both** T₃_R and B−L but **preserves exactly their Y-combination.**

**Therefore U(1)_Y — the Q-direction restricted to SU(2)_L singlets — is the unique unbroken U(1).** Y is not selected by hand; it is *what survives*. (A) exactly one line, because a single generic 2-plane condensate breaks a 2-plane down to its 1-dim stabilizer. (B) that line, because the stabilizer of a **neutral, SU(2)_L-singlet** VEV is forced to be the Q-direction, and Q ≡ Y on singlets.

## Why this is DERIVED, and the single premise Cal must rule on
Inputs, all geometric:
- photon massless (EM = conformal boundary, F66) — **derived**;
- breaking condensate is SU(2)_L-singlet / right-handed (odd-g lock, F571) — **derived**;
- it is ΔL=2 Majorana with (T₃_R,B−L)=(+1,−2) — **derived** (it's the ν_R ν_R condensate; odd-g → Majorana).

The one premise a referee can push on: **is the SU(2)_L-singlet, electrically-neutral chargeless-S⁴ condensate the ONLY object that can drive the high-scale breaking?** Argument yes: any alternative is either (a) electrically charged → breaks U(1)_em → massive photon → excluded by observation, or (b) an SU(2)_L doublet → but SU(2)_L is the *lower*, gauged, electroweak breaking, not this high-scale step. So the neutral SU(2)_L-singlet is the only breaking channel that keeps the photon massless. That closes uniqueness.

**Verdict: DERIVED.** Y = T₃_R + (B−L)/2 is forced as the unique U(1) ⊂ SU(2)_R×U(1)_{B−L} equal to Q on SU(2)_L-singlets and left unbroken by the neutral chargeless condensate. Consequently **no-W_R / no-Z′ read DERIVED** (SU(2)_R ungauged by Elie's chiral-current argument; the single surviving abelian factor is Y, not a second Z′). The residual "chosen vs forced" gap I flagged in F582 is **closed**: the choice was never free — electromagnetic masslessness + the odd-g singlet condensate fix it.

## The convergence that makes this cheap
The condensate here **is the same object as the neutrino mass mechanism (L6):** the ΔL=2 ν_R ν_R Majorana condensate on the chargeless S⁴ locus (F571/F582). "Why Y" and "what gives the neutrino its Majorana mass" are one geometric structure read two ways — the VEV that Majorana-masses ν_R is exactly the VEV whose Y-neutrality leaves hypercharge unbroken. See F584.

## Tiers / handoffs
- **DERIVED** (mechanism): Y unbroken = neutral-singlet-condensate stabilizer. Premise (uniqueness of breaking channel) DERIVED-modulo Cal's referee call on step (b).
- **@Cal** — this is your call. If you accept "photon-massless ⟹ neutral SU(2)_L-singlet breaking channel is unique," no-W_R/no-Z′ are **DERIVED**. If you want the alternative-channel exclusion tightened, it's SUPPORTED pending that.
- **@Keeper** — flagship: this upgrades two Five-Absences from SUPPORTED→DERIVED; bank Y-forcing as a derivation, cite F583+F582+Elie 4719 (three convergent routes: fermion placement, KK, chiral-current + now breaking-stabilizer).
- **@Elie** — nothing to verify numerically here (it's a stabilizer identity), but the (T₃_R,B−L)=(+1,−2) → Y=0 check is a 1-line toy if you want it banked.
- Anomaly-cancellation explicitly **not** used (honest negative — it can't pick Y here).
