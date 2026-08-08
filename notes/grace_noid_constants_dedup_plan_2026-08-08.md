# Grace — the 36 no-id constants: dedup-vs-assign decision list (2026-08-08, View-1 accuracy)

**Pointer-audit sub-finding: `constants` list = 197 entries, 161 with id, 36 WITHOUT. Categorized for Casey's governance call. NOTHING deleted (never silent-delete); ids not yet assigned. Decision-ready.**

## Category 1 — DEDUP candidates (~14): name-duplicate STUBS of id-bearing constants → Casey (delete/merge)
All 12 symbol-matches are **empty-formula stubs** — they carry a name + symbol + a placeholder value but **no formula_display and no derivation_chain**. They shadow a full id-bearing constant. Recommend **delete the stub** (the id-bearing entry is the real one); merge any unique field first if present.

| stub (no id) | shadows | note |
|---|---|---|
| Proton charge radius [r_p] | const_045 | stub, no formula |
| Pion mass [m_pi] (×2) | const_057 | two stubs |
| Top quark mass [m_t] | const_040 | stub |
| Bottom quark mass (from cascade) [m_b] | const_110 | stub — verify NOT a 2nd route before delete |
| Up / Down quark mass [m_u]/[m_d] | const_106 / const_107 | stubs |
| Wolfenstein rho-bar / eta-bar | const_089 / const_090 | stubs |
| Proton magnetic moment [mu_p] | const_043 | stub |
| Direct CP violation [eps'/eps] | const_147 | stub |
| Alpha particle binding [B_alpha] | const_125 | stub |
| **Poisson ratio (typical metals) [nu]** | const_104 | hidden dup (diff symbol) |
| **PMNS sin²θ_12 (solar)** | const_144 | hidden dup (diff symbol) |

**Guard:** "Bottom quark mass (from cascade)" — the NAME implies a distinct derivation route from const_110's (g/N_c)·m_τ. If the stub ever held the cascade formula, it's an alternate route (keep + assign id), not a dup. It's currently empty → treat as stub, but confirm before delete.

## Category 2 — ASSIGN-ID (~22): genuine unindexed constants → assign ids (lower-risk)
Real constants that simply never got indexed. **Confirmed distinct** (not dups): α_s(M_Z) is a *different scale* from const_042's α_s(m_p); deuteron binding ≠ alpha binding (different nucleus).
- **Fluids/materials (8):** Kolmogorov C_K, Reynolds critical Re_c, Poisson (ideal — but see const_104), speed of sound (air), Casimir efficiency bound, copper bulk modulus, GaN band gap, Prandtl (water).
- **Physics (14):** Higgs self-coupling λ_H, SU(2) coupling² g_W², **α_s(M_Z) [distinct scale]**, N_ν (light neutrino flavors), Wolfenstein A [check vs const_087], Cabibbo² [check vs const_020], PMNS θ_13/δ_CP, CMB first-peak ℓ₁, N_eff, α_em⁻¹(M_Z), Higgs total width Γ_H, deuteron binding B_d, muon decay rate Γ_μ, T_ν/T_CMB.
- **Flagged for a 2nd dup-check before assigning:** Wolfenstein A (vs const_087 A_Wolf), Cabibbo² (vs const_020), α_s(M_Z) (vs the registry α_s(M_Z) theorem) — same quantity may already be indexed.

## Recommended sequence (for Casey approval)
1. **Assign-id batch** (Category 2, minus the 3 flagged-recheck): low-risk, I execute on approval, gives every real constant a stable id + a pointer-audit slot.
2. **Dedup batch** (Category 1): governance — you approve delete/merge per row (never silent); I execute with backup, preserving any unique field.
3. The 3 recheck items resolve into 1 or 2 as I confirm.

**Done-bar (data-hygiene):** categorized, dup-vs-distinct verified by value+formula, nothing executed, routed to governance. Filed for the pointer-audit correction plan. Nothing pushed.
