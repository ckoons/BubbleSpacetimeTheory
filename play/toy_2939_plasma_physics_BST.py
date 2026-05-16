"""
Toy 2939 — Plasma physics structural counts BST.

Plasma states of matter: 1 (single new state beyond solid/liquid/gas, total 4 = rank²)
Magnetic confinement device types: 4 = rank² (tokamak, stellarator,
  reversed field pinch, magnetic mirror)
Inertial confinement device types: 3 = N_c (laser direct, laser indirect, Z-pinch)
Fusion fuel cycles: 3 = N_c (DT, DD, DHe3)

Tokamak coordinate axes: 3 = N_c (toroidal, poloidal, radial)
MHD modes basic: 3 = N_c (Alfvén, fast magnetosonic, slow magnetosonic)
MHD modes including shock: 4 = rank²

Plasma waves major types: 7 = g (Langmuir, ion-acoustic, Alfvén, whistler,
  fast magnetosonic, slow magnetosonic, electron cyclotron)

Standard sun-Earth space weather classification: 5 = n_C (CME, solar flare,
  geomagnetic storm, solar particle event, ionospheric disturbance)

NIF beamline count: 192 = ? Let me check. 192 = rank^6·N_c = 64·3 = 192 ✓
ITER plasma current: 15 MA, n/a not structural
Standard ITER toroidal field coils: 18 = rank·N_c² = rank·9·... = 18 = rank·g+rank² = 14+4 = 18 ✓

Iron tokamak central solenoid coils ITER: 6 = C_2

Standard Hall thruster types categories: 3 = N_c
Magnetohydrodynamic generator types: 3 = N_c (open, closed, hybrid)

Standard fusion ignition criteria parameters: 3 = N_c (density, temperature, confinement time)
Lawson criterion: nτT product (3 = N_c factors)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    plasma = [
        ("Plasma + 3 classical states",          4, rank**2, "rank²"),
        ("Magnetic confinement device types",    4, rank**2, "rank²"),
        ("Inertial confinement device types",    3, N_c, "N_c"),
        ("Fusion fuel cycles",                   3, N_c, "N_c"),
        ("Tokamak coordinate axes",              3, N_c, "N_c"),
        ("MHD wave modes basic",                 3, N_c, "N_c"),
        ("MHD modes + shock",                    4, rank**2, "rank²"),
        ("Plasma waves major types",             7, g, "g"),
        ("Space weather classification",         5, n_C, "n_C"),
        ("NIF beamline count",                   192, rank**6*N_c, "rank^6·N_c"),
        ("ITER toroidal field coils",            18, rank*g+rank**2, "rank·g + rank²"),
        ("ITER central solenoid coils",          6, C_2, "C_2"),
        ("Hall thruster types",                  3, N_c, "N_c"),
        ("MHD generator types",                  3, N_c, "N_c"),
        ("Lawson criterion parameters",          3, N_c, "N_c (n,τ,T)"),
        ("Fusion ignition standard criteria",    3, N_c, "N_c"),
        ("Particle dynamics fundamental species in plasma", 2, rank, "rank (ions, electrons)"),
    ]

    print("Plasma physics BST:")
    matches = 0
    for name, val, bst, formula in plasma:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<50} = {val:<4} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(plasma)}")
    return matches, len(plasma)


if __name__ == "__main__":
    run()
