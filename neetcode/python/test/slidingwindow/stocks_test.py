import unittest
from src.slidingwindow.stocks import Solution

class StocksTest(unittest.TestCase):
    def test_example1(self):
        prices = [7,1,5,3,6,4]
        actual = Solution.maxProfit(prices)
        expected = 5
        msg = "Buy day 2, sell day 5 for a profit of 6-1 = 5"
        self.assertEqual(actual, expected, msg)

    def test_example2(self):
        prices = [7,6,4,3,1]
        actual = Solution.maxProfit(prices)
        expected = 0
        msg = (
            "Monotonically decreasing prices imply "
            "no possible profitable transactions"
        )
        self.assertEqual(actual, expected, msg)

    def test_example3(self):
        prices = [2,1,2,1,0,1,2]
        actual = Solution.maxProfit(prices)
        expected = 2
        msg = (
            "Buy day 5, sell day 7 for a profit of 2-0 = 2"
        )
        self.assertEqual(actual, expected, msg)

