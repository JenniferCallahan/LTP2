import unittest
import remove_shared

class TestRemove_Shared(unittest.TestCase):
    """ Tests for function remove_shared.remove_shared."""

    def test_general_case(self):
        """
        Test remove_shared where there are items that appear in both lists and
        items that appear in only one or the other list.
        """
        # remember that this docstring is part of the output in case of failure,
        # so make it informative
        list_1 = [1,2,3,4,5,6]
        list_2 = [2,4,5,7]

        list_1_expected = [1,3,6]
        list_2_expected = [2,4,5,7]
        # note these variables designate the expected output values
        
        remove_shared.remove_shared(list_1, list_2)
        # function call

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)
        # note that these assertions say that after the function call, the lists
        # will be mutated (or not mutated) in the way that we predicted -- the
        # assertions DON'T say that list_1 and list_1_expected name the same list
        # BEFORE the function call

    def test_no_common(self):
        """
        Test two lists that share no common items.
        """
        list_1 = [1 ,3, 5, 7]
        list_2 = [2, 4, 6, 8]

        list_1_expected = [1 ,3, 5, 7]
        list_2_expected = [2, 4, 6, 8]

        remove_shared.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

    def test_all_common(self):
        """
        Test two lists that have all items in common.
        """
        list_1 = [1, 2, 3]
        list_2 = [1, 2, 3]

        list_1_expected = []
        list_2_expected = [1, 2, 3]

        remove_shared.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

    def test_1_empty(self):
        """
        Test with list 1 empty.
        """
        list_1 = []
        list_2 = [1, 2, 3]

        list_1_expected = []
        list_2_expected = [1, 2, 3]

        remove_shared.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

    def test_2_empty(self):
        """Test with list 2 empty."""
        list_1 = [1, 2, 3]
        list_2 = []

        list_1_expected = [1, 2, 3]
        list_2_expected = [4]
        #error introduced here -- real expected value is []
        #docstring comes back at top of failure message -- not in the code-ful
        #part
        remove_shared.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)
		
	def test_all_empty(self):
		"""Test with 2 empty lists."""
        list_1 = []
        list_2 = []

        list_1_expected = []
        list_2_expected = []
       
        remove_shared.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

        

if __name__ == '__main__':
    unittest.main(exit=False)


        
    
    
