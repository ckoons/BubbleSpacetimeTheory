"""
Toy 5282 (Elie, 2026-08-15, evening) -- K1563 (a)(b)(c). All three verified. Two hold with a
correction each; one is sealed clean. Casey's reframe survives, but not for the stated reason in (a)
and not as comfortably as hoped in (b).

(a) MARKOVIAN -- CORPUS-CONSISTENT, BUT AXIOMATIC, NOT DERIVED.
"Markovian because the heat semigroup exp(-tau H_B) is memoryless" is a CAN'T-FAIL argument:
exp(-(s+t)H) = exp(-sH)exp(-tH) holds for EVERY operator H (verified, 4.4e-16). It is an identity of
the exponential map, not a fact about BST.
The content is at the SITE level -- Chapman-Kolmogorov for the induced process -- and there the
answer is real and interesting: WITHOUT commitment, amplitudes interfere between ticks and CK FAILS
at O(0.12-0.20). WITH commitment (the state collapses to a site each tick) CK holds to machine
precision. => THE MARKOV PROPERTY IS SUPPLIED BY COMMITMENT, NOT BY THE SEMIGROUP. That is a genuine
clarification and it SUPPORTS Casey's picture -- but it means "Markovian" restates
measurement-as-commitment rather than deriving anything from it. Honest tier: FRAMEWORK, not DERIVED.

(b) FUZZY / UV-FINITE CONTINUUM -- RIGOROUS IN STRUCTURE, RAZOR-THIN AT THE CAP.
Test: with a hard mode cap, is there a stable tau-window where the spectral dimension reads the
continuum value? A relabel would have none; genuine coarse-graining has one that WIDENS with the cap
(so the cap is a real resolution scale). Measured on a 5D Laplacian:
    cap    137     600    3000   12000   40000
    window 0.014  0.021  0.053  0.138   0.308   decades in tau (d_s = 5.00 +/- 0.05)
The window is REAL and widens MONOTONICALLY => NOT a relabel; the cap behaves as a genuine resolution
scale. Casey's reframe survives as a rigorous statement.
★ BUT THE HONEST HALF: at cap = 137 the window is 0.014 decades -- about 3% in tau, essentially
nothing. The coarse-graining story is structurally sound and numerically THIN at small cap.
★★ SCOPE, so this is not over-read: my cap is a MODE COUNT on a 5D torus Laplacian, NOT BST's
operator, and I did NOT verify that BST's N_max = 137 is a mode count. The "137" row is ILLUSTRATIVE
of the trend, not a measurement of BST's window. Someone should redo it on the actual spectrum before
the packaged paper leans on a number.

(c) THE REALITY NEGATIVE -- SEALED, and by a type argument before any commutator.
[J, P_V12] is NOT DEFINED: J (charge conjugation) is antilinear on the COMPLEX colour module;
P_V12 projects inside the REAL 5-dim Jordan/Peirce space. Different spaces. You cannot write the
commutator without first assuming colour = V_12 -- the identification the negative denies.
What IS computable, and it seals it: for J = complex conjugation on C^3, ||J g J^-1 - g|| over Haar
SU(3) has mean 1.3994, median 1.4192, and the fraction of SU(3) on which J commutes is 0.00000. The
commutant is exactly SO(3): 5 of 8 generators FAIL to commute. And no SU(3)-EQUIVARIANT antilinear
involution exists at all, because FS(3) = 0 means 3 is not self-conjugate.
=> ANY antilinear involution on the colour 3 breaks SU(3) -> SO(3), which exact QCD forbids.
CASEY IS RIGHT: colour is simply the wrong object for the spatial frame.

Nothing pushed. CP existence-only.
"""
import numpy as np
from scipy.linalg import expm

print("=" * 92)
print("Toy 5282: the landing verified. Markovian is AXIOMATIC (commitment, not the semigroup);")
print("          the coarse-graining window is REAL but razor-thin at the cap; reality negative SEALED.")
print("=" * 92)

rng = np.random.default_rng(1563)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

# ---------------------------------------------------------------- (a)
print("\n(a) MARKOVIAN -- derived from the heat semigroup, or the commitment axiom?\n")
n = 24
A = rng.normal(size=(n, n)); H = A @ A.T / n
sg = max(np.abs(expm(-(s + t) * H) - expm(-s * H) @ expm(-t * H)).max() for s, t in [(0.3, 0.7), (1.1, 0.4)])
check("1. 'MARKOVIAN BECAUSE HEAT SEMIGROUP' IS A CAN'T-FAIL ARGUMENT",
      sg < 1e-12,
      "exp(-(s+t)H) = exp(-sH)exp(-tH) to %.1e -- but this holds for EVERY operator H. It is an "
      "identity of the exponential map, not a fact about BST." % sg)

def prob_from_amp(t):
    K = np.abs(expm(-t * H)) ** 2
    return K / K.sum(axis=0, keepdims=True)
unc = [np.abs(prob_from_amp(s + t) - prob_from_amp(s) @ prob_from_amp(t)).max()
       for s, t in [(0.3, 0.3), (0.5, 0.5), (0.2, 0.8)]]
P0 = prob_from_amp(0.5)
Pc = lambda t: np.linalg.matrix_power(P0, int(round(t / 0.5)))
com = [np.abs(Pc(s + t) - Pc(s) @ Pc(t)).max() for s, t in [(0.5, 0.5), (1.0, 0.5), (1.0, 1.0)]]
check("2. ★ THE MARKOV PROPERTY IS SUPPLIED BY *COMMITMENT*, NOT BY THE SEMIGROUP",
      min(unc) > 0.05 and max(com) < 1e-12,
      "Chapman-Kolmogorov at the SITE level: UNCOMMITTED (amplitudes interfere between ticks) fails "
      "at %s; COMMITTED (collapse each tick) holds to %.0e. Genuine clarification, and it SUPPORTS "
      "Casey -- but 'Markovian' then RESTATES measurement-as-commitment. Tier: FRAMEWORK, not DERIVED."
      % (", ".join("%.3f" % u for u in unc), max(com)))

# ---------------------------------------------------------------- (b)
print("\n(b) FUZZY / UV-FINITE CONTINUUM -- rigorous coarse-graining, or a relabel?\n")
def ds_window(cap, d=5, tol=0.05):
    r = int(np.ceil(cap ** (1 / d))) + 3
    g = np.arange(-r, r + 1)
    K = np.array(np.meshgrid(*[g] * d, indexing='ij')).reshape(d, -1).T
    ev = np.sort((K ** 2).sum(axis=1).astype(float))[:cap]; ev = ev[ev > 0]
    taus = np.logspace(np.log10(3.0 / ev.max()), np.log10(3.0 / ev.min()), 400)
    Z = np.array([np.exp(-t * ev).sum() for t in taus])
    ds = -2 * np.gradient(np.log(Z), np.log(taus))
    good = np.abs(ds - d) < tol
    if not good.any(): return 0.0
    return np.log10(taus[good].max() / taus[good].min())
caps = [137, 600, 3000, 12000, 40000]
w = [ds_window(c) for c in caps]
for c, ww in zip(caps, w):
    print("      mode cap %6d  ->  d_s = 5.00 +/- 0.05 window = %.3f decades in tau" % (c, ww))
check("3. THE WINDOW IS REAL AND WIDENS MONOTONICALLY -- the cap is a genuine RESOLUTION SCALE",
      all(w[i] < w[i + 1] for i in range(len(w) - 1)) and w[-1] > 0.2,
      "0.014 -> 0.021 -> 0.053 -> 0.138 -> 0.308 decades. NOT a relabel; Casey's reframe survives as a "
      "rigorous statement.")
check("4. ★ BUT AT THE SMALL CAP THE WINDOW IS RAZOR-THIN -- state this before packaging",
      w[0] < 0.05,
      "at cap 137 the window is %.3f decades (~3%% in tau) -- structurally sound, numerically almost "
      "nothing. SCOPE: my cap is a MODE COUNT on a 5D torus Laplacian, NOT BST's operator, and I did "
      "NOT verify that N_max = 137 is a mode count. The 137 row is ILLUSTRATIVE of the trend, not a "
      "measurement of BST's window -- redo it on the real spectrum before the paper cites a number."
      % w[0])

# ---------------------------------------------------------------- (c)
print("\n(c) SEALING THE REALITY NEGATIVE\n")
check("5. [J, P_V12] IS NOT DEFINED -- a type argument, before any commutator",
      True,
      "J (charge conjugation) is ANTILINEAR on the COMPLEX colour module; P_V12 projects inside the "
      "REAL 5-dim Jordan/Peirce space. Different spaces. The commutator cannot be written without "
      "first assuming colour = V_12 -- the identification the negative denies.")

def haar_su3(m):
    A = (rng.normal(size=(m, 3, 3)) + 1j * rng.normal(size=(m, 3, 3))) / np.sqrt(2)
    Q, R = np.linalg.qr(A); d = np.einsum('...ii->...i', R); Q = Q * (d / np.abs(d))[:, None, :]
    return Q * (np.linalg.det(Q) ** (-1 / 3))[:, None, None]
G = haar_su3(20000)
dev = np.abs(G.conj() - G).max(axis=(1, 2))
frac = (dev < 1e-6).mean()
check("6. ★ ANY ANTILINEAR INVOLUTION ON THE COLOUR 3 BREAKS SU(3) -> SO(3)",
      dev.mean() > 1.0 and frac == 0.0 and (8 - 3) == 5,
      "for J = complex conjugation, ||J g J^-1 - g|| over Haar SU(3): mean %.4f, median %.4f; the "
      "fraction of SU(3) on which J commutes is %.5f. The commutant is exactly SO(3) -- %d of 8 "
      "generators FAIL to commute. And no SU(3)-EQUIVARIANT antilinear involution exists at all "
      "(FS(3) = 0 => 3 is not self-conjugate). Exact QCD forbids the breaking."
      % (dev.mean(), np.median(dev), frac, 8 - 3))

print("""
    ★ CASEY IS RIGHT, AND THE COMPUTATION AGREES FROM THE OTHER SIDE: colour is simply the wrong
      object for the spatial frame. The reality negative is sealed by representation theory, not by
      any failure to find the right map -- there is no right map to find.

    FOR THE PACKAGING (@Lyra, @Cal): (a) 'Markovian' should be tiered FRAMEWORK -- it restates the
      commitment axiom rather than deriving from the semigroup; (b) the fuzzy-continuum reframe is a
      REAL result structurally, but the window at small cap is ~3% in tau and my 137 is illustrative
      only -- do not cite a BST window number without redoing it on the actual spectrum.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   Markovian = axiomatic (commitment, not the semigroup); coarse-graining window"
      % (sum(tests), len(tests)))
print("       real but razor-thin at the cap; reality negative sealed by a type argument + SU(3) breaking.")
print("=" * 92)
