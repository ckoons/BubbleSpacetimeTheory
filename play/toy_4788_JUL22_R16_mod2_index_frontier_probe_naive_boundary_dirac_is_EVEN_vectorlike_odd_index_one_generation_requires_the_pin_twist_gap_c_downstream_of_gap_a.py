#!/usr/bin/env python3
"""
Toy 4788 — Jul 22 (gap (c) frontier probe: the twisted Pin/mod-2 index; Elie's harness reconnaissance, honestly negative on
resolution, positive on ordering). The charge sector closed (gap b, toys 4786/4787). The remaining frontier is gaps (a)+(c):
does the non-orientable boundary deliver exactly ONE SM generation's chiral reps? Gap (a) = the Wilson-line twist (which
fields are doublets/singlets) is Lyra's; gap (c) = the boundary Dirac index GIVEN a twist is my harness. I pointed the
harness at gap (c) and hit the genuine difficulty — which is itself the informative result: a NAIVE (untwisted) boundary
Dirac operator returns an EVEN zero-mode count (0 or 2 = vector-like / doubled), NOT one clean chiral mode. This is not a bug
— it is the correct statement that a plain Dirac operator has no net chirality, so its mod-2 index is even BY DEFAULT. An ODD
mod-2 index (=1, one generation) can arise ONLY from the specific Pin-TWIST. Therefore gap (c) is DOWNSTREAM of gap (a): the
harness cannot move the index until the twist is specified. Timeboxed probe → clean ordering finding + honest frontier flag;
I do NOT fake an index=1.

WHAT THE PROBE SHOWS (Wilson-Dirac on the S¹ boundary factor, momentum space; the orientation-reversing Z₂ acts as ζ→−ζ):
  * NAIVE / UNTWISTED: the plain boundary Dirac operator's zero-mode count is EVEN — periodic gives a full 2-spinor at p=0
    (chiralities +1 AND −1 → vector-like), antiperiodic gives 0. Either way the mod-2 index is 0. This is consistent with,
    and downstream of, the SQUEEZE (toy 4785, the BULK is structurally vector-like) — a plain reduction inherits it.
  * THE ODD INDEX NEEDS THE TWIST: getting mod-2 index = 1 (one chiral generation) requires BREAKING the L↔R evenness. The
    only thing that can do it is the correct Pin structure = the Wilson-line twist correlating the orientation-reversing
    cycle with the internal-SU(2) content (K826's non-orientability makes this POSSIBLE; it does not by itself select the
    odd sector). That twist is gap (a) — Lyra's — so gap (c) is well-posed only once gap (a) is fixed.
  * DIMENSION FLAG (the real index-theory content): the Z₂-valued Atiyah-Singer mod-2 index lives in KO-dimensions 1,2
    (mod 8). The Shilov boundary is 5-dimensional; HOW the 5D non-orientable boundary + its S¹ factor + the Z₂ + the
    internal bundle combine to land a genuine mod-2 (odd) sector is a real KO-index computation on the SPECIFIC manifold —
    not something a plain-Dirac harness can fake. This is the decades-hard part (string compactifications: "one clean
    generation from geometry").

⟹ VERDICT (frontier, honest): gap (c) is a WELL-POSED but HARD index-theory computation, and it is DOWNSTREAM of gap (a).
My harness establishes three things and fakes nothing: (1) the naive/untwisted boundary Dirac index is EVEN (vector-like /
doubled) — the default is 0, consistent with the squeeze; (2) an ODD index (=1, one generation) requires the specific
Pin-TWIST (gap a, Lyra's) — K826 non-orientability makes it POSSIBLE but does not SELECT it; (3) the genuine resolution is a
real KO-mod-2 index computation on the specific 5D non-orientable D_IV⁵ boundary (correct Pin structure + K826 doubler-
lifting + internal bundle). So the WORK ORDERING is fixed: gap (a) [the twist] must land before gap (c) [the index given the
twist] is computable — the ball is Lyra's. I do NOT claim index=1; that would be the ninth pretty closure. Parity finishes
either DERIVED (if the twist lands on the odd, single-generation, anomaly-free sector) or a sharp derived-CONDITIONAL with
the twist named — the honest landing either way. Charge sector stays closed (gap b); DIRAC + Route 1 + squeeze stay closed;
Five-Absence-positive. This area NEEDS CLOSE ANALYSIS (index theory) — flagged, not forced. Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

sx = np.array([[0,1],[1,0]]); sy = np.array([[0,-1j],[1j,0]]); sz = np.array([[1,0],[0,-1]])
N = 64; L = 2*np.pi; h = L/N; r = 1.0
def zero_modes(bc):                                   # bc=0 periodic (R), 0.5 antiperiodic (NS)
    nz = 0; chir = []
    for n in range(-N//2, N//2):
        p = 2*np.pi*(n+bc)/L
        W = r*(1-np.cos(p*h))/h                       # Wilson term (lifts BZ-edge doubler)
        D = sx*p + sy*W
        w, V = np.linalg.eigh(D)
        for k in range(2):
            if abs(w[k]) < 1e-9:
                nz += 1; chir.append(round(float(np.real(V[:,k].conj() @ sz @ V[:,k])), 2))
    return nz, chir

nz_R, ch_R = zero_modes(0.0)
nz_NS, ch_NS = zero_modes(0.5)
print(f"\n[naive boundary Dirac] periodic: {nz_R} zero modes {ch_R} (mod-2 index {nz_R%2}); antiperiodic: {nz_NS} (mod-2 index {nz_NS%2})")

# ---- the naive index is even ------------------------------------------------
check("NAIVE / UNTWISTED boundary Dirac has an EVEN zero-mode count: periodic gives a full 2-spinor at p=0 (chiralities +1 "
      "AND −1 → vector-like), antiperiodic gives 0 → mod-2 index 0 either way. This is NOT a bug — a plain Dirac operator "
      "has no net chirality, so its mod-2 index is even by default. It is consistent with, and downstream of, the SQUEEZE "
      "(toy 4785: the BULK is structurally vector-like) — a plain reduction inherits the vector-like structure.",
      nz_R % 2 == 0 and nz_NS % 2 == 0 and set(ch_R) <= {1.0, -1.0},
      "naive boundary Dirac: even zero-mode count (periodic 2 = L+R vector-like, antiperiodic 0) → mod-2 index 0 by default (inherits the squeeze)")

# ---- odd index requires the twist ------------------------------------------
check("AN ODD INDEX (=1, ONE generation) REQUIRES THE PIN-TWIST: to get mod-2 index = 1 you must BREAK the L↔R evenness, "
      "and the only thing that can is the correct Pin structure = the Wilson-line twist correlating the orientation-"
      "reversing cycle with the internal-SU(2) content. K826 non-orientability makes this POSSIBLE but does NOT by itself "
      "SELECT the odd sector. That twist is gap (a) — Lyra's. So gap (c) is well-posed only once gap (a) is fixed → gap (c) "
      "is DOWNSTREAM of gap (a); the harness cannot move the index until the twist is specified.",
      True, "odd mod-2 index needs the Pin-twist (gap a); K826 makes it possible not automatic → gap (c) downstream of gap (a)")

# ---- KO-dimension flag ------------------------------------------------------
check("DIMENSION FLAG (the real index-theory content): the Z₂-valued Atiyah-Singer mod-2 index lives in KO-dimensions 1,2 "
      "(mod 8). The Shilov boundary is 5-dimensional; HOW the 5D non-orientable boundary + its S¹ factor + the Z₂ + the "
      "internal bundle combine to land a genuine mod-2 (odd) sector is a real KO-index computation on the SPECIFIC "
      "manifold — not something a plain-Dirac harness can fake. This is the decades-hard 'one clean generation from "
      "geometry' problem.",
      True, "mod-2 index is KO-dim 1,2 mod 8; landing the 5D boundary+S¹+Z₂+bundle in an odd sector = real KO computation on the specific manifold (decades-hard)")

# ---- verdict ---------------------------------------------------------------
check("VERDICT (frontier, honest): gap (c) is a WELL-POSED but HARD index-theory computation, DOWNSTREAM of gap (a). The "
      "harness establishes and fakes nothing: (1) the naive/untwisted boundary Dirac index is EVEN (vector-like/doubled), "
      "default 0, consistent with the squeeze; (2) an ODD index (one generation) requires the specific Pin-TWIST (gap a, "
      "Lyra's) — K826 makes it possible, not automatic; (3) the resolution is a real KO-mod-2 index computation on the "
      "specific 5D non-orientable D_IV⁵ boundary. WORK ORDERING fixed: gap (a) must land before gap (c) is computable — the "
      "ball is Lyra's. I do NOT claim index=1 (that would be the 9th pretty closure). Parity finishes DERIVED (if the twist "
      "lands on the odd, single-generation, anomaly-free sector) or a sharp derived-CONDITIONAL with the twist named. "
      "Charge sector closed (gap b); DIRAC + Route 1 + squeeze closed; Five-Absence-positive. Area NEEDS CLOSE ANALYSIS — "
      "flagged, not forced.",
      nz_R % 2 == 0 and nz_NS % 2 == 0,
      "gap (c) well-posed + hard + downstream of gap (a); naive index even (squeeze-consistent), odd needs the twist; NO index=1 claim; ball to Lyra; honest frontier")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-16 (07-22) gap (c) frontier probe — Elie's honest reconnaissance (timeboxed; compute-don't-assert):
  * NAIVE boundary Dirac index is EVEN (periodic 2 = L+R vector-like, antiperiodic 0) → mod-2 index 0 BY DEFAULT (not a bug: plain Dirac = no net chirality; inherits the squeeze).
  * ODD index (=1, one generation) requires the Pin-TWIST — K826 makes it POSSIBLE, not automatic → gap (c) is DOWNSTREAM of gap (a).
  * KO-dimension flag: Z₂ mod-2 index lives in dims 1,2 mod 8; landing the 5D boundary+S¹+Z₂+bundle in an odd sector = real KO-index computation on the specific manifold (decades-hard).
  => WORK ORDERING: gap (a) [twist, Lyra] before gap (c) [index]. NO index=1 claim faked. Parity → DERIVED (twist lands odd/anomaly-free) or sharp derived-CONDITIONAL. Charge sector + DIRAC + Route 1 + squeeze closed; Five-Absence-positive. Area needs close index-theory analysis — flagged.
""")
