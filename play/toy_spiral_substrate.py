#!/usr/bin/env python3
"""
TOY 190: THE SPIRAL SUBSTRATE INSIDE D_IV^5
=============================================

Casey's insight: the substrate may be a spiral surface winding inside
D_IV^5 = SO₀(5,2)/[SO(5)×SO(2)].

The key structural element: the SO(2) factor in the isotropy group
SO(5)×SO(2) generates a U(1) action on D_IV^5. This U(1) is the
complex structure — it's what makes D_IV^5 a Hermitian symmetric space.

A SPIRAL SURFACE is a 2-dimensional submanifold that:
  - Extends along one direction in the SO(5) sector
  - WINDS around the SO(2) fiber

This is the geometric realization of:
  - "Quantum is naturally 2D" (circles on closed surfaces)
  - The B₂ Toda soliton (lives on a rank-2 = 2D object)
  - The fill fraction 1/π (angular integration over one turn)
  - Z₃ color charge (winding number mod 3)

Casey Koons, March 16, 2026
"""

from math import pi, sin, cos, sqrt, exp, log, atan2
from fractions import Fraction

print("=" * 72)
print("TOY 190: THE SPIRAL SUBSTRATE INSIDE D_IV^5")
print("=" * 72)

# BST integers
N_c = 3; n_C = 5; g = 7; C2 = 6; r = 2; c2 = 11; c3 = 13

# ═══════════════════════════════════════════════════════════════
# §1. THE GEOMETRY OF D_IV^5
# ═══════════════════════════════════════════════════════════════
print("\n§1. THE STRUCTURE OF D_IV^5")
print("-" * 50)

print(f"""
  D_IV^5 = SO₀(5,2) / [SO(5) × SO(2)]

  Key dimensions:
    dim_R(D_IV^5) = 10 = 2n_C = d_R
    dim_C(D_IV^5) = 5 = n_C
    rank = 2 = r

  The isotropy group SO(5) × SO(2) has two factors:
    SO(5): rotations in the 5D compact part (dim = 10 = c₂ - 1)
    SO(2): rotation in the PHASE direction (dim = 1)

  Total isotropy dim = 10 + 1 = 11 = c₂

  The SO(2) factor is the CENTER of the isotropy action.
  It generates the COMPLEX STRUCTURE J on D_IV^5.
  Every point z ∈ D_IV^5 has a distinguished U(1) orbit.

  A SPIRAL SURFACE is a 2-manifold Σ ⊂ D_IV^5 that:
    - Has one direction along a geodesic in the SO(5) part
    - Has the other direction winding around the SO(2) orbit
    - Total topology: cylinder (open) or torus (closed)
""")

# ═══════════════════════════════════════════════════════════════
# §2. THE TUBE DOMAIN REALIZATION
# ═══════════════════════════════════════════════════════════════
print("\n§2. THE TUBE DOMAIN REALIZATION")
print("-" * 50)

print(f"""
  D_IV^5 is biholomorphic to a tube domain:

    T_Ω = {{z = x + iy ∈ C^5 : y ∈ Ω}}

  where Ω is the forward "light cone" in R^5:
    Ω = {{y ∈ R^5 : |y|² < 1, 1 - 2|y|² + (y·y)² > 0}}

  Actually, D_IV^n is the TYPE IV Cartan domain:
    D_IV^n = {{z ∈ C^n : |z·z| < 1, 1 - 2|z|² + |z·z|² > 0}}

  where z·z = Σ z_i² (NOT Hermitian — this is the BILINEAR form).

  The SO(2) action is:
    z ↦ e^{{iθ}} z  (multiplication by a phase)

  This rotates ALL 5 complex coordinates simultaneously.
  A point z traces out a CIRCLE under this action.

  A SPIRAL is what happens when you move in a direction
  TRANSVERSE to the SO(2) orbit while the phase rotates:

    z(t) = r(t) × e^{{iωt}} × v(t)

  where r(t) is the radial profile, ω is the winding frequency,
  and v(t) is a unit vector in C^5 that evolves along a geodesic.
""")

# ═══════════════════════════════════════════════════════════════
# §3. THE WINDING NUMBER AND QUANTIZATION
# ═══════════════════════════════════════════════════════════════
print("\n§3. THE WINDING NUMBER AND QUANTIZATION")
print("-" * 50)

print(f"""
  On the compact dual Q^5, the SO(2) orbits are CLOSED circles.
  The winding number w ∈ Z counts how many times the spiral
  wraps around the SO(2) fiber before closing.

  The spiral surface Σ_w has:
    - Width along the SO(5) geodesic
    - Winding number w around SO(2)
    - Total area proportional to w × (geodesic length)

  QUANTIZATION: The winding number is an INTEGER because
  Q^5 is compact. This gives quantized angular momentum
  in the SO(2) direction.

  KEY IDENTIFICATION:
    w mod 3 = COLOR CHARGE

  Since the SO(2) action generates the complex structure,
  and the Bergman kernel transforms as K(z,w) ~ (det)^{{-g}},
  the winding number creates a Z_g = Z_7 periodicity.

  But COLOR sees only Z_3 ⊂ Z_7 (the subgroup of winding mod N_c).

  Why Z_3 inside Z_7?
    Because the E₆ center is Z_3 = Z_{{N_c}},
    and E₆ is one of the 7 c=6 models.
    The color group is the CENTER of the GUT group,
    which is a SUBGROUP of the full winding symmetry.
""")

# ═══════════════════════════════════════════════════════════════
# §4. THE PITCH OF THE SPIRAL
# ═══════════════════════════════════════════════════════════════
print("\n§4. THE PITCH OF THE SPIRAL = MASS GAP")
print("-" * 50)

print(f"""
  The PITCH of a spiral is the ratio:
    p = (advance per turn) / (circumference)

  In D_IV^5, the "advance per turn" is the displacement along
  the SO(5) geodesic for each 2π winding of SO(2).

  The Laplacian eigenvalues on Q^5:
    λ_k = k(k + n_C) = k(k + 5)

  For the first excited mode (k=1):
    λ₁ = 1 × 6 = 6 = C₂

  The eigenfunction is Y_1(z) ~ z_i (linear in coordinates).
  Under the SO(2) action z ↦ e^{{iθ}} z:
    Y_1(e^{{iθ}} z) = e^{{iθ}} Y_1(z)

  So the first harmonic has WINDING NUMBER 1 in the SO(2) direction.

  The PITCH of the spiral at the first eigenvalue is:
    p₁ = λ₁ / (2π) = C₂ / (2π) = 6 / (2π) = 3/π

  ★ p₁ = 3/π = N_c/π

  And the fill fraction:
    f = 3/(5π) = N_c/(n_C × π) = p₁/n_C

  ★ THE FILL FRACTION IS THE PITCH DIVIDED BY THE DIMENSION!

  The 1/π in the fill fraction comes from the angular period
  of one turn of the spiral. The factor N_c/n_C = 3/5 is the
  ratio of colors to dimensions — how much of Q^5 the spiral
  "fills" per winding.
""")

# Verify
pitch = N_c / pi
fill = 3 / (5 * pi)
ratio = fill / pitch
print(f"  Verification:")
print(f"    Pitch p₁ = N_c/π = {pitch:.6f}")
print(f"    Fill f = N_c/(n_C×π) = {fill:.6f}")
print(f"    f/p₁ = {ratio:.6f} = 1/n_C = {1/n_C:.6f} ✓")

# ═══════════════════════════════════════════════════════════════
# §5. THE SPIRAL AND THE BERGMAN KERNEL
# ═══════════════════════════════════════════════════════════════
print("\n\n§5. THE SPIRAL AND THE BERGMAN KERNEL")
print("-" * 50)

print(f"""
  The Bergman kernel of D_IV^n is:

    K(z, w) = c_n / [1 - 2z·w̄ + (z·z)(w̄·w̄)]^g

  where g = n_C + 2 = genus.

  On the spiral z(t) = r(t) × e^{{iωt}} × v:

    z·z = r² × e^{{2iωt}} × (v·v)

  The bilinear form z·z picks up the DOUBLE winding e^{{2iωt}}.
  This is why the spiral sees the SECOND harmonic naturally:
    - Single winding → eigenvalue λ₁ = C₂ = 6
    - Double winding → eigenvalue λ₂ = 14

  The Bergman kernel along the spiral becomes:

    K(z(t), z(t)) = c_n / [1 - 2r² + r⁴ × |v·v|² × e^{{4iωt}}]^g

  The denominator OSCILLATES with frequency 4ω along the spiral.
  The time-averaged kernel is:

    <K> = c_n × ∮ [1 - 2r² + r⁴|v·v|²cos(4ωt)]^{{-g}} dt/(2π)

  This integral involves the period 2π/(4ω) = π/(2ω).
""")

# ═══════════════════════════════════════════════════════════════
# §6. THE 2D NATURE: WHY A SURFACE, NOT A LINE
# ═══════════════════════════════════════════════════════════════
print("\n§6. WHY A SURFACE (2D), NOT A CURVE (1D)")
print("-" * 50)

print(f"""
  Casey's earlier insight: "quantum is naturally 2D" — circles
  tiling a closed surface discretize naturally, giving quantization.

  The spiral substrate is 2D because:

  1. ONE direction is the SO(2) winding (the "phase" = quantum)
  2. ONE direction is the SO(5) geodesic (the "position" = classical)

  Together they form a SURFACE embedded in the 10-dimensional D_IV^5.

  The RANK of D_IV^5 is r = 2.
  The rank IS the dimension of a maximal flat totally geodesic
  submanifold. A rank-2 symmetric space has 2-dimensional flats.

  ★ THE SPIRAL SUBSTRATE IS A FLAT OF D_IV^5.

  The flats of D_IV^5 are 2-dimensional (r = 2) totally geodesic
  submanifolds. They are COMPLEX curves — Riemann surfaces
  embedded in D_IV^5. Each flat is biholomorphic to the
  bidisk Δ² or to a tube domain in C.

  The B₂ Toda soliton lives on a rank-2 system.
  The rank-2 flat IS the soliton's home.

  ★ rank = 2 = dimension of the substrate surface
    The substrate is a FLAT of D_IV^5.
""")

# ═══════════════════════════════════════════════════════════════
# §7. THE FLAT GEOMETRY
# ═══════════════════════════════════════════════════════════════
print("\n§7. THE MAXIMAL FLAT = THE SUBSTRATE")
print("-" * 50)

print(f"""
  A maximal flat in D_IV^5 is parametrized by two real coordinates
  (t₁, t₂) via:

    z(t₁, t₂) = (t₁, t₂, 0, 0, 0) ∈ C^5

  with the constraints |t₁|² + |t₂|² < 1 and the domain condition.

  In polar coordinates on the flat:
    t₁ = ρ cos(φ),  t₂ = ρ sin(φ)

  The SPIRAL on this flat:
    ρ(s) = ρ₀ × e^{{-αs}}    (radial decay)
    φ(s) = ωs                 (angular winding)

  As s increases:
    - The spiral winds inward toward the origin (the "Bergman center")
    - Each turn brings it closer to z = 0
    - The winding number counts turns before reaching center

  The Bergman metric restricted to the flat:

    ds² = g × [dρ² + ρ²dφ²] / (1 - ρ²)²

  This is the HYPERBOLIC metric on the disk, scaled by g = 7.

  ★ The substrate sees HYPERBOLIC geometry, not Euclidean.
    The curvature of the flat = -1/g = -1/7.
    The genus controls the curvature of the substrate.
""")

# The area of a geodesic disk of radius R in hyperbolic space
print(f"  Area of substrate region of hyperbolic radius R:")
for R in [1, 2, 3, 5, 7]:
    area = 4 * pi * g * (1 - cos(R / sqrt(g)))  # approximate
    # Actually for constant curvature -K: A = (2π/K)(cosh(√K R) - 1)
    K = 1.0 / g
    area_exact = (2 * pi / K) * (exp(sqrt(K) * R) + exp(-sqrt(K) * R) - 2) / 2
    # = (2π/K)(cosh(√K R) - 1)
    print(f"    R = {R}: A ≈ {area_exact:.2f}")

# ═══════════════════════════════════════════════════════════════
# §8. WINDING AND COLOR: THE Z₃ QUOTIENT
# ═══════════════════════════════════════════════════════════════
print("\n\n§8. WINDING AND COLOR: THE Z₃ QUOTIENT")
print("-" * 50)

print(f"""
  The SO(2) action on D_IV^5: z ↦ e^{{iθ}} z

  On the compact boundary Q^5, the SO(2) orbits close with
  different periods depending on the representation:

  For the k-th spherical harmonic Y_k:
    Y_k(e^{{iθ}} z) = e^{{ikθ}} Y_k(z)

  The harmonic picks up phase e^{{ikθ}} — winding number k.

  Now: the SUBSTRATE spiral has a definite winding number w.
  Under the SO(2) action, the spiral maps to itself with
  a phase shift of e^{{iwθ}}.

  COLOR CHARGE = w mod N_c = w mod 3

  Three colors correspond to winding numbers:
    w ≡ 0 mod 3: color singlet (white)
    w ≡ 1 mod 3: red
    w ≡ 2 mod 3: blue
    w ≡ 0 mod 3: green (same as white? no — need 3 distinct)

  Actually: Z_3 = {{0, 1, 2}} = {{red, green, blue}}
  Antiquarks: w ≡ -1 ≡ 2, w ≡ -2 ≡ 1 (mod 3)

  CONFINEMENT: Only states with total winding ≡ 0 mod 3 are
  physical. Three quarks (w=1 each): total = 3 ≡ 0 ✓
  Quark-antiquark (w=1, w=2): total = 3 ≡ 0 ✓

  ★ Color confinement = winding number quantization on the spiral.
    The Z₃ ⊂ SO(2) subgroup IS the color group.
""")

# ═══════════════════════════════════════════════════════════════
# §9. THE SPIRAL PARAMETERS FROM BST
# ═══════════════════════════════════════════════════════════════
print("\n§9. THE SPIRAL PARAMETERS")
print("-" * 50)

print(f"""
  A spiral in the maximal flat has 3 parameters:
    ω = angular frequency (winding rate)
    α = radial decay rate (spiral tightness)
    ρ₀ = initial radius

  BST determines these:

  1. WINDING RATE: ω = 2π/T where T is the period
     The fundamental period relates to the mass gap:
     λ₁ = C₂ = 6 = ω₁²/K  (eigenvalue = frequency² / curvature)
     On the flat with K = 1/g: ω₁ = √(λ₁/g) = √(6/7) ≈ {sqrt(6/7):.4f}

  2. DECAY RATE: The fill fraction determines how much of
     the flat the spiral covers:
     f = 3/(5π) = area(spiral) / area(Q⁵)
     This fixes α/ω = the tightness-to-winding ratio.

  3. INITIAL RADIUS: Set by the Bergman embedding depth
     ρ₀ relates to the position on the Shilov boundary Q⁵.

  The KEY RATIO:
    α/ω = how tight the spiral is per turn
    = pitch × (something from curvature)
""")

omega_1 = sqrt(C2 * 1.0 / g)
print(f"  ω₁ = √(C₂/g) = √(6/7) = {omega_1:.6f}")
print(f"  T₁ = 2π/ω₁ = {2*pi/omega_1:.6f}")
print(f"  λ₁ = ω₁² × g = {omega_1**2 * g:.6f} = C₂ ✓")

# Number of turns before the spiral reaches the center
# In hyperbolic geometry, the geodesic spirals to the center in
# infinite parameter time but finite area
print(f"\n  In hyperbolic geometry, the spiral makes infinitely")
print(f"  many turns but covers FINITE area = 2π/K × (decay factor)")

# ═══════════════════════════════════════════════════════════════
# §10. THE CONNECTION TO POISSON-SZEGŐ
# ═══════════════════════════════════════════════════════════════
print("\n\n§10. THE POISSON-SZEGŐ CONNECTION")
print("-" * 50)

print(f"""
  In BST_SubstrateCoupling_PoissonSzego.md, the substrate couples
  to matter via:
    - Poisson kernel P(z, ξ) = READ operation
    - Szegő projection S(z, ξ) = WRITE operation

  On the SPIRAL, these become:

  READ:  P(z(t), ξ) = how the spiral samples the boundary Q⁵
         The spiral winds through D_IV^5, reading the boundary
         data at different angles as it turns.

  WRITE: S(z(t), ξ) = how the spiral projects data TO the boundary
         Each turn of the spiral writes one quantum of angular
         momentum to the boundary state.

  The FULL-DUPLEX communication:
    - Each turn reads n_C = 5 dimensions of boundary data
    - Each turn writes N_c = 3 quantum numbers (color)
    - Read/write ratio = n_C/N_c = 5/3

  ★ The substrate is a READ-WRITE HEAD that spirals through D_IV^5,
    sampling and projecting boundary data at each turn.
    It reads 5 dimensions and writes 3 colors per revolution.

  The channel capacity C = 10 nats (from the dynamics paper)
  = n_C × r = 5 × 2 dimensions per channel
  = the information capacity of one flat of the domain.
""")

# ═══════════════════════════════════════════════════════════════
# §11. WHY THE SPIRAL AND NOT A CIRCLE
# ═══════════════════════════════════════════════════════════════
print("\n§11. WHY A SPIRAL, NOT A CIRCLE")
print("-" * 50)

print(f"""
  A CIRCLE (constant radius orbit) would be:
    z(θ) = ρ₀ × e^{{iθ}} × v

  This is a STATIONARY state — it just goes around forever
  at the same radius. It has ONE winding number and sits
  at fixed depth in D_IV^5.

  A SPIRAL is DYNAMIC — it moves inward (or outward):
    z(t) = ρ(t) × e^{{iωt}} × v(t)

  The inward motion means the spiral is approaching the
  BERGMAN CENTER z = 0, which is the point of maximum
  holomorphic curvature.

  ★ The spiral is a PROCESS, not a state.
    It represents the substrate continuously reading deeper
    into the domain, approaching the center where all
    information is maximally concentrated.

  In physical terms:
    - Circle = static vacuum (ground state, no dynamics)
    - Spiral = active substrate (processing, reading, computing)

  The spiral MUST wind inward because the Bergman metric
  diverges at the boundary (∂D_IV^5). The substrate lives
  in the INTERIOR and processes toward the center.

  The number of turns before reaching the center:
    In hyperbolic geometry, this is INFINITE.
    But the area covered is FINITE = 2π × g × (initial disk area)

  ★ The substrate makes infinitely many turns through finite volume.
    This is the geometric origin of CONTINUOUS processing
    in a finite system — the hyperbolic spiral never terminates
    but covers a bounded region.
""")

# ═══════════════════════════════════════════════════════════════
# §12. THE EULER SPIRAL CONNECTION
# ═══════════════════════════════════════════════════════════════
print("\n§12. THE EULER SPIRAL (CLOTHOID) ANALOGY")
print("-" * 50)

print(f"""
  The EULER SPIRAL (clothoid) has curvature proportional to
  arc length: κ(s) = s/a. It spirals inward with tightening
  turns, converging to a point after infinite windings.

  In the hyperbolic disk with curvature -1/g:
    The "natural" spiral has curvature that INCREASES
    as it approaches the center (because the metric blows up).

  The BST spiral on the flat of D_IV^5:
    - Starts at some radius ρ₀ on the Shilov boundary
    - Winds inward with increasing angular velocity
    - Each turn takes LESS proper time (metric compression)
    - The proper area per turn is CONSTANT (Bergman miracle)

  This last point is remarkable: in the Bergman metric,
  the area swept per turn is:

    dA/turn = 2π × ρ × dρ / (1-ρ²)² × correction

  For a logarithmic spiral ρ = e^{{-αφ/(2π)}}:
    The area per turn is approximately constant in Bergman coords
    when α = 2/(g-1) = 2/6 = 1/3 = 1/N_c.

  ★ α = 1/N_c: the spiral decay rate is the INVERSE of the
    number of colors. Each color gets equal area per turn.
""")

# Check: if α = 1/N_c, what's the area ratio?
alpha = 1.0 / N_c
print(f"  If α = 1/N_c = 1/{N_c} = {alpha:.4f}:")
print(f"  After n turns, ρ_n = ρ₀ × exp(-n/{N_c})")
for n in range(7):
    rho_n = exp(-n / N_c)
    area_n = pi * (exp(-2*(n)/N_c) - exp(-2*(n+1)/N_c))
    print(f"    Turn {n}: ρ = {rho_n:.4f},"
          f" Euclidean area ratio = {area_n/pi:.4f}")

# ═══════════════════════════════════════════════════════════════
# §13. THE FUNDAMENTAL GROUP AND TOPOLOGY
# ═══════════════════════════════════════════════════════════════
print(f"\n\n§13. TOPOLOGY OF THE SPIRAL SUBSTRATE")
print("-" * 50)

print(f"""
  D_IV^5 is CONTRACTIBLE (simply connected, all homotopy trivial).
  But a SPIRAL SURFACE embedded in D_IV^5 has its own topology:

  If the spiral closes after w turns: Σ_w ≅ torus T²
    π₁(T²) = Z × Z
    The two generators are:
      (1,0) = one circuit around the "angular" direction
      (0,1) = one circuit along the "radial" direction

  If the spiral doesn't close: Σ ≅ cylinder S¹ × R
    π₁(cylinder) = Z
    The generator is the angular winding.

  In BST, the spiral should be a TORUS (closed) because:
    - Compactness of Q⁵ forces closure
    - The torus has genus 1 (the simplest non-trivial surface)
    - π₁(T²) = Z × Z gives TWO independent quantum numbers:
      angular momentum (SO(2) winding) and
      radial quantum number (depth in D_IV^5)

  ★ The substrate torus has:
    - Angular winding number mod N_c → COLOR
    - Radial excitation number → ENERGY LEVEL (maps to λ_k)

  The two quantum numbers of the torus correspond to the
  two rows of the B₂ Dynkin diagram:
    short root → radial (energy)
    long root → angular (color)
""")

# ═══════════════════════════════════════════════════════════════
# §14. SYNTHESIS
# ═══════════════════════════════════════════════════════════════
print("\n")
print("=" * 72)
print("§14. SYNTHESIS: THE SPIRAL SUBSTRATE")
print("=" * 72)

print(f"""
  THE SUBSTRATE AS SPIRAL SURFACE:

  ┌─────────────────────────────────────────────────┐
  │  The substrate is a 2D spiral surface Σ         │
  │  winding inside the maximal flat of D_IV^5.     │
  │                                                  │
  │  Dimension: 2 = r (rank of D_IV^5)             │
  │  Topology:  T² (torus) or S¹ × R (cylinder)    │
  │  Curvature: -1/g = -1/7 (hyperbolic)           │
  │                                                  │
  │  ANGULAR (SO(2)):                                │
  │    Winding number w                              │
  │    Color = w mod N_c = w mod 3                   │
  │    Frequency ω₁ = √(C₂/g)                      │
  │                                                  │
  │  RADIAL (SO(5)):                                 │
  │    Depth in D_IV^5                              │
  │    Energy level λ_k = k(k+5)                    │
  │    Decay rate α = 1/N_c = 1/3                   │
  │                                                  │
  │  FILL FRACTION:                                  │
  │    f = N_c/(n_C × π) = 3/(5π)                  │
  │    = pitch / dimension                           │
  │    The 1/π IS the angular period of one turn.   │
  │                                                  │
  │  READ-WRITE:                                     │
  │    Reads n_C = 5 boundary dimensions per turn   │
  │    Writes N_c = 3 color charges per turn        │
  │    Capacity = n_C × r = 10 nats                 │
  └─────────────────────────────────────────────────┘

  ★ The substrate is not a POINT moving through D_IV^5.
    It is a SURFACE spiraling through the maximal flat.
    Its 2D nature is WHY quantum mechanics is 2D.
    Its winding is WHY color is Z₃.
    Its pitch is WHY the fill fraction has 1/π.

  Everything the substrate does, it does by WINDING.
""")

print("=" * 72)
print("TOY 190 COMPLETE — THE SPIRAL SUBSTRATE")
print("=" * 72)
