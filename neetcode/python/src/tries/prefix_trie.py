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
