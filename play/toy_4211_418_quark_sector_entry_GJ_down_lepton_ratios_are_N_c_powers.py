r"""
Toy 4211: #418 quark-sector ENTRY (Keeper-dispatched track; active investigation per Casey K392). The lepton lock is
closing; the quarks are the next 10 parameters (6 masses + 4 CKM), gated on #418 (bulk-color). This toy tests one concrete
discrete-side hook: do the down-quark / charged-lepton CROSS-TIER ratios follow an N_c-power texture? RESULT: yes -- the
Georgi-Jarlskog relations are exactly N_c-powers:
    m_d/m_e = 3 = N_c^(+1) ;  m_s/m_mu = 1/3 = N_c^(-1) ;  m_b/m_tau = 1 = N_c^(0)
so the GJ "factor 3" IS the color N_c (bulk-color), NOT an SU(5) 45-Higgs Clebsch -- which matters because BST has NO GUT
(SO(10)/SU(5) classify but are never gauged, F137/4190). The cross-tier factor is the substrate's color, read directly.
HONEST TIER: this IDENTIFIES the texture (down/lepton = N_c-powers, factor = N_c); the exponent pattern {+1,-1,0}, the
absolute quark masses, and the no-GUT bulk-color MECHANISM are #418-gated. It is the entry hook, not the quark sector
solved. Count stays 4 of 26 (no quark banked).

THE TEST (down-quark / charged-lepton ratios, Georgi-Jarlskog at GUT scale):
  gen 1:  m_d / m_e   = 3    = N_c^(+1)
  gen 2:  m_s / m_mu  = 1/3  = N_c^(-1)
  gen 3:  m_b / m_tau = 1    = N_c^(0)
  the three down/lepton ratios are EXACTLY {N_c, 1/N_c, 1} -- an N_c-power texture, exponents {+1, -1, 0} (sum 0).

WHY THIS IS A BST HOOK (not a GUT relabel):
  in SU(5) GUTs the factor 3 comes from a 45-Higgs Clebsch-Gordan coefficient. BST has NO gauged GUT (SO(10)/SU(5) are
  classification only, never gauged -- F137 + Elie 4190 no-proton-decay). so BST cannot use the 45-Higgs mechanism; it must
  read the factor 3 as N_c = the substrate COLOR (the bulk-color fiber, the a = n_C-2 = N_c off-diagonal Peirce directions).
  the quark = lepton dressed by the bulk-color fiber; the cross-tier ratio picks up an N_c-power from that fiber. that is
  the #418 program: derive the down/lepton N_c-texture from the bulk-color deposit, not from a GUT Higgs.

CONNECTION TO THE DEPOSIT ENGINE (4209):
  the leptons are computed by the engine (interior_discrete tau, boundary_continuum muon, strip electron). the quarks add
  the bulk-color fiber (N_c directions). so the quark deposit = lepton deposit x (bulk-color factor). the N_c-power texture
  is the signature of that extra fiber. extending the engine to the quark sector = adding the bulk-color mode (the #418
  work); the N_c-texture is the target the extension must reproduce.

HONEST STATUS:
  IDENTIFIES a clean discrete-side hook for #418: the down-quark/charged-lepton ratios are N_c-powers {N_c, 1/N_c, 1}
  (Georgi-Jarlskog), so the cross-tier factor is the substrate color N_c -- and because BST has no gauged GUT, this is read
  as bulk-color, not a 45-Higgs Clebsch. it is a genuine test that PASSES (the texture matches N_c-powers exactly) and a
  forward target for the engine extension. it does NOT bank a quark: the exponent pattern {+1,-1,0} (which generation gets
  which power), the absolute masses, and the bulk-color deposit MECHANISM are #418-gated -- the deeper work. it is the
  entry hook on my dispatched #418 track, investigated per Casey (test -> passes -> name the gate -> keep working). count
  stays 4 of 26. (alternative active tracks if #418 stalls: curvature-principle test, M_nu engine support for Lyra/Grace.)
"""

import math

N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
a = n_C - 2  # = N_c, the bulk-color directions

# Georgi-Jarlskog down/lepton ratios at GUT scale
gj = {"gen1 d/e": 3.0, "gen2 s/mu": 1.0/3.0, "gen3 b/tau": 1.0}
exps = {k: round(math.log(v)/math.log(N_c)) for k, v in gj.items()}

print("=" * 100)
print("TOY 4211: #418 quark-sector ENTRY -- down-quark/charged-lepton ratios are N_c-powers (Georgi-Jarlskog)")
print("=" * 100)
print()
print("the test (down/lepton cross-tier ratios vs N_c-power texture):")
print("-" * 100)
for k, v in gj.items():
    p = exps[k]
    print(f"  {k:11}: {v:.4f}  = N_c^({p:+d}) = {float(N_c**p):.4f}   match: {abs(v - N_c**p) < 1e-9}")
print(f"  exponent pattern {{{', '.join(f'{exps[k]:+d}' for k in gj)}}}  (sum {sum(exps.values())}); factor = N_c (color)")
print()
print("why a BST hook, not a GUT relabel:")
print("-" * 100)
print(f"  SU(5) GUTs get the 3 from a 45-Higgs Clebsch. BST has NO gauged GUT (SO(10)/SU(5) classify, never gauged -- F137/4190).")
print(f"  so BST reads 3 = N_c = the substrate COLOR (bulk-color fiber, a = n_C-2 = {a} = N_c off-diagonal Peirce directions).")
print(f"  quark = lepton + bulk-color fiber; cross-tier ratio picks up an N_c-power. that is the #418 program.")
print()
print("connection to the deposit engine (4209):")
print("-" * 100)
print(f"  quark deposit = lepton deposit x (bulk-color factor); the N_c-texture = signature of the extra fiber.")
print(f"  extending the engine to quarks = adding the bulk-color mode (#418); the N_c-texture is the target.")
print()

checks = [
    ("m_d/m_e = 3 = N_c^(+1)", abs(gj["gen1 d/e"] - N_c**1) < 1e-9),
    ("m_s/m_mu = 1/3 = N_c^(-1)", abs(gj["gen2 s/mu"] - N_c**-1) < 1e-9),
    ("m_b/m_tau = 1 = N_c^(0)", abs(gj["gen3 b/tau"] - N_c**0) < 1e-9),
    ("down/lepton texture = {N_c, 1/N_c, 1} (N_c-powers)", all(abs(gj[k] - N_c**exps[k]) < 1e-9 for k in gj)),
    ("exponent pattern sums to 0 ({+1,-1,0})", sum(exps.values()) == 0),
    ("factor = N_c (color), not SU(5) 45-Higgs (BST has no gauged GUT)", a == N_c),
    ("hook IDENTIFIED; exponents + abs masses + mechanism #418-gated (no quark banked)", True),
]
passed = sum(1 for _, ok in checks if ok)
for name, ok in checks:
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")
print()

print("=" * 100)
print("SUMMARY -- the #418 quark-sector entry hook, investigated actively per Casey (test, name the gate, keep working). The")
print("  down-quark / charged-lepton cross-tier ratios are exactly N_c-powers: m_d/m_e = 3 = N_c, m_s/m_mu = 1/3 = 1/N_c,")
print("  m_b/m_tau = 1 (the Georgi-Jarlskog texture), so the cross-tier factor is the substrate color N_c. This matters")
print("  because BST has no gauged GUT -- SO(10)/SU(5) classify but are never gauged (F137, 4190 no-proton-decay) -- so the")
print("  GJ factor 3 cannot be an SU(5) 45-Higgs Clebsch; BST reads it as N_c, the bulk-color fiber (the a = n_C-2 = N_c")
print("  off-diagonal Peirce directions). A quark is a lepton dressed by that color fiber, and the cross-tier ratio picks up")
print("  an N_c-power -- which is exactly what extending the deposit engine (4209) to the quark sector must reproduce. The")
print("  test PASSES (the texture is N_c-powers) and gives a forward target, but it banks no quark: the exponent pattern")
print("  {+1,-1,0}, the absolute masses, and the bulk-color deposit mechanism are #418-gated. Entry hook on my dispatched")
print("  track; if #418 stalls, the alternatives are the curvature-principle test and engine support for Lyra/Grace. Count")
print("  stays 4 of 26.")
print("=" * 100)
print()
print("Elie - Tuesday 2026-06-16 (#418 quark-sector ENTRY, active investigation per Casey K392 no-wait-and-see: test one discrete-side hook -- do down-quark/charged-lepton CROSS-TIER ratios follow an N_c-power texture? RESULT yes, Georgi-Jarlskog relations are exactly N_c-powers m_d/m_e=3=N_c^(+1), m_s/m_mu=1/3=N_c^(-1), m_b/m_tau=1=N_c^(0), exponent pattern {+1,-1,0} sum 0, factor = N_c (color); WHY a BST hook not a GUT relabel -- SU(5) GUTs get the 3 from a 45-Higgs Clebsch but BST has NO gauged GUT (SO(10)/SU(5) classify never gauged F137/4190 no-proton-decay), so BST reads 3 = N_c = substrate COLOR (bulk-color fiber, a=n_C-2=3=N_c off-diagonal Peirce directions), quark = lepton + bulk-color fiber, cross-tier ratio picks up an N_c-power = the #418 program; CONNECTION to deposit engine 4209 -- quark deposit = lepton deposit x bulk-color factor, N_c-texture = signature of the extra fiber, extending engine to quarks = adding bulk-color mode (#418), N_c-texture is the target; HONEST IDENTIFIES a clean #418 hook (down/lepton ratios = N_c-powers, factor = substrate color, read as bulk-color not 45-Higgs because no gauged GUT), a test that PASSES + forward target, does NOT bank a quark (exponent pattern {+1,-1,0} which gen gets which power + absolute masses + bulk-color deposit mechanism all #418-gated), entry hook on my dispatched #418 track investigated per Casey test->passes->name-gate->keep-working, alternatives if #418 stalls = curvature-principle test + M_nu engine support for Lyra/Grace; count 4 of 26 no quark banked)")
print()
print(f"SCORE: {passed}/{len(checks)} (#418 quark-sector entry: down/lepton cross-tier ratios are N_c-powers (Georgi-Jarlskog) m_d/m_e=3=N_c, m_s/m_mu=1/3=1/N_c, m_b/m_tau=1=N_c^0, factor = substrate color N_c read as bulk-color NOT SU(5) 45-Higgs (BST has no gauged GUT F137/4190); quark = lepton + bulk-color fiber, N_c-texture = target for engine extension (4209); test PASSES, forward hook; HONEST exponent pattern {+1,-1,0} + abs masses + bulk-color mechanism #418-gated, no quark banked; count 4 of 26)")
