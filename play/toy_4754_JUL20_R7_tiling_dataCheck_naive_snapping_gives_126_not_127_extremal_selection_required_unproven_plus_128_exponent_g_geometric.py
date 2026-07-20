#!/usr/bin/env python3
"""
Toy 4754 — Jul 20 (Round-7 Casey tiling hypothesis: my assigned Target-1 data check + the 126-vs-127 snapping question +
Target-2 128-from-geometry). Lyra computed Q1 (K782): the natural continuous radial Bergman integral gives a smooth
Gindikin Γ-ratio, NOT 1/2^g — at "level 127" the smooth deficit is ~0.015, not 0.0078. So the continuous geometry does
NOT output 127/128; the 128 is imposed by the RS code. Casey's frame: continuous D_IV⁵ TILES into a discrete code during
cooling. The decidable test I own the arithmetic for: **does the tiling pin the top to the MAXIMAL codeword (127/128), or
the nearest (126/128)?** My finding: naive nearest-cell snapping gives **126, not 127** — across the WHOLE plausible
continuous-deficit range — so reaching 127 REQUIRES an extremal/band-edge selection mechanism that is NOT yet shown; the
data (in the pole scheme) does favor the maximal cell, which makes extremal-selection the content, not a rescue.

TARGET 1 — DATA CHECK (in the pole scheme; v/√2 = 174.10 GeV):
  continuous Γ (deficit ~0.015): y=0.985 → m_t ≈ 171.5 GeV     (Lyra's Q1 value)
  nearest cell 126/128:          y=0.9844 → m_t ≈ 171.4 GeV     (naive snapping)
  maximal cell 127/128:          y=0.9922 → m_t = 172.74 GeV    (the code / band-edge value)
  observed pole m_t ~ 172.5–172.7 → the MAXIMAL cell is the data-consistent one; the other two are ~1.1–1.3 GeV LOW.
  Caveat: this preference is scheme-CONDITIONAL — the pole-vs-MS-bar split (5.9% ≈ 10 GeV) dwarfs the 126↔127 gap
  (1/128 = 0.78% ≈ 1.35 GeV). So "data favors 127 over 126" holds only WITHIN a fixed (pole) scheme = Q2.
TARGET 1 — NAIVE SNAPPING GIVES 126, NOT 127 (model-independent, decisive): the continuous y ≈ 0.985 ⇒ y·128 ≈ 126.1 ⇒
rounds to 126 ⇒ 126/128. Across the plausible deficit range (0.012–0.024) snapping gives 125–126, NEVER 127. So "snap the
continuous Γ-value to the nearest cell" does NOT produce the top at 127/128 — it produces 126/128 (data-LOW). Reaching the
top at 127/128 REQUIRES the tiling to place it at the MAXIMAL/band-edge cell, not the nearest. That extremal-selection is
the unproven step.
THE FORK (honest): reaching 127 needs TWO things the tiling must independently supply — (i) EDGE-PLACEMENT: the top sits
at the band-edge (maximal) cell, not the nearest; candidate mechanism = boundary-reach ordering (top = heaviest = most
boundary-localized = edge, toy 4744) — a hypothesis, not shown; (ii) EXACTLY-128-CELLS: the tiling produces exactly 2^g
cells so the edge is at 127/128 (not, e.g., 100/101). Both open. Data leans extremal; the MECHANISM is Lyra's tiling to show.
TARGET 2 — the 2^g field-size exponent IS geometrically present in the Bergman norm (non-circular, but norm ≠ cells):
‖f_(½,½)‖² = Γ(5/2)²/Γ(5) = 3π/128 = N_c·π/2^g, and the exponent g=7 decomposes as g = (n_C−1) + v₂((n_C−1)!) = 4 + 3 —
the 2^(n_C−1)=16 from the half-integer Γ(n_C/2)² tower (n_C ODD) and the 2^{v₂((n_C−1)!)}=8 from Γ(n_C)=(n_C−1)!=24. So
the code's FIELD SIZE 2^g is structurally carried by the continuous FK norm — supporting "continuous geometry → discrete
field size." BUT this is the norm's NORMALIZATION, not a demonstrated CELL-COUNT, and it is NOT the deficit — so it does
NOT rescue 127/128 (the deficit is the separate 126-vs-127 question the naive tiling gets WRONG). Keep them distinct.

⟹ VERDICT: naive nearest-cell snapping of the continuous Γ-value gives 126/128 (or less), NEVER 127 — so 127/128 does not
follow from tiling-as-snapping; it needs an EXTREMAL/band-edge selection (top at the maximal cell) that the tiling has NOT
been shown to produce, plus an exactly-2^g cell-count. The data (pole scheme) favors the maximal cell (172.74 vs ~171.4
for 126 / continuous), which makes extremal-selection the content — a real, decidable target, not a rescue. Separately,
the 2^g FIELD SIZE is geometrically present in the FK norm (g = (n_C−1)+v₂((n_C−1)!)), a non-circular support for
continuous→discrete field size — but a norm, not a cell-count, and not the deficit. 127/128 stays DOWNGRADED; the tiling
has TWO open steps. Count ~7-8 (α RULED). Five-Absence-safe.
"""
import math
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
Mg = 2**g - 1  # 127
twog = 2**g    # 128
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

v = 246.22; vr = v/math.sqrt(2)   # 174.10
y_cont = 0.985                     # Lyra Q1: deficit ~0.015
mt_cont = y_cont*vr
mt_126 = (126/128)*vr
mt_127 = (127/128)*vr
obs_lo, obs_hi = 172.5, 172.7

# ---- Target 1 data check ----------------------------------------------------
print(f"\n[data check, pole scheme, v/√2={vr:.2f}]: continuous={mt_cont:.2f}  126/128={mt_126:.2f}  127/128={mt_127:.2f}  obs~{obs_lo}-{obs_hi}")
maximal_is_consistent = obs_lo-0.3 <= mt_127 <= obs_hi+0.3 and mt_126 < obs_lo-0.5 and mt_cont < obs_lo-0.5
check("TARGET 1 DATA CHECK (pole scheme): m_t is 171.5 (continuous Γ), 171.4 (nearest cell 126/128), 172.74 (maximal cell "
      "127/128); observed pole ~172.5–172.7. The MAXIMAL cell (127/128) is the data-consistent one; the nearest cell and "
      "the pure continuous are BOTH ~1.1–1.3 GeV LOW. CAVEAT: scheme-CONDITIONAL — pole-vs-MS-bar (5.9%≈10 GeV) dwarfs the "
      "126↔127 gap (0.78%≈1.35 GeV), so the preference holds only within a fixed (pole) scheme = Q2.",
      maximal_is_consistent, f"maximal 127/128→{mt_127:.2f} data-consistent; nearest 126/128→{mt_126:.2f} & continuous→{mt_cont:.2f} both ~1.2 GeV low (scheme-conditional)")

# ---- Target 1: naive snapping gives 126, not 127 (decisive) -----------------
snaps = {round(defic,3): round((1-defic)*128) for defic in [0.012,0.015,0.018,0.021,0.024]}
never_127 = all(s <= 126 for s in snaps.values())
print(f"[naive snapping]: across deficit 0.012–0.024 → nearest cells = {sorted(set(snaps.values()))} — NEVER 127")
check("TARGET 1 — NAIVE SNAPPING GIVES 126, NOT 127 (model-independent, decisive): continuous y≈0.985 ⇒ y·128≈126.1 ⇒ "
      "rounds to 126 ⇒ 126/128. Across the plausible deficit range (0.012–0.024) snapping gives 125–126, NEVER 127. So "
      "'snap the continuous Γ-value to the nearest cell' produces 126/128 (data-LOW), NOT the top at 127/128. Reaching "
      "127/128 REQUIRES placing the top at the MAXIMAL/band-edge cell — the unproven step.",
      never_127 and round(y_cont*128) == 126, "snapping → 125–126 across the whole deficit range, never 127; reaching 127 needs extremal (band-edge), not nearest, selection")

# ---- the fork: two unproven steps -------------------------------------------
check("THE FORK (two open steps the tiling must supply): (i) EDGE-PLACEMENT — the top at the band-edge (maximal) cell, not "
      "the nearest; candidate mechanism = boundary-reach ordering (top=heaviest=most boundary-localized=edge, toy 4744) — "
      "a hypothesis, NOT shown; (ii) EXACTLY-2^g-CELLS — the tiling produces exactly 128 cells so the edge sits at 127/128 "
      "(not 100/101, etc.). Both open. The data leans extremal, but the MECHANISM is Lyra's tiling to demonstrate — this "
      "is a test, not a rescue.",
      True, "reaching 127/128 needs BOTH edge-placement (cand: boundary-reach 4744) AND exactly-128-cells — both unproven; data leans extremal but mechanism unshown")

# ---- Target 2: 2^g exponent is geometrically present ------------------------
def v2(n):
    c=0
    while n%2==0: n//=2; c+=1
    return c
exp_half = n_C - 1                     # 2^(n_C-1)=16 from Γ(n_C/2)² half-integer tower
exp_fact = v2(math.factorial(n_C-1))   # v2(24)=3 from Γ(n_C)=(n_C-1)!
g_from_norm = exp_half + exp_fact
norm_top = (((3/2)*(1/2)*math.sqrt(math.pi))**2)/math.factorial(4)  # 3π/128
print(f"[Target 2]: g exponent in ‖f_top‖²=3π/2^g  is  (n_C−1)+v₂((n_C−1)!) = {exp_half}+{exp_fact} = {g_from_norm} = g; 2^g={2**g_from_norm}")
check("TARGET 2 — 2^g FIELD SIZE is geometrically present in the FK norm (non-circular; norm ≠ cells): ‖f_(½,½)‖² = "
      "Γ(5/2)²/Γ(5) = 3π/128 = N_c·π/2^g, and the exponent g=7 decomposes as g = (n_C−1) + v₂((n_C−1)!) = 4 + 3 — the "
      "2^(n_C−1)=16 from the half-integer Γ(n_C/2)² tower (n_C ODD) and 2^{v₂((n_C−1)!)}=8 from Γ(n_C)=(n_C−1)!=24. So the "
      "code's FIELD SIZE 2^g is structurally carried by the CONTINUOUS Bergman norm. BUT this is a NORMALIZATION, not a "
      "demonstrated cell-count, and NOT the deficit — it does NOT rescue 127/128. Keep norm/cells/deficit distinct.",
      g_from_norm == g and abs(norm_top - N_c*math.pi/twog) < 1e-12,
      "2^g exponent g=(n_C−1)+v₂((n_C−1)!)=4+3=7 geometrically present in ‖f_top‖²=3π/128 — field size, not cell-count, not deficit")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: naive nearest-cell snapping of the continuous Γ-value gives 126/128 (or less), NEVER 127 — so 127/128 does "
      "NOT follow from tiling-as-snapping; it needs EXTREMAL/band-edge selection (top at the maximal cell) the tiling has "
      "not been shown to produce, PLUS an exactly-2^g cell-count. The data (pole scheme) favors the maximal cell (172.74 "
      "vs ~171.4), making extremal-selection the content — decidable, not a rescue. Separately, the 2^g FIELD SIZE is "
      "geometrically present in the FK norm (g=(n_C−1)+v₂((n_C−1)!)) — non-circular support for continuous→discrete field "
      "size, but a norm not a cell-count, and not the deficit. 127/128 stays DOWNGRADED; TWO open tiling steps.",
      never_127 and maximal_is_consistent and g_from_norm == g,
      "snapping→126 not 127 (extremal selection required+unproven, 2 steps); data(pole) favors maximal; 2^g field-size geometric; 127/128 DOWNGRADED")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
ROUND-7 (Casey's tiling hypothesis) — my Target-1 data check + snapping + Target-2 (mine):
  * DATA (pole scheme): maximal 127/128→172.74 is data-consistent; nearest 126/128→171.4 & continuous→171.5 both ~1.2 GeV LOW. (Scheme-conditional = Q2.)
  * SNAPPING (decisive): naive nearest-cell snapping gives 126 (or 125), NEVER 127, across the whole deficit range. Reaching 127 needs EXTREMAL/band-edge selection.
  * THE FORK: two unproven tiling steps — edge-placement (cand: boundary-reach 4744) AND exactly-2^g cells. Data leans extremal; mechanism unshown.
  * TARGET 2: 2^g FIELD SIZE is geometrically present in ‖f_top‖²=3π/128 (g=(n_C−1)+v₂((n_C−1)!)=4+3) — non-circular, but a norm not a cell-count, and not the deficit.
  => 127/128 stays DOWNGRADED. The tiling is a decidable test (data leans extremal) with two open steps — not a rescue.
""")
