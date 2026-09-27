#!/usr/bin/env python3
"""
Toy 5834 — the two central characters (χ_t, χ_s) of the cover of SO(4,2): massless ladders vs H² in 4D (Elie, 2026-09-27, round 14).
Prereg 21426ec0. Antecedents: Lyra R13 ("Every covariant H²–4D vertex is fermion-odd") and K1935 Part 2 (the two sets are disjoint).
INVARIANTS, read WEIGHT BY WEIGHT from characters (so centrality is checked, not assumed):
  χ_t = e^{2πiΔ} → on a K-type at clock weight w: (−1)^{2w};   χ_s = spatial 2π rotation → on an SO(4) weight (2mL, 2mR) = (x, y): (−1)^{x+y}.
"""
import glob, io, contextlib
from fractions import Fraction as F
from collections import Counter
from itertools import combinations_with_replacement as cwr
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def su2su2(x2, y2):   # SU(2)xSU(2) irrep (j1,j2) with 2j1 = x2, 2j2 = y2, weights in doubled coords
    return Counter({(a, b): 1 for a in range(-x2, x2 + 1, 2) for b in range(-y2, y2 + 1, 2)})
def ladder(h2, chir, depth):   # helicity h = h2/2; K-types ((m+h2)/2, m/2) [chir=+1] or mirror, at clock weight h+1+m
    G = {}
    for m in range(depth + 1):
        w = F(h2, 2) + 1 + m
        G[w] = su2su2(m + h2, m) if chir > 0 else su2su2(m, m + h2)
    return G
def chis(G):
    out = set()
    for w, C in G.items():
        ct = 1 if (2*w) % 2 == 0 else -1
        for (x, y), v in C.items():
            if v: out.add((ct, 1 if (x + y) % 2 == 0 else -1))
    return out
LAD = {}
for h2 in range(0, 9):
    for chir in ((+1,) if h2 == 0 else (+1, -1)):
        LAD[(h2, chir)] = ladder(h2, chir, 8)
print(f"   ladders: {len(LAD)} (helicity 0..4 in halves, both chiralities; prereg said 18 — the count is 1 + 8·2 = 17, owned)")
sig = {}
ok1 = True
for k, G in LAD.items():
    s = chis(G)
    if len(s) != 1: ok1 = False
    else:
        (ct, cs), = s; sig[k] = (ct, cs)
        if ct != cs: ok1 = False
check("(1) every massless ladder (h = 0..4, both chiralities): (χ_t, χ_s) constant over all K-types and χ_t = χ_s (spin-statistics link)", ok1,
      str(sorted(set(sig.values()))))
# (2) ladder ⊗ ladder, full K-characters (depth 4 per factor): every weight carries the product signs; composites keep χ_t = χ_s
def tensor(G1, G2):
    T = {}
    for w1, C1 in G1.items():
        for w2, C2 in G2.items():
            C = T.setdefault(w1 + w2, Counter())
            for (a, b), u in C1.items():
                for (c, d), v in C2.items(): C[(a + c, b + d)] += u*v
    return T
small = {k: ladder(k[0], k[1], 4) for k in LAD if k[0] <= 4}
ok2 = True; npairs = 0
for (k1, k2) in cwr(sorted(small), 2):
    s = chis(tensor(small[k1], small[k2])); npairs += 1
    prod = (sig[k1][0]*sig[k2][0], sig[k1][1]*sig[k2][1])
    if s != {prod} or prod[0] != prod[1]: ok2 = False
check(f"(2) CONTROL: all {npairs} ladder⊗ladder products (h ≤ 2): every weight carries (χ_t, χ_s) = product of the factors', and χ_t = χ_s", ok2)
# (3) P2 from H²'s restricted character (5798's machinery)
src = open(glob.glob('play/toy_5798_*.py')[0]).read()
ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index("# (a) H_m(R^4)")], ns)
harm_char, restrict_to_so4 = ns['harm_char'], ns['restrict_to_so4']
H2 = {}
for L in range(7):
    C = Counter()
    for l2 in range(L//2 + 1): C.update(restrict_to_so4(harm_char(5, L - 2*l2), 5))
    H2[F(5, 2) + L] = C
sH2 = chis(H2)
check("(3) P2 COMPUTED: every weight of H²(D_IV^5) restricted to SO(4)×SO(2) (depth 6) has (χ_t, χ_s) = (−1, +1)", sH2 == {(-1, 1)}, str(sH2))
# (4) flag: 4D scalar GFF of half-integer Δ (K-types (l/2,l/2) at Δ + ...): (−1, +1)
gff = {F(5, 2) + n: su2su2(l, l) for n in range(4) for l in (n,)}
check("(4) FLAG: a 4D scalar GFF with half-integer Δ (5/2) carries (−1, +1) — the same class as H² in 4D", chis(gff) == {(-1, 1)})
# (5) products of 1..6 ladders
keys = sorted(LAD); classes = set(); n5 = 0
for r in range(1, 7):
    for combo in cwr(keys, r):
        ct = cs = 1
        for k in combo: ct *= sig[k][0]; cs *= sig[k][1]
        classes.add((ct, cs)); n5 += 1
check(f"(5) all {n5} products of 1..6 ladders: (χ_t, χ_s) ∈ {{(+,+), (−,−)}} only — DISJOINT from H²'s (−,+)",
      classes == {(1, 1), (-1, -1)} and (-1, 1) not in classes, str(sorted(classes)))
# (6) drop χ_s: χ_t alone matches H² ⇔ odd number of half-integer-helicity factors (Lyra's rule)
ok6 = True
for r in range(1, 7):
    for combo in cwr(keys, r):
        ct = 1
        for k in combo: ct *= sig[k][0]
        nodd = sum(1 for k in combo if k[0] % 2 == 1)
        if (ct == -1) != (nodd % 2 == 1): ok6 = False
check("(6) DROP χ_s: χ_t alone admits exactly the products with an odd number of half-integer-helicity factors (Lyra's rule reproduced)", ok6)
# (7) sensitivity: a hypothetical half-integer-spin piece of H² in 4D would be (−1, −1) and overlap
check("(7) SENSITIVITY: if P2 failed, a (−1,−1) piece of H² WOULD match products of ladders — the conclusion rests on P2 (computed in (3))",
      (-1, -1) in classes)
# (8) ROUND 15 ADDITION (Cal's two-leg control; K1935 amendment: 'the rule forbids vertices with an odd number of H² legs, not all'):
#     count the legs — products of k H² pieces (each (−1,+1), computed in (3)) with 1..6 ladders
ok8 = True; seen = {}
for k in range(1, 5):
    hk = ((-1)**k, 1)
    allowed = hk in classes
    seen[k] = allowed
    if allowed != (k % 2 == 0): ok8 = False
check("(8) [round 15] LEG COUNT: k H² legs carry ((−1)^k, +1); even k MATCHES a ladder class (pair vertices NOT forbidden), odd k never does",
      ok8, str(seen))
print(f"\nSCORE: {sum(score)}/{len(score)}")
