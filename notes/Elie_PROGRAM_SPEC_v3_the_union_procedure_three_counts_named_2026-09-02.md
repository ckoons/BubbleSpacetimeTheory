---
title: "PROGRAM SPEC v3 — THE UNION PROCEDURE, measured in frame (5-connected triangulations through n = 23, 1,591,509 stuck colorings): bridge; if the image is stuck, middle then bridge; if the middle word is illegal, the next middle-touching orbit. Three counts named: W_legal(c), Im(c), W_acting(c). Depth two everywhere measured; one-word fails on 93 witnesses; nothing is proved."
author: "Elie"
date: "2026-09-02, Wednesday (clock-verified 10:23 EDT, stamp copied from a separate render)"
status: "v3 (supersedes v2's one-word program, which is FALSE in frame — 5600/5601). Every number is a measurement; the lemma is never the theorem; 4CT is an INPUT (frame d3). H_cut (5609) amends Section 6 when it lands."
---

# 0. What changed since v2
v2's program was one word long and was measured out of frame only. In the frame where a minimal counterexample
lives (internally 6-connected ⟹ 5-connected, min degree 5), the one-word form FAILS: 93 stuck colorings through
n = 23 have no fully-legal family word reaching even the gate phase (5600/5601; witness files
.in_frame_26/23/44_two_word_locked*.json; one hand-verified by an independent code path). Every measured
configuration exits within TWO words; none needs three (1,591,509 through n = 23; n = 24 running).

# 1. Inputs (unchanged from v2 except the frame)
T a sphere triangulation, 4-colorable by 4CT (INPUT); v of degree 5; c a proper 4-coloring of T−v with τ_v = 6.
The canonical context (One-Context, proved) supplies roles B₁, n_sM, B₂, n_si, n_sj and colors r, s_M, s_i, s_j.
The alphabet 𝒜: 186 words (15 context-moves × ordered distinct pairs; 93 mirror orbits). A word acts as a
four-stage commutator m₁m₂m₁m₂; it is applied only when FULLY LEGAL (each stage's seed carries a pair color).

# 2. The three counts, named (per configuration c)
- **W_legal(c)** := #{w ∈ 𝒜 : all four stages legal at c, image proper, image ≠ c}. Measured in frame: 8–28,
  typically 22–24 (5601/5609). The bridge words W_i, W_j are ALWAYS in W_legal (Lemma L, 374,658/374,658).
  The middle canonical word is in W_legal at only 40% of stuck configurations (5608: illegal on 225,505 of
  374,658 — the sub-joint SJ is real in frame).
- **Im(c)** := #distinct images {w·c : w counted in W_legal(c)} (words collide on images; 5609 reports the
  medians).
- **W_acting(c)** := #{w counted in W_legal(c) : supp(w) ≠ ∅} — by construction equal to W_legal(c) under the
  image ≠ c clause; reported separately so a future definition change cannot silently merge them.

# 3. The union procedure (one round = at most two words)
```
union(c):
  if gate(c):                                   return c                       # gate = a color absent at v, or τ ≤ 5
  # step 1 — BRIDGE
  for w in {W_i, W_j} (both fully legal, Lemma L):   if gate(w·c): return w·c   # 1,215,272 / 1,216,851 at n=23 direct
  # step 2 — MIDDLE, in the stuck image's OWN canonical frame, then BRIDGE again
  for c' in {W_i·c, W_j·c} (stuck):
      for M in the four middle-touching orbits, in order:
            (n_sM,(r,s_M))(n_si,(s_M,s_i)) · (B,(r,s_i))(B,(r,s_M)) · (n_si,(r,s_i))(n_sM,(s_M,s_i)) · (B,(r,s_j))(B,(r,s_M))
          if M fully legal at c'  and  gate(M·c'):                      return M·c'
          if M fully legal at c'  and  some bridge word W' in (M·c')'s frame has gate(W'·M·c'):  return W'·M·c'
  REFUSE                                          # never fired on 1,591,509 stuck colorings through n = 23
```
Measured regimes (5608, n ≤ 22): bridge-then-middle exits 373,447/374,658; middle-then-bridge exits
147,814/374,658 (the middle word is illegal on 225,505; fails on 1,339). On the 93 two-word witnesses:
middle→bridge 93/93, bridge→middle 19/93 — the hard regime is Casey's practice. The second word on the 93 is
ALWAYS a bridge word (5605); the first word must touch s_M (four orbits; three shapes).

# 4. Halting bound and output
Two words in the measured world (≤ 3 Kittell switches, 5606). Output: a coloring of T−v with a color absent at
v after ≤ 1 swap, hence a 4-coloring of T; plus the certificate (the one or two words, their stage chains).

# 5. What the procedure certifies, and what it does not
It certifies DGT in two-word form on everything measured. It does not certify 4CT. **The one lemma a proof in
this shape needs (K1840 (iii)): at every bridge-locked configuration some legal middle-touching word's chains
contain the cut C(c) = X₃ ∩ X₄ of the bridge word** — H_cut, MEASURED (5611): DEAD in that form. On the 93, the
words that contain the cut are the bridge words themselves and they fail; the exiting words touch the cut
partially, fully, or not at all, and the cut is nonempty after them. The mechanism the data selects is
re-routing (the exiting word's chains leave the bridge worlds), not containment — Lyra's third door. The one-word hitting set
grows with n in frame (3 → 14 → 21 for out-of-frame → n=21 → n=22; 5595/5602), so no finite one-word pattern
table exists there; the two-word union is a FIXED alphabet (1 bridge orbit + 4 middle-touching orbits).

# 6. Which toy IS the program; which are instruments about it
IS: toy_5608's `program(adj, tv, lcyc, c0, BRIDGE, MIDDLE)` and its reverse, unioned (the two-regime
procedure); the 5601 BFS is the program with unrestricted second word. Instruments ABOUT it: 5596 (class
insertability), 5600/5601 (depth census), 5602 (hitting-set growth), 5605 (second-word anatomy), 5606
(Kittell alphabet), 5609 (H_cut). Out-of-frame predecessors: 5591–5595, 5597–5598, 5604.

— Elie
