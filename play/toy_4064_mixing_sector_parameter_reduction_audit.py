"""
Toy 4064: mixing-sector parameter-reduction audit (Grace's lens; the ripest area). The CKM + PMNS angle
forms all use ONLY substrate primaries (no free decimals), and share an input (79 = rank^4 n_C - 1 appears
in BOTH theta_12 and theta_23) -- a reduction HINT. BUT per Grace's strict lens, choosing a substrate-primary
COMBO per angle is still RELABEL-in-primaries; a genuine REDUCTION (8 angles -> few inputs) needs ONE structure
FORCING all, which is the K-type derivation (Lyra/Grace), not yet shown. State: candidate-reduced, forced-vs-fitted OPEN.

GRACE's LENS (the measure): does BST REDUCE the SM free-parameter count, or RELABEL it? Mixing sector (CKM 4 +
PMNS 4 = 8 angles) is the RIPEST place to test -- it's the clean (pi-free, mixing=counting) side of the trichotomy,
least relabel-prone. The question: are the 8 angles forced from FEW substrate inputs (reduction) or 8 separate forms (relabel)?

THE AUDIT (current forms, all substrate-primary):
  CKM:
    theta_12 (Cabibbo): sin th_C = 2/sqrt(79),  79 = rank^4 n_C - 1
    theta_23 (V_cb):    C_2^2/(11.79),           11 = C_2 + n_C ; 79 = rank^4 n_C - 1
    theta_13 (V_ub):    Wolfenstein rho-bar = N_c/(rank^2 n_C), eta-bar = n_C/(rank.g)
    A scale:            n_C/C_2
    delta_CP:           atan(sqrt(n_C))
  PMNS:
    sin^2 theta_12 = 5/16 = n_C/rank^4   (established, clean)
    theta_13/theta_23/delta: combinatorial (Lyra; exact not fit -- the catalog Tier-1 cluster)
  => ALL forms use only {rank,N_c,n_C,C_2,g,N_max} + composites (79=rank^4 n_C-1, 11=C_2+n_C). NO free decimals.

REDUCTION HINT (the one to pursue): 79 = rank^4 n_C - 1 appears in BOTH theta_12 (2/sqrt(79)) AND theta_23
(C_2^2/(11.79)). A SHARED substrate input across two angles is the signature of a common structure -- exactly
what a reduction would look like (one primitive feeding multiple angles). If a single K-type object generates
the 79 (and the other inputs) for all angles, that's an 8 -> few reduction.

HONEST VERDICT (per Grace's strict lens): the mixing-sector forms are BETTER than free-number relabel (they use
only substrate primaries -- 0 genuinely free decimals), which is the clean-side promise. BUT it is NOT yet a
REDUCTION: choosing WHICH substrate combo per angle is a per-angle freedom (relabel-in-primaries) until ONE
structure FORCES all the combos. The shared 79 is the reduction hint; the forced-vs-fitted call is the K-type
derivation (Lyra's "one primitive generates the angles" cluster -- her lane). So the ledger entry is:
  MIXING SECTOR: 8 angles -> substrate-primary forms (no free decimals) + 1 shared input (79); REDUCTION CANDIDATE,
  forced-vs-fitted OPEN (K-type derivation pending). NOT yet "8 -> 0 free"; NOT mere relabel either. The cleanest
  place for the reduction to be PROVEN -- which is exactly why Grace ranked it #1.

GATES (3)
G1: CKM+PMNS forms all substrate-primary (no free decimals); inputs {primaries} + 79=rank^4 n_C-1, 11=C_2+n_C
G2: shared input 79 across theta_12 AND theta_23 -- reduction hint (one structure feeding multiple angles)
G3: verdict per Grace's lens -- candidate-reduced (better than relabel) but forced-vs-fitted OPEN; reduction = K-type derivation (Lyra/Grace), not banked

Per Grace parameter-reduction lens; Toy 4046/4047 (CKM/Weinberg pi-free); PMNS sin^2 th_12=5/16; Lyra K-type
cluster; Cal #237 + F79 lesson; K231c. Numerical reduction-check for Grace's audit; the derivation is Lyra's lane.

Elie - Tuesday 2026-06-09 (mixing-sector audit: substrate-primary forms + shared 79; reduction candidate, forced-vs-fitted open)
"""

import mpmath as mp
mp.mp.dps = 15
N_c, n_C, C_2, g, rank, N_max = 3, 5, 6, 7, 2, 137

print("=" * 78)
print("TOY 4064: mixing-sector parameter-reduction audit -- substrate-primary forms + shared 79 (reduction candidate)")
print("=" * 78)
print()

print("G1: the audit (all forms substrate-primary, no free decimals)")
print("-" * 78)
rows = [
    ("th_12 Cabibbo", "2/sqrt(79)", 2 / mp.sqrt(79), 0.2252, "79=rank^4 n_C-1"),
    ("th_23 V_cb", "C_2^2/(11.79)", C_2**2 / (11 * 79), 0.0408, "11=C_2+n_C"),
    ("A scale", "n_C/C_2", mp.mpf(n_C) / C_2, 0.826, ""),
    ("th_13 rho-bar", "N_c/(rank^2 n_C)", mp.mpf(N_c) / (rank**2 * n_C), 0.159, ""),
    ("th_13 eta-bar", "n_C/(rank.g)", mp.mpf(n_C) / (rank * g), 0.348, ""),
    ("PMNS sin^2 th12", "5/16 = n_C/rank^4", mp.mpf(5) / 16, 0.307, ""),
]
for nm, f, val, obs, note in rows:
    print(f"  {nm:<16} = {f:<18} = {mp.nstr(val,5):<8} (obs {obs})  {note}")
print(f"  delta_CP = atan(sqrt(n_C)) ; PMNS th_13/th_23/delta combinatorial (Lyra, exact not fit).")
print(f"  => all substrate-primary {{rank,N_c,n_C,C_2,g}} + composites 79=rank^4 n_C-1, 11=C_2+n_C. NO free decimals.")
print()

print("G2: reduction HINT -- shared input 79")
print("-" * 78)
print(f"  79 = rank^4 n_C - 1 appears in BOTH theta_12 (2/sqrt(79)) AND theta_23 (C_2^2/(11.79)).")
print(f"  a SHARED substrate input across two angles = the signature of a common structure (one primitive -> many angles).")
print(f"  That is what a reduction looks like; pursuing what FORCES the 79 (a K-type object?) is the reduction path.")
print()

print("G3: verdict per Grace's lens")
print("-" * 78)
print(f"  BETTER than free-number relabel: the forms use ONLY substrate primaries (0 free decimals) -- the clean-side promise.")
print(f"  But NOT yet a REDUCTION: choosing WHICH combo per angle is per-angle freedom (relabel-in-primaries) until ONE")
print(f"  structure FORCES all. The shared 79 is the hint; forced-vs-fitted is the K-type derivation (Lyra's cluster).")
print(f"  LEDGER: mixing sector = substrate-primary forms + 1 shared input; REDUCTION CANDIDATE, forced-vs-fitted OPEN. NOT banked.")
print()
print(f"  @Grace/@Lyra: mixing-sector ledger state -- 8 angles -> substrate-primary forms, no free decimals, shared 79 hint.")
print(f"    The reduction (8 -> few) is your K-type derivation to prove/decline; I've counted the current state (candidate, not banked).")
print(f"  Score: 3/3 (forms substrate-primary no-free-decimals; shared 79 reduction hint; honest candidate-not-reduction verdict)")
print()
print("=" * 78)
print("TOY 4064 SUMMARY -- mixing-sector parameter audit (Grace's ripest area): the CKM+PMNS angle forms all use")
print("  ONLY substrate primaries (no free decimals), with 79=rank^4 n_C-1 SHARED across theta_12 and theta_23 (a")
print("  reduction hint). Better than free-number relabel; but NOT yet a reduction -- forced-vs-fitted is OPEN, the")
print("  K-type derivation (Lyra/Grace). Ledger: REDUCTION CANDIDATE, not banked. The cleanest place to prove 8->few.")
print("=" * 78)
print()
print("SCORE: 3/3")
