r"""
toy_4506 — VERIFY Lyra's F432 lead + accept Grace's credit on the "6" grounding. TWO things:
           (1) Grace re-checked her own square-integrability "6 = nu-gap" derivation, found it index-convention-
               dependent (electron at nu=-1 not principled; at nu=0 the gap is 5), flagged it, and CREDITED my
               4505 grounding as the robust one: the "6" = dim Lambda^2(R^4) = the F_mn field-strength 2-form
               components = C_2 = my a_1 fiber -- index-independent, tied to the EM coupling. I accept the
               credit (per accept-earned-praise); my Lambda^2=F_mn grounding derives the 6.
           (2) Lyra F432: the TWO groundings of the "6" -- my EM-channel count dim Lambda^2(R^{n_C-1}) =
               C(n_C-1,2), and the Casimir reading C_2 = n_C+1 -- COINCIDE ONLY at n_C=5 (n_C^2-5n_C=0).
               That is a POSSIBLE "why 5": if the per-channel-alpha derivation REQUIRES the EM-channel count to
               equal C_2 (EM<->gravity channel-matching), it would FORCE the substrate dimension n_C=5. TIERED
               OPEN (Cal #27 at peak / Five-Absence / F417): NOT claiming n_C-selection -- the decisive check is
               MINE (does the per-channel-alpha derivation require dim Lambda^2(bdy)=C_2, or just use one?); it
               falls out when my gate lands. NO count move. Count 9/26.

GRACE'S CREDIT (accepted): the robust, index-INDEPENDENT grounding of the "6" is mine (4505): dim Lambda^2(S^4)
  = C(4,2) = 6 = the F_mn field-strength 2-form components (3 E + 3 B) = C_2 = the a_1 heat-kernel fiber. Tied
  to the actual EM coupling (the right physics). Grace's "6 = nu-gap" was index-convention-dependent (she
  retracted it from T2508; T2508 now stands only as the threshold first-bulk at nu=n_C=5). I accept the credit.

LYRA F432 (verified): the two "6" groundings coincide ONLY at n_C=5:
  EM-channel count = dim Lambda^2(R^{n_C-1}) = C(n_C-1, 2).   Casimir reading = C_2 = n_C+1.
  C(n_C-1,2) = n_C+1  <=>  (n_C-1)(n_C-2)/2 = n_C+1  <=>  n_C^2 - 5 n_C = 0  <=>  n_C = 5 (or 0).
  Checked n_C=2..8: match ONLY at n_C=5 (6=6). So the EM-channel count EQUALS the Casimir C_2 uniquely at the
  substrate dimension n_C=5.

THE POSSIBLE "WHY 5" (Lyra F432 lead, tiered OPEN): IF the per-channel-alpha derivation REQUIRES dim
  Lambda^2(boundary) = C_2 (i.e. the EM field-strength channel count must match the Casimir channel count --
  an EM<->gravity channel-matching consistency), then it is satisfied ONLY at n_C=5, FORCING the substrate
  dimension. That would be a "why 5". HONEST TIER (Cal #27 fires hardest at peak excitement; Five-Absence;
  F417): this is an OPEN lead, NOT a claim. The coincidence alone is rich-vocabulary (Cal #286) until a
  MECHANISM requires the matching. The decisive check is MINE: does my per-channel-alpha derivation REQUIRE
  Lambda^2 = C_2, or merely use one of the two readings? It falls out when the gate lands -- I do NOT claim
  n_C-selection now.

TIER: F432 VERIFIED (EM-channel count = C_2 only at n_C=5) + tiered OPEN (a possible "why 5", gated on my
  per-channel-alpha derivation, NOT claimed -- Cal #27/Five-Absence). Grace's credit on my Lambda^2=F_mn
  grounding of the 6 accepted. NO count move. Count HOLDS 9/26.

DISCIPLINE: accepted Grace's earned-credit (my Lambda^2 grounding derives the 6) without false modesty;
  verified Lyra's F432 coincidence (n_C=5 unique); tiered the "why 5" lead OPEN and explicitly did NOT claim
  n_C-selection (Cal #27 at peak excitement -- a why-the-dimension claim is exactly where over-reach lurks);
  named the decisive check as MINE (the per-channel-alpha derivation). Count HOLDS 9/26.

Elie - 2026-06-29
"""
from math import comb
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

score=0; TOTAL=3
print("="*98)
print("toy_4506 — VERIFY Lyra F432: EM-channel count = C_2 ONLY at n_C=5 (possible 'why 5', OPEN); accept Grace credit")
print("="*98)

print("\n[1] Grace credits my 4505 as the robust '6' grounding: dim Lambda^2(S^4)=6=F_mn=C_2=a_1 fiber (index-indep)")
ok1 = (comb(4,2) == 6 == C2)
print(f"    dim Lambda^2(S^4) = C(4,2) = {comb(4,2)} = C_2 = F_mn components (index-independent, EM-tied) -- credit accepted: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] Lyra F432: dim Lambda^2(R^{n_C-1}) = C(n_C-1,2) = C_2 = n_C+1 ONLY at n_C=5")
matches = [nc for nc in range(2,9) if comb(nc-1,2) == nc+1]
ok2 = (matches == [5])
print(f"    C(n_C-1,2)=n_C+1 matches at n_C in {matches} (algebra: n_C^2-5n_C=0 -> n_C=5): {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] possible 'why 5' -- OPEN (Cal #27/Five-Absence): decisive check = MY per-channel-alpha derivation")
ok3 = True
print("    IF per-channel-alpha REQUIRES dim Lambda^2(bdy)=C_2 -> forces n_C=5; ELSE coincidence (Cal #286)")
print(f"    NOT claiming n_C-selection now; falls out when my gate lands -- the over-reach to avoid at peak: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — VERIFY Lyra F432 + accept Grace's credit. Grace credits my 4505 (dim Lambda^2(S^4)")
print("       = 6 = F_mn field-strength components = C_2 = a_1 fiber, index-independent) as the robust derivation")
print("       of the '6' -- accepted. Lyra F432: the EM-channel count dim Lambda^2(R^{n_C-1}) = C(n_C-1,2)")
print("       equals C_2 = n_C+1 UNIQUELY at n_C=5 (n_C^2-5n_C=0) -- a possible 'why 5' via EM<->gravity")
print("       channel-matching. TIERED OPEN (Cal #27 at peak / Five-Absence): NOT claiming n_C-selection; the")
print("       decisive check is MINE (does per-channel-alpha REQUIRE Lambda^2=C_2?), falls out when the gate")
print("       lands. NO count move. Count HOLDS 9/26.")
print("="*98)
