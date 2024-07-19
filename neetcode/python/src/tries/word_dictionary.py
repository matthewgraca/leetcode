class TrieNode:
    def __init__(self):
        self.endOfWord = False
        self.children = {} 

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)

    def dfs(self, i: int, word: str, curr: TrieNode) -> bool:
        # scan complete; check if the word is in the trie
        if i == len(word):
            return curr.endOfWord

        # if char is wildcard, search through all children
        char = word[i]
        if char == '.':
            # find a child who search hits
            for child in curr.children.values():
                if self.dfs(i + 1, word, child):
                    return True
            # if no child succeeds, search missed 
            return False

        # char in trie; continue search
        if char in curr.children:
            return self.dfs(i + 1, word, curr.children[char])

        # char not in trie; search miss
        return False
