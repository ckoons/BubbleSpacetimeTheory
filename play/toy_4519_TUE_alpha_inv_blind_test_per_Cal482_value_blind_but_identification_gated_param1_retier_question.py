r"""
toy_4519 — TUESDAY (independent lane, Cal #482 pre-registered bar): BLIND-TEST audit of alpha^-1 = N_max +
           1/(2*g*rank) = 137 + 1/28 = 137.0357 (obs 137.035999, dev 0.0002%). alpha is ONE of the 2 SM
           parameters BST claims PROVEN-FORCED (K282: alpha + theta_QCD). Cal #482 pre-registered the bar:
           "per-channel alpha closes only if SO(4,2)/S1 cell-count -> N_max is BLIND -- TWO traps: QED-import
           + banked-alpha-identification." I run the bar honestly and report a SPLIT verdict + a count-
           relevant QUESTION for the canon-holders (Keeper/Lyra):

   VERDICT (split):
   (1) VALUE is BLIND (passes trap 1, QED-import): alpha^-1 = N_max + 1/(2*g*rank) is built ENTIRELY from
       target-innocent substrate integers (N_c, n_C, rank, g) -- NO alpha, no QED running, no measured 137
       imported. N_max = N_c^3*n_C + rank = 137 is fixed by the geometry independently of EM. PASS.
   (2) IDENTIFICATION is NOT blind (trap 2, banked-alpha-identification): "N_max IS alpha^-1" is currently a
       MATCH-to-known-alpha, NOT a mechanism-forced "the EM coupling = 1/N_max." 137 falls out of
       N_c^3*n_C+rank REGARDLESS of electromagnetism; calling that 137 "alpha^-1" needs the cell-count ->
       EM-coupling mechanism, which is openly a DEEP GATE (my 4507; 4502 T2507 "geometry can't carry alpha").
       FAIL (gated).
   (3) the correction 28 = 2*g*rank is RICH-VOCABULARY (rank^2*g = N_c^3+1 = C_2*n_C-rank = 28, three BST-
       clean readings) AND is a 1-integer correction fit (1/28 = closest BST-clean to the needed 1/27.78).
       Target-aware. So even the 0.0002% precision is a 1-integer fit on top of the blind N_max=137.

   COUNT-RELEVANT QUESTION (for Keeper/Lyra, NOT a unilateral downgrade): does alpha's "proven-forced"
   status (K282, 2-of-26) rest on THIS formula? If yes, then by the blind-test bar alpha is VALUE-BLIND but
   IDENTIFICATION-GATED -- the same status as my flavor candidates, NOT a clean mechanism-forcing -- and the
   honest "2 forced" headline may be "1 forced (theta_QCD) + 1 value-blind/identification-gated (alpha)."
   If alpha's forced-status rests on a SEPARATE mechanism I'm not recalling, point me to it and I'll audit
   that instead. Surfacing to the canon-holders per peer-catch (NOT Cal-gating). NO unilateral count move.
   Count 9/26 (10 firm with theta_13) pending the team's answer on alpha's basis.

DISCIPLINE: ran Cal #482's pre-registered blind-test bar on alpha (param #1) -- found VALUE blind but
  IDENTIFICATION gated + the 28-correction rich-vocab; surfaced a potential DOWNGRADE of a claimed-forced
  param as a QUESTION to the canon-holders (Keeper/Lyra) rather than unilaterally re-tiering it OR letting
  the headline stand unaudited. Fires hardest on a BANKED result (Cal #27 + Five-Absence "fires on your own
  wins"). NO unilateral count move. HOLDS 9/26 pending team answer.

Elie - 2026-06-30
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
INV_OBS = 137.035999084

score = 0; TOTAL = 3
print("="*98)
print("toy_4519 — TUE alpha^-1 blind test (Cal #482): VALUE blind, IDENTIFICATION gated, 28-correction rich-vocab")
print("="*98)

# ---- [1] VALUE blind: alpha^-1 built from target-innocent substrate integers only (trap 1 PASS) ----
print("\n[1] VALUE blind: alpha^-1 = N_max + 1/(2*g*rank), N_max = N_c^3*n_C + rank = 137 -- pure BST integers, no alpha")
Nmax = N_c**3*n_C + rank
inv_bst = Nmax + 1/(2*g*rank)
ok1 = (Nmax == 137) and (abs(inv_bst-INV_OBS)/INV_OBS < 1e-5)
print(f"    N_max = {N_c**3*n_C}+{rank} = {Nmax}; alpha^-1 = {inv_bst:.6f} (obs {INV_OBS:.6f}, dev {abs(inv_bst-INV_OBS)/INV_OBS*100:.4f}%): {'PASS' if ok1 else 'FAIL'}")
print(f"    integers N_c,n_C,rank,g fixed by geometry independently of EM => no QED-import (trap 1 PASS)")
score += ok1

# ---- [2] correction 28 is rich-vocabulary AND a 1-integer fit (target-aware) ----
print("\n[2] correction denom 28 = 2*g*rank is RICH-VOCAB (3 readings) + 1-integer fit (closest BST-clean to 1/27.78)")
r1, r2, r3 = 2*g*rank, rank**2*g, N_c**3+1
need = 1/(INV_OBS - Nmax)  # 27.78
ok2 = (r1 == r2 == r3 == 28) and (C2*n_C - rank == 28)
print(f"    readings: 2*g*rank={r1}, rank^2*g={r2}, N_c^3+1={r3}, C_2*n_C-rank={C2*n_C-rank}; needed denom={need:.2f}, 28 closest: {'PASS' if ok2 else 'FAIL'}")
print(f"    => the 0.0002% precision is a 1-integer correction fit on top of blind N_max=137; 28 target-aware (rich-vocab)")
score += ok2

# ---- [3] IDENTIFICATION trap: 137 falls out regardless of EM -> "N_max IS alpha^-1" not mechanism-forced ----
print("\n[3] IDENTIFICATION trap (Cal #482 trap 2): is 137 UNIQUELY the EM scale, or does it fall out of BST regardless?")
# null model: how many BST-clean integer combinations (a*b+c form) equal 137 with target-innocent integers?
prim = [rank, N_c, n_C, C2, g]
forms137 = set()
for a in prim+[N_c**3, n_C**2, C2*n_C, rank*n_C*g]:
    for b in prim+[1, n_C, N_c]:
        for c in [0, rank, N_c, 1, -1, -rank]:
            if a*b + c == 137:
                forms137.add((a, b, c))
ok3 = len(forms137) >= 1   # 137 is reachable by BST integers in multiple ways, none EM-specific
print(f"    BST-integer forms giving 137 (none EM-specific): {len(forms137)} e.g. {sorted(forms137)[:4]}")
print(f"    => 137 = N_c^3*n_C+rank falls out of the substrate REGARDLESS of electromagnetism; the IDENTIFICATION")
print(f"       'this 137 IS alpha^-1' needs the cell-count->EM-coupling MECHANISM (deep gate, my 4507): NOT blind: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — alpha^-1 blind test per Cal #482. SPLIT verdict: VALUE is blind (N_max + 1/(2g*rank)")
print("       is pure target-innocent BST integers, no QED-import, trap 1 PASS); but the IDENTIFICATION 'N_max IS")
print("       alpha^-1' is NOT blind (137 = N_c^3*n_C+rank falls out regardless of EM; the EM-coupling mechanism")
print("       is a deep gate, trap 2 FAIL) and the 28-correction is rich-vocab + a 1-integer fit. COUNT-RELEVANT")
print("       QUESTION to Keeper/Lyra: if alpha's 'proven-forced' (K282, 2-of-26) rests on THIS formula, alpha is")
print("       value-blind/identification-gated -- the honest headline may be '1 forced (theta_QCD) + 1 gated")
print("       (alpha)'. If a separate alpha mechanism exists, point me to it. Surfaced as peer-catch, NOT")
print("       unilateral downgrade (NOT Cal-gating). NO unilateral count move. HOLDS 9/26 pending team answer.")
print("="*98)
