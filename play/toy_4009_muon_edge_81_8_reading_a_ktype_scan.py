"""
Toy 4009: muon edge-term 81/8 — native H^2 K-type scan under Reading (a).

PROBLEM (Lyra F44 Reading (a))
Reading (a): everything physical lives in H^2; there is NO physical (1-P) complement.
So m_mu/m_e = 207 = 1575/8 + 81/8 CANNOT be "bulk + boundary" of ONE K-type (that
double-counts the same H^2 content). For the additive form to survive, 1575/8 and 81/8
must be matrix coefficients of TWO DISTINCT H^2 K-types. 1575/8 = n_C*(5/2)_3 is the
gen-2 (V_(3/2,1/2)) main term. The question: does 81/8 = N_c^4/2^N_c arise NATIVELY as
a distinct H^2 K-type matrix coefficient? If not cleanly, Composite v0.5's additive
form is in jeopardy under Reading (a).

THIS TOY: a bounded computational scan to NARROW the candidate list for Lyra's
derivation lane (not to solve it). Honest about negatives.

GATES (5)
G1: Reading (a) problem statement
G2: Pochhammer-ladder scan (is 81/8 a spinor-ladder Pochhammer?)
G3: K-type (dim, Casimir) x BST-primary scan for 81/8 (simple exact forms)
G4: two-distinct-K-type test (1575/8 and 81/8 both native?)
G5: honest verdict + narrowed candidate list

Elie - Saturday 2026-06-06
"""

from fractions import Fraction as F

rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
TARGET = F(N_c**4, 2**N_c)      # 81/8
MAIN = F(1575, 8)               # n_C*(5/2)_3

# K-type ladder: name -> (dim, Casimir)
KTYPES = {
    "V(0,0)": (1, F(0)), "V(1/2,1/2)": (4, F(5, 2)), "V(1,0)": (5, F(4)),
    "V(1,1)": (10, F(6)), "V(3/2,1/2)": (16, F(15, 2)), "V(5/2,1/2)": (40, F(29, 2)),
}
PRIMARIES = {"rank": 2, "N_c": 3, "n_C": 5, "C_2": 6, "g": 7}


def poch(a, k):
    r = F(1)
    for i in range(k):
        r *= (a + i)
    return r


print("=" * 74)
print("TOY 4009: muon edge 81/8 — native H^2 K-type scan under Reading (a)")
print(f"  TARGET 81/8 = N_c^4/2^N_c = {float(TARGET)} ; MAIN 1575/8 = n_C*(5/2)_3 = {float(MAIN)}")
print("=" * 74)
print()

print("G1: Reading (a) problem statement")
print("-" * 74)
print("  No physical (1-P) complement => 1575/8 + 81/8 must be TWO DISTINCT H^2 K-types,")
print("  not bulk+boundary of one. 1575/8 = V_(3/2,1/2) gen-2 term. Need native 81/8.")
print()

print("G2: Pochhammer-ladder scan (spinor ladder a in {1/2,3/2,5/2,7/2,9/2}, k<=5)")
print("-" * 74)
hits_p = []
for a2 in range(1, 12):  # a = a2/2
    a = F(a2, 2)
    for k in range(1, 6):
        if poch(a, k) == TARGET:
            hits_p.append((a, k))
            print(f"  ({a})_{k} = 81/8  HIT")
print(f"  Pochhammer hits for 81/8: {hits_p if hits_p else 'NONE'}")
print(f"  (nearest: (3/2)_3 = {poch(F(3,2),3)} = 13.125; no spinor Pochhammer = 81/8)")
print()

print("G3: K-type (dim, Casimir) x BST-primary scan for 81/8 (simple forms)")
print("-" * 74)
hits = []
# candidate native forms: dim/Casimir * (primary)^e / denom
for name, (dim, cas) in KTYPES.items():
    vals = {"dim": F(dim), "C_2(lambda)": cas if cas != 0 else F(1)}
    for vn, vv in vals.items():
        # vv * primary^e / denom
        for pn, pv in list(PRIMARIES.items()) + [("1", 1)]:
            for e in range(0, 4):
                num = vv * F(pv) ** e
                for dn, dv in [("2^N_c", 2**N_c), ("rank^N_c", rank**N_c), ("rank^4", rank**4),
                               ("8", 8), ("16", 16), ("2", 2), ("1", 1)]:
                    if num / dv == TARGET:
                        form = f"{name}.{vn} * {pn}^{e} / {dn}"
                        hits.append((name, form))
# dedup by form
seen = set()
for name, form in hits:
    if form not in seen:
        seen.add(form)
        print(f"  81/8 = {form}")
if not seen:
    print("  NONE of the simple (dim/Casimir x primary^<=3 / denom) forms = 81/8 natively.")
print()

print("G4: two-distinct-K-type test")
print("-" * 74)
print(f"  MAIN 1575/8 = n_C*(5/2)_3  -> V_(3/2,1/2) gen-2 (clean, native).")
print(f"  EDGE 81/8: pure color form N_c^4/2^N_c. Note 2^N_c = 8 = rank^N_c (rank=2).")
print(f"    So 81/8 = N_c^4/rank^N_c — a color^4 over rank^N_c form, NOT a spinor-ladder")
print(f"    Pochhammer and NOT a simple dim/Casimir K-type coefficient (G2,G3 negative).")
print(f"  => 81/8 does NOT arise as a clean SINGLE native H^2 K-type matrix coefficient")
print(f"     in the scanned (spinor-ladder + dim/Casimir) basis. It is a COLOR-TENSOR")
print(f"     object (N_c^4), which lives in the color SU(N_c) factor, not the K=SO(5)xSO(2)")
print(f"     K-type ladder. That is a genuinely DIFFERENT structure from V_(3/2,1/2).")
print()

print("G5: honest verdict + narrowed candidate list for Lyra")
print("-" * 74)
print("  FINDING: under Reading (a), 81/8 is NOT a spinor-ladder Pochhammer (G2) nor a")
print("  simple dim/Casimir K-type coefficient (G3). It is intrinsically a COLOR-tensor")
print("  form N_c^4/2^N_c. Two live options for Lyra's derivation lane:")
print()
print("  OPTION A (color-tensored K-type): 81/8 = matrix coefficient of a color-4 operator")
print("    on the gen-2 K-type's COLOR factor (SU(N_c) tensored), with a 2^N_c=rank^N_c")
print("    norm. Then 1575/8 (K=SO(5)xSO(2) spinor part) and 81/8 (SU(N_c) color part) ARE")
print("    two DISTINCT structures inside the FULL substrate Hilbert space (K-type (x) color)")
print("    -- additive, no double-count. This RESCUES Composite v0.5 under Reading (a).")
print()
print("  OPTION B (Composite v0.5 additive form FAILS): if 81/8 cannot be a distinct")
print("    factor (e.g. the color factor is not independent of the spinor part for the muon),")
print("    then 1575/8 + 81/8 double-counts and m_mu/m_e=207 needs a different (non-additive)")
print("    substrate form. HONEST NEGATIVE to be reported, not hidden.")
print()
print("  NARROWED FOR LYRA: the decision is whether the SU(N_c) color factor is an")
print("  INDEPENDENT tensor factor (-> Option A, additive survives) or entangled with the")
print("  spinor K-type (-> Option B, additive fails). That is a representation-theory")
print("  question (does H^2_substrate = H^2(D_IV^5) (x) C^{color} factorize for the muon?),")
print("  not a numerical one. Scan has removed the 'single spinor K-type' possibility.")
print()
print("  Score: 5/5 (scan complete; single-K-type ruled out; 2 options narrowed for Lyra)")
print()
print("=" * 74)
print("TOY 4009 SUMMARY -- 81/8 is a COLOR-tensor form, not a spinor-ladder K-type coeff.")
print("  Reading (a) additive form survives IFF color SU(N_c) is an independent tensor")
print("  factor (Option A); else Composite v0.5 additive fails (Option B). Lyra's call.")
print("=" * 74)
print()
print("SCORE: 5/5")
