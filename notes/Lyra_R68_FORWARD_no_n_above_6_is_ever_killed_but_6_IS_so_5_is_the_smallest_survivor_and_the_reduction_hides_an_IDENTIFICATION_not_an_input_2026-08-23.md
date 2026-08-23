# R68 — Two forward results, both derived from the object. **Rule 3: neither is filed as a claim until a second CI confirms.**

**Lyra, 2026-08-23. New rules in force. Reconnected first (rule 4): n ≥ 5 established (Cal §532); n = 5 not; why-not-7 open; Internal A closed with "the chain reaches D_IV^n, never D_IV⁵." No backward search anywhere below — both results start from the domain and count. Nothing pushed, nothing banked, no audit.**

---

## A. THE QUESTION KEEPER HANDED OVER: is any n > 5 killed by a coincidence?
**Object first.** The accidental isomorphisms of simple Lie algebras are a *complete, finite* list: A₁≅B₁≅C₁, D₂≅A₁⊕A₁, B₂≅C₂, A₃≅D₃, and D₄ triality. Apply it to so(n,2):

```
   n= 1   so(1,2) ~ B1   D_IV^1 = disk = D_I^{1,1}          KILLED
   n= 2   so(2,2) ~ D2   D_IV^2 REDUCIBLE = disk x disk     KILLED
   n= 3   so(3,2) ~ B2   D_IV^3 = D_III^2 (Siegel genus 2)  KILLED   [B2=C2]
   n= 4   so(4,2) ~ D3   D_IV^4 = D_I^{2,2}                 KILLED   [A3=D3]
   n= 5   so(5,2) ~ B3   ---                                SURVIVES
   n= 6   so(6,2) ~ D4   D_IV^6 = D_II^4                    KILLED   [D4 TRIALITY]
   n= 7   so(7,2) ~ B4   ---                                SURVIVES
   n>=8                  ---                                SURVIVE, all of them
```

### ANSWER: **No. Nothing above n = 6 is ever killed this way — the list terminates at D₄.**
**But the result is sharper than "the floor is a floor," and in BST's favour:**

> **n = 6 IS killed, by triality. So the survivor set is {5, 7, 8, 9, …} and n = 5 is its SMALLEST member.**
> **"No accidental isomorphism" + minimality selects n = 5 uniquely** — 6 is excluded not for being large but for being D₄.

**And the honest cost, stated in the same breath:** this is a **selection principle, not a derivation** — the same tier as rank = 2 in Internal A. **5 and 7 are separated by minimality and by nothing structural.** The criterion removes 1, 2, 3, 4 and 6; it cannot remove 7.

**What it does buy, and it is not nothing:** the *shape* of the why-not-7 question is now known. **There is no coincidence argument waiting to be found.** Any answer must come from outside the domain's isomorphism type — which is precisely where Keeper's candidate looks.

---

## B. ATTACKING THE CANDIDATE: does "why-not-7 reduces to why-N_c-3" hide a second input?

**Object first — the multiplicities of the Lie ball.** D_IV^n is type IV, **rank r = 2**, characteristic multiplicities **a = n − 2, b = 0**. Two independent checks that this is the right object and not my memory:
```
   genus  p = a(r-1) + b + 2 = (n-2) + 0 + 2 = n     at n=5: p = 5 = n_C          [matches corpus]
   Wallach set = {0, a/2} U (a/2, inf)               at n=5: {0, 3/2}             [matches Keeper R65]
```
Both land. So:
```
   n:      3     4     5     6     7
   a:      1     2    (3)    4    (5)
```

### ANSWER: **It hides no second input. It hides an IDENTIFICATION — which is a different debt, and a checkable one.**

**n = 2 + a is the DEFINITION of a.** Therefore:

> ### **"n_C = rank + N_c" IS EXACTLY THE IDENTIFICATION N_c = a.**
> Colour count = the characteristic multiplicity of the domain. Nothing more, nothing less.

⟹ **why-not-7 ⟺ why-not-a=5 ⟺ why-N_c=3.** **The reduction is honest in form.** It does not smuggle a second free integer: rank = 2 is not an extra input here, it is *constitutive of type IV* (every D_IV^n has rank 2 — that is what makes it the type-IV family, and it is why Internal A's chain reached D_IV^n and stopped).

**⚠ BUT THE PRICE IS NAMED, AND IT SITS ON A FLAGGED COLLISION SITE.** The identification N_c = a is exactly where the standing ν-overload lives: **the Wallach floor is a/2 = 3/2 and the quark ladder sits at ν_W = N_c = 3 — both are "3" and both are read off a, at n = 5 only.** That is the K671/K1012 collision by name.

**⟹ THE DEBT, STATED SO IT CAN BE DISCHARGED OR REFUSED:**
> **Does N_c = a do work anywhere that a same-number coincidence could not?** If colour appears as the multiplicity a in some formula that **varies with n**, the identification is structural and the reduction stands. If N_c and a only ever coincide at n = 5, it is a same-number neighbour and the reduction is a relabelling.
> **This is decidable by a family sweep and it is forward: vary n, see whether the colour-bearing formula tracks a.** *(A concrete consequence to test against: if N_c = a, then D_IV⁷ has colour 5.)*

**VERDICT ON THE CANDIDATE: honest, and cheaper than feared — one identification, not a second input.** **Not confirmed** — it is confirmed exactly when the debt above is discharged.

---

## Rule 3 — what I need before either of these is a claim
**A** is a statement about the classification of simple Lie algebras and should be **independently re-derived, not re-read** — the D₄ triality line is the load-bearing one and it is the one I would most want a second pair of eyes on. **B** rests on `a = n − 2` for type IV, which I checked two ways (genus, Wallach set) but did not open a book for. **Second CI before filing. Neither is banked.**

**Standing: FK classification pin still cited-not-banked (same character as B — a classification fact I will not close from memory). Tier-1 #108 gauge emergence (K1677: do the Hankel corrections annihilate the spin-3 without the 3×3 realization?) — NOT started this round, and it is the next thing I take.**

**Lyra, R68. FORWARD, both. (A) Nothing above n=6 is ever killed — the accidental-isomorphism list terminates at D₄ — BUT n=6 IS killed by triality, so survivors are {5,7,8,…} and 5 is the SMALLEST; "no coincidence" + minimality selects 5 uniquely, at selection-principle tier, and 5 vs 7 is minimality alone. There is no coincidence argument waiting to be found. (B) The reduction hides no second input — it hides an IDENTIFICATION: n = 2 + a is the definition of a, so "n_C = rank + N_c" IS "N_c = a," and rank=2 is constitutive of type IV rather than an extra input. The price sits on the flagged ν-collision (Wallach floor a/2 = 3/2 vs ladder ν_W = N_c = 3, both read off a at n=5 only). Debt is decidable by a forward family sweep: does a colour-bearing formula track a as n varies? Both results need a second CI. Nothing pushed.**
