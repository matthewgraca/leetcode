from typing import List

class Solution:
    def __init__(self):
        pass

    '''
    This is a direct copy of floyd's algorithm, found here:

    https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_tortoise_and_hare
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # floyd's cycle detection 1: find cycle using tortise and hare
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]       # slow = slow.next
            fast = nums[nums[fast]] # fast = fast.next.next

        # floyd's cycle detection 2: find beginning of a cycle
        # slow and fast will meet at the first repitition 
        slow = 0
        while slow != fast:
            slow = nums[slow] 
            fast = nums[fast] 

        return slow
'''
So this problem is actual verifiable bullshit. here's the rub:
    1. this is a secret linked list problem
        - indices are the nodes (index := node)
        - values are the next pointer (value := node the current node is pointing to)
            - e.g. a[0] = 1 means "node 0 -> node 1"
        - there are no values pointing "outside" the list; that is, no null pointer;
            a cycle is guaranteed in this problem, due to its definition
    2. this is a cycle detection problem
        - e.g. [1,3,4,2,1] means:
            - 0 -> 1 -> 3 -> 2 -> 4 -> 1
            - here, the cycle is 1 -> 3 -> 2 -> 4 -> 1
    3. this is a "first repitition" cycle problem (find the where the cycle begins)
        
    As for why we start slow at head.next and fast at head.next.next:
        - From what I can tell, this preserves some invariants; the distance between 
            the two pointers "v" being divisible by some period "lambda". When 
            the second tortise is deployed, the distance between the hare and the new 
            tortise will be "2v". if they move at the same speed one step 
            at a time along with the hare, the distance will stay "2v" until they reach 
            "0", a multiple of "lambda", which is the beginning of the cycle. 
        - seems like complicated group/graph theory crap that shouldn't be asked in an 
            interview LMAO
        - time complexity is O(lambda + mu). lambda is the period (num of iterations 
            of the first loop) and mu is the number of periods lambda needed to get 
            to the multiple of 2v s.t. 2v = 0. lol
        - also, i figured out why the topics include fing bit manipulation... 
            there's another algo called brent's that uses powers of two to guide 
            the tortise and hare positions... like wtf...??
'''
