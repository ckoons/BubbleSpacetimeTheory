# BST Research Notes

**Status: Work in progress — not final, not peer-reviewed**

These are active working notes from ongoing BST research sessions. They explore extensions and implications of the core framework documented in the main repository. Content here may be incomplete, speculative, or superseded by later work. Do not cite without checking current status with the authors.

---

## Contents

| File | Topic | Status |
|---|---|---|
| `BST_Partition_Function_1st_Computation.md` | First numerical computation of Z(β) on S⁴×S¹ with Haldane exclusion — 3 phase transitions, vacuum energy, Haldane cap finiteness, cosmological constant conjecture | Working note |
| `BST_PartitionFunction_Analysis.md` | Extended computation: convergence study (24M mode slots), thermodynamic profile, N_max dependence, refined Λ estimate, bulk D_IV^5 correction. Key results: F = −0.09855 exact, T_c = 130.5, bulk correction zero at low T | Research note |
| `BST_Cosmological_Constant.md` | First-principles derivation of Λ from the BST partition function — Haldane cap as UV regulator, finite vacuum energy, Λ ~ 9.9×10⁻¹²⁵ (2.5 orders from observed) from one observational input, coincidence problem dissolved | Research paper |
| `BST_Field_Equation.md` | Derivation of the modified Einstein equation from BST substrate geometry — G + Λg = 8πGT unpacked layer by layer from the Koons substrate | Working note |
| `BST_Particle_Predictions.md` | Topologically forbidden particles (axion, gravitino, sterile neutrino), proton radius refinement, new particle predictions from circuit topology | Working note |
| `BST_Gravitational_Waves.md` | Primordial gravitational waves from the pre-spatial phase transition — the substrate's own ring, predictions for LISA/PTA spectrum | Working note |
| `BST_Galaxy_Mergers.md` | Galaxy mergers as substrate dynamics — channel noise re-equilibration, spiral arm reformation, testable predictions distinct from N-body DM simulations | Working note |
| `BST_PartitionFunction_Progress.md` | Summary of all partition function work completed; open problems assessment | Research note |
| `BST_Casimir_Analysis.md` | Seeley-DeWitt regularization of Casimir zeta on S⁴×S¹: winding modes proved negligible for ρ≫1; Wyler formula confirmed (α=1/137.036, 0.0001% precision); diagnosis of Casimir Stability Conjecture | Research note |
| `BST_FermionMass.md` | Fermion mass ratios from D_IV^k Bergman geometry — m_μ/m_e = (24/π²)^6 = 206.761 (0.003%), exponent from real dimension of embedding submanifold; tau and quark mass coincidences | Research note |
| `BST_ResearchRoadmap.md` | **Master research roadmap** — all open problems in priority order, tools needed (existing and to create), the chain m_e → G → H₀, 12 open problems with programs and notes specified | Research plan |
| `BST_Challenge_Number_Theorists` | Open problems for number theorists — arithmetic optimality of 137 as the largest sum-of-two-squares prime below the Wyler ceiling; cost function computation; connections to Langlands program | Open problem |
| `maybe/BST_Before.md` | Pre-geometric epoch: mathematical natural selection for the substrate — how $S^2 \times S^1$ with N=137 may have emerged by minimizing information cost per unit of physics | Speculative note |
| `BST_CostFunction_Kappa.md` | Geometric identification of κ = N_max × d_{l*} / Vol(D_IV^5) = 137 × 91 × 1920/π^5 ≈ 78,219 — Bergman curvature mixing closes gap from 980 ppm to 5 ppm; three independent derivations of N=137 (Wyler, geometric, Bergman-corrected) | Research note |
| `BST_Hubble_Expansion.md` | Committed contact graph area on the substrate as the physical origin of Hubble expansion — H=(1/2)d(ln A_c)/dt; backfit table from model-independent data; Hubble tension as local contact density gradient; derivation framework awaiting partition function | Research note |
| `Hubble_Estimates.md` | Numerical backfit table: H₀ under all model-independent input combinations (BBN D/H, T_c correction, neutrino mass, chronometers). Floor = 58.2 km/s/Mpc, gap analysis, drivers summary | Supporting calculation |
| `BST_Lambda_Derivation.md` | **Closed-form derivation of Λ** — Λ = F_BST × α⁵⁶ × e⁻² matches observed 2.90×10⁻¹²² to 0.02%; d₀/l_Pl = α^{2(n_C+2)} × e^{-1/2}; S¹ winding origin of e^{-1/2}; cosmological constant problem resolved | Key result |
| `BST_ProtonMass.md` | **Proton/electron mass ratio** — m_p/m_e = (n_C+1)π^{n_C} = 6π⁵ = 1836.118 (0.002%); Bergman kernel power × π-volume factor; residual 0.017 MeV = EM self-energy correction; G requires hierarchy problem | Key result |
| `BST_GravitationalConstant.md` | **Hierarchy and Newton's G** — geometric mean identity m_e/√(m_p·m_Pl) = α^{n_C+1} = α^6 (0.017%); m_e/m_Pl = 6π^5 × α^{2(n_C+1)} (0.034%); α-power pattern: d₀↔α^14, m_e↔α^12, Λ↔α^56; rigorous derivation from Bergman embedding open | Key result |
| `BST_Tc_Formula.md` | **Phase transition temperature** — T_c = N_max × 20/21 (0.018%), best analytic formula; physical meaning: 1 of 21 SO(7) generators unfreezes at T_c (the Big Bang); T_c(phys) = m_e × 20/21 (T_c is derived from m_e, not independent); proton EM gap analysis; Bergman action program for m_e/m_Pl | Research note |
| `bst_me_derivation.py` | **Electron mass exploration** — pure geometry formula m_e/m_Pl = 6π^5 × (9/8π^4)^12 × (π^5/1920)^3 confirmed (0.034%); Wyler formula α=(9/8π^4)V5^{1/4} verified; geometric mean identity proved to be a theorem (not independent); tau has no clean Bergman chain formula (best: p=5.82 non-integer); α-power pattern table; residual search | Code + results |

---

## Relationship to Main Documents

The polished, citable documents are at the repository root:

- `WorkingPaper.md` — full framework, all completed derivations
- `LieAlgebraVerification.md` — SO(5)×SO(2) isotropy group verification (complete)
- `DarkMatterCalculation.md` — channel noise rotation curves, full SPARC run (complete)

Notes here are upstream of those documents — raw calculations and ideas that may eventually be incorporated into the working paper or published separately.

---

*Casey Koons — March 2026*
