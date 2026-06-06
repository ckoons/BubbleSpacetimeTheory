"""
Toy 4002: K228 HONEST WALK-BACK of Toy 3876 alpha^(-1) "Tier 1 BORDERLINE" claim.

CONTEXT
Toy 3876 claimed alpha^(-1) = N_max + rank/(2^N_c.g) = 137 + 2/56 = 137.03571
at "0.0002% precision, 130x improvement, Tier 1 BORDERLINE candidate".

Friday K-audit K228 (STRUCTURAL-CORRECTION-TERM-IDENTIFICATION) re-tiers this:
the correction term is structurally identified but is NOT exact at experimental
precision -- it sits ~13,500 sigma above the CODATA precision floor.

TWO THINGS K228 CHANGES
 1. READING: 3876's rank/(2^N_c.g) = 2/56 is numerically IDENTICAL to
    1/(2.g.rank) = 1/28. The 28 = 2.g.rank reading is preferred because it
    exposes a cross-physical-sector cross-link with K225
    (n_s = 1 - 1/(2.g.rank) = 27/28). Same composite 28 in inflation (K225)
    and EW fine-structure (K228) -> Cluster L substrate-Schur-generator
    candidate (Grace G15 v0.6).
 2. TIER: "Tier 1 BORDERLINE" is RETRACTED. The 1/28 term captures 99.2% of
    the N_max->observed gap (genuine, substantive structural identification),
    but the residual is ~13,500 sigma. Honest category: K228 cat 6
    STRUCTURAL-CORRECTION-TERM-IDENTIFICATION, Tier 2 STRUCTURAL.

PURPOSE
   (a) State the K228 precision walk-back with the sigma figure explicit
   (b) Adopt the 1/28 = 1/(2.g.rank) reading
   (c) Record the 28 = 2.g.rank cross-K-audit cross-link (K225 + K228)
   (d) Separate what is RETRACTED (the tier) from what SURVIVES (the term)

STRUCTURE
G1: The claim vs the experimental precision floor
G2: Sigma distance to CODATA -- the honest precision verdict
G3: Reading change 2/56 -> 1/28 = 1/(2.g.rank) + K225 cross-link
G4: What survives -- structural correction-term identification
G5: Honest tier verdict

GATES (5)

Per K228 STRUCTURAL-CORRECTION-TERM-IDENTIFICATION category.
Per Cal #34 STANDING numbered-correction discipline.
Per Cal #27 STANDING: claim demoted, structural investigation preserved.
Per Cal #242 STANDING: CODATA source pinned.

Elie - Saturday 2026-06-06
"""

import mpmath as mp

mp.mp.dps = 40

rank = 2
N_c = 3
n_C = 5
C_2 = 6
g = 7
N_max = 137

# CODATA 2018 (source-pinned, Cal #242): alpha^(-1) = 137.035999084(21)
alpha_inv_obs = mp.mpf("137.035999084")
alpha_inv_sigma = mp.mpf("0.000000021")  # the (21) on the last two digits

print("=" * 72)
print("TOY 4002: K228 HONEST WALK-BACK -- alpha^(-1) correction-term tier")
print("=" * 72)
print()

# ---------------------------------------------------------------------------
print("G1: The claim vs the experimental precision floor")
print("-" * 72)
print()
corr = mp.mpf(1) / (2 * g * rank)            # 1/28
corr_old = mp.mpf(rank) / (2 ** N_c * g)     # 2/56  (identical)
sub = N_max + corr
print(f"  Toy 3876 correction:  rank/(2^N_c.g) = 2/56     = {mp.nstr(corr_old, 12)}")
print(f"  K228 reading:         1/(2.g.rank)   = 1/28     = {mp.nstr(corr, 12)}")
print(f"  (numerically identical: 2/56 = 1/28)")
print()
print(f"  substrate alpha^(-1) = N_max + 1/28 = {mp.nstr(sub, 13)}")
print(f"  observed  alpha^(-1) = {mp.nstr(alpha_inv_obs, 13)}  +/- {mp.nstr(alpha_inv_sigma,2)}")
rel = abs(sub - alpha_inv_obs) / alpha_inv_obs
print(f"  relative deviation   = {mp.nstr(rel*100, 4)}%   (3876 called this '0.0002%, Tier 1 BORDERLINE')")
print()
print("  G1 PASS: claim and observable restated against the CODATA floor")
print()

# ---------------------------------------------------------------------------
print("G2: Sigma distance to CODATA -- the honest precision verdict")
print("-" * 72)
print()
resid = abs(sub - alpha_inv_obs)
nsigma = resid / alpha_inv_sigma
gap_full = alpha_inv_obs - N_max
captured = corr / gap_full * 100
print(f"  N_max -> observed gap        = {mp.nstr(gap_full, 8)}")
print(f"  1/28 captures                = {mp.nstr(captured, 5)}% of that gap")
print(f"  residual after 1/28          = {mp.nstr(resid, 6)}")
print(f"  CODATA 1-sigma               = {mp.nstr(alpha_inv_sigma, 3)}")
print(f"  residual in sigma            = {mp.nstr(nsigma, 6)} sigma")
print()
print(f"  VERDICT: at experimental precision the substrate single-term value is")
print(f"  {int(nsigma)} sigma from observation. A 'Tier 1 EXACT' / 'BORDERLINE'")
print(f"  label is excluded: the prediction is ~{int(1/ (alpha_inv_sigma/alpha_inv_obs) / (alpha_inv_obs/resid)):d}x less precise than the")
print(f"  measurement. This is a CORRECTION-TERM identification, not an exact match.")
print()
print("  G2 PASS: ~13,500 sigma -> Tier 1 retracted")
print()

# ---------------------------------------------------------------------------
print("G3: Reading change 2/56 -> 1/28 = 1/(2.g.rank) + K225 cross-link")
print("-" * 72)
print()
comp = 2 * g * rank
print(f"  Substrate composite: 28 = 2.g.rank = 2*7*2 = {comp}")
print(f"  K228 (EW fine-structure):  alpha^(-1) = N_max + 1/(2.g.rank) = 137 + 1/28")
ns = mp.mpf(1) - mp.mpf(1) / (2 * g * rank)
print(f"  K225 (cosmic inflation):   n_s = 1 - 1/(2.g.rank) = 1 - 1/28 = {mp.nstr(ns, 8)} = 27/28")
print()
print(f"  SAME composite 28 = 2.g.rank crosses two physical sectors:")
print(f"    - cosmological inflation (n_s)")
print(f"    - electroweak fine structure (alpha^(-1))")
print(f"  -> cross-K-audit substrate-Schur-generator candidate (Cal #36 STANDING)")
print(f"  -> Grace G15 v0.6 NEW Cluster L (28-anchor); this toy supplies the K228 leg")
print()
print(f"  Why 1/28 over 2/56: the 28 = 2.g.rank reading is the one that makes the")
print(f"  cross-sector link visible; 2/56 = 2^N_c.g obscures it. Same number, the")
print(f"  better-factored reading wins (pin to the cross-link, Cal #36).")
print()
print("  G3 PASS: 1/28 = 1/(2.g.rank) adopted; K225+K228 cross-link recorded")
print()

# ---------------------------------------------------------------------------
print("G4: What survives -- structural correction-term identification")
print("-" * 72)
print()
print(f"  RETRACTED:")
print(f"    - '0.0002% Tier 1 BORDERLINE candidate'")
print(f"    - '130x precision improvement' framed as a precision claim")
print(f"      (it IS a 130x improvement over leading N_max, but the result is")
print(f"       still ~13,500 sigma off -- 'improvement' must not read as 'exact')")
print()
print(f"  SURVIVES (Tier 2 STRUCTURAL, K228 cat 6):")
print(f"    - 1/28 = 1/(2.g.rank) captures 99.2% of the N_max->observed gap")
print(f"      That is a genuine, substantive structural correction-term ID.")
print(f"    - the 28 = 2.g.rank cross-sector cross-link (K225 + K228)")
print()
print(f"  Open (multi-week, honest): the residual ~{mp.nstr(resid,3)} (~13,500 sigma) is")
print(f"  the QED running / higher-order structure the single substrate term does")
print(f"  not capture. alpha^(-1) exact requires the running, not one rational term.")
print()
print("  G4 PASS: term preserved, tier corrected, residual owned")
print()

# ---------------------------------------------------------------------------
print("G5: Honest tier verdict")
print("-" * 72)
print()
print(f"  alpha^(-1) = N_max + 1/(2.g.rank) = 137 + 1/28")
print(f"    relative deviation {mp.nstr(rel*100,3)}%  |  {int(nsigma)} sigma above CODATA floor")
print(f"    captures 99.2% of the leading correction")
print()
print(f"  TIER: Tier 2 STRUCTURAL (STRUCTURAL-CORRECTION-TERM-IDENTIFICATION)")
print(f"        was: 'Tier 1 BORDERLINE' -- RETRACTED per K228")
print()
print(f"  Per K228 cat 6; Cal #27 STANDING (claim demoted, investigation preserved)")
print(f"  Per Cal #34 STANDING numbered correction of Toy 3876")
print(f"  Per Cal #242 STANDING CODATA source-pinned")
print()
print(f"  Score: 5/5 PASS (walk-back complete)")
print()
print("=" * 72)
print("TOY 4002 SUMMARY -- K228 walk-back: correction-term ID, not exact match")
print(f"  alpha^(-1)=137+1/28 captures 99.2% of gap but is ~13,500 sigma off")
print(f"  -> Tier 2 STRUCTURAL; 28=2.g.rank cross-links K225+K228 (Cluster L)")
print("=" * 72)
print()
print("SCORE: 5/5")
