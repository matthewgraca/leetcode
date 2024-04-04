from typing import List
import heapq

class Solution:
    def topKFrequent1(nums: List[int], k: int) -> List[int]:
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

    def topKFrequent(nums: List[int], k: int) -> List[int]:
        freq = dict()
        h = []
        # freq map of elements in nums
        for el in nums:
            freq[el] = 1 + freq.get(el,0)
        # put map into heap as (-1 * frequency,element); to convert into max heap
        for el in freq:
            heapq.heappush(h,(-1 * freq[el], el))
        # pop top k values by frequency, appending the element to top[]
        top = []
        for i in range(k):
            top.append(heapq.heappop(h)[1])
        return top
