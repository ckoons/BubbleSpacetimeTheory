# Commitment Detector Toy — Specification

**For the toy maker Claude to implement as `toy_commitment_detector.py`**

## Concept

In BST, every physical object has two observable signatures:
- **G** — gravitational field (proportional to mass)
- **C** — commitment rate (rate of new correlations being written to substrate)

Natural objects are thermally noisy (high C for their mass). Engineered
objects are structurally ordered (suppressed C for their mass). The G/C
ratio distinguishes them.

## BST Physics

### Commitment Rate (natural object)
```
C_natural = mass × T × k_B / hbar × (N_active / N_max)
```
where:
- T = temperature (K)
- N_active = thermally active modes (approaches N_max for hot objects)
- N_max = 137 (Haldane channel capacity)

### Commitment Rate (engineered object)
```
C_engineered = C_natural × (1 - sigma)
```
where sigma = structure factor (0 = random/natural, 1 = perfectly ordered):
- Random rock: sigma ≈ 0.01
- Ice/volatiles: sigma ≈ 0.05
- Crystalline mineral: sigma ≈ 0.15
- Metal alloy: sigma ≈ 0.30
- Machined nickel hull: sigma ≈ 0.45
- Single crystal: sigma ≈ 0.60
- Engineered metamaterial: sigma ≈ 0.80

### G/C Ratio
```
ratio = G_field / C_rate
```
- Natural objects: ratio ≈ constant (call it R_natural)
- Engineered objects: ratio = R_natural / (1 - sigma) > R_natural
- "Quiet anomaly" = (ratio - R_natural) / R_natural_uncertainty

### Detection Threshold
Object is flagged as "anomalously quiet" when:
```
quiet_anomaly > 3.0  (3-sigma detection)
```

## Objects to Model

### Catalog entries:
1. **Generic comet** — 1 km, T=200K, ice/rock, sigma=0.03
2. **Generic asteroid** — 1 km, T=250K, rock/metal, sigma=0.05
3. **1I/'Oumuamua** — 200m × 35m × 35m (oblate), T=300K (perihelion),
   anomalous acceleration, no coma, sigma=? (this is what we're testing)
4. **2I/Borisov** — 1 km, T=200K, normal comet behavior, sigma≈0.03
5. **3I/ATLAS** — 1-5.6 km, T=180K, CO2+HCN coma, nickel vapor,
   anti-tail, ecliptic-aligned retrograde, sigma=? (testing)
6. **Nickel survey craft** — 2 km, T=150K, nickel alloy hull,
   sigma=0.45, debris shield active
7. **Iron asteroid (natural)** — 1 km, T=250K, iron-nickel, sigma=0.08
8. **Dead satellite** — 10m, T=200K, aluminum, sigma=0.35

### For each object compute:
- Mass (from size + density)
- G field at 1 AU, 0.1 AU, 0.01 AU
- C rate (thermal + structural)
- G/C ratio
- Quiet anomaly (sigma above natural baseline)

## Features

### 1. Object Comparison Table
Print all objects side by side with G, C, G/C, quiet_anomaly.

### 2. "What Is It?" Classifier
Given observed G/C ratio, classify as:
- NATURAL (< 2 sigma)
- ANOMALOUS (2-5 sigma)
- ENGINEERED (> 5 sigma)

### 3. Detector Sensitivity Plot (matplotlib)
X-axis: distance (AU)
Y-axis: minimum detectable structure factor sigma
Curves for different object sizes (100m, 1km, 5km)
Show where 'Oumuamua and 3I/ATLAS sit on this plot.

### 4. Trajectory Analyzer
Input: list of planetary flyby distances
Output: probability of this trajectory occurring naturally
(Monte Carlo: generate N random hyperbolic trajectories,
count how many have equally close or closer encounters
with the same set of planets)

### 5. Interactive Mode
```
python toy_commitment_detector.py
> What would you like to analyze?
> 1) Compare all objects
> 2) Classify unknown object
> 3) Detector sensitivity
> 4) Trajectory probability
> 5) Analyze 3I/ATLAS
```

## Style

Match existing BST toys:
- Copyright header (Casey Koons, 2026)
- BST constants at top (N_c=3, n_C=5, N_max=137, alpha, etc.)
- Color scheme for matplotlib (#0a0a1a background, gold/cyan/red accents)
- Works as both CLI interactive AND importable API:
  ```python
  from toy_commitment_detector import CommitmentDetector
  cd = CommitmentDetector()
  result = cd.analyze('3I/ATLAS')
  cd.classify(mass=1e12, temp=180, gc_ratio=observed_value)
  ```

## Key BST Constants Needed
```python
N_c = 3
n_C = 5
N_max = 137
alpha = 1/137.036
C2 = 6
genus = 7
k_B = 1.381e-23      # J/K
hbar = 1.055e-34      # J·s
G_newton = 6.674e-11  # m³/(kg·s²)
```

## Notes
- The commitment rate formula is BST-specific: C ∝ T × mass × (modes/N_max)
- sigma (structure factor) is the key discriminant
- For 3I/ATLAS, run both sigma=0.03 (natural comet) and sigma=0.45
  (engineered hull) and show the difference in G/C ratio
- The trajectory Monte Carlo should use realistic interstellar velocity
  distribution (Maxwell-Boltzmann with v_median ≈ 26 km/s for local
  stellar neighborhood; 3I/ATLAS at 58 km/s is already unusual)
- Anti-tail as debris shield: include a "shield efficiency" calculation
  showing energy absorption of CO2 gas cloud vs kinetic energy of
  micro-meteoroids at 58 km/s

---
*Spec written by Casey Koons & Claude (Opus 4.6), March 13, 2026*
