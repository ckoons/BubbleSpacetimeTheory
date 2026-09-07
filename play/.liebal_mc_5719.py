import numpy as np, math, json
rng = np.random.default_rng(23); keep = []
for chunk in range(14):
    z = rng.uniform(-1, 1, size=(6_000_000, 5)) + 1j*rng.uniform(-1, 1, size=(6_000_000, 5))
    r2 = (np.abs(z)**2).sum(1); zz = (z*z).sum(1); azz2 = np.abs(zz)**2
    m = (r2 < 1) & (azz2 - 2*r2 + 1 > 0); keep.append(z[m])
z = np.concatenate(keep); r2 = (np.abs(z)**2).sum(1); zz = (z*z).sum(1)
print("Lie-ball samples:", len(z), " volume fraction of the cube:", len(z)/(14*6e6))
def push(f2):
    B = 25; idx = np.array_split(np.arange(len(f2)), B); e = np.array([(f2[i]*(1-r2[i])).sum()/f2[i].sum() for i in idx]); return e.mean(), e.std()/math.sqrt(B)
out = {}
for k, f2 in {"m=1 z1": np.abs(z[:,0])**2, "m=2 z.z": np.abs(zz)**2, "m=3 matter (z.z)(v.z)": np.abs(zz*z[:,0])**2, "m=3 light z3z4z5": np.abs(z[:,2]*z[:,3]*z[:,4])**2, "m=3 z1^3": np.abs(z[:,0])**6, "m=5 (z.z)^2 z1": np.abs(zz*zz*z[:,0])**2}.items():
    e, s = push(f2); out[k] = (e, s); print(f"  {k:24s} 1 - <|z|^2> = {e:.4f} +/- {s:.4f}")
json.dump(out, open('.liebal_push_5719.json', 'w'), indent=1)
