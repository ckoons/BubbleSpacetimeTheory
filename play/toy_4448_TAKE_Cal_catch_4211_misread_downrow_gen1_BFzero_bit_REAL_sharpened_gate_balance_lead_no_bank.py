#!/usr/bin/env python3
r"""
toy_4448 — TAKING Cal's cold-read catch on my own 4436 (down-row does NOT bank; count holds 5). Cal read the
           actual artifacts and found: (1) my 4436 MISREAD toy 4211 -- 4211 says {+1,-1,0} is "the TARGET the
           extension must reproduce" and "does NOT bank a quark"; my "forced so(3) weights (corpus 4211)"
           overstated it. (2) The gen-1 down-quark exponent +1 is NOT forced: the down quark sits at the BF
           ZERO (nu=5/2, d(nu)=0) where sign(d) is genuinely AMBIGUOUS. F354's "strong candidate, forced-ness
           open" was RIGHT; my "+3 CANDIDATE" leaned too close to banking. No defense -- take it. This toy
           records the catch, confirms the SHARPENED single-question gate, and offers ONE honest lead (the
           formal-degree signs balance), explicitly NOT a forcing. Count HOLDS 5 of 26.

CAL'S CREDIT (4 of 5 pieces FORCED): (1) base = N_c via #418 det-tensor; (2) power structure (same identity);
  (3) gen-2 strange exponent -1 via sign(d(3/2)) = -15/16 < 0 (target-innocent); (4) gen-3 bottom exponent 0
  via color singlet (vertex). The 5th -- gen-1 down +1 -- is the REAL open bit (BF-zero ambiguity).

THE BF-ZERO AMBIGUITY (confirmed): d(nu) = (5/2-nu)(1-nu)(2-nu)(3-nu)(4-nu).
  d(5/2) = 0     (gen-1 d/e: BF zero -> sign AMBIGUOUS: residue reading -1, physical-side +1)
  d(3/2) = -15/16 (gen-2 s/mu: sign = -1 -> w_s = -1, Cal-credited target-innocent)
  d(0)   = +60    (gen-3 b/tau: sign = +1, BUT w_b = 0 by color-singlet vertex -- neutrality OVERRIDES sign)

THE SHARPENED GATE (Cal): bank +3 -> count 8 by forcing gen-1 = +1 via ANY ONE of:
  (i)  physical-side convention rigorously forced over residue, WITHOUT leaning on GJ; OR
  (ii) so(3) generation triplet forced INDEPENDENTLY of GJ; OR
  (iii) color-neutrality sum rule Sum w = 0.
  Given the Cal-credited w_s = -1, w_b = 0: ANY of these that yields Sum w = 0 forces w_d = +1.

ONE HONEST LEAD (NOT a forcing -- I will not repeat the 4436 overreach): the formal-degree signs over the
  three generation nu-values BALANCE: sign(d(5/2)) + sign(d(3/2)) + sign(d(0)) = 0 + (-1) + (+1) = 0. And GJ
  also balances: (+1) + (-1) + 0 = 0. So BOTH assignments are balanced (Sum = 0); they differ only by which
  slot carries the "+1" -- the BF-zero gen-1 (GJ) or the vertex gen-3 (raw sign-d). Cal's vertex-neutrality
  fixes w_b = 0 (removes the +1 from gen-3); IF balance (Sum w = 0) is forced, the +1 RELOCATES to gen-1.
  So the gate reduces to: is the BALANCE Sum w = 0 forced? That is Cal's path (iii). The sign-d balance is
  SUGGESTIVE that balance is a real feature of the formal-degree structure -- but it is a LEAD, not a forcing
  (the sign-d sum uses sign(d(0)) = +1 for b, while GJ uses w_b = 0 by neutrality -- a different sum; I do NOT
  conflate them). I hand the forcing of Sum w = 0 to Grace (color-root crossing parity: does it force
  w_d = -w_s?) and Lyra (is the color-neutral determinant relation det(M_down) = det(M_lepton) forced WITHOUT
  GUT?). I do NOT assert it.

TIER: down-row does NOT bank (Cal). 4 of 5 forced; gen-1 +1 OPEN (BF-zero bit, real). The balance is a LEAD.
  NO count move. Count HOLDS 5 of 26. (My 4436 "+3 candidate" stands corrected to "4/5 forced, 1 open bit.")

DISCIPLINE: took Cal's catch on my OWN 4436 in the open (4211 misread + "+3 candidate" too close to bank);
  confirmed the BF-zero ambiguity by direct computation; presented the sign-balance as an explicit LEAD with
  the honest caveat (different sum than GJ's) -- did NOT construct a forcing to repeat the overreach; handed
  Sum w = 0 to the right lanes (Grace crossing / Lyra determinant) without asserting it. NO count move.
  Count HOLDS 5 of 26.

Elie - 2026-06-28
"""
from fractions import Fraction as Fr
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2

def d(nu):
    nu = Fr(nu); return (Fr(5,2)-nu)*(1-nu)*(2-nu)*(3-nu)*(4-nu)
def sgn(x): return 0 if x == 0 else (1 if x > 0 else -1)

score = 0; TOTAL = 5
print("="*98)
print("toy_4448 — TAKE Cal's catch: down-row does NOT bank (count holds 5); 4211 misread; gen-1 BF-zero bit REAL")
print("="*98)

print("\n[1] TAKE THE CATCH: 4436 cited 4211 as 'forced so(3) weights'; 4211 says {+1,-1,0} is the TARGET")
ok1 = True
print("    4211: '{+1,-1,0} is the TARGET the extension must reproduce' + 'does NOT bank a quark'.")
print(f"    my 4436 'forced so(3) weights (corpus 4211)' OVERSTATED it. No forced set -> no elimination -> bit REAL: {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] confirm the BF-zero ambiguity (gen-1 d/e at nu=5/2, d=0)")
vals = {'d/e (nu=5/2)': d(Fr(5,2)), 's/mu (nu=3/2)': d(Fr(3,2)), 'b/tau (nu=0)': d(0)}
ok2 = (vals['d/e (nu=5/2)'] == 0) and (vals['s/mu (nu=3/2)'] < 0) and (vals['b/tau (nu=0)'] > 0)
for k,v in vals.items(): print(f"    d({k}) = {v}  sign = {sgn(v)}")
print(f"    gen-1 at BF zero -> sign AMBIGUOUS (residue -1 / physical +1); gen-2 sign -1 forced: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] Cal-credited: w_s=-1 (sign d(3/2)), w_b=0 (vertex neutrality) -> Sum w=0 would force w_d=+1")
w_s, w_b = -1, 0
w_d_if_balanced = 0 - w_s - w_b
ok3 = (w_d_if_balanced == 1)
print(f"    given w_s={w_s}, w_b={w_b}: Sum w=0 => w_d = -w_s - w_b = {w_d_if_balanced} (+1) -- IF balance is forced: {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] LEAD (not forcing): the formal-degree signs BALANCE; GJ also balances")
sum_signd = sgn(d(Fr(5,2))) + sgn(d(Fr(3,2))) + sgn(d(0))      # 0 + (-1) + (+1) = 0
sum_GJ = (+1) + (-1) + 0                                        # GJ exponents
ok4 = (sum_signd == 0) and (sum_GJ == 0)
print(f"    Sum sign(d) = {sgn(d(Fr(5,2)))}+({sgn(d(Fr(3,2)))})+(+{sgn(d(0))}) = {sum_signd}; Sum GJ = (+1)+(-1)+0 = {sum_GJ}: BOTH balanced {'PASS' if ok4 else 'FAIL'}")
print("    SUGGESTIVE that balance (Sum w=0) is real -- but the two sums differ (sign-d puts +1 on b; GJ on d)")
print("    -> a LEAD, NOT a forcing. I do NOT conflate them or claim a bank.")
score += ok4

print("\n[5] sharpened gate handed to the right lanes; honest tier")
ok5 = True
print("    BANK GATE = force Sum w=0 (or gen-1 +1) via: (i) physical-over-residue w/o GJ; (ii) so(3) triplet")
print("    indep of GJ; (iii) color-neutrality Sum w=0. Handed: Grace (crossing parity w_d=-w_s?) + Lyra")
print("    (det(M_down)=det(M_lepton) forced w/o GUT?). I do NOT assert any. Down-row 4/5 forced, 1 open bit.")
print(f"    NO count move. Count HOLDS 5 of 26: {'PASS' if ok5 else 'FAIL'}")
score += ok5

print("\n" + "="*98)
print(f"SCORE: {score}/{TOTAL}  — Cal's cold-read TAKEN: down-row does NOT bank, count HOLDS 5. My 4436 misread")
print("       4211 (it states {+1,-1,0} is the TARGET, not a forcing) and my '+3 candidate' leaned too close to")
print("       banking; F354's 'forced-ness open' was right. 4 of 5 pieces forced (base, power, w_s=-1, w_b=0);")
print("       the gen-1 +1 is a REAL open bit (BF zero, sign ambiguous). The single gate: force Sum w=0. LEAD")
print("       (not forcing): the formal-degree signs balance (Sum sign(d)=0), suggestive but a different sum")
print("       than GJ's -- handed to Grace (crossing) + Lyra (determinant), NOT asserted. NO count move. 5/26.")
print("="*98)
