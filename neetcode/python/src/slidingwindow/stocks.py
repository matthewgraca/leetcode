from typing import List
class Solution:
    def maxProfit(prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            # move the left ptr if the right catches a smaller value to buy at
            if prices[right] < prices[left]:
                left = right
            profit = max(profit,prices[right]-prices[left])
            right += 1
        return profit
