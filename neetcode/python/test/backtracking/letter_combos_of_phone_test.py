import unittest
from src.backtracking.letter_combos_of_phone import Solution

class LetterCombosOfPhoneTest(unittest.TestCase):
    def test_example1(self):
        digits = "23"
        actual = Solution().letterCombinations(digits)
        expected = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example2(self):
        digits = ""
        actual = Solution().letterCombinations(digits)
        expected = []
        self.assertEqual(sorted(actual), sorted(expected))

    def test_example3(self):
        digits = "2"
        actual = Solution().letterCombinations(digits)
        expected = ["a","b","c"]
        self.assertEqual(sorted(actual), sorted(expected))
