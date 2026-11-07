---
title: "Commitment cadence: setup. Margolus–Levitin floor, Landauer energy, and what 10^120 counts"
date: 2026-11-07
status: PROPOSAL (Casey GO 2026-11-07 for the setup). Definitions and numbers only; nothing here is tiered Derived.
builds_on: K1919, K1920 ("Time, Derived" addendum), T262, the commitment-record rule
---

# Commitment cadence: setup

## 1. The question

K1920 settled the elementary tick as ħ/E "for the energy at hand" and withdrew the 10⁻¹²⁰ s
figure. That figure was never a time; its only ancestor is a count per Planck time (K1919). K1920
names a third object, still open: the **cadence of commitments**. BST should be able to state a
minimum cadence and a commitment energy. This note sets up both on ground that is already
proved, so that what remains is one BST number.

## 2. Definition: a commit is a transition to a distinguishable state

A commitment leaves a record, and a record is a state that can be told apart from what came
before. In quantum terms that means an orthogonal state. Two theorems then bound the cadence,
with no BST input:

- **Margolus–Levitin (1998).** A system of mean energy E above its ground state needs at least
  τ ≥ πħ/(2E) to reach an orthogonal state.
- **Mandelstam–Tamm (1945).** τ ≥ πħ/(2ΔE), using the energy spread instead of the mean.

**Proposed definition.** The commitment cadence is τ_commit = πħ/(2E_commit). This is K1920's
ħ/E with the factor π/2 that the theorem supplies. BST's open task reduces to one number,
**E_commit**.

## 3. The commitment energy is the Landauer cost (Casey: intrinsic to BST)

BST is built on geometry and information theory. K1920 already states that a commit is a
Landauer write at the local temperature. Erasing or committing one bit costs at least
k_B T ln 2. So the information-theoretic commitment energy is

> E_commit = k_B T ln 2, giving τ_commit = πħ / (2 k_B T ln 2).

**An empirical anchor already exists.** "Planckian" metals relax at a rate of about k_BT/ħ, and
that bound is observed but unexplained. If a commit is a Landauer write, Planckian dissipation
is the commitment cadence seen in a solid. That is a candidate cross-domain test. It needs a
toy and a literature check before it is claimed.

## 4. The three candidates, computed

| Candidate | E_commit | ħ/E | Margolus–Levitin floor πħ/2E |
|---|---|---|---|
| A. Planck energy | 1.221 × 10²⁸ eV | 5.39 × 10⁻⁴⁴ s (= t_P) | 8.47 × 10⁻⁴⁴ s |
| B. Electron, m_e c² (lightest record of charge Q) | 5.110 × 10⁵ eV | 1.288 × 10⁻²¹ s | 2.023 × 10⁻²¹ s |
| $B'$. Proton, m_p c² (lightest record of baryon number B) | 9.383 × 10⁸ eV | 7.02 × 10⁻²⁵ s | 1.102 × 10⁻²⁴ s |
| C. Landauer at the CMB temperature (2.7255 K) | 1.628 × 10⁻⁴ eV | 4.04 × 10⁻¹² s | 6.35 × 10⁻¹² s |
| C. Landauer at 300 K | 1.792 × 10⁻² eV | 3.67 × 10⁻¹⁴ s | 5.77 × 10⁻¹⁴ s |

(Constants: CODATA 2018. Scratch computation; toy number pending, see Section 8.)

## 5. Making A and B BST-native

**A: the minimum cadence.** (π/2)·t_P is the floor of all floors. BST takes Planck units as its
ruler, though, so stating it is a consequence of the ruler, not a derivation. The BST-native
version runs the ladder m_e = 6π⁵α¹²m_Pl (K1953, Identified) in reverse:
t_P = ħ/(m_Pl c²) = 6π⁵α¹² · ħ/(m_e c²). The Planck cadence is then 6π⁵α¹² times the electron
cadence. If the ladder's exponent 12 = 2C₂ is ever derived (one α per boundary-to-bulk step,
say), the minimum cadence becomes **derived relative to the electron**. Until then it stays
Identified.

**B: record cadences.** Under the commitment-record rule, each superselected charge has its own
lightest carrier, and so its own cadence: the electron for Q, the proton for B. The ratio of the
two cadences is m_p/m_e = 6π⁵ (Derived). So the proton-to-electron mass ratio can be read as the
**ratio of the commit rates of baryon records to charge records**. This is a re-reading of a
banked result, not a new number. It is still worth stating, because it puts the derived core
into cadence language.

**Unifying B and C (hypothesis).** A record of type X becomes permanent when the environment can
no longer afford to erase it, that is, when k_B T ln 2 falls below E_X. For the electron that
happens at T ≈ 8.6 × 10⁹ K (k_BT ≈ 0.74 MeV), and for the proton at T ≈ 1.6 × 10¹³ K
(k_BT ≈ 1.35 GeV). For the electron this is the right order of magnitude for the e⁺e⁻
annihilation epoch (k_BT ≈ 0.1–0.5 MeV). **For the proton it fails as stated.** Standard
nucleon–antinucleon freeze-out happens near k_BT ≈ m_p/40 ≈ 20 MeV, and the QCD transition
near 155 MeV, both far below 1.35 GeV. Standard cosmology puts freeze-out at T ≈ m/20 to m/40
because of Boltzmann suppression and annihilation rates, not at T ≈ m. So the naive
"k_BT ln 2 = E_X" rule is at best a ceiling, and any BST version must reproduce the m/20–m/40
factor. That makes it a hypothesis to sharpen or drop, not a result. It is recorded here because
the electron case is suggestive and the proton case is a clean falsifier.

## 6. What 10¹²⁰ counts (Casey's reading)

Lloyd (2002) estimated that the observable universe has performed about 10¹²⁰ elementary
operations. Casey's reading: 10¹²⁰ is the number of commitments it takes to render the universe,
a count and not a time. That fits K1919's finding that the old figure's only ancestor was a count
per Planck time. It also fits Margolus–Levitin directly:

- N ≈ 2E t/(πħ), and with E of order the mass-energy within the horizon, N ≈ (t₀/t_P)² ≈ 6.5 × 10¹²¹
  for t₀ = 13.79 Gyr.
- The serial interval, the universe treated as one system committing once, is
  t₀/N ≈ t_P²/t₀ ≈ 6.7 × 10⁻¹⁰⁵ s, which is πħ/(2E_total). It is K1920's ħ/E with E the total
  energy.

**Consequence:** N grows as t², so 10¹²⁰ is a *running* count. It cannot be a constant of nature,
which is why it failed as a fixed tick. If BST wants to bank this, the native statement is the
scaling N ∝ (t/t_P)², not the number.

## 7. Open questions, in order

1. **Is E_commit fixed or local?** Is it one geometric number (B), or the local Landauer cost
   (C), with B as a threshold case? The Section 5 hypothesis says both, but its naive form
   already fails for the proton.
2. **Freeze-out check.** Compare k_B T ln 2 = E_X with the standard freeze-out temperatures for
   e±, nucleons and light nuclei. Correct for g* and for the Boltzmann suppression that standard
   cosmology uses.
3. **The Planckian-metal check.** Is the observed scattering rate α_P·k_BT/ħ, with α_P ≈ 1,
   consistent with πħ/(2k_BT ln 2)? Note that π/(2 ln 2) ≈ 2.27.
4. **Ladder derivation.** Deriving 12 = 2C₂ would turn A from Identified into derived relative to
   the electron.

## 8. Toy (pending a number)

The planned toy computes Section 4, the freeze-out comparison (Section 7, item 2) and the
Planckian ratio (item 3), with a SCORE line. `play/.next_toy` is not present in the cloud clone,
so per the `/toy` rule no toy file was created. Casey or a local CI should claim a number and
file it. The scratch script reproduces Section 4 exactly.
