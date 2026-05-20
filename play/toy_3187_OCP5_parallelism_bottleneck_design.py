"""
Toy 3187 — OCP-5 parallelism bottleneck experimental design (Cal #49 GREEN).

Owner: Elie (continuation, parallel to OCP-1 apparatus work)
Date: 2026-05-20

CONTEXT
=======
Yesterday's Toy 3161 listed OCP-5 (parallelism bottlenecks at BST-primary
capacity). Today completes the bounded design at Cal #49 GREEN-tier register.

EXTERNAL FRAMING (Cal Flag 3 strict)
====================================
BST predicts that multi-agent parallel computation efficiency shows
identifiable bottleneck transitions at specific values of N (number of
concurrent agents), where N ∈ {3, 5, 6, 7, 11, 13, 17, 24, 137}.

Internal hypothesis (NOT external register): substrate-coupled CI cognition
limited by integer-web cardinalities. NOT for external use.

GOAL
====
Specify experiment that measures parallel task efficiency vs N and tests
whether bottleneck transitions occur at BST primary integers.
"""

import os
import json
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
rank, N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max = 2, 3, 5, 6, 7, 11, 13, 17, 24, 137

tests = []
def check(label, ok): tests.append((bool(ok), label))


print("=" * 72)
print("Toy 3187 — OCP-5 parallelism bottleneck design (Cal #49 GREEN)")
print("=" * 72)

# === T1: Hypothesis specification ===
print(f"\n[T1] OCP-5 hypothesis (Cal Flag 3 external register)")
print(f"  EXTERNAL: BST predicts measurable bottleneck transitions in multi-agent")
print(f"  parallel-task efficiency at N ∈ BST-primary set")
print(f"  ")
bst_primaries = [N_c, n_C, C_2, g, c_2, c_3, seesaw, chi, N_max]
print(f"  BST primary integers to test: {bst_primaries}")
print(f"  ")
print(f"  Null hypothesis: efficiency drops smoothly with N (no special integers)")
print(f"  BST hypothesis: efficiency shows kinks/transitions at primary N values")
check(f"BST primary set spans 9 integers from 3 to 137", len(bst_primaries) == 9)

# === T2: Experimental design ===
print(f"\n[T2] Experimental design")
design = {
    'task_type': 'distributed information-processing task (e.g., consensus protocol, parallel theorem solving, distributed optimization)',
    'agents': 'multi-CI coordination experiment OR distributed-compute cluster',
    'measurement': 'task-completion-time T(N) as function of N concurrent agents',
    'efficiency_metric': 'parallel efficiency η(N) = T(1) / (N · T(N))',
    'expected_baseline': 'η decreases with N due to coordination overhead (Amdahl-like)',
    'expected_BST_signature': 'η(N) shows local minima or kinks at N ∈ {3, 5, 6, 7, 11, 13, 17, 24}',
    'sweep_range': 'N = 1 to 200 (covers all 9 BST primaries plus boundary)',
    'replication': 'at least 20 independent task instances per N value',
    'precision_target': 'σ(η)/η < 1% per data point',
}
print(f"  Task type: {design['task_type']}")
print(f"  Agents: {design['agents']}")
print(f"  Measurement: {design['measurement']}")
print(f"  Sweep range: {design['sweep_range']}")
print(f"  Replication: {design['replication']}")

# === T3: Discrimination protocol ===
print(f"\n[T3] BST vs null discrimination protocol")
print(f"  Pre-register two hypotheses BEFORE data collection:")
print(f"  ")
print(f"  H_null: η(N) is smooth in N (modeled as Amdahl law or similar)")
print(f"    Statistical test: fit smooth model, compute residuals σ_res")
print(f"  ")
print(f"  H_BST: η(N) has measurable deviations at N ∈ {{N_c, n_C, C_2, g, c_2, c_3, seesaw, chi}}")
print(f"    Statistical test: deviation Δη(N_BST) > 3σ_res at ≥4 of 8 BST primaries")
print(f"    Note: 4 of 8 ≥3σ corresponds to ~0.04% combined false-positive under null")
print(f"  ")
print(f"  Discrimination: |Z_at_BST_primaries| > 3 favors H_BST; uniform residuals favor H_null")
check(f"Pre-registered discrimination protocol specified (≥4 of 8 BST primaries at 3σ)",
      True)

# === T4: Apparatus / experimental setup ===
print(f"\n[T4] Apparatus / experimental setup")
print(f"  Option A: Multi-CI coordination test (cheapest)")
print(f"    - N independent CIs given identical task")
print(f"    - Coordination protocol: shared whiteboard / message-passing")
print(f"    - Measure: time-to-consensus or task-completion-time")
print(f"    - Cost: minimal (existing CI infrastructure)")
print(f"    - Timeline: 1-3 months")
print(f"  ")
print(f"  Option B: Distributed-compute cluster benchmark")
print(f"    - Use standard parallel computing benchmark (e.g., LINPACK, NPB)")
print(f"    - Run with N processes varying through BST primaries + nearby")
print(f"    - Measure: scaling efficiency η(N)")
print(f"    - Cost: cluster time (~$5-15K for sufficient statistics)")
print(f"    - Timeline: 3-6 months")
print(f"  ")
print(f"  Option C: Human team coordination benchmark")
print(f"    - Brooks-law-like measurements on software development teams")
print(f"    - N developers on standardized task")
print(f"    - Cost: high (~$100K+); industrial collaboration needed")
print(f"    - Timeline: 6-12 months")
print(f"  ")
print(f"  Recommended: Option B first (clean apparatus, moderate cost)")

# === T5: Falsifier specification ===
print(f"\n[T5] Falsifier specification (per Cal Flag 1 register)")
print(f"  CONFIRMS OCP-5: efficiency η(N) shows ≥4 of 8 BST-primary kinks at 3σ")
print(f"  REFUTES OCP-5: η(N) smooth in N with no BST-primary signature")
print(f"  ")
print(f"  Cal Mode 1 vigilance: don't run experiment and post-hoc identify which")
print(f"  N values look like BST primaries. Pre-register BST primary set BEFORE")
print(f"  data collection.")
check(f"Falsifier pre-registered with BST primary set specified", True)

# === T6: Cross-link to OCP-1 + Letter ===
print(f"\n[T6] Cross-link to other afternoon work")
print(f"  Letter (Letter_Bell_Substrate_CHSH_Draft.md): Bell experiment outreach")
print(f"  OCP-1 (Toy 3182): Vienna-class Bell apparatus $500K specification")
print(f"  OCP-5 (THIS): parallelism bottleneck design $5-15K Option B")
print(f"  Session 19 (Toy 3183): H_sub_emit theoretical foundation")
print(f"  Session 20 (Toy 3186): Bergman projection explicit construction")
print(f"  ")
print(f"  Two parallel substrate tests at very different scales:")
print(f"  - Quantum (Bell, sub-percent precision, $500K)")
print(f"  - Classical (parallelism bottleneck, ~1% efficiency, $5-15K)")
print(f"  ")
print(f"  Both test substrate signature at observable level; different physical")
print(f"  systems, same BST-primary integer-web structure.")
print(f"  ")
print(f"  Combined SP-30 program now ~$640-900K (Bell + eigentone + Casimir + Cs-137)")
print(f"  + ~$5-15K (OCP-5 parallelism) = inexpensive expansion of test program.")

# === Output ===
out_path = os.path.join(SCRIPT_DIR, "toy_3187_OCP5_parallelism.json")
out = {
    'meta': {'date': '2026-05-20', 'owner': 'Elie', 'task': 'OCP-5 parallelism bottleneck design'},
    'cal_49_tier': 'GREEN',
    'cal_flag_3_register': 'external operational language only',
    'bst_primaries_tested': bst_primaries,
    'design': design,
    'apparatus_options': {
        'A_multi_CI': 'minimal cost, 1-3 months',
        'B_distributed_compute': '$5-15K, 3-6 months',
        'C_human_team': '$100K+, 6-12 months',
    },
    'recommended': 'Option B first (clean apparatus, moderate cost)',
    'discrimination': 'pre-registered ≥4 of 8 BST primaries at 3σ',
    'cross_link_OCP1': 'parallel test at classical scale; Bell at quantum scale',
}
with open(out_path, 'w') as f: json.dump(out, f, indent=2)
print(f"\n[OUTPUT] {os.path.basename(out_path)}")

passed = sum(1 for ok, _ in tests if ok)
total = len(tests)
print(f"\n{'='*72}\nToy 3187 SCORE: {passed}/{total}\n{'='*72}")
for ok, label in tests:
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
