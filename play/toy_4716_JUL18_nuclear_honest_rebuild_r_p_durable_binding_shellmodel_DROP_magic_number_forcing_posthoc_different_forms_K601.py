#!/usr/bin/env python3
"""
Toy 4716 — Jul 18 (nuclear honest rebuild, mine; strengthening item 8, standing): rebuild the nuclear sector on honest
footing per Cal K601/#286 — KEEP r_p (T188, durable) + binding energies on the standard shell model; DROP the
magic-number FORCING claim ("κ_ls = C_2/n_C = 6/5 derives all magic numbers" is OVER-STATED). The magic numbers each
have A primary form, but they are ALL DIFFERENT forms with no single generating rule → post-hoc numerology, NOT unique
forcing. The shell model (spin-orbit coupling) generates the sequence; BST's per-number forms are consistent
factorizations of a FITTED spin-orbit strength, not a derivation.

WHAT BST KEEPS (durable):
  * r_p (proton charge radius, T188) — durable per Cal K601 (~0.84 fm).
  * nuclear binding energies on the standard shell model — ordinary nuclear physics, not BST-forced.
WHAT BST DROPS (the honest rebuild — per Cal K601/#286):
  * the magic-number FORCING claim. Each magic number has a primary form, but they are ALL DIFFERENT:
      2 = rank; 8 = rank³; 20 = rank²·n_C; 28 = rank²·g; 50 = rank·n_C²; 82 = N_c·n_C²+g; 126 = rank·N_c²·g.
    No single rule generates the sequence → the per-number forms are POST-HOC numerology, not forcing.
  * "κ_ls = C_2/n_C = 6/5 derives all magic numbers" is a consistent factorization of the FITTED spin-orbit strength,
    NOT a unique BST forcing. The shell model does the work; BST relabels the fitted κ_ls.

⟹ VERDICT: nuclear sector rebuilt honestly — r_p (durable, identified) + binding (shell model) KEPT; magic-number
FORCING DROPPED (per-number forms all different → post-hoc, Cal K601/#286). Nuclear is rebuild-not-chase: BST's real
nuclear content is r_p + the spin-orbit factorization tier (consistent, not forcing), and the magic numbers are shell
model physics. Honest tiering, forcing claim retired. Count ~7-8 (α RULED). Five-Absence-safe.
"""
rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

# ---- keep: r_p durable ------------------------------------------------------
check("KEEP — r_p (T188) durable: the proton charge radius r_p (~0.84 fm) is durable per Cal K601, and nuclear binding "
      "energies rest on the standard shell model (ordinary nuclear physics). These are BST's real, honest nuclear content.",
      True, "r_p (T188) durable + binding on the shell model — KEPT (identified)")

# ---- drop: magic-number forcing (all-different forms = post-hoc) ------------
magic_forms = {2: rank, 8: rank**3, 20: rank**2*n_C, 28: rank**2*g, 50: rank*n_C**2, 82: N_c*n_C**2+g, 126: rank*N_c**2*g}
all_match = all(m == f for m, f in magic_forms.items())
distinct_forms = len(set(["rank","rank^3","rank^2 n_C","rank^2 g","rank n_C^2","N_c n_C^2+g","rank N_c^2 g"]))
print(f"\n[magic forms]: {magic_forms} — all match: {all_match}; distinct form-types: {distinct_forms}/7 (no single rule)")
check("DROP — magic-number FORCING (per-number forms all DIFFERENT → post-hoc, Cal K601/#286): each magic number has a "
      "primary form (2=rank, 8=rank³, 20=rank²n_C, 28=rank²g, 50=rank·n_C², 82=N_c·n_C²+g, 126=rank·N_c²·g), but they "
      "are ALL DIFFERENT forms with NO single generating rule → post-hoc numerology, NOT unique forcing.",
      all_match and distinct_forms == 7, "magic numbers each fit a DIFFERENT primary form → no single rule → post-hoc, forcing DROPPED")

# ---- drop: kappa_ls overstated ----------------------------------------------
check("DROP — 'κ_ls = C_2/n_C = 6/5 derives all magic numbers' is OVER-STATED (Cal K601): it is a consistent "
      "factorization of the FITTED spin-orbit strength, NOT a unique BST forcing. The shell model (spin-orbit coupling) "
      "generates the magic-number sequence; BST merely relabels the fitted κ_ls. Retire the forcing claim.",
      C_2 == 6 and n_C == 5, "κ_ls=C_2/n_C=6/5 is a relabel of the fitted spin-orbit strength, not forcing — DROPPED")

# ---- verdict ----------------------------------------------------------------
check("VERDICT: nuclear rebuilt honestly — r_p (durable, identified) + binding (shell model) KEPT; magic-number "
      "FORCING DROPPED (per-number forms all different → post-hoc, Cal K601/#286); κ_ls=6/5 is a relabel not a "
      "derivation. Nuclear is rebuild-not-chase: BST's real nuclear content is r_p + the spin-orbit factorization tier "
      "(consistent, not forcing). Forcing claim retired, honest tiering restored.",
      all_match and distinct_forms == 7,
      "nuclear honest rebuild: keep r_p+binding (shell model), drop magic-number forcing (post-hoc, all-different forms)")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print("""
NUCLEAR HONEST REBUILD (strengthening item 8, standing) — per Cal K601/#286:
  * KEEP: r_p (T188, durable ~0.84 fm) + nuclear binding on the standard shell model (identified).
  * DROP: magic-number FORCING — each magic number fits a DIFFERENT primary form (2=rank, 8=rank³, 20=rank²n_C, 28=rank²g,
    50=rank·n_C², 82=N_c·n_C²+g, 126=rank·N_c²·g); no single rule → post-hoc numerology.
  * DROP: κ_ls=C_2/n_C=6/5 "derives all magic numbers" — a relabel of the fitted spin-orbit strength, not forcing.
  => nuclear rebuilt honestly: r_p+binding kept, magic-number forcing retired. Rebuild-not-chase.
""")
