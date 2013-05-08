import unittest
import count_lowercase_vowels

class TestCount_Vowels (unittest.TestCase):
    """ Unittest test methods for count_lowercase_vowels"""

    def test_count_vowels_example1(self):
        """ Test count_lowercase_vowels with a long string containing multiple
            lowercase vowels and at least one uppercase vowel."""
        actual = count_lowercase_vowels.count_lowercase_vowels('Happy Anniversary')
        expected = 4
        self.assertEqual(actual, expected)

    def test_count_vowels_example2(self):
        "Test count_lowercase_vowels on a string containing no vowels."""
        actual = count_lowercase_vowels.count_lowercase_vowels('xyz')
        expected = 0
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main(exit=False)
