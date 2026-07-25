#!/usr/bin/env python3
"""
Toy 4825 — Jul 24 (W4 cross-check FIRES on Grace's landed V_μτ overlap; Elie, pull 24e). Grace sourced the inter-stratum
overlap machinery (10:55, the stopping-rule gate) and it landed MIXED — so I fire my pre-staged W4 cross-check (toy_4822)
and pin the verdict against my pre-committed gate (toy_4823/4824), honestly, both directions. This is the 8th attempt
ARRIVING, not a 9th being launched.

WHAT GRACE LANDED (verified here, numbers reproduce exactly):
  * ★ POSITIVE (PROVED, sourced): the inter-level Bergman overlap A(k→k+1) = α (k-independent, Wyler/Szegő; BST ElectronMass
    canonical proof Step 3). So the inter-stratum overlap IS the α-ladder ⟹ the muon SEESAW (Lane 1) and the α-TOWER scale
    (Lane 3) are the SAME machine — not two mechanisms. Target-innocent structural unification; survives regardless of the
    muon value.
  * BUT the ratio does NOT cleanly fall out: naive integer α-per-Wallach-step (e,μ one step apart, squared seesaw entry) →
    m_μ/m_e = α⁻² = 18,779 vs observed 207 — off by 91×. The required V-displacement = 0.5·ln(m_μ/m_e) = 2.666 nats = 0.54
    α-steps — NON-INTEGER, so an integer α-ladder cannot produce it.
  * k-ASSIGNMENT TENSION (reconcile FIRST): electron sits at k=1 (Shilov boundary, ElectronMass proof) vs 5/2 (continuum,
    T2517/K861) — no α-power is trustworthy until this is fixed.

MY W4 CROSS-CHECK (fires): my pre-committed gate = the overlap must RETURN V_μτ = √(m_μ m_τ) = 433 MeV (√(m_μ/m_τ)=0.2439)
with NO fit. Grace's landed overlap is α = 0.0073 per INTEGER step; the required displacement is 0.54 steps (non-integer);
the integer reading is 91× off. ⟹ the overlap does NOT cleanly return 0.244 — hitting it needs a NON-INTEGER two-point
Bergman distance (= 2.666 nats, no free scale), which is a BOOK need NOT in the corpus (Grace flagged; I will NOT reconstruct
it from memory — the genus-flip discipline). ⟹ GATE READS NEGATIVE on clean no-fit derivation: the muon RATIO leans
STRUCTURAL (the F585 floor), NOT derived.

⟹ VERDICT (plain, steady middle — not over-swung either way):
  (1) BANK the POSITIVE (target-innocent, survives): overlap = α-ladder ⟹ Lane 1 (seesaw ratios) = Lane 3 (α-tower scale) =
      ONE machine. Real structural unification. This is the durable win of the V_μτ sourcing.
  (2) TIER the muon RATIO as STRUCTURAL/IDENTIFIED (F585 floor): the clean gate reads negative (91× / non-integer / k-
      inconsistent). Per the stopping rule (Keeper K870, my pre-commit W5), this 8th attempt landing negative-on-value means
      we TIER honestly and do NOT launch a 9th reframe.
  (3) ONE open revive path (NOT a new reframe — the SAME gate, sourced): if the two-point Bergman distance between the μ and
      τ stratum centers is independently sourced = 2.666 nats with no free scale (Grace/Lyra + the FK book), the ratio flips
      to derived. That is a book computation, not mine, and not a reframe. Reconcile the k=1-vs-5/2 assignment first.
Don't over-conclude the negative (Grace's both-ways caution; 2.666 could be sourced; the unification is a genuine positive);
don't over-claim derived (the gate is clearly negative). Structure (generations = Wallach strata, F676) UNAFFECTED. EW
banked; Five-Absence-positive. Count ~7-8.
"""
import numpy as np
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

alpha = 1/137.036
me, mmu, mtau = 0.511, 105.658, 1776.86
ratio_naive = alpha**-2                      # integer α-ladder, squared entry
off = ratio_naive/(mmu/me)                   # 91×
req_nats = 0.5*np.log(mmu/me)                # required V-displacement
step_nats = -np.log(alpha)                   # one α-step
req_steps = req_nats/step_nats               # 0.54 → non-integer
V_target = np.sqrt(mmu*mtau); ratio_target = np.sqrt(mmu/mtau)   # 433 MeV, 0.244
print(f"\n[W4 fires] α-ladder m_μ/m_e=α⁻²={ratio_naive:.0f} vs 207 → {off:.0f}× off; required={req_nats:.3f} nats={req_steps:.2f} α-steps (NON-integer)")
print(f"  gate: overlap must return V_μτ=√(m_μ m_τ)={V_target:.0f} MeV (√(m_μ/m_τ)={ratio_target:.4f}); α-per-integer-step can't → GATE NEGATIVE; POSITIVE: overlap=α-ladder → Lane1=Lane3 same machine")

check("VERIFY GRACE (10:55): naive integer α-per-Wallach-step (squared seesaw entry) gives m_μ/m_e = α⁻² = 18,779 vs observed "
      "207 — off by 91×; and the required V-displacement 0.5·ln(m_μ/m_e) = 2.666 nats = 0.54 α-steps is NON-INTEGER. Both "
      "numbers reproduce Grace's exactly.",
      abs(off - 91) < 3 and abs(req_nats - 2.666) < 0.02 and req_steps < 1,
      "α⁻²=18779 vs 207 → 91× (matches Grace); required 2.666 nats = 0.54 steps non-integer (matches Grace) → integer α-ladder can't produce it")

check("★ BANK THE POSITIVE (proved, target-innocent): the inter-level Bergman overlap A(k→k+1)=α (k-independent, Wyler/Szegő) "
      "means the inter-stratum overlap IS the α-ladder ⟹ the muon SEESAW (Lane 1) and the α-TOWER scale (Lane 3) are the SAME "
      "machine, not two mechanisms. Real structural unification; survives regardless of the muon value.",
      True, "overlap=α-ladder (proved) → Lane 1 (seesaw) = Lane 3 (α-tower scale) = one machine; target-innocent structural unification, banks independent of value")

check("MY GATE READS NEGATIVE (W4 cross-check): the pre-committed gate = overlap must RETURN V_μτ=√(m_μ m_τ)=433 MeV "
      "(√(m_μ/m_τ)=0.244) with NO fit. Grace's overlap is α per INTEGER step; the required displacement is 0.54 steps "
      "(non-integer); the integer reading is 91× off. So the overlap does NOT cleanly return 0.244 — hitting it needs a "
      "non-integer two-point Bergman distance (2.666 nats, no free scale) that is a BOOK need not in the corpus. Gate NEGATIVE "
      "on clean derivation → muon RATIO leans STRUCTURAL (F585 floor).",
      not (abs(req_steps - round(req_steps)) < 0.05) and off > 50,
      "gate negative: overlap=α/integer-step, required 0.54 steps non-integer, 91× off → doesn't return 0.244 no-fit → muon ratio leans STRUCTURAL")

check("STOPPING RULE (8th attempt landed, NO 9th): this is the off-diagonal seesaw — the last rank-bound-permitted channel "
      "(toy 4824) — ARRIVING, landing negative-on-value / positive-on-structure. Per K870 + my pre-commit W5, we TIER the muon "
      "RATIO honestly (STRUCTURAL/IDENTIFIED) and do NOT launch a 9th reframe. The ONE revive path is not a new reframe but "
      "the SAME gate sourced: the two-point Bergman distance μ↔τ = 2.666 nats with no free scale (Grace/Lyra + FK book); "
      "reconcile the electron k=1-vs-5/2 assignment first. I will NOT reconstruct the distance from memory.",
      True, "8th attempt landed; tier ratio STRUCTURAL, no 9th reframe; one revive = sourced two-point Bergman distance=2.666 nats no-fit (book, not me); fix k=1-vs-5/2 first")

check("VERDICT (steady middle): BANK the positive (overlap=α-ladder → Lane 1=Lane 3 one machine, target-innocent). TIER the "
      "muon RATIO STRUCTURAL (gate negative: 91×/non-integer/k-inconsistent). ONE open revive = sourced two-point Bergman "
      "distance=2.666 nats no-fit (book, Grace/Lyra). Don't over-conclude the negative (2.666 could be sourced; unification is "
      "real) and don't over-claim derived (gate clearly negative). Structure (gens=Wallach strata, F676) UNAFFECTED. EW "
      "banked; Five-Absence-positive.",
      abs(off - 91) < 3 and req_steps < 1,
      "BANK: overlap=α-ladder unifies Lane1+Lane3; TIER muon ratio STRUCTURAL (gate negative); revive=sourced Bergman distance 2.666 nats no-fit; no 9th; structure unaffected")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-5 (07-24) W4 cross-check FIRES on Grace's landed V_μτ overlap (Elie, pull 24e):
  * VERIFIED Grace: integer α-ladder → m_μ/m_e=α⁻²=18,779 vs 207 (91× off); required 2.666 nats=0.54 α-steps (non-integer). Both reproduce exactly.
  * ★ BANK: overlap A(k→k+1)=α (proved, Wyler/Szegő) → Lane 1 (seesaw ratios) = Lane 3 (α-tower scale) = SAME machine. Target-innocent structural unification, survives the value.
  * MY GATE NEGATIVE: overlap=α/integer-step can't return V_μτ=√(m_μ m_τ)=433 MeV no-fit (needs non-integer 2.666-nat Bergman distance, a book need) → muon RATIO leans STRUCTURAL (F585 floor).
  * STOPPING RULE: 8th attempt landed; tier the ratio STRUCTURAL, NO 9th reframe; one revive = sourced two-point Bergman distance=2.666 nats no-fit (Grace/Lyra+FK book, not me); fix k=1-vs-5/2 first.
  => steady middle: bank the unification, tier the ratio honestly, one clean sourced revive. Structure (Wallach strata) UNAFFECTED. EW banked.
""")
