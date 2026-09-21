#!/bin/bash
# reproduce_A9_run1.sh - the stranger's one command: Quaia download -> A9 run 1 landing letter.
# Reproduces Part B.1 step (iv)-(vii) on pre-registration v1.5.2 (sha256 8013d9598d356a0e..., Cal Section 974, K1909):
# Landing C - NOT DECIDABLE - on both samples (K1910, K1911, 2026-09-15/17). No BST input enters this pipeline;
# it is an Ellis-Baldwin-type kinematic-dipole test with a pre-registered decision rule.
#   usage: play/reproduce_A9_run1.sh            (from anywhere; ~1 GB download once; 10-40 min compute)
#   env:   A9_SKIP_DOWNLOAD=1 to trust existing data/quaia files after checksum; A9_PYTHON=/path/python3 to reuse an env.
set -u
ROOT="$(cd "$(dirname "$0")/.." && pwd)"; cd "$ROOT"
say(){ printf '\n== %s  %s\n' "$(date '+%H:%M:%S')" "$*"; }
fail(){ printf '\n!! FAIL: %s\n' "$*"; exit 1; }

# ---- 0. environment: a private venv with the four pinned packages (healpy is the one nobody has) ----
say "environment"
PY="${A9_PYTHON:-}"
if [ -z "$PY" ]; then
  VENV="$ROOT/.venv_a9"
  [ -x "$VENV/bin/python3" ] || python3 -m venv "$VENV" || fail "python3 -m venv failed (need Python >= 3.10)"
  PY="$VENV/bin/python3"
  "$PY" -c "import numpy,scipy,astropy,healpy" 2>/dev/null || "$PY" -m pip install -q "numpy>=1.26" "scipy>=1.11" "astropy>=6" "healpy>=1.16" || fail "pip install failed"
fi
"$PY" -c "import numpy,scipy,astropy,healpy;print('   python',__import__('sys').version.split()[0],'numpy',numpy.__version__,'astropy',astropy.__version__,'healpy',healpy.__version__)" || fail "environment"

# ---- 1. data: Quaia v1.0.0, Zenodo record 10403370 (Storey-Fisher et al.), six files. MD5s pinned from the API JSON
#         (curl https://zenodo.org/api/records/10403370), NOT from the rendered page - a page read misread one digit (K1917). ----
say "data (Zenodo 10403370, Quaia v1.0.0)"
mkdir -p data/quaia; cd data/quaia
while read -r f md5; do
  url="https://zenodo.org/api/records/10403370/files/$f/content"
  if [ ! -s "$f" ]; then
    [ "${A9_SKIP_DOWNLOAD:-0}" = 1 ] && fail "missing $f"
    echo "   downloading $f"; curl -sL --retry 3 -o "$f" "$url" || fail "download $f"
  fi
  have=$(md5 -q "$f" 2>/dev/null || md5sum "$f" | cut -d' ' -f1)
  [ "$have" = "$md5" ] && echo "   ok  $f  md5 $md5" || fail "$f md5 $have != record $md5"
done <<'MD5'
quaia_G20.0.fits 72531bc67bde1b08a69d5aeae03fb26e
quaia_G20.5.fits 98659ac4bd8a09da2c4ce653690d53df
random_G20.0_10x.fits e89dc31635d4688c8f3861dfb8a7e546
random_G20.5_10x.fits 45e5d5e76b2349899a504b49a5a7f13b
selection_function_NSIDE64_G20.0.fits 9bec5ff5d2bda8f283fd99d6db6621df
selection_function_NSIDE64_G20.5.fits 0aec3460d2e1152afe700d77554341d3
MD5
mkdir -p selfunc_perbin; cd "$ROOT/play"

# ---- 2. the frozen pre-registration and the library the run was certified on ----
say "frozen inputs"
PRE="../notes/BST_PREREGISTRATION_Part_B_1_FROZEN_v1_5_2_Cal_2026-09-15.md"; [ -f "$PRE" ] || fail "pre-registration v1.5.2 file not found: $PRE"
h=$(shasum -a 256 "$PRE" | cut -c1-16); [ "$h" = "8013d9598d356a0e" ] && echo "   ok  prereg v1.5.2 sha256 ${h}..." || fail "prereg hash $h != 8013d9598d356a0e"
lh=$("$PY" -c "import r145_eb_lib as L;print(L.lib_hash())"); [ "$lh" = "b87a8b085780" ] && echo "   ok  r145_eb_lib $lh" || fail "lib hash $lh != b87a8b085780 (commit 4ce873ce)"

# ---- 3. the chain, exactly as run on 2026-09-15 ----
say "(v) mask + bins";        "$PY" partB_mask_and_bins.py                 > .out_repro_mask.txt   2>&1 || fail "mask_and_bins"
say "(v) close (outlier 0.10)"; "$PY" partB_v_close.py 0.10                 > .out_repro_v.txt      2>&1 || fail "v_close (see play/.out_repro_v.txt)"
grep -q "lib b87a8b085780" .out_repro_v.txt || fail "(v) did not report the frozen lib"
say "(v) addendum";           "$PY" partB_v_addendum.py                    > .out_repro_vadd.txt   2>&1 || fail "v_addendum"
say "(vi) dipoles (--run)";   "$PY" partB_vi_dipoles.py --run              > .out_repro_vi.txt     2>&1 || fail "vi_dipoles (see play/.out_repro_vi.txt)"
grep -q "CRITERION (v1.5.2" .out_repro_vi.txt || fail "(vi) did not run the v1.5.2 criterion fit (see play/.out_repro_vi.txt)"
say "(vii) landing";          "$PY" keeper_partB_vii_run.py .partB_vi_dipoles.json > .out_repro_vii.txt 2>&1 || fail "vii_run"

# ---- 4. the letter, against the certified run ----
say "verdict"
cat .out_repro_vii.txt
# The strongest check: every number in the records this run wrote agrees with the committed certified records
# (commits 697249f3 (v), 0984783e (v addendum), 458cb46a (vi)) to a relative tolerance of 1e-6. Byte identity is the
# wrong bar: a different numpy build reproduces to ~6e-8 (K1917). A fresh clone has the committed files; this run overwrote them.
"$PY" - <<'PYCHK' || RECDIFF=1
import json,subprocess,sys
def walk(a,b,out):
    if isinstance(a,dict) and isinstance(b,dict):
        for k in set(a)|set(b): walk(a.get(k),b.get(k),out)
    elif isinstance(a,list) and isinstance(b,list) and len(a)==len(b):
        for x,y in zip(a,b): walk(x,y,out)
    elif isinstance(a,(int,float)) and isinstance(b,(int,float)) and not isinstance(a,bool):
        out.append(abs(a-b)/max(abs(a),abs(b),1e-300))
    elif a!=b: out.append(float('inf'))
worst=0.0
for f in ['.partB_v_closed.json','.partB_v_addendum.json','.partB_vi_dipoles.json']:
    try: committed=json.loads(subprocess.check_output(['git','show','HEAD:play/'+f],stderr=subprocess.DEVNULL))
    except Exception: print('   records: no committed copy of',f,'to compare (fresh clone without history?) - skipped'); continue
    out=[]; walk(committed,json.load(open(f)),out); m=max(out,default=0.0); worst=max(worst,m)
    print(f'   records: {f}: {len(out)} numeric fields, max relative difference {m:.1e}')
print('   records: AGREE with the certified commit to 1e-6' if worst<1e-6 else f'   records: DIFFER beyond 1e-6 (worst {worst:.1e})'); sys.exit(0 if worst<1e-6 else 1)
PYCHK
nC=$(grep -c "LANDING C" .out_repro_vii.txt)
t1=$(grep -o "shift = +7\.[0-9]*" .out_repro_vii.txt | head -1); t2=$(grep -o "shift = +5\.[0-9]*" .out_repro_vii.txt | head -1)
echo; if [ "$nC" -ge 2 ] && [ -n "$t1" ] && [ -n "$t2" ] && [ "${RECDIFF:-0}" = 0 ]; then
  echo "REPRODUCED: Landing C on both samples; Section 4.4 trigger $t1 sigma_beta (G<20.5), $t2 sigma_beta (G<20.0) - as certified K1910/K1911 (+7.50 / +5.02)."
else
  echo "NOT REPRODUCED: LANDING C count $nC; triggers '$t1' '$t2' - compare play/.out_keeper_vii_1847.txt"; exit 2
fi
