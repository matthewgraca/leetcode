import unittest
from src.arraysandhashing.contains_duplicate import Solution 

class ContainsDuplicateTest(unittest.TestCase):
    def test_example1(self):
        arg = [1,2,3,1]
        actual = Solution.containsDuplicate(arg)
        expected = True
        self.assertEqual(actual, expected)

    def test_example2(self):
        arg = [1,2,3,4]
        actual = Solution.containsDuplicate(arg)
        expected = False 
        self.assertEqual(actual, expected)

    def test_example3(self):
        arg = [1,1,1,3,3,4,3,2,4,2]
        actual = Solution.containsDuplicate(arg)
        expected = True 
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
