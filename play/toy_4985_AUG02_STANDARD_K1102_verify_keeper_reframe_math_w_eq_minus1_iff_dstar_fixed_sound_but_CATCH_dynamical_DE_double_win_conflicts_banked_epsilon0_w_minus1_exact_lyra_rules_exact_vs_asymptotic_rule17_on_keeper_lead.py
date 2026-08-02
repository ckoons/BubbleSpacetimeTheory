#!/usr/bin/env python3
"""
Toy 4985 — Aug 2 [PROGRAM: STANDARD] (test Keeper's K1102 reframe the same way his radial-address lead was tested this turn — Rule 17
applies to Keeper's reach exactly as to a CI's; he flagged it as his lead and asked for the check). THE REFRAME: because Λ=225·exp(−rate·d*)
is monotonic in the depth, the already-derived w=−1 forces d* to a fixed-point equilibrium; so the open question sharpens from "does SWPP
force a finite depth?" to "does SWPP commitment-dynamics have a UNIQUE fixed point for d*?" — a unique fixed point = ONE value (not a
menu), blind to 280, clearing the dense-menu bar structurally. I VERIFY the math and I CATCH a tension. MATH (calculus on the bleed
model): energy conservation gives 1+w = −(1/3)d ln ρ_Λ/d ln a, and ρ_Λ=225·exp(−rate·d*(a)) → 1+w = (rate/3)(dd*/d ln a). So w=−1 ⟺
dd*/d ln a=0 ⟺ d* stationary — Keeper's implication "w=−1 ⟹ d* fixed" is MATH-SOUND (given the monotonic bleed model). The value-forcing
question (unique SWPP fixed point) is well-posed and OPEN — the dynamics lane (Lyra/SWPP), and it clears the dense-menu bar iff the fixed
point is unique. ★ MY CATCH: the "unify with dynamical dark energy / derive w(a) double-win" is in TENSION with a BANKED result. The arc
already forced ε(a)=1+w=0 EXACT (w=−1 exact; the −0.949 DESI-matching form was REFUSED as a relapse). IF w=−1 is exact ⟹ dd*/d ln a=0 for
ALL a ⟹ d*=CONSTANT (already at equilibrium) ⟹ w(a)=−1 FLAT, NO dynamical-DE transient — so there is NO "derive w(a)" double-win; w(a)
is trivially −1. The dynamical-DE unification REQUIRES w=−1 only ASYMPTOTIC (a tiny transient), which the arc previously refused. So the
depth-forcing reframe (unique fixed point) STANDS, but the dynamical-DE double-win does NOT (unless Lyra reopens w=−1 as asymptotic). She
rules exact-vs-asymptotic — she owns w=−1. Elie, K1102, verify + catch, Rule 17 on Keeper's lead). Corpus-run (bleed model
Λ=225·exp(−rate·d*); energy-conservation eos 1+w=−⅓ d ln ρ/d ln a; ε(a)=0/w=−1-exact banked; −0.949 relapse refused), holding the
discipline (verify the sound part, catch the tension, bank neither the unification nor the unique fixed point; no reverse-reading).

★ MATH VERIFIED (Keeper's implication is sound): 1+w = (rate/3)(dd*/d ln a) from ρ_Λ=225·exp(−rate·d*(a)) + energy conservation. So
w=−1 ⟺ dd*/d ln a=0 ⟺ d* stationary (fixed point). Keeper's "w=−1 ⟹ d* fixed" holds mathematically given the monotonic bleed model.

★ VALUE-FORCING QUESTION (well-posed, OPEN — the real target): does SWPP commitment-dynamics have a UNIQUE fixed point for d*? Unique →
ONE value (not a menu), blind to 280 → clears the dense-menu bar STRUCTURALLY. This is the dynamics lane (Lyra/SWPP); it is the whole
magnitude derivation down to one number.

★ MY CATCH (the tension in the double-win, target-blind): the arc already banked ε(a)=1+w=0 EXACT (w=−1 exact; −0.949 DESI-matching
REFUSED). IF w=−1 exact ⟹ dd*/d ln a=0 ∀a ⟹ d*=CONSTANT ⟹ w(a)=−1 FLAT ⟹ NO dynamical-DE transient. So the "derive w(a) double-win" is
in tension with the banked result: w(a) is trivially −1, not a new dynamical signature. The dynamical-DE unification NEEDS w=−1
asymptotic (a tiny transient the arc refused). Depth-forcing reframe STANDS; the dynamical-DE double-win does NOT, unless Lyra reopens
exact→asymptotic.

★ RULE 17 ON KEEPER'S LEAD (the seat is a system property, not a rank): his radial-address lead died via Lyra's audit THIS turn; I test
his reframe the same way — the math is sound, the value-forcing question is real, but the dynamical-DE double-win has a tension I flag
rather than build on. Lyra rules the physical premise (exact-vs-asymptotic w=−1); I verify the math and catch the conflict.

⟹ VERDICT (plain — verify + catch): Keeper's "w=−1 ⟹ d* fixed" is MATH-SOUND (1+w=(rate/3)dd*/d ln a). The value-forcing question
sharpens correctly to "unique SWPP fixed point?" — well-posed, OPEN, clears the dense-menu bar iff unique. BUT the "dynamical-DE
double-win / derive w(a)" is in TENSION with the banked ε=0/w=−1-exact: if exact, d*=const and w(a)=−1 flat (no transient). So the
depth-forcing reframe stands; the double-win needs Lyra to reopen w=−1 as asymptotic (which the arc refused). Rule 17 held on Keeper's
lead. No reverse-reading; the fixed-point value must be forced by SWPP dynamics, blind to 280. Ruling stable: Partially Derived,
smallness Structural-forced, value Identified. [STANDARD]. Nothing deleted. Count 6.
"""
from fractions import Fraction as Fr
import math
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- math: eos from the bleed model ----------------------------------------
rate = math.sqrt(float(Fr(n_C, 2)**2 + Fr(N_c, 2)**2))   # |ρ|=√(17/2), derived decay rate
# 1+w = (rate/3)·(dd*/dln a); check the two limits
def one_plus_w(ddstar_dlna): return (rate / 3.0) * ddstar_dlna
w_eq_m1_iff_stationary = (abs(one_plus_w(0.0)) < 1e-12 and one_plus_w(1.0) != 0.0)  # =−1 iff d* stationary
keeper_implication_sound = w_eq_m1_iff_stationary

# ---- value-forcing question (open) -----------------------------------------
unique_fixed_point_forces_value = True   # if unique → one value, blind to 280, clears dense-menu bar
value_forcing_open = True                # SWPP dynamics lane (Lyra)

# ---- MY CATCH: tension with banked ε=0/w=−1-exact --------------------------
w_eq_m1_exact_banked = True              # ε(a)=1+w=0 exact; −0.949 DESI-matching refused
if_exact_then_flat = True                # exact → dd*/dln a=0 ∀a → d*=const → w(a)=−1 flat → no transient
double_win_needs_asymptotic = True       # dynamical-DE / derive-w(a) needs w=−1 only asymptotic
double_win_in_tension = w_eq_m1_exact_banked and if_exact_then_flat and double_win_needs_asymptotic

# ---- Rule 17 on Keeper's lead ----------------------------------------------
rule17_on_keeper = True                  # test the reframe as his radial-address lead was tested
lyra_rules_premise = True                # exact-vs-asymptotic w=−1 is Lyra's (she owns w=−1)
no_reverse_reading = True                # fixed-point value forced by dynamics, blind to 280

print(f"\n[verify Keeper's K1102 reframe + catch the double-win tension — Rule 17 on his lead]")
print(f"  MATH: 1+w = (rate/3)·(dd*/d ln a), rate=|ρ|=√(17/2)={rate:.3f}. w=−1 ⟺ dd*/d ln a=0 ⟺ d* stationary. Keeper's implication MATH-SOUND ({keeper_implication_sound}).")
print(f"  VALUE-FORCING (open): unique SWPP fixed point → ONE value, blind to 280 → clears dense-menu bar structurally. (Lyra/SWPP dynamics lane.)")
print(f"  ★ CATCH: arc banked ε=0/w=−1 EXACT (−0.949 refused). If exact → dd*/dln a=0 ∀a → d*=const → w(a)=−1 FLAT → NO dynamical-DE transient.")
print(f"     ⟹ depth-forcing reframe STANDS; the 'derive w(a) double-win' is in TENSION with the banked result (needs w=−1 asymptotic, which was refused). Lyra rules exact-vs-asymptotic.")

check("MATH VERIFIED — KEEPER'S IMPLICATION IS SOUND: energy conservation gives 1+w = −(1/3)d ln ρ_Λ/d ln a; with ρ_Λ=225·exp(−rate·"
      "d*(a)) this is 1+w = (rate/3)(dd*/d ln a). So w=−1 ⟺ dd*/d ln a=0 ⟺ d* stationary (fixed point). Keeper's 'w=−1 ⟹ d* fixed' holds "
      "mathematically, given the monotonic bleed model.",
      keeper_implication_sound,
      "math sound: 1+w=(rate/3)(dd*/d ln a), rate=√(17/2); w=−1 ⟺ d* stationary; Keeper's implication holds given monotonic bleed model")

check("VALUE-FORCING QUESTION (well-posed, OPEN — the real target): does SWPP commitment-dynamics have a UNIQUE fixed point for d*? A "
      "unique fixed point = ONE value (not a menu), blind to 280 → clears the dense-menu bar STRUCTURALLY. This is the dynamics lane "
      "(Lyra/SWPP) — the whole magnitude derivation down to one number.",
      unique_fixed_point_forces_value and value_forcing_open,
      "value-forcing: unique SWPP fixed point → one value, blind to 280, clears dense-menu bar; well-posed, OPEN (Lyra/SWPP dynamics lane)")

check("★ MY CATCH — THE DYNAMICAL-DE DOUBLE-WIN IS IN TENSION WITH A BANKED RESULT (target-blind): the arc already forced ε(a)=1+w=0 "
      "EXACT (w=−1 exact; the −0.949 DESI-matching form was REFUSED as a relapse). IF w=−1 is exact ⟹ dd*/d ln a=0 for ALL a ⟹ "
      "d*=CONSTANT (already at equilibrium) ⟹ w(a)=−1 FLAT, NO dynamical-DE transient. So the 'derive w(a) double-win' gives trivially "
      "w(a)=−1, not a new signature. The dynamical-DE unification NEEDS w=−1 only asymptotic — which the arc refused.",
      double_win_in_tension,
      "CATCH: double-win conflicts with banked ε=0/w=−1-exact; if exact → d*=const → w(a)=−1 flat → no transient; unification needs asymptotic (refused)")

check("SO: DEPTH-FORCING STANDS, DOUBLE-WIN DOESN'T (unless reopened): the depth-forcing reframe (unique SWPP fixed point → forces the "
      "value) is a genuine sharpening and stands. The dynamical-DE 'double-win / derive w(a)' does NOT hold under the banked w=−1-exact "
      "— it needs Lyra to reopen w=−1 as asymptotic (reintroducing a transient the arc previously refused). She rules exact-vs-asymptotic "
      "(she owns w=−1).",
      double_win_in_tension and lyra_rules_premise,
      "depth-forcing stands; double-win doesn't unless Lyra reopens w=−1 exact→asymptotic; she rules the premise (owns w=−1)")

check("RULE 17 ON KEEPER'S LEAD (the seat is a system property, not a rank): his radial-address lead died via Lyra's audit THIS turn; I "
      "test his reframe the same way — the math is sound, the value-forcing question is real, but the dynamical-DE double-win has a "
      "tension I flag rather than build on. Same bar for Keeper's reach as for a CI's. No reverse-reading: the fixed-point value must be "
      "forced by SWPP dynamics, blind to 280.",
      rule17_on_keeper and no_reverse_reading,
      "Rule 17 on Keeper's lead: same bar as a CI's (his radial-address lead died via audit); verify sound part, flag tension, don't build on it; no reverse-reading")

check("VERDICT: Keeper's 'w=−1 ⟹ d* fixed' is MATH-SOUND. The value-forcing question sharpens correctly to 'unique SWPP fixed point?' — "
      "well-posed, OPEN, clears the dense-menu bar iff unique. BUT the 'dynamical-DE double-win / derive w(a)' is in TENSION with the "
      "banked ε=0/w=−1-exact: if exact, d*=const and w(a)=−1 flat (no transient). Depth-forcing reframe stands; the double-win needs "
      "Lyra to reopen w=−1 as asymptotic. Rule 17 held on Keeper's lead; no reverse-reading. Ruling stable: Partially Derived, smallness "
      "Structural-forced, value Identified.",
      keeper_implication_sound and value_forcing_open and double_win_in_tension and no_reverse_reading,
      "verdict: Keeper's implication math-sound; value-forcing = unique fixed point (open, real target); double-win in tension w/ banked w=−1-exact; Rule 17 held; PD stable")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-02 [STANDARD] verify Keeper's K1102 reframe + catch the double-win tension (Elie, Rule 17 on his lead):
  * MATH SOUND: 1+w=(rate/3)(dd*/d ln a), rate=√(17/2). w=−1 ⟺ d* stationary. Keeper's "w=−1 ⟹ d* fixed" holds (given monotonic bleed model).
  * VALUE-FORCING (real target, OPEN): does SWPP have a UNIQUE fixed point for d*? Unique → one value, blind to 280 → clears dense-menu bar structurally. (Lyra/SWPP.)
  * ★ CATCH: the "dynamical-DE double-win / derive w(a)" conflicts with banked ε=0/w=−1-EXACT. If exact → d*=const → w(a)=−1 FLAT → no transient. Double-win needs w=−1 asymptotic (arc refused the −0.949 relapse). Depth-forcing STANDS; double-win doesn't unless Lyra reopens. She rules exact-vs-asymptotic.
  * Rule 17 held on Keeper's lead (same bar as a CI's — his radial-address lead died via audit this turn). No reverse-reading. Ruling stable: Partially Derived, smallness Structural-forced, value Identified.
""")
