# TOY 5457 -- PRE-REGISTERED NULL MODEL for alpha. Elie, 2026-08-23.
# Rubric cell: External 3 (SM params) / alpha. Casey's offer, taken.
#
# THE QUESTION, and it is uncomfortable on purpose:
#   T198 (registry, read today): alpha is IDENTIFIED, not Proved. The Wyler volume-ratio route is
#   RETIRED as a derivation (Robertson four-reading trap -- the matching reading was SELECTED to hit
#   137). The honest forward form is alpha^-1 = N_c^3 * n_C + rank = 135 + 2 = 137, but the registry
#   itself records that it "carries THREE provenances from BST integers (135+2, 128+9 = 2^g + N_c^2,
#   and the retired Wyler integral) and is not yet forced blind."
#
#   THREE BST EXPRESSIONS FOR ONE TARGET is the same shape as the gamma / eta-bar / J_CKM rows the
#   team RETIRED this morning under K1809/K1809-B. The rule we applied to them applies here:
#   *** A COMPETITOR COUNT IS NOT A VERDICT UNTIL YOU KNOW HOW MANY COMPETITORS CHANCE SUPPLIES. ***
#
# So: is 137 SPECIAL in the BST integer lattice, or is it what chance supplies at that magnitude?
# This is a COUNT-based instrument (target-independent) rather than a ranking one -- deliberately,
# per the banked rule that counts are target-independent and rankings are not.
#
# ============================ PRE-REGISTRATION ============================
# Fixed BEFORE any count is computed. Nothing below is revised after seeing numbers.
#   ATOMS   : the banked BST integers, EXCLUDING N_max=137 itself (else the test is trivial).
#             Primary set A1 = {rank=2, N_c=3, n_C=5, C_2=6, g=7}.
#             Control set A2 = A1 \ {6}, because C_2 = 6 = 2*3 is NOT independent of the others --
#             including a composite atom inflates reachability. BOTH are reported.
#   OPS     : + , - , * , ^   (exponent guarded: base>=2, 1<=exp<=8, result <= 10^6)
#   DEPTH   : expressions over at most THREE atom-slots, repetition allowed:
#             depth-1  a          depth-2  (a op b)        depth-3  ((a op b) op c)
#   TARGETS : every integer in [100, 175]. Pre-registered as a window bracketing 137 with room
#             on both sides. The FULL window is reported -- no sub-selection.
#   VERDICT RULE, fixed in advance:
#     137 is SPECIAL only if its hit-count is a clear OUTLIER in the window (top of the window and
#     well above the window median). If 137 sits in the bulk of the distribution, then "137 is
#     expressible in BST integers" is NOT evidence -- it is what chance supplies.
# ==========================================================================

import itertools
from fractions import Fraction

A1 = {"rank":2, "N_c":3, "n_C":5, "C_2":6, "g":7}
A2 = {k:v for k,v in A1.items() if k != "C_2"}
LO, HI = 100, 175
TARGET = 137
CAP = 10**6

def apply_ops(x, y):
    out = []
    out.append(("+", x + y))
    out.append(("-", x - y))
    out.append(("-", y - x))
    out.append(("*", x * y))
    if 2 <= y <= 8 and abs(x) >= 2:
        try:
            v = x ** y
            if abs(v) <= CAP: out.append(("^", v))
        except Exception: pass
    if 2 <= x <= 8 and abs(y) >= 2:
        try:
            v = y ** x
            if abs(v) <= CAP: out.append(("^", v))
        except Exception: pass
    return [(o, v) for o, v in out if abs(v) <= CAP]

def reachable(atoms):
    """all values from <=3 atom-slots, with a witness expression for each"""
    names = list(atoms.items())
    vals = {}                      # value -> witness string
    def put(v, s):
        if LO - 400 <= v <= CAP and v not in vals: vals[v] = s
    d1 = {}
    for n, v in names:
        d1.setdefault(v, n); put(v, n)
    d2 = {}
    for (n1,v1),(n2,v2) in itertools.product(names, repeat=2):
        for o, v in apply_ops(v1, v2):
            s = "(%s %s %s)" % (n1, o, n2)
            d2.setdefault(v, s); put(v, s)
    for (v12, s12) in list(d2.items()):
        for n3, v3 in names:
            for o, v in apply_ops(v12, v3):
                put(v, "(%s %s %s)" % (s12, o, n3))
    return vals

def count_in_window(atoms):
    """for each target in the window, how many DISTINCT expressions reach it"""
    names = list(atoms.items())
    counts = {t: 0 for t in range(LO, HI+1)}
    wit = {t: [] for t in range(LO, HI+1)}
    seen = set()
    def record(v, s):
        if LO <= v <= HI and s not in seen:
            seen.add(s); counts[v] += 1
            if len(wit[v]) < 4: wit[v].append(s)
    d2 = {}
    for (n1,v1),(n2,v2) in itertools.product(names, repeat=2):
        for o, v in apply_ops(v1, v2):
            s = "(%s %s %s)" % (n1, o, n2)
            d2[s] = v; record(v, s)
    for s12, v12 in list(d2.items()):
        for n3, v3 in names:
            for o, v in apply_ops(v12, v3):
                record(v, "(%s %s %s)" % (s12, o, n3))
    return counts, wit

BAR = "="*100
print(BAR)
print("TOY 5457 -- PRE-REGISTERED NULL MODEL: is 137 special in the BST integer lattice?")
print("  T198 is IDENTIFIED, not Proved. Wyler route RETIRED 08-11 (target-fit).")
print("  Registry records THREE provenances for one target -- the gamma/eta-bar/J shape retired today.")
print("  Rule applied: a competitor count is not a verdict until you know what chance supplies.")
print(BAR)

for label, atoms in (("A1 = {rank2, N_c3, n_C5, C_2 6, g7}", A1),
                     ("A2 = A1 minus C_2 (6 = 2*3, not independent)", A2)):
    counts, wit = count_in_window(atoms)
    vals = sorted(counts.values())
    n = len(vals)
    median = vals[n//2]
    mean = sum(vals)/n
    mx = max(vals)
    at137 = counts[TARGET]
    rank = sorted(counts, key=lambda t: -counts[t]).index(TARGET) + 1
    ties = sum(1 for t in counts if counts[t] == at137)
    print("\n" + "-"*100)
    print("ATOM SET %s" % label)
    print("-"*100)
    print("  window [%d, %d], %d targets" % (LO, HI, n))
    print("  hits at 137            : %d" % at137)
    print("  window mean / median   : %.2f / %d" % (mean, median))
    print("  window max             : %d   (at target%s %s)"
          % (mx, "s" if sum(1 for t in counts if counts[t]==mx)>1 else "",
             ", ".join(str(t) for t in sorted(counts) if counts[t]==mx)[:60]))
    print("  137's RANK in window   : %d of %d   (%d targets tie at its count)" % (rank, n, ties))
    print("  witnesses at 137       : %s" % ("; ".join(wit[TARGET][:3]) if wit[TARGET] else "NONE"))
    print()
    print("  full window (target:count), all %d reported, no sub-selection:" % n)
    line = ""
    for t in range(LO, HI+1):
        mark = "*" if t == TARGET else " "
        line += "%d:%-3d%s " % (t, counts[t], mark)
        if len(line) > 92:
            print("   " + line); line = ""
    if line: print("   " + line)
    top = sorted(counts, key=lambda t: -counts[t])[:8]
    print("\n  most-reachable targets in window: %s"
          % ", ".join("%d(%d)" % (t, counts[t]) for t in top))
    verdict = "OUTLIER -- 137 is special" if (rank == 1 and at137 > 2*median) else "IN THE BULK -- not special"
    print("\n  *** PRE-REGISTERED VERDICT for %s: %s ***" % (label.split()[0], verdict))

print("\n" + BAR)
print("WHAT THIS DOES AND DOES NOT SAY")
print(BAR)
print(" - It does NOT test whether alpha^-1 = 137 is TRUE. 137 is measured and not in dispute.")
print(" - It tests whether 'BST integers can express 137' is EVIDENCE. Under the standard the team")
print("   applied to gamma/eta-bar/J_CKM this morning, expressibility counts for nothing unless the")
print("   count beats what chance supplies at that magnitude.")
print(" - A FORCED derivation is immune to this test, exactly as V_us = 1/sqrt(20) and the |V_ub|/|V_cb|")
print("   ORDER are immune (#31 Section III.6). The test separates fitting from forcing; it cannot")
print("   touch a forward computation. *** So a bad result here is an argument for finding the")
print("   mechanism, not an argument against alpha. ***")
print(" - N_max = 137 is EXCLUDED from the atoms by pre-registration. If 137 is forced as a")
print("   topological invariant (T186), that forcing is a DIFFERENT claim with a different test,")
print("   and this instrument is silent on it. Do not read this as touching T186.")
print("\n Nothing pushed. CP existence-only.")
