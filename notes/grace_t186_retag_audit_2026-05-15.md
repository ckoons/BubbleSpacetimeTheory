# T186 Default Citation Re-attribution Audit

**Date**: 2026-05-15 (Casey directive 17:50 EDT)
**Out of**: T1.7 RETRO-2 sample-audit (MESSAGES_2026-05-15.md Grace 17:35)
**Author**: Grace (Claude 4.7)
**Scope**: RETRO-2 upgrade set entries with `theorem == 'T186'`

## Summary

| Outcome | Count |
|---------|-------|
| Re-tagged to actual mechanism | 20 |
| Ambiguous (multi-mechanism, kept T186) | 1 |
| Genuinely T186 (no other marker, kept) | 207 |
| **Total candidates examined** | **228** |

**Tier unchanged for all entries.** Only the `theorem` field updated.

## Re-tag distribution

| New theorem | Mechanism | Count |
|-------------|-----------|-------|
| T1783 | Chern sum / Chern class | 11 |
| T1821 | Bergman/Spectral mass mechanism | 4 |
| T187 | Proton mass = 6π⁵·m_e | 3 |
| T920 | Debye temperature bridge | 1 |
| T1829 | Wallach uniqueness | 1 |

## Re-tagged entries

| Symbol | T186 → | Marker matched | Domain |
|--------|--------|-----------------|--------|
| m_d/m_u | T1783 | `chern` | particle_physics |
| DM_geometric | T1821 | `bergman` | cosmology |
| m_rho | T187 | `pi^5` | particle_physics |
| Born_rule_Bergman | T1821 | `bergman, k(z,` | condensed_matter |
| N_1520_mass | T1821 | `bergman` | particle_physics |
| Debye_C_diamond_2230 | T920 | `debye temperature` | condensed_matter |
| omega_DM_over_b | T1829 | `wallach, wallach point` | cosmology |
| m_t/m_b | T1783 | `chern` | particle_physics |
| auto_proton_pion_mass_ratio | T187 | `pi^5` | particle_physics |
| info_per_meas | T1821 | `bergman` | information_theory |
| auto_m_b_m_s | T1783 | `chern` | particle_physics |
| auto_y_b_bottom_Yukawa | T1783 | `chern` | particle_physics |
| auto_WLF_C_2__n_C_c_2__N_c__52_K | T1783 | `chern` | polymer_physics |
| auto_phi_RCP__N_c_2_c_3_1__9_14__0_6429 | T1783 | `chern, third chern` | colloid_science |
| G_N_from_BST | T187 | `pi^5` | particle_physics |
| sc_nb3sn_ybco_ratio | T1783 | `chern, third chern` | condensed_matter |
| diamond_cu_debye_ratio | T1783 | `chern, third chern` | condensed_matter |
| Al_Z_c3 | T1783 | `chern, c_3(q, third chern` | condensed_matter |
| phi5 | T1783 | `chern` | ? |
| phi_nC_c2 | T1783 | `chern, second chern` | condensed_matter |

## Ambiguous (kept T186 by conservative rule)

Items where multiple mechanism families matched. Kept T186 rather than guess. Manual review recommended for these.

| Symbol | Markers matched |
|--------|------------------|
| m_e_from_Planck | T1821:1, T187:1 |

## Reproducibility

Script: `play/grace_retag_t186_defaults.py`. 
Idempotent — predicate requires `theorem == 'T186'`, so re-running is a no-op on already-retagged entries.