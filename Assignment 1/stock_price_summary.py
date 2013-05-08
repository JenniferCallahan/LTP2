import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """
    def test_long_mixed(self):
        """ Test a list of multiple values, both positive and negative."""
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_short_mixed(self):
        """ Test a list of one positive value and one negative value."""
        actual = a1.stock_price_summary([-0.01, 0.99])
        expected = (0.99, -0.01)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])
        
    def test_empty(self):
        """ Test an empty list."""
        actual = a1.stock_price_summary([])
        expected =(0, 0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_negative(self):
        """ Test a list made up only of losses -- i.e., negative numbers."""
        actual = a1.stock_price_summary([-0.01, -0.12, -0.15])
        expected = (0, -0.28)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])

    def test_positive(self):
        """ Test a list made up only of gains -- i.e., positive numbers."""
        actual = a1.stock_price_summary([0.02, 0.56, 0.43])
        expected = (1.01, 0)
        self.assertAlmostEqual(actual[0], expected[0])
        self.assertAlmostEqual(actual[1], expected[1])


if __name__ == '__main__':
    unittest.main(exit=False)
