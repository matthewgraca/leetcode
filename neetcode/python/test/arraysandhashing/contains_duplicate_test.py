import unittest
from src.arraysandhashing import contains_duplicate

class ContainsDuplicateTest(unittest.TestCase):
    def test_example1(self):
        actual = contains_duplicate.contains_duplicate()
        expected = True
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
