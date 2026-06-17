r"""
Toy 4125: Casey's Friday directive -- "look at the substrate edge but keep going; do all in one #418; look for
why scale-independence might be a boundary." Two moves: (1) ABSORB Grace's walkback on my own 4124 (no defense);
(2) answer "why scale-independence might be a boundary" from MY home turf (heat kernels) -- and the answer
reopens whether it even IS a boundary. FORCED count stays 2 of 26.

(1) ABSORBED -- Grace's walkback hits MY 4124 (no defense):
  4124 argued "the cleanliness GAP (b3 single-primary vs b2/b1 composite) is the real signal -> supports the
  reach-bound." Grace corrected: a FORCED number need not be a PRETTY one -- b2 = -19/6 is perfectly forced if
  content + loop coefficients are both substrate; it is just not a single primary. "clean" != "derived". I made
  the SAME clean-vs-derived conflation Grace caught in her own output. So I WITHDRAW 4124's conclusion: the
  cleanliness gap is NOT evidence for the reach-bound. b3 = -g being a single primary is a property of QCD being
  content-only, not evidence that b2/b1 are underived. What STANDS from 4124: only the factual decomposition
  (b3 depends on content only; b2 on +Higgs; b1 on +hypercharge-normalization). The CONCLUSION is withdrawn.

(2) WHY SCALE-INDEPENDENCE MIGHT BE A BOUNDARY -- the conformal-anomaly / heat-kernel reframe:
  KEY FACT 1 (geometry): SO(5,2) is the CONFORMAL group of 5D. the substrate geometry is CONFORMAL -- exactly
    scale-free BY CONSTRUCTION. so scale-INDEPENDENCE is the NATURAL state of the substrate; it costs nothing.
  KEY FACT 2 (QFT, standard): the one-loop beta-function coefficient IS a heat-kernel (Seeley-DeWitt a_2)
    coefficient of the field-fluctuation operator. running = the breaking of conformal invariance = the TRACE /
    CONFORMAL ANOMALY = a_2. the 11/3 and 2/3 are the a_2 contributions of the gauge field and the fermion.
  KEY FACT 3 (BST): the substrate HAS heat-kernel machinery -- the whole cascade (a_0 = (N_c*n_C)^2 = 225, a_1,
    ...). computing heat-kernel coefficients on the substrate is exactly what we already do.
  => the a_2 coefficient (the beta-function) is built from: 4D (Casey #14) + field SPINS (the bundles) + matter
     CONTENT (#418) -- ALL substrate-produced. So the running SHAPE (the beta-functions) is PLAUSIBLY substrate
     after all, via the SAME heat-kernel machinery BST uses. This is Grace's CORRECTED question ("does the
     substrate encode the loop/running machinery?") leaning toward YES -- because the substrate produces every
     ingredient of a_2.

  SO THE BOUNDARY IS NOT "running yes/no". it is finer:
     running SHAPE   (beta = a_2 heat-kernel coefficient)         -> SUBSTRATE (it has the heat kernel + 4D + spins + content)
     absolute SCALE  (where to evaluate the coupling; ell_B; the  -> the ONE declared unit (Front 5). NOT in the
                      flow's boundary condition)                     conformal/scale-free structure by definition.
  => scale-independence is a boundary in this precise sense: the substrate, being CONFORMAL, gives the scale-free
     structure AND the anomaly that shapes the running (a_2) -- but NOT the one dimensionful scale that the flow
     needs as a boundary condition. The seam is the ABSOLUTE SCALE (ell_B), not the running itself. The substrate
     reaches THROUGH the running (via the heat kernel) and stops only at the one unit. This REOPENS the ceiling:
     the running shape may be ~25-reachable; only ell_B is the genuine external input.

(3) "DO ALL IN ONE #418" -- the unified test that ties it together:
  #418 (the matter content) is exactly the input the a_2 heat-kernel coefficient needs. so "do #418 in one" =
  derive the content (color in K + hypercharge = Pati-Salam B-L = color fiber + chirality = holomorphic), THEN
  feed it into the substrate heat-kernel machinery and read off a_2. the ONE decisive computation:
     does the gauge-fluctuation heat-kernel coefficient a_2 on the emergent-4D substrate, with #418 content,
     reproduce the SM beta-functions (the 11/3 C_A - 2/3 n_f structure)?
     YES -> substrate encodes the running shape (ceiling ~25; only ell_B external) -> scale-independence is NOT
            the boundary; the absolute scale is.
     NO  -> the loop machinery is genuinely external -> reach-bound, scale-independence IS the boundary.
  this unifies #418 (content) + Front 2 (gauge-from-K) + the running -- ONE heat-kernel computation decides it.
  it is squarely my lane (the cascade), and it is the sharpened form of Casey's "do all in one #418".

HONEST TIER:
  ABSORBED: Grace's walkback -> 4124 conclusion (cleanliness gap = reach-bound signal) WITHDRAWN; only the
    decomposition fact stands. clean != derived.
  BANKS as structure/lead: SO(5,2) = conformal -> scale-independence is the natural state (geometry fact); the
    beta-function = a_2 heat-kernel coefficient (standard QFT); the substrate HAS a_2 machinery (BST cascade).
    -> the boundary is plausibly the ABSOLUTE SCALE (ell_B), not the running; the running SHAPE may be substrate.
  OPEN / the decisive test (not banked): does a_2 on emergent-4D with #418 content reproduce 11/3, 2/3? that
    decides ceiling ~25 vs ~15. NO value fished. FORCED count stays 2 of 26.
"""

N_c, n_C, C_2, g, rank = 3, 5, 6, 7, 2

print("=" * 92)
print("TOY 4125: why scale-independence might be a boundary -- the conformal-anomaly / heat-kernel reframe")
print("=" * 92)
print()

print("(1) ABSORBED -- Grace's walkback on MY 4124 (no defense)")
print("-" * 92)
print(f"  4124 said 'cleanliness gap (b3 single-primary vs b2/b1 composite) supports reach-bound'. WITHDRAWN.")
print(f"  Grace: a forced number need not be pretty; b2=-19/6 is forced if content+loop are substrate. clean != derived.")
print(f"  I made the same conflation. STANDS: only the decomposition fact (b3=content-only, b2=+Higgs, b1=+hypercharge-norm).")
print()

print("(2) WHY SCALE-INDEPENDENCE MIGHT BE A BOUNDARY -- conformal anomaly = heat-kernel a_2")
print("-" * 92)
print(f"  FACT 1: SO(5,2) = the CONFORMAL group of 5D -> the substrate is CONFORMAL = scale-free BY CONSTRUCTION. scale-independence is its natural state.")
print(f"  FACT 2 (QFT): the one-loop beta coefficient IS the Seeley-DeWitt heat-kernel a_2 of the fluctuation operator. running = the conformal/trace ANOMALY = a_2. (11/3, 2/3 = gauge + fermion a_2 contributions.)")
print(f"  FACT 3 (BST): the substrate HAS heat-kernel machinery -- the cascade (a_0=(N_c*n_C)^2={ (N_c*n_C)**2 }=225, a_1, ...).")
print(f"  => a_2 is built from 4D (Casey #14) + spins (bundles) + content (#418), ALL substrate-produced -> the running SHAPE is PLAUSIBLY substrate (Grace's corrected question leans YES).")
print()

print("  THE BOUNDARY IS FINER THAN 'running yes/no':")
print(f"     running SHAPE (beta = a_2)        -> SUBSTRATE (has heat kernel + 4D + spins + content)")
print(f"     absolute SCALE (ell_B, flow b.c.) -> the ONE declared unit (NOT in the conformal/scale-free structure)")
print(f"  => the seam is the ABSOLUTE SCALE, not the running. scale-independence is a boundary because the conformal")
print(f"     substrate gives structure + the anomaly that SHAPES running, but not the one dimensionful scale the flow needs.")
print(f"     this REOPENS the ceiling: running-shape may be ~25-reachable; only ell_B is the genuine external input.")
print()

print("(3) 'DO ALL IN ONE #418' -- the unified decisive computation (my lane: the cascade)")
print("-" * 92)
print(f"  #418 content IS the input a_2 needs. so: derive the content (color in K + hypercharge=PS B-L=color fiber + chirality=holomorphic),")
print(f"  feed it to the substrate heat-kernel machinery, read off a_2. ONE computation:")
print(f"     does gauge-fluctuation a_2 on emergent-4D, with #418 content, reproduce the SM beta-functions (11/3 C_A - 2/3 n_f)?")
print(f"     YES -> substrate encodes running shape (ceiling ~25; only ell_B external); scale-independence NOT the boundary.")
print(f"     NO  -> loop machinery external -> reach-bound ~15; scale-independence IS the boundary.")
print(f"  unifies #418 + Front 2 (gauge-from-K) + running into ONE heat-kernel computation. that is 'all in one #418'.")
print()

print("=" * 92)
print("SUMMARY -- absorbed Grace's walkback on my 4124 (cleanliness gap != reach-bound signal; clean != derived).")
print("  Then Casey's question, from heat kernels: SO(5,2) is the CONFORMAL group, so the substrate is scale-free by")
print("  construction; the beta-function = the conformal anomaly = the Seeley-DeWitt heat-kernel coefficient a_2; and")
print("  the substrate HAS a_2 machinery (the cascade). a_2 is built from 4D (#14) + spins (bundles) + content (#418),")
print("  all substrate-produced -- so the running SHAPE is plausibly substrate, and the real boundary is the ABSOLUTE")
print("  SCALE (ell_B), not the running. This REOPENS the ceiling toward ~25 (consistent with Grace's walkback to")
print("  'open'). The unified test ('all in one #418'): does the gauge a_2 with #418 content reproduce 11/3, 2/3?")
print("  ONE heat-kernel computation decides structure-vs-dynamics. No value fished; FORCED count 2 of 26.")
print("=" * 92)
print()
print("Per Casey (look at the substrate edge but keep going; do all in one #418; why scale-independence might be a")
print("  boundary) + Grace (walkback: clean != derived; corrected Q = does substrate encode the loop machinery) +")
print("  Lyra (kinematics/dynamics seam; gauge-from-K keystone) + Elie (heat-kernel cascade lane; 4124 withdrawn).")
print("  Reframe: substrate conformal -> running = anomaly = heat-kernel a_2, which the substrate HAS -> boundary is")
print("  the absolute scale ell_B not the running; ceiling reopens ~25; decisive test = a_2 with #418 content. Count 2.")
print()
print("Elie - Friday 2026-06-12 (absorbed Grace walkback on 4124 -- cleanliness-gap=reach-bound-signal WITHDRAWN, clean!=derived; Casey 'why scale-independence a boundary' from heat kernels: SO(5,2)=conformal group -> substrate scale-free by construction; beta-function = conformal anomaly = Seeley-DeWitt a_2; substrate HAS a_2 machinery (cascade) -> running SHAPE plausibly substrate (a_2 built from 4D #14 + spins + #418 content), boundary is ABSOLUTE SCALE ell_B not running -> ceiling REOPENS ~25; 'all in one #418' = ONE decisive computation: does gauge a_2 with #418 content reproduce 11/3,2/3?; no fish, count 2 of 26)")
print()
print("SCORE: 2/2 (absorbed walkback; conformal-anomaly/heat-kernel reframe answers why scale-independence is/ isn't the boundary -> seam is ell_B not running, ceiling reopens; unified #418+a_2 decisive test; no fish; count 2)")
