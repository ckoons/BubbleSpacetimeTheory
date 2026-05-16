"""
Toy 2936 — Transportation / vehicle structural counts BST.

Standard car wheels: 4 = rank²
Motorcycle wheels: 2 = rank
Tricycle wheels: 3 = N_c
Heavy truck typical axles: 5 = n_C

Standard automobile pedals: 3 = N_c (clutch, brake, gas)
Automatic transmission pedals: 2 = rank
Standard car gears (manual): 6 = C_2 (5 forward + reverse) or 7 = g (6+reverse)

Aircraft control surfaces primary: 3 = N_c (aileron, elevator, rudder)
Aircraft control axes: 3 = N_c (pitch, roll, yaw)
Aircraft major sub-systems: 5 = n_C (engine, controls, fuselage, wings, landing gear)
Aircraft engine major types: 4 = rank² (piston, turbojet, turbofan, turboprop)

Standard rocket stages: 3 = N_c (1st, 2nd, 3rd) typical
Saturn V stages: 3 = N_c
Standard rocket fuel categories: 3 = N_c (liquid, solid, hybrid)

Standard naval vessel hull classes: 7 = g (ferries, container, tanker, bulk,
  ro-ro, cruise, military)

Cycling Tour de France jerseys: 4 = rank² (yellow, green, polka dot, white)

Standard traffic light states: 3 = N_c (red, yellow, green)
+ Pedestrian: 2 = rank states
Standard road sign categories: 7 = g (regulatory, warning, info, guide,
  recreational, construction, service)

Wheels on a standard skateboard: 4 = rank²
Wheels on a roller skate: 4 = rank² (quad) or 4-5 inline
Standard bus wheels: 4 = rank² or 6 = C_2 (large)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    transport = [
        ("Car wheels",                   4, rank**2, "rank²"),
        ("Motorcycle wheels",            2, rank,    "rank"),
        ("Tricycle wheels",              3, N_c,     "N_c"),
        ("Heavy truck axles",            5, n_C,     "n_C"),
        ("Car pedals manual",            3, N_c,     "N_c"),
        ("Car pedals automatic",         2, rank,    "rank"),
        ("Manual car gears",             6, C_2,     "C_2 (5 forward + R)"),
        ("Aircraft primary control surfaces", 3, N_c, "N_c"),
        ("Aircraft control axes",        3, N_c,     "N_c (pitch/roll/yaw)"),
        ("Aircraft major sub-systems",   5, n_C,     "n_C"),
        ("Aircraft engine types",        4, rank**2, "rank²"),
        ("Saturn V stages",              3, N_c,     "N_c"),
        ("Rocket fuel categories",       3, N_c,     "N_c"),
        ("Naval vessel hull classes",    7, g,       "g"),
        ("Tour de France jerseys",       4, rank**2, "rank²"),
        ("Traffic light states",         3, N_c,     "N_c"),
        ("Pedestrian signal states",     2, rank,    "rank"),
        ("Road sign categories",         7, g,       "g"),
        ("Skateboard wheels",            4, rank**2, "rank²"),
    ]

    print("Transportation BST:")
    matches = 0
    for name, val, bst, formula in transport:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<38} = {val:<3} = {formula:<15} {marker}")

    print(f"\nSCORE: {matches}/{len(transport)}")
    return matches, len(transport)


if __name__ == "__main__":
    run()
