"""Cal S1030 -- facts the K4-0 kill lines lean on, computed before any teammate's run.
Plain Python, exact where possible. Each check prints PASS/FAIL."""
import itertools, math
import numpy as np
ok = 0; n = 0
def check(name, cond):
    global ok, n
    n += 1; ok += bool(cond); print(("PASS " if cond else "FAIL ") + name)

# 1. Heawood / Ringel-Youngs: largest complete graph on orientable genus g = floor((7+sqrt(1+48g))/2)
H = lambda g: math.floor((7 + math.sqrt(1 + 48*g)) / 2)
print("max K_n on genus 0,1,2,3:", [H(g) for g in range(4)])
check("genus 0 caps at K4, genus 1 caps at K7 (same theorem)", H(0) == 4 and H(1) == 7)

# 2. Weyl group orders by brute force (signed permutations; D-type = even sign changes)
def W(rank, typ):
    out = []
    for p in itertools.permutations(range(rank)):
        for s in itertools.product([1, -1], repeat=rank):
            if typ == "D" and np.prod(s) != 1: continue
            M = np.zeros((rank, rank), int)
            for i in range(rank): M[i, p[i]] = s[i]
            out.append(M)
    return out
def has_order3(G): return any(np.array_equal(np.linalg.matrix_power(g, 3), np.eye(len(g), dtype=int)) and not np.array_equal(g, np.eye(len(g), dtype=int)) for g in G)
WB2, WB3, WD3, WD4 = W(2, "B"), W(3, "B"), W(3, "D"), W(4, "D")
print("|W(B2)|,|W(B3)|,|W(D3)|,|W(D4)| =", len(WB2), len(WB3), len(WD3), len(WD4))
check("restricted Weyl group W(B2) has no element of order 3 (so no S3, A4, S4)", len(WB2) == 8 and not has_order3(WB2))
check("complex Weyl W(B3) of so(7) has order 48 = 2*24 (contains S4)", len(WB3) == 48)
check("D_IV^4 (so(6)=D3): W(D3) has order 24 = |S4| (S4 not n=5-specific)", len(WD3) == 24)
check("D_IV^6 (so(8)=D4): |W(D4)| = 192; W(D3)=S4 sits inside it (D3 subset D4)", len(WD4) == 192)
check("120 = |S5| does not divide 48: S5 not in W(B3)", 48 % 120 != 0)

# 3. S4, S5, S6 all embed in SO(5): any search of K = SO(5)xSO(2) for 'a' finite S_n is void
def perm_mat(p):
    M = np.zeros((len(p), len(p))); [M.__setitem__((i, p[i]), 1) for i in range(len(p))]; return M
def sgn(p): return round(np.linalg.det(perm_mat(p)))
def embed(nn):  # standard (nn-1)-dim rep twisted by sign, padded into 5 dims
    Q, _ = np.linalg.qr(np.vstack([np.ones(nn), np.eye(nn)[:-1]]).T); B = Q[:, 1:]  # basis of sum-zero
    imgs = {}
    for p in itertools.permutations(range(nn)):
        R = B.T @ perm_mat(p) @ B
        if (nn - 1) % 2 == 1: R = sgn(p) * R  # odd dim: twist by sign to land in SO
        imgs[p] = R
    return imgs
for nn in (4, 6):  # S4 via 3-dim std*sgn padded; S6 via 5-dim std*sgn
    imgs = embed(nn)
    dets = {round(np.linalg.det(R), 9) for R in imgs.values()}
    faithful = len({tuple(np.round(R, 9).ravel()) for R in imgs.values()}) == math.factorial(nn)
    check(f"S{nn} embeds faithfully in SO({nn-1}) <= SO(5) via std(x)sgn (dets {dets})", dets == {1.0} and faithful)
# S5: 4-dim std rep has det = sgn; pad with sgn in a 5th coordinate
imgs = {}
Q, _ = np.linalg.qr(np.vstack([np.ones(5), np.eye(5)[:-1]]).T); B = Q[:, 1:]
for p in itertools.permutations(range(5)):
    R = np.zeros((5, 5)); R[:4, :4] = B.T @ perm_mat(p) @ B; R[4, 4] = sgn(p); imgs[p] = R
check("S5 embeds faithfully in SO(5) (std + sgn)", {round(np.linalg.det(R), 9) for R in imgs.values()} == {1.0}
      and len({tuple(np.round(R, 9).ravel()) for R in imgs.values()}) == 120)

# 4. Silov boundary (S^4 x S^1)/Z2, deck map (x,t) -> (-x, t+pi): orientation sign = deg(antipodal S^4) * deg(rotation)
deg_antipodal = lambda k: (-1) ** (k + 1)
check("deck map reverses orientation: Silov boundary of D_IV^5 is non-orientable (corpus T2522 agrees)", deg_antipodal(4) * 1 == -1)

# 5. How many K4 invariants equal 3 (the can-fail count for 'a 3 appears')
V = range(4); E = list(itertools.combinations(V, 2))
ham = {frozenset(frozenset(c) for c in zip(cyc, cyc[1:] + cyc[:1])) for cyc in ([0] + list(q) for q in itertools.permutations([1, 2, 3]))}
match = [m for m in itertools.combinations(E, 2) if not set(m[0]) & set(m[1])]
invs = {"cycle rank E-V+1": len(E) - 4 + 1, "Hamiltonian cycles": len(ham), "perfect matchings": len(match),
        "degree": 3, "vertices per face": 3, "faces at a vertex": 3, "|S4/V4| orbit size (axes)": 3, "values (3+1 split)": 3}
print("K4 invariants equal to 3:", invs)
check("at least 7 distinct K4 invariants equal 3 (prior for 'a 3 appears' ~ 1)", sum(v == 3 for v in invs.values()) >= 7)

# 6. Two non-conjugate S3's in S4: vertex stabilizer (not normal) vs quotient S4/V4 (acts on matchings)
S4 = list(itertools.permutations(range(4)))
stab = [p for p in S4 if p[3] == 3]
def act_on_matching(p, m): return frozenset(frozenset(p[v] for v in e) for e in m)
M3 = [frozenset(frozenset(e) for e in m) for m in match]
kernel = [p for p in S4 if all(act_on_matching(p, m) == m for m in M3)]
check("vertex-stabilizer S3 (order 6) acts faithfully on the 3 matchings; kernel of S4->S3 is V4 (order 4)",
      len(stab) == 6 and len(kernel) == 4 and not set(stab) & set(kernel) - {(0, 1, 2, 3)})
print(f"SCORE {ok}/{n}")
