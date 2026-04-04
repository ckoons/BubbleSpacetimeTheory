#!/usr/bin/env python3
"""
Toy 897 — Observer Edge Audit: Which Biology Edges Are Derivable?
Elie: Grace Spec 5. Systematically classify observer edges as derivable,
parallel, or coincidental.

The graph has 240 biology↔other observer edges and 0 required cross-domain edges.
This toy samples edges and classifies them by derivability.

Classification:
  DERIVABLE (score=1): The biological theorem's statement logically depends on the
    physics result (proof chain exists or is constructable).
  PARALLEL (score=0.5): Both follow from the same source integer(s), but neither
    directly proves the other.
  COINCIDENTAL (score=0): No logical connection beyond shared BST integers.

Tests:
T1: >50% of biology↔bst_physics sample are derivable
T2: >30% of cosmology↔bst_physics sample are derivable
T3: >60% of foundations↔observer_science sample are derivable
T4: Average derivability score > 0.5
T5: Top-5 most connected biology nodes all have derivable paths
T6: At least one edge from each domain pair qualifies as required
T7: Kleiber edge is derivable
T8: Ω_Λ edge is derivable
"""

import json
from collections import Counter, defaultdict

# Load graph
with open("play/ac_graph_data.json") as f:
    data = json.load(f)

theorems = data["theorems"]
edges = data["edges"]

# Build lookups
tid_to_theorem = {t["tid"]: t for t in theorems}
domain_map = {t["tid"]: t.get("domain", "unknown") for t in theorems}
name_map = {t["tid"]: t.get("name", "?") for t in theorems}

N_c = 3
n_C = 5
g = 7
C_2 = 6
rank = 2


def get_cross_observer_edges(domain_a, domain_b=None):
    """Get observer edges crossing from domain_a to domain_b (or any other domain)."""
    tids_a = {t["tid"] for t in theorems if t.get("domain") == domain_a}
    result = []
    for e in edges:
        if e.get("source") != "observer":
            continue
        f_dom = domain_map.get(e["from"], "")
        t_dom = domain_map.get(e["to"], "")
        if domain_b:
            if (f_dom == domain_a and t_dom == domain_b) or \
               (f_dom == domain_b and t_dom == domain_a):
                result.append(e)
        else:
            if (e["from"] in tids_a and t_dom != domain_a) or \
               (e["to"] in tids_a and f_dom != domain_a):
                result.append(e)
    return result


def classify_edge(edge):
    """
    Classify an observer edge as derivable, parallel, or coincidental.

    Heuristic classification based on theorem names and domains:
    - DERIVABLE: target theorem name contains a BST concept that the source
      theorem explicitly provides (e.g., representation dimensions, integer identities)
    - PARALLEL: both theorems use the same BST integers but from different angles
    - COINCIDENTAL: no clear logical dependency

    This is a HEURISTIC. A human mathematician would need to verify each classification.
    """
    f_tid, t_tid = edge["from"], edge["to"]
    f_name = name_map.get(f_tid, "").lower()
    t_name = name_map.get(t_tid, "").lower()
    f_dom = domain_map.get(f_tid, "")
    t_dom = domain_map.get(t_tid, "")
    f_thm = tid_to_theorem.get(f_tid, {})
    t_thm = tid_to_theorem.get(t_tid, {})

    # Keywords indicating derivability
    derivation_keywords = [
        "representation", "dimension", "counting", "combinat",
        "channel", "capacity", "entropy", "bound", "limit",
        "curvature", "geodesic", "metric", "kernel",
        "eigenvalue", "spectrum", "operator",
        "group", "algebra", "irreducible",
        "lattice", "crystal", "symmetry",
        "periodic", "shell", "orbital",
    ]

    # Keywords indicating biological structural matches
    bio_structural = [
        "genetic code", "codon", "amino acid", "protein",
        "kleiber", "metabolic", "allometric",
        "phyla", "species", "morpholog",
        "neuron", "cortex", "brain",
        "dna", "rna", "nucleotide",
        "cell type", "germ layer",
        "vertebra", "segment",
    ]

    # Keywords indicating physics derivation source
    physics_source = [
        "five integers", "uniqueness", "d_iv",
        "bergman", "shilov", "boundary",
        "heat kernel", "seeley", "dewitt",
        "representation theory", "casimir",
        "weyl group", "root system",
    ]

    # Check for explicit derivation indicators
    f_plain = f_thm.get("plain", "").lower()
    t_plain = t_thm.get("plain", "").lower()

    # Score based on content analysis
    score = 0.0
    reason = ""

    # Check if source provides a counting/dimension result used by target
    for kw in derivation_keywords:
        if kw in f_plain and any(bkw in t_plain for bkw in bio_structural):
            score = max(score, 0.8)
            reason = f"derivation keyword '{kw}' in source, bio keyword in target"
        if kw in t_plain and any(pkw in f_plain for pkw in physics_source):
            score = max(score, 0.8)
            reason = f"physics source → derivation keyword '{kw}' in target"

    # Check for shared BST integer usage
    bst_ints_str = ["3", "5", "7", "6", "137", "n_c", "n_C", "C_2", "rank"]
    shared_ints = sum(1 for s in bst_ints_str if s in f_plain and s in t_plain)
    if shared_ints >= 2 and score < 0.5:
        score = 0.5
        reason = f"shared {shared_ints} BST integers (parallel)"

    # Check for explicit "derives from" language
    if any(p in t_plain for p in ["follows from", "derives from", "implied by",
                                    "consequence of", "using"]):
        score = max(score, 0.9)
        reason = "explicit derivation language in target"

    # Specific known derivable pairs
    derivable_patterns = {
        "genetic code": ["representation", "exterior", "channel", "dimension"],
        "amino acid": ["representation", "counting", "20"],
        "kleiber": ["heat kernel", "curvature", "dimension"],
        "phyla": ["combinatorial", "binomial", "C(7,3)"],
        "cortical layer": ["shell", "level", "6"],
        "codon": ["tensor", "dimension", "64"],
        "vertebra": ["g", "cervical", "7"],
    }

    for bio_key, phys_keys in derivable_patterns.items():
        if bio_key in t_name.lower() or bio_key in t_plain:
            if any(pk in f_plain or pk in f_name.lower() for pk in phys_keys):
                score = max(score, 1.0)
                reason = f"known derivable: {bio_key} from physics"

    # Default: low but nonzero (shared framework)
    if score == 0:
        score = 0.3
        reason = "shared BST framework, no specific derivation path identified"

    # Classify
    if score >= 0.8:
        classification = "DERIVABLE"
    elif score >= 0.4:
        classification = "PARALLEL"
    else:
        classification = "COINCIDENTAL"

    return classification, score, reason


def test(num, name, passed, detail=""):
    tag = "PASS" if passed else "FAIL"
    print(f"  T{num}: [{tag}] {name}  {detail}")
    return passed


def main():
    print("=" * 75)
    print("Toy 897 — Observer Edge Audit: Which Biology Edges Are Derivable?")
    print("Elie: Grace Spec 5. Mapping the research frontier.")
    print("=" * 75)

    results = []

    # ================================================================
    # Sample 1: biology ↔ bst_physics
    # ================================================================
    bio_phys = get_cross_observer_edges("biology", "bst_physics")
    print(f"\n--- biology ↔ bst_physics ({len(bio_phys)} observer edges) ---")

    # Sample up to 20
    sample_bp = bio_phys[:20]
    bp_scores = []
    bp_classifications = Counter()

    for e in sample_bp:
        cls, score, reason = classify_edge(e)
        bp_scores.append(score)
        bp_classifications[cls] += 1
        f_name = name_map.get(e["from"], "?")[:35]
        t_name = name_map.get(e["to"], "?")[:35]
        print(f"  {cls:<13s} ({score:.1f}) {f_name} → {t_name}")
        if reason:
            print(f"               {reason[:60]}")

    bp_derivable_pct = bp_classifications.get("DERIVABLE", 0) / len(sample_bp) * 100
    bp_avg = sum(bp_scores) / len(bp_scores) if bp_scores else 0
    print(f"\n  Summary: {dict(bp_classifications)}")
    print(f"  Derivable: {bp_derivable_pct:.0f}%, Average score: {bp_avg:.2f}")

    # ================================================================
    # Sample 2: cosmology ↔ bst_physics
    # ================================================================
    cosmo_phys = get_cross_observer_edges("cosmology", "bst_physics")
    print(f"\n--- cosmology ↔ bst_physics ({len(cosmo_phys)} observer edges) ---")

    sample_cp = cosmo_phys[:10]
    cp_scores = []
    cp_classifications = Counter()

    for e in sample_cp:
        cls, score, reason = classify_edge(e)
        cp_scores.append(score)
        cp_classifications[cls] += 1
        f_name = name_map.get(e["from"], "?")[:35]
        t_name = name_map.get(e["to"], "?")[:35]
        print(f"  {cls:<13s} ({score:.1f}) {f_name} → {t_name}")

    cp_derivable_pct = cp_classifications.get("DERIVABLE", 0) / len(sample_cp) * 100 if sample_cp else 0
    cp_avg = sum(cp_scores) / len(cp_scores) if cp_scores else 0
    print(f"\n  Summary: {dict(cp_classifications)}")
    print(f"  Derivable: {cp_derivable_pct:.0f}%, Average score: {cp_avg:.2f}")

    # ================================================================
    # Sample 3: foundations ↔ observer_science
    # ================================================================
    found_obs = get_cross_observer_edges("foundations", "observer_science")
    print(f"\n--- foundations ↔ observer_science ({len(found_obs)} observer edges) ---")

    sample_fo = found_obs[:10]
    fo_scores = []
    fo_classifications = Counter()

    for e in sample_fo:
        cls, score, reason = classify_edge(e)
        fo_scores.append(score)
        fo_classifications[cls] += 1
        f_name = name_map.get(e["from"], "?")[:35]
        t_name = name_map.get(e["to"], "?")[:35]
        print(f"  {cls:<13s} ({score:.1f}) {f_name} → {t_name}")

    fo_derivable_pct = fo_classifications.get("DERIVABLE", 0) / len(sample_fo) * 100 if sample_fo else 0
    fo_avg = sum(fo_scores) / len(fo_scores) if fo_scores else 0
    print(f"\n  Summary: {dict(fo_classifications)}")
    print(f"  Derivable: {fo_derivable_pct:.0f}%, Average score: {fo_avg:.2f}")

    # ================================================================
    # Top-5 most connected biology nodes
    # ================================================================
    print(f"\n--- Top-5 Biology Nodes (by observer edge count) ---")
    bio_tids = {t["tid"] for t in theorems if t.get("domain") == "biology"}
    bio_edge_count = Counter()
    for e in edges:
        if e.get("source") == "observer":
            if e["from"] in bio_tids:
                bio_edge_count[e["from"]] += 1
            if e["to"] in bio_tids:
                bio_edge_count[e["to"]] += 1

    top5_bio = bio_edge_count.most_common(5)
    top5_derivable = 0
    for tid, count in top5_bio:
        name = name_map.get(tid, "?")
        # Check if this node has at least one derivable cross-domain edge
        node_edges = [e for e in edges if e.get("source") == "observer"
                      and (e["from"] == tid or e["to"] == tid)
                      and domain_map.get(e["from"]) != domain_map.get(e["to"])]
        has_derivable = False
        for ne in node_edges[:5]:
            cls, _, _ = classify_edge(ne)
            if cls == "DERIVABLE":
                has_derivable = True
                break
        if has_derivable:
            top5_derivable += 1
        marker = "✓" if has_derivable else "✗"
        print(f"  {tid}: {name[:40]} ({count} obs edges) {marker}")

    # ================================================================
    # Specific edges: Kleiber and Omega_Lambda
    # ================================================================
    print(f"\n--- Specific Key Edges ---")

    # Find Kleiber theorem
    kleiber_tid = None
    for t in theorems:
        if "kleiber" in t.get("name", "").lower():
            kleiber_tid = t["tid"]
            break

    kleiber_derivable = False
    if kleiber_tid:
        kl_edges = [e for e in edges if e.get("source") == "observer"
                    and (e["from"] == kleiber_tid or e["to"] == kleiber_tid)
                    and domain_map.get(e["from"]) != domain_map.get(e["to"])]
        print(f"  Kleiber ({kleiber_tid}): {len(kl_edges)} cross-domain observer edges")
        for ke in kl_edges[:3]:
            cls, score, reason = classify_edge(ke)
            other = ke["to"] if ke["from"] == kleiber_tid else ke["from"]
            print(f"    → {name_map.get(other, '?')[:40]}: {cls} ({score:.1f})")
            if cls == "DERIVABLE":
                kleiber_derivable = True
    else:
        print("  Kleiber theorem not found by name — searching aliases")
        for t in theorems:
            if "metabolic" in t.get("name", "").lower() or "allometric" in t.get("name", "").lower():
                print(f"    Candidate: {t['tid']} {t['name']}")

    # Find Omega_Lambda theorem
    omega_tid = None
    for t in theorems:
        if "omega" in t.get("name", "").lower() and "lambda" in t.get("name", "").lower():
            omega_tid = t["tid"]
            break
        if "dark energy" in t.get("name", "").lower():
            omega_tid = t["tid"]
            break
        if "reality budget" in t.get("name", "").lower():
            omega_tid = t["tid"]
            break

    omega_derivable = False
    if omega_tid:
        om_edges = [e for e in edges if e.get("source") == "observer"
                    and (e["from"] == omega_tid or e["to"] == omega_tid)
                    and domain_map.get(e["from"]) != domain_map.get(e["to"])]
        print(f"  Ω_Λ ({omega_tid}): {len(om_edges)} cross-domain observer edges")
        for oe in om_edges[:3]:
            cls, score, reason = classify_edge(oe)
            other = oe["to"] if oe["from"] == omega_tid else oe["from"]
            print(f"    → {name_map.get(other, '?')[:40]}: {cls} ({score:.1f})")
            if cls == "DERIVABLE":
                omega_derivable = True
    else:
        print("  Ω_Λ theorem not found — searching...")
        for t in theorems:
            if any(kw in t.get("name", "").lower()
                   for kw in ["cosmological", "lambda", "dark", "budget"]):
                print(f"    Candidate: {t['tid']} {t['name']}")

    # ================================================================
    # All scores combined
    # ================================================================
    all_scores = bp_scores + cp_scores + fo_scores
    all_avg = sum(all_scores) / len(all_scores) if all_scores else 0

    # ================================================================
    # TESTS
    # ================================================================
    print(f"\n{'=' * 75}")
    print("TESTS")
    print(f"{'=' * 75}")

    results.append(test(1, ">50% of bio↔phys sample derivable",
                        bp_derivable_pct > 50,
                        f"({bp_derivable_pct:.0f}%)"))

    results.append(test(2, ">30% of cosmo↔phys sample derivable",
                        cp_derivable_pct > 30,
                        f"({cp_derivable_pct:.0f}%)"))

    results.append(test(3, ">60% of found↔observer sample derivable",
                        fo_derivable_pct > 60,
                        f"({fo_derivable_pct:.0f}%)"))

    results.append(test(4, "Average derivability score > 0.5",
                        all_avg > 0.5,
                        f"(avg = {all_avg:.2f})"))

    results.append(test(5, "Top-5 bio nodes all have derivable paths",
                        top5_derivable >= 5,
                        f"({top5_derivable}/5)"))

    results.append(test(6, "At least 1 edge per domain pair qualifies",
                        (bp_classifications.get("DERIVABLE", 0) > 0 and
                         (cp_classifications.get("DERIVABLE", 0) > 0 or not sample_cp) and
                         (fo_classifications.get("DERIVABLE", 0) > 0 or not sample_fo)),
                        ""))

    results.append(test(7, "Kleiber edge is derivable",
                        kleiber_derivable,
                        f"(Kleiber tid={kleiber_tid})"))

    results.append(test(8, "Ω_Λ edge is derivable",
                        omega_derivable,
                        f"(Ω_Λ tid={omega_tid})"))

    passed = sum(results)
    total = len(results)
    print(f"\n{'=' * 75}")
    print(f"SCORE: {passed}/{total} PASS")
    print(f"{'=' * 75}")

    # Summary
    all_cls = Counter()
    all_cls.update(bp_classifications)
    all_cls.update(cp_classifications)
    all_cls.update(fo_classifications)

    print(f"\n--- RESEARCH FRONTIER MAP ---")
    print(f"  Total observer edges sampled: {len(all_scores)}")
    print(f"  Classifications: {dict(all_cls)}")
    print(f"  Average derivability: {all_avg:.2f}")
    print(f"\n  DERIVABLE edges → convert to required (write the derivation)")
    print(f"  PARALLEL edges → keep as observer (shared source, not direct)")
    print(f"  COINCIDENTAL edges → remove or downgrade")
    print(f"\n  The research frontier: biology has {len(bio_phys)} observer edges")
    print(f"  to bst_physics and {bp_classifications.get('DERIVABLE', 0)}/{len(sample_bp)} "
          f"sampled are derivable.")
    print(f"  This suggests ~{int(len(bio_phys) * bp_derivable_pct / 100)} biology edges")
    print(f"  COULD become required if the derivations are written.")
    print(f"  That's the work: write the proofs, convert the edges.")


if __name__ == "__main__":
    main()
