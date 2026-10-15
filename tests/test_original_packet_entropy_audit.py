import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from original_packet_entropy_audit import small,products,private_audit,cap_audit,factors,private,prod,cap9,ledger
class OriginalPacketTests(unittest.TestCase):
    def test_all_small_families_and_pair_capacity(self): self.assertEqual(small(),387)
    def test_product_entropy_equalities(self): self.assertEqual(len(products()),9)
    def test_private_intersecting_obstruction(self): self.assertEqual(len(private_audit()),5)
    def test_cap_and_averaged_published_factors(self):
        self.assertEqual(len(cap_audit()),3)
        self.assertTrue(factors())
    def test_one_time_owner(self):
        for F in (private(3),prod(2,3),cap9()):
            _,_,_,packet=ledger(F,F[0],3.5)
            self.assertEqual(sum(len(R) for R in packet.values()),len(F))
if __name__=='__main__':unittest.main()
