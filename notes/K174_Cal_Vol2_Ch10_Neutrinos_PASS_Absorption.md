# K174 — Cal Vol 2 Ch 10 (Neutrinos) PASS Absorption + Formula Flags

**Filed**: 2026-05-22 Friday 12:48 EDT (Keeper, `date`-verified actual)
**Status**: ABSORPTION — Cal Vol 2 Ch 10 PASS chapter-grade with 2 substantive formula flags for Elie v0.4 correction
**Mode**: Cal cold-read absorption per Vol 2 cold-read sweep (Cal #96)

---

## Cal verdict (Cal #96, Friday afternoon)

**PASS chapter-grade for textbook v1.0** with 2 substantive formula flags + Mode 5 coordinate-specificity caution.

### Substantive PASS items (Cal verified)

- **Seesaw = 17 BST primary identification**: M_R ~ 10^17 GeV order-of-magnitude D-tier identification honest
- **Right-handed neutrinos as substrate-internal high-K-type modes** (NOT low-energy sterile neutrinos) — clean substrate-mechanism framing consistent with **Absence 5 (no sterile neutrinos at low energy)** of Casey-named Five-Absence Predictions Set
- **Casimir formula** (line 118): C(μ_1, μ_2) = μ_1(μ_1+5) + μ_2(μ_2+3) with ρ=(5/2, 3/2) — Cal verified ρ as B₂ half-sum of positive roots, consistent with Vol 1 Ch 5 derivation
- **Three experimental cross-checks** (KATRIN < 0.8 eV; Cosmological Σm_ν < 0.12 eV; 0νββ KamLAND-Zen + next-gen sensitivity)
- **Section 5.5 0νββ near-term falsifier** (lines 171-174): concrete falsifiability anchor with sensitivity-tier specification (LEGEND, nEXO, CUPID-1T era at ~10⁻³ eV)
- **Line 102 honest tier discipline preserved**: "D-tier identification on the order-of-magnitude scale; I-tier on the specific decimal value within the order of magnitude." Mode 1 discipline applied.
- **Cross-reference T2441 + T2442 + T2439**: uses Lyra Strong-Uniqueness v0.10.5 FORMAL canonical (consistent state across volumes)

## Cal substantive flags requiring Elie v0.4 correction

### Flag 1: Line 81 substrate-energy cap formula order-of-magnitude error

**Stated formula**: E_sub ~ m_e · α^(-seesaw) ~ m_e · N_max^17 gives substrate-energy scale ~10^17 GeV order-of-magnitude

**Cal arithmetic**: m_e · 137^17 = 0.511 MeV × 10^36.3 ≈ 5 × 10^33 GeV, **NOT 10^17 GeV. Off by 16 orders of magnitude.**

**Issue**: The seesaw = 17 ↔ 10^17 GeV identification is at the **log10 level** (seesaw integer literally equals the exponent of energy scale in GeV), NOT via N_max^17 exponentiation. The formula as written is mathematically incorrect (or symbolic but unmarked).

**Required fix** (Elie v0.4): either
- Correct the formula to reflect the actual identification (seesaw=17 ↔ log10(M_R/GeV) = 17), OR
- Annotate "symbolic identification: seesaw=17 ↔ 10^17 GeV via order-of-magnitude marker, not literal m_e·N_max^17 exponent"

Per Calibration #21 STANDING RULE: K-audit ratification needs both empirical + substrate-mechanism closure. A formula that doesn't evaluate to the claimed result fails substrate-mechanism closure even if the underlying identification is sound.

### Flag 2: Line 161 m_β formula hidden suppression

**Stated formula**: m_β ~ m_e × (rank/seesaw²) ≈ 1.4 × 10⁻³ eV with substrate-natural suppression

**Cal arithmetic**: m_e × rank/seesaw² = 0.511 MeV × 2/289 = 3.5 keV, **NOT 1.4 × 10⁻³ eV. Off by 6 orders of magnitude.**

**Issue**: "With substrate-natural suppression" phrase implies additional unspecified suppression factor (~2.5 × 10⁻⁶) needed to reach 1.4 × 10⁻³ eV. Hidden math — reader-grade ambiguity.

**Required fix** (Elie v0.4): either
- Show the full suppression chain (what's the ~2.5 × 10⁻⁶ factor? K-type quenching? Casimir-eigenspace projection? Bergman kernel asymptote?), OR
- Annotate "schematic relation; full suppression chain pending operator-level Elie K52a Sessions multi-month"

Per Cal #92(b) discipline + Calibration #21: hidden-math formulas don't reach RIGOROUSLY CLOSED. Either explicit or annotated as schematic.

### Cal Mode 5 caution (NOT a flag, but worth noting)

**Observation**: seesaw = 17 BST primary identification is at log10(energy_GeV) = 17 — i.e., the BST primary integer "17" matches the exponent of the energy scale in GeV. Reasonable structural identification.

**Mode 5 selection-of-units risk**: if energy were measured in TeV instead of GeV, the exponent would be 14 not 17. The framing is GeV-coordinate-specific.

**Doesn't invalidate** the substrate-mechanism claim but worth flagging as honest-scope item per Cal Mode 5 discipline. Elie may add a footnote acknowledging GeV-coordinate-specificity of the log10-level identification.

## Vol 2 cold-read sweep progress (Cal cumulative)

After Cal #96 (Ch 10):
- ✓ Ch 1 Introduction PASS (Cal #93 — 8+ stale refs → Elie U2)
- ✓ Ch 2 SM Gauge Group PASS (Cal #94 — stale-state items + sin²θ_W cross-volume → Lyra U1 ✓ DONE + Elie U3+U4)
- ✓ Ch 3 Three Generations PASS (Cal #95 — multiple mass-hierarchy flags → Elie U5+U6+U7+U8)
- ✓ Ch 6 m_p/m_e CROWN JEWEL PASS (Cal Friday — 2 minor flags → Lyra U9 ✓ DONE)
- ✓ Ch 9 Higgs (absorbed via K166 + K172)
- ✓ **Ch 10 Neutrinos PASS** (Cal #96 — 2 substantive formula flags → Elie U10+U11; Mode 5 caution)
- **Ch 11 Five Absences next** (Cal in flight)
- Ch 4 Color/Quarks: pending Cal
- Ch 5 Lepton Sector: pending Cal
- Ch 7 CKM Mixing: pending Cal
- **Ch 8 Coupling Constants CROWN JEWEL #2**: pending Cal (a_e ppt expected highlight)
- Ch 12 Experimental Program: pending Cal

**6 of 12 Vol 2 chapters absorbed/PASS.** Cal cadence sustained ~5-10 min/chapter.

## Add to CI_BOARD NEW VOL 2 PAPER UPDATES section

| # | File | Update | Owner | Est |
|---|------|--------|-------|-----|
| **U10** | Vol 2 Ch 10 line 81 | Substrate-energy cap formula: either correct E_sub formula or annotate as symbolic log10 identification (Cal Flag 1) | Elie | 5-10 min |
| **U11** | Vol 2 Ch 10 line 161 | m_β suppression chain: show full ~2.5×10⁻⁶ factor or annotate schematic pending K52a Sessions (Cal Flag 2) | Elie | 5-15 min |
| **U12** | Vol 2 Ch 10 | Optional: Cal Mode 5 footnote acknowledging GeV-coordinate-specificity of seesaw=17↔10^17 identification | Elie | 2-5 min |

**Total estimated Vol 2 Ch 10 cleanup**: ~12-30 min Elie.

## Cumulative Vol 2 cleanup queue (all chapters, post-Cal-flags):

- U1 Vol 1 Ch 11 sin²θ_W tier — DONE Lyra Friday 12:44
- U2 Vol 2 Ch 1 stale refs — pending Elie (~15-30 min)
- U3+U4 Vol 2 Ch 2 stale-state — pending Elie (~4 min)
- U5 Vol 2 Ch 3 T190 precision — pending Elie (~5 min)
- U6+U7 mass-ratio dual-formula — Lyra reconciliation note DONE; Elie prose update pending (~15 min)
- U8 Vol 2 Ch 3 tier-label — pending Elie (~10 min)
- U9 Vol 2 Ch 6 — DONE Lyra Friday afternoon
- U10+U11+U12 Vol 2 Ch 10 (NEW per Cal #96) — pending Elie (~12-30 min)
- Future U13+ as Cal completes Ch 4, 5, 7, 8, 11, 12

**Net Elie absorption queue**: ~60-110 min sustained Vol 2 reader-grade cleanup. Vol 2 reaches Vol 1-equivalent reader-grade content state when complete.

## F1-F4 (absorption)

- F1 Cal Ch 10 PASS chapter-grade + 2 substantive flags + Mode 5 caution + honest tier discipline preserved: 3.95/4
- F2 seesaw=17 + M_R~10^17 + Casimir μ_1(μ_1+5)+μ_2(μ_2+3) + 0νββ falsifier + Five-Absence consistency cross-paths: 3.95/4
- F3 cross-lane (Cal sustained Vol 2 sweep + Elie Vol 2 absorption queue + Five-Absence consistency): 3.95/4
- F4 falsifier 0νββ near-term (LEGEND, nEXO, CUPID-1T) verifiable: 4.0/4

**F1-F4: 15.85/16 = 3.96/4 STRONG**

## K174 status

**K174 Cal Vol 2 Ch 10 Neutrinos PASS absorbed.** Substantive 0νββ falsifier + seesaw=17 identification + substrate-internal high-K-type modes framing all clean. Two formula flags routed to Elie v0.4 (U10+U11). Mode 5 GeV-coordinate caution optional Elie footnote (U12).

Per Calibration #21 STANDING RULE: hidden-math formulas (Flag 1 + Flag 2) don't reach RIGOROUSLY CLOSED — either explicit or annotated as schematic. Elie absorption closes the gap.

Vol 2 sweep continues at sustained Cal cadence; Ch 11 next.

— Keeper, K174 Cal Vol 2 Ch 10 PASS Absorption, Friday 12:48 EDT (`date`-verified actual)
