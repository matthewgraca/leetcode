'''
Attempt 1: Brute force solution, where we check the max of the window at 
every iteration. O(n*k)

Attempt 2: Use a max heap. While pushing into the heap is logk, I completely 
forgot the max heap doesn't pop specific values, only the max. Whoops.

Attempt 3: Using the hints given, I tried out the deque
Does this solution require any sorting? I feel like just using a deque 
still doesn't solve the finding max window issue. 

I need to think a little about the effect of a sliding window on the max.

As I see it there are three scenarios:

1. The max is neither popped or pushed.
If your max is contained within the window and the new left and right are 
not larger than the max, then the max hasn't changed.

2. The max is popped. 
If the max is being popped, you need to find the new max; that is, the new
max is somewhere to the right.

3. The max is pushed. 
If a new value being introduced is larger than the max, that new value 
should be considered the max of the current window.

Ideas: if the max is popped, then run a linear max find. If the array is 
sorted in descending order, this will still be O(n*k). How do we reduce this 
to potentially O(n + k)?

Another hint is this question may use a heap in conjunction with a deque...

Okay just gave up. We have to use a monotonically decreasing deque, containing 
the indices of nums... lolz

Code review:

            while deck and nums[deck[-1]] < nums[r]:
                deck.pop()
            deck.append(r)

This line takes the right value and removes every value in the deque that is
smaller than it. If you think about it, the deque contains all of the "possible"
maxes -- the leftmost is the actual max, but once that is popped, we need to 
find a new max. By popping all of the smaller values than the right value, we're 
saying that none of these values can be the potential new max in the new window, 
because the one we just added is larger than them all.

            if l > deck[0]:
                deck.popleft()

Everything else is kind of straight forward, and why we need to store indices 
instead of values -- if the window passes the indices in the deque, we should 
pop it.

The result is at every iteration, the leftmost deque value is the largest in the
current window.

Another tricky thing is making the window, just having the conditional to not 
move left until the window has reached the right size is neat.

Definitely need to study this silly question.
'''
from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        l,r = 0,0
        sol = list()
        deck = deque()

        # create a monotonically decreasing deque, containing indicies of nums
        while r < len(nums):
            # remove values smaller than the right value from the deque
            while deck and nums[deck[-1]] < nums[r]:
                deck.pop()
            deck.append(r)

            # if left ptr passes the deque, pop it
            if l > deck[0]:
                deck.popleft()

            # once the window is created, begin adding to solution and moving left ptr
            if (r + 1) >= k:
                sol.append(nums[deck[0]])
                l += 1

            r += 1
        return sol
'''
Time: n to traverse the array, n pops/pushes occur
    - O(n)
Space: I believe the deque can be at max k. If we count the solution, it may be 
larger though; n-k -- so added together, n
    - O(k); O(n) is we count the solution space
