from typing import List
class Solution:
    def maxProfit(prices: List[int]) -> int:
        left = 0
        profit = 0
        for right in range(len(prices)):
            # move the left ptr if the right catches a smaller value to buy at
            if prices[right] < prices[left]:
                left = right
            profit = max(profit,prices[right]-prices[left])
        return profit
