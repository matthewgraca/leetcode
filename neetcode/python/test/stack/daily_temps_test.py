import unittest
from src.stack.daily_temps import Solution

class DailyTempsTest(unittest.TestCase):
    def test_example1(self):
        temperatures = [73,74,75,71,69,72,76,73]
        actual = Solution.dailyTemperatures(temperatures)
        expected = [1,1,4,2,1,1,0,0]
        self.assertEqual(actual, expected)

    def test_example2(self):
        temperatures = [30,40,50,60]
        actual = Solution.dailyTemperatures(temperatures)
        expected = [1,1,1,0]
        self.assertEqual(actual, expected)

    def test_example3(self):
        temperatures = [30,60,90]
        actual = Solution.dailyTemperatures(temperatures)
        expected = [1,1,0]
        self.assertEqual(actual, expected)
