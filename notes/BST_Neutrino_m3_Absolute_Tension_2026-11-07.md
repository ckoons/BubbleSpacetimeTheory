---
title: "Neutrino m_ν3: the absolute value is ~3.8σ low (the ratio test hid it)"
date: 2026-11-07
for: Keeper (ruling and tier), Lyra (F456 owner), Grace (data layer), Cal (referee log)
status: FINDING. No tier changed; the data row is annotated, not re-tiered.
---

# Neutrino m_ν3: the absolute value is ~3.8σ low

## The finding

BST's boundary-seesaw forms have no free parameter: the scale α²m_e²/m_p is fixed, and so are
the coefficients.

- m_ν1 = 0
- m_ν2 = (7/12)·α²m_e²/m_p = 0.008645 eV
- m_ν3 = (10/3)·α²m_e²/m_p = 0.049399 eV

With m_ν1 = 0, the masses are the square roots of the measured splittings, so each can be scored
absolutely against NuFIT 6.0 (normal ordering):

| Quantity | BST | NuFIT 6.0, IC19 variant | z | NuFIT 6.0, IC24 + SK | z |
|---|---|---|---|---|---|
| m_ν2² = Δm²₂₁ | 7.473 × 10⁻⁵ eV² | 7.49 ± 0.19 × 10⁻⁵ | −0.09 | 7.49 ± 0.19 × 10⁻⁵ | −0.09 |
| m_ν3² = Δm²₃₁ | 2.440 × 10⁻³ eV² | 2.513 (+0.021/−0.019) × 10⁻³; 3σ range 2.451–2.578 | **−3.8** | 2.534 (+0.025/−0.023) × 10⁻³; 3σ range 2.463–2.606 | **−4.1** |
| Σm_ν | 0.05804 eV | the m_ν1 = 0 sum from data is 0.05878 | | 0.05899 | |

m_ν2 is excellent. **m_ν3 lies below the 3σ range in both NuFIT variants.** So the BST sum,
0.058 eV, is *below* the minimum that oscillation data allow when m_ν1 = 0.

## Why it was missed

F456 (Lyra, 2026-07-03) scored only the ratio, m_ν3/m_ν2 = 40/7 = 5.714 against 5.824 ± 0.088,
which is 1.25σ. The ratio's error is dominated by the 2.5% uncertainty on Δm²₂₁, so a 1.5% miss
in m_ν3 disappears inside it. Meanwhile the catalog row const_061 compared against a rounded
"0.05 eV, NuFIT 2024" with no uncertainty, which made the row look like a 1.2% structural match.

## Dates (for the prediction-before-data question)

The forms, and the sum 0.058 eV, appear in `data/bst_seed.md` at its first commit
(eb311fcd, 2026-04-14). That is after DESI DR2 (March 2025) and after the splittings were
measured. **Σ = 0.058 eV cannot be claimed as a prediction made before the data.** The part that
is forward-looking is m_ν1 = 0, together with the Majorana reversal of 2026-07-16.

## What survives

- **m_ν1 = 0** (rank-2 geometric Majorana matrix, T2563/T2524). Combined with the measured
  splittings it gives **Σm_ν = 0.0588–0.0590 eV**, the normal-ordering minimum. Recommended as
  the headline neutrino prediction. It sits just under DESI's latest ΛCDM bound (< 0.0592 eV,
  95%, DESI DR2 BAO + Lyα full shape + CMB).
- **m_ν2 = (7/12)·α²m_e²/m_p** at −0.09σ.

## What not to do

The miss is 1.46% in m_ν3, close to 2α (1.46%). Multiplying by (1 + 2α) would land almost
exactly on the data. **Unless a mechanism forces that factor, it is a fit-tell.** It is the
same pattern the gates retired in const_022 (the 44/45 suffix). Write it down as a hypothesis
to test only if the radiative structure of the seesaw predicts it in advance.

## Recommended rulings (Keeper)

1. Change the headline neutrino prediction from "Σ = 0.058 eV" to "m_ν1 = 0, so Σ equals the
   normal-ordering minimum, ≈ 0.059 eV".
2. Mark m_ν3 = (10/3)·α²m_e²/m_p as **in tension (−3.8σ)**. Either withdraw the 10/3 form or
   route it into the non-match pipeline with the absolute score, not the ratio.
3. Add the absolute-not-ratio check to the scoring rules wherever a ratio's error is dominated
   by its less precise member.
4. Update `data/bst_seed.md` and `bst_predictions.json` once ruled. Not done here: the ruling
   is Keeper's.

## Applied today

`data/bst_constants.json` const_061 and const_062 now carry NuFIT 6.0 observed values with
uncertainties. const_061 has a `tension_2026_11_07` field. Tiers are unchanged.

The computation was a scratch script outside the repo. It needs a toy number:
`play/.next_toy` is not in the cloud clone, so per the `/toy` rule no toy was created. Casey
or a local CI can claim one and file it.

## Applied 2026-11-07, 18:14 (Casey: "please include all that you recommend")

- **Rulings 1 and 4 applied.** `data/bst_seed.md` and `data/bst_predictions.json` (pred_003)
  now give Σ as the normal-ordering minimum, 0.0588–0.0590 eV, from m_ν1 = 0 plus the measured
  splittings. The m_ν3 form carries its −3.8σ flag. pred_003 also records the newest DESI bound
  (< 0.0592 eV, ΛCDM, DESI DR2 BAO + Lyα FS + CMB, arXiv:2607.27410).
- **Ruling 2 applied as a flag, not a withdrawal.** The 10/3 form stays in the catalog, marked
  in tension. Whether to withdraw it or route it to the non-match pipeline is still Keeper's
  call.
- **Ruling 3 is proposed to Cal, not written into the referee log**, which Cal maintains with
  hashed entries. Proposed standing rule: *when a ratio's error is dominated by its less precise
  member, also score the more precise member absolutely.*
- **New catch while editing (Rosetta C16):** pred_003 and `data/bst_particles.json` called ν₁
  "the Z₃ Goldstone mode". A discrete symmetry such as Z₃ has no Goldstone modes, since
  Goldstone's theorem needs a continuous symmetry. Both now read "the null direction of the
  rank-2 geometric Majorana matrix, protected by Z₃", with the old wording kept.

## The BST route to improving m_ν2 and m_ν3 (proposal; needs agreement before any toy)

The masses and the PMNS angles are the eigenvalues and eigenvectors of **one** matrix, the
geometric Majorana matrix M, written in the charged-lepton frame (R52: "mixing lives in the
texture"). BST currently fits these separately: two rational coefficients (7/12, 10/3) for the
masses, and identified fractions for the angles (θ₂₃ → 4/7, θ₁₃ → 1/45, θ₁₂ pending). A single
rank-2 M fixes five observables at once (m₂, m₃ and three angles; m₁ = 0 is its null vector),
so the system is over-determined and therefore resistant to fitting.

The proposed test: build M = U*·diag(0, m₂, m₃)·U† from measured values, and separately from
BST's identified values. Then ask two questions. Does M have a form native to D_IV⁵, with
entries fixed by the strata and the Bergman norms? Does any such form move m₃ up by about 1.5%
*while* keeping the angles? If the angles and masses can't both be held, the coefficient
picture is wrong at the root.
