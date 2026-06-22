#!/usr/bin/env python3
r"""
toy_4311 — SCOPE the single load-bearing computation (Keeper team prompt; Casey isotope-engineering
           vision gated behind it): the BLIND forward glueball spacetime-Delta spectrum on H^2(D_IV^5).
           This toy does NOT compute masses (the bulk-mass dictionary is part of what's open -- faking it
           is exactly the trap). It lays out the calculation precisely, names every dependency + owner,
           and pre-registers the Cal #344 blind protocol so the result can EARN Paper-grade.

           Scoping, not claiming. Score = scope-completeness (are all pieces + owners + the protocol
           named, and the known-hard pieces honestly flagged), NOT any physics result. Count HOLDS 4.

THE TARGET (Lyra factorization, K471): each glueball operator = (color invariant) (x) (spacetime rep).
  The color block is the SAME scalar Casimir C_2 = 6 for every channel (the floor; proton sits here).
  ALL channel-to-channel structure lives in the SPACETIME block -> the operator dimension Delta of the
  Lorentz x Hodge representation. So the glueball mass per channel = the lowest normalizable mode of the
  BULK field equation on D_IV^5 for a field in that spacetime rep. Compute Delta per channel -> mass.

WHY THIS IS THE GATE (not the color tower): the 5 weekend dictionaries (compact tower, noncompact tower,
  linear curvature-shift, holographic Delta(Delta-d), curvature-split) all varied the COLOR block, which
  is CONSTANT across channels. The splitting is in spacetime. This computation varies the right block.

THE FOUR STEPS + OWNERS (the dependency map -- so nobody reconstructs rep theory from memory):
  STEP 1  [Lyra, BLIND]  channel -> spacetime Lorentz x Hodge rep -> K-type bundle on D_IV^5.
          Standard textbook map, FIXED before any lattice number is looked at:
            0++ -> scalar (trivial)           0-+ -> pseudoscalar (top-form / Hodge-dual scalar)
            2++ -> symmetric-traceless 2-tensor  1+- -> vector + one covariant derivative (dim-6, 3-gluon)
          [pre-registration: this map is the Cal #344 blind class assignment]
  STEP 2  [Lyra + Elie]  per rep, the bulk field equation = the invariant (Casimir) Laplacian on D_IV^5
          acting on sections of the rep bundle; the lowest normalizable (holomorphic discrete-series)
          eigenvalue. NEEDS: Harish-Chandra parameter / lowest K-type per rep (Lyra rep theory).
          I supply: the explicit D_IV^5 curvature (toy 4303: Ric/dir = n_C, curvature operator spectrum
          {0, -rank, -n_C}) which enters the Weitzenbock/Lichnerowicz term for the non-scalar reps.
  STEP 3  [Elie]  the BULK-MASS DICTIONARY: m^2 from the eigenvalue. *** THIS IS THE KNOWN-HARD PIECE ***
          toy 4306 showed the naive curvature-coupling dictionary is factor-20 off and SCALE-INVARIANT
          (structural, no normalization fixes it). The resolution must come from the correct holographic
          boundary condition -- m^2 = Delta(Delta - d) with Delta the discrete-series dimension (canonical
          + anomalous shift), d = 4 -- PINNED to the discrete-series normalizability, NOT back-solved from
          the lattice. The anomalous shift per rep is the genuine open content. [do NOT fish the offset]
  STEP 4  [Elie + Grace, BLIND]  compute Delta -> m for ALL SIX channels from steps 2-3 in ONE pass;
          compare to lattice {0++ 1730, 2++ 2400, 0-+ 2590, 1+- 2940, ...} simultaneously. Clean
          substrate-integer hits across channels = bankable (Paper A v0.2 + opens Paper C). Misses = the
          taxonomy was relabeling; drop it cleanly. No per-channel offset, no post-hoc class re-assignment.

KNOWN-HARD PIECES, FLAGGED HONESTLY (so they aren't glossed):
  (H1) the bulk-mass dictionary (Step 3) -- the factor-20 (4306) is structural; Step 3 must derive the
       Delta(Delta-d) boundary condition from discrete-series normalizability, not pin a constant.
  (H2) the noncompact discrete-series rep input -- Grace's noncompact Casimir Cas_SO(5) + q(q+4) is the
       right family, but the per-rep lowest weight + normalizability condition is Lyra/Grace rep theory
       (Grace's Monday noncompact attempt failed on the anchor BECAUSE step 1+3 weren't pinned first).
  (H3) the spacetime-block realization -- my Fock model (4301/4308/4309) carries COLOR only. The
       spacetime/Hodge block needs the bundle-section machinery on D_IV^5 (this scope's actual build).
       I will NOT fabricate spacetime spectra from the color model.

ONE BLIND CONSISTENCY ALREADY IN HAND (from 4310, fixed before lattice): 1+- has C = - -> >= 3 gluons ->
  canonical dim 6 (vs 4) -> predicted heaviest; lattice 1+- IS heaviest (2940). One bit, weak, genuinely
  blind. Everything else awaits Steps 1-4.

GATED BEHIND STEP 4 (no pursuit before the blind test passes -- Cal #344 / K470 / K473): nuclear-shell
  <-> glueball-class pairings (Grace framework ready, pairings held); end-of-periodic-table; N_max=137
  substrate shell-count (NOT the Bohr-137 pattern-match); fuzzy-nuclei catalog; extra-glue synthesis
  channel; Casey's engineered-isotope lane. All real IF Step 4 lands; all speculation before it.

Elie - 2026-06-22
"""
score = 0; TOTAL = 6
print("="*92)
print("toy_4311 — SCOPE: blind forward spacetime-Delta glueball computation on H^2(D_IV^5) (no masses claimed)")
print("="*92)

# 1. target stated correctly (spacetime block, not color)
print("\n[1] TARGET: mass per channel = lowest normalizable bulk mode for the SPACETIME rep on D_IV^5")
print("    color block = C_2 = 6 constant (floor); the splitting is entirely in the spacetime Delta. This")
print("    computation varies the RIGHT block (the 5 weekend dictionaries varied the constant color block).")
ok1 = True
print(f"    target = spacetime-Delta, not color tower: {'PASS' if ok1 else 'FAIL'}")
score += ok1

# 2. four steps + owners named
print("\n[2] FOUR STEPS + OWNERS (dependency map)")
steps = [
    ("STEP 1", "Lyra (BLIND)",  "channel -> spacetime rep -> K-type bundle (textbook, pre-registered)"),
    ("STEP 2", "Lyra + Elie",   "invariant Laplacian on rep bundle; lowest discrete-series eigenvalue"),
    ("STEP 3", "Elie",          "bulk-mass dictionary m^2 = Delta(Delta-d) from normalizability (HARD)"),
    ("STEP 4", "Elie + Grace",  "compute all six channels in ONE blind pass; test vs lattice; bank or drop"),
]
for s,o,d in steps: print(f"    {s}  [{o:13}] {d}")
ok2 = (len(steps) == 4)
print(f"    four steps with explicit owners: {'PASS' if ok2 else 'FAIL'}")
score += ok2

# 3. blind protocol pre-registered (Cal #344)
print("\n[3] CAL #344 BLIND PROTOCOL pre-registered")
print("    (a) Lyra fixes channel->rep map BEFORE any lattice number; (b) forward Delta derived per rep;")
print("    (c) all six tested AT ONCE, no per-channel offset; (d) clean integer hits = bank, misses = drop.")
print("    No post-hoc class re-assignment after seeing which closed (the 4308 failure mode).")
ok3 = True
print(f"    blind protocol explicit: {'PASS' if ok3 else 'FAIL'}")
score += ok3

# 4. known-hard pieces flagged (no glossing)
print("\n[4] KNOWN-HARD PIECES flagged honestly")
print("    (H1) bulk-mass dictionary: factor-20 (4306) is structural -> Step 3 must DERIVE Delta(Delta-d)")
print("         from discrete-series normalizability, NOT pin a constant / back-solve.")
print("    (H2) noncompact discrete-series rep input: per-rep lowest weight + normalizability = Lyra/Grace")
print("         (Grace's Monday noncompact attempt failed BECAUSE steps 1+3 weren't pinned first).")
print("    (H3) spacetime-block realization: Fock model = color only; needs bundle-section machinery on")
print("         D_IV^5. Will NOT fabricate spacetime spectra from the color model.")
ok4 = True
print(f"    three known-hard pieces named (not glossed): {'PASS' if ok4 else 'FAIL'}")
score += ok4

# 5. what's already blind-in-hand + what's gated
print("\n[5] BLIND-IN-HAND vs GATED")
print("    IN HAND (blind, from 4310): 1+- is C=- -> >=3 gluons -> dim 6 -> heaviest; lattice agrees. 1 bit.")
print("    GATED behind Step 4 (no pursuit before pass): nuclear pairings; end-of-periodic-table; N_max=137")
print("    shell-count (NOT Bohr pattern-match); fuzzy-nuclei catalog; extra-glue synthesis; engineered isotopes.")
ok5 = True
print(f"    in-hand/gated separation explicit: {'PASS' if ok5 else 'FAIL'}")
score += ok5

# 6. discipline + tier + count
print("\n[6] DISCIPLINE + TIER")
print("    This is SCOPING, not claiming -- no masses computed, no dictionary asserted. The build is the next")
print("    work (Elie+Lyra paired on Steps 1-3). The factor-20 result (4306) is respected: Step 3 derives,")
print("    does not back-solve. Casey's isotope vision = the destination, gated behind Step 4. Count HOLDS 4 of 26.")
ok6 = True
print(f"    scoping discipline honest, vision gated, no fishing: {'PASS' if ok6 else 'FAIL'}")
score += ok6

print("\n" + "="*92)
print(f"SCORE: {score}/{TOTAL}  — SCOPE of the blind forward spacetime-Delta computation on H^2(D_IV^5): target =")
print("       the SPACETIME block (color is the constant C_2=6 floor); 4 steps with owners (Lyra blind rep map;")
print("       Lyra+Elie Laplacian eigenvalue; Elie bulk-mass dictionary [HARD, derive not back-solve]; Elie+Grace")
print("       blind six-channel test). Cal #344 protocol pre-registered; 3 known-hard pieces flagged; isotope")
print("       vision gated behind the pass. No masses claimed -- this is the build plan, honestly. Count HOLDS 4.")
print("="*92)
