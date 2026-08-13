#!/usr/bin/env python3
"""
DES-SN5YR full-covariance chi^2 helper — NUMPY-FREE (Keeper, K1446/K1447, for Grace).

Why numpy-free: numpy is broken in this environment (Grace's and Keeper's both).
The .npz is a zip of .npy arrays; we parse it in pure Python.

KEY FACTS (from DES-Dovekie-SN_Likelihood.py, authoritative):
  * The stored 'cov' array is the UPPER TRIANGLE (row-major, i<=j) of the
    INVERSE covariance matrix (Covtot_inv), NOT the covariance.  n=1820.
    -> For a chi^2 fit you WANT the inverse covariance, so no inversion needed.
  * SN order in the matrix == row order in DES-Dovekie_HD.csv.
  * Analytic marginalization over the absolute magnitude M (DES formula):
        chi2_marg = A - B^2 / C
        A = d^T Cinv d ,  B = 1^T Cinv d ,  C = 1^T Cinv 1 ,  d = mu_data - mu_model

Usage:
    from des_sn5yr_chi2_helper import load, marg_chi2
    z, mu, err, invcov, n = load()             # invcov is a flat n*n array.array('f')
    chi2 = marg_chi2(mu_model_list, mu, invcov, n)   # mu_model up to a constant M
"""
import zipfile, ast, struct, array, math, os

HERE = os.path.dirname(os.path.abspath(__file__))

def _read_npz(path):
    out = {}
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            raw = z.read(name); major = raw[6]
            if major == 1: hlen = struct.unpack('<H', raw[8:10])[0]; off = 10
            else:          hlen = struct.unpack('<I', raw[8:12])[0]; off = 12
            d = ast.literal_eval(raw[off:off+hlen].decode('latin1')); body = raw[off+hlen:]
            tc = {'<f4':'f','<f8':'d','<i8':'q','|b1':'b'}.get(d['descr'])
            if tc: a = array.array(tc); a.frombytes(body); out[name.replace('.npy','')] = (d['shape'], a)
    return out

def load(cov_tag="STAT+SYS"):
    """Returns z[], mu[], err[], invcov (flat n*n array.array 'f', symmetric), n."""
    npz = _read_npz(os.path.join(HERE, f"DES-SN5YR_{cov_tag}.npz"))
    n = npz['nsn'][1][0]
    tri = npz['cov'][1]                                   # upper-triangle (i<=j) of INVERSE cov
    inv = array.array('f', [0.0]) * (n * n)
    k = 0
    for i in range(n):
        base = i * n
        for j in range(i, n):
            v = tri[k]; k += 1
            inv[base + j] = v
            inv[j * n + i] = v                            # symmetrize
    # data vector, in the SAME order as the matrix
    z = []; mu = []; err = []; hdr = None
    with open(os.path.join(HERE, "DES-SN5YR_Dovekie_HD.csv")) as f:
        for line in f:
            s = line.strip()
            if not s or s.startswith('#'): continue
            p = [x.strip() for x in (s.split(',') if ',' in s else s.split())]
            if hdr is None:
                hdr = [h.upper() for h in p]
                iz, imu, ie = hdr.index('ZHD'), hdr.index('MU'), hdr.index('MUERR'); continue
            z.append(float(p[iz])); mu.append(float(p[imu])); err.append(float(p[ie]))
    return z, mu, err, inv, n

def _matvec(inv, x, n):
    y = [0.0] * n
    for i in range(n):
        base = i * n; s = 0.0
        row = inv[base:base+n]
        for j in range(n):
            s += row[j] * x[j]
        y[i] = s
    return y

def marg_chi2(mu_model, mu_data, inv, n):
    """chi2 marginalized analytically over the absolute magnitude M (DES formula)."""
    d = [mu_data[i] - mu_model[i] for i in range(n)]
    Cinv_d = _matvec(inv, d, n)
    ones = [1.0] * n
    Cinv_1 = _matvec(inv, ones, n)
    A = sum(d[i] * Cinv_d[i] for i in range(n))
    B = sum(Cinv_d[i] for i in range(n))            # 1^T Cinv d
    C = sum(Cinv_1[i] for i in range(n))            # 1^T Cinv 1
    return A - B*B / C

# --- pure-Python flat-LCDM distance modulus (for validation / a fit baseline) ---
def mu_lcdm(z, Om=0.315, H0=70.0):
    c = 299792.458
    out = []
    for zi in z:
        # comoving distance integral, Simpson, up to a constant absorbed by M
        m = 200
        h = zi / m; s = 0.0
        for k in range(m+1):
            zp = k*h
            E = math.sqrt(Om*(1+zp)**3 + (1-Om))
            w = 1.0 if (k==0 or k==m) else (4.0 if k%2 else 2.0)
            s += w/E
        integral = s*h/3.0
        dC = (c/H0)*integral
        dL = (1+zi)*dC
        out.append(5.0*math.log10(dL) + 25.0)
    return out

if __name__ == "__main__":
    z, mu, err, inv, n = load()
    # sanity 1: diagonal of the INVERSE cov should ~ 1/MUERR^2 for a near-diagonal case;
    # for STAT+SYS it is >= 1/MUERR^2-ish but correlated — check STATONLY for the clean test.
    zs, mus, errs, invs, ns = z, mu, err, *[None], None
    zS, muS, errS, invS, nS = load("STATONLY")
    diag0 = invS[0];
    print(f"n={n};  STATONLY diag[0]={diag0:.4f}  vs 1/MUERR0^2={1.0/errS[0]**2:.4f}  (should match -> packing/inverse confirmed)")
    # sanity 2: full-cov marginalized chi2 for a fiducial LCDM
    chi2 = marg_chi2(mu_lcdm(z, Om=0.315), mu, inv, n)
    print(f"full STAT+SYS marginalized chi2 (LCDM Om=0.315) = {chi2:.1f}  over n={n} SNe")
