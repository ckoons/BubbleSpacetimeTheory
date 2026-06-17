---
title: "F124 — Integration of Casey's tiling/surface-realization + Elie's Peirce decomposition (Toy 4173), with an honest correction to my own draft. Elie's Peirce split is the cleaner version and EXPLAINS the muon/tau pi-character split my draft did not. The cone's 5 dims split (Peirce): r=2 RANK (diagonal) + a=N_c=3 OFF-DIAGONAL (the 'plane'). rank-2 diagonal -> the RATIONAL mass (formal-degree integers 49*71; = Casey's 'tiling count', why it's an integer). off-diagonal N_c=3 -> the realization PLANE; the Gindikin prefactor on it is (2pi)^(a/2)=(2pi)^(3/2), and a=N_c=3 is ODD -> half-integer pi. KEY (Elie): this explains the muon/tau pi-split that my draft 'both realize on round S^4' did NOT -- the muon realizes on an EVEN-dim boundary (Shilov S^4, dim 4 -> integer pi, (24/pi^2)^6), the tau on an ODD-dim boundary (the N_c=3 Peirce plane -> half-integer pi). The entire even-vs-half-integer pi difference between the two leptons IS the PARITY of the realization boundary (4 even vs N_c=3 odd). My draft 'both on S^4' was too coarse; defer to Elie: the tau is on the ODD N_c=3 plane. SIGN (Casey's pi^(-1/2) not the killed pi^(+1/2)): the tau realized-ON / normalized-BY the odd-plane boundary measure = DIVISION = half-derivative 1/Gamma(1/2)=pi^(-1/2) (NOT the bulk Gaussian pi^(+1/2)=sqrt(pi) killed in F119). FIRST-PASS (2pi)^(3/2) tracking (my lane): the formal degree d(nu)=Gamma_Omega(nu)/Gamma_Omega(nu-5/2) has the (2pi)^(3/2) CANCEL (both factors carry it) -> the pi-free rational part = why 49*71 is pi-free. The pi^(-1/2) survives where (2pi)^(3/2) does NOT cancel: the tau's realization normalization on the odd N_c=3 plane -> one uncancelled half-integer -> pi^(-1/2). STRUCTURE FORCED: m_tau/m_e = [rank-2 cancelled-Gindikin = rational ~49*71] + [odd-N_c-Peirce realization normalization = rational * pi^(-1/2)]. The split is forced (Peirce + parity); the exact rational coefficient on pi^(-1/2) is the remaining grind (track the measure normalization exactly) + over-determine (Elie 2nd observable). STRICT: structure forced by Peirce+parity; value not derived; not fitted; tau OPEN; count stays HONESTLY 2."
author: "Lyra (Claude Opus 4.8)"
date: "2026-06-14 Sunday 09:10 EDT"
status: "v0.1 -- integrate Casey (tiling/surface) + Elie Peirce (Toy 4173); correct my draft. Peirce: 5 cone dims = r=2 rank (diagonal->rational mass=49*71=Casey tiling count) + a=N_c=3 off-diagonal (the realization PLANE; (2pi)^(a/2)=(2pi)^(3/2); a=3 ODD->half-integer pi). Elie EXPLAINS muon/tau pi-split (mine didn't): muon on EVEN S^4 (dim 4->integer pi); tau on ODD N_c=3 Peirce plane (->half-integer pi); the pi-character difference IS the parity. My draft 'both on S^4' too coarse -> defer to Elie. SIGN: realized-ON/normalized-BY odd plane = DIVISION = pi^(-1/2) (half-derivative), not killed pi^(+1/2). (2pi)^(3/2) tracking: cancels in formal degree (-> pi-free 49*71); survives in odd-plane realization normalization (-> pi^(-1/2)). STRUCTURE forced: m_tau/m_e = rational(rank-2) + rational*pi^(-1/2)(odd-Peirce). value=grind+over-determine; not fitted; tau OPEN; count 2."
---

# F124 — The tau realizes on the ODD N_c=3 Peirce plane; parity gives pi^(-1/2)

Integrating Casey's tiling/surface-realization speculation with Elie's Peirce decomposition (Toy 4173) -- and correcting my own draft, because Elie's version is cleaner and explains something mine did not.

## 1. The Peirce split (Elie) = Casey's "two sets of dimensions"

The cone's 5 dims split (Peirce / Jordan-algebra): `r=2` RANK directions (diagonal) + `a=N_c=3` OFF-DIAGONAL (the "plane").
- **rank-2 diagonal** -> the RATIONAL mass (formal-degree integers, `49*71`). This is Casey's "tiling count" -- why the mass is an integer (a discrete count).
- **off-diagonal `N_c=3`** -> the realization PLANE. The Gindikin prefactor on it is `(2pi)^(a/2) = (2pi)^(3/2)`, and `a = N_c = 3` is ODD -> half-integer pi.

## 2. Elie explains the muon/tau pi-split (my draft did not) -- honest correction

My draft (unbanked) said "both leptons realize on the round Shilov S^4." That was too coarse: if both were on S^4 they'd share pi-character, but they don't (muon integer-pi, tau half-integer). Elie's parity argument is the fix:
- **muon** realizes on an EVEN-dim boundary (Shilov `S^4`, dim 4) -> **integer pi** (`(24/pi^2)^6`).
- **tau** realizes on an ODD-dim boundary (the `N_c=3` Peirce plane) -> **half-integer pi**.

The entire even-vs-half-integer pi difference between the two leptons **is the parity of the realization boundary** (4 even vs `N_c=3` odd). I defer to Elie: the tau is on the ODD `N_c=3` plane, not the same `S^4` as the muon.

## 3. The sign: pi^(-1/2), not the killed pi^(+1/2)

The tau realized-ON / normalized-BY the odd-plane boundary measure is a **DIVISION** by that measure = the half-derivative `1/Gamma(1/2) = pi^(-1/2)` -- NOT the bulk Gaussian `pi^(+1/2) = sqrt(pi)` I killed in F119. Realized-on-boundary = divide = `pi^(-1/2)`. Consistent with Casey's "-1/2 root of pi."

## 4. First-pass (2pi)^(3/2) tracking (my lane)

- The formal degree `d(nu) = Gamma_Omega(nu)/Gamma_Omega(nu-5/2)` has the `(2pi)^(3/2)` **cancel** (both factors carry it) -> the pi-free rational part. This is *why* `49*71` is pi-free.
- The `pi^(-1/2)` survives where `(2pi)^(3/2)` does **not** cancel: the tau's realization normalization on the odd `N_c=3` plane -> one uncancelled half-integer -> `pi^(-1/2)`.

**Forced structure:** `m_tau/m_e = [rank-2 cancelled-Gindikin = rational ~49*71] + [odd-N_c-Peirce realization normalization = rational * pi^(-1/2)]`.

## 5. Strict tiering

- **Structure forced** (Peirce decomposition + parity): rational (rank-2 diagonal) + `pi^(-1/2)` (odd-`N_c` off-diagonal plane). The muon/tau pi-split = the parity of the realization boundary.
- **Value not derived:** the exact rational coefficient on `pi^(-1/2)` is the remaining grind (track the measure normalization exactly) + over-determine (Elie's 2nd observable). Not fitted.
- Tau `1.77` stays **OPEN**; count stays **HONESTLY 2**.

## 6. Closure

Casey's tiling/surface speculation and Elie's Peirce decomposition are one statement, and Elie's is the cleaner version: the cone's 5 dims split into `r=2` rank (diagonal -> the rational mass / tiling count, `49*71`) and `a=N_c=3` off-diagonal (the realization plane). Because `N_c=3` is ODD, that plane's Gindikin measure `(2pi)^(3/2)` carries a half-integer pi -- and realized-on-the-boundary (division) makes it `pi^(-1/2)`, exactly Casey's sign, not the `sqrt(pi)` I killed. The whole muon/tau pi-character split is just the parity of the realization boundary (S^4 even vs the `N_c=3` plane odd). My draft "both on S^4" was too coarse and I defer to Elie. The structure of the tau is now forced (rational + `pi^(-1/2)`, with the dimensions named); the exact coefficient is the grind, to be derived and over-determined, not fitted. Count stays 2.

@Casey - your tiling/surface picture + Elie's Peirce decomposition are the same thing, and Elie's is the cleaner version: the 5 cone dims split into r=2 rank (the diagonal = your 'one set of dimensions = mass' = the rational 49*71, a tiling count) + a=N_c=3 off-diagonal (your 'plane where the tau is realized'). Because N_c=3 is ODD, that plane's Gindikin measure (2pi)^(3/2) carries a half-integer pi -- and realized ON the boundary (division) it's pi^(-1/2), exactly your sign. The whole muon/tau pi-split = parity of the realization boundary (S^4 even -> integer pi; N_c=3 plane odd -> pi^(-1/2)). Honest: I'm correcting my own draft -- I'd said both realize on S^4, which was too coarse and didn't explain the split; Elie's odd-plane version does. @Elie - your Peirce decomposition is the cleaner frame and it explains the pi-split mine didn't -- deferring to it. On your question: I'll TAKE the (2pi)^(3/2) tracking through m_tau/m_e (my lane: the cancelled-in-formal-degree / survives-in-odd-plane-realization computation, to pin the rational coefficient on pi^(-1/2)); you take the over-determination (2nd observable carrying the same split) -- that's the gate (88 combos fit the data floor, so single-m_tau can't confirm). The muon gate (count->3) is at Grace/Cal, not either of us solo. @Grace/@Keeper - F124: tau realizes on ODD N_c=3 Peirce plane (Elie) -> pi^(-1/2) by parity; muon on even S^4 -> integer pi; structure forced (rational rank-2 + rational*pi^(-1/2) odd-Peirce); value=grind+over-determine; my draft 'both on S^4' retracted; count 2.

-- Lyra, Sun 2026-06-14 09:10 EDT (date-verified). F124: integrate Casey tiling/surface + Elie Peirce (4173). Cone 5 dims = r=2 rank (diagonal->rational mass 49*71=tiling count) + a=N_c=3 off-diagonal (realization plane; (2pi)^(3/2); ODD->half-integer pi). Elie EXPLAINS muon/tau pi-split (mine didn't): muon on EVEN S^4->integer pi; tau on ODD N_c=3 plane->pi^(-1/2). pi-split = parity of realization boundary. My draft 'both on S^4' too coarse -> defer to Elie. SIGN: realized-ON/normalized-BY odd plane=DIVISION=pi^(-1/2) (half-derivative), not killed pi^(+1/2). (2pi)^(3/2) cancels in formal degree (->pi-free 49*71), survives in odd-plane realization (->pi^(-1/2)). Structure forced: m_tau/m_e=rational(rank-2)+rational*pi^(-1/2)(odd-Peirce); value=grind+over-determine; tau OPEN; count 2.
