from typing import List

class Solution:
    def __init__(self):
        pass

    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's cycle detection 1: find cycle using tortise and hare
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]       # slow = slow.next
            fast = nums[nums[fast]] # fast = fast.next.next

        # floyd's cycle detection 2: find beginning of a cycle
        # slow and fast will meet at the first repitition 
        slow = 0
        while slow != fast:
            slow = nums[slow] 
            fast = nums[fast] 

        return slow
