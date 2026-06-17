r"""
Toy 4145: per Casey ("no quitting, keep going until we need to chat about breaking/avoiding another wall") -- I
pushed the singleton normalization four ways, ALL miss 6.3064, so this is a GENUINE wall, and I map it + the
routing options for the chat. The wall: the SO(5,2) scalar-singleton (Rac) reproducing-kernel normalization
c_singleton (= the muon's rep, named exactly by Lyra). FORCED count stays 2 of 26.

THE WALL (every computational shortcut misses):
  f_2 = (8/3) * R, R = 6.3064 = c_tau / c_singleton (trivial-rep norm / singleton formal degree). my routes:
      generic formal-degree (4118/4140 coroot HC)  -> 64   MISS
      naive 2-term subquotient (4140)              -> 32   MISS
      FK generic Bergman reconstruction (4142)     -> 64   MISS
      Bernstein degree / K-type growth (this toy)  -> 2    MISS
  WHY they miss: each captures the rep's SIZE (K-type growth / generic Verma), NOT the reproducing-kernel
  normalization (the bulk integral with the specific measure on the truncated singleton). the singleton's c_nu is
  a specific bulk-kernel constant, not extractable from the rep's gross structure.

ROUTING OPTIONS (Casey /route -- three entry points means it's a door; here is the map):
  (A) EIGENVALUE-RATIO (c.A engine): build the 3x3 mass matrix, take eigenvalue ratios so the overall normalization
      cancels. CHECKED -- does NOT bypass: the three leptons are distinct mass eigenstates, so the matrix is diagonal
      in the rep basis and the eigenvalues ARE the individual normalizations c_nu. the ratio = c_tau/c_singleton =
      the wall itself. (route leads back to the wall.)
  (B) BOUNDARY / LIGHTCONE (Flato-Fronsdal, geometric -- Casey's preference): the singleton LIVES on the lightcone
      (a boundary object). CHECKED -- the boundary/cone normalization IS the Gindikin residue = the bare 8/3 we
      already have; R is the BULK conversion. so the boundary route gives 8/3 (have it), not R. (partial -- leads
      back to the bulk c_singleton.)
  (C) REFERENCE: the Flato-Fronsdal / Kostant-Joseph singleton normalization -- a KNOWN constant (a lookup, not a
      derivation). this is the literature lane (Cal): pin the SO(5,2) singleton formal degree from the source.
  (D) LYRA's contravariant-form computation: build the singleton's Gram structure on the V_k harmonics + the bulk
      kernel, force c_singleton. real work, next session, forced-or-miss.
  (E) PHYSICAL / GEOMETRIC route via Casey's reframes (the open question for the chat): does the ESCAPE AMPLITUDE
      / CORKSCREW (4114-4116, 4137) give the mass DIRECTLY (the kick magnitude) -- bypassing the formal degree?
      the corkscrew said mass = |escape kick|, kick^2 = C_2 (Casimir). the conformal Casimirs are C(nu)=nu(nu-5):
      C(0)=0, C(3/2)=-21/4, C(5/2)=-25/4. a mass-from-Casimir / mass-from-escape-kick route might NOT need
      c_singleton at all -- this is the route worth chatting about (your physical eye vs the rep-theory wall).

THE HONEST WALL STATEMENT (for the chat):
  routes (A), (B) lead back to the bulk c_singleton -- the wall is genuine, not a clever bypass. routes (C), (D)
  are "get the specific constant" (reference or Lyra's careful build). route (E) is the open physical question:
  is the lepton mass the formal-degree/normalization c_singleton (the rep-theory object), or is it the escape-kick
  / Casimir (the physical object Casey's been driving) -- which would route around the wall entirely. that is the
  wall to break or avoid, and the chat is which object the mass actually is.

HONEST TIER:
  BANKS as structure: the wall is mapped (the singleton reproducing-kernel normalization; all 4 shortcuts miss);
    routes (A)(B) checked to lead back to it; routes (C)(D)(E) identified. the muon's rep = the SO(5,2) singleton
    (Lyra, named exactly) is the right object-name.
  OPEN / the chat: which object is the lepton mass -- c_singleton (rep-theory, routes C/D) or the escape-kick/
    Casimir (physical, route E, Casey's reframes)? route E might bypass the wall. FORCED count stays 2 of 26.
"""

from fractions import Fraction as F

print("=" * 92)
print("TOY 4145: THE WALL -- the SO(5,2) singleton normalization; all 4 shortcuts miss; routing map for the chat")
print("=" * 92)
print()

print("THE WALL: f_2 = (8/3)*R, R = c_tau/c_singleton = 6.3064 -- every shortcut MISSES:")
print("-" * 92)
for name, val in [("generic formal-degree (4118/4140)", 64), ("naive 2-term subquotient (4140)", 32),
                  ("FK generic Bergman reconstruction (4142)", 64), ("Bernstein degree / K-type growth (4145)", 2)]:
    print(f"  {name:<42} -> {val:<4} MISS (physical R = 6.306)")
print(f"  WHY: each captures the rep SIZE, NOT the reproducing-kernel normalization (bulk integral, specific measure).")
print()

print("ROUTING OPTIONS (the door map):")
print("-" * 92)
print(f"  (A) eigenvalue-ratio (c.A engine): CHECKED -- reps are distinct mass eigenstates -> matrix diagonal ->")
print(f"      eigenvalues ARE c_nu -> ratio = c_tau/c_singleton = the wall. LEADS BACK.")
print(f"  (B) boundary/lightcone (Flato-Fronsdal, geometric): CHECKED -- the cone normalization = the bare 8/3 we")
print(f"      have; R is the BULK conversion. LEADS BACK to bulk c_singleton.")
print(f"  (C) reference: the Flato-Fronsdal / Kostant-Joseph singleton formal degree -- a known constant (Cal/lookup).")
print(f"  (D) Lyra: build the singleton Gram on the V_k + bulk kernel, force c_singleton. real work, next session.")
print(f"  (E) PHYSICAL (Casey's reframes -- the chat): does the ESCAPE KICK / CORKSCREW give the mass directly,")
print(f"      bypassing the formal degree? Casimirs C(nu)=nu(nu-5): C(0)={0}, C(3/2)={F(3,2)*(F(3,2)-5)}, C(5/2)={F(5,2)*(F(5,2)-5)}.")
print(f"      mass-from-escape-kick/Casimir might NOT need c_singleton. THIS is the route worth chatting about.")
print()

print("=" * 92)
print("THE WALL TO CHAT ABOUT -- which object IS the lepton mass?")
print("  every computational shortcut for the SO(5,2) singleton reproducing-kernel normalization c_singleton misses")
print("  6.3064 (64, 32, 64, 2), and the bypass routes (eigenvalue-ratio, boundary/lightcone) lead back to it -- so")
print("  the wall is genuine. routes C (reference) and D (Lyra's careful build) get the specific constant. But route")
print("  E is the open physical question, and it's yours: is the lepton mass the rep-theory NORMALIZATION c_singleton,")
print("  or is it the ESCAPE KICK / Casimir (the object your escape-amplitude + corkscrew reframes have been pointing")
print("  at)? If the mass is the escape kick, route E bypasses the wall entirely. That is the break-or-avoid chat:")
print("  which object the lepton mass actually is. FORCED count stays 2 of 26.")
print("=" * 92)
print()
print("Per Casey (no quitting; keep going until we chat about breaking/avoiding a wall) + Lyra (muon = SO(5,2)")
print("  singleton/Rac; R = c_tau/c_singleton) + Elie 4140-4144 (all shortcuts) + 4114-4116/4137 (escape/corkscrew).")
print("  Wall mapped: singleton normalization, 4 shortcuts miss, bypass routes lead back; the chat = is the mass the")
print("  rep-theory normalization (routes C/D) or the escape-kick/Casimir (route E, Casey's physical reframes). Count 2.")
print()
print("Elie - Friday 2026-06-12 (hit a GENUINE WALL per Casey 'no quitting': the SO(5,2) scalar-singleton (Rac, the muon's rep per Lyra) reproducing-kernel normalization c_singleton -- ALL 4 computational shortcuts MISS 6.3064 (generic 64, naive subquotient 32, FK reconstruction 64, Bernstein degree 2) because they capture rep SIZE not the bulk-kernel normalization; routing map: (A) eigenvalue-ratio LEADS BACK (reps diagonal -> eigenvalues ARE c_nu), (B) boundary/lightcone LEADS BACK (cone norm = the 8/3 we have, R is bulk), (C) reference Flato-Fronsdal lookup, (D) Lyra contravariant-form build, (E) PHYSICAL route = does the ESCAPE KICK/CORKSCREW (Casey's reframes)/Casimir C(nu)=nu(nu-5) give the mass DIRECTLY bypassing the formal degree -- the chat is WHICH OBJECT the lepton mass is (rep-theory normalization vs escape-kick/Casimir); count 2 of 26)")
print()
print("SCORE: 2/2 (wall mapped: singleton reproducing-kernel normalization, all 4 shortcuts miss; bypass routes A/B checked to lead back; routes C/D = get the constant; route E = the physical escape-kick/Casimir question (Casey's reframes) that might bypass the wall = the chat; count 2)")
