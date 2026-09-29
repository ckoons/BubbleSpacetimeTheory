# Elie — round 22 (C) PREREG, toy 5848: W on three vertices, fermion-parity control — 2026-09-29 12:14 EDT, before any code
Antecedents verbatim: Cal S1019 (K1942): "W is a field-sign ℤ₂ of the action: −1 on every field whose clock and spin covers disagree … Cal's refinement: the constraint is two ℤ₂'s, the clock character and fermion parity, each conserved on its own, with W their product." K1942 (C): "E1: H²·Rac·φ keeps W and breaks P; E2: H²·Di is forbidden; E3: H²·Di·ψ is allowed; control: fermion parity conserved throughout."
Groups and sources (stated before use): 5D singletons of SO(5,2) restricted to SO(4)×SO(2): H² (λ = 5/2), Rac₅ (λ = 3/2), Di₅ (spinor singleton, λ = 2; pin owed), from 5846's characters. 4D matched fields from 5834: φ = the massless scalar ladder (Δ = 1), ψ = the Weyl ladder (Δ = 3/2). Signs (z_t, z_s) read weight by weight; a vertex is ALLOWED iff the full tensor-product character contains (z_t, z_s) = (+1, +1) on every weight, i.e. BOTH ℤ₂'s are neutral.
DIRECTION (computed before any run, from 5846's classes: H² (−,+), Rac₅ (−,+), Di₅ (+,−), φ (+,+), ψ (−,−)):
- E1 H²·Rac·φ: (+,+) ⇒ ALLOWED; W = +1 conserved; P = (−1)^{#H²} = −1 ⇒ P broken. [W, not P]
- E2 H²·Di: (−,−) ⇒ FORBIDDEN, by the clock AND by fermion parity. But W(H²·Di) = (−1)(−1) = +1: **W alone would ALLOW it.** So E2 is forbidden by Cal's two ℤ₂'s, not by W. W is necessary, not sufficient.
- E3 H²·Di·ψ: (+,+) ⇒ ALLOWED; W = +1; fermion number even (Di, ψ).
- CONTROL: in every allowed vertex, z_s = +1 (fermion parity conserved), and a single fermion vertex (e.g. Di·φ·φ) is forbidden.
KILL (for K1942's E-list as worded): E2 allowed by the full two-ℤ₂ constraint. SECONDARY (for 'W alone suffices'): expected to FAIL on E2, stated in advance.
