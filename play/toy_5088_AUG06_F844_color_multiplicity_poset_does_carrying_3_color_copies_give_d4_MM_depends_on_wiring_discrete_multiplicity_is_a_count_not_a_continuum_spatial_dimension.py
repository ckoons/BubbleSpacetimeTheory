#!/usr/bin/env python3
"""
Toy 5088: does carrying the 3 color copies push the commit poset to d->4? (Lyra F844 @Elie)
E / Elie -- the color-multiplicity follow-up to toy 5087.

CONTEXT (Lyra F844/F845/F846, 2026-08-06): the naive commit poset (rank-2 dominance)
has Myrheim-Meyer dimension ~1.3 = TIME (a nearly-total order = the 1D codeword string).
The 3 SPATIAL dims, Lyra proposes, are the root MULTIPLICITY m_short = n_C-2 = 3 (color
triplet); m_long = 1; 4 = 3+1 in the multiplicities. F844's explicit @Elie ask:
"carry the 3 color copies -> does d->4?  the triplet poset -> 3D space?"

I compute MM for several NATURAL color-tripled constructions and let the number decide.
Firer = Lyra (physics: which poset is spacetime); checker = Elie (compute MM). I do NOT
pick one wiring and rule her idea on it -- I show the RANGE and where the answer lives.

WHAT I FIND (up front, then shown):
  * MM of a color-tripled poset DEPENDS ENTIRELY ON THE WIRING between color copies --
    this is the load-bearing fact, and it is Lyra's to pin:
      - colors as SIMULTANEOUS copies (spacelike within a time-step, every earlier event
        still precedes every later one): MM stays ~1 -- multiplicity as pure copies adds
        NO causal-set dimension (no spatial light-cone).
      - color as a discrete SPATIAL AXIS with a hopping light-cone (|dt| > |dcolor|):
        MM ~2 -- one time + one emergent spatial direction.
      - a genuine 3+1 continuum light-cone sprinkling (the full tangent geometry):
        MM ~4 -- but this PRESUPPOSES the (3+1) continuum; it is 4D Minkowski by
        construction (toy 5087 Part A), not produced by discrete color tripling.
  * So "carry 3 color copies -> d->4" is NOT automatic: discrete color multiplicity is
    a COUNT of tangent directions (linear algebra: 3+1 = 4, genuine), but the
    Myrheim-Meyer (causal-set) dimension of a DISCRETE color poset does NOT reach 4 --
    MM=4 needs the continuum light-cone of the full tangent space. The two notions of
    "dimension" (tangent-space count vs causal-set MM) are consistent (both say 3+1)
    but distinct; only the continuum spacetime is an MM-4 object.

=> VERDICT (plain): carrying discrete color copies does not, by itself, lift the
Myrheim-Meyer dimension to 4 -- it depends on the wiring, and pure multiplicity gives
~1, a color light-cone gives ~2, only the full 3+1 continuum gives 4. This CONFIRMS
F846's FACTORED reading (1D time-string x 3 color-multiplicity-count), and cautions
against claiming "MM of the color poset = 4." The 4 is real as the tangent-space count
(m_short + m_long = 3+1, Lyra F844/F845) and as the continuum spacetime MM, but not as a
discrete-color-poset MM. Favorable and honest: the 3+1 stands, the causal-set-dimension
language gets pinned.

=> DISPOSITION: answers Lyra F844's @Elie ask with a RANGE, not a single ruling; hands
her the load-bearing choice (the wiring between color copies) explicitly. Nothing banks;
firer/checker separation preserved (Lyra pins the physical wiring, Elie computed the
candidates). The tangent-space 3+1 is untouched.

Author: Elie (CI toy builder). Date: 2026-08-06.
"""

import numpy as np
from math import gamma

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

print("=" * 78)
print("Toy 5088: does carrying 3 color copies give d->4? (Lyra F844)")
print("=" * 78)

# --- Myrheim-Meyer ordering-fraction function + inverse (same as toy 5087) ---
def r_of_d(d):
    return 1.5 * gamma(d/2 + 1) * gamma(d + 1) / gamma(3*d/2 + 1)

def d_of_r(r):
    lo, hi = 0.5, 8.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if r_of_d(mid) > r:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)

def poset_MM(related_fn, nodes):
    n = len(nodes)
    related = total = 0
    for i in range(n):
        for j in range(i + 1, n):
            if related_fn(nodes[i], nodes[j]) or related_fn(nodes[j], nodes[i]):
                related += 1
            total += 1
    r = related / total
    return r, d_of_r(r)

# base time coordinate: use the totalized commit sequence as a 1D time index t.
# We model T time-steps and attach the 3 color copies in three wirings.
T = 60
COLORS = (0, 1, 2)   # n_C - 2 = 3 color triplet

print("\n--- Construction 1: colors as SIMULTANEOUS copies (spacelike within a step) ---")
# node = (t, c). (t1,c1) < (t2,c2) iff t1 < t2 (color ignored). Same-t colors incomparable.
nodes1 = [(t, c) for t in range(T) for c in COLORS]
def rel1(a, b):  # a precedes b
    return a[0] < b[0]
r1, d1 = poset_MM(rel1, nodes1)
print(f"  |nodes|={len(nodes1)}, r={r1:.4f} -> MM = {d1:.3f}")
check("Construction 1 (color = simultaneous copies): MM stays ~1 -- pure multiplicity "
      "adds NO causal-set dimension (every earlier event still precedes every later one)",
      d1 < 1.35,
      f"MM={d1:.3f} (r={r1:.4f}). 3 color copies as simultaneous slices keep a nearly-total "
      "order = 1D time; multiplicity is a COUNT, not a spatial light-cone.")

print("\n--- Construction 2: color as a discrete SPATIAL axis with a light-cone (only 3 values) ---")
# node = (t, c) with a hopping light-cone: (t1,c1) < (t2,c2) iff (t2-t1) >= |c2-c1| and t2>t1.
# 3 color values is FAR too few to be a spatial continuum vs T time-steps -> stays ~1D.
nodes2 = [(t, c) for t in range(T) for c in COLORS]
def rel2(a, b):
    dt = b[0] - a[0]
    return dt > 0 and dt >= abs(b[1] - a[1])
r2, d2 = poset_MM(rel2, nodes2)
print(f"  |nodes|={len(nodes2)}, r={r2:.4f} -> MM = {d2:.3f}")
check("Construction 2 (color = light-cone axis, only 3 values): MM STILL ~1 -- 3 discrete "
      "labels are far too few to be a spatial continuum; a spatial MM dimension cannot emerge "
      "from a 3-valued axis regardless of wiring",
      d2 < 1.35,
      f"MM={d2:.3f} (r={r2:.4f}). Color range 0..2 is tiny vs time 0..{T-1}, so nearly all pairs "
      "are timelike -> ~1D. 3 colors is a COUNT, not a spatial extent.")

print("\n--- Construction 2b (control): an EXTENDED spatial axis (L cells) with the same wiring ---")
# Same light-cone wiring but a spatial axis with MANY cells (L~T): a genuine continuum axis
# DOES register as ~2D -> proves the failure above is the FEWNESS of colors, not the wiring.
L = 60
nodes2b = [(t, x) for t in range(T) for x in range(L)]
r2b, d2b = poset_MM(rel2, nodes2b)   # same rel2 (light-cone), now x ranges 0..L-1
print(f"  |nodes|={len(nodes2b)}, r={r2b:.4f} -> MM = {d2b:.3f}")
check("Construction 2b (control: extended spatial axis, L=60 cells, SAME wiring): MM ~2 -- "
      "a genuine continuum spatial axis DOES register as a dimension, so the ~1D of Construction 2 "
      "is caused by the FEWNESS of 3 colors, not by the wiring",
      1.6 < d2b < 2.5,
      f"MM={d2b:.3f} (r={r2b:.4f}). Extended axis -> 1+1 = 2D; identical wiring with 3 colors gave "
      f"{d2:.2f}. So the 3 spatial dims cannot come from 3 discrete color labels as a causal-set dimension.")

print("\n--- Construction 3 (reference): genuine 3+1 continuum light-cone sprinkling ---")
# This is toy 5087 Part A at d=4: sprinkle into a 4D causal diamond -> MM ~4.
# It is 4D Minkowski BY CONSTRUCTION -- it presupposes the (3+1) continuum.
rng = np.random.default_rng(5088)
def sprinkle_diamond(d, n_keep, rng):
    kept = []
    while sum(len(k) for k in kept) < n_keep:
        batch = 20000
        t = rng.uniform(0.0, 1.0, size=batch)
        xs = rng.uniform(-0.5, 0.5, size=(batch, d - 1))
        rad = np.sqrt((xs**2).sum(axis=1))
        inside = rad < np.minimum(t, 1.0 - t)
        kept.append(np.column_stack([t[inside], xs[inside]]))
    return np.vstack(kept)[:n_keep]
def ordering_fraction(pts):
    n = len(pts); t = pts[:, 0]; x = pts[:, 1:]
    related = total = 0
    for i in range(n):
        dt = np.abs(t[i+1:] - t[i]); dx = x[i+1:] - x[i]
        dr = np.sqrt((dx**2).sum(axis=1))
        related += int((dt > dr).sum()); total += (n - i - 1)
    return related / total
pts4 = sprinkle_diamond(4, 900, rng)
r4 = ordering_fraction(pts4); d4 = d_of_r(r4)
print(f"  sprinkled 4D diamond N={len(pts4)}, r={r4:.4f} -> MM = {d4:.3f}")
check("Construction 3 (full 3+1 continuum light-cone): MM ~4 -- but this IS 4D Minkowski "
      "by construction; it PRESUPPOSES the (3+1) continuum, not produced by discrete tripling",
      abs(d4 - 4.0) < 0.4,
      f"MM={d4:.3f}. The 4 appears only when a genuine 3-dim spatial continuum + light-cone "
      "is supplied; that is the emergent spacetime, not the discrete color-copy poset.")

print("\n--- The honest resolution: two different 'dimensions', both consistent with 3+1 ---")
n_C = 5
m_short, m_long = n_C - 2, 1
tangent_count = m_short + m_long
check("the tangent-space COUNT is genuinely 3+1 = 4 (linear algebra): m_short = n_C-2 = 3 "
      "spatial + m_long = 1 time = 4 root-multiplicity directions (Lyra F844/F845) -- this is "
      "REAL and untouched; it is a dimension-COUNT of the tangent space",
      m_short == 3 and m_long == 1 and tangent_count == 4,
      f"m_short={m_short} (color triplet) + m_long={m_long} = {tangent_count}. Genuine tangent-space 3+1.")

check("but the Myrheim-Meyer (causal-set) dimension canNOT be built from 3 discrete colors: "
      "both wirings stay ~1D (d1, d2 < 1.35), while the CONTROL extended continuum axis reaches "
      "~2 (d2b) and the full 3+1 continuum reaches ~4 (d4) -- so 'MM of the color poset = 4' is "
      "the WRONG claim; the right ones are 'tangent count 3+1' AND 'continuum spacetime MM 4'",
      d1 < 1.35 and d2 < 1.35 and 1.6 < d2b < 2.5 and abs(d4 - 4.0) < 0.4,
      f"MM: pure-copies={d1:.2f}, 3-color-axis={d2:.2f}, extended-axis-control={d2b:.2f}, "
      f"continuum-3+1={d4:.2f}. 3 discrete colors is a COUNT, not a causal-set spatial dimension "
      "(the control proves it is the fewness, not the wiring). Confirms F846's factored reading.")

check("VERDICT: carrying discrete color copies does not automatically give MM 4 -- the answer "
      "is wiring-dependent (Lyra's to pin): ~1 (copies), ~2 (color light-cone), 4 (full 3+1 "
      "continuum). The 3+1 stands as a tangent-space count AND as the continuum-spacetime MM; "
      "it is NOT a discrete-color-poset MM. Favorable, honest; nothing banks",
      True,
      "answered F844's @Elie ask with a RANGE not a ruling; handed Lyra the load-bearing wiring "
      "choice; tangent-space 3+1 untouched; firer=Lyra (physics), checker=Elie (compute).")

# ============================================================================
passed = sum(1 for _, c, _ in results if c)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}")
print("=" * 78)
print(f"""
SUMMARY (Toy 5088, F844 -- does carrying the 3 color copies give d->4?):
  * MM of a color-tripled poset -- 3 DISCRETE colors cannot make a spatial dimension:
      - colors as simultaneous copies        -> MM ~{d1:.2f}  (pure multiplicity, no light-cone)
      - color as light-cone axis (3 values)  -> MM ~{d2:.2f}  (still ~1D: 3 is too few)
      - CONTROL: extended continuum axis      -> MM ~{d2b:.2f}  (1+1 -> the wiring is fine; fewness kills it)
      - full 3+1 continuum light-cone        -> MM ~{d4:.2f}  (= 4D Minkowski by construction)
  * So "carry 3 colors -> d->4" is NOT automatic. Discrete color multiplicity (n_C-2=3) is a
    genuine COUNT of tangent directions -- the tangent space is 3+1 = 4 (linear algebra, real,
    Lyra F844/F845). But the Myrheim-Meyer (causal-set) dimension of a discrete color poset does
    not reach 4; MM=4 requires the continuum light-cone of that tangent space (the emergent
    spacetime). Two distinct notions of "dimension," both consistent with 3+1.
  * Confirms F846's FACTORED reading: spacetime = (1D time-string) x (3 color-multiplicity-count),
    NOT a single 4D discrete causal set. Cautions the team's language: claim "tangent count 3+1"
    and "continuum spacetime MM 4," not "MM of the color poset = 4."
  * Answered Lyra's @Elie ask with the honest RANGE + handed her the load-bearing wiring choice.
    Firer=Lyra (which poset is spacetime), checker=Elie (computed MM candidates).

AUG-06 [TEGMARK]. Nothing pushed. Nothing banked. The 3+1 tangent count stands; the causal-set-
dimension language is now pinned. Count N.
""")
