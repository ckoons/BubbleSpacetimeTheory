# L4 — Casey's parity form of the write-count idea, one page
**Lyra, Sunday 2026-09-06, 11:37 EDT. Round 120 L4. Toy 5702 (`play/.out_5702.txt`) is the control, run to 9.06 × 10⁸.**

## 1. The statement (classical, cited)
Let Ω(n) be the number of prime factors of n counted with multiplicity and λ(n) = (−1)^{Ω(n)} the Liouville function; L(x) = Σ_{n ≤ x} λ(n). Then
  Σ_{n ≥ 1} λ(n) n^{−s} = ζ(2s)/ζ(s)   (Re s > 1),
and **RH ⟺ L(x) = O(x^{½+ε}) for every ε > 0** (Landau 1899; Titchmarsh, *The Theory of the Riemann Zeta-Function*, §14.25). Proof sketch, both directions: if L(x) ≪ x^{½+ε} then partial summation continues ζ(2s)/ζ(s) holomorphically to Re s > ½, so ζ has no zero there, and the functional equation gives RH; conversely under RH, Perron's formula with the standard bounds for 1/ζ on Re s ≥ ½ + ε gives the estimate. The Möbius twin M(x) = Σ μ(n) has the same equivalence (Littlewood 1912); λ is the version that counts EVERY prime factor, which is what "one prime = one write" needs.

## 2. Casey's reading (Identified tier, stated as such)
- **One prime = one write.** In K1860's dictionary a write is a coordinate multiplication on the Hardy/record space; multiplying by p is one write. The degree of n as a written word is the number of writes, **deg(n) = Ω(n)**, additive over the multiplicative structure: Ω(mn) = Ω(m) + Ω(n). This is the grading; nothing else is needed from D_IV⁵ for the statement.
- **The parity grading (re-worded 16:1x per K1867 D2 / Cal §857 catch 2).** Reduce the degree mod 2: the parity of the write count is λ(n) = (−1)^{Ω(n)}, a completely multiplicative character of the semigroup of writes. On the Hardy space of Š this is the **m mod 2 grading** of the Hua modes e^{imθ}Y_k (m ≡ k mod 2 on L²(Š)), an abstract grading and nothing more: there is NO line-bundle twist separating odd from even write counts — every Hua mode, odd m included, is an honest function on Š, and the "twisted sections" are the m ≢ k modes, which are not in L²(Š) at all. The earlier phrase "the Z₂ fold of Š" is withdrawn: L2 shows the Z₂ of (S⁴ × S¹)/Z₂ is a rotation by π on the time circle, central, and no map from writes to Shilov directions exists in the corpus (the six-vector obstruction, K1862 addendum). The identification "m mod 2 grading = Liouville" is therefore **Identified**: the parity of the write count is Liouville by definition; its equality with anything geometric in D_IV⁵ is an open map, not a derived one.
- **RH as a statement about the fold.** RH says the running parity of the writes, summed over all words up to length x, cancels to square-root size: the writes are as balanced as a random ±1 sequence would be, and no better. This is direction-blind and dimension-blind (it needs no placement of primes in D_IV⁵), which is why it survives the obstruction that killed the placement map; what it does not do is supply a mechanism, because everything above is a restatement of RH.

## 3. The control (toy 5702), as any toy on this row must pass it
Pólya (1919) conjectured L(x) ≤ 0 for all x ≥ 2. Haselgrove (1958) proved the conjecture false without exhibiting x; Lehman (1960) found L(906,180,359) = 1; the SMALLEST counterexample is x = 906,150,257 (Tanaka 1980). Any instrument on this row must reproduce, from a sieve and not from memory:
| quantity | toy 5702 |
|---|---|
| first x ≥ 2 with L(x) > 0 | **906,150,257** |
| L(906,150,257) | **+1** |
| L(906,180,359) (Lehman's) | +1 |
| L(x) ≤ 0 on [2, 906,150,256] | HIT |
| min L on [2, 9.06×10⁸] | −29,736 at x = 712,638,284 |
| min L(x)/√x | −1.358 |
| L(10⁶), L(10⁷), L(10⁸) | −530, −842, −3,884 |
The min of L(x)/√x at −1.36 is the visible content of "O(x^{½+ε})" at this range: the fold is square-root balanced, with a negative bias that Pólya mistook for a law. (The prompt's attribution "Haselgrove's 906,150,257" should read Tanaka 1980 for the number; Haselgrove is the existence proof. Pinned from the literature as I remember it; to be checked against the primaries before any external copy.)

## 4. What is derived, what is identified, what is not
- **DERIVED (classical):** RH ⟺ L(x) = O(x^{½+ε}); Σ λ(n)n^{−s} = ζ(2s)/ζ(s).
- **IDENTIFIED (BST reading):** deg = Ω, the m mod 2 grading = λ. Honest and content-free until a map from writes to the geometry is exhibited.
- **NOT available:** any mechanism forcing the cancellation. The barrier lemma applies verbatim: the Epstein zeta ζ_{ℤ⁵} has a "parity" too (its coefficients r₅(N) admit a Z₂-graded refinement) and no Euler product, and its partial sums do not obey the square-root law at the critical line of its own strip; whatever proves RH through L(x) must use that λ is completely multiplicative, which is the Euler product of ζ(2s)/ζ(s) restated.
— Lyra
