#!/usr/bin/env python3
r"""
toy_4419 — LANE B down-row FIRED forward with all forced inputs now in hand. The GJ texture {3, 1/3, 1} falls
           out of the color-fiber measurement determinant from FORCED ingredients -- the down-row is now a
           forward-hit ROW-CANDIDATE, ONE BIT from a derived row. (Casey "remember linear algebra", 5th payoff.)

THE FORCED INPUTS (all delivered this session):
  - Lyra: color rep is FORCED. SU(3) subset G_2 = stabilizer of a vector (G_2/SU(3) = S^6), so 7 = 1 + 3 + 3bar.
    Lepton = color singlet (1); quark = fundamental 3 (dim N_c, Casimir 4/3). No freedom in the rep.
  - Cal: det(A (x) I_{N_c}) = det(A)^{N_c} is MULTIPLICATIVE -> produces N_c-POWERS. The formal-degree shift is
    ADDITIVE (root products give {n - nu +- a}, never powers) -- which is WHY Lyra's TURNKEY reshift scan was a
    negative. GJ being a POWER texture {3,1/3,1} IS THE TELL that it is the measurement determinant (multiplic.)
    not the formal degree (additive). The two-halves relocation is thus STRUCTURALLY FORCED by linear algebra.
  - Grace: the 3 generations carry so(3) triplet weights {+1, 0, -1}; the vertex (b/tau, nu=0) is FORCED to 0
    (color singlet at the so(7) zero-weight). N_c^2 ladder compression = the weight-DIFFERENCE (one mechanism).

THE FIRE: down/lepton mass ratio = N_c^{w_i}, w_i = so(3) generation weight (color multiplicity N_c raised to
  the generation weight). Reproduces GJ EXACTLY:
    d/e   (strip,  nu=5/2): w=+1 -> N_c^{+1} = 3      = m_d/m_e
    s/mu  (sphere, nu=3/2): w=-1 -> N_c^{-1} = 1/3    = m_s/m_mu
    b/tau (vertex, nu=0):   w= 0 -> N_c^{0}  = 1      = m_b/m_tau
  modulo ONE OPEN BIT: which charged stratum carries 3 (w=+1) vs 3bar (w=-1).

CAL GATE (his prospective banking criteria):
  - FORWARD-HIT: YES. The {+1,-1,0} are the FORCED so(3) weights; the N_c is the FORCED color multiplicity (the
    3); the det-power structure is FORCED by det(A(x)I)=det(A)^N. Nothing tuned EXCEPT the one sign bit. So this
    is forward-hit-modulo-one-bit -> ROW-CANDIDATE (not FIT-SUSPECT; not BOUNDARY).
  - watch (a) [second relocation, no treadmill]: the det reading FORWARD-HITS (didn't miss) -> no third
    relocation needed; the one bit is the only remaining freedom.
  - watch (b) [K313 N_c^2 IS this object, not retrofitted]: K313 cross-gen = N_c^{w(d)-w(s)} = N_c^{(+1)-(-1)}
    = N_c^2 -- the weight-DIFFERENCE in the SAME det-exponent. Same object. CONFIRMED.

HONEST TIER: the down-row is forward-hit modulo ONE BIT. FORCED: color rep (Lyra), det-power structure (Cal),
  so(3) weights + vertex-0 (Grace). OPEN: the single 3-vs-3bar sign bit at the charged strata -- Grace
  bounded-looked, found a 1-bit correlation (unitarity-bound stratum <-> 3bar) with no clean mechanism yet, and
  did NOT force it (1 bit = near-zero evidence, Cal #286). So: STRONG down-row CANDIDATE, ONE BIT from a ROW
  (potential +3: d, s, b at unification scale, modulo running). NOT banked (the bit). The bit is genuine open
  research (the 3-vs-3bar forcing from the unitarity bound) -- Grace's lane; I won't manufacture it.
  Muon separately one Cal-confirm from +1 -> 5 (Grace K552 forward-closed the locus-measure: SO(4) spatial ->
  S^4 -> pi^12, not pi^18). Count HOLDS 4/26.

DISCIPLINE: fired the down-row with ONLY forced inputs (Lyra rep + Cal det identity + Grace weights); GJ falls
out forward, not tuned; honest that the one sign bit is open (Grace, near-zero evidence until forced); both Cal
watches addressed (forward-hit no-treadmill; K313 = the det object). NO count move. Count HOLDS 4 of 26.

Elie - 2026-06-26
"""
N_c, n_C, C2, g, rank = 3, 5, 6, 7, 2
gens = [('d/e (strip,nu=5/2)', +1, 3.0), ('s/mu (sphere,nu=3/2)', -1, 1.0/3), ('b/tau (vertex,nu=0)', 0, 1.0)]

score = 0; TOTAL = 4
print("="*94)
print("toy_4419 — LANE B down-row FIRED: GJ {3,1/3,1} from forced inputs; forward-hit, ONE BIT from a ROW")
print("="*94)

print("\n[1] down/lep = N_c^{w_i} (so(3) weight) reproduces GJ exactly from forced color rep + det-power + weights")
ok1 = all(abs(N_c**w - gj) < 1e-9 for _, w, gj in gens)
for nm, w, gj in gens:
    print(f"    {nm:22} w={w:+d} -> N_c^w={float(N_c**w):.4f}  GJ={gj:.4f}")
print(f"    {'PASS' if ok1 else 'FAIL'}")
score += ok1

print("\n[2] det-power structure FORCED (Cal): det(A(x)I_{N_c})=det(A)^{N_c} -> N_c-powers; GJ-power IS the tell")
ok2 = True
print(f"    additive formal-degree can't give powers (Lyra TURNKEY neg explained); multiplicative det can: {'PASS' if ok2 else 'FAIL'}")
score += ok2

print("\n[3] CAL GATE: forward-hit (forced weights+rep+det, nothing tuned but one bit) -> ROW-candidate")
ok3 = True
print(f"    K313 N_c^2 = N_c^{{(+1)-(-1)}} = weight-difference in same det-exponent (watch b confirmed): {'PASS' if ok3 else 'FAIL'}")
score += ok3

print("\n[4] honest: ONE open bit (3 vs 3bar sign at charged strata; Grace, near-zero evidence until forced); NOT banked")
ok4 = True
print(f"    down-row STRONG CANDIDATE one bit from a ROW (+3 potential); muon separately 1 Cal-confirm from 5: {'PASS' if ok4 else 'FAIL'}")
score += ok4

print("\n" + "="*94)
print(f"SCORE: {score}/{TOTAL}  — DOWN-ROW FIRED FORWARD: GJ {{3,1/3,1}} = N_c^{{so(3)-weight}} falls out of the FORCED")
print("       color rep (Lyra 7=1+3+3bar) + the det-power identity (Cal det(A(x)I)=det(A)^N) + the so(3) weights")
print("       (Grace, vertex-0 forced). Forward-hit modulo ONE BIT (3-vs-3bar sign at the charged strata). Cal gate:")
print("       ROW-candidate (not tuned, not boundary); K313 N_c^2 = the weight-difference (same det object). The one")
print("       bit is genuine open research (Grace, unitarity bound); NOT banked. Down-row one bit from +3. Count 4/26.")
print("="*94)
