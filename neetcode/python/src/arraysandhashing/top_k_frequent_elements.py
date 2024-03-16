from typing import List

class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        d = dict()
        # create a dictionary s.t. key = element, value = number of instances of that element 
        for a in nums:
            if a in d:
                d[a] = d[a] + 1
            else:
                d[a] = 1
        # sort dictionary by values
        top = sorted(d, key=lambda x:d[x], reverse=True)
        # take only top k
        return top[0:k] 

'''
The pattern I see in this solution is that there is a lot of counting, 
or keeping track of the counts of elements. A dictionary is a really 
good way of keeping track of that stuff, with the key being the element 
and the value being the count.

From there, needing to return the elements with the largest count 
requires you to constant find the largest count over and over again. If 
done normally, this would be O(n*k); but if we can sort the dictionary by 
values instead of by keys by setting the key parameter in sorted() to the 
values, we can get that classic O(nlogn)

Suppose that the size of nums is n.
Time: n to create the dictionary, nlogn to sort the dictionary by value. I 
think taking a top k slice of the solution would be k, but I don't really 
know python here
    - O(nlogn), and if the slicing counts, then O(nlogn + k)
Space: n for the dictionary, n for the solution array
    - O(n)
'''
