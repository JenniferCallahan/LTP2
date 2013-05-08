import badbus
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """
    def test_smallest(self):
        """ Test smallest permitted input -- 0."""
        actual = badbus.num_buses(0)
        expected = 0
        self.assertEqual(actual, expected)

    def test_min(self):
        """ Test smallest permitted input that would require a bus -- 1."""
        actual = badbus.num_buses(1)
        expected = 1
        self.assertEqual(actual, expected)

    def test_1_max(self):
        """Test largest number that should require 1 bus -- 50."""
        actual = badbus.num_buses(50)
        expected = 1
        self.assertEqual(actual, expected)

    def test_2(self):
        """Test smallest number that should require 2 buses -- 51."""
        actual = badbus.num_buses(51)
        expected = 2
        self.assertEqual(actual, expected)

    def test_breakpoint(self):
        """ Test input that is >100 and should roll over to a new, higher
        number of buses -- e.g., 101, 151."""
        actual = badbus.num_buses(101)
        expected = 3
        self.assertEqual(actual, expected)
        
    def test_large(self):
        """ Test input of at least 4 figures."""
        actual = badbus.num_buses(1001)
        expected = 21
        self.assertEqual (actual, expected)
    


if __name__ == '__main__':
    unittest.main(exit=False)
