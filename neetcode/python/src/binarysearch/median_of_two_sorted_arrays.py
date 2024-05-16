from typing import List

class Solution:
    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # for convenience, we'll have the A list be smaller than the B list
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # attempt to create the global lower partition
        # arbitarily start with the smaller length array 
        globalMidIdx = (len(A) + len(B)) // 2
        l, r = 0, len(A)-1
        while True:
            # set up indices for navigating A and B
            # we take half of A's values, and the rest of the values from B
            # to create our global lower partition
            Aidx = (l + r) // 2
            # gmi - Aidx - 1 = index of median, removing A's contribution
            # index of median - 1 = index of the end of the lower partition
            Bidx = (globalMidIdx-Aidx-1) - 1

            # get the boundaries of both lists
            # it is possible the index is lower than 0; in that case, 
            # make it a lower bound of -infinity so we end up always taking 
            # from the other list.
            # on the other hand, if the index is larger than the array's len,
            # make it an upper bound of +infinity so we take from the other list.

            # the idea is that Amax and Bmax will be the largest lower partition values,
            # while ABoundary and BBoundary will the the smallest upper partition values.
            Amax = A[Aidx] if Aidx >= 0 else float('-inf')
            ABoundary = A[Aidx+1] if Aidx < (len(A)-1) else float('inf')

            Bmax = B[Bidx] if Bidx >= 0 else float('-inf')
            BBoundary = B[Bidx+1] if Bidx < (len(B)-1) else float('inf')

            # now, check if these two partitions make a valid global lower
            # parition; that is:
            # the lower partition's largest values (Amax, Bmax) are not larger 
            # than the upper partition's smallest values (ABoundary, BBoundary).
            if Amax <= BBoundary and Bmax <= ABoundary:
                # median case
                if (len(A) + len(B)) % 2 == 0:
                    # Amax and BMax are in the lower partition;
                    # ABoundary and BBoundary are in the upper partition;
                    # So the largest lower partition value and the smallest upper 
                    # partition value will make up the median.
                    return (max(Amax, Bmax) + min(ABoundary, BBoundary)) / 2
                else:
                    # note that Amax and Bmax are strictly lower partition.
                    # thus, the median will be the one value right after it;
                    # the minimum of the two boundaries is the middle, the other
                    # value is then a part of the upper partition
                    return min(ABoundary, BBoundary)
            # B has a value smaller than the largest current A value; 
            # get rid of half of A and take more from B 
            elif Amax > BBoundary:
                r = Aidx-1
            # A has a value smaller than the largest current B value;
            # get rid of half of B and take more from A
            else:
                l = Aidx+1
