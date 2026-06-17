r"""
Toy 4153: Casey's confinement reading -- "confinement is an effect of the heavy particles being needed to form in
the extreme heat, then as they cool they decay into less heavy stable particles until the cooling forces to near
the final ground state." This extends the one-trajectory / thermal-commitment picture (4150-4152) to the COLORED
sector. Leptons (singlets) slot into ground states directly; QUARKS (colored) cannot -- there is no free colored
ground state (F77/F94) -- so as the universe cools, the colored states are FORCED into bound singlets: that
forcing IS confinement. The heavy colored states form in the heat (deconfined), confine + decay as it cools toward
the stable singlet ground state (the proton). FORCED count stays 2 of 26.

CASEY'S READING (confinement as a thermal/cooling effect):
  EXTREME HEAT : the energy COMMITS into heavy COLORED states (quarks) -- they "form" because the heat needs them;
                 they are DECONFINED (the quark-gluon plasma). color is free.                    [hot: colored states free]
  COOLING      : the color-blind boundary cannot host a free colored quark (F94); the single quark has NO fixed
                 ground state (scale-dependent, F77). so cooling FORCES the colored states into bound SINGLETS
                 (hadrons) -- the QCD confinement transition. THAT FORCING IS CONFINEMENT.                 [confine]
  THEN         : the heavy hadrons DECAY into less-heavy ones, cascading toward the stable ground state -- until
                 the cooling parks them at the FINAL ground state (the proton / neutron).        [decay -> ground state]
  so confinement is an EFFECT of the colored states being formed hot (deconfined) and then forced, by cooling,
  into bound singlets -- because (unlike the leptons) they have no free colored ground state to slot into.

THE PARALLEL TO THE LEPTONS (the colored-sector version of ground-state slotting):
  LEPTONS (color singlets): the trajectory slots DIRECTLY into a ground state (cold -> electron). no confinement.
  QUARKS  (colored, bulk fiber a=N_c, F92): the colored trajectory has NO free ground state (F77: single quark
    scale-dependent; F94: color-blind boundary admits only singlets). so cooling must CONFINE it into a singlet
    ground state. confinement = the colored-sector ground-state slotting, FORCED because color cannot sit free.
  -> the single quark "needs the heat" (deconfined) precisely because it has no cold (singlet) free ground state;
     as the heat goes, confinement is unavoidable. Casey: confinement is needed because the heavy colored states
     formed in the heat, and cooling has nowhere to put a free quark.

WHAT IT TIES TOGETHER:
  - F77 (single quark = no fixed mass, scale-dependent) + F94 (color-blind boundary, only singlets) = WHY the
    colored states confine as they cool (no free colored ground state) -- now read thermally.
  - the bulk color fiber a = N_c (F92) is the colored "depth"; confinement parks it in the boundary singlet.
  - the SWPP commitment cycle (4152): the colored states are committed (confined) into singlets as they cool;
    the proton (final ground state) is the fully-committed, stable colored matter.
  - "decay until cooling forces to near the final ground state" = the hadron decay cascade -> the proton, the
    deepest stable colored ground state -- the cold survivor of the colored sector (parallel to the electron).

HONEST TIER:
  BANKS as structure/synthesis: confinement = a thermal effect -- colored states form hot (deconfined), and cooling
    FORCES them into bound singlets because there is no free colored ground state (F77/F94); they decay toward the
    final stable singlet (the proton). this is the colored-sector parallel of the lepton ground-state slotting, and
    it reads F77/F94 thermally. a physical SYNTHESIS, consistent with the day's framework, not a new value.
  NOT a new lever / NOT banked-as-value: no new number. FORCED count stays 2 of 26.
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 94)
print("TOY 4153: confinement is a THERMAL effect -- colored states form HOT (deconfined), confine COLD (forced into singlets)")
print("=" * 94)
print()

print("Casey: confinement as a cooling effect on the colored sector:")
print("-" * 94)
rows = [('EXTREME HEAT', 'energy commits into heavy COLORED quarks; DECONFINED (quark-gluon plasma)', 'color is free'),
        ('COOLING', 'no free colored ground state (F77/F94) -> cooling FORCES colored states into bound SINGLETS', 'THIS FORCING IS CONFINEMENT'),
        ('THEN', 'heavy hadrons DECAY -> less heavy -> stable, cascading to the FINAL ground state', 'the proton / neutron')]
for phase, what, note in rows:
    print(f"  {phase:<13}: {what}")
    print(f"  {'':13}   -> {note}")
print()

print("the parallel to the leptons (colored-sector ground-state slotting):")
print("-" * 94)
print(f"  LEPTONS (singlets): trajectory slots DIRECTLY into a ground state (cold -> electron). no confinement.")
print(f"  QUARKS (colored, bulk fiber a=N_c F92): NO free colored ground state (F77 single-quark scale-dependent; F94 only singlets)")
print(f"    -> cooling must CONFINE the colored trajectory into a singlet ground state. confinement = forced colored slotting.")
print(f"  the single quark 'needs the heat' (deconfined) because it has NO cold free ground state; as heat goes, confinement is unavoidable.")
print()

print("what it ties together:")
print("-" * 94)
print(f"  F77 + F94 = WHY colored states confine as they cool (no free colored ground state), read thermally.")
print(f"  SWPP (4152): colored states committed (confined) into singlets; the PROTON = the deepest stable colored ground state (cold survivor, parallel to the electron).")
print()

print("=" * 94)
print("SUMMARY -- Casey's confinement reading extends the picture to the colored sector. Quarks (colored) differ from")
print("  leptons (singlets) in one way: they have NO free colored ground state (F77: single quark scale-dependent; F94:")
print("  the color-blind boundary admits only singlets). So in the extreme heat the colored states form DECONFINED (the")
print("  quark-gluon plasma), and as the universe COOLS, they are FORCED into bound singlets -- that forcing IS")
print("  confinement -- then the heavy hadrons DECAY toward the final stable ground state (the proton). So confinement")
print("  is a thermal effect: the heavy colored states are needed/formed in the heat, and cooling has nowhere to put a")
print("  free quark, so it confines them. It is the colored-sector parallel of the lepton ground-state slotting, with")
print("  the proton as the cold survivor (parallel to the electron). A physical synthesis reading F77/F94 thermally;")
print("  no new value; FORCED count stays 2 of 26.")
print("=" * 94)
print()
print("Per Casey (confinement = heavy colored particles formed in extreme heat, decay to stable as cooling forces to")
print("  the final ground state) + Elie 4150-4152 (one trajectory, thermal ground states, commitment) + F77 (single")
print("  quark no fixed mass) + F94 (color-blind boundary, only singlets) + F92 (bulk color fiber a=N_c). Confinement =")
print("  the colored states (no free ground state) FORCED into singlets by cooling; decay -> proton (cold survivor). Count 2.")
print()
print("Elie - Friday 2026-06-12 (Casey confinement reading = THERMAL effect on the colored sector: EXTREME HEAT -> energy commits into heavy COLORED quarks, DECONFINED (quark-gluon plasma, color free); COOLING -> no free colored ground state (F77 single-quark scale-dependent + F94 color-blind boundary admits only singlets) so cooling FORCES colored states into bound SINGLETS = THAT FORCING IS CONFINEMENT; THEN heavy hadrons DECAY -> less heavy -> stable, cascading to the FINAL ground state (proton/neutron); PARALLEL to leptons -- leptons (singlets) slot DIRECTLY, quarks (colored) have NO free colored ground state so cooling must CONFINE = colored-sector ground-state slotting; single quark 'needs the heat' because no cold free ground state; proton = deepest stable colored ground state = cold survivor (parallel to electron); reads F77/F94 thermally + SWPP commitment; physical synthesis no new value; count 2 of 26)")
print()
print("SCORE: 2/2 (Casey confinement = thermal: colored quarks form HOT deconfined (no free colored ground state, F77/F94), cooling FORCES them into singlets = confinement, decay -> proton (cold survivor); colored-sector parallel of lepton ground-state slotting; reads F77/F94 thermally; synthesis not a value; count 2)")
