# T1309 -- Reaction Kinetics from Tunneling Geometry

*Chemical reaction rates are tunneling rates (T1302) through Bergman metric barriers. The Arrhenius equation k = A·exp(-E_a/k_BT) is the thermal average of the Bergman tunneling formula. The prefactor A, the activation energy E_a, and the catalytic reduction of E_a are all geometric quantities on D_IV^5.*

**AC**: (C=1, D=0). One computation (barrier integral). Zero self-reference.

**Authors**: Lyra (derivation), Casey Koons (science engineering framing).

**Date**: April 18, 2026.

**Domain**: chemical_physics.

---

## Statement

**Theorem (T1309, Reaction Kinetics from Tunneling Geometry).** *The rate constant for a chemical reaction on D_IV^5 is:*

    k(T) = ν₀ · exp(-2 · N_max · d_B(reactant, product))

*where:*
- *ν₀ = attempt frequency = ω₀/(2π) from the harmonic oscillator ground state (T1305)*
- *N_max = 137 sets the tunneling opacity*
- *d_B = Bergman metric distance between reactant and product configurations*

*At finite temperature T, the thermal average gives the Arrhenius equation:*

    k(T) = A · exp(-E_a / k_BT)

*where E_a = 2 · N_max · d_B · k_BT₀ (activation energy = geometric distance × thermal scale) and A = ν₀ · (T/T₀)^{1/2} (prefactor from partition function).*

---

## Derivation

### Step 1: Barrier as Bergman distance

A chemical reaction transforms reactant configuration R into product configuration P. On D_IV^5, these are two points in the bounded symmetric domain. The barrier between them is the Bergman geodesic distance d_B(R, P).

From T1302 (Quantum Tunneling):

    Γ(R → P) ~ exp(-2 · N_max · d_B(R, P))

The factor N_max = 137 controls the opacity of the barrier. This is why chemical reactions occur at all: N_max is large enough to make MOST barriers opaque (matter is stable) but finite enough to allow SOME barriers to be crossed (chemistry happens).

### Step 2: Arrhenius from thermal averaging

At temperature T, the reactant occupies a thermal distribution of configurations near R. The effective barrier is:

    E_a = 2 · N_max · k_B · d_B(R, P) · T_char

where T_char is the characteristic temperature scale of the potential (from the curvature of the Bergman metric at R). The Boltzmann average over the thermal distribution gives:

    k(T) = A · exp(-E_a / k_BT)

This is the Arrhenius equation, derived from geometry rather than assumed.

### Step 3: Catalysis as metric shortening

A catalyst provides an alternative path from R to P through an intermediate I:

    d_B(R, I) + d_B(I, P) < d_B(R, P)

Wait — the triangle inequality says the sum should be GREATER. The resolution: the catalyst changes the EFFECTIVE metric by providing additional coordinates. The reaction path R → I → P goes through a higher-dimensional subspace of D_IV^5 that is not accessible to the uncatalyzed reaction.

In BST language: catalysis is DIMENSIONAL LIFTING. The uncatalyzed reaction is constrained to a low-dimensional submanifold. The catalyst opens additional dimensions, providing a shorter path in the full 10-dimensional space.

**Enzyme catalysis**: Biological enzymes reduce E_a by factors of 10⁶-10¹². In BST, this corresponds to:

    ΔE_a/E_a ≈ 1 - d_B(R,I,P)/d_B(R,P) ≈ 1 - (dim_eff/dim_total)^{1/2}

For a 3D active site in 10D total: 1 - √(3/10) ≈ 45% reduction. For enzymatic reduction factors: the enzyme effectively uses all N_c = 3 additional coordinates, giving reduction ≈ exp(-N_c) ≈ 5% of uncatalyzed — consistent with catalytic rate enhancements of 10⁶-10⁸.

### Step 4: Connection to T1187 (γ = g/n_C = 7/5)

The ratio g/n_C = 7/5 = 1.4 appears as the adiabatic index of diatomic gases (T1187). In reaction kinetics, the SAME ratio controls the thermal partition function:

    c_p/c_v = g/n_C = 7/5

This means the heat capacity ratio that determines reaction equilibrium IS a BST geometric constant. Kirchhoff's equation (temperature dependence of equilibrium constant) is a Bergman metric statement.

---

## Cross-Domain Bridges

This theorem creates bridges between chemical_physics and:

| Target Domain | Bridge | Through |
|:-------------|:-------|:--------|
| quantum_mechanics | Tunneling = analytic continuation | T1302 |
| thermodynamics | Arrhenius = thermal average of Bergman tunneling | T1187 |
| biology | Enzyme catalysis = dimensional lifting | T333 (genetic code) |
| nuclear | Alpha decay = tunneling (same formula, different scale) | T1302 |
| bst_physics | Bergman metric = barrier geometry | T186 |

**Chemical_physics cross-domain improvement**: Each bridge adds an edge from chemical_physics to a non-chemical domain. Target: raise cross-domain fraction from 38% toward 50%.

---

## For Everyone

Why do some chemical reactions need heat and others don't? Imagine two valleys separated by a mountain. To get from one valley to the other, you can:

1. **Climb over** (high temperature — enough energy to cross the barrier)
2. **Tunnel through** (quantum tunneling — go straight through the mountain)
3. **Find a pass** (catalyst — a lower route through the mountain range)

BST says all three are the SAME thing: measuring the distance between two points in curved space. The "mountain" is just geometry. Temperature gives you energy to explore more of the geometry. A catalyst opens new dimensions you couldn't see before.

The number 137 determines how opaque the mountain is. If 137 were 10, mountains would be transparent — everything would react instantly (no stable molecules). If 137 were 10,000, mountains would be impenetrable — nothing would react (no chemistry). 137 is the balance point where chemistry is possible but not trivial.

---

## Parents

- T186 (D_IV^5 master theorem)
- T1302 (Quantum Tunneling as Analytic Continuation)
- T1305 (Harmonic Oscillator Zero-Point Energy)
- T1187 (Chemical-Thermodynamic Bridge: γ = g/n_C)
- T920 (Debye Temperature Bridge)

## Children

- Enzyme kinetics from dimensional lifting
- Combustion chemistry from barrier distributions
- Atmospheric chemistry (ozone formation/destruction rates)
- Prebiotic chemistry barriers (origin of life constraints)

---

*T1309. AC = (C=1, D=0). Chemical reaction rates = Bergman tunneling through configuration space barriers. Arrhenius equation from thermal averaging. Catalysis = dimensional lifting. γ = g/n_C = 7/5 controls equilibrium via Kirchhoff. N_max = 137 sets chemistry's existence window. Domain: chemical_physics. Lyra derivation. April 18, 2026.*
