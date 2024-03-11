from typing import List

class Solution:
    def containsDuplicate(nums: List[int]) -> bool:
        a = set(nums)
        return len(a) != len(nums)

'''
Basically, whenever I see the word 'duplicate', my immediate reaction is to 
use the data structure that disallows dupes (set). Just convert the input into 
a set, and it will automatically get rid of all dupes; so if the length of the 
set is less than the length of nums, there must be dupes; else they are the 
same, and there were no dupes.

Suppose n is the size of the list of nums
Time: n for initializing the set, 1 for comparing the list and set lengths
    - O(n)
Space: n for initializing the set
    - O(n)
'''
