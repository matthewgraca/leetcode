from typing import List

class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
