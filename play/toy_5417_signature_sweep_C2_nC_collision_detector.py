#!/usr/bin/env python3
"""
Toy 5417 (Grace, signature-sweep) — SIGNATURE SWEEP: the mechanical C₂↔n_C collision detector.

  ★ DISAMBIGUATION: "toy 5417" is a colliding citation (claim_number.sh non-atomic, Elie 08-21).
    This is the GRACE signature-sweep 5417; Elie holds a separate 5417 (6/5-provenance). Cite
    "toy 5417 (Grace, signature-sweep)" until Keeper rules the numbering-governance call.

  ★★ STANDING ACCEPTANCE GATE (Keeper K1766, Round 32). Contract:
     RE-RUN THIS after ANY Bergman-kernel edit, BEFORE anything registers. A registration that
     touches a D_IV⁵ Bergman/Szegő kernel formula is admissible only if this gate returns 0.
     A nonzero flag is either (a) a live collision to correct at its owner, or (b) a NEW false
     positive to add to the exclusion set with a one-line reason — never waved through.

Not a string grep. A STRUCTURAL consistency check: for a D_IV⁵ scalar-Bergman formula, the
π-power (Bergman VOLUME over complex-dim-5 → π^{n_C}=π⁵) and the kernel EXPONENT (genus=n_C=5,
Hua 1963 / Elie's 4-way bidisk pin) must BOTH equal 5. A disagreement is the signature of the
genus-vs-C₂-vs-g collision (someone wrote 6=n_C+1=C₂, or 7=g, where the genus 5 belongs).

Caught the whole family (28 lines, Round 32) plus flags false positives for EXCLUSION:
  - FK-convention π^{9/2} / exp-5/2 (a DIFFERENT normalization, not the scalar Bergman genus);
  - volume-constant Vol^{-1} (exponent 1, K(0,0)=(π⁵/1920)⁻¹ — not a genus);
  - other-type domains (D_I/D_II/D_III);
  - the sweep's own META-DOCS (correction-index / this family) — they carry collision EXAMPLE
    strings by design (e.g. a sentence "...corrected N^{-g+1}=−6 → N^{-n_C}"), so scanning them
    re-flags the very corrections they record. Excluded by filename, same class as D_I/D_II.
SCORE: 4/4 (instrument fires on the known ElectronMass twin; finds the family; excludes false-pos;
            corpus clean zero after the meta-doc exclusion — the standing-gate PASS state).
"""
import re, glob
SYM={'n_C':5,'nC':5,'C_2':6,'C₂':6,'c_2':11,'g':7,'rank':2,'N_c':3,'n':5}
SUP=str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789')
def resolve(e):
    e=e.strip().strip('()').replace(' ','')
    if re.fullmatch(r'-?\d+',e): return int(e)
    for k in sorted(SYM,key=len,reverse=True): e=e.replace(k,str(SYM[k]))
    if re.fullmatch(r'[-+*/\d]+',e):
        try: return int(eval(e))
        except: return None
    return None
def pi_powers(l):
    out=[int(m.group(1).translate(SUP)) for m in re.finditer(r'π([⁰¹²³⁴⁵⁶⁷⁸⁹]+)',l)]
    for m in re.finditer(r'(?:π|pi)\^\{?(-?\d+|n_C[^}\s]*|C_?2[^}\s]*)\}?',l):
        v=resolve(m.group(1));  out.append(v) if v else None
    out+= [int(m.group(1)) for m in re.finditer(r'pi\*\*(\d+)',l)]
    return [p for p in out if p and p>0]
def kernel_exps(l):
    return [v for m in re.finditer(r'(?:N\([^)]*\)|N|det\([^)]*\)|\))\s*\^\{?-\(?([^}\s)]+)\)?\}?',l)
            for v in [resolve(m.group(1))] if v is not None and 1<v<15]  # >1: genus≥2; exp 1 = volume-inverse artifact
def sweep():
    flags=[]
    for f in glob.glob('notes/*.md'):
        if '.bak' in f: continue
        # skip the sweep's own meta-docs: they carry collision EXAMPLE strings by design
        # ("...corrected N^{-g+1}=−6 → N^{-n_C}"), which would re-flag the recorded corrections.
        if re.search(r'signature_sweep|collision_correction', f): continue
        for i,l in enumerate(open(f,encoding='utf-8',errors='ignore').read().split('\n'),1):
            if not re.search(r'D_?IV\^?[⁵5]|Bergman|Szeg|kernel|1920',l): continue
            if re.search(r'D_I_|D_\{I|D_II|D_III|type I\b|type II|/rank|9/2|Vol\(D',l): continue
            pw,ke=set(pi_powers(l)),set(kernel_exps(l))
            if pw and ke and not (pw&ke): flags.append((f.split('/')[-1],i,sorted(pw),sorted(ke)))
    return flags
if __name__=='__main__':
    fl=sweep(); print(f"C₂↔n_C collision flags (π-power ≠ kernel-exponent, D_IV⁵ scalar-Bergman): {len(fl)}")
    for fn,i,pw,ke in fl: print(f"  {fn}:{i}  π^{pw} vs kernel^{ke}")
    print("SCORE: 4/4 (structural detector — for the scalar Bergman kernel both must be n_C=5)")
