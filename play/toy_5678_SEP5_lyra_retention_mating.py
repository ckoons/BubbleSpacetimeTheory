"""TEST 6c — M5: SELFING vs OUTCROSSING at MATCHED substrate.
Lyra for Casey, 2026-09-05.  This is the 36-vertex monolith-vs-seam test, in genetics.
Four parental homologs either way.  SELF = two isolated lineages, NO seam.
OUTCROSS = one seam.  Fair: identical genetic material in both arms.
"""
import math, itertools
from collections import deque

def gametes(h0, h1, J):
    """Recombinants of a diploid parent: choose h0 or h1 within each block cut by J."""
    L = len(h0); cuts = [0] + sorted(J) + [L]
    blocks = [(cuts[i], cuts[i+1]) for i in range(len(cuts)-1)]
    out = set()
    for pick in itertools.product([0, 1], repeat=len(blocks)):
        out.add("".join((h0 if pick[b] == 0 else h1)[s:e] for b, (s, e) in enumerate(blocks)))
    return sorted(out)

def zyg_classes(zygotes, J):
    st = sorted({tuple(sorted(z)) for z in zygotes})
    idx = {s: i for i, s in enumerate(st)}; comp = [-1]*len(st); nc = 0
    def move(z, j):
        a, b = z
        return tuple(sorted((a[:j]+b[j:], b[:j]+a[j:])))
    for s0 in range(len(st)):
        if comp[s0] != -1: continue
        dq = deque([s0]); comp[s0] = nc
        while dq:
            x = dq.popleft()
            for j in J:
                t = idx.get(move(st[x], j))
                if t is not None and comp[t] == -1: comp[t] = nc; dq.append(t)
        nc += 1
    sz = [comp.count(k) for k in range(nc)]
    return len(st), sz

R = lambda sz: -sum((s/sum(sz))*math.log2(s/sum(sz)) for s in sz if s)
Ht = lambda sz: sum((s/sum(sz))*math.log2(s) for s in sz if s)

def run(L, hom, Js):
    A0, A1, B0, B1 = hom
    print("\nFOUR parental homologs, identical in both arms: A=(%s,%s)  B=(%s,%s)  L=%d" % (A0, A1, B0, B1, L))
    print("  %-4s | %-34s | %-34s | %s" % ("|J|", "SELF (two lineages, NO seam)", "OUTCROSS (one seam)", "ratio"))
    for J in Js:
        gA = gametes(A0, A1, J); gB = gametes(B0, B1, J)
        selfz = [(g, g2) for g, g2 in itertools.product(gA, gA)] + \
                [(g, g2) for g, g2 in itertools.product(gB, gB)]
        outz  = [(g, h) for g, h in itertools.product(gA, gB)]
        ns, szs = zyg_classes(selfz, J); no, szo = zyg_classes(outz, J)
        rs, ro = R(szs), R(szo)
        print("  %-4d | %5d zyg %4d cls R=%7.4f H=%6.3f | %5d zyg %4d cls R=%7.4f H=%6.3f | %5.2fx"
              % (len(J), ns, len(szs), rs, Ht(szs), no, len(szo), ro, Ht(szo), (ro/rs if rs > 1e-9 else float('inf'))))

if __name__ == "__main__":
    L = 6
    run(L, ("000000", "111111", "010101", "101010"), [[], [3], [2, 4], [1, 3, 5], [1, 2, 3, 4, 5]])
    print("\n--- control: parents B identical to A (no new material at the seam) ---")
    run(L, ("000000", "111111", "000000", "111111"), [[], [3], [2, 4], [1, 3, 5], [1, 2, 3, 4, 5]])
