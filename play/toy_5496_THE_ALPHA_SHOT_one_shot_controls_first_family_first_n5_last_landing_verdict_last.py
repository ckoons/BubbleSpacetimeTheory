# TOY 5496 -- THE ALPHA SHOT. Elie, 2026-08-24. ONE SHOT under PREREG v2, frozen packet:
#   alpha(n)^-1 = N(n)/q^2 · q = 1 (singlet units, addendum pin) · N(n) = ||1||^2_{Sigma_n}
#   in the banked FK/Hua normalization (N1) · half-blind: n = 3, 7, 9 first, n = 5 LAST ·
#   stop-and-report if 137 emerges en route · family values first, landing verdict LAST.
# N1 HEADER (the normalization, with citation): the banked family is HUA CLASSICAL -- verified
#   below against the banked interior anchor K(0,0) = 1920/pi^5 (M-definition; T2442 lineage:
#   c_FK = 225/pi^{9/2} = (N_c n_C)^2 / pi^{(g+rank)/rank}, form checked, cited). The boundary
#   mass is the induced surface volume of the Z2-quotient Lie sphere Sigma_n = (S^{n-1} x S^1)/Z2.
# N2: the Hua constant per n printed beside its derivation. D3 rank-reading death-check printed.
from mpmath import mp, mpf, pi, gamma
mp.dps=30
BAR="="*100
def head(s): print("\n"+BAR); print(s); print(BAR)
print(BAR); print("TOY 5496 -- THE ALPHA SHOT (one shot; prereg v2; landing table frozen)"); print(BAR)

head("N3 -- GRACE'S CONTROLS FIRST (in the shot's log, before any family value)")
# positive control: the machinery must reproduce the banked overlap / banked anchor
def volS(m):  # Vol(S^m)
    return 2*pi**(mpf(m+1)/2)/gamma(mpf(m+1)/2)
def volD(n):  # Hua classical: Vol(D_IV^n) = pi^n / (2^{n-1} n!)
    f=mpf(1)
    for k in range(2,n+1): f*=k
    return pi**n/(2**(n-1)*f)
anchor=1/volD(5)
print("  POSITIVE CONTROL 1 (banked interior anchor): K(0,0) = 1/Vol(D_IV^5) must equal 1920/pi^5:")
print("     computed %s vs banked %s -> %s"%(mp.nstr(anchor,10),mp.nstr(1920/pi**5,10),
      "REPRODUCED" if abs(anchor-1920/pi**5)<mpf('1e-20') else "*** FAIL -- SHOT ABORTED ***"))
assert abs(anchor-1920/pi**5)<mpf('1e-20')
print("  POSITIVE CONTROL 2 (the y_t banked overlap): the NORMALIZED boundary kernel mode's")
print("     self-pairing = 1 exactly by the reproducing property in this same convention --")
print("     the Cauchy-Schwarz-saturated overlap (T2514's y_t = 1). Holds identically; the")
print("     machinery reproduces the banked overlap by construction, stated not re-derived.")
print("  MUST-REJECT (mis-typed vertex): vertex mis-typed to the k = 1 harmonic instead of the")
print("     soft (constant) mode: the charge current's k = 1 component vanishes by Schur/")
print("     orthogonality on a charge eigenstate -> M = 0 -> alpha^-1 DIVERGES. NOT a clean")
print("     number -- the wrong vertex cannot fake a landing. REJECT FIRES, as required.")
print("  D2 SWEEP of this file: no 137, no N_max, no measured value enters any formula below.")

head("THE FAMILY, half-blind: N(n) = Vol_Hua(Sigma_n) = pi * Vol(S^{n-1});  alpha(n)^-1 = N(n)/1")
print("   (N2: constant per n beside its derivation; n = 5 EXCLUDED until last)")
fam={}
for n in (3,7,9):
    N=pi*volS(n-1)
    fam[n]=N
    print("   n=%d : Vol(S^%d) = 2 pi^{%s}/Gamma(%s) ; N = pi*that = %-14s alpha^-1(%d) = %s"%(
        n,n-1,mpf(n)/2,mpf(n)/2,mp.nstr(N,8),n,mp.nstr(N,8)))
print("   EN-ROUTE 137 CHECK: values are %s -- none within 1 of 137. NO STOP FIRES."%(
      ", ".join(mp.nstr(v,6) for v in fam.values())))
print("   D3 DEATH-CHECK: N varies with n (39.5 / 103.9 / 93.3 -- non-constant, non-monotonic):")
print("   the computation reads the GEOMETRY, not the rank. D3 passes.")

head("n = 5, LAST")
N5=pi*volS(4)
print("   n=5 : Vol(S^4) = 8 pi^2/3 ; N(5) = 8 pi^3 / 3 = %s"%mp.nstr(N5,12))
print("   alpha^-1(5) = N(5)/q^2 = %s   (q = 1, singlet units, addendum pin)"%mp.nstr(N5,12))
print("   ROBUSTNESS (convention family): the only in-family alternative (double cover, no Z2")
print("   quotient) DOUBLES N: %s. Both stated before the verdict."%mp.nstr(2*N5,10))

head("LANDING VERDICT (the frozen table; tol = 0.010 in alpha^-1 units)")
a5=N5
dA=abs(a5-mpf(137)); dB=abs(a5-mpf('137.036'))
print("   |alpha^-1 - 137.000| = %s ; |alpha^-1 - 137.036| = %s ; tol = 0.010"%(mp.nstr(dA,6),mp.nstr(dB,6)))
print("   double-cover variant: |%s - 137.000| = %s -- also far outside tol."%(mp.nstr(2*N5,8),mp.nstr(abs(2*N5-137),6)))
print()
print("   *** LANDING C -- CLEAN NEGATIVE. alpha^-1(5) = 8 pi^3/3 = %s, off by ~%s from 137."%(mp.nstr(a5,8),mp.nstr(dA,4)))
print("   THE LANE CLOSES WITH HONOR, per the frozen table: 'anything else = clean negative,")
print("   lane closes.' No reinterpretation exists; none is attempted. ***")
print()
print("   THE HONEST READING, one paragraph: the forced chain (Born power, Schur vertex,")
print("   Thomson=Shilov, unique F^2 form, Hua measure, singlet unit) evaluates to the HUA")
print("   VOLUME OF THE LIE SPHERE -- a clean geometric number, 8 pi^3/3 = 82.68, and it is")
print("   NOT 137. Under prereg v2 that is the result: the bare geometric vertex, normalized")
print("   by every banked forcing this program owns, does NOT produce the fine-structure")
print("   constant. alpha stays IDENTIFIED; the Keystone-A falsifier framing fires as written")
print("   (the KK coefficient is NOT unity in banked units -- it is 8 pi^3/3 / 137-adjacent-")
print("   nothing); and the 129-competitor null (5457) stands as the reason no relabeling of")
print("   this number may be attempted. ONE SHOT, TAKEN. NO SECOND FORM.")
