from src.linkedlist.Node import Node

class Solution:
    def __init__(self):
        pass

    def copyRandomList(self, head: Node) -> Node:
        # create map between the original and the copy
        originalCopyMap = {}
        dummy = copy = Node(-1)
        temp = head
        while temp:
            # create copy, initializing the next pointer
            copy.next = Node(temp.val)
            copy = copy.next

            # map original to copy
            originalCopyMap[temp] = copy
            temp = temp.next
        
        # get the random pointers from the original and what they should point to for the copy
        temporg, tempcopy = head, dummy.next
        while temporg:
            tempcopy.random = originalCopyMap[temporg.random] if temporg.random else None
            temporg, tempcopy = temporg.next, tempcopy.next

        return dummy.next
