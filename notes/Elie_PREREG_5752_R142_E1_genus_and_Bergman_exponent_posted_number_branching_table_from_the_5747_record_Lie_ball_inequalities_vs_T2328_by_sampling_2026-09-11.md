# Elie PREREG — Toy 5752, Round 142 E1 (three checks, one toy). Written 2026-09-11 12:45 EDT, before the run.

Instrument: play/toy_5752_*.py. Exact arithmetic (Fraction) for every closed form; numpy uniform sampling of [-1,1]^10 for the Monte-Carlo lines; toy_5747 re-run as a subprocess and its stdout parsed (the record, not a recomputation).

## (i) genus and the Bergman-kernel exponent
- P1 (arithmetic, cannot fail): genus(r,a,b) = (r-1)a + b + 2 at (2,3,0) = 5. Also printed: the two integers the Guide used to quote, n_C + 1 = 6 and g = 7, and the ball's exponent d+1 at d = 5 (= 6).
- Convention pinned: exponent p is defined by K(z,z) = (1/V) N(z,z)^{-p}, N(z,w) = 1 - 2 z.w~ + (z.z)(w~.w~) (Hua's norm function; on the diagonal N = 1 - 2|z|^2 + |z.z|^2). Along the real ray t e1, N = (1-t^2)^2; along the isotropic ray t(e1+ie2)/sqrt2, N = 1 - 2t^2.
- Instrument A (degree-1 cell, exact identity): K_0 + K_1 on the real ray gives c1/c0 = V/||z1||^2_{A^2} = 2p, i.e. p = n/(2 <|z|^2>_D) with <.>_D the uniform mean over the domain. PREDICTION P2 (can fail): p_hat = 5/(2<|z|^2>) lands within 3 sigma of 5 and more than 5 sigma from 6.
- Instrument B (reproducing property, direct): (1/V) int_D |N(z,w0)|^{-2p} dV = N(w0,w0)^{-p} holds iff p is the exponent. Sweep p in {4, 9/2, 5, 11/2, 6, 7} at w0 = 0.4 e1 and w0 = 0.4 (e1+ie2)/sqrt2. PREDICTION P3 (can fail): the ratio LHS/RHS is 1 within 3 sigma at p = 5 on BOTH rays and off by > 5 sigma at p = 6 on both.
- Control P4: the unit ball B^5 under the same two instruments gives p = 6 = d+1 (and B^4 gives 5, so the instrument is not stuck at 5).

## (ii) Lecture 3's branching table from the 5747 record
- PREDICTION P5 (can fail — the lecture could misquote): toy_5747 re-run prints, for k = 0..5 zonal, light = (k+3)/(2k+3) and matter = k/(2k+3) — i.e. 1,0; 4/5,1/5; 5/7,2/7; 2/3,1/3; 7/11,4/11; 8/13,5/13 — and the record's three-write word is 3/7 via 1/5 + (4/5)(2/7); and the Bergman deficits printed are 1/2, 10/21, 25/63 at (0,0), (0,1), (1,1). The lecture's sentence is regex-extracted and compared fraction by fraction; a mismatch in either direction is a MISS.

## (iii) Lecture 1's Lie-ball inequalities vs the corpus definition (T2328, Hua form)
- Sets: L = {|z.z| < 1 and 1 - 2|z|^2 + |z.z|^2 > 0} (Lecture 1); C = {|z|^2 < 1 and 1 - 2|z|^2 + |z.z|^2 > 0} (registry T2328); H = {|z|^2 + sqrt(|z|^4 - |z.z|^2) < 1} (the Lie-norm form).
- PREDICTION P6 (can fail): on 60M uniform points of [-1,1]^10 the symmetric differences L^C and L^H are EMPTY (count 0), with the one-line proof printed: |z.z| <= |z|^2 (Cauchy-Schwarz), so C => L; and if |z|^2 >= 1 with |z.z| < 1 then 1 - 2|z|^2 + |z.z|^2 < 2 - 2|z|^2 <= 0, so L => C.
- Control P7: each clause is load-bearing — the quartic alone (Q) contains points outside C (the outer component; count > 0), and |z.z| < 1 alone (S) contains points outside C (count > 0).
- P8 (control): on 10^5 Shilov points z = e^{it} x, x in S^4, both clauses sit on their boundary values: |z.z| = 1 and N(z,z) = 0 to 1e-12.

Score reported as k/N with the can-fail count named. Numbers first, readings second.
