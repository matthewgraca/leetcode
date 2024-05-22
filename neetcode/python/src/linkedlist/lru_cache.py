# doubly linked list, but with data as a key-value pair
class Node:
    def __init__(self, key: int, value: int):
        self.key, self.val = key, value
        self.prev, self.next = None, None

# basically a deque (linked list) with a map for O(1) search
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cachemap = {} # {key, Node}
        self.head, self.tail = Node(-1, -1), Node(-1, -1) # two dummy nodes
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        if key not in self.cachemap:
            return -1
        else:   
            # update position in cache
            curr = self.cachemap[key]
            self.remove(curr)
            self.insert(curr)
            return curr.val
        
    def put(self, key: int, value: int) -> None:
        if key in self.cachemap:
            curr = self.cachemap[key]
            self.remove(curr)
            del self.cachemap[key]
            self.capacity += 1
        # if capacity hits 0:
        if not self.capacity:
            temp = self.head.next
            self.remove(temp)
            del self.cachemap[temp.key]
            self.capacity += 1
        
        # add and update cachemap
        temp = Node(key, value)
        self.insert(temp)
        self.cachemap[key] = temp
        self.capacity -= 1
    
    # removes a node from the list
    def remove(self, curr: Node):
        curr.prev.next = curr.next
        curr.next.prev = curr.prev
    
    # places a node at the end of the list (the node before tail)
    def insert(self, curr: Node):
        prev = self.tail.prev
        prev.next = curr
        curr.prev = prev
        curr.next = self.tail
        self.tail.prev = curr
