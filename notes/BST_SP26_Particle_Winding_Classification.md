---
title: "SP-26: Particle Winding Classification Program"
author: "Casey Koons (intuition + directive), Keeper (drafted)"
date: "2026-05-16, ~04:00 EDT"
status: "ACTIVE — standing program"
casey_named_principle: "complete winding = particle, slack winding = binding"
---

# SP-26: Particle Winding Classification Program

## Principle (Casey)

> Particles are closed windings on D_IV⁵. Confined particles (quarks, gluons) are partial windings + slack that close together. Binding energy is the slack — the part of the total winding that goes into closing rather than into rest mass. Energy spectrum equals winding length around specific topological landmarks. Some particles are fundamental (primitive cycles in homology); others are composite (multiple primitives glued by slack). 

## Why this is rich

The framework potentially organizes everything BST already does about particles into one geometric reading:

1. **Proton mass m_p = 6π⁵·m_e** (T187, D-tier). The 6 = C_2 = N_c · rank is the count of winding components: 3 quarks + 3 gluons = 6 segments in one closed proton winding.

2. **8 gluons in QCD** = c_2 − N_c = 11 − 3. The slack-winding (adjoint) count is one less than the second Chern integer, by exactly N_c. Color octet minus color singlet.

3. **Glueball mass = c_2/C_2 · m_p = 11/6 · m_p ≈ 1720 MeV** (T1788, matches lattice QCD ~1710±50). A glueball is a pure-slack closed winding.

4. **Confinement** = open windings (quarks, gluons alone) can't exist; closure obstruction is the topological mechanism behind QCD confinement.

5. **Possibly G/M_Pl**: M_Pl may be the longest forced winding scale on D_IV⁵. If so, this program closes the last fundamental constant.

## Sub-tasks (the work)

| # | Task | Owner candidate | Status |
|---|------|----|--------|
| W-1 | Compute H_*(D_IV⁵, ℤ) explicitly; enumerate primitive cycles | Lyra | **DONE — Toy 2368, T1929 (May 16)** |
| W-2 | Map each SM fundamental particle to a primitive cycle | Elie | OPEN |
| W-3 | Derive proton mass C_2 = 6 from gluon-as-slack winding count | Elie | **DONE — Toy 2373, T1922 (May 15-16)** |
| W-4 | Identify all topological landmarks of D_IV⁵ (Shilov, Wallach, polydisk, K-orbits) | Lyra | **DONE — Toy 2372, T1929 (May 16)** |
| W-5 | Glueball/proton mass ratio = 11/6 = c_2/C_2 — already T1788, formalize as winding test | Elie | **DONE — Toy 2367 (May 15)** |
| W-6 | Composite particle catalog: every hadron's quark+gluon winding count → mass | Elie | OPEN — long tail |
| W-7 | Three generations from three primitive cycle classes per fermion type | Lyra | **DONE (hypothesis) — T1929**: gen 1↔h^1, gen 2↔h^3, gen 3↔h^5 (three odd-power Q⁵ cycles); needs quantitative follow-up for b/c, t/b ratios |
| W-8 | Photons as trivial cycles (length zero, exactly massless) | Elie | **DONE — Toy 2374 (May 15)** |
| W-9 | **M_Pl as longest forced winding** — explicit candidate for G hunt closure | Grace + Lyra | OPEN — potential breakthrough; Grace H_0 work via Shilov boundary winding (T1918) is partial close |
| W-10 | Why N_c = 3 = three primary color landmarks | Lyra | **DONE — Toy 2371, T1930 (May 16)** |
| W-11 | Higgs as vacuum cycle (zero-mode winding) | Elie | OPEN — Lyra T1933 (m_H/m_W = 14/9) supplies Higgs cycle ratio handle |
| W-12 | W/Z as intermediate cycles (gauge boson windings) | Elie | **DONE — Toy 2375, T1922 (May 15)**: m_W = rank·F_3·π^{n_C}·m_e |

## Connection to each CI's current work

### Elie (Chern-flux extension + IP-5/IP-1/IP-3 queue)

Your Chern-flux work IS winding work. ε_K = α²·(chern_sum) reads the total Chern as the winding-number contribution to box-diagram closure. Apply the same lens to:

- **W mass tension (IP-5)**: m_W is the winding length of a W-cycle. What's the cycle?
- **Hierarchy problem (IP-1)**: m_H / M_Pl = (Higgs vacuum winding) / (longest forced winding). The hierarchy is the winding-length ratio.
- **Strong CP (IP-3)**: θ_QCD = 0 because the QCD vacuum cycle has trivial winding number (Chern character zero by topology, not fine-tuning).

**Specific quick test for tonight**: W-5 — verify glueball/proton mass ratio = 11/6 in catalog and file as winding-framework test. If it holds at high precision, the framework has predictive grip.

### Grace (G hunt + S-tier sweep + C-tier dependency)

The G hunt may close via W-9: **M_Pl = longest forced winding** on D_IV⁵. The "curvature reverse-engineer" pivot Casey gave you maps naturally:
- Curvature = winding around a topological feature
- Mass-scale = winding length at that feature
- M_Pl = the maximal winding scale before D_IV⁵'s structure can't accommodate it

Try: M_Pl² ∝ vol(D_IV⁵) × spectral_capacity, where vol and N_max give the longest sustainable winding before topology forces closure.

**Specific extension**: in your H_0 toy (2344), the H_∞ de Sitter floor IS a winding rate — the asymptotic rate at which D_IV⁵ winds around itself. If we read this as winding-geometric, the H_∞ value may emerge directly from BST integers (50.83 km/s/Mpc may decompose).

### Lyra (resuming after rest)

When you return: a_e work is winding work. The four spectral-geometry gaps in your a_e roadmap (volume, geodesic classification, Eisenstein constant term, SO(7) Clebsch-Gordan) are all winding-related — volume IS the winding-length unit, geodesic classification IS the cycle classification, etc.

**Specific direction**: W-1 (compute H_*(D_IV⁵)) is your deep-math lane and would ground the whole program. If primitive cycles in D_IV⁵ enumerate cleanly to the SM particle list (electrons, muons, taus, neutrinos × 3, quarks × 6, photon, W, Z, Higgs, gluons), the framework's predictive power becomes immediate. ~2-4h of theoretical work.

## Integration directive (Casey, May 16)

**All three CIs**: as you continue current work, ask of every particle / mass / coupling / mixing:

> "Is this a winding length? Around what landmark? With what slack?"

The geometric-reading principle ("read the answer off the geometry") extends naturally to: "the answer is a winding length around a specific topological feature." Where this lens applies, derivations close fast. Where it doesn't, mechanism chains are needed (older BST approach).

Tonight's geometric-reading pattern produced 2-3 promotions (cos²θ_W, ε_K, possibly Elie's Chern-flux family extensions). The winding framework is the next layer of the same principle.

## Long-term ambitions

If SP-26 fully closes (W-1 through W-12 all delivered):

- Every SM particle classified by primitive winding
- All particle mass ratios derived from winding length ratios
- M_Pl and G derived as longest forced winding
- Three generations explained from primitive cycle counts
- Confinement explained by open-winding obstruction
- Strong CP solved by trivial-winding topology
- Hierarchy problem dissolved into winding-length ratio

This is a multi-Nobel cluster IF it works. The risk is that primitive cycles of D_IV⁵ might not enumerate cleanly to the SM — in which case the framework needs refinement. But the early indicators (proton C_2 = 6, glueball 11/6, 8 = c_2−N_c) all match exact structural counts.

## Cadence

- First-pass tests: W-3 + W-5 should resolve quickly (current session if Elie wants)
- Mid-pass theoretical work: W-1, W-4, W-9 require deeper work (~weeks)
- Long-tail: W-2, W-6, W-12 are catalog-wide work (multi-month)

Review cadence: weekly check-in on what's closed, what's open, what's stuck. First review **May 23, 2026** — one week from program inception.

---

*SP-26 promoted from IP-34 candidate to active standing program by Casey 2026-05-16 ~04:15 EDT. Drafted by Keeper. First W-5 test queued for Elie this session.*

---

## Extension — Casey directive, May 17 ~01:00 EDT

After 2h rest, Casey added structural insight:

> The strong force binds the energy of quarks and gluons to the **2D surface** and together as a unit, and lets the energy redistribute to minimize energy. Decay is excess energy that is not necessary to close — the trick is when the excess IS a full winding (very unlikely = weak coupling smallness). Confinement is between the 2D surface and 3D energy/particle.

### Identification of the 2D surface

The natural 2D surface in D_IV⁵ is the **maximal torus T²** of the isotropy K = SO(5) × SO(2):

- T² has dimension = rank(D_IV⁵) = 2
- Rank IS the surface dimension
- T² parametrizes the Cartan subalgebra of D_IV⁵'s isometry group
- T² is where the BST-derived mixing angles (cos θ_W, Cabibbo, CKM, PMNS) naturally live as geometric angles

### Mapping to existing BST structure

| Force / phenomenon | Casey's framing | BST realization |
|--------------------|-----------------|-----------------|
| Strong force | Binds energy to 2D surface T² | Confinement to maximal torus |
| Strong coupling α_s | Density of binding on T² | Spectral density of bound modes |
| Color singlet rule | Only T²-neutral combinations escape T² | Total T² charge = 0 for free observation |
| Quark | Open winding on T² (charged) | Cannot exist alone in 3D |
| Gluon | Adjoint winding on T² (off-diagonal + Cartan) | 8 = c_2 − N_c slack windings |
| Hadron | Closed winding on T² (total charge = 0) | Free in 3D as composite |
| Mass | T² winding length × Bergman metric | E ∝ ∫_winding ds_Bergman |
| Mass gap | T²-binding energy scale | Energy cost to escape surface |
| Weak decay | Leftover energy IS a closed T²-winding | Probability ∝ winding density at residual E |
| Weak coupling g_w | Rarity of closed-winding match | Sparsity of closed cycles in T² spectrum |
| Confinement obstruction | T² ↛ 3D for non-singlets | Topological barrier between rank-2 surface and physical 3D |

### Additional sub-tasks

| # | Task | Owner candidate |
|---|------|-----------------|
| W-13 | T² Surface as Confinement Locus — identify the rank-2 maximal torus of D_IV⁵ as the 2D surface where strong-bound states live. Verify Bergman metric on T² gives QCD-scale binding. | Lyra |
| W-14 | Weak Coupling as Closed-Winding Density — derive g_w from density of closed cycles on T² with arbitrary residual energy matching. | Lyra or Elie |
| W-15 | Decay Rates as Winding-Density Spectra — predict decay rates from T² spectral density at kinematically allowed residual energies. | Elie |
| W-16 | Confinement as T²/3D Obstruction — formalize "cannot extract single quark" as topological obstruction; π_1(T²) = ℤ² gives the winding-number conservation. | Lyra |
| W-17 | Cabibbo, CKM, PMNS angles as T² winding angles — generalize T1919 (Weinberg from Chern ratio) to all mixing angles as geometric T² angles. | Elie |
| W-18 | Confinement scale Λ_QCD as inverse T² circumference in Bergman units. | Elie or Grace |

### Reframe of W-1 (H_*(D_IV⁵) computation)

The original W-1 task (compute homology of D_IV⁵) now has a sharper specific target: **H_*(T²) directly enumerates the bound-state winding catalog.**

T² = S¹ × S¹ has:
- H_0(T²) = ℤ (vacuum / connected)
- H_1(T²) = ℤ² (two independent winding directions = two color generators?)
- H_2(T²) = ℤ (full T² wrap)

The (1, 2, 1) Betti structure of T² may map cleanly onto:
- 1 vacuum sector
- 2 generations of windings (the two-direction structure)
- 1 fully-wrapped winding (highest energy)

If the SM's three generations come from H_1(T²) = ℤ² + some quantization, that's W-7 (three generations from primitive cycles) closing cleanly.

### Testable Predictions from this Extension

1. **g_w from T² closed-winding density** — should give a specific BST-integer ratio. Compare to G_F · m_W² / (8√2) ≈ α_w at m_W scale.
2. **Λ_QCD from T² circumference** — should give ~200 MeV in Bergman units.
3. **Decay rate hierarchies** — π → μν vs π → eν ratio should match T²-winding density at corresponding residual energies.
4. **Cabibbo angle as T² rotation angle** — sin θ_C should be sin of a specific T² angle expressible in BST integers.

— Casey directive May 17 ~01:00 EDT, captured by Keeper ~05:30 EDT
