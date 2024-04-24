from typing import List

class Solution:
    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # global partition indices
        totalLen = len(nums1) + len(nums2)
        totalMid = totalLen // 2

        # A = smaller nums length, B = larger nums length
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # create a lower partition from n1 and n2
        lower, upper = 0, len(A)-1
        while True:
            # draw from nums1 and nums2 to create the lower partition
            # cut the smaller array in half, and the remaining from the larger
            Aidx = (lower + upper) // 2
            Bidx = totalMid - (Aidx+1) - 1

            # draw partition boundaries
            Amax = A[Aidx] if Aidx >= 0 else float("-inf")
            ABoundary = A[Aidx+1] if Aidx < (len(A)-1) else float("inf")

            Bmax = B[Bidx] if Bidx >= 0 else float("-inf")
            BBoundary = B[Bidx+1] if Bidx < (len(B)-1) else float("inf")

            # check if A and B combine to make a valid partition
            if Amax <= BBoundary and Bmax <= ABoundary:
                # median case
                if totalLen % 2 == 1:
                    # value after the lower partition
                    return min(ABoundary, BBoundary)
                else:
                    # largest lower partition value and smallest upper partition value
                    return (max(Amax, Bmax) + min(ABoundary, BBoundary)) / 2
            # A has a value too big; remove one and take from B
            elif Amax > BBoundary:
                upper = Aidx - 1
            # B has a value too big; remove one and take from A
            else:
                lower = Aidx + 1
'''
this problem is actually fucking terrrible LMAOOO
ppl with (n+m)log(m+n) and (m+2) solutions are literally faster LMAOOO
straight up garbage.

allegedly, log(m+n)? i honestly can't tell. it cuts the problem in half, but
kind of just goes iteratively from that point on by the smallest, e.g. 
1. cuts problem in half
2. moves iteratively by smallest, say m
boils down to m?? idk
'''
