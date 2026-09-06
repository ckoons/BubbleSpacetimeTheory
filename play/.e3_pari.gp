\p 40
read(".r5_6000.gp");
\\ Lambda(s) = 4^{s/2} Gamma_C(s) Z5(s) = 2 pi^{-s} Gamma(s) Z5(s) = Lambda(5/2 - s); residue at 5/2 of 2*[1/(s-5/2)] = 2
L = lfuncreate([R5, 0, [0,1], 5/2, 4, 1, 2]);
print("lfuncheckfeq (log10 of the FE defect): ", lfuncheckfeq(L));
print("Lambda(1.25) = ", lfunlambda(L, 1.25), "   Z5(4) = ", lfun(L, 4));
\\ on-line zeros up to 100
zl = lfunzeros(L, 100);
print("on-line zeros below 100: ", #zl);
print("first ten: ", vector(min(10,#zl), i, zl[i]));
\\ argument principle: rectangle [-1/2, 3] x [0.1, T], adaptive-ish fixed fine step
wind(s1, s2, t1, t2, h) = {
  my(pts = List(), nR = ceil((t2-t1)/h), nT = ceil((s2-s1)/h), ph, tot = 0, prev, cur, d, mx = 0);
  for(k=0, nR, listput(pts, s2 + I*(t1 + (t2-t1)*k/nR)));
  for(k=1, nT, listput(pts, s2 - (s2-s1)*k/nT + I*t2));
  for(k=1, nR, listput(pts, s1 + I*(t2 - (t2-t1)*k/nR)));
  for(k=1, nT, listput(pts, s1 + (s2-s1)*k/nT + I*t1));
  prev = arg(lfunlambda(L, pts[1]));
  for(i=2, #pts, cur = arg(lfunlambda(L, pts[i])); d = cur - prev; while(d > Pi, d -= 2*Pi); while(d < -Pi, d += 2*Pi); if(abs(d) > mx, mx = abs(d)); tot += d; prev = cur);
  [round(tot/(2*Pi)), mx];
}
w50 = wind(-0.5, 3, 0.1, 50, 0.05);  print("winding [-1/2,3]x[0.1,50]: ", w50);
w100 = wind(-0.5, 3, 0.1, 100, 0.05); print("winding [-1/2,3]x[0.1,100]: ", w100);
\\ real segment sign changes between the poles
rs = 0; pv = real(lfunlambda(L, 0.05)); forstep(x = 0.06, 2.44, 0.01, cv = real(lfunlambda(L, x)); if(cv*pv < 0, rs++); pv = cv);
print("real zeros in (0, 5/2): ", rs, "; Lambda(1.25) sign ", sign(real(lfunlambda(L, 1.25))));
\\ off-line hunt in 1.25 < Re s < 3, 0.1 < t < 100 if the counts differ
found = List();
hunt(s1, s2, t1, t2) = {
  my(w = wind(s1, s2, t1, t2, min(0.05, (t2-t1)/6)), z);
  if(w[1] <= 0, return);
  if((s2-s1) < 0.05 && (t2-t1) < 0.05,
     z = solve_newton((s1+s2)/2 + I*(t1+t2)/2);
     listput(found, z); print("  ZERO: ", z, "   |Lambda| = ", abs(lfunlambda(L, z)), "   box winding ", wind(real(z)-0.01, real(z)+0.01, imag(z)-0.01, imag(z)+0.01, 0.002)); return);
  if((t2-t1) >= (s2-s1), hunt(s1, s2, t1, (t1+t2)/2); hunt(s1, s2, (t1+t2)/2, t2), hunt(s1, (s1+s2)/2, t1, t2); hunt((s1+s2)/2, s2, t1, t2));
}
solve_newton(z0) = { my(z = z0, f, df, h = 1e-8); for(i=1, 60, f = lfunlambda(L, z); df = (lfunlambda(L, z+h) - lfunlambda(L, z-h))/(2*h); z = z - f/df; if(abs(f/df) < 1e-25, break)); z; }
if(w100[1] > #zl, print("off-line zeros exist below 100: ", w100[1] - #zl, " -> hunting"); hunt(1.25, 3, 0.1, 100), print("all zeros below 100 are on the line"));
print("found: ", found);
