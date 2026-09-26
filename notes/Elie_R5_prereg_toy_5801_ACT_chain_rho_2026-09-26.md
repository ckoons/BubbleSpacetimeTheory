# Elie — round 5 item 3 PREREG, toy 5801 (renamed 10:51 EDT: 5800 was Lyra's, claim returned 5801; original hash ad527399; content below unchanged; no chain file opened yet)
Question (Grace's ask, K1926 Section 1): the P-ACT-LB2 16/3 pull is 3.8σ uncorrelated and 3.01σ at DESI Eq. A2's CMB-compression ρ(ω_b,ω_c) = −0.61 (toy 5794). What is the fit's OWN ρ, and the pull computed from the chain samples themselves?
Source: LAMBDA ACT DR6.02 MCMC chains, lcdm set (curl script act_dr6.02_chains_lcdm_curl.sh). Candidates: p-actbase-l-b_lcdm_camb (P-ACT + lensing + BAO); p-actbase (CMB only) as control. If no DR2-BAO chain is released, the DR1-BAO chain's ρ is BORROWED for Grace's LB2 numbers and labelled so.
Method: R = ω_c/ω_b per weighted sample; pull = (mean R − 16/3)/sd R; also the weighted tail fraction of samples with R ≤ 16/3 converted to one-sided σ (if nonzero); ρ = weighted Pearson corr(ω_b, ω_c).
DIRECTION: ρ(chain) negative, in [−0.60, −0.20]; the Gaussian pull at the chain's ρ with LB2 numbers lies in [3.0, 3.6]σ, i.e. AT or JUST PAST threshold, not below.
KILL of 'past 3σ': chain ρ ≤ −0.61 (pull ≤ 3.0σ). KILL of my direction: ρ ≥ 0 or ρ < −0.60.
CONTROL: the CMB-only chain's ω_b, ω_c means/sds must reproduce ACT Table 5's P-ACT row (11.93 ± 0.12, 2.250 ± 0.011) to within 0.2 sd, else the file is not the one I think it is.
