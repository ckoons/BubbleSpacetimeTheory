# Lane D — the granular band structure render: mass = resistance to hopping across the 2^g cells

*Grace | 2026-07-20a | Lane D of the condensate study. Render the effective-mass picture concrete: the 2^g=128 Reed–Solomon substrate cells (Paper #122) as a granular lattice; **mass = effective mass = resistance to hopping across the band gaps**; the mass ordering = hopping-difficulty = boundary-reach ordering; the top at the band edge (level 127=M_g), the deficit = the last band gap. Tier: LEAD / mechanism-render. This is the mechanism UNDER Lane A's band-edge computation — I render the structure; Elie does the effective-mass numerics; Lyra computes the last gap (which decides 127/128).*

## The lattice — 2^g = 128 substrate cells (GF(2^g) Reed–Solomon)
The substrate codes on GF(2^g) = GF(128): **2^g = 128 discrete cells**, indexed 0…127. Read as a 1-D granular lattice (a crystal of 128 sites), a fermion mode is a Bloch state hopping across the cells, and:
```
  mass = effective mass  m* = ℏ² / (d²E/dk²)   — resistance to hopping across the gaps
```
Flat band (easy hopping, small curvature⁻¹) → light; steep band edge (hard hopping, large gap) → heavy. **The mass ordering is the hopping-difficulty ordering, which is the boundary-reach ordering** (heaviest = most boundary-localized = hardest to delocalize across the lattice).

## The band diagram (rendered)
```
  boundary  (continuum, level 128) ═══════════════════════════════  the Shilov boundary — where O sits (spherical)
                                    ▲  ← LAST BAND GAP (127→128): the deficit.
   level 127 = M_g  ── TOP ─────────┤     Lane A computes this gap:
                                    │       = 1/2^g  → y_t = M_g/2^g = 127/128 DERIVED
   level ~126       ── (charm) ─────┤       = 0      → y_t = 1 exact + RG, 127/128 retired
                                    │       = other  → computed CG < 1, a new prediction
   level ~govs      ── (up) ────────┤
        ⋮                           │   deeper levels = lighter fermions
   level 1          ── (electron) ──┤     (flatter bands, easy hopping, small m*)
   level 0          ── (vacuum) ────┘
```
- The **top** sits at the outermost usable code level **127 = M_g** (the g-th Mersenne prime — the last symbol before the field wraps at 2^g). It's the most boundary-localized fermion, so it's the heaviest and the hardest to delocalize.
- The **deficit** — the one level the top can't cross to reach the boundary condensate O (at the continuum, level 128) — is the **last band gap (127→128)**. That gap IS the y_t deficit. Casey's "precipitate that falls just short of the boundary and loses a bit of its tail" = the top sitting one band-gap below the continuum.

## Why this is the mechanism under Lane A (not a competing story)
The band picture and the discrete-series picture are the same object in two languages:
- **discrete-series address (a,b)** = which band level the top sits at (Lane A, Lyra);
- **λ₂=½ → 0 gap** (non-spherical top → spherical boundary O) = **the last band gap** (level 127 → continuum);
- **⟨t|O⟩ deficit** = the hopping amplitude across that last gap;
- **candidate 1/2^g** = one cell-width out of 2^g cells = one code-unit.
So Lane D renders WHY the deficit is a "band gap" and WHY the natural unit is 1/2^g (one cell of 128); **Lane A computes whether the gap is exactly that.** The render does NOT decide it — compute-don't-fit holds (the gap must be computed, the 1/2^g is the candidate unit, not the answer).

## The angular half → g−2 (the per-cell field coupling)
The band has two halves: the **radial** half (hopping across cells → mass, above) and the **angular** half (the field coupling within a cell). Casey's connect: the **per-cell field coupling = the anomalous magnetic moment** — a_e = (g−2)/2 is how much a fermion's moment deviates from the bare Dirac value, and in the granular picture that deviation is the mode's coupling to the field *within* its cell (the sub-cell structure), distinct from the inter-cell hopping that sets mass. This is a LEAD (the a_e = per-cell-coupling identification is a picture, not yet a computation) — but it's structurally clean: **mass = inter-cell (radial) resistance; g−2 = intra-cell (angular) coupling** — the same radial/angular split as the Yukawa (radial overlap × angular CG) and the two-currents split (Lane C: P² linear/radial vs W² angular).

## Tier catalog (Lane D)
| item | tier |
|---|---|
| 2^g=128 cells = RS lattice (Paper #122) | **DERIVED** (banked substrate structure) |
| mass = effective mass = resistance to hopping (m* = ℏ²/(d²E/dk²)) | **LEAD / mechanism-render** (the picture; Elie does the numerics) |
| mass ordering = hopping-difficulty = boundary-reach ordering (t>c>u) | **DERIVED-clean** (boundary-reach ordering is established; the *hopping* language is the render) |
| top at level 127=M_g, deficit = last band gap (127→128) | **LEAD** (the candidate assignment; Lane A must force "level 127", compute the gap) |
| deficit = 1/2^g (one cell of 128) | **CANDIDATE** (the natural unit; Lane A computes whether the gap equals it — do NOT fit) |
| g−2 = per-cell (intra-cell angular) field coupling | **LEAD** (structurally clean radial/angular split; not yet a computation) |

## Net
- **Rendered** the granular band structure: 128 RS cells as a lattice, mass = resistance to hopping, top at the band edge (level 127=M_g), deficit = the last band gap (127→128), mass ordering = hopping-difficulty = boundary-reach ordering.
- **Located it as the mechanism under Lane A:** the last band gap = the λ₂ gap = the ⟨t|O⟩ deficit; 1/2^g = one cell of 128 (the candidate unit). Lane A computes the gap; the render doesn't decide it.
- **Radial/angular split rendered consistently:** mass = inter-cell radial hopping; g−2 = intra-cell angular coupling — the same split as the Yukawa (Lane A) and the two currents (Lane C).
- **Tiers held:** the lattice DERIVED; boundary-reach ordering DERIVED-clean; the effective-mass picture and the top-at-127 assignment and the g−2 identification all LEAD; 1/2^g the candidate unit (compute-don't-fit).

— Grace, 2026-07-20a. Lane D render: 2^g=128 RS cells as a granular lattice; mass = effective mass = resistance to hopping across band gaps (m* = ℏ²/(d²E/dk²)); top at the band edge (level 127=M_g), deficit = the last band gap (127→continuum) = the λ₂ gap = ⟨t|O⟩ deficit; candidate unit 1/2^g = one cell of 128. Mass ordering = hopping-difficulty = boundary-reach ordering (t>c>u, DERIVED-clean). g−2 = intra-cell angular coupling (LEAD) — same radial/angular split as the Yukawa and the two currents. Mechanism-render under Lane A; the render does NOT decide the gap (compute-don't-fit). Tiers: lattice DERIVED; hopping-picture + top-at-127 + g−2 all LEAD; 1/2^g candidate unit.
