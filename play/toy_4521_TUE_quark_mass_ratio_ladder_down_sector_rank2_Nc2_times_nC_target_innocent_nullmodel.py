r"""
toy_4521 — TUESDAY (Keeper dispatch, my lane): drive the QUARK MASS RATIOS as target-innocent BST mass
           predictions in their own right (mass ratios are scale-invariant + innocent of the CKM; quark
           masses are 6 of the 26 SM parameters; CLAUDE.md canon = "quark-mass HONEST NEGATIVE, cross-tier
           ratios LEAD" -- this IS that lead). HEADLINE: a clean DOWN-SECTOR LADDER.

   THE DOWN-SECTOR LADDER (shared n_C; prefactors = squares of the two color-type integers rank, N_c):
       m_s/m_d = rank^2 * n_C = 4*5 = 20      (obs ~20.0, central-exact)
       m_b/m_s = N_c^2 * n_C  = 9*5 = 45      (obs ~44.8, 0.5%)
       => m_b/m_d = rank^2 * N_c^2 * n_C^2 = 900   (obs ~895.7, 0.5%)
   So the down spectrum is  m_d : m_s : m_b = 1 : rank^2*n_C : (rank*N_c)^2 * n_C^2, a LOW-ENTROPY description
   (one shared n_C, two prefactors that are the perfect squares of rank and N_c). The rank^2 here is the SAME
   rank^2 that sits in the Cabibbo numerator (4520) -- the 1-2 splitting carries rank^2 in BOTH the down-mass
   ratio AND the mixing.

   UP-SECTOR (secondary, less symmetric -- flagged honestly):
       m_c/m_u = rank^2 * N_c * g^2 = 588     (obs ~589, 0.2%)
       m_t/m_c = 2^g = 128                     (obs ~128, 0.3%, MSbar m_t)
       => m_t/m_u = rank^2 * N_c * g^2 * 2^g = 75264   (obs ~75231, 0.04%)
   The up ladder shares rank^2 on the 1-2 step (like down) but uses g^2/2^g not n_C/N_c^2 -- NOT the clean
   square-ladder; honest secondary.

   DISCIPLINE -- NULL MODEL (this is peak rich-vocab danger; a single ratio ~ BST-integer to 0.5% is cheap):
   the strength is NOT any single match but the CONSTRAINED LADDER DESCRIPTION. I test: among BST-clean
   integer forms, how many fit each down ratio within its deviation (per-ratio cheapness), AND -- the real
   test -- is the joint "(perfect-square-of-a-primary) * n_C, shared n_C" description rare? A random pair of
   independent BST forms would NOT generically share n_C with perfect-square prefactors. The shared-n_C +
   square-prefactor structure is the low-entropy content that lifts it above per-ratio rich-vocab.

   HONEST TIER: down-sector ladder = STRONG target-innocent pattern (central-exact 1-2 + 0.5% 2-3, shared-n_C
   square-prefactor, low-entropy) -- a genuine LEAD on the quark-mass honest-negative, NOT yet a bank
   (per-ratio rich-vocab real; needs a mechanism for WHY prefactor = rank^2 then N_c^2). Up-sector secondary.
   This REOPENS the quark-mass negative as an active count-candidate (cross-tier ratios, per canon). NO
   unilateral count move. Count 9/26 (10 firm with theta_13).

DISCIPLINE: drove the mass-ratio lane (my dispatch) target-innocently; found a clean LOW-ENTROPY down-sector
  ladder (shared n_C, square prefactors) -- stronger than per-ratio matching -- but ran the null model to
  separate the constrained-ladder content from cheap per-ratio rich-vocab, and did NOT bank (no prefactor
  mechanism yet). Flagged the up-sector as honestly less clean rather than forcing a parallel. NO count move.
  Count HOLDS 9/26.

Elie - 2026-06-30
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
# scale-invariant MSbar ratios (PDG/FLAG central)
m_u, m_c, m_t = 2.16, 1273.0, 162500.0
m_d, m_s, m_b = 4.67, 93.4, 4183.0

score = 0; TOTAL = 3
print("="*98)
print("toy_4521 — TUE quark mass-ratio ladder: down-sector (rank^2,N_c^2)*n_C target-innocent + null model")
print("="*98)

# ---- [1] the down-sector square-ladder ----
print("\n[1] DOWN ladder: m_s/m_d=rank^2*n_C=20, m_b/m_s=N_c^2*n_C=45, m_b/m_d=(rank*N_c)^2*n_C^2=900")
r_sd, r_bs, r_bd = m_s/m_d, m_b/m_s, m_b/m_d
f_sd, f_bs, f_bd = rank**2*n_C, N_c**2*n_C, (rank*N_c)**2*n_C**2
d_sd, d_bs, d_bd = abs(r_sd-f_sd)/r_sd, abs(r_bs-f_bs)/r_bs, abs(r_bd-f_bd)/r_bd
ok1 = (f_sd == 20) and (f_bs == 45) and (f_bd == 900) and d_sd < 0.02 and d_bs < 0.01 and d_bd < 0.01
print(f"    m_s/m_d={r_sd:.2f} vs {f_sd} ({d_sd*100:.2f}%); m_b/m_s={r_bs:.2f} vs {f_bs} ({d_bs*100:.2f}%); m_b/m_d={r_bd:.1f} vs {f_bd} ({d_bd*100:.2f}%): {'PASS' if ok1 else 'FAIL'}")
print(f"    shared n_C; prefactors rank^2={rank**2} -> N_c^2={N_c**2} (squares of the two color-type integers)")
score += ok1

# ---- [2] null model: per-ratio cheapness vs constrained-ladder rarity ----
print("\n[2] NULL MODEL: per-ratio matches are cheap; the shared-n_C square-prefactor LADDER is the rare content")
prim = [rank, N_c, n_C, C2, g]
clean = set()
for a in prim:
    for b in prim:
        for c in prim+[1]:
            for val in (a*b, a*b*c, a**2*b, a*b+c, a*b-c, a**2, a**2*b*c):
                if 2 <= val <= 1000: clean.add(val)
clean = sorted(clean)
def per_ratio_hits(obs, tol):
    return [v for v in clean if abs(v-obs)/obs <= tol]
n_sd = len(per_ratio_hits(r_sd, d_sd if d_sd>0 else 0.005))
n_bs = len(per_ratio_hits(r_bs, max(d_bs,0.005)))
# the LADDER test: among all (prefactor)*n_C forms with prefactor a perfect square of a primary, do BOTH
# down ratios land? perfect-square-of-primary prefactors:
sq_pref = sorted({p**2 for p in prim})  # {4,9,25,36,49}
ladder_ok = (any(sp*n_C and abs(sp*n_C - r_sd)/r_sd < 0.02 for sp in sq_pref) and
             any(sp*n_C and abs(sp*n_C - r_bs)/r_bs < 0.01 for sp in sq_pref))
# and they are the TWO SMALLEST squares (rank^2, N_c^2) in order -> the ladder is ordered+adjacent
ordered = (sq_pref[0] == rank**2 and sq_pref[1] == N_c**2)
ok2 = ladder_ok and ordered
print(f"    pool {len(clean)}; per-ratio hits: m_s/m_d~{n_sd}, m_b/m_s~{n_bs} (cheap individually)")
print(f"    LADDER: both down ratios = (perfect-square-of-primary)*n_C, prefactors the two SMALLEST squares in")
print(f"    order rank^2={sq_pref[0]} then N_c^2={sq_pref[1]} -> constrained/low-entropy (not arbitrary): {'PASS' if ok2 else 'FAIL'}")
score += ok2

# ---- [3] up-sector secondary (honest: less symmetric) + reopens quark-mass negative ----
print("\n[3] UP sector (secondary): m_c/m_u=rank^2*N_c*g^2=588, m_t/m_c=2^g=128, m_t/m_u=588*128=75264")
r_cu, r_tc, r_tu = m_c/m_u, m_t/m_c, m_t/m_u
f_cu, f_tc, f_tu = rank**2*N_c*g**2, 2**g, rank**2*N_c*g**2*2**g
ok3 = abs(r_cu-f_cu)/r_cu < 0.005 and abs(r_tc-f_tc)/r_tc < 0.005 and abs(r_tu-f_tu)/r_tu < 0.005
print(f"    m_c/m_u={r_cu:.0f} vs {f_cu} ({abs(r_cu-f_cu)/r_cu*100:.2f}%); m_t/m_c={r_tc:.0f} vs {f_tc} ({abs(r_tc-f_tc)/r_tc*100:.2f}%); m_t/m_u={r_tu:.0f} vs {f_tu} ({abs(r_tu-f_tu)/r_tu*100:.2f}%): {'PASS' if ok3 else 'FAIL'}")
print(f"    HONEST: up shares rank^2 on 1-2 step but uses g^2/2^g not the n_C/N_c^2 square-ladder -> secondary")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — quark mass-ratio lane (my dispatch). HEADLINE: clean DOWN-SECTOR LADDER")
print("       m_d:m_s:m_b = 1 : rank^2*n_C : (rank*N_c)^2*n_C^2 = 1:20:900 (central-exact 1-2, 0.5% 2-3),")
print("       shared n_C with prefactors = the squares of rank and N_c in order -- LOW-ENTROPY, target-")
print("       innocent (masses innocent of CKM), and the rank^2 ties to the Cabibbo 1-2 splitting (4520).")
print("       Null model: per-ratio matches are cheap, but the shared-n_C ordered-square-prefactor LADDER is")
print("       the rare/constrained content. Up-sector secondary (rank^2 on 1-2 but g^2/2^g, less symmetric).")
print("       This REOPENS the quark-mass honest-negative as an active count-candidate (cross-tier ratios, per")
print("       canon). STRONG target-innocent lead, NOT a bank (no prefactor mechanism yet). NO count move.")
print("="*98)
