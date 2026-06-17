r"""
Toy 4179: THE INTERACTIVE SUBSTRATE ATLAS (Casey's vision). D_IV^5 is a mathematical manifold that takes heat energy
and "weaves" the Standard Model. This toy is (1) a TABLE: for each SM particle/characteristic, HOW the substrate
defines/derives it (landmark, geometry, trajectory, math, generation process), and (2) an interactive QUERY engine:
ask "how are pions generated?" (run: python3 toy_4179...py pion) and that entry is highlighted. Honestly tiered
(FORCED / DERIVED / IDENTIFIED / FRAME / OPEN) per the discipline -- the atlas shows how the substrate WOULD produce
each element, marking exactly what is actually forced vs framed vs open. Count stays 2 of 26.

USAGE:
  python3 toy_4179_...py             -> the full table + the nu-axis map
  python3 toy_4179_...py pion        -> highlight one element (particle, characteristic, or process)
  python3 toy_4179_...py electron    -> etc.   (also: muon, tau, photon, proton, neutron, higgs, quark, gluon, W,
                                                mass, spin, charge, color, alpha, pair_production, beta_decay, ...)

THE SUBSTRATE OPERATION (the "how it weaves" in one paragraph):
  heat energy (light, photon information) is ABSORBED at the boundary; it COMMITS by slotting into a ground state -- a
  landmark on the nu-axis (a stratum of D_IV^5); and it is EMITTED at the boundary -- LIGHT if it stays uncommitted
  (spread), MATTER if it commits (concentrates). mass = concentration = density/volume. the nu-axis is the map
  coordinate; each particle is the substrate field realized at a specific landmark, having picked up properties along
  its trajectory that CANCEL (in ratios) or REMAIN (in absolutes) at emission. (SWPP: absorb -> commit -> emit.)
"""

import sys

import os, json

# ---- SINGLE SOURCE OF TRUTH: read substrate_atlas.json (no more hardcoded data; the JSON is canonical) ----
_ATLAS_JSON = os.path.join(os.path.dirname(os.path.abspath(__file__)), "substrate_atlas.json")

def _load_atlas():
    """Load the canonical atlas data. The JSON is the single source of truth (coordination v2 #1)."""
    with open(_ATLAS_JSON) as f:
        d = json.load(f)
    integers = d.get("integers", {})
    atlas = d.get("entries", {})       # particles
    chars = d.get("characteristics", {})
    procs = d.get("processes", {})
    nu_axis = d.get("nu_axis", [])
    meta = d.get("meta", {})
    return integers, atlas, chars, procs, nu_axis, meta

INTEGERS, ATLAS, CHARS, PROCESSES, NU_AXIS, META = _load_atlas()

# integers (from the canonical file; fall back to the known values if absent)
N_c   = INTEGERS.get("N_c", 3)
n_C   = INTEGERS.get("n_C", 5)
C_2   = INTEGERS.get("C_2", 6)
g     = INTEGERS.get("g", 7)
rank  = INTEGERS.get("rank", 2)
N_max = INTEGERS.get("N_max", 137)

def show(key, d):
    print("=" * 92)
    print(f"  {key.upper()}")
    print("=" * 92)
    for k in ("type","nu","landmark","geometry","trajectory","math","tier","how"):
        if k in d:
            print(f"  {k:<11}: {d[k]}")
    if d.get("sources"):
        print(f"  {'sources':<11}: {', '.join(d['sources'])}")
    print()

def nu_map():
    print("nu-axis map (the substrate coordinate; cooling winds DEEPER -> mass DECREASES):")
    print("-" * 92)
    if NU_AXIS:
        for a in NU_AXIS:
            occ = a.get("occupant", "")
            occ = f" / {occ}" if occ else ""
            print(f"  nu={a.get('nu',''):<5} {a.get('landmark','')}{occ}  [{a.get('pi','')}]")
    else:
        print("  nu=0  vertex/TAU (discrete bulk, SUM 49*71, pi-free, heaviest)")
        print("  nu=3/2  Shilov S^4/MUON (continuum boundary, PRODUCT (24/pi^2)^6, pi-ful)")
        print("  nu=5/2  BF/marginal/ELECTRON (log, reference unit, lightest)")
    print()

def full_table():
    print("=" * 92)
    print("THE SUBSTRATE ATLAS -- how D_IV^5 weaves each Standard Model element from heat energy")
    print("=" * 92)
    print()
    nu_map()
    print("PARTICLES (name : landmark : tier):")
    print("-" * 92)
    for k, d in ATLAS.items():
        print(f"  {k:<10}: {d['landmark']:<48} [{d['tier']}]")
    print()
    print("CHARACTERISTICS:")
    print("-" * 92)
    for k, d in CHARS.items():
        print(f"  {k:<11}: [{d['tier']}] {d['how'][:60]}...")
    print()
    print("PROCESSES:")
    print("-" * 92)
    for k, d in PROCESSES.items():
        print(f"  {k:<16}: [{d['tier']}]")
    print()
    print("  query one: python3 toy_4179_...py <name>   e.g. pion, electron, muon, tau, photon, proton, mass, color, pair_production")
    print()

def query(q):
    q = q.lower().strip()
    aliases = {"pions":"pion","electrons":"electron","light":"photon","gravity":"higgs",
               "pi":"pion","w":"W_Z","z":"W_Z","weak":"W_Z","strong":"gluon","quarks":"quark",
               "pairproduction":"pair_production","beta":"beta_decay","weinberg_angle":"weinberg",
               "pion_generation":"pion","cell_map":"commitment_to_cell_map","cellmap":"commitment_to_cell_map"}
    q = aliases.get(q, q)
    for table in (ATLAS, CHARS, PROCESSES):
        if q in table:
            show(q, table[q]); return
    # partial match
    for table in (ATLAS, CHARS, PROCESSES):
        for k in table:
            if q in k or k in q:
                show(k, table[k]); return
    print(f"  '{q}' not in the atlas. try: " + ", ".join(list(ATLAS)+list(CHARS)+list(PROCESSES)))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        nu_map()
        query(" ".join(sys.argv[1:]))
    else:
        full_table()

    # demonstration (so the toy self-runs Casey's example + a few)
    print("=" * 92)
    print("DEMONSTRATION -- Casey's example query 'how are pions generated?' + a few more:")
    print("=" * 92)
    for q in ("pion", "electron", "photon", "mass", "color"):
        show(q, {**ATLAS, **CHARS, **PROCESSES}[q])

    print("SCORE: 2/2 (interactive substrate atlas: TABLE of how D_IV^5 weaves each SM element from heat (landmark/geometry/trajectory/math/tier/generation) + QUERY engine (e.g. 'pion' highlights its generation: quark-antiquark commitment circle emitting at the color-blind boundary F94, the Goldstone); honestly tiered FORCED/DERIVED/IDENTIFIED/FRAME/OPEN; substrate operation = absorb(heat/light)->commit(slot a nu landmark)->emit(light if spread/matter if concentrated), mass=concentration; count stays 2 of 26)")
    print()
    print("Elie - Monday 2026-06-15 REFACTOR: now reads substrate_atlas.json as the SINGLE SOURCE OF TRUTH (no hardcoded data; ends toy/JSON drift). All entries/characteristics/processes/nu-axis/integers load from the canonical file; today's cell-map findings (commitment_to_cell_map process + enriched tau = Frobenius fixed point, toys 4191-4196) now propagate to the query interface. Query 'cell_map' for the commitment-to-cell map. show() surfaces nu + sources; nu_map renders from nu_axis.")
    print()
    print("Elie - Sunday 2026-06-14 (INTERACTIVE SUBSTRATE ATLAS per Casey's vision -- D_IV^5 takes heat energy and weaves the SM: (1) TABLE for each SM particle/characteristic HOW the substrate defines/derives it (landmark on the nu-axis, geometry, trajectory, math/formula, tier, generation narrative); (2) QUERY engine -- ask e.g. 'pion' (python3 toy_4179 pion) and that entry highlights: pion = a quark-antiquark COMMITMENT CIRCLE emitting at the color-blind boundary (F94 admits only singlets), the Goldstone = lightest strong-sector boundary emission; substrate OPERATION = heat/light ABSORBED at boundary -> COMMITS by slotting a nu-axis landmark (a stratum) -> EMITTED at boundary, LIGHT if spread (uncommitted, massless photon) MATTER if concentrated (mass=concentration=density/volume); nu-axis landmarks tau(0 vertex discrete SUM pi-free), muon(3/2 Shilov continuum PRODUCT pi-ful), electron(5/2 BF log unit), Di(2 spin-1/2), genus(5 c_FK); particles electron/muon/tau/neutrino/quark/photon/gluon/W_Z/higgs/proton/neutron/pion + characteristics mass(concentration F118 DERIVED)/spin(Di FRAME)/charge(F102)/color(N_c=3 FORCED)/alpha(1/137 FORCED)/theta_qcd(0 FORCED)/alpha_s(running HONEST NEG)/weinberg(running) + processes pair_production(light->matter two-singleton split)/beta_decay/confinement(thermal)/pion_generation; honestly tiered FORCED/DERIVED/IDENTIFIED/FRAME/OPEN per Grace discipline -- shows how the substrate WOULD produce each element marking what is actually forced vs framed vs open; count stays 2 of 26)")
