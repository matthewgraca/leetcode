from typing import List

'''
"longest consecutive" -- e.g. [1,4,3,2] -> [1,2,3,4] -> 4
- duplicates don't count -- e.g. [0,0,0,0,1] -> [0,1] -> 2

The problem specifies that the array is unsorted, and the algorithm 
should be O(n) time -- so that eliminates the simplest solution, aka sorting.

Here's a preliminary idea: for every element in nums, store that element into 
a set. Then, we check the next element. If that element is +/- 1 of an element 
that already exists in the set, then it gets added to the sequence.

So using the first example, "1" gets added to the set. "4" is checked, but is 
not +/- 1 from an existing element (1). We obviously don't want to discard this 
because we have the foresight of knowing that "4" is included in the solution. 
So, is there a way of keeping the "4" so that it may, later on, be appended to 
the solution?

I really want to use a set. Just seeing "no duplicates" and "searching" just 
screams this data structure... so I intuitively think this is something that 
the solution may require.

I think we can try 2 scans of the input. So for 
[100,4,200,1,3,2], we'll scan:
    - scan 1: 100, 4, 200, 1, 3, 2 are added to the set
    - scan 2: 
        - check if 99/101 are in the set. not found, remove 100 from set.
        - check if 3/5 are in the set. 3 is found, so check next element.
        - check if 199/201 are in the set. not found remove 200 from set.
        - check if 0/2 are in the set. 2 is found, check the next element.
        - check if 2/4 are in the set. 2 and 4 are found, check next element.
        etc.

The issue here is that if there are two disjointed sequences e.g. [0,1,5,6,7,8,9],
then both of them will be included in the set. I need to find a way to create 
multiple sets of solutions, taking only the largest one.

---

Okay, here's the next idea. We attempt to create the solution on the first pass 
forward -- everything that doesn't fit gets its own set: e.g. for [100,4,200,1,3,2]
    - first pass: for each num, check if it's +/- 1 of an existing set element; else
        make a new set of it. This should be the result after the first pass:
        - 100
        - 4,3,2
        - 200
        - 1,2
So from here, we can try to combine sets that generate a sequence. It's my 
intuition that if two sets have an element that's the same, they should be 
combinable. So the question is, how to combine two sets that share an element?

Okay, let's review set operations: AND gets us intersecting elements, so let's 
use that as the basis for combining any combinable sets.

So, the pseudocode here after the first pass:
    - for every set, check if there is an intersection with every other set.
    If there is, union the two sets. Here should be the result:
        - 100
        - 4,3,2,1
        - 200

I think from here, we just return the length of the largest set. 

---

One issue has come up, where merging say:
    - 3,4
    - 1,2
    - 2,3
merges 1,2,3; but doesn't merge 3,4 since it "missed the boat"

Do we need to union, remove the unioned sets, then restart the loop?

---
ok, rethinking this: if a set has one element, we can remove it...
but that doesn't solve the union issue
'''
class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        numSet = set(nums)
        maxCount = 0
        for num in nums:
            count = 1
            if num in numSet:
                numSet.remove(num)

            # find and count all left values
            left = num - 1
            while left in numSet:
                numSet.remove(left)
                count += 1
                left -= 1

            # find and count all right values
            right = num + 1
            while right in numSet:
                numSet.remove(right)
                count += 1
                right += 1

            # pick only the largest set
            maxCount = max(maxCount, count)
        return maxCount

'''
At the end of the day, I just copied the solution I did a year ago. What's the 
pattern here? I don't know. I got baited into attempting to use special set 
operations, when in reality I just should've used the search function more. 
Here, we just need to search for all the adjacents of each value. The idea here 
that I missed is that once we found the value, we can remove it from the set, 
since any other value that would use that "found value" will, by definition, be 
a part of the sequence we are already building/counting.

Time: n to make the set, n to search
    - O(n)
Space: n to make the set
    - O(n)
'''
