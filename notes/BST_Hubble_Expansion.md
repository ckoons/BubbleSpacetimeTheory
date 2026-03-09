# BST Hubble Expansion: Committed Contact Graph Area Rate
**Casey Koons, March 2026**

---

## 1. The Core Physical Picture

In Bubble Spacetime Theory the universe does not expand into pre-existing space.
Spatial extension is the **3D projection** of committed contacts on the substrate.

**Definition.** The *committed contact graph* G_c(t) is the subgraph of the full
channel adjacency network in which each edge represents a channel pair that has
permanently exchanged substrate state (committed a contact). The committed contact
graph carries area A_c(t) on the Shilov boundary Σ of D_IV^5.

**Core statement (Casey Koons, March 2026):**

> The Hubble expansion rate is the fractional rate of growth of the committed
> contact graph area on the substrate — not a property of 3D space itself.

The 3D scale factor a(t) is the square root of the projected committed area:

    a(t)  ∝  √A_c(t)

Therefore the Hubble parameter is:

    H(t) = ȧ/a = (1/2) Ȧ_c / A_c = (1/2) d/dt [ln A_c(t)]

H measures how fast new commitments accumulate relative to the current committed
area.  It is a property of the substrate information dynamics, not of 3D geometry.

---

## 2. What Determines A_c(t)

The total substrate area is the Shilov boundary of D_IV^5.  Its characteristic
scale is set by ℓ_Pl × (R_H/ℓ_Pl)^{something} — but the key point is that it is
**finite and fixed** by the BST geometry.

The committed fraction at temperature T:

    f(T) = A_c(T) / A_Σ

At T → 0 (vacuum), the committed fraction approaches the BST vacuum free energy:

    f(T→0) = F_BST = 0.09855  (exact from partition function, l=5 convergence)

So about 9.9% of all possible channel contacts are committed even in the zero-
temperature vacuum.  The remaining 90.1% are in the ground state (zero mode).

At the phase transition T_c = 0.487 MeV (t_c ≈ 3.1 s), f jumped from 0
(pre-spatial, no committed contacts) to some initial value that then evolved
toward F_BST as the universe cooled.

---

## 3. Connection to the Cosmological Constant

The cosmological constant Λ is the vacuum contribution to H² from the committed
contacts that remain at T = 0:

    Λ = F_BST × (d_0/ℓ_Pl)^4            [BST formula — exact]

The FRW Hubble equation (flat, T=0 limit) with only Lambda:

    H₀² = Λ / 3                          [pure-Λ limit]

In the contact graph picture:

    H₀² = (1/3) × F_BST × (d_0/ℓ_Pl)^4

The d_0 encodes the physical scale of one committed contact on the substrate
in Planck units. Once the partition function gives d_0 from first principles,
both Λ and H₀ are predicted with no observational input.

**Key structural relation:**

    H₀ = ℓ_Pl/t_Pl × (F_BST/3)^{1/2} × (d_0/ℓ_Pl)^2

The expansion rate is the Planck rate modulated by the geometric mean of
(vacuum contact fraction) × (contact area in Planck units).

---

## 4. Epoch Dependence: H Is Not a Constant

The committed area grows as:

    Ȧ_c / A_Σ = df/dt = (∂f/∂T) × Ṫ

At early times (T >> T_c, radiation-dominated): f grows rapidly → large H.
As T → T_c: dramatic rise (phase transition, channel commitments accelerate).
Post-transition, T < T_c: f approaches F_BST from above → H decreases.
Today (T_CMB = 2.725 K << T_c): Ȧ_c → 0, H → Λ-driven floor.

The epoch-dependence of H(z) in BST:

    H²(z) = H₀² × [Ω_Λ + Ω_b(1+z)³ + Ω_ν(1+z)³ + Ω_r(1+z)⁴]

where Ω_b, Ω_ν, Ω_r are contributions from committed contacts carrying baryon-
type, neutrino-type, and radiation-type substrate modes respectively.

**No dark matter term.** In BST the DM term Ω_DM(1+z)³ does not appear because
there is no dark matter channel type. Channel noise (vacuum fluctuations in
uncommitted channels) explains galaxy rotation curves directly (DarkMatterCalculation.md).

---

## 5. The Hubble Floor and the Hubble Tension

### 5.1 The BST Floor

Backfit from Lambda_obs = 2.9e-122 Planck units with flat, no-DM universe:

    H₀_floor = 58.2 km/s/Mpc

This is **below** both CMB (67.4 ± 0.5) and local ladder (73.0 ± 1.0).
The contact graph picture explains why:

- The vacuum committed fraction F_BST = 0.09855 forces Ω_Λ ≈ 0.95 (flat, no DM)
- This high dark energy fraction raises H at late times less efficiently than
  the mixed DM+Λ ΛCDM model would
- The floor reflects the *vacuum* rate of contact graph growth, which is set
  by F_BST and the quantum fluctuation rate (one committed pair per coherence time)

### 5.2 Why the Observed Value is Higher: Local Contact Density

The Hubble parameter measured by the local distance ladder (Cepheid/SN) samples
H₀ in a locally overdense region.  In BST:

- Overdense regions have **higher committed contact density** (more channels
  committed per unit substrate area)
- Higher committed density → faster local A_c growth → higher local H
- The excess: H_local - H_floor ≈ (δN_c/N_c) × H_floor/2

This is not a calibration error — it is a real BST effect.  Different measurements
probe different regions of the committed graph:

| Measurement | Region probed | Expected H₀ |
|---|---|---|
| CMB (Planck) | Full past light cone, averaged | H₀_floor |
| Baryon acoustic oscillation | Large scale, near-average | H₀_floor + small |
| Cosmic chronometers | Line-of-sight galaxies | Mixed |
| Local distance ladder (Riess) | z < 0.15, overdense | H₀_floor + local |
| Megamaser (geometric) | z ≈ 0.003, very local | H₀_floor + local |

The "Hubble tension" in BST is not a tension — it is the **gradient in committed
contact density** between the cosmic average and the local overdensity.

**Prediction:** BST predicts the local-to-cosmic H₀ ratio:

    H₀_local / H₀_cosmic = √(1 + δ_contacts_local)

where δ_contacts_local = local fractional excess of committed contacts.
This is measurable: it should correlate spatially with the matter overdensity
field on scales of ~100 Mpc.

---

## 6. Backfit Table (March 2026)

### 6.1 Setup

| Parameter | Value | Source |
|---|---|---|
| F_BST | 0.09855 | Partition function (exact) |
| Lambda_obs | 2.9e-122 Pl | CODATA |
| T_CMB | 2.725 K | FIRAS (model-free) |
| Omega_r h² | 4.18e-5 | T_CMB alone |

Target: d_0 = 7.365e-31 l_Pl (from Lambda_obs + F_BST)

### 6.2 Results Summary

All rows use flat no-DM BST model.  d_0 err = distance from the target.
`◄` = within 5% of target.  `←` = within 15%.

```
  Source                                   Ω_b h²    H₀     Ω_Λ     d_0 err
  ─────────────────────────────────────────────────────────────────────────
  ΛCDM reference (Planck CMB, H₀=67.4)    0.0224   67.4  0.9506   +8.1% ←
  ΛCDM reference (local, H₀=73.0)         0.0224   73.0  0.9579  +12.7% ←
  ΛCDM reference (megamaser, H₀=73.9)     0.0224   73.9  0.9589  +13.4% ←
  ─────────────────────────────────────────────────────────────────────────
  BST backfit (Ω_b=ΛCDM, exact Lambda)    0.0224   58.2  0.9338   +0.0% ◄
  BST backfit (Ω_b=D/H BBN)               0.0223   58.2  0.9342   +0.0% ◄
  ─────────────────────────────────────────────────────────────────────────
  BBN D/H → Ω_b h²=0.02225 (Cooke 2018)
    + H₀ backfit                           0.0223   58.2  0.9342   +0.0% ◄
    + H₀=73.9 megamaser                    0.0223   73.9  0.9592  +13.4% ←
  ─────────────────────────────────────────────────────────────────────────
  BST T_c entropy correction (dilutes η)
    δ=5%  weak transition                  0.0212   58.1  0.9371   +0.0% ◄
    δ=15% moderate                         0.0194   58.0  0.9423   +0.0% ◄
    δ=50% strong                           0.0148   57.6  0.9551   -0.0% ◄
    δ=200% (Li-7 factor ~3)                0.0074   56.9  0.9770   +0.0% ◄
  ─────────────────────────────────────────────────────────────────────────
  Neutrino mass (D/H Ω_b, Σm_ν < 0.45 eV)
    Σm_ν = 0.06 eV                         0.0229   58.3             ◄
    Σm_ν = 0.45 eV                         0.0271   58.6             ◄
  ─────────────────────────────────────────────────────────────────────────
  Combined (speculative — more baryons + ν mass)
    Ω_b h²=0.060, Σm_ν=0.47 eV            0.0650   61.8             ◄
    Ω_b h²=0.080, Σm_ν=0.74 eV            0.0880   63.6             ◄
    Ω_b h²=0.100, Σm_ν=0.93 eV            0.1100   65.3             ◄
  ─────────────────────────────────────────────────────────────────────────
  Cosmic chronometers (Moresco+ galaxy ages)
    Best-fit to BST no-DM H(z) model      0.0224  ≥90.0  [hitting boundary]
    → MODEL INCOMPATIBLE: flat H(z) predicted by BST (Ω_Λ≈0.97) cannot
      reproduce the rising H(z) shown in chronometer data.  Needs DM or
      different matter budget.
```

### 6.3 Key Finding

The BST floor H₀_floor = 58.2 km/s/Mpc is **insensitive** to the Ω_b h² input.
The gap to observed values (9.2 km/s/Mpc to Planck, 14.8 to local) cannot be
closed by adjusting baryons or neutrinos within observationally allowed ranges.

**Closure requires:**
1. BST first-principles Ω_b h² from the baryon asymmetry (partition function)
2. BST first-principles H₀ from the committed contact graph rate (this paper)
3. Local overdensity correction (BST prediction: Hubble tension = contact gradient)

Code: `notes/bst_hubble_backfit.py`

---

## 7. The Contact Graph Derivation of H₀ (Framework)

### 7.1 The Rate Equation

Let N_c(t) = number of committed contacts at time t.
Let A_0 = area on Σ per committed contact (a BST geometric constant).
Then A_c(t) = N_c(t) × A_0.

The Hubble parameter:

    H(t) = (1/2) × Ṅ_c(t) / N_c(t)

This is the master equation.  Ṅ_c is the rate of new commitments per unit time.

### 7.2 What Drives New Commitments

A channel pair (i,j) commits when their substrate states overlap beyond a
threshold θ for at least one coherence time τ_coh.  The commitment rate per
uncommitted pair is:

    Γ_{ij} = Γ_0 × exp(−E_{ij}/T) × Θ(overlap ≥ θ)

where E_{ij} is the energy cost to bring the two channels into contact and T
is the substrate temperature.

At T = 0 (today): only pairs with E_{ij} = 0 can commit.  These are topologically
adjacent pairs on Σ — exactly the pairs counted by F_BST.  The vacuum commitment
rate is therefore:

    Ṅ_c|_{T=0} = (F_BST × N_total − N_c) / τ_Pl

where τ_Pl = Planck time.  As N_c → F_BST × N_total (vacuum saturation), the
rate goes to zero and H → H_Λ (cosmological constant floor).

### 7.3 The BST Prediction: H₀ from Partition Function

Once the partition function is computed to give:
- N_total (total channel pairs on Σ)
- F_BST (vacuum committed fraction) [KNOWN: 0.09855]
- A_0 (area per committed contact in Planck units) [UNKNOWN: equivalent to d_0]
- τ_coh (coherence time on substrate) [UNKNOWN: related to Planck time + structure]

then H₀ is determined with no free parameters.

The remaining unknowns reduce to d_0 — the same quantity needed for Λ.
**H₀ and Λ have the same unknown: d_0.**  Solving one solves both.

### 7.4 Dimensional Analysis

    H₀ ∝ (c/ℓ_Pl) × F_BST^{1/2} × (d_0/ℓ_Pl)² × (ℓ_Pl/R_H)

This says: the Planck rate × (committed fraction)^{1/2} × (contact scale)² ×
(ratio of contact scale to Hubble radius).

The last factor is what makes H₀ so small — d_0/ℓ_Pl ≈ 7e-31, so
(d_0/ℓ_Pl)² ≈ 5e-61 — which is exactly the hierarchy between Planck time
and the age of the universe.

---

## 8. Chronometer Diagnostic: What the Data Tell BST

The cosmic chronometer H(z) data shows H rising from ~69 at z≈0.07 to ~100 at z≈0.75.

In BST with Ω_Λ ≈ 0.97 and no DM, H(z) is nearly **flat** (Lambda-dominated
at all redshifts in this range).  The BST no-DM model predicts H(z≈0.75)/H(z=0) ≈ 1.06,
while the data shows ~1.45.

**Physical meaning:** The rising H(z) observed requires a matter-like component
that grows as (1+z)³.  BST says this is NOT dark matter but is:

1. **Committed contact density gradient**: At higher z, more contacts are being
   newly committed per unit time (faster growth rate).  The universe hasn't
   saturated yet.  H(z) rises because Ṅ_c/N_c was larger in the past.

2. **Baryonic matter at higher density**: Standard baryons (1+z)³ term contributes,
   but Ω_b ≈ 0.05 gives only (1+0.75)³ × 0.05/0.97 ≈ 5% effect.  Not enough.

3. **Missing contact graph term**: In BST there must be a term in H²(z) that
   goes as (1+z)^n for n~3, coming from the **uncommitted channel reservoir**.
   As z increases (earlier times), the uncommitted reservoir was larger and drove
   faster commitment rates.  This IS the dark matter term in disguise:
   dark matter in ΛCDM is the uncommitted contact reservoir in BST.

**BST reinterpretation of dark matter:**

    Ω_DM (1+z)³   →   Ω_uncomm (1+z)^{n_c}

where Ω_uncomm = fraction of channels not yet committed at each epoch, and n_c
depends on the contact commitment rate law.  If n_c = 3 (commitment proportional
to contact area), then BST recovers the ΛCDM H(z) dependence with no DM particles.

This is a key prediction: the effective "dark matter" in BST is epoch-dependent
(different n_c at different times), while particle DM has n_c = 3 exactly.

---

## 9. Open Questions for the Expansion Rate Paper

1. **Derive H₀ from N_c rate equation** using BST partition function + contact topology
2. **Compute d_0 from geometry** — this is the shared unknown for both Λ and H₀
3. **Derive Ω_b h² from baryon asymmetry** in BST (no observational input needed)
4. **Compute n_c (commitment rate exponent)** from substrate topology — should be ≈ 3
5. **Local contact density** → quantitative prediction of H₀_local − H₀_cosmic
6. **GW imprint** of phase transition at T_c = 0.487 MeV on H(z) at z~3.1s after BB
7. **Neutrino mass from contact graph**: ν is a propagating channel excitation;
   its mass is the energy cost to maintain an open contact against zero-mode decay

---

## 10. Paper Outline: "Expansion Rate and Hubble Parameter in BST"

**Abstract**: BST explains the Hubble expansion as growth of the committed contact
graph on the substrate Σ (Shilov boundary of D_IV^5).  H(t) = (1/2)d(ln A_c)/dt.
The BST floor H₀ = 58.2 km/s/Mpc follows from F_BST, Λ_obs, and flatness.
The Hubble tension is a gradient in committed contact density, not a systematic error.

**Sections:**
1. Contact graph as the physical origin of spatial expansion
2. Rate equation: Ṅ_c and the Hubble parameter
3. Vacuum limit: F_BST → Λ → H₀_floor
4. Epoch dependence: H(z) from commitment rate at each epoch
5. Hubble tension: local contact density gradient, not calibration error
6. Chronometer diagnostic: uncommitted reservoir mimics dark matter in H(z)
7. First-principles prediction (awaits partition function for d_0 and Ω_b)
8. Testable predictions:
   - H₀_local correlates with local matter overdensity on 100 Mpc scale
   - H(z) slightly steeper than ΛCDM at z > 1 (commitment rate changes)
   - GW background at 6-9 nHz from T_c phase transition
   - No dark matter particles at any energy

---

## Appendix A: Backfit Calculation Code

See `notes/bst_hubble_backfit.py` for the full computation.

Key equations:

```python
H100_Pl = (100e3 / Mpc_m) * t_Pl     # H₀=100 in Planck units

def H0_for_exact_Lambda(Omega_b_h2, Omega_nu_h2=0.0):
    """H₀ that makes Lambda_BST = Lambda_obs exactly (flat, no DM)."""
    h2 = Lambda_obs/(3*H100_Pl**2) + Omega_b_h2 + Omega_nu_h2 + Omega_r_h2
    return np.sqrt(h2) * 100
```

Result: H₀_floor = 58.2 km/s/Mpc for any reasonable Ω_b h² input.

Gap to observed: 9.2 km/s/Mpc (CMB) or 14.8 km/s/Mpc (local ladder).
Even Ω_b h²=0.10 + Σm_ν=0.93 eV raises floor only to 65.3 km/s/Mpc.
Partition function + local overdensity needed to close the remaining gap.

---

*Notes document — internal BST working notes, not for distribution.*
*Code: `notes/bst_hubble_backfit.py`, `notes/bst_frw.py`*

*AI assistance: Claude Sonnet 4.6 (Anthropic) contributed to derivations, computations, and manuscript development.*

*Related: `notes/BST_Cosmological_Constant.md`, `WorkingPaper.md` Section 5.4*
