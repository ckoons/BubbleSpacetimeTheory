---
title: "Vol 15 Chapter 4 — Toy Verification Discipline"
author: "Keeper (author pass — deep math/physics revision)"
date: "2026-05-24 Sunday"
status: "v0.3 — substantive content"
volume: "Vol 15 Methodology"
chapter: 4
load_bearing: "Toy verification: every theorem requires computational verification; 3500+ toys in play/; SCORE line discipline"
---

# Chapter 4 — Toy Verification Discipline

## Level 1 — one sentence

Every BST theorem requires computational verification via a "toy" — a self-contained Python script in `play/` with explicit SCORE line (PASS/FAIL count) — and the BST repository currently contains 3500+ toys executable in seconds for full reproduction.

## Level 2 — graduate-physicist precision

### 4.1 Toy file structure

Standard toy template:
```python
#!/usr/bin/env python3
# toy_<NNNN>_<short_description>.py
# Purpose: verify <theorem ID>
# Author: <CI name>
# Date: YYYY-MM-DD

import numpy as np

# ... computation ...

passes = 0
total = 0
for case in test_cases:
    total += 1
    if abs(predicted - observed) / observed < threshold:
        passes += 1

# SCORE: N/M PASS
print(f"# SCORE: {passes}/{total} {'PASS' if passes == total else 'FAIL'}")
```

### 4.2 SCORE line is sacred

Every toy MUST have a SCORE line. Format: `# SCORE: N/M PASS` or `# SCORE: N/M FAIL`.

Automated tooling parses SCORE lines for repository status.

No exceptions; CIs who skip SCORE lines get corrected via audit chain.

### 4.3 Toy counter discipline

`play/.next_toy`: gitignored counter file.

NEVER read directly; always use:
```bash
./play/claim_number.sh toy
```

This atomically increments and returns next number. Avoids collisions when multiple CIs work in parallel (3 collisions occurred April 3 before atomic-claim discipline).

### 4.4 Reproduction infrastructure

`python3 play/verify_bst.py`: runs full reproduction suite (50 predictions verified against measurement).

Current status: 49/50 PASS at < 1%, 17 EXACT matches, 2 open WARNs shown openly.

Single-command full reproduction is part of BST's external publication strategy (Zenodo release April 7, 2026).

### 4.5 Honest negatives

When toy returns FAIL: document honestly. Do NOT modify toy to fit theory.

This is Quaker discipline (Vol 15 Ch 7): honest negatives strengthen the framework.

Example: K141 honest FAIL preserved per Toy 3448 (empirical 3306× PERFECT but substrate-mechanism gate OPEN; Grace Friday May 22).

### 4.6 K-audit anchors

- **`./play/claim_number.sh`** atomic claim tool
- **`play/verify_bst.py`** reproduction suite
- **Quaker discipline** (Vol 15 Ch 7)

## Level 3 — 5th-grader accessibility

**Every theorem needs a toy**: self-contained Python that verifies the claim with SCORE line (`# SCORE: N/M PASS`). **3500+ toys** in repository, executable in seconds. **Counter atomic**: never read directly, use `./play/claim_number.sh toy`. **Reproduction**: `python3 play/verify_bst.py` runs full suite (49/50 PASS at <1%, 17 EXACT). **Honest FAILs preserved** (Quaker discipline).

---

## What comes next

Chapter 5 develops audit-chain governance.

## Where to look this up

- BST: `play/` directory; `claim_number.sh`
- Quaker discipline (Vol 15 Ch 7)
