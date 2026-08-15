"""
Toy 5283 (Elie, 2026-08-15, evening) -- K1564: the Hardy test, the promotion lever for Part III.
EXHIBITED, not asserted. Two results: the ontology gets STRONGER than asked, and there is a real
gap in the packaging that has to be fixed first.

THE STRUCTURAL KEY (exact): on the Shilov boundary z = e^{i theta} x with x real on S^4, the radial
invariant Q = sum z_j^2 restricts to e^{2 i theta} -- MODULUS 1. Verified to 7.9e-16 over 200000
boundary points. Everything follows from that one line.

(1) THE MAP IS NORM-PRESERVING BLOCKWISE. Because |Q| = 1 on the boundary, the block Q^k H_m
restricts to e^{i(m+2k)theta} h(x), so ||Q^k h||^2_{L2(Shilov)} = ||h||^2_{L2(S^4)} -- INDEPENDENT OF
k. Measured: ratio 1.000000 for every (m,k) with m = 1,2,3 and k = 0..3.

(2) AND IT PRESERVES ORTHOGONALITY. Distinct blocks land on mutually orthogonal boundary functions
(max off-diagonal overlap 0.0097, Monte-Carlo noise) => the restriction is INJECTIVE and
orthogonality-preserving. The isometry is EXHIBITED.

(3) ★ BUT WHICH BULK NORM? THIS IS THE GAP. The corpus runs the commit dynamics on the BERGMAN space
(CLAUDE.md: "rho_commit(tau) = exp(-tau H_B/hbar_BST) on Bergman H^2(D_IV^5)"; Born = Bergman,
T2401). My 5243 result gives the Bergman norm of the block as ||h||^2 / (2^{|lam|}(nu)_lam) with
lam = (m+k, k) -- which DEPENDS ON k, running 5 -> 3.24e7 across just twelve low blocks, a factor of
6.5e6. The boundary norm does not depend on k at all. => THE MAP BERGMAN H^2 -> L^2(SHILOV) IS NOT AN
ISOMETRY. The isometry holds for the HARDY norm, where it is TRUE BY DEFINITION (the Hardy norm IS
the boundary L^2 norm). Hardy and Bergman are DIFFERENT HILBERT SPACES.
=> Part III cannot say "the commit operator's space is isometric to the boundary." It must either
move the dynamics to the Hardy space (a different space from the one T2401 uses) or state the
blockwise rescaling explicitly. Not fatal -- but it must be said, or a referee finds it.

(4) ★★ AND THE ONTOLOGY GETS *STRONGER* THAN ASKED. The map is an isometry INTO, not ONTO: the image
has boundary frequency n = m + 2k >= m >= 0 -- NON-NEGATIVE frequencies only -- while L^2(Shilov)
carries every n of the right parity, including n < 0. So information is conserved (norm-preserving,
injective) but the boundary is strictly bigger.
AND THE MISSING HALF IS EXACTLY THE NEGATIVE FREQUENCIES. That one-sidedness is the POSITIVE-SPECTRUM
condition -- which the corpus already identifies as the ARROW OF TIME ("arrow of time = positivity of
spec(H_B)", CLAUDE.md). So the non-surjectivity is not a leak in the ontology; IT IS THE TIME
ORIENTATION. Casey's "information mapped into matter" is exact as an isometric injection, and the
part that does not map back is the direction of time.

SCOPE: the mode-count fraction (0.325 at cutoff 8) is ILLUSTRATIVE of the trend, sensitive to how the
cutoff is imposed; the exact statements are (a) |Q| = 1 on the boundary, (b) k-independence of the
boundary norm, (c) blockwise orthogonality, (d) n >= 0 on the image. Those four are what Part III can
lean on. Nothing here touches T2555, T2564 or T2565.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5283: HARDY EXHIBITED. Q restricts to a pure phase, so the boundary norm is k-independent;")
print("          the map is an ISOMETRY INTO, and the missing half IS the arrow of time.")
print("          But BERGMAN is the wrong space -- that gap must be stated before packaging.")
print("=" * 92)

rng = np.random.default_rng(2555)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

N = 200000
th = rng.uniform(0, 2 * np.pi, N)
x = rng.normal(size=(N, 5)); x /= np.linalg.norm(x, axis=1)[:, None]
z = np.exp(1j * th)[:, None] * x
Q = (z ** 2).sum(axis=1)

print("\n  Shilov boundary S = (S^4 x S^1)/Z_2: z = e^{i th} x, x real on S^4.")
print("  Bulk harmonic decomposition: Sym^d(C^5) = (+)_k Q^k H_{d-2k},  Q = sum z_j^2.\n")

check("1. THE STRUCTURAL KEY -- Q RESTRICTS TO A PURE PHASE ON THE SHILOV BOUNDARY",
      np.abs(Q - np.exp(2j * th)).max() < 1e-12,
      "max |Q(z) - e^{2i th}| over %d boundary points = %.1e  =>  |Q| = 1 there. Everything below "
      "follows from this one line." % (N, np.abs(Q - np.exp(2j * th)).max()))

harms = {1: lambda v: v[..., 0],
         2: lambda v: v[..., 0] * v[..., 1],
         3: lambda v: v[..., 0] * v[..., 1] * v[..., 2]}
ratios = []
for m in (1, 2, 3):
    base = np.mean(np.abs(harms[m](x)) ** 2)
    for k in (0, 1, 2, 3):
        ratios.append(np.mean(np.abs((Q ** k) * harms[m](z)) ** 2) / base)
check("2. THE BOUNDARY NORM IS INDEPENDENT OF k -- the map is NORM-PRESERVING BLOCKWISE",
      max(abs(r - 1) for r in ratios) < 1e-9,
      "||Q^k h||^2_{L2(Shilov)} / ||h||^2_{L2(S^4)} = 1.000000 for every (m,k), m = 1,2,3, k = 0..3 "
      "(max deviation %.1e). |Q| = 1 on the boundary contributes nothing to the norm."
      % max(abs(r - 1) for r in ratios))

blocks = [(m, k) for m in (1, 2, 3) for k in (0, 1, 2)]
V = np.array([(Q ** k) * harms[m](z) for (m, k) in blocks])
V = V / np.sqrt(np.mean(np.abs(V) ** 2, axis=1))[:, None]
Gm = np.abs(V.conj() @ V.T) / V.shape[1]
off = (Gm - np.diag(np.diag(Gm))).max()
check("3. AND IT PRESERVES ORTHOGONALITY -- the isometry is EXHIBITED, not asserted",
      off < 0.05,
      "distinct blocks land on mutually orthogonal boundary functions: max off-diagonal overlap = "
      "%.4f over %d blocks (Monte-Carlo noise), diagonal = 1. Injective + orthogonality-preserving."
      % (off, len(blocks)))

def poch(a, n):
    r = 1.0
    for i in range(n): r *= (a + i)
    return r
nu, a = 2.5, 3
facs = []
for m in (1, 2, 3):
    for k in (0, 1, 2, 3):
        lam = (m + k, k)
        facs.append(2 ** sum(lam) * poch(nu, lam[0]) * poch(nu - a / 2, lam[1]))
check("4. ★ THE GAP -- BERGMAN H^2 -> L^2(SHILOV) IS *NOT* AN ISOMETRY",
      max(facs) / min(facs) > 1e5,
      "my 5243 result gives the BERGMAN norm as ||h||^2 / (2^{|lam|}(nu)_lam), lam = (m+k,k), which "
      "runs %.0f -> %.3g across twelve low blocks -- a factor of %.2e -- while the boundary norm does "
      "not depend on k at all. The isometry holds for the HARDY norm, where it is true BY DEFINITION. "
      "Hardy and Bergman are DIFFERENT Hilbert spaces, and the corpus runs the commit dynamics on "
      "BERGMAN (T2401, Born=Bergman)." % (min(facs), max(facs), max(facs) / min(facs)))

cut = 8
img = sum(1 for m in range(cut + 1) for k in range(cut + 1) if m + 2 * k <= cut)
tot = sum(1 for m in range(cut + 1) for n in range(-cut, cut + 1) if (n - m) % 2 == 0)
check("5. ★★ ISOMETRY *INTO*, NOT ONTO -- and the missing half IS THE ARROW OF TIME",
      img < tot,
      "Q^k H_m -> e^{i(m+2k)th} h(x), so the image has frequency n = m + 2k >= 0: NON-NEGATIVE "
      "frequencies only, while L^2(Shilov) carries every n of the right parity including n < 0 "
      "(illustrative count at cutoff %d: %d of %d modes reached). That one-sidedness IS the "
      "positive-spectrum condition, which the corpus already calls the ARROW OF TIME. The "
      "non-surjectivity is not a leak in the ontology -- it is the time orientation."
      % (cut, img, tot))

print("""
    ★ WHAT PART III CAN LEAN ON (exact): (a) |Q| = 1 on the Shilov boundary; (b) the boundary norm is
      k-independent; (c) blocks map to orthogonal boundary functions; (d) the image is n >= 0.
      Casey's "information mapped into matter" is EXACT as an isometric injection -- and the part
      that does not map back is the direction of time. The ontology is stronger than the ask.

    ★★ WHAT MUST BE FIXED FIRST (@Lyra, @Cal): Part III cannot say "the commit operator's space is
      isometric to the boundary." It must either move the dynamics to the HARDY space -- a different
      space from the one T2401 uses -- or state the blockwise rescaling 2^{|lam|}(nu)_lam explicitly.
      Not fatal, but a referee finds it in one page.

    SCOPE: the 0.325 mode fraction is illustrative and cutoff-sensitive; the four exact statements
    above are the load-bearing ones. Nothing here touches T2555, T2564 or T2565.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   the isometry is EXHIBITED (|Q|=1 => k-independent boundary norm, orthogonality"
      % (sum(tests), len(tests)))
print("       preserved); it is INTO not ONTO and the missing half is the arrow of time; but the")
print("       BERGMAN space is not the isometric one -- state that before packaging.")
print("=" * 92)
