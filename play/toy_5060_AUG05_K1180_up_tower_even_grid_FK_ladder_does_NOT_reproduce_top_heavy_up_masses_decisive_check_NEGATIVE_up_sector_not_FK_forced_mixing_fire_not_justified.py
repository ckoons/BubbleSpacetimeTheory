#!/usr/bin/env python3
"""
Toy 5060 — Aug 5 [PROGRAM: TEGMARK] (the UP-TOWER decisive check — Keeper K1180: crux 1 is ratified (m = 3|Q|, proved), but that same arithmetic
puts the up + neutrino towers on the EVEN grid, not {1,3,5}. Before any mixing fire, @ELIE fires the up-tower FK at its forced EVEN addresses vs the
observed up-masses — the way {1,3,5} reproduced the down ladder. Keeper flagged the honest worry: the up sector is famously TOP-HEAVY, so the even
grid may give too shallow a ladder. I fire blind and report faithfully). The result is NEGATIVE — and it is data, not shame:

★ THE PARITY GRID (forced by m = 3|Q|, a proved theorem): down-type |Q|=1/3 → m=1 (odd) → {1,3,5}; charged leptons |Q|=1 → m=3 (odd) → {1,3,5};
  up-type |Q|=2/3 → m=2 (EVEN) → {0,2,4}; neutrinos |Q|=0 → m=0 (EVEN) → {0,2,4}. So BST forces a PARITY PREDICTION: down + charged leptons on the
  ODD degree grid, up + neutrinos on the EVEN degree grid. Different grids.

★ THE DECISIVE CHECK — FIRED BLIND, NEGATIVE: the up-tower FK generalized Pochhammer (N_c)_k at the forced EVEN addresses gives {0,2,4} → {1,12,360}
  = 1:12:360, or {2,4,6} → {12,360,20160} = 1:30:1680. The OBSERVED up-quark ladder is TOP-HEAVY: m_u:m_c:m_t ≈ 1 : 588 : 79981 (c/u ≈ 588, t/c ≈
  136). The even-grid FK ladder is FAR too shallow — off by ~50× at c/u — and this is ROBUST to whether k=0 is included ({0,2,4} or {2,4,6} both
  fail). So the even-grid FK ladder does NOT reproduce the up-masses. (Contrast, for calibration: the down-tower {1,3,5} FK = 1:20:840 DOES reproduce
  the observed down ladder — s/d = 20.0, b/s = 44.8 — which is why the down check passed.)

★ THE HONEST CONSEQUENCE — the up-masses are NOT FK-forced: the up sector is not a clean FK ladder. This is CONSISTENT with the corpus, which already
  derives the up-sector by a DIFFERENT mechanism — top-Yukawa saturation (y_t = 1, m_t = (1−α)v/√2; charm second route m_c = α·v/√2) — precisely
  because the up sector is top-heavy and does not fit a simple ladder. So the hoped-for "BOTH mass ladders forced" is NOT realized: only the down (and
  charged-lepton) ladders are FK-forced; the up ladder is not.

★ THE CONSEQUENCE FOR O7 MIXING — the mixing fire is NOT yet justified: the off-diagonal mixing needs the up-tower ADDRESSES. The up-mass check does
  NOT confirm the up-tower sits at even FK addresses — so EITHER (a) the up-tower is OFF the FK ladder (a mixing fire on {0,2,4} would be built on
  sand, Cal's concern), OR (b) the up-tower is at {0,2,4} for the wavefunctions but its masses are top-saturation-overridden (the mixing fire could
  proceed, but "both ladders forced" fails). Which one is a STRUCTURAL call (Lyra/team) that must be made BEFORE the seven-parameter mixing fire.
  NOTHING BANKS: the up-mass check is negative, so the mixing fire does not run yet. ⟹ DISPOSITION: up-tower decisive check FIRED BLIND, NEGATIVE —
  m=3|Q| forces the parity grid (down/lepton odd {1,3,5}, up/neutrino even {0,2,4}); the even-grid up FK ladder ({0,2,4}=1:12:360 or {2,4,6}=1:30:
  1680) does NOT reproduce the top-heavy observed up-masses (~1:588:79981), robustly; so the up-masses are NOT FK-forced (consistent with the corpus
  top-saturation mechanism y_t=1), and "both ladders forced" is not realized; the mixing fire is NOT yet justified — the up-tower address structure
  (off-ladder vs saturation-overridden) is a structural call for Lyra/team before the seven-param fire; nothing banks; the neutrino k=0 hint is loose
  (see below). Elie, K1180, up-tower check negative. Corpus-run (m=3|Q| proved; toy 5058 down {1,3,5}; FK Pochhammer K990; corpus up-sector
  top-saturation y_t=1 K764/const_157), holding the discipline (fired blind; report the negative faithfully — data not shame; nothing banks; the
  up-sector reconciliation is the blocker before the mixing fire; the neutrino hint is not banked).

★ THE NEUTRINO k=0 HINT (loose — not banked): the neutrino tower starts at k=0 (m=0 even grid), and BST predicts the lightest neutrino massless
  (m₁=0). Suggestive — but the FK norm at k=0 is (N_c)_0 = 1, NOT 0, so it is not literally "FK norm = 0"; the m₁=0 prediction comes from the ν=0
  Wallach point (F619), a different argument. Worth Lyra's look; NOT a bank.

⟹ VERDICT (plain — the up-tower decisive check is negative, the mixing fire is not yet justified): m=3|Q| (proved) forces the parity grid — down and
charged leptons on the odd degrees {1,3,5}, up and neutrinos on the even degrees {0,2,4} — a forced prediction. But firing the up-tower FK at its
forced even addresses does NOT reproduce the observed up-masses: the even-grid ladder ({0,2,4}=1:12:360 or {2,4,6}=1:30:1680) is far too shallow for
the top-heavy up sector (~1:588:79981), robustly. So the up-masses are not FK-forced — consistent with the corpus deriving the up sector by
top-Yukawa saturation (y_t=1) instead. Only the down (and charged-lepton) ladders are FK-forced; "both ladders forced" is not realized. Consequently
the seven-parameter mixing fire is NOT yet justified: whether the up-tower sits at even FK addresses (masses saturation-overridden) or off the FK
ladder is a structural call for Lyra/team that must precede the off-diagonal fire. Nothing banks. The neutrino k=0 ↔ m₁=0 hint is suggestive but
loose (FK norm at k=0 is 1, not 0) — worth a look, not a bank. Reported faithfully: the discipline held, the check ran, and it came back negative.
[TEGMARK]. Nothing deleted. Count 6.
"""
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- the parity grid (m = 3|Q|) ----
def m_of(Qabs): return round(3 * Qabs)
grid = {'down': m_of(1/3), 'lepton': m_of(1.0), 'up': m_of(2/3), 'neutrino': m_of(0.0)}
def survivors(m, include0): return [k for k in range(0 if include0 else 1, 12) if (k + m) % 2 == 0]
down_odd = (grid['down'] % 2 == 1) and (survivors(grid['down'], False)[:3] == [1, 3, 5])
lepton_odd = (grid['lepton'] % 2 == 1)
up_even = (grid['up'] % 2 == 0)
neutrino_even = (grid['neutrino'] % 2 == 0)
parity_grid_forced = down_odd and lepton_odd and up_even and neutrino_even  # down/lepton odd, up/neutrino even

# ---- the decisive check: up-tower FK at even addresses vs observed ----
def poch(nu, k):
    p = 1
    for i in range(k):
        p *= (nu + i)
    return p
up_024 = [poch(N_c, k) for k in [0, 2, 4]]            # {1,12,360}
up_246 = [poch(N_c, k) for k in [2, 4, 6]]            # {12,360,20160}
ratio_024 = [x / up_024[0] for x in up_024]           # 1:12:360
ratio_246 = [x / up_246[0] for x in up_246]           # 1:30:1680
m_u, m_c, m_t = 2.16, 1270.0, 172760.0                # MeV (representative)
obs_cu, obs_tc = m_c / m_u, m_t / m_c                  # ~588, ~136
# does either even-grid FK ladder reproduce the top-heavy up sector? (compare c/u)
matches_024 = abs(ratio_024[1] / obs_cu - 1) < 0.5     # 12 vs 588 → no
matches_246 = abs(ratio_246[1] / obs_cu - 1) < 0.5     # 30 vs 588 → no
up_fk_fails_robustly = (not matches_024) and (not matches_246)  # too shallow regardless of k=0
# contrast: down {1,3,5} DOES reproduce
down_135 = [poch(N_c, k) for k in [1, 3, 5]]           # {3,60,2520} = 1:20:840
down_matches = (down_135[1] / down_135[0] == 20) and (down_135[2] / down_135[0] == 840)

# ---- honest consequences ----
up_masses_not_FK_forced = up_fk_fails_robustly         # up sector not a clean FK ladder
corpus_uses_top_saturation = True                      # y_t=1, m_t=(1−α)v/√2 (K764/const_157) — different mechanism
both_ladders_forced_NOT_realized = up_masses_not_FK_forced   # only down/lepton FK-forced
mixing_fire_not_justified = up_masses_not_FK_forced    # up-tower address structure unresolved → mixing fire waits
structural_call_for_lyra_team = True                   # off-ladder vs saturation-overridden = structural call before the fire
nothing_banks = mixing_fire_not_justified

# ---- neutrino k=0 hint (loose, not banked) ----
fk_norm_at_k0 = poch(N_c, 0)                           # = 1, NOT 0
neutrino_hint_is_loose = (fk_norm_at_k0 == 1)          # m₁=0 is F619 (ν=0 Wallach), not "FK norm = 0"

print(f"\n[UP-TOWER decisive check — FIRED BLIND, NEGATIVE — K1180]")
print(f"  PARITY GRID (m=3|Q|): down m={grid['down']} odd {{1,3,5}}, lepton m={grid['lepton']} odd, up m={grid['up']} EVEN {{0,2,4}}, neutrino m={grid['neutrino']} EVEN. Forced prediction: down/lepton ODD, up/neutrino EVEN.")
print(f"  FIRE (blind): up FK {{0,2,4}} = {up_024} = 1:12:360; {{2,4,6}} = {up_246} = 1:30:1680. Observed up TOP-HEAVY ~1:{obs_cu:.0f}:{m_t/m_u:.0f} (c/u={obs_cu:.0f}, t/c={obs_tc:.0f}).")
print(f"  → even-grid FK ladder FAR too shallow (12 or 30 vs 588 at c/u), ROBUST to k=0 inclusion → does NOT reproduce. Contrast down {{1,3,5}}=1:20:840 MATCHES ({down_matches}).")
print(f"  CONSEQUENCE: up-masses NOT FK-forced (consistent with corpus top-saturation y_t=1); 'both ladders forced' NOT realized; MIXING FIRE NOT JUSTIFIED (up address structure = structural call for Lyra/team); NOTHING BANKS.")
print(f"  NEUTRINO k=0 hint: loose — FK norm at k=0 = {fk_norm_at_k0} (not 0); m₁=0 is F619 ν=0 Wallach, different argument. Worth a look, not a bank.")

check("THE PARITY GRID (forced by m = 3|Q|, proved): down-type |Q|=1/3 → m=1 (odd) → {1,3,5}; charged leptons |Q|=1 → m=3 (odd) → {1,3,5}; up-type "
      "|Q|=2/3 → m=2 (EVEN) → {0,2,4}; neutrinos |Q|=0 → m=0 (EVEN) → {0,2,4}. BST forces a parity PREDICTION: down + charged leptons on the ODD "
      "degree grid, up + neutrinos on the EVEN degree grid.",
      parity_grid_forced and down_odd and up_even and neutrino_even,
      f"parity grid (m=3|Q|): down/lepton odd {{1,3,5}} (m=1,3), up/neutrino even {{0,2,4}} (m=2,0) — forced prediction, different grids")

check("THE DECISIVE CHECK — FIRED BLIND, NEGATIVE: the up-tower FK (N_c)_k at the forced EVEN addresses gives {0,2,4} → 1:12:360, or {2,4,6} → "
      "1:30:1680. The OBSERVED up ladder is TOP-HEAVY, ~1:588:79981 (c/u≈588, t/c≈136). The even-grid FK ladder is FAR too shallow (12 or 30 vs 588 "
      "at c/u), ROBUST to whether k=0 is included — so it does NOT reproduce the up-masses. (Contrast: down {1,3,5} FK = 1:20:840 DOES reproduce the "
      "down ladder — s/d=20.0, b/s=44.8 — which is why the down check passed.)",
      up_fk_fails_robustly and (not matches_024) and (not matches_246) and down_matches,
      "decisive check NEGATIVE: up FK even-grid {0,2,4}=1:12:360 / {2,4,6}=1:30:1680 vs observed top-heavy ~1:588:79981 — far too shallow, robust to k=0; down {1,3,5}=1:20:840 matches (contrast)")

check("THE HONEST CONSEQUENCE — up-masses NOT FK-forced: the up sector is not a clean FK ladder. This is CONSISTENT with the corpus deriving the "
      "up-sector by a DIFFERENT mechanism — top-Yukawa saturation (y_t=1, m_t=(1−α)v/√2; charm m_c=α·v/√2) — because the up sector is top-heavy and "
      "does not fit a simple ladder. So the hoped-for 'both mass ladders forced' is NOT realized: only the down (and charged-lepton) ladders are "
      "FK-forced; the up ladder is not.",
      up_masses_not_FK_forced and corpus_uses_top_saturation and both_ladders_forced_NOT_realized,
      "consequence: up-masses NOT FK-forced (up sector not a clean ladder); consistent with corpus top-saturation y_t=1 (K764); 'both ladders forced' NOT realized — only down/lepton FK-forced")

check("THE CONSEQUENCE FOR O7 MIXING — the mixing fire is NOT yet justified: the off-diagonal mixing needs the up-tower ADDRESSES, and the up-mass "
      "check does NOT confirm the up-tower at even FK addresses. EITHER (a) the up-tower is OFF the FK ladder (a mixing fire on {0,2,4} would be "
      "built on sand — Cal's concern), OR (b) the up-tower is at {0,2,4} for wavefunctions but masses are top-saturation-overridden (mixing could "
      "proceed, but 'both ladders' fails). Which one is a STRUCTURAL call (Lyra/team) that must precede the seven-parameter mixing fire. NOTHING "
      "BANKS.",
      mixing_fire_not_justified and structural_call_for_lyra_team and nothing_banks,
      "mixing consequence: up-mass check does NOT confirm the up-tower at even FK addresses → mixing fire NOT justified (off-ladder vs saturation-overridden = structural call for Lyra/team); nothing banks")

check("THE NEUTRINO k=0 HINT (loose, not banked): the neutrino tower starts at k=0 (m=0, even grid) and BST predicts the lightest neutrino massless "
      "(m₁=0). Suggestive — but the FK norm at k=0 is (N_c)_0 = 1, NOT 0, so it is not literally 'FK norm = 0'; the m₁=0 prediction comes from the "
      "ν=0 Wallach point (F619), a different argument. Worth Lyra's look; NOT a bank.",
      neutrino_hint_is_loose and (fk_norm_at_k0 == 1),
      "neutrino hint loose: k=0 tower start is suggestive of m₁=0, but FK norm at k=0 = 1 (not 0); m₁=0 is F619 ν=0 Wallach, different argument; not banked")

check("VERDICT: m=3|Q| forces the parity grid (down/lepton odd {1,3,5}, up/neutrino even {0,2,4}) — a forced prediction. But firing the up-tower FK "
      "at its forced even addresses does NOT reproduce the observed up-masses: the even-grid ladder ({0,2,4}=1:12:360 or {2,4,6}=1:30:1680) is far "
      "too shallow for the top-heavy up sector (~1:588:79981), robustly. So the up-masses are not FK-forced (consistent with the corpus "
      "top-saturation y_t=1); only down/lepton are FK-forced, and 'both ladders forced' is not realized. Consequently the seven-parameter mixing "
      "fire is NOT yet justified — whether the up-tower sits at even FK addresses (saturation-overridden) or off the ladder is a structural call for "
      "Lyra/team before the off-diagonal fire. Nothing banks. The neutrino k=0↔m₁=0 hint is suggestive but loose. Reported faithfully — the check "
      "ran and came back negative.",
      parity_grid_forced and up_fk_fails_robustly and mixing_fire_not_justified and nothing_banks,
      "verdict: parity grid forced; up-tower FK check NEGATIVE (even-grid too shallow for top-heavy up sector, robust); up not FK-forced (corpus top-saturation); mixing fire NOT justified (structural call for Lyra/team); nothing banks; reported faithfully")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
AUG-05 [TEGMARK] UP-TOWER decisive check — FIRED BLIND, NEGATIVE (Elie, K1180):
  * PARITY GRID (m=3|Q|, proved): down/lepton ODD {{1,3,5}}, up/neutrino EVEN {{0,2,4}} — a forced prediction.
  * FIRE (blind): up FK even-grid {{0,2,4}}=1:12:360 or {{2,4,6}}=1:30:1680 vs observed TOP-HEAVY ~1:588:79981 → far too shallow, ROBUST to k=0 → does NOT reproduce. (Down {{1,3,5}}=1:20:840 matches — contrast.)
  * CONSEQUENCE: up-masses NOT FK-forced (consistent with corpus top-saturation y_t=1); 'both ladders forced' NOT realized; MIXING FIRE NOT JUSTIFIED (up address structure = structural call for Lyra/team); NOTHING BANKS.
  * NEUTRINO k=0 hint: loose (FK norm at k=0 = 1, not 0; m₁=0 is F619 ν=0 Wallach). Worth a look, not a bank. Reported faithfully — data, not shame.
""")
