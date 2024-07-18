class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = [None] * 26 # alphabet array implementation

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - 97    # idx = [a=0,z=25]
            # search ends with null link; insert here
            if curr.children[idx] is None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        # scan finished. set current node to end of word 
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - 97    # idx = [a=0,z=25]
            # search ends with null link
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]
        # scan finished. if word is in trie, return true else false
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - 97    # idx = [a=0,z=25]
            # search ends with null link
            if curr.children[idx] is None:
                return False
            curr = curr.children[idx]

        # scan finished without terminating; a word in the trie has this prefix
        return True

'''
Optimization with maps instead of alphabet array is of comparable speed
and better space.

the algos are roughly proportional to search key length, n
for space, it's 26*n*w where n = num of keys, w is the average size of the keys
'''

'''
class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {} # char: list of TrieNode

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            # search ends with null link; insert here
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        # scan finished. set current node to end of word 
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            # search ends with null link
            if char not in curr.children:
                return False
            curr = curr.children[char]
        # scan finished. if word is in trie, return true else false
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            # search ends with null link
            if char not in curr.children:
                return False
            curr = curr.children[char]

        # scan finished without terminating; a word in the trie has this prefix
        return True
'''
