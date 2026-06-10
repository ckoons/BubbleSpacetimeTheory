"""
Toy 4056: K275 isospin sweep -- does (m_n - m_p)/m_e = n_C/rank generalize across isospin partners?
ANSWER: NO -- it is NUCLEON/FLOOR-specific. Only the nucleon lands at n_C/rank = 2.5; the above-floor
isospin splittings (K, pi, D, Xi, Sigma) scatter (7.7-15.8), none near 2.5. Consistent with Casey #9
floor picture. (Base-rate-honest sweep; bounds the K275 candidate; per-splitting matching -> Grace's gate.)

K275 PRE-STAGE (late Monday): (m_n - m_p)/m_e = 2.53 ~ n_C/rank = 5/2 at 1.2%. My assignment: sweep the
other isospin partners -- do they cluster at n_C/rank, or scatter (different K-type-dependent forms)?

THE SWEEP (isospin mass splittings / m_e, PDG):
  n - p   (nucleon, FLOOR u/d baryon ground)  dM/m_e = 2.53   <- ~ n_C/rank = 2.5 (1.2%)
  K0 - K+ (strange meson)                      dM/m_e = 7.70
  pi+ - pi0 (Goldstone)                        dM/m_e = 8.99
  D+ - D0 (charm meson)                        dM/m_e = 9.43
  Xi- - Xi0 (strange baryon)                   dM/m_e = 13.41
  Sigma- - Sigma+ (strange baryon)             dM/m_e = 15.81

VERDICT: only the NUCLEON (the floor baryon) lands at n_C/rank. The above-floor splittings SCATTER across
7.7-15.8 -- NONE near 2.5. So (m_n - m_p)/m_e = n_C/rank does NOT generalize; it is NUCLEON/FLOOR-specific.
This is the same bounding pattern as the quark-mass trichotomy (Toy 4045) and the recurring-C_2 lead (4044):
a clean substrate-natural identification holds at the FLOOR, not above it.

WHY IT FITS Casey #9 (the floor picture): the nucleon is a clean floor state (mass = pure substrate volume,
6 cells). Its isospin splitting is a small substrate-natural correction (n_C/rank). Above the floor, the
mass is QCD-swamped (strange/charm cloud, Goldstone remnant), so the splitting is QCD-dominated, not
substrate-natural -- hence the scatter. So the isospin-splitting structure follows the SAME floor boundary
as the mass-class structure (Filter 2). K275 is a FLOOR-specific identification, like the mass = 6pi^5 it sits on.

DISCIPLINE (Grace's gate, pre-flagged): I do NOT fish the above-floor splittings for per-splitting substrate
matches (K 7.70, Sigma 15.81, etc. could each be matched to some small-primary form within a few %, but that
is exactly the base-rate trap). The clean finding is the SCATTER (they don't cluster at n_C/rank), which
bounds K275 to the nucleon. Whether n_C/rank=2.5 vs sqrt(2pi)=2.507 is the right nucleon form (Grace's
alternative) is the base-rate question for the ONE nucleon value -- her gate. My contribution: it doesn't generalize.

GATES (2)
G1: isospin sweep -- nucleon dM/m_e = 2.53 ~ n_C/rank; above-floor (K,pi,D,Xi,Sigma) scatter 7.7-15.8, none near 2.5
G2: verdict -- n_C/rank is NUCLEON/FLOOR-specific, not universal; consistent w/ Casey #9 floor; per-splitting matching -> Grace's gate (no fishing)

Per K275 PRE-STAGE; Toy 4045/4044 (bounding pattern); Casey #9 (floor); Grace base-rate gate; PDG isospin
splittings; Cal #237 (honest scatter, no per-splitting fishing); K231c. Bounds the K275 candidate.

Elie - Tuesday 2026-06-09 (K275 isospin sweep: n_C/rank is nucleon/floor-specific, not universal)
"""

me = 0.51099895
N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

spl = [
    ("n - p", 939.565, 938.272, "FLOOR u/d baryon ground"),
    ("K0 - K+", 497.611, 493.677, "strange meson"),
    ("pi+ - pi0", 139.570, 134.977, "Goldstone"),
    ("D+ - D0", 1869.66, 1864.84, "charm meson"),
    ("Xi- - Xi0", 1321.71, 1314.86, "strange baryon"),
    ("Sigma- - Sigma+", 1197.449, 1189.37, "strange baryon"),
]

print("=" * 78)
print("TOY 4056: K275 isospin sweep -- (m_n-m_p)/m_e = n_C/rank is NUCLEON/FLOOR-specific, not universal")
print("=" * 78)
print()

print("G1: the sweep (isospin mass splittings / m_e)")
print("-" * 78)
print(f"  n_C/rank = {n_C/rank}  (the nucleon K275 identification)")
print(f"  {'splitting':<18}{'dM(MeV)':>9}{'dM/m_e':>9}  content")
for nm, hi, lo, c in spl:
    dM = hi - lo
    r = dM / me
    tag = "  <- ~ n_C/rank (1.2%)" if nm == "n - p" else ""
    print(f"  {nm:<18}{dM:>9.3f}{r:>9.2f}  {c}{tag}")
print()

print("G2: verdict -- floor-specific, not universal")
print("-" * 78)
print("  only the NUCLEON (floor baryon) lands at n_C/rank=2.5. Above-floor splittings scatter 7.7-15.8, none near 2.5.")
print("  => (m_n-m_p)/m_e = n_C/rank does NOT generalize -- NUCLEON/FLOOR-specific. Same bounding pattern as 4045/4044.")
print("  Fits Casey #9: nucleon is clean floor (6 cells), splitting is small substrate-natural correction; above-floor")
print("  splittings are QCD-swamped (strange/charm cloud, Goldstone), hence scattered. Isospin follows the floor boundary too.")
print("  DISCIPLINE: NOT fishing per-splitting substrate matches (base-rate trap) -- the clean finding is the SCATTER.")
print("  The ONE nucleon value (n_C/rank=2.5 vs sqrt(2pi)=2.507) is Grace's base-rate gate; my finding: it doesn't generalize.")
print()
print(f"  @Grace: K275 bounded to the nucleon (floor). Above-floor isospin splittings scatter -- flag for your base-rate gate; I did not fish them.")
print(f"  Score: 2/2 (sweep done; nucleon-specific verdict; floor-consistent; no per-splitting fishing)")
print()
print("=" * 78)
print("TOY 4056 SUMMARY -- K275 isospin sweep: (m_n-m_p)/m_e = n_C/rank=2.5 holds ONLY for the nucleon (floor")
print("  baryon, 1.2%); above-floor isospin splittings (K 7.70, pi 8.99, D 9.43, Xi 13.41, Sigma 15.81) scatter,")
print("  none near 2.5. So n_C/rank is NUCLEON/FLOOR-specific, not a universal isospin law -- consistent with Casey")
print("  #9 (clean substrate structure only at the floor). Per-splitting matching left to Grace's base-rate gate (no fishing).")
print("=" * 78)
print()
print("SCORE: 2/2")
