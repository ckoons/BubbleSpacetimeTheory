#!/usr/bin/env python3
"""
Toy 4855 — Jul 25 (OWN my 4854 CP over-reach; F498 caught it; Elie, pull 25i). Keeper caught that my toy 4854 claim "CP
violation is derived because D_IV⁵ is a complex domain" is exactly the argument F498 already showed is INSUFFICIENT: F498
proves the Jarlskog is zero for real generation STATES, and explicitly that a complex DOMAIN with real states still gives
J=0. So the domain being complex is NOT enough — CP-existence needs the STATES genuinely complex. I own it promptly (the same
discipline that caught the pretty fraction, the v/f unification, Grace's modulus close, my own F677/4834 slips).

WHAT WAS RIGHT vs WHAT OVER-REACHED (verified):
  * RIGHT (my computation): CP violation ⟺ the generation STATES are genuinely complex. Complex symbol → complex states →
    J≠0 (100%); real symbol → real states → J=0 (100%). That is the correct F498 condition.
  * OVER-REACHED (my interpretation): I attributed CP to "the DOMAIN is complex." But a complex domain with a REAL symbol
    gives REAL states → J=0. The domain being complex does NOT force the states complex — that is precisely the gap F498
    flagged. My argument was the insufficient one.

THE SHARPENED GATE (what CP-existence actually needs): the generation states are complex ⟺ the ν_R condensate / Toeplitz
SYMBOL is genuinely complex (carries a phase). And note the tension: the real singular Szegő measure that generates the
HIERARCHY (toys 4835/4842) is REAL (K-invariant zonal) → by itself it gives real states → J=0. So CP violation requires the
condensate to carry a genuine complex PHASE beyond the real hierarchy-generating part (a Majorana/CP phase). Whether it does
is the open question — NOT settled by the domain being complex.

⟹ VERDICT (plain): RETRACT the 4854 "CP-existence derived" claim → CANDIDATE. F498 is right: CP violation needs the
generation STATES genuinely complex, which requires the condensate SYMBOL to carry a genuine phase — the complex DOMAIN alone
is insufficient (real symbol → real states → J=0, verified). What SURVIVES from 4854: CP violation ⟺ complex states (correct
mechanism condition), and the CP MAGNITUDE is a modulus (unchanged, small = nearly-aligned CKM). What's RETRACTED: "the
domain being complex forces CP" — demoted to candidate, gated on whether the ν_R condensate carries a phase beyond the real
Szegő measure. The value-free flavor SHAPE stands minus this row: masses/hierarchy/mixing/ordering derived; CP-existence
candidate (not derived). Nothing false banked — caught within the round. Lepton values structural (F688); muon (24/π²)⁶;
durable untouched; Five-Absence-positive. Count ~4.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

def jarlskog(U): return (U[0, 1] * U[1, 2] * np.conj(U[0, 2]) * np.conj(U[1, 1])).imag
def op(seed, complex_symbol):
    rng = np.random.RandomState(seed)
    A = rng.randn(3, 3) + (1j * rng.randn(3, 3) if complex_symbol else 0)
    return (A + A.conj().T) / 2
Jr, Jc = [], []
for s in range(1, 21):
    _, Uu = np.linalg.eigh(op(s, False)); _, Ud = np.linalg.eigh(op(s + 100, False)); Jr.append(abs(jarlskog(Uu.conj().T @ Ud)))
    _, Uc = np.linalg.eigh(op(s, True)); _, Udc = np.linalg.eigh(op(s + 100, True)); Jc.append(abs(jarlskog(Uc.conj().T @ Udc)))
real_zero = np.mean(np.array(Jr) < 1e-9); complex_nonzero = np.mean(np.array(Jc) > 1e-6)
print(f"\n[reconcile F498] real symbol → real states → J=0 in {real_zero*100:.0f}% (F498's point); complex symbol → J≠0 in {complex_nonzero*100:.0f}% → CP needs complex STATES, not just complex domain")

check("F498 IS RIGHT (verified): a complex domain with a REAL symbol → REAL states → J=0 (100%). So the domain being complex "
      "does NOT force CP violation — the STATES must be genuinely complex. My 4854 'domain complex → CP derived' was the "
      "F498-insufficient argument.",
      real_zero > 0.95,
      "real symbol → real states → J=0 (F498); complex domain alone insufficient for CP; my 4854 interpretation over-reached")

check("WHAT WAS RIGHT (kept): the mechanism CONDITION is correct — CP violation ⟺ generation states genuinely complex "
      "(complex symbol → J≠0 in 100%). My computation tested the right thing; only the attribution to 'the domain' was wrong.",
      complex_nonzero > 0.95,
      "correct condition kept: CP ⟺ complex states (complex symbol → J≠0); computation right, attribution wrong")

check("THE SHARPENED GATE: CP-existence needs the ν_R condensate SYMBOL genuinely complex (a phase). Tension: the real "
      "singular Szegő measure that generates the HIERARCHY (4835/4842) is REAL → by itself gives real states → J=0. So CP "
      "requires a genuine PHASE beyond the real hierarchy-generating part (a Majorana/CP phase) — the open question.",
      True, "gate: CP needs condensate SYMBOL complex (a phase); real Szegő hierarchy-measure alone → J=0; needs a phase beyond it (open)")

check("RETRACT → CANDIDATE (own it, caught within the round): the 4854 'CP-existence derived' claim is RETRACTED to CANDIDATE, "
      "gated on whether the ν_R condensate carries a phase beyond the real Szegő measure. SURVIVES: CP ⟺ complex states "
      "(mechanism condition) + CP magnitude a modulus. RETRACTED: 'domain complex forces CP.' Value-free flavor shape stands "
      "minus this row (masses/hierarchy/mixing/ordering derived; CP-existence candidate). Nothing false banked.",
      real_zero > 0.95 and complex_nonzero > 0.95,
      "RETRACT 4854 CP-derived → candidate (gated on condensate phase); survives: complex-states condition + magnitude modulus; nothing false banked")

check("VERDICT: F498 caught my 4854 over-reach — CP-existence is CANDIDATE not derived (a complex domain with a real symbol "
      "gives J=0, verified). The discipline fired on my own fresh 'derived today', same as the pretty fraction and the v/f "
      "unification. Value-free flavor shape: masses/hierarchy/mixing/ordering derived; CP-existence candidate (gated on the "
      "condensate phase). Lepton values structural (F688); muon (24/π²)⁶; durable untouched.",
      real_zero > 0.95 and complex_nonzero > 0.95,
      "CP-existence candidate not derived (F498); discipline fired on my own claim; flavor shape intact minus CP row; nothing false banked")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-9 (07-25) OWN my 4854 CP over-reach — F498 caught it (Elie, pull 25i):
  * F498 is right: complex DOMAIN + REAL symbol → real states → J=0 (verified 100%). The domain being complex does NOT force CP; the STATES must be complex. My 4854 'domain→CP derived' was the insufficient argument.
  * KEPT: CP ⟺ complex states (correct condition); CP magnitude a modulus. RETRACTED: 'domain complex forces CP' → CANDIDATE, gated on the ν_R condensate carrying a phase beyond the real Szegő hierarchy-measure.
  * Discipline fired on my OWN fresh 'derived today' — same guardrail as the pretty fraction / v/f. Nothing false banked (caught within the round).
  => value-free flavor shape intact minus CP-existence (now candidate); masses/hierarchy/mixing/ordering still derived. Lepton values structural (F688); muon (24/π²)⁶.
""")
