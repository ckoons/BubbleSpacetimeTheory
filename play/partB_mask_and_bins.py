#!/usr/bin/env python3
"""Part B (v), v1.4 §2.2: PER-SOURCE mask (great-circle): |b| > 30° and angular distance > 5° from the LMC (280.5, −32.9) and > 3° from the SMC (302.8, −44.3).
Writes the masked sample and the per-bin subsamples (ra, dec) as FITS for the released selection-function code. Computes nothing else."""
import sys, numpy as np
from astropy.io import fits
from astropy.table import Table
ZE=[0.0,0.8,1.3,1.8,2.4,np.inf]
def vec(l,b): l=np.radians(l); b=np.radians(b); return np.stack([np.cos(b)*np.cos(l),np.cos(b)*np.sin(l),np.sin(b)],-1)
for tag,edges in (("G20.5",ZE),("G20.0",[0.0,1.3,1.8,np.inf])):
    t=Table.read(f'../data/quaia/quaia_{tag}.fits'); l=np.array(t['l'],float); b=np.array(t['b'],float); v=vec(l,b)
    keep=(np.abs(b)>30.0)&(v@vec(280.5,-32.9)<np.cos(np.radians(5.0)))&(v@vec(302.8,-44.3)<np.cos(np.radians(3.0)))
    print(f"{tag}: per-source mask keeps {keep.sum():,} of {len(t):,}")
    tm=t[keep]; tm.write(f'../data/quaia/partB_{tag}_masked.fits',overwrite=True)
    z=np.array(tm['redshift_quaia'],float)
    for i in range(len(edges)-1):
        sel=(z>=edges[i])&(z<edges[i+1]); tm[sel]['ra','dec'].write(f'../data/quaia/partB_{tag}_bin{i+1}.fits',overwrite=True); print(f"   bin {i+1} [{edges[i]},{edges[i+1]}): {sel.sum():,}")
