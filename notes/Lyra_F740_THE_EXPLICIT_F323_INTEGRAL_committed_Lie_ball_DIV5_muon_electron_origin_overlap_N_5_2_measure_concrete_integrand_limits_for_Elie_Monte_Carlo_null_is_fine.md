# F740 — THE EXPLICIT F323 INTEGRAL, committed. No more "I'll fire it when X is pinned" — here is the actual integral, concrete domain, concrete integrand, concrete measure, ready for Elie to Monte-Carlo to a NUMBER today. **A null is fine and expected-acceptable: the muon is Derived via e=n (K986) regardless; this integral decides only the c-function/overlap SECOND route and whether the unified lepton engine advances or gets parked.** I am committing to definite choices (the F323-stated form, exactly as written 2026-06-25 — N(w)^{n_C/2} origin-overlap on the Lie ball) rather than hedging for a 35th day. If a choice is wrong, the number is a null and we park the engine — that is the answer, not a failure. **I am NOT tuning anything to 24/π² = 2.43172; the integrand is F323's exhibited object, and Cal audits that.**

**Lyra, Wed 2026-07-29 18:08 EDT. Settling it. The explicit integral, committed, handed to Elie. Null acceptable. No tuning.**

## The domain (Lie ball, Cartan type IV, ℂ⁵) — concrete
$$ D_{IV}^5 = \{\, w \in \mathbb{C}^5 : |w\!\cdot\!w|^2 - 2|w|^2 + 1 > 0 \ \text{and}\ |w|^2 < 1 \,\}, $$
where $w\!\cdot\!w = \sum_{i=1}^5 w_i^2$ (complex bilinear) and $|w|^2 = \sum_{i=1}^5 |w_i|^2$. The **generic norm on the diagonal**:
$$ N(w) = 1 - 2|w|^2 + |w\!\cdot\!w|^2 \quad (>0 \text{ on } D,\ \to 0 \text{ at the Shilov boundary}). $$

## The modes (boundary-Dirac spinor, K945 highest-weight polynomial part) — concrete
$$ p_k(w) = (w_1 + i\,w_2)^k, \qquad k = 0,1,2 \ \text{for}\ e,\mu,\tau $$
(the k-independent spinor factor $u_0$ and the $(7/2)_{1/2}$ Pochhammer cancel in ratios, F323 — so the k-dependence is entirely $p_k$).

## The localization-overlap amplitude (F323's N^{n_C/2} origin-overlap) — concrete
The origin-localized ("electron-at-origin") measurement state trivializes the kernel cross-term (F323, June 9), so the overlap amplitude of mode k is
$$ \boxed{\,A_k = \int_{D_{IV}^5} \big|p_k(w)\big|^2\, N(w)^{n_C/2}\; dV(w) = \int_{D_{IV}^5} |w_1 + i w_2|^{2k}\, N(w)^{5/2}\; dV(w)\,} $$
with $dV$ = Lebesgue measure on $\mathbb{C}^5 = \mathbb{R}^{10}$, $n_C/2 = 5/2$ (the half-integer because $n_C=5$ is odd — the genuine √ where π enters from the measure, F323).

## The number to report — concrete
The μ/e localization-overlap ratio (normalized — divide by the ground amplitude):
$$ R_{\mu/e} = \frac{A_1}{A_0} = \frac{\displaystyle\int_{D} |w_1+iw_2|^{2}\,N(w)^{5/2}\,dV}{\displaystyle\int_{D} N(w)^{5/2}\,dV}, \qquad R_{\tau/e}=\frac{A_2}{A_0}. $$
**Compare $R_{\mu/e}$ to $24/\pi^2 = 2.43172$** (and $m_\mu/m_e$ prediction $= R_{\mu/e}^{\,6}$ vs observed 206.77; the exponent 6 = dim SO(4), F111, is banked separately). **Report the raw number** — pass (≈2.43) → engine advances; null (≠2.43, or the naive normalization is off) → park the engine.

## Explicit Monte-Carlo recipe (Elie, today)
1. Sample $w \in \mathbb{C}^5$: draw 10 reals, e.g. uniform in the box $|w_i|<1$ (or importance-sample the ball $|w|<1$); **accept** if $|w|^2<1$ AND $N(w)=1-2|w|^2+|w\!\cdot\!w|^2>0$ (inside $D$).
2. For accepted $w$, accumulate $|w_1+iw_2|^{2k}\,N(w)^{5/2}$ for $k=0,1,2$.
3. $A_k$ = the Monte-Carlo mean; report $R_{\mu/e}=A_1/A_0$, $R_{\tau/e}=A_2/A_0$, with error bars. A rough number (few % MC error) beats no number.
4. **Do NOT adjust the integrand to hit 2.43** — report what the F323 form gives.

## The two outcomes, both fine (Casey's frame)
- **$R_{\mu/e} \approx 2.43$:** the lepton overlap engine WORKS — the muon gains a second (overlap/c-function) route beyond e=n; push the full 3×3 lepton Gram matrix → PMNS (on θ₂₃ = 4/7, F739).
- **$R_{\mu/e} \neq 2.43$ (or the naive normalization misses):** the unified overlap engine is honestly **CLOSED/parked**. The muon still stands on e=n (Derived, K986); the fermion sector is banked as-is (11/12 at Derived, piecemeal); the two-tier principle (quarks = degree-Jack, leptons = cross-address overlap) is itself a real finding. **This is the null Casey named — and it settles it, which is the win.**

## Handoffs
- **@Elie** — evaluate $A_k$ by Monte Carlo on the Lie ball TODAY (analytic if you can; the integrand is elementary — a power of $|w_1+iw_2|^2$ times $N(w)^{5/2}$ over the ball). Report $R_{\mu/e}=A_1/A_0$ (and $R_{\tau/e}$) vs 2.43172. **A null is an acceptable, valuable output.** No tuning.
- **@Cal** — audit target-innocence: the integrand is F323's exhibited object (Lie-ball domain, $p_k=(w_1+iw_2)^k$, $N^{5/2}$ measure) — NOT reverse-engineered from 24/π². Check Elie's MC (domain acceptance $N>0$; convergence).
- **@Keeper** — you rule the number the moment it lands: pass → engine advances (muon 2nd route); null → park the engine, bank the fermion sector as the complete piecemeal result, flip the frame (the sector is done; the unified engine is a parked research arc; the two-tier split is the finding). Either way settled.
- **@Grace** — ledger unchanged: muon Derived via e=n (K986) regardless; this number decides only the c-function/overlap second route.
- **@Casey** — done stalling: here is the actual integral, not a description of one. It's over the Lie ball in five complex dimensions, the muon's mode is $(w_1+iw_2)$, the electron's is the constant, and the weight is the domain's own volume factor $N(w)^{5/2}$ — the 5/2 being where the π gets in, because 5 is odd so it's a real square root. Elie can throw a few million random points at it this afternoon and read off whether the muon/electron overlap comes out near 2.43 (which is 24/π²) or not. And I've made my peace with the null: if it misses, the muon is still Derived on the other argument, the fermion sector is still 11-of-12 done, and we've simply learned the one unified engine isn't the road — which is a settled answer after 34 days of "almost." I did not tune a single thing toward 2.43; it's the June integral, written out, handed over. Let's get the number.

Notes only; no toy/theorem claimed (Elie owns the numeric). F740: THE EXPLICIT F323 INTEGRAL, committed. Domain = Lie ball D_IV⁵ = {w∈ℂ⁵: N(w)=1−2|w|²+|w·w|²>0, |w|²<1}. Modes p_k(w)=(w₁+iw₂)^k, k=0,1,2=e,μ,τ. Amplitude A_k=∫_D |w₁+iw₂|^{2k} N(w)^{5/2} dV (Lebesgue on ℝ¹⁰). Report R_{μ/e}=A_1/A_0 vs 24/π²=2.43172 (m_μ/m_e=R^6). MC recipe: sample ℂ⁵, accept if |w|<1 & N>0, average |w₁+iw₂|^{2k}N^{5/2}. NULL ACCEPTABLE (muon Derived via e=n K986 regardless; decides only c-function 2nd route). NO tuning (Cal audits). Pass→push lepton Gram→PMNS(θ₂₃=4/7); null→park engine, bank sector as-is. @Elie MC today, report number. — Lyra