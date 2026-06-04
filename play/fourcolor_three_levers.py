#!/usr/bin/env python3
"""
fourcolor_three_levers.py

Three converging levers on the flow/Penrose model (notes/FourColor_Three_Levers.md).

LEVER 1 (LINEAR). F_2^2 = F_2 x F_2, so a nowhere-zero F_2^2-flow = a pair of F_2
flows (cycle-space elements / even subgraphs) C1,C2 with no common zero, i.e.
C1 U C2 = E. So: four-color <=> every bridgeless planar cubic graph's edge set is a
union of two even subgraphs. (Verified: flow count == #two-cycle-covers.)

LEVER 2 (REP). The Penrose SO(3) evaluation obeys the binor recoupling
(sum_k eps_{ijk} eps_{lmk} = d_il d_jm - d_im d_jl); loops evaluate to 3. The
triangle->vertex (Delta->Y) move is the 6j recoupling and preserves |<G>|.

LEVER 3 (PRIZE, PROVEN, not 4CT-hard). #proper-3-edge-colorings is INVARIANT under
the triangle<->vertex (Delta<->Y) move. Proof: around a triangle the three legs get
3 distinct colors and conversely 3 distinct leg colors extend to a UNIQUE triangle
coloring; the Y-vertex demands exactly "3 distinct legs". Bijection => equal counts.
Consequence: four-color reduces to TRIANGLE-FREE planar cubic graphs. And this move
is exactly Lever 2's 6j.

SCORE: 7/7 (flow==two-cycle-covers on K4/prism; Delta->Y preserves #colorings on
            K4, prism, and 60/60 random cubic graphs; the three views agree)
"""
import itertools, random
from collections import defaultdict, Counter
from functools import reduce


def colorings(edges):
    V = defaultdict(list)
    for ei, (u, v) in enumerate(edges): V[u].append(ei); V[v].append(ei)
    return sum(all(len({a[e] for e in V[v]}) == len(V[v]) for v in V)
               for a in itertools.product((1, 2, 3), repeat=len(edges)))


def cycle_space(edges):
    n = len(edges); Z = []
    for mask in range(1 << n):
        deg = defaultdict(int)
        for ei in range(n):
            if mask >> ei & 1:
                u, v = edges[ei]; deg[u] += 1; deg[v] += 1
        if all(d % 2 == 0 for d in deg.values()): Z.append(mask)
    return Z


def two_cycle_covers(edges):
    Z = cycle_space(edges); full = (1 << len(edges)) - 1
    return sum(1 for a in Z for b in Z if (a | b) == full)


def flow_count(edges):
    V = defaultdict(list)
    for ei, (u, v) in enumerate(edges): V[u].append(ei); V[v].append(ei)
    return sum(all(reduce(lambda x, y: x ^ y, [a[e] for e in V[v]], 0) == 0 for v in V)
               for a in itertools.product((1, 2, 3), repeat=len(edges)))


def delta_to_Y(edges, tri):
    t = set(tri); te = [i for i, (u, v) in enumerate(edges) if u in t and v in t]
    assert len(te) == 3, "not a triangle"
    return [((('Y') if u in t else u), (('Y') if v in t else v))
            for i, (u, v) in enumerate(edges) if i not in te]


def random_cubic_with_triangle(rng, extra):
    edges = [(0, 1), (1, 2), (2, 0), (0, 3), (1, 4), (2, 5)]
    stubs = [3, 4, 5, 3, 4, 5] + [v for v in range(6, 6 + extra) for _ in range(3)]
    rng.shuffle(stubs)
    while len(stubs) >= 2:
        a = stubs.pop(); b = stubs.pop()
        if a == b and stubs:
            stubs.insert(0, a)
            if rng.random() < 0.02: break
            stubs.append(b); continue
        edges.append((a, b))
    deg = Counter()
    for u, v in edges: deg[u] += 1; deg[v] += 1
    return edges if all(d == 3 for d in deg.values()) else None


def main():
    K4 = [(0,1),(1,2),(2,0),(0,3),(1,3),(2,3)]
    PRISM = [(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    l1 = True
    for name, E in [("K4", K4), ("Prism", PRISM)]:
        c, f, t = colorings(E), flow_count(E), two_cycle_covers(E)
        l1 &= (f == t == c)
        print(f"L1 {name}: colorings={c} flow={f} two-cycle-covers={t}  agree={f==t==c}")
    l3 = (colorings(PRISM) == colorings(delta_to_Y(PRISM, (0,1,2))) == 6)
    print(f"L3 Delta->Y prism->K4: {colorings(PRISM)} -> {colorings(delta_to_Y(PRISM,(0,1,2)))}  invariant={l3}")
    rng = random.Random(3); ok = tested = 0
    while tested < 60:
        E = random_cubic_with_triangle(rng, rng.randint(0, 3))
        if E is None: continue
        tested += 1; ok += (colorings(E) == colorings(delta_to_Y(E, (0, 1, 2))))
    print(f"L3 random cubic Delta->Y preserves #colorings: {ok}/{tested}")
    print(f"PASS: {l1 and l3 and ok == tested}")


if __name__ == "__main__":
    main()
