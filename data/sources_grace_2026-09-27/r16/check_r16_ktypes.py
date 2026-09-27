#!/usr/bin/env python3
"""R16 K-type check (Grace, 2026-09-27). Pure ASCII, no dependencies.

Part A: Howe-Tan barriers (2.20) for O(p,q)=O(4,2), light-cone series S^a(X^0),
        unnormalized homogeneity a.  Finds where A+- and A-+ vanish on the
        parity-eps summand and prints the constituents at a = -1, -2, -3.
Part B: Lee-Loke (24) subquotients R_a(r,t) of the U(2,2) Siegel series
        I_2(s,sigma), normalized parameter s; K-types V_lambda =
        tau^lambda (x) tau^(lambda* + sigma 1)  (Lee-Loke 3.3).
        Prints SU(2)xSU(2) spins and the U(1) difference E=(|lam|-|mu|)/2
        (E normalization = INFERENCE) for the constituents at s=-1 and s=0.
"""
P, Q = 4, 2

def barriers(a, m, n, p=P, q=Q):
    return {"++": a - m - n, "+-": a - m + n + q - 2,
            "-+": a + m - n + p - 2, "--": a + m + n + p + q - 4}

print("Part A: O(4,2) light cone, Howe-Tan (2.20)")
for a in (-1, -2, -3):
    eps = "+" if a % 2 == 0 else "-"      # EE case: reducible summand eps=(-1)^a
    zpm = sorted({n - m for m in range(8) for n in range(8)
                  if (m + n - a) % 2 == 0 and barriers(a, m, n)["+-"] == 0})
    zmp = sorted({n - m for m in range(8) for n in range(8)
                  if (m + n - a) % 2 == 0 and barriers(a, m, n)["-+"] == 0})
    print(f"  a={a:2d} (Delta=-a={-a}, KO lambda=-a-2={-a-2}) summand S^(a,{eps}):"
          f" A+- zero on n-m={zpm[:1]}, A-+ zero on n-m={zmp[:1]}")
# minimal rep K-types (KO I Thm 3.6.1): a + p/2 = b + q/2  ->  b = a+1
print("  KO I (3.6.1) minimal-rep K-types for (4,2): H^a(R^4)xH^b(R^2), b=a+1:",
      [(a, a + 1) for a in range(4)], "...")
print("  SO(4) type of H^a(R^4) = (a/2,a/2) [INFERENCE]: every K-type has j1=j2")

print("\nPart B: U(2,2) Siegel series, Lee-Loke (24)")
p = 2
def consts(s, sigma, lam_max=5):
    al = -(s + p - sigma) // 2 if (s + p - sigma) % 2 == 0 else None
    be = -(s + p + sigma) // 2 if (s + p + sigma) % 2 == 0 else None
    if al is None or be is None:
        return None
    cx, cy = max(al, -be - p), min(al, -be - p)
    out = {}
    for r in range(p + 1):
        for t in range(p + 1 - r):
            if not (p - cx + cy <= r + t <= p):
                continue
            lams = []
            for l1 in range(-lam_max, lam_max + 1):
                for l2 in range(-lam_max, l1 + 1):
                    lam = (None, l1, l2, None)   # 1-indexed, lam_0=+inf, lam_3=-inf
                    def L(i):
                        if i <= 0: return 10**9
                        if i >= 3: return -10**9
                        return lam[i]
                    if L(r) >= cx + r >= L(r + 1) and L(p - t) >= cy + p - t >= L(p - t + 1):
                        lams.append((l1, l2))
            out[(r, t)] = lams
    return cx, cy, out

for s, sigma in ((-1, 1), (0, 0)):
    cx, cy, out = consts(s, sigma)
    print(f"  s={s}, sigma={sigma}: c_x={cx}, c_y={cy}")
    for (r, t), lams in sorted(out.items()):
        rows = []
        for (l1, l2) in sorted(lams, key=lambda x: (x[0] + x[1], x))[:6]:
            mu = (sigma - l2, sigma - l1)          # lambda* + sigma*1
            j1 = (l1 - l2) / 2; j2 = (mu[0] - mu[1]) / 2
            E = ((l1 + l2) - (mu[0] + mu[1])) / 2
            rows.append(f"({j1:g},{j2:g};E={E:g})")
        print(f"    R_a({r},{t}): " + " ".join(rows))
print("  => every K-type of I_2(s,sigma) has j1=j2 (Lee-Loke 3.3); a helicity-h ladder")
print("     has lowest K-type (0,|h|) or (|h|,0) (Fernando-Gunaydin 6.26-6.29), so h!=0")
print("     ladders cannot be subquotients of this scalar-character family.")
print("SCORE: R16 K-type check ran; see R16_PINS_draft.md for tiers")
