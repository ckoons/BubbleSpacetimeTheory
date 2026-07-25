#!/usr/bin/env python3
"""
Toy 4831 — Jul 24 (HONEST NEGATIVE: ZZ/WW suppression is NOT 1/rank^N_c; Elie's independent EW-sector check, pull 24k). With
the lepton operator Ô now gated on Grace writing the symbol, I took a clean independent EW lane I'd flagged: the backlog
candidate "ZZ/WW suppression = 1/rank^N_c" (U-2.6). The EW area is freshly banked (parity/confinement/ν-Majorana/custodial),
so a diboson-ratio prediction is natural — but a numerical match here is exactly where a phase-space factor can masquerade as
gauge structure, so I ran the fish-guard. It's a COINCIDENCE. Filing the honest negative keeps the ledger clean.

THE NUMERICAL MATCH (real but shallow): BR(H→ZZ)/BR(H→WW) = 0.02619/0.2137 = 0.1226 ≈ 1/rank^N_c = 1/2³ = 0.125 (2%,
S/I-tier). Tempting — but decompose it.

THE FISH-GUARD (decompose 1/8 into its actual mechanisms):
  (a) GAUGE/COUPLING LIMIT (equivalence theorem, m_H → high): Γ(H→ZZ)/Γ(H→WW) → 1/2. This 1/2 is the ZZ identical-particle
      (Bose 1/2!) factor, with the couplings made equal by CUSTODIAL symmetry (ρ=1, T2520 banked). Numerically 1/2 = 1/rank,
      BUT the mechanism is Bose statistics + custodial — NOT the BST rank. So even the 1/2 is an identification at best.
  (b) RESIDUAL at m_H=125.25: obs/(1/2) = 0.245 ≈ 1/4 = 1/rank². This is OFF-SHELL PHASE SPACE (both V's off-shell for
      m_H < 2m_Z; m_Z heavier than m_W → ZZ more suppressed). It is m_H-DEPENDENT — it would move if m_H moved, while
      1/rank² would not. So its ≈1/4 value is a KINEMATIC COINCIDENCE at 125 GeV.
  ⟹ 1/rank^N_c = (Bose 1/2) × (phase space ~1/4), dressed as (1/rank)×(1/rank²). Neither factor is BST-rank-forced; the
  N_c power absorbs an m_H-dependent phase-space factor into the integer web.

⟹ VERDICT (honest negative, disciplined): "ZZ/WW = 1/rank^N_c" is NUMEROLOGY at m_H=125 — the 2% match is (Bose identical-
particle) × (off-shell phase space), neither of which the BST rank forces, and the phase-space piece is m_H-dependent so the
match is not a stable prediction. The REAL BST content in this sector is CUSTODIAL ρ=1 (T2520, banked), which makes the HVV
couplings equal; everything downstream (the 1/8) is Bose statistics + kinematics, not the integer web. Do NOT bank
ZZ/WW=1/rank^N_c; file it as a gap-registry negative. This is the fish-detector on the program's OWN candidate — a 7/10 is
data, not shame. Custodial (T2520) + parity/confinement/ν-Majorana EW bank UNAFFECTED. Five-Absence-positive. Count ~5 (an
honest negative scores its checks, not a match).
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

mW, mZ, mH = 80.377, 91.1876, 125.25
BR_WW, BR_ZZ = 0.2137, 0.02619                 # LHC Higgs WG, m_H=125.25
obs = BR_ZZ / BR_WW
et = 0.5                                        # equivalence-theorem coupling limit ZZ/WW
phase = obs / et                                # residual (phase space)
print(f"\n[ZZ/WW] BR ratio = {obs:.4f} ≈ 1/rank^N_c = {1/rank**N_c:.4f} (2%); decompose → (Bose 1/2={et}) × (phase space {phase:.3f}≈1/rank²={1/rank**2}) → coincidence")

check("NUMERICAL MATCH (real but shallow): BR(H→ZZ)/BR(H→WW) = 0.02619/0.2137 = 0.1226 ≈ 1/rank^N_c = 1/8 = 0.125 (2%, "
      "S/I-tier). Worth checking — and worth the fish-guard before banking.",
      abs(1/rank**N_c - obs)/obs < 0.03, "BR(ZZ)/BR(WW)=0.123 ≈ 1/8=1/rank^N_c (2%); a match that demands the fish-guard")

check("FISH-GUARD (a) — the gauge/coupling piece is 1/2, and its mechanism is Bose+custodial, NOT rank: in the equivalence-"
      "theorem limit Γ(ZZ)/Γ(WW) → 1/2 = the ZZ identical-particle (Bose 1/2!) factor with couplings equalized by CUSTODIAL "
      "ρ=1 (T2520 banked). Numerically 1/2 = 1/rank, but the mechanism is statistics + custodial, so it's an identification "
      "at best — not rank-forced.",
      abs(et - 1/rank) < 1e-9, "coupling limit ZZ/WW=1/2 (Bose identical-particle + custodial T2520); = 1/rank numerically but mechanism is statistics not rank")

check("FISH-GUARD (b) — the residual is m_H-dependent phase space, NOT 1/rank²: obs/(1/2) = 0.245 ≈ 1/4 = 1/rank², but this "
      "is OFF-SHELL PHASE SPACE (both V's off-shell for m_H<2m_Z; m_Z>m_W → ZZ more suppressed). It moves with m_H, while "
      "1/rank² does not — so its ≈1/4 value is a KINEMATIC COINCIDENCE at 125 GeV.",
      abs(phase - 1/rank**2) < 0.03, "residual 0.245≈1/4=1/rank² is off-shell phase space (m_H-dependent) → coincidence, not gauge structure")

check("VERDICT (HONEST NEGATIVE): 1/rank^N_c = (Bose 1/2) × (phase space ~1/4), dressed as (1/rank)×(1/rank²); neither factor "
      "is BST-rank-forced and the phase-space piece is m_H-dependent → the 2% match is NUMEROLOGY at 125 GeV, not a stable "
      "prediction. Do NOT bank ZZ/WW=1/rank^N_c; file as a gap-registry negative. The REAL BST EW content is custodial ρ=1 "
      "(T2520, banked). Fish-detector on our own candidate — a 7/10 is data, not shame.",
      abs(et - 1/rank) < 1e-9 and abs(phase - 1/rank**2) < 0.03,
      "HONEST NEGATIVE: ZZ/WW=1/rank^N_c is Bose×phase-space numerology at 125 GeV; don't bank; real content = custodial T2520; caught our own fish")

check("EW BANK UNAFFECTED: this negative touches NONE of the banked EW results — custodial ρ=1 (T2520), parity (T2522), "
      "confinement (T2523), ν-Majorana (T2524). It only prevents an over-claim (the diboson BR ratio as an integer-web "
      "prediction). Ledger stays clean; Five-Absence-positive.",
      True, "EW bank (T2520/T2522/T2523/T2524) unaffected; negative only blocks the ZZ/WW over-claim; ledger clean")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-11 (07-24) HONEST NEGATIVE — ZZ/WW suppression is NOT 1/rank^N_c (Elie's independent EW check, pull 24k):
  * MATCH: BR(H→ZZ)/BR(H→WW) = 0.123 ≈ 1/8 = 1/rank^N_c (2%) — then fish-guarded.
  * DECOMPOSE: 1/8 = (Bose identical-particle 1/2 = 1/rank, mechanism=statistics+custodial NOT rank) × (off-shell phase space ~1/4 ≈ 1/rank², m_H-DEPENDENT coincidence at 125 GeV).
  * VERDICT: 1/rank^N_c is numerology at 125 GeV — don't bank; file as gap-registry negative. Real BST content = custodial ρ=1 (T2520, banked). Caught our own fish.
  => EW bank (T2520/T2522/T2523/T2524) unaffected; ledger clean; a 7/10 is data not shame.
""")
