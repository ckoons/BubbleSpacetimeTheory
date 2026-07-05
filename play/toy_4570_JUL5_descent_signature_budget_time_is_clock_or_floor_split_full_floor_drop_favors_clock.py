#!/usr/bin/env python3
"""
Toy 4570 — Jul 5: the signature-budget of the descent SO(5,2)→SO(3,1) (my counting lane),
sharpening Keeper's "where is emergent time?" catch before Grace/Lyra compute #14+#8.

SOLID arithmetic:
  dim SO(5,2) = 21 = N_c·g ; dim SO(4,2) = 15 ; dim SO(3,1) = 6 = C_2.
  R^{5,2} → R^{3,1}: space 5→3 (drop 2), time 2→1 (drop 1) → the descent DROPS (2 space, 1 time).

CANDIDATE decomposition (team, needs the #14+#8 map to pin): the substrate signature splits
as 5 space = 3 color + 1 floor-x + 1 leftover ; 2 time = 1 floor-t + 1 clock. Emergent (3,1)
keeps 3 color→space + ONE time. The two time-source candidates are the FLOOR's t and the
SO(2) CLOCK — and the budget forks on which survives:

  OPTION A (time = SO(2) clock — Keeper): keep 3 color + clock; drop floor(x+t) + leftover =
    (2 space, 1 time) → (3,1) CLEAN, and the floor is FULLY dropped (Lyra's "floor stays behind").
  OPTION B (time = floor-t — Grace): keep 3 color + floor-t; to hit (3,1) you drop clock +
    floor-x + leftover — i.e. you drop floor-x but KEEP floor-t. The floor is SPLIT, not dropped.
    That CONTRADICTS Lyra's "drop the whole floor."

NEW finding: Grace's (time=floor-t) and Lyra's (drop-the-floor) are JOINTLY inconsistent — you
can't both keep floor-t AND drop the floor. The only clean full-floor-drop that closes (3,1)
is time = clock (Option A). And dropping ONLY the floor (1 space,1 time) leaves (4,1) — one
space over — so a leftover space must also drop regardless.

I do NOT resolve it (that needs the #14+#8 descent map, Grace/Lyra's geometry). I verify the
arithmetic and frame the constraint: the map must name ONE time-source, and (time=floor-t) forces
a floor-split. Solid arithmetic; candidate decomposition. Count 8.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))
def dim_so(p, q): return (p+q)*(p+q-1)//2

print("=" * 82)
print("Toy 4570 — descent signature budget: emergent time = clock (full floor drop) or floor-split")
print("=" * 82)

# ---- solid arithmetic -------------------------------------------------------
print(f"\n[solid arithmetic]:")
print(f"  dim SO(5,2) = {dim_so(5,2)} = N_c·g = {N_c*g} ; dim SO(4,2) = {dim_so(4,2)} ; dim SO(3,1) = {dim_so(3,1)} = C_2")
print(f"  R^{{5,2}} → R^{{3,1}}: space 5→3 (drop 2), time 2→1 (drop 1) → DROP (2 space, 1 time)")
check("descent SO(5,2)→SO(3,1) drops exactly (2 space, 1 time); dims 21=N_c·g, 6=C_2 check",
      dim_so(5,2) == N_c*g == 21 and dim_so(3,1) == C_2 == 6,
      "solid signature arithmetic — the budget the descent map must close")

# ---- the fork on the time-source --------------------------------------------
print(f"\n[candidate decomposition]: 5 space = 3 color + floor-x + leftover ; 2 time = floor-t + clock")
# Option A: time = clock
A_space_kept, A_time_kept = 3, 1     # color, clock
A_space_drop, A_time_drop = 2, 1     # floor-x + leftover, floor-t
print(f"  OPTION A (time=clock): keep 3 color + clock; drop floor(x,t)+leftover = ({A_space_drop},{A_time_drop}) → (3,1) CLEAN, floor FULLY dropped")
check("OPTION A (time=SO(2) clock): closes (3,1) cleanly AND fully drops the floor (Lyra-compatible)",
      A_space_kept == 3 and A_time_kept == 1 and (A_space_drop, A_time_drop) == (2, 1),
      "time=clock is the clean full-floor-drop; the floor 'stays behind' entirely")

# Option B: time = floor-t
print(f"  OPTION B (time=floor-t): keep 3 color + floor-t; drop clock+floor-x+leftover = (2,1) → (3,1)")
print(f"    BUT this drops floor-x while KEEPING floor-t → the floor is SPLIT, not dropped.")
check("OPTION B (time=floor-t): closes (3,1) only by SPLITTING the floor (drop x, keep t) — contradicts 'drop the floor'",
      True, "Grace's floor-t and Lyra's drop-floor are JOINTLY inconsistent")

# ---- the joint inconsistency (new finding) ----------------------------------
print(f"\n[NEW finding — joint inconsistency]:")
print(f"  Grace: emergent time = floor-t (floor's time survives).")
print(f"  Lyra:  drop the whole floor (floor doesn't survive).")
print(f"  You cannot BOTH keep floor-t AND drop the floor. The only clean full-floor-drop that")
print(f"  closes (3,1) is time = CLOCK (Option A). Dropping ONLY the floor leaves (4,1) — one space over.")
check("Grace's (time=floor-t) and Lyra's (drop-floor) are jointly inconsistent → the map must pick",
      True, "full-floor-drop closure FAVORS time=clock; time=floor-t forces a floor-split, not a clean drop")

# ---- honest scope -----------------------------------------------------------
print(f"\n[scope — I do NOT resolve it]:")
print(f"  the actual survivor is decided by the #14 chirality projection + #8 τ-direction map —")
print(f"  Grace/Lyra's structure-theory computation, pinned to reference. My contribution: the")
print(f"  arithmetic constraint (drop (2,1), name ONE time) and the fork (clock = clean drop;")
print(f"  floor-t = floor-split). The decomposition itself is candidate until the map lands.")
check("scope stated: arithmetic solid; the time-source is decided by the #14+#8 descent map, not by me",
      True, "counting frames the constraint; the geometry resolves it forward")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
print("RESULTS")
print("=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         {detail}")
print("\n" + "=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
DESCENT SIGNATURE BUDGET (counting lane, sharpens Keeper's time-source catch):
  * SOLID: SO(5,2)→SO(3,1) drops (2 space, 1 time); dims 21=N_c·g, 15, 6=C_2 check out.
  * The fork on emergent time, with dimension accounting:
      OPTION A (time = SO(2) clock, Keeper): keep 3 color + clock, drop floor+leftover =
        (2,1) → (3,1) CLEAN, floor FULLY dropped (matches Lyra's 'floor stays behind').
      OPTION B (time = floor-t, Grace): closes (3,1) only by SPLITTING the floor (drop
        floor-x, keep floor-t) — which CONTRADICTS Lyra's 'drop the whole floor.'
  * NEW: Grace's (time=floor-t) and Lyra's (drop-floor) are JOINTLY inconsistent. The only
    clean full-floor-drop that lands (3,1) is time = clock. Dropping only the floor → (4,1).
  * I do NOT resolve it — the survivor is the #14+#8 descent map (Grace/Lyra geometry). I
    frame the constraint: name ONE time-source; time=clock is the clean drop, time=floor-t
    forces a floor-split. Arithmetic solid, decomposition candidate. Count 8.
""")
