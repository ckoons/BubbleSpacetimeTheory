#!/usr/bin/env python3
"""Part B step (iv) — download Quaia v1.0.0 (Zenodo 10.5281/zenodo.10403370) and record the FITS header VERBATIM as the first act.
NOT RUN until Cal's v1.2 hash is on the board and Keeper has verified it. Computes nothing else: no counts, no dipole.
Usage: python3 partB_iv_download_quaia.py <zenodo_file_url> [<zenodo_file_url> ...]  -> data/quaia/<file>, notes/partB_QUAIA_FITS_HEADER_<date>.txt"""
import sys, os, hashlib, subprocess, datetime
from astropy.io import fits
root=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..'); out=os.path.join(root,'data','quaia'); os.makedirs(out,exist_ok=True)
stamp=datetime.datetime.now().strftime('%Y-%m-%d_%H%M')
for url in sys.argv[1:]:
    parts=[x for x in url.split('/') if x]; name=parts[-2] if parts[-1]=='content' else parts[-1].split('?')[0]   # Zenodo API URLs end in /content
    fn=os.path.join(out,name); print(f"downloading {url} -> {fn}")
    subprocess.run(['curl','-L','-A','Mozilla','-o',fn,url],check=True)
    raw=open(fn,'rb').read(); sha=hashlib.sha256(raw).hexdigest(); md5=hashlib.md5(raw).hexdigest(); print(f"sha256 {sha}  md5 {md5}  size {os.path.getsize(fn):,} bytes")
    hdr_path=os.path.join(root,'notes',f'partB_QUAIA_FITS_HEADER_{os.path.basename(fn)}_{stamp}.txt')
    with fits.open(fn,memmap=True) as h:
        with open(hdr_path,'w') as f:
            f.write(f"# {os.path.basename(fn)}  sha256 {sha}  md5 {md5}  size {os.path.getsize(fn)}  recorded {stamp} — VERBATIM, first act of step (iv)\n")
            for i,hdu in enumerate(h):
                f.write(f"\n##### HDU {i} ({type(hdu).__name__}) #####\n"); f.write(hdu.header.tostring(sep='\n',endcard=True,padding=False)); f.write("\n")
    print(f"header written verbatim to {hdr_path}")
