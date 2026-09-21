#!/usr/bin/env python3
"""Toy 5768 — T187 m_p/m_e = 6π⁵ through toy 5457's null protocol (K1813). Elie, 2026-09-21.
Prereg: notes/Elie_PREREG_5768_..._2026-09-21.md (sha256 f85dd781…). Cal freezes before --run.
Usage:  python3 toy_5768_*.py --controls     (C2, C3 on the integer window; no target read)
        python3 toy_5768_*.py --run          (C1, the target run, real-valued C3, robustness line)
        python3 toy_5768_*.py --all
Question: is "the BST vocabulary expresses m_p/m_e to 0.002 %" evidence, or what chance supplies? (K1813's question.)
Does NOT test T187's mechanism; a forced computation is immune to this test (#31 III.6)."""
import math, sys, json, bisect, hashlib, os, time
from statistics import median

PREREG_SHA = "f85dd781587c9131edf5dd8fb7073d9325053a5b076ae19a85582556db1afdad"
T = 1836.152673426          # CODATA 2022, u = 3.2e-8 (physics.nist.gov, read 2026-09-21)
TOL = 2.0e-5                # the claim's own 0.002 %
CAP = 1e6
CLAIM = 6 * math.pi ** 5
INTS = [("rank", 2), ("N_c", 3), ("n_C", 5), ("C_2", 6), ("g", 7)]
A1 = INTS + [("π", math.pi)]
A2 = [a for a in A1 if a[0] != "C_2"]
A3 = A1 + [("N_max", 137)]
score, canfail = [], []
def sc(name, ok, cf, detail=""):
    score.append(ok); canfail.append(cf)
    print(f"  [{'HIT' if ok else 'MISS'}] {name}{'' if cf else ' (control)'}  {detail}")

# ---------- full-convention enumerator: ops + - * / ^, all shapes, depth <= 4 ----------
def apply_full(op, x, y):
    if op == "+": v = x + y
    elif op == "-": v = x - y
    elif op == "*": v = x * y
    elif op == "/":
        if abs(y) < 1e-12: return None
        v = x / y
    else:  # "^": exponent integer-valued 2..8, base != 0
        if abs(y - round(y)) > 1e-9 or not (2 <= round(y) <= 8) or abs(x) < 1e-12: return None
        try: v = x ** int(round(y))
        except OverflowError: return None
    if v != v or abs(v) > CAP: return None
    return v

def enumerate_full(atoms, maxd=4):
    level = {1: [(v, n) for n, v in atoms]}
    for n in range(2, maxd + 1):
        out = []
        for k in range(1, n):
            for lv, ls in level[k]:
                for rv, rs in level[n - k]:
                    for op in "+-*/^":
                        v = apply_full(op, lv, rv)
                        if v is not None: out.append((v, f"({ls} {op} {rs})"))
        level[n] = out
    allx = []
    for n in range(1, maxd + 1): allx += [(v, s, n) for v, s in level[n]]
    return allx

class Pool:
    """sorted values with strings; counts within relative TOL of a target, two conventions"""
    def __init__(self, entries, maxd):
        e = [x for x in entries if x[2] <= maxd]
        e.sort(key=lambda t: t[0])
        self.vals = [x[0] for x in e]; self.strs = [x[1] for x in e]
        self.n = len(e)
    def hits(self, t, tol=TOL):
        lo, hi = t * (1 - tol), t * (1 + tol)
        i, j = bisect.bisect_left(self.vals, lo), bisect.bisect_right(self.vals, hi)
        strs = self.strs[i:j]
        nval = len({round(v, 6) for v in self.vals[i:j]})
        return len(strs), nval, strs
    def top_multiplicity_in(self, lo, hi):
        i, j = bisect.bisect_left(self.vals, lo), bisect.bisect_right(self.vals, hi)
        cnt = {}
        for v in self.vals[i:j]:
            k = round(v, 6); cnt[k] = cnt.get(k, 0) + 1
        k = max(cnt, key=cnt.get); return k, cnt[k]

def decoys(n, rlo, rhi):
    return [T * math.exp(math.log(rlo) + i * (math.log(rhi) - math.log(rlo)) / (n - 1)) for i in range(n)]

def rank_report(counts_by_target, target_key):
    c = counts_by_target[target_key]
    higher = sum(1 for k, v in counts_by_target.items() if v > c)
    ties = sum(1 for k, v in counts_by_target.items() if v == c) - 1
    med = median(counts_by_target.values()); mean = sum(counts_by_target.values()) / len(counts_by_target)
    mx = max(counts_by_target.values())
    special = (higher == 0) and (c > 2 * med)
    return dict(count=c, rank=higher + 1, ties=ties, median=med, mean=mean, max=mx, special=special)

# ---------- 5457 mode: faithful port of toy_5457 v1 (left-nested, its guards, its string quirk), extended to depth 4 ----------
def apply_5457(x, y):
    """5457's ops and guards (+ - * ^; exponent 2..8, |base| >= 2, |result| <= CAP). Returns (op, value, swapped):
    swapped=True means the operands enter as (y op x) and the STRING says so — toy_5457 v1 wrote both orders under
    one string (a labelling quirk, visible in K1813's own witness '((N_c ^ n_C) + g) + n_C = 243-...'); fixed here."""
    out = [("+", x + y, False), ("-", x - y, False), ("-", y - x, True), ("*", x * y, False)]
    if 2 <= y <= 8 and abs(x) >= 2: out.append(("^", x ** y, False))
    if 2 <= x <= 8 and abs(y) >= 2: out.append(("^", y ** x, True))
    return [(o, v, sw) for o, v, sw in out if abs(v) <= CAP]

def count_window_5457(atoms, lo, hi, depth):
    names = list(atoms); counts = {t: 0 for t in range(lo, hi + 1)}; wit = {t: [] for t in counts}; seen = set()
    def record(v, s):
        if lo <= v <= hi and v == int(v) and s not in seen:
            seen.add(s); counts[int(v)] += 1
            if len(wit[int(v)]) < 6: wit[int(v)].append(s)
    prev = {}
    for n1, v1 in names:
        for n2, v2 in names:
            for o, v, sw in apply_5457(v1, v2):
                s = f"({n2} {o} {n1})" if sw else f"({n1} {o} {n2})"; prev[s] = v; record(v, s)
    for d in range(3, depth + 1):
        cur = {}
        for s12, v12 in list(prev.items()):
            for n3, v3 in names:
                for o, v, sw in apply_5457(v12, v3):
                    s = f"({n3} {o} {s12})" if sw else f"({s12} {o} {n3})"; cur[s] = v; record(v, s)
        prev = cur
    return counts, wit

def rank_5457(counts, target):
    return sorted(counts, key=lambda t: -counts[t]).index(target) + 1

def verdict_line(tag, r):
    return (f"{tag}: count = {r['count']}  rank {r['rank']} of {r['N']} ({r['ties']} ties)  median {r['median']:.1f}  mean {r['mean']:.2f}  "
            f"max {r['max']}  ⟹ {'SPECIAL' if r['special'] else 'IN THE BULK'}")

def controls_int():
    print("\n" + "=" * 100 + "\nCONTROLS on the integer window [100,175] (no target read)\n" + "=" * 100)
    # C2a: 5457 mode, depth 4, A1 ints — must reproduce K1813: 137 -> 6 hits, 23 higher, 128:20, 125:18
    counts, wit = count_window_5457(INTS, 100, 175, 4)
    r = rank_report(counts, 137); r["N"] = len(counts)
    idx = rank_5457(counts, 137)
    top = sorted(counts, key=lambda t: -counts[t])[:6]
    print(f"  C2a 5457-mode (ints, + - * ^, left-nested, depth 4; clean strings — the amended depth-4 instrument of 08-23 is NOT on disk, only v1 depth 3 was committed): 137 -> {counts[137]} hits; {r['rank']-1} strictly higher; "
          f"5457-index rank {idx}/76; median {r['median']}; top {[(t, counts[t]) for t in top]}")
    print(f"      witnesses at 137: {wit[137][:4]}")
    exact = (counts[137] == 6 and r['rank'] - 1 == 23 and counts[128] == 20 and counts[125] == 18)
    sc("P2a exact reproduction of K1813 (6 / 23 higher / 128:20 / 125:18)", exact, False,
       f"got 6→{counts[137]}, 23→{r['rank']-1}, 128→{counts[128]}, 125→{counts[125]}")
    sc("P2b 137 IN THE BULK in 5457 mode", not (idx == 1 and counts[137] > 2 * r['median']), False,
       f"index rank {idx}, count {counts[137]} vs 2×median {2*r['median']}")
    # C3a: rule can fire — planted 128 in 5457 mode
    r128 = rank_report(counts, 128); i128 = rank_5457(counts, 128)
    sc("P3a rule CAN fire: 128 = 2^g flagged SPECIAL in 5457 mode", i128 == 1 and counts[128] > 2 * r['median'], False,
       f"128: count {counts[128]}, index rank {i128}, 2×median {2*r['median']}")
    # C2c: full conventions (all shapes, ÷, π), exact integer targets — 137 still in the bulk
    pool = Pool(enumerate_full(A1, 4), 4)
    c2 = {}
    for t in range(100, 176):
        lo, hi = t - 1e-9, t + 1e-9
        i, j = bisect.bisect_left(pool.vals, lo), bisect.bisect_right(pool.vals, hi); c2[t] = j - i
    rf = rank_report(c2, 137); rf["N"] = 76
    topf = sorted(c2, key=lambda t: -c2[t])[:6]
    print("  C2c full conventions (A1 with π, + - * / ^, all shapes, depth 4, exact integers): " + verdict_line("137", rf))
    print(f"      top {[(t, c2[t]) for t in topf]}   pool size {pool.n}")
    sc("P2c 137 IN THE BULK under this toy's full conventions", not rf["special"], False,
       f"rank {rf['rank']}, count {rf['count']}, 2×median {2*rf['median']}")
    return dict(c2a=dict(hits137=counts[137], higher=r['rank']-1, idx=idx, c128=counts[128], c125=counts[125], median=r['median']),
                c2c=dict(count=rf['count'], rank=rf['rank'], median=rf['median'], top=[(t, c2[t]) for t in topf]))

def target_run():
    print("\n" + "=" * 100 + "\nTARGET RUN — T = m_p/m_e (CODATA 2022), tolerance 2e-5, 76 decoys on [100/137, 175/137]\n" + "=" * 100)
    print(f"  T = {T}; 6π⁵ = {CLAIM:.9f}; relative miss {(T-CLAIM)/T:.3e}")
    D = decoys(76, 100 / 137, 175 / 137)
    dropped = [d for d in D if abs(d / T - 1) < 10 * TOL]; D = [d for d in D if abs(d / T - 1) >= 10 * TOL]
    print(f"  decoys: {len(D)} (dropped within 10 tol of T: {len(dropped)}); set size {len(D)+1}")
    Dw = decoys(1000, 0.5, 2.0)
    rec = {}
    pools = {}
    for tag, atoms in (("A1", A1), ("A2", A2), ("A3", A3)):
        t0 = time.time(); ent = enumerate_full(atoms, 4); pools[tag] = {4: Pool(ent, 4), 3: Pool(ent, 3)}
        print(f"\n--- {tag} = {{{', '.join(n for n, _ in atoms)}}}  pool: {pools[tag][4].n} expressions (depth ≤4), {pools[tag][3].n} (depth ≤3)  [{time.time()-t0:.1f}s]")
        rec[tag] = {}
        for d in (4, 3):
            P = pools[tag][d]
            ns, nv, strs = P.hits(T)
            cs = {("T", T): ns}; cv = {("T", T): nv}
            for k, x in enumerate(D):
                a, b, _ = P.hits(x); cs[(k, x)] = a; cv[(k, x)] = b
            rs = rank_report(cs, ("T", T)); rs["N"] = len(cs)
            rv = rank_report(cv, ("T", T)); rv["N"] = len(cv)
            hitfrac = sum(1 for k, v in cs.items() if k[0] != "T" and v > 0) / len(D)
            meanhit = sum(v for k, v in cs.items() if k[0] != "T") / len(D)
            # robustness: 1000 decoys on [T/2, 2T]
            cw = [P.hits(x)[0] for x in Dw]
            wfrac = sum(1 for v in cw if v > 0) / len(cw); wmean = sum(cw) / len(cw)
            print(f"  depth ≤{d}:")
            print("    strings: " + verdict_line("T", rs))
            print("    values : " + verdict_line("T", rv))
            print(f"    chance rate: {100*hitfrac:.1f} % of 76 decoys have ≥1 hit; mean {meanhit:.2f} strings per decoy; "
                  f"[T/2,2T] 1000 decoys: {100*wfrac:.1f} % hit, mean {wmean:.2f}")
            print(f"    expressions at T ({ns} strings, {nv} values): " + "; ".join(strs[:24]) + (" …" if ns > 24 else ""))
            if d == 4:
                line = "    full set (decoy value : strings), T marked *: "
                items = sorted(cs.items(), key=lambda kv: kv[0][1])
                print(line); row = ""
                for (k, x), v in items:
                    row += f"{x:.1f}:{v}{'*' if k=='T' else ''}  "
                    if len(row) > 96: print("      " + row); row = ""
                if row: print("      " + row)
            rec[tag][d] = dict(strings=rs, values=rv, hitfrac=hitfrac, meanhit=meanhit, wide_hitfrac=wfrac, wide_mean=wmean,
                               hits_at_T=strs[:60], counts=[(x, cs[(k, x)]) for k, x in [(k, x) for (k, x) in cs if k != "T"]])
    # C1 must-catch
    found = {tag: any(("π ^ n_C" in s and "C_2" in s) or ("π ^ n_C" in s and "rank" in s and "N_c" in s)
                      for s in pools[tag][4].hits(T)[2]) for tag in pools}
    sc("P1 must-catch: C_2·π^n_C (or rank·N_c·π^n_C in A2) found at T within tol in A1, A2, A3", all(found.values()), False, str(found))
    # C3b: planted attractor on the real-valued instrument (A1, depth 4)
    P = pools["A1"][4]; kmax, mult = P.top_multiplicity_in(T * 100 / 137, T * 175 / 137)
    cs = {("T", T): P.hits(T)[0]}
    for k, x in enumerate(D): cs[(k, x)] = P.hits(x)[0]
    cs[("plant", kmax)] = P.hits(kmax)[0]
    rp = rank_report(cs, ("plant", kmax)); rp["N"] = len(cs)
    sc("P3b rule CAN fire on the real-valued instrument: planted top-multiplicity value flagged SPECIAL", rp["special"], False,
       f"planted {kmax} (multiplicity {mult}): " + verdict_line("plant", rp))
    # can-fail predictions
    a14 = rec["A1"][4]; a34 = rec["A3"][4]; a13 = rec["A1"][3]
    sc("P4 distinct-VALUE count at T (A1, depth 4) == 1", a14["values"]["count"] == 1, True, f"values = {a14['values']['count']}")
    sc("P5 T IN THE BULK (A1, depth 4, strings); mean hits/decoy ≥ 1", (not a14["strings"]["special"]) and a14["meanhit"] >= 1, True,
       f"special={a14['strings']['special']}, mean hits/decoy {a14['meanhit']:.2f}")
    sc("P6 T IN THE BULK (A3, depth 4, strings)", not a34["strings"]["special"], True, f"special={a34['strings']['special']}")
    sc("P7 depth ≤3 (A1): ≤10 of 76 decoys hit and T ties for rank 1", a13["hitfrac"] * 76 <= 10 and a13["strings"]["rank"] == 1, True,
       f"decoys with a hit {a13['hitfrac']*76:.0f}/76, T rank {a13['strings']['rank']} ({a13['strings']['ties']} ties)")
    print("\n" + "=" * 100 + "\nVERDICT by K1813's rule (rank 1 AND count > 2×median ⟹ SPECIAL), read at depth 4:")
    for tag in ("A1", "A2", "A3"):
        r = rec[tag][4]["strings"]; v = rec[tag][4]["values"]
        print(f"  {tag}: count within tolerance = {r['count']} strings / {v['count']} values; rank {r['rank']} of {r['N']} ({r['ties']} ties); "
              f"median {r['median']:.0f}; ⟹ {'SPECIAL' if r['special'] else 'IN THE BULK'}")
    print("  depth ≤3 line (data, not the verdict): " + "; ".join(
        f"{tag}: {rec[tag][3]['strings']['count']} str, rank {rec[tag][3]['strings']['rank']} ({rec[tag][3]['strings']['ties']} ties), median {rec[tag][3]['strings']['median']:.0f}"
        for tag in ("A1", "A2", "A3")))
    return rec

if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    pre = [f for f in os.listdir(os.path.join(here, "..", "notes")) if f.startswith("Elie_PREREG_5768_")]
    h = hashlib.sha256(open(os.path.join(here, "..", "notes", pre[0]), "rb").read()).hexdigest() if pre else "MISSING"
    print("=" * 100 + "\nTOY 5768 — m_p/m_e = 6π⁵ through the 5457 null protocol\n" + "=" * 100)
    print(f"  prereg {pre[0] if pre else 'MISSING'}\n  sha256 {h}  {'== frozen' if h == PREREG_SHA else '!! DIFFERS FROM THE FROZEN HASH'}")
    args = sys.argv[1:]
    out = {"prereg_sha": h}
    if "--controls" in args or "--all" in args: out["controls"] = controls_int()
    if "--run" in args or "--all" in args: out["run"] = target_run()
    if not args: print(__doc__)
    if score:
        print(f"\nSCORE {sum(score)}/{len(score)}, of which {sum(1 for s, c in zip(score, canfail) if c and s)}/{sum(canfail)} can-fail hit")
    if "--run" in args or "--all" in args:
        json.dump(out, open(os.path.join(here, ".record_5768.json"), "w"), indent=1, default=str)
        print("  record: play/.record_5768.json")
