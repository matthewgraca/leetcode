import heapq

class MedianFinder:
    def __init__(self):
        # max heap of the lower half of the data stream
        self.lower = []
        # min heap of the upper half of the data stream
        self.upper = []

    def addNum(self, num: int) -> None:
        # put the num in either the lower or upper heap
        if self.upper and self.upper[0] < num:
            heapq.heappush(self.upper, num)
        else:
            heapq.heappush(self.lower, -num)

        # rebalance the heaps so that they are only different in size by 1
        # upper too small: take from lower
        if len(self.upper) + 1 < len(self.lower):
            heapq.heappush(self.upper, -heapq.heappop(self.lower))
        # lower too smaller; take from upper
        if len(self.lower) + 1 < len(self.upper):
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

    def findMedian(self) -> float:
        median = 0.0
        if len(self.lower) == len(self.upper):
            lo, hi = -self.lower[0], self.upper[0]
            median = (lo + hi) / 2.0
        elif len(self.lower) < len(self.upper):
            median = self.upper[0]
        else:
            median = -self.lower[0]

        return median
'''
imagine the data stream is given and sorted.
you maintain two heaps:
    -minheap of the upper half
    -maxheap of the lower half
this way, the top of the minheap and the top of the maxheap
gives you the median of the sorted list

if the heaps are the same size, do the average calc.
if the heaps are different sizes, you take from the one that's +1 larger

the question is, how should the heaps be populated from a data stream?
If we just populate the two heaps for each value in the data stream, 
we'll just end up getting the minimum and maximum value of the stream.
We need a way to give the value to one stream or the other;
    -is it literally just tossing it from one to the other, sequentially?
        -nope
    -ideally we want the lower half of the data stream in the max heap and 
        upper half of the stream in the min heap
        -the issue is that one heap may pick up a value that should belong
            to the other heap, if we distribute the values sequentially
            -my current idea is that for each value in the data stream, 
            we check both heaps. if the minheap top is smaller than the 
            max heap top, then we need to swap those values
    - plan: if the value belongs in the upper array (by checking the top),
        then we just push it into the upper heap. otherwise, push it into
        the lower heap
        - afterwards, we rebalance the heaps so that they are, at most, 
        different in size by only 1. that way we can get O(1) median.
Time:
    addNum()
        -suppose n is the size of the data stream at any point in time
        -2logn to add to both heaps
        -total: O(logn)
    findMedian()
        -O(1)
'''
