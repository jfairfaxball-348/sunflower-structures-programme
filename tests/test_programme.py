import copy,json,sys,unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
import validate
class TournamentTests(unittest.TestCase):
    def test_structural_integrity(self):validate.main()
    def test_unique_positive_scores(self):
        x=json.loads((ROOT/"tournament/S000/data.json").read_text())
        self.assertEqual(len(x),10)
        self.assertTrue(all(c["score"]>0 for c in x))
    def test_separate_handoffs(self):
        self.assertIn("P001-S000", (ROOT/"papers/P001_S000_KICKOFF_PROMPT.md").read_text())
        self.assertIn("S001", (ROOT/"sessions/NEXT_SESSION.md").read_text())
    def records(self):
        return tuple(json.loads((ROOT/p).read_text()) for p in
                     ("authoritative/STATE.json", "programme/PROJECTS.json", "programme/P001_REGISTRATION.json"))
    def test_s032_preserves_earlier_results_and_does_not_promote_tik(self):
        state, projects, receipt = self.records()
        self.assertEqual(receipt["session"], "P001-S032")
        audit = receipt["independent_registration_verification"]
        self.assertEqual(audit["s026_single_original_Q_edge_bound"], "t/(9*m^2)")
        self.assertTrue(audit["s026_exact_Q_singleton_required"])
        self.assertTrue(audit["s026_light_support_overlap_allowed"])
        self.assertTrue(audit["s026_final_H_pair_singleton_empty_certified"])
        self.assertFalse(audit["s026_unrestricted_direct_edge_512_proved"])
        self.assertTrue(audit["s027_full_support_thin_first_refuted"])
        self.assertFalse(audit["s027_frozen_multihub_512_proved"])
        self.assertFalse(audit["s027_frozen_multihub_512_refuted"])
        self.assertEqual(audit["s027_q1024_thinned_optimum"], 1026)
        self.assertEqual(audit["s027_q1024_min_required"], 2047)
        self.assertEqual(audit["s027_same_family_full_valid_edges"], 1076891650)
        self.assertFalse(audit["full_tik_proved"])
        self.assertTrue(audit["bsel_universal_refuted"])
        self.assertEqual(state["session_completed"], "S000")
        self.assertEqual(projects["projects"][0]["last_child_session"], "P001-S032")
        self.assertTrue(audit["s028_frozen_C512_proved"])
        self.assertEqual(audit["s028_stronger_restricted_bound"], "t/((3m-2)*(m-1)) >= t/(3m^2)")
        self.assertTrue(audit["s028_original_Q_fixed"])
        self.assertTrue(audit["s028_original_one_Q_per_block"])
        self.assertTrue(audit["s028_all_final_exact_pair_singleton_empty_certified_symbolically"])
        self.assertFalse(audit["s028_unrestricted_direct_edge_proved"])
        self.assertFalse(audit["s028_full_tik_proved"])
        self.assertFalse(audit["independent_mathematical_review"])
        self.assertEqual(receipt["next_child_obligation"]["session"], "P001-S033")
        self.assertFalse(audit["s029_frozen_C512_proved"])
        self.assertFalse(audit["s029_frozen_C512_refuted"])
        self.assertTrue(audit["s029_A_majority_meets_C512"])
        self.assertTrue(audit["s029_B_Hall_representatives_injective"])
        self.assertTrue(audit["s029_rep_only_B512_refuted"])
        self.assertFalse(audit["s030_future_only"])
        self.assertTrue(audit["s030_mandatory_fifth_audit_completed"])
        self.assertTrue(audit["s030_hall_lift_all_refuted"])
        self.assertEqual(audit["s030_weighted_star_bound"], "W_q/(m-1)")
        self.assertEqual(audit["s030_simple_two_m_core_bound"], "T_C/(m-1)")
        self.assertFalse(audit["s030_frozen_C512_proved"])
        self.assertFalse(audit["s030_full_B_bound_proved"])
        self.assertFalse(audit["s031_future_only"])
        self.assertFalse(audit["s032_future_only"])
        self.assertTrue(audit["s033_future_only"])
        self.assertTrue(audit["s031_same_assistant_symbolic_only"])
        self.assertFalse(audit["s031_frozen_C512_all_m_proved"])
        self.assertFalse(audit["s031_full_TIK_proved"])
        self.assertEqual(audit["s031_bounded_m_C512_max"], 128)
        self.assertEqual(audit["s031_light_singleton_bad_matching"], 2)
        self.assertTrue(audit["s032_five_link_certificate_exact_same_assistant"])
        self.assertTrue(audit["s032_global_private_extra_petal_constant_fraction_refuted"])
        self.assertTrue(audit["s032_palette_full_F_internally_valid"])
        self.assertEqual(audit["s032_palette_private_mass_cap"], "2/(m+1)")
        self.assertEqual(audit["s032_sharpened_bounded_m_C512_max"], 129)
        self.assertEqual(audit["s032_sharpened_bounded_m_B256_max"], 66)
        self.assertFalse(audit["s032_universal_B256_proved"])
        self.assertFalse(audit["s032_full_TIK_proved"])
        self.assertFalse(audit["s032_independent_math_review"])
        self.assertFalse(receipt["parent_programme_session_executed"])

    def test_registration_rejects_wrong_child_sha(self):
        state, projects, receipt = self.records()
        altered = copy.deepcopy(receipt)
        altered["child"]["main_validation"]["head_sha"] = "0" * 40
        with self.assertRaises(AssertionError):
            validate.check_registration(state, projects, altered)
    def test_registration_rejects_failed_job(self):
        state, projects, receipt = self.records()
        altered = copy.deepcopy(receipt)
        altered["child"]["main_validation"]["jobs"][0]["conclusion"] = "failure"
        with self.assertRaises(AssertionError):
            validate.check_registration(state, projects, altered)
    def test_registration_cannot_promote_proof_count(self):
        state, projects, receipt = self.records()
        state["mathematical_result_count"] = 1
        with self.assertRaises(AssertionError):
            validate.check_registration(state, projects, receipt)
if __name__=="__main__":unittest.main()

