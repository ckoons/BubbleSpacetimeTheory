"""
Toy 5618 — Grace — Cal §823 §2: the TRAJECTORY TYPE exactly as Cal positioned it (0/1 only, no sizes):
 (a) the six free c₀ bits (αζ, βη, εζ, εη, δγ, ζη);
 (b) Lemma T's four bits for W_i — Δ (n_sj ∈ X₃), Δ′ ({B₂,n_si} ⊆ X₄; defined only under Δ-YES, else '-'), Q3, Q4 (in c₄) — and the mirror four for W_j;
 (c) X₂∩X₃, X₂∩X₄, X₃∩X₄ and the mirror three;
 (d) X_k ∩ K for k = 2,3,4 and K in the eight c₀ chains (24) and the mirror 24.
CONTROL = Cal's derived forced entries: X₂ ∋ B₁, n_sj, n_si and ∌ B₂, n_sM; X₃ ∋ B₂ and ∌ B₁, n_si, n_sM; X₄ ∋ B₁;
 Δ-NO ⟹ X₄ ⊇ {B₁, n_sj, n_si, B₂}; X₂∩{θ,γ,ε,β,α,δ} = 1; X₃∩{θ,δ} = 1; X₄∩{θ,γ} = 1; X₃∩X₄ = 1 when the hard-branch image is stuck (Lemma T).
Cal's empty-confirmation trap, respected: purity is reported THREE ways — with (b) included, with (b) excluded
(the "other 184 words" content), and (c)+(d) only. Population: the Lane F sample + all 349 (5,831 configurations).
Also the FIFTH bit (δγ ∨ ζη) on the 349 and the sample. Records hashed BEFORE counts. Grace, 2026-09-02.
"""
import hashlib, importlib.util, json, os, time, glob
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
G = load("t5599", "toy_5599_SEP2_GRACE_G1_G2_G3_laplacian_rank_chain_coincidence_leaf_table_wall_certificate.py")
T = load("t5603", "toy_5603_SEP2_GRACE_G2b_Q3Q4_phi_tunnel_on_S_leaves_and_the_334_in_frame_kills.py")
LF = load("t5614", "toy_5614_SEP2_GRACE_LANE_F_type_table_eight_chain_intersection_matrix_in_frame_census.py")
M = load("t5600g9", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1]); EA, E1, OF = M.EA, M.E1, M.OF
roles, same_chain, tau_rank = G.roles, G.same_chain, G.tau_rank
L = LF.LETTERS; PAIRS = [(L[i], L[j]) for i in range(8) for j in range(i + 1, 8)]
FREE = [PAIRS.index(p) for p in (('alpha','zeta'),('beta','eta'),('eps','zeta'),('eps','eta'),('gamma','delta'),('zeta','eta'))]
WI = (('B2', ('r', 's_i')), ('B1', ('r', 's_j'))); WJ = T.mirror_word(WI)
CTRL = Counter()
def word_bits(adj, c0, v, R, S, ch, which):
    w = WI if which == 'i' else WJ
    lg, im, X = T.stages(adj, c0, v, R, S, w); c4 = im[3]
    near, far = (R['B2'], R['n_sj']) if which == 'i' else (R['B1'], R['n_si'])
    other, sing = (R['B1'], R['n_si']) if which == 'i' else (R['B2'], R['n_sj'])
    d = 1 if far in X[2] else 0
    dp = ('-' if not d else (1 if (near in X[3] and sing in X[3]) else 0))
    sM = S['s_M']; q3 = 1 if same_chain(adj, c4, R['n_sM'], R['n_si'], sM, c4[R['n_si']], v) else 0; q4 = 1 if same_chain(adj, c4, R['n_sM'], R['n_sj'], sM, c4[R['n_sj']], v) else 0
    b = (d, dp, q3, q4)
    c = (1 if X[1] & X[2] else 0, 1 if X[1] & X[3] else 0, 1 if X[2] & X[3] else 0)
    dd = tuple(1 if (X[k] & ch[K]) else 0 for k in (1, 2, 3) for K in L)
    # controls (stated for W_i; mirror roles for W_j)
    B1, B2, nsi, nsj, nsM = (R['B1'], R['B2'], R['n_si'], R['n_sj'], R['n_sM']) if which == 'i' else (R['B2'], R['B1'], R['n_sj'], R['n_si'], R['n_sM'])
    CTRL['X2∋B1,nsj,nsi ∌B2,nsM'] += int(B1 in X[1] and nsj in X[1] and nsi in X[1] and B2 not in X[1] and nsM not in X[1])
    CTRL['X3∋B2 ∌B1,nsi,nsM'] += int(B2 in X[2] and B1 not in X[2] and nsi not in X[2] and nsM not in X[2])
    CTRL['X4∋B1'] += int(B1 in X[3]); CTRL['n'] += 1
    if not d: CTRL['ΔNO⟹X4⊇link4'] += int({B1, nsj, nsi, B2} <= X[3]); CTRL['ΔNO n'] += 1
    th, ga, de = ('theta', 'gamma', 'delta') if which == 'i' else ('theta', 'delta', 'gamma')
    CTRL['X2∩θγεβαδ=1'] += int(all(X[1] & ch[K] for K in ('theta', ga, 'eps', 'beta', 'alpha', de)))
    CTRL['X3∩θδ=1'] += int(bool(X[2] & ch['theta']) and bool(X[2] & ch[de])); CTRL['X4∩θγ=1'] += int(bool(X[3] & ch['theta']) and bool(X[3] & ch[ga]))
    if d and dp == 0 and q3 and q4: CTRL['hard&stuck⟹X3∩X4=1'] += int(bool(X[2] & X[3])); CTRL['hard&stuck n'] += 1
    return b, c, dd, all(lg)
if __name__ == "__main__":
    t0 = time.time(); out = json.load(open(os.path.join(HERE, '.out_5614.json'))); sample = out['sample']
    files = [('.in_frame_26_two_word_locked.json', 29), ('.in_frame_23_two_word_locked_n22.json', 55), ('.in_frame_44_two_word_locked_n23.json', 78), ('.in_frame_256_two_word_locked_n24.json', 122)]
    pop = [(s['n'], s['gi'], s['v'], s['col'], s['locked'], s['src']) for s in sample]
    for fn, base in files:
        for k, x in enumerate(json.load(open(os.path.join(HERE, fn)))):
            if x['n'] > 22: pop.append((x['n'], x['graph_index_plantri_c5'], x['v'], x['coloring_mod_S4_sorted_order'], True, 'witness24'))
    print("=" * 72); print(f"Toy 5618 — Grace — Cal-exact trajectory type on {len(pop)} configurations"); print("=" * 72, flush=True)
    cache = {}; recs = []
    for (n, gi, v, ct, locked, src) in pop:
        if n not in cache: cache[n] = EA.plantri_graphs(n, flags=('-c5',))
        adj = cache[n][gi]; faces, ok = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v); order = sorted(u for u in adj if u != v)
        c0 = {u: ct[k] for k, u in enumerate(order)}; R, S = roles(c0, lcyc)
        ch = LF.eight_chains(adj, c0, v, R, S); tb, ts = LF.type_of(ch); a = tuple(tb[i] for i in FREE)
        bi, ci, di, li = word_bits(adj, c0, v, R, S, ch, 'i'); bj, cj, dj, lj = word_bits(adj, c0, v, R, S, ch, 'j')
        recs.append({'n': n, 'locked': locked, 'src': src, 'a': a, 'b': bi + bj, 'c': ci + cj, 'd': di + dj, 'fifth': int(a[4] or a[5])})
    hh = hashlib.sha256(json.dumps([json.dumps(r, sort_keys=True, default=str) for r in recs]).encode()).hexdigest()
    print(f"\n  hashed BEFORE counts {hh[:32]}… [{time.time()-t0:.0f}s]")
    print(f"[CONTROL — Cal's forced entries] {dict(CTRL)}")
    lk = [r for r in recs if r['locked']]; print(f"[FIFTH BIT δγ∨ζη] locked {sum(r['fifth'] for r in lk)}/{len(lk)}; unlocked {sum(r['fifth'] for r in recs if not r['locked'])}/{sum(1 for r in recs if not r['locked'])}")
    def purity(keyf, name):
        by = defaultdict(lambda: [0, 0])
        for r in recs: by[keyf(r)][0 if r['locked'] else 1] += 1
        pureL = [k for k, v in by.items() if v[0] and not v[1]]; pureU = [k for k, v in by.items() if v[1] and not v[0]]; mixed = [k for k, v in by.items() if v[0] and v[1]]
        unl = sum(v[1] for v in by.values()); unl_pure = sum(by[k][1] for k in pureU); lkt = sum(v[0] for v in by.values()); lk_pure = sum(by[k][0] for k in pureL)
        nb = len(next(iter(by))); const = sum(1 for i in range(nb) if len({k[i] for k in by}) == 1)
        print(f"  {name}: bits {nb} (constant {const}); types {len(by)}; pure-locked {len(pureL)} · pure-unlocked {len(pureU)} · mixed {len(mixed)}; unlocked in locked-free types {unl_pure}/{unl}; locked in pure-locked types {lk_pure}/{lkt}; locked types {len([k for k,v in by.items() if v[0]])}")
        return by
    print("\n[TRAJECTORY TYPE — Cal's position]")
    purity(lambda r: r['a'] + r['b'] + r['c'] + r['d'], "FULL (a+b+c+d)")
    purity(lambda r: r['a'] + r['c'] + r['d'], "WITHOUT Lemma-T bits (a+c+d) — the other 184 words' content")
    purity(lambda r: r['c'] + r['d'], "(c)+(d) only")
    purity(lambda r: r['b'], "(b) Lemma-T bits only — expected pure by theorem for the bridge words")
    print(f"  Lemma-T bit words on locked: {dict(Counter(r['b'] for r in lk))}")
    json.dump({'hash': hh, 'ctrl': dict(CTRL), 'records': recs}, open(os.path.join(HERE, '.out_5618.json'), 'w'), default=str)
    print(f"\n  written .out_5618.json [{time.time()-t0:.0f}s]")
