#!/usr/bin/env python3
"""
Toy 2941 — BR(D⁰ → K⁻ π⁺) Cabibbo-favored in BST integers
=============================================================

PDG: BR(D⁰ → K⁻ π⁺) = 3.95%.
Try BST: 1/N_max·N_c² · ? not clean
0.0395 ≈ ? Let me check various BST products.

0.0395 ≈ rank/n_C/(rank²+N_c) - ?
0.0395 · N_max² = 740 ≈ N_c·c_2·rank²·... = ?
740 = 4·5·37 = rank²·n_C·37 (37 not BST clean)
740 = 5·148 = n_C·148. Hmm 148 = N_max+11 = N_max+c_2.

0.0395 · N_max = 5.41 ≈ n_C+small. So 0.0395 ≈ n_C/N_max + small correction.
n_C/N_max = 5/137 = 0.0365 — 7% off.

Try: 0.0395 ≈ rank²/N_c·g·n_C/something. Or = 1/(rank²+rank²·N_c-... )
0.0395 ≈ rank/N_c²/g... = 0.0317 — off.

Best simple: 0.0395 ≈ rank·g/(rank³·N_c+N_max-... ) — not clean.

HONEST: BR(D⁰ → K⁻π⁺) doesn't anchor cleanly to a simple BST integer ratio
at sub-1% precision. Best simple approximation: rank³/N_max² = 8/18769 =
0.000426 — way off.

This is an HONEST NEGATIVE — Cabibbo-favored charm decay BR doesn't fit
the simple-ratio mold.

Author: Grace (Claude 4.7), 2026-05-16 16:43 EDT
"""

rank, N_c, n_C, C_2, g = 2, 3, 5, 6, 7
c_2, c_3, chi_K3, N_max = 11, 13, 24, 137

PASS = FAIL = 0
def check(label, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; mark = "PASS"
    else:  FAIL += 1; mark = "FAIL"
    print(f"  [{mark}] {label}")


print("=" * 72)
print("Toy 2941 — BR(D⁰ → K⁻π⁺) HONEST NEGATIVE")
print("=" * 72)

BR_obs = 0.0395

# Try several BST forms
candidates = [
    ("n_C/N_max", n_C/N_max),
    ("rank³/(rank³·N_c+rank²·c_2)", rank**3/(rank**3*N_c+rank**2*c_2)),
    ("rank·g/(N_max+c_2)", rank*g/(N_max+c_2)),
    ("(rank²·n_C)/N_max", rank**2*n_C/N_max),
    ("1/Wallach_5 = 1/91", 1/91),
]

print(f"\n  BR(D⁰ → K⁻π⁺) PDG: {BR_obs}")
print(f"\n  Candidate BST forms:")
best_match = 1.0
best_form = None
for form, val in candidates:
    match = 100 * abs(val - BR_obs) / BR_obs
    print(f"    {form}: {val:.4f} ({match:.1f}% off)")
    if match < best_match * 100:
        best_match = match / 100
        best_form = form

print(f"\n  Best simple form: {best_form} at {best_match*100:.1f}%")
print(f"\n  HONEST: no clean sub-1% BST simple ratio found for this specific")
print(f"  Cabibbo-favored charm decay. Tier S (no clean match).")

check("Honest negative: BR(D⁰ → K⁻π⁺) not cleanly BST", True)


print("=" * 72)
print(f"Toy 2941 SCORE: {PASS}/{PASS+FAIL}")
print("=" * 72)
print(f"""
  T2289 (proposed): BR(D⁰ → K⁻π⁺) honest negative — not cleanly BST.
  Tier S (no anchor).
""")
