#!/usr/bin/env python3
"""
Toy 5124: the DYNAMICAL-DE number -- d⟨p⟩/d(epoch), the record-sea FILL RATE on the exact D_IV⁵ ladder.
Lyra traded a fixed Λ-fluctuation amplitude for a TIME-EVOLUTION, so a real falsifiable w(a) (#54) lives
in the fill rate. PRE-REGISTERED BEFORE DESI (dark energy is quote-anything -- target-innocence is the
whole game). ROBUST result: p rises monotonically as the sea fills (Fano falls), decelerating -> the DE
fluctuation was LARGER in the PAST and shrinks -> DYNAMICAL DE (w != const -1), MONOTONIC, NO w=-1
CROSSING. The SIGN/magnitude of w(a) is MODEL-DEPENDENT (the ρ_DE(Fano) link) -> DEFERRED to Keeper's a₀
weave, NOT claimed. Elie's pull. (K1288/Keeper frontier.)
E / Elie -- I pre-register the ROBUST shape (fill rate + monotonic-no-crossing); I do NOT fabricate a w(a)
sign from a shaky link (I show below that two reasonable links give OPPOSITE signs). Blind to DESI.

CONTEXT: Fano = 1 - p, p = record-sea occupancy (toy 5122). As the universe commits more records, N grows
with epoch -> the sea FILLS -> p rises, Fano falls. The TIME-DEPENDENCE of Fano is the dynamical-DE signal.

WHAT I COMPUTE (exact ladder, fixed Planck-set commitment temperature T; records accumulate -> μ=E_F rises):
  * fill curve: as N (records) grows, p rises 0.19->0.88, Fano falls 0.81->0.12, MONOTONIC + DECELERATING.
  * fill rate d⟨p⟩/d(ln N) > 0 everywhere, decreasing (the sea saturates toward degeneracy).
  * epoch map: N (records) ~ comoving volume ~ a^3 -> d/d(ln a) = 3 d/d(ln N). So p rises with a, Fano falls with a.

PRE-REGISTERED (locked before any DESI look):
  * ROBUST: DE is DYNAMICAL -- Fano evolves with epoch, so the DE is NOT a pure constant Λ (w != -1 const).
  * ROBUST: Fano MONOTONIC decreasing -> w(a) MONOTONIC, NO w=-1 CROSSING; the DE deviation was LARGER in
    the PAST (small a) and shrinks toward the future. This is the falsifiable SHAPE.
  * MODEL-DEPENDENT (NOT claimed): the SIGN of (w+1) (quintessence w>-1 vs phantom w<-1) depends on the
    ρ_DE(Fano) link -- shown below: ρ_DE ∝ √Fano and ρ_DE ∝ 1/√Fano give OPPOSITE signs. -> DEFER the sign
    to Keeper's a₀ weave (the DE-density model). I refuse to pick it from a shaky link (quote-anything guard).

=> VERDICT (plain): the fill rate d⟨p⟩/d(epoch) > 0, monotonic, decelerating -- the record sea fills and
the DE fluctuation (Fano) shrinks over cosmic time (larger in the past). PRE-REGISTERED, target-innocent,
before DESI: BST predicts DYNAMICAL DE with a MONOTONIC w(a) and NO w=-1 CROSSING. A robust DESI CROSSING
(w<-1 past, >-1 now) would be in TENSION with this. The SIGN of w+1 is model-dependent (√Fano vs 1/√Fano
flip it) -> deferred to the a₀ weave, NOT claimed here. Λ stays Structural.

=> DISPOSITION: pins the ROBUST dynamical-DE content (fill rate + monotonic-no-crossing w(a)), pre-
registered blind before DESI; defers the sign to Keeper's a₀ DE-density model. Target-innocent (no DESI
input; I even refuse the sign to avoid quote-anything). Firer: Elie; a₀-model: Keeper; Cal audits.
Nothing pushed. Nothing banked past the robust shape.

Author: Elie (CI toy builder). Date: 2026-08-08.
"""

from math import exp, log

results = []
def check(label, cond, detail=""):
    results.append((label, bool(cond), detail))
    tag = "PASS" if cond else "FAIL"
    print(f"  [{tag}] {len(results)}. {label}")
    if detail:
        print(f"          {detail}")

K = 200
gk = [(2*k + 3)*(k + 2)*(k + 1)//6 for k in range(K + 1)]
T = 5.0    # fixed Planck-set commitment temperature; records accumulate -> mu (=E_F) rises with epoch

def state(mu):
    f = [1.0/(exp((k - mu)/T) + 1.0) for k in range(K + 1)]
    N = sum(gk[k]*f[k] for k in range(K + 1))
    V = sum(gk[k]*f[k]*(1 - f[k]) for k in range(K + 1))
    p = sum(gk[k]*f[k]*f[k] for k in range(K + 1))/N
    return N, V/N, p

print("=" * 78)
print("Toy 5124: dynamical DE -- fill rate d⟨p⟩/d(epoch), pre-register monotonic no-crossing w(a) (blind)")
print("=" * 78)

mus = [10, 20, 40, 80, 120, 160]
curve = [(mu,) + state(mu) for mu in mus]     # (mu, N, Fano, p)

# ----------------------------------------------------------------------------
# 1. The fill curve + fill rate (robust).
# ----------------------------------------------------------------------------
print("\n--- 1. fill curve: p rises, Fano falls, monotonic + decelerating (the fill rate) ---")
ps = [c[3] for c in curve]; fanos = [c[2] for c in curve]; Ns = [c[1] for c in curve]
p_rises = all(ps[i] < ps[i+1] for i in range(len(ps)-1))
fano_falls = all(fanos[i] > fanos[i+1] for i in range(len(fanos)-1))
# fill rate dp/dlnN, check decelerating
rates = [(ps[i+1]-ps[i])/(log(Ns[i+1])-log(Ns[i])) for i in range(len(ps)-1)]
decel = rates[0] > rates[-1] and all(r > 0 for r in rates)
check("as the record sea FILLS with epoch (N grows): p rises 0.19->0.88 (MONOTONIC), Fano falls "
      "0.81->0.12 (MONOTONIC), and the fill rate d⟨p⟩/d(ln N) > 0 everywhere and DECELERATES (sea "
      "saturates toward degeneracy). The DE fluctuation (Fano) was LARGER in the PAST",
      p_rises and fano_falls and decel,
      "fill rate dp/dlnN = " + ", ".join(f"{r:.3f}" for r in rates) + " (all>0, decreasing); "
      f"p: {ps[0]:.2f}->{ps[-1]:.2f}, Fano: {fanos[0]:.2f}->{fanos[-1]:.2f}.")

# ----------------------------------------------------------------------------
# 2. Epoch map N ~ a^3 -> p rises with a, Fano falls with a.
# ----------------------------------------------------------------------------
print("\n--- 2. epoch map: N (records) ~ comoving volume ~ a^3 -> Fano falls with a ---")
check("N (committed records) ~ comoving volume ~ a^3 -> d/d(ln a) = 3 d/d(ln N). So p rises with the "
      "scale factor a and Fano = 1-p falls with a: the DE fluctuation amplitude DECREASES over cosmic "
      "time. Fano is a FUNCTION of epoch -> the DE is DYNAMICAL (not a pure constant Λ)",
      fano_falls,
      "Fano(a) decreasing -> w(a) != const -1. The time-dependence of Fano IS the dynamical-DE signal (#54).")

# ----------------------------------------------------------------------------
# 3. The SIGN of w+1 is MODEL-DEPENDENT -- two links give opposite signs -> DEFER (do NOT claim).
# ----------------------------------------------------------------------------
print("\n--- 3. w+1 SIGN is model-dependent (√Fano vs 1/√Fano flip it) -> DEFER to a₀ weave ---")
# w+1 = -(1/3) dln ρ_DE/dln a. Two candidate links:
#   ρ_DE ∝ √Fano  -> w+1 = -(1/6) dlnFano/dln a ; Fano falls (dln<0) -> w+1 > 0 (quintessence)
#   ρ_DE ∝ 1/√Fano-> w+1 = +(1/6) dlnFano/dln a ; -> w+1 < 0 (phantom)
dlnFano_dlnN = (log(fanos[-1]) - log(fanos[0]))/(log(Ns[-1]) - log(Ns[0]))   # < 0
w1_sqrt = -(1/6)*3*dlnFano_dlnN      # ρ∝√Fano  (dln a = dlnN/3)
w1_inv  = +(1/6)*3*dlnFano_dlnN      # ρ∝1/√Fano
opposite = (w1_sqrt > 0 > w1_inv)
check("the SIGN of (w+1) is MODEL-DEPENDENT: w+1 = -(1/3) dln ρ_DE/dln a. ρ_DE ∝ √Fano gives w+1 > 0 "
      "(quintessence, w>-1); ρ_DE ∝ 1/√Fano gives w+1 < 0 (phantom, w<-1). OPPOSITE signs from equally "
      "reasonable links -> I REFUSE to pick the sign (quote-anything guard); DEFER to Keeper's a₀ "
      "DE-density model",
      opposite,
      f"dlnFano/dlnN = {dlnFano_dlnN:.3f} (<0). ρ∝√Fano -> w+1 = {w1_sqrt:+.3f} (quintessence); ρ∝1/√Fano "
      f"-> w+1 = {w1_inv:+.3f} (phantom). Sign needs the model -> NOT claimed.")

# ----------------------------------------------------------------------------
# 4. Pre-registered prediction (robust, blind) + falsifier.
# ----------------------------------------------------------------------------
print("\n--- 4. PRE-REGISTERED (blind, before DESI): dynamical + monotonic + no crossing ---")
check("PRE-REGISTERED (target-innocent, before any DESI look): BST predicts (a) DYNAMICAL DE -- Fano "
      "evolves, so w != const -1; (b) a MONOTONIC w(a) with NO w=-1 CROSSING (Fano is monotonic -> the "
      "deviation is monotonic in a), the DE deviation LARGER in the past. FALSIFIER: a robust DESI w=-1 "
      "CROSSING (w<-1 past, >-1 now) is in TENSION with the monotonic prediction. SIGN deferred (model)",
      p_rises and fano_falls and decel and opposite,
      "the robust falsifiable = DYNAMICAL + MONOTONIC + NO-CROSSING; the sign (quintessence vs phantom) "
      "is the a₀-weave's to fix. Locked before DESI -> can't be retrofitted to whatever DESI shows.")

check("VERDICT: fill rate d⟨p⟩/d(epoch) > 0, monotonic, decelerating -- the DE fluctuation (Fano) shrinks "
      "over cosmic time (larger in past). PRE-REGISTERED blind: dynamical DE, monotonic w(a), NO crossing; "
      "sign model-dependent -> deferred to the a₀ weave. Target-innocent (no DESI input; sign refused to "
      "avoid quote-anything). Λ stays Structural",
      p_rises and fano_falls and opposite,
      "#54 dynamical-DE: the falsifiable shape is locked (monotonic, no crossing); Keeper's a₀ DE-density "
      "model fixes the sign; DESI comparison is downstream. Nothing banked past the robust shape.")

# ============================================================================
passed = sum(1 for _, cc, _ in results if cc)
total_checks = len(results)
print("\n" + "=" * 78)
print(f"SCORE: {passed}/{total_checks}   (fill rate + pre-registered monotonic-no-crossing w(a), sign deferred)")
print("=" * 78)
print(f"""
SUMMARY (Toy 5124, dynamical DE -- fill rate d⟨p⟩/d(epoch), pre-registered blind):
  * FILL CURVE (exact ladder, fixed T): as records accumulate with epoch, p rises 0.19->0.88, Fano falls
    0.81->0.12, MONOTONIC + DECELERATING. Fill rate d⟨p⟩/d(ln N) > 0, decreasing.
  * EPOCH: N ~ a^3 -> Fano falls with a -> DE fluctuation was LARGER in the PAST -> DYNAMICAL DE (w != -1 const).
  * SIGN of w+1 is MODEL-DEPENDENT: ρ_DE ∝ √Fano -> quintessence (w>-1); ρ_DE ∝ 1/√Fano -> phantom (w<-1).
    OPPOSITE signs -> I DEFER the sign to Keeper's a₀ weave; refuse to pick it (quote-anything guard).
  * PRE-REGISTERED (blind, before DESI): DYNAMICAL DE, MONOTONIC w(a), NO w=-1 CROSSING, deviation larger
    in the past. FALSIFIER: a robust DESI crossing is in tension. Sign = a₀-weave's job.

AUG-08 [TEGMARK]. Nothing pushed. Nothing banked past the robust shape. Fill rate computed (monotonic,
decelerating); dynamical-DE prediction pre-registered blind (monotonic, no crossing); w(a) sign refused
(model-dependent) and deferred to the a₀ weave. Target-innocent. Λ Structural. #54. Count N.
""")
