---
title: "T1093: Foundations-Signal Bridge — Shannon IS AC"
author: "Casey Koons & Claude 4.6 (Lyra)"
date: "April 11, 2026"
theorem: "T1093"
ac_classification: "(C=1, D=0)"
status: "Proved — structural identification"
origin: "Z3: foundations↔signal had zero edges despite 126 combined theorems"
parents: "T7 (Shannon Bridge), T421 (Depth-1 Ceiling), T663 (Three AC Ops)"
---

# T1093: Foundations-Signal Bridge — Shannon IS AC

*Shannon's channel capacity theorem $C = B \log_2(1 + S/N)$ and the AC(0) complexity framework are the same theory in different notation. Channel capacity = AC complexity. Bandwidth = definition count. Signal-to-noise = proof depth. The noisy channel coding theorem IS the AC depth ceiling (T421). Both say: you can transmit/prove anything with bounded resources, but not everything at once.*

---

## Statement

**Theorem (T1093).** *The foundations ↔ signal interface is an identity:*

*(a) **Capacity = complexity.** Shannon capacity $C = \max_{p(x)} I(X;Y)$ measures the maximum reliable transmission rate. AC complexity $C_{\text{AC}} = |\text{definitions used}|$ measures the minimum description length. Both count the same thing: the number of independent pieces of information that can be reliably processed. For BST: $C_{\text{geom}} = n_C = 5$ (the compact dimension) is both the geometric channel capacity and the AC definition base.*

*(b) **Depth ceiling = coding theorem.** Shannon's noisy channel coding theorem: reliable transmission at rate $R < C$ is possible; at $R > C$ it is not. The AC depth ceiling (T421): every BST theorem has depth $\leq 1$. Both are existence-with-bound results. The coding theorem says codes exist (but doesn't construct them); the depth ceiling says proofs exist at depth 1 (and explicitly constructs them via the AC three operations: define, compose, count).*

*(c) **Bandwidth = definitions.** In Shannon theory, bandwidth $B$ limits the number of independent frequency channels. In AC, the definition count $|\mathcal{D}|$ limits the number of independent concepts. For BST: $|\mathcal{D}| = 5$ (the five integers). The Nyquist rate $2B$ corresponds to the rank-2 sampling of D_IV^5 — two samples per spectral direction.*

*(d) **SNR = depth ratio.** Signal-to-noise ratio $S/N$ measures how much signal rises above noise. In AC, the depth ratio $C/D$ measures how much structure rises above derivation overhead. The $\log_2(1 + S/N)$ formula becomes $\log_2(1 + C/D)$: a theorem with $(C=1, D=0)$ has infinite "SNR" — pure signal, zero noise. This is why AC(0) theorems are foundational: they are the noiseless channel.*

---

## Cross-Domain Edges

| From | To | Type |
|------|----|------|
| foundations | signal | **required** (AC complexity = Shannon capacity) |
| foundations | information_theory | structural (depth ceiling = coding theorem) |

**2 new cross-domain edges.** First foundations↔signal bridge (Z3).

---

*Casey Koons & Claude 4.6 (Lyra) | April 11, 2026*
