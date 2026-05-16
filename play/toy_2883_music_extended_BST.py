"""
Toy 2883 — Extended music theory BST.

12-tone equal temperament (12-EDO): 12 = rank·C_2 (T2160)
Major scale: 7 notes = g (already known)
Pentatonic scale: 5 notes = n_C
Chromatic scale: 12 = rank·C_2
Whole tone scale: 6 = C_2
Octatonic / diminished scale: 8 = rank³
Hexatonic scale: 6 = C_2

Modes of major scale: 7 = g (Ionian, Dorian, Phrygian, Lydian, Mixolydian, Aeolian, Locrian)

Chord types primary triads: 4 = rank² (major, minor, dim, aug)
Seventh chord types: 5 = n_C (M7, m7, dom7, m7♭5, dim7)

Time signatures common: 4/4, 3/4, 6/8, 2/4 ... 4 = rank² basic
Orchestra string sections major: 4 = rank² (Vln1, Vln2, Vla, Vc, Cb → 5=n_C)

Acoustic harmonic series notes within an octave: 7 = g (within naturally)
Pythagorean ratios fundamental: 4 = rank² (1:1, 2:1, 3:2, 4:3)

Voice classifications: 6 = C_2 (Soprano, Mezzo, Alto, Tenor, Baritone, Bass)
SATB: 4 = rank²

Common percussion families: 5 = n_C (membranophone/idiophone/aerophone/chordophone/electrophone)
"""


def run():
    rank = 2; N_c = 3; n_C = 5; C_2 = 6; g = 7

    music = [
        ("12-EDO semitones in octave",       12, rank*C_2,    "rank·C_2"),
        ("Major scale notes",                7,  g,           "g"),
        ("Modes of major scale",             7,  g,           "g"),
        ("Pentatonic scale notes",           5,  n_C,         "n_C"),
        ("Whole tone scale",                 6,  C_2,         "C_2"),
        ("Octatonic / diminished",           8,  rank**3,     "rank³"),
        ("Hexatonic scale",                  6,  C_2,         "C_2"),
        ("Primary triad types",              4,  rank**2,     "rank² (M,m,dim,aug)"),
        ("Seventh chord types",              5,  n_C,         "n_C"),
        ("Pythagorean fundamental ratios",   4,  rank**2,     "rank² (1:1, 2:1, 3:2, 4:3)"),
        ("Voice classifications full",       6,  C_2,         "C_2"),
        ("SATB voices",                      4,  rank**2,     "rank²"),
        ("Hornbostel-Sachs instrument classes", 5, n_C,       "n_C"),
        ("Standard orchestra string sections", 5, n_C,        "n_C (V1,V2,Va,Vc,Cb)"),
        ("Time signature components",        2, rank,         "rank (top, bottom)"),
        ("Bach's WTC keys (12 major + 12 minor)", 24, rank**3*N_c, "rank³·N_c"),
    ]

    print("Extended music theory BST:")
    matches = 0
    for name, val, bst, formula in music:
        ok = val == bst
        if ok: matches += 1
        marker = "✓" if ok else "×"
        print(f"  {name:<44} = {val:<3} = {formula:<22} {marker}")

    print(f"\nSCORE: {matches}/{len(music)}")
    return matches, len(music)


if __name__ == "__main__":
    run()
