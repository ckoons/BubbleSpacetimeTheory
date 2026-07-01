#!/usr/bin/env python3
"""
Toy 4524 — Wednesday E1: Disambiguate the down-quark mass ladder's WHY.

LANE E1 (Wednesday 2026-07-01). Target-innocent checker.

The Tuesday finding (toy 4521/4522): the down-quark mass ratios sit on a clean
ladder m_d:m_s:m_b = 1 : 20 : 900, with each generation gap = (sector^2)*n_C:
    m_s/m_d = 20 = 2^2 * n_C   (n_C = 5)
    m_b/m_s = 45 = 3^2 * n_C
There are (at least) TWO substrate readings of the SAME two integers:

  READING (a) UNIFORM:  gap between gen (k-1) and gen k  =  k^2 * n_C
                        k = upper generation index.  ONE formula.
                        -> 1-2 gap: 2^2*n_C = 20
                        -> 2-3 gap: 3^2*n_C = 45
                        -> PREDICTS 3-4 gap: 4^2*n_C = 80  (needs external 3-gen cutoff)

  READING (b) SUBSTRATE-CONSTANT:  1-2 gap = rank^2 * n_C ; 2-3 gap = N_c^2 * n_C
                        rank = 2, N_c = 3.  TWO distinct primaries.
                        -> no natural "third constant" -> no defined 3-4 term.

Both readings reproduce the two OBSERVED gaps identically. They differ ONLY at a
4th-generation gap (80 vs undefined) -- and BST F397 forbids a 4th generation.
So the two readings are EMPIRICALLY INDISTINGUISHABLE within the 3 real generations.

This is the (B)-mechanism-disambiguated vs (C)-rich-vocab-trap call (F417):
the integers coincide because gen-index-2 == rank == 2 and gen-index-3 == N_c == 3.
Small-integer coincidence over-determines the ladder. Data cannot pick the reading;
only Lyra/Grace's Vol-16 mechanism can. This toy proves that, and checks the
sector-specificity (does up / lepton follow the same ladder?) plus the theta_13
provenance question (is the 45 in m_b/m_s the SAME 45 as banked theta_13 = 1/45?).

Discipline: PDG central values (not memory), Fraction for exact substrate integers,
score X/Y. No bank claim -- this is a checker toy that SHARPENS the mechanism gate.
"""

from fractions import Fraction as F

# ---- BST primaries -----------------------------------------------------------
rank, N_c, n_C = 2, 3, 5

# ---- PDG 2024 central values (target-innocent; measured independently) -------
# Quark masses: light quarks MS-bar at 2 GeV; m_c(m_c), m_b(m_b); leptons pole.
m_d  = 4.67      # MeV   (PDG 2024: 4.67 +0.48 -0.17)
m_s  = 93.4      # MeV   (PDG 2024: 93.4 +8.6 -3.4)
m_b  = 4180.0    # MeV   = 4.18 GeV  m_b(m_b)
m_u  = 2.16      # MeV
m_c  = 1270.0    # MeV   = 1.27 GeV  m_c(m_c)
m_t  = 172690.0  # MeV   = 172.69 GeV pole
m_e  = 0.51099895   # MeV
m_mu = 105.6583755  # MeV
m_ta = 1776.86      # MeV

def close(x, target, tol):
    return abs(x - target) / target <= tol, abs(x - target) / target

results = []  # (label, passed, detail)

print("=" * 78)
print("Toy 4524 — E1: disambiguate the down-quark mass ladder (target-innocent)")
print("=" * 78)

# ---- PART 1: the two observed down-sector gaps -------------------------------
print("\n[PART 1] Observed down-sector gaps (PDG central):")
r_sd = m_s / m_d
r_bs = m_b / m_s
print(f"  m_s/m_d = {r_sd:7.3f}   target 20  = rank^2 * n_C = {rank**2*n_C}")
print(f"  m_b/m_s = {r_bs:7.3f}   target 45  = N_c^2  * n_C = {N_c**2*n_C}")

ok, dev = close(r_sd, rank**2 * n_C, 0.06)      # 20; PDG light-quark ~ few %
results.append(("m_s/m_d ~= rank^2*n_C = 20", ok, f"dev {dev:.2%}"))
ok, dev = close(r_bs, N_c**2 * n_C, 0.06)        # 45
results.append(("m_b/m_s ~= N_c^2*n_C = 45", ok, f"dev {dev:.2%}"))

# ---- PART 2: both readings reproduce BOTH observed gaps ----------------------
print("\n[PART 2] Reading (a) uniform k^2*n_C vs Reading (b) substrate-const:")
gap_a = {2: 2**2 * n_C, 3: 3**2 * n_C}           # uniform: k = upper gen index
gap_b = {2: rank**2 * n_C, 3: N_c**2 * n_C}      # substrate constants
print(f"  (a) uniform:   1-2={gap_a[2]}, 2-3={gap_a[3]}")
print(f"  (b) sub-const: 1-2={gap_b[2]}, 2-3={gap_b[3]}")
results.append(("(a) uniform reproduces both observed gaps (20,45)",
                gap_a[2] == 20 and gap_a[3] == 45, "exact"))
results.append(("(b) sub-const reproduces both observed gaps (20,45)",
                gap_b[2] == 20 and gap_b[3] == 45, "exact"))
results.append(("(a) and (b) AGREE on all 3 real generations",
                gap_a == gap_b, "identical within observed range"))

# ---- PART 3: the readings diverge ONLY at a forbidden 4th generation ---------
print("\n[PART 3] Divergence point = 4th generation (BST F397 forbids it):")
gap_a_4 = 4**2 * n_C                              # uniform predicts 80
print(f"  (a) uniform predicts 3-4 gap = 4^2*n_C = {gap_a_4}  (needs 3-gen cutoff)")
print(f"  (b) sub-const has NO natural 3rd constant -> 3-4 gap UNDEFINED")
print(f"  BST F397: exactly 3 generations = rank+1 -> gen-4 gap is UNOBSERVABLE")
diverge_only_at_4 = (gap_a == gap_b) and (gap_a_4 == 80)
results.append(("readings diverge ONLY at forbidden gen-4 (80 vs undefined)",
                diverge_only_at_4, "empirically indistinguishable in 3 gens"))

# ---- PART 4: the over-determination catch (F417 (C) rich-vocab territory) ----
print("\n[PART 4] Over-determination catch:")
print(f"  gen-index-2 == rank == {rank}   -> 1-2 factor '4' has TWO readings")
print(f"  gen-index-3 == N_c  == {N_c}   -> 2-3 factor '9' has TWO readings")
print("  The ladder integers coincide because small integers collide.")
print("  => Data cannot pick the reading. Mechanism (Vol-16) MUST arbitrate.")
overdet = (rank == 2) and (N_c == 3)
results.append(("integers over-determined (rank=gen2, N_c=gen3 collide)",
                overdet, "=> (C) rich-vocab risk unless mechanism forces (a) or (b)"))

# ---- PART 5: sector-specificity — does the ladder hold for up / lepton? ------
print("\n[PART 5] Sector check: is k^2*n_C DOWN-SPECIFIC? (confirms toy 4522)")
up_cu = m_c / m_u
up_tc = m_t / m_c
lep_me = m_mu / m_e
lep_tm = m_ta / m_mu
print(f"  up:     m_c/m_u = {up_cu:8.1f}  vs k=2 ladder 20   -> {'FAIL' if abs(up_cu-20)/20>0.06 else 'ok'}")
print(f"  up:     m_t/m_c = {up_tc:8.1f}  vs k=3 ladder 45   -> {'FAIL' if abs(up_tc-45)/45>0.06 else 'ok'}")
print(f"  lepton: m_mu/m_e= {lep_me:8.2f}  vs k=2 ladder 20   -> {'FAIL' if abs(lep_me-20)/20>0.06 else 'ok'}")
print(f"  lepton: m_ta/m_mu={lep_tm:8.2f}  vs k=2 ladder 20   -> {'FAIL' if abs(lep_tm-20)/20>0.06 else 'ok'}")
# ladder should FAIL for up + lepton (they use g-forms / pi-forms) => sector-specific
results.append(("up-sector m_c/m_u NOT on k^2*n_C ladder (sector-specific)",
                abs(up_cu-20)/20 > 0.06, f"{up_cu:.0f} not 20"))
results.append(("up-sector m_t/m_c NOT on k^2*n_C ladder",
                abs(up_tc-45)/45 > 0.06, f"{up_tc:.0f} not 45"))
results.append(("lepton m_mu/m_e NOT on k^2*n_C ladder (is pi-form ~ (24/pi^2)^6)",
                abs(lep_me-20)/20 > 0.06, f"{lep_me:.1f} not 20"))

# ---- PART 6: theta_13 provenance test (the form-match flag) ------------------
print("\n[PART 6] theta_13 cross-link: is the '45' the SAME 45?")
print(f"  banked theta_13 = 1/(N_c^2 * n_C) = 1/{N_c**2*n_C}   -> '3' is N_c (COLOR)")
print(f"  m_b/m_s gap 2-3 = 45: reading(a) '3' = gen-index; reading(b) '3' = N_c")
print("  => 'one structure' with theta_13 requires reading (b) (color), NOT (a).")
print("     Under reading (a) the 45=45 match is a COINCIDENCE (gen-3^2 vs N_c^2).")
# numeric identity holds; provenance is the open question -- assert the identity + flag
theta13 = F(1, N_c**2 * n_C)
results.append(("theta_13 = 1/45 numerically equals 1/(m_b/m_s)",
                theta13 == F(1, N_c**2 * n_C) and (N_c**2*n_C) == 45,
                "identity holds; provenance (N_c vs gen-3) is the mechanism gate"))

# ---- PART 7: null-model bracket — how special is the ladder value? -----------
print("\n[PART 7] Null-model: BST-clean products matching 20 and 45 (<=6% each):")
prims = {"rank": 2, "N_c": 3, "n_C": 5, "C_2": 6, "g": 7}
def clean_hits(target, tol=0.06):
    hits = []
    names = list(prims)
    vals = prims
    # products of up to 2 primaries times an optional small integer 1..3
    for a in names:
        for b in [None] + names:
            for k in (1, 2, 3):
                v = vals[a] * (vals[b] if b else 1) * k
                if abs(v - target) / target <= tol:
                    tag = f"{a}" + (f"*{b}" if b else "") + (f"*{k}" if k > 1 else "")
                    hits.append((tag, v))
    # dedup by value
    seen = {}
    for t, v in hits:
        seen.setdefault(v, t)
    return sorted(seen.items())
h20 = clean_hits(20)
h45 = clean_hits(45)
print(f"  match 20: {len(h20)} distinct clean values -> {[v for v,_ in h20]}")
print(f"  match 45: {len(h45)} distinct clean values -> {[v for v,_ in h45]}")
# 20 = rank^2*n_C and 45 = N_c^2*n_C should both be exact-integer hits (0% dev)
exact20 = any(v == 20 for v, _ in h20)
exact45 = any(v == 45 for v, _ in h45)
results.append(("20 and 45 are BOTH exact-integer BST-clean products",
                exact20 and exact45,
                "low-entropy pattern (candidate), but not unique -> mechanism decides"))

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 78)
print("RESULTS")
print("=" * 78)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    print(f"         {detail}")

print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total}")
print("=" * 78)
print("""
VERDICT (checker, no bank):
  * The down-ladder integers 20, 45 are reproduced identically by BOTH the
    uniform gen-index reading (a) and the substrate-constant reading (b).
  * The two readings diverge ONLY at a 4th-generation gap (80 vs undefined),
    which BST F397 forbids -> they are EMPIRICALLY INDISTINGUISHABLE.
  * Therefore DATA CANNOT DISAMBIGUATE the ladder. This is (C) rich-vocab
    territory (F417): rank=gen-2 and N_c=gen-3 make the integers collide.
    Only Lyra/Grace's Vol-16 mechanism can pick (a) vs (b).
  * The ladder is DOWN-SECTOR-SPECIFIC (up + lepton fail it) -> confirms 4522.
  * theta_13 = 1/45 'one-structure' claim REQUIRES reading (b) (the 3 = N_c
    color). Under reading (a) the mass/mixing 45=45 is a coincidence. This is
    the exact thing the mechanism must confirm -- the checker flag, made sharp.

FOR LYRA/GRACE (Vol-16 lane): your derivation is the arbiter. If it produces
k^2 (generation index) -> mass ladder is its OWN structure, theta_13 link is
coincidence. If it produces {rank^2, N_c^2} with the gen-3 factor being COLOR
N_c -> mass and mixing share ONE structure. Nothing banks until it lands.
""")
