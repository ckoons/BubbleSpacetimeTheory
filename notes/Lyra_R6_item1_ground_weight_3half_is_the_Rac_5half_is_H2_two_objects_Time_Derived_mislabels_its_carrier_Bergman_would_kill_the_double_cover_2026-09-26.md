# Lyra R6 item 1: the ground weight. 3/2 belongs to the Rac, 5/2 to H². Two objects; Time, Derived mislabels its carrier.

**Lyra, Saturday 2026-09-26, 11:40 EDT (from `date`).** Cal pre-registered this at 3b13cbb9 (`Cal_S991_prereg_…`). **I have seen only its commit subject, not the file.** This item was written without reading it.
**didwe** "ground weight minimal representation" → 0.
**Instrument:** `play/toy_5807_lyra_R6_item1_…K_characters.py`, sha256 `0ac3218b9ae43aaf…`, hashed before the run. **SCORE 7/7**, output `play/.out_toy_5807.txt`. The checks are K-characters, exact to J-weight 40.

**Kill line (written first):** if the J-spectrum of H²(D_IV⁵) contains 3/2, Time, Derived is right as written and there is no tension. Otherwise the 3/2 sits on a different module, and the paper must name which one.

**Invariant, quoted before any number:** the eigenvalue of J, the elliptic element of span{P₀, K₀, D}, which is the centre of K. On a scalar module H_ν(D_IV⁵), the K-types are (harmonic degree a) × q^b, with J-weight ν + a + 2b. At the Wallach point ν = (n − 2)/2, only b = 0 survives.

**Paragraph (for Cal's comparison against the pre-hash):**
- **Two objects, both correct.** 3/2 is the ground J-weight of the **minimal representation (Rac, the Wallach point ν = 3/2)**. 5/2 is the ground J-weight of **H²(D_IV⁵) (the Hardy point ν = n_C/2)** (Q1).
- **Time, Derived v1.3 mislabels its carrier.** Line 26 puts "J on H²(D_IV⁵)" and gives it "ground weight E₀ = 3/2 … the U(1) energy of the minimal representation". On H², the ground weight is **5/2**. Line 19 also calls H² "the Bergman space", which is a second mislabel. It is load-bearing. The Bergman module (ν = genus = 5) has **integer** J-weights, so exp(2πiJ) = +1 there and the paper's double cover would fail on it (Q3, the control).
- **What each of the paper's results rests on:**
  - **The arrow** (spec J bounded below by a positive number) holds on both. Unaffected.
  - **The double cover** (exp(2πiJ) = −1) holds on all of H², and more strongly than the paper says: every K-type of H² lies in the single coset 5/2 + ℤ≥0 (Q2, Cal Section 990). Unaffected.
  - **The parity law** E = (3/2)·#Rac + 2·#Di + n is a statement about the multi-singleton (Flato–Fronsdal) Fock space, not about H². It is unaffected once it is said to live there.
- **The bridge is at the K-level, not the SO(4,2)-level.** Theorem B (09-14): **char H² = Σ_{b≥0} char Rac · t^{1+2b}** (Q4). The ground weight 5/2 = 3/2 + 1: the Rac weight plus one unit of the odd clock. So every state of H² has **#Rac = 1**, which puts it in the odd sector and on the 4π cover. That is Time, Derived's own parity law, applied to H².
- **K1927(c) is true but is not the bridge.** Rac|SO(4,2) = H_{3/2}(D_IV⁴) ⊕ H_{5/2}(D_IV⁴) (Q5), and H²|SO(4,2) = ⊕_k H_{5/2+k}(D_IV⁴) (Q6). They share exactly one summand, H_{5/2}(D_IV⁴) (Q7). But there is **no SO(5,2)-map Rac → H²**: both are irreducible and their lowest J-weights differ (Schur). The shared 4D summand says that a 4D observer cannot distinguish Rac's normal-derivative sector (k = 1) from H²'s k = 0 sector. It is a coincidence after descent, not a map before it.

**The fix, one line each (for Keeper's gate; this is an edit to a GO'd paper and needs Casey's word):**
- TD v1.3 line 19: "the Bergman space" → **"the Hardy space (the unitary highest-weight module at ν = n_C/2 = 5/2)"**.
- TD v1.3 line 26: → **"… with a half-integer spectrum. Its ground weight on H² is 5/2 = 3/2 + 1: the minimal representation's (Rac's) 3/2 plus one unit of the odd clock (Theorem B). The singleton weights {3/2, 2} generate the multi-singleton Fock space, where the parity law of Sections 5 and 7 lives."**

**Other corpus sites carrying E₀ = 3/2 (grep, to be checked by their owners; none has been edited by me):** BOOKDAY_LEDGER_item2 (mine, 08-24); the Time paper outline (mine, 08-17); Cal's Majorana referee note (07-15); K1687; K956; board round 143. Each needs one question answered: does it attach 3/2 to H², or to the Rac?

**Consequence for round 6:** any energy statement from here on quotes the ground weight as **5/2 on H²** (the interior clock), or **3/2 on the Rac** (the singleton), and names the module every time.
