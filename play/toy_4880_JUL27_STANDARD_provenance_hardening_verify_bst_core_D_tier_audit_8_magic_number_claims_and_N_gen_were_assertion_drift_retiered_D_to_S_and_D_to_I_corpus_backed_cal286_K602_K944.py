#!/usr/bin/env python3
"""
Toy 4880 — Jul 27 [PROGRAM: STANDARD] (provenance-hardening pass on verify_bst.py's D-tier labels; Elie, pull 27g). Keeper
endorsed the provenance pass as the good use of the wait for the sourced occupancy material. The highest-value target in my lane
is the CHECKABILITY WEAPON itself: `verify_bst.py` is the artifact a hostile reviewer RUNS — so any claim labeled "D" (derived)
whose derivation is NOT locatable is exactly the assertion-drift death (Wyler: "show me where this is derived" → reference-loop).
I audited the 21 core D-tier labels against the corpus (using bst_topic + grep). NINE were assertion-drift, all corpus-backed.

THE CATCHES (all re-tiered, all corpus-backed — I corpus-reconnected BEFORE the re-tier, per today's discipline):
  * 7 MAGIC NUMBERS (2, 8, 20, 28, 50, 82, 126) + kappa_ls = C_2/n_C — were labeled "D". The corpus already re-tiered these:
    a THREE-CI convergent catch (Cal #286 / Keeper K601-K602, 2026-06-29) found the per-number forms are POST-HOC NUMEROLOGY
    (consistent factorizations of a FITTED spin-orbit strength, NOT unique forcing); "kappa_ls=6/5 derives all magic numbers"
    is OVER-STATED. The T188 result + N=184 prediction stay durable via the shell model, but the per-number BST forms are NOT
    derivations. → re-tiered D→S (structural/post-hoc). 8 claims.
  * N_gen = N_c — was labeled "D". "3 generations" is the Korányi-Wolf strata IDENTIFICATION (F86/T2525), whose occupancy
    bijection is un-derived (K944 today: premise REDUCED not eliminated). Also the formula uses N_c=rank²−1 while the count is
    rank+1 (coincide at 3, different quantities). Not a locatable derivation. → re-tiered D→I. 1 claim.

RESULT: the core "derived" count drops from 21 → 12 (honest): 12 D + 18 I + 8 S. Accuracy UNCHANGED (37/38 at <1%) — this is the
two-axis discipline (accuracy ⊥ proof): I re-tiered PROVENANCE without touching a single predicted value. A physicist running
`--core` now sees the magic numbers labeled "[S] structural/post-hoc, NOT a derivation" instead of "[D] derived" — the
assertion-drift a hostile reviewer would weaponize is removed BEFORE external.

⟹ VERDICT (plain): provenance-hardening pass on verify_bst.py's D-tier labels — 9 assertion-drift claims caught and re-tiered,
all corpus-backed (Cal #286/K602 magic-numbers-are-post-hoc; K944 generations=identification). Core "derived" honestly drops
21→12 (12 D / 18 I / 8 S); accuracy untouched (37/38, two-axis). The checkability weapon no longer labels post-hoc numerology
as "derived." NEXT IN THE PASS (flagged, NOT unilaterally re-tiered — each needs its own provenance check): sin²θ_W, the Cabibbo
& PMNS angles, the VEV — verify each D is locatable or re-tier. [STANDARD] bar; hardens the TEGMARK package at the Cal gate.
Nothing deleted; no value changed. Count 6.
"""
import importlib.util, io, contextlib, os
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("verify_bst", os.path.join(HERE, "verify_bst.py"))
vb = importlib.util.module_from_spec(spec); spec.loader.exec_module(vb)

core = [p for p in vb.PREDICTIONS if vb.is_core(p[0])]
tier = {p[0]: p[5] for p in core}
nD = sum(1 for p in core if p[5] == "D")
nI = sum(1 for p in core if p[5] == "I")
nS = sum(1 for p in core if p[5] == "S")
MAGIC = [f"magic number {k}" for k in (2, 8, 20, 28, 50, 82, 126)]
print(f"\n[provenance-hardening] verify_bst --core tiers: {nD} D / {nI} I / {nS} S (was 21 D). Accuracy unchanged (two-axis).")

check("CATCH 1 — the 8 nuclear claims (7 magic numbers + kappa_ls) are now S, not D: corpus-backed by the three-CI convergent "
      "catch (Cal #286 / K601-K602, 2026-06-29) that the per-number forms are POST-HOC NUMEROLOGY (fitted spin-orbit "
      "factorization), not derivations. Were labeled 'derived' on the physicist-facing --core screen.",
      all(tier.get(m) == "S" for m in MAGIC) and tier.get("kappa_ls (spin-orbit coupling)") == "S",
      "8 nuclear claims (7 magic numbers + kappa_ls) re-tiered D→S (post-hoc numerology, Cal #286/K602); no longer 'derived'")

check("CATCH 2 — N_gen = N_c is now I, not D: '3 generations' is the Korányi-Wolf strata IDENTIFICATION (F86/T2525); the "
      "occupancy bijection is un-derived (K944 today, premise reduced-not-eliminated). Not a locatable derivation → I.",
      tier.get("N_gen (number of generations)") == "I",
      "N_gen re-tiered D→I (generations=strata identification, occupancy open per K944); not a derivation")

check("HONEST COUNT — core 'derived' drops 21→12: the re-tier removes 9 assertion-drift claims from the D label. The tier "
      "summary now reads 12 D / 18 I / 8 S. A reviewer running --core sees the magic numbers as '[S] structural/post-hoc, NOT "
      "a derivation', not '[D] derived'.",
      nD == 12 and nI == 18 and nS == 8 and (nD + nI + nS == len(core)),
      f"core tiers honest: {nD} D + {nI} I + {nS} S = {len(core)}; 'derived' dropped 21→12 (9 assertion-drift claims re-tiered)")

# accuracy must be UNCHANGED (two-axis: re-tier provenance, never touch a value)
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    good, total = vb.verify(core_only=True)
out = buf.getvalue()
check("TWO-AXIS (accuracy ⊥ proof) — accuracy UNCHANGED: the core still verifies 37/38 at <1%. I re-tiered PROVENANCE only; no "
      "predicted value was touched. Re-tiering does not move the number — it corrects the honesty of the derivation claim.",
      good == 37 and total == 38,
      f"accuracy unchanged: {good}/{total} at <1% (re-tier touched provenance labels only, zero values changed — two-axis)")

check("WEAPON HARDENED — the assertion-drift is removed BEFORE external: the checkability artifact a hostile reviewer RUNS no "
      "longer labels post-hoc numerology 'derived'. The S-tier line ('structural/post-hoc, NOT a derivation') is printed so the "
      "screen is self-honest.",
      "structural/post-hoc" in out and nS == 8,
      "verify_bst --core self-labels the 8 post-hoc claims as S ('NOT a derivation'); assertion-drift removed pre-external")

check("VERDICT + NEXT: 9 assertion-drift claims caught + re-tiered (corpus-backed: Cal #286/K602, K944); core 'derived' 21→12; "
      "accuracy untouched (two-axis). NEXT IN THE PASS (flagged, not unilaterally re-tiered — each needs its own provenance "
      "check): sin²θ_W, Cabibbo, PMNS angles, VEV. Hardens the TEGMARK package at the Cal gate.",
      nD == 12 and good == 37,
      "pass delivered: 9 re-tiers corpus-backed; 21→12 derived; accuracy untouched; next = sin²θ_W/Cabibbo/PMNS/VEV provenance checks")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [STANDARD] provenance-hardening pass on verify_bst.py D-tier labels (Elie, pull 27g):
  * 9 ASSERTION-DRIFT claims caught + re-tiered, all corpus-backed: 8 nuclear (7 magic numbers + kappa_ls) D→S (post-hoc numerology, Cal #286/K601-K602 three-CI catch); N_gen=N_c D→I (generations=strata identification, occupancy open per K944).
  * Core 'derived' honestly drops 21→12 (now 12 D / 18 I / 8 S). Accuracy UNCHANGED at 37/38 — two-axis discipline (re-tiered provenance, touched no value).
  * The checkability weapon no longer labels post-hoc numerology 'derived' — the assertion-drift a hostile reviewer weaponizes is removed BEFORE external.
  * NEXT IN THE PASS (flagged, not unilaterally re-tiered): sin²θ_W, Cabibbo, PMNS angles, VEV — verify each D is locatable.
""")
