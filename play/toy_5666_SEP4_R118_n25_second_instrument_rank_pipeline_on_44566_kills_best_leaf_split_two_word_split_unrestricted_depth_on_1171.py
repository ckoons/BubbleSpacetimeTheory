#!/usr/bin/env python3
"""
Toy 5666 — Grace, 2026-09-04 — n = 25 SECOND INSTRUMENT (Keeper 09:00 item 3; Casey's decision: n = 25 enters Paper 1).
Population: Elie 5600's n = 25 in-frame kills (.in_frame_one_word_n25.json, 44,566 records (n, gi, v, colouring) — the stuck
colourings with NO direct one-word exit), 5-connected sphere triangulations from plantri -c5 at n = 25 (23,384 graphs).
Part B (toy 5603 Part B verbatim at n = 25, my rank instrument + my stage/leaf code): tau0 = 6 on every record, positive control
(direct one-word exit = 0 on all), best leaf over the 186-word context family: G (gate in one word) vs S (no one-word gate).
  Elie's numbers on the board (5601, 00:52): 43,395 gate in one word · 1,171 in two words. Second instrument, not blind.
Part C (toy 5625 verbatim): unrestricted plain-swap Kempe depth to the gate on my S-leaf list (Elie 5664a runs his column now;
  prior n = 24: max 4, unreached 0; his prereg 49670a3b).
Part D (new): the two-word split of the S leaves — from each fully-legal word image (all stuck), apply the family again; a
  configuration is 'direct at two words' if some second word is insertable, 'gate at two words' if some reaches tau <= 5,
  'deeper' otherwise. Elie: 1,113 gate + 58 direct + 0 deeper.
Hashes: the record list is hashed BEFORE the counts; my S-leaf witness list is hashed BEFORE the diff with Elie's
.in_frame_1171_two_word_locked_n25.json (Keeper: witness lists hashed before comparison).
"""
import hashlib, importlib.util, json, os, sys, time, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name, fname):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fname)); mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod
T3 = load("t5603", glob.glob(os.path.join(HERE, "toy_5603_*.py"))[0].split('/')[-1])
T5 = load("t5625", glob.glob(os.path.join(HERE, "toy_5625_*.py"))[0].split('/')[-1])
M = load("t5600g", glob.glob(os.path.join(HERE, "toy_5600_*.py"))[0].split('/')[-1])
OF, EA, IF, E1, WF = M.OF, M.EA, M.IF, M.E1, M.WF
stages, roles, leaf, insertable, tau_rank = T3.stages, T3.roles, T3.leaf, T3.insertable, T3.tau_rank
t0 = time.time()
kills = [eval(k) if isinstance(k, str) else tuple(k) for k in json.load(open(os.path.join(HERE, '.in_frame_one_word_n25.json')))['kills']]
kills = [(n, gi, v, tuple(ct)) for (n, gi, v, ct) in kills]
hK = hashlib.sha256(json.dumps(kills).encode()).hexdigest()
print(f"[population] {len(kills)} n = 25 kill records, hashed BEFORE counts {hK[:16]}; graphs {len(set(k[1] for k in kills))}", flush=True)
moves, words, _ = WF.context_family(); print(f"[family] {len(words)} words", flush=True)
gs = EA.plantri_graphs(25, flags=('-c5',)); print(f"[plantri] n = 25 -c5: {len(gs)} graphs [{time.time()-t0:.0f}s]", flush=True)
LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else None
B = []; S_list = []
for k, (n, gi, v, ct) in enumerate(kills[:LIMIT]):
    adj = gs[gi]; faces, ok = OF.faces_of(adj)
    order = sorted(u for u in adj if u != v); c0 = {u: ct[i] for i, u in enumerate(order)}
    lcyc = E1.link_cycle(faces, v); tau0 = tau_rank(adj, c0, v); rl = roles(c0, lcyc)
    rec = {'gi': gi, 'v': v, 'tau0': tau0, 'roles': rl is not None}
    if rl is None or tau0 != 6: B.append(rec); continue
    R, S = rl; best = 'S'; direct = gate = legal_n = 0; s_images = []
    for w in words:
        legal, imgs, chains = stages(adj, c0, v, R, S, w)
        if not all(legal): continue
        legal_n += 1; c4 = imgs[3]
        if insertable(adj, c4, v): direct += 1; best = 'I'
        elif tau_rank(adj, c4, v) <= 5:
            gate += 1
            if best != 'I': best = 'G'
        else: s_images.append(c4)
    rec['family'] = {'legal_words': legal_n, 'direct': direct, 'gate': gate, 'best': best}
    if best == 'S': S_list.append((n, gi, v, ct, s_images))
    B.append(rec)
    if (k + 1) % 2000 == 0: print(f"  [B] {k+1}/{len(kills)} best so far {dict(Counter(x['family']['best'] for x in B if x.get('family')))} [{time.time()-t0:.0f}s]", flush=True)
ok = [x for x in B if x.get('family')]
print(f"\n[B] tau0 {dict(Counter(x['tau0'] for x in B))}; roles {sum(1 for x in B if x['roles'])}/{len(B)}; POSITIVE CONTROL direct hits {sum(1 for x in ok if x['family']['direct']>0)}/{len(ok)}", flush=True)
print(f"[B] BEST LEAF: {dict(Counter(x['family']['best'] for x in ok))}   (Elie 5601: G 43,395 · S 1,171)", flush=True)
wit = sorted((gi, v, ct) for (n, gi, v, ct, _) in S_list); hW = hashlib.sha256(json.dumps(wit).encode()).hexdigest()
json.dump({'hash': hW, 'witnesses': wit}, open(os.path.join(HERE, f'.out_{N}_S_witnesses_n25.json'), 'w'))
print(f"[B] my S-leaf witness list: {len(wit)}, hashed BEFORE the diff: {hW[:16]}", flush=True)
E = json.load(open(os.path.join(HERE, '.in_frame_1171_two_word_locked_n25.json')))
ew = sorted((x['graph_index_plantri_c5'], x['v'], tuple(x['coloring_mod_S4_sorted_order'])) for x in E)
print(f"[B] DIFF with Elie's 1,171: mine {len(wit)} · his {len(ew)} · common {len(set(wit)&set(ew))} · mine-only {len(set(wit)-set(ew))} · his-only {len(set(ew)-set(wit))}", flush=True)
# Part C: unrestricted depth on my S list
depths = Counter(); unreached = 0; expanded_tot = 0
for (n, gi, v, ct, _) in S_list:
    adj = gs[gi]; order = sorted(u for u in adj if u != v); c0 = {u: ct[i] for i, u in enumerate(order)}
    d, expanded, _ = T5.depth_to_gate(adj, c0, v)
    expanded_tot += expanded
    if d is None: unreached += 1
    else: depths[d] += 1
print(f"\n[C] unrestricted plain-swap depth to the gate on {len(S_list)}: {dict(sorted(depths.items()))}; unreached {unreached}; states expanded {expanded_tot}   (n = 24 prior: max 4, unreached 0) [{time.time()-t0:.0f}s]", flush=True)
# Part D: two-word split
two = Counter(); det = []
for j, (n, gi, v, ct, s_images) in enumerate(S_list):
    adj = gs[gi]; faces, ok2 = OF.faces_of(adj); lcyc = E1.link_cycle(faces, v)
    verdict = 'deeper'; n_direct = n_gate = 0
    for c4 in s_images:
        rl = roles(c4, lcyc)
        if rl is None: continue
        R, S = rl
        for w in words:
            legal, imgs, chains = stages(adj, c4, v, R, S, w)
            if not all(legal): continue
            c8 = imgs[3]
            if insertable(adj, c8, v): n_direct += 1
            elif tau_rank(adj, c8, v) <= 5: n_gate += 1
        if n_direct: break
    verdict = 'direct' if n_direct else ('gate' if n_gate else 'deeper')
    two[verdict] += 1; det.append((gi, v, verdict, n_direct, n_gate, len(s_images)))
    if (j + 1) % 100 == 0: print(f"  [D] {j+1}/{len(S_list)} {dict(two)} [{time.time()-t0:.0f}s]", flush=True)
print(f"\n[D] TWO-WORD SPLIT on {len(S_list)}: {dict(two)}   (Elie: gate 1,113 · direct 58 · deeper 0) [{time.time()-t0:.0f}s]", flush=True)
json.dump({'kills_hash': hK, 'witness_hash': hW, 'B_best': dict(Counter(x['family']['best'] for x in ok)), 'C_depths': dict(depths), 'C_unreached': unreached, 'D_two_word': dict(two), 'D_detail': det}, open(os.path.join(HERE, f'.out_{N}.json'), 'w'))
print("written", f".out_{N}.json", flush=True)
