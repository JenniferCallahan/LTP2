import unittest

#import the framework we want to use
# unittest looks through the current module for all the methods that
# begin with 'test' -- MUST BE LOWERCASE; calls each method and reports
# unexpected results

import divisors


class TestDivisors(unittest.TestCase):
    # this class is a subclass of unittest.TestCase
    """ Example unittest test methods for get_divisors."""
    # class definition

    ## write a separate method for each test:
    ## 1) function call
    ## 2) expected result
    ## compare 1 and 2 by calling method assertEqual -- asserting that actual
    ## and expected results are the same

    def test_divisors_example_1(self):
            """Test get_divisors with 8 and [1,2,3]."""
            actual = divisors.get_divisors(8, [1,2,3])
            # this calls the function from the imported file
            expected = [1,2]
            self.assertEqual(actual, expected)

    def test_divisors_example_2(self):
        """Test get_divisors with 4 and [-2,0,2]."""
        actual = divisors.get_divisors(4, [-2,0,2])
        expected = [-2, 2]
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)
    ## When calling unittest from within IDLE, the parameter exit should be
    ## assigned False: unittest.main(exit=False)
