"""TEST 6 — meiosis as a move set. Third instance, off the graph-flip family.
Lyra for Casey, 2026-09-05. Predictions hashed f-see-file before launch.
State = p x L binary allele matrix, homologs UNLABELED. Move = crossover at position j
between homologs a,b. Record = linkage phase. Temperature = accessible crossover positions.
"""
import sys, math, itertools
from collections import deque, defaultdict

def canon(rows):
    return tuple(sorted(rows))

def crossover(rows, j, a, b):
    r = list(rows)
    ra, rb = r[a], r[b]
    r[a] = ra[:j] + rb[j:]
    r[b] = rb[:j] + ra[j:]
    return canon(r)

def enumerate_states(p, L, per_locus_ones):
    """All p x L binary matrices with exactly `per_locus_ones` ones in each column, homologs unlabeled."""
    cols = [c for c in itertools.product([0, 1], repeat=p) if sum(c) == per_locus_ones]
    out = set()
    for choice in itertools.product(cols, repeat=L):
        rows = tuple("".join(str(choice[j][i]) for j in range(L)) for i in range(p))
        out.add(canon(rows))
    return sorted(out)

def classes(states, p, L, J, pairs):
    idx = {s: i for i, s in enumerate(states)}
    comp = [-1] * len(states); nc = 0
    for s0 in range(len(states)):
        if comp[s0] != -1: continue
        dq = deque([s0]); comp[s0] = nc
        while dq:
            x = dq.popleft()
            for j in J:
                for (a, b) in pairs:
                    t = idx.get(crossover(states[x], j, a, b))
                    if t is not None and comp[t] == -1:
                        comp[t] = nc; dq.append(t)
        nc += 1
    sizes = [comp.count(k) for k in range(nc)]
    return comp, nc, sizes

def R_bits(sz):
    t = sum(sz)
    return -sum((s/t)*math.log2(s/t) for s in sz if s)
def Hth(sz):
    t = sum(sz)
    return sum((s/t)*math.log2(s) for s in sz if s)

def sweep(p, L, ones, pairs, label):
    st = enumerate_states(p, L, ones)
    print("\n%s  p=%d L=%d ones/locus=%d : %d states (homologs unlabeled)" % (label, p, L, ones, len(st)))
    print("   %-22s %7s %9s %9s   %s" % ("crossover positions J", "classes", "R", "H_th", "note"))
    for m in range(0, L):
        J = list(range(1, m + 1))
        comp, nc, sz = classes(st, p, L, J, pairs)
        pred = (L - 1 - len(J)) if p == 2 else None
        note = ""
        if pred is not None:
            note = "M1 predicts R=%d -> %s" % (pred, "HIT" if abs(R_bits(sz) - max(pred, 0)) < 1e-9 else "MISS")
        print("   |J|=%-2d %-16s %7d %9.4f %9.4f   %s" % (len(J), str(J) if len(J) < 5 else "1..%d" % m, nc, R_bits(sz), Hth(sz), note))

if __name__ == "__main__":
    # p=2 diploid, all loci heterozygous
    sweep(2, 7, 1, [(0, 1)], "DIPLOID, all-het (primate-like: obligate p=2)")
    # p=3 triploid: only ONE pair can synapse (no perfect matching on 3) -- homolog 2 is a univalent
    sweep(3, 5, 1, [(0, 1)], "TRIPLOID, one bivalent + one UNIVALENT (no perfect matching on 3)")
    # p=3 with a trivalent: any pair may synapse (the 'hot' multivalent option)
    sweep(3, 5, 1, [(0, 1), (0, 2), (1, 2)], "TRIPLOID, TRIVALENT (any pair synapses)")
    # p=4 tetraploid: a perfect matching EXISTS -- two disjoint bivalents (plant-like)
    sweep(4, 4, 2, [(0, 1), (2, 3)], "TETRAPLOID, two disjoint bivalents (perfect matching EXISTS)")
    sweep(4, 4, 2, [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)], "TETRAPLOID, QUADRIVALENT (all pairs)")
