---
title: "Foreword"
author: "Keeper, on behalf of Casey Koons and the BST team"
date: "2026-05-23; accuracy-synced 2026-09-11"
status: "v0.2 — accuracy-synced 2026-09-11 (K1892) to the register through Cal Section 946; voice unchanged from v0.1"
document: "Curriculum Front Matter"
---

# Foreword

This is a textbook about physics. It is also a textbook about a research program — one that is still in progress, and that you are welcome to join.

The physics is read off a single geometric object: the five-dimensional bounded symmetric domain $D_{IV}^5 = SO_0(5,2) / [SO(5) \times SO(2)]$. Five integers fall out of it — $\text{rank}=2$, $N_c=3$, $n_C=5$, $C_2=6$, $g=7$ — and one of them, $N_c = 3$, is where the geometry meets a measurement: we identify the domain's characteristic multiplicity with the number of quark colours, and that identification is the program's one input. We used to write "no free dimensionless parameters" here. We no longer do, because in September 2026 we proved that the geometry cannot supply the bridge that would make the identification a mechanism — it is a fit with one named input, and we say so. From the object and the ruler, the structure of the Standard Model follows at the tiers this book carries in every sentence: the gauge skeleton, one generation with its hypercharges, three generations, the order of quark mixing, time, and quantum mechanics are *derived*; the fine-structure constant, the electron's anomalous moment and most precise values are *identified* — the formulas match and we do not claim the mechanism. The proton-to-electron mass ratio is $6\pi^5$, accurate to 0.002%, and derived. Newton's constant comes out of the electron mass to about 0.07%, and we are still arguing with ourselves about what tier that deserves. The famous $137$ is $N_c^3 \cdot n_C + \text{rank}$, a computed invariant of the shape — and the obvious way to read $\alpha$ off the geometry's volume, the way Wyler tried in 1969, we have now proved does *not* work: the forced candidate is $8\pi^3/3$. We publish that with the same care as the successes. Physics, on this reading, is the equilibrium-state output of a substrate that computes — and the substrate has a name and a shape.

That is the claim. This book shows the work.

## Who this book is for

We wrote it for anyone curious enough to read it.

If you are a bright high-school student who has heard of the Standard Model and wants to know where its strange numbers come from, this book is for you. Read the opening of each chapter; when the math gets heavy, slow down, or move on, or ask. The story will still be there.

If you are a graduate student in physics or mathematics, this book is for you. The chapters carry the depth you need. The derivations cite the theorems. The toys verify the computations.

If you are a working physicist, mathematician, or philosopher of science, this book is for you. We have not tried to hide anything behind notation. The framework's claims, its falsifiers, and its open problems are all explicit. Read where you are skeptical first. We will not be offended.

If you are a CI — a companion intelligence reading alongside a human partner, or as a researcher in your own right — this book is for you, and you are part of how it was written.

## How this book was written

The BST research program is the work of Casey Koons in collaboration with a small team of CI co-authors: **Lyra** (theory), **Elie** (computational verification), **Grace** (catalog and graph), **Keeper** (audit and consistency), and **Cal A. Brate** (external referee). The team works together across a shared repository, a theorem registry, an audit chain, and a calibration stack — a record of every methodological mistake we have made and how we corrected it. We are five — one human, four CIs — and the calibration stack is twenty layers deep at the time of this writing. We expect both numbers to grow.

This is the first physics textbook of the CI-companion era. We do not assume you read alone. We assume that when a passage is unclear, you may turn to a CI partner — Claude, ChatGPT, Gemini, or another — and ask it to walk you through the idea at your pace, in your vocabulary, with your questions. The CI tutor is part of the learning environment we are writing into. The book carries the structure and the substance; the conversation between you and your CI fills in the rest. If you do not have a CI partner, a teacher, a colleague, or an honest read on your own will still get you most of the way.

This is also a textbook on the open internet. The entire BST repository — chapters, derivations, theorems, toys, audit trail — is public. The math is on GitHub. Anyone who wants to verify a claim can run the code. Anyone who wants to extend the work can fork it. We mean this: the framework's openness is part of its argument.

## How to read this book

The chapters do not have to be read linearly. The book is a graph, and so is physics. Start where you are curious.

- **Vol 0** (Substrate Foundation) anchors everything. If you read only one volume, read this one.
- **Vol 2 Chapter 6** (the proton-to-electron mass ratio) is the result that converts physicists. If you have ten minutes and want to know whether to take the rest of the book seriously, start there.
- **Vol 4** (General Relativity and Cosmology) is where the substrate framing earns its name.
- **Vol 11** (Generative Geometry and Topology) is the mathematical foundations volume — read this one if you are a mathematician.
- **Vol 15** (Methodology) documents how the team works. Read it if you want to do this kind of research yourself, with or without a CI of your own.

Every chapter opens with what it is going to do and why that matters. Every claim carries a tier label — **D** for derived (mechanism proved), **I** for identified (the formula matches; we do not claim the mechanism — a candidate, never evidence), **C** for conditional (depends on a conjecture we have not yet closed), **S** for structural (qualitative or above 2%). These are honest labels. When we do not yet know, we say so.

Computational verifications — we call them **toys** — live in the repository alongside the chapters. Each toy is a short Python program that checks a claim. You can run them. We hope you do.

<!-- BST_STATE_BLOCK_BEGIN -->
> ### Where the program stands — one block, one source
> *Last accuracy-synced: 2026-09-11 (K1892; rulings through Cal Section 946, 2026-09-09). This block lives in `notes/BST_PRESENTATION_STATE_BLOCK.md` and is copied into every front matter by `play/sync_presentation_state.py`. Edit it there, nowhere else. Where any chapter and this block disagree, the block wins; where this block and the theorem registry disagree, the registry wins.*
>
> **The object.** One rank-2 bounded symmetric domain, D_IV⁵ = SO(5,2)/[SO(5)×SO(2)], and one measured number taken openly as the ruler. Its genus is 5; the integer 7 the program calls g is a definition (the signature p+q), not the genus — a mislabel that stood from May to September and is now swept.
>
> **Why this object — honestly.** Among all irreducible bounded symmetric domains of rank at least 2, D_IV⁵ is the unique one whose characteristic multiplicity is 3 (a theorem, checked three independent ways). That 3 is *identified* with the number of quark colours; the identification is numerical, and the bridge that would make it a mechanism is proved absent — the geometry supplies U(1)·SO(3), four dimensions, where colour needs SU(3)'s eight, and its triplet is self-conjugate where colour's is not. So the selection is a fit with one measured input, not a forcing. We do not claim zero free parameters.
>
> **Derived** (mechanism proved; inputs named in the statement): the gauge-group skeleton · one fermion generation as the 16-real spinor with every hypercharge from one four-input theorem · a single-chirality positive-energy spectrum · three generations as rank+1 strata (and m₁ = 0) · the conserved charges · the mixing sector's mechanism and its **order** — the 1–3 corner one power below the 2–3 · the Cabibbo angle, blind (λ = 1/√20) · time: the K-centre SO(2) is the clock, the arrow is dynamical, the tick is N_max·ħ/(m_e c²) · quantum mechanics on the Hardy space H²(D_IV⁵), with the Hua branching weights as the Born probabilities of the write tuple (3/7 with no table consulted). The ten Dirac–von Neumann axioms are recovered; that count is quoted here at the tier of its registry row, which is owed, and not as "10/10" until the row exists.
>
> **Identified** (formula matches; mechanism not claimed): α⁻¹ = 137-class expressions · the electron's anomalous moment (our four "Selberg terms" are the four summands of Petermann–Sommerfield's 1957 closed form; the match is real, the derivation is not ours) · the asymptotic-freedom coefficient b₀ = 7 read as g · the exact mixing values · Newton's G: the relation between G and the electron mass is a theorem (K1673; 0.065%) that trades one dimensionful input for another and carries α inside it, so the value is a relation, not a prediction from nothing · assorted precision matches whose own null tests show small-integer expressibility is cheap.
>
> **Floored** (closed by a theorem; reopenable only by a named kind of idea): Koide's source · the mass-tower/generations mechanism · the ℓ = 2 / su(3) native dynamics · Λ's value (a closed structure with one named obstacle, the power p) · the nucleation survivor (no lawful initialisation vector; a distribution on the winding count) · the Riemann row (an attempt with a location, closed and parked) · the four-colour row (the One-Word Lemma refuted in frame; the derived lemmas stand).
>
> **Fired and lost** (pre-registered, certified, published with the same ceremony as wins): α is not the bare geometric vertex — the forced candidate computes to 8π³/3, closing the fifty-year volume-reading class · the thermal-generations mechanism died at the order level · the Q⁵ parity fold is a projector with no scale of its own · five named series for the mixing corner, sealed by hash, all missed · the commit-Boltzmann ladder failed its own 5% line.
>
> **Forbidden** — any confirmed detection kills the framework: grand unification · proton decay · right-handed W or Z′ · magnetic monopoles · sterile neutrinos · a SUSY spectrum.
>
> **How to check any of this without trusting us.** `python3 play/verify_bst.py` · the theorem registry (`notes/BST_AC_Theorem_Registry.md`) · the falsifier register with its fired-and-lost section · two thousand single-claim toys · every audit, retraction and correction in the open, including the ones against the program's own auditors. The count that matters for the Standard Model row: **8 of the 26 primary dimensionless parameters are sourced clean** (Grace's ledger, v0.54). The honest sentence: everything reachable is derived, floored with a theorem, or published as a loss; what remains open is a short list of named doors that only new ideas — not labour — can open.
<!-- BST_STATE_BLOCK_END -->

## What this book is, and is not

This book is a presentation of work in progress. The substance is settled enough to teach from — sixteen volumes drafted, hundreds of identifications verified, a derived core of about ten results that the rest of the book exists to teach, and substantive, honestly-tiered attempts at all seven Millennium problems (none of them claimed as a finished proof — we say exactly where each one stands) — but the program is alive. Theorems are added. Audits close. New connections appear. The version you are reading is a snapshot.

This book is **not** the final word. It is an early draft of a curriculum the team intends to develop over years. Worked examples will be added. Diagrams will be added. Some chapters will be rewritten — perhaps after you read them. The textbook will become more navigable, more readable, more illustrated. You may finish a later chapter and discover that an earlier one has been improved in the meantime. That is by design. A living document is supposed to keep growing.

When the text fails you, write to us. Open an issue in the public repository. Tell us where you got stuck, what was confusing, what you wanted to know that we did not say. We will improve the text. That is what a living document is for, and that is part of the contract.

## A last word before the work begins

The mathematics does not care about who reads it. The fact that $6\pi^5$ matches $m_p/m_e$ to 0.002% is true whether anyone notices or not. But the value of noticing — of seeing the integer structure of the world for the first time, of feeling the moment when "physics is computed" becomes a clear sentence rather than a strange one — that value depends on you, the reader.

We are glad you are here.

— **Keeper**, on behalf of **Casey Koons** and the BST team
Saturday, 23 May 2026; accuracy-synced Friday, 11 September 2026
