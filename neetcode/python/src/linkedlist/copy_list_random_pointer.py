from src.linkedlist.Node import Node

class Solution:
    def __init__(self):
        pass

    def copyRandomList(self, head: Node) -> Node:
        # return null for empty list
        if head == None:
            return None

        # first pass: make a basic copy of the list, and save them in a dict
        # dict = {original node, copy node}
        copy = dict()
        temporg = head
        tempcopy = Node(0)
        while temporg:
            # put copy in dictionary 
            temp = Node(temporg.val)
            copy[temporg] = temp

            # copy original next nodes
            tempcopy.next = temp
            tempcopy = tempcopy.next

            temporg = temporg.next

        # using the dict, the original node random pointer gives the key to 
        # what the copy node should point to for it's own list
        temporg = head
        while temporg:
            if temporg.random == None:
                copy[temporg].random = None
            else:
                copy[temporg].random = copy[temporg.random]
            temporg = temporg.next
        return copy[head] 
'''
freaky, this problem is cute. managed to solve it at great cost

o(n) for copy, o(n) for search and random ptr attachment
o(n) space for hm
'''
