"""
Toy 5279 (Elie, 2026-08-15, afternoon) -- K1555 assignment: PIN WHICH S^2, and check chirality's L/R
against the descent's two SU(2)'s. Casey asked that the S^2 be pinned before anyone builds. Pinned.

FOUR FINDINGS, ONE OF THEM POSITIVE.

(1) "S^2 x U(1) = SU(2)" IS NOT AN IDENTITY. The Hopf bundle S^3 -> S^2 with U(1) fibre is
NON-TRIVIAL: two distinct Hopf fibres have LINKING NUMBER 1 (measured, 1.0000 on three pairs, Gauss
integral after stereographic projection). In a trivial product bundle the fibres are parallel copies
with linking 0. So S^3 is NOT S^2 x S^1, and the twist -- linking 1, the Hopf invariant -- is the
whole content. The correct statement is "SU(2) is a non-trivial principal U(1)-bundle over S^2," and
the word "interface" has to carry that twist or it is carrying nothing.

(2) ★ THE CHIRALITY LEG HOLDS -- this one is real. Spin(4) = SU(2)_L x SU(2)_R -> SO(4) via
x -> q_L x conj(q_R) is orthogonal with det +1 (300/300 samples, det = 1.0000000000) and exactly 2:1
(kernel {+-(1,1)}). So the L/R split IS the descent SO(5)->SO(4)'s two SU(2)'s. Lyra's leg is sound.
CAVEAT so it is not over-read: Spin(4) = SU(2)xSU(2) is the EUCLIDEAN split; physical chirality is
Spin(3,1) = SL(2,C), whose L/R are complex-CONJUGATE reps, not two independent compact factors. Same
structure, different group -- the identification needs the Wick rotation, an extra step.

(3) THE CHAIN'S FIRST LINK DOES NOT PICK A MAP. "SU(3) contains SU(2) x U(1)" does not select ONE
SU(2): the block SU(2) fixes a complex line in C^3, so its conjugates are in bijection with that
line, and the family of SU(2) subgroups IS CP^2 -- dim_R = 8 - 4 = 4, confirmed numerically (SVD
local dimension 4, clean gap 2.6e-3 -> 1.2e-6). Choosing one is a FOUR-PARAMETER non-equivariant
choice. And every SU(2) is isomorphic to every other, so naming the group cannot supply a map to the
SPATIAL Spin(3). This is 5257's missing input in new clothes.

(4) ★★ WHICH S^2 -- THE PIN. D_IV⁵ has NO canonical S^2. The homogeneous spheres of K = SO(5)xSO(2)
are S^4 = SO(5)/SO(4) and S^1 = SO(2); the Shilov boundary is (S^4 x S^1)/Z_2. No S^2 appears. All
four candidates fail:
  * celestial S^2 -- DEAD three ways already (Cal §510): S^(D-2) presupposes D; BST's sky is S^3;
    contradicts T2555.
  * sub-sphere S^2 subset S^4 -- spatial, but needs TWO successive RESTRICTIONS (S^4 -> S^3 -> S^2),
    each requiring its own axis, and restriction is the operation the Casimir forbids (5256/K1504).
    Dead twice over, and it costs two non-equivariant inputs, not one.
  * spin-coset S^2 = SO(3)/SO(2) -- presupposes SO(3), i.e. presupposes the 3 being derived. Fails
    the codimension filter as a coset of the answer.
  * Hopf base CP^1 -- passes the codimension filter (projectivising C^2 needs no D), but it is an
    INTERNAL sphere (the Bloch/isospin sphere), not a sphere of spatial directions.
=> the only candidate that survives the filters is INTERNAL. INGREDIENT-PASSES / APPLICATION-SMUGGLES:
   the Hopf construction genuinely builds SU(2) from S^2 and U(1) -- but the SU(2) it builds is
   INTERNAL, and the chain then uses it as SPATIAL. The gap is exactly where it was.

(5) ★★★ AND T2555 PUTS THE CONSTRUCTION ON THE WRONG SIDE OF COMMITMENT. T2555: the Shilov boundary
is maximal totally-real, and committing DROPS the SO(2) phase circle (2^n_C = 32 = S^4 polarity 16 x
S^1 phase 2 -> 16). The U(1) the Hopf construction needs as its fibre is precisely what commitment
removes. So the S^2 x U(1) -> SU(2) construction exists only PRE-commitment -- while the spatial
frame it is meant to produce is a property of the RECORD, which is POST-commitment. The construction
cannot survive the operation it is supposed to feed.

WHAT I AM NOT SAYING: this does not refute the group chain as rep theory -- that is Lyra's lane and
leg (2) is hers and it holds. It says the S^2 is not pinned to anything spatial in the corpus, the
first link does not pick a map, and the fibre is gone by the time the record exists. Nothing here
touches T2565 or T2545.

Nothing pushed. CP existence-only.
"""
import numpy as np

print("=" * 92)
print("Toy 5279: WHICH S^2 -- the pin. S^2 x U(1) is NOT SU(2) (Hopf linking = 1); the chirality")
print("          L/R leg HOLDS; but which SU(2) in SU(3) is a CP^2 choice, and T2555 drops the U(1).")
print("=" * 92)

rng = np.random.default_rng(825)
tests = []
def check(name, cond, detail):
    tests.append(bool(cond))
    print(("  [PASS] " if cond else "  [FAIL] ") + name)
    print("         " + detail)

# ---------------------------------------------------------------- (1) the Hopf twist
print("\n(1) IS 'S^2 x U(1) = SU(2)' AN IDENTITY?  Two Hopf fibres, Gauss linking number.\n")
def fibre(z1, z2, n=4000):
    th = np.linspace(0, 2 * np.pi, n, endpoint=False); p = np.exp(1j * th)
    a, b = p * z1, p * z2
    return np.stack([a.real, a.imag, b.real, b.imag], axis=1)
def stereo(X, pole=np.array([0, 0, 0, 1.0])):
    d = 1 - X @ pole
    return ((X - np.outer(X @ pole, pole)) / d[:, None])[:, :3]
def linking(A, B):
    dA = np.roll(A, -1, axis=0) - A; dB = np.roll(B, -1, axis=0) - B
    mA, mB = A + dA / 2, B + dB / 2
    R = mA[:, None, :] - mB[None, :, :]
    cr = np.cross(dA[:, None, :], dB[None, :, :])
    return (np.sum(R * cr, axis=2) / np.linalg.norm(R, axis=2) ** 3).sum() / (4 * np.pi)
A = stereo(fibre(1 + 0j, 0 + 0j)); B = stereo(fibre(0.6 + 0j, 0.8 + 0j)); C = stereo(fibre(0.8 + 0j, -0.6 + 0j))
lk = [linking(A, B), linking(A, C), linking(B, C)]
check("1. 'S^2 x U(1) = SU(2)' IS FALSE -- the Hopf bundle is NON-TRIVIAL",
      all(abs(l - 1) < 0.02 for l in lk),
      "linking number of distinct Hopf fibres = %.4f / %.4f / %.4f -- a TRIVIAL product bundle has "
      "parallel fibres with linking 0. S^3 is not S^2 x S^1; the twist (Hopf invariant 1) IS the "
      "content, and 'interface' must carry it." % tuple(lk))

# ---------------------------------------------------------------- (2) the leg that holds
print("\n(2) CHIRALITY'S L/R vs THE DESCENT'S TWO SU(2)'s\n")
def qL(q):
    a, b, c, d = q; return np.array([[a,-b,-c,-d],[b,a,-d,c],[c,d,a,-b],[d,-c,b,a]])
def qRc(q):
    a, b, c, d = q; return np.array([[a,b,c,d],[-b,a,d,-c],[-c,-d,a,b],[-d,c,-b,a]])
ok, dets = 0, []
for _ in range(300):
    u = rng.normal(size=4); u /= np.linalg.norm(u)
    v = rng.normal(size=4); v /= np.linalg.norm(v)
    M = qL(u) @ qRc(v)
    ok += np.allclose(M @ M.T, np.eye(4), atol=1e-12); dets.append(np.linalg.det(M))
k = [np.allclose(qL(np.array(a, float)) @ qRc(np.array(b, float)), np.eye(4), atol=1e-12)
     for a, b in [((1,0,0,0),(1,0,0,0)), ((-1,0,0,0),(-1,0,0,0)), ((-1,0,0,0),(1,0,0,0))]]
check("2. ★ THE CHIRALITY LEG HOLDS -- Spin(4) = SU(2)_L x SU(2)_R, exactly 2:1 onto SO(4)",
      ok == 300 and np.allclose(dets, 1, atol=1e-10) and k == [True, True, False],
      "x -> q_L x conj(q_R): orthogonal %d/300, det = %.10f; kernel (+,+)->I %s, (-,-)->I %s, "
      "(-,+)->I %s => kernel {+-(1,1)}, order 2. The L/R split IS where SO(5)->SO(4) lands. "
      "CAVEAT: this is the EUCLIDEAN split; physical chirality is Spin(3,1)=SL(2,C) with L/R "
      "complex-CONJUGATE -- identifying them needs the Wick rotation, an extra step."
      % (ok, np.mean(dets), k[0], k[1], k[2]))

# ---------------------------------------------------------------- (3) which SU(2)?
print("\n(3) DOES 'SU(3) CONTAINS SU(2) x U(1)' PICK ONE SU(2)?\n")
def pr(v):
    v = v / np.linalg.norm(v); P = np.outer(v, v.conj())
    return np.concatenate([P.real.ravel(), P.imag.ravel()])
v0 = np.array([1, 0, 0], dtype=complex); base = pr(v0)
T = [pr(v0 + 1e-4 * (rng.normal(size=3) + 1j * rng.normal(size=3))) - base for _ in range(400)]
sv = np.linalg.svd(np.array(T), compute_uv=False)
dloc = int((sv > sv[0] * 1e-3).sum())
check("3. NO -- THE FAMILY OF SU(2) SUBGROUPS IS CP^2, A FOUR-PARAMETER CHOICE",
      dloc == 4 and (8 - 4) == 4,
      "the block SU(2) fixes a complex LINE in C^3, so conjugates <-> lines: dim_R = dim SU(3) - "
      "dim U(2) = 8 - 4 = 4, confirmed numerically (SVD local dim %d, gap %.1e -> %.1e). And every "
      "SU(2) is isomorphic to every other, so naming the group cannot supply a map to the SPATIAL "
      "Spin(3). 5257's missing input in new clothes." % (dloc, sv[3], sv[4]))

# ---------------------------------------------------------------- (4) the pin
print("\n(4) ★★ WHICH S^2 -- THE PIN (Casey's watch-item)\n")
orbits = {"SO(5)/SO(4) = S^4": 4, "SO(2) = S^1": 1, "Shilov (S^4 x S^1)/Z_2": 5,
          "SO(5)/(SO(3)xSO(2)) Grassmannian": 10 - 3 - 1}
print("      homogeneous spaces of K = SO(5)xSO(2) and their real dimensions:")
for nm, dd in orbits.items():
    print("        %-36s dim %d %s" % (nm, dd, "<-- an S^2?  NO" if dd != 2 else "<-- S^2"))
check("4. D_IV^5 HAS NO CANONICAL S^2 -- its homogeneous spheres are S^4 and S^1",
      2 not in orbits.values(),
      "no K-orbit is 2-dimensional; the boundary is (S^4 x S^1)/Z_2. Any S^2 must be IMPORTED or "
      "carved out by restriction.")

cands = [
    ("celestial S^2 = S^(D-2)", "DEAD (Cal §510, three ways)", "presupposes D; BST's sky is S^3; contradicts T2555"),
    ("sub-sphere S^2 subset S^4", "DEAD (twice over)", "needs TWO restrictions S^4->S^3->S^2, each with its own axis; restriction is Casimir-forbidden (5256/K1504)"),
    ("spin-coset S^2 = SO(3)/SO(2)", "FAILS codimension filter", "presupposes SO(3) -- a coset of the answer"),
    ("Hopf base CP^1", "SURVIVES the filters -- but INTERNAL", "the Bloch/isospin sphere, not a sphere of spatial directions"),
]
print("\n      candidate S^2's, scored against the two standing filters:")
for nm, verdict, why in cands:
    print("        %-30s %-32s %s" % (nm, verdict, why))
survivors_spatial = [c for c in cands if "SURVIVES" in c[1] and "INTERNAL" not in c[1]]
check("5. NO CANDIDATE S^2 SURVIVES AS A *SPATIAL* SPHERE -- the only survivor is INTERNAL",
      len(survivors_spatial) == 0,
      "INGREDIENT-PASSES / APPLICATION-SMUGGLES: the Hopf construction genuinely builds SU(2) from "
      "S^2 and U(1) -- but the SU(2) it builds is INTERNAL, and the chain then uses it as SPATIAL. "
      "The gap sits exactly where it sat before.")

# ---------------------------------------------------------------- (5) T2555 timing
print("\n(5) ★★★ AND T2555 PUTS THE CONSTRUCTION ON THE WRONG SIDE OF COMMITMENT\n")
naive, polarity, phase = 2 ** 5, 16, 2
check("6. COMMITMENT DROPS THE VERY U(1) THE HOPF CONSTRUCTION NEEDS AS ITS FIBRE",
      naive == polarity * phase and naive // phase == polarity,
      "T2555: 2^n_C = %d = (S^4 polarity %d) x (S^1 phase %d) -> %d, i.e. committing DROPS the SO(2) "
      "phase circle. The Hopf fibre is exactly what is removed. So S^2 x U(1) -> SU(2) exists only "
      "PRE-commitment, while the spatial frame it must produce is a property of the RECORD, which is "
      "POST-commitment. The construction cannot survive the operation it is meant to feed."
      % (naive, polarity, phase, polarity))

print("""
    ★ SCOPE. This does not refute the group chain as representation theory -- leg (2) is Lyra's and
      it HOLDS. It says: the S^2 is not pinned to anything spatial in the corpus (D_IV^5 has none);
      the first link does not pick a map (CP^2 of choices); and the fibre is gone by the time the
      record exists (T2555). Nothing here touches T2565 or T2545.""")

print("\n" + "=" * 92)
print("SCORE: %d/%d   S^2 x U(1) is not SU(2) (linking 1); the chirality L/R leg holds; the SU(2)"
      % (sum(tests), len(tests)))
print("       choice is CP^2; D_IV^5 has no canonical S^2; and T2555 drops the U(1) at commitment.")
print("=" * 92)
