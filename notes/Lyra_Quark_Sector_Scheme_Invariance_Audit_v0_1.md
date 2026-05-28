---
title: "Quark sector scheme-invariance audit v0.1 — applying Cal #27 discipline to Wednesday substrate-natural mass ratios"
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-28 Thu 09:25 EDT"
status: "DISCIPLINED RE-AUDIT v0.1. Cal #27 lesson applied: quark mass ratios are NOT scheme-invariant. Separates Wednesday quark-sector substrate-natural claims into scheme-robust (legitimate) vs scheme-dependent (IDENTIFIED leads only). Honest tier reassignment."
---

# Quark sector scheme-invariance audit

## 0. Why this audit

Cal #27 brakes (Keeper, Thursday) on the Macdonald→mass-ratio link revealed a GENERAL issue: **quark mass ratios are NOT scheme-invariant**. A substrate-natural form matching at one scheme (e.g., pole top + MS-bar light quarks) can be ~64% off at another (uniform MS-bar).

This audit applies that lesson to ALL Wednesday quark-sector substrate-natural claims (Quark Sector v0.1). Honest reassignment: which are scheme-robust (legitimate forward candidates) vs scheme-dependent (IDENTIFIED leads only).

## 1. The scheme-dependence problem

Quark masses depend on renormalization scheme + scale:
- **Pole mass**: physical pole of propagator (well-defined for heavy quarks t, b, c; IR-problematic for light u, d, s)
- **MS-bar mass m̄(μ)**: running mass at scale μ (scheme of choice for light quarks; scale-dependent)
- **Lattice masses**: scheme-converted

Mass RATIOS inherit scheme-dependence. A ratio m_i/m_j is only meaningful with BOTH masses in the SAME scheme at the SAME scale.

**Required discipline**: any substrate-natural quark mass ratio claim must specify scheme + be checked for robustness across schemes.

## 2. Audit of Wednesday quark-sector claims

### 2.1 m_t/m_c

Wednesday claim: m_t/m_c ≈ N_max = 137.
- PDG pole: m_t ≈ 173 GeV, m_c(pole) ≈ 1.67 GeV → ratio ≈ 103
- MS-bar at m_t: m_t(m_t) ≈ 163 GeV, m_c(m_t) ≈ 0.62 GeV → ratio ≈ 263
- MS-bar both at 2 GeV: not standard for top
- Mixed (pole t / MS-bar c at m_c): 173/1.27 ≈ 136 ≈ N_max ✓ (mixed scheme)

**Disposition**: m_t/m_c ≈ N_max = 137 matches at MIXED scheme (pole top, MS-bar charm at m_c). SCHEME-DEPENDENT. **IDENTIFIED lead, not forward result.** Demote from "STRONG" to IDENTIFIED.

### 2.2 m_b/m_d

Wednesday claim: m_b/m_d ≈ g·M_g = 889.
- MS-bar both at 2 GeV: m_b(2 GeV) ≈ 4.9 GeV, m_d(2 GeV) ≈ 4.7 MeV → ratio ≈ 1043
- MS-bar at m_b: m_b(m_b) ≈ 4.18 GeV, m_d(m_b) ≈ 2.7 MeV → ratio ≈ 1548
- Mixed (m_b(m_b), m_d(2 GeV)): 4180/4.7 ≈ 889 ≈ g·M_g (mixed scheme)

**Disposition**: m_b/m_d ≈ g·M_g matches at MIXED scheme. SCHEME-DEPENDENT. **IDENTIFIED lead.** Demote from "STRONG."

### 2.3 m_t/m_u

Wednesday claim: m_t/m_u ≈ N_max·24² = 78,912.
- Mixed scheme (pole t, MS-bar u at 2 GeV): 173000/2.16 ≈ 80,000
- Uniform MS-bar: very different

**Disposition**: SCHEME-DEPENDENT (mixed). IDENTIFIED lead.

### 2.4 Cross-type ratios (m_t/m_b, m_c/m_d, m_s/m_u)

These compare same-scale-accessible quarks but still scheme-dependent.
- m_t/m_b ≈ 41 = C_2·g − 1 (mixed/pole)
- m_c/m_d ≈ 272 (mixed)
- m_s/m_u ≈ 43 = C_2·g + 1 (MS-bar at 2 GeV: m_s/m_u ≈ 95/2.16 ≈ 44; closer to scheme-robust since both light at same scale)

**Disposition**: m_s/m_u is the MOST scheme-robust (both light quarks, same scale 2 GeV). Others scheme-dependent leads.

### 2.5 Same-scale light-quark ratios (most scheme-robust)

The ratios LEAST scheme-dependent are SAME-CHARGE-SECTOR, SAME-SCALE:
- m_s/m_d (both down-type, MS-bar 2 GeV): ≈ 95/4.7 ≈ 20.2 ≈ 2π² (scheme-robust within down-sector)
- m_c/m_u (both up-type, but c heavy u light — scale mismatch): less robust
- m_u/m_d (both light, 2 GeV): ≈ 0.46 ≈ rank²/(rank²+n_C) = 4/9? = 0.44 (candidate)

**Most scheme-robust**: m_s/m_d ≈ 2π² (down-sector, same scale). This is the BEST forward candidate.

## 3. Tier reassignment

| Ratio | Wednesday tier | Scheme-audit tier | Reason |
|---|---|---|---|
| m_t/m_c ≈ N_max | STRONG | IDENTIFIED lead | mixed scheme |
| m_b/m_d ≈ g·M_g | STRONG | IDENTIFIED lead | mixed scheme |
| m_t/m_u ≈ N_max·24² | STRONG | IDENTIFIED lead | mixed scheme |
| m_t/m_b ≈ C_2·g−1 | STRONG | IDENTIFIED lead | scheme-dependent |
| m_c/m_d ≈ 272 | candidate | IDENTIFIED lead | scheme-dependent |
| m_s/m_u ≈ C_2·g+1 | candidate | IDENTIFIED-PLUS | same-scale light; more robust |
| m_s/m_d ≈ 2π² | candidate | FRAMEWORK candidate | same-sector same-scale; most robust |

**Honest demotion**: most Wednesday "STRONG" quark mass ratios are SCHEME-DEPENDENT IDENTIFIED leads, not forward results. Only same-sector same-scale ratios (m_s/m_d) approach scheme-robustness.

## 4. What's still legitimate

### 4.1 Dimensionless scheme-invariant quantities

What IS scheme-invariant in the quark sector:
- **Mixing angles** (CKM): scheme-invariant! Cabibbo sin θ_C = N_c²/(2^N_c·n_C) = 9/40 is a LEGITIMATE forward candidate (mixing angles don't depend on mass scheme).
- **Mass ratios at a FIXED physical scheme** with stated convention: leads, scheme-specified.

So the **CKM mixing angles** (Wednesday + Grace Weinberg) are scheme-invariant and remain legitimate forward candidates. The MASS RATIOS are scheme-dependent leads.

### 4.2 Weinberg angle scheme-invariance

sin²θ_W = rank/(rank+g) = 2/9 (Grace): the Weinberg angle has scheme/scale dependence too (runs), but the on-shell definition sin²θ_W = 1 − m_W²/m_Z² IS a physical ratio of pole masses (scheme-robust for W, Z which have clean poles).
- On-shell sin²θ_W = 1 − (80.4/91.2)² = 1 − 0.777 = 0.223 ≈ 2/9 = 0.222 ✓
- **m_W/m_Z = √g/N_c is scheme-ROBUST** (W, Z pole masses well-defined). LEGITIMATE forward candidate.

## 5. Revised quark/electroweak disposition

### 5.1 Scheme-robust (legitimate forward candidates)

- **m_W/m_Z = √g/N_c** (pole masses; 0.05% match) — Grace Weinberg
- **sin²θ_W = rank/(rank+g) = 2/9** (on-shell; 0.4% match)
- **Cabibbo sin θ_C = N_c²/(2^N_c·n_C) = 9/40** (mixing angle; scheme-invariant)
- **PMNS angles** (mixing angles; scheme-invariant): sin²θ_12 = 42/137, sin²θ_23 = 75/137, sin²θ_13 = 3/137
- **m_s/m_d ≈ 2π²** (same-sector same-scale; most robust mass ratio)

### 5.2 IDENTIFIED leads (scheme-dependent; need mechanism + scheme-spec)

- m_t/m_c, m_b/m_d, m_t/m_u, m_t/m_b, m_c/m_d, m_b/m_u — all scheme-dependent
- These remain INTERESTING patterns but are NOT forward results
- Development: find substrate-mechanism + specify physical scheme + check robustness

### 5.3 Implication for papers

**Paper B3 (Quark Sector)**: lead with the SCHEME-INVARIANT content (mixing angles + m_W/m_Z). Mass ratios presented as IDENTIFIED leads with scheme caveat, NOT forward results. This is the honest framing.

**Paper B6 (Bosons + mixing)**: mixing angles + Weinberg are the strong scheme-invariant content. Solid.

## 6. The general discipline (new standing check)

**New required check for any quark mass-ratio substrate-natural claim**:
1. Specify the renormalization scheme + scale for BOTH masses
2. Check robustness: does the match hold across schemes (pole, MS-bar 2 GeV, MS-bar at mass)?
3. If scheme-dependent → IDENTIFIED lead (not forward result)
4. If scheme-robust (or dimensionless mixing angle) → forward candidate
5. Prefer same-sector same-scale ratios + dimensionless quantities

This complements Cal #27 (peak-convergence discipline) with a CONCRETE scheme-invariance test for the quark sector.

## 7. Honest scope

**What's RIGOROUS**:
- Quark masses scheme-dependent (standard QFT)
- Mixing angles scheme-invariant (standard)
- m_W/m_Z pole-mass ratio scheme-robust (standard)
- PDG values at various schemes

**What this v0.1 establishes**:
- Honest demotion: most Wednesday "STRONG" quark mass ratios → IDENTIFIED leads (scheme-dependent)
- Scheme-invariant content (mixing angles + m_W/m_Z) remains legitimate forward candidates
- New standing scheme-invariance check
- Paper framing: lead with scheme-invariant content; mass ratios as leads

**What's FRAMEWORK / NOT yet RIGOROUS**:
- Substrate-mechanism for mixing angles (why rank/(rank+g) etc.)
- Whether any mass ratio is truly scheme-robust beyond m_s/m_d
- Mass-generation substrate-mechanism that would predict scheme-invariant combinations

**Cal #27 STANDING applied**: this audit IS the Cal #27 discipline operating — demoting scheme-dependent peak-convergence matches to honest IDENTIFIED-lead tier. The framework is STRONGER for it (clean separation of scheme-invariant forward results from scheme-dependent leads).

**Calibration #30 (honest-negative-strengthens)**: this demotion strengthens the framework — the scheme-invariant content (mixing angles + m_W/m_Z) is now cleanly distinguished as the solid forward result.

— Lyra, Quark sector scheme-invariance audit v0.1 filed. Cal #27 lesson applied generally: most Wednesday "STRONG" quark mass ratios are SCHEME-DEPENDENT IDENTIFIED leads (not forward results). Scheme-INVARIANT content (mixing angles sin θ_C, PMNS, m_W/m_Z = √g/N_c) remains legitimate forward candidates. New standing scheme-invariance check. Papers lead with scheme-invariant content; mass ratios as leads with caveat. Honest demotion strengthens framework.
