#!/usr/bin/env python3
"""Small live-research validator; historical portfolio checks deliberately retired."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    files = [
        "AGENTS.md", "README.md", "authoritative/START_HERE.md",
        "authoritative/STATE.json", "research/VERSION_BRIDGE.md",
        "research/SOURCE_REGISTER.md", "research/WORKING_PROOF.md",
        "sessions/NEXT_SESSION.md", "scripts/shift_sanity.py",
        "scripts/bridge_audit.py", "tests/test_bridge_audit.py",
        "research/SPOKE_SHIFT_THEOREM.md", "scripts/spoke_shift_audit.py",
        "tests/test_spoke_shift_audit.py",
        "research/DENSE_ANCESTOR_OBSTRUCTION.md",
        "scripts/dense_obstruction_audit.py", "tests/test_dense_obstruction_audit.py",
        "research/HIGH_RANK_DENSE_TENSOR_OBSTRUCTION.md",
        "scripts/high_rank_tensor_audit.py", "tests/test_high_rank_tensor_audit.py",
        "research/SIX_PETAL_INTERSECTING_TENSOR_OBSTRUCTION.md",
        "scripts/six_petal_factor_audit.py", "tests/test_six_petal_factor_audit.py",
        "research/TRIANGLE_TENSOR_PREVALENCE_OBSTRUCTION.md",
        "scripts/triangle_tensor_prevalence_audit.py", "tests/test_triangle_tensor_prevalence_audit.py",
        "research/ORIGINAL_MULTIWITNESS_TRACE_RANK_REDUCTION.md",
        "scripts/compatible_trace_audit.py", "tests/test_compatible_trace_audit.py",
    ]
    for name in files:
        assert (ROOT / name).is_file(), name
    state = json.loads((ROOT / "authoritative/STATE.json").read_text())
    assert state["schema"] == 2
    assert state["repository"] == "jfairfaxball-348/sunflower-structures-programme"
    assert state["mode"] == "SINGLE_REPOSITORY_DIRECT_MATHEMATICAL_RESEARCH"
    assert state["focus"] == "MISHRA_ARXIV_2606_02667_V1_V2_GAP"
    assert not state["full_conjecture_proved"]
    assert not state["legacy_hierarchy_active"]
    assert not state["legacy_hard_stop_active"]
    assert state["active_next_prompt"] == "sessions/NEXT_SESSION.md"
    assert "SHIFTED_SUBFAMILY_OF_PRODUCT_AT_MOST_Q" in state["verified_results"]
    assert "SPOKE_TO_STAR_LEX_SHIFT_THEOREM_ALL_Q_K" in state["verified_results"]
    assert "DENSE_TENSOR_LEX_SHIFT_LINEAR_STAR_ALL_S" in state["verified_results"]
    assert "ANCHORED_HIGH_RANK_FACTOR_TENSOR_SHIFT_LEMMA" in state["verified_results"]
    assert "RANK_FOUR_54_FACTOR_SHADOW_INCIDENCE_SATURATION" in state["verified_results"]
    assert "SIX_PETAL_NINE_SWAP_SHIFT_OBSTRUCTION" in state["verified_results"]
    assert "INTERSECTING_ORIGINAL_EXTRACTION_FACTOR_QK" in state["verified_results"]
    assert "ORIGINAL_INTERSECTING_MULTIWITNESS_EXACT_TRACE_RANK_REDUCTION" in state["verified_results"]
    for v in ("v1", "v2"):
        assert f"2606.02667{v}" in state["source_versions"][v]
    handoff = (ROOT / state["active_next_prompt"]).read_text()
    assert "NEXT DIRECT RESEARCH INVESTIGATION" in handoff
    assert "full Erdős" in handoff
    assert "C_s" in handoff
    assert "NO S011" not in handoff
    assert "full-shift" in handoff.lower()
    assert "original" in handoff.lower()
    assert "P(s-1,k)" in handoff
    bridge = (ROOT / "research/VERSION_BRIDGE.md").read_text().lower()
    assert "false" in bridge and "rank-dependent" in bridge
    assert "source" in (ROOT / "research/SOURCE_REGISTER.md").read_text().lower()
    from shift_sanity import main as check_examples
    from bridge_audit import main as check_bridge
    from spoke_shift_audit import main as check_spoke
    from dense_obstruction_audit import main as check_dense
    from high_rank_tensor_audit import main as check_high_rank
    from six_petal_factor_audit import main as check_six_petal
    check_examples()
    check_bridge()
    check_spoke()
    check_dense()
    check_high_rank()
    check_six_petal()
    from triangle_tensor_prevalence_audit import main as check_triangle_tensor
    check_triangle_tensor()
    from compatible_trace_audit import main as check_compatible_trace
    check_compatible_trace()
    print("PASS: active research state, audited source bridge and direct next prompt")


if __name__ == "__main__":
    main()
