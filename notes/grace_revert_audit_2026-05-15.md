# RETRO-2 Revert Audit — 73 auto_+structural items D → S

**Date**: 2026-05-15 (Casey directive 17:50 EDT)
**Out of**: T1.7 RETRO-2 sample-audit (MESSAGES_2026-05-15.md Grace 17:35)
**Author**: Grace (Claude 4.7)
**Scope**: ONLY the 73 items in the I→D upgrade set between commits 9503f92 and 0b420b0 that match `symbol=auto_*` AND `status=structural` AND `tier=D`. Pre-existing auto_+structural+D entries (~360) are NOT touched.

## Summary

Reverted 73 entries from D-tier to S-tier.

These were promoted I→D by Toy 2254's RETRO-2 batch-upgrade pass via keyword pattern matching, despite being honestly flagged `status='structural'` by their creator. Reverting tier to S matches the status field's plain meaning.

## Tier distribution

| Tier | Before | After | Δ |
|------|--------|-------|---|
| D | 3473 (85.8%) | 3400 (84.0%) | -73 |
| I | 199 (4.9%) | 199 (4.9%) | +0 |
| C | 109 (2.7%) | 109 (2.7%) | +0 |
| S | 265 (6.5%) | 338 (8.4%) | +73 |

D-tier: 85.8% → 84.0%.

## Reverted entries (73)

| Symbol | Formula | Precision | Theorem (was) | Domain |
|--------|---------|-----------|---------------|--------|
| auto_3D_Ising_omega__n_C_C_2__5_6 | `n_C/C_2` | 0.4% | T186 | statistical_mechanics |
| auto_Cascade_depth_n_c__rank_g_C_2__26_mo | `rank*(g+C_2)` | ~1% | T186 | turbulence |
| auto_Prandtl_number_air__n_C_g__5_7__0_7 | `n_C/g` | 0.6% | T186 | turbulence |
| auto_neutron_proton_mass_diff | `m_e*(rank+1/rank)` | 1.2% | T186 | particle_physics |
| auto_pion_electron_mass_ratio | `rank*N_max` | 0.3% | T186 | particle_physics |
| auto_proton_pion_mass_ratio | `C_2*pi^5/(rank*N_max)` | 0.3% | T186 | particle_physics |
| auto_qcd_deconfinement_temp | `?` | 1.4% | T186 | particle_physics |
| auto_g_eff_sm_approx | `N_max - 30` | 0.2% | T186 | thermodynamics |
| auto_higgs_vev_proton_ratio | `rank*(N_max-C_2)` | 0.2% | T186 | particle_physics |
| auto_bag_constant_fourth_root | `m_pi*sqrt(rank)` | 1.3% | T186 | particle_physics |
| auto_disk_drag_coefficient | `g/C_2` | 0.3% | T186 | fluid_dynamics |
| auto_flat_plate_drag_coeff | `rank^2/N_c = C_F` | 0.4% | T186 | fluid_dynamics |
| auto_blasius_displacement_thickness | `sqrt(N_c)` | 0.7% | T186 | fluid_dynamics |
| auto_blasius_momentum_thickness | `rank/N_c` | 0.4% | T186 | fluid_dynamics |
| auto_string_tension_sqrt_sigma | `sqrt(2*n_C)*m_pi` | 0.3% | T186 | particle_physics |
| auto_string_tension_alpha_corrected | `sqrt(2*n_C)*m_pi*sqrt(1-1/(rank^2*N_max))` | 0.2% | T186 | particle_physics |
| auto_spectral_tilt_ns | `1 - n_C/N_max` | 0.14% | T186 | cosmology |
| auto_spectral_tilt_slowroll | `1 - 2/(N_c*rank^2*n_C)` | 0.18% | T186 | cosmology |
| auto_planck_hierarchy_exponent | `(c_2+g)*log10(N_max)` | 0.6% | T186 | cosmology |
| auto_dm_baryon_ratio | `rank^(rank^2)/N_c` | 1.2% | T186 | cosmology |
| auto_z_equality | `N_max*n_C^2` | 0.7% | T186 | cosmology |
| auto_hubble_constant | `N_max/rank` | 1.6% | T186 | cosmology |
| auto_age_of_universe | `f(g/(g+N_c), N_c/(g+N_c))/(N_max/rank)` | 0.3% | T186 | cosmology |
| auto_debye_Ag_Cu_ratio | `rank/N_c` | 1.6% | T186 | condensed_matter |
| auto_he_ionization_ratio | `(rank*n_C-1)/n_C` | 0.4% | T186 | atomic_physics |
| auto_deuteron_binding_me_ratio | `rank^2 + 1/N_c` | 0.5% | T186 | nuclear_physics |
| auto_proton_magnetic_moment | `N_c - 1/n_C` | 0.25% | T186 | nuclear_physics |
| auto_neutron_magnetic_moment | `-(rank - 1/(rank*n_C))` | 0.7% | T186 | nuclear_physics |
| auto_electron_anomaly_schwinger | `1/(N_max*rank*pi)` | 0.18% | T186 | particle_physics |
| auto_alpha_s_mz | `rank/seesaw` | 0.25% | T186 | particle_physics |
| auto_pi_minus_Nc_approx | `1/g` | 0.9% | T186 | number_theory |
| auto_pi_squared_residue | `pi^2 - N_c^2 approx g/rank^N_c` | 0.6% | T186 | number_theory |
| auto_pi_fifth_integer_approx | `rank*N_max + rank^n_C` | 0.006% | T186 | number_theory |
| auto_proton_electron_integer | `C_2*(rank*N_max + rank^n_C)` | 0.008% | T186 | particle_physics |
| auto_three_sat_threshold | `rank^2 + rank/(g+1)` | 0.4% | T186 | computer_science |
| auto_V_ts | `1/(rank*(g+C_2)) = 1/beta_1` | 0.87% | T186 | particle_physics |
| auto_sin_2_theta_13_PMNS | `1/(C_2*g+N_c)` | 0.15% | T186 | particle_physics |
| auto_m_s_m_d | `rank^2*n_C` | 0.53% | T186 | particle_physics |
| auto_m_s_m_u | `(rank^2*n_C)*(rank+1/g)` | 0.99% | T186 | particle_physics |
| auto_m_tau_m_mu | `seesaw-1/g` | 0.24% | T186 | particle_physics |
| auto_m_b_m_s | `C_2*g+N_c = chern_sum+N_c` | 0.66% | T186 | particle_physics |
| auto_det_M_u_det_M_d | `rank^(rank^N_c) = 2^8` | 0.66% | T186 | particle_physics |
| auto_m_p_m_u_m_d | `N_max` | 0.16% | T186 | particle_physics |
| auto_m_p_m_s | `rank*n_C` | 0.35% | T186 | particle_physics |
| auto_y_t_top_Yukawa | `g*sqrt(2)/10` | 0.13% | T186 | particle_physics |
| auto_y_b_bottom_Yukawa | `1/chern_sum` | 0.83% | T186 | particle_physics |
| auto_Gamma_Z_Gamma_W | `C_2/n_C` | 0.27% | T186 | particle_physics |
| auto_N_nu_from_Z_width | `N_c` | 0.54% | T186 | particle_physics |
| auto_BR_H_bb | `C_2*N_c/(rank*n_C*N_c+1)` | 0.23% | T186 | particle_physics |
| auto_BR_H_WW | `N_c/(rank^2*N_c+rank)` | 0.33% | T186 | particle_physics |
| auto_f_pi_m_pi | `1-1/seesaw` | 0.89% | T186 | particle_physics |
| auto_f_K_m_K | `N_c/(N_c^2+1/N_c)` | 0.70% | T186 | particle_physics |
| auto_tau_n_neutron_lifetime | `rank^4*n_C*c_2` | 0.18% | T186 | nuclear_physics |
| auto_m_pi__m_pi0_m_e | `N_c^2` | 0.13% | T186 | particle_physics |
| auto_m_D_m_p | `rank` | 0.37% | T186 | particle_physics |
| auto_m_B_m_p | `n_C+C_2/(rank*n_C)` | 0.47% | T186 | particle_physics |
| auto_m_rho_m_pi | `c_2/rank` | 0.98% | T186 | particle_physics |
| auto_m_omega_m_rho | `1+1/(rank*n_C*g)` | 0.47% | T186 | particle_physics |
| auto_m_phi_m_pi | `g+rank*N_c/seesaw` | 0.67% | T186 | particle_physics |
| auto_m_Lambda_m_p | `1+N_c/(n_C*N_c+1)` | 0.13% | T186 | particle_physics |
| auto_m_Sigma_m_p | `(g+C_2)/(rank*n_C+1/N_c)` | 0.75% | T186 | particle_physics |
| auto_m_Xi_m_p | `1+N_c^2/(N_c*g+1)` | 0.55% | T186 | particle_physics |
| auto_m_Omega_m_p | `(g+C_2)*N_c/(N_c*g+1)` | 0.55% | T186 | particle_physics |
| auto_m_Delta_m_p_m_pi | `rank+1/(rank*n_C)` | 0.21% | T186 | particle_physics |
| auto_Decuplet_spacing | `N_max+rank*n_C` | 0.12% | T186 | particle_physics |
| auto_T_CMB | `N_max/(rank*n_C^2)` | 0.53% | T186 | cosmology |
| auto_sigma_8 | `N_c*g/(rank*(g+C_2))` | 0.41% | T186 | cosmology |
| auto_N_eff_BBN | `N_c+g/(N_max+N_c)` | 0.13% | T186 | cosmology |
| auto_t_0_age_of_universe | `N_max/(rank*n_C)` | 0.70% | T186 | cosmology |
| auto_ln_10_10_A_s | `N_c+1/44` | 0.70% | T186 | cosmology |
| auto_AC_graph_spectral_gap__rank_g | `rank/g = 2/7` | ? | T186 | graph_theory |
| auto_WLF_C_2__n_C_c_2__N_c__52_K | `n_C*c_2 - N_c = 5*11 - 3 = 52` | ? | T186 | polymer_physics |
| auto_phi_RCP__N_c_2_c_3_1__9_14__0_6429 | `N_c^2/(c_3+1) = 9/14 = 0.6429` | ? | T186 | colloid_science |

## Reproducibility

Script: `play/grace_revert_73_auto_structural.py`

The script also restores Elie's 5 Hilbert_Q5 entries from Toy 2255 that were inadvertently lost in an earlier git checkout. Restoration is idempotent — symbols are checked before re-adding.

## Open question separately

There are ~360 additional pre-existing entries with `symbol=auto_*` AND `status=structural` AND `tier=D` that were tagged in earlier data-layer passes (not RETRO-2). Casey's directive scoped this revert to the RETRO-2 73 only. Whether those 360 should also revert by the same reasoning is queued for separate review.