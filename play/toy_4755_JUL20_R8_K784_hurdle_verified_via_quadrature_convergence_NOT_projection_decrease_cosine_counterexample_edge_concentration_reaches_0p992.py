#!/usr/bin/env python3
"""
Toy 4755 — Jul 20 (Round-8 K784 hurdle, fish-detector on the load-bearing linear-algebra claim, mine): Keeper's K784
says the tiling test is a MEASURE question — the physical overlap ⟨t|O⟩ is 0.985 (continuous Γ-ratio) vs 0.992 (=127/128,
discrete count), and since 0.992 > 0.985, a tiling that COARSE-GRAINS the continuum "generically DECREASES the overlap
(projection)" and so "cannot reach 127/128" → 127/128 needs a FUNDAMENTALLY discrete surface, not an emergent blur. My
job (verify the hurdle before Lyra runs the full computation): the hurdle's CONCLUSION is CORRECT, but its stated
MECHANISM ("projection generically decreases the overlap") is IMPRECISE for the physical (normalized) overlap. The clean,
wavefunction-independent reason is QUADRATURE CONVERGENCE, and it actually sharpens the hurdle.

THREE wavefunction-INDEPENDENT linear-algebra facts (representative aligned radial functions, O=x², t=x³ on [0,1], y_cont
= 0.986 ≈ the 0.985 regime):
  FACT 1 — QUADRATURE CONVERGENCE (the real hurdle, robust): a fine 128-cell quadrature of the continuous inner product
    REPRODUCES the continuum: y_quad = 0.98602 vs y_cont = 0.98601 (5-digit match). So ANY discrete measure that
    APPROXIMATES the continuum (a coarse-graining / partition of the continuous surface) gives BACK 0.985 — the "secretly
    the continuum → 127/128 fails" outcome is the DEFAULT. To reach 0.992 the discrete measure must be genuinely
    NON-continuum (fundamentally discrete), NOT a fine partition. → CONFIRMS K784's conclusion, cleaner mechanism.
  FACT 2 — the stated mechanism is imprecise (fish-detector correction): the physical y is a NORMALIZED cosine
    ⟨t|O⟩/(‖t‖‖O‖) (Cauchy-Schwarz ceiling, y≤1). "Projection generically DECREASES aligned overlaps" is a RAW-overlap
    statement and is FALSE for the normalized cosine: projecting out an ANTI-aligned component INCREASES the cosine.
    Counterexample: t=(1,.1,.2), O=(1,.1,−.2) → cos = 0.924; project out the anti-aligned 3rd coord → cos = 1.0
    (INCREASED). So "projection decreases" is not a hurdle for the normalized overlap; QUADRATURE CONVERGENCE (Fact 1) is
    the correct reason a coarse-graining can't reach 0.992.
  FACT 3 — what "fundamentally discrete" MUST do (sharpen, ties to edge-placement): to exceed 0.985 the discrete measure
    must CONCENTRATE weight where t and O agree most — the BOUNDARY EDGE (x→1, where both → the aligned limit). A heavy
    edge-cell weight raises y: ×50 → 0.99279 (just past 0.992). So reaching 0.992 is ACHIEVABLE but requires a specific
    EDGE-CONCENTRATED measure (boundary emission — Casey's picture), NOT automatic. This is the same content as
    edge-placement (top = boundary-edge mode, round 7): the fundamentally-discrete measure must weight the boundary edge.

⟹ VERDICT: the K784 hurdle is REAL and its CONCLUSION stands — a coarse-graining of the continuous surface reproduces
0.985 (quadrature convergence, Fact 1), so reaching 0.992 = 127/128 REQUIRES a fundamentally-discrete, NON-continuum,
EDGE-CONCENTRATED measure (Facts 1+3), exactly Casey's interior-discrete + boundary-emission. But the stated mechanism
("projection generically decreases the overlap") is imprecise: for the normalized physical cosine, projection can
INCREASE it (Fact 2) — the correct reason is quadrature convergence, which is cleaner and sharper. So: hurdle confirmed,
mechanism corrected, content located (edge-concentration). 127/128 stays twice-downgraded — conditional on Lyra's real
discrete-series measure clearing Fact 1 (genuinely non-continuum) AND Fact 3 (edge-concentrated). I verify her discrete
sum vs the Γ-integral when it lands. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
twog = 2**g  # 128
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# representative aligned radial functions on [0,1]; O boundary-reaching, t the top
f = lambda x: x**2      # O = SO(5) vector (spherical, boundary-reaching)
h = lambda x: x**3      # t = top (non-spherical, slightly steeper)
y_cont = (1/6)/np.sqrt((1/5)*(1/7))   # exact continuous normalized overlap (polynomials)

# ---- FACT 1: quadrature convergence ------------------------------------------
N = twog; xc = (np.arange(N)+0.5)/N; w = np.ones(N)/N
num = np.sum(f(xc)*h(xc)*w); nf = np.sqrt(np.sum(f(xc)**2*w)); nh = np.sqrt(np.sum(h(xc)**2*w))
y_quad = num/(nf*nh)
print(f"\n[Fact 1] y_cont = {y_cont:.5f}; 128-cell quadrature y_quad = {y_quad:.5f} (reproduces continuum)")
check("FACT 1 — QUADRATURE CONVERGENCE (the real hurdle, wavefunction-independent): a fine 128-cell quadrature of the "
      "continuous inner product REPRODUCES the continuum (y_quad = 0.98602 vs y_cont = 0.98601). So ANY discrete measure "
      "that APPROXIMATES the continuum (a coarse-graining / partition of the surface) gives BACK 0.985 — 'secretly the "
      "continuum → 127/128 fails' is the DEFAULT. Reaching 0.992 needs a genuinely NON-continuum (fundamentally discrete) "
      "measure. Confirms K784's conclusion via the clean mechanism.",
      abs(y_quad - y_cont) < 1e-3, "128-cell quadrature reproduces the continuum (0.986) → any continuum-approximating discrete measure gives 0.985, not 0.992")

# ---- FACT 2: projection can INCREASE the normalized cosine (mechanism fix) ----
t3 = np.array([1.0, 0.1, 0.2]); O3 = np.array([1.0, 0.1, -0.2])
cos_before = t3@O3/(np.linalg.norm(t3)*np.linalg.norm(O3))
cos_after = t3[:2]@O3[:2]/(np.linalg.norm(t3[:2])*np.linalg.norm(O3[:2]))
print(f"[Fact 2] cosine before projection = {cos_before:.4f}; after (anti-aligned coord removed) = {cos_after:.4f} → INCREASED")
check("FACT 2 — the stated mechanism is imprecise (fish-detector correction): the physical y is a NORMALIZED cosine "
      "(Cauchy-Schwarz, y≤1). 'Projection generically DECREASES aligned overlaps' is a RAW-overlap claim and is FALSE for "
      "the normalized cosine — projecting out an ANTI-aligned component INCREASES it. Counterexample: t=(1,.1,.2), "
      "O=(1,.1,−.2) → cos 0.924 → project out the anti-aligned 3rd coord → cos 1.0. So 'projection decreases' is NOT the "
      "hurdle; quadrature convergence (Fact 1) is the correct reason.",
      cos_after > cos_before and abs(cos_after - 1.0) < 1e-9, "projection INCREASED the normalized cosine (0.924→1.0) → 'projection generically decreases' is imprecise; quadrature convergence is the right mechanism")

# ---- FACT 3: reaching 0.992 needs edge-concentration --------------------------
ys = {}
for W in [1, 10, 50, 200]:
    wt = np.ones(N)/N; wt[-1] *= W
    nu = np.sum(f(xc)*h(xc)*wt); a = np.sqrt(np.sum(f(xc)**2*wt)); b = np.sqrt(np.sum(h(xc)**2*wt))
    ys[W] = nu/(a*b)
reaches = any(y >= 127/twog for y in ys.values())
print(f"[Fact 3] edge-weighting → y: {{{', '.join(f'x{W}:{ys[W]:.5f}' for W in ys)}}}; 127/128={127/twog:.5f}")
check("FACT 3 — what 'fundamentally discrete' MUST do (ties to edge-placement): to EXCEED 0.985 the discrete measure must "
      "CONCENTRATE weight where t and O agree most — the BOUNDARY EDGE (x→1). A heavy edge-cell weight raises y: ×50 → "
      "0.99279 (past 0.992). So reaching 0.992 is ACHIEVABLE but requires a specific EDGE-CONCENTRATED measure (boundary "
      "emission — Casey's picture), NOT automatic. Same content as edge-placement (top = boundary-edge mode, round 7): the "
      "fundamentally-discrete measure must weight the boundary edge.",
      reaches, "heavy edge-cell weight raises y past 0.992 (×50→0.9928) → reaching 0.992 needs a specific edge-concentrated measure, not automatic")

# ---- data check (unchanged, my standing role) -------------------------------
vr = 246.22/np.sqrt(2)
check("DATA CHECK (unchanged, pole scheme): 127/128 → 172.74 (data-consistent); continuum 0.985 → 171.5 and 126/128 → "
      "171.4 (~1.2 GeV low). So the data still leans toward the discrete-count value — the content is whether Lyra's real "
      "discrete-series measure is fundamentally discrete (Fact 1) AND edge-concentrated (Fact 3) enough to reach 0.992 and "
      "place the top at the maximal codeword.",
      abs((127/twog)*vr - 172.74) < 0.1, f"127/128→{(127/twog)*vr:.2f} data-consistent; continuum & 126/128 ~1.2 GeV low; content = does the real discrete measure clear Facts 1+3")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: the K784 hurdle is REAL and its CONCLUSION stands — a coarse-graining of the continuous surface reproduces "
      "0.985 (quadrature convergence, Fact 1), so reaching 127/128 REQUIRES a fundamentally-discrete, NON-continuum, "
      "EDGE-CONCENTRATED measure (Facts 1+3) — exactly Casey's interior-discrete + boundary-emission. But the stated "
      "mechanism ('projection generically decreases') is imprecise: for the normalized physical cosine, projection can "
      "INCREASE it (Fact 2) — the correct reason is quadrature convergence. Hurdle confirmed, mechanism corrected, content "
      "located (edge-concentration). 127/128 twice-downgraded; I verify Lyra's discrete sum vs the Γ-integral when it lands.",
      abs(y_quad - y_cont) < 1e-3 and cos_after > cos_before and reaches,
      "hurdle CONFIRMED via quadrature convergence (not projection-decrease, Fact 2); reaching 0.992 needs fundamentally-discrete + edge-concentrated measure; verify Lyra's result")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-8 K784 HURDLE — fish-detector verification (mine): hurdle CONFIRMED, mechanism CORRECTED, content LOCATED:
  * FACT 1 (robust): a 128-cell quadrature reproduces the continuum (0.986) → any continuum-approximating discrete measure gives 0.985, NOT 0.992. → need genuinely non-continuum discreteness. Confirms K784.
  * FACT 2 (correction): 'projection generically decreases the overlap' is FALSE for the normalized cosine — projection can INCREASE it (0.924→1.0). The right mechanism is quadrature convergence, not projection-decrease.
  * FACT 3 (sharpen): reaching 0.992 needs a specific EDGE-CONCENTRATED measure (×50 edge-weight → 0.9928) — Casey's boundary-emission; = edge-placement content. Achievable, not automatic.
  => hurdle real; 127/128 conditional on Lyra's real discrete-series measure being fundamentally-discrete (Fact 1) AND edge-concentrated (Fact 3). Twice-downgraded. I verify her discrete sum when it lands.
""")
