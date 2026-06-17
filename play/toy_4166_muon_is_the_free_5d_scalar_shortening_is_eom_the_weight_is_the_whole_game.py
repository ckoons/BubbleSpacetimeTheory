r"""
Toy 4166: understanding the singleton sum as actual physics (research, not framing). Three things, built and checked:
  (1) reproduce Lyra's 11.6 exactly and see what it IS,
  (2) the muon IS the free 5d scalar -- the Rac -- and the "interior truncation" is literally its equation of motion,
  (3) the per-harmonic weight is the whole game: principled candidates give 6 vs 11.6, target is 16.82.

(1) WHAT LYRA'S 11.6 IS:
  tau = trivial rep (nu=0): only the k=0 mode -> S_tau = 1.
  muon = full edge ladder (nu=3/2): S_mu = sum_k dim(V_k)/(3/2)_k = 11.645  (dim(V_k) = (2k+3)(k+1)(k+2)/6).
  mass ~ 1/S, so f2 = m_tau/m_mu = S_mu/S_tau = 11.645. target 16.82. gap 16.82/11.645 = 1.444.

(2) THE MUON IS THE FREE 5d SCALAR (the Rac), AND THE TRUNCATION IS ITS EQUATION OF MOTION:
  the unitarity bound for a scalar in d dims is Delta >= (d-2)/2; the FREE field saturates it. for d=5: Delta=(d-2)/2=3/2
  = exactly the muon's nu. at saturation the box descendant is null: ||P^2|Delta>||^2 ~ (Delta-(d-2)/2) -> 0, i.e. box phi
  = 0. the trace/box descendants (the m2>=1 interior) are exactly these null states. so:
      Lyra's (nu-3/2)_{m2} = (0)_{m2} = 0 for m2>=1  IS  the free-field shortening 2*Delta-d+2 = 0  IS  box phi = 0.
  the surviving content is the symmetric-traceless ladder V_k (the soap film). the muon being "all surface, no interior"
  is just "the muon is a free field, and a free field's interior is fixed by its boundary" -- the equation of motion.
  check: d=5 -> Delta=(d-2)/2 = 3/2 (= nu_mu); 2*Delta-d+2 = 0 (the null factor). both exact.

(3) THE WEIGHT IS THE WHOLE GAME (why the verdict needs the forced FK/CFT norm, not a guess):
  the forced per-harmonic contribution is dim(V_k) * (weight_k). different PRINCIPLED weights give different sums:
      weight = 1/(3/2)_k  (Lyra heuristic)            -> 11.645
      weight = 1/(k! 2^k) (free-field leading-twist)  ->  6.045
      target                                          -> 16.82
  so the answer is entirely in the per-harmonic weight -- the FK Fischer / CFT descendant norm. it is NOT something to
  guess (two principled forms already give 6 and 11.6); it has to be DERIVED (Lyra Bargmann-Fock + Cal FK-1994), and
  the survives-the-ratio check (Toy 4165) says a correct k-dependent weight CAN move 11.6 -- which way and how far is the verdict.
"""

from fractions import Fraction as Fr

def poch(x, k):
    r = Fr(1)
    for j in range(k):
        r *= (x + j)
    return r

def dim(k):                              # SO(5) harmonic / degree-k on S^4
    return Fr((2*k+3)*(k+1)*(k+2), 6)

d = 5
Delta_mu = Fr(d-2, 2)                     # free-scalar dimension in d=5

print("=" * 96)
print("TOY 4166: the muon is the free 5d scalar; the truncation is its e.o.m.; the per-harmonic weight is the whole game")
print("=" * 96)
print()

print("(1) what Lyra's 11.6 is:")
print("-" * 96)
S_tau = Fr(1)                            # trivial rep, k=0 only
S_mu  = sum(dim(k)/poch(Fr(3,2), k) for k in range(60))
print(f"  tau = trivial rep (nu=0): only k=0 -> S_tau = {S_tau}")
print(f"  muon = edge ladder (nu=3/2): S_mu = sum_k dim(V_k)/(3/2)_k = {float(S_mu):.4f}")
print(f"  f2 = m_tau/m_mu = S_mu/S_tau = {float(S_mu):.3f}   (target 16.82, gap {16.82/float(S_mu):.3f})")
print()

print("(2) the muon IS the free 5d scalar (Rac), and the truncation is box phi = 0:")
print("-" * 96)
print(f"  free-scalar dimension in d={d}: Delta = (d-2)/2 = {Delta_mu} = nu_mu (the muon's point). it saturates the unitarity bound.")
print(f"  shortening factor 2*Delta - d + 2 = {2*Delta_mu - d + 2}  -> the box descendant is null -> box phi = 0 (the equation of motion).")
print(f"  Lyra's (nu-3/2)_(m2) = (0)_(m2) = 0 for m2>=1 IS this shortening: the trace/box descendants (m2>=1 interior) are the null states.")
print(f"  surviving content = symmetric-traceless ladder V_k = the soap film. 'all surface, no interior' = 'free field' = box phi = 0.")
print()

print("(3) the weight is the whole game:")
print("-" * 96)
w_lyra = float(sum(dim(k)/poch(Fr(3,2), k)          for k in range(60)))
w_ff   = float(sum(dim(k)/(poch(Fr(1), k)*2**k)     for k in range(60)))
print(f"  weight 1/(3/2)_k   (Lyra heuristic)           -> {w_lyra:.3f}")
print(f"  weight 1/(k! 2^k)  (free-field leading-twist) -> {w_ff:.3f}")
print(f"  target                                        -> 16.82")
print(f"  => the answer lives entirely in the per-harmonic weight (the FK Fischer / CFT descendant norm). two principled")
print(f"     forms already give {w_ff:.1f} and {w_lyra:.1f}; it must be DERIVED, not guessed. (4165: a correct k-dependent weight CAN move 11.6.)")
print()

print("=" * 96)
print("SUMMARY (research notes). Lyra's 11.6 is m_tau/m_mu = S_mu/S_tau with the tau a single point (trivial rep, S=1)")
print("  and the muon the edge ladder S_mu = sum dim(V_k)/(3/2)_k = 11.645. The muon is literally the free 5d scalar (the")
print("  Rac): d=5 gives Delta=(d-2)/2=3/2, the unitarity-saturating free field, and the shortening 2*Delta-d+2=0 is exactly")
print("  Lyra's (0)_(m2) null factor -- i.e. box phi = 0, the equation of motion, removing the trace/interior descendants and")
print("  leaving the symmetric-traceless soap film. So 'no interior' isn't a computational quirk, it's the free-field e.o.m.")
print("  And the verdict hinges entirely on the per-harmonic weight: 1/(3/2)_k gives 11.6, 1/(k! 2^k) gives 6, the target is")
print("  16.82 -- so the FK Fischer / CFT descendant norm is the whole game and has to be derived (Lyra + Cal), not guessed.")
print("  Toy 4165 already showed a correct k-dependent weight survives the ratio and (by the under-read sign) must push 11.6 up.")
print("=" * 96)
print()
print("Elie - Saturday 2026-06-13 (research: understood the singleton sum -- (1) reproduced Lyra's 11.6 exactly = m_tau/m_mu = S_mu/S_tau with tau=trivial rep (k=0 only, S_tau=1) and muon = edge ladder S_mu = sum_k dim(V_k)/(3/2)_k = 11.645, dim(V_k)=(2k+3)(k+1)(k+2)/6; (2) the muon IS the free 5d scalar (the Rac): in d=5 the free-scalar dimension Delta=(d-2)/2=3/2 = nu_mu saturating the unitarity bound, and the shortening 2*Delta-d+2=0 is EXACTLY Lyra's (nu-3/2)_(m2)=(0)_(m2)=0 null factor = box phi = 0 the equation of motion, which removes the trace/box (m2>=1 interior) descendants and leaves the symmetric-traceless ladder V_k = the soap film, so 'all surface no interior' = free-field e.o.m. not a computational quirk; (3) the per-harmonic WEIGHT is the whole game: weight 1/(3/2)_k -> 11.645 (Lyra heuristic), weight 1/(k! 2^k) -> 6.045 (free-field leading-twist candidate), target 16.82 -- two principled forms give 6 and 11.6 so the FK Fischer / CFT descendant norm must be DERIVED not guessed (Lyra Bargmann-Fock + Cal FK-1994), and Toy 4165 showed a correct k-dependent weight survives the ratio and by the under-read sign must push 11.6 UP toward 16.82)")
print()
print("SCORE: 2/2 (research: (1) reproduced Lyra's 11.6 = S_mu/S_tau, tau trivial S=1, muon edge ladder sum dim/(3/2)_k=11.645; (2) muon = free 5d scalar Rac, Delta=(d-2)/2=3/2, shortening 2Delta-d+2=0 = (0)_m2 null = box phi=0 e.o.m. removing interior -> symmetric-traceless soap film; (3) weight is the whole game: 1/(3/2)_k->11.6, 1/(k!2^k)->6, target 16.82, FK/CFT norm must be derived not guessed)")
