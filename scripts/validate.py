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
        "research/CENTRAL_TRACE_AMORTISATION.md",
        "scripts/central_trace_amortisation_audit.py",
        "tests/test_central_trace_amortisation_audit.py",
        "scripts/compatible_trace_audit.py", "tests/test_compatible_trace_audit.py",
        "research/PARTIAL_MULTIPLICITY_DUAL.md",
        "scripts/partial_multiplicity_audit.py",
        "tests/test_partial_multiplicity_audit.py",
        "research/CORRELATED_PARTITE_ORIGINAL_DEFECTS.md",
        "research/ORIGINAL_PAIR_BUDGET_AND_TENSOR_ENTROPY.md",
        "scripts/original_pair_budget_audit.py",
        "tests/test_original_pair_budget_audit.py",
        "scripts/correlated_partite_audit.py",
        "research/ORIGINAL_PACKET_KRAFT_AND_ENTROPY.md",
        "scripts/original_packet_entropy_audit.py",
        "research/CROSS_TRACE_TENSOR_SHIELD_AND_VC_BARRIER.md",
        "scripts/cross_trace_shield_audit.py",
        "tests/test_cross_trace_shield_audit.py",
        "research/ALTERNATING_SHIELD_RECTANGLE_DUAL.md",
        "scripts/alternating_shield_audit.py",
        "tests/test_alternating_shield_audit.py",
        "tests/test_original_packet_entropy_audit.py",
        "tests/test_correlated_partite_audit.py",
        "research/GLOBAL_MULTISHIELD_ORIGINAL_OWNERSHIP.md",
        "scripts/global_shield_audit.py",
        "tests/test_global_shield_audit.py",
        "research/NONPRODUCT_ORIGINAL_TENSOR_CORRELATION.md",
        "scripts/original_nonproduct_tensor_lp_audit.py",
        "tests/test_original_nonproduct_tensor_lp_audit.py",
        "research/OPTIMAL_ORIGINAL_OWNER_BALANCING.md",
        "research/ORIGINAL_PAIR_STAR_QUADRATIC_LP_OBSTRUCTION.md",
        "scripts/original_pair_star_quadratic_audit.py",
        "tests/test_original_pair_star_quadratic_audit.py",
        "scripts/original_owner_balancing_audit.py",
        "tests/test_original_owner_balancing_audit.py",
        "research/HETEROGENEOUS_PRODUCT_DENSITY_DUAL.md",
        "scripts/heterogeneous_product_dual_audit.py",
        "tests/test_heterogeneous_product_dual_audit.py",
        "research/FRACTIONAL_ORIGINAL_LINK_RIGIDITY.md",
        "scripts/fractional_link_lp_audit.py",
        "tests/test_fractional_link_lp_audit.py",
        "research/NONVACUOUS_WREATH_POINT_LINK_OBSTRUCTION.md",
        "scripts/original_wreath_density_audit.py",
        "tests/test_original_wreath_density_audit.py",
        "research/EXACT_WREATH_PACKET_KRAFT_OBSTRUCTION.md",
        "scripts/original_wreath_packet_budget_audit.py",
        "tests/test_original_wreath_packet_budget_audit.py",
        "research/NESTED_ORIGINAL_WREATH_PACKET_RECURSION.md",
        "scripts/nested_original_wreath_audit.py",
        "tests/test_nested_original_wreath_audit.py",
        "research/ALL_PHYSICAL_WREATH_COMPATIBILITY.md",
        "scripts/all_physical_wreath_compatibility_audit.py",
        "tests/test_all_physical_wreath_compatibility_audit.py",
        "research/PHYSICAL_CORE_TURAN_HIGH_DENSITY_SHARPNESS.md",
        "scripts/physical_core_turan_sharpness_audit.py",
        "tests/test_physical_core_turan_sharpness_audit.py",
        "research/COUPLED_CROSS_CORE_NEAR_TURAN_OBSTRUCTION.md",
        "scripts/coupled_cross_core_audit.py",
        "tests/test_coupled_cross_core_audit.py",
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
    assert "ALL_S_ALTERNATING_SHIELD_SEED" in state["verified_results"]
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
    assert "shift" in handoff.lower()
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
    from central_trace_amortisation_audit import main as check_central_trace
    check_central_trace()
    from compatible_trace_audit import main as check_compatible_trace
    check_compatible_trace()
    from partial_multiplicity_audit import main as check_partial
    from correlated_partite_audit import main as check_partite
    check_partial()
    check_partite()
    from original_pair_budget_audit import main as check_original_pair_budget
    check_original_pair_budget()
    from original_packet_entropy_audit import main as check_original_packet_entropy
    check_original_packet_entropy()
    from cross_trace_shield_audit import main as check_cross_trace_shield
    check_cross_trace_shield()
    from alternating_shield_audit import main as check_alternating_shield
    check_alternating_shield()
    from global_shield_audit import main as check_global_shield
    check_global_shield()
    from heterogeneous_product_dual_audit import main as check_heterogeneous
    check_heterogeneous()
    assert "HETEROGENEOUS_ORIGINAL_PRODUCT_GLOBAL_MULTISHIELD_LP_EXACT" in state["verified_results"]
    assert "GLOBAL_QARY_PRODUCT_EXACT_EQUAL_TRACE_FRACTIONAL_LP" in state["verified_results"]
    from original_nonproduct_tensor_lp_audit import audit as check_nonproduct
    check_nonproduct()
    assert "AS3_Q9_STRICT_TENSOR_SYNERGY_V8_V3_PLUS_V3" in state["verified_results"]
    from original_owner_balancing_audit import audit as check_balanced_owner
    check_balanced_owner()
    assert "AS3_Q9_EXACT_58_TERM_BALANCED_OPTIMAL_DUAL" in state["verified_results"]
    assert "BALANCED_ORIGINAL_DUAL_TENSOR_LIFT_ALL_M" in state["verified_results"]
    from original_pair_star_quadratic_audit import audit as check_pair_star
    check_pair_star()
    assert "ORIGINAL_PAIR_STAR_ALL_ANCHOR_QUADRATIC_OPTIMAL_LP" in state["verified_results"]
    assert "BALANCED_QUADRATIC_ORIGINAL_LP_NO_FIXED_POINT_LINK" in state["confirmed_obstructions"]
    assert "FRACTIONAL_ORIGINAL_LINK_MINIMAX_DUAL" in state["verified_results"]
    assert "ORIGINAL_FACTOR_TENSOR_CORRELATED_LINK_RIGIDITY" in state["verified_results"]
    from fractional_link_lp_audit import audit as check_fractional_link
    check_fractional_link()
    from original_wreath_density_audit import audit as check_wreath
    check_wreath()
    assert "ALL_NONVACUOUS_HIGH_DENSITY_POINT_LINK_COLLAPSE_FALSE" in state["verified_results"]
    assert "ALL_NONVACUOUS_BOUNDED_FRACTIONAL_MATCHING_COLLAPSE_FALSE" in state["confirmed_obstructions"]
    assert "ORIGINAL_WREATH_EXACT_BOUNDED_ANCHOR_PACKET_KRAFT_OPTIMUM" in state["verified_results"]
    assert "NO_FIXED_RANK_CAP_ORIGINAL_PACKET_KRAFT_AT_ANY_NONVACUOUS_DENSITY" in state["confirmed_obstructions"]
    from original_wreath_packet_budget_audit import audit as check_packet_budget
    check_packet_budget()
    from nested_original_wreath_audit import audit as check_nested_wreath
    check_nested_wreath()
    from all_physical_wreath_compatibility_audit import audit as check_all_physical
    check_all_physical()
    assert "ALL_PHYSICAL_NESTED_QPRODUCT_KRAFT_RECURSION" in state["verified_results"]
    assert "ALL_PHYSICAL_BASE_TWO_KRAFT_BUDGET_DOES_NOT_CONTROL_RESIDUAL_CAPACITY" in state["confirmed_obstructions"]
    assert "NESTED_ORIGINAL_WREATH_EXACT_SHELL_KRAFT_RECURSION" in state["verified_results"]
    assert "KRAFT_BUDGET_ALONE_NOT_FIXED_BASE_ORIGINAL_INDUCTION" in state["confirmed_obstructions"]
    from physical_core_turan_sharpness_audit import audit as check_physical_turan
    check_physical_turan()
    assert "NONVACUOUS_HIGH_DENSITY_TURAN_SHARPNESS" in state["verified_results"]
    assert "NO_STRICT_MULTI_PACKET_TURAN_BONUS_AT_NONVACUOUS_DENSITY" in state["confirmed_obstructions"]
    from coupled_cross_core_audit import audit as check_coupled_cross_core
    check_coupled_cross_core()
    assert "COUPLED_ORIGINAL_CROSS_CORE_MODAL_CONCENTRATION" in state["verified_results"]
    assert "NEAR_TURAN_NO_NEAR_TOTAL_EXACT_ORIGINAL_OWNER_PURIFICATION" in state["confirmed_obstructions"]
    print("PASS: coupled physical-core audit, full predecessors, source bridge and next prompt")


if __name__ == "__main__":
    main()
