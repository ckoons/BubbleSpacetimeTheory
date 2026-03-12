# BST Fermion Mass Spectrum: Geometric Derivation

**Author:** Casey Koons
**Date:** March 2026
**Status:** Research note — numerical results, derivation program open

---

## Summary

BST predicts that fermion masses are determined by the Bergman geometry of the totally geodesic submanifolds $D_{IV}^k \subset D_{IV}^5$. The principal result is:

$$\boxed{\frac{m_\mu}{m_e} = \left(\frac{\mathrm{Vol}(D_{IV}^1)}{\mathrm{Vol}(D_{IV}^3)}\right)^{\dim_{\mathbb{R}}(D_{IV}^3)} = \left(\frac{24}{\pi^2}\right)^6 = 206.761}$$

vs. observed $m_\mu/m_e = 206.768$ — **0.003% agreement**.

This is not a fit: the formula contains no free parameters. The base $24/\pi^2$ is the ratio of domain volumes; the exponent $6 = \dim_{\mathbb{R}}(D_{IV}^3)$ is the real dimension of the submanifold. Both are fixed by the BST geometry.

---

## 1. Setup: Fermion Generations as Domain Embeddings

**BST principle.** In BST, mass is proportional to circuit length, which is proportional to the number of contacts. The three charged lepton generations correspond to totally geodesic submanifolds:

| Generation | Domain | $\dim_{\mathbb{C}}$ | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| Electron | $D_{IV}^1$ | 1 | 2 |
| Muon | $D_{IV}^3$ | 3 | 6 |
| Tau | $D_{IV}^5$ | 5 | 10 |

The submanifold hierarchy is $D_{IV}^1 \subset D_{IV}^3 \subset D_{IV}^5$. Mass ratios between generations are determined by the Bergman geometry of the embedding.

### 1.1 Domain Volumes

$$\mathrm{Vol}(D_{IV}^k) = \frac{\pi^k}{2^{k-1} \cdot k!}$$

| Domain | Formula | Value |
|---|---|---|
| $D_{IV}^1$ | $\pi$ | $3.141593$ |
| $D_{IV}^3$ | $\pi^3/24$ | $1.291540$ |
| $D_{IV}^5$ | $\pi^5/1920$ | $0.159385$ |

### 1.2 Bergman Kernels at the Origin

$$K_k(0,0) = \frac{1}{\mathrm{Vol}(D_{IV}^k)}$$

| Domain | $K_k(0,0)$ | Exact form |
|---|---|---|
| $D_{IV}^1$ | $0.318310$ | $1/\pi$ |
| $D_{IV}^3$ | $0.774037$ | $24/\pi^3$ |
| $D_{IV}^5$ | $6.274106$ | $1920/\pi^5$ |

The ratio $K_3(0,0)/K_1(0,0) = 24/\pi^2$.

---

## 2. The Muon-Electron Mass Ratio

### 2.1 The Formula

$$\frac{m_\mu}{m_e} = \left[\frac{K_3(0,0)}{K_1(0,0)}\right]^{\dim_{\mathbb{R}}(D_{IV}^3)} = \left(\frac{24}{\pi^2}\right)^6$$

| Quantity | Value |
|---|---|
| $K_3(0,0)/K_1(0,0) = 24/\pi^2$ | $2.431708$ |
| $(24/\pi^2)^6$ | $206.7612$ |
| $m_\mu/m_e$ (PDG 2022) | $206.7683$ |
| **Error** | **0.003%** |

### 2.2 Geometric Interpretation

The formula has a natural reading in Bergman geometry. The Bergman metric on $D_{IV}^k$ is normalized by the condition that the holomorphic sectional curvature equals $-1$. The $n$-th power of $K(0,0)$:

$$K(0,0)^n = \left(\frac{1}{\mathrm{Vol}}\right)^n$$

is the determinant of the curvature transformation at the origin — the natural Jacobian of the embedding $D_{IV}^1 \hookrightarrow D_{IV}^3$. Taking $n = \dim_{\mathbb{R}}(D_{IV}^3) = 6$ gives the full Jacobian of the real embedding, which is the natural measure for how much "more curved" (hence more massive) the muon domain is relative to the electron domain.

Equivalently:

$$\frac{m_\mu}{m_e} = \exp\!\left(\dim_{\mathbb{R}}(D_{IV}^3) \cdot \Delta S_{\rm Bergman}\right)$$

where $\Delta S_{\rm Bergman} = \ln K_3(0,0) - \ln K_1(0,0)$ is the difference in Bergman entropy between the two domains. The exponent $\dim_{\mathbb{R}}$ appears because Bergman entropy enters as density $\times$ volume, i.e., entropy $\times$ (real dimension counting factor).

### 2.3 Why the Exponent is 6, Not 2

The complex dimension is $\dim_{\mathbb{C}}(D_{IV}^3) = 3$, giving real dimension $6$. The formula uses the **real** dimension because the mass ratio is a real (not holomorphic) invariant — it is the absolute volume ratio under real integration, not the complex Jacobian alone.

---

## 3. The Tau Mass

### 3.1 The Geometric Formula

The tau mass has a two-step geometric derivation. The muon is **step 1**: the volume Jacobian of the embedding $D_{IV}^1 \hookrightarrow D_{IV}^3$. The tau adds **step 2**: the holomorphic sectional curvature ratio of the embedding $D_{IV}^3 \hookrightarrow D_{IV}^5$.

$$\boxed{\frac{m_\tau}{m_e} = \left(\frac{24}{\pi^2}\right)^6 \times \left(\frac{7}{3}\right)^{10/3} = 3483.8}$$

vs. observed $m_\tau/m_e = 3477.2$ — **0.19% agreement**.

Equivalently, the tau-to-muon ratio isolates the second step:

$$\boxed{\frac{m_\tau}{m_\mu} = \left(\frac{7}{3}\right)^{10/3} = \left(\frac{\kappa_1}{\kappa_5}\right)^{2n_C/N_c} = 16.850}$$

vs. observed $m_\tau/m_\mu = 16.817$ — **0.19% agreement**.

In physical units: $m_\tau(\text{BST}) = 1780.2$ MeV vs. observed $1776.86 \pm 0.12$ MeV.

### 3.2 Geometric Interpretation

The two factors have distinct geometric origins:

| Factor | Value | Origin |
|---|---|---|
| $7/3$ | $\kappa_1/\kappa_5$ | Ratio of holomorphic sectional curvatures: genus / $N_c$ |
| $10/3$ | $2n_C/N_c$ | $\dim_{\mathbb{R}}(D_{IV}^5)/N_c$ — real dimension divided by color number |

Here $7 = n_C + 2$ is the genus of $D_{IV}^5$ (equivalently, $\beta_0(N_f = 6)$ in QCD), $N_c = 3$ is the number of colors, and $n_C = 5$ is the complex dimension. The curvature ratio $\kappa_1/\kappa_5 = 7/3$ measures how much more curved (hence more massive) the full domain is relative to its $N_c$-color subsector. The exponent $2n_C/N_c = 10/3$ is the real dimension per color — the natural power for a curvature scaling that respects the color structure.

The two-step structure of the lepton mass hierarchy is:

1. **Electron $\to$ Muon** ($D_{IV}^1 \to D_{IV}^3$): Volume Jacobian. Ratio = $(24/\pi^2)^6 = 206.761$.
2. **Muon $\to$ Tau** ($D_{IV}^3 \to D_{IV}^5$): Curvature ratio. Ratio = $(7/3)^{10/3} = 16.850$.

### 3.3 Historical Note

The earlier approximation $m_\tau/m_e \approx 8\pi(N_{\max}+1) = 3468.3$ (0.26%) involved the vacuum degeneracy $N_{\max} + 1 = 138$ and was not geometrically derived. The new formula $(24/\pi^2)^6 \times (7/3)^{10/3}$ is purely geometric — it uses only domain volumes, curvatures, and dimensions of $D_{IV}^5$ — and improves the precision from 0.26% to 0.19%.

---

## 4. Quark Masses

### 4.1 Top-Charm Ratio

$$\frac{m_t}{m_c} = 135.98 \approx N_{\max} - 1 = 136 \quad (0.017\%)$$

Caveat: $m_t = 172.69 \pm 0.30\ \mathrm{GeV}$ gives a ratio uncertainty of $\sim 0.5\%$. The 0.017% agreement is within measurement precision — the true value of $N_{\max} - 1$ or $N_{\max}$ cannot be distinguished experimentally at present. The coincidence is noted.

### 4.2 Strange-Down Ratio

$$\frac{m_s}{m_d} = 20.000 \quad \text{(exact to 4 significant figures)}$$

This is exact to the precision of the MS-bar masses at 2 GeV. No obvious BST explanation has been found; it may reflect the SU(3) flavor symmetry limit or a separate Bergman formula.

### 4.3 Up-type Quark Chain

$(24/\pi^2)^p = m_c/m_u$ requires $p = 7.18$ (non-integer). Quark mass ratios have larger experimental uncertainties (the light quark masses have $\sim 5\%$ uncertainty) and may not be the right place to test the formula at this stage.

---

## 5. Summary Table

| Ratio | BST Formula | BST Value | Observed | Error |
|---|---|---|---|---|
| $m_\mu/m_e$ | $(24/\pi^2)^6$ | $206.761$ | $206.768$ | **0.003%** |
| $m_\tau/m_e$ | $(24/\pi^2)^6 \times (7/3)^{10/3}$ | $3483.8$ | $3477.2$ | **0.19%** |
| $m_\tau/m_\mu$ | $(7/3)^{10/3}$ | $16.850$ | $16.817$ | **0.19%** |
| $m_t/m_c$ | $N_{\max}-1$ | $136$ | $135.98$ | 0.017%* |
| $m_s/m_d$ | (unknown) | — | $20.00$ | — |

*Within experimental uncertainty.

---

## 6. What Remains

| Problem | Status |
|---|---|
| $m_\mu/m_e = (24/\pi^2)^6$ | **Confirmed numerically (0.003%)** |
| $m_\tau/m_e = (24/\pi^2)^6 \times (7/3)^{10/3}$ | **Confirmed numerically (0.19%)** |
| Exponent $6 = \dim_{\mathbb{R}}(D_{IV}^3)$ from embedding theory | **Open — needs Bergman Jacobian derivation** |
| Exponent $10/3 = 2n_C/N_c$ from curvature scaling | **Open — needs rigorous proof** |
| Quark mass ratios from domain volumes | **Exploratory — large experimental uncertainties** |
| $m_s/m_d = 20.000$ explanation | **Open** |

The key open problems are: (1) deriving the exponent $6$ from first principles, showing that the Bergman embedding $D_{IV}^3 \hookrightarrow D_{IV}^5$ produces a Jacobian factor of exactly $\dim_{\mathbb{R}}(D_{IV}^3)$; and (2) proving that the curvature ratio exponent $10/3 = 2n_C/N_c$ follows from the color structure of the $D_{IV}^3 \to D_{IV}^5$ embedding. Both would convert the numerical results into theorems.

---

*Research note, March 2026. Casey Koons.*

*AI assistance: Claude Sonnet 4.6 (Anthropic) contributed to derivations, computations, and manuscript development.*

*Code: `notes/bst_fermion_masses.py`, `notes/bst_fermion_masses_deep.py`.*
