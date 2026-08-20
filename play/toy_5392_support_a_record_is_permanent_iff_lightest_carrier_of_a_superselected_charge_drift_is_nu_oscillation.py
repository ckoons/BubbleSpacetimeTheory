import numpy as np
print("="*104)
print("TOY 5392 -- WHICH PARTICLES CAN HOLD A COMMITMENT RECORD, AND HOW DOES IT FAIL?")
print("  @Casey's question: can other particles encode commitment information -- and does it drift/die?")
print("="*104)

print("\nTABLE 1 -- *** what makes the nucleon's record permanent? Two conditions, not one. ***")
print("   (a) the information is carried by a SUPERSELECTED charge (no observable connects sectors)")
print("   (b) the CARRIER is stable")
print("   ==> the proton has both: baryon number is superselected, and the proton is the LIGHTEST")
print("       baryon, so it has nothing to decay into. *** (b) FOLLOWS FROM (a) for the lightest")
print("       carrier -- that is the whole mechanism. ***")

print("\nTABLE 2 -- *** run every carrier through the two conditions ***")
print("   carrier          charge held        superselected?  lightest carrier?  record status")
rows=[
 ("proton",        "baryon number",  "YES","YES","*** PERMANENT ***"),
 ("bound neutron", "baryon number",  "YES","(bound)","*** PERMANENT ***"),
 ("free neutron",  "baryon number",  "YES","NO -> p","DIES (tau = 878 s)"),
 ("electron",      "electric charge","YES","YES","*** PERMANENT ***"),
 ("muon",          "electric charge","YES","NO -> e","DIES (tau = 2.2e-6 s)"),
 ("tau",           "electric charge","YES","NO -> mu,e","DIES (tau = 2.9e-13 s)"),
 ("nu (flavour)",  "lepton FLAVOUR", "*** NO ***","-","*** DRIFTS -- oscillates ***"),
 ("nu (lightest)", "lepton number",  "YES","YES","PERMANENT (number, not flavour)"),
 ("photon",        "none",           "-","-","holds NO record (no charge)"),
 ("pi0",           "none conserved", "-","NO","DIES (tau = 8.5e-17 s)"),
]
for r in rows: print("   %-16s %-18s %-15s %-18s %s"%r)

print("\nTABLE 3 -- *** the two failure modes are PHYSICALLY DIFFERENT, and @Casey named both ***")
print("   mode    what happens                                   example          timescale")
print("   DIE     the CARRIER decays; the record goes with it     muon            2.2e-6 s")
print("   DRIFT   the carrier SURVIVES, the LABEL rotates         nu oscillation  L_osc/c")
print("   ==> *** NEUTRINO OSCILLATION IS INFORMATION DRIFT, exactly. *** The particle persists;")
print("       its flavour label does not. That is a record degrading without its carrier dying.")

print("\nTABLE 4 -- quantify the drift: neutrino flavour half-life in proper terms")
dm21,dm31=7.53e-5,2.453e-3
for E,lab in [(1e6,"1 MeV (reactor)"),(1e9,"1 GeV (atmospheric)")]:
    L21=2.48*E/1e9/dm21/1000   # km, L = 2.48 E[GeV]/dm2[eV^2] km
    L31=2.48*E/1e9/dm31/1000
    print("   E = %-20s L_osc(21) = %10.3f km   L_osc(31) = %8.3f km"%(lab,L21,L31))
print("   ==> flavour information has a LENGTH SCALE. Baryon number does not -- it has none at all.")

print("\nTABLE 5 -- *** the information-lifetime spread ***")
print("   carrier         record lifetime")
for nm,t in [("tau lepton","2.9e-13 s"),("pi0","8.5e-17 s"),("muon","2.2e-6 s"),
             ("free neutron","878 s"),("neutrino flavour","drifts, no fixed lifetime"),
             ("electron",">6.6e28 yr (charge-protected)"),("proton","INFINITE (BST: exactly)")]:
    print("   %-16s %s"%(nm,t))
print("   ==> spread from 1e-17 s to infinity -- *** more than 40 orders of magnitude, and the top")
print("       is not a big number but a DIFFERENT KIND of answer. ***")

print("\n"+"="*104)
print("VERDICT")
print("="*104)
print(" (1) *** YES -- other particles DO encode commitment information, and there is a clean rule")
print("     for when it survives: a record is PERMANENT iff it is carried by a SUPERSELECTED CHARGE")
print("     on the LIGHTEST CARRIER of that charge. ***")
print()
print(" (2) *** AND THAT UNIFIES THE PROTON AND THE ELECTRON: they are stable for the SAME REASON.")
print("     *** The proton is the lightest baryon; the electron is the lightest charged particle.")
print("     Neither can decay because there is nothing to decay INTO that preserves the charge.")
print("     The record's permanence is not a property of the particle -- it is a property of being")
print("     at the BOTTOM of a superselected ladder.")
print()
print(" (3) *** @Casey's two failure modes are physically distinct, and both are real: ***")
print("       DIE   -- the carrier decays (muon 2.2e-6 s, tau 2.9e-13 s, FREE neutron 878 s).")
print("       DRIFT -- *** neutrino oscillation IS information drift: *** the carrier survives and")
print("                the flavour LABEL rotates. Flavour has an oscillation LENGTH; baryon number")
print("                has none at all.")
print()
print(" (4) A SHARP CONSEQUENCE WORTH NOTING: *** the free neutron is NOT a permanent record -- it")
print("     dies in 878 s. *** The nucleon record requires BINDING. So 'the proton/neutron is the")
print("     record' is right for the proton and right for the BOUND neutron, and wrong for a free one.")
print()
print(" (5) AND ONE FOR THE LEDGER: the neutrino splits. Its lepton NUMBER is superselected and the")
print("     lightest neutrino is stable -- so it holds a permanent record of ITS NUMBER. But its")
print("     FLAVOUR drifts. *** One particle, one permanent record and one drifting one. *** That is")
print("     the cleanest illustration in the table that a 'record' is a property of the CHARGE, not")
print("     of the particle.")
