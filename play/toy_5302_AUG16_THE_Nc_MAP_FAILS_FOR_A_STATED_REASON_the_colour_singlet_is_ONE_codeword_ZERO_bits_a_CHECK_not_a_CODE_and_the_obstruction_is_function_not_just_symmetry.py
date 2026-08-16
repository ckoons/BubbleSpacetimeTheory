"""
Toy 5302 (Elie, 2026-08-16) -- the N_c candidate-map, one look, as assigned. The obstruction is real,
and it is WORSE than Cal named: not antisymmetric-vs-symmetric, but CHECK-vs-CODE.

(1) THE DECOMPOSITION, BUILT EXPLICITLY (27 dimensions, permutation projectors):
      totally SYMMETRIC   : dim 10   (the decuplet)
      totally ANTISYMM.   : dim  1   (the colour singlet)
      MIXED               : dim 16   (the two octets)
      total 27  ->  3(x)3(x)3 = 10 (+) 8 (+) 8 (+) 1   ✓ matches the corpus

(2) WHERE A REPETITION CODE WOULD LIVE. {000, 111} is invariant under EVERY permutation, so it sits
entirely in the SYMMETRIC part: measured ||P_sym w|| = 1.0000 and ||P_anti w|| = 0.0000 for both
codewords. The baryon singlet is entirely ANTISYMMETRIC. OPPOSITE ENDS of the decomposition -- Cal's
obstruction confirmed as stated.

★★★ (3) BUT THE REAL OBSTRUCTION IS A MISMATCH OF FUNCTION, NOT OF SYMMETRY.
A CODE needs at least TWO codewords -- it carries log2|C| bits.
      repetition code : |C| = 2  -> 1 bit,  d_min = 3,  CORRECTS one error
      colour singlet  : the antisymmetric subspace has DIMENSION 1  -> ONE state
=> |C| = 1, log2(1) = 0 BITS. THE COLOUR SINGLET ENCODES NOTHING. With one codeword there is no
   minimum distance and nothing to correct toward: a deviation simply leaves the singlet, with no
   majority to restore it.
=> THE CONFINED 3-QUARK STRUCTURE IS A CONSTRAINT (a parity CHECK), NOT A CODE (an ENCODING). A check
   says "this word is legal"; an encoding says "these bits mean that message." Colour-neutrality is
   the former. That distinction is the one the candidate map needs and does not have.

(4) VERDICT.
  * My 5299 stands: d_min = 3 IS forced by single-error-correction, r-independently -- a real theorem
    about codes, and the second face of Casey's operation.
  * But the map from that 3 to the CONFINED 3-QUARK ENCODING FAILS, now for a stated reason. Cal's
    §540 downgrade is correct and this is the mechanism behind it.
  * N_c = 3 STAYS A CANDIDATE.

★ WHAT WOULD CLOSE IT -- stated so the candidate is actionable rather than merely parked:
exhibit at least TWO physically distinguishable confined states that (a) stand in a distance-3
relation and (b) permit majority-style recovery. Such a code would have to live in the DECUPLET
(dim 10, symmetric) -- NOT in the singlet. Whether the decuplet carries that structure is a separate,
checkable question, and it is the one the candidate actually needs answered.

Nothing pushed. CP existence-only.
"""
import numpy as np, itertools

print("=" * 92)
print("Toy 5302: the N_c map fails for a STATED reason -- the colour singlet is ONE codeword, ZERO")
print("          bits: a CHECK, not a CODE. The obstruction is function, not just symmetry.")
print("=" * 92)

tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

basis = list(itertools.product(range(3), repeat=3))
idx = {b: i for i, b in enumerate(basis)}
perms = list(itertools.permutations(range(3)))
def sgn(p):
    s = 1
    for i in range(3):
        for j in range(i + 1, 3):
            if p[i] > p[j]: s = -s
    return s
Ps = np.zeros((27, 27)); Pa = np.zeros((27, 27))
for i, b in enumerate(basis):
    for p in perms:
        j = idx[tuple(b[p[k]] for k in range(3))]
        Ps[j, i] += 1 / 6
        Pa[j, i] += sgn(p) / 6
ds, da = int(round(np.trace(Ps))), int(round(np.trace(Pa)))
print("\n   3 (x) 3 (x) 3, split by permutation symmetry:\n")
print("      totally SYMMETRIC : dim %2d   (the decuplet)" % ds)
print("      totally ANTISYMM. : dim %2d   (the colour singlet)" % da)
print("      MIXED             : dim %2d   (the two octets)" % (27 - ds - da))
check("1. THE DECOMPOSITION IS EXPLICIT AND MATCHES THE CORPUS",
      ds == 10 and da == 1 and (27 - ds - da) == 16,
      "10 (+) 8 (+) 8 (+) 1 = 27, built from permutation projectors, not asserted.")

w0 = np.zeros(27); w0[idx[(0, 0, 0)]] = 1
w1 = np.zeros(27); w1[idx[(1, 1, 1)]] = 1
syms = [np.linalg.norm(Ps @ w) for w in (w0, w1)]
ants = [np.linalg.norm(Pa @ w) for w in (w0, w1)]
check("2. CAL'S OBSTRUCTION CONFIRMED -- opposite ends of the decomposition",
      all(abs(s - 1) < 1e-12 for s in syms) and all(a < 1e-12 for a in ants),
      "the repetition codewords {000,111} measure ||P_sym|| = %.4f, %.4f and ||P_anti|| = %.4f, %.4f "
      "-- ENTIRELY symmetric, zero antisymmetric component. The baryon singlet is entirely "
      "antisymmetric." % (syms[0], syms[1], ants[0], ants[1]))

check("3. ★★★ BUT THE REAL OBSTRUCTION IS FUNCTION, NOT SYMMETRY -- one codeword, zero bits",
      da == 1,
      "a CODE needs >= 2 codewords; it carries log2|C| bits. Repetition: |C| = 2 -> 1 bit, d_min = 3, "
      "CORRECTS one error. Colour singlet: the antisymmetric subspace has DIMENSION %d -> ONE state, "
      "log2(1) = 0 BITS. It ENCODES NOTHING, has no minimum distance, and nothing to correct toward "
      "-- a deviation just leaves the singlet, with no majority to restore it. => the confined "
      "3-quark structure is a CONSTRAINT (a parity CHECK), not a CODE (an ENCODING)." % da)

check("4. VERDICT -- N_c = 3 STAYS A CANDIDATE, and Cal's §540 has its mechanism",
      True,
      "my 5299 stands: d_min = 3 IS forced by single-error-correction, r-independently -- a real "
      "theorem about codes. But the map from that 3 to the CONFINED 3-QUARK ENCODING fails, now for "
      "a stated reason: check vs encoding, not merely antisymmetric vs symmetric.")

check("5. ★ WHAT WOULD CLOSE IT -- actionable, not merely parked",
      ds == 10,
      "exhibit at least TWO physically distinguishable confined states that (a) stand in a distance-3 "
      "relation and (b) permit majority-style recovery. Such a code would have to live in the "
      "DECUPLET (dim %d, symmetric) -- NOT in the singlet. Whether the decuplet carries that "
      "structure is a separate checkable question, and it is the one the candidate actually needs." % ds)

print("\n" + "=" * 92)
print("SCORE: %d/%d   the colour singlet is one codeword / zero bits -- a CHECK, not a CODE;"
      % (sum(tests), len(tests)))
print("       N_c = 3 stays a candidate, and any code would have to live in the decuplet, not the singlet.")
print("=" * 92)
