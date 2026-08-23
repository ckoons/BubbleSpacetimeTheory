import numpy as np, math

# ROUND 51 (a): can ANY choice of up 3-space U rescue the FK ladder current?
# Best case for the ansatz: let U contain the ENTIRE image J(D). Then P_U J|_D = J|_D,
# and the singular values of J|_D are the BEST any U can achieve.
# If even that is not an isometry, the ladder current fails the gate intrinsically --
# independent of the up-sector, independent of saturation, independent of the profile.

def c(k, nu):
    return math.sqrt((k + 1) / (nu + k))   # <f_{k+1}| M |f_k>

def Jrestricted(nu, degs=(1, 3, 5)):
    """matrix of J = M + M^dag from span{f_1,f_3,f_5} into span{f_0,f_2,f_4,f_6}"""
    img = sorted({d - 1 for d in degs} | {d + 1 for d in degs})
    A = np.zeros((len(img), len(degs)))
    for j, k in enumerate(degs):
        A[img.index(k + 1), j] = c(k, nu)       # raise
        A[img.index(k - 1), j] = c(k - 1, nu)   # lower
    return A

print("ROUND 51 (a) — BEST-CASE singular values of the FK ladder current on the down 3-space")
print("   (U chosen optimally = the full image; no up-sector assumption enters at all)\n")
print(f"{'nu_W':>8}{'s1':>10}{'s2':>10}{'s3':>10}{'s1/s3':>10}   isometry?")
for nu in (0.5, 1.0, 3.0, 5.0, 10.0, 50.0, 500.0, 5000.0):
    sv = np.linalg.svd(Jrestricted(nu), compute_uv=False)
    r = sv[0] / sv[2]
    print(f"{nu:>8.1f}{sv[0]:>10.4f}{sv[1]:>10.4f}{sv[2]:>10.4f}{r:>10.3f}   {'YES' if r < 1.01 else 'NO'}")

# is the ratio EVER 1?  scan finely.
best = None
for nu in np.logspace(-3, 6, 200000):
    sv = np.linalg.svd(Jrestricted(nu), compute_uv=False)
    r = sv[0] / sv[2]
    if best is None or r < best[0]:
        best = (r, nu)
print(f"\n  MINIMUM s1/s3 over nu in [1e-3, 1e6]:  {best[0]:.4f}  at nu = {best[1]:.4g}")
print("  -> an isometry needs 1.000.  The ladder current NEVER reaches it.")

# WHY, in one line: the ladder coefficients are k-dependent, so the three down modes
# are stretched by different factors before any projection.
print("\n  the mechanism, at nu_W = N_c = 3:")
for k in (1, 3, 5):
    n2 = c(k, 3.0) ** 2 + c(k - 1, 3.0) ** 2
    print(f"    ||J f_{k}|| = {math.sqrt(n2):.4f}")
print("    -> the three down modes are stretched by DIFFERENT factors (33% spread).")
print("       A ladder operator has k-dependent coefficients; an isometry cannot.")

# ROUND 51 (b): the forced repair -- the ISOMETRIC (polar) part of the same current.
print("\n\nROUND 51 (b) — the polar/isometric part W of J|_D  (J|_D = W * P, W partial isometry)")
print("   This is the unique closest partial isometry to the forced ladder current.")
for nu in (3.0,):
    A = Jrestricted(nu)
    U_, S_, Vt_ = np.linalg.svd(A, full_matrices=False)
    W = U_ @ Vt_
    sv = np.linalg.svd(W, compute_uv=False)
    print(f"   nu={nu}:  singular values of W = {sv.round(6)}  ratio = {sv[0]/sv[2]:.6f}  <- passes the gate by construction")
    print("\n   W (rows = image degrees 0,2,4,6 ; cols = down degrees 1,3,5):")
    img = [0, 2, 4, 6]
    print("        " + "".join(f"{'d='+str(d):>10}" for d in (1, 3, 5)))
    for i, m in enumerate(img):
        print(f"   k={m:<3} " + "".join(f"{W[i,j]:>10.5f}" for j in range(3)))
