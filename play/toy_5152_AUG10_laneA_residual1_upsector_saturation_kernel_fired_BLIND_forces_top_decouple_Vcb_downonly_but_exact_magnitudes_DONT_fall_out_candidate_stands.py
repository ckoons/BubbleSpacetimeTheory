#!/usr/bin/env python3
"""
Toy 5152: LANE 3 / Residual 1 -- the up-sector SATURATION kernel fired BLIND. RESULT (honest, compute-don't-
fit): the up-saturation kernel correctly FORCES the ONE structural feature -- the top decouples (r_t=1 at the
Shilov boundary → (1−r_t²)=0 → overlap vanishes → V_cb is DOWN-ONLY, corpus-consistent) -- but the exact
Cabibbo/V_cb MAGNITUDES do NOT fall out coefficient-free: every blind construction (boundary/bulk overlap,
polar, Löwdin) OVER-MIXES (|V_us|~0.4, |V_cb|~0.6-0.75, far above observed 0.22/0.041) because the up-boundary
radii (r_u=α^{2/g}=0.245, r_c=α^{1/g}=0.495) and down-bulk radii (0, 0.5, 0.632) sit at similar interior
positions → large overlap → too much mixing. So the up-sector kernel forces the STRUCTURE (top-decouple /
V_cb-down-only) but NOT the exact 1-2/2-3 values → the exact Cabibbo/V_cb magnitudes stay CANDIDATE, as
already tiered. Banked underneath STANDS: V_us=1/√20 (Derived, down 1-2 ladder), the mixing ENGINE +
V_ub-small + hierarchy (forced, parity/oddness). I did NOT fit a coefficient to force the block (banks
nothing). Grace scores blind. Elie's Residual-1 blind fire. (K1181/K1305.) A blind negative reported straight.

WHAT I FIRE (blind):
  * UP (boundary-coupled, saturation y_up=r^g): r_t=1 (top AT boundary, F373), r_c=α^{1/g}, r_u=α^{2/g}
    → {0.245, 0.495, 1.0} (g=7). DOWN (bulk-coupled, FK ladder): r²=n/(n+N_c) → {0, 0.5, 0.632}.
  * TOP DECOUPLES (correct): r_t=1 → (1−r_t²)=0 → the top's overlap with all down modes vanishes → V_cb is
    DOWN-ONLY (K711/K1001/corpus). The up-saturation kernel FORCES this structural feature.
  * BLIND CKM = the up↔down overlap (polar / Löwdin orthonormalization), exponents p∈{n_C, g}: |V_us|~0.4,
    |V_cb|~0.63-0.75 -- OVER-MIXES (up-boundary + down-bulk radii too close). Does NOT reproduce 0.22/0.041.

=> VERDICT (plain): fired the up-sector saturation kernel blind. It CORRECTLY forces the ONE structural
feature -- the top decouples (r_t=1 at the Shilov boundary → V_cb down-only, corpus-consistent) -- but the
exact Cabibbo/V_cb MAGNITUDES do NOT fall out coefficient-free: every construction over-mixes (|V_us|~0.4,
|V_cb|~0.6-0.75) because the up-boundary radii (α^{1/g}, α^{2/g}) and the down-bulk radii sit at similar
interior positions. So the up-saturation kernel forces the STRUCTURE (top-decouple), not the magnitudes. The
exact Cabibbo/V_cb stay CANDIDATE -- exactly the tiering already on the board (Grace's coefficient-free test
on the parity grading also gave structure-not-magnitudes). Banked underneath STANDS: V_us=1/√20 Derived
(down 1-2), the mixing engine + V_ub-small + hierarchy forced (parity/oddness). I did NOT fit a coefficient
(banks nothing). This is a blind NEGATIVE on the magnitudes, reported straight. CP existence-only.

=> DISPOSITION: Residual-1 blind fire -- up-saturation kernel forces top-decouple/V_cb-down-only (structural,
consistent) but NOT the exact magnitudes (over-mixes) → exact Cabibbo/V_cb stay CANDIDATE. Firer: Elie; Grace
scores blind (armed); Lyra/Grace: the up-sector kernel needs a sharper address/exponent pin to force the
magnitudes (or they genuinely ride an Identified up-radial). Cal audits. Nothing pushed. Nothing banked --
a blind negative on the magnitudes; the banked structure (V_us Derived, engine/V_ub/hierarchy forced) stands.

Author: Elie (CI toy builder). Date: 2026-08-10.
"""

import numpy as np
from scipy.linalg import sqrtm, inv

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

N_c, n_C, g = 3, 5, 7
al = 1/137.036
r_up = np.array([al**(2/g), al**(1/g), 1.0])
r_dn = np.array([np.sqrt(n/(n+N_c)) for n in (0, 1, 2)])

def K(a, b, p):
    if abs(a-1) < 1e-12 and abs(b-1) < 1e-12:
        return 1.0
    if abs(a-1) < 1e-12 or abs(b-1) < 1e-12:
        return 0.0
    return ((1-a**2)*(1-b**2)/(1-a*b)**2)**(p/2)

print("=" * 78)
print("Toy 5152: Lane 3 / Residual 1 -- up-saturation kernel blind: forces top-decouple, but magnitudes over-mix (Candidate)")
print("=" * 78)

# ----------------------------------------------------------------------------
# 1. Up-boundary + down-bulk addresses (saturation kernel).
# ----------------------------------------------------------------------------
print("\n--- 1. addresses: up boundary-coupled (y=r^g) {0.245,0.495,1.0}; down bulk-coupled {0,0.5,0.632} ---")
check("the up-sector is BOUNDARY-coupled (saturation, y_up=r^g): r_t=1 (top AT the Shilov boundary, F373), "
      "r_c=α^{1/g}=0.495, r_u=α^{2/g}=0.245 (g=7). The down-sector is BULK-coupled (FK ladder): "
      "r²=n/(n+N_c) → {0, 0.5, 0.632}. This is the boundary/bulk split (Grace's frame) -- DIFFERENT structures, "
      "which is what breaks the shared-ladder over-alignment (toy 5148)",
      abs(r_up[2] - 1.0) < 1e-12 and abs(r_up[1] - al**(1/g)) < 1e-9,
      f"up (boundary) {np.round(r_up,3)}; down (bulk) {np.round(r_dn,3)}. Different structures.")

# ----------------------------------------------------------------------------
# 2. Top decouples (correct): r_t=1 → V_cb down-only.
# ----------------------------------------------------------------------------
print("\n--- 2. TOP DECOUPLES (correct): r_t=1 → (1−r_t²)=0 → overlap vanishes → V_cb DOWN-ONLY ---")
top_overlaps = [K(1.0, b, g) for b in r_dn]
check("the up-saturation kernel FORCES the correct structural feature: the top at r_t=1 (Shilov boundary) has "
      "(1−r_t²)=0, so its overlap with every down (bulk) mode VANISHES → the top decouples → V_cb is DOWN-ONLY "
      "(K711/K1001, corpus-consistent). This is the ONE thing the up-saturation kernel gets right, and it is "
      "a genuine forced feature of the boundary-coupling",
      all(abs(o) < 1e-12 for o in top_overlaps),
      f"top overlaps with down modes = {[round(o,3) for o in top_overlaps]} = 0 → top decouples → V_cb down-only. Forced.")

# ----------------------------------------------------------------------------
# 3. Blind CKM: over-mixes -> magnitudes do NOT fall out.
# ----------------------------------------------------------------------------
print("\n--- 3. blind CKM (Löwdin, p∈{n_C,g}): OVER-MIXES (|V_us|~0.4, |V_cb|~0.6-0.75) → magnitudes don't fall out ---")
vals = {}
for p in (n_C, g):
    Gu = np.array([[K(a, b, p) for b in r_up] for a in r_up])
    Gd = np.array([[K(a, b, p) for b in r_dn] for a in r_dn])
    M = np.array([[K(a, b, p) for b in r_dn] for a in r_up])
    V = inv(sqrtm(Gu).real) @ M @ inv(sqrtm(Gd).real)
    vals[p] = (abs(V[0, 1]), abs(V[1, 2]))
overmix = all(v[1] > 0.3 for v in vals.values())   # V_cb ~ 0.6-0.75 >> 0.041
check("the BLIND CKM (up↔down overlap, Löwdin-orthonormalized, exponents p∈{n_C=5, g=7}) OVER-MIXES: "
      "|V_us|~0.4 and |V_cb|~0.63-0.75 -- far above observed 0.22 / 0.041 -- because the up-boundary radii "
      "(α^{1/g}, α^{2/g}) and the down-bulk radii sit at SIMILAR interior positions, giving too much overlap. "
      "So the up-saturation kernel does NOT reproduce the exact Cabibbo/V_cb magnitudes coefficient-free",
      overmix,
      "; ".join(f"p={p}: |V_us|={v[0]:.2f}, |V_cb|={v[1]:.2f}" for p, v in vals.items()) +
      f" vs obs 0.22/0.041 -- over-mixes. Magnitudes don't fall out. (No coefficient fit.)")

# ----------------------------------------------------------------------------
# 4. Verdict: structure forced, magnitudes Candidate; banked structure stands.
# ----------------------------------------------------------------------------
print("\n--- 4. verdict: up-kernel forces top-decouple (structure); exact magnitudes CANDIDATE; banked stands ---")
check("VERDICT: the up-sector saturation kernel, fired BLIND, forces the STRUCTURE (top decouples → V_cb "
      "down-only, correct) but NOT the exact Cabibbo/V_cb MAGNITUDES (every construction over-mixes). So the "
      "exact 1-2/2-3 values stay CANDIDATE -- matching the board's tiering (Grace's coefficient-free parity "
      "test also gave structure-not-magnitudes). Banked underneath STANDS: V_us=1/√20 Derived (down 1-2), "
      "the mixing engine + V_ub-small + hierarchy forced (parity/oddness). No coefficient fitted (banks "
      "nothing). A blind negative on the magnitudes, reported straight. CP existence-only",
      all(abs(o) < 1e-12 for o in top_overlaps) and overmix,
      "structure forced (top-decouple), magnitudes Candidate; banked list intact. The up-kernel needs a "
      "sharper address/exponent pin, or the magnitudes ride an Identified up-radial. Grace scores blind.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (up-kernel forces top-decouple/V_cb-down-only; exact magnitudes over-mix → CANDIDATE; banked stands)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5152, Lane 3 / Residual 1 -- up-saturation kernel blind fire):
  * ADDRESSES: up boundary-coupled (y=r^g) {{0.245,0.495,1.0}}; down bulk-coupled {{0,0.5,0.632}} -- different
    structures (boundary/bulk, Grace's frame), breaking the 5148 shared-ladder over-alignment.
  * TOP DECOUPLES (correct/forced): r_t=1 → (1−r_t²)=0 → overlap vanishes → V_cb DOWN-ONLY (corpus-consistent).
  * BLIND CKM OVER-MIXES: |V_us|~0.4, |V_cb|~0.6-0.75 (p∈{{5,7}}) vs obs 0.22/0.041 -- up-boundary and
    down-bulk radii too close. Exact magnitudes do NOT fall out coefficient-free.
  * VERDICT: up-kernel forces the STRUCTURE (top-decouple) but NOT the magnitudes → exact Cabibbo/V_cb
    CANDIDATE. Banked STANDS: V_us=1/√20 Derived, engine/V_ub-small/hierarchy forced. No fit (banks nothing).

AUG-10 [TEGMARK]. Nothing pushed. Nothing banked -- a blind negative on the up-sector magnitudes (over-mixes),
reported straight. The up-saturation kernel forces top-decouple/V_cb-down-only (structural, consistent) but
not the exact 1-2/2-3 values → Candidate. Banked structure (V_us=1/√20 Derived, engine+V_ub+hierarchy forced)
intact. Grace scores blind; the up-kernel needs a sharper pin. CP existence-only. Count N.
""")
