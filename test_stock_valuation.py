import unittest
from Base import Base
from SolvencyRatio import SolvencyRatio

class TestStockValuation(unittest.TestCase):

    # Testing Methods inside Base class
    def test_percentage_growth(self):
        self.assertEqual(Base.percentage_growth([1,2,3,4]),[100.,50.,33.33333333333333])

    # Testing Methods inside SolvencyRatio Class
    def test_debttoequity(self):
        self.assertEqual(SolvencyRatio.debttoequity(self),None)

    def test_interest_coverage_ratio(self):
        self.assertEqual(SolvencyRatio.interest_coverage_ratio(self),None)

if __name__ == "__main__":
    unittest.main()