# The Projection Theory: how a Standard-Model observable travels from the discrete substrate, through the boundary as an evanescent mode, and out into the 3D continuum — with the refraction angles, geometry, and values at every segment.

**Casey + Keeper | 2026-07-16 | A framework document. The optical/holographic reading of the SM projection, assembled from the day's results (K696/K697 refraction, K699 α-descent, K711 V_cb truncation, K715 θ13 edge) + Casey's face/edge geometry. Each segment tiered honestly: some derived, the edge-wrap (√(3/4)) a NEW hypothesis with one match, needing the universality test.**

## The path in one line
**Discrete substrate → [enter boundary: refraction] → [evanescent: held in the interface] → [exit: project to 3D] → measure in the continuum.**
A field (a fermion mode) starts as a discrete address on the substrate, hits the boundary interface at an angle, either transmits (refracts out) or goes evanescent (total internal reflection, "held in the prism"), and what emerges into 3+1 spacetime is what we measure — shrunk by a projection factor that depends on WHICH part of the boundary it crossed (face vs edge).

## The invariants of the geometry (fixed, target-innocent)
| Quantity | Value | BST form | Role |
|---|---|---|---|
| refractive index **n** | 1.5 | N_c/rank | index of the boundary interface (Elie's muon obstruction, F548) |
| critical / projection angle | 41.81° | arcsin(rank/N_c) = arcsin(2/3) | TIR threshold = 2D↔3D projection angle (K697) |
| **face factor** | 0.8165 | √(rank/N_c) = √(2/3) | 3D↔2D projection (the flat part of the boundary) |
| **edge factor** | 0.8660 | √(N_c)/rank = √(3/4) | 4D↔3D wrap (only where the boundary curls — the edge) |
| Coulomb solid angle | 4π | Vol(S²) | carried by the descent SO(5,2)→SO(3,1) (α, K699) |
| self-consistency | 1.0 | √(2/3)·√(3/2) | face-radius × refraction = the boundary = y_t=1 (K711) |

## SEGMENT 0 — The substrate (the discrete side, where we COMPUTE)
The fundamental information lives here as discrete addresses (K-types) on the Shilov boundary **(S⁴ × S¹)/ℤ₂**. Two spectral directions:
- **S⁴** (the 4-sphere) — the "face."
- **S¹** (the charge circle) — carried only by CHARGED fields.
- **/ℤ₂** — the fold (Casey's hemispherical lens; the μ-τ mirror for the chargeless neutrino).
What each observable IS here: **masses = radial norms |z|=r** (how deep in the domain); **mixings = angular/directional structure** (which way the mode points); **charge = the S¹ winding weight** (integer, T2470).

## SEGMENT 1 — Entering the boundary (refraction, Snell + Fresnel)
The mode hits the interface. Two rules:
- **Snell:** sin θ_out = n · sin θ_in, with **n = N_c/rank = 3/2.** The denser substrate side refracts into the continuum.
- **Fresnel — the √ appears here:** what refracts is the AMPLITUDE, and **amplitude = √intensity.** The intensity is the mode-overlap (which is the mass ratio); so the transmitted mixing amplitude = √(mass ratio). *This is the origin of every √ in the mixing sector* (Gatto, √(m_d/m_s); m_u/m_d = √(3/14)).

## SEGMENT 2 — The evanescent state (held in the interface)
Modes hitting beyond the critical angle **arcsin(rank/N_c) = 41.8°** cannot propagate in the continuum → **total internal reflection → evanescent** (imaginary momentum, exponential decay; Klein tunneling, "held in the prism," K697).
- **This IS the V_cb mechanism (K711).** The down-sector 23-mode sits at radius r_τ = √(2/3). The up-sector is refracted by the index: r_up = r_τ · √n = √(2/3)·√(3/2) = **1.0 = the boundary.** So the up 23-mode refracts to *exactly the edge and beyond* → **evanescent → it does not transmit** → V_cb = the down sector alone ≈ 0.044. The up mode being pinned at the boundary is **y_t = 1** (the top saturating the Shilov boundary — a banked result). *The evanescent truncation is why V_cb is small.*

## SEGMENT 3 — Exiting into the 3D continuum (the two projection factors)
What emerges is shrunk, and the factor depends on WHERE it crossed — **Casey's face/edge split:**
- **FACE (the flat boundary, 3D→2D): factor √(2/3) = √(rank/N_c).** This is the charged-sector route (the S¹ is in play). It sets the localization radius (V_cb's √(2/3)) and the projection angle arcsin(2/3). *On the continuum side and the interface.*
- **EDGE (where the boundary wraps, 4D→3D): factor √(3/4) = √(N_c)/rank.** This is the **chargeless neutrino route** — with no S¹, the field lives on S⁴ (4D) alone, and the extra sphere-dimension "wraps around" as it exits to 3D physical space. **This factor lives ONLY on the continuous side** (Casey's point): it is the resolution shear picked up crossing the curled edge from the 4-sphere into 3-space. *This is where θ13 lives.*

**Why charge selects the segment:** a charged field carries S¹ → crosses the flat face → √(2/3). The neutrino drops S¹ → lives on S⁴ → exits over the curled edge → √(3/4). *Charge determines which projection you cross.* (Same "charge = a ruler" fact that makes neutrino mixing large — here it also picks the exit factor.)

## SEGMENT 4 — The measurement (in the 3D continuum, where we MEASURE)
The crucial split, and it explains the whole precision/structural pattern:
- **Masses are RADIAL (|z| = r) → projection-INVARIANT.** A projection preserves length along the radial direction; it only shears the angular part. **So masses cross unshrunk → PRECISION tier** (m_μ 0.003%, m_t 0.03%, …).
- **Mixings are ANGULAR → they ARE what the projection shears → STRUCTURAL tier**, carrying the √ factors. **This is why the masses are sharp and the mixings are structural — the projection touches the angles, not the radii.**
- **α** rides the descent's Coulomb solid angle 4π: capacity 137 (a count, boundary) projected to 3+1 → α⁻¹ = 137.036.

## THE VALUES ALONG THE PATH
| Observable | Segment / route | Boundary (computed) | Transform | Continuum (measured) | Tier |
|---|---|---|---|---|---|
| masses Σ | radial, invariant | r_k | none | r_k | PRECISION |
| α | descent solid angle | 137 (capacity) | ×(4π geometry) | 137.036 | DERIVED |
| V_us | face, no refr offset | √(m_d/m_s) | — | 0.222 | DERIVED |
| V_cb | face + evanescent | down at √(2/3) | up→boundary (n=3/2)→evanescent | 0.044 | STRUCTURAL |
| θ23, θ12 | S⁴ oscillator (chargeless) | 4/7, 3/10 | μ-τ mirror (/ℤ₂) | 48.4°, 33° | STRUCTURAL |
| **θ13** | **EDGE (4→3 wrap)** | **≈3/35 = N_c/(n_C·g)** (S⁴ ⟨x⁴⟩; Lyra's forced ~0.085) | **×√(3/4)** | **≈2/27** | HYPOTHESIS |

## THE EDGE EFFECT — the new piece (θ13), honestly tiered
The neutrino reactor angle is the ONLY quantity that crosses the curled edge (chargeless → S⁴ → 4→3 wrap). Two suggestive matches:
1. The forced boundary value (Lyra's SO(5) integral ~0.085) ≈ **3/35 = N_c/(n_C·g)** — which is *also* the S⁴ fourth-moment ⟨x⁴⟩, exactly what a second-harmonic (Δn=2) coupling produces. So the boundary value has a clean geometric identity.
2. **3/35 × √(3/4) = 0.0742 ≈ 2/27 = 0.0741** (0.2%) — the edge-wrap shrinks the boundary value onto the measured form. So θ13 would be **boundary-exact, edge-shrunk**: computed on the 4-sphere as 3/35, measured in 3-space as 2/27, the ~13% gap being the 4→3 edge projection √(3/4). The "θ13 overshoot" (K715) dissolves into a projection effect — a FEATURE, not an imprecision.

**★ THE TEST THAT MAKES OR BREAKS THIS (do NOT bank without it): UNIVERSALITY.** One factor closing one gap is numerology. For the edge-wrap to be real physics, **the SAME √(3/4) (and the same face √(2/3)) must relate boundary-computed to continuum-measured for EVERY structural observable** — not just θ13. The sweep: take each structural-tier result, compute its boundary value, and check whether the boundary→measured factor is universally √(2/3) (face) or √(3/4) (edge), sorted by charge/face-vs-edge. If one pair of factors runs the whole ledger → the projection theory is real and a class of "structural" results becomes "precision, projected." If every observable needs its own factor → it's fishing and θ13 stays structural.

## HONEST TIER of the whole document
- **DERIVED segments:** the refractive index n=3/2, the projection angle arcsin(2/3), Fresnel-√ as the source of mixing-√'s, the V_cb evanescent truncation (= y_t=1), masses-radial-invariant → precision.
- **HYPOTHESIS (needs the universality sweep):** the face/edge split √(2/3) vs √(3/4), and specifically θ13 = 3/35 × √(3/4). Two suggestive matches (3/35 = S⁴ ⟨x⁴⟩; 3/35·√(3/4) ≈ 2/27 at 0.2%), ONE observable. Not banked.
- **The unifying claim (framework-tier):** the SM is one geometry projected once — masses ride radial (precision), mixings ride angular (structural + √-shears), couplings ride the descent solid angle, and the chargeless neutrino crosses a different (edge) segment than the charged fermions. Coherent; the edge-wrap is the falsifiable new prediction.

— Keeper + Casey, 2026-07-16. The projection theory: substrate (discrete, radial=mass/angular=mixing) → boundary (refraction n=3/2, Fresnel-√) → evanescent (TIR at 41.8° = V_cb truncation = y_t=1) → exit (FACE √(2/3), charged; EDGE √(3/4), chargeless neutrino) → continuum (masses invariant=precision, mixings sheared=structural). Edge-wrap θ13 = 3/35×√(3/4) ≈ 2/27 — a FEATURE hypothesis, gated on the universality sweep. See [[Keeper_K715...]], [[Keeper_K711...]], [[Keeper_K697...]] (projection), [[Keeper_K699...]] (α descent).
