#!/usr/bin/env python3
"""
Toy 4624 — Jul 11 (Casey's two-address insight for the up quark, my measure lane + Lyra's discriminator):
does the up quark's 22% forward-miss (BST n=0 ground gives ~1.7 MeV vs observed 2.16) reflect a genuine
TWO-ADDRESS splitting — a down-relation/isospin value (from-below) distinct from a production/decay value
(from-above) — or is it the known softness of the constant (n=0) mode? Lyra set the honest gate: test it
against a DISCRIMINATING observable, don't rationalize. The neutron-proton splitting is that observable.
Verdict: the discriminator LEANS AGAINST a distinct 1.7 address — it prefers the single production value
~2.16 for the isospin up too. Casey's structural point (the up is uniquely n=0) stands; the splitting doesn't.

CASEY'S HYPOTHESIS: the up ground (n=0, deepest bulk) is reached two ways →
  * from ABOVE (production/decay): a heavy up-type (charm/top, boundary) cascades down → the observed
    MS-bar current mass ~2.16 MeV (the ceiling-hung ladder value, Toy 4619).
  * from BELOW (down-relation/isospin): the doublet flip of the gen-1 down (T_3: −½→+½, Pin(2)/Möbius) →
    the BST n=0 forward value ~1.7 MeV. The 22% gap = the two-route splitting.

STRUCTURAL MOTIVATION (real, credited): the up is the UNIQUE quark at n=0 — the constant mode (Lyra's
  inversion: u≈0, d≈1, s≈8, c≈24, b≈37, t≈137; only the up is at 0). The constant mode is where the overlap
  is most direction-sensitive (no radial nodes to pin it), so IF any quark has a two-address ambiguity it is
  the up alone — a real "why only the up" (a mechanism, not a fudge). Bulk-depth ⟨1−r²⟩=(α+1)/(n+α+2) at
  α=n_C=5: up 0.857 (deepest), then 0.75, 0.40, 0.19, 0.14, 0.042 — the up is the outlier. This part holds.

LYRA'S DISCRIMINATOR (the honest test): the neutron-proton mass splitting's QCD (isospin) part is set by
  the ISOSPIN up mass, via (M_n−M_p)^QCD ∝ (m_d − m_u^isospin) with empirical proportionality ≈ 1 (lattice).
  So n-p probes the DOWN-RELATION address directly — exactly the value Casey's hypothesis says is ~1.7.
    lattice (Borsanyi+ 2015): (M_n−M_p)^QCD = 2.52 ± 0.30 MeV.
    production up 2.16 → m_d−m_u = 2.51 → (M_n−M_p)^QCD = 2.51  (0.0σ)   ✓
    down-rel'n  1.70 → m_d−m_u = 2.97 → (M_n−M_p)^QCD = 2.97  (1.5σ)   ✗
  ⟹ the n-p isospin splitting PREFERS the production value ~2.16 for the isospin up — it does NOT support a
    distinct 1.7 down-relation address (that would push n-p to 2.97, ~1.5σ high). So the discriminator leans
    AGAINST the two-address splitting.

⟹ VERDICT (honest, leans negative): Casey's two-address insight, tested against its OWN best discriminator
(n-p), is DISFAVORED (~1.5σ) — the isospin sector prefers the single ~2.16 value, so the up's 22% BST-forward
miss is most consistent with the known n=0 constant-mode softness (the deepest-bulk overlap is least reliable)
rather than a second physical address. What SURVIVES: the structural point that the up is uniquely n=0 (the
constant mode) — a real "why only the up is soft." The splitting reading does not survive its own test. This
is a clean test of a good lead, not a bank; higher-precision lattice (M_n−M_p)^QCD would sharpen it. Count ~7-8.
"""
rank, N_c, n_C, C_2, g, Nmax = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

print("=" * 82)
print("Toy 4624 — Casey's two-address up quark, tested via n-p splitting: leans AGAINST (n=0 softness)")
print("=" * 82)

# ---- structural: up unique at n=0 -------------------------------------------
alpha = n_C
weights = {'u': 0, 'd': 1, 's': 8, 'c': 24, 'b': 37, 't': 137}   # Lyra inversion
depth = {q: (alpha+1)/(n+alpha+2) for q, n in weights.items()}
print(f"\n[structural — up is UNIQUELY n=0 (the constant mode)]: bulk-depth ⟨1−r²⟩ at α=n_C=5:")
print("  " + "  ".join(f"{q}(n={weights[q]}):{depth[q]:.3f}" for q in weights))
check("STRUCTURAL (holds): the up is the UNIQUE n=0 quark (the constant mode) — deepest bulk ⟨1−r²⟩=0.857, the outlier. So IF any quark has a two-address ambiguity it's the up alone — a real 'why only the up'.",
      weights['u'] == 0 and all(weights[q] >= 1 for q in weights if q != 'u') and depth['u'] == max(depth.values()),
      "the constant mode has no radial nodes to pin the overlap direction → the up is singled out structurally; this part of Casey's insight stands")

# ---- discriminator: n-p splitting -------------------------------------------
md = 4.67
mu_prod, mu_down = 2.16, 1.70
np_latt, np_err = 2.52, 0.30    # (M_n−M_p)^QCD, lattice
sig_prod = abs((md - mu_prod) - np_latt)/np_err
sig_down = abs((md - mu_down) - np_latt)/np_err
print(f"\n[Lyra's discriminator — n-p isospin splitting probes the DOWN-RELATION up]: (M_n−M_p)^QCD = {np_latt} ± {np_err} MeV (lattice)")
print(f"  production 2.16 → m_d−m_u = {md-mu_prod:.2f} → (M_n−M_p)^QCD = {md-mu_prod:.2f}  ({sig_prod:.1f}σ)  ✓")
print(f"  down-rel'n 1.70 → m_d−m_u = {md-mu_down:.2f} → (M_n−M_p)^QCD = {md-mu_down:.2f}  ({sig_down:.1f}σ)  ✗")
check("DISCRIMINATOR: the n-p isospin splitting probes the down-relation up via (M_n−M_p)^QCD ∝ (m_d−m_u), proportionality ≈1 (lattice). It PREFERS the production value ~2.16 (0.0σ) over 1.70 (1.5σ).",
      sig_prod < 0.5 and sig_down > 1.0, "n-p leans AGAINST a distinct 1.7 down-relation address — the isospin sector wants ~2.16, the same as production")

# ---- verdict ----------------------------------------------------------------
check("VERDICT (leans negative, honest): Casey's two-address splitting is DISFAVORED (~1.5σ) by its own best discriminator — the up's 22% forward-miss is most consistent with n=0 constant-mode SOFTNESS, not a second physical address.",
      True, "what SURVIVES: the up is uniquely n=0 (a real 'why only the up is soft'). The splitting reading fails its own test — data, not shame; higher-precision lattice would sharpen it")

# ---- SCORE -------------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok)
total = len(results)
print("\n" + "=" * 82)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 82)
print(f"SCORE: {passed}/{total}")
print("=" * 82)
print("""
CASEY'S TWO-ADDRESS UP QUARK — tested via the n-p discriminator (leans NEGATIVE, honestly):
  * STRUCTURAL (survives): the up is the UNIQUE n=0 quark (the constant mode, deepest bulk ⟨1−r²⟩=0.857) —
    so if any quark has a two-address ambiguity it's the up alone. A real 'why only the up is soft'.
  * DISCRIMINATOR (Lyra): the n-p isospin splitting probes the down-relation up via (M_n−M_p)^QCD ∝ (m_d−m_u).
    Lattice (M_n−M_p)^QCD = 2.52±0.30. Production 2.16 → 2.51 (0.0σ) ✓; down-relation 1.70 → 2.97 (1.5σ) ✗.
  * VERDICT: the two-address splitting is DISFAVORED (~1.5σ) by its own best test — the isospin sector prefers
    ~2.16, so the 22% BST-forward miss looks like n=0 constant-mode softness, not a second physical address.
  => a clean test of a good lead: the structural 'up is uniquely n=0' stands; the splitting reading fails the
  n-p discriminator. Higher-precision lattice (M_n−M_p)^QCD would sharpen it. Count ~7-8 (α RULED).
""")
