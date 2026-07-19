# K760 — Deriving an anchor for the up-type ladder (Casey directive, after the 2nd negative). The finding: m_u/m_d is a generation CROSSOVER, not a within-doublet ratio — so anchor the up-type ladder independently. **LEAD approach: the TOP anchor (y_t = 1, m_t = v/√2, tied to m_e).** Koide REJECTED (hyper-sensitive, no clean form). Georgi-Jarlskog secondary.

**Keeper | 2026-07-19 | The team returned a clean negative: m_u/m_d isn't a within-doublet quantity (Lyra — a gen-independent doublet split can't flip ordering; the inversion needs the coefficient to cross zero across generations). So derive an ANCHOR, not a ratio. Approaches identified + checked; `anchor_the_up_type_ladder.py`.**

## The reframe (why the negative redirects)
m_u = m_d anchors the *down*-type ladder (s/d = 20 = rank²·n_C banked); m_u floats. But m_u/m_d is a **crossover output** (up/down ratio climbs 0.46 → 13.6 → 41, crossing 1 between gen 1 and 2), so it has no clean closed form — which is *why* several forms fit its loose range (3/7, 1/2, 2/5, √(3/14) — all coincidences). **The fix is to anchor the up-type ladder independently; then m_u/m_d falls out as a derived consequence, not a matched input.**

## ★ LEAD APPROACH — the TOP as the up-type anchor (y_t = 1)
- **y_t = √2·m_t/v = 0.995 ≈ 1** — the top is the *only* O(1)-Yukawa fermion; its mass **is** the electroweak scale, m_t = v/√2 (0.6% from exact). It is the one *un-suppressed* quark — the natural mass anchor.
- **The anchoring chain, all tied to the fundamental anchor m_e:** m_e → v = m_p²/(g·m_e) (banked EW scale) → **m_t = v/√2 (y_t = 1)** → up-type ladder → m_u. So the up-type ladder anchors at the *heavy* end (the top), which is *clean*, rather than the light end (m_u), which is soft.
- **The mass hierarchy, reframed:** the top is O(1); every other quark is the top × a suppression factor. So the derivation splits into (a) **derive y_t = 1** (the top saturates the EW-scale radial moment) and (b) **derive the up-type suppression ladder t → c → u** (the ratios). Then **m_u = m_t / (ladder) is predicted forward**, and it inherits the top's solidity. Grace's clean rungs to build on: m_t/m_b = C₂·g = 42, m_t/m_c ≈ 136.
- **Tier:** the top anchor is strong (y_t ≈ 1 to 0.6%, m_t banked at 0.78%). The open piece is the up-type *slope* (t → c → u), especially the c → u rung where m_u lives. This is the same "up-type is steeper" question, now anchored.

## ✗ REJECTED APPROACH — the Koide relation (checked, doesn't anchor m_u)
The lepton Koide Q = (Σm)/(Σ√m)² = **2/3 = rank/N_c is DERIVED** (corpus: 45° tilt, A² = rank). Tempting to extend to quarks (colored → color-modified A² → a different Q). BUT:
- Up-type Koide Q ≈ **0.849** — no clean derived BST form (6/7 = 0.857 is 1% off; nothing lands on 0.849).
- **The Koide is HYPER-SENSITIVE to Q for m_u:** Q = 6/7 predicts m_u ≈ 0.10 MeV; Q = 2/3 predicts ≈ 20 MeV — a **1% change in Q swings m_u by ~20×** (because m_u is a tiny correction to the m_t/m_c-dominated sum). So even a derived Q can't *pin* m_u. **Koide amplifies m_u's uncertainty rather than anchoring it — reject it for this purpose.** (Good that we checked — Q_up ≈ 6/7 looked clean and would have been the week's next coincidence trap.)

## Secondary — Georgi–Jarlskog / lepton tie (N_c factor)
The GJ pattern (m_d = N_c·m_e, etc. — the factor 3 = N_c = color) ties quark anchors to the *derived* lepton anchor m_e. It's GUT-scale (BST forbids the GUT), but the **N_c-factor pattern** might survive geometrically and anchor the *down*-type to m_e. Secondary to the top anchor; worth a look for the down-type/lepton connection, not the up-type.

## RECOMMENDATION
**Pursue the top anchor.** It's clean (y_t ≈ 1 to 0.6%), standard-physics-motivated (the top is the special un-suppressed fermion), reuses banked BST results (m_t, v = m_p²/(g·m_e)), and anchors the up-type at its solid heavy end. Derivation targets: **(1) derive y_t = 1** (the top mode saturates the EW-scale radial moment — a geometric maximality statement); **(2) derive the up-type suppression ladder** t → c → u (the slope; the c → u rung is the m_u-bearing one). Then m_u is predicted forward and goes solid.
**Discipline:** the up-type ladder ratios have the same loose-range trap (c/u ≈ 577 ± 133, ±23% from m_u) — derive the slope from the geometry, don't match. Koide stays rejected.

— Keeper K760, 2026-07-19. m_u/m_d = crossover (not within-doublet) → anchor the up-type ladder. LEAD: top anchor y_t=1 (m_t=v/√2, 0.6%; chain m_e→v→m_t→ladder→m_u). Derive (1) y_t=1 (top saturates EW scale), (2) the up-type slope t→c→u. Koide REJECTED (hyper-sensitive: 1% Q → 20× m_u; Q_up≈0.849 no clean form). GJ secondary (down-lepton, GUT-scale). See [[Keeper_K759...]], [[Keeper_K757_two_mass_candidate...]].
