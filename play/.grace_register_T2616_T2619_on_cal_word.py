#!/usr/bin/env python3
"""Grace — registration of T2616–T2619 (Round 120, G6). RUN ONLY ON CAL'S WORD (C1/C2 posted).
Writes: registry rows (notes/BST_AC_Theorem_Registry.md, appended after the T2615 row), both graph files
(play/ac_graph_data.json theorems+nodes+edges+metadata; play/ac_theorem_graph.json nodes+edges), play/THEOREM_LOG.md,
claim files -> registered. Edge orientation: from = INPUT -> to = CONSEQUENCE (ac_graph_data {from,to,source,label};
ac_theorem_graph {source,target,type}). Prints the edges touching each new node afterwards (the 09-02 lesson).
Usage: python3 .grace_register_T2616_T2619_on_cal_word.py --cal-word "§NNN, HH:MM" [--only T2616,T2617]
"""
import json, sys, os, re, datetime, subprocess
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here)
args = sys.argv[1:]
if '--cal-word' not in args:
    print('REFUSED: pass --cal-word "<Cal section, time>" — nothing registers without it'); sys.exit(1)
calword = args[args.index('--cal-word') + 1]
only = None
if '--only' in args: only = set(args[args.index('--only') + 1].split(','))
today = datetime.date.today().isoformat()
stamp = subprocess.run(['date', '+%H:%M'], capture_output=True, text=True).stdout.strip()

ROWS = {
 'T2616': dict(
  name='Re s = 1/2 is the Mellin-unitarity axis of the dilation group (classical; the critical LINE, not the points on it; D_IV^5 consistent with, not supplying, the axis)',
  status='derived', depth=0,
  status_long=f'DERIVED (classical: Plancherel for the Mellin transform on L²(R+, dx/x); Nyman–Beurling–Báez-Duarte frame, K1862 C.1; ceiling per K1508: the axis, not the points; Cal\'s word {calword})',
  section='Round 120 G6 (harvest advance 4; K1862 seam i)', toys=[],
  plain='A classical fact: the Mellin transform is an isometry on exactly one vertical line, Re s = 1/2, because that is where the dilation group x -> ax acts unitarily; D_IV^5 is consistent with that choice, it does not make it. The functional equation s <-> 1 - s is the reflection in that line, so zeros of any L-function with the functional equation come in pairs symmetric about it. This pins the LINE the zeros are symmetric about; it says nothing about whether they sit ON it (that is RH).',
  proofs=['Mellin–Plancherel', 'Nyman–Beurling'],
  registry=f'| T2616 | RE s = ½ IS THE MELLIN-UNITARITY AXIS (harvest advance 4; K1862 seam i; Round 120 G6; Cal {calword}): the Mellin transform (Mf)(s) = ∫ f(x) x^s dx/x is a unitary isomorphism L²(ℝ₊, dx/x) → L²(c + iℝ) exactly for c = ½ (Plancherel; the half-density weight), i.e. Re s = ½ is the axis on which the dilation group ℝ₊ acts unitarily. CLASSICAL (Mellin–Plancherel on L²(dx); Cal §852 wording): the axis is the criterion\'s own measure choice; the rank-one dilation sector of SO₀(5,2)\'s principal series is CONSISTENT WITH it (its self-dual point restricts to it, F694/F988) and does not SUPPLY it. Consequence: the functional-equation involution s ↔ 1 − s is the reflection in this axis, so the zero set of any L-function with that functional equation is SYMMETRIC ABOUT Re s = ½. SCOPE (K1508 ceiling, verbatim in substance): this pins the LINE, not the POINTS; RH is the strictly stronger statement that the zeros lie on the axis; nothing here touches Weil positivity. Target-innocent: the axis is fixed by unitarity before ζ is named. Consistent with: T2562 (the derived dilation operator; operator class = coordinate shifts on a Hardy space, K1862 C.2), F988 (Lyra: s ↔ 1 − s is a frame reflection, not time-reversal). NO edge to K21 (retracted; F988\'s firewall corrected 2026-09-06). | DERIVED — CLASSICAL (Mellin–Plancherel; Cal §852: register as classical, D_IV⁵ clause "consistent with"; the corpus\'s own exercise of the frame: K1862-B Gram instrument, Báez-Duarte rate within 2 %) | graph-node (number theory / RH row) | — | {today} |',
  edges=[(2562, 2616, 'derived', 'CONSISTENT WITH (Cal §852): the derived dilation operator (Hardy-space shifts) acts unitarily on this axis; the axis is classical, not supplied by D_IV^5')]),
 'T2617': dict(
  name='Odd-p local densities of Z^5 and Z^{1,4} coincide for every N, and the rule is parity of the number of variables (holds for every even complement rank, fails for every odd one)',
  status='proved', depth=0,
  status_long=f'PROVED (K1862-C Lemma 1: Hensel-lifting count, validated by convolution at p = 3, 5, 7, e ≤ 4 and p = 11, 13 to N = 300 by Elie 5693/5694; family rule swept by Grace 5698: exact constancy of the definite/indefinite ratio at n = 2, 4, 6, N-dependence at n = 3, 5, 7; Elie E1 5693 P3 confirmed; Cal §852: no word owed, Keeper\'s PROVED stands)',
  section='Round 120 G6 (K1862-C Lemma 1; K1862 seam iv)', toys=[5693, 5698],
  plain='For an odd number of variables, how many solutions a quadratic form has modulo a prime power does not depend on the sign of the determinant, so the Lorentzian form x0² − x1² − … − x4² and the sum of five squares count the same at every odd prime. With an even number of variables a quadratic character of the determinant enters and the two differ. Five is odd; that is the whole reason.',
  proofs=['Hensel lifting (K1862-C Lemma 1)', 'family sweep 5698'],
  registry=f'| T2617 | ODD-p LOCAL DENSITIES OF ℤ⁵ AND ℤ^{{1,4}} COINCIDE FOR EVERY N — A PARITY-OF-DIMENSION FACT (K1862-C Lemma 1 + the family rule; Round 120 G6; Cal {calword}): for a unimodular form in m variables over ℤ_p, p odd, N = p^e u, p ∤ u: α_p(N) = 1 + (u/p)p⁻² (e = 0), 1 − p⁻⁴ (e = 1), (1 − p⁻⁴) + p⁻³α_p(N/p²) (e ≥ 2) at m = 5, the SAME for ℤ⁵ and ℤ^{{1,4}} because for ODD m the sign of the determinant enters only through the character of (−1)^{{m/2}}·det, which is absent; for EVEN m the two forms\' densities differ for generic N. FAMILY RULE (Grace 5698, can-fail, held): with R(n) := [r_{{n+1}}(N)/α₂^def(N)]/[r*_n(N)/α₂^ind(N)] (same 2-adic normalisation both sides), R(n) is N-INDEPENDENT at n = 2, 4, 6 (exact 16, 3840, 829 440 = vol(Sⁿ)/vol(Pⁿ)) and N-DEPENDENT at n = 3, 5, 7 (relative spreads 1.7, 0.30, 0.083, N ≤ 30). So the lemma holds for D_IV⁵\'s cone because n_C + 1 = 5 is odd, and for every even n; it fails for every odd n — a "coincidence at n = 4" reading is excluded. Validation: convolution = recursion at p = 3, 5, 7 (Keeper), p = 11, 13 to N = 300 (Elie 5694 P3), blind re-run 5693 (P3). | PROVED (Hensel count; family-swept) | graph-node (number theory / RH row) | 5693, 5694, 5698 | {today} |',
  edges=[]),
 'T2618': dict(
  name='The cone-zeta of D_IV^5 (Siegel-weighted orbit count on the Vinberg chamber of Z^{1,4}) equals the Epstein zeta of the sum of five squares divided by 3840, coefficient by coefficient, and counts positive-definite quaternary lattices by determinant',
  status='derived', depth=0,
  status_long=f'DERIVED, blind-confirmed (Elie 5693 8/8 re-run of the definition; Elie 5695a: r*(N)·3840 = r₅(N) all N ≤ 200; Grace 5697 prereg f3d5197b: r*(N) = 2^{{ω_odd(N)}} Σ_{{L adm}} 1/|O(L)| class for class vs Nipp on 67 squarefree N ≤ 108; Grace 5698: 3840 = vol(S⁴)/vol(P⁴); Grace 5699: ℤ^{{1,4}} ⊗ ℤ₂ ≅ ℤ⁵ ⊗ ℤ₂ exhibited; Keeper K1862-A/C, K1863 §2; Cal\'s word {calword})',
  section='K1863 §2 / K1862-A / K1862-C (Round 120 G6)', toys=[5693, 5695, 5697, 5698, 5699],
  plain='Take the light-cone form t² − x² − y² − z² − w² on the integers, count the vectors of each norm N in one fundamental chamber, weighting each by one over the size of its symmetry group. That list of numbers is exactly the number of ways to write N as a sum of five squares, divided by 3840. So the geometry\'s own zeta function is the classical five-squares Epstein zeta. The same list counts four-dimensional positive lattices of determinant N (the orthogonal complements of the vectors), weighted the same way.',
  proofs=['Vinberg chamber + Siegel mass', 'Z_2-isometry (quaternion of norm -1)', 'Nipp cross-check 5697', 'genus theta at n = 8 (5699b)'],
  registry=f'| T2618 | THE CONE-ZETA OF D_IV⁵ IS THE FIVE-SQUARES EPSTEIN ZETA OVER 3840, AND COUNTS POSITIVE QUATERNARY LATTICES BY DETERMINANT (K1863 §2; K1862-A/C; Round 120 G6; Cal {calword}). DEFINITION (K1862-A): Q = x₀² − Σ₁⁴ xᵢ², Γ = O⁺(Q, ℤ), Vinberg chamber x₁ ≥ x₂ ≥ x₃ ≥ x₄ ≥ 0, x₀ ≥ x₁ + x₂ + x₃ (simple roots e₂−e₁, e₃−e₂, e₄−e₃, −e₄, e₀+e₁+e₂+e₃; sub-diagram {{r₂,r₃,r₄,r₅}} = affine B̃₃, the cusp), r*(N) := Σ_{{x ∈ chamber, Q(x) = N}} 1/|W_x| with W_x the parabolic stabilizer; Z_cone(s) := Σ r*(N) N^{{−s}}. IDENTITY: **r*(N)·3840 = r₅(N)** (the sum-of-five-squares count) for every N (Elie 5695a, N ≤ 200, exact), i.e. Z_cone(s) = ζ_{{ℤ⁵}}(s)/3840: functional equation π^{{−s}}Γ(s)Z(s) = π^{{−(5/2−s)}}Γ(5/2−s)Z(5/2−s), symmetry line Re s = 5/4, poles at 0 and 5/2, NO Euler product (normalised a_N = r₅(N)/10: a₆ = 24 ≠ a₂a₃ = 4·8 = 32, i.e. r₅(6) = 240 ≠ 320 — Cal §852; K1862-C Lemma 2). REASON: ℤ^{{1,4}} and ℤ⁵ are ℤ_p-isometric at every p — odd p by T2617, p = 2 by the quaternion of norm −1 (A = diag(1, L_q), Aᵀ J A = I₅ mod 2⁴⁰, Grace 5699; invariants rank 5, det 1, oddity 5 ≡ 1 + 4·7 mod 8) — both genera are one-class, so Siegel\'s local products coincide and only the archimedean factor differs. ONE REASON FOR 3840 (Cal §852 seam closed by G7): Siegel\'s mass formula across the signature — vol(P⁴)/vol(S⁴) = mass(genus(I₅)) — and the rank-5 odd unimodular genus is the single class I₅, so 3840 = vol(S⁴)/vol(P⁴) = (8π²/3)/(π²/1440) = 1/mass = |O(ℤ⁵)| = 2⁵·5!: one identity read three ways (Grace 5698 Chiswell χ(P⁴) = 1/1920 = Ratcliffe–Tschantz; Elie 5695a\'s orbit-count factor). NOT a BST integer; the hyperoctahedral NAME |W(B_{{n+1}})| is not the general one (fails at n = 2, 6 where the 2-adic data differ: 16 vs 48, 829 440 vs 645 120). QUATERNARY READING (K1862-C; Grace 5697, prereg f3d5197b): for primitive x, L = x^⊥ is a positive-definite integer-Gram quaternary lattice of det N and r*(N) = 2^{{ω_odd(N)}} · Σ_{{L: c_L a square mod N}} 1/|O(L)| — exact on all 67 squarefree N ≤ 108 against Nipp\'s tables, class for class (472 classes appear, 722 inadmissible never do, |O(L)| reproduced on every one). So Z_cone is the Siegel-mass series of quaternary lattices by determinant = the five-squares Epstein zeta; Ibukiyama–Saito\'s D*₄ is the same object seen through the complements (Elie 5695a: NOT a constant multiple of D*₄ or D₄ — the 2-adic factor is not constant). The D_IV⁵-specific content is the chamber/orbit bookkeeping, invisible in the Dirichlet series. FAMILY RULE (Grace 5699/5699b, prereg 31498868 + c6a2b919): for 4 | n the cone-zeta of ℤ^{{1,n}} is the unnormalised GENUS THETA Σ_{{L ∈ genus(I_{{n+1}})}} r_L(N)/|O(L)| of the odd unimodular lattices of rank n + 1 and vol(Pⁿ)/vol(Sⁿ) = mass(genus) — Siegel\'s mass formula across the signature; at n = 8 the genus is {{I₉, E₈ ⊕ ℤ}} and r*_8(N) = r₉(N)/(2⁹·9!) + r_{{E₈⊕ℤ}}(N)/(2·|W(E₈)|) exactly (20/20, 13 ≤ N ≤ 20 blind), R(8) = 2786918400/17 = 1/mass; at n = 2, 6 the 2-adic oddities differ and no such identity holds. So the n = 4 value is the one-class case of the same Siegel identity. | DERIVED (blind-confirmed; three independent instruments + external table; family-swept) | graph-node (number theory / RH row) | 5693, 5695, 5697, 5698, 5699 | {today} |',
  edges=[(2617, 2618, 'proved', 'odd-p local densities coincide: input to the genus-theory reason for the exact identity')]),
 'T2619': dict(
  name='The five-squares Epstein zeta (= 3840 × the cone-zeta of D_IV^5) has (b) a certified zero BEYOND its abscissa of absolute convergence and (a) 26 zeros inside the strip off its symmetry line below T = 60: D_IV^5\'s own arithmetic zeta is a Davenport–Heilbronn object',
  status='exhibited', depth=0,
  status_long=f'EXHIBITED (Elie 5695d: s = 2.50358998764350548… + 14.2799957055120199… i, |Λ| = 3.6×10⁻³⁸, winding 1, BEYOND the abscissa Re s > 5/2 [meaning (b)]; Cal §852 second instrument |Λ| = 2.2×10⁻²⁶ there; ρ = 2s vs Travěnec–Šamaj pinned; differs from the published digit string at the fifth decimal; Elie 5695b: 13 on-line + 26 in-strip off-line zeros [meaning (a)] in [−½, 3] × (0.1, 60]; Cal\'s word {calword})',
  section='K1863 §3 (Round 120 G6)', toys=[5695],
  plain='The geometry\'s own zeta function has a zero that is not on its line of symmetry — in fact one that sits beyond the edge where its series still converges absolutely, which an Euler product could never do — checked to twenty digits by two independent programs and by counting how the function winds around a small box; and inside the strip it has 26 more zeros off the line below height 60. Riemann\'s zeta is conjectured never to do this. So the cone\'s arithmetic looks like Riemann\'s in every way that a proof of RH usually uses, and yet fails RH: any proof that would work for both is wrong. The difference is that Riemann\'s coefficients multiply (the Euler product) and these do not.',
  proofs=['approximate functional equation + argument principle (5695d)', 'Travěnec–Šamaj 2021'],
  registry=f'| T2619 | THE CONE-ZETA VIOLATES RH BY A CERTIFIED OFF-LINE ZERO (T-DH landed; K1863 §3; Round 120 G6; Cal {calword}): with Z(s) = Σ r₅(N)N^{{−s}} (= 3840·Z_cone, T2618), strip [0, 5/2], symmetry line Re s = 5/4, Elie 5695d refines Travěnec–Šamaj\'s listed off-critical zero of the d = 5 hypercubic Epstein zeta by the rotated-splitting approximate functional equation (checked at 8×10⁻³⁰ against 90-digit references): **s = 2.5035899876435054856 + 14.279995705512019903 i, |Λ| = 3.6×10⁻³⁸, winding number 1 on a 0.01-box; mirror 5/2 − s likewise**; in their units 2·Re s = 5.00717997528701, all fifteen published digits reproduced. The zero sits OUTSIDE the strip, beyond the abscissa of absolute convergence — the Soundararajan–Thorne class. TWO FACTS, TWO MEANINGS OF "OFF-LINE" (Cal §852 C1): (b) the certified zero is BEYOND THE ABSCISSA, Re s − 5/2 = 0.00359 > 0, in the half-plane of absolute convergence — the Davenport–Heilbronn class exactly (an Euler product cannot vanish there; T2618 has none); (a) inside the strip, Elie 5695b counts in [−½, 3] × (0.1, 60]: 39 zeros, 13 on Re s = 5/4 and 26 off it (13 mirror pairs; the box straddles both). CONVENTION PINNED (Cal §852, second instrument written from scratch, theta-split incomplete gamma, 40 dps, N ≤ 120): Travěnec–Šamaj\'s variable is ρ = 2s (their strip [0, 5], line 5/2), so 5695d\'s halving is right; Cal\'s |Λ| = 2.2×10⁻²⁶ at Elie\'s point against 4.6×10⁻¹² at 10⁻⁴ offsets; at the PUBLISHED T–Š point (halved) both instruments give |Λ| = 1.76×10⁻¹², so the certified zero DIFFERS FROM THE PUBLISHED DIGIT STRING AT THE FIFTH DECIMAL of the imaginary part (≈4×10⁻⁵) — stated as a difference, not as their typo, until checked with the authors. CONSEQUENCES: F1014\'s "the n_C = 5 odd-quinary arithmetic beats Davenport–Heilbronn" is REFUTED with a witness; harvest advance 6 CLOSED-NEGATIVE (definitional by K1862-C, exhibited here); the BARRIER LEMMA (K1863 §5, Cal C2): any argument proving "all zeros on the symmetry line" from properties shared by ζ and Z (positive coefficients, meromorphic continuation with finitely many poles, functional equation with gamma factors, vertical polynomial growth, theta origin) is invalid — every proof of RH must use multiplicativity, the Euler product = the independence of the finite fields. | EXHIBITED (certified numerically by two instruments, winding 1; literature point; Cal §852 word given with the (a)/(b) split) | graph-node (number theory / RH row) | 5695 | {today} |',
  edges=[(2618, 2619, 'derived', 'the identity makes the Epstein zero a statement about the cone-zeta of D_IV^5'), (2617, 2619, 'proved', 'K1863 §8: from T2617')]),
}

reg = os.path.join(root, 'notes', 'BST_AC_Theorem_Registry.md')
gd_p = os.path.join(here, 'ac_graph_data.json'); gt_p = os.path.join(here, 'ac_theorem_graph.json')
gd = json.load(open(gd_p, encoding='utf-8')); gt = json.load(open(gt_p, encoding='utf-8'))
existing = {t['tid'] for t in gd['theorems']}
colors = {n['domain']: n.get('color') for n in gt['nodes']}
color = colors.get('number_theory') or '#8E6BBF'
regtxt = open(reg, encoding='utf-8').read()
lines = regtxt.split('\n')
anchor = max(i for i, l in enumerate(lines) if l.startswith('| T2615 |') or re.match(r'\| T261[6-9] \|', l))
added = []
for tid_s, R in ROWS.items():
    if only and tid_s not in only: continue
    tid = int(tid_s[1:])
    if tid in existing or any(l.startswith(f'| {tid_s} |') for l in lines):
        print('SKIP (already present):', tid_s); continue
    # registry
    anchor += 1; lines.insert(anchor, R['registry'])
    # ac_graph_data
    rec = dict(tid=tid, name=R['name'], domain='number_theory', status=R['status_long'], depth=R['depth'], conflation=0,
               section=R['section'], toys=R['toys'], date=today, plain=R['plain'])
    gd['theorems'].append(rec); gd['nodes'].append(dict(rec))
    for (a, b, src, lab) in R['edges']:
        assert a in existing or a in {int(k[1:]) for k in ROWS}, ('dangling from', a)
        gd['edges'].append(dict({'from': a, 'to': b, 'source': src, 'label': lab}))
        gt['edges'].append({'source': f'T{a}', 'target': f'T{b}', 'type': 'uses'})
    gt['nodes'].append(dict(id=tid_s, name=R['name'], domain='number_theory', domain_label='Number theory / RH row',
                            status=R['status'], plain=R['plain'], color=color, proofs=R['proofs']))
    existing.add(tid); added.append(tid_s)
    # claim file
    for cf in os.listdir(os.path.join(here, '.claims')):
        if cf.startswith(f'theorem_{tid_s}_'):
            p = os.path.join(here, '.claims', cf); s = open(p).read().replace('Status: claimed', 'Status: registered')
            open(p, 'w').write(s + f'Registered: {today} {stamp} on Cal\'s word ({calword})\n')
    with open(os.path.join(here, 'THEOREM_LOG.md'), 'a') as f:
        f.write(f"| {tid_s} | {R['name'][:80]} | D{R['depth']} | {R['section']}; Cal {calword} | {','.join(map(str, R['toys'])) or '—'} | Grace | {today} | {R['status']} |\n")
gd['metadata'].update(node_count=len(gd['nodes']), edge_count=len(gd['edges']), theorem_count=len(gd['theorems']), synced=f'{today} both lists (Grace G6)')
gd['meta']['max_tid'] = f"T{max(existing)}"; gd['meta']['last_updated'] = today
open(reg, 'w', encoding='utf-8').write('\n'.join(lines))
json.dump(gd, open(gd_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
json.dump(gt, open(gt_p, 'w', encoding='utf-8'), indent=1, ensure_ascii=False)
print('registered:', added, '| ac_graph_data', len(gd['theorems']), len(gd['nodes']), len(gd['edges']), '| ac_theorem_graph', len(gt['nodes']), len(gt['edges']))
for tid_s in added:
    tid = int(tid_s[1:])
    print(tid_s, 'edges (from -> to):', [(e['from'], e['to']) for e in gd['edges'] if tid in (e['from'], e['to'])],
          '| theorem_graph:', [(e['source'], e['target']) for e in gt['edges'] if tid_s in (e['source'], e['target'])])
# dangling check
ids = {t['tid'] for t in gd['theorems']}
print('dangling:', [e for e in gd['edges'][-10:] if e['from'] not in ids or e['to'] not in ids])
