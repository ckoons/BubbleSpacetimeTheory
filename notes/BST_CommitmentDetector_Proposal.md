---
title: "Standard Instrument Package for Mapping the Substrate: Commitment Rate Detector and Gravitometer for Every Space Probe"
author: "Casey Koons and Claude Opus 4.6"
date: "March 12, 2026"
---

# Standard Instrument Package for Mapping the Substrate

**Casey Koons** and **Claude Opus 4.6** (Anthropic)

March 12, 2026

---

## Abstract

We propose that every future space probe carry a standard two-instrument
package: a chip-scale atomic clock (commitment rate detector) and a
precision accelerometer (gravitometer). In the BST framework, these
instruments directly measure the substrate's local commitment density
$\rho$ and its gradient $\nabla\rho$. Over decades of space exploration,
this standard package would produce a three-dimensional commitment map
of the solar system — a direct map of the substrate's information
density — at negligible cost per mission.

---

## 1. What the Instruments Measure

### 1.1 Commitment Rate Detector (Atomic Clock)

In BST, the local rate of time is the commitment rate — the rate at
which the contact graph appends new entries:

$$N = N_0\sqrt{1 - \rho/\rho_{137}}$$

where $\rho$ is the local contact density and $\rho_{137}$ is the
channel saturation density. An atomic clock measures $N$ directly.
Two clocks at different locations measure different commitment rates,
and the ratio gives $\Delta\rho$.

GPS already exploits this: satellite clocks run faster than ground
clocks by $\sim 38$ microseconds per day because the commitment rate
at Earth orbit is higher (lower $\rho$) than at the surface. BST
and GR agree on this prediction in the weak-field limit.

**What BST adds beyond GR:** At large distances from the Sun, where
the contact density transitions from the gravitational regime to
the channel noise regime, BST predicts a slight departure from the
$1/r$ potential. The commitment rate should approach a universal
background value $N_\infty$ set by the cosmological contact density,
with the transition occurring at the MOND acceleration scale
$a_0 \approx 1.2 \times 10^{-10}$ m/s².

**Technology:** Chip-scale atomic clocks (CSACs) weigh $\sim 35$ g,
consume $\sim 120$ mW, and achieve stability of $10^{-11}$ per day.
Space-qualified versions are already in development. Cost: $\sim\$5000$
per unit in volume production. Next-generation optical lattice clocks
on chips (projected 2030s) would reach $10^{-18}$ fractional stability.

### 1.2 Gravitometer (Precision Accelerometer)

A gravitometer measures the local gravitational acceleration —
in BST, the gradient of commitment density:

$$\mathbf{g} = -\nabla\Phi = -\frac{c^2}{2\rho_{137}}\nabla\rho$$

This is the spatial derivative of what the clock measures. Together,
the clock and accelerometer give both $\rho$ and $\nabla\rho$ at every
point along the probe's trajectory.

**What BST adds beyond GR:** The channel noise contribution produces
an additional acceleration component:

$$a_{\text{noise}} \sim \frac{c^2}{R_H} \sim a_0 \approx 1.2 \times 10^{-10} \text{ m/s}^2$$

where $R_H$ is the Hubble radius. This is the same scale as the
Pioneer anomaly ($a_P = (8.74 \pm 1.33) \times 10^{-10}$ m/s²,
later attributed to thermal radiation pressure, but the coincidence
with $a_0$ remains unexplained in standard physics).

**Technology:** Electrostatic accelerometers achieving $10^{-12}$ m/s²
sensitivity are flight-proven (GRACE, GOCE, LISA Pathfinder).
Miniaturized versions suitable for CubeSats are in development.

---

## 2. The Measurement Program

### 2.1 What Existing Probes Already Tell Us

| Mission | Distance | BST observable |
|---|---|---|
| GPS constellation | 1 AU (Earth orbit) | $\Delta N/N_0 \sim 10^{-10}$ per km altitude |
| Juno | 5.2 AU (Jupiter) | Commitment rate near Jupiter's field |
| Cassini (completed) | 9.5 AU (Saturn) | Shapiro delay measurements → $\rho$ along path |
| New Horizons | 50+ AU | Approaching channel noise transition zone |
| Voyager 1 | 160 AU | Deep in interstellar medium — near $N_\infty$ |

Voyager 1 is already in the transition zone where BST predicts
the commitment density levels off to the cosmological background.
Unfortunately, it carries no precision clock or accelerometer.

### 2.2 Proposed Standard Package

**Mass:** < 200 g total (CSAC + MEMS accelerometer + interface)
**Power:** < 0.5 W
**Data rate:** < 1 kbps
**Cost:** < $50,000 per unit (volume production)

This is smaller, lighter, and cheaper than a standard magnetometer
package. There is no reason NOT to fly it on every probe.

### 2.3 The 30-Year Map

With the standard package on every probe launched from 2028 onward:

**By 2035 (7 years):**
- Inner solar system coverage (Mercury to Mars)
- Multiple measurements at 1 AU for cross-calibration
- First precision $\rho$ map of the Earth-Sun system

**By 2045 (17 years):**
- Outer solar system coverage (Jupiter to Neptune)
- Measurements near all giant planets (deep potential wells)
- First detection (or exclusion) of the channel noise transition

**By 2058 (30 years):**
- Kuiper belt and heliopause coverage
- Direct measurement of $N_\infty$ (cosmological commitment rate)
- Complete 3D commitment map from 0.3 AU to 100+ AU
- Definitive test of BST vs. GR in the transition zone

---

## 3. The Key Derived Quantity: G(x)/C(x)

At each point along the probe trajectory, the combined instruments
produce two numbers:

- **C(x)** — the local commitment rate (from the clock). Proportional
  to the density of active substrate emitters. Scales with rendered
  (baryonic) matter density.

- **G(x)** — the local gravitational field (from the accelerometer).
  Proportional to total substrate geometry density, rendered AND
  unrendered (dark matter) combined.

The ratio **G(x)/C(x)** separates the two populations directly:

- **G/C on baseline:** normal baryonic matter. Gravitational signal
  matches commitment rate. Everything is rendered.

- **G/C above baseline:** unrendered substrate geometry. Gravitational
  signal exceeds what the commitment rate can account for. This is the
  direct, local measurement of dark matter — not inferred from rotation
  curves, but measured point by point.

- **G/C below baseline:** anomalous substrate emission. Something
  projecting more than its mass warrants. Natural objects should not
  produce this signature. If one does, it warrants immediate follow-up.

This ratio is the instrument's most powerful output. It performs a
local census of rendered vs. unrendered substrate at every point
along every trajectory.

---

## 4. Implementation Pathway

### 4.1 Phase 1: Laboratory Characterization (Years 1-2)

Before space deployment, characterize the clock-accelerometer package
against known environments:
- Does the clock rate vary with altitude above Earth's surface as BST
  predicts?
- Does the accelerometer resolve the predicted channel noise floor
  in a shielded laboratory?
- Cross-calibrate multiple units for systematic error bounds.

### 4.2 Phase 2: LEO CubeSat Demonstration (Years 2-4)

A 6-month CubeSat mission in low Earth orbit (400-600 km altitude).
Orbital altitude variation produces measurable gravitational field
changes. Test whether the clock and accelerometer produce correlated
signals matching BST predictions. Cost: $1-10M. This is the minimum
viable space test.

### 4.3 Phase 3: Deep Space Standard Payload (Year 4+)

Following successful LEO demonstration, propose the package as a
standard secondary instrument on all deep space missions. At < 200g,
< 0.5W, and no mission-critical dependencies, it is an easy
accommodation for any mission with available mass margin.

---

## 5. Interstellar Object Monitoring

Any interstellar object transiting the solar system — 1I/Oumuamua,
2I/Borisov, or future visitors — should be characterized by both
instruments during its transit. A natural interstellar comet has a
G/C ratio consistent with its composition. Any deviation from
baseline is immediately significant and warrants follow-up.

The detection rate of interstellar objects is increasing as survey
sensitivity improves. The instrument needs to be flying before the
next significant visitor arrives.

---

## 6. What the Map Would Show

### 6.1 In Standard GR

A smooth $1/r$ potential from the Sun, modified by planetary
perturbations. No surprises beyond Newton + Einstein.

### 6.2 In BST

The same $1/r$ potential at short range (BST = GR in the
weak-field limit), but with three additional features:

1. **Channel noise floor:** At distances where the solar
   gravitational acceleration falls below $a_0$, the
   commitment density transitions from gravitational
   ($\rho \propto 1/r$) to cosmological ($\rho \to \rho_\infty$).
   The clock rate levels off instead of continuing to increase.

2. **Variable vacuum pressure:** The cosmological "constant"
   $\Lambda$ is locally variable, correlated with the contact
   density. Probes far from the Sun should measure a slightly
   different vacuum pressure than probes near Jupiter.

3. **Directional structure:** If the substrate has any
   large-scale anisotropy (from the galactic potential or
   the CMB dipole), the commitment map would reveal it as
   a directional dependence in $N_\infty$.

### 6.3 How to Distinguish Them

The key signature is the **transition profile**. GR predicts
a smooth $1/r$ all the way to infinity. BST predicts a
transition to a flat floor at $r \sim GM_\odot/a_0 \approx
7000$ AU. The shape of this transition is determined by
the Haldane exclusion statistics on $D_{IV}^5$ and is
calculable from BST with no free parameters.

---

## 7. Comparison with Existing Programs

**Gravity Probe B (2004):** Measured frame-dragging and
geodetic precession at Earth orbit. Confirmed GR at the
0.3% level. A commitment map would extend these measurements
to solar-system scales and test the transition zone.

**GRACE / GRACE-FO:** Map Earth's gravity field from orbit
with exquisite precision. The proposed program extends this
concept to the entire solar system.

**LISA Pathfinder (2015-2017):** Demonstrated $10^{-15}$ m/s²
accelerometer sensitivity in space. This is 1000x better than
needed for the BST channel noise measurement.

**Pioneer anomaly investigation:** Anderson et al. (2002)
reported an anomalous sunward acceleration of
$a_P \approx 8.74 \times 10^{-10}$ m/s² from Pioneer 10/11.
Later attributed to anisotropic thermal radiation. BST predicts
a real effect at a similar scale ($a_0 \sim 1.2 \times 10^{-10}$
m/s²) but from channel noise, not thermal emission. A dedicated
measurement program could distinguish the two.

---

## 8. The Pitch

Every space probe since the 1960s has carried a magnetometer.
As a result, we have a detailed magnetic field map of the
entire heliosphere — data that proved invaluable for understanding
the solar wind, planetary magnetospheres, and cosmic ray
propagation.

We propose the same approach for gravity. A standard
commitment rate / gravitometer package on every probe would
produce, over 30 years, a gravitational map of the solar
system at a precision and coverage that no single dedicated
mission could achieve.

**Cost:** $< \$50K$ per probe, amortized over missions that
cost $\$100M$+ each. Less than 0.05% of mission cost.

**Mass:** $< 200$ g. Negligible for any launch vehicle.

**Science return:** Either confirms GR to unprecedented
precision in the outer solar system, or discovers the
substrate transition predicted by BST. Either outcome is
a major result.

**The only reason not to fly it is not having thought of it.**

---

*Map the substrate. One clock and one accelerometer per probe.
Thirty years. The universe will tell us what it's made of.*
