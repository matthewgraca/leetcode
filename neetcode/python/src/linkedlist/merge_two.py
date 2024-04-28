from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    # version 2b: in-place merge, recursive
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # base case 1: both lists empty
        if not list1 and not list2:
            return None
        # base case 2: list1 empty
        if not list1:
            return list2
        # base case 3: list2 empty
        if not list2:
            return list1

        # recursive step:
        # generates a path of nodes with values in increasing order
        # then head is connected to the previous largest node --
        # continues until linked list contains all values in increasing order
        head = None
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)
        return head

    # version 2a: in-place merge, iterative
    def mergeTwoLists2a(self, list1: ListNode, list2: ListNode) -> ListNode:
        head = merger = ListNode(0) # dummy node so we have a head to attach nodes to

        # merger pointer picks nodes from the two lists
        while list1 and list2:
            if list1.val < list2.val:
                merger.next = list1 
                list1 = list1.next
            else:
                merger.next = list2 
                list2 = list2.next
            merger = merger.next

        # if a list remains, pick nodes from that list
        # if no list remains, it's okay, it'll point to null
        merger.next = list1 if list1 else list2

        # pop dummy node
        return head.next

    # version 1: auxiliary list while iterating through both lists 
    def mergeTwoLists1(self, list1: ListNode, list2: ListNode) -> ListNode:
        temp1, temp2 = list1, list2
        res = None

        # initialize the head of the result
        if temp1 and temp2:
            if temp1.val < temp2.val:
                res = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                res = ListNode(temp2.val)
                temp2 = temp2.next
        # if any list is empty, return the non-empty list (or no list)
        elif temp1 and not temp2:
            return temp1 
        elif temp2 and not temp1:
            return temp2
        else:
            return None

        # comb through rest of the two lists
        tempres = res
        while temp1 or temp2:
            # if list 2 is empty, take from list1
            if temp1 and not temp2:
                tempres.next = temp1
                return res
            # if list 1 is empty, take from list2
            elif temp2 and not temp1:
                tempres.next = temp2
                return res
            # otherwise, take from list with smaller value
            else:
                if temp1.val < temp2.val:
                    tempres.next = ListNode(temp1.val)
                    tempres = tempres.next
                    temp1 = temp1.next
                else:
                    tempres.next = ListNode(temp2.val)
                    tempres = tempres.next
                    temp2 = temp2.next
        return res 

'''
recursion is the death of me. in this scenario we're building a path 
of nodes in increasing order. then, when the base case is hit, we 
traverse the path of nodes in decreasing order. when we recurse, we 
update the head to stitch together the nodes in that order.

I don't know how the function trace looks so im cooked 
'''
