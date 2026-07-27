#!/usr/bin/env python3
"""
Toy 4875 — Jul 27 [PROGRAM: STANDARD] (K942 checkability fixes to verify_bst.py — the "run it yourself" weapon; Elie, pull
27a). Keeper's K942 checkability audit found the headline claims TRUE and the toys clean, but flagged TWO curation catches
before the hook package goes near Tegmark — both the exact thing a physicist's numerology-alarm fires on. I fixed both in
verify_bst.py (single source of truth, computed views — matching the corpus-currency philosophy of the day); this toy SCORES
the fixes and guards against regression.

FIX 1 (LIABILITY) — the SM-CORE curation: verify_bst.py mixed SM/particle physics with "breadth" (amino acids, DNA bases,
Debye temperature, seismic ratio) on one screen → a physicist running it hears numerology. Added a `--core` flag: SM/particle/
nuclear/cosmology ONLY (38 predictions); the 12 breadth items (chemistry/biology/turbulence/seismology/condensed-matter) are
relabeled "extended reach" and EXCLUDED from --core. Nothing deleted (never delete — stamp/scope). The full run now labels
itself "38 SM core + 12 extended reach."

FIX 2 (CONFUSION) — the 49/50-vs-27/51 self-consistency: the output printed the curated "49/50 at <1%" headline AND the
null-model "27/51 at <1%" on one screen with no explanation → looks contradictory. Reconciled in-line: they are TWO DIFFERENT
SETS with different jobs — the N/M headline is THIS curated reproduction set (D/I-tier predictions, reproducibility); the 27/51
is a SEPARATE, blind, un-curated 51-constant set (Toy 1543, non-randomness test, BST 27 vs random 14.7, Z=2.9). The null-model
line now dynamically reads the actual curated count and states plainly they are different sets — self-consistent.

⟹ VERDICT (plain): both K942 curation catches fixed in verify_bst.py. --core = 38 SM-physics predictions (37/38 at <1%), the
12 breadth items excluded (no amino-acids/DNA/Debye/seismic in the physicist-facing screen); full = 50 (49/50) relabeled "SM
core + extended reach." The 49/50-vs-27/51 confusion reconciled as two distinct sets (curated reproduction vs blind null-model),
the null-model line computed from the live count. The numbers are UNCHANGED (K942: "numbers correct; presentation needs aiming")
— this is curation + self-consistency, the credibility layer for a reader who RUNS the toys. [STANDARD] bar; graduates to
TEGMARK at the Cal gate. Nothing deleted. Five-Absence-untouched. Count 6.
"""
import importlib.util, io, contextlib, os
rank, N_c, n_C, C_2, g, N_max = 2, 3, 5, 6, 7, 137
results = []
def check(label, cond, detail): results.append((label, bool(cond), detail))

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("verify_bst", os.path.join(HERE, "verify_bst.py"))
vb = importlib.util.module_from_spec(spec); spec.loader.exec_module(vb)

BREADTH = {"N_amino_acids", "N_bases (DNA bases)", "codon_length", "N_codons",
           "theta_D(Pb) (Debye temperature, K)", "v_P/v_S (seismic ratio, Poisson solid)",
           "theta_tetrahedral (degrees)", "theta_H2O (water bond angle, degrees)",
           "theta_NH3 (ammonia bond angle, degrees)", "D_e(C-H) (bond energy, eV)",
           "Kolmogorov 5/3 exponent", "gamma_adiabatic (monatomic)"}
names = [p[0] for p in vb.PREDICTIONS]
core_names = [n for n in names if vb.is_core(n)]
ext_names  = [n for n in names if not vb.is_core(n)]

def run(core):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        good, total = vb.verify(core_only=core)
    return good, total, buf.getvalue()

g_full, t_full, out_full = run(False)
g_core, t_core, out_core = run(True)
print(f"\n[K942] full={g_full}/{t_full} | core={g_core}/{t_core} | breadth excluded from core={len(ext_names)} | numerology items in core screen={[n for n in BREADTH if vb.is_core(n)]}")

check("FIX 1a — the EXTENDED-REACH set is exactly the 12 breadth items (chemistry/biology/turbulence/seismology/condensed "
      "matter): the numerology-alarm items (amino acids, DNA, Debye, seismic, bond angles/energy, Kolmogorov, adiabatic) are "
      "classified out of the SM core.",
      set(ext_names) == BREADTH and len(ext_names) == 12,
      f"extended-reach = the 12 breadth items exactly ({sorted(ext_names)}); classified out of SM core")

check("FIX 1b — --core EXCLUDES every breadth/numerology item: no amino-acids, DNA, Debye, seismic, bond-angle in the "
      "physicist-facing SM-core screen. This is the LIABILITY fix (a physicist running --core hears NO numerology).",
      all(not vb.is_core(n) for n in BREADTH) and not (set(core_names) & BREADTH),
      "--core screen contains ZERO breadth items (no amino/DNA/Debye/seismic/bond-angle) → no numerology alarm on the core")

check("FIX 1c — --core keeps the SM/particle physics (m_p/m_e, alpha, VEV, Higgs, CKM, PMNS, hadrons, cosmology, nuclear) and "
      "counts self-consistently: core + extended = full (38 + 12 = 50). Nothing deleted; the split is a computed VIEW.",
      t_core + len(ext_names) == t_full and t_core == 38 and t_full == 50,
      f"core({t_core}) + extended({len(ext_names)}) = full({t_full}); split is a computed view, nothing deleted")

check("FIX 2 — the 49/50-vs-27/51 CONFUSION reconciled: the output states the curated headline count AND labels Toy 1543's "
      "27/51 as a SEPARATE blind set (different job), so the screen is self-consistent. The null-model line reads the LIVE "
      "curated count (no hardcoded mismatch).",
      ("SEPARATE" in out_full) and ("different set" in out_full.lower()) and (f"The {g_full}/{t_full} above" in out_full)
      and ("27/51" in out_full),
      "output labels curated-set vs blind null-model (Toy 1543) as two different sets; null-model line reads the live count → self-consistent")

check("NUMBERS UNCHANGED (K942: 'numbers correct; presentation needs aiming'): full still 49/50 at <1%, core 37/38 — the "
      "fixes are curation + self-consistency, NOT a change to any predicted value. No prediction touched.",
      g_full == 49 and t_full == 50 and g_core == 37 and t_core == 38,
      "full 49/50, core 37/38 — unchanged numbers; fixes are curation + self-consistency only, no value edited")

check("REGRESSION GUARD — both modes run clean (exit-equivalent, non-empty, headers present) and the header labels are honest "
      "(full: 'SM core + extended reach'; core: 'SM-CORE ... extended reach excluded'). The checkability weapon is "
      "self-describing to a reader who RUNS it.",
      ("extended reach" in out_full) and ("SM-CORE VERIFICATION" in out_core) and ("excluded" in out_core)
      and len(out_full) > 500 and len(out_core) > 500,
      "both modes run clean with honest self-describing headers (full=core+extended; core=SM-only, extended excluded)")

# ---- SCORE -----------------------------------------------------------------
passed = sum(1 for _, ok, _ in results if ok); total = len(results)
print("\n" + "=" * 96)
for label, ok, detail in results:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}\n         → {detail}")
print("=" * 96)
print(f"SCORE: {passed}/{total}")
print("=" * 96)
print(f"""
JUL-27 [STANDARD] K942 checkability fixes to verify_bst.py (Elie, pull 27a):
  * FIX 1 (LIABILITY): --core flag → 38 SM/particle/nuclear/cosmology predictions (37/38 at <1%); the 12 breadth items (amino acids, DNA, Debye, seismic, bond angles, Kolmogorov, adiabatic) relabeled 'extended reach' and EXCLUDED from core. A physicist running --core hears no numerology. Nothing deleted.
  * FIX 2 (CONFUSION): the 49/50-vs-27/51 reconciled in-line as TWO different sets — curated reproduction (this file, {g_full}/{t_full}) vs blind null-model (Toy 1543, 27/51, non-randomness Z=2.9). Null-model line computed from the live count → self-consistent.
  * Numbers UNCHANGED (curation + self-consistency only). The checkability weapon for the TEGMARK hook package; [STANDARD] bar, graduates to TEGMARK at the Cal gate.
""")
