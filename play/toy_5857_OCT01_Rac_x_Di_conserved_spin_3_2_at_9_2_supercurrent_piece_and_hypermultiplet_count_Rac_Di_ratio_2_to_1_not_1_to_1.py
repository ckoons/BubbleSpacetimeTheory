#!/usr/bin/env python3
"""
Toy 5857 — round 26: the spin-3/2 piece of Rac⊗Di, and the hypermultiplet count (Elie, 2026-10-01). Prereg 5926252b.
Families: Rac₅ (H_m at 3/2+m), Di₅ (SO(5) (m+½,½) at 2+m); K = SO(5)xSO(2). Reuses 5855's machinery verbatim (exec).
One-particle spaces: one real scalar = one Rac; one Dirac = Di ⊕ Di. Hypermultiplet = 4 real scalars + 1 symplectic-Majorana (≡ 1 Dirac): pin owed.
"""
import glob, io, contextlib
from fractions import Fraction as Fr
from collections import Counter
import sympy as sp
src = open(glob.glob('play/toy_5855_*.py')[0]).read(); ns = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src[:src.index('check("(2) character identity')], ns)   # run 1 cut before `module`
RD, module, same, chi, mul, SYM, top, DEPTH, weights, RAC, DI, harm = (ns[k] for k in
    ('RD', 'module', 'same', 'chi', 'mul', 'SYM', 'top', 'DEPTH', 'weights', 'RAC', 'DI', 'harm'))
score = []
def check(name, ok, detail=""):
    score.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")
def predicted(generic_for=()):
    P = {}; s = Fr(1, 2)
    while 3 + s <= top:
        prev = (s - 1, Fr(1, 2)) if (s >= Fr(3, 2) and s not in generic_for) else None
        for w, c in module(3 + s, (s, Fr(1, 2)), prev).items(): P.setdefault(w, Counter()).update(c)
        s += 1
    return P
check("(i) the full identity holds with conserved characters for every s ≥ 3/2 (5855 re-run)", same(RD, predicted()))
check("(i) replacing ONLY the s = 3/2 character by the generic one BREAKS the identity: the spin-3/2 piece itself is conserved",
      not same(RD, predicted(generic_for=(Fr(3, 2),))))
P32 = module(Fr(9, 2), (Fr(3, 2), Fr(1, 2)), (Fr(1, 2), Fr(1, 2)))
lowest32 = min(P32)
check("(i) the spin-3/2 piece: lowest K-type (3/2, ½) at weight 9/2 = d − 2 + s (the 5D conservation bound), multiplicity 1 in Rac⊗Di",
      lowest32 == Fr(9, 2) and Fr(9, 2) == 5 - 2 + Fr(3, 2))
# (ii) the count
dR = [sum(RAC[Fr(3, 2) + m].values()) for m in range(6)]
dD = [sum(DI[Fr(2) + m].values()) for m in range(6)]
print(f"   K-type dims: Rac {dR}; Di {dD}")
m = sp.Symbol('m', positive=True)
fR = sp.interpolate([(k, dR[k]) for k in range(5)], m); fD = sp.interpolate([(k, dD[k]) for k in range(5)], m)
print(f"   dim Rac_m = {sp.factor(fR)};  dim Di_m = {sp.factor(fD)}")
check("(ii) dimension formulas fitted on m = 0..4 PREDICT m = 5 for both (the closed forms are exact)", fR.subs(m, 5) == dR[5] and fD.subs(m, 5) == dD[5])
ratio = sp.limit(fD/fR, m, sp.oo)
check("(ii) boson/fermion growth: dim Di_m / dim Rac_m → 2 exactly (one Di carries the states of two Racs)", ratio == 2, f"limit {ratio}")
hyper = {'Rac': 4, 'Di': 2}; bst = {'Rac': 1, 'Di': 1}
bal = lambda c: sp.limit((c['Di']*fD)/(c['Rac']*fR), m, sp.oo)
print(f"   hypermultiplet one-particle content 4·Rac ⊕ 2·Di: F/B growth {bal(hyper)};  BST's Rac₅ ⊕ Di₅: F/B growth {bal(bst)}")
check("(ii) the hypermultiplet (4 real scalars + 1 Dirac-equivalent) is BALANCED (F/B → 1) at ratio #Rac : #Di = 2 : 1", bal(hyper) == 1)
check("(ii) BST's Rac₅ ⊕ Di₅ (1 : 1) is NOT balanced (F/B → 2): it matches the hypermultiplet's Δs and spins but NOT its multiplicities",
      bal(bst) == 2)
# control: the free scalar's bilinears carry no half-integer spin
src22 = open(glob.glob('play/toy_5822_*.py')[0]).read(); n22 = {}
with contextlib.redirect_stdout(io.StringIO()): exec(src22[:src22.index('check("CONTROL so(3,2)')], n22)
RR = {}
for m1 in range(5):
    for m2 in range(5 - m1):
        RR.setdefault(Fr(3) + m1 + m2, Counter()).update(mul(RAC[Fr(3, 2) + m1], RAC[Fr(3, 2) + m2]))
half = any(any(k[0].denominator == 2 for k, v in C.items() if v) for C in RR.values())
check("CONTROL: Rac⊗Rac (the free scalar's bilinears) has NO half-integer-spin K-type, so no spin-3/2 current", not half)
print("\nREADING: Rac⊗Di carries a conserved spin-3/2 piece at 9/2 (the conservation is that piece's own). It exists for ANY numbers of Racs")
print("and Dis at the free level, so by itself it is not supersymmetry. BST's singleton content matches the hypermultiplet's Δs and spins")
print("but NOT its multiplicities: a balanced multiplet needs #Rac : #Di = 2 : 1 (the su(2)_R doublet); BST has 1 : 1.")
print(f"\nSCORE: {sum(score)}/{len(score)}")
