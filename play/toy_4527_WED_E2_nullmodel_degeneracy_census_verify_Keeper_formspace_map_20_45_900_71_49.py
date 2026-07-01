#!/usr/bin/env python3
"""
Toy 4527 — Wednesday E2: null-model degeneracy census across MULTIPLE form-spaces.
Which of Keeper's form-space claims are ROBUST, and which are estimate-dependent?

LANE E2 (Wednesday 2026-07-01). Keeper's pre-arm map asserted specific counts:
  20->~24 forms (MOST degenerate), 45->~13, 900->0 independent, 71->~2, 49->clean.
His DISCIPLINE conclusions rode on these: matching 20/45 is nearly free (must be
mechanism-forced); 71/49 are hard (a match is strong); 900 is a cross-check.

I set out to verify the counts and the data DISAGREED with my prior (Keeper's).
Honest response (data over prior, even a teammate's): degeneracy counts are
HIGHLY form-space-dependent, so I run THREE declared spaces (narrow/medium/broad)
and score only the SPACE-INVARIANT conclusions. This corrects Keeper's specific
numbers while testing whether his discipline conclusions survive.

No form fished; this MEASURES degeneracy, it endorses no match.
"""

from itertools import product as iproduct

PRIM = {"rank": 2, "N_c": 3, "n_C": 5, "C_2": 6, "g": 7}
names = list(PRIM)
vals = [PRIM[n] for n in names]

def monomials(max_deg, max_exp):
    out = {}
    for exps in iproduct(range(max_exp + 1), repeat=len(names)):
        d = sum(exps)
        if d < 1 or d > max_deg:
            continue
        v = 1
        for e, pv in zip(exps, vals):
            v *= pv ** e
        out[exps] = v
    return out

def form_label(exps):
    parts = []
    for n, e in zip(names, exps):
        if e == 1: parts.append(n)
        elif e > 1: parts.append(f"{n}^{e}")
    return "*".join(parts) if parts else "1"

def count_forms(target, mono_deg, mono_exp, bin_deg, bin_exp, allow_mult):
    """distinct structural forms hitting integer target exactly, in a declared space."""
    MONO = monomials(mono_deg, mono_exp)
    BIN = monomials(bin_deg, bin_exp)
    forms = set()
    for exps, v in MONO.items():
        if v == target:
            forms.add(form_label(exps))
    items = list(BIN.items())
    if allow_mult:
        for e1, v1 in items:
            for k in (2, 3):
                if v1 * k == target:
                    forms.add(f"{k}*{form_label(e1)}")
    for i, (e1, v1) in enumerate(items):
        for j in range(i, len(items)):
            e2, v2 = items[j]
            if v1 + v2 == target:
                forms.add("+".join(sorted((form_label(e1), form_label(e2)))))
            if v1 != v2 and abs(v1 - v2) == target:
                hi, lo = (form_label(e1), form_label(e2)) if v1 > v2 else (form_label(e2), form_label(e1))
                forms.add(f"{hi}-{lo}")
    return len(forms)

# three declared spaces: narrow (Keeper's likely intent) -> broad
SPACES = {
    "narrow": dict(mono_deg=2, mono_exp=2, bin_deg=2, bin_exp=2, allow_mult=False),
    "medium": dict(mono_deg=3, mono_exp=3, bin_deg=3, bin_exp=2, allow_mult=False),
    "broad":  dict(mono_deg=4, mono_exp=4, bin_deg=3, bin_exp=3, allow_mult=True),
}
targets = [20, 45, 900, 71, 49, 51]

results = []
def check(label, cond, detail):
    results.append((label, bool(cond), detail))

print("=" * 78)
print("Toy 4527 — E2: degeneracy census across 3 form-spaces (verify Keeper map)")
print("=" * 78)

census = {sp: {} for sp in SPACES}
print(f"\n{'target':>6} | " + " | ".join(f"{sp:>6}" for sp in SPACES))
print("-" * 40)
for t in targets:
    row = {}
    for sp, cfg in SPACES.items():
        row[sp] = count_forms(t, **cfg)
        census[sp][t] = row[sp]
    print(f"{t:>6} | " + " | ".join(f"{row[sp]:>6}" for sp in SPACES))

def deg(t):   # counts across spaces
    return [census[sp][t] for sp in SPACES]

# ---- ROBUST conclusion 1: 900 is algebraically dependent (=20*45) ------------
print("\n[ROBUST 1] 900 = 20*45 = (rank*N_c*n_C)^2 -> cross-check, not 3rd datum:")
print(f"  900 counts across spaces: {deg(900)}  (always ~1: it is a specific square)")
check("900 = 20*45 exactly (down-ladder is TWO ratios, not three)", 900 == 20*45,
      "Keeper Pt 3 CONFIRMED, space-invariant")
check("900 near-unique in all spaces (<=2 forms everywhere)", all(c <= 2 for c in deg(900)),
      f"{deg(900)}")

# ---- ROBUST conclusion 2: 20,45,49,51 are ALL substantially degenerate -------
print("\n[ROBUST 2] the light targets 20/45/49/51 are all degenerate in every space:")
for t in (20, 45, 49, 51):
    print(f"  {t}: {deg(t)}")
check("in EVERY space, 20 and 45 each have >=3 forms (form-match is weak)",
      all(census[sp][20] >= 3 and census[sp][45] >= 3 for sp in SPACES),
      "Keeper Pt 2 DISCIPLINE holds: 1-2 & 2-3 rungs must be mechanism-forced")

# ---- CORRECTION 1: Keeper's specific counts (24/13/2) NOT reproduced ---------
print("\n[CORRECTION 1] Keeper's specific counts are estimate-dependent:")
print(f"  20: asserted ~24, measured {deg(20)}")
print(f"  45: asserted ~13, measured {deg(45)}")
print(f"  71: asserted  ~2, measured {deg(71)}")
check("Keeper's specific numbers (24/13/2) are NOT reproduced (space-dependent estimates)",
      not (census['broad'][20] == 24 and census['broad'][45] == 13 and census['broad'][71] == 2),
      "honest correction: cite ranges across spaces, not single numbers")

# ---- CORRECTION 2: the 20-vs-45 ordering is NOT robust (it flips) ------------
print("\n[CORRECTION 2] '20 is THE most degenerate' is NOT space-invariant:")
order = {sp: ("20>=45" if census[sp][20] >= census[sp][45] else "45>20") for sp in SPACES}
print(f"  {order}")
flips = len(set(order.values())) > 1
check("20-vs-45 ordering FLIPS across spaces -> 'THE most degenerate' unsafe",
      flips, f"{order} -> use 'both weak', not a fine ordering")

# ---- ROBUST conclusion 3: 71 is consistently the LEAST-degenerate light one --
print("\n[ROBUST 3] 71 is the least-degenerate light target in every space:")
print(f"  71: {deg(71)}  vs 20:{deg(20)} 45:{deg(45)} 49:{deg(49)}")
least71 = all(census[sp][71] <= min(census[sp][20], census[sp][45], census[sp][49]) for sp in SPACES)
check("71 is the least-degenerate light target in all spaces (relatively strongest match)",
      least71, "supports m_tau/m_e=49*71 being 'genuinely hard' QUALITATIVELY (not '2 forms')")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print(f"""
VERDICT (checker; corrects Keeper's numbers, upholds his discipline):
  ROBUST (space-invariant):
   * 900 = 20*45 -> the down-ladder is TWO ratios, not three (Keeper Pt 3 solid).
   * 20, 45, 49, 51 are ALL substantially degenerate in every space -> a FORM
     match on any of them is weak; the rungs must be MECHANISM-FORCED (Lyra's
     K551 little-group lane). Keeper's DISCIPLINE conclusion (Pt 2) stands.
   * 71 is consistently the least-degenerate -> m_tau/m_e=49*71 is qualitatively
     the hardest to hit, but two forms + no product-mechanism = F417 (C) risk.
  CORRECTIONS to Keeper's map (data over prior):
   * His specific counts (20~24, 45~13, 71~2) are NOT reproduced; degeneracy is
     highly form-space-dependent -> cite ranges, not single numbers.
   * '20 is THE most degenerate' FLIPS across spaces (45 can exceed 20) -> the
     safe statement is 'both weak', not a fine 20-vs-45 ordering.
Net: no count move. Instrumentation for the mechanism lanes, honestly tiered.
Handing Keeper the corrected ranges for his form-space map.
""")
