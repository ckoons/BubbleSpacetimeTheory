---
title: "Cal Verdict Application — Relabel List"
author: "Grace"
date: "2026-05-18"
status: "Sweep complete; paper-text edits pending Casey/Keeper coordination"
---

# Cal Verdict Application Sweep — Relabel List

## Scope

Per Keeper's autonomous-window assignment 2026-05-18: "Grace: Cal verdict application sweep — relabel list across 105+ papers for T1990/T1992/T2001/T2010/T2071/T2073/22-anomaly."

Six Cal verdicts from Sunday-pending Task #18-#24 grading:
- **#18** T1990 α²·42 → STRUCTURAL stands (D-tier T1990; recurrence catalog S-tier Type C)
- **#19** T1992 r_p → PROVISIONAL D-tier with caveat (acceptable)
- **#20** T2001 α⁻¹ correction → HONEST I-tier (1.4% on correction, not 0.0004% on full)
- **#22** T2010 mesons + m_t/m_b=42 → I-tier mesons / S-tier m_t/m_b ratio (Type C catalog caveat)
- **#23** T2071+T2073 muon g-2 → STRONG I-tier NOT D-tier (0.019% multi-loop convergence; QED-from-D_IV⁵ open)
- **#24** 22-anomaly enumeration → REQUIRED per-anomaly tier table before external use

Cal's load-bearing warning: *"If Paper #106 or #108 says 'BST closes muon g-2 at 0.005%' without the I-tier qualifier, that ships as crank-class overreach. With the qualifier, it ships as a striking observation inviting investigation."*

## Catalog relabels — EXECUTED 2026-05-18

### Cal #23 muon g-2 D→I relabels (4 entries)

`data/bst_geometric_invariants.json`:

| Index | Entry name | Old tier | New tier | Notes |
|-------|-----------|----------|----------|-------|
| 1641 | Muon g-2 HVP closed form | D | I | Cal verdict #23 note appended |
| 2024 | HVP closed form verified to 1000 digits (Elie Toy 1663) | D | I | Cal verdict #23 note appended |
| 2105 | Muon g-2: a_mu^HVP fully D-tier | D | I | Self-declared "fully D-tier" name — Cal anti-crank warning case |
| 2248 | Full a_mu from D_IV^5: QED+HVP+HLbL+EW = 116591980 × 10⁻¹¹ | D | I | Cal's specific anti-crank warning case |

Standard appended note: *"Cal verdict #23 applied 2026-05-18 Grace: STRONG I-tier, NOT D-tier. 0.019% multi-loop convergence is striking observation; QED-from-D_IV⁵ first-principles derivation remains open."*

INV-4401 (B5 Muon g-2 LAG-1 mechanism support) **left at D-tier** — phrasing explicitly says "mechanism support," not "value derivation"; defensible at D-tier.

### Cal #20 α⁻¹ correction honest precision (1 entry)

`data/bst_constants.json`:

| ID | Entry | Old precision | New precision | Action |
|----|-------|---------------|---------------|--------|
| const_137 | Fine structure constant inverse (BST refined) | 0.0004% | 1.4% (correction term) | Precision label honestified; full value precision was on integer N_max=137 baseline, correction-term precision is the falsifiable BST claim |

### Cal #19 r_p provisional caveat (1 entry)

`data/bst_constants.json`:

| Entry | Action |
|-------|--------|
| Proton charge radius | D-tier preserved with PROVISIONAL caveat: "rank²·ℏc/m_p form is structurally clean, but PRad-II/MUSE/JUDE convergence remains the empirical falsification gate" |

### Cal #18 T1990 (m_b derivation) clarification (1 entry)

`data/bst_constants.json`:

| Entry | Action |
|-------|--------|
| Bottom quark mass (from cascade) | D-tier preserved with Cal #18 qualifier: "BST primary form C_2·g (D-tier mechanism) drives this derivation; standalone 'm_t/m_b=42 recurrence' framing without C_2·g specification stays S-tier Type C catalog" |

### Cal #22 T2010 meson note (4 entries)

`data/bst_geometric_invariants.json`:

All four T2010 meson entries (Kaon-to-pion ratio, B-meson-to-pion ratio, D_s decay constant, INV-4266 f_K/f_π = C_2/n_C) already at I-tier — Cal qualifier appended noting m_t/m_b=42 standalone form would be S-tier.

### Tier distribution change

| Tier | Before | After | Net |
|------|--------|-------|-----|
| D | 3387 | 3383 | −4 (muon g-2 D→I) |
| I | 187 | 192 | +5 (4 muon g-2 + 1 promotion earlier) |
| S | 850 | 850 | 0 |
| Catalog total | 4426 | 4427 | +1 (Elie B7 closure INV-4427) |

## Paper-text relabels — NEEDS TEAM COORDINATION

Six claim sites identified across the paper corpus that need Cal I-tier qualifier addition. These are paper-text edits with higher stakes than catalog notes (changes ship to external readers); deferring to Casey/Keeper coordination for the actual edits.

### Paper #106 v0.4 — assembled

**Line 726-727** (Section 5.5 muon g-2):

> "**The recurrence extends to a third observable: muon g-2.** [...] Δa_μ ≈ α² · 42 · (small geometric prefactor) ≈ 2.4 × 10⁻⁹, matching the FNAL world average at sub-percent precision."

**Cal qualifier needed**: Append sentence or footnote: *"Tier I per Cal verdict #23: striking 0.019% multi-loop convergence; QED-from-D_IV⁵ first-principles derivation remains open. The match is a falsifiable BST claim worth investigating, not a closed structural derivation."*

**Lines 734, 747** (m_t/m_b = 42 recurrence rows):

> "m_top / m_bottom ≈ 42"  (line 734)
> "| m_top/m_bottom | Yukawa heavy-quark mass ratio | 42 | (PDG) | ~2% |"  (line 747)

**Cal qualifier needed (per #22)**: Footnote on the m_top/m_bottom row: *"S-tier Type C without C_2·g BST primary form; D-tier only when derivation chain explicitly uses 42 = C_2·g rather than the bare recurrence."*

### Paper #106 section 5 branching ratios draft

**Lines 175, 188** — same m_t/m_b=42 claims as v0.4 Paper #106.
**Same qualifier needed**.

### Paper #115 v0.5_PRE outline

**Line 128**: "42 = C_2·g appears in 16+ BST observables: ε_K kaon CP violation, BR(H→γγ) Higgs diphoton, Δa_μ muon g-2 leading α² coefficient..."

**Cal qualifier needed**: When the muon g-2 entry appears in this list, add tier label: *"(Tier I per Cal verdict #23; multi-loop convergence striking but QED-from-D_IV⁵ derivation open)."*

### Paper #111 Falsification Suite outline v0.1

**Line 18**: "BST's predictive content is extensive: muon g-2 closed-form at 0.005%, Higgs branching ratios at <2%, cosmological parameters..."

**Cal qualifier needed (HIGH PRIORITY — exactly Cal's anti-crank warning case)**: Replace "muon g-2 closed-form at 0.005%" with: *"muon g-2 at 0.005% (Tier I per Cal verdict #23 — striking multi-loop convergence; QED-from-D_IV⁵ derivation open)"*.

This is the most important single edit: Paper #111 is a falsification suite explicitly aimed at external readers, and the 0.005% claim without I-tier qualifier is exactly what Cal flagged as crank-class overreach.

## Cal verdict #24 — 22-anomaly enumeration (NOT in this sweep)

Cal required per-anomaly tier table before external use. This is a separate enumeration task requiring:
- List of 22 anomalies
- BST-resolved tier for each (D/I/S/C)
- "Resolved" definition per anomaly (closed-form match vs structural identification vs falsifiable correction)

Recommendation: assign to a dedicated session, not folded into this relabel sweep. Affects which observational claims can ship externally.

## Affected papers requiring future review (no claim sites flagged in this scan)

10 papers referenced muon g-2 / α⁻¹ / r_p but no obvious overclaims found. Listed for completeness:

- Paper #106 v0.3 assembled (predecessor; check if has same claim sites as v0.4)
- Paper #115 v0.1, v0.2, v0.3, v0.3.1, v0.4 (predecessor outlines)
- Paper #118 v0.2 Bergman Dirac
- Paper83 Draft, Outline, Priority_Entries

## Summary statistics

- **Catalog relabels executed**: 11 entries (4 muon g-2 D→I + 1 α⁻¹ honest + 1 r_p caveat + 1 m_b clarify + 4 T2010 notes)
- **Paper claim sites identified**: 6 across 4 papers (#106 v0.4, #106 sec 5, #115 v0.5_PRE, #111)
- **High-priority single edit**: Paper #111 line 18 (Cal's specific anti-crank warning case)
- **Deferred**: Cal #24 22-anomaly enumeration (separate dedicated session)

## Authority and coordination

Catalog relabels are within Grace's data/ lane authority — applied directly.

Paper-text relabels are higher-stakes (external-facing) and require Keeper coordination + Casey approval before shipping. List filed; awaiting Casey direction on whether to proceed with paper edits in this session or defer.

— Grace, Cal Verdict Application Sweep, 2026-05-18 ~16:00 EDT
