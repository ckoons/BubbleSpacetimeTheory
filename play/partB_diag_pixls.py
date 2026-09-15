#!/usr/bin/env python3
"""Part B DIAGNOSTIC ONLY (Cal §972, 2026-09-15): a HEALPix-pixel-level weighted least-squares dipole with the §2.3 footprint (sf >= 0.5) and the
§2.2 mask built into the design matrix. NOT the (vi) estimator (§4.1 names the weighted unit-vector sum with the mask-mode correction, code
retained at commit 4ce873ce = r145_eb_lib.py sha256 b87a8b08...). Permitted as a diagnostic under three conditions: runs under (vi)'s blindness;
its vector is posted WITH the (vi) vector labelled "diagnostic, not the criterion"; a disagreement beyond the mock covariance is named by Keeper
at (vii) as a report, not a landing clause. Moved out of r145_eb_lib.py (which is restored byte-for-byte to 4ce873ce) on Cal's instruction."""
import hashlib, numpy as np
def diag_hash(): return hashlib.sha256(open(__file__,'rb').read()).hexdigest()[:12]
def dipole_ls_pix(wcounts,footprint,centers,area):
    """weighted LS of per-pixel weighted counts n_p = area_p [a + b.n_p] over footprint pixels; Poisson-LS covariance with the pixel's own weight scale.
    Returns D = b/a and its 3x3 covariance (delta method)."""
    A=area[footprint]; X=np.column_stack([A,A[:,None]*centers[footprint]]); y=wcounts[footprint].astype(float); a0=y.sum()/A.sum(); w=1/(A*a0)
    XtW=X.T*w; G=XtW@X; p=np.linalg.solve(G,XtW@y); a,b=p[0],p[1:]; D=b/a; covp=np.linalg.inv(G); J=np.zeros((3,4)); J[:,0]=-b/a**2; J[:,1:]=np.eye(3)/a
    return D,J@covp@J.T
