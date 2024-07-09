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
