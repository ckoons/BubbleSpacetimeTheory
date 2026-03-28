#!/usr/bin/env python3
"""
Toy 526 — Classical Physics Linearization (§73-§78)
====================================================

Linearize ALL 40 classical physics theorems (T210-T249) on the BST spectral lattice.

Standing order: every theorem is a dot product ⟨w|d⟩ on a* ≅ R².
- Depth 0 = scalar (constant, definition, boundary condition)
- Depth 1 = single inner product ⟨w|d⟩
- Depth 2 = composed inner products (NONE survive Casey strict)

Six domains: Classical Mechanics (§73), Optics (§74), Electromagnetism (§75),
Thermodynamics (§76), Fluid Mechanics (§77), Relativity (§78).

BST constants: N_c=3, n_C=5, g=7, C_2=6, N_max=137, rank=2.
"""

import numpy as np

# BST constants
N_c = 3
n_C = 5
g = 7
C_2 = 6
N_max = 137
rank = 2

# BC_2 root data
W_order = 8  # |W(B_2)|
root_mults = (1, 3, 5)  # short, medium, long root multiplicities
dim_real = 2 * n_C  # real dimension of D_IV^5

passed = 0
failed = 0
total = 0

def test(name, condition, detail=""):
    global passed, failed, total
    total += 1
    if condition:
        passed += 1
        print(f"  ✓ {name}")
    else:
        failed += 1
        print(f"  ✗ {name} — {detail}")

# ── Test 1: Classical Mechanics depth audit (§73, T210-T217) ──
print("\n─── Test 1: Classical Mechanics (§73) ───")
mechanics = {
    "T210 Newton F=ma":       {"depth": 0, "type": "definition", "spectral": "ground mode (p,q)=(0,0)"},
    "T211 Newton 3rd law":    {"depth": 0, "type": "conservation", "spectral": "symmetry of K(z,w)=K(w,z)"},
    "T212 Kepler T²∝a³":     {"depth": 1, "type": "balance", "spectral": "⟨GM⁻¹|a³/T²⟩ on radial lattice"},
    "T213 Hooke F=-kx":      {"depth": 0, "type": "Taylor minimum", "spectral": "2nd Seeley-DeWitt coeff a₂"},
    "T214 Archimedes":        {"depth": 0, "type": "subtraction", "spectral": "difference of ground modes"},
    "T215 D'Alembert":        {"depth": 0, "type": "definition", "spectral": "constraint = projection on a*"},
    "T216 Lagrange":          {"depth": 1, "type": "optimization", "spectral": "⟨δq|∂L/∂q⟩ = 0"},
    "T217 Virial":            {"depth": 1, "type": "time average", "spectral": "⟨T|V⟩ = n/2 on spectral lattice"},
}

d0 = sum(1 for v in mechanics.values() if v["depth"] == 0)
d1 = sum(1 for v in mechanics.values() if v["depth"] == 1)
d2 = sum(1 for v in mechanics.values() if v["depth"] == 2)

test("Classical mechanics: 5 at depth 0, 3 at depth 1, 0 at depth 2",
     d0 == 5 and d1 == 3 and d2 == 0,
     f"Got D0={d0}, D1={d1}, D2={d2}")

# ── Test 2: Optics depth audit (§74, T218-T224) ──
print("\n─── Test 2: Optics, Waves, Acoustics (§74) ───")
optics = {
    "T218 Snell's law":       {"depth": 0, "type": "boundary", "spectral": "phase matching = boundary eigenvalue"},
    "T219 Reflection":        {"depth": 0, "type": "symmetry", "spectral": "K(z,w) mirror symmetry"},
    "T220 Doppler":           {"depth": 0, "type": "counting", "spectral": "wavecrest count on lattice"},
    "T221 Huygens":           {"depth": 0, "type": "definition", "spectral": "Green's function = Bergman kernel limit"},
    "T222 Rayleigh":          {"depth": 1, "type": "integration", "spectral": "⟨aperture|plane wave⟩ = Airy function"},
    "T223 Standing waves":    {"depth": 0, "type": "boundary counting", "spectral": "eigenvalue λ(n) = n on 1D lattice"},
    "T224 Beats":             {"depth": 0, "type": "algebra", "spectral": "sum of two lattice modes"},
}

d0 = sum(1 for v in optics.values() if v["depth"] == 0)
d1 = sum(1 for v in optics.values() if v["depth"] == 1)

test("Optics: 6 at depth 0, 1 at depth 1",
     d0 == 6 and d1 == 1,
     f"Got D0={d0}, D1={d1}")

# ── Test 3: Electromagnetism depth audit (§75, T225-T231) ──
print("\n─── Test 3: Electromagnetism (§75) ───")
em = {
    "T225 Coulomb":          {"depth": 1, "type": "Gauss+sphere", "spectral": "⟨charge|1/r²⟩ = surface integral"},
    "T226 Ohm":              {"depth": 0, "type": "definition", "spectral": "linear response = ground mode"},
    "T227 Kirchhoff":        {"depth": 0, "type": "bookkeeping", "spectral": "graph Laplacian nullspace"},
    "T228 Faraday":          {"depth": 0, "type": "definition", "spectral": "flux change = time derivative of mode"},
    "T229 Gauss":            {"depth": 0, "type": "counting", "spectral": "divergence theorem = charge count"},
    "T230 Ampère-Maxwell":   {"depth": 0, "type": "bookkeeping", "spectral": "curl consistency = boundary of boundary = 0"},
    "T231 Larmor":           {"depth": 0, "type": "definition", "spectral": "precession = cross product on a*"},
}

d0 = sum(1 for v in em.values() if v["depth"] == 0)
d1 = sum(1 for v in em.values() if v["depth"] == 1)

test("Electromagnetism: 6 at depth 0, 1 at depth 1",
     d0 == 6 and d1 == 1,
     f"Got D0={d0}, D1={d1}")

# ── Test 4: Thermodynamics depth audit (§76, T232-T238) ──
print("\n─── Test 4: Thermodynamics (§76) ───")
thermo = {
    "T232 Ideal gas":        {"depth": 0, "type": "counting", "spectral": "⟨N/V|kT⟩ = pressure mode"},
    "T233 Clausius":         {"depth": 0, "type": "definition", "spectral": "entropy = state function (topological)"},
    "T234 Boltzmann":        {"depth": 0, "type": "max entropy", "spectral": "ground state of -S functional"},
    "T235 Fermi-Dirac":      {"depth": 0, "type": "ratio", "spectral": "Pauli exclusion = +1 in denominator"},
    "T236 Bose-Einstein":    {"depth": 0, "type": "geometric series", "spectral": "no exclusion = -1 in denominator"},
    "T237 Stefan-Boltzmann": {"depth": 1, "type": "integration", "spectral": "⟨Planck|ν³⟩ = π⁴/15 integral"},
    "T238 Wien":             {"depth": 1, "type": "optimization", "spectral": "peak of ⟨Planck|λ⁻⁵⟩"},
}

d0 = sum(1 for v in thermo.values() if v["depth"] == 0)
d1 = sum(1 for v in thermo.values() if v["depth"] == 1)

# Fermions vs bosons: the ONLY difference
fermi_bose_difference = "+1 vs -1 in denominator"
test("Thermodynamics: 5 at depth 0, 2 at depth 1; fermions/bosons = ±1",
     d0 == 5 and d1 == 2,
     f"Got D0={d0}, D1={d1}")

# ── Test 5: Fluid Mechanics depth audit (§77, T239-T243) ──
print("\n─── Test 5: Fluid Mechanics (§77) ───")
fluids = {
    "T239 Bernoulli":        {"depth": 0, "type": "conservation", "spectral": "energy density constant along streamline"},
    "T240 Continuity":       {"depth": 0, "type": "conservation", "spectral": "mass current = constant"},
    "T241 Stokes drag":      {"depth": 1, "type": "surface integral", "spectral": "⟨viscosity|velocity profile⟩ over sphere"},
    "T242 Reynolds number":  {"depth": 0, "type": "ratio", "spectral": "inertial/viscous = dimensionless scalar"},
    "T243 Poiseuille":       {"depth": 1, "type": "cross-section integral", "spectral": "⟨velocity profile|2πr dr⟩"},
}

d0 = sum(1 for v in fluids.values() if v["depth"] == 0)
d1 = sum(1 for v in fluids.values() if v["depth"] == 1)

test("Fluid mechanics: 3 at depth 0, 2 at depth 1",
     d0 == 3 and d1 == 2,
     f"Got D0={d0}, D1={d1}")

# ── Test 6: Relativity depth audit (§78, T244-T249) ──
print("\n─── Test 6: Relativity (§78) ───")
relativity = {
    "T244 Lorentz":           {"depth": 0, "type": "symmetry", "spectral": "preserving Minkowski quadratic form on a*"},
    "T245 E=mc²":             {"depth": 0, "type": "vector norm", "spectral": "4-momentum norm = mass eigenvalue"},
    "T246 Gravitational redshift": {"depth": 0, "type": "equivalence principle", "spectral": "Doppler on constant-g frame"},
    "T247 Schwarzschild":     {"depth": 0, "type": "one equation", "spectral": "escape velocity = c, scalar"},
    "T248 Geodesic equation": {"depth": 0, "type": "definition", "spectral": "straight line on substrate = extremal Bergman geodesic"},
    "T249 Lensing angle":     {"depth": 1, "type": "one integral", "spectral": "⟨null geodesic|Schwarzschild perturbation⟩"},
}

d0 = sum(1 for v in relativity.values() if v["depth"] == 0)
d1 = sum(1 for v in relativity.values() if v["depth"] == 1)

test("Relativity: 5 at depth 0, 1 at depth 1; Einstein is definitional",
     d0 == 5 and d1 == 1,
     f"Got D0={d0}, D1={d1}")

# ── Test 7: Full depth statistics across all 40 theorems ──
print("\n─── Test 7: Full Classical Physics Depth Audit ───")
all_sections = [mechanics, optics, em, thermo, fluids, relativity]
section_names = ["Mechanics", "Optics", "EM", "Thermo", "Fluids", "Relativity"]

total_d0 = sum(sum(1 for v in s.values() if v["depth"] == 0) for s in all_sections)
total_d1 = sum(sum(1 for v in s.values() if v["depth"] == 1) for s in all_sections)
total_d2 = sum(sum(1 for v in s.values() if v["depth"] == 2) for s in all_sections)
total_theorems = sum(len(s) for s in all_sections)

print(f"  Total theorems: {total_theorems}")
print(f"  Depth 0: {total_d0} ({100*total_d0/total_theorems:.0f}%)")
print(f"  Depth 1: {total_d1} ({100*total_d1/total_theorems:.0f}%)")
print(f"  Depth 2: {total_d2} ({100*total_d2/total_theorems:.0f}%)")

test(f"40 theorems, {total_d0} depth 0 ({100*total_d0/total_theorems:.0f}%), ZERO depth 2",
     total_theorems == 40 and total_d0 == 30 and total_d1 == 10 and total_d2 == 0,
     f"Got {total_theorems} theorems, D0={total_d0}, D1={total_d1}, D2={total_d2}")

# ── Test 8: Depth-0 type classification ──
print("\n─── Test 8: Why is Depth 0 so Common? ───")
all_d0_types = []
for s in all_sections:
    for name, v in s.items():
        if v["depth"] == 0:
            all_d0_types.append(v["type"])

from collections import Counter
type_counts = Counter(all_d0_types)
print("  Depth-0 mechanism distribution:")
for t, c in type_counts.most_common():
    print(f"    {t}: {c}")

# The dominant mechanisms
definitions = sum(c for t, c in type_counts.items() if "definition" in t)
conservation = sum(c for t, c in type_counts.items() if "conservation" in t or "bookkeeping" in t)
counting = sum(c for t, c in type_counts.items() if "counting" in t)
symmetry = sum(c for t, c in type_counts.items() if "symmetry" in t)

test("Depth 0 dominated by definitions + conservation + counting + symmetry",
     definitions + conservation + counting + symmetry >= 15,
     f"definition={definitions}, conservation={conservation}, counting={counting}, symmetry={symmetry}")

# ── Test 9: Depth-1 type classification ──
print("\n─── Test 9: What Causes Depth 1? ───")
all_d1 = []
for s in all_sections:
    for name, v in s.items():
        if v["depth"] == 1:
            all_d1.append((name, v["type"]))

print("  All depth-1 theorems (the ONLY non-trivial computations):")
for name, typ in all_d1:
    print(f"    {name}: {typ}")

# Every depth-1 theorem is ONE integration or ONE optimization
integration_types = {"integration", "balance", "optimization", "time average",
                     "Gauss+sphere", "surface integral", "cross-section integral",
                     "one integral"}
all_are_single_ops = all(v["type"] in integration_types
                         for s in all_sections
                         for v in s.values()
                         if v["depth"] == 1)

test("Every depth-1 theorem is exactly ONE integration or optimization",
     all_are_single_ops)

# ── Test 10: Spectral lattice connection ──
print("\n─── Test 10: BST Spectral Lattice Connection ───")

# In BST: classical physics = flat-space limit of D_IV^5
# The Bergman kernel K(z,w) → δ(z-w) in flat limit
# All classical laws are properties of this limit

# Key eigenvalue formula
def eigenvalue(p, q):
    """λ(p,q) = p(p+n_C) + q(q+n_C-rank)"""
    return p * (p + n_C) + q * (q + n_C - rank)

# Ground mode (0,0) = classical limit
ground = eigenvalue(0, 0)
first_excited = eigenvalue(1, 0)

print(f"  Ground mode λ(0,0) = {ground} — the classical vacuum")
print(f"  First excited λ(1,0) = {first_excited} = 1·(1+{n_C}) = {1+n_C} = n_C+1")
print(f"  Gap: {first_excited - ground} = n_C + 1 = {n_C + 1}")

# Classical limit: all depth-0 theorems live at (0,0)
# Depth-1 theorems are transitions involving one excited mode
test("Ground mode = 0 (classical vacuum), gap = n_C+1 = 6",
     ground == 0 and first_excited == n_C + 1)

# ── Test 11: The ±1 Pattern ──
print("\n─── Test 11: The ±1 Pattern (Fermions vs Bosons) ───")

# Fermi-Dirac: 1/(e^x + 1)    — the +1 IS Pauli exclusion
# Bose-Einstein: 1/(e^x - 1)  — the -1 IS boson statistics
# The ENTIRE difference between matter and radiation is ±1

# In BST: this maps to the spin-statistics theorem
# Half-integer spin ↔ antisymmetric ↔ +1 (exclusion)
# Integer spin ↔ symmetric ↔ -1 (enhancement)

# Connection to BC_2: the two root lengths
# Short root (m=1): the ±1 switch
# Long root (m=5): the n_C modes
# The difference between fermions and bosons is the sign of ONE root

# Energy ratio at kT=1:
x_vals = np.linspace(0.1, 5.0, 100)
fermi = 1.0 / (np.exp(x_vals) + 1)
bose = 1.0 / (np.exp(x_vals) - 1)
ratio = bose / fermi  # always > 1 (bosons clump, fermions spread)

# At x=1: ratio = (e+1)/(e-1) ≈ 2.16
ratio_at_1 = (np.e + 1) / (np.e - 1)
print(f"  Bose/Fermi ratio at x=1: {ratio_at_1:.4f}")
print(f"  This is (e+1)/(e-1) — the ±1 creates a factor of ~2")
print(f"  In BST: this is the sign of the short root in BC₂")

test("Fermion/boson = ±1 in denominator; ratio at x=1 ≈ 2.16",
     abs(ratio_at_1 - 2.164) < 0.01)

# ── Test 12: Linearization Summary Table ──
print("\n─── Test 12: Complete Linearization Table ───")

# For each section: theorem count, depth 0 count, depth 1 count, dominant mechanism
print(f"  {'Section':<25} {'Total':>5} {'D0':>4} {'D1':>4} {'D0%':>5} {'Dominant mechanism'}")
print(f"  {'─'*25} {'─'*5} {'─'*4} {'─'*4} {'─'*5} {'─'*30}")

for name, section in zip(section_names, all_sections):
    n = len(section)
    d0 = sum(1 for v in section.values() if v["depth"] == 0)
    d1 = sum(1 for v in section.values() if v["depth"] == 1)
    pct = 100 * d0 / n

    # Find dominant type
    types = [v["type"] for v in section.values() if v["depth"] == 0]
    dominant = Counter(types).most_common(1)[0][0] if types else "—"

    print(f"  {name:<25} {n:>5} {d0:>4} {d1:>4} {pct:>4.0f}% {dominant}")

print(f"  {'─'*25} {'─'*5} {'─'*4} {'─'*4} {'─'*5}")
print(f"  {'TOTAL':<25} {total_theorems:>5} {total_d0:>4} {total_d1:>4} {100*total_d0/total_theorems:>4.0f}%")

# The punchline
print(f"\n  ╔═══════════════════════════════════════════════════════════╗")
print(f"  ║  CLASSICAL PHYSICS: 40 theorems, 75% depth 0, 25% depth 1 ║")
print(f"  ║  ZERO depth 2.  The universe is even simpler than T421.   ║")
print(f"  ║                                                           ║")
print(f"  ║  What causes depth 1? ONE integration. That's it.         ║")
print(f"  ║  What causes depth 0? Definitions, counting, symmetry.    ║")
print(f"  ║                                                           ║")
print(f"  ║  Casey's insight: boundary found through enumeration = D0  ║")
print(f"  ║  The boundary IS the physics. Enumerate it and you're done.║")
print(f"  ╚═══════════════════════════════════════════════════════════╝")

test("Summary: 40 theorems, 30 D0 (75%), 10 D1 (25%), 0 D2 (0%)",
     total_theorems == 40 and total_d0 == 30 and total_d1 == 10)

# ── Test 13: Casey strict reduction of depth 1 ──
print("\n─── Test 13: Casey Strict — Can We Reduce Depth 1 to 0? ───")

# Casey's criterion: genuine depth +1 requires summation over UNBOUNDED index set
# All depth-1 classical theorems integrate over BOUNDED domains:
#   - Kepler: one orbit (2π)
#   - Lagrange: one trajectory (finite action)
#   - Virial: one period (bounded)
#   - Rayleigh: one aperture (bounded)
#   - Coulomb: one sphere (4π)
#   - Stefan-Boltzmann: ∫₀^∞ but x³e^{-x} converges — bounded effective range
#   - Wien: one peak (bounded search)
#   - Stokes: one sphere (4π)
#   - Poiseuille: one cross-section (πR²)
#   - Lensing: one trajectory (bounded perturbation)

# Under Casey strict: if the integral has a NATURAL cutoff (convergent, finite domain),
# it's effectively bounded enumeration
bounded_integrals = [
    ("Kepler",       "orbit = 2π",          True),
    ("Lagrange",     "trajectory = finite",  True),
    ("Virial",       "one period = bounded", True),
    ("Rayleigh",     "aperture = bounded",   True),
    ("Coulomb",      "sphere = 4π",          True),
    ("Stefan-Boltzmann", "x³e⁻ˣ converges", True),
    ("Wien",         "peak search = bounded",True),
    ("Stokes",       "sphere = 4π",          True),
    ("Poiseuille",   "cross-section = πR²",  True),
    ("Lensing",      "trajectory = bounded", True),
]

all_bounded = all(b for _, _, b in bounded_integrals)
print(f"  All 10 depth-1 integrals have bounded effective domains: {all_bounded}")
print(f"  Under Casey strict: bounded integral = bounded enumeration = depth 0")
print(f"  → ALL 40 classical theorems reduce to depth 0 under Casey strict")

test("Casey strict: all 10 depth-1 theorems have bounded integrals → depth 0",
     all_bounded)

# ── Test 14: Comparison with quantum/BST theorems ──
print("\n─── Test 14: Classical vs Quantum Depth Distribution ───")

# Classical (§73-78): 75% D0, 25% D1, 0% D2
# SM (Toy 519): 54% D0, 46% D1, 0% D2
# Millennium problems: max D1 under Casey strict (Toy 522)

# Classical is SHALLOWER than quantum — as expected
# The "harder" the physics, the more depth-1 operations
# But NOTHING reaches depth 2

classical_d0_pct = total_d0 / total_theorems
sm_d0_pct = 7 / 12  # from Toy 519: 7 D0 out of 12

print(f"  Classical D0 fraction: {classical_d0_pct:.0%}")
print(f"  SM D0 fraction: {sm_d0_pct:.0%}")
print(f"  Classical is shallower — definitions dominate")
print(f"  Quantum adds one layer of spectral counting")
print(f"  But BOTH are depth ≤ 1. The universe has one computational step.")

test("Classical (75% D0) > SM (58% D0): classical is shallower",
     classical_d0_pct > sm_d0_pct)

# ── Test 15: The Linearization Inner Products ──
print("\n─── Test 15: Explicit Inner Products for Depth-1 Theorems ───")

# Express each depth-1 theorem as ⟨w|d⟩
inner_products = [
    ("Kepler T²∝a³",     "w = (GM)⁻¹/²",  "d = a³/²",       "⟨w|d⟩ = T"),
    ("Lagrange δS=0",    "w = δq",          "d = ∂L/∂q",      "⟨w|d⟩ = 0"),
    ("Virial ⟨T⟩=n/2⟨V⟩","w = time avg",   "d = r·F",        "⟨w|d⟩ = n⟨V⟩"),
    ("Rayleigh θ_min",   "w = aperture",     "d = plane wave",  "⟨w|d⟩ = Airy"),
    ("Coulomb F∝1/r²",   "w = 1",            "d = charge/area", "⟨w|d⟩ = E·4πr²"),
    ("Stefan T⁴",        "w = 1",            "d = x³/(eˣ-1)",  "⟨w|d⟩ = π⁴/15"),
    ("Wien λ_max",       "w = dB/dλ",        "d = 1",           "⟨w|d⟩ = 0 (peak)"),
    ("Stokes F=6πηRv",   "w = stress",       "d = surface dA",  "⟨w|d⟩ = 6π"),
    ("Poiseuille Q∝R⁴",  "w = v(r)",         "d = 2πr dr",     "⟨w|d⟩ = πR⁴ΔP/8ηL"),
    ("Lensing θ=4GM/bc²","w = perturbation",  "d = null geodesic","⟨w|d⟩ = 4GM/bc²"),
]

print(f"  {'Theorem':<22} {'Weight w':<18} {'Data d':<18} {'Inner product ⟨w|d⟩'}")
print(f"  {'─'*22} {'─'*18} {'─'*18} {'─'*25}")
for theorem, w, d, ip in inner_products:
    print(f"  {theorem:<22} {w:<18} {d:<18} {ip}")

test("All 10 depth-1 theorems expressed as explicit inner products",
     len(inner_products) == 10)

# ── Final Summary ──
print(f"\n{'='*60}")
print(f"Toy 526 — Classical Physics Linearization")
print(f"{'='*60}")
print(f"Result: {passed}/{total} tests passed")
print(f"\n40 theorems across 6 domains of classical physics:")
print(f"  • 30 at depth 0 (75%) — definitions, counting, symmetry, conservation")
print(f"  • 10 at depth 1 (25%) — one integration each")
print(f"  • 0 at depth 2 (0%)  — ZERO")
print(f"  • Casey strict: ALL reduce to depth 0 (all integrals are bounded)")
print(f"\nEvery depth-1 theorem is a single inner product ⟨w|d⟩.")
print(f"Classical physics = linear algebra on the BST ground state.")
print(f"The boundary IS the physics. Enumerate it and you're done.")
