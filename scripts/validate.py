#!/usr/bin/env python3
import json
import re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def txt(p): return (ROOT/p).read_text(encoding="utf8")
def check_registration(state, projects, receipt):
    assert state["repo"] == projects["parent"] == receipt["parent"]["repository"] == "jfairfaxball-348/sunflower-structures-programme"
    assert state["repository_id"] == receipt["parent"]["repository_id"] == 1412469441
    assert state["session_completed"] == "S000" and state["next_programme_session"] == "S001"
    assert state["headline_id"] == "SUN" and state["champion"] == "Erdős–Rado Sunflower Conjecture"
    assert state["active_paper_id"] == projects["active_project"] == receipt["project_id"] == "P001"
    assert state["child_repo_created"] and state["first_paper_authorized"]
    assert not state["parent_repo_name_temporary"]
    assert len(projects["projects"]) == 1 and projects["planned"] == []
    project = projects["projects"][0]
    child = receipt["child"]
    assert project["repository_id"] == child["repository_id"] == 1412820282
    assert child["repository"] == "jfairfaxball-348/sunflower-internal-kernel-extraction"
    assert project["url"] == child["url"] == "https://github.com/" + child["repository"]
    sha = child["main_commit"]
    assert re.fullmatch(r"[0-9a-f]{40}", sha)
    assert project["verified_commit"] == sha == child["merged_pr"]["merge_sha"]
    assert child["merged_pr"]["merged"] and child["merged_pr"]["merged_at"]
    run = child["main_validation"]
    assert run["head_sha"] == sha and run["event"] == "push"
    assert run["status"] == "completed" and run["conclusion"] == "success"
    assert run["jobs"] and any(j["name"] == "validate" for j in run["jobs"])
    for job in run["jobs"]:
        assert job["id"] > 0 and job["status"] == "completed" and job["conclusion"] == "success"
        assert job["steps"] and all(s["conclusion"] == "success" for s in job["steps"])
    audit = receipt["independent_registration_verification"]
    for field in ("open_status", "novelty_status", "formal_status", "publication_status"):
        assert project[field] == audit[field]
    assert audit["open_status"] == "STRONG_EVIDENCE_OPEN"
    assert audit["novelty_status"] == "NOVELTY_UNCERTAIN"
    assert audit["formal_status"] == "NOT_STARTED" and audit["publication_status"] == "IDEA"
    assert state["mathematical_result_count"] == audit["new_theorems"] == 0
    assert state["formal_verifications"] == audit["formal_verifications"] == 0
    assert state["publications"] == audit["publications"] == 0
    next_step = receipt["next_child_obligation"]
    expected_successors = {"P001-S000": ("P001-S001", ["R3"]),
                           "P001-S001": ("P001-S002", ["L_AVG"]),
                           "P001-S002": ("P001-S003", ["L_AVG_HEAVY_LINK_CHARGING"]),
                           "P001-S003": ("P001-S004", ["L_AVG_COUNTEREXAMPLE_INDEPENDENT_AUDIT"]),
                           "P001-S004": ("P001-S005", ["FIVE_SESSION_PROGRESS_CORRECTION_AND_ROUTE_TRIAGE"]),
                           "P001-S005": ("P001-S006", ["HUMAN_PROGRAMME_DECISION_REQUIRED"])}
    expected_successors["P001-S006"] = ("P001-S007", ["HUMAN_BLOCK_COMPATIBILITY_DECISION_GATE"])
    expected_successors["P001-S007"] = ("P001-S008", ["HIGH_LOAD_VERTEX_RESERVOIR_COMPATIBILITY"])
    expected_successors["P001-S008"] = ("P001-S009", ["TWO_HUB_MULTIPLICITY_SLICE"])
    expected_successors["P001-S009"] = ("P001-S010", ["PRIVATE_LIGHT_MULTIHUB_COMPATIBILITY_AND_TENTH_AUDIT"])
    expected_successors["P001-S010"] = ("P001-S011", ["EXACT_PRIVATE_LIGHT_SINGLETON_LINK_MATCHING_CERTIFICATE"])
    expected_successors["P001-S011"] = ("P001-S012", ["DENSITY_PRESERVING_EXACT_HUB_FOOTPRINT_SELECTION"])
    expected_successors["P001-S012"] = ("P001-S013", ["PAIR_ROBUST_SINGLETON_EMPTY_SELECTION"])
    expected_successors["P001-S013"] = ("P001-S014", ["UNPROTECTED_HUB_JOINT_PAIR_CLASS_SELECTION"])
    expected_successors["P001-S014"] = ("P001-S015", ["QUANTITATIVE_PRESERVE_OR_DROP_PAIR_CLASS_REFINEMENT"])
    expected_successors["P001-S015"] = ("P001-S016", ["JOINT_WEIGHTED_CHANNEL_AND_CORE_MATCHING_SELECTION"])
    expected_successors["P001-S016"] = ("P001-S017", ["ADAPTIVE_WEIGHTED_CORE_FOOTPRINT_AND_TRUE_CHANNEL_JOINT_SELECTION"])
    expected_successors["P001-S017"] = ("P001-S018", ["CONTAMINATED_HEAVY_CHANNEL_COMPLEMENT_JOINT_SELECTION"])
    expected_successors["P001-S018"] = ("P001-S019", ["PAIR_ACTIVE_WEIGHTED_JOINT_CHANNEL_AND_FOOTPRINT"])
    expected_successors["P001-S019"] = ("P001-S020", ["FIFTH_AUDIT_AND_SHORT_MIXED_CHANNEL_BRIDGE"])
    expected_successors["P001-S020"] = ("P001-S021", ["SHORT_PAIR_CLASS_M_SAVING_BRIDGE"])
    expected_successors["P001-S021"] = ("P001-S022", ["NONPRIVATE_LIGHT_OVERLAP_LIFT"])
    expected_successors["P001-S022"] = ("P001-S023", ["LIGHT_AWARE_JOINT_SHORT_CHANNEL_SELECTION"])
    expected_successors["P001-S023"] = ("P001-S024", ["DIRECT_PARTIAL_EDGE_R3_EXTRACTION"])
    expected_successors["P001-S024"] = ("P001-S025", ["MANDATORY_FIFTH_CORRECTION_AUDIT_AND_EDGE_LEVEL_GLOBAL_BRIDGE"])
    expected_successors["P001-S025"] = ("P001-S026", ["NONPRIVATE_MIXED_SUPPORT_EDGE_REFINEMENT"])
    if receipt.get("registration_kind") == "P001_S006_APPROVAL_ONLY":
        # Last substantive session remains S005; administrative approval changes its sole unexecuted successor.
        assert receipt["session"] == "P001-S005"
        expected_successors["P001-S005"] = ("P001-S006", ["BLOCK_COMPATIBILITY_FEASIBILITY_GATE"])
        approved = receipt["approved_next_child_handoff"]
        assert approved["session"] == "P001-S006" and approved["approved"] is True and approved["executed"] is False
        assert approved["child_main_commit"] == child["main_commit"]
        assert approved["method"] == "SUNFLOWER_BLOCK_COMPATIBILITY"
        assert approved["source_first_N1_performed"] is False and approved["mathematical_proof_performed"] is False
        assert audit["owner_decision_resolved_after_s005"] is True
        assert audit["new_mathematical_session_executed"] is False
        assert (ROOT / "sessions/P001-S006/APPROVAL_REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S006":
        assert receipt["registration_kind"] == "P001_S006_SUBSTANTIVE_RESTRICTED_ONLY"
        assert receipt["independent_registration_verification"]["session_outcome"] == "RESTRICTED_BSEL_ONLY"
        assert receipt["independent_registration_verification"]["bsel_universal_proved"] is False
        assert receipt["independent_registration_verification"]["independent_mathematical_review"] is False
        assert (ROOT / "sessions/P001-S006/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S007":
        assert receipt["registration_kind"] == "P001_S007_PROOF_FIRST_RESTRICTED_LOW_LOAD"
        assert audit["session_outcome"] == "RESTRICTED_LOW_LOAD_BSEL_PROVED_NO_FULL_EXTRACTION"
        assert audit["bsel_universal_proved"] is False and audit["independent_mathematical_review"] is False
        assert audit["owner_policy"] == "PROOF_FIRST_TECHNICAL_METHOD_SELECTION_AUTONOMOUS_AND_PRIOR_ART_DEFERRED_UNTIL_COMPLETE_TIK_PROOF"
        assert project["last_child_session"] == "P001-S007"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S007/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S008":
        assert receipt["registration_kind"] == "P001_S008_PROOF_FIRST_SINGLE_HUB_RESERVOIR_NEGATIVE"
        assert audit["session_outcome"] == "SINGLE_HUB_HIGH_LOAD_RESERVOIR_REFUTED_BSEL_OPEN"
        assert audit["single_hub_reservoir_refuted"] is True
        assert audit["single_hub_counterexample_full_union_valid"] is True
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["independent_mathematical_review"] is False
        assert audit["R3_TIK_refuted"] is False
        assert project["last_child_session"] == "P001-S008"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S008/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S009":
        assert receipt["registration_kind"] == "P001_S009_TWO_HEAVY_THIN_Q_NEGATIVE_STATUS_ONLY"
        assert audit["session_outcome"] == "TWO_HEAVY_LOW_LOAD_THINNING_REFUTED_BSEL_OPEN"
        assert audit["two_heavy_thin_q_refuted"] is True
        assert audit["two_heavy_counterexample_full_union_valid"] is True
        assert audit["two_heavy_bsel_proved"] is False and audit["two_heavy_bsel_refuted"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["independent_mathematical_review"] is False and audit["R3_TIK_refuted"] is False
        assert project["last_child_session"] == "P001-S009"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S009/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S010":
        assert receipt["registration_kind"] == "P001_S010_PRIVATE_LIGHT_SAT_CROSS_NEGATIVE_TENTH_AUDIT_STATUS_ONLY"
        assert audit["session_outcome"] == "PRIVATE_LIGHT_CROSS_HUB_CLOSURE_REFUTED_BSEL_OPEN_TENTH_AUDIT"
        assert audit["private_light_sat_cross_refuted"] and audit["private_light_control_valid_over_half"]
        assert audit["tenth_audit_completed"] and audit["s005_rechecked"]
        assert not audit["private_light_two_heavy_bsel_proved"] and not audit["private_light_two_heavy_bsel_refuted"]
        assert not audit["full_tik_proved"] and not audit["R3_TIK_refuted"]
        assert not audit["independent_mathematical_review"]
        assert project["last_child_session"] == "P001-S010"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S010/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S011":
        assert receipt["registration_kind"] == "P001_S011_EXACT_LINK_CORE_CERTIFICATES_LOCAL_TO_GLOBAL_NEGATIVE_STATUS_ONLY"
        assert audit["session_outcome"] == "EXACT_LINK_CORE_CERTIFICATE_LOCAL_TO_EMPTY_LEMMA_REFUTED_DENSITY_OPEN"
        assert audit["exact_residual_matching_formula_proved_same_assistant"] is True
        assert audit["exact_mandatory_core_empty_matching_identity_same_assistant"] is True
        assert audit["local_to_empty_certification_lemma_refuted"] is True
        assert audit["two_star_positive_half_density_control"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["full_tik_proved"] is False and audit["R3_TIK_refuted"] is False
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["private_light_two_heavy_bsel_refuted"] is False
        assert project["last_child_session"] == "P001-S011"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S011/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S012":
        assert receipt["registration_kind"] == "P001_S012_PAIR_ONLY_QUANTITATIVE_SUBLEMMA_STATUS_ONLY"
        assert audit["session_outcome"] == "PAIR_FILTER_AT_LEAST_T_OVER_M_MINUS_ONE_ONLY_JOINT_DENSITY_OPEN"
        assert audit["pair_only_quantitative_lemma_same_assistant"] is True
        assert audit["pair_filter_is_not_joint_bsel"] is True
        assert audit["s012_joint_certificates_proved"] is False
        assert audit["independent_mathematical_review"] is False
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S012"
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S012/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S013":
        assert receipt["registration_kind"] == "P001_S013_RESTRICTED_PROTECTED_A0_JOINT_CERTIFICATE_STATUS_ONLY"
        assert audit["session_outcome"] == "A0_PROTECTED_JOINT_REFINE_GAMMA_ONE_GENERAL_UNPROVED"
        assert audit["protected_A0_requires_extra_assumptions"] is True
        assert audit["protected_A0_bound"] == "t/(m-1) >= t/m^3"
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["bsel_universal_proved"] is False and audit["full_tik_proved"] is False
        assert audit["independent_mathematical_review"] is False
        assert project["last_child_session"] == "P001-S013"
        assert child["final_head_validation"] and all(
            x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success"
            for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S013/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S014":
        assert receipt["registration_kind"] == "P001_S014_UNPROTECTED_SATURATED_CLASS_REPAIR_NEGATIVE_SHARP_HALF_CONTROL_STATUS_ONLY"
        assert audit["session_outcome"] == "NSCR_FALSE_SHARP_HALF_DENSITY_POSITIVE_CONTROL"
        assert audit["unprotected_all_class_repair_refuted"] is True
        assert audit["unprotected_cycle_positive_over_half"] is True
        assert audit["all_three_block_core_sizes"] is True
        assert audit["s013_protected_theorem_unchanged"] is True
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["private_light_two_heavy_bsel_refuted"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False and audit["independent_mathematical_review"] is False
        assert project["last_child_session"] == "P001-S014"
        assert child["final_head_validation"] and all(
            x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success"
            for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S014/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S015":
        assert receipt["registration_kind"] == "P001_S015_SINGLETON_ANCHORED_ALL_CLASS_EMPTY_OBSTRUCTION_DENSE_STAR_FIFTEENTH_AUDIT_STATUS_ONLY"
        assert audit["session_outcome"] == "SAKAC_FALSE_STAR_DENSITY_POSITIVE_FIFTEENTH_AUDIT"
        assert audit["singleton_anchored_keep_all_class_refuted"] is True
        assert audit["s015_star_positive_at_least_t_over_m_minus_one"] is True
        assert audit["fifteenth_audit_completed"] is True
        assert audit["s014_obstruction_and_s013_protected_retained"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["private_light_two_heavy_bsel_refuted"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S015"
        assert child["final_head_validation"] and all(
            x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success"
            and x["jobs"] and all(j["conclusion"] == "success" for j in x["jobs"])
            for x in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S015/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S016":
        assert receipt["registration_kind"] == "P001_S016_FIXED_BACKBONE_WEIGHTED_BUDGET_NEGATIVE_DENSE_CONTROL_STATUS_ONLY"
        assert audit["session_outcome"] == "FIXED_BACKBONE_BUDGET_FALSE_DENSE_ADAPTIVE_HALF_CONTROL"
        assert audit["s016_fixed_backbone_budget_refuted"] is True
        assert audit["s016_dense_valid_half_control"] is True
        assert audit["s016_short_unsaturated_class_accounted"] is True
        assert audit["s016_arbitrary_core_backbone_not_guaranteed"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["private_light_two_heavy_bsel_proved"] is False and audit["private_light_two_heavy_bsel_refuted"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S016"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S016/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S017":
        assert receipt["registration_kind"] == "P001_S017_ADAPTIVE_WEIGHTED_SAFE_SPINE_PARTIAL_JOINT_BOUND_STATUS_ONLY"
        assert audit["session_outcome"] == "SAFE_SPINE_12_PARTIAL_W_PLUS_Z_NO_UNIFORM_T_BOUND"
        assert audit["s017_safe_spine_12_partial_proved_same_assistant"] is True
        assert audit["s017_safe_spine_bound"] == "(W+Z)/(12*m^3)"
        assert audit["s017_original_heavy_fixed"] and audit["s017_actual_in_H_pair_singleton_empty_checked"]
        assert audit["s017_W_plus_Z_may_be_zero_unbounded_t"] is True
        assert audit["s017_complete_arbitrary_gamma_proved"] is False
        assert audit["independent_mathematical_review"] is False
        assert not audit["private_light_two_heavy_bsel_proved"] and not audit["private_light_two_heavy_bsel_refuted"]
        assert not audit["bsel_universal_proved"] and not audit["bsel_universal_refuted"]
        assert not audit["full_tik_proved"]
        assert project["last_child_session"] == "P001-S017"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S017/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S018":
        assert receipt["registration_kind"] == "P001_S018_A0_MAJORITY_24_CONDITIONAL_T_JOINT_BOUND_STATUS_ONLY"
        assert audit["session_outcome"] == "A0_MAJORITY_24_TRUE_ABSOLUTE_T_GAMMA_UNPROVED"
        assert audit["s018_a0_unconditional_lower_bound"] == "|A0|/[12*(m-1)^3]"
        assert audit["s018_a0_majority_t_bound"] == "t/(24*m^3)"
        assert audit["s018_full_all_k_tik_proved"] is False
        assert audit["s018_active_channel_incompatibility"] is True
        assert audit["s018_dense_valid_half_control"] is True
        assert audit["independent_mathematical_review"] is False
        assert not audit["private_light_two_heavy_bsel_proved"] and not audit["private_light_two_heavy_bsel_refuted"]
        assert not audit["bsel_universal_proved"] and not audit["bsel_universal_refuted"]
        assert not audit["full_tik_proved"]
        assert project["last_child_session"] == "P001-S018"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S018/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S019":
        assert receipt["registration_kind"] == "P001_S019_OPTIONAL_PAIR_ACTIVE_E00_RESTRICTED_JOINT_STATUS_ONLY"
        assert audit["session_outcome"] == "E00_PARTIAL_M4_SATURATED_M2_MIXED_STAR_EMPTY_FAILED_FULL_T_GAMMA_UNPROVED"
        assert audit["s019_pair_active_96_proved"] is False
        assert audit["s019_pair_active_e00_all_kernel_submass"] == "T00/[6*m*(m-1)^3]"
        assert audit["s019_pair_active_saturated_e00_all_kernel_submass"] == "T_sat/[6*(m-1)^2]"
        assert audit["s019_mixed_star_true_empty_matching"] == 3
        assert audit["s019_mixed_star_dense_valid_fraction"] == "m/(m+2) >= 2/3"
        assert audit["s019_original_Q_fixed"] is True
        assert audit["s020_mandatory_fifth_audit_unexecuted"] is True
        assert audit["independent_mathematical_review"] is False
        assert not audit["private_light_two_heavy_bsel_proved"] and not audit["private_light_two_heavy_bsel_refuted"]
        assert not audit["bsel_universal_proved"] and not audit["bsel_universal_refuted"]
        assert not audit["full_tik_proved"]
        assert project["last_child_session"] == "P001-S019"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S019/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S020":
        assert receipt["registration_kind"] == "P001_S020_DIRECTED_MIXED_PRIVATE_LIGHT_M4_FIFTH_AUDIT_STATUS_ONLY"
        assert audit["session_outcome"] == "PRIVATE_LIGHT_TWO_Q_T_OVER_48M4_PROVED_SAME_ASSISTANT_FULL_M3_UNPROVED"
        assert audit["s020_fifth_audit_completed"] is True
        assert audit["s020_mandatory_fifth_audit_unexecuted"] is False
        assert audit["s020_frozen_t_96_m3_proved"] is False
        assert audit["s020_mixed_directed_submass"] == "T_mixed/[24*(m-1)^4]"
        assert audit["s020_private_light_absolute_t_bound"] == "t/(48*m^4)"
        assert audit["s020_full_private_light_m3_gamma_proved"] is False
        assert audit["s020_full_all_k_tik_proved"] is False
        assert audit["s020_original_Q_fixed"] is True
        assert audit["s020_same_assistant_symbolic_only"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["s020_negative_controls_finite_m4_n5_checked"] is True
        assert audit["s020_local_full_project_tests_not_run"] is True
        assert audit["s021_future_only"] is True
        assert audit["s020_input_sha256"] == "dc49b17b4bd9ba309edd4bc1957359bcdbeb02dceb894e3b046ac62cfc8f1f38"
        assert audit["private_light_two_heavy_bsel_proved"] is False
        assert audit["private_light_two_heavy_bsel_refuted"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S020"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S020/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S021":
        assert receipt["registration_kind"] == "P001_S021_PRIVATE_LIGHT_FULL_M3_THREE_CHANNEL_STATUS_ONLY"
        assert audit["session_outcome"] == "PRIVATE_LIGHT_TWO_Q_FULL_T_OVER_126M3_PROVED_SAME_ASSISTANT_ALL_K_OPEN"
        assert audit["s021_frozen_t_200_m3_met"] is True
        assert audit["s021_short_graph_18_bound"] == "N/[18*(m-1)^2]"
        assert audit["s021_private_light_m3_bound"] == "t/[126*(m-1)^3]"
        assert audit["s021_same_assistant_symbolic_only"] is True
        assert audit["s021_independent_referee"] is False
        assert audit["s021_original_Q_fixed"] is True
        assert audit["s021_s018_s019_negative_controls_preserved"] is True
        assert audit["s021_input_sha256"] == "70d021f8a070967620869f0913e126aedf4c4aaafafc2bc16793a914a7b221e8"
        assert audit["s021_unrestricted_nonprivate_light_proved"] is False
        assert audit["s021_full_all_k_tik_proved"] is False
        assert audit["s022_future_only"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["private_light_two_heavy_bsel_proved"] is True
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S021"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S021/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S022":
        assert receipt["registration_kind"] == "P001_S022_NONPRIVATE_LIGHT_GATE_UNPROVED_STATUS_ONLY"
        assert audit["session_outcome"] == "GRAPH_ONLY_CONSTANT_REPAIR_FALSE_Q_EMPTY_M3_PROVED_S022_GATE_UNPROVED"
        assert audit["s022_frozen_nonprivate_t_1008_m3_proved"] is False
        assert audit["s022_graph_only_constant_repair_refuted"] is True
        assert audit["s022_q_empty_m3_bound"] == "t/[m*(3*m*(m-1)+1)] >= t/(3*m^3)"
        assert audit["s022_general_two_Q_nonprivate_fallback"] == "t/[126*(m-1)^3*(3*m*(m-1)+1)] >= t/(378*m^5)"
        assert audit["s022_projective_plane_light_pair_codegree"] == "m-1"
        assert audit["s022_full_gamma_or_tik_refuted"] is False
        assert audit["s022_original_Q_fixed"] is True
        assert audit["s022_light_pair_singleton_true_empty_tests"] is True
        assert audit["s023_future_only"] is True
        assert audit["s025_audit_future_only"] is True
        assert audit["s022_same_assistant_symbolic_only"] is True
        assert audit["independent_mathematical_review"] is False
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is False
        assert audit["full_tik_proved"] is False
        assert project["last_child_session"] == "P001-S022"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert (ROOT / "sessions/P001-S022/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S023":
        assert receipt["registration_kind"] == "P001_S023_BSEL_AUXILIARY_REFUTED_STATUS_ONLY"
        assert audit["session_outcome"] == "S023_FROZEN_NONPRIVATE_M3_AND_UNIVERSAL_BSEL_REFUTED_SAME_ASSISTANT_TIK_UNPROVED"
        assert audit["s023_frozen_nonprivate_t_1008_m3_refuted"] is True
        assert audit["s022_frozen_nonprivate_t_1008_m3_refuted"] is True
        assert audit["bsel_universal_proved"] is False and audit["bsel_universal_refuted"] is True
        assert audit["s023_three_tier_max_valid_whole_blocks"] == 1
        assert audit["s023_true_pair_singleton_empty_checked_symbolically"] is True
        assert audit["s023_same_family_valid_partial_edge_fraction"] == "1/[m*(m-1)]"
        assert audit["s023_original_Q_fixed"] is True
        assert audit["s023_same_assistant_symbolic_only"] is True
        assert audit["s024_future_only"] is True and audit["s025_audit_future_only"] is True
        assert audit["full_tik_proved"] is False and audit["independent_mathematical_review"] is False
        assert project["last_child_session"] == "P001-S023"
        assert project["bsel_universal_status"] == "REFUTED_PARAMETRIC_SAME_ASSISTANT_WHOLE_BLOCK_ONLY"
        assert child["final_head_validation"] and all(
            checked["head_sha"] == child["merged_pr"]["head_sha"] and checked["conclusion"] == "success"
            and checked["jobs"] and all(j["conclusion"] == "success" for j in checked["jobs"])
            for checked in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S023/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S024":
        assert receipt["registration_kind"] == "P001_S024_DIRECT_EDGE_GATE_UNPROVED_EXACT_OPTIMUM_STATUS_ONLY"
        assert audit["session_outcome"] == "S024_EXACT_EDGE_OPTIMUM_AND_LOCAL_UNION_FAILURE_DIRECT_M3_UNPROVED"
        assert audit["s024_frozen_direct_edge_512_proved"] is False
        assert audit["s024_frozen_direct_edge_512_refuted"] is False
        assert audit["s024_q_plane_exact_edge_optimum"] == "(m-1)*(m^2-2*m+2)"
        assert audit["s024_local_hub_union_refuted"] and audit["s024_star_forest_only_refuted"]
        assert audit["s025_audit_future_only"] and not audit["s024_future_only"]
        assert audit["bsel_universal_refuted"] and not audit["full_tik_proved"]
        assert not audit["independent_mathematical_review"]
        assert project["last_child_session"] == "P001-S024"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S024/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S025":
        assert receipt["registration_kind"] == "P001_S025_FIFTH_AUDIT_RESTRICTED_DIRECT_EDGE_M2_UNPROVED_GLOBAL_STATUS_ONLY"
        assert audit["session_outcome"] == "S025_RESTRICTED_EDGE_DENSITY_CONVERSION_GLOBAL_COLLISION_MASS_GAP_UNPROVED"
        assert audit["s025_fifth_audit_completed"] and not audit["s025_audit_future_only"]
        assert not audit["s025_global_edge_dichotomy_proved"] and not audit["s025_global_edge_dichotomy_refuted"]
        assert not audit["s025_direct_edge_512_proved"] and not audit["full_tik_proved"]
        assert audit["s025_private_light_direct_edge_count"] == "t/(126*m^2)"
        assert audit["s025_q_empty_direct_edge_count"] == "t/(3*m^2)"
        assert audit["s025_nonprivate_two_Q_fallback_edge_count"] == "t/(378*m^4)"
        assert audit["s025_same_assistant_symbolic_only"] and audit["s026_future_only"]
        assert audit["bsel_universal_refuted"] and not audit["independent_mathematical_review"]
        assert project["last_child_session"] == "P001-S025"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S025/REGISTRATION.md").is_file()
    expected_session, expected_objectives = expected_successors[receipt["session"]]
    assert next_step["session"] == expected_session and next_step["objectives"] == expected_objectives
    assert state["last_registry_update"] == receipt["session"]
    if receipt["session"] == "P001-S001":
        assert audit["session_outcome"] == "MECHANISM_OBSTRUCTION_AND_REMAINING_LEMMA"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN"
        assert project["last_child_session"] == "P001-S001"
        assert child["final_head_validation"]
        for checked in child["final_head_validation"]:
            assert checked["head_sha"] == child["merged_pr"]["head_sha"]
            assert checked["conclusion"] == "success" and checked["jobs"]
            assert all(j["conclusion"] == "success" for j in checked["jobs"])
    if receipt["session"] == "P001-S002":
        assert audit["session_outcome"] == "RESTRICTED_SUNFLOWER_FREE_BOUND_GENERAL_L_AVG_UNRESOLVED"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN"
        assert project["last_child_session"] == "P001-S002"
        assert len(child["final_head_validation"]) >= 1
        for checked in child["final_head_validation"][:1]:
            assert checked["head_sha"] == child["merged_pr"]["head_sha"]
            assert checked["conclusion"] == "success" and checked["jobs"]
            assert all(j["conclusion"] == "success" for j in checked["jobs"])
    if receipt["session"] == "P001-S003":
        assert audit["session_outcome"] == "NO_GENERAL_PROGRESS_L_AVG_REFUTED"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN"
        assert audit["auxiliary_L_AVG_status"] == "COUNTEREXAMPLE_ON_PAPER_INDEPENDENT_REVIEW_PENDING"
        assert not audit["R3_TIK_refuted"]
        assert project["last_child_session"] == "P001-S003"
        assert child["final_head_validation"]
        for checked in child["final_head_validation"]:
            assert checked["head_sha"] == child["merged_pr"]["head_sha"]
            assert checked["conclusion"] == "success" and checked["jobs"]
            assert all(j["conclusion"] == "success" for j in checked["jobs"])
    if receipt["session"] == "P001-S004":
        assert audit["session_outcome"] == "NO_GENERAL_R3_PROGRESS_L_AVG_B_CHARGE_RETIRED"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN"
        assert audit["auxiliary_L_AVG_status"] == "PROVISIONAL_ANALYTICALLY_SUPPORTED_COUNTEREXAMPLE_ROUTE_RETIRED"
        assert audit["heavy_link_B_CHARGE"] == "PROVISIONAL_ANALYTICALLY_SUPPORTED_COUNTEREXAMPLE_ROUTE_RETIRED"
        assert audit["independent_mathematical_review"] is False
        assert audit["R3_TIK_refuted"] is False
        assert project["last_child_session"] == "P001-S004"
        assert child["final_head_validation"]
        for checked in child["final_head_validation"]:
            assert checked["head_sha"] == child["merged_pr"]["head_sha"]
            assert checked["conclusion"] == "success" and checked["jobs"]
            assert all(j["conclusion"] == "success" for j in checked["jobs"])
    if receipt["session"] == "P001-S005":
        assert audit["session_outcome"] == "FIVE_SESSION_AUDIT_NO_APPROVED_SURVIVING_R3_ROUTE"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN"
        assert audit["human_decision_required"] is True
        assert audit["new_mathematical_candidate_promoted"] is False
        assert audit["independent_mathematical_review"] is False
        assert audit["R3_TIK_refuted"] is False
        assert project["last_child_session"] == "P001-S005"
        assert child["final_head_validation"]
        for checked in child["final_head_validation"]:
            assert checked["head_sha"] == child["merged_pr"]["head_sha"]
            assert checked["conclusion"] == "success" and checked["jobs"]
            assert all(j["conclusion"] == "success" for j in checked["jobs"])
    if receipt["session"] == "P001-S006":
        assert project["last_child_session"] == "P001-S006"
        assert audit["r3_literature_status"] == "STATUS_UNCERTAIN" and not audit["R3_TIK_refuted"]
        assert child["final_head_validation"] and all(x["head_sha"] == child["merged_pr"]["head_sha"] and x["conclusion"] == "success" for x in child["final_head_validation"])
    assert next_step["open_status"] == "STATUS_UNCERTAIN"
    assert not next_step["executed"] and not project["next_executed"]
    assert not receipt["parent_programme_session_executed"]
    for observed in receipt["parent_registration_ci"]:
        assert re.fullmatch(r"[0-9a-f]{40}", observed["head_sha"])
        assert observed["conclusion"] == "success" and observed["jobs"]
        assert all(j["conclusion"] == "success" for j in observed["jobs"])
def main():
    for path in ROOT.rglob("*.json"):
        json.loads(path.read_text(encoding="utf8"))
    candidates=json.loads(txt("tournament/S000/data.json"))
    assert len(candidates)==10 and len({x["id"] for x in candidates})==10
    assert sum(candidates[0]["weights"])==100
    weights=candidates[0]["weights"]
    for c in candidates:
        assert len(c["scores"])==len(weights)==8
        assert all(0<=s<=w for s,w in zip(c["scores"],weights))
        assert c["score"]==sum(c["scores"]) 
        assert len(c["ladder"])==5
    matches=json.loads(txt("tournament/S000/matches.json"))
    assert len(matches)==45
    ids={x["id"] for x in candidates}
    pairs=set(); wins={x:0 for x in ids}; losses={x:0 for x in ids}
    for m in matches:
        a,b,w=m["a"],m["b"],m["winner"]
        assert a!=b and {a,b}<=ids and w in (a,b)
        pair=frozenset((a,b)); assert pair not in pairs; pairs.add(pair)
        wins[w]+=1;losses[b if w==a else a]+=1
    assert sum(wins.values())==sum(losses.values())==45
    assert all(wins[x]+losses[x]==9 for x in ids)
    bracket=json.loads(txt("tournament/S000/bracket.json"))
    ordered=sorted(candidates,key=lambda c:(-wins[c["id"]],-c["score"],c["id"]))
    assert bracket["seeds"]==[x["id"] for x in ordered[:4]]
    for m in bracket["semifinals"]+[bracket["championship"],bracket["third_place"]]:
        assert m["winner"] in (m["a"],m["b"])
        assert any({r["a"],r["b"]}=={m["a"],m["b"]} and r["winner"]==m["winner"] for r in matches)
    s1,s2=bracket["semifinals"]
    assert {bracket["championship"]["a"],bracket["championship"]["b"]}=={s1["winner"],s2["winner"]}
    assert bracket["championship"]["winner"]=="SUN"
    assert len(bracket["ranking"])==10 and set(bracket["ranking"])==ids
    required=["AGENTS.md","authoritative/STATE.json","authoritative/NOVELTY_STANDARD.md","authoritative/FORMALISATION_POLICY.md","programme/PROJECTS.json","papers/PAPER_01_BRIEF.md","papers/P001_S000_KICKOFF_PROMPT.md","sessions/NEXT_SESSION.md","sessions/S000/CLOSEOUT.md"]
    for p in required: assert (ROOT/p).is_file(),p
    state=json.loads(txt("authoritative/STATE.json"))
    projects=json.loads(txt("programme/PROJECTS.json"))
    receipt=json.loads(txt("programme/P001_REGISTRATION.json"))
    check_registration(state, projects, receipt)
    assert (ROOT/"sessions/P001-S000/REGISTRATION.md").is_file()
    assert (ROOT/"prompts/S001_BEFORE_P001_REGISTRATION.md").is_file()
    assert not (ROOT/"sessions/S001").exists(), "Registration is not parent S001"
    if receipt["session"] == "P001-S001":
        assert (ROOT/"sessions/P001-S001/REGISTRATION.md").is_file()
        assert (ROOT/"sessions/P001-S000/REGISTRATION_RECEIPT.json").is_file()
        assert (ROOT/"prompts/S001_BEFORE_P001_S001_STATUS.md").is_file()
    if receipt["session"] == "P001-S002":
        assert (ROOT/"sessions/P001-S002/REGISTRATION.md").is_file()
        assert (ROOT/"sessions/P001-S001/REGISTRATION_RECEIPT.json").is_file()
        assert (ROOT/"prompts/S001_BEFORE_P001_S002_STATUS.md").is_file()
    if receipt["session"] == "P001-S003":
        assert (ROOT/"sessions/P001-S003/REGISTRATION.md").is_file()
        assert (ROOT/"sessions/P001-S002/REGISTRATION.md").is_file()
    assert "NOT VERBATIM" in txt("prompts/S000_INPUT.md")
    print("PASS: 10 candidates, 45 matches, scores, full bracket, ladders, JSON, checked child registration, zero-result counts and separate handoffs")
if __name__=="__main__":main()

