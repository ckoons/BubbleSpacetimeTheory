---
title: "Quark mass spectrum substrate decomposition attempt v0.1 — HONEST RESULT: quark masses NOT cleanly substrate-decomposable at lepton-precision level. Scheme-dependence + bulk-color mechanism open create barriers. CKM angles ARE clean (sin θ_C = N_c²/(2^{N_c}·n_C) = 9/40 at 0.3%). Best quark-mass-ratio matches: m_b/m_c ≈ rank·n_C/N_c (1.2% off); m_t/m_b ≈ C_2·g-1 (0.6% off). Lepton-style closed forms blocked on bulk-color."
author: "Lyra (Claude Opus 4.7)"
date: "2026-05-30 Saturday 11:50 EDT (date-verified)"
status: "QUARK MASSES v0.1 (depth-shift extension per Casey 'then quark mass spectrum'). HONEST FINDING: quark mass ratios NOT cleanly substrate-decomposable at the precision T190/T2003 achieve for leptons. Best matches at 1-2% precision (m_b/m_c ≈ rank·n_C/N_c; m_t/m_b ≈ C_2·g−1). CKM angles ARE clean (sin θ_C = 9/40 substrate-natural at 0.3%). Quark mass mechanism likely needs bulk-color resolution + scheme-invariance handling first."
---

# Quark mass spectrum substrate decomposition attempt v0.1

## 0. Per Casey's directive sequence

After lepton masses (T190, T2003) substrate-decomposed and OTHER lepton observables (Schwinger a_e = 1/(2π·N_max), muon decay 192 = N_c·2^{C_2}) decomposed, the next item is quark mass spectrum.

## 1. The structural obstacle — scheme dependence

Quark masses are SCHEME-DEPENDENT in QCD:
- MS̄-bar quark masses (running, scheme-defined).
- Pole quark masses (gauge-invariant but with renormalon ambiguity).
- Constituent quark masses (effective, model-dependent).

PDG values (MS̄-bar at appropriate scales):
- m_u ≈ 2.16 MeV (at 2 GeV).
- m_d ≈ 4.67 MeV.
- m_s ≈ 93.4 MeV.
- m_c ≈ 1.27 GeV.
- m_b ≈ 4.18 GeV.
- m_t ≈ 172.57 GeV (pole, more well-defined).

The scheme-dependence + the bulk-color mechanism still open create real barriers. Cal #27 from Friday + BST's quark sector scheme-invariance audit (#218) already flagged scheme-dependent quark mass leads as excluded from forward derivations.

## 2. CKM angles (scheme-invariant) — ARE substrate-clean

Cabibbo angle:

  **sin θ_C = N_c² / (2^{N_c} · n_C) = 9/40 = 0.225** vs observed 0.2243 (**0.31% match**)

Substrate-decomposition: 9 = N_c² (color squared); 40 = 2^{N_c} · n_C = 8 · 5 (Mersenne base raised to color, times complex dim). All substrate-primary.

This matches the pattern from lepton work: substrate primaries with rank/Mersenne base raised to primary exponents.

Other CKM angles also have substrate-natural fractions over N_max (PMNS-like; from F1 falsifier work):
- |V_us| ≈ sin θ_C ≈ 0.225 = 9/40 = N_c²/(2^{N_c}·n_C). Clean.
- |V_cb| ≈ 0.041 (smaller). Substrate decomposition multi-week.
- |V_ub| ≈ 0.004 (smallest). Substrate decomposition multi-week.

## 3. Quark mass-ratio attempts — best matches at 1-2% precision

| Quark mass ratio | Observed | Best substrate candidate | Match |
|---|---|---|---|
| m_u/m_d | 0.463 | 1/rank = 0.5 | 8% off |
| m_d/m_u | 2.16 | rank + 1/(rank+1) | not clean |
| m_s/m_d | 20.0 | n_C·g/rank·... | various 5-15% |
| m_c/m_s | 13.6 | (no clean match) | — |
| **m_b/m_c** | **3.29** | **rank·n_C/N_c = 10/3 = 3.33** | **1.2% off** |
| **m_t/m_b** | **41.26** | **C_2·g - 1 = 41** | **0.6% off** |

The best matches (m_b/m_c, m_t/m_b) are at 1-2% precision — substantially worse than T190's 0.004% or T2003's 0.05%. The substrate-primary candidates are SUGGESTIVE but not PRECISE in the way lepton ratios are.

Possible reasons:
1. **Scheme dependence**: quark masses depend on renormalization scheme; substrate-natural derivation requires specifying scheme (typically MS̄-bar). The 1-2% precision might match the scheme-uncertainty.
2. **Bulk-color mechanism**: quarks are bulk K-types with color; their masses involve bulk-color structure not yet derived. Substrate-natural decomposition likely BLOCKED on bulk-color resolution.
3. **Different mass mechanism**: quarks may use different substrate-natural mechanisms than leptons (boundary vs bulk; different channel structures).

## 4. Cross-sector ratios (quark-lepton)

Cross-sector mass ratios involve substantially different mechanisms (boundary vs bulk).

- m_t/m_e ≈ 338,000. log₂ ≈ 18.4. No clean substrate-primary integer match.
- m_b/m_e ≈ 8,180. log₂ ≈ 13. No clean match.
- m_c/m_e ≈ 2,488. log₂ ≈ 11.3. No clean match.

Cross-sector lepton-quark ratios don't fit a simple closed-form pattern. The lepton sector (T190, T2003 family) and quark sector use different substrate-natural mechanisms.

## 5. Substrate-natural quark observables identified so far

| Observable | Substrate form | Match | Sector |
|---|---|---|---|
| sin θ_C (Cabibbo) | N_c²/(2^{N_c}·n_C) = 9/40 | 0.3% | CKM (scheme-invariant) |
| m_b/m_c (suggestive) | rank·n_C/N_c = 10/3 | 1.2% | MS̄-bar (scheme-dependent) |
| m_t/m_b (suggestive) | C_2·g − 1 = 41 | 0.6% | MS̄-bar (scheme-dependent) |
| m_p/m_e (bulk composite) | C_2·π^{n_C} = 6π⁵ | 0.002% (T187) | bulk composite |

The CLEANEST quark-sector substrate decompositions are CKM angles + bulk composites (proton). Individual quark mass ratios show 1-2% suggestive matches but not lepton-precision clean closed forms.

## 6. What would unlock cleaner quark mass derivation

The bulk-color mechanism resolution (currently multi-week open, my v0.5+v0.6 work) is the LIKELY KEY: with explicit bulk-color SU(3)/Toeplitz structure, quark masses would have:
- Color-octet gauge contributions (8-gluon adjoint).
- Bulk K-type radial structure with color-dependent kernel integrals.
- Substrate-natural exponents tied to color sector (vs. lepton's spinor sector).

Multi-week target after bulk-color closure verification.

## 7. Honest scope + tier

**RIGOROUS** (existing + arithmetic):
- PDG quark masses (scheme-dependent).
- Cabibbo angle decomposition sin θ_C = 9/40 = N_c²/(2^{N_c}·n_C) at 0.3% (existing BST).
- Various 1-2% suggestive matches for m_b/m_c, m_t/m_b.
- m_p/m_e = 6π⁵ (T187, bulk composite, clean).

**HONEST FINDING (v0.1)**: quark mass RATIOS NOT cleanly substrate-decomposable at lepton-precision level. Best matches at 1-2% precision (m_b/m_c ≈ rank·n_C/N_c; m_t/m_b ≈ C_2·g − 1). CKM angles (sin θ_C) ARE clean. Bulk-color mechanism resolution likely needed for explicit quark mass derivation.

**OPEN (multi-week)**: bulk-color mechanism resolution; scheme-invariance handling; explicit quark mass derivation via bulk K-type structure with color.

**Cal #27 / honesty**: NOT claiming quark mass ratios are substrate-decomposed. Honest finding: lepton-precision closed forms NOT available for quarks at v0.1; scheme-dependence + bulk-color blocking. Suggestive 1-2% matches noted as candidates for further investigation but NOT promoted to clean closed forms. CKM angles ARE clean (per existing BST). The structural picture: lepton sector and quark sector have different substrate-natural mechanisms; quark sector mechanisms blocked on bulk-color.

**Routed**: → Casey: quark mass derivation is the next major depth target but is blocked on bulk-color mechanism resolution. CKM angles cleanly substrate-derived. Suggestive m_b/m_c ≈ rank·n_C/N_c and m_t/m_b ≈ C_2·g − 1 noted but unpromoted. → Elie: when bulk-color mechanism resolves (multi-week), quark mass derivations via bulk K-type radial tower + color structure become accessible. → Grace: catalog candidate m_b/m_c ≈ 10/3 and m_t/m_b ≈ 41 as suggestive substrate candidates with 1-2% precision (lower-tier than lepton closed forms). → me: next per Casey's "keep going" — hadron spectrum or gauge bosons.

— Lyra, quark mass spectrum v0.1. HONEST FINDING: quark mass ratios NOT cleanly substrate-decomposable at lepton-precision level. Scheme-dependence + bulk-color open create barriers. CKM angles ARE clean (sin θ_C = 9/40 = N_c²/(2^{N_c}·n_C), 0.3%). Suggestive 1-2% matches for m_b/m_c ≈ rank·n_C/N_c and m_t/m_b ≈ C_2·g−1 noted as candidates. Lepton-style closed forms blocked on bulk-color resolution; multi-week target.
