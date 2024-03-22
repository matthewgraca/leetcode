from typing import List

'''
The idea here is that we want to use two pointers, with the right pointer 
that scans the array for a value smaller than the left pointer. The reason 
is because if the left is larger, the stock will have negative profit, but 
if the right is larger, then there are potentially larger profits.

Once a the right pointer finds the smaller value, replace the left with 
the right pointer and have the right pointer continue to search for 
a smaller pointer.

Meanwhile, the entire time, calculate the largest profits you can get.
'''
class Solution:
    def maxProfit(prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        i,j = 0,1
        profit = 0
        while j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j = i+1
            else:
                profit = max(profit,prices[j]-prices[i])
                j += 1
        return profit
'''
Time: n to scan the array
    - O(n)
Space: no extra space used
    - O(1)
'''
