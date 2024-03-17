from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = 1
        suffix = 1
        ans = [0]*n

        # scan forward. first pass generates prefix-only answers
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        # scan backward. second pass finds product of prefix answers with suffix
        for i in range(n-1, -1, -1):
            ans[i] *= suffix 
            suffix *= nums[i]
            
        return ans
'''
This one was silly I had to go back to remember what I did in Java.

Honestly, I'm not exactly sure on what pattern I needed to pick up here; 
seemed more like an exercise in dynamic programming and two pointers.

I guess the lesson here is that whenever you're in a situation that you can 
tell requires you to make the same calculations over and over again (with 
very slight differences), then see if you can build the answers in some 
fashion. This one was tricky because in order to build the answer, you had 
to make two passes; forward and backward. I suppose keep that in the back 
pocket for dynamic programming problems with arrays.

Time: n for the forward pass, n for the backward pass
    - O(n)
Space: y'know, I just learned that there is such a thing as "output space" 
that is sometimes not counted towards space complexity analysis. At the end 
of the day, this array needs to be created, and that requires space. Any 
deeper distinction is academic from what I can tell. So, n for the 
solution array.
    - O(n)
'''
