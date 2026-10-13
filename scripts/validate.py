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
    expected_successors["P001-S026"] = ("P001-S027", ["MULTIHUB_NONPRIVATE_DIRECT_EDGE_AGGREGATION"])
    expected_successors["P001-S027"] = ("P001-S028", ["PETAL_FIRST_MULTIHUB_COLLISION_AWARE_SELECTION"])
    expected_successors["P001-S028"] = ("P001-S029", ["PETAL_FIRST_TWO_HEAVY_PAIR_CERTIFICATES"])
    expected_successors["P001-S029"] = ("P001-S030", ["FIFTH_AUDIT_MULTI_PETAL_TWO_Q_BRIDGE"])
    expected_successors["P001-S030"] = ("P001-S031", ["SPARSE_WEIGHTED_MULTISTAR_COLLISION_AWARE_BRIDGE"])
    expected_successors["P001-S031"] = ("P001-S032", ["SIMULTANEOUS_LIGHT_PETAL_ALLOCATION_M_SAVING"])
    expected_successors["P001-S032"] = ("P001-S033", ["SATURATED_LIGHT_FOREST_ROUNDING_M2"])
    expected_successors["P001-S033"] = ("P001-S034", ["DSE3_DEGENERATE_SPREAD_EXTRACTION"])
    expected_successors["P001-S034"] = ("P001-S035", ["MANDATORY_FIFTH_SESSION_CORRECTION_AUDIT_AND_DSE3_COMPATIBILITY_GATE"])
    expected_successors["P001-S035"] = ("P001-S036", ["DSE3_HIGH_TRANSVERSAL_COMPATIBLE_AGGREGATION"])
    expected_successors["P001-S036"] = ("P001-S037", ["HDSE3_OVERLAPPING_HIGH_DEGREE_LINK_EXTRACTION"])
    expected_successors["P001-S037"] = ("P001-S038", ["HDSE3_SATURATED_CROSS_KERNEL_AMPLIFICATION"])
    expected_successors["P001-S038"] = ("P001-S039", ["HDSE3_HYBRID_SATURATED_AND_PRIVATE_CHANNEL_BRIDGE"])
    expected_successors["P001-S039"] = ("P001-S040", ["MANDATORY_FIFTH_TENTH_AUDIT_AND_HYBRID_HIGH_DEGREE_GAP"])
    expected_successors["P001-S040"] = ("P001-S041", ["UNRESTRICTED_OVERLAP_OR_ALL_K_BREAKTHROUGH"])
    expected_successors["P001-S041"] = ("P001-S042", ["UNIVERSAL_REGIONAL_DICHOTOMY_OR_FULL_ALL_K_OVERLAP_BREAKTHROUGH"])
    expected_successors["P001-S042"] = ("P001-S043", ["NONLINEAR_PAIR_MULTIPLICITY_M_SAVING_OR_FULL_HDSE3"])
    expected_successors["P001-S043"] = ("P001-S044", ["DENSE_CORE_NONLINEAR_THIRD_CERTIFICATE_OR_HDSE3"])
    expected_successors["P001-S044"] = ("P001-S045", ["MANDATORY_FIFTH_PROGRESS_CORRECTION_AUDIT_AND_DENSE_CORE_BRIDGE"])
    expected_successors["P001-S045"] = ("P001-S046", ["DENSITY_FREE_NONLINEAR_CORE_AND_PAIR_COEXISTENCE"])
    expected_successors["P001-S046"] = ("P001-S047", ["JOINT_MULTIHUB_ORIGINAL_MASS_GLUING"])
    expected_successors["P001-S047"] = ("P001-S048", ["OVERLAPPED_LOW_BASE_COMPATIBILITY_AND_HDSE3_MASS_RESCUE"])
    expected_successors["P001-S048"] = ("P001-S049", ["INTERMEDIATE_SINGLETON_AND_MIXED_PAIR_M3_REPAIR"])
    expected_successors["P001-S049"] = ("P001-S050", ["MANDATORY_FIFTH_TENTH_CORRECTION_AUDIT_AND_LOW_RICHNESS_BRIDGE"])
    expected_successors["P001-S050"] = ("P001-S051", ["TRIPARTITE_FIVE_CERTIFICATE_UNIVERSAL_M3_PACKING"])
    expected_successors["P001-S051"] = ("P001-S052", ["LOW_RICHNESS_JX_MATCHING_REPAIR_UNRESTRICTED_TRIPARTITE_R3"])
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

    if receipt["session"] == "P001-S026":
        assert receipt["registration_kind"] == "P001_S026_ONE_GLOBAL_HEAVY_NONPRIVATE_DIRECT_EDGE_STATUS_ONLY"
        assert audit["session_outcome"] == "S026_SINGLE_GLOBAL_ORIGINAL_HEAVY_HUB_NONPRIVATE_EDGE_T_OVER_9M2_SAME_ASSISTANT"
        assert audit["s026_single_original_Q_edge_bound"] == "t/(9*m^2)"
        assert audit["s026_exact_Q_singleton_required"] and audit["s026_light_support_overlap_allowed"]
        assert audit["s026_final_H_pair_singleton_empty_certified"]
        assert audit["s026_same_assistant_symbolic_only"] and not audit["s026_future_only"]
        assert not audit["s026_unrestricted_direct_edge_512_proved"] and not audit["s026_full_tik_proved"]
        assert audit["s025_fifth_audit_completed"] and audit["bsel_universal_refuted"]
        assert not audit["independent_mathematical_review"] and not audit["full_tik_proved"]
        assert project["last_child_session"] == "P001-S026"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S026/REGISTRATION.md").is_file()
    if receipt["session"] == "P001-S027":
        assert receipt["registration_kind"] == "P001_S027_MULTIHUB_FULL_SUPPORT_THIN_FIRST_METHOD_STATUS_ONLY"
        assert audit["session_outcome"] == "S027_FULL_SUPPORT_THIN_FIRST_METHOD_REFUTED_MULTIHUB_DIRECT_EDGE_512_UNPROVED"
        assert audit["s027_original_Q_fixed"] and audit["s027_one_Q_per_block"]
        assert audit["s027_nonprivate_light_allowed"]
        assert audit["s027_full_support_thin_first_refuted"]
        assert not audit["s027_frozen_multihub_512_proved"] and not audit["s027_frozen_multihub_512_refuted"]
        assert audit["s027_q1024_m"] == 1026 and audit["s027_q1024_t"] == 1102737050625
        assert audit["s027_q1024_thinned_optimum"] == 1026
        assert audit["s027_q1024_min_required"] == 2047
        assert audit["s027_same_family_full_valid_edges"] == 1076891650
        assert not audit["independent_mathematical_review"] and not audit["full_tik_proved"]
        assert audit["s025_fifth_audit_completed"] and audit["bsel_universal_refuted"]
        assert not audit["s027_future_only"] and audit["s028_future_only"]
        assert project["last_child_session"] == "P001-S027"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S027/REGISTRATION.md").is_file()

    if receipt["session"] == "P001-S028":
        assert receipt["registration_kind"] == "P001_S028_PETAL_FIRST_ONE_Q_PER_BLOCK_DIRECT_EDGE_STATUS_ONLY"
        assert audit["session_outcome"] == "S028_MULTIHUB_ONE_Q_PER_BLOCK_PETAL_FIRST_DIRECT_EDGE_3_PROVED_SAME_ASSISTANT"
        assert audit["s028_frozen_C512_proved"]
        assert audit["s028_stronger_restricted_bound"] == "t/((3m-2)*(m-1)) >= t/(3m^2)"
        assert audit["s028_original_Q_fixed"] and audit["s028_original_one_Q_per_block"] and audit["s028_nonprivate_light_allowed"]
        assert audit["s028_all_final_exact_pair_singleton_empty_certified_symbolically"]
        assert audit["s028_same_assistant_only"] and not audit["s028_unrestricted_direct_edge_proved"] and not audit["s028_full_tik_proved"]
        assert audit["independent_mathematical_review"] is False and audit["full_tik_proved"] is False
        assert audit["s028_future_only"] is False and audit["s029_future_only"] is True
        assert project["last_child_session"] == "P001-S028"
        assert project["s028_frozen_multihub_C512_proved"]
        assert project["s028_one_Q_per_block_nonprivate_light_bound"] == "t/((3m-2)*(m-1)) >= t/(3m^2)"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S028/REGISTRATION.md").is_file()

    if receipt["session"] == "P001-S029":
        assert receipt["registration_kind"] == "P001_S029_TWO_Q_PETAL_FIRST_GRAPH_METHOD_OBSTRUCTION_STATUS_ONLY"
        assert audit["session_outcome"] == "S029_TWO_Q_A_MASS_POSITIVE_B_REP_ONLY_NEGATIVE_FULL_C512_UNPROVED"
        assert audit["s029_A_submass_bound"] == "|A|/((3m-2)*(m-1)) >= |A|/(3m^2)"
        assert audit["s029_A_majority_meets_C512"] and audit["s029_B_Hall_representatives_injective"]
        assert audit["s029_B_graph_pair_singleton_empty_exact"] and audit["s029_rep_only_B512_refuted"]
        assert not audit["s029_frozen_C512_proved"] and not audit["s029_frozen_C512_refuted"]
        assert audit["s029_same_assistant_only"] and not audit["s029_all_k_tik_proved"]
        assert not audit["independent_mathematical_review"] and not audit["full_tik_proved"]
        assert not audit["s029_future_only"] and audit["s030_future_only"]
        assert project["last_child_session"] == "P001-S029"
        assert project["s029_full_two_Q_C512"] == "UNPROVED_AND_UNREFUTED"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S029/REGISTRATION.md").is_file()

    if receipt["session"] == "P001-S030":
        assert receipt["registration_kind"] == "P001_S030_WEIGHTED_STAR_2M_CORE_FIFTH_AUDIT_STATUS_ONLY"
        assert audit["session_outcome"] == "S030_STAR_CORE_MATCHING_POSITIVES_HALL_FULL_LIFT_FALSE_C512_UNPROVED"
        assert audit["s030_mandatory_fifth_audit_completed"] and audit["s030_prior_audits_reconciled"] == ["S005","S010","S015","S020","S025"]
        assert audit["s030_weighted_star_bound"] == "W_q/(m-1)"
        assert audit["s030_simple_two_m_core_bound"] == "T_C/(m-1)"
        assert audit["s030_small_matching_bound"] == "|B|/[2*(m-1)^2]"
        assert audit["s030_hall_light_injection"] and audit["s030_hall_lift_all_refuted"]
        assert not audit["s030_frozen_C512_proved"] and not audit["s030_frozen_C512_refuted"]
        assert not audit["s030_full_B_bound_proved"] and not audit["s030_full_B_bound_refuted"]
        assert not audit["full_tik_proved"] and not audit["s030_full_TIK_proved"]
        assert audit["s030_same_assistant_symbolic_only"] and not audit["s030_independent_math_review"]
        assert audit["s030_future_only"] is False and audit["s031_future_only"] is True
        assert project["last_child_session"] == "P001-S030"
        assert project["s030_fifth_audit_completed"] and project["s030_full_two_Q_C512"] == "UNPROVED_AND_UNREFUTED"
        assert child["final_head_validation"] and all(
            z["head_sha"] == child["merged_pr"]["head_sha"] and z["conclusion"] == "success"
            and z["jobs"] and all(j["conclusion"] == "success" for j in z["jobs"])
            for z in child["final_head_validation"])
        assert child["main_validation"]["head_sha"] == child["main_commit"]
        assert child["main_validation"]["conclusion"] == "success"
        assert (ROOT / "sessions/P001-S030/REGISTRATION.md").is_file()


    if receipt["session"] == "P001-S035":
        assert receipt["registration_kind"] == "P001_S035_FIFTH_AUDIT_BOUNDED_TRANSVERSAL_DSE3_STATUS_ONLY"
        assert audit["session_outcome"] == "S035_BOUNDED_FRACTIONAL_COVER_M3_HIGH_COVER_GAP"
        assert audit["s035_fractional_cover_bound"] == "|D|/[8*m^2*tau*(D)]"
        assert audit["s035_matching_bound"] == "|D|/[24*m^2*nu(D)]"
        assert audit["s035_bounded_cover_m3_constant"] == "1/(8*B) when tau*(D)<=B*m"
        assert audit["s035_fifth_audit_completed"] and not audit["s035_fifth_audit_future_only"]
        assert audit["s035_high_cover_shortcut_refuted"] and not audit["s035_small_cover_implied_by_spread"]
        assert audit["s035_same_family_matching_fraction"] == "1/(m-1)^2"
        assert not audit["s035_dse3_proved"] and not audit["s035_r3_proved"] and not audit["s035_full_all_k_tik_proved"]
        assert audit["s036_future_only"] and not audit["s035_independent_math_review"]
        assert project["last_child_session"] == "P001-S035" and project["s035_fifth_audit_completed"]
        assert child["main_commit"] == "dfa56df29dd56197b53889d8a61f3fed1d28d77f"
        assert child["merge_parents"] == ["627e0897bfcb0702a025e5d696b3298bfdcba50f", "62455d516baa532a927e42b0a6e248e2a2847424"]
        assert child["tree_sha"] == "208536f7b40c1ac19396ca24fda982cdfcd19e8e"
        assert all(run["head_sha"] == child["merged_pr"]["head_sha"] and run["conclusion"] == "success" for run in child["final_head_validation"])
        for path in ("sessions/P001-S035/REGISTRATION.md", "sessions/P001-S035/CHILD_VERIFICATION.json", "sessions/P001-S035/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S036":
        assert receipt["registration_kind"] == "P001_S036_HDSE3_REDUCTION_BALANCED_HIGH_COVER_STATUS_ONLY"
        assert audit["s036_matching_or_high_degree_reduction_same_assistant"] is True
        assert audit["s036_hdse3_equivalence_conditional_on_s033"] is True
        assert audit["s036_hdse3_proved"] is False and audit["s036_r3_proved"] is False and audit["s036_full_tik_proved"] is False
        assert audit["s036_independent_math_review"] is False and audit["s037_future_only"] is True
        assert project["last_child_session"] == "P001-S036"
        for path in ("sessions/P001-S036/REGISTRATION.md", "sessions/P001-S036/CHILD_VERIFICATION.json", "sessions/P001-S036/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S037":
        assert receipt["registration_kind"] == "P001_S037_OVERLAPPING_PALETTE_WEIGHTED_CONFLICT_STATUS_ONLY"
        assert audit["s037_pair_core_palette_iff_same_assistant"] is True
        assert audit["s037_high_degree_overlap_example_core_free_spread_no_private_pair"] is True
        assert audit["s037_naive_union_invalid_pair"] is True
        assert audit["s037_same_family_valid_fraction"] == "1/(m-1)^2"
        assert audit["s037_hdse3_proved"] is False and audit["s037_r3_proved"] is False and audit["s037_full_tik_proved"] is False
        assert audit["s037_independent_math_review"] is False and audit["s038_future_only"] is True
        assert project["last_child_session"] == "P001-S037"
        for path in ("sessions/P001-S037/REGISTRATION.md", "sessions/P001-S037/CHILD_VERIFICATION.json", "sessions/P001-S037/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S038":
        assert receipt["registration_kind"] == "P001_S038_TENSOR_CORE_LINEAR_HDSE3_STATUS_ONLY"
        assert audit["s038_tensor_all_ranks_iff_same_assistant"] is True
        assert audit["s038_exact_robust_core_graph_mcore"] is True
        assert audit["s038_linear_spread_corefree_highdegree_no_tensor"] is True
        assert audit["s038_linear_same_E_valid_fraction"] == "1"
        assert audit["s038_universal_full_tensor_capture_refuted"] is True
        assert audit["s038_hdse3_proved"] is False and audit["s038_r3_proved"] is False and audit["s038_full_tik_proved"] is False
        assert audit["s038_independent_math_review"] is False and audit["s039_future_only"] is True
        assert project["last_child_session"] == "P001-S038"
        assert child["merged_pr"]["number"] == 40
        assert child["main_commit"] == "76916462bd3119801ccd00141b32d4dbc0b33f79"
        assert child["merge_parents"] == ["ae4893283c27af0b53f346dd759afedeba00b06a", "8c572578a20f00706eba2511467143715c567bdd"]
        assert child["tree_sha"] == "f023a428a5eedd4a596ddda6c7c7ca75f5c6ef2d"
        for path in ("sessions/P001-S038/REGISTRATION.md", "sessions/P001-S038/CHILD_VERIFICATION.json", "sessions/P001-S038/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S039":
        assert receipt["registration_kind"] == "P001_S039_PARTIAL_PALETTE_HDSE3_STATUS_ONLY"
        assert audit["s039_exact_five_link_atlas"] is True
        assert audit["s039_intermediate_private_spoke_hdse3"] is True
        assert audit["s039_private_spoke_all_pair_degree_lt_m"] is True
        assert audit["s039_private_spoke_same_e_fraction"] == "1/(m-1)"
        assert audit["s039_first_hidden_tensor_corrected"] is True
        assert audit["s039_hdse3_proved"] is False and audit["s039_r3_proved"] is False and audit["s039_full_tik_proved"] is False
        assert audit["s039_independent_math_review"] is False and audit["s040_fifth_audit_future_only"] is True
        assert project["last_child_session"] == "P001-S039"
        assert child["merged_pr"]["number"] == 41
        assert child["main_commit"] == "c6a7bcf914642fc0d90c2235cbf6794e657e4b41"
        assert child["merge_parents"] == ["76916462bd3119801ccd00141b32d4dbc0b33f79", "044a191699be63ffde5056679c7f2d577ec6e5fc"]
        assert child["tree_sha"] == "43cb1402085c40f7508e3be6496d59abfea58167"
        for path in ("sessions/P001-S039/REGISTRATION.md", "sessions/P001-S039/CHILD_VERIFICATION.json", "sessions/P001-S039/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S040":
        assert receipt["registration_kind"] == "P001_S040_FIFTH_TENTH_AUDIT_STAR_FOREST_PALETTES_STATUS_ONLY"
        assert audit["s040_fifth_tenth_audit_completed"] is True
        assert audit["s040_fifth_audit_future_only"] is False and audit["s041_future_only"] is True
        assert audit["s040_all_palette_disjoint_star_forest_bound"] == "|E|/(3*m^3)"
        assert audit["s040_arbitrary_palette_sizes"] is True
        assert audit["s040_original_complete_disjoint_star_forest_required"] is True
        assert audit["s040_true_final_pair_singleton_empty_checked_same_assistant"] is True
        assert audit["s040_hdse3_proved"] is False and audit["s040_r3_proved"] is False
        assert audit["s040_full_tik_proved"] is False and audit["s040_independent_math_review"] is False
        assert project["last_child_session"] == "P001-S040"
        assert child["main_commit"] == "e8e1c343405c94cdf3a585ef2b1db2c278f1fac1"
        assert child["merged_pr"]["number"] == 42 and child["merged_pr"]["head_sha"] == "f7a6bdbe14288260593af78f343fb0894121f1e2"
        assert child["tree_sha"] == "0cef90701db7079dc0adf798a0e97bcfd8f1ff73"
        assert child["merge_parents"] == ["c6a7bcf914642fc0d90c2235cbf6794e657e4b41", "f7a6bdbe14288260593af78f343fb0894121f1e2"]
        assert child["final_head_validation"][0]["run_id"] == 38305995855
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115000071603
        assert child["main_validation"]["run_id"] == 38306053362
        assert child["main_validation"]["jobs"][0]["id"] == 115000258001
        assert project["s040_fifth_tenth_audit_completed"] is True
        assert project["s040_hdse3_proved"] is False and project["s040_all_k_tik_proved"] is False
        for path in ("sessions/P001-S040/REGISTRATION.md", "sessions/P001-S040/CHILD_VERIFICATION.json", "sessions/P001-S040/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S041":
        assert receipt["registration_kind"] == "P001_S041_REGIONAL_WEIGHTED_OVERLAP_STATUS_ONLY"
        assert audit["s040_fifth_tenth_audit_completed"] is True and audit["s041_future_only"] is False
        assert audit["s042_future_only"] is True
        assert audit["s041_weighted_regional_all_rank_conditional"] is True
        assert audit["s041_rank3_bound"] == "|F|/(16*B*m^3)"
        assert audit["s041_partial_palette_overlap_permitted"] is True
        assert audit["s041_islands_pairwise_whole_support_disjoint"] is True
        assert audit["s041_core_overlap_unbounded"] is True
        assert audit["s041_fractional_cover_hypotheses_required"] is True
        assert audit["s041_sharp_example_total"] == "(m-1)^3"
        assert audit["s041_sharp_example_max_valid"] == 1
        assert not audit["s041_hdse3_proved"] and not audit["s041_r3_proved"]
        assert not audit["s041_full_tik_proved"] and not audit["s041_independent_math_review"]
        assert project["last_child_session"] == "P001-S041"
        assert project["s041_rank3_bound"] == audit["s041_rank3_bound"]
        assert project["s040_fifth_tenth_audit_completed"] is True
        assert child["main_commit"] == "92b3bc14caa69f81db82c98b383e75a2ae4292cf"
        assert child["merged_pr"]["number"] == 43 and child["merged_pr"]["head_sha"] == "02d7ce68c4a51e5055ed9ba34a0cd0820e69fc6f"
        assert child["tree_sha"] == "4c1e3e845f5bf16a090874ba736466b7f0e3be88"
        assert child["merge_parents"] == ["e8e1c343405c94cdf3a585ef2b1db2c278f1fac1", "02d7ce68c4a51e5055ed9ba34a0cd0820e69fc6f"]
        assert child["final_head_validation"][0]["run_id"] == 38368846313
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115200497096
        assert child["main_validation"]["run_id"] == 38368918347
        assert child["main_validation"]["jobs"][0]["id"] == 115200729864
        for path in ("sessions/P001-S041/REGISTRATION.md", "sessions/P001-S041/CHILD_VERIFICATION.json", "sessions/P001-S041/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S042":
        assert receipt["registration_kind"] == "P001_S042_ALL_RANKS_LINEAR_RESTRICTED_AND_REGIONAL_METHOD_NEGATIVE_STATUS_ONLY"
        assert audit["s042_future_only"] is False and audit["s043_future_only"] is True
        assert audit["s042_original_linear_all_rank_extraction_same_assistant"] is True
        assert audit["s042_linear_ck"] == "1/[2^(k-1)*k^k]"
        assert audit["s042_linear_rank3_bound"] == "|F|/(108*m^3)"
        assert audit["s042_bounded_pair_codegree_bound"] == "|F|/[(1+binom(k,2)*(B-1))*2^(k-1)*k^k*m^k]"
        assert audit["s042_affine_steiner_original_hdse3"] is True
        assert audit["s042_affine_steiner_same_E_entirely_valid"] is True
        assert audit["s042_two_way_regional_mass_capture_refuted"] is True
        assert audit["s042_two_way_mass_ratio_upper"] == "3*B*(m/n+1/(n-1))"
        assert not audit["s042_s041_conditional_theorem_refuted"]
        assert not audit["s042_hdse3_proved"] and not audit["s042_r3_proved"]
        assert not audit["s042_full_tik_proved"] and not audit["s042_independent_math_review"]
        assert not audit["s042_new_N1_N2"]
        assert audit["s042_next_fifth_audit"] == "P001-S045"
        assert project["last_child_session"] == "P001-S042"
        assert project["s042_linear_rank3_bound"] == audit["s042_linear_rank3_bound"]
        assert project["s042_two_way_regional_mass_capture_refuted"] is True
        assert child["main_commit"] == "47122d5c8fe01054d2db871412eb9e16dbd38c42"
        assert child["merged_pr"]["number"] == 44 and child["merged_pr"]["head_sha"] == "981507a17a0f7a68ef8cf63906f9e69754307b4a"
        assert child["tree_sha"] == "86d29139094ab35ad97e14ac74d4242e20c56927"
        assert child["merge_parents"] == ["92b3bc14caa69f81db82c98b383e75a2ae4292cf", "981507a17a0f7a68ef8cf63906f9e69754307b4a"]
        assert child["final_head_validation"][0]["run_id"] == 38373003091
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115214351394
        assert child["main_validation"]["run_id"] == 38373071947
        assert child["main_validation"]["jobs"][0]["id"] == 115214580353
        assert child["final_head_validation"][0]["conclusion"] == "success"
        for path in ("sessions/P001-S042/REGISTRATION.md", "sessions/P001-S042/CHILD_VERIFICATION.json", "sessions/P001-S042/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S043":
        assert receipt["registration_kind"] == "P001_S043_NONLINEAR_PEELED_FIBRE_M_SAVING_STATUS_ONLY"
        assert audit["s043_future_only"] is False and audit["s044_future_only"] is True
        assert audit["s043_peeled_bound"] == "|D|/(108*m^3)"
        assert audit["s043_low_delta_majority_bound"] == "|F|/(216*m^3)"
        assert audit["s043_high_delta_link_bound"] == ">|F|/(48*m^3)"
        assert audit["s043_dense_surviving_core_solved"] is False
        assert not audit["s043_hdse3_proved"] and not audit["s043_r3_proved"] and not audit["s043_full_tik_proved"]
        assert not audit["s043_independent_math_review"] and not audit["s043_new_N1_N2"]
        assert audit["s043_next_fifth_audit"] == "P001-S045"
        assert project["last_child_session"] == "P001-S043"
        assert child["main_commit"] == "56ea510dbaef8b21abbcad21a6cbcad2f8e990cd"
        assert child["merged_pr"]["number"] == 45 and child["merged_pr"]["head_sha"] == "bdad036fb015a9a90b70c8c076ad55d335caba37"
        assert child["tree_sha"] == "487f9700afaacf7e7464c1c37a0bd111c8b873eb"
        assert child["merge_parents"] == ["47122d5c8fe01054d2db871412eb9e16dbd38c42", "bdad036fb015a9a90b70c8c076ad55d335caba37"]
        assert child["final_head_validation"][0]["run_id"] == 38380577867
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115239670663
        assert child["main_validation"]["run_id"] == 38380699071
        assert child["main_validation"]["jobs"][0]["id"] == 115240078575
        for path in ("sessions/P001-S043/REGISTRATION.md", "sessions/P001-S043/CHILD_VERIFICATION.json", "sessions/P001-S043/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S044":
        assert receipt["registration_kind"] == "P001_S044_SCOPED_NONLINEAR_HDSE3_POSITIVE_SUBCLASS_STATUS_ONLY"
        assert audit["s044_future_only"] is False and audit["s045_future_only"] is True
        assert audit["s044_apex_degeneracy_bound"] == "|F|/[54*(A+1)*m^3]"
        assert audit["s044_dense_balanced_bound"] == "|F|/(36*A*m^3)"
        assert audit["s044_explicit_cyclic_original_hdse3"] is True
        assert audit["s044_explicit_cyclic_t"] == "10*m^3"
        assert audit["s044_original_full_cyclic_f_invalid"] is True
        assert audit["s044_final_H_pair_singleton_empty_verified_same_assistant"] is True
        assert audit["s044_saturated_pair_star_union_false"] is True
        assert audit["s044_same_E_saturated_rescue"] == "1/(m-1)"
        assert not audit["s044_unrestricted_hdse3_proved"] and not audit["s044_r3_proved"] and not audit["s044_full_tik_proved"]
        assert not audit["s044_independent_math_review"] and not audit["s044_new_N1_N2"]
        assert audit["s044_next_fifth_audit"] == "P001-S045"
        assert audit["s044_archive_sha256"] == "50f31dd5070a6b4d2ffcaa990de6f41fddceb0eca6c37a1ac0a3c21ad7115ec3"
        assert project["last_child_session"] == "P001-S044"
        assert child["main_commit"] == "dcc1617884c538d18a85649cad959cfeded0e28e"
        assert child["merged_pr"]["number"] == 46 and child["merged_pr"]["head_sha"] == "4ae8c9403f86c065abd0610f88b371aa07afa2fe"
        assert child["tree_sha"] == "45406c8ab1dcb98245ac95d47cdbba4f49b9025c"
        assert child["merge_parents"] == ["56ea510dbaef8b21abbcad21a6cbcad2f8e990cd", "4ae8c9403f86c065abd0610f88b371aa07afa2fe"]
        assert child["final_head_validation"][0]["run_id"] == 38383149617
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115248297568
        assert child["main_validation"]["run_id"] == 38383253404
        assert child["main_validation"]["jobs"][0]["id"] == 115248637606
        for path in ("sessions/P001-S044/REGISTRATION.md", "sessions/P001-S044/CHILD_VERIFICATION.json", "sessions/P001-S044/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S047":
        assert receipt["registration_kind"] == "P001_S047_SCOPED_MULTIHUB_GRAPH_CELL_STATUS_ONLY"
        assert audit["s047_graph_cell_bound"] == "|F|/(m-1)^2"
        assert audit["s047_sat_upgrade"] == "|F|/(m-1)"
        assert audit["s047_sat_arbitrary_base_overlap"] and audit["s047_low_common_hub_required"]
        assert audit["s047_conflicting_original_fraction"] == "1/2"
        assert audit["s047_same_E_retained_fraction"] == "1/2"
        assert audit["s047_connected_6m_spread_corefree_highhub"]
        assert audit["s047_pair_codegrees_2_and_m"] and audit["s047_global_singleton_cross_gluing_failure"]
        assert audit["s047_same_family_rescue"]
        assert not audit["s047_unrestricted_hdse3_proved"] and not audit["s047_r3_proved"] and not audit["s047_all_k_tik_proved"]
        assert not audit["s047_independent_math_review"] and not audit["s047_new_detailed_N1_N2"]
        assert project["last_child_session"] == "P001-S047"
        assert child["main_commit"] == "48e7c29d04eb449cc20d4520c25eac7030aab059"
        assert child["merged_pr"]["number"] == 49 and child["merged_pr"]["head_sha"] == "d7158fd12884b52a4226d733c198f038df43126c"
        assert child["tree_sha"] == "3bf5b46a21f12507fef6b0d6a818e3816603dcaf"
        assert child["merge_parents"] == ["ad276ba083a8939e6dc88091aa57919b3b0e9ef8", "d7158fd12884b52a4226d733c198f038df43126c"]
        assert child["final_head_validation"][0]["run_id"] == 38404426889
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115320179504
        assert child["main_validation"]["run_id"] == 38404537804
        assert child["main_validation"]["jobs"][0]["id"] == 115320575639
        for path in ("sessions/P001-S047/REGISTRATION.md", "sessions/P001-S047/CHILD_VERIFICATION.json", "sessions/P001-S047/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S050":
        assert receipt["registration_kind"] == "P001_S050_TRIPARTITE_FIVE_CERTIFICATE_AND_MANDATORY_FIFTH_TENTH_AUDIT_STATUS_ONLY"
        assert audit["s050_fifth_tenth_audit_completed"] is True
        assert audit["s050_rank3_tripartite_fraction"] == "2/9"
        assert audit["s050_all_rank_fraction"] == "k!/k^k"
        assert audit["s050_five_certificate_iff_same_assistant"] is True
        assert audit["s050_naive_link_gluing_false"] and audit["s050_same_F_valid_fraction"] == "m/(2m-1)>1/2"
        assert not audit["s050_r3_proved"] and not audit["s050_unrestricted_hdse3_proved"] and not audit["s050_all_k_proved"]
        assert not audit["s050_independent_review"] and not audit["s050_new_N1_N2"]
        assert project["last_child_session"] == "P001-S050"
        assert child["main_commit"] == "191bb6553507f3cea87d03c0f1addea0c866f96d"
        assert child["tree_sha"] == "57b23652a80aa42179711eef319c5ec1ecc3e897"
        assert child["merged_pr"]["number"] == 52 and child["merged_pr"]["head_sha"] == "b7d24e14b834b89c2807216a70b5989c05889f81"
        assert child["merge_parents"] == ["caac0918736d8fb9982a4c69d57b2be613f99ab6", "b7d24e14b834b89c2807216a70b5989c05889f81"]
        assert child["final_head_validation"][0]["run_id"] == 38450736559 and child["final_head_validation"][0]["jobs"][0]["id"] == 115480649426
        assert child["main_validation"]["run_id"] == 38450811794 and child["main_validation"]["jobs"][0]["id"] == 115480903024
        for path in ("sessions/P001-S050/REGISTRATION.md", "sessions/P001-S050/CHILD_VERIFICATION.json", "sessions/P001-S050/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

    if receipt["session"] == "P001-S051":
        assert receipt["registration_kind"] == "P001_S051_RICH_LINK_JX_TRAP_AND_SHARP_PARTITE_STATUS_ONLY"
        assert audit["s051_normalized_6m_spread_corefree_highhub"] and audit["s051_rich_links_L_plus_1"]
        assert audit["s051_jx_matching"] == 2
        assert audit["s051_same_original_valid_fraction"] == ">1-1/L>=1-m^-4"
        assert audit["s051_rainbow_pk_sharp"]
        assert not audit["s051_hdse3_proved"] and not audit["s051_r3_proved"] and not audit["s051_all_k_tik_proved"]
        assert not audit["s051_independent_math_review"] and not audit["s051_new_N1_N2"]
        assert audit["s050_fifth_tenth_audit_completed"] is True
        assert project["last_child_session"] == "P001-S051"
        assert child["main_commit"] == "c7ede2676909f335ea2bb9f247d5a0e2abdff12c"
        assert child["tree_sha"] == "bf2cd36b84b33c44a2bbf1ea7ba1c6e47bdb1cd5"
        assert child["merged_pr"]["number"] == 53 and child["merged_pr"]["head_sha"] == "e70d332eaa39920ac98e4e576f38b0a4845f8c0a"
        assert child["merge_parents"] == ["191bb6553507f3cea87d03c0f1addea0c866f96d", "e70d332eaa39920ac98e4e576f38b0a4845f8c0a"]
        assert child["final_head_validation"][0]["run_id"] == 38474098838
        assert child["final_head_validation"][0]["jobs"][0]["id"] == 115560366457
        assert child["main_validation"]["run_id"] == 38474286573
        assert child["main_validation"]["jobs"][0]["id"] == 115561024657
        for path in ("sessions/P001-S051/REGISTRATION.md", "sessions/P001-S051/CHILD_VERIFICATION.json", "sessions/P001-S051/LOCAL_VALIDATION.md"):
            assert (ROOT / path).is_file(), path

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

