from src.linkedlist.ListNode import ListNode

class Solution:
    def __init__(self):
        pass

    def mergeTwoListsRecursive(self, list1: ListNode, list2: ListNode) -> ListNode:
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
            head.next = self.mergeTwoListsRecursive(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwoListsRecursive(list1, list2.next)
        return head

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = temp = ListNode(float(-inf))
        # check through list1 and list2 values
        while list1 and list2:
            # move temp pointer to list with the smaller value
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        
        # any list with remaining values will bee pointed to
        if list1:
            temp.next = list1
        else:
            temp.next = list2
        
        # pop the dummy value
        return dummy.next
