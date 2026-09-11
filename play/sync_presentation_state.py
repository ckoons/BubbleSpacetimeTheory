#!/usr/bin/env python3
"""Copy the single-source state block (notes/BST_PRESENTATION_STATE_BLOCK.md) into every front matter
that carries the BST_STATE_BLOCK markers. One source, many consumers, no hand copies (K1892 item 1).
Usage: python3 play/sync_presentation_state.py [--check]   (--check: exit 1 if any consumer is stale)"""
import re, sys, os, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'notes', 'BST_PRESENTATION_STATE_BLOCK.md')
B, E = '<!-- BST_STATE_BLOCK_BEGIN -->', '<!-- BST_STATE_BLOCK_END -->'
CONSUMERS = ['Guide/INDEX.md', 'Curriculum/README.md', 'Curriculum/Vol00_Foreword.md',
             'Curriculum/Spine_DIV5_QM_GR_SM/INDEX.md']
block = open(SRC, encoding='utf-8').read()
m = re.search(re.escape(B) + r'.*?' + re.escape(E), block, re.S)
assert m, 'source block lacks markers'
block = m.group(0)
check = '--check' in sys.argv
stale = 0
for rel in CONSUMERS:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        print('  [skip] %s (absent)' % rel); continue
    t = open(p, encoding='utf-8').read()
    if B not in t or E not in t:
        print('  [skip] %s (no markers)' % rel); continue
    new = re.sub(re.escape(B) + r'.*?' + re.escape(E), lambda _: block, t, flags=re.S)
    if new == t:
        print('  [ok]   %s' % rel)
    elif check:
        print('  [STALE] %s' % rel); stale += 1
    else:
        open(p, 'w', encoding='utf-8').write(new); print('  [sync] %s' % rel)
sys.exit(1 if stale else 0)
