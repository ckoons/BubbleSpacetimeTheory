"""
BST: Is d_0 the Bergman Distance Between Adjacent Committed Contacts?
=====================================================================
Test Casey's insight: d_0/l_Pl = geodesic/kernel distance between two
adjacent committed contacts on the Shilov boundary Sigma of D_IV^5.

Shilov boundary: Sigma = S^4 x S^1, parameterized as z = e^{i*theta} * u
where u is a real unit vector in R^5.

Bergman kernel: K(z,w) = (1920/pi^5) / (1 - 2<z,w_bar> + (z.z)(w_bar.w_bar))^6
Norm form: N(z,w) = 1 - 2<z,w_bar> + (z.z)(w_bar.w_bar)
On Sigma for S^4-adjacent points (same S^1 phase): N = 2(1 - cos(phi))

Author: Casey Koons & Claude (Anthropic), March 2026
"""
import numpy as np
pi = np.pi

# ── BST constants ──────────────────────────────────────────────────────────────
alpha   = 1.0 / 137.036082     # Wyler fine structure constant
N_max   = 137
l_star  = 5
F_BST   = 0.09855              # vacuum free energy (exact, partition fn)
Vol_D5  = pi**5 / 1920         # real volume of D_IV^5 = 0.050733
n_C     = 5                    # complex dimension of D_IV^5

Lambda_obs = 2.9e-122          # observed Lambda, Planck units
d0_target  = (Lambda_obs / F_BST)**0.25   # = 7.365e-31

print(f"TARGET:  d_0/l_Pl = {d0_target:.6e}")
print(f"         log10    = {np.log10(d0_target):.4f}")
print()

# ── 1. Powers of alpha ─────────────────────────────────────────────────────────
print("=" * 62)
print("1. d_0/l_Pl = alpha^n  (exact n?)")
print("=" * 62)
n_alpha = np.log(d0_target) / np.log(alpha)
print(f"   Exact n = {n_alpha:.6f}")
print()
print(f"   {'n':>6}  {'alpha^n':>12}  {'error':>8}")
for n in [12, 13, 14, 14.1, 14.5, 15]:
    v = alpha**n
    e = (v - d0_target)/d0_target*100
    flag = " ◄" if abs(e) < 5 else ""
    print(f"   {n:6.1f}  {v:12.4e}  {e:+7.1f}%{flag}")
print()

# ── 2. Norm form N(z,w) on the Shilov boundary ────────────────────────────────
print("=" * 62)
print("2. Norm form N(z,w) on Sigma for various angular separations")
print("   Bergman kernel: K = (1920/pi^5) / N^6")
print("   Szego  kernel:  S = C / N^5")
print("=" * 62)

# Natural angular separations on S^4 at l* = 5
separations = [
    ("pi/(l*+1) = pi/6     [adj at l*=5]",  pi/(l_star+1)),
    ("pi/sqrt(N_max)        [N_max packing]", pi/N_max**0.5),
    ("alpha                 [fine struct]",   alpha),
    ("1/N_max               [1/137]",         1/N_max),
    ("alpha^2               [alpha^2]",       alpha**2),
]

C_berg = 1920/pi**5    # = 1/Vol(D_IV^5)

print(f"\n   {'Separation':42s}  {'phi':>8}  {'N(z,w)':>10}  {'K':>10}  {'N^k=d0: k':>10}")
for label, phi in separations:
    N  = 2*(1 - np.cos(phi))           # norm form for S^4 angle phi
    K  = C_berg / N**(n_C+1)          # Bergman kernel value
    # What power of N gives d0?
    k_N = np.log(d0_target) / np.log(N) if N > 0 else float('nan')
    # What power of K gives d0?
    k_K = np.log(d0_target) / np.log(K) if K > 0 and K != 1 else float('nan')
    print(f"   {label:42s}  {phi:8.4f}  {N:10.4e}  {K:10.4e}  k={k_N:.3f}")
print()

# ── 3. Bergman metric at z=0, geodesic step ───────────────────────────────────
print("=" * 62)
print("3. Bergman metric at z=0: ds = sqrt(2(n+1)) |dz| = sqrt(12) |dz|")
print("   If 'step' = alpha, what is ds_B?")
print("=" * 62)
ds_B_alpha = np.sqrt(2*(n_C+1)) * alpha
print(f"   ds_B(alpha) = sqrt(12) * alpha = {ds_B_alpha:.6e}")
n_dsB = np.log(d0_target) / np.log(ds_B_alpha)
print(f"   (ds_B)^n = d0 requires n = {n_dsB:.4f}")
print()

# Bergman area (2D step)
area_B = ds_B_alpha**2
n_area = np.log(d0_target) / np.log(area_B)
print(f"   Bergman area = ds_B^2 = {area_B:.6e}")
print(f"   (area)^n = d0 requires n = {n_area:.4f}")
print()

# ── 4. The alpha^14 correction factor ─────────────────────────────────────────
print("=" * 62)
print("4. Since n_exact ≈ 14.10, what is d0 / alpha^14?")
print("=" * 62)
corr = d0_target / alpha**14
print(f"   d0 / alpha^14 = {corr:.8f}")
print()
print(f"   BST constants for comparison:")
print(f"     Vol(D_IV^5)        = {Vol_D5:.8f}")
print(f"     F_BST              = {F_BST:.8f}")
print(f"     alpha              = {alpha:.8f}")
print(f"     1/sqrt(N_max)      = {1/N_max**0.5:.8f}")
print(f"     1/N_max            = {1/N_max:.8f}")
print(f"     pi/1920            = {pi/1920:.8f}")
print(f"     Vol(S^4)=8pi^2/3   = {8*pi**2/3:.8f}")
print(f"     pi^5/(137*1920)    = {pi**5/(137*1920):.8f}")
print(f"     sqrt(Vol_D5)       = {Vol_D5**0.5:.8f}")
print(f"     Vol_D5^(1/4)       = {Vol_D5**0.25:.8f}")
print(f"     alpha * N_max      = {alpha*N_max:.8f}")
print(f"     2*Vol_D5           = {2*Vol_D5:.8f}")
# The correction 0.609 — what geometric number is it?
print()
print(f"   Correction factor = {corr:.6f}")
print(f"     = 1/e^0.5 ?      ({1/np.e**0.5:.6f}  diff={abs(corr-1/np.e**0.5)/corr*100:.2f}%)")
print(f"     = Vol_D5/alpha?  ({Vol_D5/alpha:.6f}  diff={abs(corr-Vol_D5/alpha)/corr*100:.2f}%)")
print(f"     = alpha^0.1?     ({alpha**0.1:.6f}  diff={abs(corr-alpha**0.1)/corr*100:.2f}%)")
print(f"     = 2*Vol_D5^1.5?  ({2*Vol_D5**1.5:.6f}  diff={abs(corr-2*Vol_D5**1.5)/corr*100:.2f}%)")
print(f"     = (pi/6)^(1/2)?  ({(pi/6)**0.5:.6f}  diff={abs(corr-(pi/6)**0.5)/corr*100:.2f}%)")
print(f"     = sqrt(F_BST/pi)? ({(F_BST/pi)**0.5:.6f}  diff={abs(corr-(F_BST/pi)**0.5)/corr*100:.2f}%)")
print()

# ── 5. The most natural BST formula candidates ────────────────────────────────
print("=" * 62)
print("5. Best candidate formulas for d_0/l_Pl")
print("=" * 62)
candidates = [
    ("alpha^14.10",                      alpha**14.10),
    ("alpha^14 * alpha^0.1",             alpha**14 * alpha**0.1),
    ("alpha^14 * Vol_D5",                alpha**14 * Vol_D5),
    ("(alpha/pi)^14",                    (alpha/pi)**14),
    ("alpha^(2*(n+2)) = alpha^14",       alpha**(2*(n_C+2))),
    ("alpha^(2*n+4) = alpha^14",         alpha**(2*n_C+4)),
    ("Vol_D5^(n+1) = Vol^6",             Vol_D5**(n_C+1)),
    ("Vol_D5^30",                        Vol_D5**30),
    ("(alpha*F_BST)^7",                  (alpha*F_BST)**7),
    ("alpha^13 * Vol_D5^0.5",            alpha**13 * Vol_D5**0.5),
    ("alpha^12 * Vol_D5",                alpha**12 * Vol_D5),
    ("alpha^14 / sqrt(N_max)",           alpha**14 / N_max**0.5),
    ("(alpha^2 * Vol_D5)^(n+1)/2",       (alpha**2 * Vol_D5)**((n_C+1)/2)),
]

print(f"   {'Formula':42s}  {'Value':>12}  {'Error':>8}")
for label, val in candidates:
    e = (val - d0_target)/d0_target*100
    flag = " ◄◄" if abs(e) < 1 else (" ◄" if abs(e) < 10 else "")
    print(f"   {label:42s}  {val:12.4e}  {e:+7.1f}%{flag}")
print()

# ── 6. Verdict ────────────────────────────────────────────────────────────────
print("=" * 62)
print("6. VERDICT")
print("=" * 62)
best_N = 2*(1 - np.cos(pi/(l_star+1)))
k_best = np.log(d0_target) / np.log(best_N)
print(f"""
   The target d_0/l_Pl = {d0_target:.4e}

   BEST POWER LAW: alpha^{n_alpha:.3f}
     n ≈ 14.10, close to 14 = 2*(n_C+2) = 2*(5+2) for D_IV^5
     but 0.10 extra — not a clean integer.

   BERGMAN NORM: N(adjacent, l*=5) = {best_N:.4f}
     N^k = d0 requires k = {k_best:.3f}
     k ≈ 14 would give N^14 = {best_N**14:.4e}  (vs target {d0_target:.4e})

   STRUCTURAL FINDING:
     d_0 appears to involve alpha to a power near 14 = 2(n_C+2),
     suggesting a SQUARE of the Bergman kernel power (n+1=6 → 2×6=12)
     plus a correction ≈ 2 from the contact AREA vs contact LENGTH.

     The exact formula requires the partition function: d_0 is NOT
     a pure D_IV^5 geometric constant — it is the area per committed
     contact pair, which involves the full thermodynamic spectrum.

   DOES THE GUESS FEEL RIGHT?
     Structurally YES — the Bergman geometry sets the scale and the
     power n≈14 has a natural BST interpretation (double the Bergman
     kernel exponent, reflecting AREA not distance).
     Exactly: NO — a clean formula still needs the partition function
     to determine the prefactor/exponent precisely.
""")
