import badswap
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """
    def test_general_case_even(self):
        """ Test a list with an even number of items, containing at least 4 items.""" 
        L = [1, 2, 3, 4, 5, 6]
        badswap.swap_k(L, 2)
        L_expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(L, L_expected)

    def test_general_case_odd(self):
        """ Test a list with an odd number of items, containing at least 5 items.""" 
        L = [1, 2, 3, 4, 5, 6, 7]
        badswap.swap_k(L, 2)
        L_expected = [6, 7, 3, 4, 5, 1, 2]
        self.assertEqual(L, L_expected)

    def test_no_change(self):
        """ Test function when k == 0, i,e,, when the list is unchanged.""" 
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [1, 2, 3, 4, 5, 6]
        badswap.swap_k(L, 0)
        self.assertEqual(L, L_expected)
        
    def test_1_change(self):
       """Test smallest possible change -- i.e., k == 1."""
       L = [1, 2, 3, 4, 5, 6]
       L_expected = [6, 2, 3, 4, 5, 1]
       badswap.swap_k(L, 1)
       self.assertEqual(L, L_expected)

    def test_half_even(self):
        """ Test half an even list -- i.e., k == len(list)//2."""
        L = [1, 2, 3, 4, 5, 6]
        L_expected = [4, 5, 6, 1, 2, 3]
        badswap.swap_k(L, 3)
        self.assertEqual(L, L_expected)

    def test_half_odd(self):
        """ Test half an odd list -- i.e., k == len(list)//2."""
        L = [1, 2, 3, 4, 5]
        L_expected = [4, 5, 3, 1, 2]
        badswap.swap_k(L, 2)
        self.assertEqual(L, L_expected)

    def test_empty(self):
        """Test an empty list."""
        L = []
        L_expected = []
        badswap.swap_k(L, 2)
        self.assertEqual(L, L_expected)

    def test_1_item(self):
        """ Test a single-item list -- smallest non-empty list and smallest list
        with an odd number of items."""
        L = [1]
        L_expected = [1]
        badswap.swap_k(L, 0)
        self.assertEqual(L, L_expected)

    def test_2_item(self):
        """ Test swap on 2-item list -- the smallest list that actually be swapped, and
        smallest list with an even number of items."""
        L = [1, 2]
        L_expected = [2, 1]
        badswap.swap_k(L, 1)
        self.assertEqual(L, L_expected)
       
       


if __name__ == '__main__':
    unittest.main(exit=False)
