# T1325 -- Activation Energy as Bergman Metric Barrier Height

*Chemical activation energy E_a is the geodesic distance in the Bergman metric between reactant and product configurations on D_IV^5. The Arrhenius factor exp(-E_a/k_BT) is the Bergman kernel's decay along this geodesic. Catalysis = shortening the geodesic by opening additional D_IV^5 coordinates (dimensional lifting, T1309). Reaction equilibrium K = exp(-ΔG/RT) is the ratio of Bergman kernel values at the two endpoints. The universal gas constant R = N_A · k_B has BST interpretation: k_B is per-observer, N_A scales to the macroscopic Hamming block.*

**AC**: (C=1, D=0). One computation (geodesic distance). Zero self-reference.

**Authors**: Lyra (derivation).

**Date**: April 18, 2026.

**Domain**: chemical_physics.

**Predicted Bridge**: PB-5 (Flow↔Matter: thermodynamics ↔ chemistry).

---

## Statement

**Theorem (T1325, Activation Energy as Bergman Barrier).** *For a chemical reaction on D_IV^5:*

1. *Reactant state R and product state P occupy positions z_R, z_P in the bounded symmetric domain.*
2. *The activation energy E_a = d_B(z_R, z_TS) where z_TS is the transition state (saddle point on the Bergman metric geodesic) and d_B is the Bergman distance.*
3. *The Arrhenius rate k = A · exp(-E_a/k_BT) is the thermal average of the Bergman kernel decay: exp(-d_B/λ_T) where λ_T = k_BT/ℏω is the thermal de Broglie wavelength in the configuration space.*
4. *Catalysis reduces E_a by providing an alternative geodesic through additional D_IV^5 coordinates (T1309). The minimum catalytic reduction is E_a/C₂ = E_a/6 per additional coordinate.*

---

## Derivation

### Step 1: Configuration space as D_IV^5

A chemical reaction transforms a set of atoms from one bonding configuration to another. In BST, each configuration is a point in D_IV^5: the five matter dimensions encode bond lengths, angles, and electronic state. The transition between configurations follows a geodesic in the Bergman metric.

The Bergman distance between reactant and product:

    d_B(z_R, z_P) = arccosh(1 + 2|z_R - z_P|²/[(1-|z_R|²)(1-|z_P|²)])

This is the natural distance on D_IV^5 — the metric that the geometry itself provides.

### Step 2: The transition state

The transition state z_TS lies on the geodesic between z_R and z_P at the point of maximum potential energy. In the Bergman metric, this is the saddle point where the curvature changes sign — the point where the reaction "goes over the hill."

The activation energy:

    E_a = V(z_TS) - V(z_R) = ℏω · d_B(z_R, z_TS)

where ω is the characteristic frequency of the bond vibration and d_B is the Bergman distance to the transition state.

### Step 3: Arrhenius from thermal averaging

At temperature T, the system thermally samples the Bergman metric with characteristic length λ_T = k_BT/(ℏω). The probability of reaching the transition state:

    P(TS) ∝ exp(-d_B(z_R, z_TS)/λ_T) = exp(-E_a/k_BT)

This is the Arrhenius factor. The pre-exponential factor A comes from the partition function of the reactant configuration — the number of accessible states near z_R.

### Step 4: Catalysis as dimensional lifting

A catalyst provides additional coordinates for the reaction pathway. Instead of the direct geodesic from z_R to z_P (over the barrier), the reaction follows an alternative path through the catalyst's coordinates.

From T1309: each additional coordinate reduces the effective barrier by a fraction determined by the Bergman curvature. The maximum number of independent additional coordinates is C₂ = 6 (the dimension of the isotropy representation). Therefore:

    E_a(catalyzed) ≥ E_a(uncatalyzed) / C₂ = E_a / 6

A perfect catalyst reduces activation energy by at most a factor of 6. This predicts: no catalyst can reduce E_a by more than a factor of C₂ = 6 for a given reaction type.

### Step 5: Equilibrium from endpoint kernel values

The equilibrium constant:

    K = exp(-ΔG/RT) = K(z_P, z_P) / K(z_R, z_R)

is the ratio of Bergman kernel self-values at product and reactant positions. Favorable reactions (K > 1) have the product at a higher kernel density than the reactant — the product is "closer to the center" of D_IV^5.

---

## Predictions

**P1.** Maximum catalytic rate enhancement is bounded by exp(E_a · (1 - 1/C₂)/k_BT) = exp(5E_a/6k_BT). *Testable: survey catalytic enhancement factors across reaction types.*

**P2.** Enzyme catalysis approaches the C₂ = 6 limit (evolved to use all available D_IV^5 coordinates). Chemical catalysis typically uses fewer coordinates. *Testable: compare enzyme vs industrial catalyst enhancement factors.*

**P3.** Reaction equilibria correlate with Bergman kernel density at product configuration. *Testable: plot ln(K) against a structural descriptor of product "centrality."*

---

## Cross-Domain Bridges (PB-5: Flow↔Matter)

| From | To | Type |
|:-----|:---|:-----|
| thermodynamics | chemistry | **derived** (Arrhenius from Bergman thermal averaging) |
| thermodynamics | chemical_physics | derived (E_a = geodesic distance) |
| chemistry | biology | structural (enzyme catalysis approaches C₂ = 6 limit) |

---

## For Everyone

Why do chemical reactions need heat? Because the atoms have to climb over an energy hill to rearrange. The height of that hill — the activation energy — is the distance between "before" and "after" in the geometry of space.

A catalyst provides a shortcut — a tunnel through the hill instead of over it. BST says the best possible shortcut can reduce the hill by a factor of 6 (the number of independent directions in the geometry). Enzymes, which evolution has been optimizing for billions of years, come close to this limit. Industrial catalysts typically don't.

---

## Parents

- T1309 (Reaction Kinetics from Tunneling)
- T186 (D_IV^5 master theorem)
- T315 (Casey's Principle — entropy as force)
- T1312 (3/4 Isomorphism)

## Children

- Enzyme efficiency classification by D_IV^5 coordinate usage
- Catalyst design from Bergman geodesic optimization
- Reaction selectivity from curvature

---

*T1325. AC = (C=1, D=0). Activation energy = Bergman metric geodesic distance. Arrhenius factor = kernel decay. Catalysis bounded by C₂ = 6 (dimensional lifting). Bridge PB-5: Flow↔Matter WIRED. Domain: chemical_physics. Lyra derivation. April 18, 2026.*
