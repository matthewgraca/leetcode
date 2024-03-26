import unittest
from src.slidingwindow.permutation_in_string import Solution

class PermutationInStringTest(unittest.TestCase):
    def test_example1(self):
        s1 = "ab"
        s2 = "eidbaooo"
        actual = Solution().checkInclusion(s1,s2)
        expected = True
        msg = (
            f"\"{s1}\" is contained in \"{s2}\" as \"ba\""
        )
        self.assertEqual(actual,expected,msg)

    def test_example2(self):
        s1 = "ab"
        s2 = "eidboaoo"
        actual = Solution().checkInclusion(s1,s2)
        expected = False 
        self.assertEqual(actual,expected)

    def test_example3(self):
        s1 = "horse"
        s2 = "ros"
        actual = Solution().checkInclusion(s1,s2)
        expected = False 
        self.assertEqual(actual,expected)
