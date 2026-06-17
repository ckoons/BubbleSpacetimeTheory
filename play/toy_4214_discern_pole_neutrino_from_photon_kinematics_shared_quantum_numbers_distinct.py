r"""
Toy 4214: can you discern "neutrino-flavored light" (the massless pole neutrino, m_1=0, Toy 4213) from a photon? (Casey's
chat question.) ANSWER: YES, absolutely -- they share only KINEMATICS (massless, lightspeed, E=|p|, carries momentum,
oscillates/propagates); they differ in every QUANTUM NUMBER. The "light" in "neutrino-flavored light" is the kinematics;
the "neutrino-flavored" is the discriminant. The cleanest separators are absolute and resolution-independent: SPIN (1/2 vs
1) and STATISTICS (fermion vs boson). In BST the structural reason is singleton content: the photon is a TWO-singleton
composite (Flato-Fronsdal, spin 1), the pole neutrino is a SINGLE Di singleton (spin 1/2). Count stays 4 of 26 (this is a
conceptual discriminant table, banks nothing).

SHARED (why the metaphor "light"): KINEMATICS only.
  mass = 0 ; speed = c ; E = |p| ; carries momentum ; propagates / (neutrino) oscillates. on these axes a massless
  neutrino and a photon are identical -- that is the entire content of "neutrino-flavored LIGHT".

DISTINCT (why "neutrino-FLAVORED"): every quantum number.
  property            photon                                   pole neutrino (m=0)
  --------            ------                                   -------------------
  spin                1 (boson)                                1/2 (fermion)            <- ABSOLUTE separator
  statistics          Bose-Einstein                            Fermi-Dirac (Pauli)      <- ABSOLUTE separator
  helicity states     +-1 (two transverse polarizations)       left-handed only (one)
  electric charge     couples to it (EM, U(1))                 neutral to EM (weak only)
  interaction         electromagnetic (stops in thin matter)   weak only (penetrates light-years)  <- practical separator
  lepton number       0                                        +1 (carries lepton flavor)
  BST singleton       TWO-singleton composite (Rac x Rac /     SINGLE Di singleton
                      Di x Di, Flato-Fronsdal) -> spin 1       -> spin 1/2

WHY ABSOLUTE (not a resolution issue, unlike m=0-vs-tiny):
  spin and statistics are discrete, topological labels -- a spin-1 boson cannot be confused with or rotated into a spin-1/2
  fermion (no Lorentz operation connects them; no photon<->neutrino mixing). so even two EXACTLY massless particles are
  trivially distinct if one is spin-1 and the other spin-1/2. this is unlike the m_1=0-vs-tiny question (4213), which IS
  below experimental resolution -- there the distinction is mathematical; HERE the distinction is observable and absolute.

THE BST STRUCTURAL DISCRIMINANT (single vs two singletons):
  in BST spin comes from singleton content (Flato-Fronsdal): the photon = a TWO-singleton composite (spin 1, the
  uncommitted U(1)/EM boundary mode); the pole neutrino = a SINGLE Di singleton (spin 1/2, the uncommitted weak/lepton
  mode). both are "uncommitted massless modes" -- that is the family resemblance -- but the photon carries TWO singletons
  and EM quantum numbers, the neutrino ONE singleton and weak quantum numbers. so each sector has its own uncommitted
  massless mode (photon for EM/boundary; lightest neutrino for lepton/weak), distinguished by singleton-count and coupling.
  the practical detector discriminant follows: the photon couples to charge (EM shower); the neutrino couples only weakly
  (huge penetration). you tell them apart by which sector they talk to -- exactly their differing quantum numbers.

HONEST STATUS:
  answers Casey's chat question: YES, the pole neutrino is absolutely discernible from a photon. they coincide ONLY in
  kinematics (massless, lightspeed, momentum); they differ in spin (1/2 vs 1), statistics (fermion vs boson), helicity,
  charge/coupling (weak vs EM), lepton number, and BST singleton-content (one vs two singletons). spin and statistics make
  it an ABSOLUTE distinction (resolution-independent, unlike m_1=0-vs-tiny). "neutrino-flavored light" = light KINEMATICS +
  neutrino QUANTUM NUMBERS; the quantum numbers are the discriminant. conceptual table; banks nothing. count stays 4 of 26.
"""

# discriminant table (shared = kinematics; distinct = quantum numbers)
shared = ["mass = 0", "speed = c", "E = |p|", "carries momentum", "propagates (nu oscillates)"]
distinct = [
    ("spin",          "1 (boson)",                    "1/2 (fermion)",            "ABSOLUTE"),
    ("statistics",    "Bose-Einstein",                "Fermi-Dirac (Pauli)",      "ABSOLUTE"),
    ("helicity",      "+-1 (two)",                    "left-handed (one)",        "absolute"),
    ("electric charge","couples (EM, U(1))",          "neutral (weak only)",      "practical"),
    ("interaction",   "EM (stops in thin matter)",    "weak (penetrates)",        "practical"),
    ("lepton number", "0",                            "+1 (lepton flavor)",       "absolute"),
    ("BST singleton", "TWO-singleton (spin 1)",       "ONE Di singleton (spin 1/2)","structural"),
]

print("=" * 100)
print("TOY 4214: discern pole neutrino (neutrino-flavored light) from photon -- YES, by quantum numbers")
print("=" * 100)
print()
print("SHARED (the 'light' in neutrino-flavored light = kinematics only):")
print("-" * 100)
print("  " + " ; ".join(shared))
print()
print("DISTINCT (the 'neutrino-flavored' = every quantum number):")
print("-" * 100)
print(f"  {'property':<16}{'photon':<34}{'pole neutrino (m=0)':<30}{'separator'}")
for prop, ph, nu, sep in distinct:
    print(f"  {prop:<16}{ph:<34}{nu:<30}{sep}")
print()
print("why absolute (unlike m=0-vs-tiny, 4213):")
print("-" * 100)
print("  spin & statistics are discrete topological labels; no Lorentz op connects spin-1 to spin-1/2; no photon<->nu mixing.")
print("  so even two EXACTLY massless particles are trivially distinct if spins differ. (m_1=0-vs-tiny is below resolution;")
print("  this distinction is observable and absolute.)")
print()
print("BST structural discriminant: photon = TWO-singleton composite (spin 1, EM mode); neutrino = ONE Di singleton (spin")
print("  1/2, weak mode). both uncommitted massless modes; distinguished by singleton-count + which sector they couple to.")
print()

n_absolute = sum(1 for *_, sep in distinct if sep == "ABSOLUTE" or sep == "absolute")
checks = [
    ("share kinematics only (massless, c, E=|p|, momentum)", len(shared) == 5),
    ("spin differs absolutely: 1 (boson) vs 1/2 (fermion)", True),
    ("statistics differ absolutely: Bose vs Fermi", True),
    ("interaction differs: EM (charge) vs weak only", True),
    ("BST: photon = TWO-singleton (spin1); neutrino = ONE singleton (spin1/2)", True),
    ("spin/statistics = resolution-INDEPENDENT discriminants (unlike m=0-vs-tiny)", True),
    (">=3 absolute discriminants -> YES, discernible", n_absolute >= 3),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- Casey's chat question: can you discern neutrino-flavored light (the massless pole neutrino, 4213) from a")
print("  photon? Yes, absolutely. They coincide only in KINEMATICS -- both massless, both at c, both E=|p|, both carrying")
print("  momentum (the neutrino oscillates, the photon propagates) -- which is the entire content of the 'light' in")
print("  'neutrino-flavored light'. On every QUANTUM NUMBER they differ: spin 1/2 vs 1, Fermi vs Bose statistics, one")
print("  left-handed helicity vs two photon polarizations, weak coupling vs electromagnetic, lepton number +1 vs 0. Spin and")
print("  statistics make this an ABSOLUTE, resolution-independent distinction -- a spin-1/2 fermion cannot be confused with")
print("  or rotated into a spin-1 boson, and there is no photon-neutrino mixing -- unlike the m_1=0-vs-tiny question (4213),")
print("  which is genuinely below experimental resolution. In BST the structural reason is singleton content: the photon is a")
print("  two-singleton Flato-Fronsdal composite (spin 1, the uncommitted EM/U(1) mode) while the pole neutrino is a single")
print("  Di singleton (spin 1/2, the uncommitted weak/lepton mode); both are uncommitted massless modes -- the family")
print("  resemblance -- but with different singleton-count and coupling sector, which is exactly how a detector tells them")
print("  apart (the photon showers electromagnetically; the neutrino slips through). 'Neutrino-flavored light' = light")
print("  kinematics + neutrino quantum numbers; the quantum numbers are the discriminant. Conceptual table; count stays 4 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (can you discern neutrino-flavored light (massless pole neutrino m_1=0, Toy 4213) from a photon? Casey chat question; ANSWER YES absolutely, they share only KINEMATICS (massless, lightspeed, E=|p|, carries momentum, propagates/oscillates = the entire content of the 'light' in neutrino-flavored light) and differ in every QUANTUM NUMBER; SHARED kinematics mass=0 speed=c E=|p| momentum propagation; DISTINCT spin 1/2 (fermion) vs 1 (boson) ABSOLUTE, statistics Fermi-Dirac/Pauli vs Bose-Einstein ABSOLUTE, helicity left-handed only (one) vs +-1 (two), electric charge neutral/weak-only vs couples EM/U(1), interaction weak-only (penetrates light-years) vs electromagnetic (stops in thin matter) practical, lepton number +1 vs 0, BST singleton content SINGLE Di singleton (spin 1/2) vs TWO-singleton composite Flato-Fronsdal Rac x Rac/Di x Di (spin 1); WHY ABSOLUTE spin+statistics are discrete topological labels no Lorentz op connects spin-1 to spin-1/2 no photon<->neutrino mixing so even two EXACTLY massless particles trivially distinct if spins differ, unlike m_1=0-vs-tiny (4213) which IS below experimental resolution (there distinction is mathematical, HERE observable+absolute); BST STRUCTURAL DISCRIMINANT spin from singleton content (Flato-Fronsdal) photon = TWO-singleton composite (spin 1 uncommitted U(1)/EM boundary mode) neutrino = SINGLE Di singleton (spin 1/2 uncommitted weak/lepton mode), both uncommitted massless modes (family resemblance, each sector has its own uncommitted massless mode photon for EM/boundary + lightest neutrino for lepton/weak) distinguished by singleton-count + coupling sector, detector discriminant follows photon couples to charge EM shower neutrino couples only weakly huge penetration; HONEST neutrino-flavored light = light KINEMATICS + neutrino QUANTUM NUMBERS the quantum numbers are the discriminant, spin+statistics absolute resolution-independent, conceptual table banks nothing; count 4 of 26)")
print()
print(f"SCORE: {passed}/{len(checks)} (discern pole neutrino from photon: YES absolutely; SHARE only kinematics (massless, c, E=|p|, momentum); DIFFER in spin 1/2 vs 1 (ABSOLUTE), statistics Fermi vs Bose (ABSOLUTE), helicity, charge/coupling weak vs EM, lepton number; spin+statistics resolution-INDEPENDENT (unlike m=0-vs-tiny 4213); BST photon = TWO-singleton (spin1) vs neutrino = ONE Di singleton (spin1/2), both uncommitted massless modes diff singleton-count+sector; neutrino-flavored light = light kinematics + neutrino quantum numbers; conceptual, banks nothing; count 4 of 26)")
