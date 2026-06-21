#!/usr/bin/env python3
r"""
toy_4286 — Calculate + STORE the heat-kernel cascade coefficients now that the n=52 / dps=3200
           checkpoint has landed (Casey request). n=52 is the last dimension needed for a_26
           (deg 52, n_need = 2k-2 = 50 dims = n3..n52). Reuses the established toy_671d machinery
           VERBATIM (no reinvention) -- loads all checkpoints n=3..52, runs the cascade extraction
           a_1..a_26, and STORES the FULL a_k(n) polynomials (the existing results_hybrid_3200.json
           keeps only a_k(5)). Verifies a_k(5) against KNOWN_AK5 and the speaking-pair ladder.

OUTPUT: play/toy_671_checkpoint/coefficients_n52_dps3200.json with, per k:
  - poly: full a_k(n) polynomial coefficients (Fraction strings, index = power of n)
  - degree, a_k(5), and for confirmed polys the subleading/leading ratio + speaking-pair flag.
Plus speaking_pairs ladder + KNOWN_AK5 verification. Incremental save after every k.

Speaking-pair ladder (the physics): ratio at level k = p[2k-1]/p[2k]; INTEGER => "speaking pair".
Known ladder: k=5:-2, 6:-3, 10:-9, 11:-11, 15:-21, 16:-24, 20:-38, 21:-42, 25:-60, 26:-65.
Pair 5 (k=25): -60 = -rank*n_C*C_2 = -2*5*6. This run confirms it with n52 in hand.

Elie - 2026-06-20
"""
import importlib.util, os, json, time
from fractions import Fraction

PLAY = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("t671d", os.path.join(PLAY, "toy_671d_nmax52_pair5.py"))
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
import mpmath
mpmath.mp.dps = 3200

N_MIN, N_MAX, TARGET_K = 3, 52, 26
ALL = list(range(N_MIN, N_MAX + 1))
OUT = os.path.join(PLAY, "toy_671_checkpoint", "coefficients_n52_dps3200.json")

def poly_to_strs(p):
    return [f"{c.numerator}/{c.denominator}" for c in p]

def main():
    t0 = time.time()
    print("="*74); print("toy_4286 — compute + store heat-kernel coefficients (n=52, dps=3200)"); print("="*74)

    # load all dims (3200 checkpoint preferred, else 1600 promoted)
    trace = {}
    for n in ALL:
        d = m.load_checkpoint_3200(n) or m.load_checkpoint_1600(n)
        if d: trace[n] = d
    print(f"loaded {len(trace)} dims: {sorted(trace)[:3]} ... {sorted(trace)[-3:]}  ({time.time()-t0:.1f}s)")

    KP = {1: m.A1_POLY}
    allr = {1: {n: m.eval_poly(m.A1_POLY, Fraction(n)) for n in ALL}}
    store = {"meta": {"dps": 3200, "n_range": [N_MIN, N_MAX], "dims_loaded": len(trace),
                      "target_k": TARGET_K, "source": "toy_671d machinery, n52 checkpoint"},
             "coefficients": {}, "speaking_pairs": {}, "known_ak5_check": {}}
    # a_1
    store["coefficients"]["1"] = {"degree": len(m.A1_POLY)-1, "poly": poly_to_strs(m.A1_POLY),
                                  "a_k_5": str(allr[1][5])}

    for k in range(2, TARGET_K + 1):
        tk = time.time(); deg = 2*k
        ct, cs, cc = m.three_theorems(k); maxp = m.MAX_PRIME_BY_LEVEL.get(k, 47)
        clean = {}
        for n in ALL:
            if n not in trace: continue
            ts, fs, vol = trace[n]; kf = {0: Fraction(1)}; ok = True
            for j in range(1, k):
                if j not in allr or n not in allr[j]: ok = False; break
                kf[j] = allr[j][n]
            if not ok: continue
            ak, err, meth = m.extract_coefficient(fs, ts, vol, kf, k)
            fr, fe = m.identify_rational(ak, max_den=500000000000000, tol=1e-8, max_prime=maxp)
            if fr: clean[n] = fr
        n_clean = len(clean)
        poly = m.constrained_polynomial(clean, ct, cs, cc, deg) if n_clean >= deg-2 else None
        if poly:
            for nv in ALL: clean[nv] = m.eval_poly(poly, Fraction(nv))
        allr[k] = clean; KP[k] = poly

        entry = {"degree": deg if poly else None, "n_clean": n_clean, "n_need": deg-2,
                 "poly": poly_to_strs(poly) if poly else None,
                 "a_k_5": str(clean.get(5)) if clean.get(5) is not None else None}
        ratio = None; is_int = None
        if poly and len(poly) > deg:
            r = poly[deg-1]/poly[deg]; is_int = (r.denominator == 1)
            ratio = str(r); entry["ratio_sub_over_lead"] = ratio; entry["ratio_integer"] = is_int
            if is_int:
                store["speaking_pairs"][str(k)] = int(r)
        store["coefficients"][str(k)] = entry
        # KNOWN_AK5 verification
        if k in m.KNOWN_AK5:
            store["known_ak5_check"][str(k)] = (clean.get(5) == m.KNOWN_AK5[k])

        with open(OUT, "w") as f:  # incremental save
            json.dump(store, f, indent=2, default=str)
        chk = "" if k not in m.KNOWN_AK5 else (" a_k(5)OK" if clean.get(5)==m.KNOWN_AK5[k] else " a_k(5)MISMATCH!")
        rs = "" if ratio is None else f" ratio={ratio}{' INT(speaking pair)' if is_int else ''}"
        print(f"  a_{k:>2}: {n_clean:>2}/{len(trace)} clean (need {deg-2}), {'deg '+str(deg) if poly else 'FAILED'}{chk}{rs}  [{time.time()-tk:.0f}s]")
        if poly is None and k >= 17:
            print(f"  extraction failed at k={k} (precision boundary)"); break

    confirmed = [k for k in KP if KP[k] is not None]
    maxk = max(confirmed)
    store["meta"]["max_confirmed_k"] = maxk
    store["meta"]["elapsed_seconds"] = time.time()-t0
    with open(OUT, "w") as f: json.dump(store, f, indent=2, default=str)

    n_known_ok = sum(1 for v in store["known_ak5_check"].values() if v)
    n_known = len(store["known_ak5_check"])
    print("\n" + "="*74)
    print(f"max confirmed k = {maxk}; speaking pairs = {store['speaking_pairs']}")
    print(f"KNOWN_AK5 check: {n_known_ok}/{n_known} match")
    print(f"stored -> {OUT}  ({time.time()-t0:.0f}s total)")
    sp = store["speaking_pairs"]
    p5_ok = sp.get("25") == -60   # pair 5 = -rank*n_C*C_2 = -60
    print(f"SCORE: {'PASS' if (maxk>=26 and n_known_ok==n_known and p5_ok) else 'PARTIAL'} "
          f"(maxk={maxk}, known {n_known_ok}/{n_known}, pair5(k25)={sp.get('25')} {'= -2*5*6 OK' if p5_ok else ''})")
    print("="*74)

if __name__ == "__main__":
    main()
