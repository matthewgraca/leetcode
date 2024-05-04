# double linked list
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache:
    # initialize cache with positive size capacity
    # capacity = [1,3000]
    # head = lru, tail = mru
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyNodeMap = {}
        # head = left bound, tail = right bound. all nodes belong in between
        self.head, self.tail = Node(-1,-1), Node(-1, -1) 
        self.head.next, self.tail.prev = self.tail, self.head

    # return value of key. If key doesn't exist, return -1
    # get == used, so update the node as mru
    # key = [0, 10000]
    # goal: avg O(1) time
    def get(self, key: int) -> int:
        # update to mru
        if key in self.keyNodeMap:
            self.remove(self.keyNodeMap[key])
            self.insert(self.keyNodeMap[key])
            return self.keyNodeMap[key].val
        return -1

    # 1. update the value of key if it exists.
    # 2. otherwise, add the key-value pair to the cache
    # 3. if the number of keys exceeds capacity:
    #   - evict the least recently used key
    # key = [1,10000], value = [0,100000]
    # goal: avg O(1) time
    def put(self, key: int, value: int) -> None:
        if key in self.keyNodeMap:
            self.remove(self.keyNodeMap[key])
        self.keyNodeMap[key] = Node(key, value)
        self.insert(self.keyNodeMap[key])

        if len(self.keyNodeMap) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.keyNodeMap[lru.key]

    # removes a given node
    def remove(self, curr: Node) -> None:
        before, after = curr.prev, curr.next
        before.next, after.prev = after, before 

    # adds a given node to mru (before tail)
    def insert(self, node: Node) -> None:
        # attach node before tail and given node together
        before = self.tail.prev
        before.next, node.prev = node, before
        # attach given node and tail together 
        node.next, self.tail.prev = self.tail, node
'''
basically got screwed by implementation details. the idea of having a 
tail and head pointer is not new, but using the tail and head ptrs 
as actual boundaries, with their own dummy nodes? furthermore, the
every node being placed IN BETWEEN the head/tail ptrs?
never seen that pattern before.
'''
