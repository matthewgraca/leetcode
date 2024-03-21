from typing import List

'''
The goal to get all the triplets that sum to 0. Each element in the triplet 
must be unique; i.e. for the indices i,j,k, i!=j, i!=k, and j!=k

Borrowing from the last solution, we can build a solution by sorting the 
elements in the array, then using two pointers to contruct the solution.

we fix one pointer i. Then send j and k to search for a valid sum. Then 
afterwards, increment i.

---

Now, our biggest issue here is dealing with duplicates. Searching the solutions 
for duplicates will end up costing n^2 time, so we need a method of avoiding 
the duplicates.

If the next nums[i] is the same as the previous nums[i], then duplicates seem 
to be able to occur. that is, if nums[i] == nums[left], should we simply 
increment i?
'''
class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        n = len(nums)
        target = 0
        solution = []

        for i in range(n-2):
            left = i+1
            right = n-1

            # avoid evaluating duplicate nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                val1 = nums[i]
                val2 = nums[left]
                val3 = nums[right]
                triple = val1 + val2 + val3

                if triple < target:
                    left += 1
                elif triple > target:
                    right -= 1
                else:
                    solution.append([val1, val2, val3])
                    prevLeft = left
                    prevRight = right
                    # avoid evaluating duplicate nums[left]
                    while (left < right and nums[left] == nums[prevLeft]):
                        left += 1
                    # avoid evaluating duplicate nums[right]
                    while (left < right and nums[right] == nums[prevRight]):
                        right -= 1
        return solution

'''
Had to cheat for this one, the whole non-duplicates thing was pretty annoying. 
Basically just had to keep shifting i, left, and right AFTER evaluating them 
to make sure that we don't evaluate them again. I got mixed up trying to 
prevent evaluating before I evaluated the actual nums, and got stuck.

Time: nlogn for the sort, n^2 for the searching (n(n-1)/2 in this case)
    - O(n^2)
Space: I think n if every element makes up a valid distinct triple
    - O(n)
'''
