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
    def test_s026_restricted_claim_does_not_promote_tik(self):
        state, projects, receipt = self.records()
        self.assertEqual(receipt["session"], "P001-S026")
        audit = receipt["independent_registration_verification"]
        self.assertEqual(audit["s026_single_original_Q_edge_bound"], "t/(9*m^2)")
        self.assertTrue(audit["s026_exact_Q_singleton_required"])
        self.assertTrue(audit["s026_light_support_overlap_allowed"])
        self.assertTrue(audit["s026_final_H_pair_singleton_empty_certified"])
        self.assertFalse(audit["s026_unrestricted_direct_edge_512_proved"])
        self.assertFalse(audit["full_tik_proved"])
        self.assertTrue(audit["bsel_universal_refuted"])
        self.assertEqual(state["session_completed"], "S000")
        self.assertEqual(projects["projects"][0]["last_child_session"], "P001-S026")
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

